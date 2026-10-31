---
type: Playbook
id: https://w3id.org/lmodel/iso27001/knowledge/playbooks/merge-licensed-text
genre: how-to
title: Merge the standard's text into a private copy
description: How a holder of a licence to ISO/IEC 27001 fills a private copy of the overlay scaffold `iso27001-overlay.template.yaml` with the standard's wording and merges it with `just overlay-licensed-text` into `tmp/iso27001-merged.yaml`, which git ignores and which is never distributed.
resource: src/iso27001/schema/OVERLAY.md
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: overlay.md
    resource: src/iso27001/schema/OVERLAY.md
    title: the workflow and merge semantics
  - id: overlay_populated_text.py
    resource: scripts/overlay_populated_text.py
    title: the docstring and private_output
  - id: create_overlay_template.py
    resource: scripts/create_overlay_template.py
    title: the docstring
  - id: test_overlay.py
    resource: tests/test_overlay.py
    title: the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Merge the standard's text into a private copy

The schema's descriptions are the project's own words. A licence holder can put the standard's wording beside them in a private copy, never in the repository.[^overlay.md]

1. Copy `src/iso27001/schema/iso27001-overlay.template.yaml` to `src/iso27001/schema/iso27001-overlay.yaml`, which `.gitignore` keeps out of git. `just create-empty-overlay` writes the scaffold from the schema: every class with its attributes, every slot and every enum with its values, each with an empty `description`.[^create_overlay_template.py]
2. Fill the placeholders you need from your own licensed copy, finding each clause by the element's `iso27001_clause` or `annex_a_control` annotation.
3. Run `just overlay-licensed-text`. It merges only descriptive keys, such as `description` and `comments`, over the public schema, keeps every structural field, and writes `tmp/iso27001-merged.yaml`. It refuses an output path outside `tmp/`.[^overlay_populated_text.py]
4. Use the merged file with your own tools, and never commit or publish it or the overlay.

`tests/test_overlay.py` checks that the scaffold in the repository holds no text and is the one the script writes, that git ignores the overlay and `tmp/`, and that the merge changes only descriptive keys.[^test_overlay.py]

[^overlay.md]: src/iso27001/schema/OVERLAY.md, the three files, the workflow and the merge semantics
[^create_overlay_template.py]: scripts/create_overlay_template.py, the docstring
[^overlay_populated_text.py]: scripts/overlay_populated_text.py, the docstring and private_output
[^test_overlay.py]: tests/test_overlay.py, the tests
