#!/usr/bin/env python3
"""Deep-merge an overlay schema onto the public iso27001 schema.

For each element in the overlay, non-empty `description` / `comments` values
replace the corresponding values in the public schema. Structural fields
(slots, ranges, mappings, annotations, is_a, etc.) are preserved from the
public schema. The result is written to a separate file; the public schema is
never modified in place.

Usage:
    uv run python scripts/overlay_populated_text.py \
        --public  src/iso27001/schema/iso27001.yaml \
        --overlay src/iso27001/schema/iso27001-overlay.yaml \
        --output  tmp/iso27001-merged.yaml
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


OVERLAY_KEYS = ("description", "comments", "title", "aliases", "see_also", "notes")


def _is_empty(v) -> bool:
    if v is None:
        return True
    if isinstance(v, (str, list, dict)) and len(v) == 0:
        return True
    return False


def merge_element(base: dict, overlay: dict) -> dict:
    if not overlay:
        return base
    merged = dict(base) if base else {}
    for key in OVERLAY_KEYS:
        if key in overlay and not _is_empty(overlay[key]):
            merged[key] = overlay[key]
    return merged


def merge_enum(base: dict, overlay: dict) -> dict:
    merged = merge_element(base, overlay)
    base_pv = (base or {}).get("permissible_values") or {}
    over_pv = (overlay or {}).get("permissible_values") or {}
    if not over_pv:
        return merged
    new_pv = {}
    for name, base_def in base_pv.items():
        new_pv[name] = merge_element(base_def or {}, over_pv.get(name) or {})
    merged["permissible_values"] = new_pv
    return merged


def apply(public: dict, overlay: dict) -> dict:
    out = dict(public)
    for section in ("classes", "slots"):
        base_section = public.get(section) or {}
        over_section = (overlay or {}).get(section) or {}
        if not base_section:
            continue
        merged_section = {}
        for name, base_def in base_section.items():
            merged_section[name] = merge_element(base_def or {}, over_section.get(name) or {})
        out[section] = merged_section

    base_enums = public.get("enums") or {}
    over_enums = (overlay or {}).get("enums") or {}
    if base_enums:
        merged_enums = {}
        for name, base_def in base_enums.items():
            merged_enums[name] = merge_enum(base_def or {}, over_enums.get(name) or {})
        out["enums"] = merged_enums
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--public", required=True, type=Path)
    ap.add_argument("--overlay", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    if not args.overlay.exists():
        raise SystemExit(
            f"Overlay file not found: {args.overlay}\n"
            "Copy iso27001-overlay.template.yaml to iso27001-overlay.yaml and "
            "populate placeholders from your licensed ISO/IEC 27001:2022 copy."
        )

    public = yaml.safe_load(args.public.read_text(encoding="utf-8"))
    overlay = yaml.safe_load(args.overlay.read_text(encoding="utf-8")) or {}

    merged = apply(public, overlay)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fh:
        fh.write(
            "# AUTO-GENERATED merged schema. Contains verbatim ISO/IEC 27001:2022\n"
            "# text from the local overlay. NOT FOR REDISTRIBUTION.\n\n"
        )
        yaml.dump(
            merged,
            fh,
            Dumper=IndentedDumper,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=120,
            indent=2,
        )
    print(f"Wrote merged schema: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
