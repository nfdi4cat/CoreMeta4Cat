"""
inbox_to_schema.py

Converts a modified CoreMeta4Cat vocabulary workbook from the inbox/ folder
into changes in the LinkML YAML schema files.

Only what the contributor changed is applied. Every generated workbook carries
a very hidden ``_baseline`` sheet (see workbook_rows.py) with all rows exactly
as they were generated, and each row of the submitted workbook is compared
with it:

  • unchanged rows are skipped -- a workbook downloaded before other changes
    were merged never reverts them;
  • for a changed row only the edited fields are applied (a field that was
    also changed in the schema since the download is reported as a conflict);
  • new rows add slots or classes, or attach an existing slot to a class;
  • deleted rows remove the slot from that class, or remove the class.

Workbooks without a ``_baseline`` sheet (made from an older template) are
rejected -- there is no way to tell their edits from changes merged since.

Supported operations (all per row in the Excel):
  • Modify existing slots  — M/R/O (scoped to the row's class), description,
                             URI, range, multivalued, inlined_as_list, unit
  • Modify existing classes — description, URI
  • Add new slots          — derived snake_case name from label; added to the
                             owning class's YAML module and global slots: dict
  • Add new classes        — derived PascalCase name; added as a subclass of
                             the class indicated by the domain column; new
                             slots on a new class go into the same module
  • Attach existing slots  — a known slot listed on a class that does not have
                             it yet is appended to that class's slots: list; a
                             differing M/R/O is scoped to the class via slot_usage
  • Delete slots/classes   — delete the row

Rows inherited from the vendored chemdcat-ap modules and the CoreMeta4Cat
sheet are reference only: edits there are reported as warnings, never applied.

Values are compared with what LinkML actually uses (SchemaView.induced_slot,
see schema_to_excel.py), and writes take inheritance into account: switching
off a flag that a slot would otherwise inherit writes an explicit ``false``.

After applying, the schema is reloaded and the workbook rows regenerated:
every applied field must now show the contributor's value, and every added
class/slot must exist. If anything did not land, all schema files are
restored and the run fails (exit code 3).

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

import contextlib
import io
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import openpyxl
import pandas as pd
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString

_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from generate_schema_docs import (  # noqa: E402
    EDITABLE_MODULE_FILES,  # noqa: F401  (re-exported for callers)
    build_origin_index,
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    get_subclasses,
    load_merged_schema,
    load_yaml_file,
    snake_to_readable,
)
from schema_to_excel import (  # noqa: E402
    _raw_row_values,
    generate_rows,
    load_schema_view,
    slot_row_values,
)
from workbook_rows import (  # noqa: E402
    BASELINE_SHEET,
    COLUMN_ALIASES,
    FIELD_LABELS,
    REFERENCE_SHEET,
    VALUE_FIELDS,
    changed_fields,
    class_name_from_label,
    clean,
    index_rows,
    normalise_bool,
    normalise_mro,
    normalise_row,
    read_baseline,
    row_key,
    slot_name_from_label,
)

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

SCHEMA_DIR    = _ROOT / "src" / "coremeta4cat" / "schema"
DEFAULT_INBOX = _ROOT / "inbox" / "coremeta4cat_vocabulary.xlsx"
DEV_WORKBOOK_URL = "https://nfdi4cat.github.io/CoreMeta4Cat/dev/assets/coremeta4cat_vocabulary.xlsx"

# Sheet title (Excel) → LinkML class name in the schema
CLASS_MAP: dict[str, str] = {
    "Synthesis":        "Synthesis",
    "Characterization": "Characterization",
    "Reaction":         "CatalyticReaction",
    "Simulation":       "Simulation",
}

# The set of coremeta4cat-authored (editable) modules is the single canonical
# EDITABLE_MODULE_FILES list from generate_schema_docs.py -- this is also what
# build_origin_index() scans, so "editable via the inbox workflow" always means
# "defined in one of these files."
#
# New top-level slots/classes with no other owning module land here by default
# (the top-level aggregator module).
DEFAULT_NEW_ELEMENT_FILE = "coremeta4cat.yaml"

# Primitive LinkML types that are valid in the range column
PRIMITIVE_TYPES: frozenset[str] = frozenset({
    "string", "integer", "float", "boolean", "uri", "uriorcurie",
    "date", "datetime", "time", "decimal", "double", "Any",
})

# The schema's default_range. A slot with no explicit `range` key is
# equivalent to one with `range: string`.
DEFAULT_RANGE = "string"

# Workbook field → change type of a planned slot modification
_CHANGE_TYPE = {
    "mro":             "slot_mro",
    "description":     "slot_description",
    "uri":             "slot_uri",
    "range":           "slot_range",
    "multivalued":     "slot_multivalued",
    "inlined_as_list": "slot_inlined_as_list",
    "unit":            "slot_unit",
}
# Workbook field → YAML key on a slot / slot_usage node (M/R/O is two keys)
_YAML_KEY = {
    "description":     "description",
    "uri":             "slot_uri",
    "range":           "range",
    "multivalued":     "multivalued",
    "inlined_as_list": "inlined_as_list",
    "unit":            "unit",
}

_PIPELINE_HINT = "This is a pipeline problem, not a workbook problem -- please report it to a maintainer."

# Kept for callers of the old private helpers; the normalisation itself lives
# in workbook_rows.py so all scripts compare rows the same way.
_str = clean
_normalise_bool = normalise_bool
_mro_normalise = normalise_mro

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
        self._notes:   list[str] = []
        self.empty_message = (
            "✅ The workbook is fully aligned with the schema — no changes were needed."
        )

    # ── record ─────────────────────────────────────────────────────────────

    def error(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("error", sheet, context, message, hint))

    def warning(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("warning", sheet, context, message, hint))

    def info(self, sheet: str, context: str, message: str, hint: str = "") -> None:
        self._diags.append(Diagnostic("info", sheet, context, message, hint))

    def applied(self, description: str) -> None:
        self._applied.append(description)

    def note(self, text: str) -> None:
        """A line shown in the report's Notes section (context, not a problem)."""
        self._notes.append(text)

    def rolled_back(self) -> None:
        """Forget the applied list after the schema files were restored."""
        count = len(self._applied)
        self._applied = []
        if count:
            self.note(
                f"{count} prepared change(s) were rolled back because of the errors "
                f"below — the schema files are unchanged."
            )

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

        if self._notes:
            lines += ["### ℹ️ Notes", ""]
            lines += [f"- {note}" for note in self._notes]
            lines.append("")

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
                "The following items need a maintainer's review before the PR "
                "is merged:",
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
            lines += [self.empty_message, ""]

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


def _load_yaml(path: Path) -> Any:
    y = _make_yaml()
    with path.open(encoding="utf-8") as fh:
        return y.load(fh)


def _save_yaml(path: Path, doc: Any) -> None:
    y = _make_yaml()
    # newline="\n": LF on every OS (text mode would write CRLF on Windows)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        y.dump(doc, fh)


def _as_literal(value: str) -> Any:
    """Wrap multi-line strings in LiteralScalarString for block-style YAML."""
    if "\n" in value:
        return LiteralScalarString(value)
    return value


def _snapshot_schema(schema_dir: Path) -> dict[Path, bytes]:
    return {p: p.read_bytes() for p in Path(schema_dir).glob("*.yaml")}


def _restore_schema(snapshot: dict[Path, bytes]) -> None:
    for path, data in snapshot.items():
        path.write_bytes(data)


# ─────────────────────────────────────────────────────────────────────────────
# Schema index builders
# ─────────────────────────────────────────────────────────────────────────────

# build_origin_index() lives in generate_schema_docs.py (imported above) so
# schema_to_excel.py shares the exact same editable/vendored predicate for
# rendering read-only rows.


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

    for name in schema.get("slots", {}):
        label_to_slot[snake_to_readable(name)] = name

    for class_def in schema.get("classes", {}).values():
        for slot_name in ((class_def or {}).get("slot_usage") or {}):
            label = snake_to_readable(slot_name)
            if label not in label_to_slot:
                label_to_slot[label] = slot_name

    for name in schema.get("classes", {}):
        label_to_class[snake_to_readable(name)] = name

    return label_to_slot, label_to_class


# ─────────────────────────────────────────────────────────────────────────────
# Label helpers
# ─────────────────────────────────────────────────────────────────────────────


def _label_to_slot_name(label: str) -> str:
    """Derive a snake_case slot name from a human-readable label."""
    return slot_name_from_label(label)


def _label_to_class_name(label: str) -> str:
    """Derive a PascalCase class name from a human-readable label."""
    return class_name_from_label(label)


def _collect_pending_classes(rows: list[dict], label_to_class: dict[str, str]) -> dict[str, str]:
    """
    Pre-scan one sheet's rows for class-type rows that don't yet exist in the
    schema, i.e. classes proposed as new in this same submission. Returns
    {derived PascalCase name: parent class name} ('' if the parent is unknown).

    A larger submission commonly adds a new slot AND the new class it points
    to (or a new class AND its new parent class) in the same batch; treating
    these pending names as valid supports applying the whole change together.
    The parent mapping lets slots on a pending class be written into the same
    YAML module the class itself will be written to (_resolve_class_target).
    """
    new_rows = [
        row for row in rows
        if row["type"] == "class" and label_to_class.get(row["label"]) is None
    ]
    names = {_label_to_class_name(row["label"]) for row in new_rows}

    pending: dict[str, str] = {}
    for row in new_rows:
        domain = row["domain"]
        parent = label_to_class.get(domain) if domain else None
        if parent is None and domain and _label_to_class_name(domain) in names:
            parent = _label_to_class_name(domain)
        pending[_label_to_class_name(row["label"])] = parent or ""
    return pending


def _collect_pending_class_names(rows: list[dict], label_to_class: dict[str, str]) -> set[str]:
    """Names-only view of _collect_pending_classes."""
    return set(_collect_pending_classes(rows, label_to_class))


def _resolve_domain_class(
    domain: str,
    label_to_class: dict[str, str],
    pending_classes: dict[str, str] | None = None,
) -> str:
    """
    Map a row's domain cell to a class name: an existing class label, a class
    proposed as new in this same submission (matched by its derived
    PascalCase name), or -- as a last resort -- the raw cell value.
    """
    known = label_to_class.get(domain)
    if known:
        return known
    derived = _label_to_class_name(domain)
    if pending_classes and derived in pending_classes:
        return derived
    return domain


def _resolve_class_target(
    class_name: str,
    class_origin: dict[str, Path],
    pending_classes: dict[str, str] | None = None,
) -> Path:
    """
    Return the YAML module a class lives in -- or, for a class that is new in
    this submission, the module it *will* be written to: the module of its
    nearest existing ancestor (walking up through other pending classes).

    Both _plan_new_class and _plan_new_slot use this, so a new class and the
    new slots assigned to it always target the same file (PR #157).
    """
    pending_classes = pending_classes or {}
    seen: set[str] = set()
    current = class_name
    while current and current not in seen:
        seen.add(current)
        if current in class_origin:
            return class_origin[current]
        current = pending_classes.get(current, "")
    return SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE


def _class_has_slot(
    schema: dict,
    class_name: str,
    slot_name: str,
    pending_classes: dict[str, str] | None = None,
) -> bool:
    """
    True if slot_name already reaches class_name -- via its own slots: list,
    is_a inheritance, a mixin, or a slot_usage entry anywhere along that
    chain. For a class that is new in this submission, its (pending or
    existing) parent is checked instead.
    """
    classes = schema.get("classes", {})
    pending_classes = pending_classes or {}
    seen_pending: set[str] = set()
    while class_name not in classes:
        if class_name in seen_pending or class_name not in pending_classes:
            return False
        seen_pending.add(class_name)
        class_name = pending_classes[class_name]

    if slot_name in get_all_class_slots(schema, class_name):
        return True

    stack, seen = [class_name], set()
    while stack:
        cname = stack.pop()
        if cname in seen:
            continue
        seen.add(cname)
        cdef = classes.get(cname) or {}
        if slot_name in (cdef.get("slot_usage") or {}):
            return True
        if cdef.get("is_a"):
            stack.append(cdef["is_a"])
        stack.extend(cdef.get("mixins") or [])
    return False


# ─────────────────────────────────────────────────────────────────────────────
# Workbook loading + structural validation
# ─────────────────────────────────────────────────────────────────────────────

# Canonical column name → accepted aliases (all lower-case)
_COL_ALIASES: dict[str, list[str]] = COLUMN_ALIASES

# Columns that must be present (the three newer ones are optional for back-compat)
_REQUIRED_COLS = {"label", "type", "domain", "M / R / O", "range", "uri", "description"}
_OPTIONAL_COLS = {"multivalued", "inlined as list", "unit"}


def _canonical_frame(df: pd.DataFrame) -> tuple[pd.DataFrame | None, list[str]]:
    """Rename df's columns to canonical names; returns (df, missing required)."""
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    resolved: dict[str, str] = {}  # canonical → actual column name in df
    for canonical, aliases in _COL_ALIASES.items():
        found = next((c for c in df.columns if c.strip().lower() in aliases), None)
        if found:
            resolved[canonical] = found
    missing = [c for c in _REQUIRED_COLS if c not in resolved]
    if missing:
        return None, missing
    df = df.rename(columns={v: k for k, v in resolved.items()})
    for col in _OPTIONAL_COLS:
        if col not in df.columns:
            df[col] = ""
    return df.dropna(how="all"), []


def validate_structure(
    workbook_path: Path,
    reporter: Reporter,
) -> dict[str, pd.DataFrame] | None:
    """
    Load and structurally validate the workbook.
    Returns {sheet_title: DataFrame} for the data sheets (plus the CoreMeta4Cat
    reference sheet when it is readable), or None on fatal error.
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
        df, missing_required = _canonical_frame(raw[sheet_title])
        if df is None:
            reporter.error(
                sheet_title, "column check",
                f"Missing required column(s): {', '.join(sorted(missing_required))}.",
                hint="Re-download the vocabulary template from docs/assets/ and "
                     "make sure you have not deleted or renamed any column headers.",
            )
            ok = False
            continue
        sheets[sheet_title] = df

    # The reference sheet is optional: it is only checked for (ignored) edits.
    if REFERENCE_SHEET in raw:
        df, _ = _canonical_frame(raw[REFERENCE_SHEET])
        if df is not None:
            sheets[REFERENCE_SHEET] = df

    return sheets if ok else None


def scan_cell_errors(workbook_path: Path, reporter: Reporter) -> None:
    """
    Report cells that hold an Excel error value (e.g. #NAME?). They come from
    text Excel read as a formula -- a description starting with '=' -- and
    would otherwise be read as empty cells and silently dropped.
    """
    wb = openpyxl.load_workbook(str(workbook_path), data_only=True)
    try:
        for sheet_title in CLASS_MAP:
            if sheet_title not in wb.sheetnames:
                continue
            for row in wb[sheet_title].iter_rows(min_row=2):
                for cell in row:
                    if cell.data_type == "e":
                        reporter.error(
                            sheet_title, f"cell {cell.coordinate}",
                            f"Excel shows an error value (`{cell.value}`) instead of text.",
                            hint="This happens when a cell starts with `=`, `+` or `-`: "
                                 "Excel reads it as a formula. Type an apostrophe "
                                 "first (e.g. `'=…`) so Excel keeps it as text.",
                        )
    finally:
        wb.close()


def parse_excel(
    sheets: dict[str, pd.DataFrame],
) -> dict[str, list[dict[str, Any]]]:
    """Normalise validated DataFrames into row dicts (see workbook_rows.FIELDS)."""
    result: dict[str, list[dict[str, Any]]] = {}
    for sheet_title, df in sheets.items():
        rows: list[dict[str, Any]] = []
        for idx, raw in df.iterrows():
            row = normalise_row({
                "label":           raw.get("label"),
                "type":            raw.get("type"),
                "domain":          raw.get("domain"),
                "mro":             raw.get("M / R / O"),
                "range":           raw.get("range"),
                "multivalued":     raw.get("multivalued"),
                "inlined_as_list": raw.get("inlined as list"),
                "unit":            raw.get("unit"),
                "uri":             raw.get("uri"),
                "description":     raw.get("description"),
            })
            if not row["label"]:
                continue
            with contextlib.suppress(TypeError, ValueError):
                row["_row"] = int(idx) + 2   # Excel row number (header is row 1)
            rows.append(row)
        result[sheet_title] = rows
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Validation helpers
# ─────────────────────────────────────────────────────────────────────────────

_IRI_RE   = re.compile(r"^https?://\S+$")
_CURIE_RE = re.compile(r"^([A-Za-z_][\w.-]*):(\S+)$")
_DATE_RE  = re.compile(r"^\d{4}-\d{2}-\d{2}([ T]\d{2}:\d{2}(:\d{2}(\.\d+)?)?)?$")

_URI_HINT = (
    "Use a CURIE with a prefix the schema declares (e.g. `voc4cat:0000123`, "
    "`CHMO:0000123`) or a full `https://` IRI."
)
_UNIT_HINT = (
    "Use a UCUM code such as `Cel`, `K`, `bar`, `h`, `mol/L` or `m2/g`. If Excel "
    "changes what you type, format the cell as Text first."
)


def _valid_range(
    range_val: str,
    schema: dict,
    pending_class_names: set[str] | None = None,
    sv=None,
) -> bool:
    if not range_val:
        return True
    if (range_val in PRIMITIVE_TYPES or range_val in schema.get("classes", {})
            or range_val in (schema.get("enums") or {})):
        return True
    if pending_class_names and range_val in pending_class_names:
        return True
    if sv is not None:
        with contextlib.suppress(Exception):
            if (sv.get_class(range_val) is not None or sv.get_enum(range_val) is not None
                    or sv.get_type(range_val) is not None):
                return True
    return False


def _range_hint(schema: dict) -> str:
    prims = ", ".join(f"`{t}`" for t in sorted(PRIMITIVE_TYPES))
    known = sorted(schema.get("classes", {}).keys())[:20]
    classes_str = ", ".join(f"`{c}`" for c in known)
    suffix = " (…)" if len(schema.get("classes", {})) > 20 else ""
    return (
        f"Valid primitive types: {prims}. "
        f"Known schema classes (first 20): {classes_str}{suffix}."
    )


def _uri_problem(value: str, prefixes: set[str]) -> str | None:
    """Why value is not a usable slot/class URI, or None if it is."""
    if _IRI_RE.match(value):
        return None
    match = _CURIE_RE.match(value)
    if not match:
        return "is neither a CURIE (`prefix:id`) nor an `http(s)://` IRI."
    prefix = match.group(1)
    if prefix in prefixes:
        return None
    close = sorted(p for p in prefixes if p.lower() == prefix.lower())
    suggestion = f" Did you mean `{close[0]}:`?" if close else ""
    return f"uses the prefix `{prefix}:`, which the schema does not declare.{suggestion}"


def _unit_problem(value: str) -> str | None:
    """Why value is not a plausible UCUM code, or None if it is (or is empty)."""
    if not value:
        return None
    if _DATE_RE.match(value):
        return "looks like a date — Excel probably converted what you typed (e.g. `1/2`)."
    if any(ch.isspace() for ch in value):
        return "contains spaces, which UCUM codes never do."
    if any(not 33 <= ord(ch) <= 126 for ch in value):
        return "contains characters outside plain ASCII (UCUM writes `Cel`, not `°C`)."
    return None


def _short(value: Any, limit: int = 60) -> str:
    text = str(value).replace("\n", " ")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _fields_text(fields: list[str]) -> str:
    return ", ".join(f"*{FIELD_LABELS.get(f, f)}*" for f in fields)


# ─────────────────────────────────────────────────────────────────────────────
# LinkML inheritance helpers
# ─────────────────────────────────────────────────────────────────────────────


def _slot_level_value(sv, slot_name: str, key: str, include_self: bool = True) -> bool:
    """
    A flag's value from the slot definition and its parent slots. LinkML
    (SchemaView.induced_slot) only passes *true* values down the slot
    hierarchy, so the flag is set as soon as any of them sets it -- an
    explicit `false` on a child slot does not switch off a parent's `true`.
    Only a class's slot_usage can do that.
    """
    try:
        names = sv.slot_ancestors(slot_name, reflexive=include_self)
    except Exception:  # noqa: BLE001
        return False
    for name in names:
        slot = sv.get_slot(name)
        if slot is not None and getattr(slot, key, None):
            return True
    return False


def _needs_class_override(sv, f: str, value: str, slot_name: str) -> bool:
    """
    True if writing `value` into the slot definition would not take effect:
    it switches off a flag a parent slot sets (see _slot_level_value).
    """
    if f == "mro":
        keys = {"M": (), "R": ("required",), "O": ("required", "recommended")}.get(value, ())
    elif f in ("multivalued", "inlined_as_list"):
        keys = () if value == "yes" else (f,)
    else:
        return False
    return any(_slot_level_value(sv, slot_name, k, include_self=False) for k in keys)


def _class_level_value(sv, slot_name: str, class_name: str, key: str) -> bool:
    """
    The value class_name would get for a flag if its own slot_usage did not
    set it: the nearest ancestor's slot_usage, else the slot definition chain.
    """
    try:
        ancestors = sv.class_ancestors(class_name, reflexive=False)
    except Exception:  # noqa: BLE001
        ancestors = []
    for name in ancestors:
        cls = sv.get_class(name)
        usage = (cls.slot_usage or {}).get(slot_name) if cls is not None else None
        value = getattr(usage, key, None) if usage is not None else None
        if value is not None:
            return bool(value)
    return _slot_level_value(sv, slot_name, key, include_self=True)


def _ancestor_usage_sets(sv, slot_name: str, class_name: str, keys: tuple[str, ...]) -> bool:
    """True if a class ancestor's slot_usage sets one of keys for slot_name."""
    try:
        ancestors = sv.class_ancestors(class_name, reflexive=False)
    except Exception:  # noqa: BLE001
        return False
    for name in ancestors:
        cls = sv.get_class(name)
        usage = (cls.slot_usage or {}).get(slot_name) if cls is not None else None
        if usage is not None and any(getattr(usage, k, None) is not None for k in keys):
            return True
    return False


def _is_identifier(sv, slot_name: str, class_name: str | None) -> bool:
    with contextlib.suppress(Exception):
        ind = sv.induced_slot(slot_name, class_name)
        return bool(ind.identifier or ind.key)
    return False


# ─────────────────────────────────────────────────────────────────────────────
# Change planning
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class _Plan:
    """State shared by the per-row planners of one plan_changes() call."""
    schema: dict
    sv: Any
    label_to_slot: dict[str, str]
    label_to_class: dict[str, str]
    slot_origin: dict[str, Path]
    class_origin: dict[str, Path]
    reporter: Reporter
    changes: list[dict[str, Any]] = field(default_factory=list)
    # New slots planned so far (name -> its slot_add change). A new field
    # listed on several classes gets ONE global definition and is attached to
    # every further class instead of being re-added.
    planned_new_slots: dict[str, dict[str, Any]] = field(default_factory=dict)
    _docs: dict[Path, dict] = field(default_factory=dict)
    _prefixes: set[str] | None = None
    _current: dict[str, list[dict]] | None = None

    def doc(self, path: Path) -> dict:
        if path not in self._docs:
            self._docs[path] = load_yaml_file(str(path)) or {}
        return self._docs[path]

    def class_node(self, class_name: str) -> dict | None:
        """The class as written in its own module, or None if not editable."""
        path = self.class_origin.get(class_name)
        if path is None:
            return None
        return (self.doc(path).get("classes") or {}).get(class_name) or {}

    def own_usage(self, class_name: str, slot_name: str) -> dict | None:
        node = self.class_node(class_name)
        usage = (node or {}).get("slot_usage") or {}
        if slot_name not in usage:
            return None
        return usage.get(slot_name) or {}

    def own_slots(self, class_name: str) -> list[str]:
        return list((self.class_node(class_name) or {}).get("slots") or [])

    def prefixes(self) -> set[str]:
        if self._prefixes is None:
            known = set((self.schema.get("prefixes") or {}).keys())
            with contextlib.suppress(Exception):
                for schema in self.sv.all_schema():
                    known.update((schema.prefixes or {}).keys())
            self._prefixes = known
        return self._prefixes

    def current_rows(self) -> dict[str, list[dict]]:
        if self._current is None:
            self._current = generate_rows(SCHEMA_DIR)
        return self._current


def plan_changes(
    schema: dict,
    excel_data: dict[str, list[dict]],
    label_to_slot: dict[str, str],
    label_to_class: dict[str, str],
    slot_origin: dict[str, Path],
    class_origin: dict[str, Path],
    reporter: Reporter,
    *,
    baseline: dict[str, dict] | None = None,
    sv=None,
) -> list[dict[str, Any]]:
    """
    Diff the Excel data against the merged schema and return validated change
    dicts ready to apply. Unresolvable issues are recorded on reporter.

    With `baseline` (the workbook's _baseline sheet, see read_baseline) only
    the rows and fields that differ from it are planned, and rows missing
    from it are planned as removals. Without it every field of every row is
    compared with the current schema.
    """
    plan = _Plan(
        schema=schema,
        sv=sv if sv is not None else load_schema_view(SCHEMA_DIR),
        label_to_slot=label_to_slot,
        label_to_class=label_to_class,
        slot_origin=slot_origin,
        class_origin=class_origin,
        reporter=reporter,
    )
    for sheet_title, rows in excel_data.items():
        base_idx = None if baseline is None else baseline.get(sheet_title, {})
        if sheet_title == REFERENCE_SHEET:
            _check_reference_sheet(plan, rows, base_idx)
        elif sheet_title in CLASS_MAP:
            _plan_sheet(plan, sheet_title, rows, base_idx)
    return plan.changes


def _plan_sheet(p: _Plan, sheet: str, rows: list[dict], base_idx: dict | None) -> None:
    schema_class = CLASS_MAP[sheet]
    pending = _collect_pending_classes(rows, p.label_to_class)

    # One row per (label, domain): a second, different row with the same key
    # would be ambiguous.
    unique: list[dict] = []
    by_key: dict[tuple[str, str], dict] = {}
    for row in rows:
        key = row_key(row)
        first = by_key.get(key)
        if first is None:
            by_key[key] = row
            unique.append(row)
        elif changed_fields(row, first):
            p.reporter.error(
                sheet, f"{row['type']} '{row['label']}'",
                f"Appears twice with the same domain "
                f"(`{row['domain'] or 'top level'}`, rows {first.get('_row', '?')} "
                f"and {row.get('_row', '?')}) but with different values.",
                hint="Keep one row per field and class.",
            )

    for row in unique:
        base = base_idx.get(row_key(row)) if base_idx is not None else None
        fields: list[str] | None = None   # None: every field counts
        if base is not None:
            fields = changed_fields(row, base)
            if not fields:
                continue                  # untouched since the download
            if "type" in fields:
                p.reporter.warning(
                    sheet, f"row '{row['label']}'",
                    "Not applied: the *type* of an existing row (slot or class) "
                    "can't be changed.",
                    hint="Add a new row instead.",
                )
                continue

        if row["type"] == "slot":
            _plan_slot_row(p, sheet, schema_class, row, base, fields, pending)
        elif row["type"] == "class":
            _plan_class_row(p, sheet, schema_class, row, base, fields, pending)
        else:
            p.reporter.error(
                sheet, f"row '{row['label']}'",
                f"Invalid type `{row['type']}`. Use **slot** or **class**.",
            )

    if base_idx is None:
        _plan_legacy_deletions(p, sheet, schema_class, unique)
    else:
        _plan_removed_rows(p, sheet, schema_class, unique, base_idx, pending)


# ── slots ──────────────────────────────────────────────────────────────────


def _plan_slot_row(
    p: _Plan,
    sheet: str,
    schema_class: str,
    row: dict,
    base: dict | None,
    fields: list[str] | None,
    pending: dict[str, str],
) -> None:
    label, domain = row["label"], row["domain"]
    classes = p.schema.get("classes", {})
    effective_class = (
        _resolve_domain_class(domain, p.label_to_class, pending) if domain else schema_class
    )

    slot_name = p.label_to_slot.get(label)
    if slot_name is None and domain:
        # A slot_usage-only or inherited slot of the domain class whose name
        # is not a global slot (e.g. has_concentration on CoPrecipitation).
        derived = _label_to_slot_name(label)
        cdef = classes.get(effective_class) or {}
        if derived in (cdef.get("slot_usage") or {}) or (
            effective_class in classes and derived in get_all_class_slots(p.schema, effective_class)
        ):
            slot_name = derived

    if slot_name is None:
        _plan_new_slot(p, sheet, schema_class, row, pending)
    elif not _class_has_slot(p.schema, effective_class, slot_name, pending):
        # An existing slot listed on a class that does not have it yet
        # (typically a class that is new in this submission).
        _plan_slot_attach(p, sheet, row, slot_name, effective_class, pending)
    else:
        _plan_slot_changes(p, sheet, row, slot_name, effective_class, base, fields)


def _slot_owner_classes(schema: dict, slot_name: str) -> list[str]:
    """
    Every class that directly references slot_name, via its own slots: list
    or a slot_usage entry. Used to warn when an edit changes the slot's
    single, global definition for every other class that uses it too.
    """
    owners: list[str] = []
    for cname, cdef in schema.get("classes", {}).items():
        if not isinstance(cdef, dict):
            continue
        if slot_name in (cdef.get("slots") or []) or slot_name in (cdef.get("slot_usage") or {}):
            owners.append(cname)
    return owners


def _slot_target(p: _Plan, f: str, slot_name: str, cls: str) -> tuple[str, Path, str | None] | None:
    """
    Where a change to field f of slot_name on class cls is written:
    ("usage", file, cls) for cls's existing slot_usage entry, ("new_usage",
    file, cls) for a new one, ("global", file, None) for the slot definition,
    or None if it can't be applied.
    """
    own_usage = p.own_usage(cls, slot_name)
    class_file = p.class_origin.get(cls)
    slot_file = p.slot_origin.get(slot_name)
    shared = any(c != cls for c in _slot_owner_classes(p.schema, slot_name))

    if f == "mro":
        # M/R/O is per class: scope it to this class unless the slot belongs
        # to this class alone and nothing above it overrides M/R/O.
        if own_usage is not None:
            return ("usage", class_file, cls)
        overridden = _ancestor_usage_sets(p.sv, slot_name, cls, ("required", "recommended"))
        if not shared and not overridden and slot_file:
            return ("global", slot_file, None)
        if class_file:
            return ("new_usage", class_file, cls)
        return ("global", slot_file, None) if slot_file else None

    key = _YAML_KEY[f]
    if f in ("uri", "unit"):
        if own_usage is not None and key in own_usage:
            return ("usage", class_file, cls)
        return ("global", slot_file, None) if slot_file else None

    # description, range, multivalued, inlined_as_list
    if own_usage is not None:
        return ("usage", class_file, cls)
    if _ancestor_usage_sets(p.sv, slot_name, cls, (key,)):
        # Set by a parent class's slot_usage: override it for this class.
        return ("new_usage", class_file, cls) if class_file else None
    return ("global", slot_file, None) if slot_file else None


def _inherited_flags(p: _Plan, f: str, slot_name: str, where: str, owner: str | None) -> dict[str, bool]:
    """What the written node would inherit for each flag if it left it unset."""
    keys = {"mro": ("required", "recommended"),
            "multivalued": ("multivalued",),
            "inlined_as_list": ("inlined_as_list",)}.get(f, ())
    if where == "global":
        return {k: _slot_level_value(p.sv, slot_name, k, include_self=False) for k in keys}
    return {k: _class_level_value(p.sv, slot_name, owner, k) for k in keys}


def _typed_value(f: str, value: str) -> Any:
    if f in ("multivalued", "inlined_as_list"):
        return value == "yes"
    return value


def _plan_slot_changes(
    p: _Plan,
    sheet: str,
    row: dict,
    slot_name: str,
    cls: str,
    base: dict | None,
    fields: list[str] | None,
) -> None:
    reporter = p.reporter
    vals = slot_row_values(p.sv, slot_name, cls)
    if vals is None:   # SchemaView doesn't know the slot: compare with the YAML as written
        vals = _raw_row_values(p.schema, slot_name, cls, None)
    current = normalise_row({**vals, "label": row["label"], "domain": row["domain"]})

    candidates = [f for f in (fields if fields is not None else VALUE_FIELDS) if f != "type"]
    diffs = [f for f in candidates if row[f] != current[f]]
    if not diffs:
        return

    context = f"slot `{slot_name}`"
    if slot_name not in p.slot_origin:
        reporter.warning(
            sheet, f"slot '{row['label']}'",
            f"Not applied: `{slot_name}` is inherited from a chemdcat-ap base class "
            f"and is read-only here, so your change to {_fields_text(diffs)} was ignored.",
            hint="Ask a maintainer to change it in the YAML directly, or open an issue.",
        )
        return

    global_fields: list[str] = []
    for f in diffs:
        new, cur = row[f], current[f]

        # An empty description/URI/range cell means "keep".
        if f in ("description", "uri", "range") and not new:
            if fields is not None:
                reporter.warning(
                    sheet, context,
                    f"Not applied: you cleared the *{FIELD_LABELS[f]}* of `{slot_name}` "
                    f"({cls}); removing it is not supported here.",
                    hint="Ask a maintainer if it really should be removed.",
                )
            continue

        if f == "mro":
            if new not in ("M", "R", "O"):
                reporter.error(
                    sheet, context,
                    f"Invalid M/R/O value `{new!r}`. "
                    f"Only **M** (Mandatory), **R** (Recommended), or **O** (Optional) are accepted.",
                )
                continue
            if new != "M" and _is_identifier(p.sv, slot_name, cls):
                reporter.error(
                    sheet, context,
                    f"`{slot_name}` identifies the record and is always **M** (Mandatory).",
                )
                continue
        elif f == "range" and not _valid_range(new, p.schema, sv=p.sv):
            reporter.error(
                sheet, context,
                f"Unknown range `{new}`. This type is not a recognized primitive or schema class.",
                hint=_range_hint(p.schema),
            )
            continue
        elif f == "uri" and (problem := _uri_problem(new, p.prefixes())):
            reporter.error(sheet, context, f"The URI `{new}` {problem}", hint=_URI_HINT)
            continue
        elif f == "unit" and (problem := _unit_problem(new)):
            reporter.error(sheet, context, f"The unit `{new}` {problem}", hint=_UNIT_HINT)
            continue
        elif f == "inlined_as_list" and new == "yes" \
                and p.sv.get_class(row["range"] or current["range"]) is None:
            reporter.warning(
                sheet, context,
                "Not applied: *inlined as list* only applies to fields whose range is a class.",
            )
            continue

        target = _slot_target(p, f, slot_name, cls)
        if target is not None and target[0] == "global" and _needs_class_override(p.sv, f, new, slot_name):
            # Switching off a flag a parent slot sets only works in slot_usage.
            class_file = p.class_origin.get(cls)
            target = None if class_file is None else (
                "usage" if p.own_usage(cls, slot_name) is not None else "new_usage", class_file, cls,
            )
        if target is None:
            reporter.warning(
                sheet, context,
                f"Not applied: the *{FIELD_LABELS[f]}* of `{slot_name}` can't be changed "
                f"for `{cls}` through the workbook.",
                hint="Ask a maintainer to change it in the YAML directly.",
            )
            continue
        where, path, owner = target

        if base is not None and base.get(f, "") != cur:
            reporter.warning(
                sheet, context,
                f"Conflict: the *{FIELD_LABELS[f]}* of `{slot_name}` ({cls}) was also "
                f"changed in the schema after you downloaded the workbook (it is now "
                f"`{_short(cur)}`). Your value `{_short(new)}` is applied.",
                hint="Check that this is still what you want.",
            )
        if f == "range":
            reporter.warning(
                sheet, context,
                f"Range changed: `{cur}` → `{new}`. "
                f"This structural change may invalidate existing data files.",
                hint="The test suite will verify this automatically. "
                     "A maintainer will review before merging.",
            )

        p.changes.append({
            "type":         _CHANGE_TYPE[f],
            "name":         slot_name,
            "schema_class": cls,
            "field":        f,
            "value":        _typed_value(f, new),
            "mro":          new if f == "mro" else None,
            "_where":       where,
            "_target":      path,
            "_owner":       owner,
            "_inherited":   _inherited_flags(p, f, slot_name, where, owner),
            "_expect":      [(sheet, row_key(row), f, new, True)],
        })
        if where == "global":
            global_fields.append(f)

    if global_fields:
        owners = [c for c in _slot_owner_classes(p.schema, slot_name) if c != cls]
        if owners:
            owners_str = ", ".join(f"`{c}`" for c in sorted(owners))
            reporter.warning(
                sheet, context,
                f"This edit changes `{slot_name}`'s single, global definition "
                f"-- it is not scoped to `{cls}` alone. It will also "
                f"change `{slot_name}` for: {owners_str}.",
                hint="If you only meant to change it for this class, a "
                     "maintainer needs to add a slot_usage override for "
                     f"`{slot_name}` on `{cls}` first, rather than "
                     "editing the global slot.",
            )


def _mro_slot_usage(base_required: bool, base_recommended: bool, mro: str) -> dict[str, bool]:
    """
    slot_usage keys needed so that a slot whose shared definition has the
    given required/recommended flags ends up as `mro` on one specific class.
    Empty if the shared definition already matches.
    """
    su: dict[str, bool] = {}
    if (mro == "M") != base_required:
        su["required"] = mro == "M"
    if mro != "M" and (mro == "R") != base_recommended:
        su["recommended"] = mro == "R"
    return su


def _row_definition(row: dict) -> dict[str, Any]:
    """The definition-level (class-independent) fields of a workbook row."""
    return {
        "range":           row["range"] or DEFAULT_RANGE,
        "uri":             row["uri"],
        "description":     row["description"],
        "multivalued":     row["multivalued"] == "yes",
        "inlined_as_list": row["inlined_as_list"] == "yes",
        "unit":            row["unit"],
    }


def _slot_definition(slot_def: dict) -> dict[str, Any]:
    """The same fields as _row_definition, read from a schema slot dict."""
    return {
        "range":           _str(slot_def.get("range", "")) or DEFAULT_RANGE,
        "uri":             _str(slot_def.get("slot_uri", "")),
        "description":     _str(slot_def.get("description", "")),
        "multivalued":     bool(slot_def.get("multivalued", False)),
        "inlined_as_list": bool(slot_def.get("inlined_as_list", False)),
        "unit":            _str((slot_def.get("unit") or {}).get("ucum_code", "")),
    }


def _effective_definition(p: _Plan, slot_name: str) -> dict[str, Any]:
    """_slot_definition with the values LinkML uses (slot inheritance included)."""
    vals = slot_row_values(p.sv, slot_name, None)
    if vals is None:
        return _slot_definition(get_slot_details(p.schema, slot_name))
    return _row_definition(normalise_row(vals))


def _definition_diffs(row: dict, reference: dict[str, Any]) -> list[str]:
    """
    Names of definition fields where the row differs from `reference`.
    An empty range/URI/description cell means "keep".
    """
    diffs: list[str] = []
    for key, value in _row_definition(row).items():
        if key in ("range", "uri", "description") and not row[key]:
            continue
        if value != reference[key]:
            diffs.append(key)
    return diffs


def _plan_slot_attach(
    p: _Plan,
    sheet: str,
    row: dict,
    slot_name: str,
    class_name: str,
    pending: dict[str, str],
) -> None:
    """
    Plan attaching an EXISTING slot to a class that does not have it yet
    (most commonly a class that is new in this same submission).

    The slot keeps its single, shared definition. Only a differing M/R/O is
    applied, scoped to this class via slot_usage; any other differing field
    is reported but not applied, because it would silently change the slot
    for every other class that uses it.
    """
    reporter = p.reporter
    label = row["label"]
    classes = p.schema.get("classes", {})
    is_pending = class_name not in classes and class_name in pending

    if not is_pending and class_name not in classes:
        reporter.error(
            sheet, f"slot '{label}'",
            f"The domain `{row['domain']}` is not a recognised class. "
            f"Set the domain column to an existing class label, or to a class "
            f"added in this same workbook.",
            hint="Look at the class rows in this sheet for valid domain names.",
        )
        return
    if not is_pending and class_name not in p.class_origin:
        reporter.warning(
            sheet, f"slot `{slot_name}`",
            f"Not attached to `{class_name}`: it is a chemdcat-ap base class "
            f"and is not modifiable via the inbox workflow.",
            hint="Ask a maintainer to edit the YAML directly.",
        )
        return

    mro = row["mro"]
    if mro not in ("M", "R", "O"):
        reporter.error(
            sheet, f"slot `{slot_name}`",
            f"Invalid M/R/O value `{mro!r}`. "
            f"Only **M** (Mandatory), **R** (Recommended), or **O** (Optional) are accepted.",
        )
        return

    slot_usage = _mro_slot_usage(
        _slot_level_value(p.sv, slot_name, "required") or _is_identifier(p.sv, slot_name, None),
        _slot_level_value(p.sv, slot_name, "recommended"),
        mro,
    )

    diffs = _definition_diffs(row, _effective_definition(p, slot_name))
    if diffs:
        reporter.warning(
            sheet, f"slot `{slot_name}`",
            f"Attached to `{class_name}` with its existing shared definition. "
            f"Your row differs in: {', '.join(diffs)} -- these differences were "
            f"**not** applied, because they would change `{slot_name}` for "
            f"every class that uses it.",
            hint="If the shared definition should change, edit the slot's "
                 "existing row in its original class, or ask a maintainer.",
        )

    reporter.info(
        sheet, f"slot `{slot_name}`",
        f"Will attach existing slot `{slot_name}` to `{class_name}`.",
    )
    domain_label = class_name if row["domain"] else ""
    p.changes.append({
        "type":         "slot_attach",
        "name":         slot_name,
        "schema_class": class_name,
        "mro":          mro,
        "slot_usage":   slot_usage,
        "_target":      _resolve_class_target(class_name, p.class_origin, pending),
        "_expect":      [(sheet, (snake_to_readable(slot_name), domain_label), "mro", mro, False)],
    })


def _plan_new_slot(
    p: _Plan,
    sheet: str,
    schema_class: str,
    row: dict,
    pending: dict[str, str],
) -> None:
    reporter = p.reporter
    label     = row["label"]
    domain    = row["domain"]
    slot_name = _label_to_slot_name(label)
    classes   = p.schema.get("classes", {})

    # Resolve the class that will own the new slot:
    #   • empty domain     → the sheet's top-level data class (schema_class)
    #   • non-empty domain → the named (sub)class, which may also be a class
    #                        proposed as new in this same submission
    if domain:
        owner_class = _resolve_domain_class(domain, p.label_to_class, pending)
        if owner_class not in classes and owner_class not in pending:
            reporter.error(
                sheet, f"new slot '{label}'",
                f"The domain `{domain}` is not a recognised class. "
                f"Set the domain column to an existing class label, or leave it "
                f"empty to add a top-level slot.",
                hint="Look at the class rows in this sheet for valid domain names.",
            )
            return
        if owner_class in classes and owner_class not in p.class_origin:
            reporter.error(
                sheet, f"new slot '{label}'",
                f"`{owner_class}` is a chemdcat-ap base class and is not "
                f"modifiable via the inbox workflow, so no new slot can be "
                f"added to it.",
                hint="Assign the new slot to a CoreMeta4Cat class, or ask a "
                     "maintainer to edit the YAML directly.",
            )
            return
    else:
        owner_class = schema_class
    expect_key = (snake_to_readable(slot_name), owner_class if domain else "")

    # Same new slot already planned earlier in this submission: one shared
    # definition, attached to every further class. Only M/R/O may differ.
    if slot_name in p.planned_new_slots:
        first = p.planned_new_slots[slot_name]
        diffs = _definition_diffs(row, {
            "range":           first["range"],
            "uri":             first["uri"],
            "description":     first["description"],
            "multivalued":     first["multivalued"],
            "inlined_as_list": first["inlined_as_list"],
            "unit":            first["unit"],
        })
        if diffs:
            reporter.error(
                sheet, f"new slot '{label}'",
                f"`{slot_name}` appears in several rows of this workbook with "
                f"different values for: {', '.join(diffs)}. A field has one "
                f"single definition shared by every class that uses it.",
                hint="Use identical range, URI, description, multivalued, "
                     "inlined-as-list and unit values in every row of this "
                     "field (only M/R/O may differ per class), or give the "
                     "rows different labels.",
            )
            return
        mro = row["mro"]
        if mro not in ("M", "R", "O"):
            reporter.error(
                sheet, f"new slot '{label}'",
                f"Invalid M/R/O value `{mro!r}`. Use M, R, or O.",
            )
            return
        if owner_class == first["schema_class"]:
            return  # duplicate row for the same class -- nothing more to do
        reporter.info(
            sheet, f"new slot `{slot_name}`",
            f"Will also attach `{slot_name}` to `{owner_class}`.",
        )
        p.changes.append({
            "type":         "slot_attach",
            "name":         slot_name,
            "schema_class": owner_class,
            "mro":          mro,
            "slot_usage":   _mro_slot_usage(first["mro"] == "M", first["mro"] == "R", mro),
            "_target":      _resolve_class_target(owner_class, p.class_origin, pending),
            "_expect":      [(sheet, expect_key, "mro", mro, False)],
        })
        return

    if slot_name in p.schema.get("slots", {}):
        existing_label = snake_to_readable(slot_name)
        reporter.error(
            sheet, f"new slot '{label}'",
            f"The derived slot name `{slot_name}` conflicts with the existing "
            f"slot **{existing_label}**. "
            f"To modify that slot, edit its existing row; do not add a new row.",
            hint="Use a more specific label so the derived name does not clash.",
        )
        return

    mro = row["mro"]
    if mro not in ("M", "R", "O"):
        reporter.error(
            sheet, f"new slot '{label}'",
            f"Invalid M/R/O value `{mro!r}`. Use M, R, or O.",
        )
        return

    range_val = row["range"] or DEFAULT_RANGE
    if not _valid_range(range_val, p.schema, set(pending), sv=p.sv):
        reporter.error(
            sheet, f"new slot '{label}'",
            f"Unknown range `{range_val}` for new slot.",
            hint=_range_hint(p.schema),
        )
        return
    if row["uri"] and (problem := _uri_problem(row["uri"], p.prefixes())):
        reporter.error(sheet, f"new slot '{label}'", f"The URI `{row['uri']}` {problem}", hint=_URI_HINT)
        return
    if problem := _unit_problem(row["unit"]):
        reporter.error(sheet, f"new slot '{label}'", f"The unit `{row['unit']}` {problem}", hint=_UNIT_HINT)
        return

    inlined = row["inlined_as_list"] == "yes"
    if inlined and range_val not in classes and range_val not in pending \
            and p.sv.get_class(range_val) is None:
        reporter.warning(
            sheet, f"new slot '{label}'",
            "*inlined as list* was ignored: it only applies to fields whose range is a class.",
        )
        inlined = False
    if not row["description"]:
        reporter.warning(
            sheet, f"new slot '{label}'",
            "Has no description. Please add one, so others know what to record here.",
        )

    target = _resolve_class_target(owner_class, p.class_origin, pending)
    reporter.info(
        sheet, f"new slot `{slot_name}`",
        f"Will add `{slot_name}` to `{owner_class}`.",
    )
    expected = {
        "mro": mro, "range": range_val, "multivalued": row["multivalued"],
        "inlined_as_list": "yes" if inlined else "", "unit": row["unit"],
        "uri": row["uri"], "description": row["description"],
    }
    change = {
        "type":            "slot_add",
        "name":            slot_name,
        "label":           label,
        "schema_class":    owner_class,
        "range":           range_val,
        "mro":             mro,
        "description":     row["description"],
        "uri":             row["uri"],
        "multivalued":     row["multivalued"] == "yes",
        "inlined_as_list": inlined,
        "unit":            row["unit"],
        "_target":         target,
        "_expect":         [(sheet, expect_key, f, v, False) for f, v in expected.items()],
    }
    p.changes.append(change)
    p.planned_new_slots[slot_name] = change


# ── classes ────────────────────────────────────────────────────────────────


def _plan_class_row(
    p: _Plan,
    sheet: str,
    schema_class: str,
    row: dict,
    base: dict | None,
    fields: list[str] | None,
    pending: dict[str, str],
) -> None:
    reporter = p.reporter
    label = row["label"]
    class_name = p.label_to_class.get(label)
    if class_name is None:
        _plan_new_class(p, sheet, schema_class, row, pending)
        return

    class_def = p.schema.get("classes", {}).get(class_name) or {}
    current = {
        "uri":         _str(class_def.get("class_uri", "")),
        "description": _str(class_def.get("description", "")),
    }
    if fields is not None:
        other = [f for f in fields if f not in ("uri", "description")]
        if other:
            reporter.warning(
                sheet, f"class '{label}'",
                f"Not applied: the {_fields_text(other)} of a class row only repeat(s) "
                f"the slot it belongs to.",
                hint="Change the slot row above it instead.",
            )
    candidates = [f for f in (fields if fields is not None else ("uri", "description"))
                  if f in ("uri", "description")]
    diffs = [f for f in candidates if row[f] != current[f]]
    if not diffs:
        return

    if class_name not in p.class_origin:
        reporter.warning(
            sheet, f"class '{label}'",
            f"Not applied: `{class_name}` is a chemdcat-ap base class and is "
            f"read-only here, so your change to {_fields_text(diffs)} was ignored.",
            hint="Ask a maintainer to change it in the YAML directly, or open an issue.",
        )
        return

    for f in diffs:
        new = row[f]
        if not new:
            if fields is not None:
                reporter.warning(
                    sheet, f"class `{class_name}`",
                    f"Not applied: you cleared the *{FIELD_LABELS[f]}* of `{class_name}`; "
                    f"removing it is not supported here.",
                    hint="Ask a maintainer if it really should be removed.",
                )
            continue
        if f == "uri" and (problem := _uri_problem(new, p.prefixes())):
            reporter.error(sheet, f"class `{class_name}`", f"The URI `{new}` {problem}", hint=_URI_HINT)
            continue
        if base is not None and base.get(f, "") != current[f]:
            reporter.warning(
                sheet, f"class `{class_name}`",
                f"Conflict: the *{FIELD_LABELS[f]}* of `{class_name}` was also changed "
                f"in the schema after you downloaded the workbook (it is now "
                f"`{_short(current[f])}`). Your value `{_short(new)}` is applied.",
                hint="Check that this is still what you want.",
            )
        p.changes.append({
            "type":    "class_uri" if f == "uri" else "class_description",
            "name":    class_name,
            "value":   new,
            "_target": p.class_origin[class_name],
            "_expect": [(sheet, row_key(row), f, new, True)],
        })


def _plan_new_class(
    p: _Plan,
    sheet: str,
    schema_class: str,
    row: dict,
    pending: dict[str, str],
) -> None:
    reporter   = p.reporter
    label      = row["label"]
    domain     = row["domain"]
    class_name = _label_to_class_name(label)

    if class_name in p.schema.get("classes", {}):
        reporter.error(
            sheet, f"new class '{label}'",
            f"A class named `{class_name}` already exists. "
            f"Edit its existing row to modify it.",
        )
        return

    if not domain:
        reporter.error(
            sheet, f"new class '{label}'",
            "New classes require a **domain** set to the parent class label.",
            hint="Look at the existing class rows in this sheet to find valid parent names.",
        )
        return

    # The parent may already exist, or be proposed as new elsewhere in this
    # same submission (pending).
    parent_name = p.label_to_class.get(domain)
    if parent_name is None and _label_to_class_name(domain) in pending:
        parent_name = _label_to_class_name(domain)
    if parent_name is None:
        reporter.error(
            sheet, f"new class '{label}'",
            f"The domain `{domain}` is not a recognised class label. "
            f"Set the domain column to the label of an existing parent class.",
            hint="Look at the existing class rows in this sheet to find valid parent names.",
        )
        return
    if row["uri"] and (problem := _uri_problem(row["uri"], p.prefixes())):
        reporter.error(sheet, f"new class '{label}'", f"The URI `{row['uri']}` {problem}", hint=_URI_HINT)
        return
    if not row["description"]:
        reporter.warning(
            sheet, f"new class '{label}'",
            "Has no description. Please add one, so others know what the class is for.",
        )

    target = _resolve_class_target(parent_name, p.class_origin, pending)
    reporter.info(
        sheet, f"new class `{class_name}`",
        f"Will add `{class_name}` as subclass of `{parent_name}`.",
    )
    p.changes.append({
        "type":         "class_add",
        "name":         class_name,
        "is_a":         parent_name,
        "schema_class": schema_class,
        "uri":          row["uri"],
        "description":  row["description"],
        "_target":      target,
    })


# ── removed rows ───────────────────────────────────────────────────────────


def _rename_hint(base: dict, added: list[dict]) -> str:
    """' (renamed to …?)' if an added row has the same domain and values."""
    for row in added:
        if (row["type"] == base["type"] and row["domain"] == base["domain"]
                and not changed_fields(row, base)):
            return (f" It looks like you renamed it to '{row['label']}': a rename is "
                    f"applied as adding the new field and removing the old one.")
    return ""


def _slot_source(p: _Plan, slot_name: str, cls: str) -> str:
    """The ancestor (or mixin) of cls that brings slot_name, for messages."""
    with contextlib.suppress(Exception):
        for name in p.sv.class_ancestors(cls, reflexive=False):
            cdef = p.sv.get_class(name)
            if cdef is not None and (slot_name in (cdef.slots or [])
                                     or slot_name in (cdef.slot_usage or {})):
                return name
    return "a parent class"


def _class_references(schema: dict, class_name: str) -> list[str]:
    """Everything that still points at class_name (subclasses, mixins, ranges)."""
    refs: list[str] = []
    for cname, cdef in schema.get("classes", {}).items():
        cdef = cdef or {}
        if cname == class_name:
            continue
        if cdef.get("is_a") == class_name:
            refs.append(f"subclass `{cname}`")
        if class_name in (cdef.get("mixins") or []):
            refs.append(f"`{cname}` (mixin)")
        for sname, usage in (cdef.get("slot_usage") or {}).items():
            if (usage or {}).get("range") == class_name:
                refs.append(f"`{cname}.{sname}` (range)")
    for sname, sdef in schema.get("slots", {}).items():
        if (sdef or {}).get("range") == class_name:
            refs.append(f"slot `{sname}` (range)")
    return refs


def _plan_removed_rows(
    p: _Plan,
    sheet: str,
    schema_class: str,
    rows: list[dict],
    base_idx: dict,
    pending: dict[str, str],
) -> None:
    """Rows in the baseline that the contributor deleted."""
    present = {row_key(r) for r in rows}
    class_labels = {r["label"] for r in rows if r["type"] == "class"}
    added = [r for r in rows if row_key(r) not in base_idx]
    current = index_rows(p.current_rows().get(sheet, []))

    for key, base in base_idx.items():
        if key in present or key not in current:
            continue   # still there, or already gone from the schema
        if base["type"] == "class":
            if base["label"] not in class_labels:   # not still listed under another slot
                _plan_class_removal(p, sheet, base)
        else:
            _plan_slot_removal(p, sheet, schema_class, base, added, pending)


def _plan_slot_removal(
    p: _Plan,
    sheet: str,
    schema_class: str,
    base: dict,
    added: list[dict],
    pending: dict[str, str],
) -> None:
    label, domain = base["label"], base["domain"]
    cls = _resolve_domain_class(domain, p.label_to_class, pending) if domain else schema_class
    slot_name = p.label_to_slot.get(label) or _label_to_slot_name(label)
    context = f"slot `{slot_name}`"

    if slot_name not in p.slot_origin or cls not in p.class_origin:
        p.reporter.warning(
            sheet, context,
            f"Not applied: you removed the row for `{slot_name}` on `{cls}`, but it "
            f"comes from a chemdcat-ap base class and is read-only here.",
            hint="Ask a maintainer to change it in the YAML directly, or open an issue.",
        )
        return

    if slot_name in p.own_slots(cls):
        p.reporter.warning(
            sheet, context,
            f"Present in the schema but **missing** from your workbook "
            f"(expected label: *{label}*). It will be removed from `{cls}`."
            + _rename_hint(base, added),
            hint="If accidental (e.g. you filtered rows before saving), "
                 "re-download the template and start again. "
                 "If intentional, the deletion is applied and the test suite "
                 "will verify no required fields are broken.",
        )
        p.changes.append({
            "type":           "slot_delete",
            "name":           slot_name,
            "schema_class":   cls,
            "_target":        p.class_origin[cls],
            "_expect_absent": [(sheet, row_key(base))],
        })
        return

    source = _slot_source(p, slot_name, cls)
    p.reporter.warning(
        sheet, context,
        f"Not applied: you removed the row for `{slot_name}` on `{cls}`, but `{cls}` "
        f"inherits it from `{source}`. It can only be removed there, which affects "
        f"every class that inherits it.",
        hint=f"Remove its row under `{source}` instead, or ask a maintainer.",
    )


def _plan_class_removal(p: _Plan, sheet: str, base: dict) -> None:
    class_name = p.label_to_class.get(base["label"])
    if class_name is None:
        return
    context = f"class `{class_name}`"
    if class_name not in p.class_origin:
        p.reporter.warning(
            sheet, context,
            f"Not applied: you removed the row for `{class_name}`, but it is a "
            f"chemdcat-ap base class and read-only here.",
            hint="Ask a maintainer to change it in the YAML directly, or open an issue.",
        )
        return
    if class_name in CLASS_MAP.values():
        p.reporter.warning(
            sheet, context,
            f"Not applied: `{class_name}` is one of the data classes and can't be "
            f"removed through the workbook.",
        )
        return
    refs = _class_references(p.schema, class_name)
    if refs:
        shown = ", ".join(refs[:8]) + (" …" if len(refs) > 8 else "")
        p.reporter.error(
            sheet, context,
            f"Can't remove `{class_name}`: it is still used by {shown}.",
            hint="Remove or move those first, or ask a maintainer.",
        )
        return
    p.reporter.warning(
        sheet, context,
        f"Present in the schema but **missing** from your workbook "
        f"(expected label: *{base['label']}*). It will be removed.",
        hint="If accidental, re-download the template. "
             "The maintainer will review deletions before merging.",
    )
    p.changes.append({
        "type":         "class_delete",
        "name":         class_name,
        "schema_class": CLASS_MAP[sheet],
        "_target":      p.class_origin[class_name],
    })


def _plan_legacy_deletions(p: _Plan, sheet: str, schema_class: str, rows: list[dict]) -> None:
    """
    Deletion detection without a baseline: top-level slots of the sheet class
    (and the classes they range over) that no row mentions.
    """
    schema = p.schema
    schema_slot_names: set[str] = set(get_all_class_slots(schema, schema_class))
    for su_name, _ in get_class_ranged_slot_usage(schema, schema_class):
        schema_slot_names.add(su_name)

    schema_class_names: set[str] = set()
    for slot_name in schema_slot_names:
        rng = get_slot_details(schema, slot_name).get("range", "")
        if rng and rng in schema.get("classes", {}):
            schema_class_names.add(rng)
            schema_class_names.update(get_subclasses(schema, rng))

    seen_slots: set[str] = set()
    seen_classes: set[str] = set()
    for row in rows:
        if row["type"] == "slot":
            name = p.label_to_slot.get(row["label"])
            seen_slots.add(name or _label_to_slot_name(row["label"]))
        elif row["type"] == "class":
            if row["domain"] and p.label_to_slot.get(row["domain"]):
                seen_slots.add(p.label_to_slot[row["domain"]])   # the parent slot row
            name = p.label_to_class.get(row["label"])
            if name:
                seen_classes.add(name)

    for slot_name in sorted(schema_slot_names):
        if slot_name not in p.slot_origin or slot_name in seen_slots:
            continue
        if slot_name not in p.own_slots(schema_class):
            p.reporter.warning(
                sheet, f"slot `{slot_name}`",
                f"Not applied: `{slot_name}` is missing from your workbook, but "
                f"`{schema_class}` inherits it from "
                f"`{_slot_source(p, slot_name, schema_class)}`, so it was not removed.",
            )
            continue
        p.reporter.warning(
            sheet, f"slot `{slot_name}`",
            f"Present in the schema but **missing** from your workbook "
            f"(expected label: *{snake_to_readable(slot_name)}*). "
            f"It will be removed from `{schema_class}`.",
            hint="If accidental (e.g. you filtered rows before saving), "
                 "re-download the template and start again. "
                 "If intentional, the deletion is applied and the test suite "
                 "will verify no required fields are broken.",
        )
        p.changes.append({
            "type":         "slot_delete",
            "name":         slot_name,
            "schema_class": schema_class,
            "_target":      p.class_origin.get(schema_class, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE),
        })

    for class_name in sorted(schema_class_names):
        if (class_name not in p.class_origin or class_name in seen_classes
                or class_name in CLASS_MAP.values()):   # never remove a data class itself
            continue
        p.reporter.warning(
            sheet, f"class `{class_name}`",
            f"Present in the schema but **missing** from your workbook "
            f"(expected label: *{snake_to_readable(class_name)}*). "
            f"It will be removed.",
            hint="If accidental, re-download the template. "
                 "The maintainer will review deletions before merging.",
        )
        p.changes.append({
            "type":         "class_delete",
            "name":         class_name,
            "schema_class": schema_class,
            "_target":      p.class_origin.get(class_name, SCHEMA_DIR / DEFAULT_NEW_ELEMENT_FILE),
        })


# ── reference sheet ────────────────────────────────────────────────────────


def _check_reference_sheet(p: _Plan, rows: list[dict], base_idx: dict | None) -> None:
    """Edits on the CoreMeta4Cat sheet are reported, never applied."""
    reference = base_idx if base_idx is not None else index_rows(
        p.current_rows().get(REFERENCE_SHEET, [])
    )
    submitted = index_rows(rows)
    edited = [k for k, r in submitted.items() if k not in reference or changed_fields(r, reference[k])]
    removed = [k for k in reference if k not in submitted]
    labels = sorted({k[0] for k in edited + removed})
    if labels:
        shown = ", ".join(f"*{label}*" for label in labels[:6]) + (" …" if len(labels) > 6 else "")
        p.reporter.warning(
            REFERENCE_SHEET, "sheet",
            f"Not applied: the {REFERENCE_SHEET} sheet is reference only, so your "
            f"changes to {len(labels)} row(s) ({shown}) were ignored.",
            hint="Propose changes to the CatalysisDataset fields in an issue, "
                 "or ask a maintainer.",
        )


# ─────────────────────────────────────────────────────────────────────────────
# Change application
# ─────────────────────────────────────────────────────────────────────────────


def _set_flag(node: Any, key: str, desired: bool, inherited: bool) -> None:
    """Leave key unset when inheritance already gives the desired value."""
    if desired == inherited:
        if key in node:
            del node[key]
    else:
        node[key] = desired


def _apply_mro(node: Any, mro: str, inherited: dict[str, bool]) -> None:
    """Set required/recommended on a slot or slot_usage node."""
    _set_flag(node, "required", mro == "M", inherited.get("required", False))
    if mro == "M":
        if "recommended" in node:
            del node["recommended"]   # required wins either way
    else:
        _set_flag(node, "recommended", mro == "R", inherited.get("recommended", False))


def _set_mro(node: dict, mro: str) -> None:
    """Set required/recommended on a slot or slot_usage node (no inheritance)."""
    _apply_mro(node, mro, {})


def _locate_slot_node(doc: Any, ch: dict) -> Any | None:
    """The YAML node a slot change is written to (created for "new_usage")."""
    name, where = ch["name"], ch["_where"]
    if where == "global":
        slots = doc.get("slots") or {}
        if name not in slots:
            return None
        if slots[name] is None:
            slots[name] = {}
        return slots[name]

    cls_name = ch.get("_owner") or ch["schema_class"]
    classes = doc.get("classes") or {}
    if cls_name not in classes:
        return None
    if classes[cls_name] is None:
        classes[cls_name] = {}
    cls_node = classes[cls_name]
    usage = cls_node.get("slot_usage")
    if usage is None:
        if where == "usage":
            return None
        cls_node["slot_usage"] = {}
        usage = cls_node["slot_usage"]
    if name not in usage:
        if where == "usage":
            return None
        usage[name] = {}
    elif usage[name] is None:
        usage[name] = {}
    return usage[name]


def _applied_text(ch: dict) -> str:
    target = Path(ch["_target"]).name
    via = {
        "global":    f"global slot in `{target}`",
        "usage":     f"slot_usage in `{target}`",
        "new_usage": f"new slot_usage on `{ch.get('_owner')}` in `{target}`",
    }[ch["_where"]]
    f, value = ch["field"], ch["value"]
    subject = f"`{ch['name']}` ({ch['schema_class']})"
    if f == "mro":
        return f"M/R/O → **{value}**: {subject} — {via}"
    if f == "description":
        return f"description updated: {subject} — via {via}"
    if f == "uri":
        return f"URI updated: {subject} — via {via}"
    if f == "range":
        return f"range changed → `{value}`: {subject} — via {via}"
    if f == "unit":
        shown = f"`{value}`" if value else "*(removed)*"
        return f"Unit → {shown}: {subject} — via {via}"
    return f"{f} → `{value}`: {subject} — via {via}"


def _apply_slot_value(ch: dict, reporter: Reporter) -> None:
    path = Path(ch["_target"])
    doc = _load_yaml(path)
    node = _locate_slot_node(doc, ch)
    if node is None:
        reporter.error(
            "schema", f"slot `{ch['name']}`",
            f"Could not update `{ch['name']}` ({ch['schema_class']}): the definition "
            f"to change is not in `{path.name}`. Nothing will be committed.",
            hint=_PIPELINE_HINT,
        )
        return

    f, value = ch["field"], ch["value"]
    inherited = ch.get("_inherited") or {}
    if f == "mro":
        _apply_mro(node, value, inherited)
    elif f in ("multivalued", "inlined_as_list"):
        _set_flag(node, f, bool(value), inherited.get(f, False))
    elif f == "description":
        node["description"] = _as_literal(value)
    elif f == "uri":
        node["slot_uri"] = value
    elif f == "range":
        node["range"] = value
    elif f == "unit":
        if value:
            node["unit"] = {"ucum_code": value}
        elif "unit" in node:
            del node["unit"]
    _save_yaml(path, doc)
    reporter.applied(_applied_text(ch))


def _append_slot_to_class(doc: Any, class_name: str, slot_name: str) -> Any | None:
    """
    Append slot_name to class_name's slots: list inside a loaded YAML doc.
    Returns the class node, or None if the class is not defined in this doc.
    """
    classes = doc.get("classes") or {}
    if class_name not in classes:
        return None
    if classes[class_name] is None:
        classes[class_name] = {}
    cls_node = classes[class_name]
    if "slots" not in cls_node or cls_node["slots"] is None:
        cls_node["slots"] = []
    if slot_name not in cls_node["slots"]:
        cls_node["slots"].append(slot_name)
    return cls_node


def _attach_failed(reporter: Reporter, slot_name: str, class_name: str, target: Path) -> None:
    reporter.error(
        "schema", f"slot `{slot_name}`",
        f"Could not attach `{slot_name}` to `{class_name}`: the class is not "
        f"defined in `{target.name}`. Nothing will be committed.",
        hint=_PIPELINE_HINT,
    )


def apply_changes(changes: list[dict], reporter: Reporter) -> None:
    """Apply all planned changes to YAML files (ruamel round-trip, comment-safe)."""

    # New classes first (slots can only be attached to an existing class
    # node), removed classes last; everything else keeps the workbook order.
    order = {"class_add": 0, "class_delete": 2}
    ordered = sorted(changes, key=lambda c: order.get(c["type"], 1))

    for ch in ordered:
        ctype = ch["type"]

        if ctype in _CHANGE_TYPE.values():
            _apply_slot_value(ch, reporter)

        elif ctype in ("class_description", "class_uri"):
            class_name = ch["name"]
            target     = ch.get("_target")
            if target:
                doc = _load_yaml(Path(target))
                classes = doc.get("classes") or {}
                if class_name in classes:
                    if classes[class_name] is None:
                        classes[class_name] = {}
                    if ctype == "class_description":
                        classes[class_name]["description"] = _as_literal(ch["value"])
                        reporter.applied(f"Class description updated: `{class_name}`")
                    else:
                        classes[class_name]["class_uri"] = ch["value"]
                        reporter.applied(f"Class URI updated: `{class_name}`")
                    _save_yaml(Path(target), doc)

        elif ctype == "slot_add":
            slot_name    = ch["name"]
            schema_class = ch["schema_class"]
            target       = Path(ch["_target"])
            mro          = ch["mro"]

            doc = _load_yaml(target)

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

            # The planner targets the module that defines (or will define)
            # the owner class; if the class is not there, fail loudly instead
            # of writing an orphaned slot.
            if _append_slot_to_class(doc, schema_class, slot_name) is None:
                _attach_failed(reporter, slot_name, schema_class, target)
                continue

            if "slots" not in doc or doc["slots"] is None:
                doc["slots"] = {}
            doc["slots"][slot_name] = slot_def

            _save_yaml(target, doc)
            reporter.applied(
                f"New slot `{slot_name}` added to `{schema_class}` "
                f"(M/R/O: {mro}, range: {ch['range']})"
            )

        elif ctype == "slot_attach":
            slot_name    = ch["name"]
            schema_class = ch["schema_class"]
            target       = Path(ch["_target"])

            doc = _load_yaml(target)
            cls_node = _append_slot_to_class(doc, schema_class, slot_name)
            if cls_node is None:
                _attach_failed(reporter, slot_name, schema_class, target)
                continue

            if ch.get("slot_usage"):
                if "slot_usage" not in cls_node or cls_node["slot_usage"] is None:
                    cls_node["slot_usage"] = {}
                su = cls_node["slot_usage"].get(slot_name)
                if su is None:
                    cls_node["slot_usage"][slot_name] = dict(ch["slot_usage"])
                else:
                    su.update(ch["slot_usage"])

            _save_yaml(target, doc)
            reporter.applied(
                f"Slot `{slot_name}` attached to `{schema_class}` (M/R/O: {ch['mro']})"
            )

        elif ctype == "class_add":
            class_name = ch["name"]
            parent     = ch["is_a"]
            target     = Path(ch["_target"])

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

        elif ctype == "slot_delete":
            slot_name    = ch["name"]
            schema_class = ch["schema_class"]
            target       = Path(ch["_target"])

            doc = _load_yaml(target)
            classes = doc.get("classes") or {}
            removed = False
            if schema_class in classes:
                cls_node = classes[schema_class] or {}
                slot_list = cls_node.get("slots") or []
                if slot_name in slot_list:
                    slot_list.remove(slot_name)
                    cls_node["slots"] = slot_list
                    removed = True
                su = cls_node.get("slot_usage") or {}
                if slot_name in su:
                    del su[slot_name]
                    removed = True
            if removed:
                _save_yaml(target, doc)
                reporter.applied(
                    f"Slot `{slot_name}` removed from `{schema_class}` "
                    f"(global definition kept — it may still be used by other classes)"
                )

        elif ctype == "class_delete":
            class_name = ch["name"]
            target     = Path(ch["_target"])

            doc = _load_yaml(target)
            classes = doc.get("classes") or {}
            if class_name in classes:
                del classes[class_name]
                _save_yaml(target, doc)
                reporter.applied(f"Class `{class_name}` removed from the schema")


# ─────────────────────────────────────────────────────────────────────────────
# Post-apply verification
# ─────────────────────────────────────────────────────────────────────────────


def verify_applied(changes: list[dict], reporter: Reporter, schema_dir: Path | None = None) -> None:
    """
    Reload the schema after apply_changes and check that every planned
    addition actually landed: each new class exists, and each new/attached
    slot is reachable from its class. Any miss is recorded as an error.

    LinkML validation alone cannot catch this -- an empty class and an
    orphaned global slot are both perfectly valid schema (PR #157).
    """
    with contextlib.redirect_stdout(io.StringIO()):  # silence "Loading: …" lines
        schema = load_merged_schema(str(schema_dir or SCHEMA_DIR))
    classes = schema.get("classes", {})

    for ch in changes:
        ctype = ch["type"]
        if ctype == "class_add" and ch["name"] not in classes:
            reporter.error(
                "schema", f"class `{ch['name']}`",
                "Planned as a new class but missing from the schema after "
                "applying the changes. Nothing will be committed.",
                hint=_PIPELINE_HINT,
            )
        elif ctype in ("slot_add", "slot_attach"):
            slot_name, owner = ch["name"], ch["schema_class"]
            if slot_name not in get_all_class_slots(schema, owner):
                reporter.error(
                    "schema", f"slot `{slot_name}`",
                    f"Planned for `{owner}` but not part of that class after "
                    f"applying the changes. Nothing will be committed.",
                    hint=_PIPELINE_HINT,
                )
        elif ctype == "class_delete" and ch["name"] in classes:
            reporter.error(
                "schema", f"class `{ch['name']}`",
                "Planned for removal but still in the schema after applying "
                "the changes. Nothing will be committed.",
                hint=_PIPELINE_HINT,
            )


def verify_displayed(changes: list[dict], reporter: Reporter, schema_dir: Path | None = None) -> None:
    """
    Regenerate the workbook rows from the changed schema and check that every
    applied field now shows the contributor's value -- the guarantee that
    matters to them, and one that catches values a parent slot or class
    overrides. Modified rows must match (error otherwise); added rows that do
    not show up on the sheet are reported as a warning.
    """
    expects = [e for ch in changes for e in ch.get("_expect", [])]
    absents = [a for ch in changes for a in ch.get("_expect_absent", [])]
    if not expects and not absents:
        return
    rows = generate_rows(schema_dir or SCHEMA_DIR)
    index = {sheet: index_rows(sheet_rows) for sheet, sheet_rows in rows.items()}

    missing_reported: set = set()
    for sheet, key, f, value, strict in expects:
        where = f"'{key[0]}'" + (f" ({key[1]})" if key[1] else "")
        row = index.get(sheet, {}).get(key)
        if row is None:
            if (sheet, key) in missing_reported:
                continue
            missing_reported.add((sheet, key))
            if strict:
                reporter.error(
                    sheet, where,
                    "This row is missing from the regenerated workbook after applying "
                    "your changes. Nothing will be committed.",
                    hint=_PIPELINE_HINT,
                )
            else:
                reporter.warning(
                    sheet, where,
                    f"Added to the schema, but it does not show up on the {sheet} sheet "
                    f"(its class is not reachable from `{CLASS_MAP.get(sheet, sheet)}`).",
                    hint="Check the domain column; a maintainer may need to connect the class.",
                )
        elif row[f] != value:
            reporter.error(
                sheet, where,
                f"The *{FIELD_LABELS.get(f, f)}* did not take effect: after applying, the "
                f"schema gives `{_short(row[f])}` instead of `{_short(value)}`. "
                f"Nothing will be committed.",
                hint=_PIPELINE_HINT,
            )
    for sheet, key in absents:
        if key in index.get(sheet, {}):
            reporter.error(
                sheet, f"'{key[0]}'" + (f" ({key[1]})" if key[1] else ""),
                "Still shown on the sheet after removing it. Nothing will be committed.",
                hint=_PIPELINE_HINT,
            )


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────


def _note_edits(reporter: Reporter, excel_data: dict, baseline: dict, current: dict) -> None:
    """Tell the contributor what was detected, and whether the template is older."""
    edited = added = removed = stale = 0
    for sheet in CLASS_MAP:
        base_idx = baseline.get(sheet, {})
        submitted = index_rows(excel_data.get(sheet, []))
        now = index_rows(current.get(sheet, []))
        for key, row in submitted.items():
            if key not in base_idx:
                added += 1
            elif changed_fields(row, base_idx[key]):
                edited += 1
        removed += sum(1 for key in base_idx if key not in submitted)
        stale += sum(1 for key, row in base_idx.items()
                     if key not in now or changed_fields(row, now[key]))
        stale += sum(1 for key in now if key not in base_idx)
    reporter.note(
        f"Compared with the workbook you downloaded: {edited} row(s) changed, "
        f"{added} added, {removed} removed."
    )
    if stale:
        reporter.note(
            f"Your workbook was generated from an older version of the schema: "
            f"{stale} row(s) have changed on `main` since. Only the rows you edited "
            f"are applied — everything else keeps its current value."
        )


def main(inbox_path: Path) -> int:
    reporter = Reporter()

    # 1. Load the merged schema and its LinkML view
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            schema = load_merged_schema(str(SCHEMA_DIR))
        sv = load_schema_view(SCHEMA_DIR)
    except Exception as exc:  # noqa: BLE001
        reporter.error("schema", "load", f"Could not load the merged schema: {exc}")
        print(reporter.to_markdown())
        return 1

    # 2. Validate workbook structure, cell values and the baseline sheet
    sheets = validate_structure(inbox_path, reporter)
    if sheets is None or reporter.has_errors:
        print(reporter.to_markdown())
        return 3
    scan_cell_errors(inbox_path, reporter)
    baseline = read_baseline(inbox_path)
    if baseline is None:
        reporter.error(
            "workbook", f"sheet '{BASELINE_SHEET}'",
            "This workbook was made from an older template: it has no hidden "
            f"`{BASELINE_SHEET}` sheet, so your edits can't be told apart from "
            "changes merged since you downloaded it.",
            hint=f"Download the current workbook ({DEV_WORKBOOK_URL}), copy your "
                 "edits into it, and push again.",
        )
    if reporter.has_errors:
        print(reporter.to_markdown())
        return 3

    # 3. Build name→file and label→name indexes
    slot_origin, class_origin = build_origin_index(SCHEMA_DIR)
    label_to_slot, label_to_class = build_label_index(schema)

    # 4. Parse normalised row data from Excel
    excel_data = parse_excel(sheets)
    reporter.empty_message = (
        "✅ No edits found — every row matches the workbook you downloaded, "
        "so nothing was changed."
    )
    _note_edits(reporter, excel_data, baseline, generate_rows(SCHEMA_DIR))

    # 5. Plan all changes (errors go to reporter, not raised)
    changes = plan_changes(
        schema, excel_data,
        label_to_slot, label_to_class,
        slot_origin, class_origin,
        reporter,
        baseline=baseline, sv=sv,
    )

    # 6. Stop if any planning errors — nothing written yet
    if reporter.has_errors:
        print(reporter.to_markdown())
        return 3

    # 7. Apply, verify everything landed, and roll back on any error
    if changes:
        snapshot = _snapshot_schema(SCHEMA_DIR)
        apply_changes(changes, reporter)
        if not reporter.has_errors:
            verify_applied(changes, reporter)
            verify_displayed(changes, reporter)
        if reporter.has_errors:
            _restore_schema(snapshot)
            reporter.rolled_back()

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
