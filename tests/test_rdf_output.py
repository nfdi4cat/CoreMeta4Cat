"""RDF output test: activities get their class IRIs as rdf:type, and every CURIE expands.

Guards against two schema bugs that made the Turtle of every example wrong:

- Activities were typed with a string literal (``<activity> a "Synthesis"``) by a string
  type designator on rdf:type, so no class IRI was asserted at all. Now each kind of
  activity has its own slot on CatalysisDataset (was_generated_by_synthesis,
  was_generated_by_characterization, was_generated_by_simulation) and the RDF dumper types
  every activity with its class_uri.
- A prefix declared only in a module that SchemaView loads after it has cached its
  namespace map (it caches while resolving the DCAT-AP-PLUS import) was not expanded,
  e.g. ``<allotrope.quality:0001159>``. Such prefixes must be declared in coremeta4cat.yaml.
"""
from pathlib import Path

import pytest
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import yaml_loader
from rdflib import PROV, RDF, Graph, Literal, URIRef

from coremeta4cat.datamodel import coremeta4cat as datamodel

REPO_ROOT = Path(__file__).parent.parent
SCHEMA = REPO_ROOT / "src" / "coremeta4cat" / "schema" / "coremeta4cat.yaml"
# Describes one Synthesis, two Characterizations, one Simulation and the CatalyticReaction it
# is about, and uses sample_preparation, whose slot_uri is an allotrope.quality CURIE.
NESTED = REPO_ROOT / "tests" / "data" / "valid" / "CatalysisDataset-002.yaml"
TYPED_SLOTS = {
    "Synthesis": "was_generated_by_synthesis",
    "Characterization": "was_generated_by_characterization",
    "Simulation": "was_generated_by_simulation",
}


@pytest.fixture(scope="module")
def view():
    view = SchemaView(str(SCHEMA))
    view.imports_closure()  # the same calls, in the same order, as rdflib_dumper
    return view


@pytest.fixture(scope="module")
def dataset():
    return yaml_loader.load(str(NESTED), target_class=datamodel.CatalysisDataset)


@pytest.fixture(scope="module")
def graph(view, dataset):
    return Graph().parse(data=rdflib_dumper.dumps(dataset, schemaview=view), format="turtle")


def activities(dataset):
    return [activity for slot in TYPED_SLOTS.values() for activity in getattr(dataset, slot)]


def test_every_schema_curie_expands(view):
    """class_uri, slot_uri and enum meanings must expand with the namespaces the RDF dumper uses."""
    namespaces = view.namespaces()
    curies = {cls.class_uri for cls in view.all_classes().values()}
    curies |= {slot.slot_uri for slot in view.all_slots().values()}
    for cls in view.all_classes().values():
        curies |= {slot.slot_uri for slot in (cls.slot_usage or {}).values()}
    for enum in view.all_enums().values():
        curies |= {pv.meaning for pv in (enum.permissible_values or {}).values()}
    unexpanded = sorted(
        curie for curie in curies
        if curie and ":" in curie and "://" not in curie and curie.split(":", 1)[0] not in namespaces
    )
    assert not unexpanded, f"declare these prefixes in coremeta4cat.yaml: {unexpanded}"


def test_activity_class_uris_are_distinct(view):
    """All three typed slots are prov:wasGeneratedBy, so in RDF only the class tells the activities apart."""
    uris = [view.get_uri(name) for name in (*TYPED_SLOTS, "CatalyticReaction")]
    assert len(uris) == len(set(uris)), uris


def test_typed_slots_load_as_their_class(dataset):
    for cls, slot in TYPED_SLOTS.items():
        entries = getattr(dataset, slot)
        assert entries, f"{NESTED.name} has no {slot}"
        assert {type(activity).__name__ for activity in entries} == {cls}, slot


def test_activities_are_typed_with_their_class_iri(view, dataset, graph):
    for activity in activities(dataset) + list(dataset.is_about_activity):
        subject = URIRef(view.expand_curie(activity.id))
        class_iri = URIRef(view.get_uri(type(activity).class_name, expand=True))
        assert class_iri in set(graph.objects(subject, RDF.type)), activity.id


def test_dataset_links_every_activity_with_prov_was_generated_by(view, dataset, graph):
    linked = set(graph.objects(URIRef(view.expand_curie(dataset.id)), PROV.wasGeneratedBy))
    assert linked == {URIRef(view.expand_curie(activity.id)) for activity in activities(dataset)}


def test_no_literal_rdf_type(graph):
    literals = sorted({str(o) for o in graph.objects(None, RDF.type) if isinstance(o, Literal)})
    assert not literals


def test_no_unexpanded_curie_in_turtle(view, graph):
    declared = {prefix for schema in view.schema_map.values() for prefix in (schema.prefixes or {})}
    unexpanded = sorted({
        str(node) for triple in graph for node in triple
        if isinstance(node, URIRef) and str(node).split(":", 1)[0] in declared
    })
    assert not unexpanded
