---
title: CoreMeta4Cat Users
description: Projects, repositories, and communities that adopt CoreMeta4Cat
---

# CoreMeta4Cat Users

This page lists projects, data repositories, and communities that have adopted CoreMeta4Cat as their metadata standard. It is also the right place to understand how CoreMeta4Cat fits into the broader NFDI4Cat research data infrastructure.

<div style="text-align: center;">
    <a>
    <img src="/CoreMeta4Cat/images/CoreMeta4Cat_Picture.png" alt="CoreMeta4Cat logo" style="width: 40%;">
    </a>
</div>

---

## NFDI4Cat

<div style="text-align: center;">
    <a>
    <img src="/CoreMeta4Cat/images/nfdi4cat-logo.png" alt="nfdi4cat-logo" style="width: 40%;">
    </a>
</div>

CoreMeta4Cat is developed within the [NFDI4Cat](https://nfdi4cat.org) initiative — the National Research Data Infrastructure consortium for catalysis sciences in Germany. NFDI4Cat brings together universities, research institutions, and industrial partners to build shared data infrastructure for the catalysis community.

CoreMeta4Cat is the community-driven metadata model proposed within this framework, designed to enable semantically enriched, interoperable catalysis data across experimental, computational, and digitally curated research workflows.

---

## Are you using CoreMeta4Cat?

If your project, repository, or tool uses CoreMeta4Cat, we would love to list it here. Please open an issue or pull request on the [CoreMeta4Cat GitHub repository](https://github.com/HendrikBorgelt/CoreMeta4Cat) with the following information:

| Field | What to provide |
|---|---|
| **Project name** | The name of the project, repository, or tool |
| **Organisation** | The institution or consortium responsible |
| **Description** | One or two sentences on how CoreMeta4Cat is used |
| **Link** | A URL to the project, dataset collection, or publication |
| **Contact** | An optional name or email for follow-up |

---

## Scope of adoption

CoreMeta4Cat is designed to be adopted at different levels, depending on the use case:

**Metadata collection and submission**
Research groups can use CoreMeta4Cat to structure the metadata they report alongside published datasets, whether in institutional repositories, domain repositories, or supplementary materials of publications.

**Repository integration**
Data repository operators can implement CoreMeta4Cat as their metadata intake schema, enabling structured, validated metadata submission from depositing researchers. The LinkML source generates SHACL shapes, JSON Schema, and Python/Pydantic classes out of the box, making integration straightforward.

**Workflow tools and ELNs**
Electronic lab notebooks (ELNs) and data management tools used in catalysis labs can map their internal data models to CoreMeta4Cat, enabling automatic metadata export in a standardised format.

**Knowledge graph and semantic web applications**
Because CoreMeta4Cat maps every class and slot to established ontology terms (Voc4Cat, CHMO, OBI, NCIT, …), instance data can be exported as RDF and loaded into a triple store or knowledge graph for semantic querying across datasets.

---

## Related resources

| Resource | Description |
|---|---|
| [Voc4Cat](https://nfdi4cat.github.io/voc4cat/) | The NFDI4Cat controlled vocabulary, used for `rdf_type` classification terms throughout CoreMeta4Cat |
| [DCAT-AP-PLUS](https://nfdi-de.github.io/dcat-ap-plus/dev/) | The base provenance layer that CoreMeta4Cat extends |
| [LinkML](https://linkml.io/) | The schema language and tooling used to define and validate CoreMeta4Cat |
| [CoreMeta4Cat on GitHub](https://github.com/HendrikBorgelt/CoreMeta4Cat) | Schema source files, issue tracker, and contribution guide |
