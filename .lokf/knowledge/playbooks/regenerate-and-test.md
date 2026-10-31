---
type: Playbook
id: https://w3id.org/lmodel/iso27001/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit `src/iso27001/schema/iso27001.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just create-empty-overlay`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Development setup and Before opening a pull request sections
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Regenerate and test after a schema change

1. Install the toolchain once: Python 3.10 or later, `uv` and `just`, then `uv sync --group dev` in the clone.[^contributing.md]
2. Edit `src/iso27001/schema/iso27001.yaml`, the one file to write by hand. Name the clause or Annex A control a new or changed element models, by number, and quote nothing from the standard.
3. Run `just lint`, which runs `linkml-lint` on the schema under `.linkmllint.yaml` and fails on a warning.[^justfile]
4. Run `just gen-project` and `just gen-doc`, then `just create-empty-overlay`, which rewrites the overlay scaffold, and `just lokf-adapt`, which rewrites the adapt copy with its seven roots.[^project.justfile] Commit the output.
5. Add an example under `tests/data/valid/` for a new class, and a counter-example under `tests/data/invalid/` for a new constraint whose first line names where it fails, then run `just test`.
6. Run the pre-commit hooks on what you staged (`uvx pre-commit run`), and write a changelog entry under `## [Unreleased]` when the change alters behaviour.

CI runs the same: [Build and test](../workflows/main.md) runs `just lint`, `just test` and `just lokf-adapt-check`, and fails when the adapt copy is stale.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
[^project.justfile]: project.justfile, lokf-adapt and lokf-adapt-check
