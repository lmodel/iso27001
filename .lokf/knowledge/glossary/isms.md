---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/isms
genre: reference
title: Information security management system (ISMS)
description: The organization's managed set of policies, processes, roles and records for information security that ISO/IEC 27001 sets requirements for; the schema's tree root `IsmsManagementSystem` holds one, with its scope and every record it keeps.
definition: The organization's managed system of policies, processes and records by which it runs and improves its information security.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the class IsmsManagementSystem
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Information security management system (ISMS)

An information security management system (ISMS) is the managed system through which an organization sets its information security policy and objectives, treats its risks, and checks and improves what it does. ISO/IEC 27001 states requirements for one. The schema's tree root, `IsmsManagementSystem`, holds one ISMS: its scope, boundaries and exclusions, its internal and external issues, its certification status, and one list for each kind of record it keeps.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the class IsmsManagementSystem
