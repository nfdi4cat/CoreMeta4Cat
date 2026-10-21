---
title: CatalysisDataset
description: The entry-point class, its global classification enum, and how to combine multiple pillars into one dataset
---

# CatalysisDataset

`CatalysisDataset` is the entry point for every CoreMeta4Cat record. It is a `dcat:Dataset` -- fully compatible with plain DCAT and DCAT-AP -- extended with a global classification field and four link slots that connect to the [four CoreMeta4Cat pillars](design-patterns.md#the-four-pillars): [Synthesis](synthesis.md), [Characterization](characterization.md), [Reaction](reaction.md), and [Simulation](simulation.md).

This page is the reference for `CatalysisDataset` itself: its fields, the `CatalysisResearchFieldEnum` classification vocabulary, and a worked example of combining several pillars into a single dataset. For the conceptual background on *why* it's structured this way, see [Design Patterns: The entry point](design-patterns.md#the-entry-point-catalysisdataset) and [Pattern 1: Classification via rdf_type](design-patterns.md#pattern-1-classification-via-rdf_type).

## Fields

`CatalysisDataset` has four fields beyond the ones it inherits from `dcat:Dataset` (`id`, `title`, `description`, ...):

| Field | Range | Cardinality | Purpose |
|---|---|---|---|
| `rdf_type` | `CatalysisResearchFieldEnum` (via `bindings`) | Recommended | **Layer 1** -- the coarsest possible classification: which field of catalysis this dataset belongs to. |
| `was_generated_by` | `DataGeneratingActivity` | Recommended, Multivalued | **Layer 2** -- the activity/activities that *produced* this dataset's data: `Synthesis`, `Characterization`, and/or `Simulation` instances. |
| `is_about_activity` | `EvaluatedActivity` | Recommended, Multivalued | **Layer 2** -- the catalytic `Reaction` this dataset is *about*, without having generated it. |
| `is_about_entity` | `EvaluatedEntity` | Recommended, Multivalued | **Layer 2** -- the catalyst sample or material this dataset concerns. |

All four are Recommended, not Mandatory: a dataset can legitimately carry only a subset (e.g. a pure simulation dataset has no `is_about_entity`).

## Layer 1: classifying the research field

`rdf_type` on `CatalysisDataset` is not a free-form slot -- its value is constrained to `CatalysisResearchFieldEnum` via a [DCAT-AP-PLUS Pattern 3 `bindings` block](design-patterns.md#pattern-1-classification-via-rdf_type) rather than by adding a dedicated new slot. This keeps `CatalysisDataset` a drop-in `dcat:Dataset` (any DCAT-AP tool can still read `rdf_type`) while giving CoreMeta4Cat tooling a controlled, machine-actionable value to filter and facet on.

```yaml
rdf_type:
  id: VOC4CAT:0007001
  title: "heterogeneous catalysis"
```

**`CatalysisResearchFieldEnum` permissible values:**

| Value | Voc4Cat term | Description |
|---|---|---|
| `heterogeneous_catalysis` | `VOC4CAT:0007001` | Catalyst and reactants are in different phases. |
| `homogeneous_catalysis` | `VOC4CAT:0000294` | Catalyst and reactants are in the same phase. |
| `biocatalysis` | `VOC4CAT:0000204` | Use of enzymes or whole cells as catalysts. |
| `electrocatalysis` | `VOC4CAT:0000216` | Catalysis of electrochemical reactions. |
| `photocatalysis` | `VOC4CAT:0000001` | Catalysis driven by absorption of light energy by a photocatalyst. |
| `hybrid_catalysis` | -- | Combination of two or more of the above approaches. |
| `other` | -- | Any catalysis research field not covered by the terms above. |

This is a dataset-wide, single classification axis -- it says nothing about *how* a specific reaction was run. That's a separate, per-reaction concern: `CatalyticReaction.catalyst_type` uses the same `CatalysisResearchFieldEnum` values to record the catalytic regime of one particular reaction (see [Reaction: catalyst_type](reaction.md)), independent of whatever this dataset's own `rdf_type` says. A heterogeneous-catalysis dataset (`rdf_type`) can, for instance, still contain a reaction step run under homogeneous conditions as a control experiment (`catalyst_type`) -- the two fields are deliberately decoupled.

## Layer 2: linking the pillars

Layer 2 is where a `CatalysisDataset` actually points at the substance of the record. Three slots cover it, and all three are multivalued -- a single dataset can reference several activities of the same kind at once (e.g. two separate `Characterization` runs):

- **`was_generated_by`** -- activities that *produced* this dataset's data. Only `Synthesis`, `Characterization`, and `Simulation` make sense here, since only they are `DataGeneratingActivity` subclasses.
- **`is_about_activity`** -- the catalytic process this dataset *describes*, without having generated it. `Reaction` (schema name `CatalyticReaction`) is not a `DataGeneratingActivity` -- see the [🔬 deep dive on this distinction](design-patterns.md#deep-dive-the-evaluatedactivity-distinction) -- so it is linked here instead of via `was_generated_by`.
- **`is_about_entity`** -- the catalyst sample or material the dataset concerns, independent of which activity produced or observed it.

## Combining multiple pillars into one dataset

A single `CatalysisDataset` is not limited to one pillar. The most common real-world case spans several: a catalyst is synthesized, then tested in a reaction, and both the catalyst itself and the reaction products are separately characterized afterwards. All of that can live in one dataset, because `was_generated_by` and `is_about_activity` are both multivalued.

The example below reports the full lifecycle of a Ni/CeO2 catalyst used for dry methane reforming (DRM): synthesis, the catalytic reaction, characterization of the catalyst (post-synthesis XRD), and characterization of the reaction products (a dedicated GC-MS run, separate from the inline `product_identification_method` recorded on the `Reaction` itself).

```yaml
id: "coremeta4cat:DATASET_001_NiCeO2_DRM"
type: CatalysisDataset

# Layer 1 -- global classification
rdf_type:
  id: VOC4CAT:0007001
  title: "heterogeneous catalysis"

# Layer 2 -- three activities produced this dataset's data...
was_generated_by:
  - id: "coremeta4cat:SYN_001_NiCeO2"
    type: Synthesis
    rdf_type:
      id: VOC4CAT:0007016
      title: "impregnation"
    nominal_composition: "10wt% Ni/CeO2"
    had_output_entity:
      - id: "coremeta4cat:CAT_002_NiCeO2"
        type: CatalystSample
        title: "Ni/CeO2"

  - id: "coremeta4cat:CHAR_001_NiCeO2_XRD"
    type: Characterization
    rdf_type:
      id: CHMO:0000158
      title: "powder X-ray diffraction"
    evaluated_entity:
      id: "coremeta4cat:CAT_002_NiCeO2"    # same catalyst sample as above
    realized_plan:
      type: PowderXRD

  - id: "coremeta4cat:CHAR_002_DRM_products_GCMS"
    type: Characterization
    rdf_type:
      id: CHMO:0000497
      title: "gas chromatography-mass spectrometry"
    evaluated_entity:
      id: "coremeta4cat:REAC_002_DRM_NiCeO2"    # evaluating the reaction's products
    realized_plan:
      type: GCMS

# ...and one Reaction is what this dataset is about, not what generated it
is_about_activity:
  - id: "coremeta4cat:REAC_002_DRM_NiCeO2"
    type: CatalyticReaction
    used_catalyst:
      id: "coremeta4cat:CAT_002_NiCeO2"     # same catalyst sample again
    catalyst_type:
      - "heterogeneous_catalysis"

is_about_entity:
  - id: "coremeta4cat:CAT_002_NiCeO2"
```

A few things worth noticing in this example:

- The same `CatalystSample` (`CAT_002_NiCeO2`) is referenced from four places: the `Synthesis` that produced it (`had_output_entity`), the `Characterization` that measured it directly (`evaluated_entity`), the `Reaction` that consumed it (`used_catalyst`), and the dataset's own `is_about_entity`. This is what actually connects the four pillars into one coherent record -- shared identifiers, not schema-level nesting.
- The second `Characterization` (`CHAR_002_DRM_products_GCMS`) sets `evaluated_entity` to the *Reaction*, not the catalyst -- because what's being measured there is the reaction's product stream, not the catalyst material. `evaluated_entity` accepts any `EvaluatedEntity`, and a `CatalyticReaction`'s outputs qualify.
- `catalyst_type` on the `Reaction` and `rdf_type` on the `CatalysisDataset` both draw from `CatalysisResearchFieldEnum`, but independently -- see the note at the end of the Layer 1 section above.
- For a real submission, each of `SYN_001_NiCeO2`, `CHAR_001_NiCeO2_XRD`, `CHAR_002_DRM_products_GCMS`, and `REAC_002_DRM_NiCeO2` would carry their own full set of Mandatory/Recommended fields (method parameters, instrument settings, operating conditions, ...); this example only shows the fields relevant to how the four pillars connect. See [Synthesis](synthesis.md), [Characterization](characterization.md), and [Reaction](reaction.md) for the full field lists of each.
