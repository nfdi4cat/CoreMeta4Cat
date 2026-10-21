# CoreMeta4Cat

If you are a catalysis researcher, you have probably faced this at some point: you finish a project, archive your data, and six months later — or six years later — someone (including yourself) needs to make sense of it. What reactor was used? What were the exact feed conditions? What does "T" mean in this column? CoreMeta4Cat exists to prevent that problem by defining, in plain language, what information a catalysis dataset needs to include to be understood and reused by others.

**CoreMeta4Cat** is a community-driven metadata standard under [NFDI4Cat](https://nfdi4cat.org) that defines the minimum information required for reporting catalysis research data. Built on the [FAIR principles](https://www.go-fair.org/fair-principles/) — **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable — it provides a shared language for researchers to describe, share, and discover catalysis datasets across institutions and disciplines.

The model draws its terminology from [Voc4Cat](https://nfdi4cat.github.io/voc4cat/), NFDI4Cat's controlled vocabulary for catalysis, ensuring standardized semantic representation. Fields are classified as **Mandatory**, **Recommended**, or **Optional**, helping users meet minimum quality thresholds while leaving room for richer annotation.

> CoreMeta4Cat is a living standard. Community feedback — submitted via the **Submit Term Feedback** button — continuously shapes the addition, revision, and removal of data fields.

![CoreMeta4Cat model overview](images/CoreMeta4Cat_Picture.png)

---

## Not sure where to start?

The most up-to-date list of CoreMeta4Cat metadata fields for all four data classes — Synthesis, Characterization, Reaction, and Simulation — is available as a structured Excel workbook:

[⬇ Download the metadata list](https://nfdi4cat.github.io/CoreMeta4Cat/latest/assets/coremeta4cat_vocabulary.xlsx)

We are currently developing a user-friendly **Metadata Checker** tool that will make this process even easier — upload your dataset and the tool will automatically identify which required fields are present, which are missing, and give you a plain-language gap report with a downloadable template to act on. No schema knowledge required. The tool will be available here soon.

---

## Getting Started

Choose the approach that fits your workflow. Both paths are fully compatible with the CoreMeta4Cat standard.

## Excel Template

The quickest way to get started. Download the pre-structured Excel template, fill in your metadata fields, and submit or archive your dataset — no technical setup required.

**Best for:** Lab researchers, one-off submissions, teams new to structured metadata.

[→ head over to getting started](https://nfdi4cat.github.io/CoreMeta4Cat/latest/getting-started/#level-1-the-vocabulary-reference-workbook)

## LinkML Schema

Semantically enrich your data using the CoreMeta4Cat LinkML schema. Ideal for programmatic workflows, repository integration, and FAIR-compliant data pipelines.

- **[![](images/Synthesis.svg) Synthesis](#synthesis)**
- **[![](images/Characterization.svg) Characterization](#characterization)**
- **[![](images/Reaction.svg) Reaction](#reaction)**
- **[![](images/Simulation.svg) Simulation](#simulation)**

---

## Model Structure

CoreMeta4Cat is organized in two concentric layers. The **Inner CoreMeta4Cat** captures the essential metadata every catalysis dataset must provide. The **Expanded CoreMeta4Cat** adds four domain-specific groups covering the full research lifecycle.

### Inner CoreMeta4Cat

The inner layer defines mandatory baseline metadata, enabling consistent categorization and discoverability of research data across repositories.

| Field | Priority | Description |
|---|---|---|
| **Catalysis Research Field** | Mandatory | Type of catalysis: homogeneous, heterogeneous, electrocatalysis, hybrid, or other |
| **Reaction Type** | Mandatory | The catalytic reaction under investigation (e.g. hydrogenation, oxidation, hydroformylation) |
| **Active Site** | Recommended | Primary species responsible for catalytic activity — molecule, element, or other species |
| **Identifier** | Recommended | User-defined label(s) for identifying the catalyst |

---

## [Synthesis](https://nfdi4cat.github.io/CoreMeta4Cat/latest/synthesis/)

[![Synthesis logo](images/Synthesis.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/latest/synthesis)

The Synthesis metadata group defines the minimal information required to document how a catalyst is produced. It includes synthesis type, chemical components, process conditions, and preparative steps. As synthesis is fundamental to catalysis, these metadata help ensure reproducibility and provide context for how catalyst structure and performance arise from preparation methods.

## [Characterization](https://nfdi4cat.github.io/CoreMeta4Cat/latest/characterization/)

[![Characterization logo](images/Characterization.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/latest/characterization)

The Characterization metadata group specifies the information needed to describe the physical and chemical nature of a catalyst. It covers equipment, techniques, sample preparation, and detailed method-specific parameters (e.g., XRD, XAS, IR, Raman, NMR, GC-MS, TEM). By standardizing reporting across many analytical methods, it ensures catalyst properties are consistently documented and interpretable.

## [Reaction](https://nfdi4cat.github.io/CoreMeta4Cat/latest/reaction/)

[![Reaction logo](images/Reaction.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/latest/reaction)

The Reaction metadata group defines the minimum information required to describe the catalytic reaction under study and to evaluate catalyst performance. It captures essential parameters such as catalyst quantity, reactor design, reactants, operating conditions (temperature, pressure, atmosphere, feed composition), and product identification methods. These details ensure that catalytic experiments are transparent, comparable, and reproducible.

## [Simulation](https://nfdi4cat.github.io/CoreMeta4Cat/latest/simulation/)

[![Simulation logo](images/Simulation.svg)](https://nfdi4cat.github.io/CoreMeta4Cat/latest/simulation)

The Simulation metadata group specifies the essential information for reporting catalysis-related computational studies. It includes software used, simulation methods (DFT, molecular dynamics, microkinetics, Monte Carlo), conditions, and calculated properties such as thermodynamic stability, electronic structure, or kinetic parameters. These metadata ensure that theoretical insights are transparent, reproducible, and aligned with experimental research.

---

## Interactive diagram

[→ Explore the interactive metadata overview](assets/metadata_coremeta4cat_overview.html)
