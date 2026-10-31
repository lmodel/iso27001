---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/annex-a-control
genre: reference
title: Annex A control
description: One of the 93 reference controls that Annex A of ISO/IEC 27001:2022 lists in four themes; the schema names each by number in the `IsmsAnnexAControl` enum, from `a_5_1` to `a_8_34`, without its title or text.
definition: One of the 93 reference controls Annex A lists, which an organization compares its own controls against.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the enums IsmsAnnexAControl and IsmsControlTheme
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Annex A control

Annex A of ISO/IEC 27001:2022 lists 93 reference controls in four themes: organizational (A.5.1 to A.5.37), people (A.6.1 to A.6.8), physical (A.7.1 to A.7.14) and technological (A.8.1 to A.8.34). An organization compares the controls it needs with the list, so that it leaves none out by oversight. The schema names each by number in `IsmsAnnexAControl`, from `a_5_1` to `a_8_34`. Each value is titled with its number, such as `A.5.1`, and annotated with its theme. The schema carries none of the controls' titles or text, which are ISO's.[^iso27001.yaml] An organization's own control is an `IsmsControl`, which lists the Annex A controls it answers to.

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the enums IsmsAnnexAControl and IsmsControlTheme
