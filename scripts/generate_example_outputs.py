"""
generate_example_outputs.py

Publishes the real-world CatalysisDataset examples (tests/data/valid/
CatalysisDataset-<dataset-id>.yaml, e.g. -2d6m-exeb.yaml) as downloadable
.json, .yaml, and .ttl (RDF/Turtle) files under docs/assets/examples/, so
the "Working with Data" documentation page can link to them.

These files are already validated as part of `just test`
(tests/data/valid/ is the schema's test suite); this script only
republishes the already-valid YAML in JSON/RDF form and copies the YAML
alongside it, it does not re-validate.

Run:
    just gen-example-outputs
  or directly:
    uv run python scripts/generate_example_outputs.py
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import yaml
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

from coremeta4cat.datamodel.coremeta4cat import CatalysisDataset

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "tests" / "data" / "valid"
OUTPUT_DIR = REPO_ROOT / "docs" / "assets" / "examples"
SCHEMA_PATH = REPO_ROOT / "src" / "coremeta4cat" / "schema" / "coremeta4cat.yaml"

# Real-world dataset examples, identified by the dataset-id suffix in their
# filename (CatalysisDataset-<suffix>.yaml). Purely-numeric suffixes (001,
# 002, ...) are synthetic schema-testing fixtures and are excluded here --
# only handle-style dataset ids (e.g. 2d6m-exeb) get published.
DATASET_ID_PATTERN = re.compile(r"^CatalysisDataset-(.+)\.yaml$")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    schemaview = SchemaView(str(SCHEMA_PATH))
    published = []
    for source_file in sorted(SOURCE_DIR.glob("CatalysisDataset-*.yaml")):
        match = DATASET_ID_PATTERN.match(source_file.name)
        if not match:
            continue
        dataset_id = match.group(1)
        if dataset_id.isdigit():
            continue
        with open(source_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        yaml_out = OUTPUT_DIR / f"CatalysisDataset-{dataset_id}.yaml"
        shutil.copyfile(source_file, yaml_out)

        json_out = OUTPUT_DIR / f"CatalysisDataset-{dataset_id}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

        ttl_out = OUTPUT_DIR / f"CatalysisDataset-{dataset_id}.ttl"
        obj = yaml_loader.load(str(source_file), target_class=CatalysisDataset)
        rdflib_dumper.dump(obj, to_file=str(ttl_out), schemaview=schemaview)

        published.append(dataset_id)
        print(f"  OK {yaml_out.relative_to(REPO_ROOT)}")
        print(f"  OK {json_out.relative_to(REPO_ROOT)}")
        print(f"  OK {ttl_out.relative_to(REPO_ROOT)}")

    print(f"\nPublished {len(published)} example dataset(s) to {OUTPUT_DIR.relative_to(REPO_ROOT)}: {', '.join(published)}")


if __name__ == "__main__":
    main()
