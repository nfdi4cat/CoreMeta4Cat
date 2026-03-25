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

# Compare the Excel vocabulary workbook against the current schema
[group('model development')]
excel-to-schema:
  uv run python scripts/excel_to_schema.py
