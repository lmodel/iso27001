---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/nonconformity
genre: reference
title: Nonconformity
description: A requirement not met, whether of ISO/IEC 27001, of the organization or of an interested party; the schema records one as `IsmsNonconformity`, and the action that removes its cause as `IsmsCorrectiveAction`.
definition: A requirement that was not met.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the classes IsmsNonconformity, IsmsCorrectiveAction and IsmsAuditFinding
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Nonconformity

A nonconformity is a requirement that was not met. Clause 10.2 of ISO/IEC 27001 asks an organization to react to one, deal with its consequences, find its cause, and act so it does not recur. The schema records one as `IsmsNonconformity`, with how it was found, what was done at once, its consequences, its cause, whether similar ones exist, and how it was closed. An `IsmsCorrectiveAction` names the nonconformities it addresses in `action_nonconformities`, with the check that it worked. An audit finding can be a major or minor nonconformity.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the classes IsmsNonconformity, IsmsCorrectiveAction and IsmsAuditFinding
