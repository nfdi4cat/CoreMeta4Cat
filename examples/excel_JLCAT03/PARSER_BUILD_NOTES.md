# From a lab Excel workbook to CoreMeta4Cat RDF: how the parser was built

Example: catalyst JLCAT03, a Pt/Al2O3 catalyst made by incipient wetness impregnation,
characterized by powder XRD and tested in styrene epoxidation. A laboratory researcher filled in
an Excel workbook with CoreMeta4Cat fields (one sheet each for synthesis, characterization and
reaction). These notes record how that workbook was turned into a validated CoreMeta4Cat record
and RDF, so the same steps can be repeated for other workbooks.

| Where | What |
|---|---|
| `source/TestDataSet_CoreMeta4Cat.xlsx` | The workbook as received, unchanged |
| `source/provider_note.md` | The text sent with it (source of the dataset description) |
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
# 1. workbook -> record + provenance + report
uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py

# 2. validate against the schema
uv run linkml-validate -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml

# 3. convert to JSON and RDF (this also loads the record into the Python data model)
uv run linkml-convert -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    -o examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.ttl \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml
#    (the same with -o ...JLCAT03.json)

# 4. what does the workbook alone fail on? Builds the record without placeholders (into a file
#    of your choice, so the published record stays as it is) and lists the required slots left empty.
uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py --no-placeholders --out no-placeholders.yaml
```

Without a project environment, prefix the commands with
`uv run --no-project --with linkml==1.12.1 --with openpyxl --` instead of `uv run`.

The record is not part of `tests/data/valid`, so `just test` does not check it; step 2 does.

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

Result for this workbook: 76 value cells; 74 mapped and 2 recognised as repeats. 92 values were
written, 87 from the workbook and 5 from the supplement, 2 of which are placeholders. Basis of the
workbook values: 66 direct, 13 deduced, 7 schema-forced, 1 fallback. There are 13 open questions.

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
   dozens of slots, so the label decides: `calcination atmosphere` gives `has_calcination_atmosphere`.
   `voc4cat:0008113` and `voc4cat:0008114` belong to both a synthesis slot and a reactor slot; on the
   Reaction sheet they are the reactor's.
3. **Shape → generated JSON Schema.** `gen-json-schema` shows what is required and what is a list.
   Examples: `has_yield` is a list (two products are fine), `has_calcination_dwelling_time` is a
   single value, and `ProductIdentificationMethod` accepts no other designator.
4. **Subclass fields need a designator.** An impregnation plan only takes `impregnation_type` if it
   declares `plan_designator: voc4cat:0007028`. The same holds for `reactor_designator` (Autoclave)
   and `activity_designator` (in the combined record). The workbook names the subclass, either in a
   cell value (`Impregnation`, `Autoclave (NCIT:C93052)`) or in a class row (`PowderXRD`).
5. **Layout.** The Character sheet repeats the slot list of the PowderXRD class page. Rows 11, 12
   and 22 (`title`, `description`, `id`) therefore sit in the PowderXRD block and were mapped to the
   protocol. Their wording suggests the measurement itself, so this is an open question.

Decisions that were not a direct term match:

| Cell(s) | Decision | Basis and evidence |
|---|---|---|
| Synthesis D (metal loading) | Generic quantity of the catalyst sample, typed `voc4cat:0008106` | schema-forced: no metal-loading slot |
| Synthesis F–H (support, InChI, mass) | Support listed as an input entity of class Precursor | schema-forced: `had_input_entity` only accepts Precursor; no slot for the amount of support |
| Synthesis G, L (InChI of support and precursor) | Generic qualitative attribute typed `CHEMINF:000113` | schema-forced: Precursor has no `inchi` slot |
| Synthesis T (`over night`) | Kept verbatim in the plan description | fallback: a Duration needs a number |
| Synthesis X (calcination device) | Device under `Synthesis.carried_out_by` | deduced: no calcination-device slot |
| Synthesis AB (final temperature) | `max_value` of `has_calcination_temperature_range` | deduced: the schema folds initial and final temperature into one range |
| Synthesis Z (`nl/h`) | Value kept, no unit IRI, unit text in the description | no QUDT unit exists |
| Character C10 (2θ range, no unit) | Unit degree | deduced: 2θ cannot exceed 180° (π rad), so 90 only fits degrees |
| Character C8 (`Powder XRD`) | Plan designator CHMO:0000158, and activity `rdf_type` | deduced from the cell and the PowderXRD class row |
| Reaction C (`heterogeneous`) | Also the dataset's research field (`rdf_type`) | deduced: field of its only reaction |
| Reaction J (`GCMS`) | `rdf_type` CHMO:0000497 on the product identification method | schema-forced: the GCMS class cannot be designated there |
| Reaction T (`batch`) | Generic attribute of the reactor, typed `voc4cat:0000108` | schema-forced: no operation-mode slot on reactions or reactors |
| Reaction Z (reaction temperature, no unit) | Unit °C | deduced: the reactor range in column F is 50–100 °C; 100 K or 100 °F would fall outside it |
| Reaction AF (second yield, no unit) | Unit % | deduced: same quantity as AC (in %); 22 cannot be a fraction |
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
    record: {class: Synthesis, list: was_generated_by, id: "SYN_{key}", set: {activity_designator: Synthesis}}
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
    value: "..."
    source: curator          # or e.g. "data provider's accompanying text"
    why: Required. Composed only from workbook values (cells ...).
records:                     # added to every record of a sheet
  Character:
    - to: "carried_out_by[instrument]"
      value: {title: X-ray diffractometer, description: Instrument not specified in the source workbook.}
      placeholder: true      # left out by --no-placeholders
      source: curator
      why: Required by Characterization; ...
```

## Step 5: run, validate, convert

See "Run it" above. In this example:

- The record validates with no issues (`linkml-validate`).
- Without placeholders, two required slots stay empty: `Synthesis.catalyst_measured_properties` and
  `Characterization.carried_out_by`. These are the workbook's dead ends.
- `linkml-convert` produces JSON and Turtle. It loads the record into the Python data model first,
  so a missing designator would fail here even when JSON Schema validation passes.

## Step 6: review what the parser reports

`metadata/parse_report.md` is generated on every run:

- **Open questions**: the `flag`s of the crosswalk, plus automatic ones (no unit, not a number).
- **Placeholders**: what the supplement had to fill in.
- **Cell inventory**: every value cell with its status and target(s).
- **Header terms against targets** (with `--schema`): each term the provider wrote is compared with
  the slot, class, `rdf_type` or designator its cell was mapped to. Here 52 of 62 terms match. The
  8 that do not are explained in the crosswalk: no slot carries the term, the "over night" fallback,
  or a header term that is not the slot's URI. The other 2 are on repeated values.
- **Empty slots** (with `--schema`): required slots, plus recommended slots that the domain class
  itself lists. Here they are: reaction type, reactant, PXRD temperature, detector, vessel
  materials, and DCAT keyword, contact point and theme.

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

## What the RDF looks like

The catalyst is one node linking the three activities:

```turtle
coremeta4cat:SYN_JLCAT03 a "Synthesis" ;
    prov:generated coremeta4cat:CAT_JLCAT03 ;
    prov:used coremeta4cat:PREC_JLCAT03_1 , coremeta4cat:PREC_JLCAT03_support , coremeta4cat:SYN_JLCAT03_method .
coremeta4cat:CHAR_JLCAT03_PXRD a "Characterization" , CHMO:0000158 ;
    prov:used coremeta4cat:CAT_JLCAT03 , coremeta4cat:JLCAT-PXRD-03 .
coremeta4cat:REAC_JLCATTEST03 RXNO:0000425 coremeta4cat:CAT_JLCAT03 ;
    prov:wasAssociatedWith coremeta4cat:DEV_MBR01 .
coremeta4cat:SYN_JLCAT03_method a voc4cat:0007028 .   # plan_designator becomes rdf:type
coremeta4cat:DEV_MBR01 a NCIT:C93052 .                # reactor_designator: Autoclave
```

Two problems in the RDF come from the schema and also appear in the existing example outputs:
activities are typed with a string (`a "Synthesis"`), and the `sample_preparation` predicate stays
an unexpanded `<allotrope.quality:0001159>`. See `SCHEMA_FINDINGS.md`.

## Adapting this to another workbook

1. Copy `parser/` next to the new workbook and dump its cells (Step 1).
2. Check every term against its vocabulary (Step 2).
3. Declare the sheet layouts and record keys, and use the same `ids` template for the join key in
   every sheet so that the objects link up.
4. Write one entry per column or row. Start with `basis: direct` term matches. For every other entry
   write the evidence into `why`, and anything you would have to ask into `flag`.
5. Run until the parser no longer stops, then validate, convert, and read the report.
6. Send the open questions to the data provider. Change only the crosswalk or supplement, never the
   generated record.

Units: the record uses `https://qudt.org/vocab/unit/...` like every other CoreMeta4Cat example,
while QUDT itself declares `http://qudt.org/vocab/unit/...`. The choice is one setting
(`qudt.unit_ns`) in the crosswalk.
