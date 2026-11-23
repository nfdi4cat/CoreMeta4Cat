"""
workbook_rows.py

Row model shared by schema_to_excel.py, excel_to_schema.py and
inbox_to_schema.py, so all three read and compare workbook rows the same way.

A data-sheet row is normalised into a plain dict keyed by FIELDS. Within a
sheet a row is identified by its (label, domain) pair -- schema_to_excel.py
writes every pair at most once.

Every generated workbook also carries a very hidden ``_baseline`` sheet: a
copy of all data-sheet rows exactly as they were generated. The inbox
pipeline compares a contributor's workbook against that copy, so it knows
which rows and fields the contributor actually changed -- even when the
workbook was downloaded before other changes were merged.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable, Mapping

import openpyxl

# Column headers of the data sheets, in workbook order.
HEADERS = [
    "label",
    "type",
    "domain",
    "M / R / O",
    "range",
    "multivalued",
    "inlined as list",
    "unit",
    "uri",
    "description",
]

# Normalised row keys, in the same order as HEADERS.
FIELDS = (
    "label", "type", "domain", "mro", "range",
    "multivalued", "inlined_as_list", "unit", "uri", "description",
)
HEADER_TO_FIELD = dict(zip(HEADERS, FIELDS))

# Fields that can change on an existing row; label + domain identify the row.
VALUE_FIELDS = (
    "type", "mro", "range", "multivalued", "inlined_as_list",
    "unit", "uri", "description",
)

# Human-readable column names for messages.
FIELD_LABELS = {field: header for header, field in HEADER_TO_FIELD.items()}

# Accepted (lower-case) spellings of each column header.
COLUMN_ALIASES: dict[str, list[str]] = {
    "label":           ["label"],
    "type":            ["type"],
    "domain":          ["domain", "parent"],
    "M / R / O":       ["m / r / o", "m/r/o", "mro", "mandatory/recommended/optional"],
    "range":           ["range"],
    "multivalued":     ["multivalued"],
    "inlined as list": ["inlined as list", "inlined_as_list"],
    "unit":            ["unit"],
    "uri":             ["uri"],
    "description":     ["description"],
}

DATA_SHEETS = ("Synthesis", "Characterization", "Reaction", "Simulation")
REFERENCE_SHEET = "CoreMeta4Cat"   # reference only, never applied to the schema
ROW_SHEETS = (REFERENCE_SHEET, *DATA_SHEETS)

BASELINE_SHEET = "_baseline"
BASELINE_HEADERS = ["sheet", *HEADERS]


# ─────────────────────────────────────────────────────────────────────────────
# Cell normalisation
# ─────────────────────────────────────────────────────────────────────────────

def clean(val: Any) -> str:
    """Coerce a cell value to a stripped string; NaN/None become ''."""
    if val is None:
        return ""
    s = str(val).replace("\r\n", "\n").strip()
    return "" if s.lower() in ("nan", "none", "nat") else s


def normalise_bool(val: Any) -> str:
    """'yes' if the cell means true, else ''."""
    return "yes" if clean(val).lower() in ("yes", "y", "true", "1", "x") else ""


def normalise_mro(val: Any) -> str:
    """'M', 'R' or 'O'; anything else is returned upper-cased for the caller to reject."""
    s = clean(val).upper()
    if s in ("M", "MANDATORY"):
        return "M"
    if s in ("R", "RECOMMENDED"):
        return "R"
    if s in ("O", "OPTIONAL"):
        return "O"
    return s


def normalise_row(raw: Mapping[str, Any]) -> dict[str, str]:
    """Normalise a row given as {field: cell value} (keys from FIELDS)."""
    return {
        "label":           clean(raw.get("label")),
        "type":            clean(raw.get("type")).lower() or "slot",
        "domain":          clean(raw.get("domain")),
        "mro":             normalise_mro(raw.get("mro")),
        "range":           clean(raw.get("range")),
        "multivalued":     normalise_bool(raw.get("multivalued")),
        "inlined_as_list": normalise_bool(raw.get("inlined_as_list")),
        "unit":            clean(raw.get("unit")),
        "uri":             clean(raw.get("uri")),
        "description":     clean(raw.get("description")),
    }


def row_from_values(values: Iterable[Any]) -> dict[str, str]:
    """Normalise a row given as cell values in HEADERS order."""
    return normalise_row(dict(zip(FIELDS, values)))


def slot_name_from_label(label: str) -> str:
    """The snake_case slot name the inbox derives from a label."""
    return re.sub(r"[^a-z0-9]+", "_", label.strip().lower()).strip("_")


def class_name_from_label(label: str) -> str:
    """The PascalCase class name the inbox derives from a label."""
    if " " not in label and label[:1].isupper():
        return label.strip()   # already PascalCase
    return "".join(word.capitalize() for word in label.strip().split())


# ─────────────────────────────────────────────────────────────────────────────
# Row identity and comparison
# ─────────────────────────────────────────────────────────────────────────────

def row_key(row: Mapping[str, str]) -> tuple[str, str]:
    return (row["label"], row["domain"])


def generated_key(row: Mapping[str, str], class_labels: set[str]) -> tuple[str, str]:
    """
    The key a contributor's new row gets once applied: labels are turned into
    schema names (and back), so 'Adsorbate Species' on 'Adsorption Energetics'
    becomes ('adsorbate species', 'AdsorptionEnergetics').
    """
    domain = row["domain"]
    if domain and domain not in class_labels and class_name_from_label(domain) in class_labels:
        domain = class_name_from_label(domain)
    if row["type"] == "class":
        return (class_name_from_label(row["label"]), domain)
    return (slot_name_from_label(row["label"]).replace("_", " "), domain)


def index_rows(rows: Iterable[Mapping[str, str]]) -> dict[tuple[str, str], dict]:
    """{(label, domain): row}; the first row wins if a key repeats."""
    index: dict[tuple[str, str], dict] = {}
    for row in rows:
        index.setdefault(row_key(row), dict(row))
    return index


def changed_fields(row: Mapping[str, str], base: Mapping[str, str]) -> list[str]:
    """VALUE_FIELDS where row differs from base."""
    return [f for f in VALUE_FIELDS if row.get(f, "") != base.get(f, "")]


# ─────────────────────────────────────────────────────────────────────────────
# Baseline sheet
# ─────────────────────────────────────────────────────────────────────────────

def baseline_values(sheet_rows: Mapping[str, Iterable[Iterable[Any]]]) -> list[list[Any]]:
    """Rows of the _baseline sheet: header, then [sheet, *values] per data row."""
    out: list[list[Any]] = [list(BASELINE_HEADERS)]
    for sheet, rows in sheet_rows.items():
        for values in rows:
            out.append([sheet, *values])
    return out


def read_baseline(workbook_path: Path | str) -> dict[str, dict[tuple[str, str], dict]] | None:
    """
    Return {sheet: {(label, domain): row}} from the workbook's _baseline
    sheet, or None if the workbook has none (made from an older template, or
    the sheet was removed).
    """
    wb = openpyxl.load_workbook(str(workbook_path), read_only=True, data_only=True)
    try:
        if BASELINE_SHEET not in wb.sheetnames:
            return None
        rows = wb[BASELINE_SHEET].iter_rows(values_only=True)
        header = [clean(h) for h in next(rows, ())]
        if header[: len(BASELINE_HEADERS)] != BASELINE_HEADERS:
            return None
        result: dict[str, dict[tuple[str, str], dict]] = {s: {} for s in ROW_SHEETS}
        for values in rows:
            values = list(values) + [None] * (len(BASELINE_HEADERS) - len(values))
            sheet = clean(values[0])
            if not sheet:
                continue
            row = row_from_values(values[1:len(BASELINE_HEADERS)])
            if row["label"]:
                result.setdefault(sheet, {}).setdefault(row_key(row), row)
        return result
    finally:
        wb.close()
