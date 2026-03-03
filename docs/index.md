# CatCore

Catcore is a metadata collection for catalysis related research, which is intended to be developed into several schema's, such that we can harmonize Metadata representation of various research topics int the domain of catalysis.

As bepicted below, CatCore is devided into four major branches, Reaction, Synthesis, Characterisation and Simulation, each described with respective metadata terminology.


<div style="text-align: center;">
    <a>
    <img src="images/CoreMeta4Cat_Picture.png" alt="CatCore logo" style="width: 50%;">
    </a>
</div>

## [Reaction](reaction.md)

<div style="text-align: center;">
    <a href="reaction">
    <img src="images/Reaction.svg" alt="Reaction logo" style="width: 50%;">
    </a>
</div>

The Reaction metadata group defines the minimum information required to describe the catalytic reaction under study and to evaluate catalyst performance. It captures essential parameters such as catalyst quantity, reactor design, reactants, operating conditions (temperature, pressure, atmosphere, feed composition), and product identification methods. These details ensure that catalytic experiments are transparent, comparable, and reproducible.

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

## [Simulation](simulation.md)
<div style="text-align: center;">
    <a href="simulation">
    <img src="images/Simulation.svg" alt="Simulation logo" style="width: 50%;">
    </a>
</div>

The Simulation metadata group specifies the essential information for reporting catalysis-related computational studies. It includes software used, simulation methods (DFT, molecular dynamics, microkinetics, Monte Carlo), conditions, and calculated properties such as thermodynamic stability, electronic structure, or kinetic parameters. These metadata ensure that theoretical insights are transparent, reproducible, and aligned with experimental research.

## Interactive diagram

<iframe
    src="assets/metadata_collapsed_charts_all_sheets.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>

## Schema

The [Schema documentation](./elements/overview.md) for the metadata model written in LinkML Format can be found [here](elements/index.md)


