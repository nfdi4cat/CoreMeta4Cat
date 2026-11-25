#!/usr/bin/env python3
"""Convert a laboratory Excel workbook into a CoreMeta4Cat CatalysisDataset record.

Written for the JLCAT03 example (examples/excel_JLCAT03/). The workbook-specific part is not in
this code: it is in crosswalk.yaml next to this script (one entry per spreadsheet column or row,
with target path, conversion, basis and rationale) and in supplement.yaml (values that are not in
the workbook). Method and file formats: ../PARSER_BUILD_NOTES.md.

Steps:
  1. read      every non-empty cell, following the sheet layouts declared in the crosswalk
  2. map       each cell to a path in the record and convert it (text, enum, quantity, range, ...)
  3. assemble  the nested record; objects are created on first use and get minted ids
  4. account   stop if any non-empty cell is not covered by the crosswalk
  5. check     header terms against the target slots; unfilled required and recommended slots
               (uses the schema of the CoreMeta4Cat checkout this script is in, or --schema)
  6. write     the record (YAML), its provenance (source_documentation.yaml) and a parse report

Validation and RDF conversion are left to the standard LinkML tools (linkml-validate,
linkml-convert); see the build notes.

Usage (from the repository root):
  uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py
  uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py --no-placeholders --out <file.yaml>
"""
from __future__ import annotations

import argparse
import copy
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import openpyxl
import yaml
from openpyxl.utils import get_column_letter


HERE = Path(__file__).resolve().parent
SCRIPT_REF = f"{HERE.name}/{Path(__file__).name}"       # as named in generated files


class ParseError(Exception):
    pass


def default_schema():
    """coremeta4cat.yaml of the CoreMeta4Cat checkout this script lives in, if any."""
    for d in HERE.parents:
        p = d / "src" / "coremeta4cat" / "schema" / "coremeta4cat.yaml"
        if p.exists():
            return p
    return None


# ----------------------------------------------------------------------------- small helpers

def norm(v):
    """Collapse whitespace in strings; blank strings become None."""
    if isinstance(v, str):
        v = " ".join(v.split())
        return v or None
    return v


def slug(v):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(norm(v))).strip("-")


def to_number(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return v
    if isinstance(v, str):
        s = v.strip().replace(",", ".")
        if re.fullmatch(r"-?\d+", s):
            return int(s)
        if re.fullmatch(r"-?\d*\.\d+", s):
            return float(s)
    return None


RANGE = re.compile(r"^\s*(-?\d+(?:[.,]\d+)?)\s*(?:-|–|to)\s*(-?\d+(?:[.,]\d+)?)\s*$")
CURIE_IN_TEXT = re.compile(r"\b([A-Za-z][A-Za-z0-9.]*):([A-Za-z0-9_]+)\b")
ALLOTROPE_UNDERSCORE = re.compile(r"\b(AF[A-Z])_(\d{7})\b")
TEMPLATE = re.compile(r"\{(\w+)(?::([A-Za-z0-9]+))?\}")
PATH_PART = re.compile(r"([A-Za-z_]\w*)(?:\[([^\]]*)\])?")
DESIGNATORS = ("activity_designator", "plan_designator", "reactor_designator")


def terms_in(text):
    """CURIEs written in a header, e.g. 'voc4cat:0008106', 'AFR_0002018' -> 'AFR:0002018'."""
    if not text:
        return []
    found = [f"{p}:{l}" for p, l in CURIE_IN_TEXT.findall(text)]
    found += [f"{p}:{n}" for p, n in ALLOTROPE_UNDERSCORE.findall(text)]
    return found


# ----------------------------------------------------------------------------- 1. read

@dataclass
class Cell:
    sheet: str
    coord: str
    label: str | None      # column header (table) or row label (key-value)
    term: str | None       # term column (key-value sheets)
    unit: str | None       # unit row (table sheets)
    value: object
    status: list = field(default_factory=list)   # filled while mapping, for the inventory


@dataclass
class Record:
    sheet: str
    key: str
    cells: dict            # column letter (table) or row number as str (key-value) -> Cell
    where: str


@dataclass
class SheetData:
    name: str
    spec: dict
    records: list
    frame: list            # (coord, text, kind): header/unit/label/term cells
    stray: list            # non-empty cells outside the declared layout
    headers: dict          # table: column letter -> header text; key-value: row -> Cell


def read_table(ws, name, spec):
    hr, ur, first = spec["header_row"], spec.get("unit_row"), spec["first_data_row"]
    headers, frame, stray, records = {}, [], [], []
    for c in range(1, ws.max_column + 1):
        col = get_column_letter(c)
        h = norm(ws[f"{col}{hr}"].value)
        if h is not None:
            headers[col] = h
            frame.append((f"{col}{hr}", h, "header"))
        u = norm(ws[f"{col}{ur}"].value) if ur else None
        if u is not None:
            frame.append((f"{col}{ur}", u, "unit row"))
    for r in range(1, ws.max_row + 1):
        if r in (hr, ur):
            continue
        cells = {}
        for c in range(1, ws.max_column + 1):
            col = get_column_letter(c)
            v = norm(ws[f"{col}{r}"].value)
            if v is None:
                continue
            if r < first or col not in headers:
                stray.append(f"{col}{r}")
                continue
            unit = norm(ws[f"{col}{ur}"].value) if ur else None
            cells[col] = Cell(name, f"{col}{r}", headers[col], None, unit, v)
        if not cells:
            continue
        key = cells.get(spec["key_column"])
        if key is None:
            raise ParseError(f"{name} row {r}: key column {spec['key_column']} is empty")
        records.append(Record(name, str(key.value), cells, f"row {r}"))
    return SheetData(name, spec, records, frame, stray, headers)


def read_key_value(ws, name, spec):
    lc, tc, vc = spec["label_column"], spec["term_column"], spec["value_column"]
    rows, frame, stray = {}, [], []
    for r in range(1, ws.max_row + 1):
        for c in range(1, ws.max_column + 1):
            col = get_column_letter(c)
            if col not in (lc, tc, vc) and norm(ws[f"{col}{r}"].value) is not None:
                stray.append(f"{col}{r}")
        label, term, value = (norm(ws[f"{x}{r}"].value) for x in (lc, tc, vc))
        if label is None and term is None and value is None:
            continue
        rows[r] = Cell(name, f"{vc}{r}", label, term, None, value)
        if label is not None:
            frame.append((f"{lc}{r}", label, "label"))
        if term is not None:
            frame.append((f"{tc}{r}", term, "term"))
    key = rows.get(spec["key_row"])
    if key is None or key.value is None:
        raise ParseError(f"{name}: key row {spec['key_row']} has no value")
    record = Record(name, str(key.value), {str(r): c for r, c in rows.items()}, "sheet")
    return SheetData(name, spec, [record], frame, stray, rows)


READERS = {"table": read_table, "key_value": read_key_value}


# ----------------------------------------------------------------------------- 2./3. map and assemble

def render(template, rec):
    """Fill {key}, {slug:REF}, {raw:REF} (REF = column letter or row number of the same record)."""
    def sub(m):
        fn, ref = m.group(1), m.group(2)
        if fn == "key":
            return slug(rec.key)
        cell = rec.cells.get(ref)
        if cell is None or cell.value is None:
            raise ParseError(f"template {template!r}: cell {ref} of {rec.sheet} {rec.where} is empty")
        if fn == "slug":
            return slug(cell.value)
        if fn == "raw":
            return str(norm(cell.value))
        raise ParseError(f"template {template!r}: unknown function {fn!r}")
    return TEMPLATE.sub(sub, template)


def parse_path(path):
    is_root = path.startswith("^")
    parts = (path[1:] if is_root else path).split(".")
    segs = []
    for part in parts:
        m = PATH_PART.fullmatch(part)
        if not m:
            raise ParseError(f"bad path segment {part!r} in {path!r}")
        segs.append((m.group(1), m.group(2), part))   # name, key (None | "" | text), as written
    return is_root, segs


@dataclass
class Prov:
    container: dict        # object the value was written to
    slot: str
    value: object
    source: str
    basis: str
    note: str
    cell: Cell | None = None
    placeholder: bool = False


class Builder:
    def __init__(self, prefix):
        self.prefix = prefix
        self.root = {}
        self.keyed = {}       # (id(list), rendered key) -> item
        self.parent = {}      # id(obj) -> (parent obj, slot)
        self.minted = []      # (template path, id)
        self.prov = []

    def _new(self, tpl, rec, ids):
        obj = {}
        if tpl in ids:
            obj["id"] = self.prefix + render(ids[tpl], rec)
            self.minted.append((tpl, obj["id"]))
        return obj

    def child(self, node, name, key, tpl, rec, ids):
        if key is None:
            if name not in node:
                node[name] = self._new(tpl, rec, ids)
                self.parent[id(node[name])] = (node, name)
            if not isinstance(node[name], dict):
                raise ParseError(f"{tpl}: {name} holds a value, not an object")
            return node[name]
        if key == "":
            raise ParseError(f"{tpl}: '[]' (append) is only allowed at the end of a path")
        lst = node.setdefault(name, [])
        k = (id(lst), render(key, rec) if rec else key)
        if k not in self.keyed:
            obj = self._new(tpl, rec, ids)
            lst.append(obj)
            self.keyed[k] = obj
            self.parent[id(obj)] = (node, name)
        return self.keyed[k]

    def put(self, base, path, value, rec, ids):
        """Write value at path (relative to base, or to the root with a leading ^).
        Returns (container, slot) for the provenance record."""
        value = copy.deepcopy(value)
        is_root, segs = parse_path(path)
        node = self.root if is_root else base
        prefix = "^" if is_root else ""
        for i, (name, key, _) in enumerate(segs[:-1]):
            tpl = prefix + ".".join(s[2] for s in segs[: i + 1])
            node = self.child(node, name, key, tpl, rec, ids)
        name, key, _ = segs[-1]
        tpl = prefix + ".".join(s[2] for s in segs)
        if key is None:
            if name in node and node[name] != value:
                raise ParseError(f"{tpl}: already {node[name]!r}, cannot also be {value!r}")
            node[name] = value
        elif key == "":
            node.setdefault(name, []).append(value)
        else:
            item = self.child(node, name, key, tpl, rec, ids)
            for k, v in (value or {}).items():
                if k in item and item[k] != v:
                    raise ParseError(f"{tpl}.{k}: already {item[k]!r}, cannot also be {v!r}")
                item[k] = v
            return item, None
        if isinstance(value, dict):
            self.parent[id(value)] = (node, name)
        return node, name


class Converter:
    """Turns one cell into the value written to the record, per the crosswalk entry."""

    def __init__(self, cw):
        self.units = cw.get("units", {})
        self.unit_ns = cw["qudt"]["unit_ns"]
        self.kind_ns = cw["qudt"]["kind_ns"]
        self.prefix = cw["id_prefix"]

    def unit(self, entry, cell):
        """-> (QUDT local name or None, provenance note, flag or None)"""
        if cell.unit:
            if cell.unit not in self.units:
                raise ParseError(f"{cell.sheet}!{cell.coord}: unit {cell.unit!r} is not in the units table")
            if "unit" in entry:
                raise ParseError(f"{cell.sheet}!{cell.coord}: crosswalk sets a unit, but the sheet gives {cell.unit!r}")
            m = self.units[cell.unit]
            local, note = (m.get("qudt"), m.get("note")) if isinstance(m, dict) else (m, None)
            msg = f"unit from the unit row: {cell.unit!r}" + (f" -> {local}" if local else "")
            return local, msg + (f". {note}" if note else ""), None
        if entry.get("unit"):
            if not entry.get("unit_note"):
                raise ParseError(f"{cell.sheet}!{cell.coord}: a unit supplied by the crosswalk needs a unit_note")
            return entry["unit"], f"unit not in the workbook; {entry['unit_note']}", None
        return None, "no unit in the workbook; none recorded", f"No unit is given for '{cell.label}' ({cell.value})."

    def quantity_fields(self, entry, cell):
        local, unit_msg, flag = self.unit(entry, cell)
        out = {}
        if local:
            out["unit"] = self.unit_ns + local
        out["has_quantity_type"] = self.kind_ns + entry["kind"]
        if cell.unit and not local:
            out["description"] = f"{cell.value} {cell.unit} as given in the workbook; there is no QUDT unit for '{cell.unit}'"
        return out, unit_msg, flag

    def convert(self, entry, cell, rec):
        """-> (value, extra provenance notes, auto flag) ; value None means 'nothing to write'."""
        kind, v = entry["as"], cell.value
        notes, flag = [], None
        if kind == "text":
            out = str(v)
            if entry.get("strip_curie"):
                out = norm(re.sub(r"\(\s*[A-Za-z][\w.]*:\w+\s*\)", "", out))
        elif kind == "number":
            out = to_number(v)
            if out is None:
                raise ParseError(f"{cell.sheet}!{cell.coord}: {v!r} is not a number")
        elif kind == "id":
            out = self.prefix + slug(v)
        elif kind == "ref":
            out = None
        elif kind == "enum":
            table = {str(k).casefold(): val for k, val in entry["values"].items()}
            if str(v).casefold() not in table:
                raise ParseError(f"{cell.sheet}!{cell.coord}: {v!r} is not in the value map {list(entry['values'])}")
            out = table[str(v).casefold()]
        elif kind == "qualitative":
            out = {"value": str(v)}
        elif kind == "identifier":
            out = {"notation": str(v)}
        elif kind == "quantity":
            num = to_number(v)
            if num is None:
                return None, [f"{v!r} is not a number"], None
            fields, unit_msg, flag = self.quantity_fields(entry, cell)
            out = {"value": num, **fields}
            notes.append(unit_msg)
        elif kind in ("range", "range_max"):
            if kind == "range":
                m = RANGE.match(str(v))
                if not m:
                    raise ParseError(f"{cell.sheet}!{cell.coord}: {v!r} is not a range like '50-100'")
                lo, hi = (to_number(x) for x in m.groups())
                out = {"min_value": lo, "max_value": hi}
            else:
                hi = to_number(v)
                if hi is None:
                    raise ParseError(f"{cell.sheet}!{cell.coord}: {v!r} is not a number")
                out = {"max_value": hi}
            fields, unit_msg, flag = self.quantity_fields(entry, cell)
            out.update(fields)
            notes.append(unit_msg)
        else:
            raise ParseError(f"unknown conversion 'as: {kind}'")
        if isinstance(out, dict):
            for k, val in (entry.get("attrs") or {}).items():
                if k == "description" and "description" in out:
                    out[k] = f"{val}; {out[k]}"
                else:
                    out[k] = val
            if entry.get("describe"):
                d = render(entry["describe"], rec)
                out["description"] = f"{d}; {out['description']}" if "description" in out else d
        return out, notes, flag


def entries_of(spec):
    return spec.get("columns") or spec.get("rows") or []


def ref_of(entry):
    return str(entry["col"]) if "col" in entry else str(entry["row"])


def check_layout(sheet):
    """The crosswalk must match the workbook: every header/row covered, labels as expected."""
    spec, problems = sheet.spec, []
    entries = entries_of(spec)
    covered = {ref_of(e) for e in entries}
    if spec["layout"] == "table":
        for col, header in sheet.headers.items():
            if col not in covered:
                problems.append(f"{sheet.name}: column {col} '{header}' is not in the crosswalk")
        for e in entries:
            actual = sheet.headers.get(ref_of(e))
            if norm(e.get("header")) != actual:
                problems.append(f"{sheet.name}: column {ref_of(e)} header is {actual!r}, crosswalk expects {e.get('header')!r}")
    else:
        for r, cell in sheet.headers.items():
            if str(r) not in covered:
                problems.append(f"{sheet.name}: row {r} '{cell.label}' is not in the crosswalk")
        for e in entries:
            cell = sheet.headers.get(int(ref_of(e)))
            if cell is None:
                problems.append(f"{sheet.name}: crosswalk row {ref_of(e)} is empty in the workbook")
            elif norm(e.get("label")) != cell.label:
                problems.append(f"{sheet.name}: row {ref_of(e)} label is {cell.label!r}, crosswalk expects {e.get('label')!r}")
            elif e.get("expect_term") and str(cell.term).casefold() != e["expect_term"].casefold():
                problems.append(f"{sheet.name}: row {ref_of(e)} term is {cell.term!r}, expected {e['expect_term']!r}")
    for coord in sheet.stray:
        problems.append(f"{sheet.name}!{coord}: non-empty cell outside the declared layout")
    return problems


def build(cw, base_dir, use_placeholders=True):
    wb = openpyxl.load_workbook(base_dir / cw["workbook"], data_only=True)
    workbook_name = Path(cw["workbook"]).name
    sheets = []
    for name, spec in cw["sheets"].items():
        if name not in wb.sheetnames:
            raise ParseError(f"sheet {name!r} not in the workbook ({wb.sheetnames})")
        sheets.append(READERS[spec["layout"]](wb[name], name, spec))
    extra = set(wb.sheetnames) - set(cw["sheets"])
    problems = [f"sheet {s!r} is not in the crosswalk" for s in sorted(extra)]
    for sheet in sheets:
        problems += check_layout(sheet)
    if problems:
        raise ParseError("crosswalk does not match the workbook:\n  " + "\n  ".join(problems))

    supplement = yaml.safe_load((base_dir / cw["supplement"]).read_text(encoding="utf8")) if cw.get("supplement") else {}
    b = Builder(cw["id_prefix"])
    conv = Converter(cw)
    flags = [(q["about"], " ".join(q["text"].split())) for q in supplement.get("open_questions", [])]

    def supplement_value(s, rec):
        """A supplement value as written, or converted like a cell when the entry has `as:`."""
        if "as" not in s:
            return s["value"], []
        cell = Cell("supplement", "-", s["to"], None, None, s["value"])
        entry = {**s, "unit_note": s.get("unit_note", f"given in {s['source']}")}
        value, notes, _ = conv.convert(entry, cell, rec)
        if value is None:
            raise ParseError(f"supplement {s['to']}: {s['value']!r} could not be converted ({notes})")
        return value, notes

    for e in supplement.get("dataset", []):
        value, notes = supplement_value(e, None)
        container, slot = b.put(b.root, e["to"], value, None, {})
        b.prov.append(Prov(container, slot, value, f"supplement: {e['source']}", e.get("basis", "curator"),
                           " ".join([e["why"].strip()] + notes)))

    for sheet in sheets:
        spec = sheet.spec
        for rec in sheet.records:
            obj = {"id": b.prefix + render(spec["record"]["id"], rec)}
            b.minted.append((f"{sheet.name} record", obj["id"]))
            obj.update(spec["record"].get("set", {}))
            b.root.setdefault(spec["record"]["list"], []).append(obj)
            b.parent[id(obj)] = (b.root, spec["record"]["list"])
            ids = spec.get("ids", {})
            for e in entries_of(spec):
                cell = rec.cells.get(ref_of(e))
                if cell is None or cell.value is None:
                    continue
                if "structural" in e:
                    raise ParseError(f"{sheet.name}!{cell.coord}: declared structural but holds {cell.value!r}")
                if "unused" in e:
                    cell.status.append(("unused", e["unused"]))
                    continue
                if "confirm" in e:
                    other = rec.cells.get(str(e["confirm"]))
                    if other is None or norm(other.value) != norm(cell.value):
                        raise ParseError(f"{sheet.name}!{cell.coord}: expected to repeat {e['confirm']} "
                                         f"({other.value if other else None!r}), holds {cell.value!r}")
                    cell.status.append(("duplicate", f"repeats {sheet.name}!{other.coord}: {e['why']}"))
                    continue
                value, notes, auto_flag = conv.convert(e, cell, rec)
                where = f"{sheet.name}!{cell.coord}"
                targets = e["to"] if isinstance(e["to"], list) else [e["to"]]
                if value is None and e["as"] == "quantity":      # not a number -> fallback
                    fb = e.get("fallback")
                    if not fb:
                        raise ParseError(f"{where}: {cell.value!r} is not a number and the entry has no fallback")
                    text = f"{fb['label']}: {cell.value}"
                    container, slot = b.put(obj, fb["to"], text, rec, ids)
                    b.prov.append(Prov(container, slot, text, source_of(workbook_name, cell), "fallback",
                                       f"{e['why']} Not a number, so kept as text.", cell))
                    cell.status.append(("mapped", f"{fb['to']} (fallback: not a number)"))
                    if not e.get("flag") and not e.get("answered"):
                        flags.append((where, f"'{cell.label}' is {cell.value!r}, not a number."))
                else:
                    for t in targets:
                        container, slot = b.put(obj, t, value, rec, ids)
                        note = " ".join([e["why"].strip()] + [n for n in notes if n])
                        shown = container.get("id") if e["as"] == "ref" else value
                        b.prov.append(Prov(container, slot, shown, source_of(workbook_name, cell), e["basis"], note, cell))
                        cell.status.append(("mapped", t))
                    if auto_flag and not e.get("flag") and not e.get("answered"):
                        flags.append((where, auto_flag))
                if e.get("flag"):
                    flags.append((where, " ".join(e["flag"].split())))
            for s in supplement.get("records", {}).get(sheet.name, []):
                if s.get("placeholder") and not use_placeholders:
                    continue
                value, notes = supplement_value(s, rec)
                container, slot = b.put(obj, s["to"], value, rec, ids)
                shown = container.get("id", value) if isinstance(value, dict) and slot is None else value
                basis = "placeholder" if s.get("placeholder") else s.get("basis", "curator")
                b.prov.append(Prov(container, slot, shown, f"supplement: {s['source']}", basis,
                                   " ".join([s["why"].strip()] + notes), placeholder=bool(s.get("placeholder"))))
    return b, sheets, flags


def source_of(workbook, cell):
    s = f"{workbook} [{cell.sheet}!{cell.coord}, '{cell.label}'"
    if cell.term:
        s += f", term {cell.term}"
    return s + "]"


# ----------------------------------------------------------------------------- 5. schema checks

class SchemaChecks:
    def __init__(self, schema_path):
        from linkml_runtime.utils.schemaview import SchemaView
        self.sv = SchemaView(str(schema_path))
        self.classes = set(self.sv.all_classes())

    def iri(self, curie):
        try:
            return self.sv.expand_curie(str(curie))
        except Exception:
            return str(curie)

    def designated(self, item, rng):
        for d in DESIGNATORS:
            if d in item:
                v = item[d]
                if v in self.classes:
                    return v
                for c in self.sv.class_descendants(rng):
                    cu = self.sv.get_class(c).class_uri
                    if cu and self.iri(cu) == self.iri(v):
                        return c
        return rng

    def assign_classes(self, root, root_class):
        cls_of = {}

        def walk(node, cls):
            cls_of[id(node)] = cls
            slots = set(self.sv.class_slots(cls))
            for slot, val in node.items():
                if slot not in slots:
                    continue
                rng = self.sv.induced_slot(slot, cls).range
                if rng not in self.classes:
                    continue
                for item in val if isinstance(val, list) else [val]:
                    if isinstance(item, dict):
                        walk(item, self.designated(item, rng))
        walk(root, root_class)
        return cls_of

    def _class_terms(self, cls, why):
        out = []
        for c in [cls] + [a for a in self.sv.class_ancestors(cls) if a != cls]:
            cd = self.sv.get_class(c)
            role = why if c == cls else f"{why}, ancestor {c}"
            if cd.class_uri:
                out.append((self.iri(cd.class_uri), f"class_uri of {c} [{role}]"))
            for m in list(cd.exact_mappings or []) + list(cd.close_mappings or []):
                out.append((self.iri(m), f"mapping of {c} [{role}]"))
        return out

    def targets(self, p, cls_of, parent):
        """Terms the target of a provenance record is known by: slot, classes, rdf_type, designator."""
        cls = cls_of.get(id(p.container))
        out = []
        if cls is None:
            return out
        out += self._class_terms(cls, "object written to")
        if id(p.container) in parent:
            pnode, pslot = parent[id(p.container)]
            pcls = cls_of.get(id(pnode))
            if pcls and pslot in self.sv.class_slots(pcls):
                ps = self.sv.induced_slot(pslot, pcls)
                if ps.slot_uri:
                    out.append((self.iri(ps.slot_uri), f"slot_uri of {pslot} [link to the object]"))
        if p.slot and p.slot in self.sv.class_slots(cls):
            s = self.sv.induced_slot(p.slot, cls)
            if s.slot_uri:
                out.append((self.iri(s.slot_uri), f"slot_uri of {p.slot}"))
            for m in list(s.exact_mappings or []) + list(s.close_mappings or []):
                out.append((self.iri(m), f"mapping of {p.slot}"))
            if s.range in self.classes:
                out += self._class_terms(s.range, f"range of {p.slot}")
        if isinstance(p.value, dict) and isinstance(p.value.get("rdf_type"), dict):
            out.append((self.iri(p.value["rdf_type"]["id"]), "rdf_type given to the value"))
        if p.slot in DESIGNATORS and isinstance(p.value, str):
            out.append((self.iri(p.value), "designated class"))
        return out

    def declared_recommended(self, cls, sname):
        """Recommended by the class (slot_usage) or by the slot's own definition. Induced slots also
        inherit `recommended` from generic DCAT-AP-PLUS parents such as has_quantitative_attribute,
        which would flag nearly every slot; those inherited flags are ignored here."""
        for c in self.sv.class_ancestors(cls):
            usage = (self.sv.get_class(c).slot_usage or {}).get(sname)
            if usage is not None and usage.recommended is not None:
                return bool(usage.recommended)
        s = self.sv.get_slot(sname)
        return bool(s is not None and s.recommended)

    GENERIC_BASE = "https://w3id.org/nfdi-de/dcat-ap-plus"
    GENERIC_MIXINS = {"MaterialisticMixin", "ChemicalSubstanceMixin", "ClassifierMixin"}

    def own_slots(self, cls):
        """Slots a domain class lists itself (slots, slot_usage, attributes of the class, its parents
        and mixins), leaving out the generic DCAT-AP-PLUS base classes and generic mixins."""
        out = set()
        for a in self.sv.class_ancestors(cls):
            cd = self.sv.get_class(a)
            if a in self.GENERIC_MIXINS or (cd.from_schema or "").rstrip("/") == self.GENERIC_BASE:
                continue
            out |= set(cd.slots or []) | set(cd.slot_usage or {}) | set(cd.attributes or {})
        return out

    def missing(self, root, cls_of, ids_of, required_only=False):
        """Unfilled required slots, and unfilled recommended slots that the object's own domain class
        lists (for the dataset itself: those declared recommended, e.g. DCAT keyword). Recommended
        flags that every slot inherits from generic DCAT-AP-PLUS parents, and attribute nodes
        (quantities, values, terms; a missing unit is already an open question), are left out."""
        out = []
        skip_roots = ("QuantitativeAttribute", "QualitativeAttribute", "QuantitativeRange",
                      "DefinedTerm", "Identifier")
        attribute_like = {d for r in skip_roots if r in self.classes for d in self.sv.class_descendants(r)}

        def walk(node, is_root=False):
            cls = cls_of.get(id(node))
            if cls:
                own = None if is_root or cls in attribute_like else self.own_slots(cls)
                for sname in self.sv.class_slots(cls):
                    if sname in node:
                        continue
                    s = self.sv.induced_slot(sname, cls)
                    if s.required:
                        out.append((ids_of(node), cls, sname, "required"))
                    elif required_only or not s.recommended or cls in attribute_like:
                        continue
                    elif (is_root and self.declared_recommended(cls, sname)) or (own and sname in own):
                        out.append((ids_of(node), cls, sname, "recommended"))
            for val in node.values():
                for item in val if isinstance(val, list) else [val]:
                    if isinstance(item, dict):
                        walk(item)
        walk(root, is_root=True)
        return out


# ----------------------------------------------------------------------------- 6. write

ROOT_ORDER = ["id", "title", "description", "rdf_type", "keyword", "creator", "contact_point",
              "qualified_attribution", "was_generated_by", "is_about_activity", "is_about_entity"]


def ordered(node, top=False):
    """Reading order: identity first, then literal slots, then nested objects (column order within)."""
    if isinstance(node, list):
        return [ordered(x) for x in node]
    if not isinstance(node, dict):
        return node
    first = ROOT_ORDER if top else ["id", *DESIGNATORS, "title", "description", "rdf_type"]
    nested = lambda v: isinstance(v, dict) or (isinstance(v, list) and any(isinstance(x, dict) for x in v))
    rest = [k for k in node if k not in first]
    keys = ([k for k in first if k in node] + [k for k in rest if not nested(node[k])]
            + [k for k in rest if nested(node[k])])
    return {k: ordered(node[k]) for k in keys}


def path_of(builder, obj):
    """Readable location of an object: was_generated_by[SYN_x].realized_plan ..."""
    parts = []
    while id(obj) in builder.parent:
        parent, slot = builder.parent[id(obj)]
        val = parent.get(slot)
        if isinstance(val, list):
            pos = next((i for i, x in enumerate(val) if x is obj), "?")
            tag = obj.get("id", str(pos)) if isinstance(obj, dict) else str(pos)
            parts.append(f"{slot}[{tag.replace(builder.prefix, '')}]")
        else:
            parts.append(slot)
        obj = parent
    return ".".join(reversed(parts)) or "(dataset)"


def compact(v):
    if isinstance(v, dict):
        return "{" + ", ".join(f"{k}: {compact(x)}" for k, x in v.items()) + "}"
    if isinstance(v, list):
        return "[" + ", ".join(compact(x) for x in v) + "]"
    return str(v)


def md(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def write_provenance(path, b, cw):
    entries = []
    for p in b.prov:
        loc = path_of(b, p.container)
        target = f"{loc}.{p.slot}" if p.slot else loc
        entries.append({"target": target.lstrip("."), "value": p.value, "source": p.source,
                        "basis": p.basis, "note": " ".join(str(p.note).split())})
    header = (
        "# ============================================================\n"
        f"# SOURCE DOCUMENTATION (generated by {SCRIPT_REF}, do not edit)\n"
        f"# Provenance of every value in {Path(cw['output']).name}\n"
        "# ============================================================\n"
        "#\n"
        "# FORMAT\n"
        "#   target: where the value sits in the record (ids without the coremeta4cat: prefix)\n"
        "#   value:  what was written\n"
        "#   source: workbook cell [sheet!cell, header or row label, term] or supplement entry\n"
        "#   basis:  direct | deduced | schema-forced | fallback (crosswalk) ;\n"
        "#           provider | curator | placeholder (supplement)\n"
        "#   note:   why this target, plus where the unit came from\n"
        "# ============================================================\n\n")
    path.write_text(header + yaml.safe_dump({"entries": entries}, sort_keys=False, allow_unicode=True, width=100),
                    encoding="utf8")


def write_report(path, cw, b, sheets, flags, checks):
    L = []
    w = L.append
    w(f"# Parse report: {Path(cw['workbook']).name}\n")
    w(f"Generated by `{SCRIPT_REF}` from `{HERE.name}/crosswalk.yaml` and `{HERE.name}/supplement.yaml`. "
      "Do not edit; rerun the parser.\n")
    cells = [c for s in sheets for r in s.records for c in r.cells.values() if c.value is not None]
    count = lambda kind: sum(1 for c in cells if any(st[0] == kind for st in c.status))
    w("## Summary\n")
    w(f"- Value cells: {len(cells)} — mapped {count('mapped')}, repeated values {count('duplicate')}, "
      f"unused {count('unused')}")
    w(f"- Records: " + ", ".join(f"{s.name}: {len(s.records)}" for s in sheets))
    w(f"- Values written: {len(b.prov)} (from the workbook {sum(1 for p in b.prov if p.cell)}, "
      f"from the supplement {sum(1 for p in b.prov if not p.cell)}, of which placeholders "
      f"{sum(1 for p in b.prov if p.placeholder)})")
    by_basis = {}
    for p in b.prov:
        if p.cell:
            by_basis[p.basis] = by_basis.get(p.basis, 0) + 1
    w("- Basis of workbook values: " + ", ".join(f"{k} {v}" for k, v in sorted(by_basis.items())) + "\n")

    w("## Open questions for the data provider\n")
    for i, (where, text) in enumerate(flags, 1):
        w(f"{i}. **{where}**: {text}")
    if not flags:
        w("None.")
    w("")
    w("## Placeholders (required by the schema, not in the source)\n")
    placeholders = [p for p in b.prov if p.placeholder]
    for p in placeholders:
        loc = path_of(b, p.container) + (f".{p.slot}" if p.slot else "")
        w(f"- `{loc}` = {compact(p.value)} ({' '.join(str(p.note).split())})")
    if not placeholders:
        w("None.")
    w("")

    for s in sheets:
        w(f"## Cell inventory: {s.name}\n")
        w("| Cell | Label | Value | Status | Target(s) |")
        w("|---|---|---|---|---|")
        for r in s.records:
            for c in r.cells.values():
                if c.value is None:
                    continue
                kinds = sorted({st[0] for st in c.status}) or ["NOT COVERED"]
                tg = "<br>".join(md(st[1]) for st in c.status)
                w(f"| {c.coord} | {md(c.label)} | {md(c.value)} | {', '.join(kinds)} | {tg} |")
        if s.spec["layout"] == "key_value":
            for r, c in s.headers.items():
                if c.value is None:
                    entry = next((e for e in entries_of(s.spec) if int(ref_of(e)) == r), {})
                    w(f"| A{r} | {md(c.label)} | — | structural | {md(entry.get('structural', ''))} |")
        w("")

    if checks:
        w("## Header terms against the target slots\n")
        w("Each term written in a header (or the term column) is compared with the slot, class, "
          "rdf_type or designator it was mapped to (CURIEs expanded to IRIs first). A NO MATCH is "
          "explained by the `why` of that cell's crosswalk entry.\n")
        res = [r[2] for r in checks["terms"]]
        w(f"Terms: {sum(1 for r in checks['terms'] if r[1] != '—')}; match "
          f"{sum(1 for r in res if r.startswith('matches'))}; no match {sum(1 for r in res if r.startswith('NO MATCH'))}; "
          f"on repeated values {sum(1 for r in res if r.startswith('not mapped'))}; cells without a term "
          f"{sum(1 for r in checks['terms'] if r[1] == '—')}.\n")
        w("| Cell | Term | Result |")
        w("|---|---|---|")
        for row in checks["terms"]:
            w(f"| {row[0]} | {md(row[1])} | {md(row[2])} |")
        w("")
        w("## Required and recommended slots that stay empty\n")
        w("Slots declared recommended on the class or on the slot itself (flags inherited from "
          "generic DCAT-AP-PLUS slots are left out, as are quantities and other attribute values). "
          "Not every one applies to this experiment.\n")
        w("| Object | Class | Slot | Level |")
        w("|---|---|---|---|")
        for obj, cls, slot, level in checks["missing"]:
            w(f"| {md(obj)} | {cls} | {slot} | {level} |")
        w("")
    w("## Identifiers minted\n")
    for tpl, i in b.minted:
        w(f"- `{i}` ({md(tpl)})")
    path.write_text("\n".join(L) + "\n", encoding="utf8")


def run_checks(sch, cw, b, sheets):
    record = b.root
    cls_of = sch.assign_classes(record, cw["root_class"])
    terms = []
    by_cell = {}
    for p in b.prov:
        if p.cell:
            by_cell.setdefault((p.cell.sheet, p.cell.coord), []).append(p)
    for s in sheets:
        for r in s.records:
            for c in r.cells.values():
                if c.value is None:
                    continue
                written = c.term and [c.term] or terms_in(c.label)
                provs = by_cell.get((c.sheet, c.coord), [])
                if not written:
                    terms.append((f"{c.sheet}!{c.coord}", "—", "no term in the header"))
                    continue
                for t in written:
                    if not provs:
                        terms.append((f"{c.sheet}!{c.coord}", t, "not mapped (repeat of another cell)"))
                        continue
                    hits = []
                    for p in provs:
                        for iri, why in sch.targets(p, cls_of, b.parent):
                            if iri == sch.iri(t) and why not in hits:
                                hits.append(why)
                    terms.append((f"{c.sheet}!{c.coord}", t,
                                  "matches " + "; ".join(hits[:3]) if hits else "NO MATCH, see the crosswalk's why"))
    ids_of = lambda node: node.get("id", path_of(b, node)).replace(b.prefix, "")
    return {"terms": terms, "missing": sch.missing(record, cls_of, ids_of)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("crosswalk", nargs="?", default=str(HERE / "crosswalk.yaml"),
                    help="crosswalk file (default: crosswalk.yaml next to this script)")
    ap.add_argument("--schema", help="coremeta4cat.yaml for the term and empty-slot checks "
                    "(default: the schema of the CoreMeta4Cat checkout this script is in)")
    ap.add_argument("--no-checks", action="store_true", help="skip the schema-based checks")
    ap.add_argument("--no-placeholders", action="store_true",
                    help="leave out supplement placeholders (shows what validation reports without them)")
    ap.add_argument("--out", help="write the record here instead of the crosswalk's output path")
    a = ap.parse_args()
    schema = None if a.no_checks else (Path(a.schema).resolve() if a.schema else default_schema())
    if a.no_placeholders and not a.out:
        ap.error("--no-placeholders needs --out (keeps the published record unchanged)")
    cw_path = Path(a.crosswalk).resolve()
    cw = yaml.safe_load(cw_path.read_text(encoding="utf8"))
    base = cw_path.parent
    try:
        b, sheets, flags = build(cw, base, use_placeholders=not a.no_placeholders)
    except ParseError as e:
        sys.exit(f"ERROR: {e}")
    record = ordered(b.root, top=True)
    out = Path(a.out).resolve() if a.out else (base / cw["output"]).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    header = (f"# CatalysisDataset generated from {Path(cw['workbook']).name} by {SCRIPT_REF}\n"
              f"# (crosswalk: {cw_path.name}). Do not edit by hand: change the crosswalk or supplement and rerun.\n"
              "# Provenance of every value: source_documentation.yaml; open questions: parse_report.md\n")
    if a.no_placeholders:
        header += "# Built WITHOUT placeholders: required fields missing from the source stay empty.\n"
    out.write_text(header + yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100), encoding="utf8")
    print(f"record:     {out}")
    if a.no_placeholders:
        if schema:
            sch = SchemaChecks(schema)
            ids_of = lambda node: node.get("id", path_of(b, node)).replace(b.prefix, "")
            gaps = sch.missing(b.root, sch.assign_classes(b.root, cw["root_class"]), ids_of, required_only=True)
            for obj, cls, slot, _ in gaps:
                print(f"required slot not filled: {cls} {obj}: {slot}")
            print(f"{len(gaps)} required slots empty without placeholders")
        return
    checks = run_checks(SchemaChecks(schema), cw, b, sheets) if schema else None
    prov_path, report_path = (base / cw["provenance"]).resolve(), (base / cw["report"]).resolve()
    write_provenance(prov_path, b, cw)
    write_report(report_path, cw, b, sheets, flags, checks)
    print(f"provenance: {prov_path}\nreport:     {report_path}")
    print(f"{len(b.prov)} values written, {len(flags)} open questions"
          + ("" if checks else " (schema checks skipped: no schema found, or --no-checks)"))


if __name__ == "__main__":
    main()
