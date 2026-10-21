---
title: Working with Data
description: Three real published datasets, described end-to-end with CoreMeta4Cat
---

# Working with Data

The rest of this documentation explains CoreMeta4Cat field by field. This page does the opposite: it shows three **complete, real** metadata records, built for datasets that are already published on [repository.nfdi4cat.org](https://repository.nfdi4cat.org) — NFDI4Cat's data repository (nicknamed "Repo4Cat"). Nothing here is a schema reference. It's meant to give you a feel for what a finished CoreMeta4Cat record actually looks like once real experimental data goes into it, so you have something concrete to compare your own dataset against.

If you're looking for the field-by-field reference instead, see [Catalysis Dataset](catalysis-dataset.md), [Design Patterns](design-patterns.md), or the [Schema Reference](elements/overview.md).

---

## How a CoreMeta4Cat record is organised

Every record answers the same handful of questions, in this order:

1. **What is this dataset, and who made it?** — a title, a description, the people who created it, and where the original files live (`id`, `title`, `description`, `creator`, `dataset_distribution`).
2. **What activities produced the data?** — was a catalyst synthesized (`Synthesis`)? Was something measured (`Characterization`)? Was something computed (`Simulation`)? These go under `was_generated_by`.
3. **What catalytic reaction is the dataset about?** — the reaction being studied, with its reactants, catalysts, conditions, and how products were identified. This goes under `is_about_activity`.
4. **What catalyst or material is the dataset about?** — `is_about_entity`.

A simple dataset might only need one of these (e.g. a pure simulation study skips reactions entirely). The three examples below all use several at once, because that's what the underlying experiments actually did — a catalyst was characterized by several techniques, then tested in a set of reactions.

Every example below is real, validated data: the three files are part of CoreMeta4Cat's own test suite (`tests/data/valid/`), so they're guaranteed to conform to the schema.

---

## Dataset 1 — CO/CO₂ methanation over nickel

<div style="border: 1px solid #d0d7de; border-radius: 8px; padding: 1.2rem 1.5rem; background: #f6f8fa; margin: 1rem 0;" markdown>

**[Dataset for Publication: Reaction Kinetics of CO and CO2 Methanation over Nickel](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/2d6m-exeb){:target="_blank"}**
Schmider, D.; Maier, L.; Deutschmann, O. (2025) — Institute for Catalysis Research and Technology (IKFT), KIT
Related publication: [Ind. Eng. Chem. Res. (2021), DOI 10.1021/acs.iecr.1c00389](https://doi.org/10.1021/acs.iecr.1c00389){:target="_blank"}

</div>

This dataset reports steady-state CO and CO₂ methanation kinetics measured over 16 different nickel catalysts (varying support — Al₂O₃, SiO₂, ZrO₂, TiO₂, MgAl₂O₄ — and nickel loading from 5 to 41 wt%) in fixed-bed reactors. The 16 runs split into three reaction types depending on the feed gas: CO methanation, CO₂ methanation, and a mixed CO/CO₂ feed.

The CoreMeta4Cat record groups this into:

- **1 `Characterization`** (`was_generated_by`) — the outlet gas composition analysis used for every run, since it's the same analytical method throughout.
- **3 `CatalyticReaction`s** (`is_about_activity`) — one per reaction type (CO methanation, CO₂ methanation, mixed feed), each listing all the catalysts tested under that feed and the temperature range explored.

Grouping by reaction type and technique, rather than writing one entry per catalyst, keeps the record's length proportional to how the underlying study is actually organised — 4 pieces instead of 16.

<div style="text-align: center; margin: 1.2em 0;">
  <a href="../assets/examples/CatalysisDataset-2d6m-exeb.yaml"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download YAML
  </a>
  <a href="../assets/examples/CatalysisDataset-2d6m-exeb.json"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download JSON
  </a>
  <a href="../assets/examples/CatalysisDataset-2d6m-exeb.ttl"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download RDF
  </a>
</div>

---

## Dataset 2 — Phosphorus-modified Pd catalysts for selective hydrogenation

<div style="border: 1px solid #d0d7de; border-radius: 8px; padding: 1.2rem 1.5rem; background: #f6f8fa; margin: 1rem 0;" markdown>

**[Support Engineering with Phosphorus: Tuning the Palladium-Catalyzed Selective Hydrogenation of α,β-Unsaturated Aldehydes](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/32x1-99x6){:target="_blank"}**
Rang, F.; Hanf, S.; Holtermann, B.; Eggeler, Y.; Barth, S.; Grunwaldt, J.-D. (2026) — KIT

</div>

This dataset investigates how phosphorus-modification of the support tunes Pd-catalyzed selective hydrogenation, across 10 Pd/P catalysts (Al₂O₃ and SiO₂ supports, 0–5 wt% phosphorus). It combines five characterization techniques with catalytic testing of two substrates (cinnamyl alcohol and citral) across both supports.

The CoreMeta4Cat record groups this into:

- **5 `Characterization`s** (`was_generated_by`) — one per technique (BET, ICP-AES, PXRD, DRIFT, IR), each covering every catalyst that technique was applied to.
- **4 `CatalyticReaction`s** (`is_about_activity`) — one per substrate/support combination (cinnamyl alcohol × Al₂O₃, cinnamyl alcohol × SiO₂, citral × Al₂O₃, citral × SiO₂).

<div style="text-align: center; margin: 1.2em 0;">
  <a href="../assets/examples/CatalysisDataset-32x1-99x6.yaml"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download YAML
  </a>
  <a href="../assets/examples/CatalysisDataset-32x1-99x6.json"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download JSON
  </a>
  <a href="../assets/examples/CatalysisDataset-32x1-99x6.ttl"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download RDF
  </a>
</div>

---

## Dataset 3 — Palladium phosphide catalysts for carbonylation

<div style="border: 1px solid #d0d7de; border-radius: 8px; padding: 1.2rem 1.5rem; background: #f6f8fa; margin: 1rem 0;" markdown>

**[Carbonylation catalysis of aryl halides through active-site engineering](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/arp5-s69r){:target="_blank"}**
Neyyathala, A.; Jung, F.; Feldmann, C.; Barth, S.; Grunwaldt, J.-D.; Jevtovik, I.; Schunk, S. A.; Dolcet, P.; Gross, S.; Hanf, S. (2025) — KIT and collaborators

</div>

This dataset compares a phosphorus-modified palladium phosphide catalyst (Pd₃P/SiO₂) against an unmodified Pd/SiO₂ reference, across 31 batch-reactor carbonylation runs — mostly alkoxycarbonylation of aryl iodides (varying reaction time, base, temperature, and substrate), plus a handful of phenoxy- and aminocarbonylation runs. It's characterized by five different techniques, including two additional Pd₃P/SiO₂ loading variants only seen in the PXRD data, and a recycled/spent catalyst sample only seen in the STEM data.

The CoreMeta4Cat record groups this into:

- **5 `Characterization`s** (`was_generated_by`) — PXRD, DRIFT, CO chemisorption, XPS, STEM.
- **3 `CatalyticReaction`s** (`is_about_activity`) — one per reaction type (alkoxycarbonylation, phenoxycarbonylation, aminocarbonylation).

<div style="text-align: center; margin: 1.2em 0;">
  <a href="../assets/examples/CatalysisDataset-arp5-s69r.yaml"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download YAML
  </a>
  <a href="../assets/examples/CatalysisDataset-arp5-s69r.json"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download JSON
  </a>
  <a href="../assets/examples/CatalysisDataset-arp5-s69r.ttl"
     style="display: inline-block; padding: 0.6em 1.4em; background: #1976d2; color: white;
            border-radius: 4px; text-decoration: none; font-weight: bold; margin: 0.3em;">
    ⬇ Download RDF
  </a>
</div>

---

## A note on grouping

None of these three datasets describe just one catalyst measured once. Real studies screen many catalysts, or run the same technique across a whole series. Writing one `Characterization` per catalyst, or one `CatalyticReaction` per experimental run, would make the record balloon to dozens of near-identical entries.

All three examples above instead group by **what was actually shared**: one `Characterization` per analytical technique (covering every sample that technique was applied to), and one `CatalyticReaction` per reaction type or substrate/condition combination (covering every catalyst tested under it, with things like temperature expressed as the range explored rather than one value per run). This keeps a record's size proportional to the *number of distinct methods and reaction types* in a study, not the number of individual data points — which is usually a much smaller number.

---

## Next steps

- **See the field-by-field reference** for `CatalysisDataset` → [Catalysis Dataset](catalysis-dataset.md)
- **Understand the four pillars** (Synthesis, Characterization, Reaction, Simulation) → [Design Patterns](design-patterns.md)
- **Start from your own spreadsheet** → [Getting Started](getting-started.md)
- **Browse every field CoreMeta4Cat defines** → [Schema Reference](elements/overview.md)
