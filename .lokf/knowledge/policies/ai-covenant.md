---
type: Policy
id: https://w3id.org/lmodel/iso27001/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema names its clause and never quotes it, no text of ISO/IEC 27001 goes anywhere in the repository, ISO Open Data's records are never edited, and the scheduled librarian proposes changes only through reviewed pull requests."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the project note and the section on agent automation
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that everything a contributor submits is theirs, whatever tools helped make it, and that they must understand, verify and defend it.[^ai_covenant.md] Its note for this project says that the repository models someone else's standard, whose text is copyright and sold. So two failure modes are worse here:

- a requirement or control a model produced, presented as what ISO/IEC 27001 says;
- the standard's own text, reproduced by a model that has read it.

Four rules follow:

- an element under `src/iso27001/schema/` names the clause or Annex A control it models by number, in the project's own words, cited in the pull request;
- no text of the standard goes anywhere in the repository, and a licence holder's wording goes only into the private overlay;
- ISO Open Data's records under `src/iso27001/schema/iso-open-data/` are upstream data, never edited, only replaced from one day's dataset;
- everything the schema defines is in the `iso27001:` namespace, with the standard's own identifiers, such as `A.5.1`, appearing only as values.

The covenant forbids posting AI output as an independent voice in issues or discussions. It sets these rules for the scheduled librarian:

- every change is a pull request that a person approves;
- a read-only job hands its patch to a job that runs no agent;
- a verdict is recorded only where a person said it. AI co-authorship trailers in commits are discouraged.

[^ai_covenant.md]: AI_COVENANT.md, A note specific to this project and Repository-Owned Agent Automation
