---
type: Dataset
id: https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
genre: reference
title: iso27001 LinkML schema
description: "The LinkML schema `src/iso27001/schema/iso27001.yaml`, version `2022/Amd 1:2024`: the records an organization keeps to run an information security management system (ISMS) to ISO/IEC 27001:2022, in 38 classes with the `Isms` prefix, 13 enums including the 93 Annex A controls by number, and its `lokf adapt` copy `.lokf/iso27001.yaml`, rooted on seven classes."
resource: src/iso27001/schema/iso27001.yaml
derivedFrom:
  - https://w3id.org/lmodel/iso27001/knowledge/references/iso-iec-27001-2022
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the header, the classes, slots, enums and types
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their comment
  - id: iso27001-copy.yaml
    resource: .lokf/iso27001.yaml
    title: the notes lokf adapt wrote
  - id: lokf-justfile
    resource: .lokf/justfile
    title: the schema line
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# iso27001 LinkML schema

`src/iso27001/schema/iso27001.yaml` is a LinkML schema named `iso27001`, in the namespace `https://w3id.org/lmodel/iso27001/`, under the Apache-2.0 licence.[^iso27001.yaml] Its `version` is `2022/Amd 1:2024`, the edition it models with its one amendment, and its `source` is ISO's page for the edition. Its annotations give the edition (3), its publication date (2022-10-25), the amendment's date (2024-02-23), and the date of ISO Open Data's records it was checked against (2026-10-28). Its comments say that it reproduces no text of the standard.

The schema has 38 classes. One, `IsmsManagementSystem`, is the tree root: it holds the scope and context of the information security management system (ISMS), and one list for each kind of record. Every record mixes in `IsmsRecordMixin`, which gives it an `isms_id`, a `title` and a `description`, and a reference to a record holds its `isms_id`. The records under document control also mix in `IsmsDocumentControlMixin`. The classes cover:

- context and leadership: the organization, interested parties, the information security policy, topic-specific policies and roles;
- planning and risk: objectives, the risk assessment and treatment processes, risk assessments, risks and risk treatment plans;
- controls: the organization's controls, and the Statement of Applicability with its included and excluded entries;
- support and operation: resources, competence records, the awareness programme, the communication plan, other documented information, operational procedures and assets;
- performance evaluation: the monitoring programme, audit programmes, audits, audit findings and management reviews;
- improvement: nonconformities, corrective actions and opportunities for improvement, and security events and incidents.

It has 13 enums. `IsmsAnnexAControl` holds the 93 Annex A controls as `a_5_1` to `a_8_34`, each titled `A.5.1` and so on and annotated with its theme, and `IsmsControlTheme` the four themes. Two types check a retention period as an ISO 8601 duration and a requirement as a clause or Annex A number.

`just lokf-adapt` writes `.lokf/iso27001.yaml`, the copy a knowledge bundle validates against.[^project.justfile] It roots seven classes on `Concept`, the base class of the Linked Open Knowledge Format (LOKF): `IsmsPolicy`, `IsmsTopicSpecificPolicy`, `IsmsRole`, `IsmsControl`, `IsmsAsset`, `IsmsDocumentedInformation` and `IsmsOperationalProcedure`. In the copy, LOKF's `id` takes the place of `isms_id`, `title` and `description` fold into LOKF's, and the two type designators become plain slots.[^iso27001-copy.yaml] The sidecar's justfile names the copy on its `schema :=` line.[^lokf-justfile]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the header, the classes, slots, enums and types
[^project.justfile]: project.justfile, lokf-adapt and its comment
[^iso27001-copy.yaml]: .lokf/iso27001.yaml, the notes
[^lokf-justfile]: .lokf/justfile, the schema line
