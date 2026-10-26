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
| Catalysis research field | heterogeneous catalysis, electrocatalysis, biocatalysis | Recommended |
| Reaction type | CO oxidation, ammonia synthesis, hydrogenation | Recommended |

**Layer 2 — Data-class-specific metadata** is structured around the four data classes: Synthesis, Characterization, Reaction, and Simulation. Each data class carries its own set of Mandatory, Recommended, and Optional fields.

```
CatalysisDataset
 ├── catalysis research field          [Layer 1 — applies to all]
 ├── reaction type                     [Layer 1 — applies to all]
 ├── was_generated_by → Synthesis      [Layer 2 — data-class specific]
 ├── was_generated_by → Characterization
 ├── was_generated_by → Simulation
 └── is_about_activity → Reaction
```

---

## The four data classes

### Synthesis

Reproducibility of catalyst synthesis is one of the most persistent challenges in catalysis research. The Synthesis data class defines the minimum metadata for twelve preparation methods — from common routes such as Impregnation and Co-Precipitation to more specialised techniques like Atomic Layer Deposition, Flame Spray Pyrolysis, and Exsolution Synthesis.

Method-specific parameter sets are organized into concrete preparation method types. Cross-cutting steps shared across methods (drying, calcination, precipitation) are defined once and reused, so the same parameter is never described differently depending on which method it appears in.

| Preparation method | Key shared steps |
|---|---|
| Impregnation | Drying, Calcination |
| Co-Precipitation | Precipitation, Drying, Calcination |
| Deposition-Precipitation | Precipitation, Drying, Calcination |
| Solvothermal, Plasma-Assisted, Combustion, Microwave-Assisted, Mechanochemical, Sublimation | Thermal process |
| Sol-Gel, Flame Spray Pyrolysis, Atomic Layer Deposition, Exsolution | Method-specific only |

### Characterization

The Characterization data class covers twenty-eight analytical techniques currently used in catalysis. Each technique is modelled with slots for instrument parameters, sample state, and measurement conditions. Cross-cutting parameter groups are shared across related techniques:

- X-ray source parameters — shared by Powder XRD, Single Crystal XRD, XPS, EDX
- Electron microscopy parameters — shared by TEM, SEM
- Temperature program parameters — shared by TPR, TPO, Thermogravimetry
- Chromatography and mass range parameters — shared by GC, GC-MS, HPLC, HPLC-MS

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

The Simulation data class covers four major computational method classes: DFT, Molecular Dynamics, Microkinetics, and Monte Carlo. The simulation software used is recorded alongside the method. Twelve calculated property types — such as electronic structure, band gap, phonon dispersion, and thermodynamic stability — capture the computed output.

---

## What does a CoreMeta4Cat record look like?

Here is a minimal example showing how a reaction dataset is described. Every class and property links to a controlled vocabulary term and can be validated and converted to RDF using standard tooling:

```yaml
id: ex:dataset-001
title: "CO oxidation activity of 1wt% Pt/Al2O3 at 200–400°C"
catalysis_research_field: heterogeneous catalysis

was_generated_by:
  - type: Reaction
    catalyst_quantity: 100.0    # mg
    reactant:
      - "1 vol% CO in N2"
      - "2 vol% O2 in N2"
    reactor_temperature_range: "200–400 °C"
    experiment_pressure: 1.0    # bar
    carried_out_by:
      type: FixedBedReactor

is_about_entity:
  - type: CatalystSample
    nominal_composition: "1wt% Pt/Al2O3"
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
