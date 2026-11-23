"""
generate_usage_patterns.py

Builds the "Usage patterns" documentation page from small excerpts of the
community datasets in tests/data/valid/.

Each pattern is defined in scripts/usage_patterns.yaml: which dataset file it
comes from, which object to take (a path such as
``was_generated_by[id=coremeta4cat:CHAR_b74m-m6rp_TCD]``), and which fields
to keep. For every pattern the script

  1. cuts the excerpt out of the dataset record,
  2. validates it against its class (same validator as ``just test``) and
     loads it into the Python datamodel -- a pattern that no longer fits the
     schema stops the build,
  3. renders it three ways: a Mermaid graph, the YAML excerpt and RDF/Turtle,
  4. writes docs/working-with-data/usage-patterns.md and downloadable copies
     to docs/assets/patterns/.

Keep rules (``keep:`` in the spec):
  key: true            keep the value as is
  key: 3               keep the first 3 items of a list
  key: {a: true, ...}  keep only these sub-keys (applied to every item of a list)
     _limit: n         ... of the first n items
     _ids: [...]       ... of the items with these ids, in this order
     _all: true        ... keep all sub-keys, the listed ones get their own rule

Run:
    just gen-usage-patterns
  or directly:
    uv run python scripts/generate_usage_patterns.py
"""

from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

from coremeta4cat.datamodel import coremeta4cat as datamodel

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = REPO_ROOT / "scripts" / "usage_patterns.yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "coremeta4cat" / "schema" / "coremeta4cat.yaml"
PAGE_PATH = REPO_ROOT / "docs" / "working-with-data" / "usage-patterns.md"
ASSET_DIR = REPO_ROOT / "docs" / "assets" / "patterns"
SLOT_DOCS = REPO_ROOT / "docs" / "elements" / "slots"

DESIGNATORS = ("activity_designator", "plan_designator", "reactor_designator")
# Shown in the node label, not as separate leaves of the graph.
LABEL_KEYS = {"id", "title", "description", *DESIGNATORS}

# Node kinds: (ancestor class that decides the kind, kind name)
KIND_ORDER = [
    ("Dataset", "dataset"),
    ("Distribution", "dataset"),
    ("Activity", "activity"),
    ("Plan", "plan"),
    ("AgenticEntity", "agent"),
    ("Agent", "agent"),
    ("QuantitativeAttribute", "quantity"),
    ("QuantitativeRange", "quantity"),
    ("QualitativeAttribute", "attribute"),
    ("Concept", "term"),
    ("DefinedTerm", "term"),
    ("Entity", "entity"),
]
STYLES = {
    "dataset": ("#cfe9ef", "#00838f", "Dataset"),
    "activity": ("#fde2c4", "#c26b00", "Activity (synthesis, characterization, simulation, reaction)"),
    "plan": ("#e3dcf7", "#5b3fb5", "Plan (method, technique, protocol)"),
    "entity": ("#d4ecd6", "#2e7d32", "Entity (sample, catalyst, precursor, chemical)"),
    "agent": ("#d5e6f7", "#1565c0", "Agent (instrument, reactor)"),
    "quantity": ("#fff4c2", "#9a7d00", "Quantity (value or range with unit)"),
    "attribute": ("#f3e5f5", "#8e24aa", "Qualitative value or calculated property"),
    "term": ("#fce4ec", "#ad1457", "Vocabulary term"),
    "literal": ("#eeeeee", "#757575", "Literal value"),
    "other": ("#ffffff", "#757575", "Other object"),
}


# ---------------------------------------------------------------- excerpts

_SEGMENT = re.compile(r"^(?P<key>[^\[\]]+)(\[(?P<sel>[^\]]+)\])?$")


def select(data, path: str | None):
    """Follow a path like ``was_generated_by[id=X]/realized_plan`` or ``is_about_activity[0]``."""
    if not path:
        return data
    for segment in path.split("/"):
        match = _SEGMENT.match(segment)
        if not match:
            raise ValueError(f"bad path segment {segment!r}")
        data = data[match["key"]]
        sel = match["sel"]
        if sel is None:
            continue
        if sel.isdigit():
            data = data[int(sel)]
        else:
            field, value = sel.split("=", 1)
            hits = [item for item in data if str(item.get(field)) == value]
            if len(hits) != 1:
                raise ValueError(f"{segment!r} matched {len(hits)} items")
            data = hits[0]
    return data


def prune(value, rule):
    if rule is True:
        return value
    if isinstance(rule, int) and not isinstance(rule, bool):
        return value[:rule] if isinstance(value, list) else value
    if isinstance(rule, dict):
        if isinstance(value, list):
            items = value
            if "_ids" in rule:
                by_id = {item.get("id"): item for item in items}
                items = [by_id[i] for i in rule["_ids"]]
            if "_limit" in rule:
                items = items[: rule["_limit"]]
            return [prune(item, rule) for item in items]
        if isinstance(value, dict):
            keep_all = rule.get("_all", False)
            return {
                key: prune(val, rule.get(key, True))
                for key, val in value.items()
                if keep_all or key in rule
            }
        return value
    raise ValueError(f"bad keep rule {rule!r}")


# ---------------------------------------------------------------- schema helpers


class Schema:
    def __init__(self, path: Path):
        self.view = SchemaView(str(path))
        self.uri_to_class = {}
        for name, cls in self.view.all_classes().items():
            if cls.class_uri and not cls.abstract:
                self.uri_to_class.setdefault(cls.class_uri, name)

    @lru_cache(maxsize=None)
    def slot_range(self, slot: str, cls: str | None) -> str | None:
        try:
            return self.view.induced_slot(slot, cls).range if cls else self.view.get_slot(slot).range
        except (ValueError, AttributeError):
            slot_def = self.view.get_slot(slot)
            return slot_def.range if slot_def else None

    @lru_cache(maxsize=None)
    def kind(self, cls: str | None) -> str:
        if not cls or cls not in self.view.all_classes():
            return "other"
        ancestors = set(self.view.class_ancestors(cls))
        for ancestor, kind in KIND_ORDER:
            if ancestor in ancestors:
                return kind
        return "other"

    def concrete(self, declared: str | None, obj: dict) -> str | None:
        if "activity_designator" in obj:
            return obj["activity_designator"]
        for slot in ("plan_designator", "reactor_designator"):
            if slot in obj:
                return self.uri_to_class.get(obj[slot], declared)
        return declared


# ---------------------------------------------------------------- graph


def _text(value, limit: int = 42) -> str:
    text = " ".join(str(value).split())
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return text.replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")


def _short_iri(iri: str) -> str:
    return str(iri).rstrip("/").rsplit("/", 1)[-1]


def _first(value):
    return value[0] if isinstance(value, list) and value else value


class Graph:
    def __init__(self, schema: Schema):
        self.schema = schema
        self.nodes: dict[str, tuple[str, str]] = {}  # key -> (label, kind)
        self.edges: list[tuple[str, str, str]] = []
        self.counter = 0

    def _new(self, key: str | None, label: str, kind: str) -> str:
        if key is not None and key in self.nodes:
            return self.nodes[key][2]
        self.counter += 1
        node = f"n{self.counter}"
        self.nodes[key or node] = (label, kind, node)
        return node

    def add_object(self, obj: dict, cls: str | None) -> str:
        cls = self.schema.concrete(cls, obj)
        kind = self.schema.kind(cls)
        if kind == "quantity":
            if "min_value" in obj or "max_value" in obj:
                magnitude = f"{obj.get('min_value')}–{obj.get('max_value')}"
            else:
                magnitude = str(obj.get("value", ""))
            unit = _short_iri(obj["unit"]) if obj.get("unit") else ""
            qkind = _short_iri(obj["has_quantity_type"]) if obj.get("has_quantity_type") else cls
            label = f"{_text(magnitude + ' ' + unit)}<br/>«{qkind}»"
            node = self._new(None, label, kind)
            return node
        if kind == "attribute" and "value" in obj:
            node = self._new(None, f"{_text(obj['value'])}<br/>«{cls}»", kind)
            return node
        if kind == "term" or (cls in (None, "Concept", "DefinedTerm") and set(obj) <= {"id", "title"}):
            label = f"{_text(obj.get('title', ''))}<br/>{_text(obj.get('id', ''))}"
            return self._new(f"term:{obj.get('id')}", label, "term")
        title = (_first(obj.get("title")) or _first(obj.get("name")) or obj.get("notation")
                 or obj.get("id") or cls or "object")
        label = f"{_text(title)}<br/>«{cls or 'object'}»"
        node = self._new(obj.get("id"), label, kind)
        for slot, value in obj.items():
            if slot in LABEL_KEYS or (slot == "name" and "title" not in obj):
                continue
            target_cls = self.schema.slot_range(slot, cls)
            for item in value if isinstance(value, list) else [value]:
                if isinstance(item, dict):
                    child = self.add_object(item, target_cls)
                else:
                    child = self._new(None, f"“{_text(item)}”", "literal")
                self.edges.append((node, slot, child))
        return node

    def mermaid(self) -> str:
        lines = ["flowchart LR"]
        for label, kind, node in self.nodes.values():
            shape = ('(["', '"])') if kind == "literal" else ('["', '"]')
            lines.append(f"    {node}{shape[0]}{label}{shape[1]}")
        for source, slot, target in self.edges:
            lines.append(f"    {source} -->|{slot}| {target}")
        for kind, (fill, stroke, _) in STYLES.items():
            lines.append(f"    classDef {kind} fill:{fill},stroke:{stroke},color:#222")
        by_kind: dict[str, list[str]] = {}
        for _, kind, node in self.nodes.values():
            by_kind.setdefault(kind, []).append(node)
        for kind, nodes in by_kind.items():
            lines.append(f"    class {','.join(nodes)} {kind}")
        return "\n".join(lines)


# ---------------------------------------------------------------- build


class SchemaDirValidator:
    """JSON Schema validator as used by `just test`.

    The schema's imports are resolved relative to the working directory, so
    validation runs from inside the schema directory.
    """

    def __init__(self):
        self.validator = self._in_schema_dir(
            lambda: Validator(SCHEMA_PATH.name, validation_plugins=[JsonschemaValidationPlugin(closed=True)])
        )

    @staticmethod
    def _in_schema_dir(call):
        cwd = Path.cwd()
        os.chdir(SCHEMA_PATH.parent)
        try:
            return call()
        finally:
            os.chdir(cwd)

    def errors(self, instance: dict, cls: str) -> list[str]:
        return self._in_schema_dir(lambda: [r.message for r in self.validator.validate(instance, cls).results])


def build_pattern(pattern: dict, validator: SchemaDirValidator) -> dict:
    source = REPO_ROOT / pattern["source"]
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    excerpt = prune(select(data, pattern.get("select")), pattern["keep"])
    cls = pattern["class"]
    errors = validator.errors(excerpt, cls)
    if errors:
        raise ValueError(f"pattern {pattern['id']} is not valid as {cls}: {errors[0][-300:]}")
    obj = yaml_loader.load(excerpt, target_class=getattr(datamodel, cls))
    return {"excerpt": excerpt, "object": obj}


def slot_link(slot: str) -> str:
    if (SLOT_DOCS / f"{slot}.md").exists():
        return f"[`{slot}`](../elements/slots/{slot}.md)"
    return f"`{slot}`"


# Generic sub-fields of quantities and identifiers, left out of the "Fields used" line.
GENERIC_SLOTS = {"id", "title", "description", "value", "min_value", "max_value", "unit",
                 "has_quantity_type", "notation"}


def used_slots(value, found=None) -> list[str]:
    found = [] if found is None else found
    if isinstance(value, dict):
        for key, val in value.items():
            if key not in GENERIC_SLOTS and key not in found:
                found.append(key)
            used_slots(val, found)
    elif isinstance(value, list):
        for item in value:
            used_slots(item, found)
    return found


def indent(text: str, spaces: int = 8) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else "" for line in text.splitlines())


def render(spec: dict, schema: Schema, validator: SchemaDirValidator) -> str:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    out = [
        "---",
        f"title: {spec['title']}",
        f"description: {spec['description']}",
        "---",
        "",
        "<!-- Generated by scripts/generate_usage_patterns.py from scripts/usage_patterns.yaml. Do not edit by hand. -->",
        "",
        f"# {spec['title']}",
        "",
        spec["intro"].strip(),
        "",
        "**Legend of the graphs:**",
        "",
        " ".join(
            f'<span style="background:{fill};border:1px solid {stroke};border-radius:4px;'
            f'padding:1px 6px;margin:2px;display:inline-block;color:#222">{name}</span>'
            for kind, (fill, stroke, name) in STYLES.items()
            if kind != "other"
        ),
        "",
        "Boxes show an object's title (or id) and, in «guillemets», its class. Arrows are labelled "
        "with the field that links two objects. Descriptions are left out of the graph; the YAML tab "
        "shows the full excerpt.",
        "",
    ]
    number = 0
    for section in spec["sections"]:
        out += ["---", "", f"## {section['title']}", ""]
        if section.get("intro"):
            out += [section["intro"].strip(), ""]
        for pattern in section["patterns"]:
            number += 1
            built = build_pattern(pattern, validator)
            graph = Graph(schema)
            graph.add_object(built["excerpt"], pattern["class"])
            yaml_text = yaml.safe_dump(built["excerpt"], sort_keys=False, allow_unicode=True, width=100).rstrip()
            ttl_text = rdflib_dumper.dumps(built["object"], schemaview=schema.view).rstrip()
            stem = f"pattern-{number:02d}-{pattern['id']}"
            (ASSET_DIR / f"{stem}.yaml").write_text(yaml_text + "\n", encoding="utf-8", newline="\n")
            (ASSET_DIR / f"{stem}.ttl").write_text(ttl_text + "\n", encoding="utf-8", newline="\n")

            out += [f"### Pattern {number} – {pattern['title']} {{ #{pattern['id']} }}", ""]
            out += [f"**Purpose:** {pattern['purpose'].strip()}", ""]
            out += [f"**Example use case:** {pattern['use_case'].strip()}", ""]
            if pattern.get("notes"):
                out += ["**Notes:**", ""] + [f"- {note.strip()}" for note in pattern["notes"]] + [""]
            out += ["**Fields used:** " + ", ".join(slot_link(s) for s in used_slots(built["excerpt"])), ""]
            out += [
                '=== "Graph"',
                "",
                "    ```mermaid",
                indent(graph.mermaid(), 4),
                "    ```",
                "",
                '=== "YAML"',
                "",
                "    ```yaml",
                indent(yaml_text, 4),
                "    ```",
                "",
                '=== "RDF (Turtle)"',
                "",
                "    ```turtle",
                indent(ttl_text, 4),
                "    ```",
                "",
                f"Excerpt of [{pattern['dataset_label']}](community-datasets.md#{pattern['dataset']}) "
                f"as `{pattern['class']}`, validated against the current schema. "
                f"Download: [YAML](../assets/patterns/{stem}.yaml) · [Turtle](../assets/patterns/{stem}.ttl)",
                "",
            ]
            print(f"  OK pattern {number}: {pattern['id']} ({pattern['class']})")
    return "\n".join(out)


def main() -> None:
    spec = yaml.safe_load(SPEC_PATH.read_text(encoding="utf-8"))
    schema = Schema(SCHEMA_PATH)
    page = render(spec, schema, SchemaDirValidator())
    PAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    PAGE_PATH.write_text(page, encoding="utf-8", newline="\n")
    print(f"\nWrote {PAGE_PATH.relative_to(REPO_ROOT)} and {ASSET_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
