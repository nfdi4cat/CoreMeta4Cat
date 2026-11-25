"""
tests/test_schema_graph.py

Checks the class graph behind the interactive class map on the data-class
pages (scripts/schema_graph.py) and that the generated pages embed it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# ── path setup ────────────────────────────────────────────────────────────────
_ROOT    = Path(__file__).parent.parent
_SCRIPTS = _ROOT / "scripts"
_SCHEMA  = _ROOT / "src" / "coremeta4cat" / "schema"

sys.path.insert(0, str(_SCRIPTS))

from generate_schema_docs import (   # noqa: E402
    build_origin_index,
    generate_markdown_for_main_class,
    load_merged_schema,
)
from schema_graph import MAIN_CLASSES, build_schema_graph   # noqa: E402

KINDS = {"range", "choice", "struct", "quantity", "term", "ref"}


@pytest.fixture(scope="module")
def schema() -> dict:
    return load_merged_schema(str(_SCHEMA))


@pytest.fixture(scope="module")
def graph(schema) -> dict:
    _, class_origin = build_origin_index(str(_SCHEMA))
    return build_schema_graph(schema, pages={"Synthesis": "synthesis.md"}, editable=set(class_origin))


def test_roots_and_colours(graph):
    assert graph["roots"] == MAIN_CLASSES
    for root in MAIN_CLASSES:
        assert root in graph["classes"]
        assert set(graph["colors"][root]) == {"M", "R", "O"}


def test_every_linked_class_is_in_the_graph(graph):
    classes = graph["classes"]
    for name, entry in classes.items():
        assert entry["kind"] in KINDS, name
        for field in entry["fields"]:
            assert field["requirement"] in {"M", "R", "O"}
            if field["kind"] == "class":
                assert field["range"] in classes, f"{name}.{field['name']} -> {field['range']}"
        for option in entry["options"]:
            assert option in classes, f"{name} option {option}"


def test_reactor_types_and_shared_fields(graph):
    classes = graph["classes"]
    reactor = classes["ChemicalReactor"]
    assert reactor["kind"] == "choice"
    assert "ElectrochemicalReactor" in reactor["options"]
    shared = {f["name"] for f in reactor["fields"]}
    electro = {f["name"] for f in classes["ElectrochemicalReactor"]["fields"]}
    assert shared < electro, "a reactor type must keep the fields shared by all reactors"


def test_quantitative_range_shows_bounds(graph):
    qr = graph["classes"]["QuantitativeRange"]
    assert qr["kind"] == "range"
    names = [f["name"] for f in qr["fields"]]
    for name in ("min_value", "max_value", "unit"):
        assert name in names


def test_quantities_are_value_and_unit(graph):
    assert graph["classes"]["Temperature"]["kind"] == "quantity"


def test_output_is_deterministic_json(schema):
    assert json.dumps(build_schema_graph(schema)) == json.dumps(build_schema_graph(schema))


def test_pages_are_directory_urls(graph):
    assert graph["pages"] == {"Synthesis": "synthesis/"}


def test_data_class_roles(graph):
    for name in ("Synthesis", "Characterization", "Simulation"):
        assert graph["classes"][name]["role"] == "DataGeneratingActivity"
    assert graph["classes"]["CatalyticReaction"]["role"] == "EvaluatedActivity"


def test_origins_of_data_generating_activities(graph):
    for name in ("Synthesis", "Characterization", "Simulation"):
        origins = [(o["class"], o["field"], o["as"]) for o in graph["origins"][name]]
        # each activity is described in its own slot; was_generated_by only lists ids
        assert origins == [("CatalysisDataset", f"was_generated_by_{name.lower()}", None)]


def test_origins_of_reaction(graph):
    origins = [(o["class"], o["field"], o["as"]) for o in graph["origins"]["CatalyticReaction"]]
    assert ("ReactionMonitoring", "evaluated_activity", "ChemicalReaction") in origins
    assert ("CatalysisDataset", "is_about_activity", None) in origins
    # generic upstream datasets are left out
    assert all(cls != "ReactionMonitoringDataset" for cls, _, _ in origins)


def test_dataset_overview_uses_specific_classes(graph):
    fields = {f["name"]: f for f in graph["overviews"]["CatalysisDataset"]["fields"]}
    assert fields["rdf_type"]["kind"] == "enum"
    assert fields["rdf_type"]["range"] == "CatalysisResearchFieldEnum"
    assert fields["was_generated_by"]["targets"] == ["Synthesis", "Characterization", "Simulation"]
    assert fields["was_generated_by"]["requirement"] == "M"
    for name in ("Synthesis", "Characterization", "Simulation"):
        assert fields[f"was_generated_by_{name.lower()}"]["targets"] == [name]
    # the typed slots follow their parent slot
    names = [f["name"] for f in graph["overviews"]["CatalysisDataset"]["fields"]]
    start = names.index("was_generated_by")
    assert names[start:start + 4] == ["was_generated_by", "was_generated_by_synthesis",
                                      "was_generated_by_characterization", "was_generated_by_simulation"]
    assert fields["is_about_activity"]["targets"] == ["CatalyticReaction"]
    entities = fields["is_about_entity"]["targets"]
    assert "CatalystSample" in entities and "EvaluatedEntity" not in entities
    for field in fields.values():
        for target in field["targets"]:
            assert target in graph["classes"], target


def test_page_embeds_class_map(schema, tmp_path):
    out = tmp_path / "simulation.md"
    generate_markdown_for_main_class(schema, "Simulation", str(out))
    text = out.read_text(encoding="utf-8")
    assert text.startswith("---\nhide:\n  - toc\n---\n")
    assert 'class="cm4c-classmap" data-root="Simulation"' in text
    assert 'data-src="../assets/schema_graph.json"' in text
    # the sunburst chart stays available as the alternative view
    assert 'data-sunburst="../assets/metadata_simulation_hierarchy.html"' in text
    assert (_ROOT / "docs" / "assets" / "metadata_simulation_hierarchy.html").exists()
    assert "<iframe" not in text
