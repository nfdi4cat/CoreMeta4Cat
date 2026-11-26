# From a lab Excel workbook to CoreMeta4Cat RDF: how the parser was built

Example: catalyst JLCAT03, a Pt/Al2O3 catalyst made by incipient wetness impregnation,
characterized by powder XRD and tested in styrene epoxidation. A laboratory researcher filled in
an Excel workbook with CoreMeta4Cat fields (one sheet each for synthesis, characterization and
reaction). These notes record how that workbook was turned into a validated CoreMeta4Cat record
and RDF, so the same steps can be repeated for other workbooks. It took two rounds:
- a first parse of the workbook alone, which produced a list of open questions;
- a second parse after the data provider answered them (Step 7).

| Where | What |
|---|---|
| `source/TestDataSet_CoreMeta4Cat.xlsx` | The workbook as received, unchanged |
| `source/provider_note.md` | The text sent with it |
| `source/provider_answers_2026-11-24.docx`, `source/provider_answers.md` | The provider's answers to the open questions, and a verbatim transcript (questions numbered Q1–Q17) |
| `parser/crosswalk.yaml` | The mapping: one entry per column or row, with target, conversion and reason |
| `parser/supplement.yaml` | Everything the record needs that is not in the workbook, with its source |
| `parser/xlsx_to_coremeta4cat.py` | The parser. Its code has no workbook-specific knowledge; that sits in the two YAML files next to it |
| `metadata/CatalysisDataset-JLCAT03.yaml`, `.json`, `.ttl` | The record, validated, as YAML, JSON and RDF (Turtle) |
| `metadata/source_documentation.yaml` | Provenance of every value in the record (generated) |
| `metadata/parse_report.md` | Open questions, cell inventory, term check, empty slots (generated) |
| `FEEDBACK_FOR_DATA_PROVIDER.md` | Questions and template advice for the person who filled in the workbook |
| `SCHEMA_FINDINGS.md` | What this example revealed about the schema itself |

## Run it

From the root of the CoreMeta4Cat repository, in the project environment (`uv sync`, which
includes linkml and openpyxl). The parser finds its crosswalk next to itself and the schema of the
checkout it is in.

```bash
# 1. workbook -> record (YAML and JSON) + provenance + report
uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py

# 2. validate against the schema (the .json validates the same way)
uv run linkml-validate -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml

# 3. convert to RDF (this also loads the record into the Python data model)
uv run linkml-convert --no-validate -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    -o examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.ttl \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml

# 4. what does the workbook alone fail on? Builds the record without placeholders (into a file
#    of your choice, so the published record stays as it is) and lists the required slots left empty.
uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py --no-placeholders --out no-placeholders.yaml
```

Without a project environment, prefix the commands with
`uv run --no-project --with linkml==1.12.1 --with openpyxl --` instead of `uv run`.

The record is not part of `tests/data/valid`, so `just test` does not check it; step 2 does.

Why the JSON comes from the parser and step 3 uses `--no-validate`: since nfdi4cat/CoreMeta4Cat#199
the dataset lists its activities' ids in `was_generated_by`. After a round trip through the Python
data model, LinkML writes these as `{"id": ...}` objects, which the schema does not accept. Without
`--no-validate`, `linkml-convert` checks that round-tripped data and stops. The parser therefore
writes the JSON straight from the record, as `scripts/generate_example_outputs.py` does for the
docs. Step 2 validates the record itself, and the Turtle is not affected.

## The rule: deduce, never invent

The record has to be defensible value by value, so the parser follows five rules.

1. **Every non-empty cell is accounted for.** It is mapped, recognised as a repeat of another cell,
   or declared structural. If a cell is not covered by the crosswalk, the parser stops.
2. **Values are only changed by declared conversions**: unit text to a QUDT IRI, `50-100` to a
   minimum and maximum, `heterogeneous` to the enum value `heterogeneous_catalysis`.
3. **Every target is labelled with its basis.**
   - *direct*: the header term or label names the slot or class.
   - *deduced*: the evidence is another cell, the sheet layout or a physical limit, and it is written down.
   - *schema-forced*: no slot exists for the term, so the generic DCAT-AP-PLUS attribute pattern is used.
4. **Nothing missing is filled silently.** When the schema requires a field the source does not
   give, the supplement states the absence ("Instrument not specified in the source workbook")
   and marks it as a placeholder. The report lists every placeholder, and `--no-placeholders`
   leaves them out.
5. **Identifiers are minted by fixed rules** from the lab IDs in the workbook (`CAT_JLCAT03`,
   `REAC_JLCATTEST03`, `DEV_MBR01`). The lab IDs themselves are kept as `other_identifier`.

Result for this workbook: 76 value cells; 74 mapped and 2 recognised as repeats.

| | Values written | From the workbook | From the supplement | Placeholders | Basis of workbook values | Open questions |
|---|---|---|---|---|---|---|
| Round 1 (workbook only) | 92 | 87 | 5 | 2 | 66 direct, 13 deduced, 7 schema-forced, 1 fallback | 13 |
| Round 2 (with the answers) | 108 | 87 | 21 | 0 | 65 direct, 9 deduced, 12 schema-forced, 1 fallback | 4 |
| Schema after #192 and #199 | 109 | 88 | 21 | 0 | 65 direct, 10 deduced, 12 schema-forced, 1 fallback | 4 |

## Step 1: inventory the workbook

Dump every cell, with its formatting, before deciding anything. This workbook has three layouts:

| Sheet | Layout | Notes |
|---|---|---|
| Synthesis | Table: header row 1, unit row 2, one catalyst per row from row 3 | Term IDs written into the header text (`metal loading voc4cat:0008106`) |
| Character | Vertical: label (A), term (B), value (C), one measurement per sheet | Bold rows are class names (`PowderXRD`, `Duration`), plain rows are slots. No units at all |
| Reaction | Table like Synthesis, one test per row | Repeating column groups (`generated product 1`, `... 2`) |

The catalyst ID (`JLCAT03`) appears in all three sheets and is the join key: synthesis output,
characterized sample and catalyst used in the test are the same object, with the same IRI.

## Step 2: check the vocabulary terms the provider used

Before trusting a header term, look it up in the vocabulary it comes from.

- **voc4cat**: all 39 IDs in the headers exist in the current release (v2026-10-31, read from
  `https://nfdi4cat.github.io/voc4cat/latest/voc4cat.ttl`), and each label matches the column name.
  Read the whole file: concepts are sorted in several separate runs, not by ID overall. A first,
  partial reading wrongly reported 14 IDs as missing.
- **QUDT**: the 13 unit local names needed exist (checked on `qudt.org`, v3.5.4). QUDT has no unit
  for normal litres, so `nl/h` cannot be expressed as a unit IRI.
- **Allotrope**: `AFR_0002018` is "device identifier".

The definitions matter as well as the labels. voc4cat:0000153 "reaction chamber volume" includes
connected pipes and valves, but the schema slot that uses it says the opposite (see
`SCHEMA_FINDINGS.md`).

## Step 3: find the target of each cell

Work from the term, then the label, then the layout:

1. **Term → schema.** Look the CURIE up as a `slot_uri`, a `class_uri` or a mapping in the schema
   (SchemaView, with CURIEs expanded to IRIs so that `VOC4CAT:` and `voc4cat:` agree). Most columns
   resolve this way: `voc4cat:0008121` is `impregnation_temperature`.
2. **Ambiguous terms → label and context.** `SIO:000008` ("has attribute") is the `slot_uri` of
   dozens of slots, so the label decides: `starting material volume SIO:000008` gives `has_volume`.
   `voc4cat:0008113` and `voc4cat:0008114` belong to both a synthesis slot and a reactor slot; on the
   Reaction sheet they are the reactor's.
3. **Shape → generated JSON Schema.** `gen-json-schema` shows what is required and what is a list.
   Examples: `has_yield` is a list (two products are fine), `has_experiment_duration` is a
   single value, and `ProductIdentificationMethod` accepts no other designator.
4. **Subclass fields need a designator.** An impregnation plan only takes `impregnation_type` if it
   declares `plan_designator: voc4cat:0007028`. The same holds for `reactor_designator` (Autoclave).
   The workbook names the subclass, either in a cell value (`Impregnation`, `Autoclave
   (NCIT:C93052)`) or in a class row (`PowderXRD`). Activities need no designator: since #199 each
   kind has its own dataset slot (`was_generated_by_synthesis`, `..._characterization`), and
   `was_generated_by` lists the ids of all of them.
5. **Layout is evidence, not proof.** The Character sheet repeats the slot list of the PowderXRD
   class page. Rows 11, 12 and 22 (`title`, `description`, `id`) sit in the PowderXRD block, so round
   1 mapped them to the protocol and flagged that their wording suggests the measurement itself. The
   provider confirmed the measurement (Q8), and round 2 maps them to the Characterization activity.
6. **Headers can name the wrong process.** Columns W–AB are headed "calcination", but the gas was
   5 % H2/N2. Round 1 mapped them to the calcination slots and asked. The provider answered that the
   step was a reduction and no calcination took place (Q10), so round 2 maps them to a reduction
   step. Term matches are only as good as the provider's choice of term.

Decisions that were not a direct term match (round 2; "Q" numbers are the provider's answers):

| Cell(s) | Decision | Basis and evidence |
|---|---|---|
| Synthesis D (metal loading) | Generic quantity of the catalyst sample, typed `voc4cat:0008106`, described as nominal | schema-forced: no metal-loading slot; nominal per Q9 |
| Synthesis F–H (support, InChI, mass) | Support listed as an input entity of class Precursor | schema-forced: `had_input_entity` only accepts Precursor; no slot for the amount of support |
| Synthesis G, L (InChI of support and precursor) | Generic qualitative attribute typed `CHEMINF:000113` | schema-forced: Precursor has no `inchi` slot |
| Synthesis T (`over night`) | Text kept in the plan description; 12 h as `has_drying_duration` | fallback: a Duration needs a number; the number is from Q6 |
| Synthesis W–AB (`calcination ...`) | A reduction step: generic Activity under `Synthesis.has_part`, typed voc4cat:0000098 'reduction'. Its parameters are typed attributes, using generic voc4cat terms where they exist (atmosphere, heating rate, gas flow rate). The furnace is its `carried_out_by`; the start temperature comes from Q11 | schema-forced: the provider says reduction, not calcination (Q10), and the preparation methods have no reduction step |
| Synthesis Z (`nl/h`) | Litre per hour, with "normal litres at NTP" in the description | QUDT has no normal-litre unit; reading and NTP confirmed by Q7 |
| Character C10, C13, C18, C20 (no units) | Degree (2θ range and step size), rpm, min | Q3. The 2θ unit had been deduced, since 2θ cannot exceed 180°. `step_size` holds a bare number, so its unit is stated in the protocol description |
| Character C11, C12, C22 | Title, description and `other_identifier` of the measurement; the activity and protocol IRIs are minted from C22 | read as the protocol's by layout in round 1; the measurement per Q8 |
| Character C8 (`Powder XRD`) | Plan designator CHMO:0000158, and activity `rdf_type` | deduced from the cell and the PowderXRD class row |
| Reaction C (`heterogeneous`) | Also the dataset's research field (`rdf_type`, a list since #192) | deduced: field of its only reaction |
| Reaction E (`epoxidation`) | Reaction type `rdf_type` voc4cat:0000205 'epoxidation' | deduced, to be confirmed. Required since #192, but the provider left it open (Q14). voc4cat defines it as converting an alkene into an epoxide, and the test turns styrene (K3) into styrene oxide (AA3) |
| Reaction J (`GCMS`) | `rdf_type` CHMO:0000497 on the product identification method | schema-forced: the GCMS class cannot be designated there |
| Reaction T (`batch`) | Generic attribute of the reactor, typed `voc4cat:0000108` | schema-forced: no operation-mode slot on reactions or reactors |
| Reaction X (chamber volume) | `reactor_working_volume`, described as vessel only | Q12, which matches the slot's definition, not voc4cat's |
| Reaction Z (reaction temperature, no unit) | Unit °C | deduced (the reactor range in column F is 50–100 °C), confirmed by Q4 |
| Reaction AF (second yield, no unit) | Unit % | deduced (same quantity as AC), confirmed by Q5 |
| Reaction AC, AF (yields) | `has_yield` of the reaction, product named in the description | direct; the schema cannot link a yield to a product |

## Step 4: write the crosswalk

All knowledge about a workbook lives in two files: `crosswalk.yaml` (what each cell means) and
`supplement.yaml` (what is not in the workbook). The parser is generic.

### Crosswalk layout

```yaml
workbook: ../source/TestDataSet_CoreMeta4Cat.xlsx   # paths are relative to the crosswalk
supplement: supplement.yaml
output: ../metadata/CatalysisDataset-JLCAT03.yaml
provenance: ../metadata/source_documentation.yaml
report: ../metadata/parse_report.md
root_class: CatalysisDataset
id_prefix: "coremeta4cat:"
qudt: {unit_ns: "https://qudt.org/vocab/unit/", kind_ns: "http://qudt.org/vocab/quantitykind/"}
units: {"degC": DEG_C, "mg": MilliGM, "nl/h": {qudt: null, note: "..."}}   # unit text -> QUDT
sheets:
  Synthesis:
    layout: table            # or key_value (label_column, term_column, value_column, key_row)
    header_row: 1
    unit_row: 2
    first_data_row: 3
    key_column: B            # record key, available as {key}
    record:                  # one record per data row
      class: Synthesis
      list: was_generated_by_synthesis   # where the record goes, in full
      id_list: was_generated_by          # optional: also list its id here
      id: "SYN_{key}"
      # set: {...}           # optional fixed fields of every record
    ids:                     # ids of objects created inside the record, by path
      realized_plan: "SYN_{key}_method"
      "had_input_entity[precursor_1]": "PREC_{key}_1"
    columns:                 # key_value sheets: rows, addressed by row + label
      - col: M
        header: precursor quantity 1 VOC4CAT:0008118   # checked against the workbook
        to: "had_input_entity[precursor_1].precursor_quantity[]"
        as: quantity
        kind: Mass           # QUDT quantity kind
        basis: direct
        why: voc4cat:0008118 is the slot_uri of precursor_quantity (Precursor).
        flag: ...            # optional open question for the data provider
```

### Target paths

| Path | Meaning |
|---|---|
| `a.b` | Slot `b` of the single object in slot `a` (created on first use) |
| `a[]` | Append to the list in slot `a` |
| `a[name]` | The list item called `name` in slot `a`; created on first use with the id from `ids`, reused afterwards |
| `^a` | Start at the dataset instead of the record (e.g. `^rdf_type`) |
| `to: [p1, p2]` | Write the same value to several places |

An entry may also be `confirm: <row/col>` (repeats another cell; the parser checks they are equal),
`structural: <reason>` (a label without a value, e.g. a class row), or `unused: <reason>`.

### Conversions (`as:`)

| `as` | Result |
|---|---|
| `text` | The string (`strip_curie: true` drops a bracketed term such as `(NCIT:C93052)`) |
| `number` | A bare number (for unitless slots such as `step_size`) |
| `enum` | Value looked up in `values:` (an enum value, a CURIE or a whole object) |
| `quantity` | `{value, unit, has_quantity_type}`. The unit comes from the unit row through `units`; if the sheet has none, from `unit:` with a mandatory `unit_note`. Non-numbers go to `fallback` |
| `range`, `range_max` | `{min_value, max_value, ...}` from `50-100` / `2 to 90`, or only `max_value` |
| `qualitative` | `{value}` (Atmosphere, InChI, ...); `attrs:` adds e.g. `title`, `rdf_type` |
| `identifier` | `{notation}` for `other_identifier` |
| `id` | The cell becomes the object's `id` (`id_prefix` + value) |
| `ref` | Only creates the object at the path (its id comes from `ids`); used for joins |

`attrs:` adds fixed fields to the produced object. `describe:` adds a description template. Templates
accept `{key}`, `{slug:REF}` and `{raw:REF}`, where REF is a column letter or row number of the same
record.

### Supplement

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
      as: quantity           # converted like a workbook cell
      value: 12
      unit: HR
      kind: Time
      basis: provider
      source: data provider's answers, Q6
      why: The workbook says 'over night'; the data provider gave 12 hours.
  Character:                 # round 1, before the answers:
    - to: "carried_out_by[instrument]"
      value: {title: X-ray diffractometer, description: Instrument not specified in the source workbook.}
      placeholder: true      # left out by --no-placeholders
      source: curator
      why: Required by Characterization; ...
open_questions:              # listed in parse_report.md with the crosswalk's flags
  - about: Dataset (Q17)
    text: No licence was given. ...
```

## Step 5: run, validate, convert

See "Run it" above. In this example:

- The record validates with no issues (`linkml-validate`), in both rounds.
- In round 1, without placeholders, two required slots stayed empty:
  `Synthesis.catalyst_measured_properties` and `Characterization.carried_out_by`. These were the
  workbook's dead ends. In round 2 the provider's answers fill both, and the record validates
  without any placeholder.
- `linkml-convert` produces the Turtle. It loads the record into the Python data model first, so a
  missing designator would fail here even when JSON Schema validation passes. The JSON is written
  by the parser (see "Run it").

## Step 6: review what the parser reports

`metadata/parse_report.md` is generated on every run:

- **Open questions**: the `flag`s of the crosswalk, plus automatic ones (no unit, not a number).
- **Placeholders**: what the supplement had to fill in.
- **Cell inventory**: every value cell with its status and target(s).
- **Header terms against targets** (with `--schema`): each term the provider wrote is compared with
  the slot, class, `rdf_type` or designator its cell was mapped to. Round 1: 52 of 62 terms match.
  Round 2: 49 match. The 11 that do not are explained in the crosswalk:
  - no slot carries the term (catalyst ID 3×, device identifier, reaction temperature);
  - the "over night" fallback;
  - a header term that is not the slot's URI;
  - four "calcination" terms on what the provider identified as a reduction.

  The other 2 are on repeated values.
- **Empty slots** (with `--schema`): required slots, plus recommended slots that the domain class
  itself lists.
  - Round 1: reaction type, reactant, PXRD temperature, detector, vessel materials, and DCAT
    keyword, contact point and theme.
  - Round 2: the answers fill all of these except the reaction type, and `contact_point`, which
    cannot hold a name (see `SCHEMA_FINDINGS.md`). The Impregnation calcination slots are now
    listed as empty, correctly, since no calcination took place.

`metadata/source_documentation.yaml` gives, for every value in the record, its location, the cell
it came from, the basis and the reason, in the format of the curated datasets' provenance files.

The parser also refuses workbooks that no longer match the crosswalk. Tested cases:

| Change to workbook or crosswalk | Parser stops with |
|---|---|
| Column E removed from the crosswalk | `column E 'storage conditions (voc4cat:0008105)' is not in the crosswalk` |
| Header E1 renamed | `column E header is 'storage temperature', crosswalk expects ...` |
| A note typed into Synthesis!A7 | `Synthesis!A7: non-empty cell outside the declared layout` |
| Provider adds the missing unit in Reaction!AF2 | `crosswalk sets a unit, but the sheet gives '%'` (remove the curator's unit) |
| Unit `g` instead of `mg` | `unit 'g' is not in the units table` |
| `homogeneous` instead of `heterogeneous` | `'homogeneous' is not in the value map` |
| Repeated value differs (Character!C21 = 90) | `expected to repeat 20 (80), holds 90` |

## Step 7: fold in the provider's answers

Round 1 ends with the open questions of the report, sent to the data provider. They answered in a
copy of the questions; round 2 works the answers in without touching the workbook.

1. **Keep the answers as a source.** The returned `.docx` goes to `source/` unchanged, and a
   verbatim Markdown transcript is generated from it. The transcript is not retyped, and it numbers
   the questions (Q1–Q17), so that provenance can cite them.
2. **Answers that settle how a cell is read change the crosswalk.**
   - A unit goes into `unit:` with a `unit_note` citing the question (Q3, Q4, Q5).
   - A new reading changes the entry's target: the measurement's title and ID (Q8), and the
     calcination columns becoming a reduction step (Q10).
   - The entry's `flag` is removed; `answered:` silences an automatic flag (Q6).
3. **Answers that add values change the supplement**, with `basis: provider` and the question as
   `source`. Examples: the diffractometer (Q1), measured properties (Q2), drying time (Q6), start
   temperature (Q11), oxygen as reactant (Q13), and title, description, keywords and contact (Q17).
   `as: quantity` converts them with the same units table as the workbook.
4. **Placeholders go.** Whatever is still unanswered is listed under `open_questions` of the
   supplement. Here that is the licence, the authors and the definition of "NTP". The reaction-type
   term was optional in round 2. Since #192 it is required, so it was deduced and flagged for
   confirmation (see "Keeping up with schema changes").
5. **Rerun, validate, convert.** The workbook stays as received. If the provider later fixes the
   workbook itself, for example by typing the missing unit into Reaction!AF2, the parser stops at
   the curator-supplied unit, which then has to go (see the guard rails above).

The answers also change the RDF. The calcination slots of the impregnation plan are gone. The
record gains a reduction step under the synthesis. The characterization activity takes its IRI
from the measurement ID.

## What the RDF looks like

The catalyst is one node linking the three activities, and every activity is typed with an
ontology class:

```turtle
coremeta4cat:DS_excel_JLCAT03 a dcat:Dataset , voc4cat:0007001 ;      # research field
    prov:wasGeneratedBy coremeta4cat:CHAR_JLCAT-PXRD-03 , coremeta4cat:SYN_JLCAT03 .
coremeta4cat:SYN_JLCAT03 a PROCO:0000001 , prov:Activity ;            # synthetic chemical process
    dcterms:hasPart coremeta4cat:SYN_JLCAT03_reduction ;
    prov:generated coremeta4cat:CAT_JLCAT03 ;
    prov:used coremeta4cat:PREC_JLCAT03_1 , coremeta4cat:PREC_JLCAT03_support , coremeta4cat:SYN_JLCAT03_method .
coremeta4cat:SYN_JLCAT03_reduction a prov:Activity , voc4cat:0000098 ;   # reduction step (Q10)
    prov:wasAssociatedWith coremeta4cat:DEV_JLCAT03_tube-furnace .
coremeta4cat:CHAR_JLCAT-PXRD-03 a CHMO:0000158 , OBI:0000070 , prov:Activity ;   # powder XRD, assay
    prov:used coremeta4cat:CAT_JLCAT03 , coremeta4cat:CHAR_JLCAT-PXRD-03_method ;
    prov:wasAssociatedWith coremeta4cat:DEV_Stoe-STADI-MP .
coremeta4cat:REAC_JLCATTEST03 a REX:0000051 , voc4cat:0000205 ;     # catalytic reaction, epoxidation
    RXNO:0000425 coremeta4cat:CAT_JLCAT03 ;
    RO:0004009 coremeta4cat:REAG_JLCATTEST03_oxygen , coremeta4cat:SM_JLCATTEST03_styrene ;
    prov:wasAssociatedWith coremeta4cat:DEV_MBR01 .
coremeta4cat:SYN_JLCAT03_method a voc4cat:0007028 .   # plan_designator becomes rdf:type
coremeta4cat:DEV_MBR01 a NCIT:C93052 .                # reactor_designator: Autoclave
```

Until nfdi4cat/CoreMeta4Cat#199 the activities were typed with a string (`a "Synthesis"`), and
`sample_preparation` came out as an unexpanded `<allotrope.quality:0001159>`. Both are fixed; see
`SCHEMA_FINDINGS.md`.

## Keeping up with schema changes

A crosswalk is written against one version of the schema. When the schema changes, merge the new
schema, rerun, and let validation say what broke. For this record, after nfdi4cat/CoreMeta4Cat#192
and #199, validation reported four errors:

| Error | Schema change | Fix in the crosswalk |
|---|---|---|
| Research field (`rdf_type` of the dataset) must be a list | #192 | Target `^rdf_type[]` instead of `^rdf_type` |
| Activities under `was_generated_by` are objects with `activity_designator` | #199: each kind of activity has its own slot, and `was_generated_by` lists ids | `list: was_generated_by_synthesis` (or `_characterization`), `id_list: was_generated_by`, no `set: {activity_designator: ...}` |
| (same, second activity) | #199 | as above |
| Reaction type (`rdf_type` of the reaction) is required | #192 | New entry on column E: voc4cat:0000205, deduced from the reaction name and flagged for confirmation |

The crosswalk and the parser changed; the workbook and the provider's answers did not.

## Adapting this to another workbook

1. Copy `parser/` next to the new workbook and dump its cells (Step 1).
2. Check every term against its vocabulary (Step 2).
3. Declare the sheet layouts and record keys, and use the same `ids` template for the join key in
   every sheet so that the objects link up.
4. Write one entry per column or row. Start with `basis: direct` term matches. For every other entry
   write the evidence into `why`, and anything you would have to ask into `flag`.
5. Run until the parser no longer stops, then validate, convert, and read the report.
6. Send the open questions to the data provider, and fold the answers in as in Step 7. Change only
   the crosswalk or supplement, never the generated record.

Units: the record uses `https://qudt.org/vocab/unit/...` like every other CoreMeta4Cat example,
while QUDT itself declares `http://qudt.org/vocab/unit/...`. The choice is one setting
(`qudt.unit_ns`) in the crosswalk.
