"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import iso27001.datamodel.iso27001

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR_VALID = DATA_DIR / "valid"
DATA_DIR_INVALID = DATA_DIR / "invalid"
DATA_DIR_PROBO = DATA_DIR / "third_party" / "probo"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))
PROBO_FILES = sorted(glob.glob(os.path.join(DATA_DIR_PROBO, "IsmsControl-*.yaml")))

SCHEMA = Path(__file__).parent.parent / "src" / "iso27001" / "schema" / "iso27001.yaml"


def _class_of(filepath):
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclass of its class."""
    tgt_class = getattr(iso27001.datamodel.iso27001, _class_of(filepath))
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
# The examples quote their dates, as JSON carries them, because the validator
# reads a date as text.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES + PROBO_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example, and every example derived from Probo's
    mitigations, passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        str(SCHEMA),
        _class_of(filepath),
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text(encoding="utf-8")
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(yaml.safe_load(text), str(SCHEMA), _class_of(filepath))
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_class_has_an_example():
    """Each class that data can be written in has a valid example: every
    class but the abstract base, the mixin and the abstract kind of entry."""
    classes = {
        name
        for name, cls in yaml.safe_load(SCHEMA.read_text())["classes"].items()
        if not cls.get("abstract") and not cls.get("mixin")
    }
    examples = {_class_of(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


def test_probo_examples_cover_the_mitigations():
    """Every Probo mitigation that names an Annex A control has an example."""
    assert len(PROBO_FILES) == 61
