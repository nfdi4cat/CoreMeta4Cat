# CoreMeta4Cat — Overview

CoreMeta4Cat defines the minimum information that should be reported alongside catalysis research data, across four domains: Synthesis, Characterization, Reaction, and Simulation. This page gives you a structured overview of what the standard covers, how it is organized, and how the different parts connect.

---

## What is CoreMeta4Cat?

CoreMeta4Cat is a metadata standard for catalysis research data, developed within the [NFDI4Cat](https://nfdi4cat.org) initiative. It is implemented as a [LinkML](https://linkml.io/) schema — a format that allows the standard to automatically generate multiple useful outputs from a single source: an Excel reference workbook, a JSON Schema for validation, Python data classes, and a full RDF/OWL representation for semantic querying.

CoreMeta4Cat is built as a domain-specific application profile on top of [DCAT-AP-PLUS](https://nfdi-de.github.io/dcat-ap-plus/dev/), a provenance-aware extension of the DCAT Application Profile 3.0. This means every CoreMeta4Cat dataset is a valid `dcat:Dataset`, every activity is a valid `prov:Activity`, and all schema artefacts are generated automatically from the single LinkML source.

In practical terms: a dataset described with CoreMeta4Cat is not just a well-labelled spreadsheet. It is a structured, machine-readable record that can be validated, searched, and connected to other datasets across repositories — because every field links back to a shared scientific vocabulary.

---

## Two-layer architecture

CoreMeta4Cat organises metadata in two layers.

**Layer 1 — Global classification** applies to every catalysis dataset, regardless of data class. It captures the two fields needed for the coarsest-possible filtering across a repository:

| Field | Example values | Obligation |
|---|---|---|
| Catalysis research field | heterogeneous catalysis, electrocatalysis, biocatalysis (several can be given) | Mandatory |
| Reaction type | CO oxidation, ammonia synthesis, hydrogenation | Mandatory for every reaction |

**Layer 2 — Data-class-specific metadata** is structured around the four data classes: Synthesis, Characterization, Reaction, and Simulation. Each data class carries its own set of Mandatory, Recommended, and Optional fields.

```
CatalysisDataset
 ├── catalysis research field          [Layer 1 — applies to all]
 ├── reaction type                     [Layer 1 — on each Reaction]
 ├── was_generated_by → Synthesis      [Layer 2 — data-class specific]
 ├── was_generated_by → Characterization
 ├── was_generated_by → Simulation
 └── is_about_activity → Reaction
```

---

## The four data classes

### Synthesis

Reproducibility of catalyst synthesis is one of the most persistent challenges in catalysis research. The Synthesis data class defines the minimum metadata for fifteen preparation methods — from common routes such as Impregnation and Co-Precipitation to more specialised techniques like Atomic Layer Deposition, Flame Spray Pyrolysis, and Exsolution Synthesis.

Method-specific parameter sets are organized into concrete preparation method types. Cross-cutting steps shared across methods (drying, calcination, precipitation) are defined once and reused, so the same parameter is never described differently depending on which method it appears in.

| Preparation method | Key shared steps |
|---|---|
| Impregnation, Sonochemical | Drying, Calcination |
| Co-Precipitation, Deposition-Precipitation | Precipitation, Drying, Calcination |
| Sol-Gel, Molecular Synthesis | Drying |
| Exsolution | Calcination |
| Solvothermal, Plasma-Assisted, Combustion, Microwave-Assisted, Mechanochemical, Sublimation | Thermal process |
| Flame Spray Pyrolysis, Atomic Layer Deposition | Method-specific only |

### Characterization

The Characterization data class covers twenty-seven analytical techniques currently used in catalysis. Each technique is modelled with slots for instrument parameters, sample state, and measurement conditions. Cross-cutting parameter groups are shared across related techniques:

- X-ray source parameters — shared by Powder XRD, Single Crystal XRD, XPS, XAS
- Electron microscopy parameters — shared by TEM, SEM
- Temperature program parameters — shared by TPR, TPO, Thermogravimetry
- Chromatography parameters — shared by GC-MS, HPLC-MS, size exclusion chromatography
- Mass range parameters — shared by GC-MS, ESI-MS

### Reaction

The Reaction data class represents the catalytic process being studied. An important design detail: for operando experiments — for example, in-situ XRD carried out while a reaction is running — the dataset carries both a Characterization record (the process that generated the data) and a Reaction record (the process the data is about). CoreMeta4Cat models both links explicitly.

Eight reactor design types are currently defined:

- Electrochemical Reactor
- CSTR (Continuous Stirred Tank Reactor)
- Plug Flow Reactor
- Autoclave
- Slurry Reactor
- Microreactor
- Fixed Bed Reactor
- Fluidized Bed Reactor

### Simulation

The Simulation data class covers four major computational method classes: DFT, Molecular Dynamics, Microkinetics, and Monte Carlo. The simulation software used is recorded alongside the method. Seventeen calculated property types capture the computed output — from material properties such as electronic structure, band gap, phonon dispersion, and thermodynamic stability to catalysis-specific ones such as adsorption energetics, reaction energetics, and transition states.

---

## What does a CoreMeta4Cat record look like?

Here is a small example showing how a reaction dataset is described: the GC-MS measurement that produced the data, and the catalytic reaction the data is about. Every class and property links to a controlled vocabulary term, and the record validates and converts to RDF with standard LinkML tooling:

```yaml
id: ex:dataset-001
title:
  - "CO oxidation activity of 1wt% Pt/Al2O3 at 200–400 °C"
description:
  - "Light-off test in a fixed-bed reactor, products analysed by online GC-MS."
rdf_type:                                 # catalysis research field (Layer 1)
  - id: voc4cat:0007001
    title: "heterogeneous catalysis"

was_generated_by:                         # the measurement that produced the data
  - id: ex:gcms-001
    activity_designator: Characterization
    carried_out_by:
      - id: ex:gcms-instrument-001
        title: "online GC-MS"
    evaluated_activity:
      - id: ex:reaction-001
    realized_plan:
      id: ex:gcms-method-001
      plan_designator: CHMO:0000497       # GCMS
      title: "online GC-MS of the reactor effluent"

is_about_activity:                        # the catalytic reaction the data is about
  - id: ex:reaction-001
    rdf_type:                             # reaction type (Layer 1)
      id: voc4cat:0000289
      title: "CO oxidation"
    catalyst_mass:
      - value: 100.0
        has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
        unit: https://qudt.org/vocab/unit/MilliGM
    used_reactant:
      - id: ex:feed-co
        title: "1 vol% CO in N2"
      - id: ex:feed-o2
        title: "2 vol% O2 in N2"
    reactor_temperature_range:
      - min_value: 200.0
        max_value: 400.0
        has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        unit: https://qudt.org/vocab/unit/DEG_C
    experiment_pressure:
      - value: 1.0
        has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
        unit: https://qudt.org/vocab/unit/BAR
    used_reactor:
      - id: ex:reactor-001
        reactor_designator: coremeta4cat:FixedBedReactor

is_about_entity:                          # the catalyst
  - id: ex:catalyst-001
    title: "1wt% Pt/Al2O3"
```

---

## Further reading

| Page | What it covers |
|---|---|
| [Design Patterns](https://nfdi4cat.github.io/CoreMeta4Cat/latest/design-patterns/) | How the four data classes map to DCAT-AP-PLUS, the mixin pattern, ontology alignment |
| [How to Extend](https://nfdi4cat.github.io/CoreMeta4Cat/latest/how-to-extend/) | Rules for adding new preparation methods, techniques, reactor types, and properties |
| [Schema Reference](https://nfdi4cat.github.io/CoreMeta4Cat/latest/elements/overview/) | Auto-generated reference for all classes and slots |
| [Intended Users](https://nfdi4cat.github.io/CoreMeta4Cat/latest/coremeta4cat-users/) | Projects and repositories that adopt CoreMeta4Cat |

The LinkML schema, build scripts, and documentation source are on GitHub: [nfdi4cat/CoreMeta4Cat](https://github.com/nfdi4cat/CoreMeta4Cat)
