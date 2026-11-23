"""
schema_to_excel.py

Exports the merged CoreMeta4Cat LinkML schema to an Excel workbook.

Sheet order:
  1. Introduction  -- overview, how to use the workbook
  2. Legend        -- colour coding and column explanations
  3. CoreMeta4Cat  -- CatalysisDataset top-level fields (the minimal cross-cutting layer)
  4. Synthesis
  5. Characterization
  6. Reaction
  7. Simulation

Columns (sheets 3-7):
  label          human-readable slot or class name
  type           "slot" or "class"
  domain         the slot or class this entry belongs to (empty for top-level entries)
  M / R / O      Mandatory / Recommended / Optional classification
  range          LinkML range type
  multivalued    "Yes" if the field accepts a list of values (empty = single value)
  inlined as list  "Yes" if linked records are stored inline as an ordered list
  unit           UCUM code for the unit of measurement (empty if not applicable)
  uri            ontology CURIE for the term
  description    documentation string

Slot values are the *effective* values LinkML works with (SchemaView
.induced_slot): a slot inherits from its parent slots (e.g. everything that
is_a has_quantitative_attribute is recommended and multivalued unless it says
otherwise), identifier slots are mandatory, and class slot_usage overrides
apply. This is what the generated JSON Schema / Pydantic models enforce.

Hidden sheet:
  _baseline      very hidden copy of every data row exactly as generated. The
                 inbox pipeline compares a contributor's workbook against it to
                 find the rows they actually changed (see workbook_rows.py).

Output:
  docs/assets/coremeta4cat_vocabulary.xlsx  (rewritten only if its content changed)

Run:
    just schema-to-excel
  or directly:
    uv run python scripts/schema_to_excel.py
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import sys
import zipfile
from pathlib import Path
from typing import Any

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from generate_schema_docs import (  # noqa: E402
    build_origin_index,
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    get_subclasses,
    is_mixin,
    load_merged_schema,
    snake_to_readable,
)
from workbook_rows import (  # noqa: E402
    BASELINE_SHEET,
    DATA_SHEETS,
    HEADERS,
    REFERENCE_SHEET,
    baseline_values,
    row_from_values,
)

SCHEMA_DIR  = _ROOT / "src" / "coremeta4cat" / "schema"
OUTPUT_PATH = _ROOT / "docs" / "assets" / "coremeta4cat_vocabulary.xlsx"
ROOT_MODULE = "coremeta4cat.yaml"   # imports every other module

# ─────────────────────────────────────────────────────────────────────────────
# Styles
# ─────────────────────────────────────────────────────────────────────────────

FILL_HEADER   = PatternFill("solid", fgColor="1F4E79")
FONT_HEADER   = Font(color="FFFFFF", bold=True)
FILL_TITLE    = PatternFill("solid", fgColor="2E75B6")
FONT_TITLE    = Font(color="FFFFFF", bold=True, size=14)
FILL_SECTION  = PatternFill("solid", fgColor="BDD7EE")
FONT_SECTION  = Font(bold=True)
FILL_M        = PatternFill("solid", fgColor="FCE4D6")
FILL_R        = PatternFill("solid", fgColor="DEEAF1")
FILL_O        = PatternFill("solid", fgColor="E2EFDA")
FILL_M_LEGEND = PatternFill("solid", fgColor="C00000")
FILL_R_LEGEND = PatternFill("solid", fgColor="2E75B6")
FILL_O_LEGEND = PatternFill("solid", fgColor="70AD47")
FONT_WHITE    = Font(color="FFFFFF", bold=True)

FILL_CLASS    = PatternFill("solid", fgColor="D9D9D9")
FONT_CLASS    = Font(bold=True, italic=True)

# Rows inherited from a vendored chemdcat-ap class (e.g. ChemicalReaction's
# used_reactant on CatalyticReaction) are shown for reference but are not
# editable via the Excel inbox workflow -- styled distinctly so contributors
# don't try to change them.
FILL_INHERITED = PatternFill("solid", fgColor="F2F2F2")
FONT_INHERITED = Font(italic=True, color="7F7F7F")
FONT_INHERITED_CLASS = Font(bold=True, italic=True, color="7F7F7F")

# Maps sheet title (user-facing) -> LinkML class name in the schema
CLASS_MAP = {
    "Synthesis": "Synthesis",
    "Characterization": "Characterization",
    "Reaction": "CatalyticReaction",
    "Simulation": "Simulation",
}

# Dropdowns offered on the data sheets: column letter -> allowed values.
DROPDOWNS = {
    "B": ("slot", "class"),
    "D": ("M", "R", "O"),
    "F": ("Yes",),
    "G": ("Yes",),
}
DROPDOWN_SPARE_ROWS = 500   # blank rows below the data that get the dropdowns too

# ─────────────────────────────────────────────────────────────────────────────
# Effective slot values (LinkML SchemaView)
# ─────────────────────────────────────────────────────────────────────────────

# Both caches are keyed by the schema's content (schema_fingerprint), so copies
# of the same schema share one entry and any edit to a module invalidates it.
_VIEW_CACHE: dict[str, Any] = {}
_ROWS_CACHE: dict[str, dict[str, list[dict]]] = {}
_CACHE_SIZE = 6


def schema_fingerprint(schema_dir: Path | str) -> str:
    """Hash of every YAML module in schema_dir, used to cache per schema state."""
    digest = hashlib.sha1()
    for path in sorted(Path(schema_dir).glob("*.yaml")):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def _cache_put(cache: dict, key, value) -> None:
    while len(cache) >= _CACHE_SIZE:
        cache.pop(next(iter(cache)))
    cache[key] = value


def load_schema_view(schema_dir: Path | str = SCHEMA_DIR):
    """
    LinkML SchemaView of the full schema, imports resolved.

    The vendored chemdcat-ap modules import dcat-ap-plus from the web; the
    slot inheritance that decides most M/R/O and multivalued values
    (has_qualitative_attribute, has_quantitative_attribute, ...) lives there,
    so this needs network access -- like every LinkML generator run.
    """
    from linkml_runtime import SchemaView

    key = schema_fingerprint(schema_dir)
    sv = _VIEW_CACHE.get(key)
    if sv is None:
        try:
            sv = SchemaView(str(Path(schema_dir) / ROOT_MODULE))
            sv.all_slots()   # resolve all imports now, so failures surface here
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(
                f"Could not load the LinkML schema from {schema_dir}: {exc}. "
                "The vendored chemdcat-ap modules import dcat-ap-plus from the "
                "web, so this needs network access."
            ) from exc
        _cache_put(_VIEW_CACHE, key, sv)
    return sv


def slot_row_values(sv, slot_name: str, class_name: str) -> dict | None:
    """
    The values the workbook shows for slot_name on class_name: LinkML's
    induced slot (slot inheritance, identifier => mandatory, slot_usage of
    the class and its ancestors). None if LinkML does not know the slot.
    """
    try:
        ind = sv.induced_slot(slot_name, class_name)
    except Exception:  # noqa: BLE001 -- unknown slot or class
        return None
    unit = getattr(ind.unit, "ucum_code", None) if ind.unit is not None else None
    rng = ind.range or "string"
    # inlined_as_list only means something for class-valued fields; LinkML
    # also reports it (inherited) on string/number slots.
    inlined = bool(ind.inlined_as_list) and sv.get_class(rng) is not None
    return {
        "mro":             "M" if ind.required else ("R" if ind.recommended else "O"),
        "range":           rng,
        "multivalued":     "Yes" if ind.multivalued else "",
        "inlined_as_list": "Yes" if inlined else "",
        "unit":            unit or "",
        "uri":             ind.slot_uri or "",
        "description":     ind.description or "",
    }


def _raw_row_values(schema: dict, slot_name: str, class_name: str, synthetic: dict | None) -> dict:
    """Fallback for slots SchemaView cannot resolve: the YAML values as written."""
    slot_def = dict(synthetic or get_slot_details(schema, slot_name))
    usage = ((schema.get("classes", {}).get(class_name) or {}).get("slot_usage") or {}).get(slot_name) or {}
    slot_def.update({k: v for k, v in usage.items() if v is not None})
    mro = "M" if slot_def.get("required") else ("R" if slot_def.get("recommended") else "O")
    return {
        "mro":             mro,
        "range":           slot_def.get("range") or "string",
        "multivalued":     "Yes" if slot_def.get("multivalued") else "",
        "inlined_as_list": "Yes" if slot_def.get("inlined_as_list") else "",
        "unit":            (slot_def.get("unit") or {}).get("ucum_code", "") or "",
        "uri":             slot_def.get("slot_uri", "") or "",
        "description":     slot_def.get("description", "") or "",
    }


def _write_data_headers(ws) -> None:
    for col, header in enumerate(HEADERS, start=1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
    ws.freeze_panes = "A2"


def _append_row(ws, row_data: list, row_type: str, mro: str, owned: bool = True) -> None:
    ws.append(row_data)
    if not owned:
        # Inherited from a vendored chemdcat-ap class -- reference-only,
        # not modifiable via the Excel inbox workflow.
        for cell in ws[ws.max_row]:
            cell.fill = FILL_INHERITED
            cell.font = FONT_INHERITED_CLASS if row_type == "class" else FONT_INHERITED
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    elif row_type == "class":
        for cell in ws[ws.max_row]:
            cell.fill = FILL_CLASS
            cell.font = FONT_CLASS
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    else:
        fill = {"M": FILL_M, "R": FILL_R, "O": FILL_O}.get(mro)
        if fill:
            for cell in ws[ws.max_row]:
                cell.fill = fill
                cell.alignment = Alignment(wrap_text=True, vertical="top")


def _auto_width(ws) -> None:
    for col_cells in ws.columns:
        max_len = max((len(str(c.value or "")) for c in col_cells), default=10)
        ws.column_dimensions[get_column_letter(col_cells[0].column)].width = min(max_len + 4, 60)


def _add_dropdowns(ws) -> None:
    """In-cell dropdowns for the columns that only accept a few values."""
    last_row = ws.max_row + DROPDOWN_SPARE_ROWS
    for column, values in DROPDOWNS.items():
        dv = DataValidation(
            type="list",
            formula1='"' + ",".join(values) + '"',
            allow_blank=True,
            showErrorMessage=True,
            errorStyle="warning",
            errorTitle="Unexpected value",
            error=f"Expected one of: {', '.join(values)} (or leave it empty).",
        )
        dv.add(f"{column}2:{column}{last_row}")
        ws.add_data_validation(dv)


# ─────────────────────────────────────────────────────────────────────────────
# Introduction sheet
# ─────────────────────────────────────────────────────────────────────────────

def build_intro_sheet(wb: openpyxl.Workbook) -> None:
    ws = wb.create_sheet(title="Introduction")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 90

    def _title(row: int, text: str) -> None:
        ws.row_dimensions[row].height = 28
        c = ws.cell(row=row, column=1, value=text)
        c.font = FONT_TITLE
        c.fill = FILL_TITLE
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=2)

    def _section(row: int, text: str) -> None:
        ws.row_dimensions[row].height = 18
        c = ws.cell(row=row, column=1, value=text)
        c.font = FONT_SECTION
        c.fill = FILL_SECTION
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=2)

    def _row(row: int, label: str, value: str) -> None:
        ws.row_dimensions[row].height = 40
        lc = ws.cell(row=row, column=1, value=label)
        lc.font = Font(bold=True)
        lc.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        vc = ws.cell(row=row, column=2, value=value)
        vc.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    def _blank(row: int) -> None:
        ws.row_dimensions[row].height = 8

    r = 1
    _title(r, "CoreMeta4Cat Vocabulary Reference Workbook"); r += 1
    _blank(r); r += 1

    _section(r, "About this workbook"); r += 1
    _row(r, "Project", "CoreMeta4Cat is a community-driven metadata initiative under NFDI4Cat that defines the minimum information required for reporting catalysis research data. It is built on the FAIR principles (Findable, Accessible, Interoperable, Reusable)."); r += 1
    _row(r, "Purpose", "This workbook is both a structured reference of the CoreMeta4Cat vocabulary and the way to propose changes to it. Browse it as a lookup reference when designing or annotating your own data sheets -- or edit it and submit it as a pull request to propose new fields, classes, or corrections. See 'How to propose changes' below."); r += 1
    _row(r, "Ground truth", "The LinkML schema files in src/coremeta4cat/schema/ are the authoritative source. This workbook is generated automatically from the schema via: just schema-to-excel"); r += 1
    _row(r, "Source", "https://github.com/nfdi4cat/CoreMeta4Cat"); r += 1
    _blank(r); r += 1

    _section(r, "Sheet overview"); r += 1
    _row(r, "Introduction", "This sheet — project overview and guidance."); r += 1
    _row(r, "Legend", "Explanation of colour coding and column meanings."); r += 1
    _row(r, "CoreMeta4Cat", "The minimal cross-cutting fields that apply to every catalysis dataset, regardless of data class (based on CatalysisDataset). Reference only -- edits on this sheet are not applied."); r += 1
    _row(r, "Synthesis", "Metadata fields for catalyst preparation / synthesis experiments."); r += 1
    _row(r, "Characterization", "Metadata fields for analytical characterization of catalysts."); r += 1
    _row(r, "Reaction", "Metadata fields for catalytic reaction testing and performance evaluation."); r += 1
    _row(r, "Simulation", "Metadata fields for computational / theoretical catalysis studies."); r += 1
    _blank(r); r += 1

    _section(r, "How to propose changes"); r += 1
    _row(r, "1. Edit", "Download a fresh copy of this file and edit the Synthesis / Characterization / Reaction / Simulation sheets directly. Do not rename sheets or change column headers -- the automated check requires exact names. The file keeps a hidden copy of how it looked when it was generated, so only the rows you change are applied -- even if the schema changed after your download."); r += 1
    _row(r, "2. Modify a field", "Edit an existing row's M/R/O, range, multivalued, unit, uri, or description to propose a correction. An M/R/O change applies to the row's class only."); r += 1
    _row(r, "3. Add a field", "Add a new row: give it a label, set type to 'slot', and set domain to the class it belongs to (leave empty for a top-level field). You can add a new slot and the new class it points to in the same submission -- both rows will be validated together. Please always fill in a description."); r += 1
    _row(r, "4. Remove a field", "Delete its row. A field a class inherits from its parent class can only be removed from the parent; the automated check tells you if that applies."); r += 1
    _row(r, "5. Submit", "Place the edited file at inbox/coremeta4cat_vocabulary.xlsx and open a pull request. An automated check validates the changes and reports any problems as a PR comment before a maintainer reviews it. See inbox/README.md for the full workflow."); r += 1
    _row(r, "Read-only rows", "Rows shown in grey italics (see Legend) are inherited from chemdcat-ap, the chemistry model CoreMeta4Cat builds on. They are shown for reference but cannot be added, changed, or removed through this workflow -- edits to them are reported, not applied."); r += 1
    _row(r, "Shared fields", "Some fields (e.g. has_atmosphere) are defined once and reused across several classes -- editing their description, range, multivalued, unit or uri is a global change, not scoped to a single sheet section. The automated check will warn you and list every other class affected if this applies to your edit."); r += 1
    _blank(r); r += 1

    _section(r, "How to read the data sheets"); r += 1
    _row(r, "label", "Human-readable name of the metadata field or class."); r += 1
    _row(r, "type", "Whether this row is a 'slot' (a metadata field) or a 'class' (a structured sub-record type)."); r += 1
    _row(r, "domain", "The slot or class this entry belongs to. Empty means it is a top-level entry of the data class."); r += 1
    _row(r, "M / R / O", "Whether the field is Mandatory (must be reported), Recommended (strongly encouraged), or Optional -- including what a field inherits from the more general field it is based on. See the Legend sheet for colour coding."); r += 1
    _row(r, "range", "The expected value type — a primitive (string, float, integer) or a class name that expands into its own set of fields."); r += 1
    _row(r, "multivalued", "'Yes' if the field accepts a list of values; empty means a single value. Most fields are single-valued."); r += 1
    _row(r, "inlined as list", "'Yes' if linked sub-records are stored directly inside the parent as an ordered list. Empty if not applicable. See Legend for details."); r += 1
    _row(r, "unit", "Unit of measurement expressed as a UCUM code (e.g. 'Cel', 'cm', 'mol/L'). Empty if the field has no unit."); r += 1
    _row(r, "uri", "The CURIE (Compact URI) linking this field to a term in an established ontology (e.g. Voc4Cat, CHMO, OBI)."); r += 1
    _row(r, "description", "Documentation string from the schema explaining the purpose of the field."); r += 1


# ─────────────────────────────────────────────────────────────────────────────
# Legend sheet
# ─────────────────────────────────────────────────────────────────────────────

def build_legend_sheet(wb: openpyxl.Workbook) -> None:
    ws = wb.create_sheet(title="Legend")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 70

    def _title(row: int, text: str) -> None:
        ws.row_dimensions[row].height = 28
        c = ws.cell(row=row, column=1, value=text)
        c.font = FONT_TITLE
        c.fill = FILL_TITLE
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)

    def _section(row: int, text: str) -> None:
        ws.row_dimensions[row].height = 18
        c = ws.cell(row=row, column=1, value=text)
        c.font = FONT_SECTION
        c.fill = FILL_SECTION
        c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)

    def _color_row(row: int, label: str, fill: PatternFill, font: Font, example: str, desc: str) -> None:
        ws.row_dimensions[row].height = 36
        lc = ws.cell(row=row, column=1, value=label)
        lc.fill = fill
        lc.font = font
        lc.alignment = Alignment(horizontal="center", vertical="center")
        ec = ws.cell(row=row, column=2, value=example)
        ec.fill = fill
        ec.font = font
        ec.alignment = Alignment(horizontal="center", vertical="center")
        dc = ws.cell(row=row, column=3, value=desc)
        dc.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    def _col_row(row: int, col_name: str, desc: str) -> None:
        ws.row_dimensions[row].height = 40
        lc = ws.cell(row=row, column=1, value=col_name)
        lc.font = Font(bold=True)
        lc.alignment = Alignment(horizontal="left", vertical="top", indent=1, wrap_text=True)
        dc = ws.cell(row=row, column=3, value=desc)
        dc.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    def _blank(row: int) -> None:
        ws.row_dimensions[row].height = 8

    r = 1
    _title(r, "Legend"); r += 1
    _blank(r); r += 1

    _section(r, "Colour coding — M / R / O"); r += 1
    _color_row(r, "Mandatory (M)", FILL_M_LEGEND, FONT_WHITE,
               "M", "Must be reported. The field is required to produce a valid, schema-compliant record."); r += 1
    _color_row(r, "Recommended (R)", FILL_R_LEGEND, FONT_WHITE,
               "R", "Strongly encouraged. Omitting these fields significantly reduces the findability and reusability of the data."); r += 1
    _color_row(r, "Optional (O)", FILL_O_LEGEND, FONT_WHITE,
               "O", "Useful additional context. Provide if available; not required for a valid record."); r += 1
    _color_row(r, "Inherited (read-only)", FILL_INHERITED, FONT_INHERITED,
               "—", "Shown in grey italics: a field or class inherited from chemdcat-ap (the underlying chemistry data model CoreMeta4Cat is built on). These rows are for reference only — they cannot be added, changed, or removed via the Excel inbox workflow."); r += 1
    _blank(r); r += 1

    _section(r, "Column descriptions"); r += 1
    _col_row(r, "label",
             "Human-readable name of the metadata field or class, derived from the LinkML slot or class name."); r += 1
    _col_row(r, "type",
             "'slot' — a metadata field carrying a value. 'class' — a structured sub-record type reachable via the slot above it. Class rows are shown in grey italics."); r += 1
    _col_row(r, "domain",
             "The slot or class this entry belongs to in the hierarchy. An empty domain means the entry is at the top level of the data class."); r += 1
    _col_row(r, "M / R / O",
             "M = Mandatory, R = Recommended, O = Optional. The 'required' and 'recommended' values LinkML uses for this field on this class -- including values inherited from the more general field it is based on. Identifier fields (id) are always mandatory."); r += 1
    _col_row(r, "range",
             "The expected value type. Primitives (string, float, integer, boolean, uri) are leaf values. A class name means the field expands into a structured sub-record defined by the named class."); r += 1
    _col_row(r, "multivalued",
             "'Yes' means a list of values is expected for this field (e.g. several reactants). Empty means a single value only. Class rows leave this empty — it is a property of slots."); r += 1
    _col_row(r, "inlined as list",
             "'Yes' means linked sub-records are stored directly inside the parent record as an ordered list, rather than as separate entries referenced by identifier. Empty = not inlined. Relevant only when the range is a class type."); r += 1
    _col_row(r, "unit",
             "Unit of measurement for numeric fields, expressed as a UCUM code (e.g. 'Cel' for Celsius, 'cm' for centimetres, 'mol/L' for molarity). Empty if the field has no unit."); r += 1
    _col_row(r, "uri",
             "CURIE (Compact URI) linking this field or class to a term in an established ontology. Click the linked term in the schema documentation for the full URI."); r += 1
    _col_row(r, "description",
             "Documentation string from the schema explaining the meaning and purpose of the field."); r += 1
    _blank(r); r += 1

    _section(r, "Notes"); r += 1
    ws.row_dimensions[r].height = 32
    nc = ws.cell(row=r, column=1,
                 value="This workbook is generated automatically from the LinkML schema (just schema-to-excel), so the schema is always the ground truth. You can still edit a downloaded copy to propose changes -- see 'How to propose changes' on the Introduction sheet -- your edits just don't change the schema until they're submitted, validated, and merged.")
    nc.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)


# ─────────────────────────────────────────────────────────────────────────────
# CoreMeta4Cat (CatalysisDataset) sheet
# ─────────────────────────────────────────────────────────────────────────────

CATCORE_CLASS = "CatalysisDataset"


def collect_catcore_rows(schema: dict, sv=None) -> list[list]:
    """
    The minimal cross-cutting layer -- the CatalysisDataset fields its
    slot_usage highlights, with the values LinkML uses for them.
    """
    sv = sv if sv is not None else load_schema_view(SCHEMA_DIR)
    slot_usage = (schema.get("classes", {}).get(CATCORE_CLASS) or {}).get("slot_usage") or {}

    rows: list[list] = []
    seen: set = set()
    for su_name, su_def in slot_usage.items():
        if not su_def:
            continue
        label = snake_to_readable(su_name)
        if label in seen:
            continue
        seen.add(label)
        vals = (slot_row_values(sv, su_name, CATCORE_CLASS)
                or _raw_row_values(schema, su_name, CATCORE_CLASS, su_def))
        rows.append([label, "slot", "", vals["mro"], vals["range"], vals["multivalued"],
                     vals["inlined_as_list"], vals["unit"], vals["uri"], vals["description"]])
    return rows


def build_catcore_sheet(wb: openpyxl.Workbook, schema: dict, sv=None) -> list[list]:
    """Write the CoreMeta4Cat sheet; returns the rows written."""
    ws = wb.create_sheet(title=REFERENCE_SHEET)
    _write_data_headers(ws)
    rows = collect_catcore_rows(schema, sv)
    for row in rows:
        _append_row(ws, row, "slot", row[3])
    _auto_width(ws)
    return rows


# ─────────────────────────────────────────────────────────────────────────────
# Data-class sheet builder (Synthesis, Characterization, Reaction, Simulation)
# ─────────────────────────────────────────────────────────────────────────────

def _class_row(schema: dict, class_name: str, domain_label: str, mro: str) -> tuple:
    class_def = schema.get("classes", {}).get(class_name) or {}
    return (snake_to_readable(class_name), "class", domain_label, mro, "", "", "", "",
            class_def.get("class_uri", "") or "", class_def.get("description", "") or "",
            class_name)


def _collect_rows(
    schema: dict,
    sv,
    class_name: str,
    parent_label: str,
    seen: set,
    rows: list,
    depth: int = 0,
) -> None:
    if class_name in seen or depth > 8:
        return
    seen = seen | {class_name}
    classes = schema.get("classes", {})

    # The class's own, inherited and mixin slots first, then the slot_usage
    # entries that narrow an inherited slot to a class range (e.g. Synthesis
    # realized_plan -> PreparationMethod).
    direct_slots = get_all_class_slots(schema, class_name)
    entries = [(name, None) for name in direct_slots]
    entries += [
        (name, synthetic)
        for name, synthetic in get_class_ranged_slot_usage(schema, class_name)
        if name not in direct_slots
    ]

    for slot_name, synthetic in entries:
        vals = (slot_row_values(sv, slot_name, class_name)
                or _raw_row_values(schema, slot_name, class_name, synthetic))
        label = snake_to_readable(slot_name)
        rows.append((label, "slot", parent_label, vals["mro"], vals["range"],
                     vals["multivalued"], vals["inlined_as_list"], vals["unit"],
                     vals["uri"], vals["description"], slot_name))

        # Expand the class the slot is declared with, and every subclass of
        # it. This keeps the sheet layout; the range column above shows the
        # effective (possibly narrowed) range.
        rng = (synthetic or get_slot_details(schema, slot_name)).get("range", "string")
        if rng in classes and not is_mixin(schema, rng):
            class_label = snake_to_readable(rng)
            rows.append(_class_row(schema, rng, label, vals["mro"]))
            _collect_rows(schema, sv, rng, class_label, seen, rows, depth + 1)
            for sub in get_subclasses(schema, rng):
                rows.append(_class_row(schema, sub, class_label, vals["mro"]))
                _collect_rows(schema, sv, sub, snake_to_readable(sub), seen | {rng}, rows, depth + 2)


def collect_sheet_rows(
    schema: dict,
    sv,
    sheet_title: str,
    class_name: str | None = None,
    slot_origin: dict | None = None,
    class_origin: dict | None = None,
) -> list[tuple[list, str, str, bool]]:
    """
    Rows of one data sheet as (values, row type, M/R/O, owned), one per
    (label, domain) pair. `owned` is False for rows inherited from a vendored
    chemdcat-ap module; ownership is only checked when an origin index is given.
    """
    if class_name is None:
        class_name = CLASS_MAP.get(sheet_title, sheet_title)
    raw_rows: list = []
    _collect_rows(schema, sv, class_name, "", set(), raw_rows)

    check_ownership = slot_origin is not None or class_origin is not None
    out: list[tuple[list, str, str, bool]] = []
    seen: set = set()
    for row in raw_rows:
        key = (row[0], row[2])  # label + domain
        if key in seen:
            continue
        seen.add(key)
        row_type, raw_name = row[1], row[10]
        origin = (slot_origin if row_type == "slot" else class_origin) or {}
        owned = (raw_name in origin) if check_ownership else True
        out.append((list(row[:10]), row_type, row[3], owned))
    return out


def build_sheet(
    wb: openpyxl.Workbook,
    schema: dict,
    sheet_title: str,
    class_name: str | None = None,
    slot_origin: dict | None = None,
    class_origin: dict | None = None,
    sv=None,
) -> list[list]:
    """Write one data sheet; returns the rows written (cell values)."""
    sv = sv if sv is not None else load_schema_view(SCHEMA_DIR)
    ws = wb.create_sheet(title=sheet_title)
    _write_data_headers(ws)

    rows = collect_sheet_rows(schema, sv, sheet_title, class_name, slot_origin, class_origin)
    for values, row_type, mro, owned in rows:
        _append_row(ws, values, row_type, mro, owned=owned)

    _auto_width(ws)
    _add_dropdowns(ws)
    return [values for values, *_ in rows]


def build_baseline_sheet(wb: openpyxl.Workbook, sheet_rows: dict[str, list[list]]) -> None:
    """Very hidden copy of every data row, used by the inbox pipeline."""
    ws = wb.create_sheet(title=BASELINE_SHEET)
    for values in baseline_values(sheet_rows):
        ws.append(values)
    ws.sheet_state = "veryHidden"


# ─────────────────────────────────────────────────────────────────────────────
# Whole workbook, rows for other scripts, stable saving
# ─────────────────────────────────────────────────────────────────────────────

def build_workbook(schema_dir: Path | str = SCHEMA_DIR, verbose: bool = False) -> openpyxl.Workbook:
    log = print if verbose else (lambda *_: None)
    if verbose:
        schema = load_merged_schema(str(schema_dir))
    else:
        with contextlib.redirect_stdout(io.StringIO()):
            schema = load_merged_schema(str(schema_dir))
    sv = load_schema_view(schema_dir)
    slot_origin, class_origin = build_origin_index(schema_dir)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    log("  Building sheet: Introduction")
    build_intro_sheet(wb)
    log("  Building sheet: Legend")
    build_legend_sheet(wb)

    log(f"  Building sheet: {REFERENCE_SHEET}")
    sheet_rows = {REFERENCE_SHEET: build_catcore_sheet(wb, schema, sv)}
    for sheet_title in DATA_SHEETS:
        log(f"  Building sheet: {sheet_title}")
        sheet_rows[sheet_title] = build_sheet(
            wb, schema, sheet_title,
            slot_origin=slot_origin, class_origin=class_origin, sv=sv,
        )

    log(f"  Building sheet: {BASELINE_SHEET} (very hidden)")
    build_baseline_sheet(wb, sheet_rows)
    return wb


def generate_rows(schema_dir: Path | str = SCHEMA_DIR) -> dict[str, list[dict]]:
    """
    {sheet: [normalised row dict]} for the CoreMeta4Cat sheet and the data
    sheets -- exactly the rows a workbook generated from schema_dir contains.
    Cached per schema state.
    """
    key = schema_fingerprint(schema_dir)
    rows = _ROWS_CACHE.get(key)
    if rows is None:
        with contextlib.redirect_stdout(io.StringIO()):
            schema = load_merged_schema(str(schema_dir))
        sv = load_schema_view(schema_dir)
        rows = {REFERENCE_SHEET: [row_from_values(v) for v in collect_catcore_rows(schema, sv)]}
        for sheet_title in DATA_SHEETS:
            rows[sheet_title] = [
                row_from_values(values)
                for values, *_ in collect_sheet_rows(schema, sv, sheet_title)
            ]
        _cache_put(_ROWS_CACHE, key, rows)
    return {sheet: [dict(r) for r in sheet_rows] for sheet, sheet_rows in rows.items()}


def _workbook_parts(data: bytes) -> dict[str, bytes]:
    """The parts of an .xlsx file, minus docProps/core.xml (creation/save time)."""
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        return {name: zf.read(name) for name in zf.namelist() if name != "docProps/core.xml"}


def save_workbook(wb: openpyxl.Workbook, output_path: Path | str) -> bool:
    """
    Save wb to output_path unless the file there already has identical
    content. Returns True if the file was written. Keeps regeneration from
    producing a "changed" binary (and an auto-PR) when only the timestamps differ.
    """
    out = Path(output_path)
    buffer = io.BytesIO()
    wb.save(buffer)
    data = buffer.getvalue()
    if out.exists():
        try:
            if _workbook_parts(out.read_bytes()) == _workbook_parts(data):
                return False
        except zipfile.BadZipFile:
            pass
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    return True


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main(schema_dir: Path | str = SCHEMA_DIR, output_path: Path | str = OUTPUT_PATH) -> None:
    print(f"\nLoading CoreMeta4Cat modules from: {schema_dir}")
    wb = build_workbook(schema_dir, verbose=True)
    if save_workbook(wb, output_path):
        print(f"\nSaved -> {output_path}")
    else:
        print(f"\nUnchanged -> {output_path} (same content, file left as is)")


if __name__ == "__main__":
    main(SCHEMA_DIR, OUTPUT_PATH)
