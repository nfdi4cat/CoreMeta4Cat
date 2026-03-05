# Auto generated from catcore.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-04T22:31:48
# Schema: catcore-metadata
#
# id: https://w3id.org/nfdi4cat/catcore
# description: The CatCore describes the minimum information which must be reported with research
#   data concerning the field of catalysis. This guideline helps to handle and
#   standardize data based on the FAIR principle (Findable, Accessible, Interoperable,
#   Reusable).
#
#   Architecture
#   ------------
#   CatCore follows the DCAT-AP-PLUS design patterns (see design-patterns.md):
#
#   - The entry point is the dcat:Dataset, extended here as CatalysisDataset.
#     The catalysis research field is expressed via rdf_type (ClassifierMixin,
#     Pattern 3) using voc4cat terms — analogous to how NMRSpectroscopy uses
#     rdf_type: CHMO:0000613 to classify the measurement type.
#
#   - The four CatCore pillars are modelled as DCAT-AP-PLUS Activity subclasses,
#     following the same pattern as NMRSpectroscopy (is_a: DataGeneratingActivity):
#
#       Synthesis      --> is_a: DataGeneratingActivity
#                        Produces a catalyst (MaterialSample) as had_output_entity.
#                        The PreparationMethod (protocol) is linked via realized_plan.
#
#       Characterization --> is_a: DataGeneratingActivity
#                          Produces measurement data about a catalyst or reaction.
#                          The catalyst/sample is the evaluated_entity.
#                          The CharacterizationTechnique is linked via realized_plan.
#
#       Reaction       --> is_a: EvaluatedActivity
#                        The catalytic process being studied, NOT a data-generating
#                        activity itself. Characterization datasets are about this.
#                        Analogous to the reaction being observed in a reaction
#                        monitoring dataset.
#
#       Simulation     --> is_a: DataGeneratingActivity
#                        Generates computational data about a catalyst or reaction.
#                        The SimulationMethod (protocol) is linked via realized_plan.
#                        The simulation software is carried_out_by: Software.
#
#   - Catalyst samples and precursor materials are modelled as MaterialSample
#     (from material_entities_ap), which is an EvaluatedEntity.
#
#   - Reactors and instruments are modelled as Device (from dcat_ap_plus), which
#     is an AgenticEntity carried_out_by the relevant Activity.
#
#   - PreparationMethod, CharacterizationTechnique, and SimulationMethod are
#     modelled as Plan (from dcat_ap_plus), the protocol realized by the Activity.
#
#   This file is the top-level aggregator. It imports catcore_common (shared
#   slots and enums) and the four subprofile modules.
#
#   Full import hierarchy:
#     catcore.yaml  (this file — aggregator + CatalysisDataset entry point)
#       +-- catcore_common.yaml         (shared slots, enums)
#             +-- chem_dcat_ap          (SubstanceSample, ChemicalSubstance, …)
#                   +-- chemical_reaction_ap
#                         +-- chemical_entities_ap
#                               +-- material_entities_ap
#                                     +-- dcat_ap_plus  (DCAT-AP-PLUS base)
#       +-- catcore_synthesis_ap         (Step 3 — Synthesis, PreparationMethod, mixins)
#       +-- catcore_characterization_ap  (Step 4 — Characterization, 24 techniques, mixins)
#       +-- catcore_reaction_ap          (Step 5 — Reaction, 8 ReactorDesignTypes)
#       +-- catcore_simulation_ap        (Step 6 — Simulation, 4 methods, 12 properties, mixins)
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Decimal, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "1.0.0"

# Namespaces
AFE = CurieNamespace('AFE', 'http://purl.allotrope.org/ontologies/equipment#AFE_')
AFP = CurieNamespace('AFP', 'http://purl.allotrope.org/ontologies/process#AFP_')
AFQ = CurieNamespace('AFQ', 'http://purl.allotrope.org/ontologies/quality#AFQ_')
AFR = CurieNamespace('AFR', 'http://purl.allotrope.org/ontologies/result#AFR_')
AFRL = CurieNamespace('AFRL', 'http://purl.allotrope.org/ontologies/role#AFRL_')
AFX = CurieNamespace('AFX', 'http://purl.allotrope.org/ontologies/property#AFX_')
APOLLO_SV = CurieNamespace('APOLLO_SV', 'http://purl.obolibrary.org/obo/APOLLO_SV_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/data_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MOP = CurieNamespace('MOP', 'http://purl.obolibrary.org/obo/MOP_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PROCO = CurieNamespace('PROCO', 'http://purl.obolibrary.org/obo/PROCO_')
REX = CurieNamespace('REX', 'http://purl.obolibrary.org/obo/REX_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNO = CurieNamespace('RXNO', 'http://purl.obolibrary.org/obo/RXNO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
VOC4CAT = CurieNamespace('VOC4CAT', 'https://w3id.org/nfdi4cat/voc4cat_')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CATCORE = CurieNamespace('catcore', 'https://w3id.org/nfdi4cat/catcore/')
CHEMDCATAP = CurieNamespace('chemdcatap', 'https://nfdi-de.github.io/chem-dcat-ap/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCATAP_PLUS = CurieNamespace('dcatap_plus', 'https://w3id.org/nfdi-de/dcat-ap-plus/')
DCATAPPLUS = CurieNamespace('dcatapplus', 'https://nfdi-de.github.io/dcat-ap-plus/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
EPOS = CurieNamespace('epos', 'https://www.epos-eu.org/epos-dcat-ap#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
MATERIAL_ENTITIES_AP = CurieNamespace('material_entities_ap', 'https://nfdi-de.github.io/chem-dcat-ap/material_entities_ap.yaml#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CATCORE


# Types
class Duration(str):
    """ The datatype that represents durations of time. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration"
    type_model_uri = CATCORE.Duration


class HexBinary(str):
    """ The datatype that represents arbitrary hex-encoded binary data. """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "hexBinary"
    type_model_uri = CATCORE.HexBinary


class NonNegativeInteger(int):
    """ The datatype that represents non-negative integers. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "nonNegativeInteger"
    type_model_uri = CATCORE.NonNegativeInteger


# Class references
class ActivityId(URIorCURIE):
    pass


class AgenticEntityId(URIorCURIE):
    pass


class DataGeneratingActivityId(ActivityId):
    pass


class SynthesisId(DataGeneratingActivityId):
    pass


class CharacterizationId(DataGeneratingActivityId):
    pass


class SimulationId(DataGeneratingActivityId):
    pass


class DataAnalysisId(DataGeneratingActivityId):
    pass


class DatasetId(URIorCURIE):
    pass


class CatalysisDatasetId(DatasetId):
    pass


class AnalysisDatasetId(DatasetId):
    pass


class DefinedTermId(URIorCURIE):
    pass


class DeviceId(AgenticEntityId):
    pass


class ReactorDesignTypeId(DeviceId):
    pass


class ElectrochemicalReactorId(ReactorDesignTypeId):
    pass


class CSTRId(ReactorDesignTypeId):
    pass


class PlugFlowReactorId(ReactorDesignTypeId):
    pass


class AutoclaveId(ReactorDesignTypeId):
    pass


class SlurryReactorId(ReactorDesignTypeId):
    pass


class MicroreactorId(ReactorDesignTypeId):
    pass


class FixedBedReactorId(ReactorDesignTypeId):
    pass


class FluidizedBedReactorId(ReactorDesignTypeId):
    pass


class EntityId(URIorCURIE):
    pass


class EvaluatedActivityId(ActivityId):
    pass


class ReactionId(EvaluatedActivityId):
    pass


class EvaluatedEntityId(EntityId):
    pass


class AnalysisSourceDataId(EvaluatedEntityId):
    pass


class SoftwareId(AgenticEntityId):
    pass


class DocumentId(URIorCURIE):
    pass


class LegalResourceId(URIorCURIE):
    pass


class LicenseDocumentId(URIorCURIE):
    pass


class ResourceId(URIorCURIE):
    pass


class ChemicalReactionId(ActivityId):
    pass


class DissolvingSubstanceId(AgenticEntityId):
    pass


class CatalystId(AgenticEntityId):
    pass


class ReactorId(DeviceId):
    pass


class MaterialEntityId(EntityId):
    pass


class ChemicalEntityId(MaterialEntityId):
    pass


class AtomId(ChemicalEntityId):
    pass


class ChemicalSubstanceId(MaterialEntityId):
    pass


class PolymerId(ChemicalSubstanceId):
    pass


class StartingMaterialId(ChemicalSubstanceId):
    pass


class ReagentId(ChemicalSubstanceId):
    pass


class ChemicalProductId(ChemicalSubstanceId):
    pass


class MaterialSampleId(EvaluatedEntityId):
    pass


class PrecursorId(MaterialSampleId):
    pass


class CatalystSampleId(MaterialSampleId):
    pass


class SubstanceSampleId(MaterialSampleId):
    pass


class PolymerSampleId(SubstanceSampleId):
    pass


@dataclass(repr=False)
class DryingMixin(YAMLRoot):
    """
    Mixin providing drying step parameters. Used by preparation methods that
    include a drying step after synthesis or precipitation
    (Impregnation, CoPrecipitation, DepositionPrecipitation,
    SonochemicalSynthesis, MolecularSynthesis).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DryingMixin"]
    class_class_curie: ClassVar[str] = "catcore:DryingMixin"
    class_name: ClassVar[str] = "DryingMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.DryingMixin

    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalcinationMixin(YAMLRoot):
    """
    Mixin providing calcination step parameters. Used by preparation methods
    that include a thermal calcination step
    (Impregnation, CoPrecipitation, DepositionPrecipitation,
    SonochemicalSynthesis, ExsolutionSynthesis).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CalcinationMixin"]
    class_class_curie: ClassVar[str] = "catcore:CalcinationMixin"
    class_name: ClassVar[str] = "CalcinationMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.CalcinationMixin

    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrecipitationMixin(YAMLRoot):
    """
    Mixin providing precipitation and wet-chemistry step parameters. Used by
    preparation methods based on precipitation from solution
    (CoPrecipitation, DepositionPrecipitation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PrecipitationMixin"]
    class_class_curie: ClassVar[str] = "catcore:PrecipitationMixin"
    class_name: ClassVar[str] = "PrecipitationMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.PrecipitationMixin

    precipitating_agent: Optional[Union[str, list[str]]] = empty_list()
    precipitating_concentration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_ph: Optional[Union[float, list[float]]] = empty_list()
    mixing_rate: Optional[Union[float, list[float]]] = empty_list()
    mixing_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    order_of_addition: Optional[Union[str, list[str]]] = empty_list()
    filtration: Optional[Union[str, list[str]]] = empty_list()
    purification: Optional[Union[str, list[str]]] = empty_list()
    aging_temperature: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.precipitating_agent, list):
            self.precipitating_agent = [self.precipitating_agent] if self.precipitating_agent is not None else []
        self.precipitating_agent = [v if isinstance(v, str) else str(v) for v in self.precipitating_agent]

        if not isinstance(self.precipitating_concentration, list):
            self.precipitating_concentration = [self.precipitating_concentration] if self.precipitating_concentration is not None else []
        self.precipitating_concentration = [v if isinstance(v, float) else float(v) for v in self.precipitating_concentration]

        if not isinstance(self.synthesis_ph, list):
            self.synthesis_ph = [self.synthesis_ph] if self.synthesis_ph is not None else []
        self.synthesis_ph = [v if isinstance(v, float) else float(v) for v in self.synthesis_ph]

        if not isinstance(self.mixing_rate, list):
            self.mixing_rate = [self.mixing_rate] if self.mixing_rate is not None else []
        self.mixing_rate = [v if isinstance(v, float) else float(v) for v in self.mixing_rate]

        if not isinstance(self.mixing_time, list):
            self.mixing_time = [self.mixing_time] if self.mixing_time is not None else []
        self.mixing_time = [v if isinstance(v, float) else float(v) for v in self.mixing_time]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.order_of_addition, list):
            self.order_of_addition = [self.order_of_addition] if self.order_of_addition is not None else []
        self.order_of_addition = [v if isinstance(v, str) else str(v) for v in self.order_of_addition]

        if not isinstance(self.filtration, list):
            self.filtration = [self.filtration] if self.filtration is not None else []
        self.filtration = [v if isinstance(v, str) else str(v) for v in self.filtration]

        if not isinstance(self.purification, list):
            self.purification = [self.purification] if self.purification is not None else []
        self.purification = [v if isinstance(v, str) else str(v) for v in self.purification]

        if not isinstance(self.aging_temperature, list):
            self.aging_temperature = [self.aging_temperature] if self.aging_temperature is not None else []
        self.aging_temperature = [v if isinstance(v, float) else float(v) for v in self.aging_temperature]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThermalSynthesisMixin(YAMLRoot):
    """
    Mixin providing thermal process parameters common to synthesis methods
    carried out at elevated temperature in a closed vessel or reactor
    (Solvothermal, PlasmaAssisted, CombustionSynthesis,
    MicrowaveAssisted, MechanochemicalSynthesis, Sublimation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ThermalSynthesisMixin"]
    class_class_curie: ClassVar[str] = "catcore:ThermalSynthesisMixin"
    class_name: ClassVar[str] = "ThermalSynthesisMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.ThermalSynthesisMixin

    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRaySourceMixin(YAMLRoot):
    """
    Mixin providing X-ray source and monochromator slots, shared by all
    X-ray based techniques (PowderXRD, XRayAbsorptionSpectroscopy, XPS,
    SingleCrystalXRD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["XRaySourceMixin"]
    class_class_curie: ClassVar[str] = "catcore:XRaySourceMixin"
    class_name: ClassVar[str] = "XRaySourceMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.XRaySourceMixin

    xray_source: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnergyRangeMixin(YAMLRoot):
    """
    Mixin providing energy scan range slots, shared by X-ray spectroscopy
    techniques that scan over an energy range (XRayAbsorptionSpectroscopy, XPS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["EnergyRangeMixin"]
    class_class_curie: ClassVar[str] = "catcore:EnergyRangeMixin"
    class_name: ClassVar[str] = "EnergyRangeMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.EnergyRangeMixin

    minimum_energy: Optional[Union[float, list[float]]] = empty_list()
    maximum_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.minimum_energy, list):
            self.minimum_energy = [self.minimum_energy] if self.minimum_energy is not None else []
        self.minimum_energy = [v if isinstance(v, float) else float(v) for v in self.minimum_energy]

        if not isinstance(self.maximum_energy, list):
            self.maximum_energy = [self.maximum_energy] if self.maximum_energy is not None else []
        self.maximum_energy = [v if isinstance(v, float) else float(v) for v in self.maximum_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectronMicroscopyMixin(YAMLRoot):
    """
    Mixin providing electron gun and image parameters shared by electron
    microscopy techniques (TransmissionElectronMicroscopy,
    ScanningElectronMicroscopy).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElectronMicroscopyMixin"]
    class_class_curie: ClassVar[str] = "catcore:ElectronMicroscopyMixin"
    class_name: ClassVar[str] = "ElectronMicroscopyMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectronMicroscopyMixin

    gun_type: Optional[Union[str, list[str]]] = empty_list()
    acceleration_voltage: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gun_type, list):
            self.gun_type = [self.gun_type] if self.gun_type is not None else []
        self.gun_type = [v if isinstance(v, str) else str(v) for v in self.gun_type]

        if not isinstance(self.acceleration_voltage, list):
            self.acceleration_voltage = [self.acceleration_voltage] if self.acceleration_voltage is not None else []
        self.acceleration_voltage = [v if isinstance(v, float) else float(v) for v in self.acceleration_voltage]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureProgramMixin(YAMLRoot):
    """
    Mixin providing temperature-programme parameters shared by thermal
    analysis and temperature-programmed reaction techniques
    (Thermogravimetry, TPO, TPR).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["TemperatureProgramMixin"]
    class_class_curie: ClassVar[str] = "catcore:TemperatureProgramMixin"
    class_name: ClassVar[str] = "TemperatureProgramMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.TemperatureProgramMixin

    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChromatographyMixin(YAMLRoot):
    """
    Mixin providing chromatographic separation parameters shared by
    separation techniques (GCMS, SizeExclusionChromatography, HPLC_MS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ChromatographyMixin"]
    class_class_curie: ClassVar[str] = "catcore:ChromatographyMixin"
    class_name: ClassVar[str] = "ChromatographyMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChromatographyMixin

    column_type: Optional[Union[str, list[str]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()
    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassRangeMixin(YAMLRoot):
    """
    Mixin providing mass-to-charge scan range slots shared by mass
    spectrometry techniques (GCMS, ESI_MS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MassRangeMixin"]
    class_class_curie: ClassVar[str] = "catcore:MassRangeMixin"
    class_name: ClassVar[str] = "MassRangeMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.MassRangeMixin

    mz_minimum: Optional[Union[float, list[float]]] = empty_list()
    mz_maximum: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.mz_minimum, list):
            self.mz_minimum = [self.mz_minimum] if self.mz_minimum is not None else []
        self.mz_minimum = [v if isinstance(v, float) else float(v) for v in self.mz_minimum]

        if not isinstance(self.mz_maximum, list):
            self.mz_maximum = [self.mz_maximum] if self.mz_maximum is not None else []
        self.mz_maximum = [v if isinstance(v, float) else float(v) for v in self.mz_maximum]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhotoluminescenceMixin(YAMLRoot):
    """
    Mixin providing optical excitation/emission parameters shared by
    photoluminescence techniques (PhotoluminescenceSpectroscopy,
    PhotoluminescenceLifetime).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhotoluminescenceMixin"]
    class_class_curie: ClassVar[str] = "catcore:PhotoluminescenceMixin"
    class_name: ClassVar[str] = "PhotoluminescenceMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhotoluminescenceMixin

    excitation_wavelength: Optional[Union[float, list[float]]] = empty_list()
    emission_wavelength: Optional[Union[float, list[float]]] = empty_list()
    optical_filter: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.excitation_wavelength, list):
            self.excitation_wavelength = [self.excitation_wavelength] if self.excitation_wavelength is not None else []
        self.excitation_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_wavelength]

        if not isinstance(self.emission_wavelength, list):
            self.emission_wavelength = [self.emission_wavelength] if self.emission_wavelength is not None else []
        self.emission_wavelength = [v if isinstance(v, float) else float(v) for v in self.emission_wavelength]

        if not isinstance(self.optical_filter, list):
            self.optical_filter = [self.optical_filter] if self.optical_filter is not None else []
        self.optical_filter = [v if isinstance(v, str) else str(v) for v in self.optical_filter]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectrochemistryMixin(YAMLRoot):
    """
    Mixin providing electrochemical cell parameters shared by
    electrochemical characterization techniques (CyclicVoltammetry,
    ConductivityMeasurement).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElectrochemistryMixin"]
    class_class_curie: ClassVar[str] = "catcore:ElectrochemistryMixin"
    class_name: ClassVar[str] = "ElectrochemistryMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectrochemistryMixin

    reference_electrode: Optional[Union[str, list[str]]] = empty_list()
    working_electrode: Optional[Union[str, list[str]]] = empty_list()
    counter_electrode: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_composition: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_concentration: Optional[Union[float, list[float]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.reference_electrode, list):
            self.reference_electrode = [self.reference_electrode] if self.reference_electrode is not None else []
        self.reference_electrode = [v if isinstance(v, str) else str(v) for v in self.reference_electrode]

        if not isinstance(self.working_electrode, list):
            self.working_electrode = [self.working_electrode] if self.working_electrode is not None else []
        self.working_electrode = [v if isinstance(v, str) else str(v) for v in self.working_electrode]

        if not isinstance(self.counter_electrode, list):
            self.counter_electrode = [self.counter_electrode] if self.counter_electrode is not None else []
        self.counter_electrode = [v if isinstance(v, str) else str(v) for v in self.counter_electrode]

        if not isinstance(self.electrolyte_composition, list):
            self.electrolyte_composition = [self.electrolyte_composition] if self.electrolyte_composition is not None else []
        self.electrolyte_composition = [v if isinstance(v, str) else str(v) for v in self.electrolyte_composition]

        if not isinstance(self.electrolyte_concentration, list):
            self.electrolyte_concentration = [self.electrolyte_concentration] if self.electrolyte_concentration is not None else []
        self.electrolyte_concentration = [v if isinstance(v, float) else float(v) for v in self.electrolyte_concentration]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialDescriptorMixin(YAMLRoot):
    """
    Mixin providing material identity slots shared by CalculatedProperty
    subclasses that target a specific material composition and crystal
    structure (DielectricTensors, PhononDispersion, EquationsOfState,
    AqueousStability, GrainBoundaries, ElectronicStructure, Ferroelectrics,
    BandGap).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MaterialDescriptorMixin"]
    class_class_curie: ClassVar[str] = "catcore:MaterialDescriptorMixin"
    class_name: ClassVar[str] = "MaterialDescriptorMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.MaterialDescriptorMixin

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DFTSettingsMixin(YAMLRoot):
    """
    Mixin providing plane-wave DFT numerical settings shared by CalculatedProperty
    subclasses that are computed with periodic DFT (DielectricTensors,
    EquationsOfState, ElectronicStructure, BandGap).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DFTSettingsMixin"]
    class_class_curie: ClassVar[str] = "catcore:DFTSettingsMixin"
    class_name: ClassVar[str] = "DFTSettingsMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.DFTSettingsMixin

    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    See [DCAT-AP specs:Activity](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Activity)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = CATCORE.Activity

    id: Union[str, ActivityId] = None
    title: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    had_input_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_output_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_input_activity: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    carried_out_by: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    part_of: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_output_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_activity", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=AgenticEntity, key_name="id", keyed=True)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Activity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    See [DCAT-AP specs:Agent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Agent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = CATCORE.Agent

    name: Union[str, list[str]] = None
    type: Optional[Union[dict, "Concept"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self.type is not None and not isinstance(self.type, Concept):
            self.type = Concept(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgenticEntity(YAMLRoot):
    """
    An entity that is somehow responsible for an Activity to take place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "AgenticEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.AgenticEntity

    id: Union[str, AgenticEntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgenticEntityId):
            self.id = AgenticEntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=AgenticEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=AgenticEntity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Catalogue(YAMLRoot):
    """
    See [DCAT-AP specs:Catalogue](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Catalogue)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = CATCORE.Catalogue

    description: Union[str, list[str]] = None
    publisher: Union[dict, Agent] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    catalogue: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    creator: Optional[Union[dict, Agent]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    has_part: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    homepage: Optional[Union[dict, "Document"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    record: Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]] = empty_list()
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    service: Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]] = empty_list()
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    themes: Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.publisher):
            self.MissingRequiredField("publisher")
        if not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.catalogue, list):
            self.catalogue = [self.catalogue] if self.catalogue is not None else []
        self.catalogue = [v if isinstance(v, Catalogue) else Catalogue(**as_dict(v)) for v in self.catalogue]

        if self.creator is not None and not isinstance(self.creator, Agent):
            self.creator = Agent(**as_dict(self.creator))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_dataset", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, Catalogue) else Catalogue(**as_dict(v)) for v in self.has_part]

        if self.homepage is not None and not isinstance(self.homepage, Document):
            self.homepage = Document(**as_dict(self.homepage))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.record, list):
            self.record = [self.record] if self.record is not None else []
        self.record = [v if isinstance(v, CatalogueRecord) else CatalogueRecord(**as_dict(v)) for v in self.record]

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        if not isinstance(self.service, list):
            self.service = [self.service] if self.service is not None else []
        self.service = [v if isinstance(v, DataService) else DataService(**as_dict(v)) for v in self.service]

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        if not isinstance(self.themes, list):
            self.themes = [self.themes] if self.themes is not None else []
        self.themes = [v if isinstance(v, ConceptScheme) else ConceptScheme(**as_dict(v)) for v in self.themes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogueRecord(YAMLRoot):
    """
    See [DCAT-AP specs:CatalogueRecord](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CatalogueRecord)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogueRecord"
    class_model_uri: ClassVar[URIRef] = CATCORE.CatalogueRecord

    modification_date: Union[str, XSDDate] = None
    primary_topic: Union[dict, Any] = None
    application_profile: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    change_type: Optional[Union[dict, "Concept"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    listing_date: Optional[Union[str, XSDDate]] = None
    source_metadata: Optional[Union[dict, "CatalogueRecord"]] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modification_date):
            self.MissingRequiredField("modification_date")
        if not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.application_profile, list):
            self.application_profile = [self.application_profile] if self.application_profile is not None else []
        self.application_profile = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.application_profile]

        if self.change_type is not None and not isinstance(self.change_type, Concept):
            self.change_type = Concept(**as_dict(self.change_type))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.listing_date is not None and not isinstance(self.listing_date, XSDDate):
            self.listing_date = XSDDate(self.listing_date)

        if self.source_metadata is not None and not isinstance(self.source_metadata, CatalogueRecord):
            self.source_metadata = CatalogueRecord(**as_dict(self.source_metadata))

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Checksum(YAMLRoot):
    """
    See [DCAT-AP specs:Checksum](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Checksum)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "Checksum"
    class_model_uri: ClassVar[URIRef] = CATCORE.Checksum

    algorithm: Union[dict, "ChecksumAlgorithm"] = None
    checksum_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, ChecksumAlgorithm):
            self.algorithm = ChecksumAlgorithm(**as_dict(self.algorithm))

        if self._is_empty(self.checksum_value):
            self.MissingRequiredField("checksum_value")
        if not isinstance(self.checksum_value, str):
            self.checksum_value = str(self.checksum_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassifierMixin(YAMLRoot):
    """
    A mixin with which an entity of this schema can be classified via an additional rdf:type or dcterms:type assertion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCATAP_PLUS["ClassifierMixin"]
    class_class_curie: ClassVar[str] = "dcatap_plus:ClassifierMixin"
    class_name: ClassVar[str] = "ClassifierMixin"
    class_model_uri: ClassVar[URIRef] = CATCORE.ClassifierMixin

    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataGeneratingActivity(Activity):
    """
    An Activity (process) that has the objective to produce information (in form of a dataset) about another Activity
    or Entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataGeneratingActivity"
    class_model_uri: ClassVar[URIRef] = CATCORE.DataGeneratingActivity

    id: Union[str, DataGeneratingActivityId] = None
    evaluated_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    evaluated_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()
    realized_plan: Optional[Union[dict, "Plan"]] = None
    occurred_in: Optional[Union[dict, "Surrounding"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGeneratingActivityId):
            self.id = DataGeneratingActivityId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="evaluated_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        if self.realized_plan is not None and not isinstance(self.realized_plan, Plan):
            self.realized_plan = Plan(**as_dict(self.realized_plan))

        if self.occurred_in is not None and not isinstance(self.occurred_in, Surrounding):
            self.occurred_in = Surrounding(**as_dict(self.occurred_in))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Synthesis(DataGeneratingActivity):
    """
    A DataGeneratingActivity in which a catalyst is prepared.

    The preparation protocol is linked via realized_plan using a
    PreparationMethod instance. Input materials (Precursors) are linked via
    had_input_entity. The resulting catalyst (CatalystSample) is linked via
    had_output_entity.

    The type of synthesis is further specified via rdf_type using an ontology
    term (e.g. a voc4cat preparation method term), following DCAT-AP-PLUS
    Pattern 3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Synthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.Synthesis

    id: Union[str, SynthesisId] = None
    nominal_composition: Union[str, list[str]] = None
    catalyst_measured_properties: Union[str, list[str]] = None
    had_input_entity: Union[dict[Union[str, PrecursorId], Union[dict, "Precursor"]], list[Union[dict, "Precursor"]]] = empty_dict()
    realized_plan: Union[dict, "PreparationMethod"] = None
    storage_conditions: Optional[Union[str, list[str]]] = empty_list()
    support: Optional[Union[str, list[str]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    sample_pretreatment: Optional[Union[str, list[str]]] = empty_list()
    had_output_entity: Optional[Union[dict[Union[str, CatalystSampleId], Union[dict, "CatalystSample"]], list[Union[dict, "CatalystSample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynthesisId):
            self.id = SynthesisId(self.id)

        if self._is_empty(self.nominal_composition):
            self.MissingRequiredField("nominal_composition")
        if not isinstance(self.nominal_composition, list):
            self.nominal_composition = [self.nominal_composition] if self.nominal_composition is not None else []
        self.nominal_composition = [v if isinstance(v, str) else str(v) for v in self.nominal_composition]

        if self._is_empty(self.catalyst_measured_properties):
            self.MissingRequiredField("catalyst_measured_properties")
        if not isinstance(self.catalyst_measured_properties, list):
            self.catalyst_measured_properties = [self.catalyst_measured_properties] if self.catalyst_measured_properties is not None else []
        self.catalyst_measured_properties = [v if isinstance(v, str) else str(v) for v in self.catalyst_measured_properties]

        if self._is_empty(self.had_input_entity):
            self.MissingRequiredField("had_input_entity")
        self._normalize_inlined_as_list(slot_name="had_input_entity", slot_type=Precursor, key_name="id", keyed=True)

        if self._is_empty(self.realized_plan):
            self.MissingRequiredField("realized_plan")
        if not isinstance(self.realized_plan, PreparationMethod):
            self.realized_plan = PreparationMethod(**as_dict(self.realized_plan))

        if not isinstance(self.storage_conditions, list):
            self.storage_conditions = [self.storage_conditions] if self.storage_conditions is not None else []
        self.storage_conditions = [v if isinstance(v, str) else str(v) for v in self.storage_conditions]

        if not isinstance(self.support, list):
            self.support = [self.support] if self.support is not None else []
        self.support = [v if isinstance(v, str) else str(v) for v in self.support]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.sample_pretreatment, list):
            self.sample_pretreatment = [self.sample_pretreatment] if self.sample_pretreatment is not None else []
        self.sample_pretreatment = [v if isinstance(v, str) else str(v) for v in self.sample_pretreatment]

        self._normalize_inlined_as_list(slot_name="had_output_entity", slot_type=CatalystSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characterization(DataGeneratingActivity):
    """
    A DataGeneratingActivity in which a catalyst sample or catalytic material
    is characterized using an analytical technique.

    The catalyst sample being characterized is linked via evaluated_entity.
    The analytical protocol is linked via realized_plan using a
    CharacterizationTechnique instance. The instrument used is linked via
    carried_out_by as a Device.

    The specific technique type is expressed via rdf_type using an ontology
    term (e.g. CHMO:0000158 for powder XRD, CHMO:0000404 for XPS),
    following DCAT-AP-PLUS Pattern 3 — exactly as NMRSpectroscopy uses
    rdf_type: CHMO:0000613.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Characterization"
    class_model_uri: ClassVar[URIRef] = CATCORE.Characterization

    id: Union[str, CharacterizationId] = None
    equipment: Union[str, list[str]] = None
    realized_plan: Union[dict, "CharacterizationTechnique"] = None
    sample_state: Optional[Union[Union[str, "SampleStateEnum"], list[Union[str, "SampleStateEnum"]]]] = empty_list()
    sample_description: Optional[Union[str, list[str]]] = empty_list()
    sample_preparation: Optional[Union[str, list[str]]] = empty_list()
    sample_pretreatment: Optional[Union[str, list[str]]] = empty_list()
    detector_type: Optional[Union[str, list[str]]] = empty_list()
    evaluated_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CharacterizationId):
            self.id = CharacterizationId(self.id)

        if self._is_empty(self.equipment):
            self.MissingRequiredField("equipment")
        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if self._is_empty(self.realized_plan):
            self.MissingRequiredField("realized_plan")
        if not isinstance(self.realized_plan, CharacterizationTechnique):
            self.realized_plan = CharacterizationTechnique(**as_dict(self.realized_plan))

        if not isinstance(self.sample_state, list):
            self.sample_state = [self.sample_state] if self.sample_state is not None else []
        self.sample_state = [v if isinstance(v, SampleStateEnum) else SampleStateEnum(v) for v in self.sample_state]

        if not isinstance(self.sample_description, list):
            self.sample_description = [self.sample_description] if self.sample_description is not None else []
        self.sample_description = [v if isinstance(v, str) else str(v) for v in self.sample_description]

        if not isinstance(self.sample_preparation, list):
            self.sample_preparation = [self.sample_preparation] if self.sample_preparation is not None else []
        self.sample_preparation = [v if isinstance(v, str) else str(v) for v in self.sample_preparation]

        if not isinstance(self.sample_pretreatment, list):
            self.sample_pretreatment = [self.sample_pretreatment] if self.sample_pretreatment is not None else []
        self.sample_pretreatment = [v if isinstance(v, str) else str(v) for v in self.sample_pretreatment]

        if not isinstance(self.detector_type, list):
            self.detector_type = [self.detector_type] if self.detector_type is not None else []
        self.detector_type = [v if isinstance(v, str) else str(v) for v in self.detector_type]

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Simulation(DataGeneratingActivity):
    """
    A DataGeneratingActivity in which a catalyst, catalytic material, or
    catalytic process is modelled computationally.

    The simulation software is linked via carried_out_by as a Software agent.
    The simulation method (protocol) is linked via realized_plan using a
    SimulationMethod instance. The catalyst model or reaction being simulated
    is linked via evaluated_entity or evaluated_activity.

    The specific simulation type is expressed via rdf_type (e.g. catcore:DFT,
    NCIT:C18097 for molecular dynamics), following DCAT-AP-PLUS Pattern 3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C48936"]
    class_class_curie: ClassVar[str] = "NCIT:C48936"
    class_name: ClassVar[str] = "Simulation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Simulation

    id: Union[str, SimulationId] = None
    software_package: Union[str, list[str]] = None
    calculated_property: Union[Union[dict, "CalculatedProperty"], list[Union[dict, "CalculatedProperty"]]] = None
    realized_plan: Union[Union[dict, "SimulationMethod"], list[Union[dict, "SimulationMethod"]]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None
    carried_out_by: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]] = empty_dict()
    evaluated_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SimulationId):
            self.id = SimulationId(self.id)

        if self._is_empty(self.software_package):
            self.MissingRequiredField("software_package")
        if not isinstance(self.software_package, list):
            self.software_package = [self.software_package] if self.software_package is not None else []
        self.software_package = [v if isinstance(v, str) else str(v) for v in self.software_package]

        if self._is_empty(self.calculated_property):
            self.MissingRequiredField("calculated_property")
        if not isinstance(self.calculated_property, list):
            self.calculated_property = [self.calculated_property] if self.calculated_property is not None else []
        self.calculated_property = [v if isinstance(v, CalculatedProperty) else CalculatedProperty(**as_dict(v)) for v in self.calculated_property]

        if self._is_empty(self.realized_plan):
            self.MissingRequiredField("realized_plan")
        if not isinstance(self.realized_plan, list):
            self.realized_plan = [self.realized_plan] if self.realized_plan is not None else []
        self.realized_plan = [v if isinstance(v, SimulationMethod) else SimulationMethod(**as_dict(v)) for v in self.realized_plan]

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=AgenticEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataAnalysis(DataGeneratingActivity):
    """
    An Activity that evaluates the data produced by another Activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataAnalysis"
    class_model_uri: ClassVar[URIRef] = CATCORE.DataAnalysis

    id: Union[str, DataAnalysisId] = None
    evaluated_entity: Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAnalysisId):
            self.id = DataAnalysisId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=AnalysisSourceData, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataService(YAMLRoot):
    """
    See [DCAT-AP specs:DataService](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = CATCORE.DataService

    endpoint_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    title: Union[str, list[str]] = None
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    endpoint_description: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]] = empty_list()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    publisher: Optional[Union[dict, Agent]] = None
    serves_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.endpoint_URL):
            self.MissingRequiredField("endpoint_URL")
        self._normalize_inlined_as_list(slot_name="endpoint_URL", slot_type=Resource, key_name="id", keyed=True)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="endpoint_description", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, MediaTypeOrExtent) else MediaTypeOrExtent(**as_dict(v)) for v in self.format]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        self._normalize_inlined_as_list(slot_name="serves_dataset", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.theme, list):
            self.theme = [self.theme] if self.theme is not None else []
        self.theme = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.theme]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = CATCORE.Dataset

    id: Union[str, DatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]] = empty_dict()
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    creator: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    dataset_distribution: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_version: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    identifier: Optional[Union[str, list[str]]] = empty_list()
    in_series: Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]] = empty_list()
    is_referenced_by: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    provenance: Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]] = empty_list()
    publisher: Optional[Union[dict, Agent]] = None
    qualified_attribution: Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]] = empty_list()
    qualified_relation: Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]] = empty_list()
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    release_date: Optional[Union[str, XSDDate]] = None
    sample: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    source: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    spatial_resolution: Optional[Decimal] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    temporal_resolution: Optional[str] = None
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    type: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    version: Optional[str] = None
    version_notes: Optional[Union[str, list[str]]] = empty_list()
    is_about_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.was_generated_by):
            self.MissingRequiredField("was_generated_by")
        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.creator]

        if not isinstance(self.dataset_distribution, list):
            self.dataset_distribution = [self.dataset_distribution] if self.dataset_distribution is not None else []
        self.dataset_distribution = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.dataset_distribution]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_version", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if not isinstance(self.in_series, list):
            self.in_series = [self.in_series] if self.in_series is not None else []
        self.in_series = [v if isinstance(v, DatasetSeries) else DatasetSeries(**as_dict(v)) for v in self.in_series]

        self._normalize_inlined_as_list(slot_name="is_referenced_by", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, ProvenanceStatement) else ProvenanceStatement(**as_dict(v)) for v in self.provenance]

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.qualified_attribution, list):
            self.qualified_attribution = [self.qualified_attribution] if self.qualified_attribution is not None else []
        self.qualified_attribution = [v if isinstance(v, Attribution) else Attribution(**as_dict(v)) for v in self.qualified_attribution]

        if not isinstance(self.qualified_relation, list):
            self.qualified_relation = [self.qualified_relation] if self.qualified_relation is not None else []
        self.qualified_relation = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.qualified_relation]

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.sample]

        self._normalize_inlined_as_list(slot_name="source", slot_type=Dataset, key_name="id", keyed=True)

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if not isinstance(self.theme, list):
            self.theme = [self.theme] if self.theme is not None else []
        self.theme = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.theme]

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.type]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.version_notes, list):
            self.version_notes = [self.version_notes] if self.version_notes is not None else []
        self.version_notes = [v if isinstance(v, str) else str(v) for v in self.version_notes]

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalysisDataset(Dataset):
    """
    A dcat:Dataset that contains research data in the field of catalysis.

    The catalysis research field is expressed via rdf_type using a voc4cat
    term from CatalysisResearchFieldEnum (following DCAT-AP-PLUS Pattern 3).
    For example, a dataset from heterogeneous catalysis research would carry:
    rdf_type:
    id: VOC4CAT:0007001
    title: "heterogeneous catalysis"

    The four CatCore minimum information pillars are linked via the slots
    below, each pointing to the corresponding DataGeneratingActivity or
    EvaluatedActivity subclass defined in the CatCore subprofile modules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "CatalysisDataset"
    class_model_uri: ClassVar[URIRef] = CATCORE.CatalysisDataset

    id: Union[str, CatalysisDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None
    was_generated_by: Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()
    is_about_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalysisDatasetId):
            self.id = CatalysisDatasetId(self.id)

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisDataset(Dataset):
    """
    A Dataset that was generated by an analysis of some previously generated data. For example, a dataset that
    contains the data of an assignment of a chemical structure to a sample based on the spectral data obtained from
    the sample is an AnalyticalDataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "AnalysisDataset"
    class_model_uri: ClassVar[URIRef] = CATCORE.AnalysisDataset

    id: Union[str, AnalysisDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisDatasetId):
            self.id = AnalysisDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataAnalysis, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetSeries(YAMLRoot):
    """
    See [DCAT-AP specs:DatasetSeries](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DatasetSeries)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "DatasetSeries"
    class_model_uri: ClassVar[URIRef] = CATCORE.DatasetSeries

    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    publisher: Optional[Union[dict, Agent]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DefinedTerm(YAMLRoot):
    """
    A word, name, acronym or phrase that is defined in a controlled vocabulary (CV) and that is used to provide an
    additional rdf:type or dcterms:type of a class within this schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = CATCORE.DefinedTerm

    id: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    from_CV: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermId):
            self.id = DefinedTermId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.from_CV is not None and not isinstance(self.from_CV, URIorCURIE):
            self.from_CV = URIorCURIE(self.from_CV)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Device(AgenticEntity):
    """
    A material instrument that is designed to perform a function primarily by means of its mechanical or electrical
    nature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = CATCORE.Device

    id: Union[str, DeviceId] = None
    has_part: Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Device, key_name="id", keyed=True)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactorDesignType(Device):
    """
    Abstract Device representing the type of reactor used in a catalytic experiment.
    Concrete subclasses specify the reactor geometry and operating mode.
    Linked from Reaction via carried_out_by.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007018"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007018"
    class_name: ClassVar[str] = "ReactorDesignType"
    class_model_uri: ClassVar[URIRef] = CATCORE.ReactorDesignType

    id: Union[str, ReactorDesignTypeId] = None

@dataclass(repr=False)
class ElectrochemicalReactor(ReactorDesignType):
    """
    Electrochemical reactor used in electrocatalytic experiments, including
    H-cells, flow cells, and membrane electrode assemblies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000193"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000193"
    class_name: ClassVar[str] = "ElectrochemicalReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectrochemicalReactor

    id: Union[str, ElectrochemicalReactorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElectrochemicalReactorId):
            self.id = ElectrochemicalReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CSTR(ReactorDesignType):
    """
    Continuous stirred tank reactor (CSTR) — a well-mixed, continuous-flow
    reactor operating at steady state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007019"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007019"
    class_name: ClassVar[str] = "CSTR"
    class_model_uri: ClassVar[URIRef] = CATCORE.CSTR

    id: Union[str, CSTRId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CSTRId):
            self.id = CSTRId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlugFlowReactor(ReactorDesignType):
    """
    Plug flow reactor (PFR) — a tubular reactor in which reactant composition
    varies along the axis with no axial mixing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007102"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007102"
    class_name: ClassVar[str] = "PlugFlowReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.PlugFlowReactor

    id: Union[str, PlugFlowReactorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlugFlowReactorId):
            self.id = PlugFlowReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Autoclave(ReactorDesignType):
    """
    Autoclave reactor — a sealed pressure vessel for batch reactions at
    elevated temperature and/or pressure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C93052"]
    class_class_curie: ClassVar[str] = "NCIT:C93052"
    class_name: ClassVar[str] = "Autoclave"
    class_model_uri: ClassVar[URIRef] = CATCORE.Autoclave

    id: Union[str, AutoclaveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutoclaveId):
            self.id = AutoclaveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlurryReactor(ReactorDesignType):
    """
    Slurry reactor — a three-phase reactor in which catalyst particles are
    suspended in a liquid phase through which gas is bubbled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SlurryReactor"]
    class_class_curie: ClassVar[str] = "catcore:SlurryReactor"
    class_name: ClassVar[str] = "SlurryReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.SlurryReactor

    id: Union[str, SlurryReactorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlurryReactorId):
            self.id = SlurryReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Microreactor(ReactorDesignType):
    """
    Microreactor — a miniaturised flow reactor with characteristic dimensions
    in the sub-millimetre range, enabling precise thermal control and rapid
    screening.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000234"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000234"
    class_name: ClassVar[str] = "Microreactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.Microreactor

    id: Union[str, MicroreactorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicroreactorId):
            self.id = MicroreactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixedBedReactor(ReactorDesignType):
    """
    Fixed bed reactor — a tubular reactor packed with a stationary catalyst bed.
    The most common reactor type in heterogeneous catalysis testing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["FixedBedReactor"]
    class_class_curie: ClassVar[str] = "catcore:FixedBedReactor"
    class_name: ClassVar[str] = "FixedBedReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.FixedBedReactor

    id: Union[str, FixedBedReactorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixedBedReactorId):
            self.id = FixedBedReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FluidizedBedReactor(ReactorDesignType):
    """
    Fluidized bed reactor — a reactor in which the catalyst particles are
    suspended in an upward-flowing gas or liquid stream.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["FluidizedBedReactor"]
    class_class_curie: ClassVar[str] = "catcore:FluidizedBedReactor"
    class_name: ClassVar[str] = "FluidizedBedReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.FluidizedBedReactor

    id: Union[str, FluidizedBedReactorId] = None
    gas_distributor_type: Optional[Union[str, list[str]]] = empty_list()
    bed_expansion_height: Optional[Union[float, list[float]]] = empty_list()
    bubble_size_distribution: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FluidizedBedReactorId):
            self.id = FluidizedBedReactorId(self.id)

        if not isinstance(self.gas_distributor_type, list):
            self.gas_distributor_type = [self.gas_distributor_type] if self.gas_distributor_type is not None else []
        self.gas_distributor_type = [v if isinstance(v, str) else str(v) for v in self.gas_distributor_type]

        if not isinstance(self.bed_expansion_height, list):
            self.bed_expansion_height = [self.bed_expansion_height] if self.bed_expansion_height is not None else []
        self.bed_expansion_height = [v if isinstance(v, float) else float(v) for v in self.bed_expansion_height]

        if self.bubble_size_distribution is not None and not isinstance(self.bubble_size_distribution, str):
            self.bubble_size_distribution = str(self.bubble_size_distribution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distribution(YAMLRoot):
    """
    See [DCAT-AP specs:Distribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = CATCORE.Distribution

    access_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    access_service: Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]] = empty_list()
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    availability: Optional[Union[dict, "Concept"]] = None
    byte_size: Optional[int] = None
    checksum: Optional[Union[dict, Checksum]] = None
    compression_format: Optional[Union[dict, "MediaType"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    download_URL: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[dict, "MediaTypeOrExtent"]] = None
    has_policy: Optional[Union[dict, "Policy"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    linked_schemas: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    media_type: Optional[Union[dict, "MediaType"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    packaging_format: Optional[Union[dict, "MediaType"]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    spatial_resolution: Optional[Decimal] = None
    status: Optional[Union[dict, "Concept"]] = None
    temporal_resolution: Optional[str] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_URL):
            self.MissingRequiredField("access_URL")
        self._normalize_inlined_as_list(slot_name="access_URL", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.access_service, list):
            self.access_service = [self.access_service] if self.access_service is not None else []
        self.access_service = [v if isinstance(v, DataService) else DataService(**as_dict(v)) for v in self.access_service]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if self.availability is not None and not isinstance(self.availability, Concept):
            self.availability = Concept(**as_dict(self.availability))

        if self.byte_size is not None and not isinstance(self.byte_size, int):
            self.byte_size = int(self.byte_size)

        if self.checksum is not None and not isinstance(self.checksum, Checksum):
            self.checksum = Checksum(**as_dict(self.checksum))

        if self.compression_format is not None and not isinstance(self.compression_format, MediaType):
            self.compression_format = MediaType(**as_dict(self.compression_format))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="download_URL", slot_type=Resource, key_name="id", keyed=True)

        if self.format is not None and not isinstance(self.format, MediaTypeOrExtent):
            self.format = MediaTypeOrExtent(**as_dict(self.format))

        if self.has_policy is not None and not isinstance(self.has_policy, Policy):
            self.has_policy = Policy(**as_dict(self.has_policy))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if not isinstance(self.linked_schemas, list):
            self.linked_schemas = [self.linked_schemas] if self.linked_schemas is not None else []
        self.linked_schemas = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.linked_schemas]

        if self.media_type is not None and not isinstance(self.media_type, MediaType):
            self.media_type = MediaType(**as_dict(self.media_type))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.packaging_format is not None and not isinstance(self.packaging_format, MediaType):
            self.packaging_format = MediaType(**as_dict(self.packaging_format))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if self.status is not None and not isinstance(self.status, Concept):
            self.status = Concept(**as_dict(self.status))

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    A physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CATCORE.Entity

    id: Union[str, EntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedActivity(Activity):
    """
    An activity or process that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "EvaluatedActivity"
    class_model_uri: ClassVar[URIRef] = CATCORE.EvaluatedActivity

    id: Union[str, EvaluatedActivityId] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedActivityId):
            self.id = EvaluatedActivityId(self.id)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reaction(EvaluatedActivity):
    """
    An EvaluatedActivity representing the catalytic reaction being studied.

    Reaction is NOT a DataGeneratingActivity — it is the catalytic process
    being observed, not the process that generates the dataset. A CatalysisDataset
    is linked to the Reaction it is about via is_about_activity.

    For operando experiments (e.g. in-situ XRD during a reaction), the dataset
    carries both:
    was_generated_by: Characterization  (the measurement producing data)
    is_about_activity: Reaction         (the catalytic process being monitored)

    The reactor is linked via carried_out_by as a ReactorDesignType (Device).
    Reactants are linked via had_input_entity. The type of catalytic reaction
    (e.g. ammonia synthesis, CO oxidation) is expressed via rdf_type using a
    voc4cat or ChemO term.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010345"]
    class_class_curie: ClassVar[str] = "SIO:010345"
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = CATCORE.Reaction

    id: Union[str, ReactionId] = None
    catalyst_quantity: Union[float, list[float]] = None
    reactant: Union[str, list[str]] = None
    carried_out_by: Union[dict[Union[str, ReactorDesignTypeId], Union[dict, ReactorDesignType]], list[Union[dict, ReactorDesignType]]] = empty_dict()
    product_identification_method: Union[Union[dict, "ProductIdentificationMethod"], list[Union[dict, "ProductIdentificationMethod"]]] = None
    catalyst_type: Optional[Union[str, list[str]]] = empty_list()
    reactor_temperature_range: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    experiment_pressure: Optional[Union[float, list[float]]] = empty_list()
    feed_composition_range: Optional[Union[str, list[str]]] = empty_list()
    experiment_duration: Optional[Union[float, list[float]]] = empty_list()
    rdf_type: Optional[Union[dict, DefinedTerm]] = None
    had_input_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        if self._is_empty(self.catalyst_quantity):
            self.MissingRequiredField("catalyst_quantity")
        if not isinstance(self.catalyst_quantity, list):
            self.catalyst_quantity = [self.catalyst_quantity] if self.catalyst_quantity is not None else []
        self.catalyst_quantity = [v if isinstance(v, float) else float(v) for v in self.catalyst_quantity]

        if self._is_empty(self.reactant):
            self.MissingRequiredField("reactant")
        if not isinstance(self.reactant, list):
            self.reactant = [self.reactant] if self.reactant is not None else []
        self.reactant = [v if isinstance(v, str) else str(v) for v in self.reactant]

        if self._is_empty(self.carried_out_by):
            self.MissingRequiredField("carried_out_by")
        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=ReactorDesignType, key_name="id", keyed=True)

        if self._is_empty(self.product_identification_method):
            self.MissingRequiredField("product_identification_method")
        if not isinstance(self.product_identification_method, list):
            self.product_identification_method = [self.product_identification_method] if self.product_identification_method is not None else []
        self.product_identification_method = [v if isinstance(v, ProductIdentificationMethod) else ProductIdentificationMethod(**as_dict(v)) for v in self.product_identification_method]

        if not isinstance(self.catalyst_type, list):
            self.catalyst_type = [self.catalyst_type] if self.catalyst_type is not None else []
        self.catalyst_type = [v if isinstance(v, str) else str(v) for v in self.catalyst_type]

        if not isinstance(self.reactor_temperature_range, list):
            self.reactor_temperature_range = [self.reactor_temperature_range] if self.reactor_temperature_range is not None else []
        self.reactor_temperature_range = [v if isinstance(v, str) else str(v) for v in self.reactor_temperature_range]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.experiment_pressure, list):
            self.experiment_pressure = [self.experiment_pressure] if self.experiment_pressure is not None else []
        self.experiment_pressure = [v if isinstance(v, float) else float(v) for v in self.experiment_pressure]

        if not isinstance(self.feed_composition_range, list):
            self.feed_composition_range = [self.feed_composition_range] if self.feed_composition_range is not None else []
        self.feed_composition_range = [v if isinstance(v, str) else str(v) for v in self.feed_composition_range]

        if not isinstance(self.experiment_duration, list):
            self.experiment_duration = [self.experiment_duration] if self.experiment_duration is not None else []
        self.experiment_duration = [v if isinstance(v, float) else float(v) for v in self.experiment_duration]

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        self._normalize_inlined_as_list(slot_name="had_input_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedEntity(Entity):
    """
    An Entity that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "EvaluatedEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.EvaluatedEntity

    id: Union[str, EvaluatedEntityId] = None
    was_generated_by: Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]] = empty_dict()
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedEntityId):
            self.id = EvaluatedEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=Activity, key_name="id", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisSourceData(EvaluatedEntity):
    """
    Information that was evaluated within a DataAnalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "AnalysisSourceData"
    class_model_uri: ClassVar[URIRef] = CATCORE.AnalysisSourceData

    id: Union[str, AnalysisSourceDataId] = None
    was_generated_by: Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisSourceDataId):
            self.id = AnalysisSourceDataId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class Kind(YAMLRoot):
    """
    See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "Kind"
    class_model_uri: ClassVar[URIRef] = CATCORE.Kind


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    See [DCAT-AP specs:Location](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Location)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Location"]
    class_class_curie: ClassVar[str] = "dcterms:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = CATCORE.Location

    bbox: Optional[str] = None
    centroid: Optional[str] = None
    geometry: Optional[Union[dict, "Geometry"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bbox is not None and not isinstance(self.bbox, str):
            self.bbox = str(self.bbox)

        if self.centroid is not None and not isinstance(self.centroid, str):
            self.centroid = str(self.centroid)

        if self.geometry is not None and not isinstance(self.geometry, Geometry):
            self.geometry = Geometry(**as_dict(self.geometry))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plan(YAMLRoot):
    """
    A piece of information that specifies how an activity has to be carried out by its agents including what kind of
    steps have to be taken and what kind of parameters have to be met/set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Plan"]
    class_class_curie: ClassVar[str] = "prov:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = CATCORE.Plan

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


class PreparationMethod(Plan):
    """
    An abstract Plan describing the protocol used to prepare a catalyst.
    Concrete subclasses (Impregnation, CoPrecipitation, …) specify the
    method-specific parameters. Linked from Synthesis via realized_plan.

    The specific preparation method type should additionally be expressed
    via rdf_type on the Synthesis activity using a voc4cat term
    (e.g. VOC4CAT:0007016 for preparation method).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "PreparationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.PreparationMethod


@dataclass(repr=False)
class Impregnation(PreparationMethod):
    """
    Catalyst preparation by impregnation: a solution of the active phase
    precursor is brought into contact with the support material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Impregnation"]
    class_class_curie: ClassVar[str] = "catcore:Impregnation"
    class_name: ClassVar[str] = "Impregnation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Impregnation

    impregnation_type: Optional[Union[Union[str, "ImpregnationTypeEnum"], list[Union[str, "ImpregnationTypeEnum"]]]] = empty_list()
    impregnation_duration: Optional[Union[float, list[float]]] = empty_list()
    impregnation_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.impregnation_type, list):
            self.impregnation_type = [self.impregnation_type] if self.impregnation_type is not None else []
        self.impregnation_type = [v if isinstance(v, ImpregnationTypeEnum) else ImpregnationTypeEnum(v) for v in self.impregnation_type]

        if not isinstance(self.impregnation_duration, list):
            self.impregnation_duration = [self.impregnation_duration] if self.impregnation_duration is not None else []
        self.impregnation_duration = [v if isinstance(v, float) else float(v) for v in self.impregnation_duration]

        if not isinstance(self.impregnation_temperature, list):
            self.impregnation_temperature = [self.impregnation_temperature] if self.impregnation_temperature is not None else []
        self.impregnation_temperature = [v if isinstance(v, float) else float(v) for v in self.impregnation_temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoPrecipitation(PreparationMethod):
    """
    Catalyst preparation by co-precipitation: precursor salts are
    simultaneously precipitated from solution by a precipitating agent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CoPrecipitation"]
    class_class_curie: ClassVar[str] = "catcore:CoPrecipitation"
    class_name: ClassVar[str] = "CoPrecipitation"
    class_model_uri: ClassVar[URIRef] = CATCORE.CoPrecipitation

    precipitating_agent: Optional[Union[str, list[str]]] = empty_list()
    precipitating_concentration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_ph: Optional[Union[float, list[float]]] = empty_list()
    mixing_rate: Optional[Union[float, list[float]]] = empty_list()
    mixing_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    order_of_addition: Optional[Union[str, list[str]]] = empty_list()
    filtration: Optional[Union[str, list[str]]] = empty_list()
    purification: Optional[Union[str, list[str]]] = empty_list()
    aging_temperature: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.precipitating_agent, list):
            self.precipitating_agent = [self.precipitating_agent] if self.precipitating_agent is not None else []
        self.precipitating_agent = [v if isinstance(v, str) else str(v) for v in self.precipitating_agent]

        if not isinstance(self.precipitating_concentration, list):
            self.precipitating_concentration = [self.precipitating_concentration] if self.precipitating_concentration is not None else []
        self.precipitating_concentration = [v if isinstance(v, float) else float(v) for v in self.precipitating_concentration]

        if not isinstance(self.synthesis_ph, list):
            self.synthesis_ph = [self.synthesis_ph] if self.synthesis_ph is not None else []
        self.synthesis_ph = [v if isinstance(v, float) else float(v) for v in self.synthesis_ph]

        if not isinstance(self.mixing_rate, list):
            self.mixing_rate = [self.mixing_rate] if self.mixing_rate is not None else []
        self.mixing_rate = [v if isinstance(v, float) else float(v) for v in self.mixing_rate]

        if not isinstance(self.mixing_time, list):
            self.mixing_time = [self.mixing_time] if self.mixing_time is not None else []
        self.mixing_time = [v if isinstance(v, float) else float(v) for v in self.mixing_time]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.order_of_addition, list):
            self.order_of_addition = [self.order_of_addition] if self.order_of_addition is not None else []
        self.order_of_addition = [v if isinstance(v, str) else str(v) for v in self.order_of_addition]

        if not isinstance(self.filtration, list):
            self.filtration = [self.filtration] if self.filtration is not None else []
        self.filtration = [v if isinstance(v, str) else str(v) for v in self.filtration]

        if not isinstance(self.purification, list):
            self.purification = [self.purification] if self.purification is not None else []
        self.purification = [v if isinstance(v, str) else str(v) for v in self.purification]

        if not isinstance(self.aging_temperature, list):
            self.aging_temperature = [self.aging_temperature] if self.aging_temperature is not None else []
        self.aging_temperature = [v if isinstance(v, float) else float(v) for v in self.aging_temperature]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolGel(PreparationMethod):
    """
    Catalyst preparation by the sol-gel process: hydrolysis and condensation
    of precursor molecules to form a colloidal network (gel).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SolGel"]
    class_class_curie: ClassVar[str] = "catcore:SolGel"
    class_name: ClassVar[str] = "SolGel"
    class_model_uri: ClassVar[URIRef] = CATCORE.SolGel

    hydrolysis_ratio: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()
    drying: Optional[Union[str, list[str]]] = empty_list()
    surfactant_template: Optional[Union[str, list[str]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.hydrolysis_ratio, list):
            self.hydrolysis_ratio = [self.hydrolysis_ratio] if self.hydrolysis_ratio is not None else []
        self.hydrolysis_ratio = [v if isinstance(v, float) else float(v) for v in self.hydrolysis_ratio]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        if not isinstance(self.drying, list):
            self.drying = [self.drying] if self.drying is not None else []
        self.drying = [v if isinstance(v, str) else str(v) for v in self.drying]

        if not isinstance(self.surfactant_template, list):
            self.surfactant_template = [self.surfactant_template] if self.surfactant_template is not None else []
        self.surfactant_template = [v if isinstance(v, str) else str(v) for v in self.surfactant_template]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Solvothermal(PreparationMethod):
    """
    Catalyst preparation under elevated temperature and pressure in a
    sealed vessel using a non-aqueous solvent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Solvothermal"]
    class_class_curie: ClassVar[str] = "catcore:Solvothermal"
    class_name: ClassVar[str] = "Solvothermal"
    class_model_uri: ClassVar[URIRef] = CATCORE.Solvothermal

    filling_volume: Optional[Union[float, list[float]]] = empty_list()
    stirrer_type: Optional[Union[str, list[str]]] = empty_list()
    cooling_rate: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.filling_volume, list):
            self.filling_volume = [self.filling_volume] if self.filling_volume is not None else []
        self.filling_volume = [v if isinstance(v, float) else float(v) for v in self.filling_volume]

        if not isinstance(self.stirrer_type, list):
            self.stirrer_type = [self.stirrer_type] if self.stirrer_type is not None else []
        self.stirrer_type = [v if isinstance(v, str) else str(v) for v in self.stirrer_type]

        if not isinstance(self.cooling_rate, list):
            self.cooling_rate = [self.cooling_rate] if self.cooling_rate is not None else []
        self.cooling_rate = [v if isinstance(v, float) else float(v) for v in self.cooling_rate]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlasmaAssisted(PreparationMethod):
    """
    Catalyst preparation using plasma treatment to modify surface
    properties or deposit active components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PlasmaAssisted"]
    class_class_curie: ClassVar[str] = "catcore:PlasmaAssisted"
    class_name: ClassVar[str] = "PlasmaAssisted"
    class_model_uri: ClassVar[URIRef] = CATCORE.PlasmaAssisted

    plasma_type: Optional[Union[str, list[str]]] = empty_list()
    power_input: Optional[Union[float, list[float]]] = empty_list()
    exposure_time: Optional[Union[float, list[float]]] = empty_list()
    synthesis_pressure: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.plasma_type, list):
            self.plasma_type = [self.plasma_type] if self.plasma_type is not None else []
        self.plasma_type = [v if isinstance(v, str) else str(v) for v in self.plasma_type]

        if not isinstance(self.power_input, list):
            self.power_input = [self.power_input] if self.power_input is not None else []
        self.power_input = [v if isinstance(v, float) else float(v) for v in self.power_input]

        if not isinstance(self.exposure_time, list):
            self.exposure_time = [self.exposure_time] if self.exposure_time is not None else []
        self.exposure_time = [v if isinstance(v, float) else float(v) for v in self.exposure_time]

        if not isinstance(self.synthesis_pressure, list):
            self.synthesis_pressure = [self.synthesis_pressure] if self.synthesis_pressure is not None else []
        self.synthesis_pressure = [v if isinstance(v, float) else float(v) for v in self.synthesis_pressure]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CombustionSynthesis(PreparationMethod):
    """
    Catalyst preparation by combustion of a fuel/oxidizer mixture,
    producing metal oxide catalysts in a single rapid step.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CombustionSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:CombustionSynthesis"
    class_name: ClassVar[str] = "CombustionSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.CombustionSynthesis

    fuel: Optional[Union[str, list[str]]] = empty_list()
    oxidizer: Optional[Union[str, list[str]]] = empty_list()
    fuel_to_oxidizer_ratio: Optional[Union[float, list[float]]] = empty_list()
    set_temperature: Optional[Union[float, list[float]]] = empty_list()
    post_treatment: Optional[Union[str, list[str]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fuel, list):
            self.fuel = [self.fuel] if self.fuel is not None else []
        self.fuel = [v if isinstance(v, str) else str(v) for v in self.fuel]

        if not isinstance(self.oxidizer, list):
            self.oxidizer = [self.oxidizer] if self.oxidizer is not None else []
        self.oxidizer = [v if isinstance(v, str) else str(v) for v in self.oxidizer]

        if not isinstance(self.fuel_to_oxidizer_ratio, list):
            self.fuel_to_oxidizer_ratio = [self.fuel_to_oxidizer_ratio] if self.fuel_to_oxidizer_ratio is not None else []
        self.fuel_to_oxidizer_ratio = [v if isinstance(v, float) else float(v) for v in self.fuel_to_oxidizer_ratio]

        if not isinstance(self.set_temperature, list):
            self.set_temperature = [self.set_temperature] if self.set_temperature is not None else []
        self.set_temperature = [v if isinstance(v, float) else float(v) for v in self.set_temperature]

        if not isinstance(self.post_treatment, list):
            self.post_treatment = [self.post_treatment] if self.post_treatment is not None else []
        self.post_treatment = [v if isinstance(v, str) else str(v) for v in self.post_treatment]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomicLayerDeposition(PreparationMethod):
    """
    Catalyst preparation by atomic layer deposition (ALD): sequential
    self-limiting surface reactions deposit a conformal thin film
    of active phase onto a substrate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["AtomicLayerDeposition"]
    class_class_curie: ClassVar[str] = "catcore:AtomicLayerDeposition"
    class_name: ClassVar[str] = "AtomicLayerDeposition"
    class_model_uri: ClassVar[URIRef] = CATCORE.AtomicLayerDeposition

    substrate: Optional[Union[str, list[str]]] = empty_list()
    pulse_time: Optional[Union[float, list[float]]] = empty_list()
    purging_duration: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    deposition_temperature: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.substrate, list):
            self.substrate = [self.substrate] if self.substrate is not None else []
        self.substrate = [v if isinstance(v, str) else str(v) for v in self.substrate]

        if not isinstance(self.pulse_time, list):
            self.pulse_time = [self.pulse_time] if self.pulse_time is not None else []
        self.pulse_time = [v if isinstance(v, float) else float(v) for v in self.pulse_time]

        if not isinstance(self.purging_duration, list):
            self.purging_duration = [self.purging_duration] if self.purging_duration is not None else []
        self.purging_duration = [v if isinstance(v, float) else float(v) for v in self.purging_duration]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.deposition_temperature, list):
            self.deposition_temperature = [self.deposition_temperature] if self.deposition_temperature is not None else []
        self.deposition_temperature = [v if isinstance(v, float) else float(v) for v in self.deposition_temperature]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DepositionPrecipitation(PreparationMethod):
    """
    Catalyst preparation by deposition-precipitation: the active phase
    is precipitated directly onto the support surface.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DepositionPrecipitation"]
    class_class_curie: ClassVar[str] = "catcore:DepositionPrecipitation"
    class_name: ClassVar[str] = "DepositionPrecipitation"
    class_model_uri: ClassVar[URIRef] = CATCORE.DepositionPrecipitation

    deposition_temperature: Optional[Union[float, list[float]]] = empty_list()
    deposition_time: Optional[Union[float, list[float]]] = empty_list()
    precipitating_agent: Optional[Union[str, list[str]]] = empty_list()
    precipitating_concentration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_ph: Optional[Union[float, list[float]]] = empty_list()
    mixing_rate: Optional[Union[float, list[float]]] = empty_list()
    mixing_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    order_of_addition: Optional[Union[str, list[str]]] = empty_list()
    filtration: Optional[Union[str, list[str]]] = empty_list()
    purification: Optional[Union[str, list[str]]] = empty_list()
    aging_temperature: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.deposition_temperature, list):
            self.deposition_temperature = [self.deposition_temperature] if self.deposition_temperature is not None else []
        self.deposition_temperature = [v if isinstance(v, float) else float(v) for v in self.deposition_temperature]

        if not isinstance(self.deposition_time, list):
            self.deposition_time = [self.deposition_time] if self.deposition_time is not None else []
        self.deposition_time = [v if isinstance(v, float) else float(v) for v in self.deposition_time]

        if not isinstance(self.precipitating_agent, list):
            self.precipitating_agent = [self.precipitating_agent] if self.precipitating_agent is not None else []
        self.precipitating_agent = [v if isinstance(v, str) else str(v) for v in self.precipitating_agent]

        if not isinstance(self.precipitating_concentration, list):
            self.precipitating_concentration = [self.precipitating_concentration] if self.precipitating_concentration is not None else []
        self.precipitating_concentration = [v if isinstance(v, float) else float(v) for v in self.precipitating_concentration]

        if not isinstance(self.synthesis_ph, list):
            self.synthesis_ph = [self.synthesis_ph] if self.synthesis_ph is not None else []
        self.synthesis_ph = [v if isinstance(v, float) else float(v) for v in self.synthesis_ph]

        if not isinstance(self.mixing_rate, list):
            self.mixing_rate = [self.mixing_rate] if self.mixing_rate is not None else []
        self.mixing_rate = [v if isinstance(v, float) else float(v) for v in self.mixing_rate]

        if not isinstance(self.mixing_time, list):
            self.mixing_time = [self.mixing_time] if self.mixing_time is not None else []
        self.mixing_time = [v if isinstance(v, float) else float(v) for v in self.mixing_time]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.order_of_addition, list):
            self.order_of_addition = [self.order_of_addition] if self.order_of_addition is not None else []
        self.order_of_addition = [v if isinstance(v, str) else str(v) for v in self.order_of_addition]

        if not isinstance(self.filtration, list):
            self.filtration = [self.filtration] if self.filtration is not None else []
        self.filtration = [v if isinstance(v, str) else str(v) for v in self.filtration]

        if not isinstance(self.purification, list):
            self.purification = [self.purification] if self.purification is not None else []
        self.purification = [v if isinstance(v, str) else str(v) for v in self.purification]

        if not isinstance(self.aging_temperature, list):
            self.aging_temperature = [self.aging_temperature] if self.aging_temperature is not None else []
        self.aging_temperature = [v if isinstance(v, float) else float(v) for v in self.aging_temperature]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrowaveAssisted(PreparationMethod):
    """
    Catalyst preparation using microwave irradiation to rapidly and
    uniformly heat the reaction mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MicrowaveAssisted"]
    class_class_curie: ClassVar[str] = "catcore:MicrowaveAssisted"
    class_name: ClassVar[str] = "MicrowaveAssisted"
    class_model_uri: ClassVar[URIRef] = CATCORE.MicrowaveAssisted

    power: Optional[Union[float, list[float]]] = empty_list()
    microwave_frequency: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.power, list):
            self.power = [self.power] if self.power is not None else []
        self.power = [v if isinstance(v, float) else float(v) for v in self.power]

        if not isinstance(self.microwave_frequency, list):
            self.microwave_frequency = [self.microwave_frequency] if self.microwave_frequency is not None else []
        self.microwave_frequency = [v if isinstance(v, float) else float(v) for v in self.microwave_frequency]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SonochemicalSynthesis(PreparationMethod):
    """
    Catalyst preparation using ultrasonic irradiation to drive chemical
    reactions via acoustic cavitation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SonochemicalSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:SonochemicalSynthesis"
    class_name: ClassVar[str] = "SonochemicalSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.SonochemicalSynthesis

    sonication_power: Optional[Union[float, list[float]]] = empty_list()
    sonication_duration: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.sonication_power, list):
            self.sonication_power = [self.sonication_power] if self.sonication_power is not None else []
        self.sonication_power = [v if isinstance(v, float) else float(v) for v in self.sonication_power]

        if not isinstance(self.sonication_duration, list):
            self.sonication_duration = [self.sonication_duration] if self.sonication_duration is not None else []
        self.sonication_duration = [v if isinstance(v, float) else float(v) for v in self.sonication_duration]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FlameSprayPyrolysis(PreparationMethod):
    """
    Catalyst preparation by flame spray pyrolysis (FSP): a liquid precursor
    solution is atomised and combusted in a flame to produce nanoparticles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007031"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007031"
    class_name: ClassVar[str] = "FlameSprayPyrolysis"
    class_model_uri: ClassVar[URIRef] = CATCORE.FlameSprayPyrolysis

    flame_type: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    inlet_system: Optional[Union[str, list[str]]] = empty_list()
    flame_ring: Optional[Union[str, list[str]]] = empty_list()
    dispersant: Optional[Union[str, list[str]]] = empty_list()
    capillary_pressure: Optional[Union[float, list[float]]] = empty_list()
    fuel_dispersant_ratio: Optional[Union[float, list[float]]] = empty_list()
    filtration_device: Optional[Union[str, list[str]]] = empty_list()
    filter_type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.flame_type, list):
            self.flame_type = [self.flame_type] if self.flame_type is not None else []
        self.flame_type = [v if isinstance(v, str) else str(v) for v in self.flame_type]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.inlet_system, list):
            self.inlet_system = [self.inlet_system] if self.inlet_system is not None else []
        self.inlet_system = [v if isinstance(v, str) else str(v) for v in self.inlet_system]

        if not isinstance(self.flame_ring, list):
            self.flame_ring = [self.flame_ring] if self.flame_ring is not None else []
        self.flame_ring = [v if isinstance(v, str) else str(v) for v in self.flame_ring]

        if not isinstance(self.dispersant, list):
            self.dispersant = [self.dispersant] if self.dispersant is not None else []
        self.dispersant = [v if isinstance(v, str) else str(v) for v in self.dispersant]

        if not isinstance(self.capillary_pressure, list):
            self.capillary_pressure = [self.capillary_pressure] if self.capillary_pressure is not None else []
        self.capillary_pressure = [v if isinstance(v, float) else float(v) for v in self.capillary_pressure]

        if not isinstance(self.fuel_dispersant_ratio, list):
            self.fuel_dispersant_ratio = [self.fuel_dispersant_ratio] if self.fuel_dispersant_ratio is not None else []
        self.fuel_dispersant_ratio = [v if isinstance(v, float) else float(v) for v in self.fuel_dispersant_ratio]

        if not isinstance(self.filtration_device, list):
            self.filtration_device = [self.filtration_device] if self.filtration_device is not None else []
        self.filtration_device = [v if isinstance(v, str) else str(v) for v in self.filtration_device]

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, str) else str(v) for v in self.filter_type]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanochemicalSynthesis(PreparationMethod):
    """
    Catalyst preparation by mechanical milling or grinding, optionally
    combined with thermal treatment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MechanochemicalSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:MechanochemicalSynthesis"
    class_name: ClassVar[str] = "MechanochemicalSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.MechanochemicalSynthesis

    vessel_volume: Optional[Union[float, list[float]]] = empty_list()
    size_and_material: Optional[Union[str, list[str]]] = empty_list()
    milling_speed: Optional[Union[float, list[float]]] = empty_list()
    milling_duration: Optional[Union[float, list[float]]] = empty_list()
    ball_material: Optional[Union[str, list[str]]] = empty_list()
    ball_size: Optional[Union[float, list[float]]] = empty_list()
    ball_to_powder_ratio: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vessel_volume, list):
            self.vessel_volume = [self.vessel_volume] if self.vessel_volume is not None else []
        self.vessel_volume = [v if isinstance(v, float) else float(v) for v in self.vessel_volume]

        if not isinstance(self.size_and_material, list):
            self.size_and_material = [self.size_and_material] if self.size_and_material is not None else []
        self.size_and_material = [v if isinstance(v, str) else str(v) for v in self.size_and_material]

        if not isinstance(self.milling_speed, list):
            self.milling_speed = [self.milling_speed] if self.milling_speed is not None else []
        self.milling_speed = [v if isinstance(v, float) else float(v) for v in self.milling_speed]

        if not isinstance(self.milling_duration, list):
            self.milling_duration = [self.milling_duration] if self.milling_duration is not None else []
        self.milling_duration = [v if isinstance(v, float) else float(v) for v in self.milling_duration]

        if not isinstance(self.ball_material, list):
            self.ball_material = [self.ball_material] if self.ball_material is not None else []
        self.ball_material = [v if isinstance(v, str) else str(v) for v in self.ball_material]

        if not isinstance(self.ball_size, list):
            self.ball_size = [self.ball_size] if self.ball_size is not None else []
        self.ball_size = [v if isinstance(v, float) else float(v) for v in self.ball_size]

        if not isinstance(self.ball_to_powder_ratio, list):
            self.ball_to_powder_ratio = [self.ball_to_powder_ratio] if self.ball_to_powder_ratio is not None else []
        self.ball_to_powder_ratio = [v if isinstance(v, float) else float(v) for v in self.ball_to_powder_ratio]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sublimation(PreparationMethod):
    """
    Catalyst preparation by sublimation: a solid precursor is vaporised
    and deposited onto a substrate without passing through a liquid phase.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Sublimation"]
    class_class_curie: ClassVar[str] = "catcore:Sublimation"
    class_name: ClassVar[str] = "Sublimation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Sublimation

    synthesis_pressure: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.synthesis_pressure, list):
            self.synthesis_pressure = [self.synthesis_pressure] if self.synthesis_pressure is not None else []
        self.synthesis_pressure = [v if isinstance(v, float) else float(v) for v in self.synthesis_pressure]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSynthesis(PreparationMethod):
    """
    Catalyst preparation by molecular (organometallic or coordination)
    chemistry routes, including crystallisation and purification steps.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MolecularSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:MolecularSynthesis"
    class_name: ClassVar[str] = "MolecularSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolecularSynthesis

    reaction_vessel: Optional[Union[str, list[str]]] = empty_list()
    mixing_device: Optional[Union[str, list[str]]] = empty_list()
    stirring_duration: Optional[Union[float, list[float]]] = empty_list()
    stirring_speed: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    filtration_device: Optional[Union[str, list[str]]] = empty_list()
    filter_type: Optional[Union[str, list[str]]] = empty_list()
    crystallisation_solvents: Optional[Union[str, list[str]]] = empty_list()
    precipitation_agent: Optional[Union[str, list[str]]] = empty_list()
    crystallisation_duration: Optional[Union[float, list[float]]] = empty_list()
    purification_solvent: Optional[Union[str, list[str]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    temperature_ramp: Optional[Union[float, list[float]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.reaction_vessel, list):
            self.reaction_vessel = [self.reaction_vessel] if self.reaction_vessel is not None else []
        self.reaction_vessel = [v if isinstance(v, str) else str(v) for v in self.reaction_vessel]

        if not isinstance(self.mixing_device, list):
            self.mixing_device = [self.mixing_device] if self.mixing_device is not None else []
        self.mixing_device = [v if isinstance(v, str) else str(v) for v in self.mixing_device]

        if not isinstance(self.stirring_duration, list):
            self.stirring_duration = [self.stirring_duration] if self.stirring_duration is not None else []
        self.stirring_duration = [v if isinstance(v, float) else float(v) for v in self.stirring_duration]

        if not isinstance(self.stirring_speed, list):
            self.stirring_speed = [self.stirring_speed] if self.stirring_speed is not None else []
        self.stirring_speed = [v if isinstance(v, float) else float(v) for v in self.stirring_speed]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.filtration_device, list):
            self.filtration_device = [self.filtration_device] if self.filtration_device is not None else []
        self.filtration_device = [v if isinstance(v, str) else str(v) for v in self.filtration_device]

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, str) else str(v) for v in self.filter_type]

        if not isinstance(self.crystallisation_solvents, list):
            self.crystallisation_solvents = [self.crystallisation_solvents] if self.crystallisation_solvents is not None else []
        self.crystallisation_solvents = [v if isinstance(v, str) else str(v) for v in self.crystallisation_solvents]

        if not isinstance(self.precipitation_agent, list):
            self.precipitation_agent = [self.precipitation_agent] if self.precipitation_agent is not None else []
        self.precipitation_agent = [v if isinstance(v, str) else str(v) for v in self.precipitation_agent]

        if not isinstance(self.crystallisation_duration, list):
            self.crystallisation_duration = [self.crystallisation_duration] if self.crystallisation_duration is not None else []
        self.crystallisation_duration = [v if isinstance(v, float) else float(v) for v in self.crystallisation_duration]

        if not isinstance(self.purification_solvent, list):
            self.purification_solvent = [self.purification_solvent] if self.purification_solvent is not None else []
        self.purification_solvent = [v if isinstance(v, str) else str(v) for v in self.purification_solvent]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.temperature_ramp, list):
            self.temperature_ramp = [self.temperature_ramp] if self.temperature_ramp is not None else []
        self.temperature_ramp = [v if isinstance(v, float) else float(v) for v in self.temperature_ramp]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExsolutionSynthesis(PreparationMethod):
    """
    Catalyst preparation by exsolution: metal nanoparticles are grown on
    a perovskite oxide surface by reduction/oxidation cycling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ExsolutionSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:ExsolutionSynthesis"
    class_name: ClassVar[str] = "ExsolutionSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.ExsolutionSynthesis

    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


class CharacterizationTechnique(Plan):
    """
    An abstract Plan describing the analytical protocol used to characterize
    a catalyst. Concrete subclasses specify technique-specific parameters.
    Linked from Characterization via realized_plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "CharacterizationTechnique"
    class_model_uri: ClassVar[URIRef] = CATCORE.CharacterizationTechnique


@dataclass(repr=False)
class PowderXRD(CharacterizationTechnique):
    """
    Powder X-ray diffraction for phase identification and structural analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000158"]
    class_class_curie: ClassVar[str] = "CHMO:0000158"
    class_name: ClassVar[str] = "PowderXRD"
    class_model_uri: ClassVar[URIRef] = CATCORE.PowderXRD

    minimum_2theta: Optional[Union[float, list[float]]] = empty_list()
    maximum_2theta: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    sample_spinning_speed: Optional[Union[float, list[float]]] = empty_list()
    experiment_duration: Optional[Union[float, list[float]]] = empty_list()
    xray_source: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.minimum_2theta, list):
            self.minimum_2theta = [self.minimum_2theta] if self.minimum_2theta is not None else []
        self.minimum_2theta = [v if isinstance(v, float) else float(v) for v in self.minimum_2theta]

        if not isinstance(self.maximum_2theta, list):
            self.maximum_2theta = [self.maximum_2theta] if self.maximum_2theta is not None else []
        self.maximum_2theta = [v if isinstance(v, float) else float(v) for v in self.maximum_2theta]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.sample_spinning_speed, list):
            self.sample_spinning_speed = [self.sample_spinning_speed] if self.sample_spinning_speed is not None else []
        self.sample_spinning_speed = [v if isinstance(v, float) else float(v) for v in self.sample_spinning_speed]

        if not isinstance(self.experiment_duration, list):
            self.experiment_duration = [self.experiment_duration] if self.experiment_duration is not None else []
        self.experiment_duration = [v if isinstance(v, float) else float(v) for v in self.experiment_duration]

        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleCrystalXRD(CharacterizationTechnique):
    """
    Single crystal X-ray diffraction for structure determination.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000852"]
    class_class_curie: ClassVar[str] = "CHMO:0000852"
    class_name: ClassVar[str] = "SingleCrystalXRD"
    class_model_uri: ClassVar[URIRef] = CATCORE.SingleCrystalXRD

    temperature: Optional[Union[float, list[float]]] = empty_list()
    xray_source: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayAbsorptionSpectroscopy(CharacterizationTechnique):
    """
    X-ray absorption spectroscopy (XAS/XANES/EXAFS) for electronic and local structure analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000286"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000286"
    class_name: ClassVar[str] = "XRayAbsorptionSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.XRayAbsorptionSpectroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    element_analyzed: Optional[Union[str, list[str]]] = empty_list()
    absorption_edge: Optional[Union[str, list[str]]] = empty_list()
    energy_resolution: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    beamline_source: Optional[Union[str, list[str]]] = empty_list()
    noise_of_measurement: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    xray_source: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()
    minimum_energy: Optional[Union[float, list[float]]] = empty_list()
    maximum_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.element_analyzed, list):
            self.element_analyzed = [self.element_analyzed] if self.element_analyzed is not None else []
        self.element_analyzed = [v if isinstance(v, str) else str(v) for v in self.element_analyzed]

        if not isinstance(self.absorption_edge, list):
            self.absorption_edge = [self.absorption_edge] if self.absorption_edge is not None else []
        self.absorption_edge = [v if isinstance(v, str) else str(v) for v in self.absorption_edge]

        if not isinstance(self.energy_resolution, list):
            self.energy_resolution = [self.energy_resolution] if self.energy_resolution is not None else []
        self.energy_resolution = [v if isinstance(v, float) else float(v) for v in self.energy_resolution]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.beamline_source, list):
            self.beamline_source = [self.beamline_source] if self.beamline_source is not None else []
        self.beamline_source = [v if isinstance(v, str) else str(v) for v in self.beamline_source]

        if not isinstance(self.noise_of_measurement, list):
            self.noise_of_measurement = [self.noise_of_measurement] if self.noise_of_measurement is not None else []
        self.noise_of_measurement = [v if isinstance(v, float) else float(v) for v in self.noise_of_measurement]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        if not isinstance(self.minimum_energy, list):
            self.minimum_energy = [self.minimum_energy] if self.minimum_energy is not None else []
        self.minimum_energy = [v if isinstance(v, float) else float(v) for v in self.minimum_energy]

        if not isinstance(self.maximum_energy, list):
            self.maximum_energy = [self.maximum_energy] if self.maximum_energy is not None else []
        self.maximum_energy = [v if isinstance(v, float) else float(v) for v in self.maximum_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XPS(CharacterizationTechnique):
    """
    X-ray photoelectron spectroscopy for surface elemental and chemical state analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000404"]
    class_class_curie: ClassVar[str] = "CHMO:0000404"
    class_name: ClassVar[str] = "XPS"
    class_model_uri: ClassVar[URIRef] = CATCORE.XPS

    total_acquisition_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    pass_energy: Optional[Union[float, list[float]]] = empty_list()
    spot_size: Optional[Union[float, list[float]]] = empty_list()
    lense_mode: Optional[Union[str, list[str]]] = empty_list()
    charge_compensation: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    xray_source: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()
    minimum_energy: Optional[Union[float, list[float]]] = empty_list()
    maximum_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.total_acquisition_time, list):
            self.total_acquisition_time = [self.total_acquisition_time] if self.total_acquisition_time is not None else []
        self.total_acquisition_time = [v if isinstance(v, float) else float(v) for v in self.total_acquisition_time]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.pass_energy, list):
            self.pass_energy = [self.pass_energy] if self.pass_energy is not None else []
        self.pass_energy = [v if isinstance(v, float) else float(v) for v in self.pass_energy]

        if not isinstance(self.spot_size, list):
            self.spot_size = [self.spot_size] if self.spot_size is not None else []
        self.spot_size = [v if isinstance(v, float) else float(v) for v in self.spot_size]

        if not isinstance(self.lense_mode, list):
            self.lense_mode = [self.lense_mode] if self.lense_mode is not None else []
        self.lense_mode = [v if isinstance(v, str) else str(v) for v in self.lense_mode]

        if not isinstance(self.charge_compensation, list):
            self.charge_compensation = [self.charge_compensation] if self.charge_compensation is not None else []
        self.charge_compensation = [v if isinstance(v, str) else str(v) for v in self.charge_compensation]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        if not isinstance(self.minimum_energy, list):
            self.minimum_energy = [self.minimum_energy] if self.minimum_energy is not None else []
        self.minimum_energy = [v if isinstance(v, float) else float(v) for v in self.minimum_energy]

        if not isinstance(self.maximum_energy, list):
            self.maximum_energy = [self.maximum_energy] if self.maximum_energy is not None else []
        self.maximum_energy = [v if isinstance(v, float) else float(v) for v in self.maximum_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EDX(CharacterizationTechnique):
    """
    Energy-dispersive X-ray spectroscopy for elemental mapping and quantification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000309"]
    class_class_curie: ClassVar[str] = "CHMO:0000309"
    class_name: ClassVar[str] = "EDX"
    class_model_uri: ClassVar[URIRef] = CATCORE.EDX

    primary_energy: Optional[Union[float, list[float]]] = empty_list()
    counting_time: Optional[Union[float, list[float]]] = empty_list()
    resolution: Optional[Union[float, list[float]]] = empty_list()
    calibration_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.primary_energy, list):
            self.primary_energy = [self.primary_energy] if self.primary_energy is not None else []
        self.primary_energy = [v if isinstance(v, float) else float(v) for v in self.primary_energy]

        if not isinstance(self.counting_time, list):
            self.counting_time = [self.counting_time] if self.counting_time is not None else []
        self.counting_time = [v if isinstance(v, float) else float(v) for v in self.counting_time]

        if not isinstance(self.resolution, list):
            self.resolution = [self.resolution] if self.resolution is not None else []
        self.resolution = [v if isinstance(v, float) else float(v) for v in self.resolution]

        if not isinstance(self.calibration_method, list):
            self.calibration_method = [self.calibration_method] if self.calibration_method is not None else []
        self.calibration_method = [v if isinstance(v, str) else str(v) for v in self.calibration_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfraredSpectroscopy(CharacterizationTechnique):
    """
    Infrared spectroscopy (FTIR/ATR) for functional group and surface species identification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["InfraredSpectroscopy"]
    class_class_curie: ClassVar[str] = "catcore:InfraredSpectroscopy"
    class_name: ClassVar[str] = "InfraredSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.InfraredSpectroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    minimum_wavenumber: Optional[Union[float, list[float]]] = empty_list()
    maximum_wavenumber: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    background_correction: Optional[Union[str, list[str]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.minimum_wavenumber, list):
            self.minimum_wavenumber = [self.minimum_wavenumber] if self.minimum_wavenumber is not None else []
        self.minimum_wavenumber = [v if isinstance(v, float) else float(v) for v in self.minimum_wavenumber]

        if not isinstance(self.maximum_wavenumber, list):
            self.maximum_wavenumber = [self.maximum_wavenumber] if self.maximum_wavenumber is not None else []
        self.maximum_wavenumber = [v if isinstance(v, float) else float(v) for v in self.maximum_wavenumber]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.background_correction, list):
            self.background_correction = [self.background_correction] if self.background_correction is not None else []
        self.background_correction = [v if isinstance(v, str) else str(v) for v in self.background_correction]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DRIFTS(CharacterizationTechnique):
    """
    Diffuse reflectance infrared Fourier transform spectroscopy for in-situ
    surface species identification under reactive gas conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000645"]
    class_class_curie: ClassVar[str] = "CHMO:0000645"
    class_name: ClassVar[str] = "DRIFTS"
    class_model_uri: ClassVar[URIRef] = CATCORE.DRIFTS

    adsorption_gas: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    diluting_reference: Optional[Union[str, list[str]]] = empty_list()
    ratio_reference_sample: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    resolution: Optional[Union[float, list[float]]] = empty_list()
    background_correction_method: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.adsorption_gas, list):
            self.adsorption_gas = [self.adsorption_gas] if self.adsorption_gas is not None else []
        self.adsorption_gas = [v if isinstance(v, str) else str(v) for v in self.adsorption_gas]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.diluting_reference, list):
            self.diluting_reference = [self.diluting_reference] if self.diluting_reference is not None else []
        self.diluting_reference = [v if isinstance(v, str) else str(v) for v in self.diluting_reference]

        if not isinstance(self.ratio_reference_sample, list):
            self.ratio_reference_sample = [self.ratio_reference_sample] if self.ratio_reference_sample is not None else []
        self.ratio_reference_sample = [v if isinstance(v, float) else float(v) for v in self.ratio_reference_sample]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.resolution, list):
            self.resolution = [self.resolution] if self.resolution is not None else []
        self.resolution = [v if isinstance(v, float) else float(v) for v in self.resolution]

        if not isinstance(self.background_correction_method, list):
            self.background_correction_method = [self.background_correction_method] if self.background_correction_method is not None else []
        self.background_correction_method = [v if isinstance(v, str) else str(v) for v in self.background_correction_method]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RamanSpectroscopy(CharacterizationTechnique):
    """
    Raman spectroscopy for vibrational and structural characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000069"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000069"
    class_name: ClassVar[str] = "RamanSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.RamanSpectroscopy

    excitation_laser_wavelength: Optional[Union[float, list[float]]] = empty_list()
    excitation_laser_power: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()
    integration_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    filter_or_grating: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.excitation_laser_wavelength, list):
            self.excitation_laser_wavelength = [self.excitation_laser_wavelength] if self.excitation_laser_wavelength is not None else []
        self.excitation_laser_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_laser_wavelength]

        if not isinstance(self.excitation_laser_power, list):
            self.excitation_laser_power = [self.excitation_laser_power] if self.excitation_laser_power is not None else []
        self.excitation_laser_power = [v if isinstance(v, float) else float(v) for v in self.excitation_laser_power]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        if not isinstance(self.integration_time, list):
            self.integration_time = [self.integration_time] if self.integration_time is not None else []
        self.integration_time = [v if isinstance(v, float) else float(v) for v in self.integration_time]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.filter_or_grating, list):
            self.filter_or_grating = [self.filter_or_grating] if self.filter_or_grating is not None else []
        self.filter_or_grating = [v if isinstance(v, str) else str(v) for v in self.filter_or_grating]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectroscopy(CharacterizationTechnique):
    """
    Nuclear magnetic resonance spectroscopy for structure elucidation.
    Note: for detailed liquid-state NMR minimum information, the dedicated
    nmr_dcat_ap profile (MARGARITAS) should be used in combination with
    this subprofile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000073"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000073"
    class_name: ClassVar[str] = "NMRSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.NMRSpectroscopy

    nucleus: Optional[Union[str, list[str]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    irradiation_frequency: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    nmr_pulse_sequence: Optional[Union[str, list[str]]] = empty_list()
    nmr_sample_tube: Optional[Union[str, list[str]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.nucleus, list):
            self.nucleus = [self.nucleus] if self.nucleus is not None else []
        self.nucleus = [v if isinstance(v, str) else str(v) for v in self.nucleus]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.irradiation_frequency, list):
            self.irradiation_frequency = [self.irradiation_frequency] if self.irradiation_frequency is not None else []
        self.irradiation_frequency = [v if isinstance(v, float) else float(v) for v in self.irradiation_frequency]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.nmr_pulse_sequence, list):
            self.nmr_pulse_sequence = [self.nmr_pulse_sequence] if self.nmr_pulse_sequence is not None else []
        self.nmr_pulse_sequence = [v if isinstance(v, str) else str(v) for v in self.nmr_pulse_sequence]

        if not isinstance(self.nmr_sample_tube, list):
            self.nmr_sample_tube = [self.nmr_sample_tube] if self.nmr_sample_tube is not None else []
        self.nmr_sample_tube = [v if isinstance(v, str) else str(v) for v in self.nmr_sample_tube]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TransmissionElectronMicroscopy(CharacterizationTechnique):
    """
    TEM for atomic-resolution imaging and diffraction of catalyst particles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000078"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000078"
    class_name: ClassVar[str] = "TransmissionElectronMicroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.TransmissionElectronMicroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    gun_type: Optional[Union[str, list[str]]] = empty_list()
    acceleration_voltage: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.gun_type, list):
            self.gun_type = [self.gun_type] if self.gun_type is not None else []
        self.gun_type = [v if isinstance(v, str) else str(v) for v in self.gun_type]

        if not isinstance(self.acceleration_voltage, list):
            self.acceleration_voltage = [self.acceleration_voltage] if self.acceleration_voltage is not None else []
        self.acceleration_voltage = [v if isinstance(v, float) else float(v) for v in self.acceleration_voltage]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScanningElectronMicroscopy(CharacterizationTechnique):
    """
    SEM for surface morphology and particle size/shape imaging.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000075"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000075"
    class_name: ClassVar[str] = "ScanningElectronMicroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.ScanningElectronMicroscopy

    image_resolution: Optional[Union[float, list[float]]] = empty_list()
    field_emitter: Optional[Union[str, list[str]]] = empty_list()
    gun_type: Optional[Union[str, list[str]]] = empty_list()
    acceleration_voltage: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.image_resolution, list):
            self.image_resolution = [self.image_resolution] if self.image_resolution is not None else []
        self.image_resolution = [v if isinstance(v, float) else float(v) for v in self.image_resolution]

        if not isinstance(self.field_emitter, list):
            self.field_emitter = [self.field_emitter] if self.field_emitter is not None else []
        self.field_emitter = [v if isinstance(v, str) else str(v) for v in self.field_emitter]

        if not isinstance(self.gun_type, list):
            self.gun_type = [self.gun_type] if self.gun_type is not None else []
        self.gun_type = [v if isinstance(v, str) else str(v) for v in self.gun_type]

        if not isinstance(self.acceleration_voltage, list):
            self.acceleration_voltage = [self.acceleration_voltage] if self.acceleration_voltage is not None else []
        self.acceleration_voltage = [v if isinstance(v, float) else float(v) for v in self.acceleration_voltage]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Thermogravimetry(CharacterizationTechnique):
    """
    Thermogravimetric analysis (TGA/DTG) for mass loss, decomposition, and oxidation state characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000690"]
    class_class_curie: ClassVar[str] = "CHMO:0000690"
    class_name: ClassVar[str] = "Thermogravimetry"
    class_model_uri: ClassVar[URIRef] = CATCORE.Thermogravimetry

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    final_temperature: Optional[Union[float, list[float]]] = empty_list()
    sample_mass: Optional[Union[float, list[float]]] = empty_list()
    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.initial_temperature, list):
            self.initial_temperature = [self.initial_temperature] if self.initial_temperature is not None else []
        self.initial_temperature = [v if isinstance(v, float) else float(v) for v in self.initial_temperature]

        if not isinstance(self.final_temperature, list):
            self.final_temperature = [self.final_temperature] if self.final_temperature is not None else []
        self.final_temperature = [v if isinstance(v, float) else float(v) for v in self.final_temperature]

        if not isinstance(self.sample_mass, list):
            self.sample_mass = [self.sample_mass] if self.sample_mass is not None else []
        self.sample_mass = [v if isinstance(v, float) else float(v) for v in self.sample_mass]

        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TPR(CharacterizationTechnique):
    """
    Temperature-programmed reduction for reducibility and metal-support interaction characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002908"]
    class_class_curie: ClassVar[str] = "CHMO:0002908"
    class_name: ClassVar[str] = "TPR"
    class_model_uri: ClassVar[URIRef] = CATCORE.TPR

    reducing_gas_composition: Optional[Union[str, list[str]]] = empty_list()
    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.reducing_gas_composition, list):
            self.reducing_gas_composition = [self.reducing_gas_composition] if self.reducing_gas_composition is not None else []
        self.reducing_gas_composition = [v if isinstance(v, str) else str(v) for v in self.reducing_gas_composition]

        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TPO(CharacterizationTechnique):
    """
    Temperature-programmed oxidation for coke quantification and reoxidation characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002907"]
    class_class_curie: ClassVar[str] = "CHMO:0002907"
    class_name: ClassVar[str] = "TPO"
    class_model_uri: ClassVar[URIRef] = CATCORE.TPO

    oxidizing_gas_composition: Optional[Union[str, list[str]]] = empty_list()
    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.oxidizing_gas_composition, list):
            self.oxidizing_gas_composition = [self.oxidizing_gas_composition] if self.oxidizing_gas_composition is not None else []
        self.oxidizing_gas_composition = [v if isinstance(v, str) else str(v) for v in self.oxidizing_gas_composition]

        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BET(CharacterizationTechnique):
    """
    Brunauer-Emmett-Teller analysis for specific surface area and pore size distribution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["BET"]
    class_class_curie: ClassVar[str] = "catcore:BET"
    class_name: ClassVar[str] = "BET"
    class_model_uri: ClassVar[URIRef] = CATCORE.BET

    adsorbate_gas: Optional[Union[str, list[str]]] = empty_list()
    degassing_temperature: Optional[Union[float, list[float]]] = empty_list()
    measurement_temperature: Optional[Union[float, list[float]]] = empty_list()
    pore_size_distribution_method: Optional[Union[str, list[str]]] = empty_list()
    sample_mass: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.adsorbate_gas, list):
            self.adsorbate_gas = [self.adsorbate_gas] if self.adsorbate_gas is not None else []
        self.adsorbate_gas = [v if isinstance(v, str) else str(v) for v in self.adsorbate_gas]

        if not isinstance(self.degassing_temperature, list):
            self.degassing_temperature = [self.degassing_temperature] if self.degassing_temperature is not None else []
        self.degassing_temperature = [v if isinstance(v, float) else float(v) for v in self.degassing_temperature]

        if not isinstance(self.measurement_temperature, list):
            self.measurement_temperature = [self.measurement_temperature] if self.measurement_temperature is not None else []
        self.measurement_temperature = [v if isinstance(v, float) else float(v) for v in self.measurement_temperature]

        if not isinstance(self.pore_size_distribution_method, list):
            self.pore_size_distribution_method = [self.pore_size_distribution_method] if self.pore_size_distribution_method is not None else []
        self.pore_size_distribution_method = [v if isinstance(v, str) else str(v) for v in self.pore_size_distribution_method]

        if not isinstance(self.sample_mass, list):
            self.sample_mass = [self.sample_mass] if self.sample_mass is not None else []
        self.sample_mass = [v if isinstance(v, float) else float(v) for v in self.sample_mass]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICPAES(CharacterizationTechnique):
    """
    Inductively coupled plasma atomic emission spectroscopy for bulk elemental composition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000267"]
    class_class_curie: ClassVar[str] = "CHMO:0000267"
    class_name: ClassVar[str] = "ICPAES"
    class_model_uri: ClassVar[URIRef] = CATCORE.ICPAES

    element_analyzed: Optional[Union[str, list[str]]] = empty_list()
    calibration_method: Optional[Union[str, list[str]]] = empty_list()
    detection_limit: Optional[Union[float, list[float]]] = empty_list()
    matrix_effect_correction: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.element_analyzed, list):
            self.element_analyzed = [self.element_analyzed] if self.element_analyzed is not None else []
        self.element_analyzed = [v if isinstance(v, str) else str(v) for v in self.element_analyzed]

        if not isinstance(self.calibration_method, list):
            self.calibration_method = [self.calibration_method] if self.calibration_method is not None else []
        self.calibration_method = [v if isinstance(v, str) else str(v) for v in self.calibration_method]

        if not isinstance(self.detection_limit, list):
            self.detection_limit = [self.detection_limit] if self.detection_limit is not None else []
        self.detection_limit = [v if isinstance(v, float) else float(v) for v in self.detection_limit]

        if not isinstance(self.matrix_effect_correction, list):
            self.matrix_effect_correction = [self.matrix_effect_correction] if self.matrix_effect_correction is not None else []
        self.matrix_effect_correction = [v if isinstance(v, str) else str(v) for v in self.matrix_effect_correction]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementalAnalysis(CharacterizationTechnique):
    """
    Combustion elemental analysis (CHNS/O) for carbon, hydrogen, nitrogen, sulfur content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0001075"]
    class_class_curie: ClassVar[str] = "CHMO:0001075"
    class_name: ClassVar[str] = "ElementalAnalysis"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElementalAnalysis

    elements_analyzed: Optional[Union[str, list[str]]] = empty_list()
    combustion_temperature: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.elements_analyzed, list):
            self.elements_analyzed = [self.elements_analyzed] if self.elements_analyzed is not None else []
        self.elements_analyzed = [v if isinstance(v, str) else str(v) for v in self.elements_analyzed]

        if not isinstance(self.combustion_temperature, list):
            self.combustion_temperature = [self.combustion_temperature] if self.combustion_temperature is not None else []
        self.combustion_temperature = [v if isinstance(v, float) else float(v) for v in self.combustion_temperature]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UVVisSpectroscopy(CharacterizationTechnique):
    """
    UV-Vis spectroscopy for electronic transitions, band gap, and concentration determination.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000079"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000079"
    class_name: ClassVar[str] = "UVVisSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.UVVisSpectroscopy

    minimum_wavelength: Optional[Union[float, list[float]]] = empty_list()
    maximum_wavelength: Optional[Union[float, list[float]]] = empty_list()
    path_length: Optional[Union[float, list[float]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.minimum_wavelength, list):
            self.minimum_wavelength = [self.minimum_wavelength] if self.minimum_wavelength is not None else []
        self.minimum_wavelength = [v if isinstance(v, float) else float(v) for v in self.minimum_wavelength]

        if not isinstance(self.maximum_wavelength, list):
            self.maximum_wavelength = [self.maximum_wavelength] if self.maximum_wavelength is not None else []
        self.maximum_wavelength = [v if isinstance(v, float) else float(v) for v in self.maximum_wavelength]

        if not isinstance(self.path_length, list):
            self.path_length = [self.path_length] if self.path_length is not None else []
        self.path_length = [v if isinstance(v, float) else float(v) for v in self.path_length]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhotoluminescenceSpectroscopy(CharacterizationTechnique):
    """
    Photoluminescence spectroscopy for defect and charge carrier characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhotoluminescenceSpectroscopy"]
    class_class_curie: ClassVar[str] = "catcore:PhotoluminescenceSpectroscopy"
    class_name: ClassVar[str] = "PhotoluminescenceSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhotoluminescenceSpectroscopy

    emission_range: Optional[Union[str, list[str]]] = empty_list()
    slit_width: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    integration_time: Optional[Union[float, list[float]]] = empty_list()
    excitation_wavelength: Optional[Union[float, list[float]]] = empty_list()
    emission_wavelength: Optional[Union[float, list[float]]] = empty_list()
    optical_filter: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.emission_range, list):
            self.emission_range = [self.emission_range] if self.emission_range is not None else []
        self.emission_range = [v if isinstance(v, str) else str(v) for v in self.emission_range]

        if not isinstance(self.slit_width, list):
            self.slit_width = [self.slit_width] if self.slit_width is not None else []
        self.slit_width = [v if isinstance(v, float) else float(v) for v in self.slit_width]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.integration_time, list):
            self.integration_time = [self.integration_time] if self.integration_time is not None else []
        self.integration_time = [v if isinstance(v, float) else float(v) for v in self.integration_time]

        if not isinstance(self.excitation_wavelength, list):
            self.excitation_wavelength = [self.excitation_wavelength] if self.excitation_wavelength is not None else []
        self.excitation_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_wavelength]

        if not isinstance(self.emission_wavelength, list):
            self.emission_wavelength = [self.emission_wavelength] if self.emission_wavelength is not None else []
        self.emission_wavelength = [v if isinstance(v, float) else float(v) for v in self.emission_wavelength]

        if not isinstance(self.optical_filter, list):
            self.optical_filter = [self.optical_filter] if self.optical_filter is not None else []
        self.optical_filter = [v if isinstance(v, str) else str(v) for v in self.optical_filter]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhotoluminescenceLifetime(CharacterizationTechnique):
    """
    Time-resolved photoluminescence for charge carrier lifetime and recombination dynamics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhotoluminescenceLifetime"]
    class_class_curie: ClassVar[str] = "catcore:PhotoluminescenceLifetime"
    class_name: ClassVar[str] = "PhotoluminescenceLifetime"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhotoluminescenceLifetime

    lifetime_fitting_model: Optional[Union[str, list[str]]] = empty_list()
    number_of_shots: Optional[Union[int, list[int]]] = empty_list()
    excitation_wavelength: Optional[Union[float, list[float]]] = empty_list()
    emission_wavelength: Optional[Union[float, list[float]]] = empty_list()
    optical_filter: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.lifetime_fitting_model, list):
            self.lifetime_fitting_model = [self.lifetime_fitting_model] if self.lifetime_fitting_model is not None else []
        self.lifetime_fitting_model = [v if isinstance(v, str) else str(v) for v in self.lifetime_fitting_model]

        if not isinstance(self.number_of_shots, list):
            self.number_of_shots = [self.number_of_shots] if self.number_of_shots is not None else []
        self.number_of_shots = [v if isinstance(v, int) else int(v) for v in self.number_of_shots]

        if not isinstance(self.excitation_wavelength, list):
            self.excitation_wavelength = [self.excitation_wavelength] if self.excitation_wavelength is not None else []
        self.excitation_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_wavelength]

        if not isinstance(self.emission_wavelength, list):
            self.emission_wavelength = [self.emission_wavelength] if self.emission_wavelength is not None else []
        self.emission_wavelength = [v if isinstance(v, float) else float(v) for v in self.emission_wavelength]

        if not isinstance(self.optical_filter, list):
            self.optical_filter = [self.optical_filter] if self.optical_filter is not None else []
        self.optical_filter = [v if isinstance(v, str) else str(v) for v in self.optical_filter]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CyclicVoltammetry(CharacterizationTechnique):
    """
    Cyclic voltammetry for electrochemical activity, redox potential, and capacitance characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000025"]
    class_class_curie: ClassVar[str] = "CHMO:0000025"
    class_name: ClassVar[str] = "CyclicVoltammetry"
    class_model_uri: ClassVar[URIRef] = CATCORE.CyclicVoltammetry

    scan_rate: Optional[Union[float, list[float]]] = empty_list()
    minimum_potential: Optional[Union[float, list[float]]] = empty_list()
    maximum_potential: Optional[Union[float, list[float]]] = empty_list()
    step_size_potential: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    reference_electrode: Optional[Union[str, list[str]]] = empty_list()
    working_electrode: Optional[Union[str, list[str]]] = empty_list()
    counter_electrode: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_composition: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_concentration: Optional[Union[float, list[float]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.scan_rate, list):
            self.scan_rate = [self.scan_rate] if self.scan_rate is not None else []
        self.scan_rate = [v if isinstance(v, float) else float(v) for v in self.scan_rate]

        if not isinstance(self.minimum_potential, list):
            self.minimum_potential = [self.minimum_potential] if self.minimum_potential is not None else []
        self.minimum_potential = [v if isinstance(v, float) else float(v) for v in self.minimum_potential]

        if not isinstance(self.maximum_potential, list):
            self.maximum_potential = [self.maximum_potential] if self.maximum_potential is not None else []
        self.maximum_potential = [v if isinstance(v, float) else float(v) for v in self.maximum_potential]

        if not isinstance(self.step_size_potential, list):
            self.step_size_potential = [self.step_size_potential] if self.step_size_potential is not None else []
        self.step_size_potential = [v if isinstance(v, float) else float(v) for v in self.step_size_potential]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.reference_electrode, list):
            self.reference_electrode = [self.reference_electrode] if self.reference_electrode is not None else []
        self.reference_electrode = [v if isinstance(v, str) else str(v) for v in self.reference_electrode]

        if not isinstance(self.working_electrode, list):
            self.working_electrode = [self.working_electrode] if self.working_electrode is not None else []
        self.working_electrode = [v if isinstance(v, str) else str(v) for v in self.working_electrode]

        if not isinstance(self.counter_electrode, list):
            self.counter_electrode = [self.counter_electrode] if self.counter_electrode is not None else []
        self.counter_electrode = [v if isinstance(v, str) else str(v) for v in self.counter_electrode]

        if not isinstance(self.electrolyte_composition, list):
            self.electrolyte_composition = [self.electrolyte_composition] if self.electrolyte_composition is not None else []
        self.electrolyte_composition = [v if isinstance(v, str) else str(v) for v in self.electrolyte_composition]

        if not isinstance(self.electrolyte_concentration, list):
            self.electrolyte_concentration = [self.electrolyte_concentration] if self.electrolyte_concentration is not None else []
        self.electrolyte_concentration = [v if isinstance(v, float) else float(v) for v in self.electrolyte_concentration]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConductivityMeasurement(CharacterizationTechnique):
    """
    Electrical conductivity measurement for ionic and electronic transport characterization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ConductivityMeasurement"]
    class_class_curie: ClassVar[str] = "catcore:ConductivityMeasurement"
    class_name: ClassVar[str] = "ConductivityMeasurement"
    class_model_uri: ClassVar[URIRef] = CATCORE.ConductivityMeasurement

    electrode_configuration: Optional[Union[str, list[str]]] = empty_list()
    ac_frequency: Optional[Union[float, list[float]]] = empty_list()
    ac_dc_mode: Optional[Union[str, list[str]]] = empty_list()
    sample_geometry: Optional[Union[str, list[str]]] = empty_list()
    reference_electrode: Optional[Union[str, list[str]]] = empty_list()
    working_electrode: Optional[Union[str, list[str]]] = empty_list()
    counter_electrode: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_composition: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_concentration: Optional[Union[float, list[float]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.electrode_configuration, list):
            self.electrode_configuration = [self.electrode_configuration] if self.electrode_configuration is not None else []
        self.electrode_configuration = [v if isinstance(v, str) else str(v) for v in self.electrode_configuration]

        if not isinstance(self.ac_frequency, list):
            self.ac_frequency = [self.ac_frequency] if self.ac_frequency is not None else []
        self.ac_frequency = [v if isinstance(v, float) else float(v) for v in self.ac_frequency]

        if not isinstance(self.ac_dc_mode, list):
            self.ac_dc_mode = [self.ac_dc_mode] if self.ac_dc_mode is not None else []
        self.ac_dc_mode = [v if isinstance(v, str) else str(v) for v in self.ac_dc_mode]

        if not isinstance(self.sample_geometry, list):
            self.sample_geometry = [self.sample_geometry] if self.sample_geometry is not None else []
        self.sample_geometry = [v if isinstance(v, str) else str(v) for v in self.sample_geometry]

        if not isinstance(self.reference_electrode, list):
            self.reference_electrode = [self.reference_electrode] if self.reference_electrode is not None else []
        self.reference_electrode = [v if isinstance(v, str) else str(v) for v in self.reference_electrode]

        if not isinstance(self.working_electrode, list):
            self.working_electrode = [self.working_electrode] if self.working_electrode is not None else []
        self.working_electrode = [v if isinstance(v, str) else str(v) for v in self.working_electrode]

        if not isinstance(self.counter_electrode, list):
            self.counter_electrode = [self.counter_electrode] if self.counter_electrode is not None else []
        self.counter_electrode = [v if isinstance(v, str) else str(v) for v in self.counter_electrode]

        if not isinstance(self.electrolyte_composition, list):
            self.electrolyte_composition = [self.electrolyte_composition] if self.electrolyte_composition is not None else []
        self.electrolyte_composition = [v if isinstance(v, str) else str(v) for v in self.electrolyte_composition]

        if not isinstance(self.electrolyte_concentration, list):
            self.electrolyte_concentration = [self.electrolyte_concentration] if self.electrolyte_concentration is not None else []
        self.electrolyte_concentration = [v if isinstance(v, float) else float(v) for v in self.electrolyte_concentration]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DynamicLightScattering(CharacterizationTechnique):
    """
    Dynamic light scattering for hydrodynamic particle size distribution in suspension.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000167"]
    class_class_curie: ClassVar[str] = "CHMO:0000167"
    class_name: ClassVar[str] = "DynamicLightScattering"
    class_model_uri: ClassVar[URIRef] = CATCORE.DynamicLightScattering

    solvent: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()
    light_wavelength: Optional[Union[float, list[float]]] = empty_list()
    scattering_angle: Optional[Union[float, list[float]]] = empty_list()
    refractive_index: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    dispersant: Optional[Union[str, list[str]]] = empty_list()
    measurement_duration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        if not isinstance(self.light_wavelength, list):
            self.light_wavelength = [self.light_wavelength] if self.light_wavelength is not None else []
        self.light_wavelength = [v if isinstance(v, float) else float(v) for v in self.light_wavelength]

        if not isinstance(self.scattering_angle, list):
            self.scattering_angle = [self.scattering_angle] if self.scattering_angle is not None else []
        self.scattering_angle = [v if isinstance(v, float) else float(v) for v in self.scattering_angle]

        if not isinstance(self.refractive_index, list):
            self.refractive_index = [self.refractive_index] if self.refractive_index is not None else []
        self.refractive_index = [v if isinstance(v, float) else float(v) for v in self.refractive_index]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.dispersant, list):
            self.dispersant = [self.dispersant] if self.dispersant is not None else []
        self.dispersant = [v if isinstance(v, str) else str(v) for v in self.dispersant]

        if not isinstance(self.measurement_duration, list):
            self.measurement_duration = [self.measurement_duration] if self.measurement_duration is not None else []
        self.measurement_duration = [v if isinstance(v, float) else float(v) for v in self.measurement_duration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ESIMS(CharacterizationTechnique):
    """
    Electrospray ionisation mass spectrometry for molecular mass and identity determination.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000482"]
    class_class_curie: ClassVar[str] = "CHMO:0000482"
    class_name: ClassVar[str] = "ESI_MS"
    class_model_uri: ClassVar[URIRef] = CATCORE.ESIMS

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    spray_voltage: Optional[Union[float, list[float]]] = empty_list()
    capillary_temperature: Optional[Union[float, list[float]]] = empty_list()
    solvent_composition: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()
    mz_minimum: Optional[Union[float, list[float]]] = empty_list()
    mz_maximum: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.spray_voltage, list):
            self.spray_voltage = [self.spray_voltage] if self.spray_voltage is not None else []
        self.spray_voltage = [v if isinstance(v, float) else float(v) for v in self.spray_voltage]

        if not isinstance(self.capillary_temperature, list):
            self.capillary_temperature = [self.capillary_temperature] if self.capillary_temperature is not None else []
        self.capillary_temperature = [v if isinstance(v, float) else float(v) for v in self.capillary_temperature]

        if not isinstance(self.solvent_composition, list):
            self.solvent_composition = [self.solvent_composition] if self.solvent_composition is not None else []
        self.solvent_composition = [v if isinstance(v, str) else str(v) for v in self.solvent_composition]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        if not isinstance(self.mz_minimum, list):
            self.mz_minimum = [self.mz_minimum] if self.mz_minimum is not None else []
        self.mz_minimum = [v if isinstance(v, float) else float(v) for v in self.mz_minimum]

        if not isinstance(self.mz_maximum, list):
            self.mz_maximum = [self.mz_maximum] if self.mz_maximum is not None else []
        self.mz_maximum = [v if isinstance(v, float) else float(v) for v in self.mz_maximum]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GCMS(CharacterizationTechnique):
    """
    Gas chromatography-mass spectrometry for volatile compound identification and quantification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000497"]
    class_class_curie: ClassVar[str] = "CHMO:0000497"
    class_name: ClassVar[str] = "GCMS"
    class_model_uri: ClassVar[URIRef] = CATCORE.GCMS

    carrier_gas: Optional[Union[str, list[str]]] = empty_list()
    carrier_gas_purity: Optional[Union[str, list[str]]] = empty_list()
    inlet_temperature: Optional[Union[float, list[float]]] = empty_list()
    minimum_oven_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_oven_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_ramp: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()
    acquisition_mode: Optional[Union[str, list[str]]] = empty_list()
    solvent_delay: Optional[Union[float, list[float]]] = empty_list()
    trace_ion_detection: Optional[Union[str, list[str]]] = empty_list()
    split_ratio: Optional[Union[float, list[float]]] = empty_list()
    column_type: Optional[Union[str, list[str]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()
    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()
    mz_minimum: Optional[Union[float, list[float]]] = empty_list()
    mz_maximum: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        if not isinstance(self.carrier_gas_purity, list):
            self.carrier_gas_purity = [self.carrier_gas_purity] if self.carrier_gas_purity is not None else []
        self.carrier_gas_purity = [v if isinstance(v, str) else str(v) for v in self.carrier_gas_purity]

        if not isinstance(self.inlet_temperature, list):
            self.inlet_temperature = [self.inlet_temperature] if self.inlet_temperature is not None else []
        self.inlet_temperature = [v if isinstance(v, float) else float(v) for v in self.inlet_temperature]

        if not isinstance(self.minimum_oven_temperature, list):
            self.minimum_oven_temperature = [self.minimum_oven_temperature] if self.minimum_oven_temperature is not None else []
        self.minimum_oven_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_oven_temperature]

        if not isinstance(self.maximum_oven_temperature, list):
            self.maximum_oven_temperature = [self.maximum_oven_temperature] if self.maximum_oven_temperature is not None else []
        self.maximum_oven_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_oven_temperature]

        if not isinstance(self.heating_ramp, list):
            self.heating_ramp = [self.heating_ramp] if self.heating_ramp is not None else []
        self.heating_ramp = [v if isinstance(v, float) else float(v) for v in self.heating_ramp]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        if not isinstance(self.acquisition_mode, list):
            self.acquisition_mode = [self.acquisition_mode] if self.acquisition_mode is not None else []
        self.acquisition_mode = [v if isinstance(v, str) else str(v) for v in self.acquisition_mode]

        if not isinstance(self.solvent_delay, list):
            self.solvent_delay = [self.solvent_delay] if self.solvent_delay is not None else []
        self.solvent_delay = [v if isinstance(v, float) else float(v) for v in self.solvent_delay]

        if not isinstance(self.trace_ion_detection, list):
            self.trace_ion_detection = [self.trace_ion_detection] if self.trace_ion_detection is not None else []
        self.trace_ion_detection = [v if isinstance(v, str) else str(v) for v in self.trace_ion_detection]

        if not isinstance(self.split_ratio, list):
            self.split_ratio = [self.split_ratio] if self.split_ratio is not None else []
        self.split_ratio = [v if isinstance(v, float) else float(v) for v in self.split_ratio]

        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        if not isinstance(self.mz_minimum, list):
            self.mz_minimum = [self.mz_minimum] if self.mz_minimum is not None else []
        self.mz_minimum = [v if isinstance(v, float) else float(v) for v in self.mz_minimum]

        if not isinstance(self.mz_maximum, list):
            self.mz_maximum = [self.mz_maximum] if self.mz_maximum is not None else []
        self.mz_maximum = [v if isinstance(v, float) else float(v) for v in self.mz_maximum]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SizeExclusionChromatography(CharacterizationTechnique):
    """
    Size exclusion chromatography for molecular weight distribution determination.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFP["0000843"]
    class_class_curie: ClassVar[str] = "AFP:0000843"
    class_name: ClassVar[str] = "SizeExclusionChromatography"
    class_model_uri: ClassVar[URIRef] = CATCORE.SizeExclusionChromatography

    temperature: Optional[Union[float, list[float]]] = empty_list()
    calibration_standard: Optional[Union[str, list[str]]] = empty_list()
    column_type: Optional[Union[str, list[str]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()
    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.calibration_standard, list):
            self.calibration_standard = [self.calibration_standard] if self.calibration_standard is not None else []
        self.calibration_standard = [v if isinstance(v, str) else str(v) for v in self.calibration_standard]

        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HPLCMS(CharacterizationTechnique):
    """
    High-performance liquid chromatography-mass spectrometry for compound identification and quantification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000796"]
    class_class_curie: ClassVar[str] = "CHMO:0000796"
    class_name: ClassVar[str] = "HPLC_MS"
    class_model_uri: ClassVar[URIRef] = CATCORE.HPLCMS

    gradient_program: Optional[Union[str, list[str]]] = empty_list()
    ionization_mode: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    column_type: Optional[Union[str, list[str]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()
    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gradient_program, list):
            self.gradient_program = [self.gradient_program] if self.gradient_program is not None else []
        self.gradient_program = [v if isinstance(v, str) else str(v) for v in self.gradient_program]

        if not isinstance(self.ionization_mode, list):
            self.ionization_mode = [self.ionization_mode] if self.ionization_mode is not None else []
        self.ionization_mode = [v if isinstance(v, str) else str(v) for v in self.ionization_mode]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        super().__post_init__(**kwargs)


class ProductIdentificationMethod(Plan):
    """
    Abstract Plan representing the method used to identify and quantify reaction
    products. In practice, users should reference a concrete CharacterizationTechnique
    subclass from catcore_characterization_ap (e.g. GCMS, HPLC_MS, NMRSpectroscopy).

    This abstract class is retained for backward compatibility with the original
    CatCore monolith. It is a subclass of Plan (prov:Plan / OBI:0000272) so that
    it can participate in the realized_plan slot if needed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "ProductIdentificationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.ProductIdentificationMethod


class SimulationMethod(Plan):
    """
    Abstract Plan describing the computational method (protocol) used in a
    Simulation. Concrete subclasses carry method-specific parameter slots.
    Linked from Simulation via realized_plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "SimulationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.SimulationMethod


@dataclass(repr=False)
class DFT(SimulationMethod):
    """
    Density functional theory — a quantum mechanical method for calculating
    the electronic structure of atoms, molecules, and periodic solids.
    The most widely used ab initio method in computational catalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DFT"]
    class_class_curie: ClassVar[str] = "catcore:DFT"
    class_name: ClassVar[str] = "DFT"
    class_model_uri: ClassVar[URIRef] = CATCORE.DFT

    exchange_correlation_functional: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    dft_u_parameters: Optional[Union[str, list[str]]] = empty_list()
    spin_polarization: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    total_energy_per_atom: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.exchange_correlation_functional, list):
            self.exchange_correlation_functional = [self.exchange_correlation_functional] if self.exchange_correlation_functional is not None else []
        self.exchange_correlation_functional = [v if isinstance(v, str) else str(v) for v in self.exchange_correlation_functional]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.dft_u_parameters, list):
            self.dft_u_parameters = [self.dft_u_parameters] if self.dft_u_parameters is not None else []
        self.dft_u_parameters = [v if isinstance(v, str) else str(v) for v in self.dft_u_parameters]

        if not isinstance(self.spin_polarization, list):
            self.spin_polarization = [self.spin_polarization] if self.spin_polarization is not None else []
        self.spin_polarization = [v if isinstance(v, Bool) else Bool(v) for v in self.spin_polarization]

        if not isinstance(self.total_energy_per_atom, list):
            self.total_energy_per_atom = [self.total_energy_per_atom] if self.total_energy_per_atom is not None else []
        self.total_energy_per_atom = [v if isinstance(v, float) else float(v) for v in self.total_energy_per_atom]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularDynamics(SimulationMethod):
    """
    Molecular dynamics simulation — a method for computing the time evolution
    of a system of interacting particles by integrating the equations of motion.
    Used to study diffusion, reaction kinetics, and thermal properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C18097"]
    class_class_curie: ClassVar[str] = "NCIT:C18097"
    class_name: ClassVar[str] = "MolecularDynamics"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolecularDynamics

    force_field: Optional[Union[str, list[str]]] = empty_list()
    simulation_timestep: Optional[Union[float, list[float]]] = empty_list()
    simulation_time: Optional[Union[float, list[float]]] = empty_list()
    ensemble_type: Optional[Union[str, list[str]]] = empty_list()
    number_of_atoms: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.force_field, list):
            self.force_field = [self.force_field] if self.force_field is not None else []
        self.force_field = [v if isinstance(v, str) else str(v) for v in self.force_field]

        if not isinstance(self.simulation_timestep, list):
            self.simulation_timestep = [self.simulation_timestep] if self.simulation_timestep is not None else []
        self.simulation_timestep = [v if isinstance(v, float) else float(v) for v in self.simulation_timestep]

        if not isinstance(self.simulation_time, list):
            self.simulation_time = [self.simulation_time] if self.simulation_time is not None else []
        self.simulation_time = [v if isinstance(v, float) else float(v) for v in self.simulation_time]

        if not isinstance(self.ensemble_type, list):
            self.ensemble_type = [self.ensemble_type] if self.ensemble_type is not None else []
        self.ensemble_type = [v if isinstance(v, str) else str(v) for v in self.ensemble_type]

        if not isinstance(self.number_of_atoms, list):
            self.number_of_atoms = [self.number_of_atoms] if self.number_of_atoms is not None else []
        self.number_of_atoms = [v if isinstance(v, int) else int(v) for v in self.number_of_atoms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Microkinetics(SimulationMethod):
    """
    Microkinetic modelling — a mean-field kinetic approach that integrates
    elementary reaction steps and their rate constants to predict catalytic
    activity and selectivity under reaction conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Microkinetics"]
    class_class_curie: ClassVar[str] = "catcore:Microkinetics"
    class_name: ClassVar[str] = "Microkinetics"
    class_model_uri: ClassVar[URIRef] = CATCORE.Microkinetics

    rate_constants: Optional[Union[str, list[str]]] = empty_list()
    solver_type: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    pressure: Optional[Union[float, list[float]]] = empty_list()
    surface_coverage: Optional[Union[float, list[float]]] = empty_list()
    activation_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.rate_constants, list):
            self.rate_constants = [self.rate_constants] if self.rate_constants is not None else []
        self.rate_constants = [v if isinstance(v, str) else str(v) for v in self.rate_constants]

        if not isinstance(self.solver_type, list):
            self.solver_type = [self.solver_type] if self.solver_type is not None else []
        self.solver_type = [v if isinstance(v, str) else str(v) for v in self.solver_type]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.pressure, list):
            self.pressure = [self.pressure] if self.pressure is not None else []
        self.pressure = [v if isinstance(v, float) else float(v) for v in self.pressure]

        if not isinstance(self.surface_coverage, list):
            self.surface_coverage = [self.surface_coverage] if self.surface_coverage is not None else []
        self.surface_coverage = [v if isinstance(v, float) else float(v) for v in self.surface_coverage]

        if not isinstance(self.activation_energy, list):
            self.activation_energy = [self.activation_energy] if self.activation_energy is not None else []
        self.activation_energy = [v if isinstance(v, float) else float(v) for v in self.activation_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonteCarlo(SimulationMethod):
    """
    Monte Carlo simulation — a stochastic method that samples configuration
    space using random moves accepted or rejected according to a statistical
    criterion (e.g. Metropolis). Used for adsorption isotherms, phase diagrams,
    and lattice-based kinetics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MonteCarlo"]
    class_class_curie: ClassVar[str] = "catcore:MonteCarlo"
    class_name: ClassVar[str] = "MonteCarlo"
    class_model_uri: ClassVar[URIRef] = CATCORE.MonteCarlo

    interaction_potential: Optional[Union[str, list[str]]] = empty_list()
    number_of_steps: Optional[Union[int, list[int]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    lattice_size_type: Optional[Union[str, list[str]]] = empty_list()
    acceptance_criteria: Optional[Union[str, list[str]]] = empty_list()
    equilibration_steps: Optional[Union[int, list[int]]] = empty_list()
    sampling_interval: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.interaction_potential, list):
            self.interaction_potential = [self.interaction_potential] if self.interaction_potential is not None else []
        self.interaction_potential = [v if isinstance(v, str) else str(v) for v in self.interaction_potential]

        if not isinstance(self.number_of_steps, list):
            self.number_of_steps = [self.number_of_steps] if self.number_of_steps is not None else []
        self.number_of_steps = [v if isinstance(v, int) else int(v) for v in self.number_of_steps]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.lattice_size_type, list):
            self.lattice_size_type = [self.lattice_size_type] if self.lattice_size_type is not None else []
        self.lattice_size_type = [v if isinstance(v, str) else str(v) for v in self.lattice_size_type]

        if not isinstance(self.acceptance_criteria, list):
            self.acceptance_criteria = [self.acceptance_criteria] if self.acceptance_criteria is not None else []
        self.acceptance_criteria = [v if isinstance(v, str) else str(v) for v in self.acceptance_criteria]

        if not isinstance(self.equilibration_steps, list):
            self.equilibration_steps = [self.equilibration_steps] if self.equilibration_steps is not None else []
        self.equilibration_steps = [v if isinstance(v, int) else int(v) for v in self.equilibration_steps]

        if not isinstance(self.sampling_interval, list):
            self.sampling_interval = [self.sampling_interval] if self.sampling_interval is not None else []
        self.sampling_interval = [v if isinstance(v, int) else int(v) for v in self.sampling_interval]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualitativeAttribute(YAMLRoot):
    """
    A piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "QualitativeAttribute"
    class_model_uri: ClassVar[URIRef] = CATCORE.QualitativeAttribute

    value: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalculatedProperty(QualitativeAttribute):
    """
    Abstract QualitativeAttribute representing a property computed by a
    Simulation. Concrete subclasses carry the property-specific output
    values and the computational settings used to produce them.
    Linked from Simulation via the calculated_property slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CalculatedProperty"]
    class_class_curie: ClassVar[str] = "catcore:CalculatedProperty"
    class_name: ClassVar[str] = "CalculatedProperty"
    class_model_uri: ClassVar[URIRef] = CATCORE.CalculatedProperty

    value: str = None

@dataclass(repr=False)
class ThermodynamicStability(CalculatedProperty):
    """
    Thermodynamic stability of a material or phase, characterised by formation
    energy, convex hull distance, and competing phases. Used to screen catalyst
    stability and predict synthesis feasibility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ThermodynamicStability"]
    class_class_curie: ClassVar[str] = "catcore:ThermodynamicStability"
    class_name: ClassVar[str] = "ThermodynamicStability"
    class_model_uri: ClassVar[URIRef] = CATCORE.ThermodynamicStability

    value: str = None
    formation_energy: Optional[Union[float, list[float]]] = empty_list()
    reference_energies: Optional[Union[str, list[str]]] = empty_list()
    energy_above_hull: Optional[Union[float, list[float]]] = empty_list()
    phase_diagram_type: Optional[Union[str, list[str]]] = empty_list()
    competing_phases: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.formation_energy, list):
            self.formation_energy = [self.formation_energy] if self.formation_energy is not None else []
        self.formation_energy = [v if isinstance(v, float) else float(v) for v in self.formation_energy]

        if not isinstance(self.reference_energies, list):
            self.reference_energies = [self.reference_energies] if self.reference_energies is not None else []
        self.reference_energies = [v if isinstance(v, str) else str(v) for v in self.reference_energies]

        if not isinstance(self.energy_above_hull, list):
            self.energy_above_hull = [self.energy_above_hull] if self.energy_above_hull is not None else []
        self.energy_above_hull = [v if isinstance(v, float) else float(v) for v in self.energy_above_hull]

        if not isinstance(self.phase_diagram_type, list):
            self.phase_diagram_type = [self.phase_diagram_type] if self.phase_diagram_type is not None else []
        self.phase_diagram_type = [v if isinstance(v, str) else str(v) for v in self.phase_diagram_type]

        if not isinstance(self.competing_phases, list):
            self.competing_phases = [self.competing_phases] if self.competing_phases is not None else []
        self.competing_phases = [v if isinstance(v, str) else str(v) for v in self.competing_phases]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Piezoelectricity(CalculatedProperty):
    """
    Piezoelectric response of a non-centrosymmetric material, described by the
    piezoelectric tensor. Relevant for piezocatalysis applications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Piezoelectricity"]
    class_class_curie: ClassVar[str] = "catcore:Piezoelectricity"
    class_name: ClassVar[str] = "Piezoelectricity"
    class_model_uri: ClassVar[URIRef] = CATCORE.Piezoelectricity

    value: str = None
    piezoelectric_tensor: Optional[Union[str, list[str]]] = empty_list()
    crystal_symmetry: Optional[Union[str, list[str]]] = empty_list()
    strain_applied: Optional[Union[float, list[float]]] = empty_list()
    ionic_electronic_contributions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.piezoelectric_tensor, list):
            self.piezoelectric_tensor = [self.piezoelectric_tensor] if self.piezoelectric_tensor is not None else []
        self.piezoelectric_tensor = [v if isinstance(v, str) else str(v) for v in self.piezoelectric_tensor]

        if not isinstance(self.crystal_symmetry, list):
            self.crystal_symmetry = [self.crystal_symmetry] if self.crystal_symmetry is not None else []
        self.crystal_symmetry = [v if isinstance(v, str) else str(v) for v in self.crystal_symmetry]

        if not isinstance(self.strain_applied, list):
            self.strain_applied = [self.strain_applied] if self.strain_applied is not None else []
        self.strain_applied = [v if isinstance(v, float) else float(v) for v in self.strain_applied]

        if not isinstance(self.ionic_electronic_contributions, list):
            self.ionic_electronic_contributions = [self.ionic_electronic_contributions] if self.ionic_electronic_contributions is not None else []
        self.ionic_electronic_contributions = [v if isinstance(v, str) else str(v) for v in self.ionic_electronic_contributions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElasticConstants(CalculatedProperty):
    """
    Elastic mechanical properties of a material derived from the elastic tensor,
    including bulk modulus, shear modulus, and Young's modulus.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElasticConstants"]
    class_class_curie: ClassVar[str] = "catcore:ElasticConstants"
    class_name: ClassVar[str] = "ElasticConstants"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElasticConstants

    value: str = None
    elastic_tensor: Optional[Union[str, list[str]]] = empty_list()
    bulk_modulus: Optional[Union[float, list[float]]] = empty_list()
    shear_modulus: Optional[Union[float, list[float]]] = empty_list()
    poisson_ratio: Optional[Union[float, list[float]]] = empty_list()
    young_modulus: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.elastic_tensor, list):
            self.elastic_tensor = [self.elastic_tensor] if self.elastic_tensor is not None else []
        self.elastic_tensor = [v if isinstance(v, str) else str(v) for v in self.elastic_tensor]

        if not isinstance(self.bulk_modulus, list):
            self.bulk_modulus = [self.bulk_modulus] if self.bulk_modulus is not None else []
        self.bulk_modulus = [v if isinstance(v, float) else float(v) for v in self.bulk_modulus]

        if not isinstance(self.shear_modulus, list):
            self.shear_modulus = [self.shear_modulus] if self.shear_modulus is not None else []
        self.shear_modulus = [v if isinstance(v, float) else float(v) for v in self.shear_modulus]

        if not isinstance(self.poisson_ratio, list):
            self.poisson_ratio = [self.poisson_ratio] if self.poisson_ratio is not None else []
        self.poisson_ratio = [v if isinstance(v, float) else float(v) for v in self.poisson_ratio]

        if not isinstance(self.young_modulus, list):
            self.young_modulus = [self.young_modulus] if self.young_modulus is not None else []
        self.young_modulus = [v if isinstance(v, float) else float(v) for v in self.young_modulus]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Surfaces(CalculatedProperty):
    """
    Surface properties of a catalyst computed from a periodic slab model,
    including surface energy, Miller index, slab thickness, and vacuum spacing.
    Central to heterogeneous catalysis modelling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Surfaces"]
    class_class_curie: ClassVar[str] = "catcore:Surfaces"
    class_name: ClassVar[str] = "Surfaces"
    class_model_uri: ClassVar[URIRef] = CATCORE.Surfaces

    value: str = None
    surface_energy: Optional[Union[float, list[float]]] = empty_list()
    miller_indices: Optional[Union[str, list[str]]] = empty_list()
    slab_thickness: Optional[Union[float, list[float]]] = empty_list()
    vacuum_spacing: Optional[Union[float, list[float]]] = empty_list()
    surface_termination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.surface_energy, list):
            self.surface_energy = [self.surface_energy] if self.surface_energy is not None else []
        self.surface_energy = [v if isinstance(v, float) else float(v) for v in self.surface_energy]

        if not isinstance(self.miller_indices, list):
            self.miller_indices = [self.miller_indices] if self.miller_indices is not None else []
        self.miller_indices = [v if isinstance(v, str) else str(v) for v in self.miller_indices]

        if not isinstance(self.slab_thickness, list):
            self.slab_thickness = [self.slab_thickness] if self.slab_thickness is not None else []
        self.slab_thickness = [v if isinstance(v, float) else float(v) for v in self.slab_thickness]

        if not isinstance(self.vacuum_spacing, list):
            self.vacuum_spacing = [self.vacuum_spacing] if self.vacuum_spacing is not None else []
        self.vacuum_spacing = [v if isinstance(v, float) else float(v) for v in self.vacuum_spacing]

        if not isinstance(self.surface_termination_method, list):
            self.surface_termination_method = [self.surface_termination_method] if self.surface_termination_method is not None else []
        self.surface_termination_method = [v if isinstance(v, str) else str(v) for v in self.surface_termination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DielectricTensors(CalculatedProperty):
    """
    Dielectric tensor computed from density functional perturbation theory (DFPT).
    Characterises the optical and static dielectric response of a material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DielectricTensors"]
    class_class_curie: ClassVar[str] = "catcore:DielectricTensors"
    class_name: ClassVar[str] = "DielectricTensors"
    class_model_uri: ClassVar[URIRef] = CATCORE.DielectricTensors

    value: str = None
    dielectric_tensor: Optional[Union[str, list[str]]] = empty_list()
    born_effective_charges: Optional[Union[str, list[str]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.dielectric_tensor, list):
            self.dielectric_tensor = [self.dielectric_tensor] if self.dielectric_tensor is not None else []
        self.dielectric_tensor = [v if isinstance(v, str) else str(v) for v in self.dielectric_tensor]

        if not isinstance(self.born_effective_charges, list):
            self.born_effective_charges = [self.born_effective_charges] if self.born_effective_charges is not None else []
        self.born_effective_charges = [v if isinstance(v, str) else str(v) for v in self.born_effective_charges]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhononDispersion(CalculatedProperty):
    """
    Phonon dispersion relations computed from interatomic force constants,
    providing access to vibrational frequencies, thermodynamic quantities,
    and dynamical stability (imaginary modes).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhononDispersion"]
    class_class_curie: ClassVar[str] = "catcore:PhononDispersion"
    class_name: ClassVar[str] = "PhononDispersion"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhononDispersion

    value: str = None
    force_constant_method: Optional[Union[str, list[str]]] = empty_list()
    kq_point_mesh: Optional[Union[str, list[str]]] = empty_list()
    smearing_parameter: Optional[Union[float, list[float]]] = empty_list()
    imaginary_modes: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.force_constant_method, list):
            self.force_constant_method = [self.force_constant_method] if self.force_constant_method is not None else []
        self.force_constant_method = [v if isinstance(v, str) else str(v) for v in self.force_constant_method]

        if not isinstance(self.kq_point_mesh, list):
            self.kq_point_mesh = [self.kq_point_mesh] if self.kq_point_mesh is not None else []
        self.kq_point_mesh = [v if isinstance(v, str) else str(v) for v in self.kq_point_mesh]

        if not isinstance(self.smearing_parameter, list):
            self.smearing_parameter = [self.smearing_parameter] if self.smearing_parameter is not None else []
        self.smearing_parameter = [v if isinstance(v, float) else float(v) for v in self.smearing_parameter]

        if not isinstance(self.imaginary_modes, list):
            self.imaginary_modes = [self.imaginary_modes] if self.imaginary_modes is not None else []
        self.imaginary_modes = [v if isinstance(v, Bool) else Bool(v) for v in self.imaginary_modes]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EquationsOfState(CalculatedProperty):
    """
    Equation of state relating energy (or enthalpy) to volume, fitted to a
    parametric model (e.g. Birch-Murnaghan). Used to extract equilibrium
    volume, bulk modulus, and its pressure derivative.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["EquationsOfState"]
    class_class_curie: ClassVar[str] = "catcore:EquationsOfState"
    class_name: ClassVar[str] = "EquationsOfState"
    class_model_uri: ClassVar[URIRef] = CATCORE.EquationsOfState

    value: str = None
    fit_method: Optional[Union[str, list[str]]] = empty_list()
    bulk_modulus: Optional[Union[float, list[float]]] = empty_list()
    pressure_derivative: Optional[Union[float, list[float]]] = empty_list()
    fit_residuals: Optional[Union[float, list[float]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fit_method, list):
            self.fit_method = [self.fit_method] if self.fit_method is not None else []
        self.fit_method = [v if isinstance(v, str) else str(v) for v in self.fit_method]

        if not isinstance(self.bulk_modulus, list):
            self.bulk_modulus = [self.bulk_modulus] if self.bulk_modulus is not None else []
        self.bulk_modulus = [v if isinstance(v, float) else float(v) for v in self.bulk_modulus]

        if not isinstance(self.pressure_derivative, list):
            self.pressure_derivative = [self.pressure_derivative] if self.pressure_derivative is not None else []
        self.pressure_derivative = [v if isinstance(v, float) else float(v) for v in self.pressure_derivative]

        if not isinstance(self.fit_residuals, list):
            self.fit_residuals = [self.fit_residuals] if self.fit_residuals is not None else []
        self.fit_residuals = [v if isinstance(v, float) else float(v) for v in self.fit_residuals]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AqueousStability(CalculatedProperty):
    """
    Electrochemical (Pourbaix) stability of a catalyst in aqueous solution as
    a function of pH and electrode potential. Critical for electrocatalyst
    stability screening.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["AqueousStability"]
    class_class_curie: ClassVar[str] = "catcore:AqueousStability"
    class_name: ClassVar[str] = "AqueousStability"
    class_model_uri: ClassVar[URIRef] = CATCORE.AqueousStability

    value: str = None
    ph_range: Optional[Union[str, list[str]]] = empty_list()
    potential_range: Optional[Union[str, list[str]]] = empty_list()
    solvation_model: Optional[Union[str, list[str]]] = empty_list()
    ionic_strength: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.ph_range, list):
            self.ph_range = [self.ph_range] if self.ph_range is not None else []
        self.ph_range = [v if isinstance(v, str) else str(v) for v in self.ph_range]

        if not isinstance(self.potential_range, list):
            self.potential_range = [self.potential_range] if self.potential_range is not None else []
        self.potential_range = [v if isinstance(v, str) else str(v) for v in self.potential_range]

        if not isinstance(self.solvation_model, list):
            self.solvation_model = [self.solvation_model] if self.solvation_model is not None else []
        self.solvation_model = [v if isinstance(v, str) else str(v) for v in self.solvation_model]

        if not isinstance(self.ionic_strength, list):
            self.ionic_strength = [self.ionic_strength] if self.ionic_strength is not None else []
        self.ionic_strength = [v if isinstance(v, float) else float(v) for v in self.ionic_strength]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrainBoundaries(CalculatedProperty):
    """
    Grain boundary structure and energetics from atomistic simulation.
    Relevant for understanding polycrystalline catalyst behaviour,
    sintering, and charge/defect segregation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["GrainBoundaries"]
    class_class_curie: ClassVar[str] = "catcore:GrainBoundaries"
    class_name: ClassVar[str] = "GrainBoundaries"
    class_model_uri: ClassVar[URIRef] = CATCORE.GrainBoundaries

    value: str = None
    grain_boundary_plane: Optional[Union[str, list[str]]] = empty_list()
    misorientation_angle: Optional[Union[float, list[float]]] = empty_list()
    grain_boundary_energy: Optional[Union[float, list[float]]] = empty_list()
    simulation_cell_size: Optional[Union[str, list[str]]] = empty_list()
    gb_excess_volume: Optional[Union[float, list[float]]] = empty_list()
    gb_structural_units: Optional[Union[str, list[str]]] = empty_list()
    charge_defect_segregation: Optional[Union[str, list[str]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.grain_boundary_plane, list):
            self.grain_boundary_plane = [self.grain_boundary_plane] if self.grain_boundary_plane is not None else []
        self.grain_boundary_plane = [v if isinstance(v, str) else str(v) for v in self.grain_boundary_plane]

        if not isinstance(self.misorientation_angle, list):
            self.misorientation_angle = [self.misorientation_angle] if self.misorientation_angle is not None else []
        self.misorientation_angle = [v if isinstance(v, float) else float(v) for v in self.misorientation_angle]

        if not isinstance(self.grain_boundary_energy, list):
            self.grain_boundary_energy = [self.grain_boundary_energy] if self.grain_boundary_energy is not None else []
        self.grain_boundary_energy = [v if isinstance(v, float) else float(v) for v in self.grain_boundary_energy]

        if not isinstance(self.simulation_cell_size, list):
            self.simulation_cell_size = [self.simulation_cell_size] if self.simulation_cell_size is not None else []
        self.simulation_cell_size = [v if isinstance(v, str) else str(v) for v in self.simulation_cell_size]

        if not isinstance(self.gb_excess_volume, list):
            self.gb_excess_volume = [self.gb_excess_volume] if self.gb_excess_volume is not None else []
        self.gb_excess_volume = [v if isinstance(v, float) else float(v) for v in self.gb_excess_volume]

        if not isinstance(self.gb_structural_units, list):
            self.gb_structural_units = [self.gb_structural_units] if self.gb_structural_units is not None else []
        self.gb_structural_units = [v if isinstance(v, str) else str(v) for v in self.gb_structural_units]

        if not isinstance(self.charge_defect_segregation, list):
            self.charge_defect_segregation = [self.charge_defect_segregation] if self.charge_defect_segregation is not None else []
        self.charge_defect_segregation = [v if isinstance(v, str) else str(v) for v in self.charge_defect_segregation]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectronicStructure(CalculatedProperty):
    """
    Electronic band structure and density of states, characterising the
    electronic properties of a catalyst relevant to activity descriptors
    (d-band centre, band gap, Fermi energy).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElectronicStructure"]
    class_class_curie: ClassVar[str] = "catcore:ElectronicStructure"
    class_name: ClassVar[str] = "ElectronicStructure"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectronicStructure

    value: str = None
    smearing_method: Optional[Union[str, list[str]]] = empty_list()
    spin_polarized: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    band_path: Optional[Union[str, list[str]]] = empty_list()
    fermi_energy: Optional[Union[float, list[float]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.smearing_method, list):
            self.smearing_method = [self.smearing_method] if self.smearing_method is not None else []
        self.smearing_method = [v if isinstance(v, str) else str(v) for v in self.smearing_method]

        if not isinstance(self.spin_polarized, list):
            self.spin_polarized = [self.spin_polarized] if self.spin_polarized is not None else []
        self.spin_polarized = [v if isinstance(v, Bool) else Bool(v) for v in self.spin_polarized]

        if not isinstance(self.band_path, list):
            self.band_path = [self.band_path] if self.band_path is not None else []
        self.band_path = [v if isinstance(v, str) else str(v) for v in self.band_path]

        if not isinstance(self.fermi_energy, list):
            self.fermi_energy = [self.fermi_energy] if self.fermi_energy is not None else []
        self.fermi_energy = [v if isinstance(v, float) else float(v) for v in self.fermi_energy]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ferroelectrics(CalculatedProperty):
    """
    Ferroelectric properties computed from DFT, including spontaneous
    polarization, switching barrier, and coercive field. Relevant for
    ferroelectric-photocatalyst design.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Ferroelectrics"]
    class_class_curie: ClassVar[str] = "catcore:Ferroelectrics"
    class_name: ClassVar[str] = "Ferroelectrics"
    class_model_uri: ClassVar[URIRef] = CATCORE.Ferroelectrics

    value: str = None
    polarization_direction: Optional[Union[str, list[str]]] = empty_list()
    spontaneous_polarization: Optional[Union[float, list[float]]] = empty_list()
    reference_structure: Optional[Union[str, list[str]]] = empty_list()
    switching_barrier: Optional[Union[float, list[float]]] = empty_list()
    coercive_field: Optional[Union[float, list[float]]] = empty_list()
    temperature_dependence: Optional[Union[str, list[str]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.polarization_direction, list):
            self.polarization_direction = [self.polarization_direction] if self.polarization_direction is not None else []
        self.polarization_direction = [v if isinstance(v, str) else str(v) for v in self.polarization_direction]

        if not isinstance(self.spontaneous_polarization, list):
            self.spontaneous_polarization = [self.spontaneous_polarization] if self.spontaneous_polarization is not None else []
        self.spontaneous_polarization = [v if isinstance(v, float) else float(v) for v in self.spontaneous_polarization]

        if not isinstance(self.reference_structure, list):
            self.reference_structure = [self.reference_structure] if self.reference_structure is not None else []
        self.reference_structure = [v if isinstance(v, str) else str(v) for v in self.reference_structure]

        if not isinstance(self.switching_barrier, list):
            self.switching_barrier = [self.switching_barrier] if self.switching_barrier is not None else []
        self.switching_barrier = [v if isinstance(v, float) else float(v) for v in self.switching_barrier]

        if not isinstance(self.coercive_field, list):
            self.coercive_field = [self.coercive_field] if self.coercive_field is not None else []
        self.coercive_field = [v if isinstance(v, float) else float(v) for v in self.coercive_field]

        if not isinstance(self.temperature_dependence, list):
            self.temperature_dependence = [self.temperature_dependence] if self.temperature_dependence is not None else []
        self.temperature_dependence = [v if isinstance(v, str) else str(v) for v in self.temperature_dependence]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BandGap(CalculatedProperty):
    """
    Electronic band gap and its character (direct/indirect), with optional
    many-body (GW) or excitonic corrections. Critical for photocatalyst
    and semiconductor catalyst screening.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["BandGap"]
    class_class_curie: ClassVar[str] = "catcore:BandGap"
    class_name: ClassVar[str] = "BandGap"
    class_model_uri: ClassVar[URIRef] = CATCORE.BandGap

    value: str = None
    material_sample: Optional[Union[str, list[str]]] = empty_list()
    structure_model: Optional[Union[str, list[str]]] = empty_list()
    smearing_broadening: Optional[Union[float, list[float]]] = empty_list()
    direct_indirect: Optional[Union[str, list[str]]] = empty_list()
    experimental_reference: Optional[Union[float, list[float]]] = empty_list()
    gw_hybrid_correction: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    excitonic_correction: Optional[Union[float, list[float]]] = empty_list()
    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_sample, list):
            self.material_sample = [self.material_sample] if self.material_sample is not None else []
        self.material_sample = [v if isinstance(v, str) else str(v) for v in self.material_sample]

        if not isinstance(self.structure_model, list):
            self.structure_model = [self.structure_model] if self.structure_model is not None else []
        self.structure_model = [v if isinstance(v, str) else str(v) for v in self.structure_model]

        if not isinstance(self.smearing_broadening, list):
            self.smearing_broadening = [self.smearing_broadening] if self.smearing_broadening is not None else []
        self.smearing_broadening = [v if isinstance(v, float) else float(v) for v in self.smearing_broadening]

        if not isinstance(self.direct_indirect, list):
            self.direct_indirect = [self.direct_indirect] if self.direct_indirect is not None else []
        self.direct_indirect = [v if isinstance(v, str) else str(v) for v in self.direct_indirect]

        if not isinstance(self.experimental_reference, list):
            self.experimental_reference = [self.experimental_reference] if self.experimental_reference is not None else []
        self.experimental_reference = [v if isinstance(v, float) else float(v) for v in self.experimental_reference]

        if not isinstance(self.gw_hybrid_correction, list):
            self.gw_hybrid_correction = [self.gw_hybrid_correction] if self.gw_hybrid_correction is not None else []
        self.gw_hybrid_correction = [v if isinstance(v, Bool) else Bool(v) for v in self.gw_hybrid_correction]

        if not isinstance(self.excitonic_correction, list):
            self.excitonic_correction = [self.excitonic_correction] if self.excitonic_correction is not None else []
        self.excitonic_correction = [v if isinstance(v, float) else float(v) for v in self.excitonic_correction]

        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeAttribute(YAMLRoot):
    """
    A quantifiable piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "QuantitativeAttribute"
    class_model_uri: ClassVar[URIRef] = CATCORE.QuantitativeAttribute

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[Union[str, DefinedTermId]] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.has_quantity_type):
            self.MissingRequiredField("has_quantity_type")
        if not isinstance(self.has_quantity_type, DefinedTermId):
            self.has_quantity_type = DefinedTermId(self.has_quantity_type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.unit is not None and not isinstance(self.unit, DefinedTermId):
            self.unit = DefinedTermId(self.unit)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    See [DCAT-AP specs:Relationship](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Relationship)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = CATCORE.Relationship

    had_role: Union[Union[dict, "Role"], list[Union[dict, "Role"]]] = None
    relation: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.had_role):
            self.MissingRequiredField("had_role")
        if not isinstance(self.had_role, list):
            self.had_role = [self.had_role] if self.had_role is not None else []
        self.had_role = [v if isinstance(v, Role) else Role(**as_dict(v)) for v in self.had_role]

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        self._normalize_inlined_as_list(slot_name="relation", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Software(AgenticEntity):
    """
    An instrument composed of a series of instructions that can be interpreted by or directly executed by a computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "prov:SoftwareAgent"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = CATCORE.Software

    id: Union[str, SoftwareId] = None
    has_part: Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Software, key_name="id", keyed=True)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportiveEntity(YAMLRoot):
    """
    The supportive entities are supporting the main entities in the Application Profile. They are included in the
    Application Profile because they form the range of properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCATAP_PLUS["SupportiveEntity"]
    class_class_curie: ClassVar[str] = "dcatap_plus:SupportiveEntity"
    class_name: ClassVar[str] = "SupportiveEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.SupportiveEntity

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribution(SupportiveEntity):
    """
    See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = CATCORE.Attribution

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChecksumAlgorithm(SupportiveEntity):
    """
    See [DCAT-AP specs:ChecksumAlgorithm](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ChecksumAlgorithm)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["ChecksumAlgorithm"]
    class_class_curie: ClassVar[str] = "spdx:ChecksumAlgorithm"
    class_name: ClassVar[str] = "ChecksumAlgorithm"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChecksumAlgorithm

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(SupportiveEntity):
    """
    See [DCAT-AP specs:Concept](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Concept)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = CATCORE.Concept

    preferred_label: Union[str, list[str]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_label):
            self.MissingRequiredField("preferred_label")
        if not isinstance(self.preferred_label, list):
            self.preferred_label = [self.preferred_label] if self.preferred_label is not None else []
        self.preferred_label = [v if isinstance(v, str) else str(v) for v in self.preferred_label]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptScheme(SupportiveEntity):
    """
    See [DCAT-AP specs:ConceptScheme](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ConceptScheme)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptScheme"
    class_model_uri: ClassVar[URIRef] = CATCORE.ConceptScheme

    title: Union[str, list[str]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Document(SupportiveEntity):
    """
    See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = CATCORE.Document

    id: Union[str, DocumentId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentId):
            self.id = DocumentId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Frequency(SupportiveEntity):
    """
    See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Frequency"]
    class_class_curie: ClassVar[str] = "dcterms:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = CATCORE.Frequency

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Geometry(SupportiveEntity):
    """
    See [DCAT-AP specs:Geometry](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Geometry)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Geometry"]
    class_class_curie: ClassVar[str] = "locn:Geometry"
    class_name: ClassVar[str] = "Geometry"
    class_model_uri: ClassVar[URIRef] = CATCORE.Geometry

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifier(SupportiveEntity):
    """
    See [DCAT-AP specs:Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["Identifier"]
    class_class_curie: ClassVar[str] = "adms:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CATCORE.Identifier

    notation: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.notation):
            self.MissingRequiredField("notation")
        if not isinstance(self.notation, str):
            self.notation = str(self.notation)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalResource(SupportiveEntity):
    """
    See [DCAT-AP specs:LegalResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LegalResource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "LegalResource"
    class_model_uri: ClassVar[URIRef] = CATCORE.LegalResource

    id: Union[str, LegalResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalResourceId):
            self.id = LegalResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseDocument(SupportiveEntity):
    """
    See [DCAT-AP specs:LicenseDocument](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LicenseDocument)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dcterms:LicenseDocument"
    class_name: ClassVar[str] = "LicenseDocument"
    class_model_uri: ClassVar[URIRef] = CATCORE.LicenseDocument

    id: Union[str, LicenseDocumentId] = None
    type: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LicenseDocumentId):
            self.id = LicenseDocumentId(self.id)

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.type]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LinguisticSystem(SupportiveEntity):
    """
    See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dcterms:LinguisticSystem"
    class_name: ClassVar[str] = "LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = CATCORE.LinguisticSystem

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaType(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaType"]
    class_class_curie: ClassVar[str] = "dcterms:MediaType"
    class_name: ClassVar[str] = "MediaType"
    class_model_uri: ClassVar[URIRef] = CATCORE.MediaType

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaTypeOrExtent(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaTypeOrExtent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaTypeOrExtent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dcterms:MediaTypeOrExtent"
    class_name: ClassVar[str] = "MediaTypeOrExtent"
    class_model_uri: ClassVar[URIRef] = CATCORE.MediaTypeOrExtent

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PeriodOfTime(SupportiveEntity):
    """
    See [DCAT-AP specs:PeriodOfTime](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#PeriodOfTime)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dcterms:PeriodOfTime"
    class_name: ClassVar[str] = "PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = CATCORE.PeriodOfTime

    beginning: Optional[Union[dict, "TimeInstant"]] = None
    end: Optional[Union[dict, "TimeInstant"]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    start_date: Optional[Union[str, XSDDate]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.beginning is not None and not isinstance(self.beginning, TimeInstant):
            self.beginning = TimeInstant(**as_dict(self.beginning))

        if self.end is not None and not isinstance(self.end, TimeInstant):
            self.end = TimeInstant(**as_dict(self.end))

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Policy(SupportiveEntity):
    """
    See [DCAT-AP specs:Policy](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Policy)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ODRL["Policy"]
    class_class_curie: ClassVar[str] = "odrl:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = CATCORE.Policy

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvenanceStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["ProvenanceStatement"]
    class_class_curie: ClassVar[str] = "dcterms:ProvenanceStatement"
    class_name: ClassVar[str] = "ProvenanceStatement"
    class_model_uri: ClassVar[URIRef] = CATCORE.ProvenanceStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(SupportiveEntity):
    """
    See [DCAT-AP specs:Resource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Resource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = CATCORE.Resource

    id: Union[str, ResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["RightsStatement"]
    class_class_curie: ClassVar[str] = "dcterms:RightsStatement"
    class_name: ClassVar[str] = "RightsStatement"
    class_model_uri: ClassVar[URIRef] = CATCORE.RightsStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(SupportiveEntity):
    """
    See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Role"]
    class_class_curie: ClassVar[str] = "dcat:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = CATCORE.Role

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(SupportiveEntity):
    """
    See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Standard"]
    class_class_curie: ClassVar[str] = "dcterms:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = CATCORE.Standard

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Surrounding(YAMLRoot):
    """
    The surrounding in which the dataset creating activity took place (e.g. a lab).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Location"]
    class_class_curie: ClassVar[str] = "prov:Location"
    class_name: ClassVar[str] = "Surrounding"
    class_model_uri: ClassVar[URIRef] = CATCORE.Surrounding

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


class Laboratory(Surrounding):
    """
    A facility that provides controlled conditions in which scientific or technological research, experiments, and
    measurement may be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ENVO["01001405"]
    class_class_curie: ClassVar[str] = "ENVO:01001405"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = CATCORE.Laboratory


@dataclass(repr=False)
class TimeInstant(SupportiveEntity):
    """
    See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["Instant"]
    class_class_curie: ClassVar[str] = "time:Instant"
    class_name: ClassVar[str] = "TimeInstant"
    class_model_uri: ClassVar[URIRef] = CATCORE.TimeInstant

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InChIKey(QualitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000059"]
    class_class_curie: ClassVar[str] = "CHEMINF:000059"
    class_name: ClassVar[str] = "InChIKey"
    class_model_uri: ClassVar[URIRef] = CATCORE.InChIKey

    value: str = None

@dataclass(repr=False)
class InChi(QualitativeAttribute):
    """
    A structure descriptor which conforms to the InChI format specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000113"]
    class_class_curie: ClassVar[str] = "CHEMINF:000113"
    class_name: ClassVar[str] = "InChi"
    class_model_uri: ClassVar[URIRef] = CATCORE.InChi

    value: str = None

@dataclass(repr=False)
class MolecularFormula(QualitativeAttribute):
    """
    A structure descriptor which identifies each constituent element by its chemical symbol and indicates the number
    of atoms of each element found in each discrete molecule of that compound.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000042"]
    class_class_curie: ClassVar[str] = "CHEMINF:000042"
    class_name: ClassVar[str] = "MolecularFormula"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolecularFormula

    value: str = None

@dataclass(repr=False)
class IUPACName(QualitativeAttribute):
    """
    A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out
    by the International Union of Pure and Applied Chemistry (IUPAC).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000107"]
    class_class_curie: ClassVar[str] = "CHEMINF:000107"
    class_name: ClassVar[str] = "IUPACName"
    class_model_uri: ClassVar[URIRef] = CATCORE.IUPACName

    value: str = None

@dataclass(repr=False)
class SMILES(QualitativeAttribute):
    """
    A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format
    specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000018"]
    class_class_curie: ClassVar[str] = "CHEMINF:000018"
    class_name: ClassVar[str] = "SMILES"
    class_model_uri: ClassVar[URIRef] = CATCORE.SMILES

    value: str = None

@dataclass(repr=False)
class Concentration(QuantitativeAttribute):
    """
    A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume
    of the mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002820"]
    class_class_curie: ClassVar[str] = "CHMO:0002820"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = CATCORE.Concentration

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class AmountOfSubstance(QuantitativeAttribute):
    """
    The total amount of substance used in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "AmountOfSubstance"
    class_model_uri: ClassVar[URIRef] = CATCORE.AmountOfSubstance

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PHValue(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001089"]
    class_class_curie: ClassVar[str] = "SIO:001089"
    class_name: ClassVar[str] = "PHValue"
    class_model_uri: ClassVar[URIRef] = CATCORE.PHValue

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class ChemicalReaction(Activity):
    """
    A process that leads to the transformation of one set of chemical substances to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010345"]
    class_class_curie: ClassVar[str] = "SIO:010345"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChemicalReaction

    id: Union[str, ChemicalReactionId] = None
    used_starting_material: Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, "StartingMaterial"]], list[Union[dict, "StartingMaterial"]]]] = empty_dict()
    used_reactant: Optional[Union[dict[Union[str, ReagentId], Union[dict, "Reagent"]], list[Union[dict, "Reagent"]]]] = empty_dict()
    generated_product: Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, "ChemicalProduct"]], list[Union[dict, "ChemicalProduct"]]]] = empty_dict()
    used_catalyst: Optional[Union[dict[Union[str, CatalystId], Union[dict, "Catalyst"]], list[Union[dict, "Catalyst"]]]] = empty_dict()
    used_solvent: Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, "DissolvingSubstance"]], list[Union[dict, "DissolvingSubstance"]]]] = empty_dict()
    has_duration: Optional[str] = None
    used_reactor: Optional[Union[dict[Union[str, ReactorId], Union[dict, "Reactor"]], list[Union[dict, "Reactor"]]]] = empty_dict()
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_yield: Optional[Union[Union[dict, "Yield"], list[Union[dict, "Yield"]]]] = empty_list()
    has_reaction_step: Optional[Union[str, ChemicalReactionId]] = None
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalReactionId):
            self.id = ChemicalReactionId(self.id)

        self._normalize_inlined_as_list(slot_name="used_starting_material", slot_type=StartingMaterial, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_reactant", slot_type=Reagent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="generated_product", slot_type=ChemicalProduct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_catalyst", slot_type=Catalyst, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_solvent", slot_type=DissolvingSubstance, key_name="id", keyed=True)

        if self.has_duration is not None and not isinstance(self.has_duration, str):
            self.has_duration = str(self.has_duration)

        self._normalize_inlined_as_list(slot_name="used_reactor", slot_type=Reactor, key_name="id", keyed=True)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_yield, list):
            self.has_yield = [self.has_yield] if self.has_yield is not None else []
        self.has_yield = [v if isinstance(v, Yield) else Yield(**as_dict(v)) for v in self.has_yield]

        if self.has_reaction_step is not None and not isinstance(self.has_reaction_step, ChemicalReactionId):
            self.has_reaction_step = ChemicalReactionId(self.has_reaction_step)

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DissolvingSubstance(AgenticEntity):
    """
    A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010417"]
    class_class_curie: ClassVar[str] = "SIO:010417"
    class_name: ClassVar[str] = "DissolvingSubstance"
    class_model_uri: ClassVar[URIRef] = CATCORE.DissolvingSubstance

    id: Union[str, DissolvingSubstanceId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, "PercentageOfTotal"], list[Union[dict, "PercentageOfTotal"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, "MolarEquivalent"], list[Union[dict, "MolarEquivalent"]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DissolvingSubstanceId):
            self.id = DissolvingSubstanceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalyst(AgenticEntity):
    """
    A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being
    affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010344"]
    class_class_curie: ClassVar[str] = "SIO:010344"
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = CATCORE.Catalyst

    id: Union[str, CatalystId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_molar_equivalent: Optional[Union[Union[dict, "MolarEquivalent"], list[Union[dict, "MolarEquivalent"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, "PercentageOfTotal"], list[Union[dict, "PercentageOfTotal"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystId):
            self.id = CatalystId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reactor(Device):
    """
    A reactor is a container for controlling a biological or chemical reaction or process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000153"]
    class_class_curie: ClassVar[str] = "AFE:0000153"
    class_name: ClassVar[str] = "Reactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.Reactor

    id: Union[str, ReactorId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactorId):
            self.id = ReactorId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Yield(QuantitativeAttribute):
    """
    A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking
    into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100
    %).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Yield"
    class_model_uri: ClassVar[URIRef] = CATCORE.Yield

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarEquivalent(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "MolarEquivalent"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolarEquivalent

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PercentageOfTotal(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "PercentageOfTotal"
    class_model_uri: ClassVar[URIRef] = CATCORE.PercentageOfTotal

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Materialistic(YAMLRoot):
    """
    A LinkML mixin used to pass down properties common to all material entities. It is needed for example to have
    MaterialSample have the same properties as MaterialEntity, although it is defined as a subclass of
    EvaluatedEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MATERIAL_ENTITIES_AP["Materialistic"]
    class_class_curie: ClassVar[str] = "material_entities_ap:Materialistic"
    class_name: ClassVar[str] = "Materialistic"
    class_model_uri: ClassVar[URIRef] = CATCORE.Materialistic

    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialEntity(Entity):
    """
    A material is an Entity that has some portion of matter as proper part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    has_part: Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]] = empty_dict()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=MaterialEntity, key_name="id", keyed=True)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(MaterialEntity):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex,
    conformer etc., identifiable as a separately distinguishable entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["23367"]
    class_class_curie: ClassVar[str] = "CHEBI:23367"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    inchi: Optional[Union[Union[dict, InChi], list[Union[dict, InChi]]]] = empty_list()
    inchikey: Optional[Union[Union[dict, InChIKey], list[Union[dict, InChIKey]]]] = empty_list()
    smiles: Optional[Union[Union[dict, SMILES], list[Union[dict, SMILES]]]] = empty_list()
    molecular_formula: Optional[Union[Union[dict, MolecularFormula], list[Union[dict, MolecularFormula]]]] = empty_list()
    iupac_name: Optional[Union[Union[dict, IUPACName], list[Union[dict, IUPACName]]]] = empty_list()
    has_molar_mass: Optional[Union[Union[dict, "MolarMass"], list[Union[dict, "MolarMass"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if not isinstance(self.inchi, list):
            self.inchi = [self.inchi] if self.inchi is not None else []
        self.inchi = [v if isinstance(v, InChi) else InChi(**as_dict(v)) for v in self.inchi]

        if not isinstance(self.inchikey, list):
            self.inchikey = [self.inchikey] if self.inchikey is not None else []
        self.inchikey = [v if isinstance(v, InChIKey) else InChIKey(**as_dict(v)) for v in self.inchikey]

        if not isinstance(self.smiles, list):
            self.smiles = [self.smiles] if self.smiles is not None else []
        self.smiles = [v if isinstance(v, SMILES) else SMILES(**as_dict(v)) for v in self.smiles]

        if not isinstance(self.molecular_formula, list):
            self.molecular_formula = [self.molecular_formula] if self.molecular_formula is not None else []
        self.molecular_formula = [v if isinstance(v, MolecularFormula) else MolecularFormula(**as_dict(v)) for v in self.molecular_formula]

        if not isinstance(self.iupac_name, list):
            self.iupac_name = [self.iupac_name] if self.iupac_name is not None else []
        self.iupac_name = [v if isinstance(v, IUPACName) else IUPACName(**as_dict(v)) for v in self.iupac_name]

        if not isinstance(self.has_molar_mass, list):
            self.has_molar_mass = [self.has_molar_mass] if self.has_molar_mass is not None else []
        self.has_molar_mass = [v if isinstance(v, MolarMass) else MolarMass(**as_dict(v)) for v in self.has_molar_mass]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Atom(ChemicalEntity):
    """
    A MaterialEntity constituting the smallest component of an element having the chemical properties of the element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["33250"]
    class_class_curie: ClassVar[str] = "CHEBI:33250"
    class_name: ClassVar[str] = "Atom"
    class_model_uri: ClassVar[URIRef] = CATCORE.Atom

    id: Union[str, AtomId] = None
    rdf_type: Union[dict, DefinedTerm] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomId):
            self.id = AtomId(self.id)

        if self._is_empty(self.rdf_type):
            self.MissingRequiredField("rdf_type")
        if not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSubstance(MaterialEntity):
    """
    A MaterialEntity of constant composition, composed of chemical entities of the same type or of different types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["59999"]
    class_class_curie: ClassVar[str] = "CHEBI:59999"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Polymer(ChemicalSubstance):
    """
    A ChemicalSubstance that is composed of macromolecules of different kinds and which may be differentiated by
    composition, length, degree of branching etc..
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["60027"]
    class_class_curie: ClassVar[str] = "CHEBI:60027"
    class_name: ClassVar[str] = "Polymer"
    class_model_uri: ClassVar[URIRef] = CATCORE.Polymer

    id: Union[str, PolymerId] = None

@dataclass(repr=False)
class StartingMaterial(ChemicalSubstance):
    """
    A ChemicalSubstance with that has a starting material role in a synthesis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCO["0000029"]
    class_class_curie: ClassVar[str] = "PROCO:0000029"
    class_name: ClassVar[str] = "StartingMaterial"
    class_model_uri: ClassVar[URIRef] = CATCORE.StartingMaterial

    id: Union[str, StartingMaterialId] = None
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StartingMaterialId):
            self.id = StartingMaterialId(self.id)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reagent(ChemicalSubstance):
    """
    A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010411"]
    class_class_curie: ClassVar[str] = "SIO:010411"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = CATCORE.Reagent

    id: Union[str, ReagentId] = None
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReagentId):
            self.id = ReagentId(self.id)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalProduct(ChemicalSubstance):
    """
    A chemical substance that is produced by a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C48810"]
    class_class_curie: ClassVar[str] = "NCIT:C48810"
    class_name: ClassVar[str] = "ChemicalProduct"
    class_model_uri: ClassVar[URIRef] = CATCORE.ChemicalProduct

    id: Union[str, ChemicalProductId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalProductId):
            self.id = ChemicalProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialSample(EvaluatedEntity):
    """
    A Sample that was derived from a previous MaterialSample or some other kind of MaterialEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000747"]
    class_class_curie: ClassVar[str] = "OBI:0000747"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = CATCORE.MaterialSample

    id: Union[str, MaterialSampleId] = None
    derived_from: Optional[Union[dict, Entity]] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        if self.derived_from is not None and not isinstance(self.derived_from, Entity):
            self.derived_from = Entity(**as_dict(self.derived_from))

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Precursor(MaterialSample):
    """
    A MaterialSample that serves as input material in a catalyst Synthesis.
    Precursors are consumed or transformed during the preparation process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["52717"]
    class_class_curie: ClassVar[str] = "CHEBI:52717"
    class_name: ClassVar[str] = "Precursor"
    class_model_uri: ClassVar[URIRef] = CATCORE.Precursor

    id: Union[str, PrecursorId] = None
    precursor_quantity: Union[float, list[float]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrecursorId):
            self.id = PrecursorId(self.id)

        if self._is_empty(self.precursor_quantity):
            self.MissingRequiredField("precursor_quantity")
        if not isinstance(self.precursor_quantity, list):
            self.precursor_quantity = [self.precursor_quantity] if self.precursor_quantity is not None else []
        self.precursor_quantity = [v if isinstance(v, float) else float(v) for v in self.precursor_quantity]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalystSample(MaterialSample):
    """
    A MaterialSample that is the product of a catalyst Synthesis.
    The specific type of catalyst (e.g. heterogeneous, supported metal)
    is expressed via rdf_type using a voc4cat term.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000747"]
    class_class_curie: ClassVar[str] = "OBI:0000747"
    class_name: ClassVar[str] = "CatalystSample"
    class_model_uri: ClassVar[URIRef] = CATCORE.CatalystSample

    id: Union[str, CatalystSampleId] = None
    derived_from: Optional[Union[dict, MaterialSample]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystSampleId):
            self.id = CatalystSampleId(self.id)

        if self.derived_from is not None and not isinstance(self.derived_from, MaterialSample):
            self.derived_from = MaterialSample(**as_dict(self.derived_from))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubstanceSample(MaterialSample):
    """
    A MaterialSample derived from a ChemicalSubstance that is of interest in an analytical procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "SubstanceSample"
    class_model_uri: ClassVar[URIRef] = CATCORE.SubstanceSample

    id: Union[str, SubstanceSampleId] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceSampleId):
            self.id = SubstanceSampleId(self.id)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolymerSample(SubstanceSample):
    """
    A SubstanceSample derived from a Polymer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "PolymerSample"
    class_model_uri: ClassVar[URIRef] = CATCORE.PolymerSample

    id: Union[str, PolymerSampleId] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymerSampleId):
            self.id = PolymerSampleId(self.id)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Temperature(QuantitativeAttribute):
    """
    A physical quantity that quantitatively expresses the attribute of hotness or coldness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Temperature"
    class_model_uri: ClassVar[URIRef] = CATCORE.Temperature

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Mass(QuantitativeAttribute):
    """
    The strength of a body's gravitational attraction to other bodies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Mass"
    class_model_uri: ClassVar[URIRef] = CATCORE.Mass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarMass(Mass):
    """
    A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23
    atoms or molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFR["0002409"]
    class_class_curie: ClassVar[str] = "AFR:0002409"
    class_name: ClassVar[str] = "MolarMass"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolarMass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Volume(QuantitativeAttribute):
    """
    A measure of regions in three-dimensional space.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = CATCORE.Volume

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Density(QuantitativeAttribute):
    """
    A measure of the mass per unit volume of a substance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001406"]
    class_class_curie: ClassVar[str] = "SIO:001406"
    class_name: ClassVar[str] = "Density"
    class_model_uri: ClassVar[URIRef] = CATCORE.Density

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Pressure(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Pressure"
    class_model_uri: ClassVar[URIRef] = CATCORE.Pressure

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

# Enumerations
class CatalysisResearchFieldEnum(EnumDefinitionImpl):
    """
    Enumeration of catalysis research fields.
    Intended for use via rdf_type on a dcat:Dataset (via ClassifierMixin)
    to classify which field of catalysis the dataset belongs to,
    following DCAT-AP-PLUS Pattern 3 (Flexible classification).
    """
    heterogeneous_catalysis = PermissibleValue(
        text="heterogeneous_catalysis",
        description="Heterogeneous catalysis — catalyst and reactants are in different phases.",
        meaning=VOC4CAT["0007001"])
    homogeneous_catalysis = PermissibleValue(
        text="homogeneous_catalysis",
        description="Homogeneous catalysis — catalyst and reactants are in the same phase.",
        meaning=VOC4CAT["0000294"])
    biocatalysis = PermissibleValue(
        text="biocatalysis",
        description="Biocatalysis — use of enzymes or whole cells as catalysts.",
        meaning=VOC4CAT["0000204"])
    electrocatalysis = PermissibleValue(
        text="electrocatalysis",
        description="Electrocatalysis — catalysis of electrochemical reactions.",
        meaning=VOC4CAT["0000216"])
    hybrid_catalysis = PermissibleValue(
        text="hybrid_catalysis",
        description="Hybrid catalysis — combination of two or more catalytic approaches.")
    other = PermissibleValue(
        text="other",
        description="Other catalysis research field not covered by the above terms.")

    _defn = EnumDefinition(
        name="CatalysisResearchFieldEnum",
        description="""Enumeration of catalysis research fields.
Intended for use via rdf_type on a dcat:Dataset (via ClassifierMixin)
to classify which field of catalysis the dataset belongs to,
following DCAT-AP-PLUS Pattern 3 (Flexible classification).""",
    )

class ImpregnationTypeEnum(EnumDefinitionImpl):
    """
    Enumeration of impregnation types used in catalyst synthesis.
    """
    wet_impregnation = PermissibleValue(
        text="wet_impregnation",
        description="Wet impregnation — excess solution is used to impregnate the support.")
    dry_impregnation = PermissibleValue(
        text="dry_impregnation",
        description="Dry impregnation — solution volume equals the pore volume of the support.")
    incipient_wetness = PermissibleValue(
        text="incipient_wetness",
        description="Incipient wetness impregnation — synonym for dry impregnation.")
    other = PermissibleValue(
        text="other",
        description="Other impregnation type.")

    _defn = EnumDefinition(
        name="ImpregnationTypeEnum",
        description="Enumeration of impregnation types used in catalyst synthesis.",
    )

class SampleStateEnum(EnumDefinitionImpl):
    """
    Enumeration of physical states in which a catalyst sample may be present.
    """
    solid = PermissibleValue(
        text="solid",
        description="Solid state.")
    liquid = PermissibleValue(
        text="liquid",
        description="Liquid state.")
    gas = PermissibleValue(
        text="gas",
        description="Gas state.")
    solution = PermissibleValue(
        text="solution",
        description="Dissolved in solvent.")
    powder = PermissibleValue(
        text="powder",
        description="Powder form.")
    pellet = PermissibleValue(
        text="pellet",
        description="Pellet form (pressed powder).")
    thin_film = PermissibleValue(
        text="thin_film",
        description="Thin film deposited on a substrate.")
    other = PermissibleValue(
        text="other",
        description="Other sample state.")

    _defn = EnumDefinition(
        name="SampleStateEnum",
        description="Enumeration of physical states in which a catalyst sample may be present.",
    )

class DatasetThemes(EnumDefinitionImpl):

    AGRI = PermissibleValue(
        text="AGRI",
        description="Agriculture, fisheries, forestry and food",
        meaning=None)
    ECON = PermissibleValue(
        text="ECON",
        description="Economy and finance",
        meaning=None)
    EDUC = PermissibleValue(
        text="EDUC",
        description="Education, culture and sport",
        meaning=None)
    ENER = PermissibleValue(
        text="ENER",
        description="Energy",
        meaning=None)
    ENVI = PermissibleValue(
        text="ENVI",
        description="Environment",
        meaning=None)
    GOVE = PermissibleValue(
        text="GOVE",
        description="Government and public sector",
        meaning=None)
    HEAL = PermissibleValue(
        text="HEAL",
        description="Health",
        meaning=None)
    INTR = PermissibleValue(
        text="INTR",
        description="International issues",
        meaning=None)
    JUST = PermissibleValue(
        text="JUST",
        description="Justice, legal system and public safety",
        meaning=None)
    OP_DATPRO = PermissibleValue(
        text="OP_DATPRO",
        description="Provisional data",
        meaning=None)
    REGI = PermissibleValue(
        text="REGI",
        description="Regions and cities",
        meaning=None)
    SOCI = PermissibleValue(
        text="SOCI",
        description="Population and society",
        meaning=None)
    TECH = PermissibleValue(
        text="TECH",
        description="Science and technology",
        meaning=None)
    TRAN = PermissibleValue(
        text="TRAN",
        description="Transport",
        meaning=None)

    _defn = EnumDefinition(
        name="DatasetThemes",
    )

class TopLevelMediaTypes(EnumDefinitionImpl):

    application = PermissibleValue(text="application")
    audio = PermissibleValue(text="audio")
    example = PermissibleValue(text="example")
    font = PermissibleValue(text="font")
    haptics = PermissibleValue(text="haptics")
    image = PermissibleValue(text="image")
    message = PermissibleValue(text="message")
    model = PermissibleValue(text="model")
    multipart = PermissibleValue(text="multipart")
    text = PermissibleValue(text="text")
    video = PermissibleValue(text="video")

    _defn = EnumDefinition(
        name="TopLevelMediaTypes",
    )

class QUDTQuantityKindEnum(EnumDefinitionImpl):
    """
    Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.
    """
    _defn = EnumDefinition(
        name="QUDTQuantityKindEnum",
        description="Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.",
    )

class QUDTUnitEnum(EnumDefinitionImpl):
    """
    Possible kinds of QUDT unit instances.
    """
    _defn = EnumDefinition(
        name="QUDTUnitEnum",
        description="Possible kinds of QUDT unit instances.",
    )

class PhysicalStateEnum(EnumDefinitionImpl):

    SOLID = PermissibleValue(
        text="SOLID",
        description="A state of matter in which molecules are closely packed and cannot move past each other.",
        meaning=PATO["0001736"])
    CRYSTAL = PermissibleValue(
        text="CRYSTAL",
        description="""A solid state of matter whose constituents (such as atoms, molecules, or ions) are arranged in a highly ordered microscopic structure, forming a crystal lattice that extends in all directions.""",
        meaning=PATO["0002066"])
    LIQUID = PermissibleValue(
        text="LIQUID",
        description="""A state of matter with a definite volume but no fixed shape. Liquids adapt to the shape of their container and are nearly incompressible, maintaining their volume even under pressure.""",
        meaning=PATO["0001735"])
    GASEOUS = PermissibleValue(
        text="GASEOUS",
        description="A state of matter with neither fixed volume nor fixed shape.",
        meaning=PATO["0001737"])

    _defn = EnumDefinition(
        name="PhysicalStateEnum",
    )

# Slots
class slots:
    pass

slots.atmosphere = Slot(uri=CATCORE.atmosphere, name="atmosphere", curie=CATCORE.curie('atmosphere'),
                   model_uri=CATCORE.atmosphere, domain=None, range=Optional[Union[str, list[str]]])

slots.temperature = Slot(uri=AFR['0001584'], name="temperature", curie=AFR.curie('0001584'),
                   model_uri=CATCORE.temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.equipment = Slot(uri=VOC4CAT['0000187'], name="equipment", curie=VOC4CAT.curie('0000187'),
                   model_uri=CATCORE.equipment, domain=None, range=Optional[Union[str, list[str]]])

slots.flow_rate = Slot(uri=CATCORE.flow_rate, name="flow_rate", curie=CATCORE.curie('flow_rate'),
                   model_uri=CATCORE.flow_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.heating_rate = Slot(uri=CATCORE.heating_rate, name="heating_rate", curie=CATCORE.curie('heating_rate'),
                   model_uri=CATCORE.heating_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.heating_procedure = Slot(uri=CATCORE.heating_procedure, name="heating_procedure", curie=CATCORE.curie('heating_procedure'),
                   model_uri=CATCORE.heating_procedure, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_cycles = Slot(uri=CATCORE.number_of_cycles, name="number_of_cycles", curie=CATCORE.curie('number_of_cycles'),
                   model_uri=CATCORE.number_of_cycles, domain=None, range=Optional[Union[int, list[int]]])

slots.sample_mass = Slot(uri=CATCORE.sample_mass, name="sample_mass", curie=CATCORE.curie('sample_mass'),
                   model_uri=CATCORE.sample_mass, domain=None, range=Optional[Union[float, list[float]]])

slots.sample_pretreatment = Slot(uri=VOC4CAT['0000122'], name="sample_pretreatment", curie=VOC4CAT.curie('0000122'),
                   model_uri=CATCORE.sample_pretreatment, domain=None, range=Optional[Union[str, list[str]]])

slots.stirring_speed = Slot(uri=CATCORE.stirring_speed, name="stirring_speed", curie=CATCORE.curie('stirring_speed'),
                   model_uri=CATCORE.stirring_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.stirring_duration = Slot(uri=CATCORE.stirring_duration, name="stirring_duration", curie=CATCORE.curie('stirring_duration'),
                   model_uri=CATCORE.stirring_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.vessel_type = Slot(uri=CATCORE.vessel_type, name="vessel_type", curie=CATCORE.curie('vessel_type'),
                   model_uri=CATCORE.vessel_type, domain=None, range=Optional[Union[str, list[str]]])

slots.carrier_gas = Slot(uri=CATCORE.carrier_gas, name="carrier_gas", curie=CATCORE.curie('carrier_gas'),
                   model_uri=CATCORE.carrier_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.dispersant = Slot(uri=CATCORE.dispersant, name="dispersant", curie=CATCORE.curie('dispersant'),
                   model_uri=CATCORE.dispersant, domain=None, range=Optional[Union[str, list[str]]])

slots.drying_device = Slot(uri=CATCORE.drying_device, name="drying_device", curie=CATCORE.curie('drying_device'),
                   model_uri=CATCORE.drying_device, domain=None, range=Optional[Union[str, list[str]]])

slots.drying_temperature = Slot(uri=CATCORE.drying_temperature, name="drying_temperature", curie=CATCORE.curie('drying_temperature'),
                   model_uri=CATCORE.drying_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.drying_time = Slot(uri=CATCORE.drying_time, name="drying_time", curie=CATCORE.curie('drying_time'),
                   model_uri=CATCORE.drying_time, domain=None, range=Optional[Union[float, list[float]]])

slots.drying_atmosphere = Slot(uri=CATCORE.drying_atmosphere, name="drying_atmosphere", curie=CATCORE.curie('drying_atmosphere'),
                   model_uri=CATCORE.drying_atmosphere, domain=None, range=Optional[Union[str, list[str]]])

slots.calcination_initial_temperature = Slot(uri=VOC4CAT['0000057'], name="calcination_initial_temperature", curie=VOC4CAT.curie('0000057'),
                   model_uri=CATCORE.calcination_initial_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_final_temperature = Slot(uri=VOC4CAT['0000058'], name="calcination_final_temperature", curie=VOC4CAT.curie('0000058'),
                   model_uri=CATCORE.calcination_final_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_dwelling_time = Slot(uri=VOC4CAT['0000060'], name="calcination_dwelling_time", curie=VOC4CAT.curie('0000060'),
                   model_uri=CATCORE.calcination_dwelling_time, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_gaseous_environment = Slot(uri=VOC4CAT['0000055'], name="calcination_gaseous_environment", curie=VOC4CAT.curie('0000055'),
                   model_uri=CATCORE.calcination_gaseous_environment, domain=None, range=Optional[Union[str, list[str]]])

slots.calcination_heating_rate = Slot(uri=VOC4CAT['0000059'], name="calcination_heating_rate", curie=VOC4CAT.curie('0000059'),
                   model_uri=CATCORE.calcination_heating_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_gas_flow_rate = Slot(uri=VOC4CAT['0000056'], name="calcination_gas_flow_rate", curie=VOC4CAT.curie('0000056'),
                   model_uri=CATCORE.calcination_gas_flow_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.step_size = Slot(uri=AFR['0000950'], name="step_size", curie=AFR.curie('0000950'),
                   model_uri=CATCORE.step_size, domain=None, range=Optional[Union[float, list[float]]])

slots.resolution = Slot(uri=CATCORE.resolution, name="resolution", curie=CATCORE.curie('resolution'),
                   model_uri=CATCORE.resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.integration_time = Slot(uri=CATCORE.integration_time, name="integration_time", curie=CATCORE.curie('integration_time'),
                   model_uri=CATCORE.integration_time, domain=None, range=Optional[Union[float, list[float]]])

slots.number_of_scans = Slot(uri=CATCORE.number_of_scans, name="number_of_scans", curie=CATCORE.curie('number_of_scans'),
                   model_uri=CATCORE.number_of_scans, domain=None, range=Optional[Union[int, list[int]]])

slots.operation_mode = Slot(uri=VOC4CAT['0000108'], name="operation_mode", curie=VOC4CAT.curie('0000108'),
                   model_uri=CATCORE.operation_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.concentration = Slot(uri=CATCORE.concentration, name="concentration", curie=CATCORE.curie('concentration'),
                   model_uri=CATCORE.concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.solvent = Slot(uri=VOC4CAT['0007246'], name="solvent", curie=VOC4CAT.curie('0007246'),
                   model_uri=CATCORE.solvent, domain=None, range=Optional[Union[str, list[str]]])

slots.injection_volume = Slot(uri=CATCORE.injection_volume, name="injection_volume", curie=CATCORE.curie('injection_volume'),
                   model_uri=CATCORE.injection_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.external_standard = Slot(uri=CATCORE.external_standard, name="external_standard", curie=CATCORE.curie('external_standard'),
                   model_uri=CATCORE.external_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.internal_standard = Slot(uri=CATCORE.internal_standard, name="internal_standard", curie=CATCORE.curie('internal_standard'),
                   model_uri=CATCORE.internal_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.calibration_method = Slot(uri=CATCORE.calibration_method, name="calibration_method", curie=CATCORE.curie('calibration_method'),
                   model_uri=CATCORE.calibration_method, domain=None, range=Optional[Union[str, list[str]]])

slots.column_type = Slot(uri=CATCORE.column_type, name="column_type", curie=CATCORE.curie('column_type'),
                   model_uri=CATCORE.column_type, domain=None, range=Optional[Union[str, list[str]]])

slots.experiment_duration = Slot(uri=AFR['0002455'], name="experiment_duration", curie=AFR.curie('0002455'),
                   model_uri=CATCORE.experiment_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.filtration_device = Slot(uri=CATCORE.filtration_device, name="filtration_device", curie=CATCORE.curie('filtration_device'),
                   model_uri=CATCORE.filtration_device, domain=None, range=Optional[Union[str, list[str]]])

slots.filter_type = Slot(uri=CATCORE.filter_type, name="filter_type", curie=CATCORE.curie('filter_type'),
                   model_uri=CATCORE.filter_type, domain=None, range=Optional[Union[str, list[str]]])

slots.nominal_composition = Slot(uri=CATCORE.nominal_composition, name="nominal_composition", curie=CATCORE.curie('nominal_composition'),
                   model_uri=CATCORE.nominal_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.catalyst_measured_properties = Slot(uri=CATCORE.catalyst_measured_properties, name="catalyst_measured_properties", curie=CATCORE.curie('catalyst_measured_properties'),
                   model_uri=CATCORE.catalyst_measured_properties, domain=None, range=Optional[Union[str, list[str]]])

slots.storage_conditions = Slot(uri=CATCORE.storage_conditions, name="storage_conditions", curie=CATCORE.curie('storage_conditions'),
                   model_uri=CATCORE.storage_conditions, domain=None, range=Optional[Union[str, list[str]]])

slots.support = Slot(uri=CATCORE.support, name="support", curie=CATCORE.curie('support'),
                   model_uri=CATCORE.support, domain=None, range=Optional[Union[str, list[str]]])

slots.precursor_quantity = Slot(uri=CATCORE.precursor_quantity, name="precursor_quantity", curie=CATCORE.curie('precursor_quantity'),
                   model_uri=CATCORE.precursor_quantity, domain=None, range=Optional[Union[float, list[float]]])

slots.impregnation_type = Slot(uri=CATCORE.impregnation_type, name="impregnation_type", curie=CATCORE.curie('impregnation_type'),
                   model_uri=CATCORE.impregnation_type, domain=None, range=Optional[Union[Union[str, "ImpregnationTypeEnum"], list[Union[str, "ImpregnationTypeEnum"]]]])

slots.impregnation_duration = Slot(uri=CATCORE.impregnation_duration, name="impregnation_duration", curie=CATCORE.curie('impregnation_duration'),
                   model_uri=CATCORE.impregnation_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.impregnation_temperature = Slot(uri=CATCORE.impregnation_temperature, name="impregnation_temperature", curie=CATCORE.curie('impregnation_temperature'),
                   model_uri=CATCORE.impregnation_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.precipitating_agent = Slot(uri=CATCORE.precipitating_agent, name="precipitating_agent", curie=CATCORE.curie('precipitating_agent'),
                   model_uri=CATCORE.precipitating_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.precipitating_concentration = Slot(uri=CATCORE.precipitating_concentration, name="precipitating_concentration", curie=CATCORE.curie('precipitating_concentration'),
                   model_uri=CATCORE.precipitating_concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_ph = Slot(uri=VOC4CAT['0000052'], name="synthesis_ph", curie=VOC4CAT.curie('0000052'),
                   model_uri=CATCORE.synthesis_ph, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_rate = Slot(uri=CATCORE.mixing_rate, name="mixing_rate", curie=CATCORE.curie('mixing_rate'),
                   model_uri=CATCORE.mixing_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_time = Slot(uri=CATCORE.mixing_time, name="mixing_time", curie=CATCORE.curie('mixing_time'),
                   model_uri=CATCORE.mixing_time, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_temperature = Slot(uri=CATCORE.mixing_temperature, name="mixing_temperature", curie=CATCORE.curie('mixing_temperature'),
                   model_uri=CATCORE.mixing_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.order_of_addition = Slot(uri=CATCORE.order_of_addition, name="order_of_addition", curie=CATCORE.curie('order_of_addition'),
                   model_uri=CATCORE.order_of_addition, domain=None, range=Optional[Union[str, list[str]]])

slots.filtration = Slot(uri=CATCORE.filtration, name="filtration", curie=CATCORE.curie('filtration'),
                   model_uri=CATCORE.filtration, domain=None, range=Optional[Union[str, list[str]]])

slots.purification = Slot(uri=CATCORE.purification, name="purification", curie=CATCORE.curie('purification'),
                   model_uri=CATCORE.purification, domain=None, range=Optional[Union[str, list[str]]])

slots.aging_temperature = Slot(uri=CATCORE.aging_temperature, name="aging_temperature", curie=CATCORE.curie('aging_temperature'),
                   model_uri=CATCORE.aging_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.aging_time = Slot(uri=CATCORE.aging_time, name="aging_time", curie=CATCORE.curie('aging_time'),
                   model_uri=CATCORE.aging_time, domain=None, range=Optional[Union[float, list[float]]])

slots.deposition_temperature = Slot(uri=CATCORE.deposition_temperature, name="deposition_temperature", curie=CATCORE.curie('deposition_temperature'),
                   model_uri=CATCORE.deposition_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.deposition_time = Slot(uri=CATCORE.deposition_time, name="deposition_time", curie=CATCORE.curie('deposition_time'),
                   model_uri=CATCORE.deposition_time, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_temperature = Slot(uri=VOC4CAT['0000051'], name="synthesis_temperature", curie=VOC4CAT.curie('0000051'),
                   model_uri=CATCORE.synthesis_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_duration = Slot(uri=VOC4CAT['0000050'], name="synthesis_duration", curie=VOC4CAT.curie('0000050'),
                   model_uri=CATCORE.synthesis_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_pressure = Slot(uri=VOC4CAT['0000053'], name="synthesis_pressure", curie=VOC4CAT.curie('0000053'),
                   model_uri=CATCORE.synthesis_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.hydrolysis_ratio = Slot(uri=CATCORE.hydrolysis_ratio, name="hydrolysis_ratio", curie=CATCORE.curie('hydrolysis_ratio'),
                   model_uri=CATCORE.hydrolysis_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.drying = Slot(uri=CATCORE.drying, name="drying", curie=CATCORE.curie('drying'),
                   model_uri=CATCORE.drying, domain=None, range=Optional[Union[str, list[str]]])

slots.surfactant_template = Slot(uri=CATCORE.surfactant_template, name="surfactant_template", curie=CATCORE.curie('surfactant_template'),
                   model_uri=CATCORE.surfactant_template, domain=None, range=Optional[Union[str, list[str]]])

slots.filling_volume = Slot(uri=CATCORE.filling_volume, name="filling_volume", curie=CATCORE.curie('filling_volume'),
                   model_uri=CATCORE.filling_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.stirrer_type = Slot(uri=CATCORE.stirrer_type, name="stirrer_type", curie=CATCORE.curie('stirrer_type'),
                   model_uri=CATCORE.stirrer_type, domain=None, range=Optional[Union[str, list[str]]])

slots.cooling_rate = Slot(uri=CATCORE.cooling_rate, name="cooling_rate", curie=CATCORE.curie('cooling_rate'),
                   model_uri=CATCORE.cooling_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.plasma_type = Slot(uri=CATCORE.plasma_type, name="plasma_type", curie=CATCORE.curie('plasma_type'),
                   model_uri=CATCORE.plasma_type, domain=None, range=Optional[Union[str, list[str]]])

slots.power_input = Slot(uri=CATCORE.power_input, name="power_input", curie=CATCORE.curie('power_input'),
                   model_uri=CATCORE.power_input, domain=None, range=Optional[Union[float, list[float]]])

slots.exposure_time = Slot(uri=CATCORE.exposure_time, name="exposure_time", curie=CATCORE.curie('exposure_time'),
                   model_uri=CATCORE.exposure_time, domain=None, range=Optional[Union[float, list[float]]])

slots.fuel = Slot(uri=CATCORE.fuel, name="fuel", curie=CATCORE.curie('fuel'),
                   model_uri=CATCORE.fuel, domain=None, range=Optional[Union[str, list[str]]])

slots.oxidizer = Slot(uri=CATCORE.oxidizer, name="oxidizer", curie=CATCORE.curie('oxidizer'),
                   model_uri=CATCORE.oxidizer, domain=None, range=Optional[Union[str, list[str]]])

slots.fuel_to_oxidizer_ratio = Slot(uri=CATCORE.fuel_to_oxidizer_ratio, name="fuel_to_oxidizer_ratio", curie=CATCORE.curie('fuel_to_oxidizer_ratio'),
                   model_uri=CATCORE.fuel_to_oxidizer_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.set_temperature = Slot(uri=CATCORE.set_temperature, name="set_temperature", curie=CATCORE.curie('set_temperature'),
                   model_uri=CATCORE.set_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.post_treatment = Slot(uri=CATCORE.post_treatment, name="post_treatment", curie=CATCORE.curie('post_treatment'),
                   model_uri=CATCORE.post_treatment, domain=None, range=Optional[Union[str, list[str]]])

slots.substrate = Slot(uri=VOC4CAT['0000024'], name="substrate", curie=VOC4CAT.curie('0000024'),
                   model_uri=CATCORE.substrate, domain=None, range=Optional[Union[str, list[str]]])

slots.pulse_time = Slot(uri=CATCORE.pulse_time, name="pulse_time", curie=CATCORE.curie('pulse_time'),
                   model_uri=CATCORE.pulse_time, domain=None, range=Optional[Union[float, list[float]]])

slots.purging_duration = Slot(uri=VOC4CAT['0000112'], name="purging_duration", curie=VOC4CAT.curie('0000112'),
                   model_uri=CATCORE.purging_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.power = Slot(uri=CATCORE.power, name="power", curie=CATCORE.curie('power'),
                   model_uri=CATCORE.power, domain=None, range=Optional[Union[float, list[float]]])

slots.microwave_frequency = Slot(uri=CATCORE.microwave_frequency, name="microwave_frequency", curie=CATCORE.curie('microwave_frequency'),
                   model_uri=CATCORE.microwave_frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.sonication_power = Slot(uri=CATCORE.sonication_power, name="sonication_power", curie=CATCORE.curie('sonication_power'),
                   model_uri=CATCORE.sonication_power, domain=None, range=Optional[Union[float, list[float]]])

slots.sonication_duration = Slot(uri=CATCORE.sonication_duration, name="sonication_duration", curie=CATCORE.curie('sonication_duration'),
                   model_uri=CATCORE.sonication_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.flame_type = Slot(uri=CATCORE.flame_type, name="flame_type", curie=CATCORE.curie('flame_type'),
                   model_uri=CATCORE.flame_type, domain=None, range=Optional[Union[str, list[str]]])

slots.inlet_system = Slot(uri=CATCORE.inlet_system, name="inlet_system", curie=CATCORE.curie('inlet_system'),
                   model_uri=CATCORE.inlet_system, domain=None, range=Optional[Union[str, list[str]]])

slots.flame_ring = Slot(uri=CATCORE.flame_ring, name="flame_ring", curie=CATCORE.curie('flame_ring'),
                   model_uri=CATCORE.flame_ring, domain=None, range=Optional[Union[str, list[str]]])

slots.capillary_pressure = Slot(uri=CATCORE.capillary_pressure, name="capillary_pressure", curie=CATCORE.curie('capillary_pressure'),
                   model_uri=CATCORE.capillary_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.fuel_dispersant_ratio = Slot(uri=CATCORE.fuel_dispersant_ratio, name="fuel_dispersant_ratio", curie=CATCORE.curie('fuel_dispersant_ratio'),
                   model_uri=CATCORE.fuel_dispersant_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.vessel_volume = Slot(uri=CATCORE.vessel_volume, name="vessel_volume", curie=CATCORE.curie('vessel_volume'),
                   model_uri=CATCORE.vessel_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.size_and_material = Slot(uri=CATCORE.size_and_material, name="size_and_material", curie=CATCORE.curie('size_and_material'),
                   model_uri=CATCORE.size_and_material, domain=None, range=Optional[Union[str, list[str]]])

slots.milling_speed = Slot(uri=CATCORE.milling_speed, name="milling_speed", curie=CATCORE.curie('milling_speed'),
                   model_uri=CATCORE.milling_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.milling_duration = Slot(uri=CATCORE.milling_duration, name="milling_duration", curie=CATCORE.curie('milling_duration'),
                   model_uri=CATCORE.milling_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.ball_material = Slot(uri=CATCORE.ball_material, name="ball_material", curie=CATCORE.curie('ball_material'),
                   model_uri=CATCORE.ball_material, domain=None, range=Optional[Union[str, list[str]]])

slots.ball_size = Slot(uri=CATCORE.ball_size, name="ball_size", curie=CATCORE.curie('ball_size'),
                   model_uri=CATCORE.ball_size, domain=None, range=Optional[Union[float, list[float]]])

slots.ball_to_powder_ratio = Slot(uri=CATCORE.ball_to_powder_ratio, name="ball_to_powder_ratio", curie=CATCORE.curie('ball_to_powder_ratio'),
                   model_uri=CATCORE.ball_to_powder_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.reaction_vessel = Slot(uri=CATCORE.reaction_vessel, name="reaction_vessel", curie=CATCORE.curie('reaction_vessel'),
                   model_uri=CATCORE.reaction_vessel, domain=None, range=Optional[Union[str, list[str]]])

slots.mixing_device = Slot(uri=CATCORE.mixing_device, name="mixing_device", curie=CATCORE.curie('mixing_device'),
                   model_uri=CATCORE.mixing_device, domain=None, range=Optional[Union[str, list[str]]])

slots.crystallisation_solvents = Slot(uri=CATCORE.crystallisation_solvents, name="crystallisation_solvents", curie=CATCORE.curie('crystallisation_solvents'),
                   model_uri=CATCORE.crystallisation_solvents, domain=None, range=Optional[Union[str, list[str]]])

slots.precipitation_agent = Slot(uri=CATCORE.precipitation_agent, name="precipitation_agent", curie=CATCORE.curie('precipitation_agent'),
                   model_uri=CATCORE.precipitation_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.crystallisation_duration = Slot(uri=CATCORE.crystallisation_duration, name="crystallisation_duration", curie=CATCORE.curie('crystallisation_duration'),
                   model_uri=CATCORE.crystallisation_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.purification_solvent = Slot(uri=CATCORE.purification_solvent, name="purification_solvent", curie=CATCORE.curie('purification_solvent'),
                   model_uri=CATCORE.purification_solvent, domain=None, range=Optional[Union[str, list[str]]])

slots.temperature_ramp = Slot(uri=CATCORE.temperature_ramp, name="temperature_ramp", curie=CATCORE.curie('temperature_ramp'),
                   model_uri=CATCORE.temperature_ramp, domain=None, range=Optional[Union[float, list[float]]])

slots.sample_state = Slot(uri=CATCORE.sample_state, name="sample_state", curie=CATCORE.curie('sample_state'),
                   model_uri=CATCORE.sample_state, domain=None, range=Optional[Union[Union[str, "SampleStateEnum"], list[Union[str, "SampleStateEnum"]]]])

slots.sample_description = Slot(uri=CATCORE.sample_description, name="sample_description", curie=CATCORE.curie('sample_description'),
                   model_uri=CATCORE.sample_description, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_preparation = Slot(uri=AFP['0001159'], name="sample_preparation", curie=AFP.curie('0001159'),
                   model_uri=CATCORE.sample_preparation, domain=None, range=Optional[Union[str, list[str]]])

slots.detector_type = Slot(uri=AFR['0000317'], name="detector_type", curie=AFR.curie('0000317'),
                   model_uri=CATCORE.detector_type, domain=None, range=Optional[Union[str, list[str]]])

slots.xray_source = Slot(uri=OBI['0001138'], name="xray_source", curie=OBI.curie('0001138'),
                   model_uri=CATCORE.xray_source, domain=None, range=Optional[Union[str, list[str]]])

slots.monochromator = Slot(uri=CHMO['0002120'], name="monochromator", curie=CHMO.curie('0002120'),
                   model_uri=CATCORE.monochromator, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_energy = Slot(uri=CATCORE.minimum_energy, name="minimum_energy", curie=CATCORE.curie('minimum_energy'),
                   model_uri=CATCORE.minimum_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_energy = Slot(uri=CATCORE.maximum_energy, name="maximum_energy", curie=CATCORE.curie('maximum_energy'),
                   model_uri=CATCORE.maximum_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.gun_type = Slot(uri=CATCORE.gun_type, name="gun_type", curie=CATCORE.curie('gun_type'),
                   model_uri=CATCORE.gun_type, domain=None, range=Optional[Union[str, list[str]]])

slots.acceleration_voltage = Slot(uri=CATCORE.acceleration_voltage, name="acceleration_voltage", curie=CATCORE.curie('acceleration_voltage'),
                   model_uri=CATCORE.acceleration_voltage, domain=None, range=Optional[Union[float, list[float]]])

slots.magnification_setting = Slot(uri=AFR['0002226'], name="magnification_setting", curie=AFR.curie('0002226'),
                   model_uri=CATCORE.magnification_setting, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_temperature = Slot(uri=CATCORE.minimum_temperature, name="minimum_temperature", curie=CATCORE.curie('minimum_temperature'),
                   model_uri=CATCORE.minimum_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_temperature = Slot(uri=CATCORE.maximum_temperature, name="maximum_temperature", curie=CATCORE.curie('maximum_temperature'),
                   model_uri=CATCORE.maximum_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.initial_temperature = Slot(uri=NCIT.C164644, name="initial_temperature", curie=NCIT.curie('C164644'),
                   model_uri=CATCORE.initial_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.final_temperature = Slot(uri=NCIT.C164644, name="final_temperature", curie=NCIT.curie('C164644'),
                   model_uri=CATCORE.final_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.mz_minimum = Slot(uri=AFR['0002652'], name="mz_minimum", curie=AFR.curie('0002652'),
                   model_uri=CATCORE.mz_minimum, domain=None, range=Optional[Union[float, list[float]]])

slots.mz_maximum = Slot(uri=AFR['0002653'], name="mz_maximum", curie=AFR.curie('0002653'),
                   model_uri=CATCORE.mz_maximum, domain=None, range=Optional[Union[float, list[float]]])

slots.excitation_wavelength = Slot(uri=AFR['0002479'], name="excitation_wavelength", curie=AFR.curie('0002479'),
                   model_uri=CATCORE.excitation_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.emission_wavelength = Slot(uri=NCIT.C204101, name="emission_wavelength", curie=NCIT.curie('C204101'),
                   model_uri=CATCORE.emission_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.optical_filter = Slot(uri=CATCORE.optical_filter, name="optical_filter", curie=CATCORE.curie('optical_filter'),
                   model_uri=CATCORE.optical_filter, domain=None, range=Optional[Union[str, list[str]]])

slots.reference_electrode = Slot(uri=VOC4CAT['0007204'], name="reference_electrode", curie=VOC4CAT.curie('0007204'),
                   model_uri=CATCORE.reference_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.working_electrode = Slot(uri=VOC4CAT['0007202'], name="working_electrode", curie=VOC4CAT.curie('0007202'),
                   model_uri=CATCORE.working_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.counter_electrode = Slot(uri=VOC4CAT['0007203'], name="counter_electrode", curie=VOC4CAT.curie('0007203'),
                   model_uri=CATCORE.counter_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.electrolyte_composition = Slot(uri=CATCORE.electrolyte_composition, name="electrolyte_composition", curie=CATCORE.curie('electrolyte_composition'),
                   model_uri=CATCORE.electrolyte_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.electrolyte_concentration = Slot(uri=CATCORE.electrolyte_concentration, name="electrolyte_concentration", curie=CATCORE.curie('electrolyte_concentration'),
                   model_uri=CATCORE.electrolyte_concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_2theta = Slot(uri=CATCORE.minimum_2theta, name="minimum_2theta", curie=CATCORE.curie('minimum_2theta'),
                   model_uri=CATCORE.minimum_2theta, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_2theta = Slot(uri=CATCORE.maximum_2theta, name="maximum_2theta", curie=CATCORE.curie('maximum_2theta'),
                   model_uri=CATCORE.maximum_2theta, domain=None, range=Optional[Union[float, list[float]]])

slots.sample_spinning_speed = Slot(uri=CATCORE.sample_spinning_speed, name="sample_spinning_speed", curie=CATCORE.curie('sample_spinning_speed'),
                   model_uri=CATCORE.sample_spinning_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.absorption_edge = Slot(uri=CATCORE.absorption_edge, name="absorption_edge", curie=CATCORE.curie('absorption_edge'),
                   model_uri=CATCORE.absorption_edge, domain=None, range=Optional[Union[str, list[str]]])

slots.element_analyzed = Slot(uri=CATCORE.element_analyzed, name="element_analyzed", curie=CATCORE.curie('element_analyzed'),
                   model_uri=CATCORE.element_analyzed, domain=None, range=Optional[Union[str, list[str]]])

slots.beamline_source = Slot(uri=CATCORE.beamline_source, name="beamline_source", curie=CATCORE.curie('beamline_source'),
                   model_uri=CATCORE.beamline_source, domain=None, range=Optional[Union[str, list[str]]])

slots.noise_of_measurement = Slot(uri=CATCORE.noise_of_measurement, name="noise_of_measurement", curie=CATCORE.curie('noise_of_measurement'),
                   model_uri=CATCORE.noise_of_measurement, domain=None, range=Optional[Union[float, list[float]]])

slots.energy_resolution = Slot(uri=AFR['0000950'], name="energy_resolution", curie=AFR.curie('0000950'),
                   model_uri=CATCORE.energy_resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.total_acquisition_time = Slot(uri=CATCORE.total_acquisition_time, name="total_acquisition_time", curie=CATCORE.curie('total_acquisition_time'),
                   model_uri=CATCORE.total_acquisition_time, domain=None, range=Optional[Union[float, list[float]]])

slots.pass_energy = Slot(uri=CATCORE.pass_energy, name="pass_energy", curie=CATCORE.curie('pass_energy'),
                   model_uri=CATCORE.pass_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.spot_size = Slot(uri=CATCORE.spot_size, name="spot_size", curie=CATCORE.curie('spot_size'),
                   model_uri=CATCORE.spot_size, domain=None, range=Optional[Union[float, list[float]]])

slots.lense_mode = Slot(uri=VOC4CAT['0000108'], name="lense_mode", curie=VOC4CAT.curie('0000108'),
                   model_uri=CATCORE.lense_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.charge_compensation = Slot(uri=CATCORE.charge_compensation, name="charge_compensation", curie=CATCORE.curie('charge_compensation'),
                   model_uri=CATCORE.charge_compensation, domain=None, range=Optional[Union[str, list[str]]])

slots.primary_energy = Slot(uri=CATCORE.primary_energy, name="primary_energy", curie=CATCORE.curie('primary_energy'),
                   model_uri=CATCORE.primary_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.counting_time = Slot(uri=CATCORE.counting_time, name="counting_time", curie=CATCORE.curie('counting_time'),
                   model_uri=CATCORE.counting_time, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_wavenumber = Slot(uri=CATCORE.minimum_wavenumber, name="minimum_wavenumber", curie=CATCORE.curie('minimum_wavenumber'),
                   model_uri=CATCORE.minimum_wavenumber, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_wavenumber = Slot(uri=CATCORE.maximum_wavenumber, name="maximum_wavenumber", curie=CATCORE.curie('maximum_wavenumber'),
                   model_uri=CATCORE.maximum_wavenumber, domain=None, range=Optional[Union[float, list[float]]])

slots.background_correction = Slot(uri=AFP['0003721'], name="background_correction", curie=AFP.curie('0003721'),
                   model_uri=CATCORE.background_correction, domain=None, range=Optional[Union[str, list[str]]])

slots.adsorption_gas = Slot(uri=CATCORE.adsorption_gas, name="adsorption_gas", curie=CATCORE.curie('adsorption_gas'),
                   model_uri=CATCORE.adsorption_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.diluting_reference = Slot(uri=CATCORE.diluting_reference, name="diluting_reference", curie=CATCORE.curie('diluting_reference'),
                   model_uri=CATCORE.diluting_reference, domain=None, range=Optional[Union[str, list[str]]])

slots.ratio_reference_sample = Slot(uri=CATCORE.ratio_reference_sample, name="ratio_reference_sample", curie=CATCORE.curie('ratio_reference_sample'),
                   model_uri=CATCORE.ratio_reference_sample, domain=None, range=Optional[Union[float, list[float]]])

slots.background_correction_method = Slot(uri=CATCORE.background_correction_method, name="background_correction_method", curie=CATCORE.curie('background_correction_method'),
                   model_uri=CATCORE.background_correction_method, domain=None, range=Optional[Union[str, list[str]]])

slots.excitation_laser_wavelength = Slot(uri=AFR['0001594'], name="excitation_laser_wavelength", curie=AFR.curie('0001594'),
                   model_uri=CATCORE.excitation_laser_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.excitation_laser_power = Slot(uri=AFR['0001595'], name="excitation_laser_power", curie=AFR.curie('0001595'),
                   model_uri=CATCORE.excitation_laser_power, domain=None, range=Optional[Union[float, list[float]]])

slots.filter_or_grating = Slot(uri=CATCORE.filter_or_grating, name="filter_or_grating", curie=CATCORE.curie('filter_or_grating'),
                   model_uri=CATCORE.filter_or_grating, domain=None, range=Optional[Union[str, list[str]]])

slots.nucleus = Slot(uri=CATCORE.nucleus, name="nucleus", curie=CATCORE.curie('nucleus'),
                   model_uri=CATCORE.nucleus, domain=None, range=Optional[Union[str, list[str]]])

slots.irradiation_frequency = Slot(uri=CATCORE.irradiation_frequency, name="irradiation_frequency", curie=CATCORE.curie('irradiation_frequency'),
                   model_uri=CATCORE.irradiation_frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.nmr_pulse_sequence = Slot(uri=CATCORE.nmr_pulse_sequence, name="nmr_pulse_sequence", curie=CATCORE.curie('nmr_pulse_sequence'),
                   model_uri=CATCORE.nmr_pulse_sequence, domain=None, range=Optional[Union[str, list[str]]])

slots.nmr_sample_tube = Slot(uri=CATCORE.nmr_sample_tube, name="nmr_sample_tube", curie=CATCORE.curie('nmr_sample_tube'),
                   model_uri=CATCORE.nmr_sample_tube, domain=None, range=Optional[Union[str, list[str]]])

slots.image_resolution = Slot(uri=CATCORE.image_resolution, name="image_resolution", curie=CATCORE.curie('image_resolution'),
                   model_uri=CATCORE.image_resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.field_emitter = Slot(uri=CATCORE.field_emitter, name="field_emitter", curie=CATCORE.curie('field_emitter'),
                   model_uri=CATCORE.field_emitter, domain=None, range=Optional[Union[str, list[str]]])

slots.reducing_gas_composition = Slot(uri=CATCORE.reducing_gas_composition, name="reducing_gas_composition", curie=CATCORE.curie('reducing_gas_composition'),
                   model_uri=CATCORE.reducing_gas_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.oxidizing_gas_composition = Slot(uri=CATCORE.oxidizing_gas_composition, name="oxidizing_gas_composition", curie=CATCORE.curie('oxidizing_gas_composition'),
                   model_uri=CATCORE.oxidizing_gas_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.adsorbate_gas = Slot(uri=CATCORE.adsorbate_gas, name="adsorbate_gas", curie=CATCORE.curie('adsorbate_gas'),
                   model_uri=CATCORE.adsorbate_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.degassing_temperature = Slot(uri=CATCORE.degassing_temperature, name="degassing_temperature", curie=CATCORE.curie('degassing_temperature'),
                   model_uri=CATCORE.degassing_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.measurement_temperature = Slot(uri=CATCORE.measurement_temperature, name="measurement_temperature", curie=CATCORE.curie('measurement_temperature'),
                   model_uri=CATCORE.measurement_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.pore_size_distribution_method = Slot(uri=CATCORE.pore_size_distribution_method, name="pore_size_distribution_method", curie=CATCORE.curie('pore_size_distribution_method'),
                   model_uri=CATCORE.pore_size_distribution_method, domain=None, range=Optional[Union[str, list[str]]])

slots.elements_analyzed = Slot(uri=CATCORE.elements_analyzed, name="elements_analyzed", curie=CATCORE.curie('elements_analyzed'),
                   model_uri=CATCORE.elements_analyzed, domain=None, range=Optional[Union[str, list[str]]])

slots.combustion_temperature = Slot(uri=CATCORE.combustion_temperature, name="combustion_temperature", curie=CATCORE.curie('combustion_temperature'),
                   model_uri=CATCORE.combustion_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.detection_limit = Slot(uri=NCIT.C105701, name="detection_limit", curie=NCIT.curie('C105701'),
                   model_uri=CATCORE.detection_limit, domain=None, range=Optional[Union[float, list[float]]])

slots.matrix_effect_correction = Slot(uri=CATCORE.matrix_effect_correction, name="matrix_effect_correction", curie=CATCORE.curie('matrix_effect_correction'),
                   model_uri=CATCORE.matrix_effect_correction, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_wavelength = Slot(uri=CATCORE.minimum_wavelength, name="minimum_wavelength", curie=CATCORE.curie('minimum_wavelength'),
                   model_uri=CATCORE.minimum_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_wavelength = Slot(uri=CATCORE.maximum_wavelength, name="maximum_wavelength", curie=CATCORE.curie('maximum_wavelength'),
                   model_uri=CATCORE.maximum_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.path_length = Slot(uri=AFQ['0000268'], name="path_length", curie=AFQ.curie('0000268'),
                   model_uri=CATCORE.path_length, domain=None, range=Optional[Union[float, list[float]]])

slots.emission_range = Slot(uri=CATCORE.emission_range, name="emission_range", curie=CATCORE.curie('emission_range'),
                   model_uri=CATCORE.emission_range, domain=None, range=Optional[Union[str, list[str]]])

slots.slit_width = Slot(uri=CATCORE.slit_width, name="slit_width", curie=CATCORE.curie('slit_width'),
                   model_uri=CATCORE.slit_width, domain=None, range=Optional[Union[float, list[float]]])

slots.lifetime_fitting_model = Slot(uri=CATCORE.lifetime_fitting_model, name="lifetime_fitting_model", curie=CATCORE.curie('lifetime_fitting_model'),
                   model_uri=CATCORE.lifetime_fitting_model, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_shots = Slot(uri=CATCORE.number_of_shots, name="number_of_shots", curie=CATCORE.curie('number_of_shots'),
                   model_uri=CATCORE.number_of_shots, domain=None, range=Optional[Union[int, list[int]]])

slots.scan_rate = Slot(uri=VOC4CAT['0007213'], name="scan_rate", curie=VOC4CAT.curie('0007213'),
                   model_uri=CATCORE.scan_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_potential = Slot(uri=CATCORE.minimum_potential, name="minimum_potential", curie=CATCORE.curie('minimum_potential'),
                   model_uri=CATCORE.minimum_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_potential = Slot(uri=CATCORE.maximum_potential, name="maximum_potential", curie=CATCORE.curie('maximum_potential'),
                   model_uri=CATCORE.maximum_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.step_size_potential = Slot(uri=VOC4CAT['0007218'], name="step_size_potential", curie=VOC4CAT.curie('0007218'),
                   model_uri=CATCORE.step_size_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.electrode_configuration = Slot(uri=CATCORE.electrode_configuration, name="electrode_configuration", curie=CATCORE.curie('electrode_configuration'),
                   model_uri=CATCORE.electrode_configuration, domain=None, range=Optional[Union[str, list[str]]])

slots.ac_frequency = Slot(uri=VOC4CAT['0007239'], name="ac_frequency", curie=VOC4CAT.curie('0007239'),
                   model_uri=CATCORE.ac_frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.ac_dc_mode = Slot(uri=CATCORE.ac_dc_mode, name="ac_dc_mode", curie=CATCORE.curie('ac_dc_mode'),
                   model_uri=CATCORE.ac_dc_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_geometry = Slot(uri=CATCORE.sample_geometry, name="sample_geometry", curie=CATCORE.curie('sample_geometry'),
                   model_uri=CATCORE.sample_geometry, domain=None, range=Optional[Union[str, list[str]]])

slots.light_wavelength = Slot(uri=VOC4CAT['0000176'], name="light_wavelength", curie=VOC4CAT.curie('0000176'),
                   model_uri=CATCORE.light_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.scattering_angle = Slot(uri=CATCORE.scattering_angle, name="scattering_angle", curie=CATCORE.curie('scattering_angle'),
                   model_uri=CATCORE.scattering_angle, domain=None, range=Optional[Union[float, list[float]]])

slots.refractive_index = Slot(uri=CATCORE.refractive_index, name="refractive_index", curie=CATCORE.curie('refractive_index'),
                   model_uri=CATCORE.refractive_index, domain=None, range=Optional[Union[float, list[float]]])

slots.measurement_duration = Slot(uri=CATCORE.measurement_duration, name="measurement_duration", curie=CATCORE.curie('measurement_duration'),
                   model_uri=CATCORE.measurement_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.spray_voltage = Slot(uri=CHMO['0002792'], name="spray_voltage", curie=CHMO.curie('0002792'),
                   model_uri=CATCORE.spray_voltage, domain=None, range=Optional[Union[float, list[float]]])

slots.capillary_temperature = Slot(uri=CATCORE.capillary_temperature, name="capillary_temperature", curie=CATCORE.curie('capillary_temperature'),
                   model_uri=CATCORE.capillary_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.solvent_composition = Slot(uri=VOC4CAT['0007246'], name="solvent_composition", curie=VOC4CAT.curie('0007246'),
                   model_uri=CATCORE.solvent_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.carrier_gas_purity = Slot(uri=CATCORE.carrier_gas_purity, name="carrier_gas_purity", curie=CATCORE.curie('carrier_gas_purity'),
                   model_uri=CATCORE.carrier_gas_purity, domain=None, range=Optional[Union[str, list[str]]])

slots.inlet_temperature = Slot(uri=CATCORE.inlet_temperature, name="inlet_temperature", curie=CATCORE.curie('inlet_temperature'),
                   model_uri=CATCORE.inlet_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_oven_temperature = Slot(uri=CATCORE.minimum_oven_temperature, name="minimum_oven_temperature", curie=CATCORE.curie('minimum_oven_temperature'),
                   model_uri=CATCORE.minimum_oven_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_oven_temperature = Slot(uri=CATCORE.maximum_oven_temperature, name="maximum_oven_temperature", curie=CATCORE.curie('maximum_oven_temperature'),
                   model_uri=CATCORE.maximum_oven_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.heating_ramp = Slot(uri=CATCORE.heating_ramp, name="heating_ramp", curie=CATCORE.curie('heating_ramp'),
                   model_uri=CATCORE.heating_ramp, domain=None, range=Optional[Union[float, list[float]]])

slots.acquisition_mode = Slot(uri=CATCORE.acquisition_mode, name="acquisition_mode", curie=CATCORE.curie('acquisition_mode'),
                   model_uri=CATCORE.acquisition_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.solvent_delay = Slot(uri=CATCORE.solvent_delay, name="solvent_delay", curie=CATCORE.curie('solvent_delay'),
                   model_uri=CATCORE.solvent_delay, domain=None, range=Optional[Union[float, list[float]]])

slots.trace_ion_detection = Slot(uri=CATCORE.trace_ion_detection, name="trace_ion_detection", curie=CATCORE.curie('trace_ion_detection'),
                   model_uri=CATCORE.trace_ion_detection, domain=None, range=Optional[Union[str, list[str]]])

slots.split_ratio = Slot(uri=CATCORE.split_ratio, name="split_ratio", curie=CATCORE.curie('split_ratio'),
                   model_uri=CATCORE.split_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.eluent = Slot(uri=AFRL['0000011'], name="eluent", curie=AFRL.curie('0000011'),
                   model_uri=CATCORE.eluent, domain=None, range=Optional[Union[str, list[str]]])

slots.calibration_standard = Slot(uri=CATCORE.calibration_standard, name="calibration_standard", curie=CATCORE.curie('calibration_standard'),
                   model_uri=CATCORE.calibration_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.gradient_program = Slot(uri=CATCORE.gradient_program, name="gradient_program", curie=CATCORE.curie('gradient_program'),
                   model_uri=CATCORE.gradient_program, domain=None, range=Optional[Union[str, list[str]]])

slots.ionization_mode = Slot(uri=CATCORE.ionization_mode, name="ionization_mode", curie=CATCORE.curie('ionization_mode'),
                   model_uri=CATCORE.ionization_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.catalyst_quantity = Slot(uri=CATCORE.catalyst_quantity, name="catalyst_quantity", curie=CATCORE.curie('catalyst_quantity'),
                   model_uri=CATCORE.catalyst_quantity, domain=None, range=Union[float, list[float]])

slots.reactant = Slot(uri=VOC4CAT['0000101'], name="reactant", curie=VOC4CAT.curie('0000101'),
                   model_uri=CATCORE.reactant, domain=None, range=Union[str, list[str]])

slots.catalyst_type = Slot(uri=VOC4CAT['0007014'], name="catalyst_type", curie=VOC4CAT.curie('0007014'),
                   model_uri=CATCORE.catalyst_type, domain=None, range=Optional[Union[str, list[str]]])

slots.reactor_temperature_range = Slot(uri=VOC4CAT['0007032'], name="reactor_temperature_range", curie=VOC4CAT.curie('0007032'),
                   model_uri=CATCORE.reactor_temperature_range, domain=None, range=Optional[Union[str, list[str]]])

slots.experiment_pressure = Slot(uri=VOC4CAT['0000118'], name="experiment_pressure", curie=VOC4CAT.curie('0000118'),
                   model_uri=CATCORE.experiment_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.feed_composition_range = Slot(uri=CATCORE.feed_composition_range, name="feed_composition_range", curie=CATCORE.curie('feed_composition_range'),
                   model_uri=CATCORE.feed_composition_range, domain=None, range=Optional[Union[str, list[str]]])

slots.gas_distributor_type = Slot(uri=CATCORE.gas_distributor_type, name="gas_distributor_type", curie=CATCORE.curie('gas_distributor_type'),
                   model_uri=CATCORE.gas_distributor_type, domain=None, range=Optional[Union[str, list[str]]])

slots.bed_expansion_height = Slot(uri=CATCORE.bed_expansion_height, name="bed_expansion_height", curie=CATCORE.curie('bed_expansion_height'),
                   model_uri=CATCORE.bed_expansion_height, domain=None, range=Optional[Union[float, list[float]]])

slots.bubble_size_distribution = Slot(uri=CATCORE.bubble_size_distribution, name="bubble_size_distribution", curie=CATCORE.curie('bubble_size_distribution'),
                   model_uri=CATCORE.bubble_size_distribution, domain=None, range=Optional[str])

slots.software_package = Slot(uri=CATCORE.software_package, name="software_package", curie=CATCORE.curie('software_package'),
                   model_uri=CATCORE.software_package, domain=None, range=Union[str, list[str]])

slots.calculated_property = Slot(uri=CATCORE.calculated_property, name="calculated_property", curie=CATCORE.curie('calculated_property'),
                   model_uri=CATCORE.calculated_property, domain=None, range=Union[Union[dict, CalculatedProperty], list[Union[dict, CalculatedProperty]]])

slots.exchange_correlation_functional = Slot(uri=CATCORE.exchange_correlation_functional, name="exchange_correlation_functional", curie=CATCORE.curie('exchange_correlation_functional'),
                   model_uri=CATCORE.exchange_correlation_functional, domain=None, range=Optional[Union[str, list[str]]])

slots.energy_cutoff = Slot(uri=CATCORE.energy_cutoff, name="energy_cutoff", curie=CATCORE.curie('energy_cutoff'),
                   model_uri=CATCORE.energy_cutoff, domain=None, range=Optional[Union[float, list[float]]])

slots.convergence_criteria = Slot(uri=CATCORE.convergence_criteria, name="convergence_criteria", curie=CATCORE.curie('convergence_criteria'),
                   model_uri=CATCORE.convergence_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.dft_u_parameters = Slot(uri=CATCORE.dft_u_parameters, name="dft_u_parameters", curie=CATCORE.curie('dft_u_parameters'),
                   model_uri=CATCORE.dft_u_parameters, domain=None, range=Optional[Union[str, list[str]]])

slots.spin_polarization = Slot(uri=CATCORE.spin_polarization, name="spin_polarization", curie=CATCORE.curie('spin_polarization'),
                   model_uri=CATCORE.spin_polarization, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.total_energy_per_atom = Slot(uri=CATCORE.total_energy_per_atom, name="total_energy_per_atom", curie=CATCORE.curie('total_energy_per_atom'),
                   model_uri=CATCORE.total_energy_per_atom, domain=None, range=Optional[Union[float, list[float]]])

slots.force_field = Slot(uri=CATCORE.force_field, name="force_field", curie=CATCORE.curie('force_field'),
                   model_uri=CATCORE.force_field, domain=None, range=Optional[Union[str, list[str]]])

slots.simulation_timestep = Slot(uri=APOLLO_SV['00000012'], name="simulation_timestep", curie=APOLLO_SV.curie('00000012'),
                   model_uri=CATCORE.simulation_timestep, domain=None, range=Optional[Union[float, list[float]]])

slots.simulation_time = Slot(uri=CATCORE.simulation_time, name="simulation_time", curie=CATCORE.curie('simulation_time'),
                   model_uri=CATCORE.simulation_time, domain=None, range=Optional[Union[float, list[float]]])

slots.ensemble_type = Slot(uri=CATCORE.ensemble_type, name="ensemble_type", curie=CATCORE.curie('ensemble_type'),
                   model_uri=CATCORE.ensemble_type, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_atoms = Slot(uri=CATCORE.number_of_atoms, name="number_of_atoms", curie=CATCORE.curie('number_of_atoms'),
                   model_uri=CATCORE.number_of_atoms, domain=None, range=Optional[Union[int, list[int]]])

slots.rate_constants = Slot(uri=NCIT.C94967, name="rate_constants", curie=NCIT.curie('C94967'),
                   model_uri=CATCORE.rate_constants, domain=None, range=Optional[Union[str, list[str]]])

slots.solver_type = Slot(uri=CATCORE.solver_type, name="solver_type", curie=CATCORE.curie('solver_type'),
                   model_uri=CATCORE.solver_type, domain=None, range=Optional[Union[str, list[str]]])

slots.pressure = Slot(uri=CATCORE.pressure, name="pressure", curie=CATCORE.curie('pressure'),
                   model_uri=CATCORE.pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_coverage = Slot(uri=CATCORE.surface_coverage, name="surface_coverage", curie=CATCORE.curie('surface_coverage'),
                   model_uri=CATCORE.surface_coverage, domain=None, range=Optional[Union[float, list[float]]])

slots.activation_energy = Slot(uri=CATCORE.activation_energy, name="activation_energy", curie=CATCORE.curie('activation_energy'),
                   model_uri=CATCORE.activation_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.interaction_potential = Slot(uri=CATCORE.interaction_potential, name="interaction_potential", curie=CATCORE.curie('interaction_potential'),
                   model_uri=CATCORE.interaction_potential, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_steps = Slot(uri=CATCORE.number_of_steps, name="number_of_steps", curie=CATCORE.curie('number_of_steps'),
                   model_uri=CATCORE.number_of_steps, domain=None, range=Optional[Union[int, list[int]]])

slots.lattice_size_type = Slot(uri=CATCORE.lattice_size_type, name="lattice_size_type", curie=CATCORE.curie('lattice_size_type'),
                   model_uri=CATCORE.lattice_size_type, domain=None, range=Optional[Union[str, list[str]]])

slots.acceptance_criteria = Slot(uri=CATCORE.acceptance_criteria, name="acceptance_criteria", curie=CATCORE.curie('acceptance_criteria'),
                   model_uri=CATCORE.acceptance_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.equilibration_steps = Slot(uri=CATCORE.equilibration_steps, name="equilibration_steps", curie=CATCORE.curie('equilibration_steps'),
                   model_uri=CATCORE.equilibration_steps, domain=None, range=Optional[Union[int, list[int]]])

slots.sampling_interval = Slot(uri=CATCORE.sampling_interval, name="sampling_interval", curie=CATCORE.curie('sampling_interval'),
                   model_uri=CATCORE.sampling_interval, domain=None, range=Optional[Union[int, list[int]]])

slots.material_composition = Slot(uri=CATCORE.material_composition, name="material_composition", curie=CATCORE.curie('material_composition'),
                   model_uri=CATCORE.material_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.crystal_structure = Slot(uri=SIO['001100'], name="crystal_structure", curie=SIO.curie('001100'),
                   model_uri=CATCORE.crystal_structure, domain=None, range=Optional[Union[str, list[str]]])

slots.k_point_mesh = Slot(uri=CATCORE.k_point_mesh, name="k_point_mesh", curie=CATCORE.curie('k_point_mesh'),
                   model_uri=CATCORE.k_point_mesh, domain=None, range=Optional[Union[str, list[str]]])

slots.formation_energy = Slot(uri=CATCORE.formation_energy, name="formation_energy", curie=CATCORE.curie('formation_energy'),
                   model_uri=CATCORE.formation_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.reference_energies = Slot(uri=CATCORE.reference_energies, name="reference_energies", curie=CATCORE.curie('reference_energies'),
                   model_uri=CATCORE.reference_energies, domain=None, range=Optional[Union[str, list[str]]])

slots.energy_above_hull = Slot(uri=CATCORE.energy_above_hull, name="energy_above_hull", curie=CATCORE.curie('energy_above_hull'),
                   model_uri=CATCORE.energy_above_hull, domain=None, range=Optional[Union[float, list[float]]])

slots.phase_diagram_type = Slot(uri=CATCORE.phase_diagram_type, name="phase_diagram_type", curie=CATCORE.curie('phase_diagram_type'),
                   model_uri=CATCORE.phase_diagram_type, domain=None, range=Optional[Union[str, list[str]]])

slots.competing_phases = Slot(uri=CATCORE.competing_phases, name="competing_phases", curie=CATCORE.curie('competing_phases'),
                   model_uri=CATCORE.competing_phases, domain=None, range=Optional[Union[str, list[str]]])

slots.piezoelectric_tensor = Slot(uri=CATCORE.piezoelectric_tensor, name="piezoelectric_tensor", curie=CATCORE.curie('piezoelectric_tensor'),
                   model_uri=CATCORE.piezoelectric_tensor, domain=None, range=Optional[Union[str, list[str]]])

slots.crystal_symmetry = Slot(uri=CATCORE.crystal_symmetry, name="crystal_symmetry", curie=CATCORE.curie('crystal_symmetry'),
                   model_uri=CATCORE.crystal_symmetry, domain=None, range=Optional[Union[str, list[str]]])

slots.strain_applied = Slot(uri=CATCORE.strain_applied, name="strain_applied", curie=CATCORE.curie('strain_applied'),
                   model_uri=CATCORE.strain_applied, domain=None, range=Optional[Union[float, list[float]]])

slots.ionic_electronic_contributions = Slot(uri=CATCORE.ionic_electronic_contributions, name="ionic_electronic_contributions", curie=CATCORE.curie('ionic_electronic_contributions'),
                   model_uri=CATCORE.ionic_electronic_contributions, domain=None, range=Optional[Union[str, list[str]]])

slots.elastic_tensor = Slot(uri=CATCORE.elastic_tensor, name="elastic_tensor", curie=CATCORE.curie('elastic_tensor'),
                   model_uri=CATCORE.elastic_tensor, domain=None, range=Optional[Union[str, list[str]]])

slots.bulk_modulus = Slot(uri=CATCORE.bulk_modulus, name="bulk_modulus", curie=CATCORE.curie('bulk_modulus'),
                   model_uri=CATCORE.bulk_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.shear_modulus = Slot(uri=CATCORE.shear_modulus, name="shear_modulus", curie=CATCORE.curie('shear_modulus'),
                   model_uri=CATCORE.shear_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.poisson_ratio = Slot(uri=CATCORE.poisson_ratio, name="poisson_ratio", curie=CATCORE.curie('poisson_ratio'),
                   model_uri=CATCORE.poisson_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.young_modulus = Slot(uri=CATCORE.young_modulus, name="young_modulus", curie=CATCORE.curie('young_modulus'),
                   model_uri=CATCORE.young_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_energy = Slot(uri=CATCORE.surface_energy, name="surface_energy", curie=CATCORE.curie('surface_energy'),
                   model_uri=CATCORE.surface_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.miller_indices = Slot(uri=CATCORE.miller_indices, name="miller_indices", curie=CATCORE.curie('miller_indices'),
                   model_uri=CATCORE.miller_indices, domain=None, range=Optional[Union[str, list[str]]])

slots.slab_thickness = Slot(uri=CATCORE.slab_thickness, name="slab_thickness", curie=CATCORE.curie('slab_thickness'),
                   model_uri=CATCORE.slab_thickness, domain=None, range=Optional[Union[float, list[float]]])

slots.vacuum_spacing = Slot(uri=CATCORE.vacuum_spacing, name="vacuum_spacing", curie=CATCORE.curie('vacuum_spacing'),
                   model_uri=CATCORE.vacuum_spacing, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_termination_method = Slot(uri=CATCORE.surface_termination_method, name="surface_termination_method", curie=CATCORE.curie('surface_termination_method'),
                   model_uri=CATCORE.surface_termination_method, domain=None, range=Optional[Union[str, list[str]]])

slots.dielectric_tensor = Slot(uri=CATCORE.dielectric_tensor, name="dielectric_tensor", curie=CATCORE.curie('dielectric_tensor'),
                   model_uri=CATCORE.dielectric_tensor, domain=None, range=Optional[Union[str, list[str]]])

slots.born_effective_charges = Slot(uri=CATCORE.born_effective_charges, name="born_effective_charges", curie=CATCORE.curie('born_effective_charges'),
                   model_uri=CATCORE.born_effective_charges, domain=None, range=Optional[Union[str, list[str]]])

slots.force_constant_method = Slot(uri=CATCORE.force_constant_method, name="force_constant_method", curie=CATCORE.curie('force_constant_method'),
                   model_uri=CATCORE.force_constant_method, domain=None, range=Optional[Union[str, list[str]]])

slots.kq_point_mesh = Slot(uri=CATCORE.kq_point_mesh, name="kq_point_mesh", curie=CATCORE.curie('kq_point_mesh'),
                   model_uri=CATCORE.kq_point_mesh, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_parameter = Slot(uri=CATCORE.smearing_parameter, name="smearing_parameter", curie=CATCORE.curie('smearing_parameter'),
                   model_uri=CATCORE.smearing_parameter, domain=None, range=Optional[Union[float, list[float]]])

slots.imaginary_modes = Slot(uri=CATCORE.imaginary_modes, name="imaginary_modes", curie=CATCORE.curie('imaginary_modes'),
                   model_uri=CATCORE.imaginary_modes, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.fit_method = Slot(uri=CATCORE.fit_method, name="fit_method", curie=CATCORE.curie('fit_method'),
                   model_uri=CATCORE.fit_method, domain=None, range=Optional[Union[str, list[str]]])

slots.pressure_derivative = Slot(uri=CATCORE.pressure_derivative, name="pressure_derivative", curie=CATCORE.curie('pressure_derivative'),
                   model_uri=CATCORE.pressure_derivative, domain=None, range=Optional[Union[float, list[float]]])

slots.fit_residuals = Slot(uri=CATCORE.fit_residuals, name="fit_residuals", curie=CATCORE.curie('fit_residuals'),
                   model_uri=CATCORE.fit_residuals, domain=None, range=Optional[Union[float, list[float]]])

slots.ph_range = Slot(uri=CATCORE.ph_range, name="ph_range", curie=CATCORE.curie('ph_range'),
                   model_uri=CATCORE.ph_range, domain=None, range=Optional[Union[str, list[str]]])

slots.potential_range = Slot(uri=CATCORE.potential_range, name="potential_range", curie=CATCORE.curie('potential_range'),
                   model_uri=CATCORE.potential_range, domain=None, range=Optional[Union[str, list[str]]])

slots.solvation_model = Slot(uri=CATCORE.solvation_model, name="solvation_model", curie=CATCORE.curie('solvation_model'),
                   model_uri=CATCORE.solvation_model, domain=None, range=Optional[Union[str, list[str]]])

slots.ionic_strength = Slot(uri=CATCORE.ionic_strength, name="ionic_strength", curie=CATCORE.curie('ionic_strength'),
                   model_uri=CATCORE.ionic_strength, domain=None, range=Optional[Union[float, list[float]]])

slots.grain_boundary_plane = Slot(uri=CATCORE.grain_boundary_plane, name="grain_boundary_plane", curie=CATCORE.curie('grain_boundary_plane'),
                   model_uri=CATCORE.grain_boundary_plane, domain=None, range=Optional[Union[str, list[str]]])

slots.misorientation_angle = Slot(uri=CATCORE.misorientation_angle, name="misorientation_angle", curie=CATCORE.curie('misorientation_angle'),
                   model_uri=CATCORE.misorientation_angle, domain=None, range=Optional[Union[float, list[float]]])

slots.grain_boundary_energy = Slot(uri=CATCORE.grain_boundary_energy, name="grain_boundary_energy", curie=CATCORE.curie('grain_boundary_energy'),
                   model_uri=CATCORE.grain_boundary_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.simulation_cell_size = Slot(uri=CATCORE.simulation_cell_size, name="simulation_cell_size", curie=CATCORE.curie('simulation_cell_size'),
                   model_uri=CATCORE.simulation_cell_size, domain=None, range=Optional[Union[str, list[str]]])

slots.gb_excess_volume = Slot(uri=CATCORE.gb_excess_volume, name="gb_excess_volume", curie=CATCORE.curie('gb_excess_volume'),
                   model_uri=CATCORE.gb_excess_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.gb_structural_units = Slot(uri=CATCORE.gb_structural_units, name="gb_structural_units", curie=CATCORE.curie('gb_structural_units'),
                   model_uri=CATCORE.gb_structural_units, domain=None, range=Optional[Union[str, list[str]]])

slots.charge_defect_segregation = Slot(uri=CATCORE.charge_defect_segregation, name="charge_defect_segregation", curie=CATCORE.curie('charge_defect_segregation'),
                   model_uri=CATCORE.charge_defect_segregation, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_method = Slot(uri=CATCORE.smearing_method, name="smearing_method", curie=CATCORE.curie('smearing_method'),
                   model_uri=CATCORE.smearing_method, domain=None, range=Optional[Union[str, list[str]]])

slots.spin_polarized = Slot(uri=CATCORE.spin_polarized, name="spin_polarized", curie=CATCORE.curie('spin_polarized'),
                   model_uri=CATCORE.spin_polarized, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.band_path = Slot(uri=CATCORE.band_path, name="band_path", curie=CATCORE.curie('band_path'),
                   model_uri=CATCORE.band_path, domain=None, range=Optional[Union[str, list[str]]])

slots.fermi_energy = Slot(uri=CATCORE.fermi_energy, name="fermi_energy", curie=CATCORE.curie('fermi_energy'),
                   model_uri=CATCORE.fermi_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.polarization_direction = Slot(uri=CATCORE.polarization_direction, name="polarization_direction", curie=CATCORE.curie('polarization_direction'),
                   model_uri=CATCORE.polarization_direction, domain=None, range=Optional[Union[str, list[str]]])

slots.spontaneous_polarization = Slot(uri=CATCORE.spontaneous_polarization, name="spontaneous_polarization", curie=CATCORE.curie('spontaneous_polarization'),
                   model_uri=CATCORE.spontaneous_polarization, domain=None, range=Optional[Union[float, list[float]]])

slots.reference_structure = Slot(uri=CATCORE.reference_structure, name="reference_structure", curie=CATCORE.curie('reference_structure'),
                   model_uri=CATCORE.reference_structure, domain=None, range=Optional[Union[str, list[str]]])

slots.switching_barrier = Slot(uri=CATCORE.switching_barrier, name="switching_barrier", curie=CATCORE.curie('switching_barrier'),
                   model_uri=CATCORE.switching_barrier, domain=None, range=Optional[Union[float, list[float]]])

slots.coercive_field = Slot(uri=CATCORE.coercive_field, name="coercive_field", curie=CATCORE.curie('coercive_field'),
                   model_uri=CATCORE.coercive_field, domain=None, range=Optional[Union[float, list[float]]])

slots.temperature_dependence = Slot(uri=CATCORE.temperature_dependence, name="temperature_dependence", curie=CATCORE.curie('temperature_dependence'),
                   model_uri=CATCORE.temperature_dependence, domain=None, range=Optional[Union[str, list[str]]])

slots.material_sample = Slot(uri=VOC4CAT['0005056'], name="material_sample", curie=VOC4CAT.curie('0005056'),
                   model_uri=CATCORE.material_sample, domain=None, range=Optional[Union[str, list[str]]])

slots.structure_model = Slot(uri=CATCORE.structure_model, name="structure_model", curie=CATCORE.curie('structure_model'),
                   model_uri=CATCORE.structure_model, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_broadening = Slot(uri=CATCORE.smearing_broadening, name="smearing_broadening", curie=CATCORE.curie('smearing_broadening'),
                   model_uri=CATCORE.smearing_broadening, domain=None, range=Optional[Union[float, list[float]]])

slots.direct_indirect = Slot(uri=CATCORE.direct_indirect, name="direct_indirect", curie=CATCORE.curie('direct_indirect'),
                   model_uri=CATCORE.direct_indirect, domain=None, range=Optional[Union[str, list[str]]])

slots.experimental_reference = Slot(uri=CATCORE.experimental_reference, name="experimental_reference", curie=CATCORE.curie('experimental_reference'),
                   model_uri=CATCORE.experimental_reference, domain=None, range=Optional[Union[float, list[float]]])

slots.gw_hybrid_correction = Slot(uri=CATCORE.gw_hybrid_correction, name="gw_hybrid_correction", curie=CATCORE.curie('gw_hybrid_correction'),
                   model_uri=CATCORE.gw_hybrid_correction, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.excitonic_correction = Slot(uri=CATCORE.excitonic_correction, name="excitonic_correction", curie=CATCORE.curie('excitonic_correction'),
                   model_uri=CATCORE.excitonic_correction, domain=None, range=Optional[Union[float, list[float]]])

slots.access_URL = Slot(uri=DCAT.accessURL, name="access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=CATCORE.access_URL, domain=None, range=Optional[str])

slots.access_rights = Slot(uri=DCTERMS.accessRights, name="access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=CATCORE.access_rights, domain=None, range=Optional[str])

slots.access_service = Slot(uri=DCAT.accessService, name="access_service", curie=DCAT.curie('accessService'),
                   model_uri=CATCORE.access_service, domain=None, range=Optional[str])

slots.algorithm = Slot(uri=SPDX.algorithm, name="algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=CATCORE.algorithm, domain=None, range=Optional[str])

slots.applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.applicable_legislation, domain=None, range=Optional[str])

slots.application_profile = Slot(uri=DCTERMS.conformsTo, name="application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.application_profile, domain=None, range=Optional[str])

slots.availability = Slot(uri=DCATAP.availability, name="availability", curie=DCATAP.curie('availability'),
                   model_uri=CATCORE.availability, domain=None, range=Optional[str])

slots.bbox = Slot(uri=DCAT.bbox, name="bbox", curie=DCAT.curie('bbox'),
                   model_uri=CATCORE.bbox, domain=None, range=Optional[str])

slots.beginning = Slot(uri=TIME.hasBeginning, name="beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=CATCORE.beginning, domain=None, range=Optional[str])

slots.byte_size = Slot(uri=DCAT.byteSize, name="byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=CATCORE.byte_size, domain=None, range=Optional[str])

slots.carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.carried_out_by, domain=None, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]])

slots.catalogue = Slot(uri=DCAT.catalog, name="catalogue", curie=DCAT.curie('catalog'),
                   model_uri=CATCORE.catalogue, domain=None, range=Optional[str])

slots.centroid = Slot(uri=DCAT.centroid, name="centroid", curie=DCAT.curie('centroid'),
                   model_uri=CATCORE.centroid, domain=None, range=Optional[str])

slots.change_type = Slot(uri=ADMS.status, name="change_type", curie=ADMS.curie('status'),
                   model_uri=CATCORE.change_type, domain=None, range=Optional[str])

slots.checksum = Slot(uri=SPDX.checksum, name="checksum", curie=SPDX.curie('checksum'),
                   model_uri=CATCORE.checksum, domain=None, range=Optional[str])

slots.checksum_value = Slot(uri=SPDX.checksumValue, name="checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=CATCORE.checksum_value, domain=None, range=Optional[str])

slots.compression_format = Slot(uri=DCAT.compressFormat, name="compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=CATCORE.compression_format, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DCTERMS.conformsTo, name="conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.conforms_to, domain=None, range=Optional[str])

slots.contact_point = Slot(uri=DCAT.contactPoint, name="contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=CATCORE.contact_point, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=CATCORE.creator, domain=None, range=Optional[str])

slots.dataset_distribution = Slot(uri=DCAT.distribution, name="dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=CATCORE.dataset_distribution, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.description, domain=None, range=Optional[str])

slots.documentation = Slot(uri=FOAF.page, name="documentation", curie=FOAF.curie('page'),
                   model_uri=CATCORE.documentation, domain=None, range=Optional[str])

slots.download_URL = Slot(uri=DCAT.downloadURL, name="download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=CATCORE.download_URL, domain=None, range=Optional[str])

slots.end = Slot(uri=TIME.hasEnd, name="end", curie=TIME.curie('hasEnd'),
                   model_uri=CATCORE.end, domain=None, range=Optional[str])

slots.end_date = Slot(uri=DCAT.endDate, name="end_date", curie=DCAT.curie('endDate'),
                   model_uri=CATCORE.end_date, domain=None, range=Optional[str])

slots.endpoint_URL = Slot(uri=DCAT.endpointURL, name="endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=CATCORE.endpoint_URL, domain=None, range=Optional[str])

slots.endpoint_description = Slot(uri=DCAT.endpointDescription, name="endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=CATCORE.endpoint_description, domain=None, range=Optional[str])

slots.evaluated_activity = Slot(uri=PROV.wasInformedBy, name="evaluated_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=CATCORE.evaluated_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.evaluated_entity = Slot(uri=PROV.used, name="evaluated_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.evaluated_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=CATCORE.format, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=CATCORE.frequency, domain=None, range=Optional[str])

slots.geographical_coverage = Slot(uri=DCTERMS.spatial, name="geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=CATCORE.geographical_coverage, domain=None, range=Optional[str])

slots.geometry = Slot(uri=LOCN.geometry, name="geometry", curie=LOCN.curie('geometry'),
                   model_uri=CATCORE.geometry, domain=None, range=Optional[str])

slots.had_input_activity = Slot(uri=PROV.wasInformedBy, name="had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=CATCORE.had_input_activity, domain=None, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.had_input_entity = Slot(uri=PROV.used, name="had_input_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.had_input_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_output_entity = Slot(uri=PROV.generated, name="had_output_entity", curie=PROV.curie('generated'),
                   model_uri=CATCORE.had_output_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_role = Slot(uri=DCAT.hadRole, name="had_role", curie=DCAT.curie('hadRole'),
                   model_uri=CATCORE.had_role, domain=None, range=Optional[str])

slots.has_dataset = Slot(uri=DCAT.dataset, name="has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=CATCORE.has_dataset, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DCTERMS.hasPart, name="has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.has_part, domain=None, range=Optional[Union[str, ActivityId]])

slots.has_policy = Slot(uri=ODRL.hasPolicy, name="has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=CATCORE.has_policy, domain=None, range=Optional[str])

slots.has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.has_qualitative_attribute, domain=None, range=Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]])

slots.has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.has_quantitative_attribute, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.has_version = Slot(uri=DCAT.hasVersion, name="has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=CATCORE.has_version, domain=None, range=Optional[str])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=CATCORE.homepage, domain=None, range=Optional[str])

slots.id = Slot(uri=DCATAP_PLUS.id, name="id", curie=DCATAP_PLUS.curie('id'),
                   model_uri=CATCORE.id, domain=None, range=URIRef)

slots.identifier = Slot(uri=DCTERMS.identifier, name="identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=CATCORE.identifier, domain=None, range=Optional[str])

slots.in_series = Slot(uri=DCAT.inSeries, name="in_series", curie=DCAT.curie('inSeries'),
                   model_uri=CATCORE.in_series, domain=None, range=Optional[str])

slots.is_about_activity = Slot(uri=DCTERMS.subject, name="is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=CATCORE.is_about_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.is_about_entity = Slot(uri=DCTERMS.subject, name="is_about_entity", curie=DCTERMS.curie('subject'),
                   model_uri=CATCORE.is_about_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=CATCORE.is_referenced_by, domain=None, range=Optional[str])

slots.keyword = Slot(uri=DCAT.keyword, name="keyword", curie=DCAT.curie('keyword'),
                   model_uri=CATCORE.keyword, domain=None, range=Optional[str])

slots.landing_page = Slot(uri=DCAT.landingPage, name="landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=CATCORE.landing_page, domain=None, range=Optional[str])

slots.language = Slot(uri=DCTERMS.language, name="language", curie=DCTERMS.curie('language'),
                   model_uri=CATCORE.language, domain=None, range=Optional[str])

slots.licence = Slot(uri=DCTERMS.license, name="licence", curie=DCTERMS.curie('license'),
                   model_uri=CATCORE.licence, domain=None, range=Optional[str])

slots.linked_schemas = Slot(uri=DCTERMS.conformsTo, name="linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.linked_schemas, domain=None, range=Optional[str])

slots.listing_date = Slot(uri=DCTERMS.issued, name="listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.listing_date, domain=None, range=Optional[str])

slots.media_type = Slot(uri=DCAT.mediaType, name="media_type", curie=DCAT.curie('mediaType'),
                   model_uri=CATCORE.media_type, domain=None, range=Optional[str])

slots.modification_date = Slot(uri=DCTERMS.modified, name="modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.modification_date, domain=None, range=Optional[str])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=CATCORE.name, domain=None, range=Optional[str])

slots.notation = Slot(uri=SKOS.notation, name="notation", curie=SKOS.curie('notation'),
                   model_uri=CATCORE.notation, domain=None, range=Optional[str])

slots.occurred_in = Slot(uri=PROV.atLocation, name="occurred_in", curie=PROV.curie('atLocation'),
                   model_uri=CATCORE.occurred_in, domain=None, range=Optional[Union[dict, Surrounding]])

slots.other_identifier = Slot(uri=ADMS.identifier, name="other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.other_identifier, domain=None, range=Optional[str])

slots.packaging_format = Slot(uri=DCAT.packageFormat, name="packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=CATCORE.packaging_format, domain=None, range=Optional[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=CATCORE.part_of, domain=None, range=Optional[Union[str, ActivityId]])

slots.preferred_label = Slot(uri=SKOS.prefLabel, name="preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=CATCORE.preferred_label, domain=None, range=Optional[str])

slots.primary_topic = Slot(uri=FOAF.primaryTopic, name="primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=CATCORE.primary_topic, domain=None, range=Optional[str])

slots.provenance = Slot(uri=DCTERMS.provenance, name="provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=CATCORE.provenance, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=CATCORE.publisher, domain=None, range=Optional[str])

slots.qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=CATCORE.qualified_attribution, domain=None, range=Optional[str])

slots.qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=CATCORE.qualified_relation, domain=None, range=Optional[str])

slots.rdf_type = Slot(uri=RDF.type, name="rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.rdf_type, domain=None, range=Optional[Union[dict, DefinedTerm]])

slots.realized_plan = Slot(uri=PROV.used, name="realized_plan", curie=PROV.curie('used'),
                   model_uri=CATCORE.realized_plan, domain=None, range=Optional[Union[dict, Plan]])

slots.record = Slot(uri=DCAT.record, name="record", curie=DCAT.curie('record'),
                   model_uri=CATCORE.record, domain=None, range=Optional[str])

slots.related_resource = Slot(uri=DCTERMS.relation, name="related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.related_resource, domain=None, range=Optional[str])

slots.relation = Slot(uri=DCTERMS.relation, name="relation", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.relation, domain=None, range=Optional[str])

slots.release_date = Slot(uri=DCTERMS.issued, name="release_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.release_date, domain=None, range=Optional[str])

slots.rights = Slot(uri=DCTERMS.rights, name="rights", curie=DCTERMS.curie('rights'),
                   model_uri=CATCORE.rights, domain=None, range=Optional[str])

slots.sample = Slot(uri=ADMS.sample, name="sample", curie=ADMS.curie('sample'),
                   model_uri=CATCORE.sample, domain=None, range=Optional[str])

slots.serves_dataset = Slot(uri=DCAT.servesDataset, name="serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=CATCORE.serves_dataset, domain=None, range=Optional[str])

slots.service = Slot(uri=DCAT.service, name="service", curie=DCAT.curie('service'),
                   model_uri=CATCORE.service, domain=None, range=Optional[str])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=CATCORE.source, domain=None, range=Optional[str])

slots.source_metadata = Slot(uri=DCTERMS.source, name="source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=CATCORE.source_metadata, domain=None, range=Optional[str])

slots.spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=CATCORE.spatial_resolution, domain=None, range=Optional[str])

slots.start_date = Slot(uri=DCAT.startDate, name="start_date", curie=DCAT.curie('startDate'),
                   model_uri=CATCORE.start_date, domain=None, range=Optional[str])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=CATCORE.status, domain=None, range=Optional[str])

slots.temporal_coverage = Slot(uri=DCTERMS.temporal, name="temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=CATCORE.temporal_coverage, domain=None, range=Optional[str])

slots.temporal_resolution = Slot(uri=DCAT.temporalResolution, name="temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=CATCORE.temporal_resolution, domain=None, range=Optional[str])

slots.theme = Slot(uri=DCAT.theme, name="theme", curie=DCAT.curie('theme'),
                   model_uri=CATCORE.theme, domain=None, range=Optional[str])

slots.themes = Slot(uri=DCAT.themeTaxonomy, name="themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=CATCORE.themes, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.title, domain=None, range=Optional[str])

slots.type = Slot(uri=DCTERMS.type, name="type", curie=DCTERMS.curie('type'),
                   model_uri=CATCORE.type, domain=None, range=Optional[str])

slots.value = Slot(uri=PROV.value, name="value", curie=PROV.curie('value'),
                   model_uri=CATCORE.value, domain=None, range=Optional[str])

slots.version = Slot(uri=DCAT.version, name="version", curie=DCAT.curie('version'),
                   model_uri=CATCORE.version, domain=None, range=Optional[str])

slots.version_notes = Slot(uri=ADMS.versionNotes, name="version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=CATCORE.version_notes, domain=None, range=Optional[str])

slots.was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.was_generated_by, domain=None, range=Optional[str])

slots.composed_of = Slot(uri=BFO['0000051'], name="composed_of", curie=BFO.curie('0000051'),
                   model_uri=CATCORE.composed_of, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.has_concentration = Slot(uri=SIO['000008'], name="has_concentration", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_concentration, domain=None, range=Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]])

slots.has_amount = Slot(uri=SIO['000008'], name="has_amount", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_amount, domain=None, range=Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]])

slots.has_ph_value = Slot(uri=SIO['000008'], name="has_ph_value", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_ph_value, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.inchi = Slot(uri=SIO['000008'], name="inchi", curie=SIO.curie('000008'),
                   model_uri=CATCORE.inchi, domain=None, range=Optional[Union[Union[dict, InChi], list[Union[dict, InChi]]]])

slots.inchikey = Slot(uri=SIO['000008'], name="inchikey", curie=SIO.curie('000008'),
                   model_uri=CATCORE.inchikey, domain=None, range=Optional[Union[Union[dict, InChIKey], list[Union[dict, InChIKey]]]])

slots.smiles = Slot(uri=SIO['000008'], name="smiles", curie=SIO.curie('000008'),
                   model_uri=CATCORE.smiles, domain=None, range=Optional[Union[Union[dict, SMILES], list[Union[dict, SMILES]]]])

slots.molecular_formula = Slot(uri=SIO['000008'], name="molecular_formula", curie=SIO.curie('000008'),
                   model_uri=CATCORE.molecular_formula, domain=None, range=Optional[Union[Union[dict, MolecularFormula], list[Union[dict, MolecularFormula]]]])

slots.iupac_name = Slot(uri=SIO['000008'], name="iupac_name", curie=SIO.curie('000008'),
                   model_uri=CATCORE.iupac_name, domain=None, range=Optional[Union[Union[dict, IUPACName], list[Union[dict, IUPACName]]]])

slots.has_molar_mass = Slot(uri=SIO['000008'], name="has_molar_mass", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_molar_mass, domain=None, range=Optional[Union[Union[dict, MolarMass], list[Union[dict, MolarMass]]]])

slots.used_starting_material = Slot(uri=RO['0004009'], name="used_starting_material", curie=RO.curie('0004009'),
                   model_uri=CATCORE.used_starting_material, domain=None, range=Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, StartingMaterial]], list[Union[dict, StartingMaterial]]]])

slots.used_reactant = Slot(uri=RO['0004009'], name="used_reactant", curie=RO.curie('0004009'),
                   model_uri=CATCORE.used_reactant, domain=None, range=Optional[Union[dict[Union[str, ReagentId], Union[dict, Reagent]], list[Union[dict, Reagent]]]])

slots.generated_product = Slot(uri=RO['0004008'], name="generated_product", curie=RO.curie('0004008'),
                   model_uri=CATCORE.generated_product, domain=None, range=Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, ChemicalProduct]], list[Union[dict, ChemicalProduct]]]])

slots.used_catalyst = Slot(uri=RXNO['0000425'], name="used_catalyst", curie=RXNO.curie('0000425'),
                   model_uri=CATCORE.used_catalyst, domain=None, range=Optional[Union[dict[Union[str, CatalystId], Union[dict, Catalyst]], list[Union[dict, Catalyst]]]])

slots.used_solvent = Slot(uri=PROV.wasAssociatedWith, name="used_solvent", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.used_solvent, domain=None, range=Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, DissolvingSubstance]], list[Union[dict, DissolvingSubstance]]]])

slots.has_duration = Slot(uri=SCHEMA.duration, name="has_duration", curie=SCHEMA.curie('duration'),
                   model_uri=CATCORE.has_duration, domain=None, range=Optional[str])

slots.used_reactor = Slot(uri=PROV.wasAssociatedWith, name="used_reactor", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.used_reactor, domain=None, range=Optional[Union[dict[Union[str, ReactorId], Union[dict, Reactor]], list[Union[dict, Reactor]]]])

slots.has_yield = Slot(uri=SIO['000008'], name="has_yield", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_yield, domain=None, range=Optional[Union[Union[dict, Yield], list[Union[dict, Yield]]]])

slots.has_molar_equivalent = Slot(uri=SIO['000008'], name="has_molar_equivalent", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_molar_equivalent, domain=None, range=Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]])

slots.has_percentage_of_total = Slot(uri=SIO['000008'], name="has_percentage_of_total", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_percentage_of_total, domain=None, range=Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]])

slots.has_reaction_step = Slot(uri=BFO['0000051'], name="has_reaction_step", curie=BFO.curie('0000051'),
                   model_uri=CATCORE.has_reaction_step, domain=None, range=Optional[Union[str, ChemicalReactionId]])

slots.alternative_label = Slot(uri=SKOS.altLabel, name="alternative_label", curie=SKOS.curie('altLabel'),
                   model_uri=CATCORE.alternative_label, domain=None, range=Optional[str])

slots.has_physical_state = Slot(uri=SIO['000008'], name="has_physical_state", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_physical_state, domain=None, range=Optional[Union[str, "PhysicalStateEnum"]])

slots.has_temperature = Slot(uri=SIO['000008'], name="has_temperature", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_temperature, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_mass = Slot(uri=SIO['000008'], name="has_mass", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_mass, domain=None, range=Optional[Union[Union[dict, Mass], list[Union[dict, Mass]]]])

slots.has_volume = Slot(uri=SIO['000008'], name="has_volume", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.has_density = Slot(uri=SIO['000008'], name="has_density", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_density, domain=None, range=Optional[Union[Union[dict, Density], list[Union[dict, Density]]]])

slots.has_pressure = Slot(uri=SIO['000008'], name="has_pressure", curie=SIO.curie('000008'),
                   model_uri=CATCORE.has_pressure, domain=None, range=Optional[Union[Union[dict, Pressure], list[Union[dict, Pressure]]]])

slots.derived_from = Slot(uri=PROV.wasDerivedFrom, name="derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=CATCORE.derived_from, domain=None, range=Optional[Union[dict, Entity]])

slots.definedTerm__from_CV = Slot(uri=SCHEMA.inDefinedTermSet, name="definedTerm__from_CV", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=CATCORE.definedTerm__from_CV, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.quantitativeAttribute__has_quantity_type = Slot(uri=QUDT.hasQuantityKind, name="quantitativeAttribute__has_quantity_type", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CATCORE.quantitativeAttribute__has_quantity_type, domain=None, range=Union[str, DefinedTermId])

slots.quantitativeAttribute__unit = Slot(uri=QUDT.unit, name="quantitativeAttribute__unit", curie=QUDT.curie('unit'),
                   model_uri=CATCORE.quantitativeAttribute__unit, domain=None, range=Optional[Union[str, DefinedTermId]])

slots.product_identification_method = Slot(uri=CATCORE.product_identification_method, name="product_identification_method", curie=CATCORE.curie('product_identification_method'),
                   model_uri=CATCORE.product_identification_method, domain=None, range=Union[Union[dict, ProductIdentificationMethod], list[Union[dict, ProductIdentificationMethod]]])

slots.CatalysisDataset_rdf_type = Slot(uri=RDF.type, name="CatalysisDataset_rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.CatalysisDataset_rdf_type, domain=CatalysisDataset, range=Optional[Union[dict, "DefinedTerm"]])

slots.CatalysisDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="CatalysisDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.CatalysisDataset_was_generated_by, domain=CatalysisDataset, range=Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]])

slots.CatalysisDataset_is_about_activity = Slot(uri=DCTERMS.subject, name="CatalysisDataset_is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=CATCORE.CatalysisDataset_is_about_activity, domain=CatalysisDataset, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]])

slots.CatalysisDataset_is_about_entity = Slot(uri=DCTERMS.subject, name="CatalysisDataset_is_about_entity", curie=DCTERMS.curie('subject'),
                   model_uri=CATCORE.CatalysisDataset_is_about_entity, domain=CatalysisDataset, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]])

slots.Synthesis_nominal_composition = Slot(uri=CATCORE.nominal_composition, name="Synthesis_nominal_composition", curie=CATCORE.curie('nominal_composition'),
                   model_uri=CATCORE.Synthesis_nominal_composition, domain=Synthesis, range=Union[str, list[str]])

slots.Synthesis_catalyst_measured_properties = Slot(uri=CATCORE.catalyst_measured_properties, name="Synthesis_catalyst_measured_properties", curie=CATCORE.curie('catalyst_measured_properties'),
                   model_uri=CATCORE.Synthesis_catalyst_measured_properties, domain=Synthesis, range=Union[str, list[str]])

slots.Synthesis_had_input_entity = Slot(uri=PROV.used, name="Synthesis_had_input_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.Synthesis_had_input_entity, domain=Synthesis, range=Union[dict[Union[str, PrecursorId], Union[dict, "Precursor"]], list[Union[dict, "Precursor"]]])

slots.Synthesis_had_output_entity = Slot(uri=PROV.generated, name="Synthesis_had_output_entity", curie=PROV.curie('generated'),
                   model_uri=CATCORE.Synthesis_had_output_entity, domain=Synthesis, range=Optional[Union[dict[Union[str, CatalystSampleId], Union[dict, "CatalystSample"]], list[Union[dict, "CatalystSample"]]]])

slots.Synthesis_realized_plan = Slot(uri=PROV.used, name="Synthesis_realized_plan", curie=PROV.curie('used'),
                   model_uri=CATCORE.Synthesis_realized_plan, domain=Synthesis, range=Union[dict, "PreparationMethod"])

slots.Synthesis_storage_conditions = Slot(uri=CATCORE.storage_conditions, name="Synthesis_storage_conditions", curie=CATCORE.curie('storage_conditions'),
                   model_uri=CATCORE.Synthesis_storage_conditions, domain=Synthesis, range=Optional[Union[str, list[str]]])

slots.Precursor_precursor_quantity = Slot(uri=CATCORE.precursor_quantity, name="Precursor_precursor_quantity", curie=CATCORE.curie('precursor_quantity'),
                   model_uri=CATCORE.Precursor_precursor_quantity, domain=Precursor, range=Union[float, list[float]])

slots.CatalystSample_derived_from = Slot(uri=PROV.wasDerivedFrom, name="CatalystSample_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=CATCORE.CatalystSample_derived_from, domain=CatalystSample, range=Optional[Union[dict, MaterialSample]])

slots.Characterization_equipment = Slot(uri=VOC4CAT['0000187'], name="Characterization_equipment", curie=VOC4CAT.curie('0000187'),
                   model_uri=CATCORE.Characterization_equipment, domain=Characterization, range=Union[str, list[str]])

slots.Characterization_evaluated_entity = Slot(uri=PROV.used, name="Characterization_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.Characterization_evaluated_entity, domain=Characterization, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]])

slots.Characterization_realized_plan = Slot(uri=PROV.used, name="Characterization_realized_plan", curie=PROV.curie('used'),
                   model_uri=CATCORE.Characterization_realized_plan, domain=Characterization, range=Union[dict, "CharacterizationTechnique"])

slots.Characterization_rdf_type = Slot(uri=RDF.type, name="Characterization_rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.Characterization_rdf_type, domain=Characterization, range=Optional[Union[dict, "DefinedTerm"]])

slots.Reaction_rdf_type = Slot(uri=RDF.type, name="Reaction_rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.Reaction_rdf_type, domain=Reaction, range=Optional[Union[dict, DefinedTerm]])

slots.Reaction_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="Reaction_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.Reaction_carried_out_by, domain=Reaction, range=Union[dict[Union[str, ReactorDesignTypeId], Union[dict, ReactorDesignType]], list[Union[dict, ReactorDesignType]]])

slots.Reaction_had_input_entity = Slot(uri=PROV.used, name="Reaction_had_input_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.Reaction_had_input_entity, domain=Reaction, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]])

slots.Reaction_product_identification_method = Slot(uri=CATCORE.product_identification_method, name="Reaction_product_identification_method", curie=CATCORE.curie('product_identification_method'),
                   model_uri=CATCORE.Reaction_product_identification_method, domain=Reaction, range=Union[Union[dict, "ProductIdentificationMethod"], list[Union[dict, "ProductIdentificationMethod"]]])

slots.Simulation_rdf_type = Slot(uri=RDF.type, name="Simulation_rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.Simulation_rdf_type, domain=Simulation, range=Optional[Union[dict, "DefinedTerm"]])

slots.Simulation_realized_plan = Slot(uri=PROV.used, name="Simulation_realized_plan", curie=PROV.curie('used'),
                   model_uri=CATCORE.Simulation_realized_plan, domain=Simulation, range=Union[Union[dict, "SimulationMethod"], list[Union[dict, "SimulationMethod"]]])

slots.Simulation_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="Simulation_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.Simulation_carried_out_by, domain=Simulation, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]])

slots.Simulation_evaluated_entity = Slot(uri=PROV.used, name="Simulation_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.Simulation_evaluated_entity, domain=Simulation, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]])

slots.Activity_title = Slot(uri=DCTERMS.title, name="Activity_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.Activity_title, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_description = Slot(uri=DCTERMS.description, name="Activity_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.Activity_description, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_has_part = Slot(uri=DCTERMS.hasPart, name="Activity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.Activity_has_part, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_part_of = Slot(uri=DCTERMS.isPartOf, name="Activity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=CATCORE.Activity_part_of, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_other_identifier = Slot(uri=ADMS.identifier, name="Activity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.Activity_other_identifier, domain=Activity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Activity_has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.Activity_has_qualitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]])

slots.Activity_has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.Activity_has_quantitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]])

slots.Activity_had_input_entity = Slot(uri=PROV.used, name="Activity_had_input_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.Activity_had_input_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_output_entity = Slot(uri=PROV.generated, name="Activity_had_output_entity", curie=PROV.curie('generated'),
                   model_uri=CATCORE.Activity_had_output_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_input_activity = Slot(uri=PROV.wasInformedBy, name="Activity_had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=CATCORE.Activity_had_input_activity, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="Activity_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=CATCORE.Activity_carried_out_by, domain=Activity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.Agent_name = Slot(uri=FOAF.name, name="Agent_name", curie=FOAF.curie('name'),
                   model_uri=CATCORE.Agent_name, domain=Agent, range=Union[str, list[str]])

slots.Agent_type = Slot(uri=DCTERMS.type, name="Agent_type", curie=DCTERMS.curie('type'),
                   model_uri=CATCORE.Agent_type, domain=Agent, range=Optional[Union[dict, "Concept"]])

slots.AgenticEntity_has_part = Slot(uri=DCTERMS.hasPart, name="AgenticEntity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.AgenticEntity_has_part, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_part_of = Slot(uri=DCTERMS.isPartOf, name="AgenticEntity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=CATCORE.AgenticEntity_part_of, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_other_identifier = Slot(uri=ADMS.identifier, name="AgenticEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.AgenticEntity_other_identifier, domain=AgenticEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.AnalysisDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.AnalysisDataset_was_generated_by, domain=AnalysisDataset, range=Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]])

slots.AnalysisSourceData_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisSourceData_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.AnalysisSourceData_was_generated_by, domain=AnalysisSourceData, range=Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]])

slots.Catalogue_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Catalogue_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.Catalogue_applicable_legislation, domain=Catalogue, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Catalogue_catalogue = Slot(uri=DCAT.catalog, name="Catalogue_catalogue", curie=DCAT.curie('catalog'),
                   model_uri=CATCORE.Catalogue_catalogue, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_creator = Slot(uri=DCTERMS.creator, name="Catalogue_creator", curie=DCTERMS.curie('creator'),
                   model_uri=CATCORE.Catalogue_creator, domain=Catalogue, range=Optional[Union[dict, Agent]])

slots.Catalogue_description = Slot(uri=DCTERMS.description, name="Catalogue_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.Catalogue_description, domain=Catalogue, range=Union[str, list[str]])

slots.Catalogue_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Catalogue_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=CATCORE.Catalogue_geographical_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Catalogue_has_dataset = Slot(uri=DCAT.dataset, name="Catalogue_has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=CATCORE.Catalogue_has_dataset, domain=Catalogue, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Catalogue_has_part = Slot(uri=DCTERMS.hasPart, name="Catalogue_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.Catalogue_has_part, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_homepage = Slot(uri=FOAF.homepage, name="Catalogue_homepage", curie=FOAF.curie('homepage'),
                   model_uri=CATCORE.Catalogue_homepage, domain=Catalogue, range=Optional[Union[dict, "Document"]])

slots.Catalogue_language = Slot(uri=DCTERMS.language, name="Catalogue_language", curie=DCTERMS.curie('language'),
                   model_uri=CATCORE.Catalogue_language, domain=Catalogue, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Catalogue_licence = Slot(uri=DCTERMS.license, name="Catalogue_licence", curie=DCTERMS.curie('license'),
                   model_uri=CATCORE.Catalogue_licence, domain=Catalogue, range=Optional[Union[dict, "LicenseDocument"]])

slots.Catalogue_modification_date = Slot(uri=DCTERMS.modified, name="Catalogue_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.Catalogue_modification_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_publisher = Slot(uri=DCTERMS.publisher, name="Catalogue_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=CATCORE.Catalogue_publisher, domain=Catalogue, range=Union[dict, Agent])

slots.Catalogue_record = Slot(uri=DCAT.record, name="Catalogue_record", curie=DCAT.curie('record'),
                   model_uri=CATCORE.Catalogue_record, domain=Catalogue, range=Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]])

slots.Catalogue_release_date = Slot(uri=DCTERMS.issued, name="Catalogue_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.Catalogue_release_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_rights = Slot(uri=DCTERMS.rights, name="Catalogue_rights", curie=DCTERMS.curie('rights'),
                   model_uri=CATCORE.Catalogue_rights, domain=Catalogue, range=Optional[Union[dict, "RightsStatement"]])

slots.Catalogue_service = Slot(uri=DCAT.service, name="Catalogue_service", curie=DCAT.curie('service'),
                   model_uri=CATCORE.Catalogue_service, domain=Catalogue, range=Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]])

slots.Catalogue_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Catalogue_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=CATCORE.Catalogue_temporal_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Catalogue_themes = Slot(uri=DCAT.themeTaxonomy, name="Catalogue_themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=CATCORE.Catalogue_themes, domain=Catalogue, range=Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]])

slots.Catalogue_title = Slot(uri=DCTERMS.title, name="Catalogue_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.Catalogue_title, domain=Catalogue, range=Union[str, list[str]])

slots.CatalogueRecord_application_profile = Slot(uri=DCTERMS.conformsTo, name="CatalogueRecord_application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.CatalogueRecord_application_profile, domain=CatalogueRecord, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.CatalogueRecord_change_type = Slot(uri=ADMS.status, name="CatalogueRecord_change_type", curie=ADMS.curie('status'),
                   model_uri=CATCORE.CatalogueRecord_change_type, domain=CatalogueRecord, range=Optional[Union[dict, "Concept"]])

slots.CatalogueRecord_description = Slot(uri=DCTERMS.description, name="CatalogueRecord_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.CatalogueRecord_description, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.CatalogueRecord_language = Slot(uri=DCTERMS.language, name="CatalogueRecord_language", curie=DCTERMS.curie('language'),
                   model_uri=CATCORE.CatalogueRecord_language, domain=CatalogueRecord, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.CatalogueRecord_listing_date = Slot(uri=DCTERMS.issued, name="CatalogueRecord_listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.CatalogueRecord_listing_date, domain=CatalogueRecord, range=Optional[Union[str, XSDDate]])

slots.CatalogueRecord_modification_date = Slot(uri=DCTERMS.modified, name="CatalogueRecord_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.CatalogueRecord_modification_date, domain=CatalogueRecord, range=Union[str, XSDDate])

slots.CatalogueRecord_primary_topic = Slot(uri=FOAF.primaryTopic, name="CatalogueRecord_primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=CATCORE.CatalogueRecord_primary_topic, domain=CatalogueRecord, range=Union[dict, Any])

slots.CatalogueRecord_source_metadata = Slot(uri=DCTERMS.source, name="CatalogueRecord_source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=CATCORE.CatalogueRecord_source_metadata, domain=CatalogueRecord, range=Optional[Union[dict, "CatalogueRecord"]])

slots.CatalogueRecord_title = Slot(uri=DCTERMS.title, name="CatalogueRecord_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.CatalogueRecord_title, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.Checksum_algorithm = Slot(uri=SPDX.algorithm, name="Checksum_algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=CATCORE.Checksum_algorithm, domain=Checksum, range=Union[dict, "ChecksumAlgorithm"])

slots.Checksum_checksum_value = Slot(uri=SPDX.checksumValue, name="Checksum_checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=CATCORE.Checksum_checksum_value, domain=Checksum, range=str)

slots.ClassifierMixin_type = Slot(uri=DCTERMS.type, name="ClassifierMixin_type", curie=DCTERMS.curie('type'),
                   model_uri=CATCORE.ClassifierMixin_type, domain=None, range=Optional[Union[dict, "DefinedTerm"]])

slots.Concept_preferred_label = Slot(uri=SKOS.prefLabel, name="Concept_preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=CATCORE.Concept_preferred_label, domain=Concept, range=Union[str, list[str]])

slots.ConceptScheme_title = Slot(uri=DCTERMS.title, name="ConceptScheme_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.ConceptScheme_title, domain=ConceptScheme, range=Union[str, list[str]])

slots.DataAnalysis_evaluated_entity = Slot(uri=PROV.used, name="DataAnalysis_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=CATCORE.DataAnalysis_evaluated_entity, domain=DataAnalysis, range=Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]])

slots.DataService_access_rights = Slot(uri=DCTERMS.accessRights, name="DataService_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=CATCORE.DataService_access_rights, domain=DataService, range=Optional[Union[dict, "RightsStatement"]])

slots.DataService_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DataService_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.DataService_applicable_legislation, domain=DataService, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DataService_conforms_to = Slot(uri=DCTERMS.conformsTo, name="DataService_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.DataService_conforms_to, domain=DataService, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.DataService_contact_point = Slot(uri=DCAT.contactPoint, name="DataService_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=CATCORE.DataService_contact_point, domain=DataService, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DataService_description = Slot(uri=DCTERMS.description, name="DataService_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.DataService_description, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_documentation = Slot(uri=FOAF.page, name="DataService_documentation", curie=FOAF.curie('page'),
                   model_uri=CATCORE.DataService_documentation, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_endpoint_URL = Slot(uri=DCAT.endpointURL, name="DataService_endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=CATCORE.DataService_endpoint_URL, domain=DataService, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.DataService_endpoint_description = Slot(uri=DCAT.endpointDescription, name="DataService_endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=CATCORE.DataService_endpoint_description, domain=DataService, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.DataService_format = Slot(uri=DCTERMS.format, name="DataService_format", curie=DCTERMS.curie('format'),
                   model_uri=CATCORE.DataService_format, domain=DataService, range=Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]])

slots.DataService_keyword = Slot(uri=DCAT.keyword, name="DataService_keyword", curie=DCAT.curie('keyword'),
                   model_uri=CATCORE.DataService_keyword, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_landing_page = Slot(uri=DCAT.landingPage, name="DataService_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=CATCORE.DataService_landing_page, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_licence = Slot(uri=DCTERMS.license, name="DataService_licence", curie=DCTERMS.curie('license'),
                   model_uri=CATCORE.DataService_licence, domain=DataService, range=Optional[Union[dict, "LicenseDocument"]])

slots.DataService_publisher = Slot(uri=DCTERMS.publisher, name="DataService_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=CATCORE.DataService_publisher, domain=DataService, range=Optional[Union[dict, Agent]])

slots.DataService_serves_dataset = Slot(uri=DCAT.servesDataset, name="DataService_serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=CATCORE.DataService_serves_dataset, domain=DataService, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.DataService_theme = Slot(uri=DCAT.theme, name="DataService_theme", curie=DCAT.curie('theme'),
                   model_uri=CATCORE.DataService_theme, domain=DataService, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.DataService_title = Slot(uri=DCTERMS.title, name="DataService_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.DataService_title, domain=DataService, range=Union[str, list[str]])

slots.Dataset_access_rights = Slot(uri=DCTERMS.accessRights, name="Dataset_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=CATCORE.Dataset_access_rights, domain=Dataset, range=Optional[Union[dict, "RightsStatement"]])

slots.Dataset_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Dataset_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.Dataset_applicable_legislation, domain=Dataset, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Dataset_conforms_to = Slot(uri=DCTERMS.conformsTo, name="Dataset_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.Dataset_conforms_to, domain=Dataset, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Dataset_contact_point = Slot(uri=DCAT.contactPoint, name="Dataset_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=CATCORE.Dataset_contact_point, domain=Dataset, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.Dataset_creator = Slot(uri=DCTERMS.creator, name="Dataset_creator", curie=DCTERMS.curie('creator'),
                   model_uri=CATCORE.Dataset_creator, domain=Dataset, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.Dataset_dataset_distribution = Slot(uri=DCAT.distribution, name="Dataset_dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=CATCORE.Dataset_dataset_distribution, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_description = Slot(uri=DCTERMS.description, name="Dataset_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.Dataset_description, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_documentation = Slot(uri=FOAF.page, name="Dataset_documentation", curie=FOAF.curie('page'),
                   model_uri=CATCORE.Dataset_documentation, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="Dataset_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=CATCORE.Dataset_frequency, domain=Dataset, range=Optional[Union[dict, "Frequency"]])

slots.Dataset_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Dataset_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=CATCORE.Dataset_geographical_coverage, domain=Dataset, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Dataset_has_version = Slot(uri=DCAT.hasVersion, name="Dataset_has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=CATCORE.Dataset_has_version, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_identifier = Slot(uri=DCTERMS.identifier, name="Dataset_identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=CATCORE.Dataset_identifier, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_in_series = Slot(uri=DCAT.inSeries, name="Dataset_in_series", curie=DCAT.curie('inSeries'),
                   model_uri=CATCORE.Dataset_in_series, domain=Dataset, range=Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]])

slots.Dataset_is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="Dataset_is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=CATCORE.Dataset_is_referenced_by, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_keyword = Slot(uri=DCAT.keyword, name="Dataset_keyword", curie=DCAT.curie('keyword'),
                   model_uri=CATCORE.Dataset_keyword, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_landing_page = Slot(uri=DCAT.landingPage, name="Dataset_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=CATCORE.Dataset_landing_page, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_language = Slot(uri=DCTERMS.language, name="Dataset_language", curie=DCTERMS.curie('language'),
                   model_uri=CATCORE.Dataset_language, domain=Dataset, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Dataset_modification_date = Slot(uri=DCTERMS.modified, name="Dataset_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.Dataset_modification_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_other_identifier = Slot(uri=ADMS.identifier, name="Dataset_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.Dataset_other_identifier, domain=Dataset, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Dataset_provenance = Slot(uri=DCTERMS.provenance, name="Dataset_provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=CATCORE.Dataset_provenance, domain=Dataset, range=Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]])

slots.Dataset_publisher = Slot(uri=DCTERMS.publisher, name="Dataset_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=CATCORE.Dataset_publisher, domain=Dataset, range=Optional[Union[dict, Agent]])

slots.Dataset_qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="Dataset_qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=CATCORE.Dataset_qualified_attribution, domain=Dataset, range=Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]])

slots.Dataset_qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="Dataset_qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=CATCORE.Dataset_qualified_relation, domain=Dataset, range=Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]])

slots.Dataset_related_resource = Slot(uri=DCTERMS.relation, name="Dataset_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.Dataset_related_resource, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_release_date = Slot(uri=DCTERMS.issued, name="Dataset_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.Dataset_release_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_sample = Slot(uri=ADMS.sample, name="Dataset_sample", curie=ADMS.curie('sample'),
                   model_uri=CATCORE.Dataset_sample, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_source = Slot(uri=DCTERMS.source, name="Dataset_source", curie=DCTERMS.curie('source'),
                   model_uri=CATCORE.Dataset_source, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Dataset_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=CATCORE.Dataset_spatial_resolution, domain=Dataset, range=Optional[Decimal])

slots.Dataset_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Dataset_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=CATCORE.Dataset_temporal_coverage, domain=Dataset, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Dataset_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Dataset_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=CATCORE.Dataset_temporal_resolution, domain=Dataset, range=Optional[str])

slots.Dataset_theme = Slot(uri=DCAT.theme, name="Dataset_theme", curie=DCAT.curie('theme'),
                   model_uri=CATCORE.Dataset_theme, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_title = Slot(uri=DCTERMS.title, name="Dataset_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.Dataset_title, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_type = Slot(uri=DCTERMS.type, name="Dataset_type", curie=DCTERMS.curie('type'),
                   model_uri=CATCORE.Dataset_type, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_version = Slot(uri=DCAT.version, name="Dataset_version", curie=DCAT.curie('version'),
                   model_uri=CATCORE.Dataset_version, domain=Dataset, range=Optional[str])

slots.Dataset_version_notes = Slot(uri=ADMS.versionNotes, name="Dataset_version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=CATCORE.Dataset_version_notes, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="Dataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.Dataset_was_generated_by, domain=Dataset, range=Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]])

slots.DatasetSeries_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DatasetSeries_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.DatasetSeries_applicable_legislation, domain=DatasetSeries, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DatasetSeries_contact_point = Slot(uri=DCAT.contactPoint, name="DatasetSeries_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=CATCORE.DatasetSeries_contact_point, domain=DatasetSeries, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DatasetSeries_description = Slot(uri=DCTERMS.description, name="DatasetSeries_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.DatasetSeries_description, domain=DatasetSeries, range=Union[str, list[str]])

slots.DatasetSeries_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="DatasetSeries_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=CATCORE.DatasetSeries_frequency, domain=DatasetSeries, range=Optional[Union[dict, "Frequency"]])

slots.DatasetSeries_geographical_coverage = Slot(uri=DCTERMS.spatial, name="DatasetSeries_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=CATCORE.DatasetSeries_geographical_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.DatasetSeries_modification_date = Slot(uri=DCTERMS.modified, name="DatasetSeries_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.DatasetSeries_modification_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_publisher = Slot(uri=DCTERMS.publisher, name="DatasetSeries_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=CATCORE.DatasetSeries_publisher, domain=DatasetSeries, range=Optional[Union[dict, Agent]])

slots.DatasetSeries_release_date = Slot(uri=DCTERMS.issued, name="DatasetSeries_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.DatasetSeries_release_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_temporal_coverage = Slot(uri=DCTERMS.temporal, name="DatasetSeries_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=CATCORE.DatasetSeries_temporal_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.DatasetSeries_title = Slot(uri=DCTERMS.title, name="DatasetSeries_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.DatasetSeries_title, domain=DatasetSeries, range=Union[str, list[str]])

slots.DefinedTerm_title = Slot(uri=SCHEMA.name, name="DefinedTerm_title", curie=SCHEMA.curie('name'),
                   model_uri=CATCORE.DefinedTerm_title, domain=DefinedTerm, range=Optional[str])

slots.Device_has_part = Slot(uri=DCTERMS.hasPart, name="Device_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.Device_has_part, domain=Device, range=Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]])

slots.Device_other_identifier = Slot(uri=ADMS.identifier, name="Device_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.Device_other_identifier, domain=Device, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Distribution_access_URL = Slot(uri=DCAT.accessURL, name="Distribution_access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=CATCORE.Distribution_access_URL, domain=Distribution, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Distribution_access_service = Slot(uri=DCAT.accessService, name="Distribution_access_service", curie=DCAT.curie('accessService'),
                   model_uri=CATCORE.Distribution_access_service, domain=Distribution, range=Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]])

slots.Distribution_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Distribution_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=CATCORE.Distribution_applicable_legislation, domain=Distribution, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Distribution_availability = Slot(uri=DCATAP.availability, name="Distribution_availability", curie=DCATAP.curie('availability'),
                   model_uri=CATCORE.Distribution_availability, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_byte_size = Slot(uri=DCAT.byteSize, name="Distribution_byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=CATCORE.Distribution_byte_size, domain=Distribution, range=Optional[int])

slots.Distribution_checksum = Slot(uri=SPDX.checksum, name="Distribution_checksum", curie=SPDX.curie('checksum'),
                   model_uri=CATCORE.Distribution_checksum, domain=Distribution, range=Optional[Union[dict, Checksum]])

slots.Distribution_compression_format = Slot(uri=DCAT.compressFormat, name="Distribution_compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=CATCORE.Distribution_compression_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_description = Slot(uri=DCTERMS.description, name="Distribution_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.Distribution_description, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Distribution_documentation = Slot(uri=FOAF.page, name="Distribution_documentation", curie=FOAF.curie('page'),
                   model_uri=CATCORE.Distribution_documentation, domain=Distribution, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Distribution_download_URL = Slot(uri=DCAT.downloadURL, name="Distribution_download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=CATCORE.Distribution_download_URL, domain=Distribution, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Distribution_format = Slot(uri=DCTERMS.format, name="Distribution_format", curie=DCTERMS.curie('format'),
                   model_uri=CATCORE.Distribution_format, domain=Distribution, range=Optional[Union[dict, "MediaTypeOrExtent"]])

slots.Distribution_has_policy = Slot(uri=ODRL.hasPolicy, name="Distribution_has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=CATCORE.Distribution_has_policy, domain=Distribution, range=Optional[Union[dict, "Policy"]])

slots.Distribution_language = Slot(uri=DCTERMS.language, name="Distribution_language", curie=DCTERMS.curie('language'),
                   model_uri=CATCORE.Distribution_language, domain=Distribution, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Distribution_licence = Slot(uri=DCTERMS.license, name="Distribution_licence", curie=DCTERMS.curie('license'),
                   model_uri=CATCORE.Distribution_licence, domain=Distribution, range=Optional[Union[dict, "LicenseDocument"]])

slots.Distribution_linked_schemas = Slot(uri=DCTERMS.conformsTo, name="Distribution_linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=CATCORE.Distribution_linked_schemas, domain=Distribution, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Distribution_media_type = Slot(uri=DCAT.mediaType, name="Distribution_media_type", curie=DCAT.curie('mediaType'),
                   model_uri=CATCORE.Distribution_media_type, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_modification_date = Slot(uri=DCTERMS.modified, name="Distribution_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=CATCORE.Distribution_modification_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_packaging_format = Slot(uri=DCAT.packageFormat, name="Distribution_packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=CATCORE.Distribution_packaging_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_release_date = Slot(uri=DCTERMS.issued, name="Distribution_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=CATCORE.Distribution_release_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_rights = Slot(uri=DCTERMS.rights, name="Distribution_rights", curie=DCTERMS.curie('rights'),
                   model_uri=CATCORE.Distribution_rights, domain=Distribution, range=Optional[Union[dict, "RightsStatement"]])

slots.Distribution_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Distribution_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=CATCORE.Distribution_spatial_resolution, domain=Distribution, range=Optional[Decimal])

slots.Distribution_status = Slot(uri=ADMS.status, name="Distribution_status", curie=ADMS.curie('status'),
                   model_uri=CATCORE.Distribution_status, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Distribution_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=CATCORE.Distribution_temporal_resolution, domain=Distribution, range=Optional[str])

slots.Distribution_title = Slot(uri=DCTERMS.title, name="Distribution_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.Distribution_title, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Entity_title = Slot(uri=DCTERMS.title, name="Entity_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.Entity_title, domain=Entity, range=Optional[str])

slots.Entity_description = Slot(uri=DCTERMS.description, name="Entity_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.Entity_description, domain=Entity, range=Optional[str])

slots.Entity_other_identifier = Slot(uri=ADMS.identifier, name="Entity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.Entity_other_identifier, domain=Entity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Entity_has_part = Slot(uri=DCTERMS.hasPart, name="Entity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.Entity_has_part, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Entity_part_of = Slot(uri=DCTERMS.isPartOf, name="Entity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=CATCORE.Entity_part_of, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.EvaluatedActivity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedActivity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.EvaluatedActivity_other_identifier, domain=EvaluatedActivity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.EvaluatedEntity_title = Slot(uri=DCTERMS.title, name="EvaluatedEntity_title", curie=DCTERMS.curie('title'),
                   model_uri=CATCORE.EvaluatedEntity_title, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_description = Slot(uri=DCTERMS.description, name="EvaluatedEntity_description", curie=DCTERMS.curie('description'),
                   model_uri=CATCORE.EvaluatedEntity_description, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="EvaluatedEntity_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=CATCORE.EvaluatedEntity_was_generated_by, domain=EvaluatedEntity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.EvaluatedEntity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.EvaluatedEntity_other_identifier, domain=EvaluatedEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Identifier_notation = Slot(uri=SKOS.notation, name="Identifier_notation", curie=SKOS.curie('notation'),
                   model_uri=CATCORE.Identifier_notation, domain=Identifier, range=str)

slots.LicenseDocument_type = Slot(uri=DCTERMS.type, name="LicenseDocument_type", curie=DCTERMS.curie('type'),
                   model_uri=CATCORE.LicenseDocument_type, domain=LicenseDocument, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.Location_bbox = Slot(uri=DCAT.bbox, name="Location_bbox", curie=DCAT.curie('bbox'),
                   model_uri=CATCORE.Location_bbox, domain=Location, range=Optional[str])

slots.Location_centroid = Slot(uri=DCAT.centroid, name="Location_centroid", curie=DCAT.curie('centroid'),
                   model_uri=CATCORE.Location_centroid, domain=Location, range=Optional[str])

slots.Location_geometry = Slot(uri=LOCN.geometry, name="Location_geometry", curie=LOCN.curie('geometry'),
                   model_uri=CATCORE.Location_geometry, domain=Location, range=Optional[Union[dict, "Geometry"]])

slots.PeriodOfTime_beginning = Slot(uri=TIME.hasBeginning, name="PeriodOfTime_beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=CATCORE.PeriodOfTime_beginning, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end = Slot(uri=TIME.hasEnd, name="PeriodOfTime_end", curie=TIME.curie('hasEnd'),
                   model_uri=CATCORE.PeriodOfTime_end, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end_date = Slot(uri=DCAT.endDate, name="PeriodOfTime_end_date", curie=DCAT.curie('endDate'),
                   model_uri=CATCORE.PeriodOfTime_end_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.PeriodOfTime_start_date = Slot(uri=DCAT.startDate, name="PeriodOfTime_start_date", curie=DCAT.curie('startDate'),
                   model_uri=CATCORE.PeriodOfTime_start_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.QualitativeAttribute_value = Slot(uri=PROV.value, name="QualitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=CATCORE.QualitativeAttribute_value, domain=QualitativeAttribute, range=str)

slots.QuantitativeAttribute_value = Slot(uri=PROV.value, name="QuantitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=CATCORE.QuantitativeAttribute_value, domain=QuantitativeAttribute, range=float)

slots.Relationship_had_role = Slot(uri=DCAT.hadRole, name="Relationship_had_role", curie=DCAT.curie('hadRole'),
                   model_uri=CATCORE.Relationship_had_role, domain=Relationship, range=Union[Union[dict, "Role"], list[Union[dict, "Role"]]])

slots.Relationship_relation = Slot(uri=DCTERMS.relation, name="Relationship_relation", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.Relationship_relation, domain=Relationship, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Software_has_part = Slot(uri=DCTERMS.hasPart, name="Software_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=CATCORE.Software_has_part, domain=Software, range=Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]])

slots.Software_other_identifier = Slot(uri=ADMS.identifier, name="Software_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=CATCORE.Software_other_identifier, domain=Software, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Atom_rdf_type = Slot(uri=RDF.type, name="Atom_rdf_type", curie=RDF.curie('type'),
                   model_uri=CATCORE.Atom_rdf_type, domain=Atom, range=Union[dict, DefinedTerm])

slots.ChemicalReaction_has_temperature = Slot(uri=SIO['000008'], name="ChemicalReaction_has_temperature", curie=SIO.curie('000008'),
                   model_uri=CATCORE.ChemicalReaction_has_temperature, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]])

slots.ChemicalReaction_has_pressure = Slot(uri=SIO['000008'], name="ChemicalReaction_has_pressure", curie=SIO.curie('000008'),
                   model_uri=CATCORE.ChemicalReaction_has_pressure, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]])

slots.ChemicalReaction_related_resource = Slot(uri=DCTERMS.relation, name="ChemicalReaction_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=CATCORE.ChemicalReaction_related_resource, domain=ChemicalReaction, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]])

slots.MaterialEntity_has_part = Slot(uri=BFO['0000051'], name="MaterialEntity_has_part", curie=BFO.curie('0000051'),
                   model_uri=CATCORE.MaterialEntity_has_part, domain=MaterialEntity, range=Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]])

slots.MaterialSample_derived_from = Slot(uri=PROV.wasDerivedFrom, name="MaterialSample_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=CATCORE.MaterialSample_derived_from, domain=MaterialSample, range=Optional[Union[dict, Entity]])
