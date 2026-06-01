import pandera.polars as pla
from pandera.api.polars.types import PolarsData
from . import panderagen_polars_schema as pa_pl
import polars as pl
from typing import Optional


from pandera.typing import (
    Index,
    DataFrame,
    Series
)
from pandera.engines.polars_engine import (
    DateTime,
    Date,
    Time,
    Enum,
    Struct,
    List,
    Object
)


from linkml.generators.panderagen.linkml_pandera_validator import LinkmlPanderaValidator as _LinkmlPanderaValidator


# These are all str for now
ID_TYPES = {
    "NamedEntity": "str",
    "InformationSecurityManagementSystem": "str",
    "DocumentedInformation": "str",
    "InformationSecurityPolicy": "str",
    "TopicSpecificPolicy": "str",
    "InformationSecurityObjective": "str",
    "RiskAssessment": "str",
    "Risk": "str",
    "RiskTreatmentPlan": "str",
    "SoAEntry": "str",
    "StatementOfApplicability": "str",
    "SecurityControl": "str",
    "CommunicationItem": "str",
    "CommunicationPlan": "str",
    "OperationalProcedure": "str",
    "MonitoringItem": "str",
    "MonitoringProgram": "str",
    "InternalAudit": "str",
    "AuditProgramme": "str",
    "AuditFinding": "str",
    "Nonconformity": "str",
    "CorrectiveAction": "str",
    "Asset": "str",
    "InformationSecurityEvent": "str",
    "InformationSecurityIncident": "str",
    "Organization": "str",
    "InterestedParty": "str",
    "Role": "str",
    "RiskAssessmentProcess": "str",
    "RiskTreatmentProcess": "str",
    "Resource": "str",
    "CompetenceRecord": "str",
    "AwarenessProgram": "str",
    "ManagementReview": "str",
    "ImprovementOpportunity": "str",
}

# metamodel_version: 1.11.0
# version: 1.0.0class NamedEntity(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
    """

    _id_name : str =  'id' 
    id: str = pla.Field()
    """
    Unique identifier for this entity instance.
    """
    
    name: str = pla.Field()
    """
    Human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Detailed description of the entity.
    """
    
    created_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the entity was created.
    """
    
    modified_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the entity was last modified.
    """
    
    version: Optional[str] = pla.Field(nullable=True, )
    """
    Version identifier for the entity.
    """
    
    
class InformationSecurityManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required to support the full ISMS lifecycle.
    """

    _id_name : str =  'id' 
    organization: Optional[ID_TYPES['Organization']] = pla.Field(nullable=True, )
    """
    Reference to the organization operating the ISMS.
    """
    
    top_management: Optional[str] = pla.Field(nullable=True, )
    """
    The person or group of people who direct and control the organization at the highest level, accountable for the ISMS per Clause 5.1.
    """
    
    governing_body: Optional[str] = pla.Field(nullable=True, )
    """
    The governing body to which top management reports, where applicable (e.g., board of directors). Referenced in ISO/IEC 27001:2022 Clause 5.1 NOTE.
    """
    
    leadership_commitment_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    Evidence of leadership and commitment with respect to the ISMS as required by Clause 5.1 a-h).
    """
    
    scope_statement: Optional[str] = pla.Field(nullable=True, )
    """
    Documented statement of ISMS scope per 4.3.
    """
    
    scope_boundaries: Optional[str] = pla.Field(nullable=True, )
    """
    Defined boundaries of the ISMS scope.
    """
    
    scope_exclusions: Optional[str] = pla.Field(nullable=True, )
    """
    Any exclusions from scope with justification.
    """
    
    interfaces_and_dependencies: Optional[str] = pla.Field(nullable=True, )
    """
    Interfaces and dependencies between activities performed by the organization and those performed by other organizations, considered when determining the ISMS scope per Clause 4.3 c).
    """
    
    processes_and_interactions: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the processes needed for the ISMS and their interactions, per Clause 4.4.
    """
    
    context_internal_issues: Optional[str] = pla.Field(nullable=True, )
    """
    Internal issues relevant to ISMS per 4.1.
    """
    
    context_external_issues: Optional[str] = pla.Field(nullable=True, )
    """
    External issues relevant to ISMS per 4.1.
    """
    
    interested_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Stakeholders relevant to the ISMS.
    """
    
    information_security_policy: Optional[ID_TYPES['InformationSecurityPolicy']] = pla.Field(nullable=True, )
    """
    Reference to the information security policy.
    """
    
    objectives: Optional[List] = pla.Field(nullable=True, )
    """
    Information security objectives.
    """
    
    risks_and_opportunities_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to address risks and opportunities determined per Clause 6.1.1, including how they are integrated into ISMS processes and how their effectiveness is evaluated.
    """
    
    planned_changes: Optional[str] = pla.Field(nullable=True, )
    """
    Changes to the ISMS planned and controlled per Clause 6.3 and 8.1 (planning of changes; control of planned changes).
    """
    
    externally_provided_services: Optional[str] = pla.Field(nullable=True, )
    """
    Externally provided processes, products or services relevant to the ISMS that are controlled per Clause 8.1.
    """
    
    risk_assessment_process: Optional[ID_TYPES['RiskAssessmentProcess']] = pla.Field(nullable=True, )
    """
    Reference to the risk assessment process.
    """
    
    risk_treatment_process: Optional[ID_TYPES['RiskTreatmentProcess']] = pla.Field(nullable=True, )
    """
    Reference to the risk treatment process.
    """
    
    statement_of_applicability: Optional[ID_TYPES['StatementOfApplicability']] = pla.Field(nullable=True, )
    """
    Reference to the Statement of Applicability.
    """
    
    controls: Optional[List] = pla.Field(nullable=True, )
    """
    Security controls applied in the ISMS.
    """
    
    roles: Optional[List] = pla.Field(nullable=True, )
    """
    Information security roles defined in the ISMS.
    """
    
    resources: Optional[List] = pla.Field(nullable=True, )
    """
    Resources provided for the ISMS.
    """
    
    competence_records: Optional[List] = pla.Field(nullable=True, )
    """
    Competence records for personnel.
    """
    
    awareness_program: Optional[ID_TYPES['AwarenessProgram']] = pla.Field(nullable=True, )
    """
    Reference to the awareness program.
    """
    
    communication_plan: Optional[ID_TYPES['CommunicationPlan']] = pla.Field(nullable=True, )
    """
    Reference to the communication plan.
    """
    
    documented_information_register: Optional[List] = pla.Field(nullable=True, )
    """
    Register of documented information.
    """
    
    operational_procedures: Optional[List] = pla.Field(nullable=True, )
    """
    Operational procedures.
    """
    
    risk_assessments: Optional[List] = pla.Field(nullable=True, )
    """
    Risk assessment instances.
    """
    
    risk_treatment_plans: Optional[List] = pla.Field(nullable=True, )
    """
    Risk treatment plans.
    """
    
    monitoring_program: Optional[ID_TYPES['MonitoringProgram']] = pla.Field(nullable=True, )
    """
    Reference to the monitoring program.
    """
    
    internal_audits: Optional[List] = pla.Field(nullable=True, )
    """
    Internal audit instances.
    """
    
    management_reviews: Optional[List] = pla.Field(nullable=True, )
    """
    Management review instances.
    """
    
    nonconformities: Optional[List] = pla.Field(nullable=True, )
    """
    Nonconformities identified.
    """
    
    corrective_actions: Optional[List] = pla.Field(nullable=True, )
    """
    Corrective actions.
    """
    
    improvements: Optional[List] = pla.Field(nullable=True, )
    """
    Improvement opportunities tracked.
    """
    
    certification_status: Optional[str] = pla.Field(nullable=True, )
    """
    Current certification status.
    """
    
    certification_body: Optional[str] = pla.Field(nullable=True, )
    """
    Accredited certification body.
    """
    
    certification_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date certification was achieved.
    """
    
    recertification_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date recertification is due.
    """
    
    
class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
    """

    _id_name : str =  'id' 
    document_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('policy','procedure','standard','guideline','record','plan','report',)})
    """
    Classification of the documented information.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    Unique reference number for document control.
    """
    
    author: Optional[str] = pla.Field(nullable=True, )
    """
    Person who created the document.
    """
    
    owner: Optional[str] = pla.Field(nullable=True, )
    """
    Person accountable for the document content and maintenance.
    """
    
    approved_by: Optional[str] = pla.Field(nullable=True, )
    """
    Person who approved the document.
    """
    
    approved_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the document was approved.
    """
    
    effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the document becomes effective.
    """
    
    review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the document is due for review.
    """
    
    status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of the document or entity.
    """
    
    classification: Optional[str] = pla.Field(nullable=True, )
    """
    Information classification level.
    """
    
    retention_period: Optional[str] = pla.Field(nullable=True, )
    """
    Duration for which the document is retained.
    """
    
    distribution_controls: Optional[str] = pla.Field(nullable=True, )
    """
    Controls governing distribution, access, retrieval and use of the documented information, per Clause 7.5.3 c).
    """
    
    storage_and_preservation: Optional[str] = pla.Field(nullable=True, )
    """
    Arrangements for storage and preservation (including preservation of legibility) of the documented information, per Clause 7.5.3 d).
    """
    
    change_control_method: Optional[str] = pla.Field(nullable=True, )
    """
    Method used for control of changes (e.g., version control) of the documented information, per Clause 7.5.3 e).
    """
    
    external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the documented information is of external origin and has been identified as necessary for the planning and operation of the ISMS, per Clause 7.5.3.
    """
    
    external_origin_source: Optional[str] = pla.Field(nullable=True, )
    """
    Source or provider of the externally originated documented information, per Clause 7.5.3.
    """
    
    
class InformationSecurityPolicy(DocumentedInformation):
    """
    The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
    """

    _id_name : str =  'id' 
    policy_statement: Optional[str] = pla.Field(nullable=True, )
    """
    The core policy statement text.
    """
    
    policy_objectives_framework: Optional[str] = pla.Field(nullable=True, )
    """
    Framework for setting information security objectives.
    """
    
    commitment_statements: Optional[str] = pla.Field(nullable=True, )
    """
    Statements of commitment included in the policy.
    """
    
    applicability_statement: Optional[str] = pla.Field(nullable=True, )
    """
    Statement of policy applicability.
    """
    
    communication_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when the policy was communicated.
    """
    
    acknowledgment_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether acknowledgment is required from personnel.
    """
    
    last_policy_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date of the most recent information security policy review.
    """
    
    next_policy_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Planned date of the next information security policy review.
    """
    
    related_topic_policies: Optional[List] = pla.Field(nullable=True, )
    """
    Topic-specific policies supporting this policy.
    """
    
    integrated_management_systems: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('iso_iec_27001','iso_iec_27701','iso_iec_27017','iso_iec_27018','iso_iec_42001','iso_9001','iso_14001','iso_22301','iso_iec_20000_1','iso_31000',)})
    """
    Other ISO/IEC management system standards with which the ISMS is integrated or aligned (per the harmonized structure of Annex SL).
    """
    
    
class TopicSpecificPolicy(DocumentedInformation):
    """
    A policy addressing a specific information security topic, supporting the overarching information security policy.
    """

    _id_name : str =  'id' 
    topic_area: Optional[str] = pla.Field(nullable=True, )
    """
    The specific topic addressed by the policy.
    """
    
    parent_policy: Optional[ID_TYPES['InformationSecurityPolicy']] = pla.Field(nullable=True, )
    """
    The parent policy this topic-specific policy supports.
    """
    
    applicable_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Controls related to this policy.
    """
    
    target_audience: Optional[str] = pla.Field(nullable=True, )
    """
    Intended audience for the policy or document.
    """
    
    
class InformationSecurityObjective(NamedEntity):
    """
    A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
    """

    _id_name : str =  'id' 
    objective_statement: Optional[str] = pla.Field(nullable=True, )
    """
    Clear statement of the objective.
    """
    
    target_value: Optional[str] = pla.Field(nullable=True, )
    """
    Target value for the objective metric.
    """
    
    current_value: Optional[str] = pla.Field(nullable=True, )
    """
    Current measured value.
    """
    
    metric_definition: Optional[str] = pla.Field(nullable=True, )
    """
    Definition of how the objective is measured.
    """
    
    measurement_method: Optional[str] = pla.Field(nullable=True, )
    """
    Method used to measure the metric.
    """
    
    measurement_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often measurement is performed.
    """
    
    responsible_role: Optional[ID_TYPES['Role']] = pla.Field(nullable=True, )
    """
    Role responsible for the objective or control.
    """
    
    target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Target date for achieving the objective.
    """
    
    achievement_status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of objective achievement.
    """
    
    related_risks: Optional[List] = pla.Field(nullable=True, )
    """
    Associated risks.
    """
    
    related_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Other controls related to this one.
    """
    
    action_plan: Optional[str] = pla.Field(nullable=True, )
    """
    Plan for achieving the objective.
    """
    
    objective_resources_required: Optional[str] = pla.Field(nullable=True, )
    """
    Resources required to achieve the information security objective.
    """
    
    
class RiskAssessment(DocumentedInformation):
    """
    An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
    """

    _id_name : str =  'id' 
    assessment_scope: Optional[str] = pla.Field(nullable=True, )
    """
    Scope of the assessment.
    """
    
    assessment_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the assessment was conducted.
    """
    
    assessor: Optional[str] = pla.Field(nullable=True, )
    """
    Person or team who conducted the assessment.
    """
    
    methodology_used: Optional[str] = pla.Field(nullable=True, )
    """
    Specific methodology applied in this assessment.
    """
    
    risks_identified: Optional[List] = pla.Field(nullable=True, )
    """
    Risks identified in this assessment.
    """
    
    summary_findings: Optional[str] = pla.Field(nullable=True, )
    """
    Summary of assessment findings.
    """
    
    recommendations: Optional[str] = pla.Field(nullable=True, )
    """
    Recommendations from the assessment.
    """
    
    next_assessment_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Planned date for next assessment.
    """
    
    
class Risk(NamedEntity):
    """
    An identified information security risk that may affect information security properties within the ISMS scope.
    """

    _id_name : str =  'id' 
    risk_source: Optional[str] = pla.Field(nullable=True, )
    """
    Source or origin of the risk.
    """
    
    threat_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the threat exploiting the vulnerability.
    """
    
    vulnerability_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the vulnerability that could be exploited.
    """
    
    affected_assets: Optional[List] = pla.Field(nullable=True, )
    """
    Assets affected by this risk or incident.
    """
    
    affected_cia_properties: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('confidentiality','integrity','availability',)})
    """
    Which CIA properties are affected (confidentiality, integrity, availability).
    """
    
    risk_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Person accountable for managing the risk.
    """
    
    likelihood: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('rare','unlikely','possible','likely','almost_certain',)})
    """
    Assessed likelihood of risk occurrence.
    """
    
    impact: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('negligible','minor','moderate','major','severe',)})
    """
    Assessed impact if risk materializes.
    """
    
    inherent_risk_level: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    Risk level before controls are applied.
    """
    
    existing_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Controls currently in place affecting this risk.
    """
    
    residual_risk_level: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    Risk level after controls are applied.
    """
    
    risk_treatment_option: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('modify','accept','avoid','share',)})
    """
    Selected treatment option for the risk.
    """
    
    treatment_priority: Optional[str] = pla.Field(nullable=True, )
    """
    Priority for treating this risk.
    """
    
    related_treatment_plan: Optional[ID_TYPES['RiskTreatmentPlan']] = pla.Field(nullable=True, )
    """
    Risk treatment plan addressing this risk.
    """
    
    
class RiskTreatmentPlan(DocumentedInformation):
    """
    A risk treatment plan documenting planned actions to address identified risks through selected controls.
    """

    _id_name : str =  'id' 
    plan_scope: Optional[str] = pla.Field(nullable=True, )
    """
    Scope of the plan.
    """
    
    risks_addressed: Optional[List] = pla.Field(nullable=True, )
    """
    Risks addressed by this plan.
    """
    
    treatment_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to be taken for treatment.
    """
    
    controls_to_implement: Optional[List] = pla.Field(nullable=True, )
    """
    Controls to be implemented as part of treatment.
    """
    
    resources_required: Optional[str] = pla.Field(nullable=True, )
    """
    Resources required for implementation.
    """
    
    responsible_parties: Optional[str] = pla.Field(nullable=True, )
    """
    Parties responsible for implementation.
    """
    
    implementation_timeline: Optional[str] = pla.Field(nullable=True, )
    """
    Timeline for implementation.
    """
    
    risk_owner_approval: Optional[str] = pla.Field(nullable=True, )
    """
    Risk owner who approved the plan.
    """
    
    residual_risk_acceptance: Optional[str] = pla.Field(nullable=True, )
    """
    Documentation of residual risk acceptance.
    """
    
    implementation_status: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('not_started','planned','in_progress','implemented','not_applicable',)})
    """
    Current implementation status.
    """
    
    completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date when implementation was completed.
    """
    
    
class SoAEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
    """

    _id_name : str = None
    control_reference: Optional[ID_TYPES['SecurityControl']] = pla.Field(nullable=True, )
    """
    Reference to the control (e.g., A.5.1).
    """
    
    is_applicable: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the control is applicable.
    """
    
    inclusion_justification: Optional[str] = pla.Field(nullable=True, )
    """
    Justification for including the control.
    """
    
    exclusion_justification: Optional[str] = pla.Field(nullable=True, )
    """
    Justification for excluding the control.
    """
    
    implementation_status: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('not_started','planned','in_progress','implemented','not_applicable',)})
    """
    Current implementation status.
    """
    
    implementation_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    Evidence of control implementation.
    """
    
    responsible_role: Optional[ID_TYPES['Role']] = pla.Field(nullable=True, )
    """
    Role responsible for the objective or control.
    """
    
    target_implementation_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Target date for implementing the control.
    """
    
    
class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation state.
    """

    _id_name : str =  'id' 
    soa_entries: Optional[List] = pla.Field(nullable=True, )
    """
    Individual control entries in the SoA.
    """
    
    total_controls: Optional[int] = pla.Field(nullable=True, )
    """
    Total number of controls in scope.
    """
    
    implemented_count: Optional[int] = pla.Field(nullable=True, )
    """
    Number of implemented controls.
    """
    
    planned_count: Optional[int] = pla.Field(nullable=True, )
    """
    Number of controls planned for implementation.
    """
    
    not_applicable_count: Optional[int] = pla.Field(nullable=True, )
    """
    Number of controls marked not applicable.
    """
    
    last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date of last review.
    """
    
    
    @pla.check("soa_entries")
    def check_nested_struct_soa_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SoAEntry, pa_pl.SoAEntryDict)
        
class SecurityControl(NamedEntity):
    """
    A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
    """

    _id_name : str =  'id' 
    control_id: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('a_5_1','a_5_2','a_5_3','a_5_4','a_5_5','a_5_6','a_5_7','a_5_8','a_5_9','a_5_10','a_5_11','a_5_12','a_5_13','a_5_14','a_5_15','a_5_16','a_5_17','a_5_18','a_5_19','a_5_20','a_5_21','a_5_22','a_5_23','a_5_24','a_5_25','a_5_26','a_5_27','a_5_28','a_5_29','a_5_30','a_5_31','a_5_32','a_5_33','a_5_34','a_5_35','a_5_36','a_5_37','a_6_1','a_6_2','a_6_3','a_6_4','a_6_5','a_6_6','a_6_7','a_6_8','a_7_1','a_7_2','a_7_3','a_7_4','a_7_5','a_7_6','a_7_7','a_7_8','a_7_9','a_7_10','a_7_11','a_7_12','a_7_13','a_7_14','a_8_1','a_8_2','a_8_3','a_8_4','a_8_5','a_8_6','a_8_7','a_8_8','a_8_9','a_8_10','a_8_11','a_8_12','a_8_13','a_8_14','a_8_15','a_8_16','a_8_17','a_8_18','a_8_19','a_8_20','a_8_21','a_8_22','a_8_23','a_8_24','a_8_25','a_8_26','a_8_27','a_8_28','a_8_29','a_8_30','a_8_31','a_8_32','a_8_33','a_8_34',)})
    """
    Control identifier from Annex A (e.g., a_5_1, a_8_24).
    """
    
    control_title: Optional[str] = pla.Field(nullable=True, )
    """
    Title of the control.
    """
    
    control_category: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('organizational','people','physical','technological',)})
    """
    Domain category of the control.
    """
    
    control_text: Optional[str] = pla.Field(nullable=True, )
    """
    Organization-authored control statement or external control summary.
    """
    
    implementation_guidance: Optional[str] = pla.Field(nullable=True, )
    """
    Organization-authored implementation notes for the control.
    """
    
    related_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Other controls related to this one.
    """
    
    applicable_threats: Optional[str] = pla.Field(nullable=True, )
    """
    Threats this control addresses.
    """
    
    applicable_assets: Optional[str] = pla.Field(nullable=True, )
    """
    Asset types this control applies to.
    """
    
    control_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Person responsible for the control.
    """
    
    implementation_status: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('not_started','planned','in_progress','implemented','not_applicable',)})
    """
    Current implementation status.
    """
    
    implementation_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the control was implemented.
    """
    
    effectiveness_rating: Optional[str] = pla.Field(nullable=True, )
    """
    Rating of control effectiveness.
    """
    
    last_test_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the control was last tested.
    """
    
    evidence_references: Optional[str] = pla.Field(nullable=True, )
    """
    References to evidence of implementation.
    """
    
    
class CommunicationItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single communication requirement within the communication plan.
    """

    _id_name : str = None
    subject: Optional[str] = pla.Field(nullable=True, )
    """
    Subject of the communication.
    """
    
    purpose: Optional[str] = pla.Field(nullable=True, )
    """
    Purpose of the communication.
    """
    
    audience: Optional[str] = pla.Field(nullable=True, )
    """
    Target audience.
    """
    
    frequency: Optional[str] = pla.Field(nullable=True, )
    """
    Frequency of the activity.
    """
    
    method: Optional[str] = pla.Field(nullable=True, )
    """
    Method of communication.
    """
    
    responsible_party: Optional[str] = pla.Field(nullable=True, )
    """
    Party responsible for the activity.
    """
    
    records_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether records are required.
    """
    
    
class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the ISMS per Clause 7.4.
    """

    _id_name : str =  'id' 
    communication_items: Optional[List] = pla.Field(nullable=True, )
    """
    Communication items in the plan.
    """
    
    
    @pla.check("communication_items")
    def check_nested_struct_communication_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, CommunicationItem, pa_pl.CommunicationItemDict)
        
class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control per Clause 8.1.
    """

    _id_name : str =  'id' 
    procedure_scope: Optional[str] = pla.Field(nullable=True, )
    """
    Scope of the procedure.
    """
    
    process_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria established for the process.
    """
    
    control_measures: Optional[str] = pla.Field(nullable=True, )
    """
    Control measures implemented.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Roles responsible for the procedure.
    """
    
    related_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Other controls related to this one.
    """
    
    change_control_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Requirements for controlling changes.
    """
    
    
class MonitoringItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single item to be monitored and measured per 9.1.
    """

    _id_name : str = None
    metric_name: Optional[str] = pla.Field(nullable=True, )
    """
    Name of the metric.
    """
    
    metric_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of what is measured.
    """
    
    measurement_method: Optional[str] = pla.Field(nullable=True, )
    """
    Method used to measure the metric.
    """
    
    measurement_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often measurement is performed.
    """
    
    responsible_party: Optional[str] = pla.Field(nullable=True, )
    """
    Party responsible for the activity.
    """
    
    analysis_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often analysis is performed.
    """
    
    analyst: Optional[str] = pla.Field(nullable=True, )
    """
    Person performing analysis.
    """
    
    target_threshold: Optional[str] = pla.Field(nullable=True, )
    """
    Target threshold value.
    """
    
    alert_threshold: Optional[str] = pla.Field(nullable=True, )
    """
    Threshold triggering alerts.
    """
    
    current_value: Optional[str] = pla.Field(nullable=True, )
    """
    Current measured value.
    """
    
    trend: Optional[str] = pla.Field(nullable=True, )
    """
    Current trend direction.
    """
    
    
class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
    """

    _id_name : str =  'id' 
    monitoring_items: Optional[List] = pla.Field(nullable=True, )
    """
    Items to be monitored.
    """
    
    
    @pla.check("monitoring_items")
    def check_nested_struct_monitoring_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MonitoringItem, pa_pl.MonitoringItemDict)
        
class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
    """

    _id_name : str =  'id' 
    audit_reference: Optional[str] = pla.Field(nullable=True, )
    """
    Reference identifier for the audit.
    """
    
    audit_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('internal','external_second_party','external_third_party','surveillance','recertification','combined',)})
    """
    Type of audit per ISO/IEC 27001:2022 Clause 9.2 and ISO/IEC 17021-1.
    """
    
    audit_scope: Optional[str] = pla.Field(nullable=True, )
    """
    Scope of the audit.
    """
    
    audit_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria against which audit is conducted.
    """
    
    audit_objectives: Optional[str] = pla.Field(nullable=True, )
    """
    Objectives of the audit.
    """
    
    audit_period_start: Optional[Date] = pla.Field(nullable=True, )
    """
    Start date of audit period.
    """
    
    audit_period_end: Optional[Date] = pla.Field(nullable=True, )
    """
    End date of audit period.
    """
    
    lead_auditor: Optional[str] = pla.Field(nullable=True, )
    """
    Lead auditor for the audit.
    """
    
    audit_team: Optional[str] = pla.Field(nullable=True, )
    """
    Audit team members.
    """
    
    auditee_representatives: Optional[str] = pla.Field(nullable=True, )
    """
    Representatives from audited areas.
    """
    
    audit_plan: Optional[str] = pla.Field(nullable=True, )
    """
    Audit plan document reference.
    """
    
    findings: Optional[List] = pla.Field(nullable=True, )
    """
    Audit findings.
    """
    
    positive_observations: Optional[str] = pla.Field(nullable=True, )
    """
    Positive observations noted.
    """
    
    audit_conclusion: Optional[str] = pla.Field(nullable=True, )
    """
    Overall audit conclusion.
    """
    
    report_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the report was issued.
    """
    
    report_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    Distribution list for the report.
    """
    
    
class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per 9.2.2, planning audit activities over a defined period.
    """

    _id_name : str =  'id' 
    programme_period: Optional[str] = pla.Field(nullable=True, )
    """
    Period covered by the audit programme.
    """
    
    planned_audits: Optional[List] = pla.Field(nullable=True, )
    """
    Audits planned in this programme.
    """
    
    audit_frequency_rationale: Optional[str] = pla.Field(nullable=True, )
    """
    Rationale for audit frequency decisions.
    """
    
    resource_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Resource requirements for the programme.
    """
    
    auditor_qualifications: Optional[str] = pla.Field(nullable=True, )
    """
    Required qualifications for auditors.
    """
    
    programme_status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of the programme.
    """
    
    
class AuditFinding(NamedEntity):
    """
    A finding from an internal audit, including nonconformities, observations, and positive findings.
    """

    _id_name : str =  'id' 
    finding_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('major_nonconformity','minor_nonconformity','observation','positive_finding',)})
    """
    Type of audit finding.
    """
    
    clause_reference: Optional[str] = pla.Field(nullable=True, )
    """
    Reference to standard clause.
    """
    
    control_reference: Optional[ID_TYPES['SecurityControl']] = pla.Field(nullable=True, )
    """
    Reference to the control (e.g., A.5.1).
    """
    
    finding_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the finding.
    """
    
    objective_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    Evidence supporting the finding.
    """
    
    root_cause_analysis: Optional[str] = pla.Field(nullable=True, )
    """
    Analysis of root cause.
    """
    
    risk_implication: Optional[str] = pla.Field(nullable=True, )
    """
    Risk implications of the finding.
    """
    
    recommended_action: Optional[str] = pla.Field(nullable=True, )
    """
    Recommended action to address finding.
    """
    
    auditee_response: Optional[str] = pla.Field(nullable=True, )
    """
    Response from the auditee.
    """
    
    linked_corrective_action: Optional[ID_TYPES['CorrectiveAction']] = pla.Field(nullable=True, )
    """
    Corrective action linked to this finding.
    """
    
    closure_status: Optional[str] = pla.Field(nullable=True, )
    """
    Status of finding closure.
    """
    
    closure_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the finding was closed.
    """
    
    
class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
    """

    _id_name : str =  'id' 
    nonconformity_source: Optional[str] = pla.Field(nullable=True, )
    """
    Source of nonconformity detection.
    """
    
    detection_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the nonconformity was detected.
    """
    
    detected_by: Optional[str] = pla.Field(nullable=True, )
    """
    Person or process that detected the nonconformity.
    """
    
    requirement_violated: Optional[str] = pla.Field(nullable=True, )
    """
    Requirement that was not fulfilled.
    """
    
    nonconformity_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the nonconformity.
    """
    
    immediate_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Immediate actions taken to control/correct.
    """
    
    consequences_addressed: Optional[str] = pla.Field(nullable=True, )
    """
    How consequences were dealt with.
    """
    
    root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    Root cause of the nonconformity.
    """
    
    similar_nonconformities_check: Optional[str] = pla.Field(nullable=True, )
    """
    Check for similar nonconformities elsewhere.
    """
    
    linked_corrective_actions: Optional[List] = pla.Field(nullable=True, )
    """
    Corrective actions addressing this nonconformity.
    """
    
    status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of the document or entity.
    """
    
    closure_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the finding was closed.
    """
    
    closure_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    Evidence supporting closure.
    """
    
    
class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of recurrence.
    """

    _id_name : str =  'id' 
    linked_nonconformity: Optional[ID_TYPES['Nonconformity']] = pla.Field(nullable=True, )
    """
    Nonconformity this action addresses.
    """
    
    action_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the action.
    """
    
    root_cause_addressed: Optional[str] = pla.Field(nullable=True, )
    """
    Root cause this action addresses.
    """
    
    responsible_party: Optional[str] = pla.Field(nullable=True, )
    """
    Party responsible for the activity.
    """
    
    target_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Target date for completing the action.
    """
    
    actual_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Actual date the action was completed.
    """
    
    resources_required: Optional[str] = pla.Field(nullable=True, )
    """
    Resources required for implementation.
    """
    
    effectiveness_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria for evaluating effectiveness.
    """
    
    effectiveness_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date effectiveness was reviewed.
    """
    
    effectiveness_verified: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether effectiveness was verified.
    """
    
    isms_changes_required: Optional[str] = pla.Field(nullable=True, )
    """
    Changes to ISMS required as a result.
    """
    
    status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of the document or entity.
    """
    
    
class Asset(NamedEntity):
    """
    An information asset or associated asset requiring protection, per Annex A control 5.9.
    """

    _id_name : str =  'id' 
    asset_type: Optional[str] = pla.Field(nullable=True, )
    """
    Type of asset.
    """
    
    asset_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Owner of the asset.
    """
    
    asset_custodian: Optional[str] = pla.Field(nullable=True, )
    """
    Custodian responsible for day-to-day protection.
    """
    
    classification: Optional[str] = pla.Field(nullable=True, )
    """
    Information classification level.
    """
    
    location: Optional[str] = pla.Field(nullable=True, )
    """
    Physical or logical location.
    """
    
    criticality: Optional[str] = pla.Field(nullable=True, )
    """
    Criticality rating of the asset.
    """
    
    related_risks: Optional[List] = pla.Field(nullable=True, )
    """
    Associated risks.
    """
    
    applicable_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Controls related to this policy.
    """
    
    
class InformationSecurityEvent(NamedEntity):
    """
    An information security event per A.5.25, which may or may not be categorized as an incident.
    """

    _id_name : str =  'id' 
    event_datetime: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    Date and time of the event.
    """
    
    reporter: Optional[str] = pla.Field(nullable=True, )
    """
    Person who reported the event.
    """
    
    event_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the event.
    """
    
    affected_assets: Optional[List] = pla.Field(nullable=True, )
    """
    Assets affected by this risk or incident.
    """
    
    initial_assessment: Optional[str] = pla.Field(nullable=True, )
    """
    Initial assessment of the event.
    """
    
    categorized_as_incident: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the event was categorized as an incident.
    """
    
    linked_incident: Optional[ID_TYPES['InformationSecurityIncident']] = pla.Field(nullable=True, )
    """
    Linked incident if categorized.
    """
    
    
class InformationSecurityIncident(NamedEntity):
    """
    An information security incident per A.5.26, requiring response per documented procedures.
    """

    _id_name : str =  'id' 
    incident_datetime: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    Date and time the incident occurred or was detected.
    """
    
    incident_category: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('malware','ransomware','phishing','social_engineering','unauthorized_access','account_compromise','privilege_misuse','data_breach','data_loss','denial_of_service','web_application_attack','supply_chain','insider_threat','physical_security','configuration_error','cryptographic_failure','policy_violation','other',)})
    """
    Category of incident.
    """
    
    severity: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    Severity rating of the incident.
    """
    
    affected_assets: Optional[List] = pla.Field(nullable=True, )
    """
    Assets affected by this risk or incident.
    """
    
    affected_cia: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('confidentiality','integrity','availability',)})
    """
    CIA properties affected by the incident.
    """
    
    incident_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the incident.
    """
    
    detection_method: Optional[str] = pla.Field(nullable=True, )
    """
    How the incident was detected.
    """
    
    response_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions taken in response.
    """
    
    containment_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to contain the incident.
    """
    
    eradication_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to eradicate the cause.
    """
    
    recovery_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to recover normal operations.
    """
    
    root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    Root cause of the nonconformity.
    """
    
    lessons_learned: Optional[str] = pla.Field(nullable=True, )
    """
    Lessons learned from the incident.
    """
    
    evidence_collected: Optional[str] = pla.Field(nullable=True, )
    """
    Evidence collected.
    """
    
    notification_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether notification to authorities/parties was required.
    """
    
    notifications_made: Optional[str] = pla.Field(nullable=True, )
    """
    Notifications that were made.
    """
    
    closure_datetime: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    Date and time of incident closure.
    """
    
    post_incident_review: Optional[str] = pla.Field(nullable=True, )
    """
    Post-incident review findings.
    """
    
    
class Organization(NamedEntity):
    """
    The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
    """

    _id_name : str =  'id' 
    legal_name: Optional[str] = pla.Field(nullable=True, )
    """
    Legal registered name of the organization.
    """
    
    trading_names: Optional[str] = pla.Field(nullable=True, )
    """
    Names under which the organization conducts business.
    """
    
    organization_type: Optional[str] = pla.Field(nullable=True, )
    """
    Type of organization (e.g., corporation, government, nonprofit).
    """
    
    industry_sector: Optional[str] = pla.Field(nullable=True, )
    """
    Primary industry sector of the organization.
    """
    
    size_category: Optional[str] = pla.Field(nullable=True, )
    """
    Organization size classification.
    """
    
    employee_count: Optional[int] = pla.Field(nullable=True, )
    """
    Approximate number of employees.
    """
    
    geographic_locations: Optional[str] = pla.Field(nullable=True, )
    """
    Countries or regions where the organization operates.
    """
    
    regulatory_jurisdictions: Optional[str] = pla.Field(nullable=True, )
    """
    Jurisdictions whose regulations apply to the organization.
    """
    
    parent_organization: Optional[str] = pla.Field(nullable=True, )
    """
    Parent organization if applicable.
    """
    
    subsidiaries: Optional[str] = pla.Field(nullable=True, )
    """
    Subsidiary organizations if applicable.
    """
    
    climate_change_relevant: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether climate change has been determined to be a relevant issue for the organization's context, per Clause 4.1 as amended by Amd. 1:2024.
    """
    
    
class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
    """

    _id_name : str =  'id' 
    party_type: Optional[str] = pla.Field(nullable=True, )
    """
    Category of interested party.
    """
    
    relationship: Optional[str] = pla.Field(nullable=True, )
    """
    Nature of the relationship with the organization.
    """
    
    requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Requirements of the interested party.
    """
    
    addressed_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Requirements of the interested party that the organization has determined will be addressed through the ISMS, per Clause 4.2 c).
    """
    
    climate_change_related_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Climate-change-related requirements of the interested party, per ISO/IEC 27001:2022 Clause 4.2 NOTE 2 as added by Amd. 1:2024.
    """
    
    communication_needs: Optional[str] = pla.Field(nullable=True, )
    """
    Communication requirements for this party.
    """
    
    contact_information: Optional[str] = pla.Field(nullable=True, )
    """
    Contact details for the party.
    """
    
    
class Role(NamedEntity):
    """
    An information security role with defined responsibilities and authorities per Clause 5.3.
    """

    _id_name : str =  'id' 
    role_type: Optional[str] = pla.Field(nullable=True, )
    """
    Category of the role.
    """
    
    responsibilities: Optional[str] = pla.Field(nullable=True, )
    """
    Responsibilities assigned to the role.
    """
    
    authorities: Optional[str] = pla.Field(nullable=True, )
    """
    Authorities granted to the role.
    """
    
    accountability: Optional[str] = pla.Field(nullable=True, )
    """
    What the role is accountable for.
    """
    
    assigned_to: Optional[str] = pla.Field(nullable=True, )
    """
    Person(s) assigned to this role.
    """
    
    delegation_rules: Optional[str] = pla.Field(nullable=True, )
    """
    Rules for delegating responsibilities.
    """
    
    reporting_line: Optional[str] = pla.Field(nullable=True, )
    """
    To whom this role reports.
    """
    
    
class RiskAssessmentProcess(DocumentedInformation):
    """
    The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
    """

    _id_name : str =  'id' 
    risk_acceptance_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria for accepting risks.
    """
    
    assessment_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria for performing risk assessments.
    """
    
    assessment_methodology: Optional[str] = pla.Field(nullable=True, )
    """
    Methodology used for risk assessment.
    """
    
    likelihood_scale: Optional[str] = pla.Field(nullable=True, )
    """
    Scale used for likelihood rating.
    """
    
    impact_scale: Optional[str] = pla.Field(nullable=True, )
    """
    Scale used for impact rating.
    """
    
    risk_matrix: Optional[str] = pla.Field(nullable=True, )
    """
    Risk matrix or calculation method.
    """
    
    assessment_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    Planned frequency of risk assessments.
    """
    
    trigger_events: Optional[str] = pla.Field(nullable=True, )
    """
    Events that trigger risk assessment outside planned schedule.
    """
    
    
class RiskTreatmentProcess(DocumentedInformation):
    """
    The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
    """

    _id_name : str =  'id' 
    treatment_options_guidance: Optional[str] = pla.Field(nullable=True, )
    """
    Guidance on selecting treatment options.
    """
    
    control_selection_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    Criteria for selecting controls.
    """
    
    annex_a_omission_verification: Optional[str] = pla.Field(nullable=True, )
    """
    Description of how controls determined as necessary are compared with those in Annex A to verify that no necessary controls have been omitted, per Clause 6.1.3 c).
    """
    
    soa_template: Optional[str] = pla.Field(nullable=True, )
    """
    Template used for Statement of Applicability.
    """
    
    approval_workflow: Optional[str] = pla.Field(nullable=True, )
    """
    Workflow for approving risk treatment.
    """
    
    
class Resource(NamedEntity):
    """
    A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
    """

    _id_name : str =  'id' 
    resource_type: Optional[str] = pla.Field(nullable=True, )
    """
    Type of resource.
    """
    
    quantity: Optional[str] = pla.Field(nullable=True, )
    """
    Quantity of the resource.
    """
    
    allocation_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date the resource was allocated.
    """
    
    allocated_to: Optional[str] = pla.Field(nullable=True, )
    """
    What the resource is allocated to.
    """
    
    cost: Optional[str] = pla.Field(nullable=True, )
    """
    Cost of the resource.
    """
    
    availability_status: Optional[str] = pla.Field(nullable=True, )
    """
    Current availability of the resource.
    """
    
    
class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
    """

    _id_name : str =  'id' 
    person_name: Optional[str] = pla.Field(nullable=True, )
    """
    Name of the person.
    """
    
    person_role: Optional[str] = pla.Field(nullable=True, )
    """
    Role of the person.
    """
    
    required_competencies: Optional[str] = pla.Field(nullable=True, )
    """
    Competencies required for the role.
    """
    
    education_records: Optional[str] = pla.Field(nullable=True, )
    """
    Education qualifications.
    """
    
    training_records: Optional[str] = pla.Field(nullable=True, )
    """
    Training completed.
    """
    
    experience_records: Optional[str] = pla.Field(nullable=True, )
    """
    Relevant experience.
    """
    
    competency_assessment_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date of last competency assessment.
    """
    
    competency_gaps: Optional[str] = pla.Field(nullable=True, )
    """
    Identified competency gaps.
    """
    
    development_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Actions to address competency gaps.
    """
    
    
class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
    """

    _id_name : str =  'id' 
    awareness_topics: Optional[str] = pla.Field(nullable=True, )
    """
    Topics covered in awareness program.
    """
    
    delivery_methods: Optional[str] = pla.Field(nullable=True, )
    """
    Methods used to deliver awareness content.
    """
    
    target_audience: Optional[str] = pla.Field(nullable=True, )
    """
    Intended audience for the policy or document.
    """
    
    frequency: Optional[str] = pla.Field(nullable=True, )
    """
    Frequency of the activity.
    """
    
    completion_tracking: Optional[str] = pla.Field(nullable=True, )
    """
    How completion is tracked.
    """
    
    effectiveness_measures: Optional[str] = pla.Field(nullable=True, )
    """
    How effectiveness is measured.
    """
    
    
class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness for purpose.
    """

    _id_name : str =  'id' 
    attendees: Optional[str] = pla.Field(nullable=True, )
    """
    Attendees of the review.
    """
    
    previous_actions_status: Optional[str] = pla.Field(nullable=True, )
    """
    Status of actions from previous reviews.
    """
    
    context_changes: Optional[str] = pla.Field(nullable=True, )
    """
    Changes in context since last review.
    """
    
    interested_party_changes: Optional[str] = pla.Field(nullable=True, )
    """
    Changes in interested party requirements.
    """
    
    interested_party_feedback: Optional[str] = pla.Field(nullable=True, )
    """
    Feedback from interested parties considered in the management review.
    """
    
    performance_trends: Optional[str] = pla.Field(nullable=True, )
    """
    Trends in information security performance.
    """
    
    audit_results_summary: Optional[str] = pla.Field(nullable=True, )
    """
    Summary of audit results.
    """
    
    risk_assessment_results: Optional[str] = pla.Field(nullable=True, )
    """
    Results of risk assessment.
    """
    
    risk_treatment_status: Optional[str] = pla.Field(nullable=True, )
    """
    Status of the risk treatment plan considered in the management review.
    """
    
    risks_and_opportunities_changes: Optional[str] = pla.Field(nullable=True, )
    """
    Changes in risks and opportunities considered in the management review, per Clause 9.3.2 f).
    """
    
    improvement_opportunities: Optional[str] = pla.Field(nullable=True, )
    """
    Opportunities for improvement identified.
    """
    
    decisions: Optional[str] = pla.Field(nullable=True, )
    """
    Decisions made in the review.
    """
    
    action_items: Optional[str] = pla.Field(nullable=True, )
    """
    Action items from the review.
    """
    
    next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Planned date for next review.
    """
    
    
class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
    """

    _id_name : str =  'id' 
    improvement_source: Optional[str] = pla.Field(nullable=True, )
    """
    Source of the improvement opportunity.
    """
    
    identification_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Date identified.
    """
    
    identified_by: Optional[str] = pla.Field(nullable=True, )
    """
    Person who identified it.
    """
    
    improvement_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the improvement.
    """
    
    expected_benefit: Optional[str] = pla.Field(nullable=True, )
    """
    Expected benefit from implementation.
    """
    
    priority: Optional[str] = pla.Field(nullable=True, )
    """
    Priority level.
    """
    
    implementation_plan: Optional[str] = pla.Field(nullable=True, )
    """
    Plan for implementing the improvement.
    """
    
    responsible_party: Optional[str] = pla.Field(nullable=True, )
    """
    Party responsible for the activity.
    """
    
    target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Target date for achieving the objective.
    """
    
    actual_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Actual date the action was completed.
    """
    
    outcome_assessment: Optional[str] = pla.Field(nullable=True, )
    """
    Assessment of actual outcomes.
    """
    
    status: Optional[str] = pla.Field(nullable=True, )
    """
    Current status of the document or entity.
    """
    
    

