export type NamedEntityId = string;
export type DocumentedInformationId = string;
export type InformationSecurityManagementSystemId = string;
export type OrganizationId = string;
export type InterestedPartyId = string;
export type InformationSecurityPolicyId = string;
export type TopicSpecificPolicyId = string;
export type RoleId = string;
export type InformationSecurityObjectiveId = string;
export type RiskAssessmentProcessId = string;
export type RiskAssessmentId = string;
export type RiskId = string;
export type RiskTreatmentProcessId = string;
export type RiskTreatmentPlanId = string;
export type StatementOfApplicabilityId = string;
export type SecurityControlId = string;
export type ResourceId = string;
export type CompetenceRecordId = string;
export type AwarenessProgramId = string;
export type CommunicationPlanId = string;
export type OperationalProcedureId = string;
export type MonitoringProgramId = string;
export type InternalAuditId = string;
export type AuditProgrammeId = string;
export type AuditFindingId = string;
export type ManagementReviewId = string;
export type NonconformityId = string;
export type CorrectiveActionId = string;
export type ImprovementOpportunityId = string;
export type AssetId = string;
export type InformationSecurityEventId = string;
export type InformationSecurityIncidentId = string;
/**
* The four control domains defined in ISO/IEC 27001:2022 Annex A, corresponding to Clauses 5-8 of ISO/IEC 27002:2022.
*/
export enum ControlCategory {
    
    /** Organizational controls (Annex A.5) — policies, roles, asset management, access control, supplier relationships, incident management, compliance. */
    organizational = "organizational",
    /** People controls (Annex A.6) — screening, employment terms, awareness, disciplinary process, termination responsibilities, remote working. */
    people = "people",
    /** Physical controls (Annex A.7) — perimeters, entry controls, equipment protection, secure areas, media handling, cabling, maintenance. */
    physical = "physical",
    /** Technological controls (Annex A.8) — endpoint security, access restrictions, authentication, malware protection, logging, cryptography, secure development. */
    technological = "technological",
};
/**
* Lifecycle status of a security control, used in Statement of Applicability and control tracking.
*/
export enum ImplementationStatus {
    
    /** Control identified but no implementation activities begun. */
    not_started = "not_started",
    /** Control scheduled for implementation with defined timeline. */
    planned = "planned",
    /** Implementation actively underway but not yet complete. */
    in_progress = "in_progress",
    /** Control fully implemented and operational. */
    implemented = "implemented",
    /** Control excluded from scope with documented justification per 6.1.3 d). */
    not_applicable = "not_applicable",
};
/**
* Standard risk treatment options per ISO 31000 and ISO 27005.
*/
export enum RiskTreatmentOption {
    
    /** Apply controls to change the risk level (reduce likelihood or impact). */
    modify = "modify",
    /** Accept the risk without further treatment, within risk appetite. Requires risk owner approval. */
    accept = "accept",
    /** Eliminate the risk by removing the activity or asset that creates it. */
    avoid = "avoid",
    /** Transfer or share risk with external parties (e.g., insurance, outsourcing). */
    share = "share",
};
/**
* Qualitative risk rating derived from likelihood × impact analysis.
*/
export enum RiskLevel {
    
    /** Negligible risk requiring no immediate action. */
    very_low = "very_low",
    /** Minor risk manageable through routine procedures. */
    low = "low",
    /** Moderate risk requiring management attention and planned controls. */
    medium = "medium",
    /** Significant risk requiring priority treatment and escalation. */
    high = "high",
    /** Severe risk threatening organizational objectives; requires immediate executive action and resource allocation. */
    critical = "critical",
};
/**
* Categories of documented information required or recommended by ISO 27001.
*/
export enum DocumentType {
    
    /** High-level statement of intent and direction (e.g., IS policy per 5.2). */
    policy = "policy",
    /** Documented steps for performing activities consistently. */
    procedure = "procedure",
    /** Mandatory requirements for specific technologies or processes. */
    standard = "standard",
    /** Recommended practices that support policies and procedures. */
    guideline = "guideline",
    /** Evidence of activities performed or results achieved. */
    record = "record",
    /** Documented approach for achieving objectives (e.g., risk treatment plan). */
    plan = "plan",
    /** Formal output of assessment, audit, or review activities. */
    report = "report",
};
/**
* Classification of internal audit findings.
*/
export enum AuditFindingType {
    
    /** Significant failure to fulfill a requirement that affects ISMS capability to achieve intended outcomes. */
    major_nonconformity = "major_nonconformity",
    /** Isolated lapse that does not significantly affect ISMS effectiveness. */
    minor_nonconformity = "minor_nonconformity",
    /** Noted condition that could lead to nonconformity if not addressed. */
    observation = "observation",
    /** Evidence of effective implementation exceeding requirements. */
    positive_finding = "positive_finding",
};
/**
* Qualitative likelihood scale for risk assessment.
*/
export enum LikelihoodRating {
    
    /** Highly unlikely to occur (< 5% probability). */
    rare = "rare",
    /** Not expected but possible (5-20% probability). */
    unlikely = "unlikely",
    /** May occur at some point (20-50% probability). */
    possible = "possible",
    /** Probably will occur (50-80% probability). */
    likely = "likely",
    /** Expected to occur in most circumstances (> 80% probability). */
    almost_certain = "almost_certain",
};
/**
* Qualitative impact scale for risk assessment.
*/
export enum ImpactRating {
    
    /** No significant impact on operations or objectives. */
    negligible = "negligible",
    /** Limited impact, easily absorbed by normal operations. */
    minor = "minor",
    /** Noticeable impact requiring management intervention. */
    moderate = "moderate",
    /** Serious impact on objectives, reputation, or compliance. */
    major = "major",
    /** Catastrophic impact threatening organizational viability. */
    severe = "severe",
};


/**
 * Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
 */
export interface NamedEntity {
    /** Unique identifier for this entity instance. */
    id: string,
    /** Human-readable name or title. */
    name: string,
    /** Detailed description of the entity. */
    description?: string,
    /** Date when the entity was created. */
    created_date?: date,
    /** Date when the entity was last modified. */
    modified_date?: date,
    /** Version identifier for the entity. */
    version?: string,
}


/**
 * Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
 */
export interface DocumentedInformation extends NamedEntity {
    /** Classification of the documented information. */
    document_type?: string,
    /** Unique reference number for document control. */
    document_reference?: string,
    /** Person who created the document. */
    author?: string,
    /** Person accountable for the document content and maintenance. */
    owner?: string,
    /** Person who approved the document. */
    approved_by?: string,
    /** Date when the document was approved. */
    approved_date?: date,
    /** Date when the document becomes effective. */
    effective_date?: date,
    /** Date when the document is due for review. */
    review_date?: date,
    /** Current status of the document or entity. */
    status?: string,
    /** Information classification level. */
    classification?: string,
    /** Duration for which the document must be retained. */
    retention_period?: string,
}


/**
 * Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required for establishing, implementing, maintaining, and continually improving information security management.
 */
export interface InformationSecurityManagementSystem extends NamedEntity {
    /** Reference to the organization operating the ISMS. */
    organization?: OrganizationId,
    /** Documented statement of ISMS scope per 4.3. */
    scope_statement?: string,
    /** Defined boundaries of the ISMS scope. */
    scope_boundaries?: string[],
    /** Any exclusions from scope with justification. */
    scope_exclusions?: string[],
    /** Internal issues relevant to ISMS per 4.1. */
    context_internal_issues?: string[],
    /** External issues relevant to ISMS per 4.1. */
    context_external_issues?: string[],
    /** Stakeholders relevant to the ISMS. */
    interested_parties?: InterestedPartyId[],
    /** Reference to the information security policy. */
    information_security_policy?: InformationSecurityPolicyId,
    /** Information security objectives. */
    objectives?: InformationSecurityObjectiveId[],
    /** Reference to the risk assessment process. */
    risk_assessment_process?: RiskAssessmentProcessId,
    /** Reference to the risk treatment process. */
    risk_treatment_process?: RiskTreatmentProcessId,
    /** Reference to the Statement of Applicability. */
    statement_of_applicability?: StatementOfApplicabilityId,
    /** Security controls applied in the ISMS. */
    controls?: SecurityControlId[],
    /** Information security roles defined in the ISMS. */
    roles?: RoleId[],
    /** Resources provided for the ISMS. */
    resources?: ResourceId[],
    /** Competence records for personnel. */
    competence_records?: CompetenceRecordId[],
    /** Reference to the awareness program. */
    awareness_program?: AwarenessProgramId,
    /** Reference to the communication plan. */
    communication_plan?: CommunicationPlanId,
    /** Register of documented information. */
    documented_information_register?: DocumentedInformationId[],
    /** Operational procedures. */
    operational_procedures?: OperationalProcedureId[],
    /** Risk assessment instances. */
    risk_assessments?: RiskAssessmentId[],
    /** Risk treatment plans. */
    risk_treatment_plans?: RiskTreatmentPlanId[],
    /** Reference to the monitoring program. */
    monitoring_program?: MonitoringProgramId,
    /** Internal audit instances. */
    internal_audits?: InternalAuditId[],
    /** Management review instances. */
    management_reviews?: ManagementReviewId[],
    /** Nonconformities identified. */
    nonconformities?: NonconformityId[],
    /** Corrective actions. */
    corrective_actions?: CorrectiveActionId[],
    /** Improvement opportunities tracked. */
    improvements?: ImprovementOpportunityId[],
    /** Current certification status. */
    certification_status?: string,
    /** Accredited certification body. */
    certification_body?: string,
    /** Date certification was achieved. */
    certification_date?: date,
    /** Date recertification is due. */
    recertification_date?: date,
}


/**
 * The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
 */
export interface Organization extends NamedEntity {
    /** Legal registered name of the organization. */
    legal_name?: string,
    /** Names under which the organization conducts business. */
    trading_names?: string[],
    /** Type of organization (e.g., corporation, government, nonprofit). */
    organization_type?: string,
    /** Primary industry sector of the organization. */
    industry_sector?: string,
    /** Organization size classification. */
    size_category?: string,
    /** Approximate number of employees. */
    employee_count?: number,
    /** Countries or regions where the organization operates. */
    geographic_locations?: string[],
    /** Jurisdictions whose regulations apply to the organization. */
    regulatory_jurisdictions?: string[],
    /** Parent organization if applicable. */
    parent_organization?: string,
    /** Subsidiary organizations if applicable. */
    subsidiaries?: string[],
}


/**
 * A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
 */
export interface InterestedParty extends NamedEntity {
    /** Category of interested party. */
    party_type?: string,
    /** Nature of the relationship with the organization. */
    relationship?: string,
    /** Requirements of the interested party. */
    requirements?: string[],
    /** Communication requirements for this party. */
    communication_needs?: string,
    /** Contact details for the party. */
    contact_information?: string,
}


/**
 * The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
 */
export interface InformationSecurityPolicy extends DocumentedInformation {
    /** The core policy statement text. */
    policy_statement?: string,
    /** Framework for setting information security objectives. */
    policy_objectives_framework?: string,
    /** Statements of commitment included in the policy. */
    commitment_statements?: string[],
    /** Statement of policy applicability. */
    applicability_statement?: string,
    /** Date when the policy was communicated. */
    communication_date?: date,
    /** Whether acknowledgment is required from personnel. */
    acknowledgment_required?: boolean,
    /** Topic-specific policies supporting this policy. */
    related_topic_policies?: TopicSpecificPolicyId[],
}


/**
 * A policy addressing a specific information security topic, supporting the overarching information security policy.
 */
export interface TopicSpecificPolicy extends DocumentedInformation {
    /** The specific topic addressed by the policy. */
    topic_area?: string,
    /** The parent policy this topic-specific policy supports. */
    parent_policy?: InformationSecurityPolicyId,
    /** Controls related to this policy. */
    applicable_controls?: SecurityControlId[],
    /** Intended audience for the policy or document. */
    target_audience?: string,
}


/**
 * An information security role with defined responsibilities and authorities per Clause 5.3.
 */
export interface Role extends NamedEntity {
    /** Category of the role. */
    role_type?: string,
    /** Responsibilities assigned to the role. */
    responsibilities?: string[],
    /** Authorities granted to the role. */
    authorities?: string[],
    /** What the role is accountable for. */
    accountability?: string,
    /** Person(s) assigned to this role. */
    assigned_to?: string[],
    /** Rules for delegating responsibilities. */
    delegation_rules?: string,
    /** To whom this role reports. */
    reporting_line?: string,
}


/**
 * A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
 */
export interface InformationSecurityObjective extends NamedEntity {
    /** Clear statement of the objective. */
    objective_statement?: string,
    /** Target value for the objective metric. */
    target_value?: string,
    /** Current measured value. */
    current_value?: string,
    /** Definition of how the objective is measured. */
    metric_definition?: string,
    /** Method used to measure the metric. */
    measurement_method?: string,
    /** How often measurement is performed. */
    measurement_frequency?: string,
    /** Role responsible for the objective or control. */
    responsible_role?: RoleId,
    /** Target date for achieving the objective. */
    target_date?: date,
    /** Current status of objective achievement. */
    achievement_status?: string,
    /** Associated risks. */
    related_risks?: RiskId[],
    /** Other controls related to this one. */
    related_controls?: SecurityControlId[],
    /** Plan for achieving the objective. */
    action_plan?: string,
}


/**
 * The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
 */
export interface RiskAssessmentProcess extends DocumentedInformation {
    /** Criteria for accepting risks. */
    risk_acceptance_criteria?: string,
    /** Criteria for performing risk assessments. */
    assessment_criteria?: string,
    /** Methodology used for risk assessment. */
    assessment_methodology?: string,
    /** Scale used for likelihood rating. */
    likelihood_scale?: string,
    /** Scale used for impact rating. */
    impact_scale?: string,
    /** Risk matrix or calculation method. */
    risk_matrix?: string,
    /** Planned frequency of risk assessments. */
    assessment_frequency?: string,
    /** Events that trigger risk assessment outside planned schedule. */
    trigger_events?: string[],
}


/**
 * An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
 */
export interface RiskAssessment extends DocumentedInformation {
    /** Scope of the assessment. */
    assessment_scope?: string,
    /** Date the assessment was conducted. */
    assessment_date?: date,
    /** Person or team who conducted the assessment. */
    assessor?: string,
    /** Specific methodology applied in this assessment. */
    methodology_used?: string,
    /** Risks identified in this assessment. */
    risks_identified?: RiskId[],
    /** Summary of assessment findings. */
    summary_findings?: string,
    /** Recommendations from the assessment. */
    recommendations?: string[],
    /** Planned date for next assessment. */
    next_assessment_date?: date,
}


/**
 * An identified information security risk associated with loss of confidentiality, integrity, or availability per 6.1.2 c).
 */
export interface Risk extends NamedEntity {
    /** Source or origin of the risk. */
    risk_source?: string,
    /** Description of the threat exploiting the vulnerability. */
    threat_description?: string,
    /** Description of the vulnerability that could be exploited. */
    vulnerability_description?: string,
    /** Assets affected by this risk or incident. */
    affected_assets?: AssetId[],
    /** Which CIA properties are affected (confidentiality, integrity, availability). */
    affected_cia_properties?: string[],
    /** Person accountable for managing the risk. */
    risk_owner?: string,
    /** Assessed likelihood of risk occurrence. */
    likelihood?: string,
    /** Assessed impact if risk materializes. */
    impact?: string,
    /** Risk level before controls are applied. */
    inherent_risk_level?: string,
    /** Controls currently in place affecting this risk. */
    existing_controls?: SecurityControlId[],
    /** Risk level after controls are applied. */
    residual_risk_level?: string,
    /** Selected treatment option for the risk. */
    risk_treatment_option?: string,
    /** Priority for treating this risk. */
    treatment_priority?: string,
    /** Risk treatment plan addressing this risk. */
    related_treatment_plan?: RiskTreatmentPlanId,
}


/**
 * The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
 */
export interface RiskTreatmentProcess extends DocumentedInformation {
    /** Guidance on selecting treatment options. */
    treatment_options_guidance?: string,
    /** Criteria for selecting controls. */
    control_selection_criteria?: string,
    /** Template used for Statement of Applicability. */
    soa_template?: string,
    /** Workflow for approving risk treatment. */
    approval_workflow?: string,
}


/**
 * A risk treatment plan per 6.1.3 e), documenting actions to implement selected treatment options and controls.
 */
export interface RiskTreatmentPlan extends DocumentedInformation {
    /** Scope of the plan. */
    plan_scope?: string,
    /** Risks addressed by this plan. */
    risks_addressed?: RiskId[],
    /** Actions to be taken for treatment. */
    treatment_actions?: string[],
    /** Controls to be implemented as part of treatment. */
    controls_to_implement?: SecurityControlId[],
    /** Resources required for implementation. */
    resources_required?: string,
    /** Parties responsible for implementation. */
    responsible_parties?: string[],
    /** Timeline for implementation. */
    implementation_timeline?: string,
    /** Risk owner who approved the plan. */
    risk_owner_approval?: string,
    /** Date when the risk treatment plan was approved. */
    approved_date?: date,
    /** Documentation of residual risk acceptance. */
    residual_risk_acceptance?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Date when implementation was completed. */
    completion_date?: date,
}


/**
 * The Statement of Applicability (SoA) per 6.1.3 d), listing necessary controls with justification and implementation status.
 */
export interface StatementOfApplicability extends DocumentedInformation {
    /** Individual control entries in the SoA. */
    soa_entries?: SoAEntry[],
    /** Total number of controls in scope. */
    total_controls?: number,
    /** Number of implemented controls. */
    implemented_count?: number,
    /** Number of controls planned for implementation. */
    planned_count?: number,
    /** Number of controls marked not applicable. */
    not_applicable_count?: number,
    /** Date of last review. */
    last_review_date?: date,
    /** Person who approved the document. */
    approved_by?: string,
}


/**
 * A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
 */
export interface SoAEntry {
    /** Reference to the control (e.g., A.5.1). */
    control_reference?: SecurityControlId,
    /** Whether the control is applicable. */
    is_applicable?: boolean,
    /** Justification for including the control. */
    inclusion_justification?: string,
    /** Justification for excluding the control. */
    exclusion_justification?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Evidence of control implementation. */
    implementation_evidence?: string,
    /** Role responsible for the objective or control. */
    responsible_role?: RoleId,
    /** Target date for implementing the control. */
    target_implementation_date?: date,
}


/**
 * A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
 */
export interface SecurityControl extends NamedEntity {
    /** Control identifier from Annex A (e.g., 5.1, 8.24). */
    control_id?: string,
    /** Title of the control. */
    control_title?: string,
    /** Domain category of the control. */
    control_category?: string,
    /** Full text of the control requirement. */
    control_text?: string,
    /** Guidance for implementing the control. */
    implementation_guidance?: string,
    /** Other controls related to this one. */
    related_controls?: SecurityControlId[],
    /** Threats this control addresses. */
    applicable_threats?: string[],
    /** Asset types this control applies to. */
    applicable_assets?: string[],
    /** Person responsible for the control. */
    control_owner?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Date the control was implemented. */
    implementation_date?: date,
    /** Rating of control effectiveness. */
    effectiveness_rating?: string,
    /** Date the control was last tested. */
    last_test_date?: date,
    /** References to evidence of implementation. */
    evidence_references?: string[],
}


/**
 * A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
 */
export interface Resource extends NamedEntity {
    /** Type of resource. */
    resource_type?: string,
    /** Quantity of the resource. */
    quantity?: string,
    /** Date the resource was allocated. */
    allocation_date?: date,
    /** What the resource is allocated to. */
    allocated_to?: string,
    /** Cost of the resource. */
    cost?: string,
    /** Current availability of the resource. */
    availability_status?: string,
}


/**
 * Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
 */
export interface CompetenceRecord extends DocumentedInformation {
    /** Name of the person. */
    person_name?: string,
    /** Role of the person. */
    person_role?: string,
    /** Competencies required for the role. */
    required_competencies?: string[],
    /** Education qualifications. */
    education_records?: string[],
    /** Training completed. */
    training_records?: string[],
    /** Relevant experience. */
    experience_records?: string[],
    /** Date of last competency assessment. */
    competency_assessment_date?: date,
    /** Identified competency gaps. */
    competency_gaps?: string[],
    /** Actions to address competency gaps. */
    development_actions?: string[],
}


/**
 * The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
 */
export interface AwarenessProgram extends DocumentedInformation {
    /** Topics covered in awareness program. */
    awareness_topics?: string[],
    /** Methods used to deliver awareness content. */
    delivery_methods?: string[],
    /** Intended audience for the policy or document. */
    target_audience?: string,
    /** Frequency of the activity. */
    frequency?: string,
    /** How completion is tracked. */
    completion_tracking?: string,
    /** How effectiveness is measured. */
    effectiveness_measures?: string,
}


/**
 * Plan for internal and external communications relevant to the ISMS per Clause 7.4.
 */
export interface CommunicationPlan extends DocumentedInformation {
    /** Communication items in the plan. */
    communication_items?: CommunicationItem[],
}


/**
 * A single communication requirement within the communication plan.
 */
export interface CommunicationItem {
    /** Subject of the communication. */
    subject?: string,
    /** Purpose of the communication. */
    purpose?: string,
    /** Target audience. */
    audience?: string,
    /** Frequency of the activity. */
    frequency?: string,
    /** Method of communication. */
    method?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Whether records are required. */
    records_required?: boolean,
}


/**
 * A documented procedure for operational planning and control per Clause 8.1.
 */
export interface OperationalProcedure extends DocumentedInformation {
    /** Scope of the procedure. */
    procedure_scope?: string,
    /** Criteria established for the process. */
    process_criteria?: string,
    /** Control measures implemented. */
    control_measures?: string[],
    /** Roles responsible for the procedure. */
    responsible_roles?: RoleId[],
    /** Other controls related to this one. */
    related_controls?: SecurityControlId[],
    /** Requirements for controlling changes. */
    change_control_requirements?: string,
}


/**
 * The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
 */
export interface MonitoringProgram extends DocumentedInformation {
    /** Items to be monitored. */
    monitoring_items?: MonitoringItem[],
}


/**
 * A single item to be monitored and measured per 9.1.
 */
export interface MonitoringItem {
    /** Name of the metric. */
    metric_name?: string,
    /** Description of what is measured. */
    metric_description?: string,
    /** Method used to measure the metric. */
    measurement_method?: string,
    /** How often measurement is performed. */
    measurement_frequency?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** How often analysis is performed. */
    analysis_frequency?: string,
    /** Person performing analysis. */
    analyst?: string,
    /** Target threshold value. */
    target_threshold?: string,
    /** Threshold triggering alerts. */
    alert_threshold?: string,
    /** Current measured value. */
    current_value?: string,
    /** Current trend direction. */
    trend?: string,
}


/**
 * An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
 */
export interface InternalAudit extends DocumentedInformation {
    /** Reference identifier for the audit. */
    audit_reference?: string,
    /** Type of audit. */
    audit_type?: string,
    /** Scope of the audit. */
    audit_scope?: string,
    /** Criteria against which audit is conducted. */
    audit_criteria?: string[],
    /** Objectives of the audit. */
    audit_objectives?: string[],
    /** Start date of audit period. */
    audit_period_start?: date,
    /** End date of audit period. */
    audit_period_end?: date,
    /** Lead auditor for the audit. */
    lead_auditor?: string,
    /** Audit team members. */
    audit_team?: string[],
    /** Representatives from audited areas. */
    auditee_representatives?: string[],
    /** Audit plan document reference. */
    audit_plan?: string,
    /** Audit findings. */
    findings?: AuditFindingId[],
    /** Positive observations noted. */
    positive_observations?: string[],
    /** Overall audit conclusion. */
    audit_conclusion?: string,
    /** Date the report was issued. */
    report_date?: date,
    /** Distribution list for the report. */
    report_distribution?: string[],
}


/**
 * The internal audit programme per 9.2.2, planning audit activities over a defined period.
 */
export interface AuditProgramme extends DocumentedInformation {
    /** Period covered by the audit programme. */
    programme_period?: string,
    /** Audits planned in this programme. */
    planned_audits?: InternalAuditId[],
    /** Rationale for audit frequency decisions. */
    audit_frequency_rationale?: string,
    /** Resource requirements for the programme. */
    resource_requirements?: string,
    /** Required qualifications for auditors. */
    auditor_qualifications?: string,
    /** Current status of the programme. */
    programme_status?: string,
}


/**
 * A finding from an internal audit, including nonconformities, observations, and positive findings.
 */
export interface AuditFinding extends NamedEntity {
    /** Type of audit finding. */
    finding_type?: string,
    /** Reference to standard clause. */
    clause_reference?: string,
    /** Reference to the control (e.g., A.5.1). */
    control_reference?: SecurityControlId,
    /** Description of the finding. */
    finding_description?: string,
    /** Evidence supporting the finding. */
    objective_evidence?: string,
    /** Analysis of root cause. */
    root_cause_analysis?: string,
    /** Risk implications of the finding. */
    risk_implication?: string,
    /** Recommended action to address finding. */
    recommended_action?: string,
    /** Response from the auditee. */
    auditee_response?: string,
    /** Corrective action linked to this finding. */
    linked_corrective_action?: CorrectiveActionId,
    /** Status of finding closure. */
    closure_status?: string,
    /** Date the finding was closed. */
    closure_date?: date,
}


/**
 * A management review per Clause 9.3, conducted by top management to ensure ISMS suitability, adequacy, and effectiveness.
 */
export interface ManagementReview extends DocumentedInformation {
    /** Date when the management review was conducted. */
    review_date?: date,
    /** Attendees of the review. */
    attendees?: string[],
    /** Status of actions from previous reviews. */
    previous_actions_status?: string,
    /** Changes in context since last review. */
    context_changes?: string,
    /** Changes in interested party requirements. */
    interested_party_changes?: string,
    /** Trends in information security performance. */
    performance_trends?: string,
    /** Summary of audit results. */
    audit_results_summary?: string,
    /** Results of risk assessment. */
    risk_assessment_results?: string,
    /** Opportunities for improvement identified. */
    improvement_opportunities?: string[],
    /** Decisions made in the review. */
    decisions?: string[],
    /** Action items from the review. */
    action_items?: string[],
    /** Planned date for next review. */
    next_review_date?: date,
}


/**
 * A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
 */
export interface Nonconformity extends NamedEntity {
    /** Source of nonconformity detection. */
    nonconformity_source?: string,
    /** Date the nonconformity was detected. */
    detection_date?: date,
    /** Person or process that detected the nonconformity. */
    detected_by?: string,
    /** Requirement that was not fulfilled. */
    requirement_violated?: string,
    /** Description of the nonconformity. */
    nonconformity_description?: string,
    /** Immediate actions taken to control/correct. */
    immediate_actions?: string[],
    /** How consequences were dealt with. */
    consequences_addressed?: string,
    /** Root cause of the nonconformity. */
    root_cause?: string,
    /** Check for similar nonconformities elsewhere. */
    similar_nonconformities_check?: string,
    /** Corrective actions addressing this nonconformity. */
    linked_corrective_actions?: CorrectiveActionId[],
    /** Current status of the document or entity. */
    status?: string,
    /** Date the finding was closed. */
    closure_date?: date,
    /** Evidence supporting closure. */
    closure_evidence?: string,
}


/**
 * A corrective action per Clause 10.2 to eliminate the cause of a nonconformity and prevent recurrence.
 */
export interface CorrectiveAction extends NamedEntity {
    /** Nonconformity this action addresses. */
    linked_nonconformity?: NonconformityId,
    /** Description of the action. */
    action_description?: string,
    /** Root cause this action addresses. */
    root_cause_addressed?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Target date for completing the action. */
    target_completion_date?: date,
    /** Actual date the action was completed. */
    actual_completion_date?: date,
    /** Resources required for implementation. */
    resources_required?: string,
    /** Criteria for evaluating effectiveness. */
    effectiveness_criteria?: string,
    /** Date effectiveness was reviewed. */
    effectiveness_review_date?: date,
    /** Whether effectiveness was verified. */
    effectiveness_verified?: boolean,
    /** Changes to ISMS required as a result. */
    isms_changes_required?: string,
    /** Current status of the document or entity. */
    status?: string,
}


/**
 * An opportunity for continual improvement per Clause 10.1, enhancing ISMS suitability, adequacy, or effectiveness.
 */
export interface ImprovementOpportunity extends NamedEntity {
    /** Source of the improvement opportunity. */
    improvement_source?: string,
    /** Date identified. */
    identification_date?: date,
    /** Person who identified it. */
    identified_by?: string,
    /** Description of the improvement. */
    improvement_description?: string,
    /** Expected benefit from implementation. */
    expected_benefit?: string,
    /** Priority level. */
    priority?: string,
    /** Plan for implementing the improvement. */
    implementation_plan?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Target date for achieving the objective. */
    target_date?: date,
    /** Actual date the action was completed. */
    actual_completion_date?: date,
    /** Assessment of actual outcomes. */
    outcome_assessment?: string,
    /** Current status of the document or entity. */
    status?: string,
}


/**
 * An information asset or associated asset requiring protection, per Annex A control 5.9.
 */
export interface Asset extends NamedEntity {
    /** Type of asset. */
    asset_type?: string,
    /** Owner of the asset. */
    asset_owner?: string,
    /** Custodian responsible for day-to-day protection. */
    asset_custodian?: string,
    /** Information classification level. */
    classification?: string,
    /** Physical or logical location. */
    location?: string,
    /** Criticality rating of the asset. */
    criticality?: string,
    /** Associated risks. */
    related_risks?: RiskId[],
    /** Controls related to this policy. */
    applicable_controls?: SecurityControlId[],
}


/**
 * An information security event per A.5.25, which may or may not be categorized as an incident.
 */
export interface InformationSecurityEvent extends NamedEntity {
    /** Date and time of the event. */
    event_datetime?: string,
    /** Person who reported the event. */
    reporter?: string,
    /** Description of the event. */
    event_description?: string,
    /** Assets affected by this risk or incident. */
    affected_assets?: AssetId[],
    /** Initial assessment of the event. */
    initial_assessment?: string,
    /** Whether the event was categorized as an incident. */
    categorized_as_incident?: boolean,
    /** Linked incident if categorized. */
    linked_incident?: InformationSecurityIncidentId,
}


/**
 * An information security incident per A.5.26, requiring response per documented procedures.
 */
export interface InformationSecurityIncident extends NamedEntity {
    /** Date and time the incident occurred or was detected. */
    incident_datetime?: string,
    /** Category of incident. */
    incident_category?: string,
    /** Severity rating. */
    severity?: string,
    /** Assets affected by this risk or incident. */
    affected_assets?: AssetId[],
    /** CIA properties affected. */
    affected_cia?: string[],
    /** Description of the incident. */
    incident_description?: string,
    /** How the incident was detected. */
    detection_method?: string,
    /** Actions taken in response. */
    response_actions?: string[],
    /** Actions to contain the incident. */
    containment_actions?: string[],
    /** Actions to eradicate the cause. */
    eradication_actions?: string[],
    /** Actions to recover normal operations. */
    recovery_actions?: string[],
    /** Root cause of the nonconformity. */
    root_cause?: string,
    /** Lessons learned from the incident. */
    lessons_learned?: string,
    /** Evidence collected. */
    evidence_collected?: string[],
    /** Whether notification to authorities/parties was required. */
    notification_required?: boolean,
    /** Notifications that were made. */
    notifications_made?: string[],
    /** Date and time of incident closure. */
    closure_datetime?: string,
    /** Post-incident review findings. */
    post_incident_review?: string,
}



