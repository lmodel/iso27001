#!/usr/bin/env python3
"""Turn Probo's mitigations.json into IsmsControl examples for this schema.

Source: https://github.com/getprobo/probo, under the MIT License that the
LICENSE file beside this script carries.

Each Probo mitigation that names one or more Annex A controls becomes an
IsmsControl, written to IsmsControl-NNN.yaml beside this script: its
`control_annex_a_controls` list every Annex A control the mitigation names, in
order, and its theme is the first one's. The text and guidance are Probo's
own words, its "Why?" and "What?" sections cut to two sentences each.

A mitigation that names only clauses of the standard, or only other
frameworks, has no Annex A control to answer to, so it is skipped and listed.

Usage::

    uv run python tests/data/third_party/probo/convert.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).parent
SOURCE = HERE / "mitigations.json"

_ANNEX_A_RE = re.compile(r"ISO27001:2022-A\.(\d)\.(\d+)")
THEMES = {"5": "organizational", "6": "people", "7": "physical", "8": "technological"}


class IndentedDumper(yaml.SafeDumper):
    """A safe dumper that indents a list under its key, as yamllint expects."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def annex_a_controls(standards: str) -> list[str]:
    """The Annex A controls a mitigation names, as enum values, in order."""
    seen = []
    for theme, number in _ANNEX_A_RE.findall(standards):
        value = f"a_{theme}_{number}"
        if value not in seen:
            seen.append(value)
    return seen


def first_sentences(text: str, n: int = 2) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(sentences[:n]).strip().rstrip(".")


def parse_description(raw: str) -> tuple[str, str]:
    """Split a Probo description into its "Why?" and "What?" sections."""
    raw = re.sub(r"\s+", " ", raw.replace("\N{RIGHTWARDS DOUBLE ARROW}", "so")).strip()
    parts = re.split(r"##\s*[Ww]hat\?", raw, maxsplit=1)
    why = re.sub(r"##\s*[Ww]hy\?\s*", "", parts[0]).strip()
    what = parts[1].strip() if len(parts) > 1 else ""
    return (first_sentences(why) if why else ""), (
        first_sentences(what) if what else ""
    )


def convert() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    entries, skipped = [], []
    for entry in data:
        controls = annex_a_controls(entry.get("standards", ""))
        (entries if controls else skipped).append((controls, entry))
    entries.sort(key=lambda item: tuple(int(p) for p in item[0][0].split("_")[1:]))

    for old in HERE.glob("IsmsControl-*.yaml"):
        old.unlink()
    for seq, (controls, entry) in enumerate(entries, start=1):
        text, guidance = parse_description(entry.get("description", ""))
        record = {
            "isms_id": f"probo:{entry['id']}",
            "title": entry["name"],
            "control_annex_a_controls": controls,
            "control_theme": THEMES[controls[0].split("_")[1]],
        }
        if text:
            record["control_text"] = text
        if guidance:
            record["control_guidance"] = guidance
        record["implementation_state"] = "not_started"
        out = HERE / f"IsmsControl-{seq:03d}.yaml"
        out.write_text(
            yaml.dump(
                record,
                Dumper=IndentedDumper,
                sort_keys=False,
                allow_unicode=True,
                width=88,
            ),
            encoding="utf-8",
        )
    print(f"Wrote {len(entries)} IsmsControl examples to {HERE}")
    if skipped:
        print(f"Skipped {len(skipped)} mitigations that name no Annex A control:")
        for _, entry in skipped:
            print(f"  {entry['id']}")


if __name__ == "__main__":
    convert()
