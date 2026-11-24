# Excel workbook example: catalyst JLCAT03

A worked example of turning a laboratory Excel workbook into a CoreMeta4Cat record, in YAML, JSON
and RDF. The workbook has one sheet each for synthesis, characterization and reaction. It describes
a Pt/Al2O3 catalyst (JLCAT03) made by incipient wetness impregnation, measured by powder XRD, and
tested in the epoxidation of styrene in an autoclave.

**Status: draft.**
- The record validates against the schema.
- 13 questions to the data provider are still open, and two required fields hold "not specified"
  placeholders (see `metadata/parse_report.md`).
- The record is not yet part of `tests/data/valid` or of the documentation site.

## Contents

| Path | What |
|---|---|
| `source/` | The workbook as received, and the text that came with it |
| `parser/` | The parser for this example: `xlsx_to_coremeta4cat.py` reads `crosswalk.yaml` (what each cell means) and `supplement.yaml` (what the workbook does not contain) |
| `metadata/` | Generated output: the record (`.yaml`, `.json`, `.ttl`), the provenance of every value (`source_documentation.yaml`), and `parse_report.md` (open questions, cell inventory, checks) |
| `PARSER_BUILD_NOTES.md` | How the parser was built: method, mapping decisions, crosswalk format |
| `FEEDBACK_FOR_DATA_PROVIDER.md` | Questions for the person who filled in the workbook, and template advice |
| `SCHEMA_FINDINGS.md` | Issues in the schema that this example revealed |

The script in `parser/` belongs to this example. It is not one of the repository's maintenance tools
in `scripts/`.

## Regenerate

From the repository root, in the project environment (`uv sync`):

```bash
uv run python examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py
uv run linkml-validate -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml
uv run linkml-convert -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    -o examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.ttl \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml
uv run linkml-convert -s src/coremeta4cat/schema/coremeta4cat.yaml -C CatalysisDataset \
    -o examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.json \
    examples/excel_JLCAT03/metadata/CatalysisDataset-JLCAT03.yaml
```

To change the record, edit `parser/crosswalk.yaml` or `parser/supplement.yaml` and regenerate.
Never edit the files in `metadata/` by hand.
