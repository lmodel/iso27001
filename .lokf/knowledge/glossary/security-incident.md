---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/security-incident
genre: reference
title: Information security event and incident
description: An event is something reported that may bear on information security; an incident is an event assessed as harming it; the schema records an event as `IsmsSecurityEvent` and an incident as its kind `IsmsSecurityIncident`.
definition: An event is something observed that may bear on information security; an incident is an event assessed as harming or threatening it.
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the classes IsmsSecurityEvent and IsmsSecurityIncident
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Information security event and incident

An information security event is something someone reports that may bear on information security. An event that is assessed as harming or threatening information security is an incident, which the organization then responds to and learns from (Annex A 5.24 to 5.28). The schema records an event as `IsmsSecurityEvent`, with when it happened, who reported it, the assets it affects and the assessment. An incident is an `IsmsSecurityIncident`, a kind of event named by `event_type`, with its category, severity, response, containment, eradication and recovery, its evidence, who was told, and what was learned.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the classes IsmsSecurityEvent and IsmsSecurityIncident
