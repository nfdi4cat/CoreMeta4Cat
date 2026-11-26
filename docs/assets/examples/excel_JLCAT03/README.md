# Spreadsheet example: catalyst JLCAT03

The source files and the parser behind the worked example in
[Building a parser](../../../working-with-data/building-a-parser.md): a laboratory Excel workbook
(synthesis, PXRD and a catalytic test of a Pt/Al₂O₃ catalyst) converted into a CoreMeta4Cat record.
How such a workbook should be set up is described in
[Annotating a spreadsheet](../../../working-with-data/annotating-a-spreadsheet.md).

| Folder | Contents |
|---|---|
| `source/` | The workbook as received, and the data provider's answers to our questions (`.docx` and verbatim transcript) |
| `parser/` | `xlsx_to_coremeta4cat.py` reads `crosswalk.yaml` (what each cell means) and `supplement.yaml` (what the workbook does not contain) |
| `provenance/` | Generated: the provenance of every value (`source_documentation.yaml`) and the parse report |

The record itself is `tests/data/valid/CatalysisDataset-JLCAT03.yaml`, where the test suite
validates it; `just gen-doc` publishes it as YAML, JSON and RDF next to this folder. The parser
belongs to this example and is not one of the repository's maintenance tools in `scripts/`.

Regenerate from the repository root (project environment, `uv sync`):

```bash
uv run python docs/assets/examples/excel_JLCAT03/parser/xlsx_to_coremeta4cat.py
```

To change the record, edit the crosswalk or the supplement and rerun; never edit the generated
files by hand.
