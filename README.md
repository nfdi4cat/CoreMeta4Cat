[![Build and test](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml)
[![Deploy docs](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/deploy-docs.yaml/badge.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/)
[![Copier Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json)](https://github.com/linkml/linkml-project-copier)

# CoreMeta4Cat

**CoreMeta4Cat** is a community-driven metadata standard for catalysis research, developed under [NFDI4Cat](https://www.nfdi4cat.de/). It defines the minimum information required to describe, share, and discover catalysis datasets in a FAIR-compliant way — Findable, Accessible, Interoperable, and Reusable.

CoreMeta4Cat extends [DCAT-AP+](https://nfdi-de.github.io/dcat-ap-plus/) and [ChemDCAT-AP](https://nfdi-de.github.io/chem-dcat-ap/), adding catalysis-specific metadata fields on top of their shared data model. Terminology is drawn from [Voc4Cat](https://nfdi4cat.github.io/voc4cat/), NFDI4Cat's controlled vocabulary for catalysis. Fields are classified as Mandatory, Recommended, or Optional.

> **Documentation:** [nfdi4cat.github.io/CoreMeta4Cat](https://nfdi4cat.github.io/CoreMeta4Cat/)

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

The schema generates Python datamodels, OWL ontology, JSON-LD, and TypeScript representations automatically. Explore the four data classes in the documentation:
[Synthesis](https://nfdi4cat.github.io/CoreMeta4Cat/synthesis/) ·
[Characterization](https://nfdi4cat.github.io/CoreMeta4Cat/characterization/) ·
[Reaction](https://nfdi4cat.github.io/CoreMeta4Cat/reaction/) ·
[Simulation](https://nfdi4cat.github.io/CoreMeta4Cat/simulation/)

---

## Vocabulary reference workbook

A structured Excel overview of all metadata fields (grouped by data class, colour-coded by M/R/O) is available at [`docs/assets/coremeta4cat_vocabulary.xlsx`](docs/assets/coremeta4cat_vocabulary.xlsx). This file is generated automatically from the schema — the schema is the authoritative source.

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
