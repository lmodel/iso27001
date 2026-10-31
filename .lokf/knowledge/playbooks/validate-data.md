---
type: Playbook
id: https://w3id.org/lmodel/iso27001/knowledge/playbooks/validate-data
genre: how-to
title: Validate ISMS data against the schema
description: How to check a file of ISMS records with `linkml-validate -s src/iso27001/schema/iso27001.yaml -C <Class>`, why dates are written quoted, and what the generated dataclasses and Pydantic models leave unchecked.
resource: docs/index.md
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Validate ISMS data against the schema

1. Run `linkml-validate -s src/iso27001/schema/iso27001.yaml -C IsmsRisk risk.yaml`, naming the class the file holds. It checks the file against the JSON Schema generated from the schema.[^docs-index.md]
2. Write each date and time as a quoted string, as JSON carries them: the validator reads a date as text.
3. Validate a file before loading it into either model in `src/iso27001/datamodel/`. The dataclasses check required fields and enum values but no pattern and no minimum. The Pydantic models also check a pattern or a minimum a field carries itself, but not the patterns of the two types. Neither checks that an included control names an Annex A control or one of the organization's controls.

No check covers that a reference names a record the ISMS holds, that a list never repeats an identifier, that an audit ends after it begins, or that the Statement of Applicability has an entry for each Annex A control.

[^docs-index.md]: docs/index.md, Validating data
