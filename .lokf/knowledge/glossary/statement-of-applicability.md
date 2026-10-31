---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/statement-of-applicability
genre: reference
title: Statement of Applicability
description: The record that lists each control an organization needs, with why and whether it is in place, and each Annex A control it leaves out, with why; the schema models it as `IsmsStatementOfApplicability`, with `IsmsIncludedControl` and `IsmsExcludedControl` entries.
definition: The record of which controls an organization includes, why, and whether each is in place, and which Annex A controls it excludes, and why.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the classes IsmsStatementOfApplicability, IsmsIncludedControl and IsmsExcludedControl
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Statement of Applicability

The Statement of Applicability is the record ISO/IEC 27001 clause 6.1.3 asks for: the controls an organization needs, why it includes each and whether each is in place, and why it leaves out any Annex A control. The schema models it as `IsmsStatementOfApplicability`, whose `soa_entries` hold `IsmsIncludedControl` and `IsmsExcludedControl` entries. Every entry gives a justification. An included entry names an Annex A control, one of the organization's controls or both, and its implementation state. An excluded entry names the Annex A control it leaves out.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the classes IsmsStatementOfApplicability, IsmsIncludedControl and IsmsExcludedControl
