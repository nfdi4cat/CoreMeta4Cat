---
title: Building a parser
description: How a laboratory workbook was turned into a validated CoreMeta4Cat record — the method, the crosswalk format, requirements and limitations
---

# Building a parser

[Level 3 of Getting Started](../getting-started.md#level-3-writing-a-json-converter-for-your-sheet)
shows a minimal converter for one sheet. This page shows what it takes for a real workbook: three
sheets in two layouts, a round of questions to the data provider, and a record that can be defended
value by value. The parser was written for one workbook, but the method carries over to others.
How the workbook itself should be set up is described in
[Annotating a spreadsheet](annotating-a-spreadsheet.md).

---

## The worked example { #jlcat03 }

!!! abstract ""

    **Supported Pt catalyst for the epoxidation of styrene (JLCAT03).** Alumina-supported Pt
    prepared by incipient wetness impregnation and reduction, characterized by powder XRD, and
    tested in the liquid-phase epoxidation of styrene with O₂ in an autoclave. Recorded by a
    laboratory researcher in an Excel template with CoreMeta4Cat fields.

The record contains one `Synthesis` (with the reduction as a step of its own), one
`Characterization` (the PXRD measurement) and one `CatalyticReaction` (the test). The catalyst
`JLCAT03` links them: it is the output of the synthesis, the sample of the measurement and the
catalyst of the test. Like the [community datasets](community-datasets.md), the record is part of
the test suite (`tests/data/valid/CatalysisDataset-JLCAT03.yaml`), so it is validated on every
change of the schema.

**Patterns from this dataset:** [A preparation step the schema has no field for](usage-patterns.md#synthesis-step-without-field),
[A value the schema has no field for](usage-patterns.md#value-without-field)

[:material-download: YAML](../assets/examples/CatalysisDataset-JLCAT03.yaml){ .md-button }
[:material-download: JSON](../assets/examples/CatalysisDataset-JLCAT03.json){ .md-button }
[:material-download: RDF](../assets/examples/CatalysisDataset-JLCAT03.ttl){ .md-button }

Everything that went into the record is kept next to the parser, in
[`docs/assets/examples/excel_JLCAT03/`](https://github.com/nfdi4cat/CoreMeta4Cat/tree/main/docs/assets/examples/excel_JLCAT03):

| File | What it is |
|---|---|
| [`source/TestDataSet_CoreMeta4Cat.xlsx`](../assets/examples/excel_JLCAT03/source/TestDataSet_CoreMeta4Cat.xlsx) | The workbook, as received |
| [`source/provider_answers.md`](../assets/examples/excel_JLCAT03/source/provider_answers.md) | The provider's answers to the questions of the first round (transcript of the returned `.docx`) |
| [`parser/xlsx_to_coremeta4cat.py`](../assets/examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py) | The parser. Its code has no knowledge of this workbook |
| [`parser/crosswalk.yaml`](../assets/examples/excel_JLCAT03/parser/crosswalk.yaml) | What each column or row means: target, conversion, basis and reason |
| [`parser/supplement.yaml`](../assets/examples/excel_JLCAT03/parser/supplement.yaml) | What the record needs but the workbook does not contain, with its source |
| [`provenance/source_documentation.yaml`](../assets/examples/excel_JLCAT03/provenance/source_documentation.yaml) | For every value in the record: where it came from and why it sits where it does |
| [`provenance/parse_report.md`](../assets/examples/excel_JLCAT03/provenance/parse_report.md) | Open questions, cell inventory, term check, empty fields |

---

## Deduce, never invent

The record has to be defensible value by value, so the parser follows five rules.

1. **Every non-empty cell is accounted for.** It is mapped, recognised as a repeat of another cell,
   or declared structural (a label without a value). A cell the crosswalk does not cover stops the
   parser.
2. **Values change only through declared conversions**: unit text to a QUDT unit, `50-100` to a
   minimum and a maximum, `heterogeneous` to the value `heterogeneous_catalysis`.
3. **Every target has a basis.** *Direct*: the header term or label names the field. *Deduced*: the
   evidence is another cell, the layout or a physical limit, and it is written down. *Schema-forced*:
   no field exists, so the generic DCAT-AP-PLUS attribute pattern is used.
4. **Nothing missing is filled in silently.** When the schema requires something the source does not
   give, the record states the absence ("Instrument not specified in the source workbook") as a
   marked placeholder, until the data provider supplies it.
5. **Identifiers follow fixed rules** from the lab IDs in the workbook (`CAT_JLCAT03`,
   `REAC_JLCATTEST03`, `DEV_MBR01`). The lab IDs themselves are kept as `other_identifier`.

For this workbook: 76 value cells, 74 mapped and 2 recognised as repeats. Of the 109 values in the
record, 88 come from the workbook (65 direct, 10 deduced, 12 schema-forced, 1 kept as text) and
21 from the provider's answers or the curator.

---

## How the parser was built

1. **Inventory the workbook.** Dump every cell, with its formatting, before deciding anything. The
   example has three layouts (a table with a unit row, a vertical label–term–value list, and a
   second table), and the catalyst ID is the key that links them.
2. **Check every term against its vocabulary.** All 39 Voc4Cat IDs in the headers were looked up in
   the current release, and every QUDT unit used was checked on qudt.org. Definitions matter as much as labels:
   voc4cat:0000153 "reaction chamber volume" includes connected pipes and valves, while the schema
   field that uses it excludes them, so the provider was asked which one they meant.
3. **Find the target of each cell.**
    - *Term first.* A header term is looked up as a field's `slot_uri`, a class's `class_uri`
      or a mapping; most columns resolve this way.
    - *Label when the term is ambiguous.* `SIO:000008` belongs to dozens of fields, so the
      label decides.
    - *Shape from the generated JSON Schema*: whether a field is required, and whether it
      takes a list.
    - *Designators for subclass fields*: an impregnation plan takes `impregnation_type` only
      when it declares `plan_designator: voc4cat:0007028`.
    - *Layout is evidence, not proof*: the rows of the PXRD block looked like the technique's
      title and ID, but the provider meant the measurement's.
    - *Headers can name the wrong process*: the "calcination" columns turned out to describe
      a reduction.
4. **Write the crosswalk**, one entry per column or row, with its target, conversion, basis and
   reason (format below). Anything that would have to be asked goes into a `flag`.
5. **Run and validate.** The parser writes the record, its provenance and a report;
   `linkml-validate` checks the record against the schema.
6. **Read the report.** It lists the open questions, every cell with its target, a check of each
   header term against the field it was mapped to (49 of 62 match; each of the others is explained
   in the crosswalk), and the recommended fields that stay empty.
7. **Send the questions, and work the answers in.** The answers go into the record without
   changing the workbook:
    - An answer that settles how a cell is read changes its crosswalk entry, e.g. a unit, or the
      reduction instead of the calcination.
    - An answer that adds a value goes into the supplement, with the question number as its
      source.

    The example's 13 questions reduced to four still open (licence, authors, the definition of
    "NTP", and confirming the reaction type).

The parser also refuses a workbook that no longer matches its crosswalk:

| Change | The parser stops with |
|---|---|
| A column the crosswalk does not know | `column E '…' is not in the crosswalk` |
| A renamed header | `column E header is '…', crosswalk expects '…'` |
| A note typed somewhere outside the table | `Synthesis!A7: non-empty cell outside the declared layout` |
| The provider adds a unit the curator had supplied | `crosswalk sets a unit, but the sheet gives '%'` |
| An unknown unit, or a value outside a pick-list | `unit 'g' is not in the units table`, `'homogeneous' is not in the value map` |

These cases are tested in `tests/test_excel_example.py`, together with a check that the parser
still reproduces the committed record.

---

## Crosswalk format

All knowledge about a workbook lives in two files: `crosswalk.yaml` (what each cell means) and
`supplement.yaml` (what is not in the workbook). The parser itself is generic.

```yaml
workbook: ../source/TestDataSet_CoreMeta4Cat.xlsx   # paths are relative to the crosswalk
supplement: supplement.yaml
output: ../../../../../tests/data/valid/CatalysisDataset-JLCAT03.yaml
provenance: ../provenance/source_documentation.yaml
report: ../provenance/parse_report.md
root_class: CatalysisDataset
id_prefix: "coremeta4cat:"
qudt: {unit_ns: "https://qudt.org/vocab/unit/", kind_ns: "http://qudt.org/vocab/quantitykind/"}
units: {"degC": DEG_C, "mg": MilliGM, "nl/h": {qudt: L-PER-HR, note: "..."}}   # unit text -> QUDT
sheets:
  Synthesis:
    layout: table            # or key_value (label_column, term_column, value_column, key_row)
    header_row: 1
    unit_row: 2
    first_data_row: 3
    key_column: B            # record key, available as {key}
    record:
      class: Synthesis
      list: was_generated_by_synthesis   # where each record goes, in full
      id_list: was_generated_by          # and where its id is listed
      id: "SYN_{key}"
    ids:                     # ids of the objects created inside a record
      realized_plan: "SYN_{key}_method"
      "had_input_entity[precursor_1]": "PREC_{key}_1"
    columns:                 # key_value sheets have rows, addressed by row number and label
      - col: M
        header: precursor quantity 1 VOC4CAT:0008118   # checked against the workbook
        to: "had_input_entity[precursor_1].precursor_quantity[]"
        as: quantity
        kind: Mass           # QUDT quantity kind
        basis: direct
        why: voc4cat:0008118 is the slot_uri of precursor_quantity (Precursor).
```

**Target paths**

| Path | Meaning |
|---|---|
| `a.b` | Field `b` of the object in field `a` (created on first use) |
| `a[]` | Append to the list in field `a` |
| `a[name]` | The list item called `name` in field `a`, created on first use with its id from `ids` |
| `^a` | Start at the dataset instead of the record, e.g. `^rdf_type[]` |
| `to: [p1, p2]` | Write the same value to several places |

An entry can instead be `confirm: <row or column>` (repeats another cell; the parser checks they are
equal), `structural: <reason>` (a label without a value) or `unused: <reason>`.

**Conversions (`as:`)**

| `as` | Result |
|---|---|
| `text` | The text (`strip_curie: true` removes a term in brackets, e.g. `(NCIT:C93052)`) |
| `number` | A bare number, for fields without a unit such as `step_size` |
| `enum` | The value looked up in `values:`: an enum value, a term ID, or a whole object |
| `quantity` | `{value, unit, has_quantity_type}`. The unit comes from the unit row through `units:`, or from `unit:` with a `unit_note` saying where it came from. A value that is not a number goes to the entry's `fallback` |
| `range`, `range_max` | `{min_value, max_value}` from `50-100` or `2 to 90`, or only `max_value` |
| `qualitative` | `{value}`; `attrs:` adds fields such as `title` or `rdf_type` |
| `identifier` | `{notation}`, for `other_identifier` |
| `id` | The cell becomes the object's id |
| `ref` | Creates the object at the path, with its id from `ids`; used to link sheets |

Templates (in `id`, `ids` and `describe`) accept `{key}`, `{slug:REF}` and `{raw:REF}`, where REF is
a column letter or a row number of the same record.

**Supplement**

```yaml
dataset:                     # fields of the dataset itself
  - to: "title[]"
    value: "Supported Pt catalyst for the epoxidation of styrene"
    basis: provider          # provider | curator (default) | placeholder
    source: data provider's answers, Q17
    why: Required.
records:                     # added to every record of a sheet
  Synthesis:
    - to: realized_plan.has_drying_duration
      as: quantity           # converted like a cell, with the same units
      value: 12
      unit: HR
      kind: Time
      basis: provider
      source: data provider's answers, Q6
      why: The workbook says 'over night'; the provider gave 12 hours.
open_questions:              # listed in the report next to the crosswalk's flags
  - about: Dataset (Q17)
    text: No licence was given. ...
```

An entry with `placeholder: true` stands for a required value the source does not give; running the
parser with `--no-placeholders` leaves these out and lists the required fields that stay empty.

---

## Requirements

**From the workbook.** A parser like this one needs:

- a fixed layout on every sheet;
- a key column for every record, with the same key wherever sheets refer to the same object;
- a term ID or a field name for every column;
- a unit for every number, and the values the schema requires.

What the workbook lacks has to come from the data provider. [Annotating a spreadsheet](annotating-a-spreadsheet.md)
shows how to set a workbook up so that little is missing.

**For the conversion.** You need:

- Python with openpyxl and LinkML (both part of the project's development environment, `uv sync`);
- the CoreMeta4Cat schema;
- time to look up every term in its vocabulary (Voc4Cat, QUDT, and others such as ChEBI or CHMO).

---

## Limitations

**Of the schema.** Some things the example needed have no field of their own yet. The record uses
the generic DCAT-AP-PLUS pattern for them; your parser may run into the same gaps:

| What the workbook needed | How the record expresses it |
|---|---|
| A reduction step after drying (impregnation has calcination fields only) | A generic activity under `Synthesis.has_part`, typed voc4cat:0000098 "reduction", with typed attributes for atmosphere, heating rate and gas flow rate |
| The metal loading | A generic quantity of the catalyst sample, typed voc4cat:0008106 "metal loading" |
| The amount and InChI of the support | The support listed as an input entity of class `Precursor` |
| The InChI of a precursor | A generic attribute typed CHEMINF:000113 (InChI descriptor) |
| The yield of a particular product | `has_yield` of the reaction, with the product named in the description |
| GC-MS as the product identification method | `rdf_type` CHMO:0000497; the GCMS class itself cannot be used there |
| The operation mode of the reactor (batch) | A generic attribute of the reactor, typed voc4cat:0000108 "operation mode" |
| The unit of the PXRD step size | Stated in the description of the technique; `step_size` holds a bare number |
| A contact person | `qualified_attribution` with the name as text; `contact_point` cannot hold a name |
| Normal litres per hour | Litre per hour, with the reference conditions in the description |

**Of this parser.**

- **One crosswalk per workbook layout.** The parser stops as soon as the workbook no longer matches.
  This is deliberate: a moved column should be noticed, not silently mapped.
- **Simple conversions only.** The parser does not convert units, compute InChIKeys or molar masses,
  or look up ChEBI or PubChem IDs; chemicals get local identifiers.
- **Some choices stay with the curator.** Terms that are not in the workbook are chosen by the
  curator, checked in the vocabulary, and flagged for the provider to confirm. Here these are the
  reaction type and the type of the reduction step.

!!! warning "The schema changes over time"
    CoreMeta4Cat is still evolving, so fields, classes and the terms they require can change between
    releases. Check your records against the latest version of the schema instead of relying on the
    examples on these pages alone. A crosswalk is written for one version of the schema: after a new
    release, rerun the parser and validate the record, and the validation errors show what to change.

---

## Running it

From the root of the CoreMeta4Cat repository, in the project environment (`uv sync`):

```bash
# workbook -> tests/data/valid/CatalysisDataset-JLCAT03.yaml, provenance and report
uv run python docs/assets/examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py

# validate the record
uv run linkml-validate -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    tests/data/valid/CatalysisDataset-JLCAT03.yaml

# publish it as YAML, JSON and RDF under docs/assets/examples/ (also part of `just gen-doc`)
just gen-example-outputs
```

`just test` validates the record with the rest of the test suite and checks that the parser still
reproduces it.

**For another workbook:**

1. Copy the parser and write a new crosswalk and supplement for the new workbook.
2. Look up every term in its vocabulary.
3. Use the same `ids` template for the linking key in every sheet, so that the objects link up.
4. Start with the direct term matches. For every other entry, write the evidence into `why`, and
   every open point into `flag`.
5. Run until the parser no longer stops, then validate and read the report.
6. Send the questions to the data provider, and work the answers in through the crosswalk and the
   supplement, never by editing the record.
