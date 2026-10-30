#!/usr/bin/env python3
"""Deep-merge a licence holder's overlay onto the public iso27001 schema.

For each class, class attribute, slot, enum and permissible value in the
overlay, a non-empty descriptive value (`description`, `comments`, `title`,
`aliases`, `see_also`, `notes`) replaces the public schema's. Structural
fields (slots, ranges, mappings, annotations, is_a and the rest) are kept
from the public schema. The result is written to a separate file; the
public schema is never changed.

The overlay holds the standard's text, so the merged schema does too. The
script therefore writes it only under the repository's tmp/ folder, which
git ignores, and refuses any other output path. src/iso27001/schema/OVERLAY.md
says how to fill the overlay.

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

ROOT = Path(__file__).resolve().parent.parent
# The one folder the merged schema, which holds licensed text, may go to.
PRIVATE_OUTPUT_DIR = ROOT / "tmp"


class IndentedDumper(yaml.SafeDumper):
    """yaml.SafeDumper that indents block-sequence items under their key,
    matching yamllint's default `indentation.indent-sequences: true` rule.
    """

    def increase_indent(self, flow=False, indentless=False):  # noqa: ARG002
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


def merge_class(base: dict, overlay: dict) -> dict:
    """Merge a class and, one by one, its attributes."""
    merged = merge_element(base, overlay)
    base_attrs = (base or {}).get("attributes") or {}
    over_attrs = (overlay or {}).get("attributes") or {}
    if base_attrs and over_attrs:
        merged["attributes"] = {
            name: merge_element(definition or {}, over_attrs.get(name) or {})
            for name, definition in base_attrs.items()
        }
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
    for section, merge in (
        ("classes", merge_class),
        ("slots", merge_element),
        ("enums", merge_enum),
    ):
        base_section = public.get(section) or {}
        over_section = (overlay or {}).get(section) or {}
        if base_section:
            out[section] = {
                name: merge(base_def or {}, over_section.get(name) or {})
                for name, base_def in base_section.items()
            }
    return out


def private_output(path: Path) -> Path:
    """The output path, if it lies under PRIVATE_OUTPUT_DIR; else stop."""
    resolved = path.resolve()
    if not resolved.is_relative_to(PRIVATE_OUTPUT_DIR.resolve()):
        raise SystemExit(
            f"Refusing to write {path}: the merged schema holds licensed text, so "
            f"it goes under {PRIVATE_OUTPUT_DIR}, which git ignores."
        )
    return resolved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--public", required=True, type=Path)
    ap.add_argument("--overlay", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args(argv)

    output = private_output(args.output)
    if not args.overlay.exists():
        raise SystemExit(
            f"Overlay file not found: {args.overlay}\n"
            "Copy iso27001-overlay.template.yaml to iso27001-overlay.yaml and "
            "populate placeholders from your licensed ISO/IEC 27001:2022 copy."
        )

    public = yaml.safe_load(args.public.read_text(encoding="utf-8"))
    overlay = yaml.safe_load(args.overlay.read_text(encoding="utf-8")) or {}

    merged = apply(public, overlay)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as fh:
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
    print(f"Wrote merged schema: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
