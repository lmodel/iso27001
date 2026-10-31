---
type: Explanation
id: https://w3id.org/lmodel/iso27001/knowledge/explanations/names-and-references
genre: explanation
title: How the schema names its elements and links records
description: Why every class and enum carries the `Isms` prefix, how attributes and shared slots are named, how a record refers to another by `isms_id` through `IsmsRecordMixin`, why the record base is a mixin, and how the Statement of Applicability entries and security incidents are told apart by a type designator.
resource: docs/about.md
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Names and Records and references
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: IsmsRecordMixin's comment and the designators
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# How the schema names its elements and links records

Every class and enum carries the `Isms` prefix, so a host can import the schema beside the Linked Open Knowledge Format (LOKF) and other vocabularies without a name clashing. Enums are singular. Slots and enum values are snake_case. A field that one class uses is an attribute of that class, named after the class's subject, such as `risk_owner`. A field that several classes share is a slot of its own, such as `responsible_role`.[^about.md] `linkml-lint` applies its recommended rules unchanged under `.linkmllint.yaml`, and `just lint` fails on a warning.[^linkmllint.yaml]

Every record mixes in `IsmsRecordMixin`, which gives it an `isms_id`, a `title` and a `description`. A reference to another record holds that record's `isms_id`, and `IsmsManagementSystem` lists every kind of record, so each reference can be found there. The base is a mixin rather than a parent class, so that the adapt copy can root some record classes on LOKF's `Concept` and leave the rest alone. `lokf adapt` replaces `isms_id` with LOKF's `id`, and a class that declares `id` itself must descend from `Concept`.[^iso27001.yaml]

Two kinds of record come in variants. A Statement of Applicability entry is an `IsmsIncludedControl` or an `IsmsExcludedControl`, named in `entry_type`. An event assessed as an incident is an `IsmsSecurityIncident`, a kind of `IsmsSecurityEvent`, named in `event_type`. So no field applies only when another holds a given value.

[^about.md]: docs/about.md, Names and Records and references
[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, IsmsRecordMixin's comment
[^linkmllint.yaml]: .linkmllint.yaml, the comment
