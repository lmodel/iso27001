"""Checks the overlay that lets a licence holder add the standard's text.

The repository ships an empty scaffold of the schema's elements; a licence
holder fills a private copy of it, and scripts/overlay_populated_text.py
merges that copy into the schema under tmp/. These tests hold the scaffold
to the schema and to holding no text, keep the private copy out of git, and
show that the merge changes only descriptive keys and writes only under tmp/.
"""

import importlib.util
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "iso27001" / "schema"
SCHEMA = SCHEMA_DIR / "iso27001.yaml"
TEMPLATE = SCHEMA_DIR / "iso27001-overlay.template.yaml"
PRIVATE = SCHEMA_DIR / "iso27001-overlay.yaml"


def _script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _placeholders(node, path=""):
    """Every (path, key, value) of a descriptive key in the scaffold."""
    if isinstance(node, dict):
        for key, value in node.items():
            # A slot may be named description too; its entry is a mapping.
            if key in ("description", "comments") and not isinstance(value, dict):
                yield path, key, value
            else:
                yield from _placeholders(value, f"{path}/{key}")


def test_template_is_what_the_script_writes(tmp_path):
    """The committed scaffold is the one `just create-empty-overlay` writes
    from the schema, so it lists every element the schema has now."""
    out = tmp_path / "template.yaml"
    _script("create_overlay_template").main(
        ["--public", str(SCHEMA), "--output", str(out)]
    )
    assert out.read_text(encoding="utf-8") == TEMPLATE.read_text(encoding="utf-8")


def test_template_holds_no_text():
    """Every placeholder of the shipped scaffold is empty."""
    scaffold = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
    found = list(_placeholders({k: scaffold[k] for k in ("classes", "slots", "enums")}))
    assert found
    for path, key, value in found:
        assert value in ("", []), f"{path}/{key} is not empty"


def test_private_overlay_is_ignored():
    """git ignores the private overlay and the tmp/ folder the merge writes to."""
    if shutil.which("git") is None or not (ROOT / ".git").exists():
        pytest.skip("not a git checkout")
    for path in (PRIVATE, ROOT / "tmp" / "iso27001-merged.yaml"):
        result = subprocess.run(
            ["git", "-C", str(ROOT), "check-ignore", "-q", str(path)], check=False
        )
        assert result.returncode == 0, f"{path} is not ignored"


def test_merge_changes_only_descriptive_keys(tmp_path, monkeypatch):
    """A filled overlay replaces descriptions, including an attribute's and a
    permissible value's, and leaves ranges and structure alone."""
    merge = _script("overlay_populated_text")
    monkeypatch.setattr(merge, "PRIVATE_OUTPUT_DIR", tmp_path)
    overlay = tmp_path / "overlay.yaml"
    overlay.write_text(
        yaml.safe_dump(
            {
                "classes": {
                    "IsmsPolicy": {
                        "description": "LICENSED CLASS TEXT",
                        "range": "string",
                        "attributes": {
                            "policy_statement": {
                                "description": "LICENSED ATTRIBUTE TEXT"
                            }
                        },
                    }
                },
                "enums": {
                    "IsmsAnnexAControl": {
                        "permissible_values": {
                            "a_5_1": {"description": "LICENSED VALUE TEXT"}
                        }
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    out = tmp_path / "merged.yaml"
    merge.main(
        ["--public", str(SCHEMA), "--overlay", str(overlay), "--output", str(out)]
    )
    merged = yaml.safe_load(out.read_text(encoding="utf-8"))
    public = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    policy = merged["classes"]["IsmsPolicy"]
    assert policy["description"] == "LICENSED CLASS TEXT"
    assert (
        policy["attributes"]["policy_statement"]["description"]
        == "LICENSED ATTRIBUTE TEXT"
    )
    assert "range" not in policy
    assert policy["is_a"] == public["classes"]["IsmsPolicy"]["is_a"]
    pv = merged["enums"]["IsmsAnnexAControl"]["permissible_values"]["a_5_1"]
    assert pv["description"] == "LICENSED VALUE TEXT"
    assert pv["title"] == "A.5.1"


def test_merge_writes_only_under_tmp(tmp_path):
    """The merge refuses an output path outside tmp/, before it reads the
    overlay."""
    merge = _script("overlay_populated_text")
    with pytest.raises(SystemExit, match="Refusing to write"):
        merge.main(
            [
                "--public",
                str(SCHEMA),
                "--overlay",
                str(tmp_path / "overlay.yaml"),
                "--output",
                str(SCHEMA_DIR / "merged.yaml"),
            ]
        )
    assert not (SCHEMA_DIR / "merged.yaml").exists()
