---
title: Community datasets
description: Six real published datasets, described end-to-end with CoreMeta4Cat
---

# Community datasets

This page shows six **complete, real** metadata records, built for datasets that are published
on [repository.nfdi4cat.org](https://repository.nfdi4cat.org), NFDI4Cat's data repository
("Repo4Cat"). Nothing here is a schema reference. Each record shows what a finished CoreMeta4Cat
description looks like once real data goes into it, so you have something concrete to compare
your own dataset against.

All six records are part of CoreMeta4Cat's test suite (`tests/data/valid/`), so they are validated
against the schema on every change. The [usage patterns](usage-patterns.md) are small excerpts of
these records.

| # | Dataset | Field | Activities in the record | Sources |
|---|---|---|---|---|
| 1 | [CO/CO₂ methanation over nickel](#2d6m-exeb) | heterogeneous catalysis | 1 characterization, 3 reactions | deposit |
| 2 | [P-modified Pd catalysts for selective hydrogenation](#32x1-99x6) | heterogeneous catalysis | 5 characterizations, 4 reactions | deposit |
| 3 | [Palladium phosphide catalysts for carbonylation](#arp5-s69r) | heterogeneous catalysis | 5 characterizations, 3 reactions | deposit |
| 4 | [Cu–Ga–Al mixed oxides for CO₂ to methanol/DME](#6mxw-xsrd) | heterogeneous catalysis, DFT, ML potentials | 4 syntheses, 1 characterization, 3 simulations, 2 reactions | deposit + article |
| 5 | [NH₃ decomposition over Ru/Ni-BCZY](#b74m-m6rp) | heterogeneous catalysis, microkinetics | 2 syntheses, 1 characterization, 2 simulations, 1 reaction | deposit + article |
| 6 | [Amine transaminase molecular dynamics](#8ppb-aeky) | biocatalysis, simulation | 4 simulations | deposit + article |

"Deposit + article" means the repository files alone did not contain everything CoreMeta4Cat
asks for. The missing pieces (synthesis routes, instruments, software, reactor) came from the
publication.

---

## Dataset 1 — CO/CO₂ methanation over nickel { #2d6m-exeb }

!!! abstract ""

    **[Dataset for Publication: Reaction Kinetics of CO and CO2 Methanation over Nickel](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/2d6m-exeb){:target="_blank"}**
    Schmider, D.; Maier, L.; Deutschmann, O. (2025) — Institute for Catalysis Research and Technology (IKFT), KIT
    Related publication: [Ind. Eng. Chem. Res. (2021), doi:10.1021/acs.iecr.1c00389](https://doi.org/10.1021/acs.iecr.1c00389){:target="_blank"}

This dataset reports steady-state CO and CO₂ methanation kinetics measured over 16 nickel
catalysts (supports Al₂O₃, SiO₂, ZrO₂, TiO₂ and MgAl₂O₄; nickel loading 5–41 wt%) in fixed-bed
reactors. The 16 runs split into three reaction types depending on the feed: CO methanation, CO₂
methanation, and a mixed CO/CO₂ feed.

The CoreMeta4Cat record groups this into:

- **1 `Characterization`** (`was_generated_by`): the outlet gas analysis used for every run.
- **3 `CatalyticReaction`s** (`is_about_activity`): one per reaction type, each listing all
  catalysts tested under that feed and the temperature range explored.

Grouping by reaction type and technique keeps the record proportional to how the study is
organised: 4 pieces instead of 16.

**Patterns from this dataset:** [Classifying with vocabulary terms](usage-patterns.md#vocabulary-terms)

[:material-download: YAML](../assets/examples/CatalysisDataset-2d6m-exeb.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-2d6m-exeb.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-2d6m-exeb.ttl){ .md-button }

---

## Dataset 2 — Phosphorus-modified Pd catalysts for selective hydrogenation { #32x1-99x6 }

!!! abstract ""

    **[Support Engineering with Phosphorus: Tuning the Palladium-Catalyzed Selective Hydrogenation of α,β-Unsaturated Aldehydes](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/32x1-99x6){:target="_blank"}**
    Rang, F.; Hanf, S.; Holtermann, B.; Eggeler, Y.; Barth, S.; Grunwaldt, J.-D. (2026) — KIT

This dataset investigates how phosphorus modification of the support tunes Pd-catalyzed
selective hydrogenation, across 10 Pd/P catalysts (Al₂O₃ and SiO₂ supports, 0–5 wt% P). It
combines five characterization techniques with catalytic testing of two substrates (cinnamyl
alcohol and citral) on both supports.

The CoreMeta4Cat record groups this into:

- **5 `Characterization`s** (`was_generated_by`): one per technique (BET, ICP-AES, PXRD, DRIFT,
  IR), each covering every catalyst that technique was applied to.
- **4 `CatalyticReaction`s** (`is_about_activity`): one per substrate and support.

**Patterns from this dataset:** [One technique, many samples](usage-patterns.md#characterization-many-samples)

[:material-download: YAML](../assets/examples/CatalysisDataset-32x1-99x6.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-32x1-99x6.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-32x1-99x6.ttl){ .md-button }

---

## Dataset 3 — Palladium phosphide catalysts for carbonylation { #arp5-s69r }

!!! abstract ""

    **[Carbonylation catalysis of aryl halides through active-site engineering](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/arp5-s69r){:target="_blank"}**
    Neyyathala, A.; Jung, F.; Feldmann, C.; Barth, S.; Grunwaldt, J.-D.; Jevtovik, I.; Schunk, S. A.; Dolcet, P.; Gross, S.; Hanf, S. (2025) — KIT and collaborators

This dataset compares a phosphorus-modified palladium phosphide catalyst (Pd₃P/SiO₂) with an
unmodified Pd/SiO₂ reference across 31 batch-reactor carbonylation runs, mostly
alkoxycarbonylation of aryl iodides plus a few phenoxy- and aminocarbonylation runs. It is
characterized by five techniques; PXRD also covers two further loading variants, and STEM a spent
catalyst.

The CoreMeta4Cat record groups this into:

- **5 `Characterization`s** (`was_generated_by`): PXRD, DRIFT, CO chemisorption, XPS, STEM.
- **3 `CatalyticReaction`s** (`is_about_activity`): one per reaction type.

[:material-download: YAML](../assets/examples/CatalysisDataset-arp5-s69r.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-arp5-s69r.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-arp5-s69r.ttl){ .md-button }

---

## Dataset 4 — Cu–Ga–Al mixed oxides for CO₂ to methanol and DME { #6mxw-xsrd }

!!! abstract ""

    **[Copper Gallium Aluminum Mixed Metal Oxides as Alternative Catalyst Candidates for Efficient Conversion of Carbon Dioxide to Methanol and Dimethyl Ether](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/6mxw-xsrd){:target="_blank"}**
    Weber, S. (2025) — hte GmbH
    Related publication: [Weber et al., ACS Catal. 2025, 15, 18857, doi:10.1021/acscatal.5c03876](https://doi.org/10.1021/acscatal.5c03876){:target="_blank"}

This study combines computational screening with synthesis and high-throughput testing. DFT and
two machine-learned interatomic potentials (an Open Catalyst Project model and MACE-MPA-0) give
OH and CO binding energies for doped oxide sites and 37 intermetallic compositions. 76 Cu–Ga–Al
hydrotalcite precursors are co-precipitated and analysed by XRF; 13 of them are screened for CO₂/CO
hydrogenation, and seven optimized catalysts are tested under 17 conditions at 80 bar in a 16-fold
fixed-bed reactor.

The CoreMeta4Cat record groups this into:

- **4 `Synthesis`** (`was_generated_by`): the co-precipitation route (with the article's worked
  example), the first-generation catalyst, and the second-generation catalyst in two chained
  steps (co-precipitation, then Ga impregnation).
- **1 `Characterization`**: XRF of the precursor library.
- **3 `Simulation`s**: DFT binding energies and the two machine-learned-potential screenings.
- **2 `CatalyticReaction`s** (`is_about_activity`): the 13-sample screening and the tests of the
  optimized catalysts.

**Sources:** the deposit has the computed binding energies, compositions and the test protocol;
synthesis route, instruments, reactor and DFT code come from the article. Not stated in either:
precursor masses except for one worked example, and the product analysis method (presumably in
the article's supporting information). Both fields are recommended, so the record is valid
without them.

**Patterns from this dataset:**
[A synthesis with precursors, amounts and a typed preparation method](usage-patterns.md#synthesis-coprecipitation) ·
[A preparation in two steps](usage-patterns.md#synthesis-multi-step) ·
[A simulation with a typed method and calculated properties](usage-patterns.md#simulation-dft-properties)

[:material-download: YAML](../assets/examples/CatalysisDataset-6mxw-xsrd.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-6mxw-xsrd.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-6mxw-xsrd.ttl){ .md-button }

---

## Dataset 5 — NH₃ decomposition over Ru/Ni-BCZY, experiment and microkinetics { #b74m-m6rp }

!!! abstract ""

    **[Dataset for Publication: Experimental and Microkinetic Investigation of Thermo-Catalytic Ammonia Decomposition over a Ba-promoted Ru/Ni-BCZY Catalyst for Use in Ammonia-fed Protonic Ceramic Cells](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/b74m-m6rp){:target="_blank"}**
    Davari, S.; Chacko, R.; Bastek, T.; Lott, P.; Dailly, J.; Angeli, S.; Deutschmann, O. (2025) — KIT and EIFER
    Related publication: [Davari et al., Appl. Catal. A 708 (2025) 120571, doi:10.1016/j.apcata.2025.120571](https://doi.org/10.1016/j.apcata.2025.120571){:target="_blank"}

Six Ru/Ba catalysts on Ni-BCZY, Ni-YSZ and YSZ supports are tested for thermocatalytic NH₃
decomposition as light-off curves in a packed bed (500–3000 ppm NH₃ in Ar, 1 bar, GHSV
50,000 h⁻¹). A microkinetic packed-bed model (DETCHEM) is fitted to the experiments and then used
for reactor profiles, turnover frequencies and a parameter study.

The CoreMeta4Cat record groups this into:

- **2 `Synthesis`** (`was_generated_by`): the cermet supports (tape casting and sintering), then
  Ru and Ba by incipient wetness impregnation.
- **1 `Characterization`**: H₂-TPR of the Ni-BCZY cermet.
- **2 `Simulation`s**: the microkinetic model compared with the experiments, and the parameter
  study.
- **1 `CatalyticReaction`** (`is_about_activity`): the light-off experiments of all six
  catalysts.

**Sources:** the deposit has the light-off curves and simulation results, organised by figure;
catalysts, reactor, analyser, software and the TPR conditions come from the article. Not stated:
precursor masses (the article gives target loadings).

**Patterns from this dataset:**
[A dataset, its classification and its activities](usage-patterns.md#dataset-entry-point) ·
[A measurement with a typed technique](usage-patterns.md#characterization-typed-technique) ·
[Catalysts, reactants and products](usage-patterns.md#reaction-participants) ·
[Reactor, conditions and product analysis](usage-patterns.md#reaction-reactor-conditions) ·
[Values, ranges and fractions with units](usage-patterns.md#quantities)

[:material-download: YAML](../assets/examples/CatalysisDataset-b74m-m6rp.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-b74m-m6rp.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-b74m-m6rp.ttl){ .md-button }

---

## Dataset 6 — Amine transaminase molecular dynamics { #8ppb-aeky }

!!! abstract ""

    **[Datasets for Publication: Navigating the Sequence-Function Landscape: AI-Driven Discovery of Unseen and Synergistic Mutations in an Amine Transaminase - Molecular Dynamic Simulations](https://repository.nfdi4cat.org/dataset.xhtml?persistentId=hdl:21.11165/4cat/8ppb-aeky){:target="_blank"}**
    Doerr, M.; Weigmann, K.; Schulig, L. (2026) — University of Greifswald
    Related publication: [Weigmann et al., ACS Catal. (2025), doi:10.1021/acscatal.5c04248](https://doi.org/10.1021/acscatal.5c04248){:target="_blank"}

The computational part of a protein-engineering study: an amine transaminase variant (3FCR-4M)
and two mutants are prepared, the PLP-bound substrate (S)-1-(2-chlorophenyl)ethanamine is docked,
the complexes are simulated by molecular dynamics, and MM/GBSA gives relative binding free
energies. The deposit consists of the software archives of each step (about 33 GB).

The CoreMeta4Cat record groups this into:

- **4 `Simulation`s** (`was_generated_by`): protein preparation, induced-fit docking, molecular
  dynamics and MM/GBSA. There is no `CatalyticReaction`; the enzyme kinetics are not part of this
  deposit.

**Sources:** the deposit's file descriptions name the software and the variants; the article
gives the enzyme and substrate identities and the MM/GBSA results. Not stated in the main text:
MD settings (in the article's supporting information and the archives).

**Patterns from this dataset:**
[Comparing variants with relative values](usage-patterns.md#simulation-relative-values) ·
[A simulation step that produces structures, not properties](usage-patterns.md#simulation-workflow-step)

[:material-download: YAML](../assets/examples/CatalysisDataset-8ppb-aeky.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-8ppb-aeky.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-8ppb-aeky.ttl){ .md-button }

---

## A note on grouping

None of these datasets describes one catalyst measured once. Real studies screen many catalysts,
or run the same technique across a whole series. Writing one `Characterization` per catalyst, or
one `CatalyticReaction` per run, would make a record balloon to dozens of near-identical entries.

The records therefore group by **what was actually shared**: one `Characterization` per
technique, covering every sample it was applied to, and one `CatalyticReaction` per reaction type
or condition set, covering every catalyst tested under it. Values such as temperature are given
as the range explored, not one value per run. A record then grows with the number of distinct
methods and reaction types in a study, not with the number of data points.
