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
    "IsmsRecordMixin": "str",
    "IsmsOrganization": "str",
    "IsmsInterestedParty": "str",
    "IsmsDocumentControlMixin": "str",
    "IsmsPolicy": "str",
    "IsmsTopicSpecificPolicy": "str",
    "IsmsRole": "str",
    "IsmsObjective": "str",
    "IsmsRiskAssessmentProcess": "str",
    "IsmsRiskTreatmentProcess": "str",
    "IsmsRiskAssessment": "str",
    "IsmsRisk": "str",
    "IsmsRiskTreatmentPlan": "str",
    "IsmsApplicabilityEntry": "str",
    "IsmsStatementOfApplicability": "str",
    "IsmsControl": "str",
    "IsmsAsset": "str",
    "IsmsResource": "str",
    "IsmsCompetenceRecord": "str",
    "IsmsAwarenessProgramme": "str",
    "IsmsCommunication": "str",
    "IsmsCommunicationPlan": "str",
    "IsmsDocumentedInformation": "str",
    "IsmsOperationalProcedure": "str",
    "IsmsMonitoringItem": "str",
    "IsmsMonitoringProgramme": "str",
    "IsmsAuditProgramme": "str",
    "IsmsAuditFinding": "str",
    "IsmsAudit": "str",
    "IsmsManagementReview": "str",
    "IsmsNonconformity": "str",
    "IsmsCorrectiveAction": "str",
    "IsmsImprovementOpportunity": "str",
    "IsmsSecurityEvent": "str",
    "IsmsManagementSystem": "str",
    "IsmsIncludedControl": "str",
    "IsmsSecurityIncident": "str",
    "IsmsExcludedControl": "str",
}

# metamodel_version: 1.12.0
# version: 2022/Amd 1:2024class IsmsRecordMixin(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    What every record of the ISMS has, so that other records can refer to it: an identifier, a title and a description.
    """

    _id_name : str =  'isms_id' 
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsOrganization(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The organization that runs the ISMS, with what it needs to know about itself to understand its context.
    """

    _id_name : str =  'isms_id' 
    organization_legal_name: Optional[str] = pla.Field(nullable=True, )
    """
    The organization's registered legal name.
    """
    
    organization_trading_names: Optional[str] = pla.Field(nullable=True, )
    """
    Other names the organization trades under.
    """
    
    organization_kind: Optional[str] = pla.Field(nullable=True, )
    """
    What kind of organization it is, such as a company, an agency or a charity.
    """
    
    organization_sector: Optional[str] = pla.Field(nullable=True, )
    """
    The organization's main industry sector.
    """
    
    organization_size: Optional[str] = pla.Field(nullable=True, )
    """
    How the organization classes its own size.
    """
    
    organization_employee_count: Optional[int] = pla.Field(ge=1, nullable=True, )
    """
    About how many people the organization employs.
    """
    
    organization_locations: Optional[str] = pla.Field(nullable=True, )
    """
    The countries or regions the organization works in.
    """
    
    organization_jurisdictions: Optional[str] = pla.Field(nullable=True, )
    """
    The jurisdictions whose laws and regulations apply to the organization.
    """
    
    organization_parent: Optional[str] = pla.Field(nullable=True, )
    """
    The organization's parent, if it has one.
    """
    
    organization_subsidiaries: Optional[str] = pla.Field(nullable=True, )
    """
    The organization's subsidiaries, if it has any.
    """
    
    organization_climate_change_relevant: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the organization has determined that climate change is a relevant issue for its ISMS.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsInterestedParty(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
    """

    _id_name : str =  'isms_id' 
    party_category: Optional[str] = pla.Field(nullable=True, )
    """
    What kind of interested party it is, in the organization's own terms.
    """
    
    party_relationship: Optional[str] = pla.Field(nullable=True, )
    """
    How the party relates to the organization.
    """
    
    party_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    The party's requirements that bear on information security.
    """
    
    party_addressed_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    Which of those requirements the ISMS addresses.
    """
    
    party_climate_change_requirements: Optional[str] = pla.Field(nullable=True, )
    """
    The party's requirements that concern climate change.
    """
    
    party_communication_needs: Optional[str] = pla.Field(nullable=True, )
    """
    What the party needs to be told, and how.
    """
    
    party_contact: Optional[str] = pla.Field(nullable=True, )
    """
    How to reach the party.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsDocumentControlMixin(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The control that documented information is kept under: who wrote, owns and approved it, when it takes effect and is reviewed, how it is classified, distributed, stored and changed, how long it is retained, and whether it came from outside the organization.
    """

    _id_name : str = None
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsPolicy(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The information security policy that top management sets: the organization's commitment and the frame for its information security objectives.
    """

    _id_name : str =  'isms_id' 
    policy_statement: Optional[str] = pla.Field(nullable=True, )
    """
    The policy's own statement, in the organization's words.
    """
    
    policy_objectives_framework: Optional[str] = pla.Field(nullable=True, )
    """
    How the policy frames the setting of information security objectives.
    """
    
    policy_commitments: Optional[str] = pla.Field(nullable=True, )
    """
    The commitments the policy makes.
    """
    
    policy_applicability: Optional[str] = pla.Field(nullable=True, )
    """
    To whom and to what the policy applies.
    """
    
    policy_communication_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the policy was communicated within the organization.
    """
    
    policy_acknowledgement_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether staff must acknowledge the policy.
    """
    
    policy_management_systems: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('iso_iec_27001','iso_iec_27701','iso_iec_42001','iso_9001','iso_14001','iso_22301','iso_iec_20000_1',)})
    """
    The other management system standards the ISMS is integrated with under the same policy.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsTopicSpecificPolicy(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A policy on one topic of information security, such as access control or backup, that supports the information security policy.
    """

    _id_name : str =  'isms_id' 
    relevant_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls that the record concerns.
    """
    
    topic_policy_topic: Optional[str] = pla.Field(nullable=True, )
    """
    The topic the policy covers.
    """
    
    topic_policy_parent: Optional[ID_TYPES['IsmsPolicy']] = pla.Field(nullable=True, )
    """
    The information security policy this policy supports.
    """
    
    topic_policy_audience: Optional[str] = pla.Field(nullable=True, )
    """
    Whom the policy is written for.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsRole(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
    """

    _id_name : str =  'isms_id' 
    role_category: Optional[str] = pla.Field(nullable=True, )
    """
    What kind of role it is, in the organization's own terms.
    """
    
    role_responsibilities: Optional[str] = pla.Field(nullable=True, )
    """
    The responsibilities assigned to the role.
    """
    
    role_authorities: Optional[str] = pla.Field(nullable=True, )
    """
    The authorities the role carries.
    """
    
    role_accountability: Optional[str] = pla.Field(nullable=True, )
    """
    What the role is accountable for.
    """
    
    role_holders: Optional[str] = pla.Field(nullable=True, )
    """
    The people who hold the role.
    """
    
    role_delegation: Optional[str] = pla.Field(nullable=True, )
    """
    How the role may delegate its responsibilities.
    """
    
    role_reports_to: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role this role reports to.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsObjective(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
    """

    _id_name : str =  'isms_id' 
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    relevant_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls that the record concerns.
    """
    
    objective_statement: Optional[str] = pla.Field(nullable=True, )
    """
    The objective, as the organization states it.
    """
    
    objective_target: Optional[str] = pla.Field(nullable=True, )
    """
    The value the objective aims for.
    """
    
    objective_current_value: Optional[str] = pla.Field(nullable=True, )
    """
    The value last measured.
    """
    
    objective_metric: Optional[str] = pla.Field(nullable=True, )
    """
    How the objective's value is defined.
    """
    
    objective_measurement_method: Optional[str] = pla.Field(nullable=True, )
    """
    How the value is measured.
    """
    
    objective_measurement_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often the value is measured.
    """
    
    objective_target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the objective is to be reached.
    """
    
    objective_achievement: Optional[str] = pla.Field(nullable=True, )
    """
    How far the objective has been reached, in the organization's own terms.
    """
    
    objective_risks: Optional[List] = pla.Field(nullable=True, )
    """
    The risks the objective concerns.
    """
    
    objective_action_plan: Optional[str] = pla.Field(nullable=True, )
    """
    What will be done to reach the objective.
    """
    
    objective_resources: Optional[str] = pla.Field(nullable=True, )
    """
    The resources needed to reach the objective.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsRiskAssessmentProcess(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
    """

    _id_name : str =  'isms_id' 
    risk_acceptance_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    The criteria for accepting a risk.
    """
    
    risk_assessment_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    The criteria for carrying out a risk assessment.
    """
    
    risk_assessment_method: Optional[str] = pla.Field(nullable=True, )
    """
    The method used to identify, analyse and evaluate risks.
    """
    
    risk_likelihood_scale: Optional[str] = pla.Field(nullable=True, )
    """
    The scale for rating likelihood.
    """
    
    risk_impact_scale: Optional[str] = pla.Field(nullable=True, )
    """
    The scale for rating consequences.
    """
    
    risk_matrix: Optional[str] = pla.Field(nullable=True, )
    """
    How likelihood and consequence combine into a risk level.
    """
    
    risk_assessment_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often risks are assessed.
    """
    
    risk_assessment_triggers: Optional[str] = pla.Field(nullable=True, )
    """
    The events that start a risk assessment outside the planned ones.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsRiskTreatmentProcess(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
    """

    _id_name : str =  'isms_id' 
    treatment_options_guidance: Optional[str] = pla.Field(nullable=True, )
    """
    How a treatment option is chosen for a risk.
    """
    
    treatment_control_selection: Optional[str] = pla.Field(nullable=True, )
    """
    How the controls a treatment needs are chosen.
    """
    
    treatment_annex_a_comparison: Optional[str] = pla.Field(nullable=True, )
    """
    How the chosen controls are compared with Annex A, so that no necessary control is left out.
    """
    
    treatment_soa_template: Optional[str] = pla.Field(nullable=True, )
    """
    The template the Statement of Applicability follows.
    """
    
    treatment_approval_workflow: Optional[str] = pla.Field(nullable=True, )
    """
    How a treatment plan and its residual risks are approved.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsRiskAssessment(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One risk assessment carried out under the risk assessment process, and what it found.
    """

    _id_name : str =  'isms_id' 
    assessment_scope: Optional[str] = pla.Field(nullable=True, )
    """
    What the assessment covered.
    """
    
    assessment_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the assessment was carried out.
    """
    
    assessment_assessor: Optional[str] = pla.Field(nullable=True, )
    """
    Who carried out the assessment.
    """
    
    assessment_method_used: Optional[str] = pla.Field(nullable=True, )
    """
    The method this assessment applied.
    """
    
    assessment_risks: Optional[List] = pla.Field(nullable=True, )
    """
    The risks the assessment identified.
    """
    
    assessment_summary: Optional[str] = pla.Field(nullable=True, )
    """
    A summary of what the assessment found.
    """
    
    assessment_recommendations: Optional[str] = pla.Field(nullable=True, )
    """
    What the assessment recommends.
    """
    
    assessment_next_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the next assessment is planned.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsRisk(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
    """

    _id_name : str =  'isms_id' 
    affected_assets: Optional[List] = pla.Field(nullable=True, )
    """
    The assets the risk, event or incident affects.
    """
    
    affected_security_properties: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('confidentiality','integrity','availability',)})
    """
    Which of confidentiality, integrity and availability the risk or incident threatens.
    """
    
    risk_source: Optional[str] = pla.Field(nullable=True, )
    """
    Where the risk comes from.
    """
    
    risk_threat: Optional[str] = pla.Field(nullable=True, )
    """
    The threat that could cause harm.
    """
    
    risk_vulnerability: Optional[str] = pla.Field(nullable=True, )
    """
    The weakness the threat could exploit.
    """
    
    risk_owner: Optional[str] = pla.Field(nullable=True, )
    """
    The person who is accountable for the risk and has the authority to manage it.
    """
    
    risk_likelihood: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('rare','unlikely','possible','likely','almost_certain',)})
    """
    How likely the risk is.
    """
    
    risk_impact: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('negligible','minor','moderate','major','severe',)})
    """
    How severe the consequences would be.
    """
    
    risk_inherent_level: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    The risk's level before controls.
    """
    
    risk_existing_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls already acting on the risk.
    """
    
    risk_residual_level: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    The risk's level after controls.
    """
    
    risk_treatment_option: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('modify','retain','avoid','share',)})
    """
    The treatment chosen for the risk.
    """
    
    risk_treatment_priority: Optional[str] = pla.Field(nullable=True, )
    """
    How soon the risk is to be treated, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsRiskTreatmentPlan(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
    """

    _id_name : str =  'isms_id' 
    implementation_state: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('not_started','planned','in_progress','implemented',)})
    """
    How far the control or the plan has been put into effect.
    """
    
    plan_scope: Optional[str] = pla.Field(nullable=True, )
    """
    What the plan covers.
    """
    
    plan_risks: Optional[List] = pla.Field(nullable=True, )
    """
    The risks the plan treats.
    """
    
    plan_actions: Optional[str] = pla.Field(nullable=True, )
    """
    The actions the plan takes.
    """
    
    plan_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The controls the plan puts in place.
    """
    
    plan_resources: Optional[str] = pla.Field(nullable=True, )
    """
    The resources the plan needs.
    """
    
    plan_responsible_parties: Optional[str] = pla.Field(nullable=True, )
    """
    Who carries out the plan.
    """
    
    plan_timeline: Optional[str] = pla.Field(nullable=True, )
    """
    When the plan's actions are to happen.
    """
    
    plan_risk_owner_approval: Optional[str] = pla.Field(nullable=True, )
    """
    The risk owner who approved the plan.
    """
    
    plan_residual_risk_acceptance: Optional[str] = pla.Field(nullable=True, )
    """
    How the risk owners accepted the risk that remains.
    """
    
    plan_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the plan was completed.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsApplicabilityEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
    """

    _id_name : str = None
    entry_annex_a_control: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('a_5_1','a_5_2','a_5_3','a_5_4','a_5_5','a_5_6','a_5_7','a_5_8','a_5_9','a_5_10','a_5_11','a_5_12','a_5_13','a_5_14','a_5_15','a_5_16','a_5_17','a_5_18','a_5_19','a_5_20','a_5_21','a_5_22','a_5_23','a_5_24','a_5_25','a_5_26','a_5_27','a_5_28','a_5_29','a_5_30','a_5_31','a_5_32','a_5_33','a_5_34','a_5_35','a_5_36','a_5_37','a_6_1','a_6_2','a_6_3','a_6_4','a_6_5','a_6_6','a_6_7','a_6_8','a_7_1','a_7_2','a_7_3','a_7_4','a_7_5','a_7_6','a_7_7','a_7_8','a_7_9','a_7_10','a_7_11','a_7_12','a_7_13','a_7_14','a_8_1','a_8_2','a_8_3','a_8_4','a_8_5','a_8_6','a_8_7','a_8_8','a_8_9','a_8_10','a_8_11','a_8_12','a_8_13','a_8_14','a_8_15','a_8_16','a_8_17','a_8_18','a_8_19','a_8_20','a_8_21','a_8_22','a_8_23','a_8_24','a_8_25','a_8_26','a_8_27','a_8_28','a_8_29','a_8_30','a_8_31','a_8_32','a_8_33','a_8_34',)})
    """
    The Annex A control a Statement of Applicability entry concerns.
    """
    
    entry_type: Optional[str] = pla.Field(nullable=True, )
    """
    The kind of entry: IsmsIncludedControl or IsmsExcludedControl.
    """
    
    entry_justification: str = pla.Field(str_contains=r"^\s*\S", )
    """
    Why the control is included or excluded.
    """
    
    
class IsmsStatementOfApplicability(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
    """

    _id_name : str =  'isms_id' 
    soa_entries: Optional[List] = pla.Field(nullable=True, )
    """
    The statement's entries, one for each control included or Annex A control excluded.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
    @pla.check("soa_entries")
    def check_nested_struct_soa_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsApplicabilityEntry, pa_pl.IsmsApplicabilityEntryDict)
        
class IsmsControl(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A control the organization has determined it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
    """

    _id_name : str =  'isms_id' 
    relevant_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls that the record concerns.
    """
    
    implementation_state: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('not_started','planned','in_progress','implemented',)})
    """
    How far the control or the plan has been put into effect.
    """
    
    control_annex_a_controls: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('a_5_1','a_5_2','a_5_3','a_5_4','a_5_5','a_5_6','a_5_7','a_5_8','a_5_9','a_5_10','a_5_11','a_5_12','a_5_13','a_5_14','a_5_15','a_5_16','a_5_17','a_5_18','a_5_19','a_5_20','a_5_21','a_5_22','a_5_23','a_5_24','a_5_25','a_5_26','a_5_27','a_5_28','a_5_29','a_5_30','a_5_31','a_5_32','a_5_33','a_5_34','a_5_35','a_5_36','a_5_37','a_6_1','a_6_2','a_6_3','a_6_4','a_6_5','a_6_6','a_6_7','a_6_8','a_7_1','a_7_2','a_7_3','a_7_4','a_7_5','a_7_6','a_7_7','a_7_8','a_7_9','a_7_10','a_7_11','a_7_12','a_7_13','a_7_14','a_8_1','a_8_2','a_8_3','a_8_4','a_8_5','a_8_6','a_8_7','a_8_8','a_8_9','a_8_10','a_8_11','a_8_12','a_8_13','a_8_14','a_8_15','a_8_16','a_8_17','a_8_18','a_8_19','a_8_20','a_8_21','a_8_22','a_8_23','a_8_24','a_8_25','a_8_26','a_8_27','a_8_28','a_8_29','a_8_30','a_8_31','a_8_32','a_8_33','a_8_34',)})
    """
    The Annex A controls the control answers to.
    """
    
    control_theme: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('organizational','people','physical','technological',)})
    """
    Which of Annex A's four themes the control belongs to.
    """
    
    control_text: Optional[str] = pla.Field(nullable=True, )
    """
    What the control does, in the organization's own words.
    """
    
    control_guidance: Optional[str] = pla.Field(nullable=True, )
    """
    The organization's notes on putting the control in place.
    """
    
    control_threats: Optional[str] = pla.Field(nullable=True, )
    """
    The threats the control acts against.
    """
    
    control_asset_types: Optional[str] = pla.Field(nullable=True, )
    """
    The kinds of asset the control applies to.
    """
    
    control_owner: Optional[str] = pla.Field(nullable=True, )
    """
    The person who owns the control.
    """
    
    control_implementation_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the control was put in place.
    """
    
    control_effectiveness: Optional[str] = pla.Field(nullable=True, )
    """
    How well the control works, in the organization's own terms.
    """
    
    control_last_tested: Optional[Date] = pla.Field(nullable=True, )
    """
    When the control was last tested.
    """
    
    control_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    Where the evidence that the control is in place is kept.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsAsset(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
    """

    _id_name : str =  'isms_id' 
    relevant_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls that the record concerns.
    """
    
    asset_category: Optional[str] = pla.Field(nullable=True, )
    """
    What kind of asset it is, such as information, software, hardware or a service.
    """
    
    asset_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who owns the asset.
    """
    
    asset_custodian: Optional[str] = pla.Field(nullable=True, )
    """
    Who looks after the asset from day to day.
    """
    
    asset_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the asset carries.
    """
    
    asset_location: Optional[str] = pla.Field(nullable=True, )
    """
    Where the asset is, physically or logically.
    """
    
    asset_criticality: Optional[str] = pla.Field(nullable=True, )
    """
    How much the asset matters, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsResource(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A resource provided for the ISMS, such as people, time, tools or budget.
    """

    _id_name : str =  'isms_id' 
    resource_category: Optional[str] = pla.Field(nullable=True, )
    """
    What kind of resource it is.
    """
    
    resource_quantity: Optional[str] = pla.Field(nullable=True, )
    """
    How much of the resource is provided.
    """
    
    resource_allocation_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the resource was allocated.
    """
    
    resource_allocated_to: Optional[str] = pla.Field(nullable=True, )
    """
    What the resource is allocated to.
    """
    
    resource_cost: Optional[str] = pla.Field(nullable=True, )
    """
    What the resource costs.
    """
    
    resource_availability: Optional[str] = pla.Field(nullable=True, )
    """
    Whether the resource is available now, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsCompetenceRecord(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The evidence of one person's competence for work that affects information security, and what is done to close any gap.
    """

    _id_name : str =  'isms_id' 
    competence_person: Optional[str] = pla.Field(nullable=True, )
    """
    The person the record is about.
    """
    
    competence_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role the person holds.
    """
    
    competence_required: Optional[str] = pla.Field(nullable=True, )
    """
    The competences the role needs.
    """
    
    competence_education: Optional[str] = pla.Field(nullable=True, )
    """
    The person's relevant education.
    """
    
    competence_training: Optional[str] = pla.Field(nullable=True, )
    """
    The training the person has completed.
    """
    
    competence_experience: Optional[str] = pla.Field(nullable=True, )
    """
    The person's relevant experience.
    """
    
    competence_assessment_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the person's competence was last assessed.
    """
    
    competence_gaps: Optional[str] = pla.Field(nullable=True, )
    """
    The gaps the assessment found.
    """
    
    competence_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What is done to close the gaps.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsAwarenessProgramme(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
    """

    _id_name : str =  'isms_id' 
    awareness_topics: Optional[str] = pla.Field(nullable=True, )
    """
    The topics the programme covers.
    """
    
    awareness_methods: Optional[str] = pla.Field(nullable=True, )
    """
    How the programme is delivered.
    """
    
    awareness_audience: Optional[str] = pla.Field(nullable=True, )
    """
    Whom the programme is for.
    """
    
    awareness_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often the programme runs.
    """
    
    awareness_completion_tracking: Optional[str] = pla.Field(nullable=True, )
    """
    How completion is tracked.
    """
    
    awareness_effectiveness: Optional[str] = pla.Field(nullable=True, )
    """
    How the programme's effect is measured.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsCommunication(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
    """

    _id_name : str = None
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    communication_subject: str = pla.Field()
    """
    What the communication is about.
    """
    
    communication_purpose: Optional[str] = pla.Field(nullable=True, )
    """
    Why it is communicated.
    """
    
    communication_audience: Optional[str] = pla.Field(nullable=True, )
    """
    To whom it is communicated.
    """
    
    communication_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often it is communicated.
    """
    
    communication_method: Optional[str] = pla.Field(nullable=True, )
    """
    How it is communicated.
    """
    
    communication_records_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether a record of the communication is kept.
    """
    
    
class IsmsCommunicationPlan(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The plan for communication about the ISMS, inside the organization and outside it.
    """

    _id_name : str =  'isms_id' 
    communication_items: Optional[List] = pla.Field(nullable=True, )
    """
    The communications the plan provides for.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
    @pla.check("communication_items")
    def check_nested_struct_communication_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsCommunication, pa_pl.IsmsCommunicationDict)
        
class IsmsDocumentedInformation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A piece of documented information the ISMS keeps under control that no more specific record describes, such as a procedure, a standard, a plan or a report.
    """

    _id_name : str =  'isms_id' 
    document_kind: Enum = pla.Field(dtype_kwargs={"categories":('procedure','standard','guideline','record','plan','report',)})
    """
    What kind of documented information it is.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsOperationalProcedure(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A procedure by which the organization plans and controls the processes that meet its information security requirements.
    """

    _id_name : str =  'isms_id' 
    relevant_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The organization's controls that the record concerns.
    """
    
    procedure_scope: Optional[str] = pla.Field(nullable=True, )
    """
    What the procedure covers.
    """
    
    procedure_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    The criteria the processes are run to.
    """
    
    procedure_control_measures: Optional[str] = pla.Field(nullable=True, )
    """
    The measures that control the processes.
    """
    
    procedure_roles: Optional[List] = pla.Field(nullable=True, )
    """
    The roles that carry out the procedure.
    """
    
    procedure_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the processes are controlled.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsMonitoringItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
    """

    _id_name : str = None
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    monitoring_metric: str = pla.Field()
    """
    The name of what is measured.
    """
    
    monitoring_description: Optional[str] = pla.Field(nullable=True, )
    """
    What the measurement shows.
    """
    
    monitoring_method: Optional[str] = pla.Field(nullable=True, )
    """
    How it is measured.
    """
    
    monitoring_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often it is measured.
    """
    
    monitoring_analysis_frequency: Optional[str] = pla.Field(nullable=True, )
    """
    How often the results are analysed and evaluated.
    """
    
    monitoring_analyst: Optional[str] = pla.Field(nullable=True, )
    """
    Who analyses and evaluates the results.
    """
    
    monitoring_target: Optional[str] = pla.Field(nullable=True, )
    """
    The value aimed for.
    """
    
    monitoring_alert_threshold: Optional[str] = pla.Field(nullable=True, )
    """
    The value that calls for action.
    """
    
    monitoring_current_value: Optional[str] = pla.Field(nullable=True, )
    """
    The value last measured.
    """
    
    monitoring_trend: Optional[str] = pla.Field(nullable=True, )
    """
    Which way the value is moving.
    """
    
    
class IsmsMonitoringProgramme(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The programme of monitoring, measurement, analysis and evaluation of information security performance and of the ISMS's effectiveness.
    """

    _id_name : str =  'isms_id' 
    monitoring_items: Optional[List] = pla.Field(nullable=True, )
    """
    What the programme monitors and measures.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
    @pla.check("monitoring_items")
    def check_nested_struct_monitoring_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsMonitoringItem, pa_pl.IsmsMonitoringItemDict)
        
class IsmsAuditProgramme(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
    """

    _id_name : str =  'isms_id' 
    programme_period: Optional[str] = pla.Field(nullable=True, )
    """
    The period the programme covers.
    """
    
    programme_audits: Optional[List] = pla.Field(nullable=True, )
    """
    The audits the programme plans.
    """
    
    programme_frequency_rationale: Optional[str] = pla.Field(nullable=True, )
    """
    Why the audits happen as often as they do.
    """
    
    programme_resources: Optional[str] = pla.Field(nullable=True, )
    """
    The resources the programme needs.
    """
    
    programme_auditor_qualifications: Optional[str] = pla.Field(nullable=True, )
    """
    The qualifications the auditors need.
    """
    
    programme_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the programme stands, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsAuditFinding(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
    """

    _id_name : str =  'isms_id' 
    finding_type: Enum = pla.Field(dtype_kwargs={"categories":('major_nonconformity','minor_nonconformity','observation','positive_finding',)})
    """
    What kind of finding it is.
    """
    
    finding_requirement: Optional[str] = pla.Field(nullable=True, )
    """
    The clause or Annex A control of ISO/IEC 27001:2022 the finding concerns, by number.
    """
    
    finding_control: Optional[ID_TYPES['IsmsControl']] = pla.Field(nullable=True, )
    """
    The organization's control the finding concerns.
    """
    
    finding_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    The objective evidence for the finding.
    """
    
    finding_root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    What the analysis of the finding's cause found.
    """
    
    finding_risk: Optional[str] = pla.Field(nullable=True, )
    """
    What the finding means for risk.
    """
    
    finding_recommendation: Optional[str] = pla.Field(nullable=True, )
    """
    What the auditor recommends.
    """
    
    finding_auditee_response: Optional[str] = pla.Field(nullable=True, )
    """
    How the auditee responded.
    """
    
    finding_corrective_action: Optional[ID_TYPES['IsmsCorrectiveAction']] = pla.Field(nullable=True, )
    """
    The corrective action the finding led to.
    """
    
    finding_closure_status: Optional[str] = pla.Field(nullable=True, )
    """
    Whether the finding is closed, in the organization's own terms.
    """
    
    finding_closure_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the finding was closed.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsAudit(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
    """

    _id_name : str =  'isms_id' 
    audit_type: Enum = pla.Field(dtype_kwargs={"categories":('first_party','second_party','third_party',)})
    """
    Who carries out the audit, relative to the organization.
    """
    
    audit_standards: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('iso_iec_27001','iso_iec_27701','iso_iec_42001','iso_9001','iso_14001','iso_22301','iso_iec_20000_1',)})
    """
    The management system standards the audit covers.
    """
    
    audit_scope: Optional[str] = pla.Field(nullable=True, )
    """
    What the audit covers.
    """
    
    audit_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    What the audit compares the ISMS against.
    """
    
    audit_objectives: Optional[str] = pla.Field(nullable=True, )
    """
    What the audit sets out to establish.
    """
    
    audit_period_start: Optional[Date] = pla.Field(nullable=True, )
    """
    When the audit began.
    """
    
    audit_period_end: Optional[Date] = pla.Field(nullable=True, )
    """
    When the audit ended.
    """
    
    audit_lead: Optional[str] = pla.Field(nullable=True, )
    """
    Who led the audit.
    """
    
    audit_team: Optional[str] = pla.Field(nullable=True, )
    """
    Who else audited.
    """
    
    audit_auditees: Optional[str] = pla.Field(nullable=True, )
    """
    Who represented the parts of the organization audited.
    """
    
    audit_plan: Optional[ID_TYPES['IsmsDocumentedInformation']] = pla.Field(nullable=True, )
    """
    The documented information that holds the audit plan.
    """
    
    audit_findings: Optional[List] = pla.Field(nullable=True, )
    """
    What the audit found, good and bad.
    """
    
    audit_conclusion: Optional[str] = pla.Field(nullable=True, )
    """
    The audit's overall conclusion.
    """
    
    audit_report_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the audit report was issued.
    """
    
    audit_report_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    Who received the audit report.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
    @pla.check("audit_findings")
    def check_nested_struct_audit_findings(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsAuditFinding, pa_pl.IsmsAuditFindingDict)
        
class IsmsManagementReview(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
    """

    _id_name : str =  'isms_id' 
    review_held_on: Date = pla.Field()
    """
    When the review was held.
    """
    
    review_attendees: Optional[str] = pla.Field(nullable=True, )
    """
    Who attended the review.
    """
    
    review_previous_actions: Optional[str] = pla.Field(nullable=True, )
    """
    Where the actions from earlier reviews stand.
    """
    
    review_context_changes: Optional[str] = pla.Field(nullable=True, )
    """
    How the issues that bear on the ISMS have changed.
    """
    
    review_interested_party_changes: Optional[str] = pla.Field(nullable=True, )
    """
    How interested parties' needs and expectations have changed.
    """
    
    review_interested_party_feedback: Optional[str] = pla.Field(nullable=True, )
    """
    What interested parties said.
    """
    
    review_performance_trends: Optional[str] = pla.Field(nullable=True, )
    """
    The trends in information security performance.
    """
    
    review_audit_results: Optional[str] = pla.Field(nullable=True, )
    """
    What the audits found.
    """
    
    review_risk_assessment_results: Optional[str] = pla.Field(nullable=True, )
    """
    What the risk assessments found.
    """
    
    review_risk_treatment_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where risk treatment stands.
    """
    
    review_risks_and_opportunities: Optional[str] = pla.Field(nullable=True, )
    """
    How risks and opportunities have changed.
    """
    
    review_improvement_opportunities: Optional[str] = pla.Field(nullable=True, )
    """
    The opportunities for improvement raised.
    """
    
    review_decisions: Optional[str] = pla.Field(nullable=True, )
    """
    What the review decided.
    """
    
    review_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What the review asked to be done.
    """
    
    review_next_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the next review is planned.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    document_reference: Optional[str] = pla.Field(nullable=True, )
    """
    The reference the organization's document control gives it.
    """
    
    document_version: Optional[str] = pla.Field(nullable=True, )
    """
    The version of the document.
    """
    
    document_author: Optional[str] = pla.Field(nullable=True, )
    """
    Who wrote the document.
    """
    
    document_owner: Optional[str] = pla.Field(nullable=True, )
    """
    Who answers for the document's content and upkeep.
    """
    
    document_approver: Optional[str] = pla.Field(nullable=True, )
    """
    Who approved the document.
    """
    
    document_approval_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was approved.
    """
    
    document_effective_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document takes effect.
    """
    
    document_last_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document was last reviewed.
    """
    
    document_next_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the document is next due for review.
    """
    
    document_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
    """
    
    document_classification: Optional[str] = pla.Field(nullable=True, )
    """
    The information classification the document carries.
    """
    
    document_retention: Optional[str] = pla.Field(nullable=True, )
    """
    How long the document is kept, as an ISO 8601 duration.
    """
    
    document_distribution: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is distributed, accessed, retrieved and used.
    """
    
    document_storage: Optional[str] = pla.Field(nullable=True, )
    """
    How the document is stored and preserved, so that it stays legible.
    """
    
    document_change_control: Optional[str] = pla.Field(nullable=True, )
    """
    How changes to the document are controlled, such as version control.
    """
    
    document_external_origin: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the document comes from outside the organization and is kept because the ISMS needs it.
    """
    
    document_external_source: Optional[str] = pla.Field(nullable=True, )
    """
    Who the document came from, when it comes from outside.
    """
    
    
class IsmsNonconformity(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
    """

    _id_name : str =  'isms_id' 
    nonconformity_source: Optional[str] = pla.Field(nullable=True, )
    """
    How the nonconformity came to light, such as an audit, a review or an incident.
    """
    
    nonconformity_detected_on: Optional[Date] = pla.Field(nullable=True, )
    """
    When the nonconformity was found.
    """
    
    nonconformity_detected_by: Optional[str] = pla.Field(nullable=True, )
    """
    Who or what found it.
    """
    
    nonconformity_requirement: Optional[str] = pla.Field(nullable=True, )
    """
    The requirement that was not met, of ISO/IEC 27001, of the organization or of an interested party.
    """
    
    nonconformity_immediate_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What was done at once to control and correct it.
    """
    
    nonconformity_consequences: Optional[str] = pla.Field(nullable=True, )
    """
    How its consequences were dealt with.
    """
    
    nonconformity_root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    What caused it.
    """
    
    nonconformity_similar_check: Optional[str] = pla.Field(nullable=True, )
    """
    Whether similar nonconformities exist or could occur, and where.
    """
    
    nonconformity_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the nonconformity stands, in the organization's own terms.
    """
    
    nonconformity_closure_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When it was closed.
    """
    
    nonconformity_closure_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    What shows that it is closed.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsCorrectiveAction(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
    """

    _id_name : str =  'isms_id' 
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    action_nonconformities: Optional[List] = pla.Field(nullable=True, )
    """
    The nonconformities the action addresses.
    """
    
    action_root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    The cause the action removes.
    """
    
    action_target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the action is to be complete.
    """
    
    action_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the action was complete.
    """
    
    action_resources: Optional[str] = pla.Field(nullable=True, )
    """
    The resources the action needs.
    """
    
    action_effectiveness_criteria: Optional[str] = pla.Field(nullable=True, )
    """
    How the action's effect will be judged.
    """
    
    action_effectiveness_review_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the action's effect was reviewed.
    """
    
    action_effective: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the review found the action effective.
    """
    
    action_isms_changes: Optional[str] = pla.Field(nullable=True, )
    """
    The changes to the ISMS the action needs.
    """
    
    action_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the action stands, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsImprovementOpportunity(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
    """

    _id_name : str =  'isms_id' 
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    improvement_source: Optional[str] = pla.Field(nullable=True, )
    """
    Where the opportunity came from, such as a review, an audit or daily work.
    """
    
    improvement_identified_on: Optional[Date] = pla.Field(nullable=True, )
    """
    When the opportunity was identified.
    """
    
    improvement_identified_by: Optional[str] = pla.Field(nullable=True, )
    """
    Who identified it.
    """
    
    improvement_benefit: Optional[str] = pla.Field(nullable=True, )
    """
    What the improvement is expected to bring.
    """
    
    improvement_priority: Optional[str] = pla.Field(nullable=True, )
    """
    How soon it is to be acted on, in the organization's own terms.
    """
    
    improvement_plan: Optional[str] = pla.Field(nullable=True, )
    """
    How the improvement is to be made.
    """
    
    improvement_target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the improvement is to be made.
    """
    
    improvement_completion_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When it was made.
    """
    
    improvement_outcome: Optional[str] = pla.Field(nullable=True, )
    """
    What the improvement brought.
    """
    
    improvement_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where it stands, in the organization's own terms.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsSecurityEvent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
    """

    _id_name : str =  'isms_id' 
    affected_assets: Optional[List] = pla.Field(nullable=True, )
    """
    The assets the risk, event or incident affects.
    """
    
    event_type: Optional[str] = pla.Field(nullable=True, )
    """
    The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident.
    """
    
    event_occurred_at: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    When the event happened, or when it was first noticed.
    """
    
    event_reporter: Optional[str] = pla.Field(nullable=True, )
    """
    Who reported the event.
    """
    
    event_assessment: Optional[str] = pla.Field(nullable=True, )
    """
    What the assessment of the event found.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
class IsmsManagementSystem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
    """

    _id_name : str =  'isms_id' 
    isms_organization: Optional[Struct] = pla.Field(nullable=True, )
    """
    The organization that runs the ISMS.
    """
    
    isms_top_management: Optional[str] = pla.Field(nullable=True, )
    """
    The person or group that directs and controls the organization at the highest level.
    """
    
    isms_governing_body: Optional[str] = pla.Field(nullable=True, )
    """
    The body top management answers to, such as a board, where there is one.
    """
    
    isms_leadership_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    What shows that top management leads and commits to the ISMS.
    """
    
    isms_scope: Optional[str] = pla.Field(nullable=True, )
    """
    The scope of the ISMS, as the organization states it.
    """
    
    isms_scope_boundaries: Optional[str] = pla.Field(nullable=True, )
    """
    Where the scope of the ISMS ends.
    """
    
    isms_scope_exclusions: Optional[str] = pla.Field(nullable=True, )
    """
    What the scope leaves out, each with the reason.
    """
    
    isms_interfaces: Optional[str] = pla.Field(nullable=True, )
    """
    The interfaces and dependencies between what the organization does and what other organizations do, which the scope takes into account.
    """
    
    isms_processes: Optional[str] = pla.Field(nullable=True, )
    """
    The processes the ISMS needs and how they interact.
    """
    
    isms_internal_issues: Optional[str] = pla.Field(nullable=True, )
    """
    The internal issues that bear on the ISMS.
    """
    
    isms_external_issues: Optional[str] = pla.Field(nullable=True, )
    """
    The external issues that bear on the ISMS.
    """
    
    isms_risk_and_opportunity_actions: Optional[str] = pla.Field(nullable=True, )
    """
    The actions planned to address the ISMS's risks and opportunities, and how they fit into its processes.
    """
    
    isms_planned_changes: Optional[str] = pla.Field(nullable=True, )
    """
    The changes to the ISMS that are planned.
    """
    
    isms_external_services: Optional[str] = pla.Field(nullable=True, )
    """
    The processes, products or services from outside the organization that the ISMS relies on and controls.
    """
    
    isms_certification_status: Optional[str] = pla.Field(nullable=True, )
    """
    Where the ISMS stands with certification, in the organization's own terms.
    """
    
    isms_certification_body: Optional[str] = pla.Field(nullable=True, )
    """
    The body that certifies the ISMS.
    """
    
    isms_certification_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the ISMS was certified.
    """
    
    isms_recertification_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the ISMS is next due for recertification.
    """
    
    isms_interested_parties: Optional[List] = pla.Field(nullable=True, )
    """
    The interested parties the ISMS takes into account.
    """
    
    isms_policy: Optional[Struct] = pla.Field(nullable=True, )
    """
    The information security policy.
    """
    
    isms_topic_specific_policies: Optional[List] = pla.Field(nullable=True, )
    """
    The topic-specific policies under the information security policy.
    """
    
    isms_roles: Optional[List] = pla.Field(nullable=True, )
    """
    The roles that carry the ISMS's responsibilities and authorities.
    """
    
    isms_objectives: Optional[List] = pla.Field(nullable=True, )
    """
    The information security objectives.
    """
    
    isms_risk_assessment_process: Optional[Struct] = pla.Field(nullable=True, )
    """
    The information security risk assessment process.
    """
    
    isms_risk_treatment_process: Optional[Struct] = pla.Field(nullable=True, )
    """
    The information security risk treatment process.
    """
    
    isms_risk_assessments: Optional[List] = pla.Field(nullable=True, )
    """
    The risk assessments carried out.
    """
    
    isms_risks: Optional[List] = pla.Field(nullable=True, )
    """
    The risks identified, the risk register.
    """
    
    isms_risk_treatment_plans: Optional[List] = pla.Field(nullable=True, )
    """
    The risk treatment plans.
    """
    
    isms_statement_of_applicability: Optional[Struct] = pla.Field(nullable=True, )
    """
    The Statement of Applicability.
    """
    
    isms_controls: Optional[List] = pla.Field(nullable=True, )
    """
    The controls the organization has determined it needs.
    """
    
    isms_assets: Optional[List] = pla.Field(nullable=True, )
    """
    The inventory of information and other associated assets.
    """
    
    isms_resources: Optional[List] = pla.Field(nullable=True, )
    """
    The resources provided for the ISMS.
    """
    
    isms_competence_records: Optional[List] = pla.Field(nullable=True, )
    """
    The records of competence.
    """
    
    isms_awareness_programme: Optional[Struct] = pla.Field(nullable=True, )
    """
    The awareness programme.
    """
    
    isms_communication_plan: Optional[Struct] = pla.Field(nullable=True, )
    """
    The plan for communication about the ISMS.
    """
    
    isms_documented_information: Optional[List] = pla.Field(nullable=True, )
    """
    The documented information the ISMS keeps that no more specific list holds, such as procedures, plans and reports.
    """
    
    isms_operational_procedures: Optional[List] = pla.Field(nullable=True, )
    """
    The procedures for operational planning and control.
    """
    
    isms_monitoring_programme: Optional[Struct] = pla.Field(nullable=True, )
    """
    The programme of monitoring and measurement.
    """
    
    isms_audit_programmes: Optional[List] = pla.Field(nullable=True, )
    """
    The audit programmes.
    """
    
    isms_audits: Optional[List] = pla.Field(nullable=True, )
    """
    The audits of the ISMS, internal and external.
    """
    
    isms_management_reviews: Optional[List] = pla.Field(nullable=True, )
    """
    The management reviews.
    """
    
    isms_nonconformities: Optional[List] = pla.Field(nullable=True, )
    """
    The nonconformities found.
    """
    
    isms_corrective_actions: Optional[List] = pla.Field(nullable=True, )
    """
    The corrective actions taken.
    """
    
    isms_improvements: Optional[List] = pla.Field(nullable=True, )
    """
    The opportunities for improvement identified.
    """
    
    isms_security_events: Optional[List] = pla.Field(nullable=True, )
    """
    The information security events reported, the incidents among them.
    """
    
    isms_id: str = pla.Field()
    """
    The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
    """
    
    title: str = pla.Field(str_contains=r"^\s*\S", )
    """
    The name the organization gives the record.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    What the record says or describes, in the organization's own words.
    """
    
    
    @pla.check("isms_organization")
    def check_nested_struct_isms_organization(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsOrganization, pa_pl.IsmsOrganization)
        
    @pla.check("isms_interested_parties")
    def check_nested_struct_isms_interested_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsInterestedParty, pa_pl.IsmsInterestedPartyDict)
        
    @pla.check("isms_policy")
    def check_nested_struct_isms_policy(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsPolicy, pa_pl.IsmsPolicy)
        
    @pla.check("isms_topic_specific_policies")
    def check_nested_struct_isms_topic_specific_policies(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsTopicSpecificPolicy, pa_pl.IsmsTopicSpecificPolicyDict)
        
    @pla.check("isms_roles")
    def check_nested_struct_isms_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsRole, pa_pl.IsmsRoleDict)
        
    @pla.check("isms_objectives")
    def check_nested_struct_isms_objectives(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsObjective, pa_pl.IsmsObjectiveDict)
        
    @pla.check("isms_risk_assessment_process")
    def check_nested_struct_isms_risk_assessment_process(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsRiskAssessmentProcess, pa_pl.IsmsRiskAssessmentProcess)
        
    @pla.check("isms_risk_treatment_process")
    def check_nested_struct_isms_risk_treatment_process(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsRiskTreatmentProcess, pa_pl.IsmsRiskTreatmentProcess)
        
    @pla.check("isms_risk_assessments")
    def check_nested_struct_isms_risk_assessments(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsRiskAssessment, pa_pl.IsmsRiskAssessmentDict)
        
    @pla.check("isms_risks")
    def check_nested_struct_isms_risks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsRisk, pa_pl.IsmsRiskDict)
        
    @pla.check("isms_risk_treatment_plans")
    def check_nested_struct_isms_risk_treatment_plans(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsRiskTreatmentPlan, pa_pl.IsmsRiskTreatmentPlanDict)
        
    @pla.check("isms_statement_of_applicability")
    def check_nested_struct_isms_statement_of_applicability(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsStatementOfApplicability, pa_pl.IsmsStatementOfApplicability)
        
    @pla.check("isms_controls")
    def check_nested_struct_isms_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsControl, pa_pl.IsmsControlDict)
        
    @pla.check("isms_assets")
    def check_nested_struct_isms_assets(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsAsset, pa_pl.IsmsAssetDict)
        
    @pla.check("isms_resources")
    def check_nested_struct_isms_resources(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsResource, pa_pl.IsmsResourceDict)
        
    @pla.check("isms_competence_records")
    def check_nested_struct_isms_competence_records(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsCompetenceRecord, pa_pl.IsmsCompetenceRecordDict)
        
    @pla.check("isms_awareness_programme")
    def check_nested_struct_isms_awareness_programme(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsAwarenessProgramme, pa_pl.IsmsAwarenessProgramme)
        
    @pla.check("isms_communication_plan")
    def check_nested_struct_isms_communication_plan(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsCommunicationPlan, pa_pl.IsmsCommunicationPlan)
        
    @pla.check("isms_documented_information")
    def check_nested_struct_isms_documented_information(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsDocumentedInformation, pa_pl.IsmsDocumentedInformationDict)
        
    @pla.check("isms_operational_procedures")
    def check_nested_struct_isms_operational_procedures(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsOperationalProcedure, pa_pl.IsmsOperationalProcedureDict)
        
    @pla.check("isms_monitoring_programme")
    def check_nested_struct_isms_monitoring_programme(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IsmsMonitoringProgramme, pa_pl.IsmsMonitoringProgramme)
        
    @pla.check("isms_audit_programmes")
    def check_nested_struct_isms_audit_programmes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsAuditProgramme, pa_pl.IsmsAuditProgrammeDict)
        
    @pla.check("isms_audits")
    def check_nested_struct_isms_audits(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsAudit, pa_pl.IsmsAuditDict)
        
    @pla.check("isms_management_reviews")
    def check_nested_struct_isms_management_reviews(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsManagementReview, pa_pl.IsmsManagementReviewDict)
        
    @pla.check("isms_nonconformities")
    def check_nested_struct_isms_nonconformities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsNonconformity, pa_pl.IsmsNonconformityDict)
        
    @pla.check("isms_corrective_actions")
    def check_nested_struct_isms_corrective_actions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsCorrectiveAction, pa_pl.IsmsCorrectiveActionDict)
        
    @pla.check("isms_improvements")
    def check_nested_struct_isms_improvements(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsImprovementOpportunity, pa_pl.IsmsImprovementOpportunityDict)
        
    @pla.check("isms_security_events")
    def check_nested_struct_isms_security_events(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IsmsSecurityEvent, pa_pl.IsmsSecurityEventDict)
        
class IsmsIncludedControl(IsmsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
    """

    _id_name : str = None
    implementation_state: Enum = pla.Field(dtype_kwargs={"categories":('not_started','planned','in_progress','implemented',)})
    """
    How far the control or the plan has been put into effect.
    """
    
    responsible_role: Optional[ID_TYPES['IsmsRole']] = pla.Field(nullable=True, )
    """
    The role that answers for the record's activity or outcome.
    """
    
    included_control: Optional[ID_TYPES['IsmsControl']] = pla.Field(nullable=True, )
    """
    The organization's control the entry includes.
    """
    
    included_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    What shows that the control is in place.
    """
    
    included_target_date: Optional[Date] = pla.Field(nullable=True, )
    """
    When the control is to be in place, if it is not yet.
    """
    
    
class IsmsSecurityIncident(IsmsSecurityEvent):
    """
    An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
    """

    _id_name : str =  'isms_id' 
    affected_security_properties: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('confidentiality','integrity','availability',)})
    """
    Which of confidentiality, integrity and availability the risk or incident threatens.
    """
    
    incident_category: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('malware','ransomware','phishing','social_engineering','unauthorized_access','account_compromise','privilege_misuse','data_breach','data_loss','denial_of_service','web_application_attack','supply_chain','insider_threat','physical_security','configuration_error','cryptographic_failure','policy_violation','other',)})
    """
    What kind of incident it is.
    """
    
    incident_severity: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('very_low','low','medium','high','critical',)})
    """
    How severe the incident is.
    """
    
    incident_detection_method: Optional[str] = pla.Field(nullable=True, )
    """
    How the incident was detected.
    """
    
    incident_response_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What was done in response.
    """
    
    incident_containment_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What was done to contain it.
    """
    
    incident_eradication_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What was done to remove its cause.
    """
    
    incident_recovery_actions: Optional[str] = pla.Field(nullable=True, )
    """
    What was done to restore normal operation.
    """
    
    incident_root_cause: Optional[str] = pla.Field(nullable=True, )
    """
    What caused the incident.
    """
    
    incident_lessons_learned: Optional[str] = pla.Field(nullable=True, )
    """
    What the organization learned from it.
    """
    
    incident_evidence: Optional[str] = pla.Field(nullable=True, )
    """
    The evidence collected about it.
    """
    
    incident_notification_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether authorities or other parties had to be told.
    """
    
    incident_notifications: Optional[str] = pla.Field(nullable=True, )
    """
    Whom the organization told, and when.
    """
    
    incident_closed_at: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    When the incident was closed.
    """
    
    incident_review: Optional[str] = pla.Field(nullable=True, )
    """
    What the review after the incident found.
    """
    
    
class IsmsExcludedControl(IsmsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """

    _id_name : str = None
    pass
    
    

