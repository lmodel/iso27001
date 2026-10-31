---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/documented-information
genre: reference
title: Documented information
description: Information an organization must keep under control, and the medium it is kept on, such as a policy, a procedure or a record; the schema gives such records `IsmsDocumentControlMixin`'s fields for reference, approval, review, classification, retention and change control.
definition: Information an organization is required to keep under control, with the medium that holds it.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the classes IsmsDocumentControlMixin and IsmsDocumentedInformation
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Documented information

Documented information is what an organization must keep under control, whatever holds it: policies, procedures, plans and the records that show what was done. Clause 7.5 of ISO/IEC 27001 asks for it to be identified, approved, protected, kept and changed under control. The schema mixes `IsmsDocumentControlMixin` into the records that are documented information, with fields for their reference, version, owner, approver, dates, classification, retention, distribution, storage and change control, and holds any other piece of it as an `IsmsDocumentedInformation` of a given kind.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the classes IsmsDocumentControlMixin and IsmsDocumentedInformation
