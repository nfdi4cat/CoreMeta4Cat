"""
schema_graph.py

Builds the class graph behind the interactive class map on the data-class
documentation pages (docs/synthesis.md, docs/reaction.md, ...) and the
overview on docs/catalysis-dataset.md.

Every class reachable from the four data classes appears exactly once, with
its fields (type, mandatory / recommended / optional, multivalued, UCUM
unit, short description) and, where a class comes in several types, the
list of those types. Drawing each class once is what keeps the class map
readable: the sunburst charts repeat a shared class (e.g. the substance
class behind used_reactant, used_solvent, generated_product, ...) under
every field that points to it.

On top of that the graph records:
  origins   -- where each data class is used from (e.g. Synthesis via
               CatalysisDataset.was_generated_by_synthesis, Reaction via
               ReactionMonitoring.evaluated_activity)
  overviews -- a reduced, CoreMeta4Cat-specific view of CatalysisDataset in
               which classes that only exist to model inheritance
               (abstract type-designator classes) and generic upstream
               classes (EvaluatedEntity) are replaced by the specific
               CoreMeta4Cat classes behind them
  pages     -- the documentation page of each class that has one

generate_schema_docs.py writes the result to docs/assets/schema_graph.json;
docs/javascripts/schema_classmap.js reads it in the browser.
"""

from __future__ import annotations

import json
import re
from collections import deque
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

from generate_schema_docs import (
    DISPLAY_NAMES,
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    get_subclasses,
    is_mixin,
)

# Colour palette per data class: Mandatory / Recommended / Optional.
# Also used by generate_charts.py for the sunburst charts.
BASE_COLORS: Dict[str, Dict[str, str]] = {
    "synthesis":        {"M": "#d73027", "R": "#f46d43", "O": "#fdae61"},
    "characterization": {"M": "#4575b4", "R": "#74add1", "O": "#abd9e9"},
    "reaction":         {"M": "#1a9850", "R": "#66bd63", "O": "#a6d96a"},
    "simulation":       {"M": "#984ea3", "R": "#b358cb", "O": "#e082ea"},
    "coremeta4cat":     {"M": "#e66101", "R": "#fdb863", "O": "#fddbc7"},
}

MAIN_CLASSES = ["Synthesis", "Characterization", "CatalyticReaction", "Simulation"]
OVERVIEW_CLASSES = ["CatalysisDataset"]

# Upstream base class of the activities that produce data. An origin owned by
# such an activity (e.g. ReactionMonitoring) is shown even when the owner comes
# from a vendored module rather than from CoreMeta4Cat itself.
DATA_GENERATING_ACTIVITY = "DataGeneratingActivity"

_MAX_DESCRIPTION = 230


def _short(text: Optional[str], limit: int = _MAX_DESCRIPTION) -> str:
    """Collapse whitespace and cut long descriptions at a sentence end."""
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    dot = cut.rfind(". ")
    return cut[:dot + 1] if dot > 80 else cut.rsplit(" ", 1)[0] + " …"


def _is_a_chain(schema: dict, class_name: str) -> List[str]:
    """class_name and its is_a ancestors, ending with the first one that is
    not part of the loaded schema (e.g. DataGeneratingActivity)."""
    classes = schema.get("classes", {})
    chain: List[str] = []
    current: Optional[str] = class_name
    while current and current not in chain:
        chain.append(current)
        current = (classes.get(current) or {}).get("is_a")
    return chain


def _role(schema: dict, class_name: str) -> Optional[str]:
    """The upstream base class a class specialises, if it lies outside the
    loaded schema -- e.g. DataGeneratingActivity for Synthesis,
    EvaluatedActivity for CatalyticReaction."""
    chain = _is_a_chain(schema, class_name)
    top = chain[-1]
    return top if len(chain) > 1 and top not in schema.get("classes", {}) else None


def _requirement(details: dict) -> str:
    if details.get("required"):
        return "M"
    if details.get("recommended"):
        return "R"
    return "O"


def _field(schema: dict, name: str, details: dict) -> dict:
    classes = schema.get("classes", {})
    rng = details.get("range") or "string"
    if rng in classes and not is_mixin(schema, rng):
        kind = "class"
    elif rng in (schema.get("enums") or {}):
        kind = "enum"
    else:
        kind = "primitive"
    return {
        "name": name,
        "range": rng,
        "kind": kind,
        "requirement": _requirement(details),
        "multivalued": bool(details.get("multivalued")),
        "unit": (details.get("unit") or {}).get("ucum_code", ""),
        "description": _short(details.get("description")),
    }


def class_fields(schema: dict, class_name: str) -> List[dict]:
    """All fields of a class, with slot_usage overrides applied.

    Covers inherited and mixin slots, class-ranged slot_usage entries and
    LinkML `attributes:` (inline slots, e.g. QuantitativeRange's min_value
    and max_value), including attributes inherited via is_a.
    """
    class_def = schema.get("classes", {}).get(class_name) or {}
    usage = class_def.get("slot_usage") or {}
    direct = get_all_class_slots(schema, class_name)

    fields = []
    for name in direct:
        override = {k: v for k, v in (usage.get(name) or {}).items() if v is not None}
        fields.append(_field(schema, name, {**get_slot_details(schema, name), **override}))
    for name, synthetic in get_class_ranged_slot_usage(schema, class_name, exclude=set(direct)):
        fields.append(_field(schema, name, synthetic))

    seen = {f["name"] for f in fields}
    for ancestor in _is_a_chain(schema, class_name):
        attributes = (schema["classes"].get(ancestor) or {}).get("attributes") or {}
        for name, details in attributes.items():
            if name not in seen:
                fields.append(_field(schema, name, details or {}))
                seen.add(name)
    return fields


def _class_kind(schema: dict, class_name: str, fields: List[dict], options: List[str]) -> str:
    """How the class map shows a class.

    range    -- min / max / unit (QuantitativeRange)
    choice   -- comes in several types (has subclasses)
    struct   -- a record with its own fields
    quantity -- value + unit (QuantitativeAttribute subclasses)
    term     -- a vocabulary term (QualitativeAttribute subclasses)
    ref      -- anything else (external class without local fields)
    """
    names = {f["name"] for f in fields}
    if {"min_value", "max_value"} <= names:
        return "range"
    if options:
        return "choice"
    if fields:
        return "struct"
    chain = _is_a_chain(schema, class_name)
    if "QuantitativeAttribute" in chain:
        return "quantity"
    if "QualitativeAttribute" in chain:
        return "term"
    return "ref"


def _type_designators(schema: dict) -> Set[str]:
    return {name for name, d in (schema.get("slots") or {}).items() if (d or {}).get("designates_type")}


def is_stand_in(schema: dict, class_name: str) -> bool:
    """True for an abstract class that adds nothing but a type designator:
    it only exists so that a slot can accept any of its subclasses, and
    readers are better served by seeing those subclasses directly."""
    class_def = schema.get("classes", {}).get(class_name) or {}
    if not class_def.get("abstract") or not get_subclasses(schema, class_name):
        return False
    own = {f["name"] for f in class_fields(schema, class_name)}
    return own <= _type_designators(schema)


def specific_classes(schema: dict, class_name: str, editable: Optional[Set[str]] = None) -> List[str]:
    """The CoreMeta4Cat classes a reader should see for a range.

    A stand-in class is replaced by its direct subclasses; a generic class
    from outside the loaded schema (e.g. EvaluatedEntity) by the CoreMeta4Cat
    classes that specialise it; anything else stays as it is.
    """
    classes = schema.get("classes", {})
    if class_name in classes:
        if is_stand_in(schema, class_name):
            return [c for c, d in classes.items()
                    if (d or {}).get("is_a") == class_name and not is_mixin(schema, c)]
        return [class_name]
    return [c for c in classes
            if (editable is None or c in editable)
            and c != class_name and class_name in _is_a_chain(schema, c)]


def _origins(schema: dict, roots: Iterable[str], editable: Optional[Set[str]]) -> Dict[str, List[dict]]:
    """For each root: the fields elsewhere in the schema that point at it or
    at one of its ancestors, e.g. CatalysisDataset.was_generated_by_synthesis
    for Synthesis. Owners must be CoreMeta4Cat classes or data-generating
    activities, which keeps generic upstream datasets out."""
    classes = schema.get("classes", {})
    result: Dict[str, List[dict]] = {}
    for root in roots:
        chain = _is_a_chain(schema, root)
        found = []
        for owner in sorted(classes):
            if owner in chain:
                continue
            owner_chain = _is_a_chain(schema, owner)
            if editable is not None and owner not in editable and DATA_GENERATING_ACTIVITY not in owner_chain:
                continue
            for f in class_fields(schema, owner):
                if f["range"] not in chain:
                    continue
                via = f["range"]
                found.append({
                    "class": owner,
                    "label": DISPLAY_NAMES.get(owner, owner),
                    "field": f["name"],
                    # name the class the field actually expects, unless that is
                    # the root itself or a stand-in nobody needs to know about
                    "as": None if via == root or is_stand_in(schema, via) else via,
                    "description": _short((classes[owner] or {}).get("description"), 180),
                })
        found.sort(key=lambda o: (DATA_GENERATING_ACTIVITY not in _is_a_chain(schema, o["class"]), o["class"]))
        result[root] = found
    return result


def _overview(schema: dict, class_name: str, editable: Optional[Set[str]]) -> dict:
    """A CoreMeta4Cat-specific view of a class: only the fields it declares
    itself (its slot_usage and its own slots), with every range replaced by
    the specific CoreMeta4Cat classes behind it. Fields inherited from generic
    upstream classes (id, title, ... from dcat:Dataset) are left out. A slot
    declared as a specialisation of another one (is_a, e.g.
    was_generated_by_synthesis of was_generated_by) follows its parent."""
    classes = schema.get("classes", {})
    enums = schema.get("enums") or {}
    class_def = classes.get(class_name) or {}
    declared = {slot: {} for slot in class_def.get("slots") or [] if slot not in (class_def.get("slot_usage") or {})}
    entries = list((class_def.get("slot_usage") or {}).items())
    for slot, usage in declared.items():
        parent = get_slot_details(schema, slot).get("is_a")
        after = [i for i, (name, _) in enumerate(entries) if name == parent or get_slot_details(schema, name).get("is_a") == parent]
        entries.insert(after[-1] + 1 if parent and after else len(entries), (slot, usage))
    fields = []
    for slot, usage in entries:
        usage = usage or {}
        details = {**get_slot_details(schema, slot), **{k: v for k, v in usage.items() if v is not None}}
        bound = [b.get("range") for b in (usage.get("bindings") or []) if (b or {}).get("range")]
        if bound and bound[0] in enums:
            rng, kind, targets = bound[0], "enum", []
        elif details.get("range"):
            rng, kind = details["range"], "class"
            targets = specific_classes(schema, rng, editable)
        else:
            continue
        fields.append({
            "name": slot,
            "range": rng,
            "kind": kind,
            "requirement": _requirement(details),
            "multivalued": bool(details.get("multivalued")),
            "unit": "",
            "description": _short(details.get("description")),
            "targets": targets,
        })
    return {
        "label": DISPLAY_NAMES.get(class_name, class_name),
        "role": _role(schema, class_name),
        "description": _short(class_def.get("description")),
        "fields": fields,
    }


def build_schema_graph(schema: dict, roots: Optional[List[str]] = None,
                       pages: Optional[Dict[str, str]] = None,
                       editable: Optional[Set[str]] = None) -> dict:
    """Return the JSON-ready class graph reachable from `roots`.

    `pages` maps class names to their documentation page (e.g.
    "synthesis.md"); `editable` is the set of classes defined in the
    CoreMeta4Cat modules (see build_origin_index), used to prefer
    CoreMeta4Cat classes over generic upstream ones.
    """
    roots = roots or MAIN_CLASSES
    classes = schema.get("classes", {})
    overviews = {name: _overview(schema, name, editable) for name in OVERVIEW_CLASSES if name in classes}

    graph: Dict[str, dict] = {}
    queue = deque(list(roots) + [t for o in overviews.values() for f in o["fields"] for t in f["targets"]])
    while queue:
        name = queue.popleft()
        if name in graph or name not in classes:
            continue
        fields = class_fields(schema, name)
        options = [o for o in get_subclasses(schema, name) if o in classes]
        class_def = classes[name] or {}
        graph[name] = {
            "label": DISPLAY_NAMES.get(name, name),
            "is_a": class_def.get("is_a"),
            "role": _role(schema, name),
            "kind": _class_kind(schema, name, fields, options),
            "description": _short(class_def.get("description")),
            "fields": fields,
            "options": options,
        }
        queue.extend(f["range"] for f in fields if f["kind"] == "class")
        queue.extend(options)

    # A class whose types add no fields (e.g. Atmosphere) is just a term.
    for entry in graph.values():
        if (entry["kind"] == "choice" and not entry["fields"]
                and not any(graph.get(o, {}).get("fields") for o in entry["options"])):
            entry["kind"] = "term"

    enums = {
        name: list(((enum or {}).get("permissible_values") or {}).keys())
        for name, enum in (schema.get("enums") or {}).items()
    }
    colors = {
        name: BASE_COLORS.get(DISPLAY_NAMES.get(name, name).lower(), BASE_COLORS["coremeta4cat"])
        for name in list(roots) + list(overviews)
    }
    page_urls = {
        name: (page[:-3] if page.endswith(".md") else page) + "/"
        for name, page in (pages or {}).items()
    }
    return {
        "roots": list(roots),
        "colors": colors,
        "pages": page_urls,
        "origins": _origins(schema, roots, editable),
        "overviews": overviews,
        "classes": {name: graph[name] for name in sorted(graph)},
        "enums": {name: enums[name] for name in sorted(enums)},
    }


def write_schema_graph(schema: dict, output_file: Path,
                       pages: Optional[Dict[str, str]] = None,
                       editable: Optional[Set[str]] = None) -> None:
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    graph = build_schema_graph(schema, pages=pages, editable=editable)
    output_file.write_text(json.dumps(graph, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  OK {output_file} ({len(graph['classes'])} classes)")
