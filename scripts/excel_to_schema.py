"""
excel_to_schema.py

Compares a CoreMeta4Cat vocabulary workbook against the current LinkML schema
and reports differences.

The schema is the ground truth — this script does NOT modify the schema.
It compares the workbook with the rows a workbook generated from the current
schema would contain (schema_to_excel.generate_rows), column by column: label,
type, domain, M/R/O, range, multivalued, inlined as list, unit, uri and
description.

If the workbook carries a ``_baseline`` sheet (every generated workbook does),
only the rows and fields the contributor changed relative to it are checked.
That is the round-trip check after an inbox submission: every edit should now
be in the schema, and every removed row gone. Without a baseline the whole
workbook is compared.

Usage:
    just excel-to-schema
  or directly:
    uv run python scripts/excel_to_schema.py [path/to/workbook.xlsx]

If no path is given it defaults to docs/assets/coremeta4cat_vocabulary.xlsx.
Exit code 0 when the workbook and schema are aligned, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

import openpyxl

_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from schema_to_excel import generate_rows  # noqa: E402
from workbook_rows import (  # noqa: E402
    COLUMN_ALIASES,
    DATA_SHEETS,
    FIELD_LABELS,
    HEADER_TO_FIELD,
    VALUE_FIELDS,
    changed_fields,
    generated_key,
    index_rows,
    normalise_row,
    read_baseline,
)

DEFAULT_WORKBOOK = _ROOT / "docs" / "assets" / "coremeta4cat_vocabulary.xlsx"
SCHEMA_DIR = _ROOT / "src" / "coremeta4cat" / "schema"

MAIN_CLASSES = list(DATA_SHEETS)

ALIGNED_MESSAGE = "OK Schema and workbook are fully aligned."


# ─────────────────────────────────────────────────────────────────────────────
# Reading
# ─────────────────────────────────────────────────────────────────────────────

def read_workbook_rows(workbook_path: Path | str) -> dict[str, list[dict]]:
    """{sheet: [normalised row]} for the data sheets present in the workbook."""
    wb = openpyxl.load_workbook(str(workbook_path), read_only=True, data_only=True)
    try:
        result: dict[str, list[dict]] = {}
        for sheet_name in wb.sheetnames:
            title = next((s for s in DATA_SHEETS if s.lower() == sheet_name.strip().lower()), None)
            if title is None:
                continue
            values_iter = wb[sheet_name].iter_rows(values_only=True)
            header = [str(h).strip().lower() if h is not None else "" for h in next(values_iter, ())]
            columns: dict[str, int] = {}
            for canonical, aliases in COLUMN_ALIASES.items():
                index = next((i for i, h in enumerate(header) if h in aliases), None)
                if index is not None:
                    columns[HEADER_TO_FIELD[canonical]] = index
            rows: list[dict] = []
            for values in values_iter:
                raw = {f: (values[i] if i < len(values) else None) for f, i in columns.items()}
                row = normalise_row(raw)
                if row["label"]:
                    rows.append(row)
            result[title] = rows
        return result
    finally:
        wb.close()


# ─────────────────────────────────────────────────────────────────────────────
# Comparison
# ─────────────────────────────────────────────────────────────────────────────

def _where(key: tuple[str, str]) -> str:
    return f"{key[0]} ({key[1]})" if key[1] else key[0]


def _short(value: str, limit: int = 50) -> str:
    text = value.replace("\n", " ")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _value_diffs(row: dict, now: dict, fields) -> str:
    return "; ".join(
        f"{FIELD_LABELS[f]}: workbook={_short(row[f])!r} schema={_short(now[f])!r}"
        for f in fields
    )


def sheet_differences(
    workbook_rows: list[dict],
    schema_rows: list[dict],
    base_idx: dict | None = None,
) -> list[str]:
    """Report lines for one sheet; empty if it is aligned with the schema."""
    submitted = index_rows(workbook_rows)
    current = index_rows(schema_rows)
    lines: list[str] = []

    if base_idx is None:
        missing = sorted(k for k in current if k not in submitted)
        extra = sorted(k for k in submitted if k not in current)
        changed = sorted(
            (k, [f for f in VALUE_FIELDS if submitted[k][f] != current[k][f]])
            for k in submitted if k in current
        )
        changed = [(k, fields) for k, fields in changed if fields]
        if missing:
            lines.append(f"\n  In schema but NOT in workbook ({len(missing)}):")
            lines += [f"    + [{current[k]['mro']}] {_where(k)}" for k in missing]
        if extra:
            lines.append(f"\n  In workbook but NOT in schema ({len(extra)}):")
            lines += [f"    - [{submitted[k]['mro']}] {_where(k)}" for k in extra]
        if changed:
            lines.append(f"\n  Values that differ ({len(changed)}):")
            lines += [f"    ~ {_where(k)}: {_value_diffs(submitted[k], current[k], fields)}"
                      for k, fields in changed]
        return lines

    # Baseline mode: only what the contributor changed.
    class_labels = {k[0] for k, r in current.items() if r["type"] == "class"}
    not_in_schema: list[str] = []
    not_applied: list[str] = []
    for key, row in sorted(submitted.items()):
        base = base_idx.get(key)
        if base is not None:
            fields = changed_fields(row, base)
        elif row["type"] == "class":
            fields = ["uri", "description"]   # a class row's other cells follow its slot
        else:
            fields = list(VALUE_FIELDS)
            row = {**row, "range": row["range"] or "string"}   # new slots default to string
        if not fields:
            continue
        now = current.get(key)
        if now is None and base is None:
            now = current.get(generated_key(row, class_labels))
        if now is None:
            not_in_schema.append(f"    - [{row['mro']}] {_where(key)}")
            continue
        differing = [f for f in fields if row[f] != now[f]]
        if differing:
            not_applied.append(f"    ~ {_where(key)}: {_value_diffs(row, now, differing)}")
    still_there = sorted(k for k in base_idx if k not in submitted and k in current)

    if not_in_schema:
        lines.append(f"\n  Rows you added or edited that are NOT in the schema ({len(not_in_schema)}):")
        lines += not_in_schema
    if not_applied:
        lines.append(f"\n  Edits that are not in the schema ({len(not_applied)}):")
        lines += not_applied
    if still_there:
        lines.append(f"\n  Rows you removed that are still in the schema ({len(still_there)}):")
        lines += [f"    + {_where(k)}" for k in still_there]
    return lines


def compare(workbook_path: Path, schema_dir: Path = SCHEMA_DIR) -> bool:
    """Print the comparison report; True if the workbook and schema are aligned."""
    print(f"\nSchema:   {schema_dir}")
    print(f"Workbook: {workbook_path}")
    current = generate_rows(schema_dir)
    submitted = read_workbook_rows(workbook_path)
    baseline = read_baseline(workbook_path)
    if baseline is not None:
        print("Mode:     only the rows changed relative to the workbook's _baseline sheet\n")
    else:
        print("Mode:     whole workbook (no _baseline sheet)\n")

    any_diff = False
    for sheet in DATA_SHEETS:
        print("=" * 60)
        print(f"  {sheet}")
        print("=" * 60)
        if sheet not in submitted:
            print(f"  [!] Sheet '{sheet}' not found in workbook — skipping comparison.\n")
            continue
        lines = sheet_differences(
            submitted[sheet], current.get(sheet, []),
            None if baseline is None else baseline.get(sheet, {}),
        )
        if not lines:
            print("  OK No differences found.\n")
            continue
        any_diff = True
        print("\n".join(lines))
        print()

    if not any_diff:
        print(f"\n{ALIGNED_MESSAGE}")
    else:
        print(
            "\nNOTE: The schema is the ground truth. Please review the differences above\n"
            "and update the workbook (via 'just schema-to-excel') or open a schema\n"
            "issue if a workbook entry should be added to the schema."
        )
    return not any_diff


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    wb_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_WORKBOOK
    if not wb_path.exists():
        print(f"ERROR: workbook not found: {wb_path}")
        sys.exit(1)
    sys.exit(0 if compare(wb_path) else 1)
