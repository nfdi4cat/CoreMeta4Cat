"""Usage patterns test: every pattern in scripts/usage_patterns.yaml still fits the schema."""
import importlib.util
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
SPEC = yaml.safe_load((REPO_ROOT / "scripts" / "usage_patterns.yaml").read_text(encoding="utf-8"))
PATTERNS = [pattern for section in SPEC["sections"] for pattern in section["patterns"]]

_spec = importlib.util.spec_from_file_location("generate_usage_patterns", REPO_ROOT / "scripts" / "generate_usage_patterns.py")
generator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generator)


@pytest.fixture(scope="module")
def validator():
    return generator.SchemaDirValidator()


@pytest.mark.parametrize("pattern", PATTERNS, ids=[p["id"] for p in PATTERNS])
def test_usage_pattern_is_valid(pattern, validator):
    """Cut the excerpt, validate it against its class and load it into the datamodel."""
    built = generator.build_pattern(pattern, validator)
    assert built["object"]
