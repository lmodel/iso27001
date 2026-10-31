# Use Cases for the ISO/IEC 27001:2022 LinkML Schema

## Contents

- [LinkML](#linkml)
- [ISO27001 SCHEMA](#iso27001-schema)
- [Governance](#governance)
  - [ISMS-as-Data](#isms-as-data)
  - [Policy Lifecycle Management](#policy-lifecycle-management)
  - [Roles, Responsibilities, and Accountability](#roles-responsibilities-and-accountability)
  - [Management Review Evidence](#management-review-evidence)
  - [Objectives Tracking](#objectives-tracking)
- [Cybersecurity](#cybersecurity)
  - [Risk Register](#risk-register)
  - [Control Tracking Against Annex A](#control-tracking-against-annex-a)
  - [Statement of Applicability Automation](#statement-of-applicability-automation)
  - [Incident Response Traceability](#incident-response-traceability)
  - [Threat Intelligence Integration](#threat-intelligence-integration)
- [DevSecOps](#devsecops)
  - [Schema-as-Code](#schema-as-code)
  - [CI/CD Compliance Gates](#cicd-compliance-gates)
  - [Infrastructure-as-Code Alignment](#infrastructure-as-code-alignment)
  - [Automated Evidence Collection](#automated-evidence-collection)
  - [SHACL/ShEx Validation of Linked Data Artifacts](#shaclshex-validation-of-linked-data-artifacts)
- [Regulatory Compliance](#regulatory-compliance)
  - [Multi-Framework Mapping](#multi-framework-mapping)
  - [Documented Information Inventory](#documented-information-inventory)
  - [Nonconformity and Corrective Action Audit Trail](#nonconformity-and-corrective-action-audit-trail)
  - [Audit Programme Management](#audit-programme-management)
  - [NIS2 / DORA Readiness](#nis2--dora-readiness)
  - [Export to SQL / Relational GRC](#export-to-sql--relational-grc)
- [Integration](#integration)
  - [Linked Data and Knowledge Graph](#linked-data-and-knowledge-graph)
  - [GRC Platform Data Exchange](#grc-platform-data-exchange)
  - [SIEM and SOAR Enrichment](#siem-and-soar-enrichment)
  - [Asset Management System Integration](#asset-management-system-integration)
  - [Spreadsheet / GRC Import via SchemaSheets](#spreadsheet--grc-import-via-schemasheets)
  - [Python and TypeScript SDK Generation](#python-and-typescript-sdk-generation)
  - [Semantic Cross-Framework Alignment via LinkML Mappings](#semantic-cross-framework-alignment-via-linkml-mappings)
- [lmodel Ecosystem](#lmodel-ecosystem)
- [Compliance and Control Frameworks](#compliance-and-control-frameworks)
- [Threat Intelligence and Incident Response](#threat-intelligence-and-incident-response)
- [Unified Cyber Ontology](#unified-cyber-ontology)
- [Supply Chain and Software Integrity](#supply-chain-and-software-integrity)
- [Linked Data Infrastructure](#linked-data-infrastructure)
- [Summary Assessment](#summary-assessment)
- [Implementation Status](#implementation-status)

## LinkML

Assisted-By: [LinkML Community](https://linkml.io/linkml/intro/overview.html)

LinkML models are organized around the core concepts of Classes and Slots. They are authored in YAML and allow both rich expressivity while keeping things simple in a way that allows non-technical domain modelers to contribute.

LinkML offers many features of use to data modelers, while retaining a simple core

- Classes can be arranged in inheritance hierarchies
- Powerful yet easy to use Semantic enumerations that can optionally be backed by ontologies
- Create data models that are independent of a database technology
- Develop machine-actionable reporting standards and data dictionaries
- Include rich annotations and mappings as part of a model
- “Linked Data” ready
  - All schemas have a corresponding JSON-LD context
  - Compatibility with RDF tooling, without committing to an RDF stack
  - Compilation to SHACL and ShEx
  - Export of data models to OWL Schemas

Many frameworks lock you in to a particular view of the world or technology. This can lead to silos, and the need to create mappings and transformations between different representations of the same data; for example, if your JSON documents need to work in concert with your relational database or graph store.

LinkML has many different generators for existing frameworks that allow the translation of a LinkML schema to other frameworks:

- Convert to JSON-LD contexts, and instantly port your data to RDF
- Convert to JSON-Schema and using JSON-Schema validators
- Convert to SHACL or ShEx and validate your RDF data
- Convert to Python dataclasses or pydantic for easy use within applications
- Generate SQL Schemas or SQL Alchemy for use with relational databases and validate your database with SQL Validation

Using the LinkML toolchain you can go from a schema to a statically hosted searchable website in minutes, with pages for each of your schema elements. Using lightweight namespace registries such as w3id.org you can easily have resolvable URIs for all your concepts.

LinkML can be thought of as two interlocking parts:

- A standard for representing schemas, data dictionaries, standards, and metadata
- A reference tool stack for doing things with artefacts that conform to the standard

The core LinkML toolchain is written in Python allows for:

- generating downstream schema artefacts, including:
  - documentation and static sites
  - code for use by developers (data class in Python, Java, and Typescript, ORMs, enumerations)
  - conversion between alternate representations like JSON-Schema, SQL DDL, RDF Shapes, Protobuf, …
  - validation and linting of schemas
  - data conversion between JSON, TSV, and RDF (where that data conforms to a LinkML schema)
  - data validation of JSON, TSVs, or RDF using either JSON-Schema, SPARQL, or ShEx
  - easy programmatic manipulation of schemas

LinkML is part of a growing ecosystem of general purpose tools that make curating, mapping, ingesting, and organizing data much easier

- schema-automator bootstraps schemas from existing structured and semi-structured sources
- LinkML-OWL allows for generation of complex OWL axioms from datamodels
- SchemaSheets converts between spreadsheets and schemas
- DataHarmonizer is an ontology-based curation tool that is being adapted to LinkML

## ISO27001 SCHEMA

Assisted-By: Claude Code

The schema is not just a data model - it is a machine-actionable, multi-format artifact generator.The combination of ISO 27001 clause coverage, LinkML's compilation targets, and Linked Data identity (w3id.org URIs) opens a wide range of downstream applications.

### Governance

#### ISMS-as-Data

The root `IsmsManagementSystem` class aggregates every governance artifact - scope,policy, roles, objectives, and review records - into a single addressable entity. This enables an organisation to publish its ISMS structure as structured open data rather than collections of Word documents.

#### Policy Lifecycle Management

`IsmsPolicy` and `IsmsTopicSpecificPolicy` carry approval dates, review dates, commitment statements, and audience assignments. A governance team can drive policy review workflows from structured YAML records rather than spreadsheet trackers, with automated alerts when `document_next_review_date`is approaching.

#### Roles, Responsibilities, and Accountability

`IsmsRole` with `role_responsibilities`, `role_authorities`, `role_accountability`, `role_holders`, and `role_reports_to` slots maps directly to Clause 5.3 requirements. It can power org-chart tooling, responsibility assignment matrices (RACI), and automated checks that every ISMS process has a named owner.

#### Management Review Evidence

`IsmsManagementReview` captures all Clause 9.3 inputs (context changes, interested-party changes, performance trends, audit results, risk status) and outputs (decisions, action items). Structured records make it straightforward to extract management review packs automatically or generate evidence bundles for certification bodies.

#### Objectives Tracking

`IsmsObjective` includes `objective_target`, `objective_current_value`, `objective_metric`, and `objective_measurement_method`. A dashboard layer can query these records to produce live objective achievement status without manual reporting.

### Cybersecurity

#### Risk Register

`IsmsRisk`, `IsmsRiskAssessment`, and `IsmsRiskAssessmentProcess` implement the full Clause 6.1.2 workflow: criteria definition, threat/vulnerability pairing, CIA impact analysis, likelihood/impact scoring, and risk-level derivation. The `IsmsLikelihood` and `IsmsImpact` enumerations with `numeric_value` annotations make automated risk matrix computation straightforward.

#### Control Tracking Against Annex A

`IsmsControl` with the `IsmsControlTheme` enum (organizational / people / physical / technological) and `IsmsImplementationStatus` enum models all 93 Annex A controls. `implementation_state`, `control_effectiveness`, `control_last_tested`, and `control_evidence` slots enable a live control effectiveness dashboard without a dedicated GRC product.

#### Statement of Applicability Automation

`IsmsStatementOfApplicability` with `IsmsApplicabilityEntry` records (an `IsmsIncludedControl` or `IsmsExcludedControl` each, with its `entry_justification`, and the included control's `implementation_state`) can be generated directly from risk treatment decisions. Changes to the risk register can automatically propagate to the SoA, replacing the error-prone manual maintenance of spreadsheet-based SoAs.

#### Incident Response Traceability

`IsmsSecurityEvent` and its kind `IsmsSecurityIncident`, with the `incident_containment_actions`, `incident_eradication_actions`, `incident_recovery_actions`, `incident_lessons_learned` and `incident_evidence` slots, model the full incident lifecycle. An event assessed as an incident is recorded as an incident, and an audit finding's `finding_corrective_action` names the corrective action it led to, so the chain from detection to ISMS improvement is traceable.

#### Threat Intelligence Integration

`control_threats` on `IsmsControl` and `risk_threat` / `risk_vulnerability` on `IsmsRisk` provide structured attachment points for threat intelligence feeds. Because all entities have URI-based identifiers, external threat data (CVEs, STIX objects) can be linked in rather than embedded.

### DevSecOps

#### Schema-as-Code

LinkML compiles `iso27001.yaml` to Python dataclasses (`iso27001.py`), Pydantic models
(`iso27001_pydantic.py`), TypeScript types, and JSON-Schema. Application teams can import the generated dataclasses directly, making compliance data a typed first-class citizen in pipelines - not an afterthought.

#### CI/CD Compliance Gates

The generated JSON-Schema (`project/jsonschema/iso27001.schema.json`) can be applied as a validation step in a pipeline. Any ISMS artifact committed to a repository (control records, risk assessments, SoA entries) is validated against the schema before merge, enforcing data quality at the source.

#### Infrastructure-as-Code Alignment

`IsmsControl` records map Annex A controls to `control_asset_types` and `control_threats`. When a Terraform or Ansible change modifies a listed asset, tooling can automatically flag which controls and risks reference that asset, surfacing security review requirements without manual cross-referencing.

#### Automated Evidence Collection

`IsmsOperationalProcedure` with `procedure_control_measures` and `document_last_review_date` alongside `IsmsCompetenceRecord` and `IsmsAwarenessProgramme` (with `awareness_completion_tracking` and `awareness_effectiveness`) give automation agents structured targets. Evidence-collection scripts can populate these records from ticketing
systems, LMS platforms, and SIEM logs.

#### SHACL/ShEx Validation of Linked Data Artifacts

`project/shacl/iso27001.shacl.ttl` can validate RDF-serialised compliance data in any graph-based pipeline. A DevSecOps team building a knowledge graph of assets, risks, and controls can enforce schema correctness using standard RDF tooling without writing custom validators.

### Regulatory Compliance

#### Multi-Framework Mapping

Classes in the schema carry `iso27001_clause` and `annex_a_control` annotations that anchor each construct to the source standard and act as extension points. Annotations for ISO 27002 control guidance references, NIST CSF subcategory mappings, SOC 2 criteria, or NIS2 obligations can be added alongside the existing clause references. A single ISMS record can carry alignment metadata for multiple frameworks simultaneously.

#### Documented Information Inventory

`IsmsDocumentControlMixin`, mixed into the policies, processes, plans, records and `IsmsDocumentedInformation`, with the `document_reference`, `document_approver`, `document_approval_date`, `document_effective_date`, `document_next_review_date` and `document_classification` slots, and `IsmsDocumentedInformation`'s `document_kind`, provides the full Clause 7.5 documented information control register. This is directly auditable by certification bodies.

#### Nonconformity and Corrective Action Audit Trail

`IsmsNonconformity` and `IsmsCorrectiveAction`, with `nonconformity_root_cause`, `nonconformity_immediate_actions`, the corrective action's `action_nonconformities`, `nonconformity_closure_date` and `nonconformity_closure_evidence`, implement the complete Clause 10.2 audit trail. Every step is structured and linkable, satisfying both internal audit and third-party certification evidence requirements.

#### Audit Programme Management

`IsmsAuditProgramme` and `IsmsAudit` with `audit_criteria`, `audit_period_start` and `audit_period_end`, `audit_lead`, `audit_auditees`, `audit_findings` and `audit_report_distribution` model the Clause 9.2.2 audit programme. Structured records support audit scheduling systems, finding trackers, and closure verification workflows.

#### NIS2 / DORA Readiness

`IsmsSecurityIncident` with `incident_notification_required` and `incident_notifications` slots directly supports regulatory incident notification obligations (NIS2 Article 23, DORA Article 19). Structured incident records can feed a notification tracking system and produce regulator-ready evidence exports.

#### Export to SQL / Relational GRC

`project/sqlschema/iso27001.sql` provides a relational schema for loading ISMS data into any SQL database. Organisations with existing GRC databases can import or synchronise records without building a bespoke data model.

### Integration

#### Linked Data and Knowledge Graph

All entity identifiers are URIs under `https://w3id.org/lmodel/iso27001/`.
`project/jsonld/iso27001.jsonld` and `project/owl/iso27001.owl.ttl` enable ISMS data to participate in enterprise knowledge graphs alongside asset inventories, identity systems, and vulnerability databases - with SPARQL as the query layer.

#### GRC Platform Data Exchange

`project/jsonschema/iso27001.schema.json` is the interchange format for GRC platform APIs. Any GRC product that accepts JSON-Schema-validated payloads (ServiceNow GRC, Archer, OneTrust, Vanta) can ingest or export ISMS records through this schema without proprietary data mapping.

#### SIEM and SOAR Enrichment

`IsmsSecurityEvent` and `IsmsSecurityIncident` records referenced by URI can be enriched from SIEM alert payloads. A SOAR playbook can populate `incident_detection_method`, `affected_assets`, `incident_containment_actions`, and `incident_evidence` slots automatically when an alert fires, creating structured incident records without analyst data entry.

#### Asset Management System Integration

`IsmsAsset` with `asset_category`, `asset_owner`, `asset_custodian`, `asset_classification`, `asset_location`, and `criticality` links to risk and control records by URI. This is the bridge between CMDB/asset inventory tools (ServiceNow CMDB, Snipe-IT) and the ISMS risk register - changes in the asset inventory can trigger automatic risk reassessment workflows.

#### Spreadsheet / GRC Import via SchemaSheets

Existing SoA spreadsheets, risk registers, or control tracking workbooks can be bootstrapped into schema-conformant YAML using SchemaSheets, lowering the migration barrier for organisations moving from spreadsheet-based ISMS management.

#### Python and TypeScript SDK Generation

The generated `iso27001.py` (dataclasses), `iso27001_pydantic.py`, and
`project/typescript/iso27001.ts` are drop-in libraries for application developers building compliance portals, audit tooling, or internal GRC APIs. No hand-written data models are required - the schema is the single source of truth for both validation and application code.

#### Semantic Cross-Framework Alignment via LinkML Mappings

LinkML provides five semantic mapping slots - `exact_mappings`, `close_mappings`, `broad_mappings`, `narrow_mappings`, and `related_mappings` - that attach external vocabulary URIs directly to any class or slot in the schema. Once declared, these mappings are automatically embedded in the generated JSON-LD `@context`, OWL axioms, and SPARQL endpoints, enabling federated queries across datasets without hand-written translation code.

The five slots carry distinct semantic precision:

| Slot | Meaning | Example application |
|---|---|---|
| `exact_mappings` | Concepts are fully equivalent | `IsmsOrganization` -> `schema:Organization`; `IsmsDocumentControlMixin` slots -> Dublin Core `dc:title`, `dc:date` |
| `close_mappings` | Closely related but not identical | `IsmsCorrectiveAction` -> ISO 9001 corrective action; `IsmsNonconformity` -> COBIT process deviation |
| `broad_mappings` | External concept is broader | `IsmsObjective` -> COBIT governance objective category |
| `narrow_mappings` | External concept is narrower | `IsmsControl` -> a specific CIS Control sub-control or NIST SP 800-53 control enhancement |
| `related_mappings` | Loosely associated | `IsmsAuditFinding` -> PROV-O `Activity`; `control_threats` values -> MITRE ATT&CK technique IDs |

**NIST Cybersecurity Framework alignment.** Adding `exact_mappings` or `close_mappings` from `IsmsControl` instances to NIST CSF v2 subcategory URIs (e.g., `PR.AA-01` identity-management, `DE.CM-01` network monitoring) allows a single control record to simultaneously satisfy ISO 27001 Annex A and CSF reporting requirements. Tools that consume the JSON-LD output resolve both identifiers without any additional mapping layer.

**MITRE ATT&CK threat linkage.** The `control_threats` slot on `IsmsControl` and
`risk_threat` on `IsmsRisk` can carry `related_mappings` to ATT&CK technique, tactic, or mitigation URIs. An ATT&CK mapping set once attached Annex A controls to ATT&CK *Mitigation* identifiers and incident categories to *Tactic* identifiers; it was dropped until lmodel/attack has a release whose terms a mapping can name. Restored, it would connect the ISMS risk register directly to the threat intelligence vocabulary, enabling automated correlation between SIEM detections (tagged with ATT&CK IDs) and the controls designed to address them.

**STIX/TAXII incident interoperability.** `IsmsSecurityIncident` mapped via `close_mappings` to the STIX 2.1 `Incident` object type lets incident records be exported as STIX bundles for sharing via TAXII feeds, or enriched from incoming threat intelligence without field-by-field translation.

**Provenance and audit trail via PROV-O.** `IsmsAuditFinding` and `IsmsCorrectiveAction` mapped to PROV-O `Entity` and `Activity` concepts make ISMS audit trails consumable by any W3C PROV-aware tool - useful for regulatory submissions requiring machine-readable provenance chains.

**Dublin Core for document registry interoperability.** `IsmsDocumentControlMixin` slot mappings to `dc:title`, `dc:creator`, `dc:date`, and `dc:identifier` allow the ISMS document inventory to be harvested by enterprise content management systems and institutional repositories that speak Dublin Core, without a dedicated connector.

**Multi-framework GRC without duplication.** Because mappings live in the schema rather than in application code, adding alignment to a new framework (SOC 2 Trust Service Criteria, GDPR articles, NIS2 obligations) is a schema annotation change, not a new integration project. All downstream artefacts - JSON-LD, OWL, SHACL, SQL - inherit the alignment automatically on the next schema compilation.

## lmodel Ecosystem

The [lmodel](https://github.com/lmodel) organisation publishes a growing collection of LinkML schemas for cybersecurity, compliance, and linked data infrastructure. Because all lmodel schemas share the same LinkML type system and URI conventions, aligning iso27001 schema classes and slots with these schemas is a matter of adding `exact_mappings`, `close_mappings`, or `related_mappings` annotations.

The downstream artefacts - JSON-LD context, OWL axioms, SHACL shapes, SQL DDL - inherit every declared alignment automatically on the next schema compilation.

The [lmodel](https://github.com/lmodel/) schemas below are grouped by their primary relevance to the iso27001 schema use cases.

### Compliance and Control Frameworks

| Schema | Relevance |
|---|---|
| **oscal** | Open Security Controls Assessment Language (NIST). Highest-priority alignment target. `IsmsControl` ↔ OSCAL `control`; `IsmsStatementOfApplicability`/`IsmsApplicabilityEntry` ↔ OSCAL `system-security-plan` implemented-requirement; `IsmsAudit` ↔ OSCAL `assessment-results`; `IsmsCorrectiveAction` ↔ OSCAL `poam-item`. Organisations using OSCAL tooling (e.g. Trestle, OSCAL-CLI) can round-trip ISMS records without hand-written mappings. |
| **nist-sp-800-53** | NIST SP 800-53 Rev 5 control catalogue. `IsmsControl` instances can carry `close_mappings` or `narrow_mappings` to SP 800-53 control IDs, satisfying FedRAMP and DoD authorisation reporting alongside ISO 27001 Annex A. |
| **nist-csf-v2** | NIST Cybersecurity Framework v2. `IsmsControl` instances mapped to CSF subcategory URIs (e.g. `PR.AC-1`, `DE.CM-7`) let a single control record simultaneously address ISO 27001 and CSF reporting requirements. |
| **nist-sp-800-171** | Controlled Unclassified Information (CUI) protection requirements. Relevant for organisations in US defence supply chains; `IsmsControl` mappings cover the 110 CUI requirements. |
| **nist-sp-800-218** | Secure Software Development Framework (SSDF). Maps to `IsmsOperationalProcedure` and `IsmsControl` in DevSecOps pipelines; supports software supply chain assurance requirements in Annex A 8.25–8.31. |

### Threat Intelligence and Incident Response

| Schema | Relevance |
|---|---|
| **attack** | MITRE ATT&CK Enterprise and ICS matrices. `SecurityControl.applicable_threats` and `Risk.threat_description` accept `related_mappings` to ATT&CK technique URIs, connecting the ISMS risk register to the threat intelligence vocabulary. The ICS sub-matrix directly addresses the OT/ICS threat-modelling weakness identified in this schema. |
| **capec** | MITRE CAPEC attack pattern catalogue. Complements ATT&CK at the attack-pattern level; `related_mappings` on `IsmsRisk` instances link threat descriptions to structured attack patterns, enabling automated correlation with vulnerability scan findings. |
| **d3fend** | MITRE D3FEND defensive countermeasure knowledge graph. `close_mappings` from `IsmsControl` to D3FEND countermeasure URIs creates a machine-traversable chain: ATT&CK technique → D3FEND countermeasure → iso27001 `IsmsControl`. This enables automated gap analysis between observed threats and implemented controls. |
| **stix** | STIX 2.1 cyber threat intelligence objects. `IsmsSecurityIncident` mapped via `close_mappings` to STIX `Incident` allows incident records to be exported as STIX bundles for TAXII sharing, or enriched from incoming threat intelligence without field-by-field translation. |

### Unified Cyber Ontology

The UCO (Unified Cyber Ontology) family provides a modular foundational ontology used beneath CASE, STIX, and related standards. Several UCO modules map cleanly onto iso27001 classes.

| UCO Module | iso27001 alignment |
|---|---|
| **uco-core** | Base `UcoObject` identity and provenance attributes align with the slots every record has (`isms_id`, `title`, `description`). |
| **uco-observable** | Observable objects (network, file, process, device) align with `IsmsAsset` subtypes; `asset_category` enum values correspond to UCO observable class hierarchy. |
| **uco-action** | `Action` with `performer`, `result`, and `asset_location` aligns with `IsmsCorrectiveAction` and `IsmsOperationalProcedure.procedure_control_measures`. |
| **uco-analysis** | `Analysis` and `AnalyticResult` align with `IsmsRiskAssessment` and `IsmsAuditFinding`; supports interoperability with CASE-based forensic tooling. |
| **uco-identity** | `Identity` and `Organization` align with `IsmsOrganization` and `IsmsRole`; exact URI mappings enable federated identity queries across UCO-consuming tools. |
| **uco-location** | `Location` with geospatial properties aligns with `IsmsAsset.asset_location`; combining with GeoSPARQL enables spatial asset queries for OT zone modelling. |
| **uco-marking** | Data marking definitions align with `IsmsDocumentControlMixin.document_classification`; enables machine-readable sensitivity labels compatible with STIX Traffic Light Protocol. |
| **uco-tool** | `Tool` objects align with `IsmsAsset` subtype software-tooling references; relevant for evidence-of-control implementation. |
| **uco-vocabulary** | Controlled vocabularies underpin enum-to-URI alignment patterns shared by iso27001 enums (e.g. `IsmsImplementationStatus`). |

### Supply Chain and Software Integrity

These schemas directly address the supply chain risk scoring weakness identified in the Summary Assessment.

| Schema | Relevance |
|---|---|
| **slsa** | Supply-chain Levels for Software Artefacts (SLSA). Provides a structured vocabulary for build integrity levels (SLSA v1.0 Build track `L1`–`L3`). A proposed `IsmsSupplierAssessment` class extension (see Summary Assessment) can carry a `slsa_level` slot with `close_mappings` to SLSA provenance requirement URIs, satisfying Annex A 5.19–5.23 supplier relationship controls with machine-verifiable build provenance. |
| **spdx** | Software Package Data Exchange (SPDX). Software Bill of Materials (SBOM) format. `IsmsAsset` instances of type `software` can carry `related_mappings` to SPDX `Package` URIs, linking the ISMS asset inventory to the SBOM for automated vulnerability correlation (Annex A 8.8). |
| **nist-sp-800-218** | SSDF practices map onto software supplier assessment criteria; combined with SLSA levels provides a two-axis (practice maturity × build integrity) supplier scoring rubric. |

### Linked Data Infrastructure

| Schema | Relevance |
|---|---|
| **void** | Vocabulary of Interlinked Datasets. A VoID dataset descriptor for the iso27001 knowledge graph enables discoverability by linked data crawlers and SPARQL federation clients. Organisations publishing ISMS data as linked open data should include a VoID description referencing this schema's base URI (`https://w3id.org/lmodel/iso27001/`). |
| **geosparql** | OGC GeoSPARQL. `IsmsAsset.asset_location` can be expressed as GeoSPARQL `Feature` and `Geometry` objects, enabling spatial queries over asset inventories - particularly relevant for OT zone and physical perimeter modelling. |
| **datatype** | LinkML datatype library. Ensures consistent XSD-aligned type usage across the schema (dates, URIs, integers); reduces datatype impedance mismatches when round-tripping through JSON-Schema, SQL, and RDF serialisations. |
| **collections** | LinkML collections primitives. Supports typed list and set slots in generated Python, TypeScript, and SQL artefacts; underpins multi-valued slots such as `control_threats`, `control_evidence`, and `procedure_control_measures`. |

### Additional Schemas to Target

The following schemas remain high-value alignment targets that are not yet published as SSSOM mapping sets. The sets for `cwe`, `cve`/`nvd`, `ocsf`, `cis-controls` and `iso29100` were dropped until those schemas are released; the Implementation Status section says why.

| Schema | Rationale | Notes |
|---|---|---|
| **prov-o** | W3C PROV Ontology. `exact_mappings` from `IsmsAuditFinding` and `IsmsCorrectiveAction` to PROV-O `Entity` and `Activity` make ISMS audit trails consumable by any W3C PROV-aware tool. | Stable W3C URIs available; straightforward to publish. |
| **iec-62443** | IEC 62443 OT/ICS security standard. Zone-and-conduit model, security levels (SL-1–SL-4), and component requirement sets provide the OT vocabulary that ATT&CK for ICS alone does not cover. | No public canonical URI scheme; an lmodel placeholder namespace would be required. |
| **schema-org** | Schema.org. `Organization`, `Person`, and `Event` exact mappings improve discoverability of ISMS entities in general-purpose knowledge graphs. | Stable `https://schema.org/` URIs. |
| **dublin-core** | Dublin Core Metadata Initiative. `IsmsDocumentControlMixin` slot mappings to `dc:title`, `dc:creator`, `dc:date`, `dc:identifier`. | Stable DCMI URIs; small mapping set. |
| **iso31000** | ISO 31000 risk management vocabulary. `exact_mappings` from `IsmsRisk`, `IsmsRiskAssessment`, `IsmsRiskTreatmentPlan` to ISO 31000 terms. | ISO does not publish stable concept URIs; an lmodel placeholder namespace would be required. |
| **gdpr** | GDPR articles as linked data. `related_mappings` from `IsmsSecurityIncident.incident_notification_required` and `IsmsPolicy` to article URIs. | Several community URI schemes exist (e.g. ELI, DPV); choice affects portability. |
| **soc2** | AICPA SOC 2 Trust Service Criteria. `close_mappings` from `IsmsControl` and `IsmsAuditFinding` to TSC criterion URIs. | AICPA does not publish canonical URIs; lmodel placeholder namespace required. |

## Summary Assessment

The schema's primary differentiators over commercial GRC tools are LinkML-specific:

- **One source, many targets.** A single YAML compiles to Python dataclasses, Pydantic models, JSON-Schema, SHACL/ShEx, SQL DDL, JSON-LD context, OWL, GraphQL and Protobuf - keeping validators, application code, database schema, and RDF representation in lockstep.

- **First-class semantic mapping slots.** `exact_mappings`/`close_mappings`/`broad_mappings`/`narrow_mappings`/`related_mappings` carry external vocabulary alignments inside the schema itself, where they flow into every generated artefact rather than living in a separate translation layer.

- **Addressable enum values.** Permissible values (e.g. the 93 `IsmsAnnexAControl` controls) have their own URIs and can therefore be SSSOM subjects, JSON-LD nodes, and OWL named individuals without auxiliary classes.

- **Version-controlled, vendor-neutral artefact.** Compliance data becomes queryable in SPARQL/SQL/JSON-Schema validators rather than locked in a SaaS product.

**What this is not.** A LinkML schema does not provide a workflow engine, evidence-collection UI, ticketing integration, row-level access control, or change-data-capture audit log. Commercial GRC products differentiate on operational automation; this schema differentiates on the data substrate beneath that automation.

**Caveat on "annotation, not re-implementation".** The claim that cross-framework alignment is an annotation change holds only when the target framework publishes stable concept URIs. ISO standards, AICPA SOC 2 Trust Service Criteria, and (in part) IEC 62443 do not. For those, an lmodel placeholder namespace is required first, which is itself a small re-implementation step.

**Coverage gaps.** Structural-class gaps remain in operational technology (OT/ICS) and supplier assessment. The SSSOM mappings that once tied Annex A 5.19–5.23 and 8.25–8.34 to SLSA, NIST SSDF, SP 800-171, CVE/NVD and KEV were dropped, because their targets name no term of a released schema (see Implementation Status). The dedicated `IsmsOtAsset` and `IsmsSupplierAssessment` classes, and the slots that would let such mappings attach to first-class records, are not in the schema.

**Addressing the OT/ICS gap.** An `IsmsOtAsset` subclass of `IsmsAsset` carrying a `purdue_level` slot (enumeration `L0`–`L4` for field devices through enterprise network) and `related_mappings` to ATT&CK for ICS technique URIs and IEC 62443 security-level URIs would provide the domain-specific vocabulary that Annex A 7.x physical controls and Annex A 8.x technological controls require for OT environments. `IsmsAsset.asset_location` combined with GeoSPARQL geometries can then express OT zone and conduit topology in a spatially queryable form.

**Addressing the supplier-class gap.** An `IsmsSupplierAssessment` class and an `IsmsSupplierRisk` subclass of `IsmsRisk` would give Annex A 5.19–5.23 structured slots for supplier scoring: `slsa_level` (SLSA v1.0 Build track `L1`–`L3` build integrity), `ssdf_maturity` (NIST SP 800-218 practice maturity), `spdx_sbom_reference` (link to SPDX SBOM for each supplied software asset), and `supplier_criticality`. These additions would let SLSA, SSDF, SPDX, CVE and KEV mappings, once their targets are released, attach directly to supplier records, enabling automated re-assessment workflows when upstream CVEs or SLSA provenance violations are detected.

## Implementation Status

The cross-framework alignment described above is implemented as SSSOM/TSV mapping sets under [`src/iso27001/mappings/`](https://github.com/lmodel/iso27001/tree/main/src/iso27001/mappings), which `just gen-project` merges into the schema as `exact_mappings`, `close_mappings`, `broad_mappings`, `narrow_mappings` and `related_mappings`. A row stays only when both ends exist: its subject in this schema, and its object as a term of a released lmodel schema that `tests/neighbours/` holds, named by the IRI that release gives it. `tests/test_schema_rules.py` checks both, and that the files and the schema's mappings agree.

### Published (14 rows)

| Mapping set | Rows | Notes |
|---|---|---|
| `iso27001-to-oscal.sssom.tsv` | 11 | Class-level: the ISMS, a control, the Statement of Applicability and an included control, a risk treatment plan, a corrective action, an audit and an audit programme, a role, the organization and an asset, to lmodel/oscal v0.1.2. |
| `iso27001-to-nist-sp-800-53.sssom.tsv` | 1 | `IsmsControl` related to SP 800-53's control, in lmodel/nist-sp-800-53 v0.1.0. |
| `iso27001-to-spdx.sssom.tsv` | 2 | `IsmsOrganization` close to SPDX's organization and `IsmsAsset` related to SPDX's package, in lmodel/spdx v0.1.0. |

### Dropped until their targets are released

The mapping sets to ATT&CK, CAPEC, CIS Controls, CVE and NVD, CWE, D3FEND, ISO/IEC 29100, ISO/IEC 42001, the KEV catalog, OCSF and STIX were removed, because none of those lmodel schemas has a release yet. The sets to NIST CSF 2.0, SP 800-171, SP 800-218 and SLSA were removed too: their rows named terms that the released schemas do not hold, such as one IRI per control. So were the per-control rows of the OSCAL, SP 800-53 and SPDX sets. Each can come back once a release holds terms for it.

### Caveats and remaining work

- Mapping justification is `semapv:LLMBasedMatching`: each kept row was drafted by a language model and then checked against both classes' descriptions, with its predicate no stronger than the meaning supports. Rows should be reviewed by domain experts and promoted to `semapv:ManualMappingCuration`.
- The named gaps (`IsmsOtAsset` and `IsmsSupplierAssessment` classes, `purdue_level` and `slsa_level` slots, an IEC 62443 schema) are not addressed.
- The PROV-O, Dublin Core, schema.org, ISO 31000, GDPR, SOC 2, IEC 62443 and UCO mappings called out above are not published.

### Tooling, testing, and generated artefacts

- **SSSOM overlay tool.** [`scripts/apply_sssom_overlay.py`](https://github.com/lmodel/iso27001/blob/main/scripts/apply_sssom_overlay.py) merges the SSSOM rows into the schema. It is idempotent and uses `ruamel.yaml` round-trip mode to preserve comments and folded scalars.
- **Tests.** `just test` runs pytest over every valid example and counter-example, the upstream watch, the overlay and the schema rules, then the valid and invalid example pipeline and the third-party Probo examples.
- **Third-party validation corpus.** 61 `IsmsControl` examples under [`tests/data/third_party/probo/`](https://github.com/lmodel/iso27001/tree/main/tests/data/third_party/probo) are generated from the MIT-licensed [Probo](https://github.com/getprobo/probo) ISMS mitigation catalogue. The converter maps Probo's `ISO27001:2022-A.X.Y` references onto the `IsmsAnnexAControl` permissible values (`a_X_Y`) so every example validates against the schema's enum without manual editing.
- **Standard generator targets** (`just gen-project`): Pydantic / Python dataclasses, JSON Schema, ShEx, SHACL, OWL/TTL, GraphQL, Protobuf, JSON-LD context, SQLDDL, Java POJOs, TypeScript, Excel.
- **Extended generator targets** (`just gen-project-extended`): all standard targets plus `project/cpp/iso27001.h` (C++ header), `project/pandera/iso27001_pandera.py` (Pandera-on-Polars dataframe schema for tabular validation pipelines), `project/markdown-datadict/iso27001.md` (human-readable data dictionary), and `project/golr/` (GOLR Solr-index views). Each runs the stock LinkML generator, except the DBML one, whose wrapper `scripts/gen_dbml_patched.py` says why.
