---
title: How to Extend
description: Rules and patterns for extending CoreMeta4Cat with new methods, techniques, and properties
---

# How to Extend CoreMeta4Cat

This page explains how to add new entries to the CoreMeta4Cat schema — new preparation methods, characterisation techniques, reactor types, simulation methods, or shared slots. Each section follows the same general pattern, adapted to the specific pillar.

<div style="text-align: center;">
    <a>
    <img src="images/CoreMeta4Cat_Picture.png" alt="CoreMeta4Cat logo" style="width: 40%;">
    </a>
</div>

!!! tip "Before you start"
    Read the [Design Patterns](design-patterns.md) page first if you are new to the schema. Understanding the Activity/Plan split and the mixin pattern will make the extension rules below straightforward.

---

## General rules

These rules apply when extending any part of CoreMeta4Cat.

**Rule 1 — Extend, don't modify.**
Add new subclasses and slots. Do not rename or remove existing classes, slots, or enum values — this would break backward compatibility for any dataset already using them.

**Rule 2 — Inherit from the right parent.**
Each extension type has a designated parent class (see the table below). Always use `is_a:` with that parent, not with a sibling class.

| What you are adding | Parent class | File |
|---|---|---|
| New preparation method | `PreparationMethod` | `catcore_synthesis_ap.yaml` |
| New characterisation technique | `CharacterizationTechnique` | `catcore_characterization_ap.yaml` |
| New reactor type | `ReactorDesignType` | `catcore_reaction_ap.yaml` |
| New simulation method | `SimulationMethod` | `catcore_simulation_ap.yaml` |
| New calculated property | `CalculatedProperty` | `catcore_simulation_ap.yaml` |
| New mixin (slot group) | *(no parent — mixin: true)* | Appropriate subprofile |
| New shared slot | *(no class — top-level slot)* | `catcore_common.yaml` |

**Rule 3 — Register an ontology term.**
Every new class should have a `class_uri:` pointing to a term in an established ontology (Voc4Cat, CHMO, OBI, NCIT, …). If no suitable term exists yet, use a provisional catcore-prefixed URI (`catcore:MyNewClass`) and open a Voc4Cat issue to request a proper term.

**Rule 4 — Declare slots in the right file.**
Slots used by exactly one class go in that class's subprofile file. Slots shared by two or more classes go in `catcore_common.yaml`.

**Rule 5 — Apply existing mixins before adding new slots.**
If your new class needs drying, calcination, precipitation, or thermal process parameters, apply the appropriate mixin rather than redeclaring those slots. Only add method-specific slots beyond what the mixin provides.

**Rule 6 — Mark obligation levels.**
Every slot in a new class should have either `required: true` (Mandatory), `recommended: true` (Recommended), or neither (Optional). Do not leave obligations implicit.

---

## Adding a preparation method

New catalyst synthesis routes are added to `catcore_synthesis_ap.yaml` as `PreparationMethod` subclasses.

### Step-by-step

**1. Identify which mixins apply.**

Before declaring any slots, check whether the method includes a drying step, calcination step, precipitation step, or generic thermal process. Apply all relevant mixins:

```yaml
MyNewMethod:
  is_a: PreparationMethod
  class_uri: voc4cat:XXXXXXX   # register a real term, or use catcore: prefix temporarily
  mixins:
    - DryingMixin              # if the method has a drying step
    - CalcinationMixin         # if the method has a calcination step
  description: |-
    Brief description of the preparation route.
```

**2. Add only method-specific slots.**

Slots already provided by mixins must not be redeclared. Only list slots that are unique to this method:

```yaml
  slots:
    - my_specific_parameter_a
    - my_specific_parameter_b
```

**3. Declare the new slots in the slots section.**

Add the slot definitions below the class definitions in the same file. Include `slot_uri`, `range`, `unit` (where applicable), and `multivalued: true`:

```yaml
slots:

  my_specific_parameter_a:
    description: What this parameter means and its typical range.
    range: float
    slot_uri: catcore:my_specific_parameter_a   # or a Voc4Cat / ontology URI
    multivalued: true
    unit:
      ucum_code: Cel   # use UCUM codes — e.g. Cel, h, mL/min, bar, g

  my_specific_parameter_b:
    description: What this parameter means.
    range: string
    slot_uri: catcore:my_specific_parameter_b
    multivalued: true
```

### Minimal complete example — PhotochemicalSynthesis

```yaml
PhotochemicalSynthesis:
  is_a: PreparationMethod
  class_uri: catcore:PhotochemicalSynthesis   # replace with Voc4Cat term when available
  mixins:
    - DryingMixin
  description: |-
    Catalyst preparation using light irradiation to drive photochemical
    reduction or deposition of an active phase onto a support.
  slots:
    - light_source
    - irradiation_wavelength
    - irradiation_duration
    - light_intensity

slots:

  light_source:
    description: Type of light source used (e.g. Xe lamp, UV-LED, solar simulator).
    range: string
    slot_uri: catcore:light_source
    multivalued: true

  irradiation_wavelength:
    description: Dominant wavelength of the irradiation source.
    range: float
    slot_uri: catcore:irradiation_wavelength
    multivalued: true
    unit:
      ucum_code: nm

  irradiation_duration:
    description: Total duration of light irradiation.
    range: float
    slot_uri: catcore:irradiation_duration
    multivalued: true
    unit:
      ucum_code: h

  light_intensity:
    description: Irradiance at the sample surface.
    range: float
    slot_uri: catcore:light_intensity
    multivalued: true
    unit:
      ucum_code: mW/cm2
```

---

## Adding a characterisation technique

New analytical techniques are added to `catcore_characterization_ap.yaml` as `CharacterizationTechnique` subclasses.

### Step-by-step

**1. Check available mixins for the technique.**

The characterisation subprofile provides these mixins — apply all that fit:

| Mixin | Covers |
|---|---|
| `XRaySourceMixin` | X-ray source type, anode, wavelength |
| `ElectronMicroscopyMixin` | Accelerating voltage, detector, magnification |
| `TemperatureProgramMixin` | Ramp rate, hold temperature, atmosphere |
| `ChromatographyMixin` | Column type, carrier gas, injection volume |
| `MassRangeMixin` | Mass range, ionisation mode, resolution |
| `PhotoluminescenceMixin` | Excitation wavelength, emission range |
| `ElectrochemistryMixin` | Scan rate, potential range, electrolyte |

**2. Declare the new class.**

```yaml
MyNewTechnique:
  is_a: CharacterizationTechnique
  class_uri: CHMO:XXXXXXX   # use a CHMO term where one exists
  mixins:
    - RelevantMixin
  description: |-
    What the technique measures and what information it provides about the catalyst.
  slots:
    - technique_specific_slot_a
```

**3. Declare technique-specific slots.**

Use the same pattern as for preparation method slots (see above). Place them in the `slots:` section of `catcore_characterization_ap.yaml`.

### Minimal complete example — NeutronDiffraction

```yaml
NeutronDiffraction:
  is_a: CharacterizationTechnique
  class_uri: CHMO:0000957
  description: |-
    Neutron powder diffraction for structure determination, particularly
    sensitive to light elements and magnetic ordering.
  slots:
    - neutron_wavelength
    - moderator_type
    - detector_coverage

slots:

  neutron_wavelength:
    description: Wavelength of the neutron beam.
    range: float
    slot_uri: catcore:neutron_wavelength
    multivalued: true
    unit:
      ucum_code: Ao   # Angstrom

  moderator_type:
    description: Type of neutron moderator (e.g. cold, thermal, hot source).
    range: string
    slot_uri: catcore:moderator_type
    multivalued: true

  detector_coverage:
    description: Angular range covered by the detector bank.
    range: float
    slot_uri: catcore:detector_coverage
    multivalued: true
    unit:
      ucum_code: deg
```

---

## Adding a reactor type

New reactor geometries or operating modes are added to `catcore_reaction_ap.yaml` as `ReactorDesignType` subclasses.

### Step-by-step

New reactor types are simpler than new preparation methods — there are currently no reactor-specific mixins, so you just add the class and any reactor-specific slots directly:

```yaml
MyNewReactor:
  is_a: ReactorDesignType
  class_uri: voc4cat:XXXXXXX
  description: |-
    Brief description of the reactor geometry and typical operating conditions.
  slots:
    - reactor_specific_slot_a
```

If the reactor shares parameters with an existing type (e.g. both are tubular flow reactors), consider whether a shared mixin should be introduced rather than duplicating slots.

### Minimal complete example — MonolithReactor

```yaml
MonolithReactor:
  is_a: ReactorDesignType
  class_uri: catcore:MonolithReactor   # replace with Voc4Cat term when available
  description: |-
    Monolith reactor — a reactor containing a structured monolithic substrate
    (ceramic or metallic) with parallel channels coated with catalyst.
  slots:
    - channel_density
    - washcoat_loading
    - monolith_material

slots:

  channel_density:
    description: Number of channels per unit cross-sectional area of the monolith.
    range: float
    slot_uri: catcore:channel_density
    multivalued: true
    unit:
      ucum_code: 1/cm2

  washcoat_loading:
    description: Mass of washcoat (catalyst layer) per unit volume of monolith.
    range: float
    slot_uri: catcore:washcoat_loading
    multivalued: true
    unit:
      ucum_code: g/L

  monolith_material:
    description: Material of the monolith substrate (e.g. cordierite, FeCrAlloy).
    range: string
    slot_uri: catcore:monolith_material
    multivalued: true
```

---

## Adding a simulation method

New computational approaches are added to `catcore_simulation_ap.yaml` as `SimulationMethod` subclasses.

### Step-by-step

**1. Check the `DFTSettingsMixin` if the method uses a plane-wave basis.**

The simulation subprofile provides `DFTSettingsMixin` (exchange-correlation functional, k-point mesh, energy cutoff, pseudopotential type) for DFT-based methods. If your new method is DFT-derived (e.g. DFT+U, hybrid-DFT, GW), apply this mixin.

**2. Declare the class and its specific slots.**

```yaml
MyNewSimulationMethod:
  is_a: SimulationMethod
  class_uri: NCIT:XXXXXXX   # or catcore: prefix temporarily
  mixins:
    - DFTSettingsMixin      # if DFT-based
  description: |-
    Description of the theoretical approach and its typical use cases in catalysis.
  slots:
    - method_specific_slot
```

### Minimal complete example — KineticMonteCarlo

```yaml
KineticMonteCarlo:
  is_a: SimulationMethod
  class_uri: catcore:KineticMonteCarlo
  description: |-
    Kinetic Monte Carlo simulation of surface reaction kinetics, using
    a reaction network of elementary steps with rate constants.
  slots:
    - reaction_network_size
    - simulation_time_kmc
    - surface_coverage_tracking

slots:

  reaction_network_size:
    description: Number of elementary reaction steps in the KMC reaction network.
    range: integer
    slot_uri: catcore:reaction_network_size
    multivalued: true

  simulation_time_kmc:
    description: Total simulated physical time of the KMC trajectory.
    range: float
    slot_uri: catcore:simulation_time_kmc
    multivalued: true
    unit:
      ucum_code: s

  surface_coverage_tracking:
    description: Species for which surface coverage is tracked as a function of time.
    range: string
    slot_uri: catcore:surface_coverage_tracking
    multivalued: true
```

---

## Adding a calculated property

New computed outputs are added to `catcore_simulation_ap.yaml` as `CalculatedProperty` subclasses.

```yaml
MyNewProperty:
  is_a: CalculatedProperty
  class_uri: catcore:MyNewProperty
  description: |-
    What physical or chemical quantity is computed and what it tells us about the catalyst.
  slots:
    - property_specific_slot
```

---

## Adding a shared slot

If a slot is needed by **two or more subprofiles**, declare it in `catcore_common.yaml` rather than in any individual subprofile. This keeps the schema DRY and avoids slot name collisions.

**Checklist before adding a slot to catcore_common:**

- [ ] The slot is genuinely needed in at least two different subprofile modules
- [ ] No existing slot in `catcore_common` covers the same concept
- [ ] The slot has a `slot_uri` pointing to an established ontology term (or a provisional catcore URI)
- [ ] A UCUM unit code is provided for all numeric slots

```yaml
# In catcore_common.yaml, under the slots: section:

my_shared_slot:
  description: What this parameter means, with any relevant units or value constraints.
  range: float
  slot_uri: catcore:my_shared_slot   # replace with ontology URI if available
  multivalued: true
  unit:
    ucum_code: mL/min
```

---

## Adding a mixin class

If a set of slots is shared across three or more classes in the same subprofile, consider factoring them into a new mixin. Mixins shared across two subprofiles should go in `catcore_common.yaml`.

```yaml
MyNewMixin:
  mixin: true
  description: |-
    Brief description of what process step or parameter group this mixin covers,
    and which classes are expected to use it.
  slots:
    - slot_a
    - slot_b
    - slot_c
```

Apply the mixin to a class via:

```yaml
SomeConcreteClass:
  is_a: PreparationMethod
  mixins:
    - MyNewMixin
```

!!! warning "Mixin scope"
    A mixin should cover a coherent, reusable process step — not an arbitrary collection of slots. If a set of slots is only needed by one class, declare the slots directly on that class rather than creating a mixin.

---

## 🔬 Deep dive: Extending the import hierarchy

!!! warning "Technical section"
    This section is for schema developers who need to introduce a new chemistry-layer or intermediate module between CoreMeta4Cat and DCAT-AP-PLUS. Most users extending the four pillars do not need this.

CoreMeta4Cat sits at the top of a layered import chain:

```
catcore.yaml  →  catcore_common.yaml  →  chem_dcat_ap  →  …  →  dcat_ap_plus
```

If you need to introduce a new intermediate chemistry layer (e.g. a `polymer_catalysis_ap` that adds polymer-specific base classes used across multiple pillars), add it between `catcore_common` and the first pillar that needs it. Import it in `catcore_common.yaml` via the `imports:` key, and document the new layer in the import hierarchy diagram in `catcore.yaml`.

Do not import new intermediate layers directly in individual pillar files — this would create hidden import order dependencies and make the schema harder to reason about.

---

## Checklist summary

Before submitting a pull request with a new extension:

- [ ] New class uses `is_a:` with the correct parent (see [General rules](#general-rules))
- [ ] `class_uri:` is set (Voc4Cat / ontology term, or `catcore:` placeholder with issue link)
- [ ] Existing mixins are applied before adding new slots
- [ ] Slots exclusive to this class are declared in the correct subprofile file
- [ ] Slots shared across subprofiles are declared in `catcore_common.yaml`
- [ ] All slots have `slot_uri:`, `range:`, `multivalued: true`
- [ ] Numeric slots have `unit: { ucum_code: ... }`
- [ ] Obligation levels are set (`required:` or `recommended:`) on all slots
- [ ] A brief description is provided on both the class and each new slot
- [ ] The schema validates with `gen-linkml` / `linkml-validate` before opening the PR
