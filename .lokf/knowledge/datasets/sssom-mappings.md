---
type: Dataset
id: https://w3id.org/lmodel/iso27001/knowledge/datasets/sssom-mappings
genre: reference
title: SSSOM mappings to released lmodel schemas
description: The three SSSOM mapping sets under `src/iso27001/mappings/`, 14 class-level rows from the schema's classes to classes of the released lmodel/oscal, lmodel/nist-sp-800-53 and lmodel/spdx schemas, which `just gen-project` merges into the schema, and the sets dropped until their targets are released.
resource: src/iso27001/mappings
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: mappings
    resource: src/iso27001/mappings
    title: the three mapping sets
  - id: apply_sssom_overlay.py
    resource: scripts/apply_sssom_overlay.py
    title: the docstring
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the mapping tests
  - id: value.md
    resource: docs/value.md
    title: the Implementation Status section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# SSSOM mappings to released lmodel schemas

`src/iso27001/mappings/` holds three mapping sets in the Simple Standard for Sharing Ontological Mappings (SSSOM) format, under CC BY 4.0, with 14 rows in all:[^mappings]

- `iso27001-to-oscal.sssom.tsv`, 11 rows to classes of lmodel/oscal v0.1.2;
- `iso27001-to-nist-sp-800-53.sssom.tsv`, one row to lmodel/nist-sp-800-53 v0.1.0;
- `iso27001-to-spdx.sssom.tsv`, two rows to lmodel/spdx v0.1.0.

Each row maps a class of the schema to a class of a released schema, named by the IRI that release gives it, with `skos:closeMatch`, `skos:broadMatch` or `skos:relatedMatch`. Each row's justification is `semapv:LLMBasedMatching`: a language model drafted it, and each kept row was then checked against both classes' descriptions. `just apply-sssom-overlay`, which `just gen-project` runs first, merges the rows into the schema's mapping slots.[^apply_sssom_overlay.py]

`tests/test_schema_rules.py` checks that every mapping in the adapt copy names a term of a released copy in `tests/neighbours/`, and that the SSSOM rows and the schema's mappings agree.[^test_schema_rules.py] The sets to schemas with no release, and the rows that named terms the releases do not hold, were dropped; `docs/value.md` lists them.[^value.md]

[^mappings]: src/iso27001/mappings, the three mapping sets
[^apply_sssom_overlay.py]: scripts/apply_sssom_overlay.py, the docstring
[^test_schema_rules.py]: tests/test_schema_rules.py, test_mappings_name_a_released_term and test_sssom_rows_are_the_schema_mappings
[^value.md]: docs/value.md, Implementation Status
