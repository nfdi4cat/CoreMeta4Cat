# CoreMeta4Cat

**CoreMeta4Cat** is a community-driven metadata initiative under [NFDI4Cat](https://nfdi4cat.org) that defines the minimum information required for reporting catalysis research data. Built on the [FAIR principles](https://www.go-fair.org/fair-principles/) — **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable — it provides a shared language for researchers to describe, share, and discover catalysis datasets across institutions and disciplines.

The model draws its terminology from [Voc4Cat](https://nfdi4cat.github.io/voc4cat/), NFDI4Cat's controlled vocabulary for catalysis, ensuring standardized semantic representation. Fields are classified as **Mandatory**, **Recommended**, or **Optional**, helping users meet minimum quality thresholds while leaving room for richer annotation.

> CoreMeta4Cat is a living standard. Community feedback — submitted via the **Submit Term Feedback** button — continuously shapes the addition, revision, and removal of data fields.

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="images/CoreMeta4Cat_Picture.png" alt="CoreMeta4Cat model overview" style="width: 60%; border-radius: 8px;">
</div>

## Getting Started

Choose the approach that fits your workflow. Both paths are fully compatible with the CoreMeta4Cat standard.

<div class="grid" markdown>

<!-- Card 1: just text -->
<div class="card"  style="border: 1px solid #d0d7de; border-radius: 8px; padding: 1.5rem; background: #f6f8fa;" markdown>
## Excel Template

The quickest way to get started. Download the pre-structured Excel template, fill in your metadata fields, and submit or archive your dataset — no technical setup required.

**Best for:** Lab researchers, one-off submissions, teams new to structured metadata.

[→ head over to getting started ](getting-started.md#level-1-the-vocabulary-reference-workbook)
</div>

<!-- Card 2: text + nested 2x2 grid -->
<div class="card"  style="border: 1px solid #d0d7de; border-radius: 8px; padding: 1.5rem; background: #f6f8fa;" markdown>
## LinkML Schema

Semantically enrich your data using the CoreMeta4Cat LinkML schema. Ideal for programmatic workflows, repository integration, and FAIR-compliant data pipelines.

<div class="grid cards" style="color: #1a1a2e; background: #eef2fb; font-size: 0.9rem;" markdown>

- **[<img src="images/Synthesis.svg" width="30"> Synthesis](#synthesis)**

- **[<img src="images/Characterization.svg" width="30"> Characterization](#characterization)**

- **[<img src="images/Reaction.svg" width="30"> Reaction](#reaction)**

- **[<img src="images/Simulation.svg" width="30"> Simulation](#simulation)**
    
    

</div>
</div>
</div>


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

## [Synthesis](synthesis.md)
<div style="text-align: center;">
    <a href="synthesis">
    <img src="images/Synthesis.svg" alt="Synthesis logo" style="width: 50%;">
    </a>
</div>

The Synthesis metadata group defines the minimal information required to document how a catalyst is produced. It includes synthesis type, chemical components, process conditions, and preparative steps. As synthesis is fundamental to catalysis, these metadata help ensure reproducibility and provide context for how catalyst structure and performance arise from preparation methods.

## [Characterization](characterization.md)
<div style="text-align: center;">
    <a href="characterization">
    <img src="images/Characterization.svg" alt="Characterization logo" style="width: 50%;">
    </a>
</div>
The Characterization metadata group specifies the information needed to describe the physical and chemical nature of a catalyst. It covers equipment, techniques, sample preparation, and detailed method-specific parameters (e.g., XRD, XAS, IR, Raman, NMR, GC-MS, TEM). By standardizing reporting across many analytical methods, it ensures catalyst properties are consistently documented and interpretable.

## [Reaction](reaction.md)

<div style="text-align: center;">
    <a href="reaction">
    <img src="images/Reaction.svg" alt="Reaction logo" style="width: 50%;">
    </a>
</div>

The Reaction metadata group defines the minimum information required to describe the catalytic reaction under study and to evaluate catalyst performance. It captures essential parameters such as catalyst quantity, reactor design, reactants, operating conditions (temperature, pressure, atmosphere, feed composition), and product identification methods. These details ensure that catalytic experiments are transparent, comparable, and reproducible.

## [Simulation](simulation.md)
<div style="text-align: center;">
    <a href="simulation">
    <img src="images/Simulation.svg" alt="Simulation logo" style="width: 50%;">
    </a>
</div>

The Simulation metadata group specifies the essential information for reporting catalysis-related computational studies. It includes software used, simulation methods (DFT, molecular dynamics, microkinetics, Monte Carlo), conditions, and calculated properties such as thermodynamic stability, electronic structure, or kinetic parameters. These metadata ensure that theoretical insights are transparent, reproducible, and aligned with experimental research.

## Interactive diagram

<iframe
    src="assets/metadata_coremeta4cat_overview.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>

## Schema

The [Schema documentation](./elements/overview.md) for the metadata model written in LinkML Format can be found [here](elements/overview.md)


