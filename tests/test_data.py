"""Data test."""
import os
import glob
import pytest
from collections import Counter
from pathlib import Path

import yaml

import src.coremeta4cat.datamodel.coremeta4cat
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))
CATALYSIS_DATASET_FILES = [f for f in VALID_EXAMPLE_FILES if Path(f).name.startswith("CatalysisDataset-")]
TYPED_ACTIVITY_SLOTS = (
    "was_generated_by_synthesis",
    "was_generated_by_characterization",
    "was_generated_by_simulation",
)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        src.coremeta4cat.datamodel.coremeta4cat,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", CATALYSIS_DATASET_FILES, ids=lambda f: Path(f).stem)
def test_was_generated_by_lists_the_described_activities(filepath):
    """was_generated_by holds the ids of exactly the activities described in the typed slots."""
    data = yaml.safe_load(Path(filepath).read_text(encoding="utf-8"))
    described = [activity["id"] for slot in TYPED_ACTIVITY_SLOTS for activity in data.get(slot) or []]
    assert Counter(data["was_generated_by"]) == Counter(described)
