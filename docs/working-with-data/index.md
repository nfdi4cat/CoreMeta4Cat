---
title: Working with Data
description: How CoreMeta4Cat looks in practice, from complete community datasets to small reusable patterns
---

# Working with Data

The rest of this documentation explains CoreMeta4Cat field by field. This section does the
opposite: it shows CoreMeta4Cat applied to real data. Use it to see what a finished record looks
like, and as a source of examples to copy when you describe your own dataset.

<div class="grid cards" markdown>

-   :material-database-outline:{ .lg .middle } **[Community datasets](community-datasets.md)**

    ---

    Six published datasets from [Repo4Cat](https://repository.nfdi4cat.org), each described
    end to end: heterogeneous catalysis, microkinetics, DFT and machine-learned potentials,
    and biocatalysis. Download each record as YAML, JSON or RDF.

-   :material-puzzle-outline:{ .lg .middle } **[Usage patterns](usage-patterns.md)**

    ---

    Small examples for recurring tasks: a synthesis with its precursors, a measurement with a
    specific technique, a test in a fixed-bed reactor, a simulation and its results. Each one is
    shown as a graph, as YAML and as RDF, and is taken from a community dataset.

-   :material-file-excel-outline:{ .lg .middle } **[From spreadsheet to record](annotating-a-spreadsheet.md)**

    ---

    A laboratory Excel workbook turned into a validated record: how to
    [annotate a spreadsheet](annotating-a-spreadsheet.md) so it converts without guesswork, and
    how to [build a parser](building-a-parser.md) for it, with its requirements and limitations.

</div>

---

## How a CoreMeta4Cat record is organised

Every record answers the same handful of questions, in this order:

1. **What is this dataset, and who made it?** A title, a description, the research field, the
   people who created it, and where the original files live (`id`, `title`, `description`,
   `rdf_type`, `creator`, `dataset_distribution`).
2. **What activities produced the data?** Was a catalyst synthesized (`Synthesis`)? Was
   something measured (`Characterization`)? Was something computed (`Simulation`)? Each goes
   under the field for its kind (`was_generated_by_synthesis`,
   `was_generated_by_characterization`, `was_generated_by_simulation`), and `was_generated_by`
   lists the ids of all of them.
3. **What catalytic reaction is the dataset about?** The reaction being studied, with its
   reactants, catalysts, reactor, conditions, and how products were identified. This goes under
   `is_about_activity`.
4. **What catalyst or material is the dataset about?** This goes under `is_about_entity`.

A simple dataset might need only some of these; a pure simulation study, for example, has no
reaction. [Usage pattern 1](usage-patterns.md#dataset-entry-point) shows the dataset level in
detail.

Every activity follows the same pattern: *what happened* (the activity), *how it was done* (the
plan in `realized_plan`, e.g. a preparation method or a characterization technique), *with what*
(`carried_out_by`, e.g. an instrument) and *on what* (`evaluated_entity`, e.g. a catalyst sample).
[Design Patterns](../design-patterns.md) explains why the schema is built this way.

---

## Where to go next

- **Copy a pattern** that matches what you need to describe → [Usage patterns](usage-patterns.md)
- **Compare with a complete record** from a similar study → [Community datasets](community-datasets.md)
- **Start from your own spreadsheet** → [Getting Started](../getting-started.md), then
  [Annotating a spreadsheet](annotating-a-spreadsheet.md) and [Building a parser](building-a-parser.md)
- **Look up a field** → [Catalysis Dataset](../catalysis-dataset.md) or the
  [Schema Reference](../elements/overview.md)
