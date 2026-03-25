"""
excel_to_schema.py

Compares the CoreMeta4Cat vocabulary Excel workbook against the current
merged LinkML schema and reports differences.

The schema is the ground truth — this script does NOT modify the schema.
It produces a human-readable diff report showing:

  - Slots/classes present in the Excel workbook but missing from the schema
  - Slots/classes present in the schema but not in the workbook
  - M/R/O mismatches between the workbook and the schema

Usage:
    just excel-to-schema
  or directly:
    uv run python scripts/excel_to_schema.py [path/to/workbook.xlsx]

If no path is given it defaults to docs/assets/coremeta4cat_vocabulary.xlsx.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from generate_schema_docs import (  # noqa: E402
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    load_merged_schema,
    snake_to_readable,
)

DEFAULT_WORKBOOK = _ROOT / "docs" / "assets" / "coremeta4cat_vocabulary.xlsx"
SCHEMA_DIR = _ROOT / "src" / "coremeta4cat" / "schema"

MAIN_CLASSES = ["Synthesis", "Characterization", "Reaction", "Simulation"]

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _slot_mro(schema: dict, class_name: str, slot_name: str) -> str:
    class_def = schema.get("classes", {}).get(class_name, {})
    usage = (class_def.get("slot_usage") or {}).get(slot_name) or {}
    slot_def = get_slot_details(schema, slot_name)
    required    = usage.get("required",    slot_def.get("required",    False))
    recommended = usage.get("recommended", slot_def.get("recommended", False))
    if required:
        return "M"
    if recommended:
        return "R"
    return "O"


def _schema_labels_for_class(schema: dict, class_name: str) -> dict[str, str]:
    """
    Return {readable_label: mro} for all top-level slots of a main data class.
    Includes slots contributed by gateway slot_usage ranges.
    """
    result: dict[str, str] = {}
    direct_slots = get_all_class_slots(schema, class_name)
    for slot_name in direct_slots:
        label = snake_to_readable(slot_name)
        result[label] = _slot_mro(schema, class_name, slot_name)

    for su_name, _ in get_class_ranged_slot_usage(schema, class_name):
        if su_name not in direct_slots:
            label = snake_to_readable(su_name)
            result[label] = _slot_mro(schema, class_name, su_name)

    return result


def _excel_labels_for_sheet(df: pd.DataFrame, mro_col: str) -> dict[str, str]:
    """
    Return {label: mro} for all top-level rows (no parent) in an Excel sheet.
    """
    result: dict[str, str] = {}
    top = df[df["parent"].isin(["", "na", float("nan")])]
    for _, row in top.iterrows():
        label = str(row.get("label", "")).strip()
        mro = str(row.get(mro_col, "")).strip().upper()[:1]
        if label:
            result[label] = mro if mro in ("M", "R", "O") else "O"
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Diff report
# ─────────────────────────────────────────────────────────────────────────────

def compare(workbook_path: Path) -> None:
    print(f"\nLoading schema from: {SCHEMA_DIR}")
    schema = load_merged_schema(str(SCHEMA_DIR))

    print(f"Loading workbook from: {workbook_path}\n")
    xls = pd.ExcelFile(workbook_path)

    any_diff = False

    for cls in MAIN_CLASSES:
        print(f"{'='*60}")
        print(f"  {cls}")
        print(f"{'='*60}")

        schema_labels = _schema_labels_for_class(schema, cls)

        # Try to match sheet by class name (case-insensitive)
        sheet_match = next(
            (s for s in xls.sheet_names if s.strip().lower() == cls.lower()), None
        )
        if sheet_match is None:
            print(f"  [!] Sheet '{cls}' not found in workbook — skipping comparison.\n")
            continue

        df = xls.parse(sheet_match).fillna("")
        df.columns = [str(c).strip().lower() for c in df.columns]
        # Detect the M/R/O column (flexible naming)
        mro_col = next(
            (c for c in df.columns if "mandatory" in c or "mro" in c or c == "m/r/o"), None
        )
        if mro_col is None:
            print(f"  [!] Could not find M/R/O column in sheet '{sheet_match}' — skipping.\n")
            continue

        df["parent"] = df["parent"].astype(str).str.strip().str.lower()
        excel_labels = _excel_labels_for_sheet(df, mro_col)

        schema_set = set(schema_labels)
        excel_set  = set(excel_labels)

        in_schema_not_excel = schema_set - excel_set
        in_excel_not_schema = excel_set - schema_set
        in_both = schema_set & excel_set
        mro_mismatches = {
            label for label in in_both
            if schema_labels[label] != excel_labels[label]
        }

        if not in_schema_not_excel and not in_excel_not_schema and not mro_mismatches:
            print("  OK No differences found.\n")
            continue

        any_diff = True

        if in_schema_not_excel:
            print(f"\n  In schema but NOT in workbook ({len(in_schema_not_excel)}):")
            for label in sorted(in_schema_not_excel):
                print(f"    + [{schema_labels[label]}] {label}")

        if in_excel_not_schema:
            print(f"\n  In workbook but NOT in schema ({len(in_excel_not_schema)}):")
            for label in sorted(in_excel_not_schema):
                print(f"    - [{excel_labels[label]}] {label}")

        if mro_mismatches:
            print(f"\n  M/R/O mismatches ({len(mro_mismatches)}):")
            for label in sorted(mro_mismatches):
                print(f"    ~ {label}: schema={schema_labels[label]}, workbook={excel_labels[label]}")

        print()

    if not any_diff:
        print("\nOK Schema and workbook are fully aligned at the top-level slot layer.")
    else:
        print(
            "\nNOTE: The schema is the ground truth. Please review the differences above\n"
            "and update the workbook (via 'just schema-to-excel') or open a schema\n"
            "issue if a workbook entry should be added to the schema."
        )


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    wb_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_WORKBOOK
    if not wb_path.exists():
        print(f"ERROR: workbook not found: {wb_path}")
        sys.exit(1)
    compare(wb_path)
