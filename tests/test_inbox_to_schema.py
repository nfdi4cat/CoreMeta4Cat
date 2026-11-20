"""
tests/test_inbox_to_schema.py

Regression tests for the inbox → schema pipeline (scripts/inbox_to_schema.py),
focused on adding *new* slots that are assigned to a domain (sub-)class via the
Excel "domain" column.

Background
----------
Previously, a new slot whose "domain" column named a subclass (e.g. anode /
cathode → ElectrochemicalReactor) was silently dropped: it was neither a known
global slot nor present in the class slot_usage, so plan_changes routed it into
the "structural display row" skip branch and _plan_new_slot rejected any
non-empty domain outright. These tests pin the corrected behaviour:

  • a genuinely new domain-assigned slot is planned as a slot_add targeting the
    named subclass and the YAML module that defines it;
  • a real structural slot (own slots:/mixin of the domain class) keeps being
    skipped and is never planned as a new slot;
  • the top-level (empty-domain) path is unchanged;
  • an unrecognised domain is reported as an error rather than written.

The planning-level tests are read-only (plan_changes never writes); the apply
test copies the schema into a tmp dir and redirects SCHEMA_DIR so nothing in the
repository is mutated.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

# ── path setup ──────────────────────────────────────────────────────────────
_ROOT    = Path(__file__).parent.parent
_SCRIPTS = _ROOT / "scripts"
_SCHEMA  = _ROOT / "src" / "coremeta4cat" / "schema"

sys.path.insert(0, str(_SCRIPTS))

import inbox_to_schema as ib                 # noqa: E402
from generate_schema_docs import load_merged_schema  # noqa: E402


# ── helpers ─────────────────────────────────────────────────────────────────

def _slot_row(label: str, domain: str = "", mro: str = "O",
              range_: str = "string", **extra) -> dict:
    """Build one normalised slot row, mirroring parse_excel's output shape."""
    return {
        "label":           label,
        "type":            "slot",
        "domain":          domain,
        "mro":             mro,
        "range":           range_,
        "multivalued":     extra.get("multivalued", ""),
        "inlined_as_list": extra.get("inlined_as_list", ""),
        "unit":            extra.get("unit", ""),
        "uri":             extra.get("uri", ""),
        "description":     extra.get("description", ""),
    }


def _plan(indexes, excel_data):
    """Run the read-only planning phase and return (changes, reporter)."""
    schema, slot_origin, class_origin, label_to_slot, label_to_class = indexes
    reporter = ib.Reporter()
    changes = ib.plan_changes(
        schema, excel_data,
        label_to_slot, label_to_class,
        slot_origin, class_origin,
        reporter,
    )
    return changes, reporter


@pytest.fixture(scope="module")
def indexes():
    """Load the merged schema and build the name/label indexes once."""
    schema = load_merged_schema(str(_SCHEMA))
    slot_origin, class_origin = ib.build_origin_index(_SCHEMA)
    label_to_slot, label_to_class = ib.build_label_index(schema)
    return schema, slot_origin, class_origin, label_to_slot, label_to_class


# ── planning-level tests (read-only) ────────────────────────────────────────

def test_new_slot_with_domain_is_planned_for_subclass(indexes):
    """A new slot assigned to an existing subclass is planned as a slot_add
    targeting that subclass and the YAML module that defines it.

    Uses a synthetic slot name that is never shipped in the schema, so the test
    stays valid even after real domain slots (e.g. anode/cathode) have been
    applied via the pipeline. A hard-coded real name would stop being "new" once
    it lands in the schema and would silently invalidate the assertion.
    """
    schema        = indexes[0]
    label_to_slot = indexes[3]

    label = "qa synthetic electrode probe"
    name  = "qa_synthetic_electrode_probe"

    # Precondition: the slot must genuinely be absent for this test to be
    # meaningful. Asserting it makes the assumption explicit and self-checking.
    assert name not in schema.get("slots", {})
    assert label not in label_to_slot
    assert name not in ib.get_all_class_slots(schema, "ElectrochemicalReactor")

    excel = {"Reaction": [
        _slot_row(label, domain="ElectrochemicalReactor", mro="M"),
    ]}
    changes, reporter = _plan(indexes, excel)

    adds = [c for c in changes if c["type"] == "slot_add" and c["name"] == name]
    assert len(adds) == 1, f"expected exactly one slot_add for '{name}'"
    add = adds[0]
    assert add["schema_class"] == "ElectrochemicalReactor"
    assert add["mro"] == "M"
    assert Path(add["_target"]).name == "coremeta4cat_reaction_ap.yaml"
    assert not reporter.has_errors


def test_structural_subclass_slot_is_not_added(indexes):
    """A slot that already belongs to the domain class -- via the class's own
    slots: list or via a mixin -- keeps being skipped and is never planned as a
    new slot."""
    # 'title'/'description' are in QuantitativeRange.slots:; 'has concentration'
    # reaches CoPrecipitation via PrecipitationMixin. All three are real
    # structural rows emitted by the Excel generator and must stay skips.
    excel = {
        "Reaction": [
            _slot_row("title", domain="QuantitativeRange"),
            _slot_row("description", domain="QuantitativeRange"),
        ],
        "Synthesis": [
            _slot_row("has concentration", domain="CoPrecipitation"),
        ],
    }
    changes, reporter = _plan(indexes, excel)

    new_names = {c["name"] for c in changes if c["type"] == "slot_add"}
    assert "title" not in new_names
    assert "description" not in new_names
    assert "has_concentration" not in new_names
    assert not reporter.has_errors


def test_top_level_new_slot_still_targets_sheet_class(indexes):
    """Regression guard: an empty-domain new slot still attaches to the sheet's
    top-level data class (CatalyticReaction for the Reaction sheet)."""
    excel = {"Reaction": [
        _slot_row("brand new toplevel field", domain="", mro="R"),
    ]}
    changes, reporter = _plan(indexes, excel)

    add = next(
        (c for c in changes
         if c["type"] == "slot_add" and c["name"] == "brand_new_toplevel_field"),
        None,
    )
    assert add is not None
    assert add["schema_class"] == "CatalyticReaction"
    assert not reporter.has_errors


def test_new_slot_with_unknown_domain_is_an_error(indexes):
    """A new slot whose domain is not a known class is reported as an error and
    not planned for application."""
    excel = {"Reaction": [
        _slot_row("weird slot", domain="NotARealClass"),
    ]}
    changes, reporter = _plan(indexes, excel)

    assert reporter.has_errors
    assert not any(
        c["type"] == "slot_add" and c["name"] == "weird_slot" for c in changes
    )


# ── apply-level test (writes into a tmp copy, never the repo) ────────────────

def test_apply_writes_new_domain_slot_into_subclass(tmp_path, monkeypatch):
    """End-to-end: applying a domain-assigned slot_add creates the global slot
    definition and references it from the subclass's slots: list."""
    dst = tmp_path / "schema"
    dst.mkdir()
    for f in _SCHEMA.glob("*.yaml"):
        shutil.copy(f, dst / f.name)
    monkeypatch.setattr(ib, "SCHEMA_DIR", dst)

    reporter = ib.Reporter()
    schema = load_merged_schema(str(dst))
    slot_origin, class_origin = ib.build_origin_index(dst)
    label_to_slot, label_to_class = ib.build_label_index(schema)

    excel = {"Reaction": [
        _slot_row("test electrode", domain="ElectrochemicalReactor", mro="M",
                  description="A test electrode slot."),
    ]}
    changes = ib.plan_changes(
        schema, excel, label_to_slot, label_to_class,
        slot_origin, class_origin, reporter,
    )

    # Apply only our slot_add so unrelated deletion-detection changes (the
    # single-row workbook makes every other Reaction slot look "missing") do
    # not mutate the copy.
    adds = [c for c in changes
            if c["type"] == "slot_add" and c["name"] == "test_electrode"]
    assert len(adds) == 1
    ib.apply_changes(adds, reporter)

    doc = ib._load_yaml(dst / "coremeta4cat_reaction_ap.yaml")

    # (a) global slot definition was created with the required flag
    assert "test_electrode" in (doc.get("slots") or {})
    assert doc["slots"]["test_electrode"].get("required") is True

    # (b) the subclass references the new slot in its slots: list
    er = (doc.get("classes") or {}).get("ElectrochemicalReactor") or {}
    assert "test_electrode" in (er.get("slots") or [])


def test_new_string_slot_writes_range_and_second_run_is_noop(tmp_path, monkeypatch):
    """A new slot with the default ``string`` range gets ``range: string`` written on
    the first run, and re-applying the same workbook row is a no-op.

    Regression test for the idempotency bug where a new string-range slot was created
    without a ``range`` key, so the next run -- with the regenerated Excel, which
    always emits ``string`` -- saw a phantom "range changed -> string" and appended
    ``range: string`` only on the second pass (as happened to anode / cathode).
    """
    dst = tmp_path / "schema"
    dst.mkdir()
    for f in _SCHEMA.glob("*.yaml"):
        shutil.copy(f, dst / f.name)
    monkeypatch.setattr(ib, "SCHEMA_DIR", dst)

    label = "qa idempotent string field"
    name  = "qa_idempotent_string_field"
    excel = {"Reaction": [_slot_row(label, domain="", mro="R", range_="string")]}

    # ── First run: create the slot ──────────────────────────────────────────
    reporter1 = ib.Reporter()
    schema1 = load_merged_schema(str(dst))
    slot_origin1, class_origin1 = ib.build_origin_index(dst)
    label_to_slot1, label_to_class1 = ib.build_label_index(schema1)

    assert name not in schema1.get("slots", {})

    changes1 = ib.plan_changes(
        schema1, excel, label_to_slot1, label_to_class1,
        slot_origin1, class_origin1, reporter1,
    )
    # Apply only our slot_add so single-row deletion-detection does not mutate the copy.
    adds = [c for c in changes1 if c["type"] == "slot_add" and c["name"] == name]
    assert len(adds) == 1
    ib.apply_changes(adds, reporter1)

    # range: string is written explicitly on the first run (fix #2).
    doc = ib._load_yaml(dst / "coremeta4cat_reaction_ap.yaml")
    assert doc["slots"][name].get("range") == "string"

    # ── Second run: same row, against the freshly reloaded schema ───────────
    reporter2 = ib.Reporter()
    schema2 = load_merged_schema(str(dst))
    slot_origin2, class_origin2 = ib.build_origin_index(dst)
    label_to_slot2, label_to_class2 = ib.build_label_index(schema2)

    # The slot is now known, so it routes through the modify path, not slot_add.
    assert label in label_to_slot2

    changes2 = ib.plan_changes(
        schema2, excel, label_to_slot2, label_to_class2,
        slot_origin2, class_origin2, reporter2,
    )

    # No phantom change (range or otherwise) for our slot on the second run.
    slot_changes = [c for c in changes2 if c.get("name") == name]
    assert not slot_changes, (
        f"second run was not idempotent for '{name}': {slot_changes}"
    )


# ── inheritance-aware editability tests ──────────────────────────────────────
#
# CatalyticReaction is_a ChemicalReaction (chemdcat-ap): get_all_class_slots
# now returns chemdcat-ap-inherited slots (e.g. used_reactant, used_catalyst,
# has_reaction_step) alongside CatalyticReaction's own slots. These tests pin
# that inherited, vendored names are visible for reference but are never
# treated as deletable or editable via the inbox workflow -- regression guard
# for the false-positive deletion / silent-edit risk this introduced.

def test_inherited_slot_absent_from_workbook_is_not_flagged_for_deletion(indexes):
    """A workbook containing only CatalyticReaction's own (pre-inheritance)
    slots -- i.e. missing every chemdcat-ap-inherited slot such as
    used_reactant/used_catalyst/has_reaction_step -- must not propose deleting
    any of those inherited slots or the vendored classes reachable through them
    (Reactor, Catalyst, ChemicalProduct, ...). They were never addable/
    removable via Excel, so their absence is not a deletion signal."""
    schema = indexes[0]
    own_only = [
        "catalyst_quantity", "catalyst_type", "catalyst_form",
        "reaction_name", "reactor_temperature_range", "has_atmosphere",
        "experiment_pressure", "feed_composition_range",
        "has_experiment_duration", "product_identification_method",
    ]
    inherited = set(ib.get_all_class_slots(schema, "CatalyticReaction")) - set(own_only)
    assert inherited, "precondition: CatalyticReaction must have inherited slots"

    excel = {"Reaction": [_slot_row(ib.snake_to_readable(n)) for n in own_only]}
    changes, reporter = _plan(indexes, excel)

    deleted_names = {c["name"] for c in changes if c["type"] in ("slot_delete", "class_delete")}
    assert not (deleted_names & inherited), (
        f"inherited names were incorrectly flagged for deletion: {deleted_names & inherited}"
    )


def test_inherited_slot_present_in_workbook_is_not_editable(indexes):
    """A row for a known, inherited chemdcat-ap slot (e.g. 'used reactant')
    that differs from the schema (different M/R/O, URI, description) must not
    produce any change -- it is display-only, never modifiable via inbox."""
    schema, slot_origin = indexes[0], indexes[1]
    assert "used_reactant" not in slot_origin, (
        "precondition: used_reactant must be a vendored (non-editable) slot"
    )

    row = _slot_row(
        "used reactant", mro="M", uri="FAKE:000001",
        description="a hijacked description",
    )
    excel = {"Reaction": [row]}
    changes, reporter = _plan(indexes, excel)

    assert not any(c.get("name") == "used_reactant" for c in changes)
    assert not reporter.has_errors


def test_inherited_class_present_in_workbook_is_not_editable(indexes):
    """A class row for a known, inherited chemdcat-ap class (e.g. 'Catalyst')
    that differs from the schema must not produce any change."""
    schema, slot_origin, class_origin = indexes[0], indexes[1], indexes[2]
    assert "Catalyst" not in class_origin, (
        "precondition: Catalyst must be a vendored (non-editable) class"
    )

    row = _slot_row("Catalyst", description="a hijacked description")
    row["type"] = "class"
    excel = {"Reaction": [row]}
    changes, reporter = _plan(indexes, excel)

    assert not any(c.get("name") == "Catalyst" for c in changes)
    assert not reporter.has_errors


def test_own_slot_absent_from_workbook_is_still_flagged_for_deletion(indexes):
    """Regression guard for the fix itself: a genuinely owned/editable slot
    that is missing from the workbook must still be detected as a deletion --
    the inheritance-awareness fix must not silently disable deletion detection
    for editable slots too."""
    schema = indexes[0]
    # A minimal, otherwise-complete-looking workbook missing one own slot.
    own_minus_one = [
        "catalyst_type", "reactor_temperature_range",
        "has_atmosphere", "experiment_pressure", "feed_composition_range",
        "has_experiment_duration", "product_identification_method",
    ]
    excel = {"Reaction": [_slot_row(ib.snake_to_readable(n)) for n in own_minus_one]}
    changes, reporter = _plan(indexes, excel)

    assert any(
        c["type"] == "slot_delete" and c["name"] == "catalyst_quantity"
        for c in changes
    )


# ── same-batch forward-reference tests ───────────────────────────────────────
#
# A larger submission commonly adds a new slot AND the new class it ranges
# over (or a new class AND its new parent class) together. Without a
# same-batch pre-scan, this always failed: validation only ever saw the
# schema as it existed before the batch, so any forward reference to a class
# defined elsewhere in the same sheet looked "unknown" regardless of row
# order. These tests pin the fix.

def test_new_slot_referencing_new_class_in_same_batch_resolves(indexes):
    """A new slot whose range names a class that is ALSO new in this same
    submission must resolve without error, not fail with 'unknown range'."""
    class_label = "QA Forward Ref Technique"
    class_name = ib._label_to_class_name(class_label)
    assert class_name not in indexes[0].get("classes", {})

    class_row = _slot_row(class_label, domain="ProductIdentificationMethod")
    class_row["type"] = "class"
    slot_row = _slot_row("qa forward ref method", range_=class_name, mro="R")

    changes, reporter = _plan(indexes, {"Reaction": [slot_row, class_row]})

    assert not reporter.has_errors, [d.message for d in reporter._diags if d.level == "error"]
    assert any(c["type"] == "slot_add" and c["range"] == class_name for c in changes)
    assert any(c["type"] == "class_add" and c["name"] == class_name for c in changes)


def test_new_class_with_new_parent_in_same_batch_resolves(indexes):
    """A new class whose domain (parent) is ALSO new in this same submission
    must resolve without error, not fail with 'domain not recognised'."""
    parent_label = "QA Forward Ref Parent"
    child_label = "QA Forward Ref Child"
    parent_name = ib._label_to_class_name(parent_label)
    child_name = ib._label_to_class_name(child_label)
    assert parent_name not in indexes[0].get("classes", {})

    parent_row = _slot_row(parent_label, domain="ProductIdentificationMethod")
    parent_row["type"] = "class"
    child_row = _slot_row(child_label, domain=parent_label)
    child_row["type"] = "class"

    changes, reporter = _plan(indexes, {"Reaction": [parent_row, child_row]})

    assert not reporter.has_errors, [d.message for d in reporter._diags if d.level == "error"]
    assert any(c["type"] == "class_add" and c["name"] == parent_name for c in changes)
    assert any(
        c["type"] == "class_add" and c["name"] == child_name and c["is_a"] == parent_name
        for c in changes
    )


# ── shared/global-slot-change warning tests ──────────────────────────────────

def test_shared_slot_edit_warns_about_other_owner_classes(indexes):
    """Editing a field on a slot that has no existing slot_usage override and
    is directly used by more than one class must warn, naming the other
    classes it will also affect -- the edit changes the slot's single global
    definition, not something scoped to the row's class."""
    schema = indexes[0]
    owners = ib._slot_owner_classes(schema, "has_atmosphere")
    assert len(owners) > 1, "precondition: has_atmosphere must be genuinely shared"

    excel = {"Reaction": [_slot_row("has atmosphere", uri="FAKE:000001")]}
    _, reporter = _plan(indexes, excel)

    shared_warnings = [
        d for d in reporter._diags
        if d.level == "warning"
        and d.context == "slot `has_atmosphere`"
        and "global definition" in d.message
    ]
    assert len(shared_warnings) == 1
    for other in owners:
        if other != "CatalyticReaction":
            assert other in shared_warnings[0].message


def test_non_shared_slot_edit_does_not_warn_about_sharing(indexes):
    """Editing a slot used by only one class must not trigger the shared-slot
    warning, even though other warnings (e.g. a range change) may still
    legitimately fire."""
    schema = indexes[0]
    owners = ib._slot_owner_classes(schema, "reactor_working_volume")
    assert owners == ["CSTR"], "precondition: reactor_working_volume must be single-owner"

    excel = {"Reaction": [_slot_row("reactor working volume", uri="FAKE:000002", domain="CSTR")]}
    _, reporter = _plan(indexes, excel)

    shared_warnings = [
        d for d in reporter._diags
        if d.level == "warning" and "global definition" in d.message
    ]
    assert not shared_warnings


# ── new class + its slots in the same submission (PR #157 regression) ────────
#
# PR #157 added five new CalculatedProperty subclasses together with their
# slots via the inbox. The classes were written to coremeta4cat_simulation_ap
# .yaml (their parent's module), but every new slot whose domain was one of
# those new classes fell back to coremeta4cat.yaml: the definitions landed
# there as orphaned global slots and were never attached to the classes.
# Existing slots reused on the new classes (e.g. miller indices) were dropped
# without any message, and the report still claimed success. These tests pin
# the fix. All names are synthetic so they stay "new" whatever lands later.

_SIM_FILE  = "coremeta4cat_simulation_ap.yaml"
_MAIN_FILE = "coremeta4cat.yaml"


def _class_row(label: str, parent: str) -> dict:
    row = _slot_row(label, domain=parent)
    row["type"] = "class"
    return row


def _tmp_schema(tmp_path, monkeypatch) -> Path:
    """Copy the schema into tmp_path and point the pipeline at the copy."""
    dst = tmp_path / "schema"
    dst.mkdir()
    for f in _SCHEMA.glob("*.yaml"):
        shutil.copy(f, dst / f.name)
    monkeypatch.setattr(ib, "SCHEMA_DIR", dst)
    return dst


def _plan_in(schema_dir: Path, excel_data):
    """Plan against a (tmp) schema dir; returns (changes, reporter)."""
    schema = load_merged_schema(str(schema_dir))
    slot_origin, class_origin = ib.build_origin_index(schema_dir)
    label_to_slot, label_to_class = ib.build_label_index(schema)
    reporter = ib.Reporter()
    changes = ib.plan_changes(
        schema, excel_data, label_to_slot, label_to_class,
        slot_origin, class_origin, reporter,
    )
    return changes, reporter


def _additions(changes, names):
    """Only the additions for our synthetic names -- a partial workbook would
    otherwise flag every other slot of the sheet's class for deletion."""
    return [
        c for c in changes
        if c["type"] in ("class_add", "slot_add", "slot_attach") and c["name"] in names
    ]


def _class_slots(schema_dir: Path, filename: str, class_name: str) -> list:
    doc = ib._load_yaml(schema_dir / filename)
    cls = (doc.get("classes") or {}).get(class_name) or {}
    return list(cls.get("slots") or [])


def _defined_slots(schema_dir: Path, filename: str) -> set:
    return set((ib._load_yaml(schema_dir / filename).get("slots") or {}))


def test_new_slots_on_new_class_land_in_the_class_module(tmp_path, monkeypatch):
    """New slots whose domain is a class added in the same workbook are
    defined in the module of that class and listed in its slots: -- not
    orphaned in coremeta4cat.yaml."""
    dst = _tmp_schema(tmp_path, monkeypatch)
    excel = {"Simulation": [
        _class_row("QaProbeEnergetics", "CalculatedProperty"),
        _slot_row("qa probe adsorbate", domain="QaProbeEnergetics", mro="R"),
        _slot_row("qa probe energy", domain="QaProbeEnergetics",
                  range_="float", unit="eV"),
    ]}
    names = {"QaProbeEnergetics", "qa_probe_adsorbate", "qa_probe_energy"}

    changes, reporter = _plan_in(dst, excel)
    assert not reporter.has_errors
    adds = _additions(changes, names)
    assert {Path(c["_target"]).name for c in adds} == {_SIM_FILE}

    ib.apply_changes(adds, reporter)
    ib.verify_applied(adds, reporter)
    assert not reporter.has_errors, [d.message for d in reporter._diags if d.level == "error"]

    assert _class_slots(dst, _SIM_FILE, "QaProbeEnergetics") == [
        "qa_probe_adsorbate", "qa_probe_energy",
    ]
    assert {"qa_probe_adsorbate", "qa_probe_energy"} <= _defined_slots(dst, _SIM_FILE)
    assert not ({"qa_probe_adsorbate", "qa_probe_energy"} & _defined_slots(dst, _MAIN_FILE))


def test_existing_slot_on_new_class_is_attached(tmp_path, monkeypatch):
    """An existing slot listed on a new class is attached to it; a differing
    M/R/O is scoped to that class via slot_usage, the shared definition stays."""
    dst = _tmp_schema(tmp_path, monkeypatch)
    schema = load_merged_schema(str(dst))
    glob = schema["slots"]["miller_indices"]
    assert not glob.get("required"), "precondition: miller_indices is not mandatory"

    excel = {"Simulation": [
        _class_row("QaProbeSurfaceThing", "CalculatedProperty"),
        _slot_row("miller indices", domain="QaProbeSurfaceThing", mro="M",
                  multivalued="yes" if glob.get("multivalued") else ""),
    ]}
    changes, reporter = _plan_in(dst, excel)
    assert not reporter.has_errors
    attaches = [c for c in changes if c["type"] == "slot_attach"]
    assert len(attaches) == 1
    assert attaches[0]["name"] == "miller_indices"
    assert attaches[0]["schema_class"] == "QaProbeSurfaceThing"
    assert Path(attaches[0]["_target"]).name == _SIM_FILE

    adds = _additions(changes, {"QaProbeSurfaceThing", "miller_indices"})
    ib.apply_changes(adds, reporter)
    ib.verify_applied(adds, reporter)
    assert not reporter.has_errors

    doc = ib._load_yaml(dst / _SIM_FILE)
    cls = doc["classes"]["QaProbeSurfaceThing"]
    assert list(cls["slots"]) == ["miller_indices"]
    assert cls["slot_usage"]["miller_indices"]["required"] is True
    assert not doc["slots"]["miller_indices"].get("required")  # shared def untouched


def test_existing_slot_already_on_class_is_not_attached(indexes):
    """Rows for slots a class already has (own list, inheritance, mixin) are
    never planned as attachments."""
    excel = {"Simulation": [
        _slot_row("material composition", domain="BandGap"),  # via MaterialDescriptorMixin
        _slot_row("miller indices", domain="Surfaces"),       # own slots: list
    ]}
    changes, _ = _plan(indexes, excel)
    assert not [c for c in changes if c["type"] == "slot_attach"]


def test_same_new_slot_on_two_new_classes_is_defined_once(tmp_path, monkeypatch):
    """A new field listed on two new classes gets one definition and is
    attached to both classes."""
    dst = _tmp_schema(tmp_path, monkeypatch)
    excel = {"Simulation": [
        _class_row("QaProbeStepA", "CalculatedProperty"),
        _slot_row("qa probe shared step", domain="QaProbeStepA", mro="R"),
        _class_row("QaProbeStepB", "CalculatedProperty"),
        _slot_row("qa probe shared step", domain="QaProbeStepB", mro="R"),
    ]}
    names = {"QaProbeStepA", "QaProbeStepB", "qa_probe_shared_step"}
    changes, reporter = _plan_in(dst, excel)
    assert not reporter.has_errors
    adds = _additions(changes, names)
    assert [c["type"] for c in adds if c["name"] == "qa_probe_shared_step"] == [
        "slot_add", "slot_attach",
    ]

    ib.apply_changes(adds, reporter)
    ib.verify_applied(adds, reporter)
    assert not reporter.has_errors
    assert _class_slots(dst, _SIM_FILE, "QaProbeStepA") == ["qa_probe_shared_step"]
    assert _class_slots(dst, _SIM_FILE, "QaProbeStepB") == ["qa_probe_shared_step"]


def test_same_new_slot_with_conflicting_definition_is_an_error(indexes):
    """The same new field with different definition values in two rows is
    rejected -- a field has a single shared definition."""
    excel = {"Simulation": [
        _class_row("QaProbeStepA", "CalculatedProperty"),
        _slot_row("qa probe shared step", domain="QaProbeStepA", range_="string"),
        _class_row("QaProbeStepB", "CalculatedProperty"),
        _slot_row("qa probe shared step", domain="QaProbeStepB", range_="float"),
    ]}
    _, reporter = _plan(indexes, excel)
    errors = [d for d in reporter._diags if d.level == "error"]
    assert errors and "range" in errors[0].message


def test_slot_rows_before_class_row_still_attach(tmp_path, monkeypatch):
    """Row order does not matter: slot rows above their new class's row are
    still attached (class_add is applied first)."""
    dst = _tmp_schema(tmp_path, monkeypatch)
    excel = {"Simulation": [
        _slot_row("qa probe early field", domain="QaProbeLateClass"),
        _slot_row("miller indices", domain="QaProbeLateClass"),
        _class_row("QaProbeLateClass", "CalculatedProperty"),
    ]}
    names = {"QaProbeLateClass", "qa_probe_early_field", "miller_indices"}
    changes, reporter = _plan_in(dst, excel)
    assert not reporter.has_errors
    adds = _additions(changes, names)
    ib.apply_changes(adds, reporter)
    ib.verify_applied(adds, reporter)
    assert not reporter.has_errors
    assert _class_slots(dst, _SIM_FILE, "QaProbeLateClass") == [
        "qa_probe_early_field", "miller_indices",
    ]


def test_new_slot_on_class_with_new_parent_targets_ancestor_module(indexes):
    """A slot on a new class whose parent is ALSO new resolves to the module
    of the nearest existing ancestor."""
    excel = {"Simulation": [
        _class_row("QaProbeParentProp", "CalculatedProperty"),
        _class_row("QaProbeChildProp", "QaProbeParentProp"),
        _slot_row("qa probe child field", domain="QaProbeChildProp"),
    ]}
    changes, reporter = _plan(indexes, excel)
    assert not reporter.has_errors
    targets = {
        c["name"]: Path(c["_target"]).name
        for c in changes if c["type"] in ("class_add", "slot_add")
    }
    assert targets == {
        "QaProbeParentProp":    _SIM_FILE,
        "QaProbeChildProp":     _SIM_FILE,
        "qa_probe_child_field": _SIM_FILE,
    }


def test_slot_add_into_wrong_module_fails_loudly(tmp_path, monkeypatch):
    """If a slot cannot be attached because its class is not in the target
    module, apply reports an error instead of writing an orphaned slot and
    claiming success."""
    dst = _tmp_schema(tmp_path, monkeypatch)
    before = _defined_slots(dst, _MAIN_FILE)
    change = {
        "type": "slot_add", "name": "qa_probe_orphan", "label": "qa probe orphan",
        "schema_class": "Surfaces", "range": "string", "mro": "O",
        "description": "", "uri": "", "multivalued": False,
        "inlined_as_list": False, "unit": "",
        "_target": dst / _MAIN_FILE,   # Surfaces lives in the simulation module
    }
    reporter = ib.Reporter()
    ib.apply_changes([change], reporter)

    assert reporter.has_errors
    assert not reporter._applied
    assert _defined_slots(dst, _MAIN_FILE) == before


def test_verify_applied_flags_additions_that_did_not_land(tmp_path, monkeypatch):
    """The post-apply check reports additions that are not in the schema."""
    _tmp_schema(tmp_path, monkeypatch)
    reporter = ib.Reporter()
    ib.verify_applied(
        [{"type": "slot_attach", "name": "qa_probe_missing", "schema_class": "Surfaces"},
         {"type": "class_add", "name": "QaProbeMissingClass"}],
        reporter,
    )
    contexts = {d.context for d in reporter._diags if d.level == "error"}
    assert contexts == {"slot `qa_probe_missing`", "class `QaProbeMissingClass`"}


def test_generated_workbook_plans_no_additions(tmp_path):
    """Regression guard for the attach logic: the workbook generated from the
    current schema must not plan any addition (no false attachments of the
    structural/inherited display rows)."""
    import openpyxl
    from schema_to_excel import (
        build_catcore_sheet, build_intro_sheet, build_legend_sheet, build_sheet,
    )

    schema = load_merged_schema(str(_SCHEMA))
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    build_intro_sheet(wb)
    build_legend_sheet(wb)
    build_catcore_sheet(wb, schema)
    for sheet_title in ib.CLASS_MAP:
        build_sheet(wb, schema, sheet_title)
    path = tmp_path / "generated.xlsx"
    wb.save(str(path))

    reporter = ib.Reporter()
    sheets = ib.validate_structure(path, reporter)
    assert sheets is not None
    slot_origin, class_origin = ib.build_origin_index(_SCHEMA)
    label_to_slot, label_to_class = ib.build_label_index(schema)
    changes = ib.plan_changes(
        schema, ib.parse_excel(sheets), label_to_slot, label_to_class,
        slot_origin, class_origin, reporter,
    )
    assert not reporter.has_errors
    assert not [c for c in changes if c["type"] in ("class_add", "slot_add", "slot_attach")]
