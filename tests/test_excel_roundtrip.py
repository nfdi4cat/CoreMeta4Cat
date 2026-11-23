"""
tests/test_excel_roundtrip.py

Verifies the schema → Excel → schema round trip:

  1. schema_to_excel builds the workbook, including the very hidden
     _baseline sheet the inbox pipeline relies on.
  2. excel_to_schema compares it with the rows the current schema produces:
     no differences in any column, on any sheet.
  3. Every slot row shows the values LinkML itself uses for that field on that
     class (SchemaView.induced_slot) -- checked here independently of the
     generator, so inherited M/R/O / multivalued values can't silently regress.

The helpers are imported directly rather than subprocess-calling the scripts,
so failures produce tracebacks that point to the exact line.
"""

from __future__ import annotations

import sys
from pathlib import Path

import openpyxl
import pytest

# ── path setup ────────────────────────────────────────────────────────────────
_ROOT    = Path(__file__).parent.parent
_SCRIPTS = _ROOT / "scripts"
_SCHEMA  = _ROOT / "src" / "coremeta4cat" / "schema"

sys.path.insert(0, str(_SCRIPTS))

from excel_to_schema import read_workbook_rows, sheet_differences  # noqa: E402
from schema_to_excel import (  # noqa: E402
    CLASS_MAP,
    DROPDOWNS,
    build_workbook,
    generate_rows,
    save_workbook,
)
from workbook_rows import (  # noqa: E402
    BASELINE_SHEET,
    DATA_SHEETS,
    HEADERS,
    REFERENCE_SHEET,
    index_rows,
    read_baseline,
    row_from_values,
)

SHEET_NAMES = list(DATA_SHEETS)
VISIBLE_SHEETS = {"Introduction", "Legend", REFERENCE_SHEET, *SHEET_NAMES}


# ── fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def generated_workbook(tmp_path_factory) -> Path:
    """Generate the vocabulary workbook into a temporary file."""
    out_path = tmp_path_factory.mktemp("excel") / "coremeta4cat_vocabulary.xlsx"
    save_workbook(build_workbook(_SCHEMA), out_path)
    return out_path


@pytest.fixture(scope="module")
def schema_view():
    from linkml_runtime import SchemaView
    return SchemaView(str(_SCHEMA / "coremeta4cat.yaml"))


# ── structure ─────────────────────────────────────────────────────────────────

def test_workbook_has_all_sheets(generated_workbook):
    """The seven visible sheets, plus the very hidden baseline."""
    wb = openpyxl.load_workbook(str(generated_workbook))
    visible = {ws.title for ws in wb.worksheets if ws.sheet_state == "visible"}
    assert visible == VISIBLE_SHEETS
    assert wb[BASELINE_SHEET].sheet_state == "veryHidden"


def test_data_sheets_have_rows(generated_workbook):
    """Each of the four main data sheets has at least one data row."""
    wb = openpyxl.load_workbook(str(generated_workbook), read_only=True, data_only=True)
    for sheet_name in SHEET_NAMES:
        rows = list(wb[sheet_name].iter_rows(min_row=2, values_only=True))
        assert len(rows) > 0, f"Sheet '{sheet_name}' has no data rows"


def test_header_columns(generated_workbook):
    """Each data sheet has exactly the expected column headers in order."""
    wb = openpyxl.load_workbook(str(generated_workbook), read_only=True, data_only=True)
    for sheet_name in SHEET_NAMES:
        header = [cell.value for cell in next(wb[sheet_name].iter_rows(max_row=1))]
        assert header == HEADERS, (
            f"Sheet '{sheet_name}' header mismatch.\n"
            f"  Expected: {HEADERS}\n  Got:      {header}"
        )


def test_type_column_values(generated_workbook):
    """The 'type' column contains only 'slot' or 'class' values."""
    wb = openpyxl.load_workbook(str(generated_workbook), read_only=True, data_only=True)
    for sheet_name in SHEET_NAMES:
        for row_idx, row in enumerate(wb[sheet_name].iter_rows(min_row=2, values_only=True), start=2):
            assert row[1] in ("slot", "class"), (
                f"Sheet '{sheet_name}', row {row_idx}: unexpected type value '{row[1]}'"
            )


def test_data_sheets_have_dropdowns(generated_workbook):
    """type, M/R/O, multivalued and inlined-as-list offer in-cell dropdowns."""
    wb = openpyxl.load_workbook(str(generated_workbook))
    for sheet_name in SHEET_NAMES:
        found = {
            str(dv.sqref)[0]: dv.formula1
            for dv in wb[sheet_name].data_validations.dataValidation
        }
        for column, values in DROPDOWNS.items():
            assert found.get(column) == '"' + ",".join(values) + '"', (sheet_name, column)


def test_class_map_coverage():
    """CLASS_MAP covers exactly the four main sheet titles."""
    assert set(CLASS_MAP.keys()) == set(SHEET_NAMES)


# ── round trip ────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("sheet_title", SHEET_NAMES)
def test_roundtrip_no_differences(generated_workbook, sheet_title):
    """
    Every row and every column of the generated workbook matches what the
    schema produces: schema → Excel → compare → no diff.
    """
    current = generate_rows(_SCHEMA)
    submitted = read_workbook_rows(generated_workbook)
    lines = sheet_differences(submitted[sheet_title], current[sheet_title])
    assert not lines, "\n".join(lines)


def test_baseline_matches_the_sheets(generated_workbook):
    """The _baseline sheet holds exactly the rows of every data sheet."""
    baseline = read_baseline(generated_workbook)
    assert baseline is not None
    submitted = read_workbook_rows(generated_workbook)
    for sheet_name in SHEET_NAMES:
        assert baseline[sheet_name] == index_rows(submitted[sheet_name]), sheet_name

    wb = openpyxl.load_workbook(str(generated_workbook), read_only=True, data_only=True)
    reference = [row_from_values(v) for v in wb[REFERENCE_SHEET].iter_rows(min_row=2, values_only=True)]
    assert baseline[REFERENCE_SHEET] == index_rows(reference)


def test_slot_rows_show_linkml_values(generated_workbook, schema_view):
    """
    M/R/O, range and multivalued of every slot row are the values LinkML uses
    for that slot on that class -- inheritance from parent slots (e.g.
    has_quantitative_attribute is recommended and multivalued), identifiers
    being mandatory and slot_usage overrides included.
    """
    wb = openpyxl.load_workbook(str(generated_workbook), read_only=True, data_only=True)
    mismatches: list[str] = []
    checked = 0
    for sheet_name, top_class in CLASS_MAP.items():
        for values in wb[sheet_name].iter_rows(min_row=2, values_only=True):
            row = row_from_values(values)
            if row["type"] != "slot":
                continue
            slot_name = row["label"].replace(" ", "_")
            class_name = row["domain"] or top_class
            induced = schema_view.induced_slot(slot_name, class_name)
            expected = {
                "mro": "M" if induced.required else ("R" if induced.recommended else "O"),
                "range": induced.range or "string",
                "multivalued": "yes" if induced.multivalued else "",
            }
            checked += 1
            for field, value in expected.items():
                if row[field] != value:
                    mismatches.append(
                        f"[{sheet_name}] {class_name}.{slot_name} {field}: "
                        f"workbook={row[field]!r} LinkML={value!r}"
                    )
    assert checked > 500
    assert not mismatches, "\n".join(mismatches[:40])


def test_regeneration_leaves_an_unchanged_file_alone(tmp_path):
    """Regenerating without schema changes does not rewrite the workbook
    (openpyxl stamps the save time into docProps/core.xml, which would
    otherwise make every run look like a change)."""
    out = tmp_path / "coremeta4cat_vocabulary.xlsx"
    assert save_workbook(build_workbook(_SCHEMA), out) is True
    before = out.read_bytes()
    assert save_workbook(build_workbook(_SCHEMA), out) is False
    assert out.read_bytes() == before
