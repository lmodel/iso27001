---
type: Explanation
id: https://w3id.org/lmodel/iso27001/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and what is left out
description: "What the iso27001 schema models (the records an ISMS keeps under clauses 4 to 10 and Annex A of ISO/IEC 27001:2022), what shaped it (the standard, with names from ISO/IEC 27000, ISO/IEC 27005 and ISO 19011), what it maps to, and what it leaves out: the standard's text, certification itself and a fixed risk method."
resource: README.md
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: about.md
    resource: docs/about.md
    title: What is left out
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Unreleased section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Scope, influences and what is left out

The schema models the records an organization keeps to run an ISMS to ISO/IEC 27001:2022, third edition, with Amendment 1:2024, which adds climate action changes. It covers the requirements of clauses 4 to 10 and the 93 reference controls of Annex A, which it names by number alone.[^readme.md]

Its influences are that one publication, and the names three other standards give to what its enums list: ISO/IEC 27000:2026 for the security properties, ISO/IEC 27005 for the risk treatment options and ISO 19011 for the kinds of audit. Its release asset and governance files follow lmodel/nist-csf-v2. It maps to OSCAL, SP 800-53 and SPDX through their released lmodel schemas, and borrows from none.

It leaves out:[^about.md]

- the text of ISO/IEC 27001 and ISO/IEC 27002: clauses, control titles and guidance;
- certification itself, beyond the ISMS's own record of an audit and its certification status;
- a fixed method of risk assessment: its likelihood, impact and risk-level scales and its incident categories are offered for an organization that adopts them.

The changelog's Unreleased section records how the schema was rewritten for its first release: the `Isms` prefix, `isms_id` references, variants told apart by a type designator, and mappings kept only to released terms.[^changelog.md]

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^about.md]: docs/about.md, What is left out
[^changelog.md]: CHANGELOG.md, Unreleased
