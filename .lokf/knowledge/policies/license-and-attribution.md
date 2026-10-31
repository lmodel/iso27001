---
type: Policy
id: https://w3id.org/lmodel/iso27001/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The repository's licences and third-party terms: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle and the mappings, no right to the text of ISO/IEC 27001 or 27002, ODC-By for ISO Open Data's records, MIT for Probo's mitigations and the copier template, and Apache-2.0 for the KTL copies."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the Apache License, Version 2.0
  - id: readme.md
    resource: README.md
    title: the License section
  - id: rights.md
    resource: docs/rights.md
    title: the licensing note
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Licence and attribution

The schema and the code are under the Apache License 2.0.[^license] The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares. The mapping sets in the Simple Standard for Sharing Ontological Mappings (SSSOM) format carry the same licence.[^readme.md]

`NOTICE` lists the third-party work the repository carries:[^notice]

- ISO/IEC 27001 is copyright ISO and IEC. The schema models it in the project's own words, cites its clauses by number, and reproduces none of its text. The repository's licence grants no right to that text, and the overlay scaffold holds none.
- ISO Open Data's records under `src/iso27001/schema/iso-open-data/` are under the ODC Attribution License (ODC-By) v1.0, with ISO's attribution text.
- Probo's mitigations and the examples derived from them, under `tests/data/third_party/probo/`, are under the MIT License.
- The justfile, configuration and documentation scaffolding derive from linkml-project-copier, under the MIT License.
- The sidecar's scripts and workflows, and the website, are copies of the Knowledge Trust Ladder templates, under the Apache License 2.0.

`docs/rights.md` sends anyone who needs to reuse ISO's text to ISO.[^rights.md] The project is not an official ISO project.

[^license]: LICENSE, the Apache License, Version 2.0
[^readme.md]: README.md, License
[^notice]: NOTICE, every section
[^rights.md]: docs/rights.md, the licensing note
