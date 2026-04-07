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

The root `InformationSecurityManagementSystem` class aggregates every governance artifact - scope,policy, roles, objectives, and review records - into a single addressable entity. This enables an organisation to publish its ISMS structure as structured open data rather than collections of Word documents.

#### Policy Lifecycle Management

`InformationSecurityPolicy` and `TopicSpecificPolicy` carry approval dates, review dates, commitment statements, and audience assignments. A governance team can drive policy review workflows from structured YAML records rather than spreadsheet trackers, with automated alerts when `review_date`is approaching.

#### Roles, Responsibilities, and Accountability

`Role` with `responsibilities`, `authorities`, `accountability`, `assigned_to`, and `reporting_line` slots maps directly to Clause 5.3 requirements. It can power org-chart tooling, responsibility assignment matrices (RACI), and automated checks that every ISMS process has a named owner.


#### Management Review Evidence

`ManagementReview` captures all Clause 9.3 inputs (context changes, interested-party changes, performance trends, audit results, risk status) and outputs (decisions, action items). Structured records make it straightforward to extract management review packs automatically or generate evidence bundles for certification bodies.

#### Objectives Tracking

`InformationSecurityObjective` includes `target_value`, `current_value`, `metric_definition`, and `measurement_method`. A dashboard layer can query these records to produce live objective achievement status without manual reporting.


### Cybersecurity

#### Risk Register

`Risk`, `RiskAssessment`, and `RiskAssessmentProcess` implement the full Clause 6.1.2 workflow: criteria definition, threat/vulnerability pairing, CIA impact analysis, likelihood/impact scoring, and risk-level derivation. The `LikelihoodRating` and `ImpactRating` enumerations with `numeric_value` annotations make automated risk matrix computation straightforward.

#### Control Tracking Against Annex A

`SecurityControl` with the `ControlCategory` enum (organizational / people / physical / technological) and `ImplementationStatus` enum models all 93 Annex A controls. `implementation_status`, `effectiveness_rating`, `last_test_date`, and `evidence_references` slots enable a live control effectiveness dashboard without a dedicated GRC product.


#### Statement of Applicability Automation

`StatementOfApplicability` with `SoAEntry` records (including `inclusion_justification`, `exclusion_justification`, and `implementation_status`) can be generated directly from risk treatment decisions. Changes to the risk register can automatically propagate to the SoA, replacing the error-prone manual maintenance of spreadsheet-based SoAs.

#### Incident Response Traceability

`InformationSecurityEvent` -> `InformationSecurityIncident` with `containment_actions`, `eradication_actions`, `recovery_actions`, `lessons_learned`, and `evidence_collected` slots model the full incident lifecycle. `linked_incident` and `linked_corrective_action` references create a traceable chain from detection through to ISMS improvement.

#### Threat Intelligence Integration

`applicable_threats` on `SecurityControl` and `threat_description` / `vulnerability_description` on `Risk` provide structured attachment points for threat intelligence feeds. Because all entities have URI-based identifiers, external threat data (CVEs, STIX objects) can be linked in rather than embedded.

### DevSecOps

#### Schema-as-Code

LinkML compiles `iso27001.yaml` to Python dataclasses (`iso27001.py`), Pydantic models
(`iso27001_pydantic.py`), TypeScript types, and JSON-Schema. Application teams can import the generated dataclasses directly, making compliance data a typed first-class citizen in pipelines - not an afterthought.

#### CI/CD Compliance Gates

The generated JSON-Schema (`project/jsonschema/iso27001.schema.json`) can be applied as a validation step in a pipeline. Any ISMS artifact committed to a repository (control records, risk assessments, SoA entries) is validated against the schema before merge, enforcing data quality at the source.

#### Infrastructure-as-Code Alignment

`SecurityControl` records map Annex A controls to `applicable_assets` and `applicable_threats`. When a Terraform or Ansible change modifies a listed asset, tooling can automatically flag which controls and risks reference that asset, surfacing security review requirements without manual cross-referencing.

#### Automated Evidence Collection

`OperationalProcedure` with `procedure_steps` and `last_reviewed_date` alongside `CompetenceRecord` and `AwarenessProgram` (with `completion_tracking` and `effectiveness_measures`) give automation agents structured targets. Evidence-collection scripts can populate these records from ticketing
systems, LMS platforms, and SIEM logs.


#### SHACL/ShEx Validation of Linked Data Artifacts

`project/shacl/iso27001.shacl.ttl` can validate RDF-serialised compliance data in any graph-based pipeline. A DevSecOps team building a knowledge graph of assets, risks, and controls can enforce schema correctness using standard RDF tooling without writing custom validators.

### Regulatory Compliance

#### Multi-Framework Mapping

The `iso27001_clause` and `annex_a_control` annotations on every class are extension points. Annotations for ISO 27002 control guidance references, NIST CSF subcategory mappings, SOC 2 criteria, or NIS2 obligations can be added alongside the existing clause references. A single ISMS record can carry alignment metadata for multiple frameworks simultaneously.

#### Documented Information Inventory

`DocumentedInformation` (the base class for Policy, Procedure, Plan, Report, and Record classes) with `document_type`, `document_reference`, `approved_by`, `approval_date`, `effective_date`, `review_due_date`, and `classification` slots provides the full Clause 7.5 documented information control register. This is directly auditable by certification bodies.

#### Nonconformity and Corrective Action Audit Trail

`Nonconformity` -> `CorrectiveAction` with `root_cause`, `immediate_actions`,
`linked_corrective_actions`, `closure_date`, and `closure_evidence` implements the complete Clause 10.2 audit trail. Every step is structured and linkable, satisfying both internal audit and third-party certification evidence requirements.

#### Audit Programme Management

`AuditProgramme` and `InternalAudit` with `audit_criteria`, `audit_period_start/end`,
`lead_auditor`, `auditee_representatives`, `findings`, and `report_distribution` model the Clause 9.2.2 audit programme. Structured records support audit scheduling systems, finding trackers, and closure verification workflows.


#### NIS2 / DORA Readiness

`InformationSecurityIncident` with `notification_required` and `notifications_made` slots directly supports regulatory incident notification obligations (NIS2 Article 23, DORA Article 19). Structured incident records can feed a notification tracking system and produce regulator-ready evidence exports.

#### Export to SQL / Relational GRC

`project/sqlschema/iso27001.sql` provides a relational schema for loading ISMS data into any SQL database. Organisations with existing GRC databases can import or synchronise records without building a bespoke data model.

### Integration

#### Linked Data and Knowledge Graph

All entity identifiers are URIs under `https://w3id.org/lmodel/iso-iec-27001/`.
`project/jsonld/iso27001.jsonld` and `project/owl/iso27001.owl.ttl` enable ISMS data to participate in enterprise knowledge graphs alongside asset inventories, identity systems, and vulnerability databases - with SPARQL as the query layer.

#### GRC Platform Data Exchange

`project/jsonschema/iso27001.schema.json` is the interchange format for GRC platform APIs. Any GRC product that accepts JSON-Schema-validated payloads (ServiceNow GRC, Archer, OneTrust, Vanta) can ingest or export ISMS records through this schema without proprietary data mapping.

#### SIEM and SOAR Enrichment

`InformationSecurityEvent` and `InformationSecurityIncident` records referenced by URI can be enriched from SIEM alert payloads. A SOAR playbook can populate `detection_method`, `affected_assets`, `containment_actions`, and `evidence_collected` slots automatically when an alert fires, creating structured incident records without analyst data entry.

#### Asset Management System Integration

`Asset` with `asset_type`, `asset_owner`, `asset_custodian`, `classification`, `location`, and `criticality` links to risk and control records by URI. This is the bridge between CMDB/asset inventory tools (ServiceNow CMDB, Snipe-IT) and the ISMS risk register - changes in the asset inventory can trigger automatic risk reassessment workflows.


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
| `exact_mappings` | Concepts are fully equivalent | `Organization` -> `schema:Organization`; `DocumentedInformation` slots -> Dublin Core `dc:title`, `dc:date` |
| `close_mappings` | Closely related but not identical | `CorrectiveAction` -> ISO 9001 corrective action; `Nonconformity` -> COBIT process deviation |
| `broad_mappings` | External concept is broader | `InformationSecurityObjective` -> COBIT governance objective category |
| `narrow_mappings` | External concept is narrower | `SecurityControl` -> a specific CIS Control sub-control or NIST SP 800-53 control enhancement |
| `related_mappings` | Loosely associated | `AuditFinding` -> PROV-O `Activity`; `applicable_threats` values -> MITRE ATT&CK technique IDs |

**NIST Cybersecurity Framework alignment.** Adding `exact_mappings` or `close_mappings` from `SecurityControl` instances to NIST CSF subcategory URIs (e.g., `PR.AC-1`, `DE.CM-7`) allows a single control record to simultaneously satisfy ISO 27001 Annex A and CSF reporting requirements. Tools that consume the JSON-LD output resolve both identifiers without any additional mapping layer.

**MITRE ATT&CK threat linkage.** The `applicable_threats` slot on `SecurityControl` and
`threat_description` on `Risk` can carry `related_mappings` to ATT&CK technique or tactic URIs. This connects the ISMS risk register directly to the threat intelligence vocabulary, enabling automated correlation between SIEM detections (tagged with ATT&CK IDs) and the controls designed to address them.

**STIX/TAXII incident interoperability.** `InformationSecurityIncident` mapped via `close_mappings` to the STIX 2.1 `Incident` object type lets incident records be exported as STIX bundles for sharing via TAXII feeds, or enriched from incoming threat intelligence without field-by-field translation.

**Provenance and audit trail via PROV-O.** `AuditFinding` and `CorrectiveAction` mapped to PROV-O `Entity` and `Activity` concepts make ISMS audit trails consumable by any W3C PROV-aware tool - useful for regulatory submissions requiring machine-readable provenance chains.

**Dublin Core for document registry interoperability.** `DocumentedInformation` slot mappings to `dc:title`, `dc:creator`, `dc:date`, and `dc:identifier` allow the ISMS document inventory to be harvested by enterprise content management systems and institutional repositories that speak Dublin Core, without a dedicated connector.

**Multi-framework GRC without duplication.** Because mappings live in the schema rather than in application code, adding alignment to a new framework (SOC 2 Trust Service Criteria, GDPR articles, NIS2 obligations) is a schema annotation change, not a new integration project. All downstream artefacts - JSON-LD, OWL, SHACL, SQL - inherit the alignment automatically on the next schema compilation.

## lmodel Ecosystem

The [lmodel](https://github.com/lmodel) organisation publishes a growing collection of LinkML schemas for cybersecurity, compliance, and linked data infrastructure. Because all lmodel schemas share the same LinkML type system and URI conventions, aligning iso27001 schema classes and slots with these schemas is a matter of adding `exact_mappings`, `close_mappings`, or `related_mappings` annotations.

The downstream artefacts - JSON-LD context, OWL axioms, SHACL shapes, SQL DDL - inherit every declared alignment automatically on the next schema compilation.

The [lmodel](https://github.com/lmodel/) schemas below are grouped by their primary relevance to the iso27001 schema use cases.

### Compliance and Control Frameworks

| Schema | Relevance |
|---|---|
| **oscal** | Open Security Controls Assessment Language (NIST). Highest-priority alignment target. `SecurityControl` ↔ OSCAL `control`; `StatementOfApplicability`/`SoAEntry` ↔ OSCAL `system-security-plan` implemented-requirement; `InternalAudit` ↔ OSCAL `assessment-results`; `CorrectiveAction` ↔ OSCAL `poam-item`. Organisations using OSCAL tooling (e.g. Trestle, OSCAL-CLI) can round-trip ISMS records without hand-written mappings. |
| **nist-sp-800-53** | NIST SP 800-53 Rev 5 control catalogue. `SecurityControl` instances can carry `close_mappings` or `narrow_mappings` to SP 800-53 control IDs, satisfying FedRAMP and DoD authorisation reporting alongside ISO 27001 Annex A. |
| **nist-csf-v2** | NIST Cybersecurity Framework v2. `SecurityControl` instances mapped to CSF subcategory URIs (e.g. `PR.AC-1`, `DE.CM-7`) let a single control record simultaneously address ISO 27001 and CSF reporting requirements. |
| **nist-sp-800-171** | Controlled Unclassified Information (CUI) protection requirements. Relevant for organisations in US defence supply chains; `SecurityControl` mappings cover the 110 CUI requirements. |
| **nist-sp-800-218** | Secure Software Development Framework (SSDF). Maps to `OperationalProcedure` and `SecurityControl` in DevSecOps pipelines; supports software supply chain assurance requirements in Annex A 8.25–8.31. |


### Threat Intelligence and Incident Response

| Schema | Relevance |
|---|---|
| **attack** | MITRE ATT&CK Enterprise and ICS matrices. `SecurityControl.applicable_threats` and `Risk.threat_description` accept `related_mappings` to ATT&CK technique URIs, connecting the ISMS risk register to the threat intelligence vocabulary. The ICS sub-matrix directly addresses the OT/ICS threat-modelling weakness identified in this schema. |
| **capec** | MITRE CAPEC attack pattern catalogue. Complements ATT&CK at the attack-pattern level; `related_mappings` on `Risk` instances link threat descriptions to structured attack patterns, enabling automated correlation with vulnerability scan findings. |
| **d3fend** | MITRE D3FEND defensive countermeasure knowledge graph. `close_mappings` from `SecurityControl` to D3FEND countermeasure URIs creates a machine-traversable chain: ATT&CK technique → D3FEND countermeasure → iso27001 `SecurityControl`. This enables automated gap analysis between observed threats and implemented controls. |
| **stix** | STIX 2.1 cyber threat intelligence objects. `InformationSecurityIncident` mapped via `close_mappings` to STIX `Incident` allows incident records to be exported as STIX bundles for TAXII sharing, or enriched from incoming threat intelligence without field-by-field translation. |


### Unified Cyber Ontology

The UCO (Unified Cyber Ontology) family provides a modular foundational ontology used beneath CASE, STIX, and related standards. Several UCO modules map cleanly onto iso27001 classes.

| UCO Module | iso27001 alignment |
|---|---|
| **uco-core** | Base `UcoObject` identity and provenance attributes align with `DocumentedInformation` common slots (`id`, `name`, `description`, `created`). |
| **uco-observable** | Observable objects (network, file, process, device) align with `Asset` subtypes; `asset_type` enum values correspond to UCO observable class hierarchy. |
| **uco-action** | `Action` with `performer`, `result`, and `location` aligns with `CorrectiveAction` and `OperationalProcedure.procedure_steps`. |
| **uco-analysis** | `Analysis` and `AnalyticResult` align with `RiskAssessment` and `AuditFinding`; supports interoperability with CASE-based forensic tooling. |
| **uco-identity** | `Identity` and `Organization` align with ISMS `Organization` and `Role`; exact URI mappings enable federated identity queries across UCO-consuming tools. |
| **uco-role** | `Role` concept aligns with iso27001 `Role`; `responsibilities` and `authorities` slot semantics match. |
| **uco-location** | `Location` with geospatial properties aligns with `Asset.location`; combining with GeoSPARQL enables spatial asset queries for OT zone modelling. |
| **uco-victim** | `Victim` concept aligns with `affected_assets` and incident impact scope; relevant for regulatory incident notification evidence. |
| **uco-marking** | Data marking definitions align with `DocumentedInformation.classification`; enables machine-readable sensitivity labels compatible with STIX Traffic Light Protocol. |
| **uco-configuration** | `Configuration` objects align with OT/ICS asset configuration records; relevant for Annex A 8.8 (management of technical vulnerabilities) in OT environments. |
| **uco-pattern** | `Pattern` concept aligns with monitoring criteria in `SecurityControl`; supports detection rule linkage for SIEM and SOAR enrichment. |


### Supply Chain and Software Integrity

These schemas directly address the supply chain risk scoring weakness identified in the Summary Assessment.

| Schema | Relevance |
|---|---|
| **slsa** | Supply-chain Levels for Software Artefacts (SLSA). Provides a structured vocabulary for build integrity levels (`SLSA_L0`–`SLSA_L3`). A proposed `SupplierAssessment` class extension (see Summary Assessment) can carry a `slsa_level` slot with `close_mappings` to SLSA provenance requirement URIs, satisfying Annex A 5.19–5.22 supplier relationship controls with machine-verifiable build provenance. |
| **spdx** | Software Package Data Exchange (SPDX). Software Bill of Materials (SBOM) format. `Asset` instances of type `software` can carry `related_mappings` to SPDX `Package` URIs, linking the ISMS asset inventory to the SBOM for automated vulnerability correlation (Annex A 8.8). |
| **nist-sp-800-218** | SSDF practices map onto software supplier assessment criteria; combined with SLSA levels provides a two-axis (practice maturity × build integrity) supplier scoring rubric. |


### Linked Data Infrastructure

| Schema | Relevance |
|---|---|
| **void** | Vocabulary of Interlinked Datasets. A VoID dataset descriptor for the iso27001 knowledge graph enables discoverability by linked data crawlers and SPARQL federation clients. Organisations publishing ISMS data as linked open data should include a VoID description referencing this schema's base URI (`https://w3id.org/lmodel/iso-iec-27001/`). |
| **geosparql** | OGC GeoSPARQL. `Asset.location` can be expressed as GeoSPARQL `Feature` and `Geometry` objects, enabling spatial queries over asset inventories - particularly relevant for OT zone and physical perimeter modelling. |
| **datatype** | LinkML datatype library. Ensures consistent XSD-aligned type usage across the schema (dates, URIs, integers); reduces datatype impedance mismatches when round-tripping through JSON-Schema, SQL, and RDF serialisations. |
| **collections** | LinkML collections primitives. Supports typed list and set slots in generated Python, TypeScript, and SQL artefacts; underpins multi-valued slots such as `applicable_threats`, `evidence_references`, and `procedure_steps`. |


### Additional Schemas to Target

The following schemas are not yet in the lmodel catalogue but represent high-value alignment targets for the use cases and weaknesses identified in this document.

| Schema | Rationale |
|---|---|
| **cwe** | MITRE Common Weakness Enumeration. `close_mappings` on `Risk.vulnerability_description` to CWE IDs links ISMS vulnerabilities to the structured weakness taxonomy, enabling automated correlation with static analysis tool output. |
| **cve / nvd** | CVE / NIST NVD vulnerability records. `related_mappings` on `Risk` and `Asset` instances to CVE URIs creates a live bridge between the ISMS risk register and the vulnerability database for automated risk re-scoring when new CVEs are published. |
| **ocsf** | Open Cybersecurity Schema Framework. A vendor-neutral event schema used by AWS Security Hub, Splunk, and others. Mapping `InformationSecurityEvent` slots to OCSF event classes enables zero-translation ingestion of SIEM alerts into ISMS incident records. |
| **prov-o** | W3C PROV Ontology. `exact_mappings` from `AuditFinding` and `CorrectiveAction` to PROV-O `Entity` and `Activity` make ISMS audit trails consumable by any W3C PROV-aware tool - useful for regulatory submissions requiring machine-readable provenance chains. |
| **iec-62443** | IEC 62443 OT/ICS security standard. Zone and conduit model, security levels (SL-1–SL-4), and component requirement sets provide the domain-specific vocabulary needed for OT asset subclasses and threat modelling beyond what ATT&CK for ICS covers alone. |
| **schema-org** | Schema.org. `Organization`, `Person`, and `Event` exact mappings improve discoverability of ISMS entities in general-purpose knowledge graphs and search engine structured data. |
| **dublin-core** | Dublin Core Metadata Initiative. `DocumentedInformation` slot mappings to `dc:title`, `dc:creator`, `dc:date`, and `dc:identifier` allow the ISMS document inventory to be harvested by enterprise content management systems and institutional repositories. |
| **iso31000** | ISO 31000 risk management vocabulary. `exact_mappings` or `close_mappings` from `Risk`, `RiskAssessment`, and `RiskTreatmentPlan` to ISO 31000 terms ensures interoperability with enterprise-wide risk frameworks that are not information-security-specific. |
| **gdpr** | General Data Protection Regulation articles as linked data. `related_mappings` from `InformationSecurityIncident.notification_required` and `InformationSecurityPolicy` to GDPR article URIs surfaces ISMS–GDPR overlaps in the JSON-LD output without a separate compliance mapping exercise. |
| **cis-controls-v8** | CIS Controls v8 safeguards. `close_mappings` from `SecurityControl` to CIS safeguard URIs provides a third control framework axis alongside NIST SP 800-53 and CSF, relevant for organisations using the CIS benchmarks as implementation guidance. |
| **soc2** | AICPA SOC 2 Trust Service Criteria. `close_mappings` from `SecurityControl` and `AuditFinding` to TSC criterion URIs satisfies SOC 2 reporting alongside ISO 27001 certification from the same structured ISMS records. |


## Summary Assessment

The schema's primary differentiator over commercial GRC tools is that it externalises the data model as a vendor-neutral, open, version-controlled artifact. This means:

  - **Compliance data becomes queryable** (SPARQL, SQL, JSON-Schema validators) rather than locked in a SaaS product.
  - **Evidence is machine-verifiable** at the CI/CD layer, not just auditor-visible.
  - **Cross-framework alignment** is an annotation problem, not a re-implementation.
  - **Integration is schema-first** - any system that speaks JSON, RDF, or SQL can participate without proprietary connectors.

The weakest current coverage is operational technology (OT/ICS) asset types and supply chain risk scoring - areas where Annex A 5.19–5.22 are represented structurally but without domain-specific slots for OT-specific threat modelling or supplier scoring rubrics.

**Addressing the OT/ICS gap.** An `OTAsset` subclass of `Asset` carrying a `purdue_level` slot (enumeration `L0`–`L4` for field devices through enterprise network) and `related_mappings` to ATT&CK for ICS technique URIs and IEC 62443 security-level URIs would provide the domain-specific vocabulary that Annex A 7.x physical controls and Annex A 8.x technological controls require for OT environments. `Asset.location` combined with GeoSPARQL geometries can then express OT zone and conduit topology in a spatially queryable form.

**Addressing the supply chain gap.** A `SupplierAssessment` class and a `SupplierRisk` subclass of `Risk` would give Annex A 5.19–5.22 structured slots for supplier scoring: `slsa_level` (SLSA `L0`–`L3` build integrity), `ssdf_maturity` (NIST SP 800-218 practice maturity), `spdx_sbom_reference` (link to SPDX SBOM for each supplied software asset), and `supplier_criticality`. These additions transform the current structural coverage of supply chain controls into machine-verifiable supplier risk records that can feed automated re-assessment workflows when upstream CVEs or SLSA provenance violations are detected.
