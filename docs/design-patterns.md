---
title: Design Patterns
description: How CoreMeta4Cat is structured and why
---

# Design Patterns

This page explains the key structural decisions behind CoreMeta4Cat — how the four pillars are modelled, how they connect to a dataset, and what design patterns make the schema extensible and machine-actionable.

<div style="text-align: center;">
    <a>
    <img src="/CoreMeta4Cat/images/CoreMeta4Cat_Picture.png" alt="CoreMeta4Cat logo" style="width: 40%;">
    </a>
</div>
---

## Reading guide

This page is written in three tiers. Most users only need the first two.

| Tier | Who it's for | Sections |
|---|---|---|
| **Overview** | Everyone — data providers, repository managers | [The entry point](#the-entry-point-catalysisdataset), [The four pillars](#the-four-pillars) |
| **Pattern explanations** | Users who want to understand how to navigate or extend the schema | [Classification pattern](#pattern-1-classification-via-rdf_type), [Activity pattern](#pattern-2-activities-and-plans), [Mixin pattern](#pattern-3-mixin-classes) |
| **Technical depth** | Schema developers and DCAT-AP-PLUS integrators | [Sections marked with 🔬](#deep-dive-the-evaluated-activity-distinction) |

---

## The entry point: CatalysisDataset

Every CoreMeta4Cat record starts with a **`CatalysisDataset`**. This is a `dcat:Dataset` — fully compatible with plain DCAT and DCAT-AP — extended with four additional link slots that connect to the four CoreMeta4Cat pillars.

```yaml
id: ex:dataset-001
type: CatalysisDataset                  # → dcat:Dataset

# Layer 1: global classification
rdf_type:
  id: voc4cat:0007001
  title: "heterogeneous catalysis"

# Layer 2: links to the four pillars
was_generated_by:
  - id: ex:synthesis-001
    type: Synthesis
  - id: ex:characterization-001
    type: Characterization

is_about_activity:
  - id: ex:reaction-001
    type: Reaction

is_about_entity:
  - id: ex:catalyst-001
    type: CatalystSample
```

The key points here are:

- `rdf_type` carries a **controlled vocabulary term** from [Voc4Cat](https://nfdi4cat.github.io/voc4cat/) to classify which field of catalysis the dataset belongs to.
- `was_generated_by` links to **activities that produced the data** (Synthesis, Characterization, Simulation).
- `is_about_activity` links to the **Reaction being studied** — which is the catalytic process itself, not a data-generating step.
- `is_about_entity` links to the **catalyst sample or material** the dataset concerns.

---

## The four pillars

The four CoreMeta4Cat pillars — **Synthesis**, **Characterization**, **Reaction**, and **Simulation** — are the core of the metadata model. Each is a separate class, defined in its own subprofile module, and linked from the `CatalysisDataset` via the slots above.

```
catcore.yaml  (aggregator + CatalysisDataset)
  ├── catcore_common.yaml          (shared slots and enumerations)
  ├── catcore_synthesis_ap.yaml    (Synthesis + 12 preparation methods)
  ├── catcore_characterization_ap.yaml  (Characterization + 28 techniques)
  ├── catcore_reaction_ap.yaml     (Reaction + 8 reactor types)
  └── catcore_simulation_ap.yaml   (Simulation + 4 methods + 12 properties)
```

### Synthesis

**What it is:** The process of preparing a catalyst. Synthesis is a `DataGeneratingActivity` — it produces data *about* the preparation, and it produces a `CatalystSample` as its physical output.

**Key links:**

- `realized_plan` → a `PreparationMethod` subclass (the protocol used)
- `had_input_entity` → `Precursor` instances (the starting materials)
- `had_output_entity` → `CatalystSample` (the resulting catalyst)

**Twelve preparation methods** are currently defined, each as a concrete `PreparationMethod` subclass:

<div class="grid cards" markdown>

-   **Wet chemistry**

    Impregnation, Co-Precipitation, Deposition-Precipitation, Sol-Gel, Molecular Synthesis

-   **Thermal / gas-phase**

    Solvothermal, Combustion Synthesis, Flame Spray Pyrolysis, Sublimation, Plasma-Assisted

-   **Mechanical / energy-assisted**

    Mechanochemical Synthesis, Microwave-Assisted, Sonochemical Synthesis

-   **Surface / thin-film**

    Atomic Layer Deposition, Exsolution Synthesis

</div>

### Characterization

**What it is:** The measurement of a catalyst or catalytic system using an analytical technique. Characterization is also a `DataGeneratingActivity` — it produces measurement data.

**Key links:**

- `evaluated_entity` → the `CatalystSample` or material being measured
- `realized_plan` → a `CharacterizationTechnique` subclass (the measurement protocol)
- `carried_out_by` → the instrument (`Device`) performing the measurement

**Twenty-eight techniques** are currently defined, organised into groups:

| Group | Techniques |
|---|---|
| Diffraction | Powder XRD, Single Crystal XRD |
| X-ray spectroscopy | XAS/XANES/EXAFS, XPS, EDX |
| Vibrational spectroscopy | FTIR, DRIFTS, Raman, NMR |
| Electron microscopy | TEM, SEM |
| Thermal analysis | TGA, TPR, TPO |
| Surface & pore analysis | BET |
| Elemental analysis | ICP-AES, Elemental Analysis (CHNS) |
| Optical & electronic | UV-Vis, Photoluminescence, Photoluminescence Lifetime |
| Electrochemistry | Cyclic Voltammetry, Conductivity Measurement |
| Particle sizing | Dynamic Light Scattering |
| Mass spectrometry | ESI-MS, GC-MS, HPLC-MS |
| Chromatography | GC, HPLC |

### Reaction

**What it is:** The catalytic reaction being studied. Unlike Synthesis and Characterization, Reaction is **not** a `DataGeneratingActivity`. It is the process being *observed*, not the process generating the dataset.

**Key links:**

- `carried_out_by` → a `ReactorDesignType` (the physical reactor)
- `had_input_entity` → reactant feeds
- `product_identification_method` → a `CharacterizationTechnique` used for product analysis

**Eight reactor design types** are defined:

`FixedBedReactor` · `CSTR` · `PlugFlowReactor` · `Autoclave` · `SlurryReactor` · `Microreactor` · `ElectrochemicalReactor` · `FluidizedBedReactor`

!!! info "Operando experiments"
    For in-situ or operando experiments (e.g. XRD measured while a reaction runs), the dataset carries **both** links simultaneously:
    ```yaml
    was_generated_by:
      - type: Characterization     # PowderXRD — the process that made the data
    is_about_activity:
      - type: Reaction             # the catalytic process being monitored
    ```

### Simulation

**What it is:** A computational study of a catalyst or catalytic mechanism. Simulation is a `DataGeneratingActivity` — it generates data computationally.

**Key links:**

- `realized_plan` → a `SimulationMethod` subclass (DFT, MD, Microkinetics, MonteCarlo)
- `carried_out_by` → a `Software` agent (the simulation package)
- `evaluated_entity` → the catalyst model or structure being simulated

**Twelve calculated property classes** capture the type of computed output: `ElectronicStructure`, `BandGap`, `ThermodynamicStability`, `PhononDispersion`, `Surfaces`, `GrainBoundaries`, `ElasticConstants`, `DielectricTensors`, `EquationsOfState`, `AqueousStability`, `Piezoelectricity`, `Ferroelectrics`.

---

## Pattern 1: Classification via rdf_type

!!! abstract "Pattern summary"
    Flexible, machine-actionable classification of datasets, activities, and entities using ontology terms — without creating a separate class for every possible value.

Rather than defining a fixed class hierarchy for every type of catalysis or every synthesis method, CoreMeta4Cat uses a single `rdf_type` slot on each class to carry a controlled vocabulary term from Voc4Cat, CHMO, or another ontology. This keeps the schema compact while staying fully machine-actionable.

**On CatalysisDataset** — classify the catalysis research field:

```yaml
rdf_type:
  id: voc4cat:0007001
  title: "heterogeneous catalysis"
```

**On Synthesis** — classify the preparation method type:

```yaml
type: Synthesis
rdf_type:
  id: voc4cat:0007016
  title: "impregnation"
realized_plan:
  type: Impregnation    # the concrete method class with all parameter slots
```

**On Characterization** — classify the measurement technique:

```yaml
type: Characterization
rdf_type:
  id: CHMO:0000158
  title: "powder X-ray diffraction"
realized_plan:
  type: PowderXRD       # the concrete technique class with all measurement slots
```

The `rdf_type` slot gives the machine-readable ontology term; the concrete subclass (`Impregnation`, `PowderXRD`, …) provides the structured parameter slots. Both are used together.

The allowed values for `rdf_type` on `CatalysisDataset` are defined in `CatalysisResearchFieldEnum`:

| Value | Ontology term | Description |
|---|---|---|
| `heterogeneous_catalysis` | `voc4cat:0007001` | Catalyst and reactants in different phases |
| `homogeneous_catalysis` | `voc4cat:0000294` | Catalyst and reactants in the same phase |
| `electrocatalysis` | `voc4cat:0000216` | Catalysis of electrochemical reactions |
| `biocatalysis` | `voc4cat:0000204` | Enzyme or whole-cell catalysis |
| `hybrid_catalysis` | *(pending)* | Combination of two or more approaches |
| `other` | — | Fallback for unlisted fields |

---

## Pattern 2: Activities and Plans

!!! abstract "Pattern summary"
    A two-part structure separates *what was done* (the Activity) from *the protocol describing how to do it* (the Plan). This mirrors the PROV-O model and keeps the schema clean.

Each pillar that generates data follows this two-part structure:

```
Activity (what was done)        Plan (the protocol)
─────────────────────────       ───────────────────────────
Synthesis              ──→      PreparationMethod
Characterization       ──→      CharacterizationTechnique
Simulation             ──→      SimulationMethod
```

The Activity carries the **instance-level data** (who did it, when, on what sample, with what output). The Plan carries the **method-level data** (parameter settings, instrument configuration, protocol steps).

```yaml
# The activity — what happened
id: ex:synthesis-001
type: Synthesis
nominal_composition: "5wt% Ni/Al2O3"
had_input_entity:
  - id: ex:precursor-001
    type: Precursor
    name: "Ni(NO3)2·6H2O"
    precursor_quantity: 1.24   # g
had_output_entity:
  - id: ex:catalyst-001
    type: CatalystSample

# The plan — the protocol
realized_plan:
  id: ex:method-001
  type: Impregnation
  impregnation_type: incipient_wetness
  impregnation_duration: 12.0   # h
  drying_temperature: 120.0     # °C
  drying_time: 12.0             # h
  calcination_final_temperature: 500.0   # °C
  calcination_dwelling_time: 4.0         # h
  calcination_gaseous_environment: "air"
```

This separation means a single `PreparationMethod` record could in principle be shared across multiple `Synthesis` activities — a direct gain for reproducibility.

---

## Pattern 3: Mixin classes

!!! abstract "Pattern summary"
    Slot groups that are shared across multiple methods are factored into reusable mixin classes, so each slot is defined exactly once and inherited wherever needed.

Many preparation methods share common process steps — drying, calcination, precipitation. Rather than repeating the same slots in every method class, CoreMeta4Cat uses **mixin classes** that bundle related slots:

| Mixin | Slots it provides | Used by |
|---|---|---|
| `DryingMixin` | `drying_device`, `drying_temperature`, `drying_time`, `drying_atmosphere` | Impregnation, CoPrecipitation, DepositionPrecipitation, SonochemicalSynthesis, MolecularSynthesis |
| `CalcinationMixin` | `calcination_initial_temperature`, `calcination_final_temperature`, `calcination_dwelling_time`, `calcination_heating_rate`, `calcination_gaseous_environment`, `calcination_gas_flow_rate`, `number_of_cycles` | Impregnation, CoPrecipitation, DepositionPrecipitation, SonochemicalSynthesis, ExsolutionSynthesis |
| `PrecipitationMixin` | `precipitating_agent`, `synthesis_ph`, `mixing_rate`, `mixing_time`, `mixing_temperature`, `order_of_addition`, `aging_temperature`, `aging_time` | CoPrecipitation, DepositionPrecipitation |
| `ThermalSynthesisMixin` | `synthesis_temperature`, `synthesis_duration`, `equipment`, `vessel_type`, `atmosphere` | Solvothermal, PlasmaAssisted, CombustionSynthesis, MicrowaveAssisted, MechanochemicalSynthesis, Sublimation |

The same pattern is used in the **Characterization** subprofile for analytical techniques:

| Mixin | Used by |
|---|---|
| `XRaySourceMixin` | PowderXRD, SingleCrystalXRD, XPS, EDX |
| `ElectronMicroscopyMixin` | TEM, SEM |
| `TemperatureProgramMixin` | TPR, TPO, Thermogravimetry |
| `ChromatographyMixin` | GC, HPLC, GC-MS, HPLC-MS |
| `MassRangeMixin` | GC-MS, HPLC-MS, ESI-MS |
| `ElectrochemistryMixin` | CyclicVoltammetry, ConductivityMeasurement |

In LinkML, a mixin class has no `class_uri` of its own and generates no independent node shape. It is a pure slot container, mixed in via the `mixins:` key on a concrete class.

---

## Pattern 4: Shared slots in catcore_common

!!! abstract "Pattern summary"
    Slots referenced by two or more subprofiles are declared once in `catcore_common.yaml` and imported by all subprofiles. This keeps the schema DRY (Don't Repeat Yourself).

Some slots appear in multiple pillars — for example, `temperature` is relevant to Synthesis (calcination), Characterization (temperature-programmed experiments), and Reaction (reactor temperature). These shared slots live in `catcore_common.yaml`:

```
catcore_common.yaml — shared slots include:
  atmosphere, temperature, flow_rate, heating_rate,
  equipment, sample_mass, stirring_speed, stirring_duration,
  drying_*, calcination_*, concentration, solvent,
  experiment_duration, step_size, resolution, ...
```

Slots that are exclusive to a single subprofile are declared in that subprofile file only.

---

## 🔬 Deep dive: The EvaluatedActivity distinction

!!! warning "Technical section"
    This section is intended for schema developers and DCAT-AP-PLUS integrators. It is not required reading for data providers.

One of the most important architectural decisions in CoreMeta4Cat is that **Reaction is not a `DataGeneratingActivity`**. Instead it is an `EvaluatedActivity`.

In DCAT-AP-PLUS, the distinction is:

| Class | Meaning | Links to dataset via |
|---|---|---|
| `DataGeneratingActivity` | A process that produces the data in the dataset | `prov:wasGeneratedBy` |
| `EvaluatedActivity` | A process that the dataset is *about*, but which did not produce it | `is_about_activity` |

For catalysis, a `Reaction` is the catalytic process being studied. The data is generated by *measuring* that reaction — via a `Characterization` activity. The `Reaction` itself does not produce the data file.

This distinction enables operando experiments to be described correctly:

```yaml
# Operando XRD during CO oxidation
was_generated_by:
  - type: Characterization      # PowderXRD run — this produced the data
    rdf_type:
      id: CHMO:0000158
      title: "powder X-ray diffraction"

is_about_activity:
  - type: Reaction              # the CO oxidation reaction being monitored
    catalyst_quantity: 50.0
    reactant: ["1 vol% CO", "2 vol% O2"]
    carried_out_by:
      type: FixedBedReactor
```

If `Reaction` were modelled as a `DataGeneratingActivity`, this relationship would collapse: it would be impossible to distinguish the measurement from the catalytic process it monitors.

The same distinction appears in DCAT-AP-PLUS itself — the NMR example in the base documentation uses `was_generated_by: NMRSpectroscopy` (the measurement) and `evaluated_entity: MaterialSample` (the thing measured). CoreMeta4Cat extends this by adding `is_about_activity: Reaction` for cases where a process — not just a material — is being monitored.

---

## Import hierarchy

The full import chain, from the CoreMeta4Cat top level down to the DCAT-AP-PLUS base, is:

```
catcore.yaml
  └── catcore_common.yaml
        └── chem_dcat_ap
              └── chemical_reaction_ap
                    └── chemical_entities_ap
                          └── material_entities_ap
                                └── dcat_ap_plus   ← DCAT-AP-PLUS base
  ├── catcore_synthesis_ap.yaml
  ├── catcore_characterization_ap.yaml
  ├── catcore_reaction_ap.yaml
  └── catcore_simulation_ap.yaml
```

Each layer adds domain-specific classes and slots on top of the layer below, without modifying it. This means CoreMeta4Cat datasets remain valid DCAT-AP-PLUS instances, which in turn remain valid DCAT-AP datasets.
