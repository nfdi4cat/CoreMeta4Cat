---
title: Annotating a spreadsheet
description: How to set up an Excel workbook so that it converts into a CoreMeta4Cat record without guesswork, shown on a real laboratory workbook
---

# Annotating a spreadsheet

Many labs record their syntheses, measurements and catalytic tests in Excel. This page shows how to
set up such a workbook so that it can be converted into a CoreMeta4Cat record without guesswork. It
builds on [Level 2 of Getting Started](../getting-started.md#level-2-annotating-your-own-spreadsheets)
and uses a real workbook as its example: what made it easy to convert, and what led to questions.
No programming is needed for anything on this page. The conversion itself is described in
[Building a parser](building-a-parser.md).

!!! abstract ""

    **Example: catalyst JLCAT03.** A laboratory researcher recorded a simplified but connected
    workflow in an Excel template with CoreMeta4Cat fields. It covers the synthesis of an
    alumina-supported Pt catalyst by incipient wetness impregnation, its characterization by powder
    X-ray diffraction (PXRD), and its use in the liquid-phase epoxidation of styrene with O₂ in an
    autoclave.

    [:material-download: Workbook (.xlsx)](../assets/examples/excel_JLCAT03/source/TestDataSet_CoreMeta4Cat.xlsx){ .md-button }
    [:material-file-document-outline: The finished record](building-a-parser.md#jlcat03){ .md-button }

---

## The example workbook

The workbook has three sheets, one per CoreMeta4Cat data class:

| Sheet | What it records | Layout |
|---|---|---|
| Synthesis | Composition, support, precursors and their amounts, impregnation, drying, the thermal treatment | One catalyst per row; a header row with field name and term ID, then a unit row |
| Character | One PXRD measurement: sample, technique, scan and instrument settings | Vertical: label, term ID and value in three columns, class names as bold rows |
| Reaction | Catalyst, conditions, reactor, starting material, solvent, products and yields | One test per row, like the Synthesis sheet |

The catalyst ID `JLCAT03` appears in all three sheets. This is what makes the workflow connected:
the catalyst made in the synthesis, the sample measured by PXRD and the catalyst tested in the
autoclave become one and the same object in the record.

## What made it convert well

- **The term IDs are right.** Every Voc4Cat ID in the headers (39 of them) exists, and its label
  matches the column name. The other IDs (PROCO, AFE, NCIT, RO, CHMO, OBI, Allotrope) are correct
  too.
- **Units have a row of their own** on the Synthesis and Reaction sheets, so they can be read
  without interpretation.
- **One catalyst ID links the sheets**, as described above.
- **Every substance has an InChI**, which identifies it unambiguously.
- **The numbers are consistent.** 100.9 mg Pt(NH₃)₄(NO₃)₂ on 957.9 mg Al₂O₃ gives 5.0 wt% Pt, which
  matches the stated metal loading.

## What led to questions

The first conversion ended with 13 questions to the data provider. They fall into a few groups, and
each has a simple fix in the workbook:

| What happened | Example from the workbook | Set it up like this instead |
|---|---|---|
| A number without a unit | 2θ range "2 to 90", spinning speed 30, measurement time 80 (no units on the whole Character sheet); a reaction temperature and a yield without unit cells | Give every numeric column a unit, in the unit row |
| Text in a number column | Drying duration "over night" | A number of hours |
| Two values in one cell | "50-100" (°C), "2 to 90" (°) | Separate minimum and maximum columns |
| A term inside a value | "Autoclave (NCIT:C93052)", "incipient wetness impregnation (voc4cat:0007806)" | The plain value, chosen from a pick-list (see below) |
| A unit whose reference conditions are unclear | "15 nl/h" (normal litres at which temperature and pressure?) | L/h, plus a column for the reference conditions |
| A header naming the wrong process | "calcination …" columns for a treatment in 5 % H₂/N₂, which was in fact a reduction | Name the step that was done; if the template has no columns for it, add them |
| Rows whose owner is unclear | Title, description and ID inside the PXRD technique block, meant for the measurement itself | One record per row, with its own ID column |
| A generic term in a header | `SIO:000008` for the calcination atmosphere; dozens of fields share this term | The CoreMeta4Cat field name next to the term |
| Required information with no place in the workbook | The diffractometer, the measured properties of the catalyst, the dataset's title, authors and licence | A column for the instrument of each measurement, and a Dataset sheet |

The provider answered the questions in a copy of them ([transcript](../assets/examples/excel_JLCAT03/source/provider_answers.md)),
and the record was completed from the answers. Two answers changed how whole groups of cells are
read: the "calcination" columns describe a reduction, and the title, description and ID in the PXRD
block belong to the measurement.

---

## How to set up a workbook

### One record per row, on every sheet

Use the same layout on every sheet: a table with one record per row (a catalyst, a measurement, a
test) and one field per column. The vertical layout of the example's Character sheet mixed class
rows (in bold) with field rows. Values sat sometimes on the class row (`OperationMode`,
`Atmosphere`), sometimes on the field row, and sometimes on both (`Duration` repeated
`has experiment duration`). A table avoids all of this, and formatting such as bold never has to
carry meaning.

### Field name, term and unit in three header rows

Keep the three apart, instead of writing the term ID into the header text:

| (row 1) field | impregnation_temperature | has_drying_duration | has_drying_atmosphere |
|---|---|---|---|
| **(row 2) term** | voc4cat:0008121 | voc4cat:0008206 | voc4cat:0008208 |
| **(row 3) unit** | °C | h | |
| **(row 4 onwards) data** | 25 | a number, e.g. 16 | air |

The field name in row 1 is what makes a column unambiguous. Some term IDs are shared: `SIO:000008`
belongs to dozens of fields, and `voc4cat:0008113` (stirrer type) to both a synthesis field and a
reactor field. Write term IDs one way: with a lower-case prefix (`voc4cat:`, not `VOC4CAT:`) and a
colon (`AFR:0002018`, not `AFR_0002018`).

### Numbers only in number columns

- One number per cell, with its unit in the unit row. Write each unit the same way throughout
  (`mL`, not sometimes `ml`).
- Ranges get two columns, minimum and maximum.
- For gas flows at normal conditions, use `L/h` and add a column that states the reference
  conditions; the unit vocabulary CoreMeta4Cat uses (QUDT) has no unit for normal litres.

### Pick-lists for controlled values

Where the schema accepts only certain values, offer exactly these values as an Excel drop-down
(*Data → Data Validation → List*). The example workbook used "heterogeneous", "powder" and
"incipient wetness impregnation (voc4cat:0007806)", which a converter has to translate by hand.

| Field | Values the schema accepts |
|---|---|
| Catalyst type (`catalyst_type`) | `heterogeneous_catalysis`, `homogeneous_catalysis`, `biocatalysis`, `electrocatalysis`, `photocatalysis`, `hybrid_catalysis`, `other` |
| Catalyst form (`catalyst_form`) | `thin_film`, `bulk`, `powdered`, `deposited_sample`, `supported`, `other` |
| Impregnation type (`impregnation_type`) | `wet_impregnation`, `dry_impregnation`, `incipient_wetness`, `other` |
| Sample state (`sample_state`) | `solid`, `liquid`, `gas`, `solution`, `powder`, `pellet`, `thin_film`, `other` |
| Preparation method | `Impregnation`, `CoPrecipitation`, `SolGel`, `Solvothermal`, … (see [Synthesis](../synthesis.md)) |
| Reactor | `Autoclave`, `FixedBedReactor`, `CSTR`, `PlugFlowReactor`, … (see [Reaction](../reaction.md)) |

The reaction type and the research field are vocabulary terms. Give them as term IDs, for example
`voc4cat:0000205` (epoxidation) and `voc4cat:0007001` (heterogeneous catalysis). The reaction type
is mandatory for every reaction.

### Repeating groups on a sheet of their own

Instead of numbered column groups ("Precursor 1", "Precursor 2", "generated product 1", "… 2"), use
a sheet for precursors (catalyst ID, substance, InChI, quantity, unit) and one for products (test
ID, product, InChI, yield, unit). Numbered groups drift apart: in the example, "Precursor 2" had no
InChI column, and the second product had no unit cell.

### Identifiers that link the sheets

Keep one ID per catalyst and use it wherever the catalyst appears, as the example does. Give every
measurement and every test its own ID column too (like `JLCAT-PXRD-03` and `JLCATTEST03`), and the
instruments and reactors as well (like `MBR01`).

### A Dataset sheet

A record needs dataset-level information that no experiment sheet holds: a title and a description,
the authors (with ORCID), a contact person, a licence, keywords, the research field, and a related
publication if there is one. Give them a sheet of their own.

### Instruments and required fields

Every measurement needs the instrument it was made with (make and model), and every synthesis needs
at least one measured property of the catalyst (for example the phases seen by PXRD or the BET
surface area). Mark the mandatory fields of the template, for example by colour, so that they are
not left empty; the [minimal field set](../getting-started.md#the-coremeta4cat-minimal-field-set)
lists the ones every dataset needs.

### Chemical identifiers

The InChI the example gives for every substance is a good start. An InChIKey, a PubChem CID or a
ChEBI ID next to it lets a converter link the substance to a public identifier instead of
inventing a local one.

---

## Before you send a workbook

- [ ] Every sheet is a table with one record per row.
- [ ] Every column has a field name, a term ID and, for numbers, a unit.
- [ ] Number columns contain only numbers; ranges have minimum and maximum columns.
- [ ] Controlled values come from pick-lists.
- [ ] Catalysts, measurements, tests and instruments have IDs, and the same ID is used everywhere.
- [ ] Mandatory fields are filled, including the instrument of each measurement and a measured
      catalyst property.
- [ ] A Dataset sheet gives title, description, authors, contact, licence and keywords.

Whoever converts the workbook will still have questions: about a unit, a value, or which step a
column describes. A workbook set up like this keeps them few. How the conversion is done, and how
the answers are worked in, is described in [Building a parser](building-a-parser.md).
