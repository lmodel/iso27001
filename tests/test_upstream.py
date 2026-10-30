"""Checks that the schema models the edition ISO's records name.

ISO sells the text of ISO/IEC 27001, so src/iso27001/schema/iso-open-data/
holds ISO Open Data's records of the edition and its amendment instead, which
scripts/check_upstream_release.py pins and watches. These tests read that
extract with the standard library, hold the schema header to it and to the
watch's pins, and hold the Annex A enum to the standard's structure: 93
controls in four themes, numbered without gaps.
"""

import importlib.util
import json
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "iso27001" / "schema" / "iso27001.yaml"
EXTRACT = (
    ROOT
    / "src"
    / "iso27001"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)

# Annex A's four themes, the clause of Annex A each takes, and how many
# controls each holds.
THEMES = {
    "organizational": (5, 37),
    "people": (6, 8),
    "physical": (7, 14),
    "technological": (8, 34),
}


@cache
def _watch():
    """The upstream watch script, loaded once as a module."""
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def _schema():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def _records():
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    return {r["id"]: r for r in map(json.loads, lines)}


def test_extract_matches_the_pinned_lines():
    """Each line of the extract hashes to the watch's pin, and the extract
    holds no scope, the field that summarizes the standard in ISO's words."""
    watch = _watch()
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    hashes = {json.loads(line)["id"]: watch.digest(line) for line in lines}
    assert hashes == watch.PINNED_RECORDS
    for record in _records().values():
        assert not set(watch.LEFT_OUT) & record.keys(), record["id"]
        assert watch.line_of(record) in lines


def test_header_pins_match_the_watch():
    """The header's version, source and dates are the ones the watch pins and
    the extract records."""
    watch = _watch()
    header = _schema()
    notes = header["annotations"]
    records = _records()
    edition = records[watch.EDITION_ID]
    amendments = [
        r
        for r in records.values()
        if r["reference"].startswith(watch.SUPPLEMENT_PREFIX)
    ]
    assert header["version"] == watch.PINNED_VERSION
    assert header["source"] == watch.PINNED_SOURCE
    assert header["source"].endswith(f"/{watch.EDITION_ID}.html")
    assert notes["standard"] == edition["reference"] == watch.PINNED_EDITION
    assert notes["edition"] == str(edition["edition"])
    assert notes["publication_date"] == edition["publicationDate"]
    assert notes["iso_open_data_date"] == watch.PINNED_DATE
    assert [a["reference"] for a in amendments] == [notes["amendment"]]
    assert notes["amendment_publication_date"] == amendments[0]["publicationDate"]
    assert watch.PINNED_VERSION == "2022/" + notes["amendment"].rpartition("/")[2]
    assert notes["overview_and_terms"] in {r["reference"] for r in records.values()}


def test_pinned_records_are_published():
    """Every pinned record is at the published stage, and only ISO/IEC
    27002:2022 names a successor."""
    watch = _watch()
    for record in _records().values():
        assert record["currentStage"] == watch.PUBLISHED, record["reference"]
    replaced = {
        r["reference"]: r["replacedBy"] for r in _records().values() if r["replacedBy"]
    }
    assert replaced == {"ISO/IEC 27002:2022": sorted(watch.SUCCESSOR_PROJECTS)}


def test_annex_a_has_93_controls_in_four_themes():
    """The Annex A enum holds a_<clause>_<n> for every control of each theme,
    numbered from 1 without gaps, titled A.<clause>.<n>, and nothing more."""
    enum = _schema()["enums"]["IsmsAnnexAControl"]["permissible_values"]
    expected = {
        f"a_{clause}_{n}": theme
        for theme, (clause, count) in THEMES.items()
        for n in range(1, count + 1)
    }
    assert len(expected) == 93
    assert {name: pv["annotations"]["theme"] for name, pv in enum.items()} == expected
    for name, pv in enum.items():
        assert pv["title"] == "A." + name[2:].replace("_", ".")
        assert "description" not in pv, f"{name} carries no text of the standard"


def test_themes_match_annex_a():
    """The theme enum names the four themes, each with its clause and count."""
    themes = _schema()["enums"]["IsmsControlTheme"]["permissible_values"]
    assert {
        name: (
            int(pv["annotations"]["annex_a_clause"]),
            int(pv["annotations"]["control_count"]),
        )
        for name, pv in themes.items()
    } == THEMES
