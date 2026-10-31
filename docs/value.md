# Use cases for the ISO/IEC 27001:2022 LinkML schema

This page is for anyone deciding whether to keep their information security management system (ISMS) records as data with this schema. It says what the records support, what the schema does not do, and which mappings it holds today. [About](about.md) says how the elements are named, and [the schema's pages](elements/index.md) describe each one.

## What the records support

### Governance

- **The ISMS as data.** `IsmsManagementSystem` holds the scope, the context and one list for each kind of record, so an organization can keep its ISMS as files in a repository rather than as office documents.
- **Policy reviews.** `IsmsPolicy` and `IsmsTopicSpecificPolicy` carry the document-control fields, among them `document_approval_date` and `document_next_review_date`, so a script can list the policies that are due for review.
- **Roles.** `IsmsRole` records each role's responsibilities, authorities, accountability, holders and line of report, as clause 5.3 asks. A check can then find a process with no named owner.
- **Management review.** `IsmsManagementReview` records the inputs that clause 9.3 lists, such as context changes, performance trends, audit results and risk assessment results, and the decisions and actions that follow.
- **Objectives.** `IsmsObjective` records a target, the current value, the metric and how it is measured, which a dashboard can read.

### Risk, controls and incidents

- **Risk register.** `IsmsRiskAssessment` and `IsmsRisk` record each risk's threat, vulnerability, likelihood, impact, owner and treatment. Each value of `IsmsLikelihood` and `IsmsImpact` carries a `numeric_value` annotation, so a script can compute a risk matrix.
- **Controls.** `IsmsControl` records one of the organization's own controls: the Annex A controls it answers to, its theme, its implementation state, its effectiveness, its last test and its evidence.
- **Statement of Applicability.** `IsmsStatementOfApplicability` holds an `IsmsIncludedControl` or an `IsmsExcludedControl` entry for each Annex A control, each with its justification. So the statement can be built from the risk treatment decisions instead of being kept by hand.
- **Incidents.** `IsmsSecurityEvent` and its kind `IsmsSecurityIncident` record detection, containment, eradication, recovery, evidence and lessons learned. An audit finding's `finding_corrective_action` names the corrective action it led to, so the path from an event to an improvement can be followed.
- **Notification duties.** `incident_notification_required` and `incident_notifications` record whether a regulator must be told and when it was, as NIS2 Article 23 and DORA Article 19 ask.
- **Audit trail.** `IsmsNonconformity` and `IsmsCorrectiveAction` record a nonconformity's cause, the immediate actions, its closure and its evidence, and the corrective actions that address it, as clause 10.2 asks. `IsmsAuditProgramme` and `IsmsAudit` record the audit programme of clause 9.2.2.

### Records kept beside code

- **Checks before a merge.** `project/jsonschema/iso27001.schema.json` validates each record committed to a repository before it is merged, and `linkml-validate` does the same: see [Validating data](index.md#validating-data).
- **Typed code.** The generated dataclasses, Pydantic models and TypeScript types give application code the fields that the validator checks.
- **Linked data.** Each `isms_id` expands to an IRI under `https://w3id.org/lmodel/iso27001/`. The JSON-LD context, the OWL ontology and the SHACL shapes in `project/` let records join a knowledge graph and be checked there.
- **Relational stores.** `project/sqlschema/iso27001.sql` gives a relational schema for the same records.
- **Spreadsheets.** SchemaSheets can turn a spreadsheet register into records of this schema.
- **Evidence collection.** A script can fill `IsmsCompetenceRecord`, `IsmsAwarenessProgramme` (`awareness_completion_tracking` and `awareness_effectiveness`) and `IsmsOperationalProcedure` (`procedure_control_measures`) from training and ticketing systems.

## What the schema does not do

The schema holds records. It runs no workflow, collects no evidence, sends no alert and controls no access to a record: a product or a script does that over the records. It holds none of the standard's text either, as [Licensing and standards rights](rights.md) says.

## Mappings to other vocabularies

LinkML's mapping slots, `exact_mappings`, `close_mappings`, `broad_mappings`, `narrow_mappings` and `related_mappings`, tie a class or a slot to a term of another vocabulary. This schema fills them only from the SSSOM files under `src/iso27001/mappings/`, and only with terms of a released lmodel schema.

These targets wait for a release, or for a namespace:

- MITRE ATT&CK techniques for `control_threats` and `risk_threat`, and the STIX 2.1 Incident for `IsmsSecurityIncident`, once lmodel/attack and lmodel/stix are released;
- NIST CSF 2.0 subcategories, such as `PR.AA-01`, and single SP 800-53 controls, once their lmodel schemas give each one an IRI;
- PROV-O, Dublin Core and schema.org, which publish stable IRIs and need no lmodel schema;
- ISO 31000, SOC 2 and IEC 62443, which publish no IRI for their terms, so a mapping to them needs a namespace of its own first.

Two gaps in the classes limit what a mapping can attach to:

- **Operational technology.** No class records an operational technology (OT) asset. An `IsmsOtAsset`, with its Purdue level from L0 to L4 and mappings to ATT&CK for ICS and IEC 62443, would fill it.
- **Suppliers.** No class records a supplier assessment. An `IsmsSupplierAssessment`, with an SLSA build level, the supplier's SSDF practice maturity, an SPDX SBOM reference and a criticality, would give Annex A 5.19 to 5.23 a record to map to.

## Implementation Status

The SSSOM mapping sets under [`src/iso27001/mappings/`](https://github.com/lmodel/iso27001/tree/main/src/iso27001/mappings) hold the schema's mappings, which `just gen-project` merges into its mapping slots. A row stays only when both ends exist: its subject in this schema, and its object as a term of a released lmodel schema that `tests/neighbours/` holds, named by the IRI that release gives it. `tests/test_schema_rules.py` checks both, and that the files and the schema's mappings agree.

### Published (14 rows)

| Mapping set | Rows | Notes |
|---|---|---|
| `iso27001-to-oscal.sssom.tsv` | 11 | Class-level: the ISMS, a control, the Statement of Applicability and an included control, a risk treatment plan, a corrective action, an audit and an audit programme, a role, the organization and an asset, to lmodel/oscal v0.1.2. |
| `iso27001-to-nist-sp-800-53.sssom.tsv` | 1 | `IsmsControl` related to SP 800-53's control, in lmodel/nist-sp-800-53 v0.1.0. |
| `iso27001-to-spdx.sssom.tsv` | 2 | `IsmsOrganization` close to SPDX's organization and `IsmsAsset` related to SPDX's package, in lmodel/spdx v0.1.0. |

### Dropped until their targets are released

The mapping sets to ATT&CK, CAPEC, CIS Controls, CVE and NVD, CWE, D3FEND, ISO/IEC 29100, ISO/IEC 42001, the KEV catalog, OCSF and STIX were removed, because none of those lmodel schemas has a release yet. The sets to NIST CSF 2.0, SP 800-171, SP 800-218 and SLSA were removed too, because their rows named terms that the released schemas do not hold, such as one IRI per control. The per-control rows of the OSCAL, SP 800-53 and SPDX sets went for the same reason. Each can come back once a release holds terms for it.

### Caveats

Each row's justification is `semapv:LLMBasedMatching`: a language model drafted it, and each kept row was then checked against both classes' descriptions, with a predicate no stronger than the meaning supports. A domain expert should review the rows and promote them to `semapv:ManualMappingCuration`.

### Tooling, tests and generated artefacts

- [`scripts/apply_sssom_overlay.py`](https://github.com/lmodel/iso27001/blob/main/scripts/apply_sssom_overlay.py) merges the SSSOM rows into the schema. Running it twice changes nothing, and it uses `ruamel.yaml` in round-trip mode to keep comments and folded text.
- `just test` runs pytest over every valid example and counter-example, the upstream watch, the overlay and the schema rules. It then runs the valid and invalid examples and the Probo examples through the example runner.
- 61 `IsmsControl` examples under [`tests/data/third_party/probo/`](https://github.com/lmodel/iso27001/tree/main/tests/data/third_party/probo) are derived from the MIT-licensed mitigation catalogue of [Probo](https://github.com/getprobo/probo). The converter turns Probo's `ISO27001:2022-A.X.Y` references into the `IsmsAnnexAControl` values (`a_X_Y`), so every example validates with no edit by hand.
- `just gen-project` writes the Pydantic models and Python dataclasses, JSON Schema, ShEx, SHACL, OWL, GraphQL, Protobuf, the JSON-LD context, SQL DDL, Java classes, TypeScript and an Excel workbook.
- `just gen-project-extended` adds a C++ header, a Pandera schema for tabular checks, a Markdown data dictionary and GOLR index views, among others. Each runs the stock LinkML generator except DBML, whose wrapper, `scripts/gen_dbml_patched.py`, says why.
