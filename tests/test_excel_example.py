"""Spreadsheet example (docs/assets/examples/excel_JLCAT03): the parser still reproduces the record in
tests/data/valid, and it refuses a workbook that no longer matches its crosswalk.

The parser runs on a copy of the workbook and writes into a temporary folder, so the committed files
are never touched. See docs/working-with-data/building-a-parser.md.
"""
import shutil
import subprocess
import sys
from pathlib import Path

import openpyxl
import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
EXAMPLE = REPO_ROOT / "docs" / "assets" / "examples" / "excel_JLCAT03"
PARSER = EXAMPLE / "parser" / "xlsx_to_coremeta4cat.py"
RECORD = REPO_ROOT / "tests" / "data" / "valid" / "CatalysisDataset-JLCAT03.yaml"


def run_parser(tmp_path, change_workbook=None, change_crosswalk=None):
    """Run the parser on a copy of the workbook, with every output redirected into tmp_path."""
    workbook = tmp_path / "workbook.xlsx"
    shutil.copy(EXAMPLE / "source" / "TestDataSet_CoreMeta4Cat.xlsx", workbook)
    if change_workbook:
        book = openpyxl.load_workbook(workbook)
        change_workbook(book)
        book.save(workbook)
    crosswalk = yaml.safe_load((EXAMPLE / "parser" / "crosswalk.yaml").read_text(encoding="utf-8"))
    crosswalk.update(
        workbook=str(workbook),
        supplement=str(EXAMPLE / "parser" / "supplement.yaml"),
        output=str(tmp_path / "record.yaml"),
        provenance=str(tmp_path / "provenance.yaml"),
        report=str(tmp_path / "report.md"),
    )
    if change_crosswalk:
        change_crosswalk(crosswalk)
    path = tmp_path / "crosswalk.yaml"
    path.write_text(yaml.safe_dump(crosswalk, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(PARSER), str(path), "--no-checks"],
        capture_output=True, text=True, encoding="utf-8",
    )


def body(path):
    """The record without its header comments, which name the files it was written from."""
    return [line for line in Path(path).read_text(encoding="utf-8").splitlines() if not line.startswith("#")]


def test_parser_reproduces_the_committed_record(tmp_path):
    result = run_parser(tmp_path)
    assert result.returncode == 0, result.stderr
    assert body(tmp_path / "record.yaml") == body(RECORD), (
        "The parser no longer produces tests/data/valid/CatalysisDataset-JLCAT03.yaml: rerun "
        "docs/assets/examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py and commit the result."
    )


def set_cell(sheet, cell, value):
    def change(book):
        book[sheet][cell] = value
    return change


def drop_column(column):
    def change(crosswalk):
        columns = crosswalk["sheets"]["Synthesis"]["columns"]
        crosswalk["sheets"]["Synthesis"]["columns"] = [entry for entry in columns if entry["col"] != column]
    return change


GUARD_RAILS = {
    "column-not-in-crosswalk": (
        {"change_crosswalk": drop_column("E")},
        "column E 'storage conditions (voc4cat:0008105)' is not in the crosswalk",
    ),
    "header-renamed": (
        {"change_workbook": set_cell("Synthesis", "E1", "storage temperature")},
        "column E header is 'storage temperature'",
    ),
    "stray-cell": (
        {"change_workbook": set_cell("Synthesis", "A7", "note: sample re-calcined")},
        "Synthesis!A7: non-empty cell outside the declared layout",
    ),
    "unit-added-later": (
        {"change_workbook": set_cell("Reaction", "AF2", "%")},
        "crosswalk sets a unit, but the sheet gives '%'",
    ),
    "unknown-unit": (
        {"change_workbook": set_cell("Reaction", "B2", "g")},
        "unit 'g' is not in the units table",
    ),
    "value-not-in-pick-list": (
        {"change_workbook": set_cell("Reaction", "C3", "homogeneous")},
        "'homogeneous' is not in the value map",
    ),
    "repeated-value-differs": (
        {"change_workbook": set_cell("Character", "C21", 90)},
        "expected to repeat 20 (80), holds 90",
    ),
}


@pytest.mark.parametrize("case", GUARD_RAILS, ids=list(GUARD_RAILS))
def test_parser_refuses_a_changed_workbook(case, tmp_path):
    changes, message = GUARD_RAILS[case]
    result = run_parser(tmp_path, **changes)
    assert result.returncode == 1
    assert message in result.stderr
