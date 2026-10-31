export type IsmsRecordMixinIsmsId = string;
export type IsmsManagementSystemIsmsId = string;
export type IsmsOrganizationIsmsId = string;
export type IsmsInterestedPartyIsmsId = string;
export type IsmsPolicyIsmsId = string;
export type IsmsTopicSpecificPolicyIsmsId = string;
export type IsmsRoleIsmsId = string;
export type IsmsObjectiveIsmsId = string;
export type IsmsRiskAssessmentProcessIsmsId = string;
export type IsmsRiskAssessmentIsmsId = string;
export type IsmsRiskIsmsId = string;
export type IsmsRiskTreatmentProcessIsmsId = string;
export type IsmsRiskTreatmentPlanIsmsId = string;
export type IsmsStatementOfApplicabilityIsmsId = string;
export type IsmsControlIsmsId = string;
export type IsmsAssetIsmsId = string;
export type IsmsResourceIsmsId = string;
export type IsmsCompetenceRecordIsmsId = string;
export type IsmsAwarenessProgrammeIsmsId = string;
export type IsmsCommunicationPlanIsmsId = string;
export type IsmsDocumentedInformationIsmsId = string;
export type IsmsOperationalProcedureIsmsId = string;
export type IsmsMonitoringProgrammeIsmsId = string;
export type IsmsAuditProgrammeIsmsId = string;
export type IsmsAuditIsmsId = string;
export type IsmsAuditFindingIsmsId = string;
export type IsmsManagementReviewIsmsId = string;
export type IsmsNonconformityIsmsId = string;
export type IsmsCorrectiveActionIsmsId = string;
export type IsmsImprovementOpportunityIsmsId = string;
export type IsmsSecurityEventIsmsId = string;
export type IsmsSecurityIncidentIsmsId = string;
/**
* The four themes Annex A sorts its controls into, which ISO/IEC 27002:2022 also uses.
*/
export enum IsmsControlTheme {
    
    /** The organizational controls, numbered A.5.1 to A.5.37. */
    organizational = "organizational",
    /** The people controls, numbered A.6.1 to A.6.8. */
    people = "people",
    /** The physical controls, numbered A.7.1 to A.7.14. */
    physical = "physical",
    /** The technological controls, numbered A.8.1 to A.8.34. */
    technological = "technological",
};
/**
* The 93 reference controls of Annex A, by their numbers. The values carry no titles: the titles and the control text are ISO's.
*/
export enum IsmsAnnexAControl {
    
    AFULL_STOP5FULL_STOP1 = "a_5_1",
    AFULL_STOP5FULL_STOP2 = "a_5_2",
    AFULL_STOP5FULL_STOP3 = "a_5_3",
    AFULL_STOP5FULL_STOP4 = "a_5_4",
    AFULL_STOP5FULL_STOP5 = "a_5_5",
    AFULL_STOP5FULL_STOP6 = "a_5_6",
    AFULL_STOP5FULL_STOP7 = "a_5_7",
    AFULL_STOP5FULL_STOP8 = "a_5_8",
    AFULL_STOP5FULL_STOP9 = "a_5_9",
    AFULL_STOP5FULL_STOP10 = "a_5_10",
    AFULL_STOP5FULL_STOP11 = "a_5_11",
    AFULL_STOP5FULL_STOP12 = "a_5_12",
    AFULL_STOP5FULL_STOP13 = "a_5_13",
    AFULL_STOP5FULL_STOP14 = "a_5_14",
    AFULL_STOP5FULL_STOP15 = "a_5_15",
    AFULL_STOP5FULL_STOP16 = "a_5_16",
    AFULL_STOP5FULL_STOP17 = "a_5_17",
    AFULL_STOP5FULL_STOP18 = "a_5_18",
    AFULL_STOP5FULL_STOP19 = "a_5_19",
    AFULL_STOP5FULL_STOP20 = "a_5_20",
    AFULL_STOP5FULL_STOP21 = "a_5_21",
    AFULL_STOP5FULL_STOP22 = "a_5_22",
    AFULL_STOP5FULL_STOP23 = "a_5_23",
    AFULL_STOP5FULL_STOP24 = "a_5_24",
    AFULL_STOP5FULL_STOP25 = "a_5_25",
    AFULL_STOP5FULL_STOP26 = "a_5_26",
    AFULL_STOP5FULL_STOP27 = "a_5_27",
    AFULL_STOP5FULL_STOP28 = "a_5_28",
    AFULL_STOP5FULL_STOP29 = "a_5_29",
    AFULL_STOP5FULL_STOP30 = "a_5_30",
    AFULL_STOP5FULL_STOP31 = "a_5_31",
    AFULL_STOP5FULL_STOP32 = "a_5_32",
    AFULL_STOP5FULL_STOP33 = "a_5_33",
    AFULL_STOP5FULL_STOP34 = "a_5_34",
    AFULL_STOP5FULL_STOP35 = "a_5_35",
    AFULL_STOP5FULL_STOP36 = "a_5_36",
    AFULL_STOP5FULL_STOP37 = "a_5_37",
    AFULL_STOP6FULL_STOP1 = "a_6_1",
    AFULL_STOP6FULL_STOP2 = "a_6_2",
    AFULL_STOP6FULL_STOP3 = "a_6_3",
    AFULL_STOP6FULL_STOP4 = "a_6_4",
    AFULL_STOP6FULL_STOP5 = "a_6_5",
    AFULL_STOP6FULL_STOP6 = "a_6_6",
    AFULL_STOP6FULL_STOP7 = "a_6_7",
    AFULL_STOP6FULL_STOP8 = "a_6_8",
    AFULL_STOP7FULL_STOP1 = "a_7_1",
    AFULL_STOP7FULL_STOP2 = "a_7_2",
    AFULL_STOP7FULL_STOP3 = "a_7_3",
    AFULL_STOP7FULL_STOP4 = "a_7_4",
    AFULL_STOP7FULL_STOP5 = "a_7_5",
    AFULL_STOP7FULL_STOP6 = "a_7_6",
    AFULL_STOP7FULL_STOP7 = "a_7_7",
    AFULL_STOP7FULL_STOP8 = "a_7_8",
    AFULL_STOP7FULL_STOP9 = "a_7_9",
    AFULL_STOP7FULL_STOP10 = "a_7_10",
    AFULL_STOP7FULL_STOP11 = "a_7_11",
    AFULL_STOP7FULL_STOP12 = "a_7_12",
    AFULL_STOP7FULL_STOP13 = "a_7_13",
    AFULL_STOP7FULL_STOP14 = "a_7_14",
    AFULL_STOP8FULL_STOP1 = "a_8_1",
    AFULL_STOP8FULL_STOP2 = "a_8_2",
    AFULL_STOP8FULL_STOP3 = "a_8_3",
    AFULL_STOP8FULL_STOP4 = "a_8_4",
    AFULL_STOP8FULL_STOP5 = "a_8_5",
    AFULL_STOP8FULL_STOP6 = "a_8_6",
    AFULL_STOP8FULL_STOP7 = "a_8_7",
    AFULL_STOP8FULL_STOP8 = "a_8_8",
    AFULL_STOP8FULL_STOP9 = "a_8_9",
    AFULL_STOP8FULL_STOP10 = "a_8_10",
    AFULL_STOP8FULL_STOP11 = "a_8_11",
    AFULL_STOP8FULL_STOP12 = "a_8_12",
    AFULL_STOP8FULL_STOP13 = "a_8_13",
    AFULL_STOP8FULL_STOP14 = "a_8_14",
    AFULL_STOP8FULL_STOP15 = "a_8_15",
    AFULL_STOP8FULL_STOP16 = "a_8_16",
    AFULL_STOP8FULL_STOP17 = "a_8_17",
    AFULL_STOP8FULL_STOP18 = "a_8_18",
    AFULL_STOP8FULL_STOP19 = "a_8_19",
    AFULL_STOP8FULL_STOP20 = "a_8_20",
    AFULL_STOP8FULL_STOP21 = "a_8_21",
    AFULL_STOP8FULL_STOP22 = "a_8_22",
    AFULL_STOP8FULL_STOP23 = "a_8_23",
    AFULL_STOP8FULL_STOP24 = "a_8_24",
    AFULL_STOP8FULL_STOP25 = "a_8_25",
    AFULL_STOP8FULL_STOP26 = "a_8_26",
    AFULL_STOP8FULL_STOP27 = "a_8_27",
    AFULL_STOP8FULL_STOP28 = "a_8_28",
    AFULL_STOP8FULL_STOP29 = "a_8_29",
    AFULL_STOP8FULL_STOP30 = "a_8_30",
    AFULL_STOP8FULL_STOP31 = "a_8_31",
    AFULL_STOP8FULL_STOP32 = "a_8_32",
    AFULL_STOP8FULL_STOP33 = "a_8_33",
    AFULL_STOP8FULL_STOP34 = "a_8_34",
};
/**
* How far a control or a plan has been put into effect.
*/
export enum IsmsImplementationStatus {
    
    /** Nothing has been done yet. */
    not_started = "not_started",
    /** The work is planned, with a timeline. */
    planned = "planned",
    /** The work is under way. */
    in_progress = "in_progress",
    /** The work is done and in operation. */
    implemented = "implemented",
};
/**
* The ways of treating a risk, by the names ISO/IEC 27005 gives them.
*/
export enum IsmsRiskTreatmentOption {
    
    /** Change the risk with controls that lower its likelihood or its consequences. */
    modify = "modify",
    /** Keep the risk as it is, with the risk owner's approval. */
    retain = "retain",
    /** Remove the risk by stopping or changing what gives rise to it. */
    avoid = "avoid",
    /** Share the risk with another party, such as an insurer or a supplier. */
    share = "share",
};
/**
* A five-point scale of risk level, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
*/
export enum IsmsRiskLevel {
    
    /** Small enough to need no action. */
    very_low = "very_low",
    /** Managed by routine procedures. */
    low = "low",
    /** Needs management's attention and planned controls. */
    medium = "medium",
    /** Needs treatment first and escalation. */
    high = "high",
    /** Threatens the organization's objectives and needs action at once. */
    critical = "critical",
};
/**
* A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
*/
export enum IsmsLikelihood {
    
    /** Not expected to happen. */
    rare = "rare",
    /** Could happen, but is not expected to. */
    unlikely = "unlikely",
    /** Might happen at some point. */
    possible = "possible",
    /** Will probably happen. */
    likely = "likely",
    /** Expected to happen. */
    almost_certain = "almost_certain",
};
/**
* A five-point scale of consequence, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
*/
export enum IsmsImpact {
    
    /** No noticeable effect on operations or objectives. */
    negligible = "negligible",
    /** An effect normal operations absorb. */
    minor = "minor",
    /** An effect that needs management to step in. */
    moderate = "moderate",
    /** A serious effect on objectives, reputation or compliance. */
    major = "major",
    /** An effect that threatens the organization's survival. */
    severe = "severe",
};
/**
* The three properties of information that information security preserves, as ISO/IEC 27000 names them.
*/
export enum IsmsSecurityProperty {
    
    /** Only those allowed to see the information can see it. */
    confidentiality = "confidentiality",
    /** The information is accurate and complete. */
    integrity = "integrity",
    /** Those allowed to use the information can use it when they need it. */
    availability = "availability",
};
/**
* The kinds of documented information an IsmsDocumentedInformation record holds. Policies have records of their own.
*/
export enum IsmsDocumentKind {
    
    /** The steps for carrying out an activity the same way each time. */
    procedure = "procedure",
    /** Mandatory requirements for a technology or a process. */
    standard = "standard",
    /** Recommended practice that supports a policy or a procedure. */
    guideline = "guideline",
    /** Evidence of what was done or achieved. */
    record = "record",
    /** How the organization means to reach an objective. */
    plan = "plan",
    /** The formal output of an assessment, audit or review. */
    report = "report",
};
/**
* Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
*/
export enum IsmsAuditType {
    
    /** The organization audits itself; an internal audit. */
    first_party = "first_party",
    /** A party with an interest in the organization audits it, such as a customer. */
    second_party = "second_party",
    /** An independent body audits it, such as a certification body or a regulator. */
    third_party = "third_party",
};
/**
* The kinds of audit finding.
*/
export enum IsmsAuditFindingType {
    
    /** A requirement not met in a way that puts the ISMS's intended results in doubt. */
    major_nonconformity = "major_nonconformity",
    /** A requirement not met in an isolated way that leaves the ISMS's intended results in reach. */
    minor_nonconformity = "minor_nonconformity",
    /** A condition that could lead to a nonconformity if left alone. */
    observation = "observation",
    /** Evidence of practice that works well. */
    positive_finding = "positive_finding",
};
/**
* Kinds of information security incident, for sorting incidents. ISO/IEC 27001 sets no list of its own.
*/
export enum IsmsIncidentCategory {
    
    /** Malicious software, such as a virus, a worm or a trojan. */
    malware = "malware",
    /** Malware that encrypts or takes data to extort money. */
    ransomware = "ransomware",
    /** A message that tries to trick someone into giving up credentials or acting. */
    phishing = "phishing",
    /** Manipulating people into disclosing information or acting unsafely. */
    social_engineering = "social_engineering",
    /** Access to systems or data by someone not allowed it. */
    unauthorized_access = "unauthorized_access",
    /** Someone else taking control of a legitimate account. */
    account_compromise = "account_compromise",
    /** An authorized user going beyond or misusing their privileges. */
    privilege_misuse = "privilege_misuse",
    /** Confidential or personal information disclosed. */
    data_breach = "data_breach",
    /** Information lost or corrupted, by accident or otherwise. */
    data_loss = "data_loss",
    /** Systems made unavailable by flooding or attack. */
    denial_of_service = "denial_of_service",
    /** An attack on a web application, such as an injection. */
    web_application_attack = "web_application_attack",
    /** An incident that starts at a supplier, a partner or a third-party component. */
    supply_chain = "supply_chain",
    /** Harm done by someone inside the organization, on purpose or by neglect. */
    insider_threat = "insider_threat",
    /** Theft, loss or damage of physical assets, or physical access without permission. */
    physical_security = "physical_security",
    /** A misconfiguration that exposes something. */
    configuration_error = "configuration_error",
    /** Cryptography that is weak, broken or misused. */
    cryptographic_failure = "cryptographic_failure",
    /** A breach of the organization's security policies or procedures. */
    policy_violation = "policy_violation",
    /** Any incident the other categories do not fit. */
    other = "other",
};
/**
* Management system standards an ISMS may be integrated with or audited beside, each written to ISO's harmonized structure.
*/
export enum IsmsManagementSystemStandard {
    
    /** Information security management systems. */
    iso_iec_27001 = "iso_iec_27001",
    /** Privacy information management systems. */
    iso_iec_27701 = "iso_iec_27701",
    /** Artificial intelligence management systems. */
    iso_iec_42001 = "iso_iec_42001",
    /** Quality management systems. */
    iso_9001 = "iso_9001",
    /** Environmental management systems. */
    iso_14001 = "iso_14001",
    /** Business continuity management systems. */
    iso_22301 = "iso_22301",
    /** Service management systems. */
    iso_iec_20000_1 = "iso_iec_20000_1",
};


/**
 * What every record of the ISMS has, so that other records can refer to it: an identifier, a title and a description.
 */
export interface IsmsRecordMixin {
    /** The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it. */
    isms_id: string,
    /** The name the organization gives the record. */
    title: string,
    /** What the record says or describes, in the organization's own words. */
    description?: string,
}


/**
 * The control that documented information is kept under. It records who wrote, owns and approved the information, when it takes effect and is reviewed, and how it is classified, distributed, stored and changed. It also records how long it is retained, and whether it came from outside the organization.
 */
export interface IsmsDocumentControlMixin {
    /** The reference the organization's document control gives it. */
    document_reference?: string,
    /** The version of the document. */
    document_version?: string,
    /** Who wrote the document. */
    document_author?: string,
    /** Who answers for the document's content and upkeep. */
    document_owner?: string,
    /** Who approved the document. */
    document_approver?: string,
    /** When the document was approved. */
    document_approval_date?: date,
    /** When the document takes effect. */
    document_effective_date?: date,
    /** When the document was last reviewed. */
    document_last_review_date?: date,
    /** When the document is next due for review. */
    document_next_review_date?: date,
    /** Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn. */
    document_status?: string,
    /** The information classification the document carries. */
    document_classification?: string,
    /** How long the document is kept, as an ISO 8601 duration. */
    document_retention?: string,
    /** How the document is distributed, accessed, retrieved and used. */
    document_distribution?: string[],
    /** How the document is stored and preserved, so that it stays legible. */
    document_storage?: string,
    /** How changes to the document are controlled, such as version control. */
    document_change_control?: string,
    /** Whether the document comes from outside the organization and is kept because the ISMS needs it. */
    document_external_origin?: boolean,
    /** Who the document came from, when it comes from outside. */
    document_external_source?: string,
}


/**
 * One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
 */
export interface IsmsManagementSystem extends IsmsRecordMixin {
    /** The organization that runs the ISMS. */
    isms_organization?: IsmsOrganization,
    /** The person or group that directs and controls the organization at the highest level. */
    isms_top_management?: string,
    /** The body top management answers to, such as a board, where there is one. */
    isms_governing_body?: string,
    /** What shows that top management leads and commits to the ISMS. */
    isms_leadership_evidence?: string[],
    /** The scope of the ISMS, as the organization states it. */
    isms_scope?: string,
    /** Where the scope of the ISMS ends. */
    isms_scope_boundaries?: string[],
    /** What the scope leaves out, each with the reason. */
    isms_scope_exclusions?: string[],
    /** The interfaces and dependencies between what the organization does and what other organizations do, which the scope takes into account. */
    isms_interfaces?: string[],
    /** The processes the ISMS needs and how they interact. */
    isms_processes?: string,
    /** The internal issues that bear on the ISMS. */
    isms_internal_issues?: string[],
    /** The external issues that bear on the ISMS. */
    isms_external_issues?: string[],
    /** The actions planned to address the ISMS's risks and opportunities, and how they fit into its processes. */
    isms_risk_and_opportunity_actions?: string[],
    /** The changes to the ISMS that are planned. */
    isms_planned_changes?: string[],
    /** The processes, products or services from outside the organization that the ISMS relies on and controls. */
    isms_external_services?: string[],
    /** Where the ISMS stands with certification, in the organization's own terms. */
    isms_certification_status?: string,
    /** The body that certifies the ISMS. */
    isms_certification_body?: string,
    /** When the ISMS was certified. */
    isms_certification_date?: date,
    /** When the ISMS is next due for recertification. */
    isms_recertification_date?: date,
    /** The interested parties the ISMS takes into account. */
    isms_interested_parties?: IsmsInterestedParty[],
    /** The information security policy. */
    isms_policy?: IsmsPolicy,
    /** The topic-specific policies under the information security policy. */
    isms_topic_specific_policies?: IsmsTopicSpecificPolicy[],
    /** The roles that carry the ISMS's responsibilities and authorities. */
    isms_roles?: IsmsRole[],
    /** The information security objectives. */
    isms_objectives?: IsmsObjective[],
    /** The information security risk assessment process. */
    isms_risk_assessment_process?: IsmsRiskAssessmentProcess,
    /** The information security risk treatment process. */
    isms_risk_treatment_process?: IsmsRiskTreatmentProcess,
    /** The risk assessments carried out. */
    isms_risk_assessments?: IsmsRiskAssessment[],
    /** The risks identified, the risk register. */
    isms_risks?: IsmsRisk[],
    /** The risk treatment plans. */
    isms_risk_treatment_plans?: IsmsRiskTreatmentPlan[],
    /** The Statement of Applicability. */
    isms_statement_of_applicability?: IsmsStatementOfApplicability,
    /** The controls the organization has determined it needs. */
    isms_controls?: IsmsControl[],
    /** The inventory of information and other associated assets. */
    isms_assets?: IsmsAsset[],
    /** The resources provided for the ISMS. */
    isms_resources?: IsmsResource[],
    /** The records of competence. */
    isms_competence_records?: IsmsCompetenceRecord[],
    /** The awareness programme. */
    isms_awareness_programme?: IsmsAwarenessProgramme,
    /** The plan for communication about the ISMS. */
    isms_communication_plan?: IsmsCommunicationPlan,
    /** The documented information the ISMS keeps that no more specific list holds, such as procedures, plans and reports. */
    isms_documented_information?: IsmsDocumentedInformation[],
    /** The procedures for operational planning and control. */
    isms_operational_procedures?: IsmsOperationalProcedure[],
    /** The programme of monitoring and measurement. */
    isms_monitoring_programme?: IsmsMonitoringProgramme,
    /** The audit programmes. */
    isms_audit_programmes?: IsmsAuditProgramme[],
    /** The audits of the ISMS, internal and external. */
    isms_audits?: IsmsAudit[],
    /** The management reviews. */
    isms_management_reviews?: IsmsManagementReview[],
    /** The nonconformities found. */
    isms_nonconformities?: IsmsNonconformity[],
    /** The corrective actions taken. */
    isms_corrective_actions?: IsmsCorrectiveAction[],
    /** The opportunities for improvement identified. */
    isms_improvements?: IsmsImprovementOpportunity[],
    /** The information security events reported, the incidents among them. */
    isms_security_events?: IsmsSecurityEvent[],
}


/**
 * The organization that runs the ISMS, with what it needs to know about itself to understand its context.
 */
export interface IsmsOrganization extends IsmsRecordMixin {
    /** The organization's registered legal name. */
    organization_legal_name?: string,
    /** Other names the organization trades under. */
    organization_trading_names?: string[],
    /** What kind of organization it is, such as a company, an agency or a charity. */
    organization_kind?: string,
    /** The organization's main industry sector. */
    organization_sector?: string,
    /** How the organization classes its own size. */
    organization_size?: string,
    /** About how many people the organization employs. */
    organization_employee_count?: number,
    /** The countries or regions the organization works in. */
    organization_locations?: string[],
    /** The jurisdictions whose laws and regulations apply to the organization. */
    organization_jurisdictions?: string[],
    /** The organization's parent, if it has one. */
    organization_parent?: string,
    /** The organization's subsidiaries, if it has any. */
    organization_subsidiaries?: string[],
    /** Whether the organization has determined that climate change is a relevant issue for its ISMS. */
    organization_climate_change_relevant?: boolean,
}


/**
 * A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
 */
export interface IsmsInterestedParty extends IsmsRecordMixin {
    /** What kind of interested party it is, in the organization's own terms. */
    party_category?: string,
    /** How the party relates to the organization. */
    party_relationship?: string,
    /** The party's requirements that bear on information security. */
    party_requirements?: string[],
    /** Which of those requirements the ISMS addresses. */
    party_addressed_requirements?: string[],
    /** The party's requirements that concern climate change. */
    party_climate_change_requirements?: string[],
    /** What the party needs to be told, and how. */
    party_communication_needs?: string,
    /** How to reach the party. */
    party_contact?: string,
}


/**
 * The information security policy that top management sets: the organization's commitment and the frame for its information security objectives.
 */
export interface IsmsPolicy extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The policy's own statement, in the organization's words. */
    policy_statement?: string,
    /** How the policy frames the setting of information security objectives. */
    policy_objectives_framework?: string,
    /** The commitments the policy makes. */
    policy_commitments?: string[],
    /** To whom and to what the policy applies. */
    policy_applicability?: string,
    /** When the policy was communicated within the organization. */
    policy_communication_date?: date,
    /** Whether staff must acknowledge the policy. */
    policy_acknowledgement_required?: boolean,
    /** The other management system standards the ISMS is integrated with under the same policy. */
    policy_management_systems?: string,
}


/**
 * A policy on one topic of information security, such as access control or backup, that supports the information security policy.
 */
export interface IsmsTopicSpecificPolicy extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The organization's controls that the record concerns. */
    relevant_controls?: IsmsControlIsmsId[],
    /** The topic the policy covers. */
    topic_policy_topic?: string,
    /** The information security policy this policy supports. */
    topic_policy_parent?: IsmsPolicyIsmsId,
    /** Whom the policy is written for. */
    topic_policy_audience?: string,
}


/**
 * A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
 */
export interface IsmsRole extends IsmsRecordMixin {
    /** What kind of role it is, in the organization's own terms. */
    role_category?: string,
    /** The responsibilities assigned to the role. */
    role_responsibilities?: string[],
    /** The authorities the role carries. */
    role_authorities?: string[],
    /** What the role is accountable for. */
    role_accountability?: string,
    /** The people who hold the role. */
    role_holders?: string[],
    /** How the role may delegate its responsibilities. */
    role_delegation?: string,
    /** The role this role reports to. */
    role_reports_to?: IsmsRoleIsmsId,
}


/**
 * An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
 */
export interface IsmsObjective extends IsmsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** The organization's controls that the record concerns. */
    relevant_controls?: IsmsControlIsmsId[],
    /** The objective, as the organization states it. */
    objective_statement?: string,
    /** The value the objective aims for. */
    objective_target?: string,
    /** The value last measured. */
    objective_current_value?: string,
    /** How the objective's value is defined. */
    objective_metric?: string,
    /** How the value is measured. */
    objective_measurement_method?: string,
    /** How often the value is measured. */
    objective_measurement_frequency?: string,
    /** When the objective is to be reached. */
    objective_target_date?: date,
    /** How far the objective has been reached, in the organization's own terms. */
    objective_achievement?: string,
    /** The risks the objective concerns. */
    objective_risks?: IsmsRiskIsmsId[],
    /** What will be done to reach the objective. */
    objective_action_plan?: string,
    /** The resources needed to reach the objective. */
    objective_resources?: string,
}


/**
 * The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
 */
export interface IsmsRiskAssessmentProcess extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The criteria for accepting a risk. */
    risk_acceptance_criteria?: string,
    /** The criteria for carrying out a risk assessment. */
    risk_assessment_criteria?: string,
    /** The method used to identify, analyse and evaluate risks. */
    risk_assessment_method?: string,
    /** The scale for rating likelihood. */
    risk_likelihood_scale?: string,
    /** The scale for rating consequences. */
    risk_impact_scale?: string,
    /** How likelihood and consequence combine into a risk level. */
    risk_matrix?: string,
    /** How often risks are assessed. */
    risk_assessment_frequency?: string,
    /** The events that start a risk assessment outside the planned ones. */
    risk_assessment_triggers?: string[],
}


/**
 * One risk assessment carried out under the risk assessment process, and what it found.
 */
export interface IsmsRiskAssessment extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** What the assessment covered. */
    assessment_scope?: string,
    /** When the assessment was carried out. */
    assessment_date?: date,
    /** Who carried out the assessment. */
    assessment_assessor?: string,
    /** The method this assessment applied. */
    assessment_method_used?: string,
    /** The risks the assessment identified. */
    assessment_risks?: IsmsRiskIsmsId[],
    /** A summary of what the assessment found. */
    assessment_summary?: string,
    /** What the assessment recommends. */
    assessment_recommendations?: string[],
    /** When the next assessment is planned. */
    assessment_next_date?: date,
}


/**
 * An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
 */
export interface IsmsRisk extends IsmsRecordMixin {
    /** The assets the risk, event or incident affects. */
    affected_assets?: IsmsAssetIsmsId[],
    /** Which of confidentiality, integrity and availability the risk or incident threatens. */
    affected_security_properties?: string,
    /** Where the risk comes from. */
    risk_source?: string,
    /** The threat that could cause harm. */
    risk_threat?: string,
    /** The weakness the threat could exploit. */
    risk_vulnerability?: string,
    /** The person who is accountable for the risk and has the authority to manage it. */
    risk_owner?: string,
    /** How likely the risk is. */
    risk_likelihood?: string,
    /** How severe the consequences would be. */
    risk_impact?: string,
    /** The risk's level before controls. */
    risk_inherent_level?: string,
    /** The organization's controls already acting on the risk. */
    risk_existing_controls?: IsmsControlIsmsId[],
    /** The risk's level after controls. */
    risk_residual_level?: string,
    /** The treatment chosen for the risk. */
    risk_treatment_option?: string,
    /** How soon the risk is to be treated, in the organization's own terms. */
    risk_treatment_priority?: string,
}


/**
 * The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
 */
export interface IsmsRiskTreatmentProcess extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** How a treatment option is chosen for a risk. */
    treatment_options_guidance?: string,
    /** How the controls a treatment needs are chosen. */
    treatment_control_selection?: string,
    /** How the chosen controls are compared with Annex A, so that no necessary control is left out. */
    treatment_annex_a_comparison?: string,
    /** The template the Statement of Applicability follows. */
    treatment_soa_template?: string,
    /** How a treatment plan and its residual risks are approved. */
    treatment_approval_workflow?: string,
}


/**
 * A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
 */
export interface IsmsRiskTreatmentPlan extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** How far the control or the plan has been put into effect. */
    implementation_state?: string,
    /** What the plan covers. */
    plan_scope?: string,
    /** The risks the plan treats. */
    plan_risks?: IsmsRiskIsmsId[],
    /** The actions the plan takes. */
    plan_actions?: string[],
    /** The controls the plan puts in place. */
    plan_controls?: IsmsControlIsmsId[],
    /** The resources the plan needs. */
    plan_resources?: string,
    /** Who carries out the plan. */
    plan_responsible_parties?: string[],
    /** When the plan's actions are to happen. */
    plan_timeline?: string,
    /** The risk owner who approved the plan. */
    plan_risk_owner_approval?: string,
    /** How the risk owners accepted the risk that remains. */
    plan_residual_risk_acceptance?: string,
    /** When the plan was completed. */
    plan_completion_date?: date,
}


/**
 * The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
 */
export interface IsmsStatementOfApplicability extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The statement's entries, one for each control included or Annex A control excluded. */
    soa_entries?: IsmsApplicabilityEntry[],
}


/**
 * One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
 */
export interface IsmsApplicabilityEntry {
    /** The Annex A control a Statement of Applicability entry concerns. */
    entry_annex_a_control?: string,
    /** The kind of entry: IsmsIncludedControl or IsmsExcludedControl. */
    entry_type?: string,
    /** Why the control is included or excluded. */
    entry_justification: string,
}


/**
 * An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
 */
export interface IsmsIncludedControl extends IsmsApplicabilityEntry {
    /** How far the control or the plan has been put into effect. */
    implementation_state: string,
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** The organization's control the entry includes. */
    included_control?: IsmsControlIsmsId,
    /** What shows that the control is in place. */
    included_evidence?: string,
    /** When the control is to be in place, if it is not yet. */
    included_target_date?: date,
}


/**
 * An entry that leaves out an Annex A control the organization does not need, and says why.
 */
export interface IsmsExcludedControl extends IsmsApplicabilityEntry {
}


/**
 * A control the organization has determined it needs to treat its risks. It records what the control does in the organization's words and which Annex A controls it answers to. It also records who owns it, how far it is in place and how well it works.
 */
export interface IsmsControl extends IsmsRecordMixin {
    /** The organization's controls that the record concerns. */
    relevant_controls?: IsmsControlIsmsId[],
    /** How far the control or the plan has been put into effect. */
    implementation_state?: string,
    /** The Annex A controls the control answers to. */
    control_annex_a_controls?: string,
    /** Which of Annex A's four themes the control belongs to. */
    control_theme?: string,
    /** What the control does, in the organization's own words. */
    control_text?: string,
    /** The organization's notes on putting the control in place. */
    control_guidance?: string,
    /** The threats the control acts against. */
    control_threats?: string[],
    /** The kinds of asset the control applies to. */
    control_asset_types?: string[],
    /** The person who owns the control. */
    control_owner?: string,
    /** When the control was put in place. */
    control_implementation_date?: date,
    /** How well the control works, in the organization's own terms. */
    control_effectiveness?: string,
    /** When the control was last tested. */
    control_last_tested?: date,
    /** Where the evidence that the control is in place is kept. */
    control_evidence?: string[],
}


/**
 * An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
 */
export interface IsmsAsset extends IsmsRecordMixin {
    /** The organization's controls that the record concerns. */
    relevant_controls?: IsmsControlIsmsId[],
    /** What kind of asset it is, such as information, software, hardware or a service. */
    asset_category?: string,
    /** Who owns the asset. */
    asset_owner?: string,
    /** Who looks after the asset from day to day. */
    asset_custodian?: string,
    /** The information classification the asset carries. */
    asset_classification?: string,
    /** Where the asset is, physically or logically. */
    asset_location?: string,
    /** How much the asset matters, in the organization's own terms. */
    asset_criticality?: string,
}


/**
 * A resource provided for the ISMS, such as people, time, tools or budget.
 */
export interface IsmsResource extends IsmsRecordMixin {
    /** What kind of resource it is. */
    resource_category?: string,
    /** How much of the resource is provided. */
    resource_quantity?: string,
    /** When the resource was allocated. */
    resource_allocation_date?: date,
    /** What the resource is allocated to. */
    resource_allocated_to?: string,
    /** What the resource costs. */
    resource_cost?: string,
    /** Whether the resource is available now, in the organization's own terms. */
    resource_availability?: string,
}


/**
 * The evidence of one person's competence for work that affects information security, and what is done to close any gap.
 */
export interface IsmsCompetenceRecord extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The person the record is about. */
    competence_person?: string,
    /** The role the person holds. */
    competence_role?: IsmsRoleIsmsId,
    /** The competences the role needs. */
    competence_required?: string[],
    /** The person's relevant education. */
    competence_education?: string[],
    /** The training the person has completed. */
    competence_training?: string[],
    /** The person's relevant experience. */
    competence_experience?: string[],
    /** When the person's competence was last assessed. */
    competence_assessment_date?: date,
    /** The gaps the assessment found. */
    competence_gaps?: string[],
    /** What is done to close the gaps. */
    competence_actions?: string[],
}


/**
 * The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
 */
export interface IsmsAwarenessProgramme extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The topics the programme covers. */
    awareness_topics?: string[],
    /** How the programme is delivered. */
    awareness_methods?: string[],
    /** Whom the programme is for. */
    awareness_audience?: string,
    /** How often the programme runs. */
    awareness_frequency?: string,
    /** How completion is tracked. */
    awareness_completion_tracking?: string,
    /** How the programme's effect is measured. */
    awareness_effectiveness?: string,
}


/**
 * The plan for communication about the ISMS, inside the organization and outside it.
 */
export interface IsmsCommunicationPlan extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The communications the plan provides for. */
    communication_items?: IsmsCommunication[],
}


/**
 * One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
 */
export interface IsmsCommunication {
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** What the communication is about. */
    communication_subject: string,
    /** Why it is communicated. */
    communication_purpose?: string,
    /** To whom it is communicated. */
    communication_audience?: string,
    /** How often it is communicated. */
    communication_frequency?: string,
    /** How it is communicated. */
    communication_method?: string,
    /** Whether a record of the communication is kept. */
    communication_records_required?: boolean,
}


/**
 * A piece of documented information the ISMS keeps under control that no more specific record describes, such as a procedure, a standard, a plan or a report.
 */
export interface IsmsDocumentedInformation extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** What kind of documented information it is. */
    document_kind: string,
}


/**
 * A procedure by which the organization plans and controls the processes that meet its information security requirements.
 */
export interface IsmsOperationalProcedure extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The organization's controls that the record concerns. */
    relevant_controls?: IsmsControlIsmsId[],
    /** What the procedure covers. */
    procedure_scope?: string,
    /** The criteria the processes are run to. */
    procedure_criteria?: string,
    /** The measures that control the processes. */
    procedure_control_measures?: string[],
    /** The roles that carry out the procedure. */
    procedure_roles?: IsmsRoleIsmsId[],
    /** How changes to the processes are controlled. */
    procedure_change_control?: string,
}


/**
 * The programme of monitoring, measurement, analysis and evaluation of information security performance and of the ISMS's effectiveness.
 */
export interface IsmsMonitoringProgramme extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** What the programme monitors and measures. */
    monitoring_items?: IsmsMonitoringItem[],
}


/**
 * One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
 */
export interface IsmsMonitoringItem {
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** The name of what is measured. */
    monitoring_metric: string,
    /** What the measurement shows. */
    monitoring_description?: string,
    /** How it is measured. */
    monitoring_method?: string,
    /** How often it is measured. */
    monitoring_frequency?: string,
    /** How often the results are analysed and evaluated. */
    monitoring_analysis_frequency?: string,
    /** Who analyses and evaluates the results. */
    monitoring_analyst?: string,
    /** The value aimed for. */
    monitoring_target?: string,
    /** The value that calls for action. */
    monitoring_alert_threshold?: string,
    /** The value last measured. */
    monitoring_current_value?: string,
    /** Which way the value is moving. */
    monitoring_trend?: string,
}


/**
 * An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
 */
export interface IsmsAuditProgramme extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** The period the programme covers. */
    programme_period?: string,
    /** The audits the programme plans. */
    programme_audits?: IsmsAuditIsmsId[],
    /** Why the audits happen as often as they do. */
    programme_frequency_rationale?: string,
    /** The resources the programme needs. */
    programme_resources?: string,
    /** The qualifications the auditors need. */
    programme_auditor_qualifications?: string,
    /** Where the programme stands, in the organization's own terms. */
    programme_status?: string,
}


/**
 * An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
 */
export interface IsmsAudit extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** Who carries out the audit, relative to the organization. */
    audit_type: string,
    /** The management system standards the audit covers. */
    audit_standards?: string,
    /** What the audit covers. */
    audit_scope?: string,
    /** What the audit compares the ISMS against. */
    audit_criteria?: string[],
    /** What the audit sets out to establish. */
    audit_objectives?: string[],
    /** When the audit began. */
    audit_period_start?: date,
    /** When the audit ended. */
    audit_period_end?: date,
    /** Who led the audit. */
    audit_lead?: string,
    /** Who else audited. */
    audit_team?: string[],
    /** Who represented the parts of the organization audited. */
    audit_auditees?: string[],
    /** The documented information that holds the audit plan. */
    audit_plan?: IsmsDocumentedInformationIsmsId,
    /** What the audit found, good and bad. */
    audit_findings?: IsmsAuditFinding[],
    /** The audit's overall conclusion. */
    audit_conclusion?: string,
    /** When the audit report was issued. */
    audit_report_date?: date,
    /** Who received the audit report. */
    audit_report_distribution?: string[],
}


/**
 * One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
 */
export interface IsmsAuditFinding extends IsmsRecordMixin {
    /** What kind of finding it is. */
    finding_type: string,
    /** The clause or Annex A control of ISO/IEC 27001:2022 the finding concerns, by number. */
    finding_requirement?: string,
    /** The organization's control the finding concerns. */
    finding_control?: IsmsControlIsmsId,
    /** The objective evidence for the finding. */
    finding_evidence?: string,
    /** What the analysis of the finding's cause found. */
    finding_root_cause?: string,
    /** What the finding means for risk. */
    finding_risk?: string,
    /** What the auditor recommends. */
    finding_recommendation?: string,
    /** How the auditee responded. */
    finding_auditee_response?: string,
    /** The corrective action the finding led to. */
    finding_corrective_action?: IsmsCorrectiveActionIsmsId,
    /** Whether the finding is closed, in the organization's own terms. */
    finding_closure_status?: string,
    /** When the finding was closed. */
    finding_closure_date?: date,
}


/**
 * A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
 */
export interface IsmsManagementReview extends IsmsRecordMixin, IsmsDocumentControlMixin {
    /** When the review was held. */
    review_held_on: date,
    /** Who attended the review. */
    review_attendees?: string[],
    /** Where the actions from earlier reviews stand. */
    review_previous_actions?: string,
    /** How the issues that bear on the ISMS have changed. */
    review_context_changes?: string,
    /** How interested parties' needs and expectations have changed. */
    review_interested_party_changes?: string,
    /** What interested parties said. */
    review_interested_party_feedback?: string,
    /** The trends in information security performance. */
    review_performance_trends?: string,
    /** What the audits found. */
    review_audit_results?: string,
    /** What the risk assessments found. */
    review_risk_assessment_results?: string,
    /** Where risk treatment stands. */
    review_risk_treatment_status?: string,
    /** How risks and opportunities have changed. */
    review_risks_and_opportunities?: string,
    /** The opportunities for improvement raised. */
    review_improvement_opportunities?: string[],
    /** What the review decided. */
    review_decisions?: string[],
    /** What the review asked to be done. */
    review_actions?: string[],
    /** When the next review is planned. */
    review_next_date?: date,
}


/**
 * A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
 */
export interface IsmsNonconformity extends IsmsRecordMixin {
    /** How the nonconformity came to light, such as an audit, a review or an incident. */
    nonconformity_source?: string,
    /** When the nonconformity was found. */
    nonconformity_detected_on?: date,
    /** Who or what found it. */
    nonconformity_detected_by?: string,
    /** The requirement that was not met, of ISO/IEC 27001, of the organization or of an interested party. */
    nonconformity_requirement?: string,
    /** What was done at once to control and correct it. */
    nonconformity_immediate_actions?: string[],
    /** How its consequences were dealt with. */
    nonconformity_consequences?: string,
    /** What caused it. */
    nonconformity_root_cause?: string,
    /** Whether similar nonconformities exist or could occur, and where. */
    nonconformity_similar_check?: string,
    /** Where the nonconformity stands, in the organization's own terms. */
    nonconformity_status?: string,
    /** When it was closed. */
    nonconformity_closure_date?: date,
    /** What shows that it is closed. */
    nonconformity_closure_evidence?: string,
}


/**
 * An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
 */
export interface IsmsCorrectiveAction extends IsmsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** The nonconformities the action addresses. */
    action_nonconformities?: IsmsNonconformityIsmsId[],
    /** The cause the action removes. */
    action_root_cause?: string,
    /** When the action is to be complete. */
    action_target_date?: date,
    /** When the action was complete. */
    action_completion_date?: date,
    /** The resources the action needs. */
    action_resources?: string,
    /** How the action's effect will be judged. */
    action_effectiveness_criteria?: string,
    /** When the action's effect was reviewed. */
    action_effectiveness_review_date?: date,
    /** Whether the review found the action effective. */
    action_effective?: boolean,
    /** The changes to the ISMS the action needs. */
    action_isms_changes?: string,
    /** Where the action stands, in the organization's own terms. */
    action_status?: string,
}


/**
 * An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
 */
export interface IsmsImprovementOpportunity extends IsmsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    responsible_role?: IsmsRoleIsmsId,
    /** Where the opportunity came from, such as a review, an audit or daily work. */
    improvement_source?: string,
    /** When the opportunity was identified. */
    improvement_identified_on?: date,
    /** Who identified it. */
    improvement_identified_by?: string,
    /** What the improvement is expected to bring. */
    improvement_benefit?: string,
    /** How soon it is to be acted on, in the organization's own terms. */
    improvement_priority?: string,
    /** How the improvement is to be made. */
    improvement_plan?: string,
    /** When the improvement is to be made. */
    improvement_target_date?: date,
    /** When it was made. */
    improvement_completion_date?: date,
    /** What the improvement brought. */
    improvement_outcome?: string,
    /** Where it stands, in the organization's own terms. */
    improvement_status?: string,
}


/**
 * An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
 */
export interface IsmsSecurityEvent extends IsmsRecordMixin {
    /** The assets the risk, event or incident affects. */
    affected_assets?: IsmsAssetIsmsId[],
    /** The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident. */
    event_type?: string,
    /** When the event happened, or when it was first noticed. */
    event_occurred_at?: string,
    /** Who reported the event. */
    event_reporter?: string,
    /** What the assessment of the event found. */
    event_assessment?: string,
}


/**
 * An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
 */
export interface IsmsSecurityIncident extends IsmsSecurityEvent {
    /** Which of confidentiality, integrity and availability the risk or incident threatens. */
    affected_security_properties?: string,
    /** What kind of incident it is. */
    incident_category?: string,
    /** How severe the incident is. */
    incident_severity?: string,
    /** How the incident was detected. */
    incident_detection_method?: string,
    /** What was done in response. */
    incident_response_actions?: string[],
    /** What was done to contain it. */
    incident_containment_actions?: string[],
    /** What was done to remove its cause. */
    incident_eradication_actions?: string[],
    /** What was done to restore normal operation. */
    incident_recovery_actions?: string[],
    /** What caused the incident. */
    incident_root_cause?: string,
    /** What the organization learned from it. */
    incident_lessons_learned?: string[],
    /** The evidence collected about it. */
    incident_evidence?: string[],
    /** Whether authorities or other parties had to be told. */
    incident_notification_required?: boolean,
    /** Whom the organization told, and when. */
    incident_notifications?: string[],
    /** When the incident was closed. */
    incident_closed_at?: string,
    /** What the review after the incident found. */
    incident_review?: string,
}



