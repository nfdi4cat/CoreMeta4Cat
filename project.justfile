## Add your own just recipes here. This is imported by the main justfile.

# Generate interactive schema documentation pages (synthesis, reaction, etc.)
[group('model development')]
gen-schema-docs:
  uv run python scripts/generate_schema_docs.py

# Generate sunburst hierarchy charts from the LinkML schema
[group('model development')]
gen-charts:
  uv run python scripts/generate_charts.py

# Export the current schema to Excel (coremeta4cat_vocabulary.xlsx)
[group('model development')]
schema-to-excel:
  uv run python scripts/schema_to_excel.py

# Publish the real-world CatalysisDataset examples as downloadable json/yaml
# (docs/assets/examples/) for the "Working with Data" documentation page
[group('model development')]
gen-example-outputs:
  uv run python scripts/generate_example_outputs.py

# Compare the Excel vocabulary workbook against the current schema
[group('model development')]
excel-to-schema:
  uv run python scripts/excel_to_schema.py

# Convert an inbox Excel workbook into schema YAML changes.
# Place the modified workbook at inbox/coremeta4cat_vocabulary.xlsx first.
# After running: just schema-to-excel && just excel-to-schema && just test
[group('model development')]
inbox-to-schema:
  uv run python scripts/inbox_to_schema.py

# Validate an Excel file in the inbox/ folder against the current schema.
# Place your file as inbox/coremeta4cat_vocabulary.xlsx before running.
[group('model development')]
excel-inbox:
  uv run python scripts/excel_to_schema.py inbox/coremeta4cat_vocabulary.xlsx
