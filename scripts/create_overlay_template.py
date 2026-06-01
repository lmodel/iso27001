#!/usr/bin/env python3
"""Generate an empty overlay scaffold from the public iso27001 schema.

The scaffold lists every class, slot, and enum permissible value with empty
placeholder fields (`description`, `comments`) for a license owner to fill in
with verbatim normative ISO/IEC text. The scaffold itself contains NO
copyrighted text and is safe to commit.

Usage:
    uv run python scripts/create_overlay_template.py \
        --public src/iso27001/schema/iso27001.yaml \
        --output src/iso27001/schema/iso27001-overlay.template.yaml
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml


class IndentedDumper(yaml.SafeDumper):
    """yaml.SafeDumper that indents block-sequence items under their key,
    matching yamllint's default `indentation.indent-sequences: true` rule.
    """

    def increase_indent(self, flow=False, indentless=False):  # noqa: D401, ARG002
        return super().increase_indent(flow, False)


HEADER = """\
# =============================================================================
# iso27001-overlay.template.yaml
#
# Empty overlay scaffold for ISO/IEC 27001:2022 + Amd. 1:2024. Generated from
# the public schema. Contains NO copyrighted text and is safe to distribute.
#
# License owners of ISO/IEC 27001:2022 may copy this file to
#     iso27001-overlay.yaml
# and populate the empty `description:` / `comments:` placeholders with
# verbatim normative text from their licensed copy of the standard.
#
# The populated `iso27001-overlay.yaml` is ignored by git (see .gitignore)
# and must NOT be redistributed. Apply it locally with:
#     just overlay-licensed-text
#
# Merge semantics: deep-merge over iso27001.yaml. For each element, only the
# `description` and `comments` keys are overlaid; all structural fields
# (slots, ranges, mappings, annotations) are preserved from the public schema.
# =============================================================================

id: https://w3id.org/lmodel/iso27001/overlay
name: iso27001-overlay
description: |-
  Verbatim normative-text overlay for the iso27001 LinkML schema.
  Not for redistribution. Requires a valid ISO/IEC 27001:2022 license.
license: PROPRIETARY-ISO-IEC-27001-2022
"""


def _placeholder() -> dict:
    return {"description": "", "comments": []}


def build_scaffold(public: dict) -> dict:
    out: dict = {}

    classes = public.get("classes") or {}
    if classes:
        out["classes"] = {name: _placeholder() for name in sorted(classes)}

    slots = public.get("slots") or {}
    if slots:
        out["slots"] = {name: {"description": ""} for name in sorted(slots)}

    enums = public.get("enums") or {}
    if enums:
        enum_block: dict = {}
        for ename, edef in sorted(enums.items()):
            pv = (edef or {}).get("permissible_values") or {}
            enum_block[ename] = {
                "description": "",
                "permissible_values": {v: {"description": ""} for v in sorted(pv)},
            }
        out["enums"] = enum_block

    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--public", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    public = yaml.safe_load(args.public.read_text(encoding="utf-8"))
    scaffold = build_scaffold(public)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fh:
        fh.write(HEADER)
        fh.write("\n")
        yaml.dump(
            scaffold,
            fh,
            Dumper=IndentedDumper,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100,
            indent=2,
        )
    print(f"Wrote scaffold: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
