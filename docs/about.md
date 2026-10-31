# About iso27001

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named, how records refer to one another, and
what the model leaves out.

ISO/IEC 27001:2022 sets requirements for an information security management
system in its clauses 4 to 10, and lists 93 reference controls in Annex A,
sorted into four themes. The schema models the records an organization keeps
to meet those requirements, one class for each kind of record, and holds them
in one `IsmsManagementSystem`. It names each Annex A control by its number
alone, in the `IsmsAnnexAControl` enum.

## Names

Element names are the schema's own. Classes and enums carry the `Isms` prefix
(`IsmsRisk`, `IsmsControlTheme`), so they can be imported beside the Linked
Open Knowledge Format (LOKF) and other vocabularies without a clash. Enums are
singular. Slots and enum values are snake_case. A field one class uses is an
attribute of that class, and its name starts with the class's subject
(`risk_owner`, `audit_scope`). A field several classes share is a slot of its
own (`responsible_role`, `affected_assets`). Every element is in the
`iso27001:` namespace (`https://w3id.org/lmodel/iso27001/`).

The Annex A values are `a_5_1` to `a_8_34`, each titled `A.5.1` and so on and
annotated with its theme. Each class and many slots cite the clause or Annex
A control they model, by number, in an `iso27001_clause` or `annex_a_control`
annotation.

The descriptions are this project's own words, and none quotes the standard.
[OVERLAY.md](https://github.com/lmodel/iso27001/blob/main/src/iso27001/schema/OVERLAY.md)
says how a licence holder merges the standard's wording into a private copy.

## Records and references

Every record mixes in `IsmsRecordMixin`, so it has an `isms_id`, a `title` and
a `description`. A record that refers to another holds the other's `isms_id`,
as `topic_policy_parent` and `risk_existing_controls` do, and
`IsmsManagementSystem` holds each kind of record in a list of its own, so
every identifier a reference names can be found there. The records under
document control (clause 7.5) also mix in `IsmsDocumentControlMixin`, which
carries their reference, version, owner, approval, review dates,
classification and retention.

Two kinds of record come in variants, told apart by a type designator:

- An entry of the Statement of Applicability is an `IsmsIncludedControl`,
  which says why the control is needed and whether it is in place, or an
  `IsmsExcludedControl`, which says why an Annex A control is left out.
  `entry_type` names which.
- An information security event that is assessed as an incident is an
  `IsmsSecurityIncident`, a kind of `IsmsSecurityEvent`. `event_type` names
  which.

## What is left out

The schema holds no text of ISO/IEC 27001 or ISO/IEC 27002: no clause, no
control title and no guidance. It models no audit by a certification body
beyond its record as an `IsmsAudit`, and no certification scheme. Its scales
of likelihood, impact and risk level, and its incident categories, are offered
for an organization that adopts them. The standard leaves both to the
organization. The mappings name only terms of released lmodel schemas, and
[Use cases](value.md#implementation-status) lists the ones dropped until their
targets are released.

## Reference

- [ISO/IEC 27001:2022 on ISO's site](https://www.iso.org/standard/82875.html)
- [ISO/IEC 27001:2022/Amd 1:2024 on ISO's site](https://www.iso.org/standard/88435.html)
- [ISO Open Data](https://www.iso.org/open-data.html), whose records of both
  the repository keeps
