---
title: CoreMeta4Cat
description: Comprehensive Metadata Guidelines for Catalysis Research Data
---

# CoreMeta4Cat — Comprehensive Metadata Guidelines for Catalysis Research Data

<div class="grid cards" markdown>

-   :material-flask-outline: **Synthesis**

    Twelve preparation methods with method-specific parameter sets, shared mixin classes for drying and calcination steps.

-   :material-microscope: **Characterization**

    Twenty-eight analytical techniques, from Powder XRD to Cyclic Voltammetry, each with dedicated measurement slots.

-   :material-thermometer: **Reaction**

    Eight reactor design types, flattened operation parameter slots, and product identification links.

-   :octicons-cpu-16: **Simulation**

    Four computational methods (DFT, MD, Microkinetics, Monte Carlo) with 12 calculated property classes.

</div>

---

## What is CoreMeta4Cat?

CoreMeta4Cat is a [LinkML](https://linkml.io/)-based metadata reference model for catalysis research data, developed within the [NFDI4Cat](https://nfdi4cat.org) initiative. It defines the **minimum information** that should be reported alongside research data in the field of catalysis, following the FAIR principles (Findable, Accessible, Interoperable, Reusable).

CoreMeta4Cat is built as a domain-specific application profile on top of [DCAT-AP-PLUS](https://nfdi-de.github.io/dcat-ap-plus/dev/), a provenance-aware extension of the DCAT Application Profile 3.0. This means every CoreMeta4Cat dataset is a valid `dcat:Dataset`, every activity is a valid `prov:Activity`, and all schema artefacts — SHACL shapes, JSON Schema, Python/Pydantic classes, HTML reference documentation — are generated automatically from the single LinkML source.

---

## Quick Start: What does CoreMeta4Cat add?

In plain DCAT-AP, a `Dataset` can describe what data exists but says little about *how* it was produced or *what material* it concerns. DCAT-AP-PLUS adds a structured provenance graph via `prov:wasGeneratedBy`. CoreMeta4Cat specialises that graph for catalysis:

```yaml
# A dataset about the CO oxidation performance of a supported Pt catalyst
id: ex:dataset-001
title: "CO oxidation activity of 1wt% Pt/Al2O3 at 200–400°C"
rdf_type:
  id: voc4cat:0007001
  title: "heterogeneous catalysis"

was_generated_by:
  - id: ex:reaction-001
    type: Reaction
    catalyst_quantity: 100.0   # mg
    reactant:
      - "1 vol% CO in N2"
      - "2 vol% O2 in N2"
    reactor_temperature_range: "200–400 °C"
    experiment_pressure: 1.0   # bar
    carried_out_by:
      id: ex:reactor-001
      type: FixedBedReactor

is_about_entity:
  - id: ex:catalyst-001
    type: CatalystSample
    nominal_composition: "1wt% Pt/Al2O3"
```

This is valid CoreMeta4Cat instance data. Every class and property is mapped to a controlled ontology term (voc4cat, CHMO, OBI, …) and can be validated and converted to RDF using standard LinkML tooling.

---

## Two-layer architecture

CoreMeta4Cat organises metadata in two layers.

**Layer 1 — Global classification** is data-class-independent. It applies to every `CatalysisDataset` and captures the two fields needed for the coarsest-possible filtering of a repository:

| Field | Example values | Obligation |
|---|---|---|
| Catalysis research field (`rdf_type`) | heterogeneous catalysis, electrocatalysis, biocatalysis | Recommended |
| Reaction type (`rdf_type` on `Reaction`) | CO oxidation, ammonia synthesis, hydrogenation | Recommended |

**Layer 2 — Data-class-specific metadata** is structured around the four *pillars*: Synthesis, Characterization, Reaction, and Simulation. Each pillar maps to a DCAT-AP-PLUS Activity subclass and carries its own set of Mandatory, Recommended, and Optional fields.

```
CatalysisDataset (dcat:Dataset)
 ├── rdf_type → CatalysisResearchFieldEnum   [Layer 1]
 ├── was_generated_by → Synthesis            [Layer 2]
 ├── was_generated_by → Characterization     [Layer 2]
 ├── was_generated_by → Simulation           [Layer 2]
 └── is_about_activity → Reaction            [Layer 2]
```

---

## The four CoreMeta4Cat pillars

### Synthesis

Reproducibility of catalyst synthesis is one of the most persistent challenges in catalysis research. The **Synthesis** pillar defines the minimum metadata for twelve preparation methods, from common routes such as Impregnation and Co-Precipitation to more specialised techniques like Atomic Layer Deposition, Flame Spray Pyrolysis, and Exsolution Synthesis.

Method-specific parameter sets are organised into concrete `PreparationMethod` subclasses. Cross-cutting slot groups (drying step, calcination step, precipitation step, thermal process) are factored out as **mixin classes**, so parameters shared by multiple methods are defined exactly once.

| Class | Key mixins applied |
|---|---|
| `Impregnation` | `DryingMixin`, `CalcinationMixin` |
| `CoPrecipitation` | `PrecipitationMixin`, `DryingMixin`, `CalcinationMixin` |
| `DepositionPrecipitation` | `PrecipitationMixin`, `DryingMixin`, `CalcinationMixin` |
| `Solvothermal`, `PlasmaAssisted`, `CombustionSynthesis`, `MicrowaveAssisted`, `MechanochemicalSynthesis`, `Sublimation` | `ThermalSynthesisMixin` |
| `SonochemicalSynthesis`, `MolecularSynthesis` | `DryingMixin` / `CalcinationMixin` |
| `AtomicLayerDeposition`, `SolGel`, `FlameSprayPyrolysis`, `ExsolutionSynthesis` | method-specific slots only |

### Characterization

The **Characterization** pillar covers twenty-eight analytical techniques currently used in catalysis. Each technique is modelled as a concrete `CharacterizationTechnique` subclass (a DCAT-AP-PLUS `Plan`), with slots for instrument parameters, sample state, and measurement conditions. Cross-cutting parameter groups are again factored out as mixins:

- `XRaySourceMixin` — shared by PowderXRD, SingleCrystalXRD, XPS, EDX
- `ElectronMicroscopyMixin` — shared by TEM, SEM
- `TemperatureProgramMixin` — shared by TPR, TPO, Thermogravimetry
- `ChromatographyMixin`, `MassRangeMixin` — shared by GC, GC-MS, HPLC, HPLC-MS

### Reaction

The **Reaction** pillar represents the catalytic process being studied. It is modelled as a DCAT-AP-PLUS `EvaluatedActivity` — the process the dataset is *about*, not the process that *generates* the data. This distinction matters: for operando experiments (e.g. in-situ XRD during a reaction), the dataset carries both `was_generated_by: Characterization` and `is_about_activity: Reaction`.

The reactor is linked via `carried_out_by` as one of eight `ReactorDesignType` subclasses:

<div class="grid" markdown>

- `ElectrochemicalReactor`
- `CSTR`
- `PlugFlowReactor`
- `Autoclave`
- `SlurryReactor`
- `Microreactor`
- `FixedBedReactor`
- `FluidizedBedReactor`

</div>

### Simulation

The **Simulation** pillar covers four major computational method classes, each a `SimulationMethod` subclass (DCAT-AP-PLUS `Plan`): **DFT**, **MolecularDynamics**, **Microkinetics**, and **MonteCarlo**. The simulation software is linked via `carried_out_by` as a `Software` agent. Twelve `CalculatedProperty` classes (e.g. `ElectronicStructure`, `BandGap`, `PhononDispersion`, `ThermodynamicStability`) capture the computed output type.

---

## Documentation

| Page | What it covers |
|---|---|
| [Design Patterns](design-patterns.md) | How the four pillars map to DCAT-AP-PLUS, the mixin pattern, ontology alignment |
| [How to Extend](how-to-extend.md) | Rules for adding new preparation methods, techniques, reactor types, and properties |
| [Schema Reference](elements/overview.md) | Auto-generated reference for all classes and slots |
| [CoreMeta4Cat Users](coremeta4cat-users.md) | Projects and repositories that adopt CoreMeta4Cat |

## Source code

The LinkML schema, build scripts, and documentation source are on GitHub: [HendrikBorgelt/CoreMeta4Cat](https://github.com/HendrikBorgelt/CoreMeta4Cat)

The schema is built as a domain-specific application profile on top of DCAT-AP-PLUS. The base layer is maintained by [NFDI4Cat](https://nfdi4cat.org).
