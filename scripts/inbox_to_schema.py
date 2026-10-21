"""
inbox_to_schema.py

Converts a modified CoreMeta4Cat vocabulary workbook from the inbox/ folder
into changes in the LinkML YAML schema files.

Supported operations (all per-row in the Excel):
  • Modify existing slots  — M/R/O, description, URI, range, multivalued,
                             inlined_as_list, unit
  • Modify existing classes — description, URI
  • Add new slots          — derived snake_case name from label; added to the
                             owning class's YAML module and global slots: dict
  • Add new classes        — derived PascalCase name; added as a subclass of
                             the class indicated by the domain column
  • Delete slots/classes   — a slot/class absent from the Excel but present in
                             the schema is flagged and removed

All errors and warnings are printed as Markdown, suitable for pasting directly
into a GitHub PR comment.

Usage:
    just inbox-to-schema
  or directly:
    uv run python scripts/inbox_to_schema.py [path/to/inbox.xlsx]

Exit codes:
  0  All changes applied cleanly, no warnings
  1  Fatal error (workbook unreadable, schema unloadable)
  2  Changes applied but warnings require human review
  3  Errors found — nothing was written; fix the workbook and re-submit
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import pandas as pd
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString

_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from generate_schema_docs import (  # noqa: E402
    EDITABLE_MODULE_FILES,
    build_origin_index,
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    get_subclasses,
    load_merged_schema,
    snake_to_readable,
)

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

SCHEMA_DIR    = _ROOT / "src" / "coremeta4cat" / "schema"
DEFAULT_INBOX = _ROOT / "inbox" / "coremeta4cat_vocabulary.xlsx"

# Sheet title (Excel) → LinkML class name in the schema
CLASS_MAP: dict[str, str] = {
    "Synthesis":        "Synthesis",
    "Characterization": "Characterization",
    "Reaction":         "CatalyticReaction",
    "Simulation":       "Simulation",
}

# The set of coremeta4cat-authored (editable) modules is the single canonical
# EDITABLE_MODULE_FILES list from generate_schema_docs.py (imported above) —
# this is also what build_origin_index() scans, so "editable via the inbox
# workflow" always means "defined in one of these files."
#
# New top-level slots/classes with no other owning module land here by default
# (the top-level aggregator module — deliberately NOT EDITABLE_MODULE_FILES[-1],
# since that list is ordered for schema-merge precedence, not for this purpose).
DEFAULT_NEW_ELEMENT_FILE = "coremeta4cat.yaml"

# Primitive LinkML types that are valid in the range column
PRIMITIVE_TYPES: frozenset[str] = frozenset({
    "string", "integer", "float", "boolean", "uri", "uriorcurie",
    "date", "datetime", "time", "decimal", "double", "Any",
})

# The schema's default_range (coremeta4cat.yaml / coremeta4cat_common.yaml).
# A slot with no explicit `range` key is equivalent to one with `range: string`,
# so the two must be treated as equal when diffing against the Excel (which always
# emits a range value via schema_to_excel).
DEFAULT_RANGE = "string"

# ─────────────────────────────────────────────────────────────────────────────
# Diagnostic / reporting system
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class Diagnostic:
    level:   Literal["error", "warning", "info"]
    sheet:   str
    context: str   # what we were looking at (slot name, class name, …)
    message: str   # one-line summary
    hint:    str = ""  # what the researcher should do to fix it


class Reporter:
    """Collects diagnostics and formats them as Markdown for GitHub PR comments."""

    def __init__(self) -> None:
        self._diags:   list[Diagnostic] = []
        self._applied: list[str] = []

    # ── record ─────────────────────────────────────────────────────────────

    def error(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("error", sheet, context, message, hint))

    def warning(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("warning", sheet, context, message, hint))

    def info(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("info", sheet, context, message, hint))

    def applied(self, description: str) -> None:
        self._applied.append(description)

    # ── query ──────────────────────────────────────────────────────────────

    @property
    def has_errors(self) -> bool:
        return any(d.level == "error" for d in self._diags)

    @property
    def has_warnings(self) -> bool:
        return any(d.level == "warning" for d in self._diags)

    # ── markdown output ────────────────────────────────────────────────────

    def to_markdown(self) -> str:
        lines: list[str] = [
            "## 📋 Inbox vocabulary — processing report",
            "",
        ]

        if self._applied:
            lines += ["### ✅ Changes applied", ""]
            for desc in self._applied:
                lines.append(f"- {desc}")
            lines.append("")

        warnings = [d for d in self._diags if d.level == "warning"]
        if warnings:
            lines += [
                "### ⚠️ Warnings — please review",
                "",
                "The following items were applied but require maintainer review "
                "before the PR is merged:",
                "",
            ]
            for d in warnings:
                lines.append(f"**[{d.sheet}] {d.context}**: {d.message}")
                if d.hint:
                    lines.append(f"  > 💡 *{d.hint}*")
                lines.append("")

        errors = [d for d in self._diags if d.level == "error"]
        if errors:
            lines += [
                "### ❌ Errors — must be fixed before this PR can be merged",
                "",
                "No changes were written to the schema. "
                "Fix the issues below, update the workbook, and push again.",
                "",
            ]
            for d in errors:
                lines.append(f"**[{d.sheet}] {d.context}**: {d.message}")
                if d.hint:
                    lines.append(f"  > 💡 *{d.hint}*")
                lines.append("")

        if not self._applied and not warnings and not errors:
            lines += [
                "✅ The workbook is fully aligned with the schema — "
                "no changes were needed.",
                "",
            ]

        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# YAML round-trip setup
# ─────────────────────────────────────────────────────────────────────────────


def _make_yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.width = 4096
    y.best_sequence_indent = 2
    y.best_map_flow_style = False
    return y


# ─────────────────────────────────────────────────────────────────────────────
# Schema index builders
# ─────────────────────────────────────────────────────────────────────────────

# build_origin_index() now lives in generate_schema_docs.py (imported above)
# so schema_to_excel.py can share the exact same editable/vendored predicate
# for rendering read-only rows.


def build_label_index(schema: dict) -> tuple[dict[str, str], dict[str, str]]:
    """
    Return (label_to_slot, label_to_class): inverse of snake_to_readable for
    every slot and class defined in the merged schema.

    label_to_slot covers:
      • globally-defined slots (schema["slots"])
      • slots referenced only via class slot_usage blocks (e.g. had_input_entity,
        realized_plan) that are not in the global slots dict but appear in the
        Excel because _collect_rows uses get_class_ranged_slot_usage.
    """
    label_to_slot:  dict[str, str] = {}
    label_to_class: dict[str, str] = {}

    # 1. Global slots
    for name in schema.get("slots", {}):
        label_to_slot[snake_to_readable(name)] = name

    # 2. Slot-usage-only slots: referenced in class slot_usage but not globally
    #    defined (e.g. had_input_entity in Synthesis.slot_usage).  These are
    #    rendered by schema_to_excel as top-level slot rows with an empty domain
    #    and must be recognised as existing, not new.
    for class_def in schema.get("classes", {}).values():
        for slot_name in (class_def.get("slot_usage") or {}):
            label = snake_to_readable(slot_name)
            if label not in label_to_slot:
                label_to_slot[label] = slot_name

    for name in schema.get("classes", {}):
        label_to_class[snake_to_readable(name)] = name

    return label_to_slot, label_to_class


# ─────────────────────────────────────────────────────────────────────────────
# Excel parsing helpers
# ─────────────────────────────────────────────────────────────────────────────


def _str(val: Any) -> str:
    """Coerce a cell value to a stripped string; treats NaN/None as ''."""
    if val is None:
        return ""
    s = str(val).strip()
    return "" if s.lower() in ("nan", "none", "nat") else s


def _normalise_bool(val: Any) -> str:
    """Return 'yes' if the cell indicates True, else ''."""
    s = _str(val).lower()
    return "yes" if s in ("yes", "y", "true", "1", "x") else ""


def _mro_normalise(val: Any) -> str:
    """Return 'M', 'R', 'O', or the raw upper-cased value for unknowns."""
    s = _str(val).upper()
    if s in ("M", "MANDATORY"):
        return "M"
    if s in ("R", "RECOMMENDED"):
        return "R"
    if s in ("O", "OPTIONAL"):
        return "O"
    return s  # caller detects invalids


def _label_to_slot_name(label: str) -> str:
    """Derive a snake_case slot name from a human-readable label."""
    return re.sub(r"[^a-z0-9]+", "_", label.strip().lower()).strip("_")


def _label_to_class_name(label: str) -> str:
    """Derive a PascalCase class name from a human-readable label."""
    if " " not in label and label[:1].isupper():
        return label.strip()   # already PascalCase
    return "".join(word.capitalize() for word in label.strip().split())


def _collect_pending_class_names(rows: list[dict], label_to_class: dict[str, str]) -> set[str]:
    """
    Pre-scan one sheet's rows for class-type rows that don't yet exist in the
    schema, i.e. classes proposed as new in this same submission. Returns
    their derived PascalCase names.

    A larger submission commonly adds a new slot AND the new class it points
    to (or a new class AND its new parent class) in the same batch. Without
    this pre-scan, validating each row only against the schema as it exists
    *before* the batch means such forward references always fail, regardless
    of row order. Treating these pending names as valid supports reviewing
    and applying the whole multi-part change together.
    """
    pending: set[str] = set()
    for row in rows:
        if row["type"] != "class":
            continue
        label = row["label"]
        if label_to_class.get(label) is None:
            pending.add(_label_to_class_name(label))
    return pending


# ─────────────────────────────────────────────────────────────────────────────
# Workbook loading + structural validation
# ─────────────────────────────────────────────────────────────────────────────

# Canonical column name → accepted aliases (all lower-case)
_COL_ALIASES: dict[str, list[str]] = {
    "label":           ["label"],
    "type":            ["type"],
    "domain":          ["domain"],
    "M / R / O":       ["m / r / o", "m/r/o", "mro", "mandatory/recommended/optional"],
    "range":           ["range"],
    "multivalued":     ["multivalued"],
    "inlined as list": ["inlined as list", "inlined_as_list"],
    "unit":            ["unit"],
    "uri":             ["uri"],
    "description":     ["description"],
}

# Columns that must be present (the three new ones are optional for back-compat)
_REQUIRED_COLS = {"label", "type", "domain", "M / R / O", "range", "uri", "description"}
_OPTIONAL_COLS = {"multivalued", "inlined as list", "unit"}


def validate_structure(
    workbook_path: Path,
    reporter: Reporter,
) -> dict[str, pd.DataFrame] | None:
    """
    Load and structurally validate the workbook.
    Returns a dict {sheet_title: DataFrame} or None on fatal error.
    """
    try:
        raw: dict[str, pd.DataFrame] = pd.read_excel(
            str(workbook_path), sheet_name=None, dtype=str
        )
    except Exception as exc:  # noqa: BLE001
        reporter.error(
            "workbook", workbook_path.name,
            f"Could not read the workbook: {exc}",
            hint="Make sure the file is a valid .xlsx and is not open in Excel.",
        )
        return None

    # All expected data sheets must be present
    missing = [s for s in CLASS_MAP if s not in raw]
    if missing:
        for s in missing:
            reporter.error(
                "workbook", f"sheet '{s}'",
                f"Required sheet **{s}** is missing.",
                hint="Re-download the vocabulary template from docs/assets/ and "
                     "fill it in rather than creating a new workbook.",
            )
        return None

    sheets: dict[str, pd.DataFrame] = {}
    ok = True

    for sheet_title in CLASS_MAP:
        df = raw[sheet_title].copy()
        df.columns = [str(c).strip() for c in df.columns]

        # Resolve actual column names to canonical names (case-insensitive)
        resolved: dict[str, str] = {}  # canonical → actual column name in df
        for canonical, aliases in _COL_ALIASES.items():
            found = next(
                (c for c in df.columns if c.strip().lower() in aliases),
                None,
            )
            if found:
                resolved[canonical] = found

        missing_required = [c for c in _REQUIRED_COLS if c not in resolved]
        if missing_required:
            reporter.error(
                sheet_title, "column check",
                f"Missing required column(s): {', '.join(missing_required)}.",
                hint="Re-download the vocabulary template from docs/assets/ and "
                     "make sure you have not deleted or renamed any column headers.",
            )
            ok = False
            continue

        # Rename to canonical names
        df = df.rename(columns={v: k for k, v in resolved.items()})

        # Add missing optional columns as empty
        for col in _OPTIONAL_COLS:
            if col not in df.columns:
                df[col] = ""

        df = df.dropna(how="all")
        sheets[sheet_title] = df

    return sheets if ok else None


def parse_excel(
    sheets: dict[str, pd.DataFrame],
) -> dict[str, list[dict[str, Any]]]:
    """Normalise validated DataFrames into typed row dicts."""
    result: dict[str, list[dict[str, Any]]] = {}
    for sheet_title, df in sheets.items():
        rows: list[dict[str, Any]] = []
        for _, raw in df.iterrows():
            label = _str(raw.get("label", ""))
            if not label:
                continue
            rows.append({
                "label":           label,
                "type":            _str(raw.get("type", "slot")).lower() or "slot",
                "domain":          _str(raw.get("domain", "")),
                "mro":             _mro_normalise(raw.get("M / R / O", "O")),
                "range":           _str(raw.get("range", "")),
                "multivalued":     _normalise_bool(raw.get("multivalued", "")),
                "inlined_as_list": _normalise_bool(raw.get("inlined as list", "")),
                "unit":            _str(raw.get("unit", "")),
                "uri":             _str(raw.get("uri", "")),
                "description":     _str(raw.get("description", "")),
            })
        result[sheet_title] = rows
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Validation helpers
# ─────────────────────────────────────────────────────────────────────────────


def _valid_range(range_val: str, schema: dict, pending_class_names: set[str] | None = None) -> bool:
    if not range_val:
        return True
    if range_val in PRIMITIVE_TYPES or range_val in schema.get("classes", {}):
        return True
    return bool(pending_class_names) and range_val in pending_class_names


def _range_hint(schema: dict) -> str:
    prims = ", ".join(f"`{t}`" for t in sorted(PRIMITIVE_TYPES))
    known = sorted(schema.get("classes", {}).keys())[:20]
    classes_str = ", ".join(f"`{c}`" for c in known)
    suffix = " (…)" if len(schema.get("classes", {})) > 20 else ""
    return (
        f"Valid primitive types: {prims}. "
        f"Known schema classes (first 20): {classes_str}{suffix}."
    )


# ─────────────────────────────────────────────────────────────────────────────
# Change planning
# ─────────────────────────────────────────────────────────────────────────────


def plan_changes(
    schema: dict,
    excel_data: dict[str, list[dict]],
    label_to_slot: dict[str, str],
    label_to_class: dict[str, str],
    slot_origin: dict[str, Path],
    class_origin: dict[str, Path],
    reporter: Reporter,
) -> list[dict[str, Any]]:
    """
    Diff the Excel data against the merged schema.
    Returns validated Change dicts ready to apply.
    Unresolvable issues are recorded as errors or warnings on reporter.
    """
    changes: list[dict[str, Any]] = []

    for sheet_title, rows in excel_data.items():
        # Classes proposed as new elsewhere in this same sheet -- lets a new
        # slot/class reference another new class in the same submission
        # (e.g. adding a slot together with the class it ranges over).
        pending_class_names = _collect_pending_class_names(rows, label_to_class)
        schema_class = CLASS_MAP[sheet_title]

        # Collect all slot/class names the schema knows about for this class
        schema_slot_names: set[str] = set(get_all_class_slots(schema, schema_class))
        for su_name, _ in get_class_ranged_slot_usage(schema, schema_class):
            schema_slot_names.add(su_name)

        schema_class_names: set[str] = set()
        for slot_name in schema_slot_names:
            slot_def = get_slot_details(schema, slot_name)
            rng = slot_def.get("range", "")
            if rng and rng in schema.get("classes", {}):
                schema_class_names.add(rng)
                for sub in get_subclasses(schema, rng):
                    schema_class_names.add(sub)

        # Track which schema names appear in the Excel (for deletion detection)
        seen_slot_names:  set[str] = set()
        seen_class_names: set[str] = set()

        for row in rows:
            label    = row["label"]
            row_type = row["type"]
            domain   = row["domain"]

            if row_type == "slot":
                slot_name = label_to_slot.get(label)

                if slot_name is not None:
                    # ── Known global slot ───────────────────────────────────
                    # If the row has a domain (e.g. domain="Precursor"), the
                    # slot lives in that subclass's slot_usage, not in the
                    # top-level class.  Use the domain class as context so
                    # _plan_slot_changes targets the right YAML node.
                    seen_slot_names.add(slot_name)
                    if slot_name not in slot_origin:
                        # Inherited from a vendored chemdcat-ap module (e.g.
                        # ChemicalReaction's used_reactant) — visible for
                        # reference on the effective class, but not owned by
                        # any editable module. Never modifiable via the inbox
                        # workflow, regardless of what the row contains.
                        reporter.info(
                            sheet_title, f"slot '{label}'",
                            f"Skipped: `{slot_name}` is inherited from a chemdcat-ap "
                            f"base class and is not modifiable via the inbox workflow "
                            f"(edit the YAML directly).",
                        )
                    else:
                        effective_class = (
                            (label_to_class.get(domain) or domain)
                            if domain else schema_class
                        )
                        _plan_slot_changes(
                            row, slot_name, schema, sheet_title, effective_class,
                            slot_origin, class_origin, changes, reporter,
                        )

                elif domain:
                    # ── Unknown label + non-empty domain ───────────────────
                    # Could be a slot_usage-only slot (not in global slots:)
                    # defined on the domain class (e.g. has_concentration in
                    # CoPrecipitation).  Derive the slot name and check.
                    effective_class = label_to_class.get(domain) or domain
                    derived_name = _label_to_slot_name(label)
                    cls_def = schema.get("classes", {}).get(effective_class, {})
                    if derived_name in (cls_def.get("slot_usage") or {}):
                        seen_slot_names.add(derived_name)
                        _plan_slot_changes(
                            row, derived_name, schema, sheet_title,
                            effective_class, slot_origin, class_origin,
                            changes, reporter,
                        )
                    elif derived_name in get_all_class_slots(schema, effective_class):
                        # Slot already belongs to the subclass hierarchy (its own
                        # slots: list or a mixin) and cannot be modified via the
                        # inbox workflow.  Skip silently — these rows are
                        # structural display information from the Excel
                        # generator, not editable fields.
                        reporter.info(
                            sheet_title, f"slot '{label}'",
                            f"Skipped: belongs to sub-class `{effective_class}` "
                            f"and is not modifiable via the inbox workflow "
                            f"(edit the YAML directly).",
                        )
                    else:
                        # Unknown slot assigned to a domain class that does not
                        # already define it → a genuinely new slot to be added to
                        # that subclass (e.g. anode/cathode on ElectrochemicalReactor).
                        # _plan_new_slot resolves the owner class from the domain.
                        _plan_new_slot(
                            row, sheet_title, schema_class,
                            schema, class_origin, slot_origin, label_to_slot,
                            label_to_class, changes, reporter,
                            pending_class_names,
                        )

                else:
                    # ── Unknown label + empty domain → new top-level slot ──
                    _plan_new_slot(
                        row, sheet_title, schema_class,
                        schema, class_origin, slot_origin, label_to_slot,
                        label_to_class, changes, reporter,
                        pending_class_names,
                    )

            elif row_type == "class":
                # ── When a class row has a domain, that domain is the label
                # of the parent slot (e.g. "had input entity" for Precursor).
                # Mark that parent slot as seen so the deletion detector does
                # not falsely warn that it is missing from the workbook.
                if domain:
                    parent_slot_name = label_to_slot.get(domain)
                    if parent_slot_name:
                        seen_slot_names.add(parent_slot_name)

                class_name = label_to_class.get(label)
                if class_name is None:
                    _plan_new_class(
                        row, sheet_title, schema_class,
                        schema, class_origin, label_to_class,
                        changes, reporter,
                        pending_class_names,
                    )
                else:
                    seen_class_names.add(class_name)
                    if class_name not in class_origin:
                        # Inherited from a vendored chemdcat-ap module (e.g.
                        # Catalyst, Reactor) — visible for reference, but not
                        # owned by any editable module and never modifiable
                        # via the inbox workflow.
                        reporter.info(
                            sheet_title, f"class '{label}'",
                            f"Skipped: `{class_name}` is a chemdcat-ap base class "
                            f"and is not modifiable via the inbox workflow "
                            f"(edit the YAML directly).",
                        )
                    else:
                        _plan_class_changes(
                            row, class_name, schema, sheet_title,
                            class_origin, changes, reporter,
                        )

        # ── detect deletions ───────────────────────────────────────────────
        # Only slots/classes owned by an editable module can ever be
        # "deleted" via the inbox workflow. Names inherited from a vendored
        # chemdcat-ap module (not in slot_origin/class_origin) are skipped
        # here entirely — they were never addable/removable via Excel in the
        # first place, so their absence from a contributor's workbook is not
        # a deletion signal.

        for slot_name in schema_slot_names:
            if slot_name not in slot_origin:
                continue
            if slot_name not in seen_slot_names:
                reporter.warning(
                    sheet_title, f"slot `{slot_name}`",
                    f"Present in the schema but **missing** from your workbook "
                    f"(expected label: *{snake_to_readable(slot_name)}*). "
                    f"It will be removed from `{schema_class}`.",
                    hint="If accidental (e.g. you filtered rows before saving), "
                         "re-download the template and start again. "
                         "If intentional, the deletion is applied and the test suite "
                         "will verify no required fields are broken.",
                )
                changes.append({
                    "type":         "slot_delete",
                    "name":         slot_name,
                    "schema_class": schema_class,
                    "_target":      class_origin.get(
                        schema_class, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE
                    ),
                })

        for class_name in schema_class_names:
            if class_name not in class_origin:
                continue
            if class_name not in seen_class_names:
                reporter.warning(
                    sheet_title, f"class `{class_name}`",
                    f"Present in the schema but **missing** from your workbook "
                    f"(expected label: *{snake_to_readable(class_name)}*). "
                    f"It will be removed.",
                    hint="If accidental, re-download the template. "
                         "The maintainer will review deletions before merging.",
                )
                changes.append({
                    "type":         "class_delete",
                    "name":         class_name,
                    "schema_class": schema_class,
                    "_target":      class_origin.get(
                        class_name, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE
                    ),
                })

    return changes


# ── per-row change planners ────────────────────────────────────────────────


def _effective(slot_def: dict, su: dict, key: str, default: Any = None) -> Any:
    """Return slot_usage value if set, else global slot value."""
    if key in su:
        return su[key]
    return slot_def.get(key, default)


def _slot_owner_classes(schema: dict, slot_name: str) -> list[str]:
    """
    Return every class that directly references slot_name, via its own
    slots: list or a slot_usage entry. Used to warn when an edit to a slot
    that has no existing slot_usage override for the row's class would fall
    through to the slot's single, global definition -- silently changing it
    for every other class that also uses it, not just the one being edited.
    """
    owners: list[str] = []
    for cname, cdef in schema.get("classes", {}).items():
        if not isinstance(cdef, dict):
            continue
        if slot_name in (cdef.get("slots") or []) or slot_name in (cdef.get("slot_usage") or {}):
            owners.append(cname)
    return owners


def _plan_slot_changes(
    row: dict,
    slot_name: str,
    schema: dict,
    sheet: str,
    schema_class: str,
    slot_origin: dict[str, Path],
    class_origin: dict[str, Path],
    changes: list,
    reporter: Reporter,
) -> None:
    slot_def  = get_slot_details(schema, slot_name)
    class_def = schema.get("classes", {}).get(schema_class, {})
    has_su_override = slot_name in (class_def.get("slot_usage") or {})
    su        = (class_def.get("slot_usage") or {}).get(slot_name) or {}

    target_su   = class_origin.get(schema_class)
    target_slot = slot_origin.get(slot_name)
    changes_before = len(changes)

    # -- M/R/O --
    new_mro = row["mro"]
    if new_mro not in ("M", "R", "O"):
        reporter.error(
            sheet, f"slot `{slot_name}`",
            f"Invalid M/R/O value `{new_mro!r}`. "
            f"Only **M** (Mandatory), **R** (Recommended), or **O** (Optional) are accepted.",
        )
    else:
        cur_req = bool(_effective(slot_def, su, "required",    False))
        cur_rec = bool(_effective(slot_def, su, "recommended", False))
        cur_mro = "M" if cur_req else ("R" if cur_rec else "O")
        if new_mro != cur_mro:
            changes.append({
                "type": "slot_mro", "name": slot_name,
                "schema_class": schema_class, "mro": new_mro,
                "_target_su": target_su, "_target_slot": target_slot,
            })

    # -- description --
    new_desc = row["description"]
    if new_desc and new_desc != _str(_effective(slot_def, su, "description", "")):
        changes.append({
            "type": "slot_description", "name": slot_name,
            "schema_class": schema_class, "value": new_desc,
            "_target_su": target_su, "_target_slot": target_slot,
        })

    # -- URI --
    new_uri = row["uri"]
    if new_uri and new_uri != _str(_effective(slot_def, su, "slot_uri", "")):
        changes.append({
            "type": "slot_uri", "name": slot_name,
            "schema_class": schema_class, "value": new_uri,
            "_target_su": target_su, "_target_slot": target_slot,
        })

    # -- range --
    new_range = row["range"]
    if new_range:
        # An absent range key means the schema default (string); normalise so a
        # default-range slot is not seen as "changing" to string on the next run.
        cur_range = _str(_effective(slot_def, su, "range", "")) or DEFAULT_RANGE
        if new_range != cur_range:
            if not _valid_range(new_range, schema):
                reporter.error(
                    sheet, f"slot `{slot_name}`",
                    f"Unknown range `{new_range}`. "
                    f"This type is not a recognized primitive or schema class.",
                    hint=_range_hint(schema),
                )
            else:
                reporter.warning(
                    sheet, f"slot `{slot_name}`",
                    f"Range changed: `{cur_range}` → `{new_range}`. "
                    f"This structural change may invalidate existing data files.",
                    hint="The test suite will verify this automatically. "
                         "A maintainer will review before merging.",
                )
                changes.append({
                    "type": "slot_range", "name": slot_name,
                    "schema_class": schema_class, "value": new_range,
                    "_target_su": target_su, "_target_slot": target_slot,
                })

    # -- multivalued --
    new_mv = row["multivalued"] == "yes"
    cur_mv = bool(_effective(slot_def, su, "multivalued", False))
    if new_mv != cur_mv:
        changes.append({
            "type": "slot_multivalued", "name": slot_name,
            "schema_class": schema_class, "value": new_mv,
            "_target_su": target_su, "_target_slot": target_slot,
        })

    # -- inlined_as_list --
    new_il = row["inlined_as_list"] == "yes"
    cur_il = bool(_effective(slot_def, su, "inlined_as_list", False))
    if new_il != cur_il:
        changes.append({
            "type": "slot_inlined_as_list", "name": slot_name,
            "schema_class": schema_class, "value": new_il,
            "_target_su": target_su, "_target_slot": target_slot,
        })

    # -- unit --
    new_unit = row["unit"]
    cur_unit = _str((slot_def.get("unit") or {}).get("ucum_code", ""))
    if new_unit != cur_unit:
        changes.append({
            "type": "slot_unit", "name": slot_name,
            "schema_class": schema_class, "value": new_unit,
            "_target_slot": target_slot,
        })

    # -- warn if this edit falls through to the slot's single global
    # definition, shared by more than one class ---------------------------
    if len(changes) > changes_before and not has_su_override:
        owners = [c for c in _slot_owner_classes(schema, slot_name) if c != schema_class]
        if owners:
            owners_str = ", ".join(f"`{c}`" for c in sorted(owners))
            reporter.warning(
                sheet, f"slot `{slot_name}`",
                f"This edit changes `{slot_name}`'s single, global definition "
                f"-- it is not scoped to `{schema_class}` alone. It will also "
                f"change `{slot_name}` for: {owners_str}.",
                hint="If you only meant to change it for this class, a "
                     "maintainer needs to add a slot_usage override for "
                     f"`{slot_name}` on `{schema_class}` first, rather than "
                     "editing the global slot.",
            )


def _plan_class_changes(
    row: dict,
    class_name: str,
    schema: dict,
    sheet: str,
    class_origin: dict[str, Path],
    changes: list,
    reporter: Reporter,
) -> None:
    class_def = schema.get("classes", {}).get(class_name, {})
    target = class_origin.get(class_name)

    new_desc = row["description"]
    if new_desc and new_desc != _str(class_def.get("description", "")):
        changes.append({
            "type": "class_description", "name": class_name,
            "value": new_desc, "_target": target,
        })

    new_uri = row["uri"]
    if new_uri and new_uri != _str(class_def.get("class_uri", "")):
        changes.append({
            "type": "class_uri", "name": class_name,
            "value": new_uri, "_target": target,
        })


def _plan_new_slot(
    row: dict,
    sheet: str,
    schema_class: str,
    schema: dict,
    class_origin: dict[str, Path],
    slot_origin: dict[str, Path],
    label_to_slot: dict[str, str],
    label_to_class: dict[str, str],
    changes: list,
    reporter: Reporter,
    pending_class_names: set[str] | None = None,
) -> None:
    label     = row["label"]
    domain    = row["domain"]
    slot_name = _label_to_slot_name(label)
    pending_class_names = pending_class_names or set()

    # Resolve the class that will own the new slot:
    #   • empty domain     → the sheet's top-level data class (schema_class)
    #   • non-empty domain → the named subclass (e.g. ElectrochemicalReactor),
    #                        added to that class exactly like the top-level case.
    #                        The domain may also be a class proposed as new
    #                        elsewhere in this same submission (pending_class_names).
    if domain:
        owner_class = label_to_class.get(domain) or domain
        if owner_class not in schema.get("classes", {}) and owner_class not in pending_class_names:
            reporter.error(
                sheet, f"new slot '{label}'",
                f"The domain `{domain}` is not a recognised class. "
                f"Set the domain column to an existing class label, or leave it "
                f"empty to add a top-level slot.",
                hint="Look at the class rows in this sheet for valid domain names.",
            )
            return
    else:
        owner_class = schema_class

    # Name conflict: same derived name as an existing slot
    if slot_name in schema.get("slots", {}):
        existing_label = snake_to_readable(slot_name)
        reporter.error(
            sheet, f"new slot '{label}'",
            f"The derived slot name `{slot_name}` conflicts with the existing "
            f"slot **{existing_label}**. "
            f"To modify that slot, edit its existing row; do not add a new row.",
            hint="Use a more specific label so the derived name does not clash.",
        )
        return

    # M/R/O validation
    mro = row["mro"]
    if mro not in ("M", "R", "O"):
        reporter.error(
            sheet, f"new slot '{label}'",
            f"Invalid M/R/O value `{mro!r}`. Use M, R, or O.",
        )
        return

    # Range validation
    range_val = row["range"] or DEFAULT_RANGE
    if not _valid_range(range_val, schema, pending_class_names):
        reporter.error(
            sheet, f"new slot '{label}'",
            f"Unknown range `{range_val}` for new slot.",
            hint=_range_hint(schema),
        )
        return

    target = class_origin.get(owner_class, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE)
    reporter.info(
        sheet, f"new slot `{slot_name}`",
        f"Will add `{slot_name}` to `{owner_class}`.",
    )
    changes.append({
        "type":           "slot_add",
        "name":           slot_name,
        "label":          label,
        "schema_class":   owner_class,
        "range":          range_val,
        "mro":            mro,
        "description":    row["description"],
        "uri":            row["uri"],
        "multivalued":    row["multivalued"] == "yes",
        "inlined_as_list": row["inlined_as_list"] == "yes",
        "unit":           row["unit"],
        "_target":        target,
    })


def _plan_new_class(
    row: dict,
    sheet: str,
    schema_class: str,
    schema: dict,
    class_origin: dict[str, Path],
    label_to_class: dict[str, str],
    changes: list,
    reporter: Reporter,
    pending_class_names: set[str] | None = None,
) -> None:
    label      = row["label"]
    domain     = row["domain"]
    class_name = _label_to_class_name(label)
    pending_class_names = pending_class_names or set()

    # Name conflict
    if class_name in schema.get("classes", {}):
        reporter.error(
            sheet, f"new class '{label}'",
            f"A class named `{class_name}` already exists. "
            f"Edit its existing row to modify it.",
        )
        return

    # Parent class required
    if not domain:
        reporter.error(
            sheet, f"new class '{label}'",
            "New classes require a **domain** set to the parent class label.",
            hint="Look at the existing class rows in this sheet to find valid parent names.",
        )
        return

    # The parent may already exist, or be proposed as new elsewhere in this
    # same submission (pending_class_names) -- e.g. "Chromatographic Methods"
    # and "Gas Chromatography (GC)" added together, one as the other's parent.
    parent_name = label_to_class.get(domain)
    if parent_name is None and _label_to_class_name(domain) in pending_class_names:
        parent_name = _label_to_class_name(domain)
    if parent_name is None:
        reporter.error(
            sheet, f"new class '{label}'",
            f"The domain `{domain}` is not a recognised class label. "
            f"Set the domain column to the label of an existing parent class.",
            hint="Look at the existing class rows in this sheet to find valid parent names.",
        )
        return

    target = class_origin.get(parent_name, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE)
    reporter.info(
        sheet, f"new class `{class_name}`",
        f"Will add `{class_name}` as subclass of `{parent_name}`.",
    )
    changes.append({
        "type":         "class_add",
        "name":         class_name,
        "is_a":         parent_name,
        "schema_class": schema_class,
        "uri":          row["uri"],
        "description":  row["description"],
        "_target":      target,
    })


# ─────────────────────────────────────────────────────────────────────────────
# YAML file I/O helpers
# ─────────────────────────────────────────────────────────────────────────────


def _load_yaml(path: Path) -> Any:
    y = _make_yaml()
    with path.open(encoding="utf-8") as fh:
        return y.load(fh)


def _save_yaml(path: Path, doc: Any) -> None:
    y = _make_yaml()
    with path.open("w", encoding="utf-8") as fh:
        y.dump(doc, fh)


def _as_literal(value: str) -> Any:
    """Wrap multi-line strings in LiteralScalarString for block-style YAML."""
    if "\n" in value:
        return LiteralScalarString(value)
    return value


def _set_mro(node: dict, mro: str) -> None:
    """Set required/recommended on a slot or slot_usage node (clears old keys)."""
    for key in ("required", "recommended"):
        if key in node:
            del node[key]
    if mro == "M":
        node["required"] = True
    elif mro == "R":
        node["recommended"] = True
    # O → neither key present


# ─────────────────────────────────────────────────────────────────────────────
# Change application
# ─────────────────────────────────────────────────────────────────────────────


def _apply_slot_field(
    ch: dict,
    field_key: str,
    value: Any,
    reporter: Reporter,
    label: str,
) -> None:
    """
    Apply a single-field update to a slot, preferring slot_usage if it exists,
    falling back to the global slots: entry.
    """
    schema_class = ch["schema_class"]
    slot_name    = ch["name"]
    target_su    = ch.get("_target_su")
    target_slot  = ch.get("_target_slot")
    applied_via  = None

    if target_su:
        doc = _load_yaml(target_su)
        cls = (doc.get("classes") or {}).get(schema_class) or {}
        su  = (cls.get("slot_usage") or {}).get(slot_name)
        if su is not None:
            su[field_key] = value
            _save_yaml(target_su, doc)
            applied_via = f"slot_usage in `{target_su.name}`"

    if applied_via is None and target_slot:
        doc   = _load_yaml(target_slot)
        slots = doc.get("slots") or {}
        if slot_name in slots:
            if slots[slot_name] is None:
                slots[slot_name] = {}
            slots[slot_name][field_key] = value
            _save_yaml(target_slot, doc)
            applied_via = f"global slot in `{target_slot.name}`"

    if applied_via:
        reporter.applied(f"{label}: `{slot_name}` ({schema_class}) — via {applied_via}")


def _apply_slot_flag(
    ch: dict,
    field_key: str,
    value: bool,
    reporter: Reporter,
    label: str,
) -> None:
    """Apply a boolean flag (True → set key; False → delete key)."""
    schema_class = ch["schema_class"]
    slot_name    = ch["name"]
    target_su    = ch.get("_target_su")
    target_slot  = ch.get("_target_slot")
    applied_via  = None

    if target_su:
        doc = _load_yaml(target_su)
        cls = (doc.get("classes") or {}).get(schema_class) or {}
        su  = (cls.get("slot_usage") or {}).get(slot_name)
        if su is not None:
            if value:
                su[field_key] = True
            elif field_key in su:
                del su[field_key]
            _save_yaml(target_su, doc)
            applied_via = target_su.name

    if applied_via is None and target_slot:
        doc   = _load_yaml(target_slot)
        slots = doc.get("slots") or {}
        if slot_name in slots:
            if slots[slot_name] is None:
                slots[slot_name] = {}
            if value:
                slots[slot_name][field_key] = True
            elif field_key in slots[slot_name]:
                del slots[slot_name][field_key]
            _save_yaml(target_slot, doc)
            applied_via = target_slot.name

    if applied_via:
        reporter.applied(f"{label} → `{value}`: `{slot_name}` ({schema_class})")


def apply_changes(changes: list[dict], reporter: Reporter) -> None:
    """Apply all planned changes to YAML files (ruamel round-trip, comment-safe)."""

    for ch in changes:
        ctype = ch["type"]

        # ── slot M/R/O ────────────────────────────────────────────────────

        if ctype == "slot_mro":
            slot_name    = ch["name"]
            mro          = ch["mro"]
            schema_class = ch["schema_class"]
            target_su    = ch.get("_target_su")
            target_slot  = ch.get("_target_slot")
            applied_via  = None

            if target_su:
                doc = _load_yaml(target_su)
                cls = (doc.get("classes") or {}).get(schema_class) or {}
                su  = (cls.get("slot_usage") or {}).get(slot_name)
                if su is not None:
                    _set_mro(su, mro)
                    _save_yaml(target_su, doc)
                    applied_via = f"slot_usage in `{target_su.name}`"

            if applied_via is None and target_slot:
                doc   = _load_yaml(target_slot)
                slots = doc.get("slots") or {}
                if slot_name in slots:
                    if slots[slot_name] is None:
                        slots[slot_name] = {}
                    _set_mro(slots[slot_name], mro)
                    _save_yaml(target_slot, doc)
                    applied_via = f"global slot in `{target_slot.name}`"

            if applied_via:
                reporter.applied(
                    f"M/R/O → **{mro}**: `{slot_name}` ({schema_class}) — {applied_via}"
                )

        # ── slot description ──────────────────────────────────────────────

        elif ctype == "slot_description":
            _apply_slot_field(
                ch, "description", _as_literal(ch["value"]),
                reporter, "description updated",
            )

        # ── slot URI ──────────────────────────────────────────────────────

        elif ctype == "slot_uri":
            _apply_slot_field(ch, "slot_uri", ch["value"], reporter, "URI updated")

        # ── slot range ────────────────────────────────────────────────────

        elif ctype == "slot_range":
            _apply_slot_field(
                ch, "range", ch["value"],
                reporter,
                f"range changed → `{ch['value']}`",
            )

        # ── slot multivalued / inlined_as_list ────────────────────────────

        elif ctype == "slot_multivalued":
            _apply_slot_flag(
                ch, "multivalued", ch["value"],
                reporter, "multivalued",
            )

        elif ctype == "slot_inlined_as_list":
            _apply_slot_flag(
                ch, "inlined_as_list", ch["value"],
                reporter, "inlined_as_list",
            )

        # ── slot unit ─────────────────────────────────────────────────────

        elif ctype == "slot_unit":
            slot_name   = ch["name"]
            new_unit    = ch["value"]
            target_slot = ch.get("_target_slot")

            if target_slot:
                doc   = _load_yaml(target_slot)
                slots = doc.get("slots") or {}
                if slot_name in slots:
                    if slots[slot_name] is None:
                        slots[slot_name] = {}
                    if new_unit:
                        slots[slot_name]["unit"] = {"ucum_code": new_unit}
                    elif "unit" in slots[slot_name]:
                        del slots[slot_name]["unit"]
                    _save_yaml(target_slot, doc)
                    label = f"`{new_unit}`" if new_unit else "*(removed)*"
                    reporter.applied(f"Unit → {label}: `{slot_name}`")

        # ── class description ─────────────────────────────────────────────

        elif ctype == "class_description":
            class_name = ch["name"]
            target     = ch.get("_target")
            if target:
                doc = _load_yaml(target)
                classes = doc.get("classes") or {}
                if class_name in classes:
                    if classes[class_name] is None:
                        classes[class_name] = {}
                    classes[class_name]["description"] = _as_literal(ch["value"])
                    _save_yaml(target, doc)
                    reporter.applied(f"Class description updated: `{class_name}`")

        # ── class URI ─────────────────────────────────────────────────────

        elif ctype == "class_uri":
            class_name = ch["name"]
            target     = ch.get("_target")
            if target:
                doc = _load_yaml(target)
                classes = doc.get("classes") or {}
                if class_name in classes:
                    if classes[class_name] is None:
                        classes[class_name] = {}
                    classes[class_name]["class_uri"] = ch["value"]
                    _save_yaml(target, doc)
                    reporter.applied(f"Class URI updated: `{class_name}`")

        # ── add new slot ──────────────────────────────────────────────────

        elif ctype == "slot_add":
            slot_name    = ch["name"]
            schema_class = ch["schema_class"]
            target       = ch["_target"]
            mro          = ch["mro"]

            doc = _load_yaml(target)

            # Build slot definition dict
            slot_def: dict[str, Any] = {}
            if ch["description"]:
                slot_def["description"] = _as_literal(ch["description"])
            if ch["range"]:
                slot_def["range"] = ch["range"]
            if ch["uri"]:
                slot_def["slot_uri"] = ch["uri"]
            if mro == "M":
                slot_def["required"] = True
            elif mro == "R":
                slot_def["recommended"] = True
            if ch["multivalued"]:
                slot_def["multivalued"] = True
            if ch["inlined_as_list"]:
                slot_def["inlined_as_list"] = True
            if ch["unit"]:
                slot_def["unit"] = {"ucum_code": ch["unit"]}

            # Add to global slots:
            if "slots" not in doc or doc["slots"] is None:
                doc["slots"] = {}
            doc["slots"][slot_name] = slot_def

            # Append to class slots: list
            classes = doc.get("classes") or {}
            if schema_class in classes:
                cls_node = classes[schema_class]
                if cls_node is None:
                    classes[schema_class] = {"slots": [slot_name]}
                else:
                    if "slots" not in cls_node or cls_node["slots"] is None:
                        cls_node["slots"] = []
                    if slot_name not in cls_node["slots"]:
                        cls_node["slots"].append(slot_name)

            _save_yaml(target, doc)
            reporter.applied(
                f"New slot `{slot_name}` added to `{schema_class}` "
                f"(M/R/O: {mro}, range: {ch['range']})"
            )

        # ── add new class ─────────────────────────────────────────────────

        elif ctype == "class_add":
            class_name = ch["name"]
            parent     = ch["is_a"]
            target     = ch["_target"]

            doc = _load_yaml(target)

            class_def: dict[str, Any] = {"is_a": parent}
            if ch["uri"]:
                class_def["class_uri"] = ch["uri"]
            if ch["description"]:
                class_def["description"] = _as_literal(ch["description"])

            if "classes" not in doc or doc["classes"] is None:
                doc["classes"] = {}
            doc["classes"][class_name] = class_def

            _save_yaml(target, doc)
            reporter.applied(
                f"New class `{class_name}` added as subclass of `{parent}`"
            )

        # ── delete slot ───────────────────────────────────────────────────

        elif ctype == "slot_delete":
            slot_name    = ch["name"]
            schema_class = ch["schema_class"]
            target       = ch["_target"]

            doc = _load_yaml(target)
            classes = doc.get("classes") or {}
            if schema_class in classes:
                cls_node = classes[schema_class] or {}
                # Remove from class slots list
                slot_list = cls_node.get("slots") or []
                if slot_name in slot_list:
                    slot_list.remove(slot_name)
                    cls_node["slots"] = slot_list
                # Remove from slot_usage
                su = cls_node.get("slot_usage") or {}
                if slot_name in su:
                    del su[slot_name]
            _save_yaml(target, doc)
            reporter.applied(
                f"Slot `{slot_name}` removed from `{schema_class}` "
                f"(global definition kept — it may still be used by other classes)"
            )

        # ── delete class ──────────────────────────────────────────────────

        elif ctype == "class_delete":
            class_name = ch["name"]
            target     = ch["_target"]

            doc = _load_yaml(target)
            classes = doc.get("classes") or {}
            if class_name in classes:
                del classes[class_name]
                _save_yaml(target, doc)
                reporter.applied(f"Class `{class_name}` removed from the schema")


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────


def main(inbox_path: Path) -> int:
    reporter = Reporter()

    # 1. Load the merged schema
    try:
        schema = load_merged_schema(str(SCHEMA_DIR))
    except Exception as exc:  # noqa: BLE001
        reporter.error("schema", "load", f"Could not load the merged schema: {exc}")
        print(reporter.to_markdown())
        return 1

    # 2. Validate workbook structure
    sheets = validate_structure(inbox_path, reporter)
    if sheets is None or reporter.has_errors:
        print(reporter.to_markdown())
        return 3

    # 3. Build name→file and label→name indexes
    slot_origin, class_origin = build_origin_index(SCHEMA_DIR)
    label_to_slot, label_to_class = build_label_index(schema)

    # 4. Parse normalised row data from Excel
    excel_data = parse_excel(sheets)

    # 5. Plan all changes (errors go to reporter, not raised)
    changes = plan_changes(
        schema, excel_data,
        label_to_slot, label_to_class,
        slot_origin, class_origin,
        reporter,
    )

    # 6. Stop if any planning errors — nothing written yet
    if reporter.has_errors:
        print(reporter.to_markdown())
        return 3

    # 7. Apply changes to YAML files
    if changes:
        apply_changes(changes, reporter)

    # 8. Print markdown report (captured by excel_inbox.yaml for PR comment)
    print(reporter.to_markdown())

    if reporter.has_errors:
        return 3
    if reporter.has_warnings:
        return 2
    return 0


if __name__ == "__main__":
    # Ensure stdout is UTF-8 even on Windows (emoji in Markdown output otherwise
    # crash with UnicodeEncodeError on cp1252 consoles / cmd.exe).
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    inbox_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INBOX
    if not inbox_path.exists():
        print(
            f"## ❌ Inbox file not found\n\n`{inbox_path}` does not exist.\n\n"
            f"Place the modified workbook at `inbox/coremeta4cat_vocabulary.xlsx` "
            f"and try again.",
            file=sys.stderr,
        )
        sys.exit(1)
    sys.exit(main(inbox_path))
