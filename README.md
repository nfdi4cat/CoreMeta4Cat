[![Build and test](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml)
[![Deploy docs](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/deploy-docs.yaml/badge.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20564227.svg)](https://doi.org/10.5281/zenodo.20564227)
[![Copier Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json)](https://github.com/linkml/linkml-project-copier)

# CoreMeta4Cat

**CoreMeta4Cat** is a shared metadata standard for catalysis research developed under [NFDI4Cat](https://www.nfdi4cat.de/). At its core, it answers questions that come up whenever catalysis datasets need to be shared, compared, or reused: *what information does a dataset need to include to be understood by someone outside your group?*

CoreMeta4Cat defines that minimum set of information — which fields are required, which are recommended, and which are optional — across four data classes: Synthesis, Characterization, Reaction, and Simulation. It builds on [DCAT-AP+](https://nfdi-de.github.io/dcat-ap-plus/) and [ChemDCAT-AP](https://nfdi-de.github.io/chem-dcat-ap/), and draws its terminology from [Voc4Cat](https://nfdi4cat.github.io/voc4cat/), NFDI4Cat's controlled vocabulary for catalysis.

> **Documentation:** [nfdi4cat.github.io/CoreMeta4Cat](https://nfdi4cat.github.io/CoreMeta4Cat/)

---

## Who is this for?

| I am… | Start here |
|---|---|
| A **researcher** who wants to check or improve the metadata in my dataset | [Download metadata list](https://nfdi4cat.github.io/CoreMeta4Cat/latest/assets/coremeta4cat_vocabulary.xlsx) · [Metadata Checker (in development)](#metadata-list-and-metadata-checker) |
| A **data steward** or repository manager | [Getting Started on the docs site](https://nfdi4cat.github.io/CoreMeta4Cat/latest/getting-started/) |
| A **developer** contributing to the schema or tooling | [Schema architecture](#schema-architecture) · [Developer tooling](#developer-tooling) |
| **New to CoreMeta4Cat** and just exploring | [Documentation site](https://nfdi4cat.github.io/CoreMeta4Cat/latest/) |

---


## Metadata list and Metadata Checker

The most up-to-date list of CoreMeta4Cat metadata fields for all four research domains — Synthesis, Characterization, Reaction, and Simulation — is available as a structured Excel workbook:

[⬇ Download the metadata list](https://nfdi4cat.github.io/CoreMeta4Cat/latest/assets/coremeta4cat_vocabulary.xlsx)

Each domain lists its fields grouped by priority (Mandatory, Recommended, Optional), with plain-language descriptions and links to controlled vocabulary terms where available. This is the right starting point if you want to understand what metadata your dataset should include.

We are also developing a **Metadata Checker**: an ELN-style form for entering and submitting new data along the CoreMeta4Cat fields, with feedback buttons for reporting problems with a field while you work. It is still in development and will be linked here once it is available.

---

## The four research domains

CoreMeta4Cat covers four domains of catalysis research. Each defines its own set of Mandatory, Recommended, and Optional metadata fields.

| Domain | What it covers |
|---|---|
| **Synthesis** | How a catalyst is prepared — precursors, preparation method, process conditions, and measured properties |
| **Characterization** | How a catalyst is analysed — technique, instrument, sample, and method-specific parameters |
| **Reaction** | How a catalytic experiment is run — reactor type, reactants, conditions, and product identification |
| **Simulation** | How a computational study is performed — software, method, conditions, and calculated properties |

Full field listings: [Synthesis](https://nfdi4cat.github.io/CoreMeta4Cat/latest/synthesis/) · [Characterization](https://nfdi4cat.github.io/CoreMeta4Cat/latest/characterization/) · [Reaction](https://nfdi4cat.github.io/CoreMeta4Cat/latest/reaction/) · [Simulation](https://nfdi4cat.github.io/CoreMeta4Cat/latest/simulation/)

---

## Vocabulary reference workbook

A structured Excel overview of all metadata fields — grouped by domain, colour-coded by Mandatory / Recommended / Optional — is available at [`docs/assets/coremeta4cat_vocabulary.xlsx`](docs/assets/coremeta4cat_vocabulary.xlsx).

This file is **generated automatically from the schema** and is intended as a reference and starting point, not a data entry form. The schema is the authoritative source; the workbook reflects it.

[⬇ Download the vocabulary workbook](https://nfdi4cat.github.io/CoreMeta4Cat/latest/assets/coremeta4cat_vocabulary.xlsx)

---

## Schema architecture

CoreMeta4Cat is implemented as a modular [LinkML](https://linkml.io/) schema:

```
coremeta4cat.yaml              ← top-level aggregator + CatalysisDataset
  └── coremeta4cat_common.yaml          ← shared slots and enumerations
        ├── coremeta4cat_synthesis_ap.yaml       ← Synthesis + preparation methods
        ├── coremeta4cat_characterization_ap.yaml ← Characterization + techniques
        ├── coremeta4cat_reaction_ap.yaml        ← Reaction + reactor types
        └── coremeta4cat_simulation_ap.yaml      ← Simulation + methods
```

The schema generates Python datamodels, OWL ontology, JSON-LD, and TypeScript representations automatically.

---

## Repository structure

```
src/coremeta4cat/
  schema/       ← LinkML schema modules (edit these)
  datamodel/    ← generated Python datamodels (do not edit)
scripts/
  generate_schema_docs.py  ← builds the interactive docs pages from schema
  generate_charts.py       ← builds sunburst hierarchy charts from schema
  schema_to_excel.py       ← exports schema → vocabulary workbook
  excel_to_schema.py       ← compares workbook against schema
docs/           ← MkDocs documentation source
tests/
  data/valid/   ← example YAML records used as unit tests
project/        ← generated artifacts (OWL, JSON-LD, TypeScript) — do not edit
```

---

## Developer tooling

| Tool | Purpose |
|---|---|
| [uv](https://docs.astral.sh/uv/) | Dependency management and virtual environments |
| [just](https://github.com/casey/just) | Command runner — run `just` to list all available recipes |
| [LinkML](https://linkml.io/) | Schema language and code generation |
| [pre-commit](https://pre-commit.com/) | Linting, formatting, and datamodel regeneration on commit |
| [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | Documentation site |

Key `just` commands:

```bash
just install         # install all dependencies
just test            # run schema validation + pytest + example tests
just gen-schema-docs # regenerate interactive documentation pages
just gen-charts      # regenerate sunburst hierarchy charts
just schema-to-excel # export schema to vocabulary workbook
just gen-doc         # regenerate MkDocs element pages
just site            # regenerate everything locally
```

---

## Contributing

We welcome contributions of all kinds — from term feedback and bug reports to schema extensions and documentation improvements.

See [CONTRIBUTING.md](CONTRIBUTING.md) for developer guidelines, or visit the [documentation](https://nfdi4cat.github.io/CoreMeta4Cat/contributing/) for a beginner-friendly introduction.

---

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
