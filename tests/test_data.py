"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

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


# The rules the validator cannot check, held over the examples. docs/index.md
# lists them.
VIEW = SchemaView(str(SCHEMA))
CLASSES = set(VIEW.all_classes())
DESIGNATORS = {
    name: slot.name
    for name in CLASSES
    for slot in VIEW.class_induced_slots(name)
    if slot.designates_type
}
THEMES = {
    name: value.annotations["theme"].value
    for name, value in VIEW.get_enum("IsmsAnnexAControl").permissible_values.items()
}


def _records(node, cls, found):
    """Collect every record a document holds, as (class, data), with each
    inlined record under the class its slot ranges over, or the class its
    designator names."""
    if isinstance(node, list):
        for item in node:
            _records(item, cls, found)
        return
    if not isinstance(node, dict):
        return
    cls = node.get(DESIGNATORS.get(cls, ""), cls)
    found.append((cls, node))
    slots = {s.name: s for s in VIEW.class_induced_slots(cls)}
    for key, value in node.items():
        slot = slots.get(key)
        if slot and slot.range in CLASSES and (slot.inlined or slot.inlined_as_list):
            _records(value, slot.range, found)


def _all_records(filepath):
    found = []
    _records(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        _class_of(filepath),
        found,
    )
    return found


@pytest.mark.parametrize(
    "filepath",
    [f for f in VALID_EXAMPLE_FILES if _class_of(f) == "IsmsManagementSystem"],
)
def test_an_isms_names_each_record_once_and_resolves_its_references(filepath):
    """Within a whole ISMS, no two records share an isms_id, and each
    reference names a record the ISMS holds, of the class it ranges over."""
    records = _all_records(filepath)
    ids = [data["isms_id"] for _, data in records if "isms_id" in data]
    repeated = sorted({i for i in ids if ids.count(i) > 1})
    assert not repeated, repeated
    classes = {data["isms_id"]: cls for cls, data in records if "isms_id" in data}
    for cls, data in records:
        for slot in VIEW.class_induced_slots(cls):
            if slot.range not in CLASSES or slot.inlined or slot.inlined_as_list:
                continue
            value = data.get(slot.name)
            targets = value if isinstance(value, list) else [value]
            for target in (t for t in targets if t is not None):
                assert target in classes, (slot.name, target)
                assert slot.range in VIEW.class_ancestors(classes[target]), (
                    slot.name,
                    target,
                    classes[target],
                )


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES + PROBO_FILES)
def test_examples_keep_the_rules_no_validator_checks(filepath):
    """A control's theme is the theme of one of the Annex A controls it
    answers to, an audit ends on or after the day it begins, and a Statement
    of Applicability lists each Annex A control once. A control holds one
    theme, so one that answers to controls of two themes takes one of them,
    as Probo's converter takes the first one's."""
    for _, data in _all_records(filepath):
        theme = data.get("control_theme")
        annex_a = data.get("control_annex_a_controls") or []
        if theme and annex_a:
            assert theme in {THEMES[c] for c in annex_a}, data.get("isms_id")
        start, end = data.get("audit_period_start"), data.get("audit_period_end")
        if start and end:
            assert str(start) <= str(end), data.get("isms_id")
        controls = [e["entry_annex_a_control"] for e in data.get("soa_entries") or []]
        repeated = sorted({c for c in controls if controls.count(c) > 1})
        assert not repeated, (data.get("isms_id"), repeated)
