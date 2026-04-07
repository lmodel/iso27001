#!/usr/bin/env python3
"""Convert Probo mitigations.json to iso27001 LinkML-compliant YAML test fixtures.

Source: https://github.com/getprob/propo (MIT licence)

Output:
  tests/data/third_party/probo/SecurityControl-NNN.yaml  — one per Annex A mitigation (61 entries)

Clause-level mitigations (references to main ISO 27001 clauses rather than Annex A
controls) are written to a separate summary report and not converted to YAML fixtures
because they describe ISMS governance activities that map to classes such as
InformationSecurityObjective, ManagementReview, and AwarenessProgram — classes that
already have hand-authored fixtures covering their required fields.
"""

import json
import re
import sys
import textwrap
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

HERE = Path(__file__).parent
OUTPUT_DIR = HERE          # write fixtures alongside the source data
SOURCE = HERE / "mitigations.json"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_ANNEX_A_RE = re.compile(r"ISO27001:2022-A\.([\d.]+)")
_CLAUSE_RE = re.compile(r"ISO27001:2022-([\d.]+)")

CATEGORY_MAP = {5: "organizational", 6: "people", 7: "physical", 8: "technological"}


def first_annex_a_control(standards: str) -> str | None:
    """Return the first Annex A control number from the standards string, or None."""
    m = _ANNEX_A_RE.search(standards)
    if not m:
        return None
    return m.group(1).rstrip(".")  # strip any trailing dot from source data


def control_category(control_id: str) -> str:
    """Derive ControlCategory enum value from the Annex A control number prefix."""
    major = int(control_id.split(".")[0])
    return CATEGORY_MAP.get(major, "organizational")


def parse_description(raw: str) -> tuple[str, str]:
    """
    Split a Probo description into (control_text, implementation_guidance).

    Probo descriptions use '## Why?' and optionally '## What?' markdown headings.
    Returns plain-text sentences suitable for YAML scalar values.
    """
    # Normalise arrow characters and extra whitespace
    raw = raw.replace("⇒", "->").replace("\u21d2", "->")
    raw = re.sub(r"\s+", " ", raw).strip()

    # Split on ## What? (case-insensitive)
    parts = re.split(r"##\s*[Ww]hat\?", raw, maxsplit=1)
    why_part = parts[0]
    what_part = parts[1] if len(parts) > 1 else ""

    # Strip ## Why? heading
    why_text = re.sub(r"##\s*[Ww]hy\?\s*", "", why_part).strip()
    what_text = what_part.strip()

    # Take the first two sentences of each section to keep fixtures concise
    def first_sentences(text: str, n: int = 2) -> str:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return " ".join(sentences[:n]).strip().rstrip(".")

    control_text = first_sentences(why_text, 2) if why_text else why_text
    implementation_guidance = first_sentences(what_text, 2) if what_text else ""

    return control_text, implementation_guidance


def yaml_scalar(value: str, indent: int = 0) -> str:
    """Render a string as a YAML scalar; use block style for long values."""
    if not value:
        return '""'
    if len(value) <= 90 and "\n" not in value:
        # Inline — escape any problematic characters
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    # Block folded scalar
    prefix = " " * indent
    wrapped = textwrap.fill(value, width=90, subsequent_indent=prefix)
    lines = wrapped.split("\n")
    block = "\n".join(f"{prefix}{l}" for l in lines)
    return f">\n{block}"


def slug_to_id(probo_id: str) -> str:
    return f"iso27001:control-{probo_id}"


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------


def convert() -> None:
    data = json.loads(SOURCE.read_text())

    annex_a_entries = []
    skipped = []

    for entry in data:
        std = entry.get("standards", "")
        ctrl = first_annex_a_control(std)
        if ctrl:
            annex_a_entries.append((ctrl, entry))
        else:
            skipped.append(entry)

    # Sort by Annex A control number (numerically by major.minor)
    def sort_key(item):
        parts = [p for p in item[0].split(".") if p]
        return tuple(int(p) for p in parts)

    annex_a_entries.sort(key=sort_key)

    generated = []
    for seq, (ctrl_id, entry) in enumerate(annex_a_entries, start=1):
        num = f"{seq:03d}"
        filename = OUTPUT_DIR / f"SecurityControl-{num}.yaml"

        cat = control_category(ctrl_id)
        ctrl_text, impl_guidance = parse_description(entry.get("description", ""))

        lines = [
            f'id: {slug_to_id(entry["id"])}',
            f'name: {entry["name"]}',
            f'control_id: "{ctrl_id}"',
            f'control_title: {entry["name"]}',
            f'control_category: {cat}',
        ]

        if ctrl_text:
            # Inline if short, block if long
            if len(ctrl_text) <= 90:
                lines.append(f'control_text: "{ctrl_text}"')
            else:
                lines.append(f"control_text: >-")
                for part in textwrap.wrap(ctrl_text, width=90):
                    lines.append(f"  {part}")

        if impl_guidance:
            if len(impl_guidance) <= 90:
                lines.append(f'implementation_guidance: "{impl_guidance}"')
            else:
                lines.append(f"implementation_guidance: >-")
                for part in textwrap.wrap(impl_guidance, width=90):
                    lines.append(f"  {part}")

        lines.append("implementation_status: not_started")

        content = "\n".join(lines) + "\n"
        filename.write_text(content)
        generated.append(filename.name)

    print(f"Generated {len(generated)} SecurityControl fixtures in {OUTPUT_DIR}")

    if skipped:
        print(f"\nSkipped {len(skipped)} non-Annex-A mitigations (clause-level or SOC2-only):")
        for e in skipped:
            stds = e.get("standards", "")
            clauses = _CLAUSE_RE.findall(stds)
            cat = e.get("category", "")
            print(f"  {e['id']:55s}  clauses={clauses}  [{cat}]")


if __name__ == "__main__":
    convert()
