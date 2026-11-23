"""
tests/test_inbox_baseline.py

End-to-end tests of the inbox pipeline (scripts/inbox_to_schema.py) on real
generated workbooks: generate the workbook from a tmp copy of the schema,
edit it the way a contributor would (openpyxl), run main(), then check the
YAML files and the regenerated workbook rows.

They pin the fixes for issue #188:

  • only the rows a contributor changed are applied (hidden _baseline sheet),
    so a workbook downloaded before other changes were merged reverts nothing;
  • values a slot inherits (M/R/O, multivalued) can be switched off;
  • edits to slots with a slot_usage override survive regeneration;
  • deleted nested rows remove the slot; inherited ones are reported instead;
  • edits that can't be applied are reported, never dropped silently;
  • invalid URIs / units / Excel error cells are rejected;
  • anything that does not land rolls the schema files back.

Candidate rows are looked up by their properties rather than hard-coded, so
the tests keep working as the schema evolves; if no candidate is left, the
test fails with a message saying which kind of row it needs.
"""

from __future__ import annotations

import contextlib
import io
import shutil
import sys
from pathlib import Path

import openpyxl
import pytest

_ROOT    = Path(__file__).parent.parent
_SCRIPTS = _ROOT / "scripts"
_SCHEMA  = _ROOT / "src" / "coremeta4cat" / "schema"

sys.path.insert(0, str(_SCRIPTS))

import inbox_to_schema as ib  # noqa: E402
import schema_to_excel as s2e  # noqa: E402
from generate_schema_docs import build_origin_index, load_yaml_file  # noqa: E402
from workbook_rows import (  # noqa: E402
    BASELINE_SHEET,
    HEADERS,
    REFERENCE_SHEET,
    index_rows,
    row_from_values,
)


# ── helpers ─────────────────────────────────────────────────────────────────

class Contribution:
    """A tmp copy of the schema plus a workbook generated from it, to edit."""

    def __init__(self, tmp_path: Path, monkeypatch) -> None:
        self.schema_dir = tmp_path / "schema"
        shutil.copytree(_SCHEMA, self.schema_dir)
        monkeypatch.setattr(ib, "SCHEMA_DIR", self.schema_dir)
        self.slot_origin, self.class_origin = build_origin_index(self.schema_dir)
        self.path = tmp_path / "coremeta4cat_vocabulary.xlsx"
        s2e.save_workbook(s2e.build_workbook(self.schema_dir), self.path)
        self.wb = openpyxl.load_workbook(self.path)
        self.snapshot = self._files()
        self.report = ""

    # ── workbook ─────────────────────────────────────────────────────────

    def rows(self, sheet: str):
        """(cells, normalised row) for every data row of a sheet."""
        return [
            (cells, row_from_values([c.value for c in cells]))
            for cells in self.wb[sheet].iter_rows(min_row=2)
        ]

    def slot_rows(self):
        """(sheet, cells, row, slot name, class name) for every slot row."""
        for sheet, top_class in ib.CLASS_MAP.items():
            for cells, row in self.rows(sheet):
                if row["type"] == "slot":
                    yield (sheet, cells, row, row["label"].replace(" ", "_"),
                           row["domain"] or top_class)

    def pick(self, predicate, what: str):
        for item in self.slot_rows():
            if predicate(*item):
                return item
        raise AssertionError(f"No {what} left in the schema -- choose another candidate.")

    @staticmethod
    def set(cells, column: str, value) -> None:
        cells[HEADERS.index(column)].value = value

    def delete(self, sheet: str, cells) -> None:
        self.wb[sheet].delete_rows(cells[0].row)

    # ── schema files ─────────────────────────────────────────────────────

    def _files(self) -> dict[str, bytes]:
        return {p.name: p.read_bytes() for p in self.schema_dir.glob("*.yaml")}

    def unchanged(self) -> bool:
        return self._files() == self.snapshot

    def class_node(self, class_name: str) -> dict:
        path = self.class_origin.get(class_name)
        if path is None:
            return {}
        return (load_yaml_file(str(path)).get("classes") or {}).get(class_name) or {}

    def slot_node(self, slot_name: str) -> dict:
        path = self.slot_origin.get(slot_name)
        if path is None:
            return {}
        return (load_yaml_file(str(path)).get("slots") or {}).get(slot_name) or {}

    def own_usage(self, class_name: str, slot_name: str):
        usage = self.class_node(class_name).get("slot_usage") or {}
        return usage.get(slot_name) if slot_name in usage else None

    def edit_schema(self, slot_name: str, **values) -> None:
        """Change a global slot definition directly, like a merge to main would."""
        path = self.slot_origin[slot_name]
        doc = ib._load_yaml(path)
        node = doc["slots"][slot_name]
        for key, value in values.items():
            node[key] = value
        ib._save_yaml(path, doc)

    # ── pipeline ─────────────────────────────────────────────────────────

    def run(self) -> int:
        self.wb.save(self.path)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = ib.main(self.path)
        self.report = out.getvalue()
        return code

    def current(self, sheet: str) -> dict:
        return index_rows(s2e.generate_rows(self.schema_dir)[sheet])

    def editable(self, slot_name: str, class_name: str) -> bool:
        return (slot_name in self.slot_origin and class_name in self.class_origin
                and slot_name != "id")


@pytest.fixture
def contribution(tmp_path, monkeypatch) -> Contribution:
    return Contribution(tmp_path, monkeypatch)


def _key(row: dict) -> tuple[str, str]:
    return (row["label"], row["domain"])


# ── baseline: only the contributor's edits ──────────────────────────────────

def test_unchanged_workbook_changes_nothing(contribution):
    assert contribution.run() == 0, contribution.report
    assert "No edits found" in contribution.report
    assert contribution.unchanged()


def test_old_workbook_does_not_revert_newer_schema_changes(contribution):
    """Changes merged after the download survive; only the contributor's edit lands."""
    c = contribution
    chosen = None
    for sheet in ib.CLASS_MAP:
        top = [item for item in c.slot_rows()
               if item[0] == sheet and not item[2]["domain"]
               and c.editable(item[3], item[4]) and c.own_usage(item[4], item[3]) is None]
        mro_item = next((item for item in top if item[2]["mro"] != "M"), None)
        others = [item for item in top if item is not mro_item]
        if mro_item and len(others) >= 2:
            chosen = (sheet, mro_item, others[0], others[1])
            break
    assert chosen, "needs three editable top-level slots on one sheet, one not mandatory"
    sheet, (_, _, main_mro, mro_slot, _), (_, _, main_desc, desc_slot, _), (_, cells, edited, _, _) = chosen

    # Merged to main after the workbook was downloaded:
    c.edit_schema(desc_slot, description="Changed on main after the download.")
    c.edit_schema(mro_slot, required=True)
    # The contributor's own edit, in the old workbook:
    c.set(cells, "description", "Edited by the contributor.")

    code = c.run()
    assert code in (0, 2), c.report
    now = c.current(sheet)
    assert now[_key(main_desc)]["description"] == "Changed on main after the download."
    assert now[_key(main_mro)]["mro"] == "M"
    assert now[_key(edited)]["description"] == "Edited by the contributor."
    assert "older version of the schema" in c.report


def test_edit_that_conflicts_with_a_newer_change_is_reported(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls) and c.own_usage(cls, slot) is None
        and not r["domain"],
        "editable top-level slot without slot_usage",
    )
    c.edit_schema(slot, description="Changed on main after the download.")
    c.set(cells, "description", "The contributor's version.")

    assert c.run() in (0, 2), c.report
    assert "Conflict" in c.report
    assert c.current(sheet)[_key(row)]["description"] == "The contributor's version."


# ── inheritance-aware writes ────────────────────────────────────────────────

def test_optional_overrides_an_inherited_recommended(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: r["mro"] == "R" and c.editable(slot, cls)
        and c.own_usage(cls, slot) is None
        and "recommended" not in c.slot_node(slot) and "required" not in c.slot_node(slot),
        "slot row that is R only by inheritance",
    )
    c.set(cells, "M / R / O", "O")
    assert c.run() in (0, 2), c.report
    assert c.current(sheet)[_key(row)]["mro"] == "O"


def test_clearing_an_inherited_multivalued_takes_effect(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: r["multivalued"] == "yes" and c.editable(slot, cls)
        and c.own_usage(cls, slot) is None and "multivalued" not in c.slot_node(slot),
        "slot row that is multivalued only by inheritance",
    )
    c.set(cells, "multivalued", None)
    assert c.run() in (0, 2), c.report
    assert c.current(sheet)[_key(row)]["multivalued"] == ""


def test_slot_usage_edit_survives_regeneration(contribution, tmp_path):
    """An edit written to a class's slot_usage shows up in the regenerated
    workbook, and resubmitting that workbook unchanged is a no-op."""
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls)
        and "description" in (c.own_usage(cls, slot) or {}),
        "slot row whose class overrides the description in slot_usage",
    )
    c.set(cells, "description", "Edited through the class's slot_usage.")
    assert c.run() in (0, 2), c.report
    assert c.current(sheet)[_key(row)]["description"] == "Edited through the class's slot_usage."

    again = tmp_path / "regenerated.xlsx"
    s2e.save_workbook(s2e.build_workbook(c.schema_dir), again)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        assert ib.main(again) == 0, out.getvalue()
    assert "No edits found" in out.getvalue()


def test_mro_edit_on_a_shared_slot_stays_with_its_class(contribution):
    c = contribution
    sv = s2e.load_schema_view(c.schema_dir)
    by_slot: dict[str, list] = {}
    for item in c.slot_rows():
        sheet, cells, row, slot, cls = item
        if c.editable(slot, cls):
            by_slot.setdefault(slot, []).append(item)

    pair = None
    for slot, items in by_slot.items():
        for first in items:
            if c.own_usage(first[4], slot) is not None:
                continue
            for other in items:
                if other[4] != first[4] and first[4] not in sv.class_ancestors(other[4]) \
                        and other[2]["mro"] == first[2]["mro"]:
                    pair = (first, other)
                    break
            if pair:
                break
        if pair:
            break
    assert pair, "needs one editable slot shown on two unrelated classes"
    (sheet, cells, row, slot, cls), (other_sheet, _, other_row, _, other_cls) = pair

    new_mro = "M" if row["mro"] != "M" else "O"
    c.set(cells, "M / R / O", new_mro)
    assert c.run() in (0, 2), c.report
    assert c.current(sheet)[_key(row)]["mro"] == new_mro
    assert c.current(other_sheet)[_key(other_row)]["mro"] == other_row["mro"]
    assert c.own_usage(cls, slot) is not None, "the change belongs in the class's slot_usage"


# ── removed rows ────────────────────────────────────────────────────────────

def test_removing_a_nested_slot_row_removes_the_slot(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: r["domain"] and c.editable(slot, cls)
        and slot in (c.class_node(cls).get("slots") or []),
        "nested slot row the class lists itself",
    )
    c.delete(sheet, cells)
    assert c.run() == 2, c.report
    assert slot not in (c.class_node(cls).get("slots") or [])
    assert _key(row) not in c.current(sheet)


def test_removing_an_inherited_slot_row_is_reported(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls)
        and slot not in (c.class_node(cls).get("slots") or [])
        and c.own_usage(cls, slot) is None,
        "slot row a class only inherits",
    )
    c.delete(sheet, cells)
    assert c.run() == 2, c.report
    assert "inherits it from" in c.report
    assert c.unchanged()


def test_rename_is_applied_as_add_and_remove(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: r["domain"] and c.editable(slot, cls)
        and slot in (c.class_node(cls).get("slots") or []),
        "nested slot row the class lists itself",
    )
    c.set(cells, "label", f"{row['label']} renamed")
    assert c.run() == 2, c.report
    assert "renamed" in c.report
    slots = c.class_node(cls).get("slots") or []
    assert slot not in slots and f"{slot}_renamed" in slots


# ── edits that can't be applied are reported ────────────────────────────────

def test_editing_a_read_only_row_is_reported(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: slot not in c.slot_origin,
        "slot row inherited from chemdcat-ap",
    )
    c.set(cells, "description", "A contributor's edit of a read-only row.")
    assert c.run() == 2, c.report
    assert "read-only" in c.report
    assert c.unchanged()


def test_editing_the_reference_sheet_is_reported(contribution):
    c = contribution
    cells, row = c.rows(REFERENCE_SHEET)[0]
    c.set(cells, "M / R / O", "M" if row["mro"] != "M" else "O")
    assert c.run() == 2, c.report
    assert "reference only" in c.report
    assert c.unchanged()


def test_new_slot_without_description_is_flagged(contribution):
    c = contribution
    c.wb["Simulation"].append(["qa bare new field", "slot", "", "O", "string"])
    assert c.run() == 2, c.report
    assert "no description" in c.report
    assert "qa_bare_new_field" in (c.class_node("Simulation").get("slots") or [])


# ── validation ──────────────────────────────────────────────────────────────

@pytest.mark.parametrize(("column", "value", "message"), [
    ("uri",       "NOTAPREFIX:12345",    "does not declare"),
    ("uri",       "not a uri",           "neither a CURIE"),
    ("unit",      "2026-01-02 00:00:00", "looks like a date"),
    ("unit",      "°C",                  "plain ASCII"),
    ("M / R / O", "Recomended",          "Invalid M/R/O"),
])
def test_invalid_values_are_rejected(contribution, column, value, message):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls), "editable slot row",
    )
    c.set(cells, column, value)
    assert c.run() == 3, c.report
    assert message in c.report
    assert c.unchanged()


def test_excel_error_cell_is_rejected(contribution):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls), "editable slot row",
    )
    c.set(cells, "description", "#NAME?")   # what Excel stores for text starting with '='
    assert cells[HEADERS.index("description")].data_type == "e"
    assert c.run() == 3, c.report
    assert "error value" in c.report
    assert c.unchanged()


def test_workbook_without_baseline_is_rejected(contribution):
    c = contribution
    del c.wb[BASELINE_SHEET]
    assert c.run() == 3, c.report
    assert "older template" in c.report
    assert c.unchanged()


# ── verification and rollback ───────────────────────────────────────────────

def test_changes_are_rolled_back_when_verification_fails(contribution, monkeypatch):
    c = contribution
    sheet, cells, row, slot, cls = c.pick(
        lambda s, cells, r, slot, cls: c.editable(slot, cls), "editable slot row",
    )
    c.set(cells, "description", "This edit will be rolled back.")

    def failing_check(changes, reporter, schema_dir=None):
        reporter.error("schema", "test", "forced verification failure")

    monkeypatch.setattr(ib, "verify_displayed", failing_check)
    assert c.run() == 3, c.report
    assert "rolled back" in c.report
    assert c.unchanged()
