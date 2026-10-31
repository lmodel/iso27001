# Auto generated from iso27001.yaml by pythongen.py version: 0.0.1
# Schema: iso27001
#
# id: https://w3id.org/lmodel/iso27001
# description: A LinkML model of the records an organization keeps to run an information security management system (ISMS) to ISO/IEC 27001:2022 with Amendment 1:2024. The records cover the ISMS's context and scope, policies, roles and objectives, risks and their treatment, and its controls and Statement of Applicability. They also cover the support and operation it needs, its audits and management reviews, and its nonconformities, corrective actions and improvements. The 93 reference controls of Annex A appear by their numbers alone.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.12.0"
version = "2022/Amd 1:2024"

# Namespaces
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX_CORE = CurieNamespace('spdx_core', 'https://spdx.org/rdf/3.0.1/terms/Core/')
SPDX_SOFTWARE = CurieNamespace('spdx_software', 'https://spdx.org/rdf/3.0.1/terms/Software/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO27001


# Types
class IsmsDuration(String):
    """ A length of time as ISO 8601 writes it, such as P7Y for seven years or P30D for thirty days. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "isms_duration"
    type_model_uri = ISO27001.IsmsDuration


class IsmsRequirementReference(String):
    """ The number of a clause of ISO/IEC 27001:2022, from 4 to 10, such as 6.1.2, or of an Annex A control, such as A.5.9. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "isms_requirement_reference"
    type_model_uri = ISO27001.IsmsRequirementReference


# Class references
class IsmsRecordMixinIsmsId(URIorCURIE):
    pass


class IsmsManagementSystemIsmsId(URIorCURIE):
    pass


class IsmsOrganizationIsmsId(URIorCURIE):
    pass


class IsmsInterestedPartyIsmsId(URIorCURIE):
    pass


class IsmsPolicyIsmsId(URIorCURIE):
    pass


class IsmsTopicSpecificPolicyIsmsId(URIorCURIE):
    pass


class IsmsRoleIsmsId(URIorCURIE):
    pass


class IsmsObjectiveIsmsId(URIorCURIE):
    pass


class IsmsRiskAssessmentProcessIsmsId(URIorCURIE):
    pass


class IsmsRiskAssessmentIsmsId(URIorCURIE):
    pass


class IsmsRiskIsmsId(URIorCURIE):
    pass


class IsmsRiskTreatmentProcessIsmsId(URIorCURIE):
    pass


class IsmsRiskTreatmentPlanIsmsId(URIorCURIE):
    pass


class IsmsStatementOfApplicabilityIsmsId(URIorCURIE):
    pass


class IsmsControlIsmsId(URIorCURIE):
    pass


class IsmsAssetIsmsId(URIorCURIE):
    pass


class IsmsResourceIsmsId(URIorCURIE):
    pass


class IsmsCompetenceRecordIsmsId(URIorCURIE):
    pass


class IsmsAwarenessProgrammeIsmsId(URIorCURIE):
    pass


class IsmsCommunicationPlanIsmsId(URIorCURIE):
    pass


class IsmsDocumentedInformationIsmsId(URIorCURIE):
    pass


class IsmsOperationalProcedureIsmsId(URIorCURIE):
    pass


class IsmsMonitoringProgrammeIsmsId(URIorCURIE):
    pass


class IsmsAuditProgrammeIsmsId(URIorCURIE):
    pass


class IsmsAuditIsmsId(URIorCURIE):
    pass


class IsmsAuditFindingIsmsId(URIorCURIE):
    pass


class IsmsManagementReviewIsmsId(URIorCURIE):
    pass


class IsmsNonconformityIsmsId(URIorCURIE):
    pass


class IsmsCorrectiveActionIsmsId(URIorCURIE):
    pass


class IsmsImprovementOpportunityIsmsId(URIorCURIE):
    pass


class IsmsSecurityEventIsmsId(URIorCURIE):
    pass


class IsmsSecurityIncidentIsmsId(IsmsSecurityEventIsmsId):
    pass


@dataclass(repr=False)
class IsmsRecordMixin(YAMLRoot):
    """
    What every record of the ISMS has, so that other records can refer to it: an identifier, a title and a description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRecordMixin"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRecordMixin"
    class_name: ClassVar[str] = "IsmsRecordMixin"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRecordMixin

    isms_id: Union[str, IsmsRecordMixinIsmsId] = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRecordMixinIsmsId):
            self.isms_id = IsmsRecordMixinIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsDocumentControlMixin(YAMLRoot):
    """
    The control that documented information is kept under. It records who wrote, owns and approved the information,
    when it takes effect and is reviewed, and how it is classified, distributed, stored and changed. It also records
    how long it is retained, and whether it came from outside the organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsDocumentControlMixin"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsDocumentControlMixin"
    class_name: ClassVar[str] = "IsmsDocumentControlMixin"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsDocumentControlMixin

    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsManagementSystem(YAMLRoot):
    """
    One organization's information security management system: its scope and context, and every record it keeps, each
    kind in a list of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsManagementSystem"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsManagementSystem"
    class_name: ClassVar[str] = "IsmsManagementSystem"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsManagementSystem

    isms_id: Union[str, IsmsManagementSystemIsmsId] = None
    title: str = None
    isms_organization: Optional[Union[dict, "IsmsOrganization"]] = None
    isms_top_management: Optional[str] = None
    isms_governing_body: Optional[str] = None
    isms_leadership_evidence: Optional[Union[str, list[str]]] = empty_list()
    isms_scope: Optional[str] = None
    isms_scope_boundaries: Optional[Union[str, list[str]]] = empty_list()
    isms_scope_exclusions: Optional[Union[str, list[str]]] = empty_list()
    isms_interfaces: Optional[Union[str, list[str]]] = empty_list()
    isms_processes: Optional[str] = None
    isms_internal_issues: Optional[Union[str, list[str]]] = empty_list()
    isms_external_issues: Optional[Union[str, list[str]]] = empty_list()
    isms_risk_and_opportunity_actions: Optional[Union[str, list[str]]] = empty_list()
    isms_planned_changes: Optional[Union[str, list[str]]] = empty_list()
    isms_external_services: Optional[Union[str, list[str]]] = empty_list()
    isms_certification_status: Optional[str] = None
    isms_certification_body: Optional[str] = None
    isms_certification_date: Optional[Union[str, XSDDate]] = None
    isms_recertification_date: Optional[Union[str, XSDDate]] = None
    isms_interested_parties: Optional[Union[dict[Union[str, IsmsInterestedPartyIsmsId], Union[dict, "IsmsInterestedParty"]], list[Union[dict, "IsmsInterestedParty"]]]] = empty_dict()
    isms_policy: Optional[Union[dict, "IsmsPolicy"]] = None
    isms_topic_specific_policies: Optional[Union[dict[Union[str, IsmsTopicSpecificPolicyIsmsId], Union[dict, "IsmsTopicSpecificPolicy"]], list[Union[dict, "IsmsTopicSpecificPolicy"]]]] = empty_dict()
    isms_roles: Optional[Union[dict[Union[str, IsmsRoleIsmsId], Union[dict, "IsmsRole"]], list[Union[dict, "IsmsRole"]]]] = empty_dict()
    isms_objectives: Optional[Union[dict[Union[str, IsmsObjectiveIsmsId], Union[dict, "IsmsObjective"]], list[Union[dict, "IsmsObjective"]]]] = empty_dict()
    isms_risk_assessment_process: Optional[Union[dict, "IsmsRiskAssessmentProcess"]] = None
    isms_risk_treatment_process: Optional[Union[dict, "IsmsRiskTreatmentProcess"]] = None
    isms_risk_assessments: Optional[Union[dict[Union[str, IsmsRiskAssessmentIsmsId], Union[dict, "IsmsRiskAssessment"]], list[Union[dict, "IsmsRiskAssessment"]]]] = empty_dict()
    isms_risks: Optional[Union[dict[Union[str, IsmsRiskIsmsId], Union[dict, "IsmsRisk"]], list[Union[dict, "IsmsRisk"]]]] = empty_dict()
    isms_risk_treatment_plans: Optional[Union[dict[Union[str, IsmsRiskTreatmentPlanIsmsId], Union[dict, "IsmsRiskTreatmentPlan"]], list[Union[dict, "IsmsRiskTreatmentPlan"]]]] = empty_dict()
    isms_statement_of_applicability: Optional[Union[dict, "IsmsStatementOfApplicability"]] = None
    isms_controls: Optional[Union[dict[Union[str, IsmsControlIsmsId], Union[dict, "IsmsControl"]], list[Union[dict, "IsmsControl"]]]] = empty_dict()
    isms_assets: Optional[Union[dict[Union[str, IsmsAssetIsmsId], Union[dict, "IsmsAsset"]], list[Union[dict, "IsmsAsset"]]]] = empty_dict()
    isms_resources: Optional[Union[dict[Union[str, IsmsResourceIsmsId], Union[dict, "IsmsResource"]], list[Union[dict, "IsmsResource"]]]] = empty_dict()
    isms_competence_records: Optional[Union[dict[Union[str, IsmsCompetenceRecordIsmsId], Union[dict, "IsmsCompetenceRecord"]], list[Union[dict, "IsmsCompetenceRecord"]]]] = empty_dict()
    isms_awareness_programme: Optional[Union[dict, "IsmsAwarenessProgramme"]] = None
    isms_communication_plan: Optional[Union[dict, "IsmsCommunicationPlan"]] = None
    isms_documented_information: Optional[Union[dict[Union[str, IsmsDocumentedInformationIsmsId], Union[dict, "IsmsDocumentedInformation"]], list[Union[dict, "IsmsDocumentedInformation"]]]] = empty_dict()
    isms_operational_procedures: Optional[Union[dict[Union[str, IsmsOperationalProcedureIsmsId], Union[dict, "IsmsOperationalProcedure"]], list[Union[dict, "IsmsOperationalProcedure"]]]] = empty_dict()
    isms_monitoring_programme: Optional[Union[dict, "IsmsMonitoringProgramme"]] = None
    isms_audit_programmes: Optional[Union[dict[Union[str, IsmsAuditProgrammeIsmsId], Union[dict, "IsmsAuditProgramme"]], list[Union[dict, "IsmsAuditProgramme"]]]] = empty_dict()
    isms_audits: Optional[Union[dict[Union[str, IsmsAuditIsmsId], Union[dict, "IsmsAudit"]], list[Union[dict, "IsmsAudit"]]]] = empty_dict()
    isms_management_reviews: Optional[Union[dict[Union[str, IsmsManagementReviewIsmsId], Union[dict, "IsmsManagementReview"]], list[Union[dict, "IsmsManagementReview"]]]] = empty_dict()
    isms_nonconformities: Optional[Union[dict[Union[str, IsmsNonconformityIsmsId], Union[dict, "IsmsNonconformity"]], list[Union[dict, "IsmsNonconformity"]]]] = empty_dict()
    isms_corrective_actions: Optional[Union[dict[Union[str, IsmsCorrectiveActionIsmsId], Union[dict, "IsmsCorrectiveAction"]], list[Union[dict, "IsmsCorrectiveAction"]]]] = empty_dict()
    isms_improvements: Optional[Union[dict[Union[str, IsmsImprovementOpportunityIsmsId], Union[dict, "IsmsImprovementOpportunity"]], list[Union[dict, "IsmsImprovementOpportunity"]]]] = empty_dict()
    isms_security_events: Optional[Union[dict[Union[str, IsmsSecurityEventIsmsId], Union[dict, "IsmsSecurityEvent"]], list[Union[dict, "IsmsSecurityEvent"]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsManagementSystemIsmsId):
            self.isms_id = IsmsManagementSystemIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.isms_organization is not None and not isinstance(self.isms_organization, IsmsOrganization):
            self.isms_organization = IsmsOrganization(**as_dict(self.isms_organization))

        if self.isms_top_management is not None and not isinstance(self.isms_top_management, str):
            self.isms_top_management = str(self.isms_top_management)

        if self.isms_governing_body is not None and not isinstance(self.isms_governing_body, str):
            self.isms_governing_body = str(self.isms_governing_body)

        if not isinstance(self.isms_leadership_evidence, list):
            self.isms_leadership_evidence = [self.isms_leadership_evidence] if self.isms_leadership_evidence is not None else []
        self.isms_leadership_evidence = [v if isinstance(v, str) else str(v) for v in self.isms_leadership_evidence]

        if self.isms_scope is not None and not isinstance(self.isms_scope, str):
            self.isms_scope = str(self.isms_scope)

        if not isinstance(self.isms_scope_boundaries, list):
            self.isms_scope_boundaries = [self.isms_scope_boundaries] if self.isms_scope_boundaries is not None else []
        self.isms_scope_boundaries = [v if isinstance(v, str) else str(v) for v in self.isms_scope_boundaries]

        if not isinstance(self.isms_scope_exclusions, list):
            self.isms_scope_exclusions = [self.isms_scope_exclusions] if self.isms_scope_exclusions is not None else []
        self.isms_scope_exclusions = [v if isinstance(v, str) else str(v) for v in self.isms_scope_exclusions]

        if not isinstance(self.isms_interfaces, list):
            self.isms_interfaces = [self.isms_interfaces] if self.isms_interfaces is not None else []
        self.isms_interfaces = [v if isinstance(v, str) else str(v) for v in self.isms_interfaces]

        if self.isms_processes is not None and not isinstance(self.isms_processes, str):
            self.isms_processes = str(self.isms_processes)

        if not isinstance(self.isms_internal_issues, list):
            self.isms_internal_issues = [self.isms_internal_issues] if self.isms_internal_issues is not None else []
        self.isms_internal_issues = [v if isinstance(v, str) else str(v) for v in self.isms_internal_issues]

        if not isinstance(self.isms_external_issues, list):
            self.isms_external_issues = [self.isms_external_issues] if self.isms_external_issues is not None else []
        self.isms_external_issues = [v if isinstance(v, str) else str(v) for v in self.isms_external_issues]

        if not isinstance(self.isms_risk_and_opportunity_actions, list):
            self.isms_risk_and_opportunity_actions = [self.isms_risk_and_opportunity_actions] if self.isms_risk_and_opportunity_actions is not None else []
        self.isms_risk_and_opportunity_actions = [v if isinstance(v, str) else str(v) for v in self.isms_risk_and_opportunity_actions]

        if not isinstance(self.isms_planned_changes, list):
            self.isms_planned_changes = [self.isms_planned_changes] if self.isms_planned_changes is not None else []
        self.isms_planned_changes = [v if isinstance(v, str) else str(v) for v in self.isms_planned_changes]

        if not isinstance(self.isms_external_services, list):
            self.isms_external_services = [self.isms_external_services] if self.isms_external_services is not None else []
        self.isms_external_services = [v if isinstance(v, str) else str(v) for v in self.isms_external_services]

        if self.isms_certification_status is not None and not isinstance(self.isms_certification_status, str):
            self.isms_certification_status = str(self.isms_certification_status)

        if self.isms_certification_body is not None and not isinstance(self.isms_certification_body, str):
            self.isms_certification_body = str(self.isms_certification_body)

        if self.isms_certification_date is not None and not isinstance(self.isms_certification_date, XSDDate):
            self.isms_certification_date = XSDDate(self.isms_certification_date)

        if self.isms_recertification_date is not None and not isinstance(self.isms_recertification_date, XSDDate):
            self.isms_recertification_date = XSDDate(self.isms_recertification_date)

        self._normalize_inlined_as_list(slot_name="isms_interested_parties", slot_type=IsmsInterestedParty, key_name="isms_id", keyed=True)

        if self.isms_policy is not None and not isinstance(self.isms_policy, IsmsPolicy):
            self.isms_policy = IsmsPolicy(**as_dict(self.isms_policy))

        self._normalize_inlined_as_list(slot_name="isms_topic_specific_policies", slot_type=IsmsTopicSpecificPolicy, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_roles", slot_type=IsmsRole, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_objectives", slot_type=IsmsObjective, key_name="isms_id", keyed=True)

        if self.isms_risk_assessment_process is not None and not isinstance(self.isms_risk_assessment_process, IsmsRiskAssessmentProcess):
            self.isms_risk_assessment_process = IsmsRiskAssessmentProcess(**as_dict(self.isms_risk_assessment_process))

        if self.isms_risk_treatment_process is not None and not isinstance(self.isms_risk_treatment_process, IsmsRiskTreatmentProcess):
            self.isms_risk_treatment_process = IsmsRiskTreatmentProcess(**as_dict(self.isms_risk_treatment_process))

        self._normalize_inlined_as_list(slot_name="isms_risk_assessments", slot_type=IsmsRiskAssessment, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_risks", slot_type=IsmsRisk, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_risk_treatment_plans", slot_type=IsmsRiskTreatmentPlan, key_name="isms_id", keyed=True)

        if self.isms_statement_of_applicability is not None and not isinstance(self.isms_statement_of_applicability, IsmsStatementOfApplicability):
            self.isms_statement_of_applicability = IsmsStatementOfApplicability(**as_dict(self.isms_statement_of_applicability))

        self._normalize_inlined_as_list(slot_name="isms_controls", slot_type=IsmsControl, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_assets", slot_type=IsmsAsset, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_resources", slot_type=IsmsResource, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_competence_records", slot_type=IsmsCompetenceRecord, key_name="isms_id", keyed=True)

        if self.isms_awareness_programme is not None and not isinstance(self.isms_awareness_programme, IsmsAwarenessProgramme):
            self.isms_awareness_programme = IsmsAwarenessProgramme(**as_dict(self.isms_awareness_programme))

        if self.isms_communication_plan is not None and not isinstance(self.isms_communication_plan, IsmsCommunicationPlan):
            self.isms_communication_plan = IsmsCommunicationPlan(**as_dict(self.isms_communication_plan))

        self._normalize_inlined_as_list(slot_name="isms_documented_information", slot_type=IsmsDocumentedInformation, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_operational_procedures", slot_type=IsmsOperationalProcedure, key_name="isms_id", keyed=True)

        if self.isms_monitoring_programme is not None and not isinstance(self.isms_monitoring_programme, IsmsMonitoringProgramme):
            self.isms_monitoring_programme = IsmsMonitoringProgramme(**as_dict(self.isms_monitoring_programme))

        self._normalize_inlined_as_list(slot_name="isms_audit_programmes", slot_type=IsmsAuditProgramme, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_audits", slot_type=IsmsAudit, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_management_reviews", slot_type=IsmsManagementReview, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_nonconformities", slot_type=IsmsNonconformity, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_corrective_actions", slot_type=IsmsCorrectiveAction, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_improvements", slot_type=IsmsImprovementOpportunity, key_name="isms_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="isms_security_events", slot_type=IsmsSecurityEvent, key_name="isms_id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsOrganization(YAMLRoot):
    """
    The organization that runs the ISMS, with what it needs to know about itself to understand its context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsOrganization"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsOrganization"
    class_name: ClassVar[str] = "IsmsOrganization"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsOrganization

    isms_id: Union[str, IsmsOrganizationIsmsId] = None
    title: str = None
    organization_legal_name: Optional[str] = None
    organization_trading_names: Optional[Union[str, list[str]]] = empty_list()
    organization_kind: Optional[str] = None
    organization_sector: Optional[str] = None
    organization_size: Optional[str] = None
    organization_employee_count: Optional[int] = None
    organization_locations: Optional[Union[str, list[str]]] = empty_list()
    organization_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    organization_parent: Optional[str] = None
    organization_subsidiaries: Optional[Union[str, list[str]]] = empty_list()
    organization_climate_change_relevant: Optional[Union[bool, Bool]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsOrganizationIsmsId):
            self.isms_id = IsmsOrganizationIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.organization_legal_name is not None and not isinstance(self.organization_legal_name, str):
            self.organization_legal_name = str(self.organization_legal_name)

        if not isinstance(self.organization_trading_names, list):
            self.organization_trading_names = [self.organization_trading_names] if self.organization_trading_names is not None else []
        self.organization_trading_names = [v if isinstance(v, str) else str(v) for v in self.organization_trading_names]

        if self.organization_kind is not None and not isinstance(self.organization_kind, str):
            self.organization_kind = str(self.organization_kind)

        if self.organization_sector is not None and not isinstance(self.organization_sector, str):
            self.organization_sector = str(self.organization_sector)

        if self.organization_size is not None and not isinstance(self.organization_size, str):
            self.organization_size = str(self.organization_size)

        if self.organization_employee_count is not None and not isinstance(self.organization_employee_count, int):
            self.organization_employee_count = int(self.organization_employee_count)

        if not isinstance(self.organization_locations, list):
            self.organization_locations = [self.organization_locations] if self.organization_locations is not None else []
        self.organization_locations = [v if isinstance(v, str) else str(v) for v in self.organization_locations]

        if not isinstance(self.organization_jurisdictions, list):
            self.organization_jurisdictions = [self.organization_jurisdictions] if self.organization_jurisdictions is not None else []
        self.organization_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.organization_jurisdictions]

        if self.organization_parent is not None and not isinstance(self.organization_parent, str):
            self.organization_parent = str(self.organization_parent)

        if not isinstance(self.organization_subsidiaries, list):
            self.organization_subsidiaries = [self.organization_subsidiaries] if self.organization_subsidiaries is not None else []
        self.organization_subsidiaries = [v if isinstance(v, str) else str(v) for v in self.organization_subsidiaries]

        if self.organization_climate_change_relevant is not None and not isinstance(self.organization_climate_change_relevant, Bool):
            self.organization_climate_change_relevant = Bool(self.organization_climate_change_relevant)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsInterestedParty(YAMLRoot):
    """
    A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it,
    such as staff, customers, regulators or suppliers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsInterestedParty"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsInterestedParty"
    class_name: ClassVar[str] = "IsmsInterestedParty"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsInterestedParty

    isms_id: Union[str, IsmsInterestedPartyIsmsId] = None
    title: str = None
    party_category: Optional[str] = None
    party_relationship: Optional[str] = None
    party_requirements: Optional[Union[str, list[str]]] = empty_list()
    party_addressed_requirements: Optional[Union[str, list[str]]] = empty_list()
    party_climate_change_requirements: Optional[Union[str, list[str]]] = empty_list()
    party_communication_needs: Optional[str] = None
    party_contact: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsInterestedPartyIsmsId):
            self.isms_id = IsmsInterestedPartyIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.party_category is not None and not isinstance(self.party_category, str):
            self.party_category = str(self.party_category)

        if self.party_relationship is not None and not isinstance(self.party_relationship, str):
            self.party_relationship = str(self.party_relationship)

        if not isinstance(self.party_requirements, list):
            self.party_requirements = [self.party_requirements] if self.party_requirements is not None else []
        self.party_requirements = [v if isinstance(v, str) else str(v) for v in self.party_requirements]

        if not isinstance(self.party_addressed_requirements, list):
            self.party_addressed_requirements = [self.party_addressed_requirements] if self.party_addressed_requirements is not None else []
        self.party_addressed_requirements = [v if isinstance(v, str) else str(v) for v in self.party_addressed_requirements]

        if not isinstance(self.party_climate_change_requirements, list):
            self.party_climate_change_requirements = [self.party_climate_change_requirements] if self.party_climate_change_requirements is not None else []
        self.party_climate_change_requirements = [v if isinstance(v, str) else str(v) for v in self.party_climate_change_requirements]

        if self.party_communication_needs is not None and not isinstance(self.party_communication_needs, str):
            self.party_communication_needs = str(self.party_communication_needs)

        if self.party_contact is not None and not isinstance(self.party_contact, str):
            self.party_contact = str(self.party_contact)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsPolicy(YAMLRoot):
    """
    The information security policy that top management sets: the organization's commitment and the frame for its
    information security objectives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsPolicy"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsPolicy"
    class_name: ClassVar[str] = "IsmsPolicy"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsPolicy

    isms_id: Union[str, IsmsPolicyIsmsId] = None
    title: str = None
    policy_statement: Optional[str] = None
    policy_objectives_framework: Optional[str] = None
    policy_commitments: Optional[Union[str, list[str]]] = empty_list()
    policy_applicability: Optional[str] = None
    policy_communication_date: Optional[Union[str, XSDDate]] = None
    policy_acknowledgement_required: Optional[Union[bool, Bool]] = None
    policy_management_systems: Optional[Union[Union[str, "IsmsManagementSystemStandard"], list[Union[str, "IsmsManagementSystemStandard"]]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsPolicyIsmsId):
            self.isms_id = IsmsPolicyIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.policy_statement is not None and not isinstance(self.policy_statement, str):
            self.policy_statement = str(self.policy_statement)

        if self.policy_objectives_framework is not None and not isinstance(self.policy_objectives_framework, str):
            self.policy_objectives_framework = str(self.policy_objectives_framework)

        if not isinstance(self.policy_commitments, list):
            self.policy_commitments = [self.policy_commitments] if self.policy_commitments is not None else []
        self.policy_commitments = [v if isinstance(v, str) else str(v) for v in self.policy_commitments]

        if self.policy_applicability is not None and not isinstance(self.policy_applicability, str):
            self.policy_applicability = str(self.policy_applicability)

        if self.policy_communication_date is not None and not isinstance(self.policy_communication_date, XSDDate):
            self.policy_communication_date = XSDDate(self.policy_communication_date)

        if self.policy_acknowledgement_required is not None and not isinstance(self.policy_acknowledgement_required, Bool):
            self.policy_acknowledgement_required = Bool(self.policy_acknowledgement_required)

        if not isinstance(self.policy_management_systems, list):
            self.policy_management_systems = [self.policy_management_systems] if self.policy_management_systems is not None else []
        self.policy_management_systems = [v if isinstance(v, IsmsManagementSystemStandard) else IsmsManagementSystemStandard(v) for v in self.policy_management_systems]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsTopicSpecificPolicy(YAMLRoot):
    """
    A policy on one topic of information security, such as access control or backup, that supports the information
    security policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsTopicSpecificPolicy"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsTopicSpecificPolicy"
    class_name: ClassVar[str] = "IsmsTopicSpecificPolicy"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsTopicSpecificPolicy

    isms_id: Union[str, IsmsTopicSpecificPolicyIsmsId] = None
    title: str = None
    relevant_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    topic_policy_topic: Optional[str] = None
    topic_policy_parent: Optional[Union[str, IsmsPolicyIsmsId]] = None
    topic_policy_audience: Optional[str] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsTopicSpecificPolicyIsmsId):
            self.isms_id = IsmsTopicSpecificPolicyIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.relevant_controls, list):
            self.relevant_controls = [self.relevant_controls] if self.relevant_controls is not None else []
        self.relevant_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.relevant_controls]

        if self.topic_policy_topic is not None and not isinstance(self.topic_policy_topic, str):
            self.topic_policy_topic = str(self.topic_policy_topic)

        if self.topic_policy_parent is not None and not isinstance(self.topic_policy_parent, IsmsPolicyIsmsId):
            self.topic_policy_parent = IsmsPolicyIsmsId(self.topic_policy_parent)

        if self.topic_policy_audience is not None and not isinstance(self.topic_policy_audience, str):
            self.topic_policy_audience = str(self.topic_policy_audience)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRole(YAMLRoot):
    """
    A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRole"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRole"
    class_name: ClassVar[str] = "IsmsRole"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRole

    isms_id: Union[str, IsmsRoleIsmsId] = None
    title: str = None
    role_category: Optional[str] = None
    role_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    role_authorities: Optional[Union[str, list[str]]] = empty_list()
    role_accountability: Optional[str] = None
    role_holders: Optional[Union[str, list[str]]] = empty_list()
    role_delegation: Optional[str] = None
    role_reports_to: Optional[Union[str, IsmsRoleIsmsId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRoleIsmsId):
            self.isms_id = IsmsRoleIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.role_category is not None and not isinstance(self.role_category, str):
            self.role_category = str(self.role_category)

        if not isinstance(self.role_responsibilities, list):
            self.role_responsibilities = [self.role_responsibilities] if self.role_responsibilities is not None else []
        self.role_responsibilities = [v if isinstance(v, str) else str(v) for v in self.role_responsibilities]

        if not isinstance(self.role_authorities, list):
            self.role_authorities = [self.role_authorities] if self.role_authorities is not None else []
        self.role_authorities = [v if isinstance(v, str) else str(v) for v in self.role_authorities]

        if self.role_accountability is not None and not isinstance(self.role_accountability, str):
            self.role_accountability = str(self.role_accountability)

        if not isinstance(self.role_holders, list):
            self.role_holders = [self.role_holders] if self.role_holders is not None else []
        self.role_holders = [v if isinstance(v, str) else str(v) for v in self.role_holders]

        if self.role_delegation is not None and not isinstance(self.role_delegation, str):
            self.role_delegation = str(self.role_delegation)

        if self.role_reports_to is not None and not isinstance(self.role_reports_to, IsmsRoleIsmsId):
            self.role_reports_to = IsmsRoleIsmsId(self.role_reports_to)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsObjective(YAMLRoot):
    """
    An information security objective: a measurable result the organization aims for, with how it plans to reach it
    and how it measures progress.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsObjective"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsObjective"
    class_name: ClassVar[str] = "IsmsObjective"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsObjective

    isms_id: Union[str, IsmsObjectiveIsmsId] = None
    title: str = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    relevant_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    objective_statement: Optional[str] = None
    objective_target: Optional[str] = None
    objective_current_value: Optional[str] = None
    objective_metric: Optional[str] = None
    objective_measurement_method: Optional[str] = None
    objective_measurement_frequency: Optional[str] = None
    objective_target_date: Optional[Union[str, XSDDate]] = None
    objective_achievement: Optional[str] = None
    objective_risks: Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]] = empty_list()
    objective_action_plan: Optional[str] = None
    objective_resources: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsObjectiveIsmsId):
            self.isms_id = IsmsObjectiveIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if not isinstance(self.relevant_controls, list):
            self.relevant_controls = [self.relevant_controls] if self.relevant_controls is not None else []
        self.relevant_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.relevant_controls]

        if self.objective_statement is not None and not isinstance(self.objective_statement, str):
            self.objective_statement = str(self.objective_statement)

        if self.objective_target is not None and not isinstance(self.objective_target, str):
            self.objective_target = str(self.objective_target)

        if self.objective_current_value is not None and not isinstance(self.objective_current_value, str):
            self.objective_current_value = str(self.objective_current_value)

        if self.objective_metric is not None and not isinstance(self.objective_metric, str):
            self.objective_metric = str(self.objective_metric)

        if self.objective_measurement_method is not None and not isinstance(self.objective_measurement_method, str):
            self.objective_measurement_method = str(self.objective_measurement_method)

        if self.objective_measurement_frequency is not None and not isinstance(self.objective_measurement_frequency, str):
            self.objective_measurement_frequency = str(self.objective_measurement_frequency)

        if self.objective_target_date is not None and not isinstance(self.objective_target_date, XSDDate):
            self.objective_target_date = XSDDate(self.objective_target_date)

        if self.objective_achievement is not None and not isinstance(self.objective_achievement, str):
            self.objective_achievement = str(self.objective_achievement)

        if not isinstance(self.objective_risks, list):
            self.objective_risks = [self.objective_risks] if self.objective_risks is not None else []
        self.objective_risks = [v if isinstance(v, IsmsRiskIsmsId) else IsmsRiskIsmsId(v) for v in self.objective_risks]

        if self.objective_action_plan is not None and not isinstance(self.objective_action_plan, str):
            self.objective_action_plan = str(self.objective_action_plan)

        if self.objective_resources is not None and not isinstance(self.objective_resources, str):
            self.objective_resources = str(self.objective_resources)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRiskAssessmentProcess(YAMLRoot):
    """
    The organization's process for assessing information security risks: its criteria for accepting risk and for
    assessing it, its scales and method, and when it runs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRiskAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRiskAssessmentProcess"
    class_name: ClassVar[str] = "IsmsRiskAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRiskAssessmentProcess

    isms_id: Union[str, IsmsRiskAssessmentProcessIsmsId] = None
    title: str = None
    risk_acceptance_criteria: Optional[str] = None
    risk_assessment_criteria: Optional[str] = None
    risk_assessment_method: Optional[str] = None
    risk_likelihood_scale: Optional[str] = None
    risk_impact_scale: Optional[str] = None
    risk_matrix: Optional[str] = None
    risk_assessment_frequency: Optional[str] = None
    risk_assessment_triggers: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRiskAssessmentProcessIsmsId):
            self.isms_id = IsmsRiskAssessmentProcessIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.risk_acceptance_criteria is not None and not isinstance(self.risk_acceptance_criteria, str):
            self.risk_acceptance_criteria = str(self.risk_acceptance_criteria)

        if self.risk_assessment_criteria is not None and not isinstance(self.risk_assessment_criteria, str):
            self.risk_assessment_criteria = str(self.risk_assessment_criteria)

        if self.risk_assessment_method is not None and not isinstance(self.risk_assessment_method, str):
            self.risk_assessment_method = str(self.risk_assessment_method)

        if self.risk_likelihood_scale is not None and not isinstance(self.risk_likelihood_scale, str):
            self.risk_likelihood_scale = str(self.risk_likelihood_scale)

        if self.risk_impact_scale is not None and not isinstance(self.risk_impact_scale, str):
            self.risk_impact_scale = str(self.risk_impact_scale)

        if self.risk_matrix is not None and not isinstance(self.risk_matrix, str):
            self.risk_matrix = str(self.risk_matrix)

        if self.risk_assessment_frequency is not None and not isinstance(self.risk_assessment_frequency, str):
            self.risk_assessment_frequency = str(self.risk_assessment_frequency)

        if not isinstance(self.risk_assessment_triggers, list):
            self.risk_assessment_triggers = [self.risk_assessment_triggers] if self.risk_assessment_triggers is not None else []
        self.risk_assessment_triggers = [v if isinstance(v, str) else str(v) for v in self.risk_assessment_triggers]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRiskAssessment(YAMLRoot):
    """
    One risk assessment carried out under the risk assessment process, and what it found.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRiskAssessment"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRiskAssessment"
    class_name: ClassVar[str] = "IsmsRiskAssessment"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRiskAssessment

    isms_id: Union[str, IsmsRiskAssessmentIsmsId] = None
    title: str = None
    assessment_scope: Optional[str] = None
    assessment_date: Optional[Union[str, XSDDate]] = None
    assessment_assessor: Optional[str] = None
    assessment_method_used: Optional[str] = None
    assessment_risks: Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]] = empty_list()
    assessment_summary: Optional[str] = None
    assessment_recommendations: Optional[Union[str, list[str]]] = empty_list()
    assessment_next_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRiskAssessmentIsmsId):
            self.isms_id = IsmsRiskAssessmentIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.assessment_scope is not None and not isinstance(self.assessment_scope, str):
            self.assessment_scope = str(self.assessment_scope)

        if self.assessment_date is not None and not isinstance(self.assessment_date, XSDDate):
            self.assessment_date = XSDDate(self.assessment_date)

        if self.assessment_assessor is not None and not isinstance(self.assessment_assessor, str):
            self.assessment_assessor = str(self.assessment_assessor)

        if self.assessment_method_used is not None and not isinstance(self.assessment_method_used, str):
            self.assessment_method_used = str(self.assessment_method_used)

        if not isinstance(self.assessment_risks, list):
            self.assessment_risks = [self.assessment_risks] if self.assessment_risks is not None else []
        self.assessment_risks = [v if isinstance(v, IsmsRiskIsmsId) else IsmsRiskIsmsId(v) for v in self.assessment_risks]

        if self.assessment_summary is not None and not isinstance(self.assessment_summary, str):
            self.assessment_summary = str(self.assessment_summary)

        if not isinstance(self.assessment_recommendations, list):
            self.assessment_recommendations = [self.assessment_recommendations] if self.assessment_recommendations is not None else []
        self.assessment_recommendations = [v if isinstance(v, str) else str(v) for v in self.assessment_recommendations]

        if self.assessment_next_date is not None and not isinstance(self.assessment_next_date, XSDDate):
            self.assessment_next_date = XSDDate(self.assessment_next_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRisk(YAMLRoot):
    """
    An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is
    rated before and after controls, and how it is treated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRisk"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRisk"
    class_name: ClassVar[str] = "IsmsRisk"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRisk

    isms_id: Union[str, IsmsRiskIsmsId] = None
    title: str = None
    affected_assets: Optional[Union[Union[str, IsmsAssetIsmsId], list[Union[str, IsmsAssetIsmsId]]]] = empty_list()
    affected_security_properties: Optional[Union[Union[str, "IsmsSecurityProperty"], list[Union[str, "IsmsSecurityProperty"]]]] = empty_list()
    risk_source: Optional[str] = None
    risk_threat: Optional[str] = None
    risk_vulnerability: Optional[str] = None
    risk_owner: Optional[str] = None
    risk_likelihood: Optional[Union[str, "IsmsLikelihood"]] = None
    risk_impact: Optional[Union[str, "IsmsImpact"]] = None
    risk_inherent_level: Optional[Union[str, "IsmsRiskLevel"]] = None
    risk_existing_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    risk_residual_level: Optional[Union[str, "IsmsRiskLevel"]] = None
    risk_treatment_option: Optional[Union[str, "IsmsRiskTreatmentOption"]] = None
    risk_treatment_priority: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRiskIsmsId):
            self.isms_id = IsmsRiskIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.affected_assets, list):
            self.affected_assets = [self.affected_assets] if self.affected_assets is not None else []
        self.affected_assets = [v if isinstance(v, IsmsAssetIsmsId) else IsmsAssetIsmsId(v) for v in self.affected_assets]

        if not isinstance(self.affected_security_properties, list):
            self.affected_security_properties = [self.affected_security_properties] if self.affected_security_properties is not None else []
        self.affected_security_properties = [v if isinstance(v, IsmsSecurityProperty) else IsmsSecurityProperty(v) for v in self.affected_security_properties]

        if self.risk_source is not None and not isinstance(self.risk_source, str):
            self.risk_source = str(self.risk_source)

        if self.risk_threat is not None and not isinstance(self.risk_threat, str):
            self.risk_threat = str(self.risk_threat)

        if self.risk_vulnerability is not None and not isinstance(self.risk_vulnerability, str):
            self.risk_vulnerability = str(self.risk_vulnerability)

        if self.risk_owner is not None and not isinstance(self.risk_owner, str):
            self.risk_owner = str(self.risk_owner)

        if self.risk_likelihood is not None and not isinstance(self.risk_likelihood, IsmsLikelihood):
            self.risk_likelihood = IsmsLikelihood(self.risk_likelihood)

        if self.risk_impact is not None and not isinstance(self.risk_impact, IsmsImpact):
            self.risk_impact = IsmsImpact(self.risk_impact)

        if self.risk_inherent_level is not None and not isinstance(self.risk_inherent_level, IsmsRiskLevel):
            self.risk_inherent_level = IsmsRiskLevel(self.risk_inherent_level)

        if not isinstance(self.risk_existing_controls, list):
            self.risk_existing_controls = [self.risk_existing_controls] if self.risk_existing_controls is not None else []
        self.risk_existing_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.risk_existing_controls]

        if self.risk_residual_level is not None and not isinstance(self.risk_residual_level, IsmsRiskLevel):
            self.risk_residual_level = IsmsRiskLevel(self.risk_residual_level)

        if self.risk_treatment_option is not None and not isinstance(self.risk_treatment_option, IsmsRiskTreatmentOption):
            self.risk_treatment_option = IsmsRiskTreatmentOption(self.risk_treatment_option)

        if self.risk_treatment_priority is not None and not isinstance(self.risk_treatment_priority, str):
            self.risk_treatment_priority = str(self.risk_treatment_priority)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRiskTreatmentProcess(YAMLRoot):
    """
    The organization's process for treating information security risks: how it chooses treatments and controls, checks
    them against Annex A, and produces the Statement of Applicability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRiskTreatmentProcess"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRiskTreatmentProcess"
    class_name: ClassVar[str] = "IsmsRiskTreatmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRiskTreatmentProcess

    isms_id: Union[str, IsmsRiskTreatmentProcessIsmsId] = None
    title: str = None
    treatment_options_guidance: Optional[str] = None
    treatment_control_selection: Optional[str] = None
    treatment_annex_a_comparison: Optional[str] = None
    treatment_soa_template: Optional[str] = None
    treatment_approval_workflow: Optional[str] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRiskTreatmentProcessIsmsId):
            self.isms_id = IsmsRiskTreatmentProcessIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.treatment_options_guidance is not None and not isinstance(self.treatment_options_guidance, str):
            self.treatment_options_guidance = str(self.treatment_options_guidance)

        if self.treatment_control_selection is not None and not isinstance(self.treatment_control_selection, str):
            self.treatment_control_selection = str(self.treatment_control_selection)

        if self.treatment_annex_a_comparison is not None and not isinstance(self.treatment_annex_a_comparison, str):
            self.treatment_annex_a_comparison = str(self.treatment_annex_a_comparison)

        if self.treatment_soa_template is not None and not isinstance(self.treatment_soa_template, str):
            self.treatment_soa_template = str(self.treatment_soa_template)

        if self.treatment_approval_workflow is not None and not isinstance(self.treatment_approval_workflow, str):
            self.treatment_approval_workflow = str(self.treatment_approval_workflow)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsRiskTreatmentPlan(YAMLRoot):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's
    approval of the plan and of the residual risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsRiskTreatmentPlan"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsRiskTreatmentPlan"
    class_name: ClassVar[str] = "IsmsRiskTreatmentPlan"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsRiskTreatmentPlan

    isms_id: Union[str, IsmsRiskTreatmentPlanIsmsId] = None
    title: str = None
    implementation_state: Optional[Union[str, "IsmsImplementationStatus"]] = None
    plan_scope: Optional[str] = None
    plan_risks: Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]] = empty_list()
    plan_actions: Optional[Union[str, list[str]]] = empty_list()
    plan_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    plan_resources: Optional[str] = None
    plan_responsible_parties: Optional[Union[str, list[str]]] = empty_list()
    plan_timeline: Optional[str] = None
    plan_risk_owner_approval: Optional[str] = None
    plan_residual_risk_acceptance: Optional[str] = None
    plan_completion_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsRiskTreatmentPlanIsmsId):
            self.isms_id = IsmsRiskTreatmentPlanIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.implementation_state is not None and not isinstance(self.implementation_state, IsmsImplementationStatus):
            self.implementation_state = IsmsImplementationStatus(self.implementation_state)

        if self.plan_scope is not None and not isinstance(self.plan_scope, str):
            self.plan_scope = str(self.plan_scope)

        if not isinstance(self.plan_risks, list):
            self.plan_risks = [self.plan_risks] if self.plan_risks is not None else []
        self.plan_risks = [v if isinstance(v, IsmsRiskIsmsId) else IsmsRiskIsmsId(v) for v in self.plan_risks]

        if not isinstance(self.plan_actions, list):
            self.plan_actions = [self.plan_actions] if self.plan_actions is not None else []
        self.plan_actions = [v if isinstance(v, str) else str(v) for v in self.plan_actions]

        if not isinstance(self.plan_controls, list):
            self.plan_controls = [self.plan_controls] if self.plan_controls is not None else []
        self.plan_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.plan_controls]

        if self.plan_resources is not None and not isinstance(self.plan_resources, str):
            self.plan_resources = str(self.plan_resources)

        if not isinstance(self.plan_responsible_parties, list):
            self.plan_responsible_parties = [self.plan_responsible_parties] if self.plan_responsible_parties is not None else []
        self.plan_responsible_parties = [v if isinstance(v, str) else str(v) for v in self.plan_responsible_parties]

        if self.plan_timeline is not None and not isinstance(self.plan_timeline, str):
            self.plan_timeline = str(self.plan_timeline)

        if self.plan_risk_owner_approval is not None and not isinstance(self.plan_risk_owner_approval, str):
            self.plan_risk_owner_approval = str(self.plan_risk_owner_approval)

        if self.plan_residual_risk_acceptance is not None and not isinstance(self.plan_residual_risk_acceptance, str):
            self.plan_residual_risk_acceptance = str(self.plan_residual_risk_acceptance)

        if self.plan_completion_date is not None and not isinstance(self.plan_completion_date, XSDDate):
            self.plan_completion_date = XSDDate(self.plan_completion_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsStatementOfApplicability(YAMLRoot):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in
    place, and each Annex A control it leaves out, with why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsStatementOfApplicability"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsStatementOfApplicability"
    class_name: ClassVar[str] = "IsmsStatementOfApplicability"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsStatementOfApplicability

    isms_id: Union[str, IsmsStatementOfApplicabilityIsmsId] = None
    title: str = None
    soa_entries: Optional[Union[Union[dict, "IsmsApplicabilityEntry"], list[Union[dict, "IsmsApplicabilityEntry"]]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsStatementOfApplicabilityIsmsId):
            self.isms_id = IsmsStatementOfApplicabilityIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="soa_entries", slot_type=IsmsApplicabilityEntry, key_name="entry_justification", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsApplicabilityEntry(YAMLRoot):
    """
    One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and
    says why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsApplicabilityEntry"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsApplicabilityEntry"
    class_name: ClassVar[str] = "IsmsApplicabilityEntry"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsApplicabilityEntry

    entry_justification: str = None
    entry_annex_a_control: Optional[Union[str, "IsmsAnnexAControl"]] = None
    entry_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entry_justification):
            self.MissingRequiredField("entry_justification")
        if not isinstance(self.entry_justification, str):
            self.entry_justification = str(self.entry_justification)

        if self.entry_annex_a_control is not None and not isinstance(self.entry_annex_a_control, IsmsAnnexAControl):
            self.entry_annex_a_control = IsmsAnnexAControl(self.entry_annex_a_control)

        self.entry_type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_entry_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "entry_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class IsmsIncludedControl(IsmsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in
    place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsIncludedControl"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsIncludedControl"
    class_name: ClassVar[str] = "IsmsIncludedControl"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsIncludedControl

    entry_justification: str = None
    implementation_state: Union[str, "IsmsImplementationStatus"] = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    included_control: Optional[Union[str, IsmsControlIsmsId]] = None
    included_evidence: Optional[str] = None
    included_target_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.implementation_state):
            self.MissingRequiredField("implementation_state")
        if not isinstance(self.implementation_state, IsmsImplementationStatus):
            self.implementation_state = IsmsImplementationStatus(self.implementation_state)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if self.included_control is not None and not isinstance(self.included_control, IsmsControlIsmsId):
            self.included_control = IsmsControlIsmsId(self.included_control)

        if self.included_evidence is not None and not isinstance(self.included_evidence, str):
            self.included_evidence = str(self.included_evidence)

        if self.included_target_date is not None and not isinstance(self.included_target_date, XSDDate):
            self.included_target_date = XSDDate(self.included_target_date)

        super().__post_init__(**kwargs)
        self.unknown_entry_type = str(self.class_name)


@dataclass(repr=False)
class IsmsExcludedControl(IsmsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsExcludedControl"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsExcludedControl"
    class_name: ClassVar[str] = "IsmsExcludedControl"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsExcludedControl

    entry_justification: str = None
    entry_annex_a_control: Union[str, "IsmsAnnexAControl"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entry_annex_a_control):
            self.MissingRequiredField("entry_annex_a_control")
        if not isinstance(self.entry_annex_a_control, IsmsAnnexAControl):
            self.entry_annex_a_control = IsmsAnnexAControl(self.entry_annex_a_control)

        super().__post_init__(**kwargs)
        self.unknown_entry_type = str(self.class_name)


@dataclass(repr=False)
class IsmsControl(YAMLRoot):
    """
    A control the organization has determined it needs to treat its risks. It records what the control does in the
    organization's words and which Annex A controls it answers to. It also records who owns it, how far it is in place
    and how well it works.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsControl"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsControl"
    class_name: ClassVar[str] = "IsmsControl"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsControl

    isms_id: Union[str, IsmsControlIsmsId] = None
    title: str = None
    relevant_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    implementation_state: Optional[Union[str, "IsmsImplementationStatus"]] = None
    control_annex_a_controls: Optional[Union[Union[str, "IsmsAnnexAControl"], list[Union[str, "IsmsAnnexAControl"]]]] = empty_list()
    control_theme: Optional[Union[str, "IsmsControlTheme"]] = None
    control_text: Optional[str] = None
    control_guidance: Optional[str] = None
    control_threats: Optional[Union[str, list[str]]] = empty_list()
    control_asset_types: Optional[Union[str, list[str]]] = empty_list()
    control_owner: Optional[str] = None
    control_implementation_date: Optional[Union[str, XSDDate]] = None
    control_effectiveness: Optional[str] = None
    control_last_tested: Optional[Union[str, XSDDate]] = None
    control_evidence: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsControlIsmsId):
            self.isms_id = IsmsControlIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.relevant_controls, list):
            self.relevant_controls = [self.relevant_controls] if self.relevant_controls is not None else []
        self.relevant_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.relevant_controls]

        if self.implementation_state is not None and not isinstance(self.implementation_state, IsmsImplementationStatus):
            self.implementation_state = IsmsImplementationStatus(self.implementation_state)

        if not isinstance(self.control_annex_a_controls, list):
            self.control_annex_a_controls = [self.control_annex_a_controls] if self.control_annex_a_controls is not None else []
        self.control_annex_a_controls = [v if isinstance(v, IsmsAnnexAControl) else IsmsAnnexAControl(v) for v in self.control_annex_a_controls]

        if self.control_theme is not None and not isinstance(self.control_theme, IsmsControlTheme):
            self.control_theme = IsmsControlTheme(self.control_theme)

        if self.control_text is not None and not isinstance(self.control_text, str):
            self.control_text = str(self.control_text)

        if self.control_guidance is not None and not isinstance(self.control_guidance, str):
            self.control_guidance = str(self.control_guidance)

        if not isinstance(self.control_threats, list):
            self.control_threats = [self.control_threats] if self.control_threats is not None else []
        self.control_threats = [v if isinstance(v, str) else str(v) for v in self.control_threats]

        if not isinstance(self.control_asset_types, list):
            self.control_asset_types = [self.control_asset_types] if self.control_asset_types is not None else []
        self.control_asset_types = [v if isinstance(v, str) else str(v) for v in self.control_asset_types]

        if self.control_owner is not None and not isinstance(self.control_owner, str):
            self.control_owner = str(self.control_owner)

        if self.control_implementation_date is not None and not isinstance(self.control_implementation_date, XSDDate):
            self.control_implementation_date = XSDDate(self.control_implementation_date)

        if self.control_effectiveness is not None and not isinstance(self.control_effectiveness, str):
            self.control_effectiveness = str(self.control_effectiveness)

        if self.control_last_tested is not None and not isinstance(self.control_last_tested, XSDDate):
            self.control_last_tested = XSDDate(self.control_last_tested)

        if not isinstance(self.control_evidence, list):
            self.control_evidence = [self.control_evidence] if self.control_evidence is not None else []
        self.control_evidence = [v if isinstance(v, str) else str(v) for v in self.control_evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsAsset(YAMLRoot):
    """
    An item in the inventory of information and other associated assets: what it is, who owns and looks after it,
    where it is, how it is classified and how much it matters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsAsset"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsAsset"
    class_name: ClassVar[str] = "IsmsAsset"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsAsset

    isms_id: Union[str, IsmsAssetIsmsId] = None
    title: str = None
    relevant_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    asset_category: Optional[str] = None
    asset_owner: Optional[str] = None
    asset_custodian: Optional[str] = None
    asset_classification: Optional[str] = None
    asset_location: Optional[str] = None
    asset_criticality: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsAssetIsmsId):
            self.isms_id = IsmsAssetIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.relevant_controls, list):
            self.relevant_controls = [self.relevant_controls] if self.relevant_controls is not None else []
        self.relevant_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.relevant_controls]

        if self.asset_category is not None and not isinstance(self.asset_category, str):
            self.asset_category = str(self.asset_category)

        if self.asset_owner is not None and not isinstance(self.asset_owner, str):
            self.asset_owner = str(self.asset_owner)

        if self.asset_custodian is not None and not isinstance(self.asset_custodian, str):
            self.asset_custodian = str(self.asset_custodian)

        if self.asset_classification is not None and not isinstance(self.asset_classification, str):
            self.asset_classification = str(self.asset_classification)

        if self.asset_location is not None and not isinstance(self.asset_location, str):
            self.asset_location = str(self.asset_location)

        if self.asset_criticality is not None and not isinstance(self.asset_criticality, str):
            self.asset_criticality = str(self.asset_criticality)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsResource(YAMLRoot):
    """
    A resource provided for the ISMS, such as people, time, tools or budget.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsResource"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsResource"
    class_name: ClassVar[str] = "IsmsResource"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsResource

    isms_id: Union[str, IsmsResourceIsmsId] = None
    title: str = None
    resource_category: Optional[str] = None
    resource_quantity: Optional[str] = None
    resource_allocation_date: Optional[Union[str, XSDDate]] = None
    resource_allocated_to: Optional[str] = None
    resource_cost: Optional[str] = None
    resource_availability: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsResourceIsmsId):
            self.isms_id = IsmsResourceIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.resource_category is not None and not isinstance(self.resource_category, str):
            self.resource_category = str(self.resource_category)

        if self.resource_quantity is not None and not isinstance(self.resource_quantity, str):
            self.resource_quantity = str(self.resource_quantity)

        if self.resource_allocation_date is not None and not isinstance(self.resource_allocation_date, XSDDate):
            self.resource_allocation_date = XSDDate(self.resource_allocation_date)

        if self.resource_allocated_to is not None and not isinstance(self.resource_allocated_to, str):
            self.resource_allocated_to = str(self.resource_allocated_to)

        if self.resource_cost is not None and not isinstance(self.resource_cost, str):
            self.resource_cost = str(self.resource_cost)

        if self.resource_availability is not None and not isinstance(self.resource_availability, str):
            self.resource_availability = str(self.resource_availability)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsCompetenceRecord(YAMLRoot):
    """
    The evidence of one person's competence for work that affects information security, and what is done to close any
    gap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsCompetenceRecord"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsCompetenceRecord"
    class_name: ClassVar[str] = "IsmsCompetenceRecord"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsCompetenceRecord

    isms_id: Union[str, IsmsCompetenceRecordIsmsId] = None
    title: str = None
    competence_person: Optional[str] = None
    competence_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    competence_required: Optional[Union[str, list[str]]] = empty_list()
    competence_education: Optional[Union[str, list[str]]] = empty_list()
    competence_training: Optional[Union[str, list[str]]] = empty_list()
    competence_experience: Optional[Union[str, list[str]]] = empty_list()
    competence_assessment_date: Optional[Union[str, XSDDate]] = None
    competence_gaps: Optional[Union[str, list[str]]] = empty_list()
    competence_actions: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsCompetenceRecordIsmsId):
            self.isms_id = IsmsCompetenceRecordIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.competence_person is not None and not isinstance(self.competence_person, str):
            self.competence_person = str(self.competence_person)

        if self.competence_role is not None and not isinstance(self.competence_role, IsmsRoleIsmsId):
            self.competence_role = IsmsRoleIsmsId(self.competence_role)

        if not isinstance(self.competence_required, list):
            self.competence_required = [self.competence_required] if self.competence_required is not None else []
        self.competence_required = [v if isinstance(v, str) else str(v) for v in self.competence_required]

        if not isinstance(self.competence_education, list):
            self.competence_education = [self.competence_education] if self.competence_education is not None else []
        self.competence_education = [v if isinstance(v, str) else str(v) for v in self.competence_education]

        if not isinstance(self.competence_training, list):
            self.competence_training = [self.competence_training] if self.competence_training is not None else []
        self.competence_training = [v if isinstance(v, str) else str(v) for v in self.competence_training]

        if not isinstance(self.competence_experience, list):
            self.competence_experience = [self.competence_experience] if self.competence_experience is not None else []
        self.competence_experience = [v if isinstance(v, str) else str(v) for v in self.competence_experience]

        if self.competence_assessment_date is not None and not isinstance(self.competence_assessment_date, XSDDate):
            self.competence_assessment_date = XSDDate(self.competence_assessment_date)

        if not isinstance(self.competence_gaps, list):
            self.competence_gaps = [self.competence_gaps] if self.competence_gaps is not None else []
        self.competence_gaps = [v if isinstance(v, str) else str(v) for v in self.competence_gaps]

        if not isinstance(self.competence_actions, list):
            self.competence_actions = [self.competence_actions] if self.competence_actions is not None else []
        self.competence_actions = [v if isinstance(v, str) else str(v) for v in self.competence_actions]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsAwarenessProgramme(YAMLRoot):
    """
    The programme that makes people working for the organization aware of the policy, their part in the ISMS and what
    failing it would mean.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsAwarenessProgramme"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsAwarenessProgramme"
    class_name: ClassVar[str] = "IsmsAwarenessProgramme"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsAwarenessProgramme

    isms_id: Union[str, IsmsAwarenessProgrammeIsmsId] = None
    title: str = None
    awareness_topics: Optional[Union[str, list[str]]] = empty_list()
    awareness_methods: Optional[Union[str, list[str]]] = empty_list()
    awareness_audience: Optional[str] = None
    awareness_frequency: Optional[str] = None
    awareness_completion_tracking: Optional[str] = None
    awareness_effectiveness: Optional[str] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsAwarenessProgrammeIsmsId):
            self.isms_id = IsmsAwarenessProgrammeIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.awareness_topics, list):
            self.awareness_topics = [self.awareness_topics] if self.awareness_topics is not None else []
        self.awareness_topics = [v if isinstance(v, str) else str(v) for v in self.awareness_topics]

        if not isinstance(self.awareness_methods, list):
            self.awareness_methods = [self.awareness_methods] if self.awareness_methods is not None else []
        self.awareness_methods = [v if isinstance(v, str) else str(v) for v in self.awareness_methods]

        if self.awareness_audience is not None and not isinstance(self.awareness_audience, str):
            self.awareness_audience = str(self.awareness_audience)

        if self.awareness_frequency is not None and not isinstance(self.awareness_frequency, str):
            self.awareness_frequency = str(self.awareness_frequency)

        if self.awareness_completion_tracking is not None and not isinstance(self.awareness_completion_tracking, str):
            self.awareness_completion_tracking = str(self.awareness_completion_tracking)

        if self.awareness_effectiveness is not None and not isinstance(self.awareness_effectiveness, str):
            self.awareness_effectiveness = str(self.awareness_effectiveness)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsCommunicationPlan(YAMLRoot):
    """
    The plan for communication about the ISMS, inside the organization and outside it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsCommunicationPlan"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsCommunicationPlan"
    class_name: ClassVar[str] = "IsmsCommunicationPlan"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsCommunicationPlan

    isms_id: Union[str, IsmsCommunicationPlanIsmsId] = None
    title: str = None
    communication_items: Optional[Union[Union[dict, "IsmsCommunication"], list[Union[dict, "IsmsCommunication"]]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsCommunicationPlanIsmsId):
            self.isms_id = IsmsCommunicationPlanIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="communication_items", slot_type=IsmsCommunication, key_name="communication_subject", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsCommunication(YAMLRoot):
    """
    One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsCommunication"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsCommunication"
    class_name: ClassVar[str] = "IsmsCommunication"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsCommunication

    communication_subject: str = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    communication_purpose: Optional[str] = None
    communication_audience: Optional[str] = None
    communication_frequency: Optional[str] = None
    communication_method: Optional[str] = None
    communication_records_required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.communication_subject):
            self.MissingRequiredField("communication_subject")
        if not isinstance(self.communication_subject, str):
            self.communication_subject = str(self.communication_subject)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if self.communication_purpose is not None and not isinstance(self.communication_purpose, str):
            self.communication_purpose = str(self.communication_purpose)

        if self.communication_audience is not None and not isinstance(self.communication_audience, str):
            self.communication_audience = str(self.communication_audience)

        if self.communication_frequency is not None and not isinstance(self.communication_frequency, str):
            self.communication_frequency = str(self.communication_frequency)

        if self.communication_method is not None and not isinstance(self.communication_method, str):
            self.communication_method = str(self.communication_method)

        if self.communication_records_required is not None and not isinstance(self.communication_records_required, Bool):
            self.communication_records_required = Bool(self.communication_records_required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsDocumentedInformation(YAMLRoot):
    """
    A piece of documented information the ISMS keeps under control that no more specific record describes, such as a
    procedure, a standard, a plan or a report.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsDocumentedInformation"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsDocumentedInformation"
    class_name: ClassVar[str] = "IsmsDocumentedInformation"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsDocumentedInformation

    isms_id: Union[str, IsmsDocumentedInformationIsmsId] = None
    document_kind: Union[str, "IsmsDocumentKind"] = None
    title: str = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsDocumentedInformationIsmsId):
            self.isms_id = IsmsDocumentedInformationIsmsId(self.isms_id)

        if self._is_empty(self.document_kind):
            self.MissingRequiredField("document_kind")
        if not isinstance(self.document_kind, IsmsDocumentKind):
            self.document_kind = IsmsDocumentKind(self.document_kind)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsOperationalProcedure(YAMLRoot):
    """
    A procedure by which the organization plans and controls the processes that meet its information security
    requirements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsOperationalProcedure"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsOperationalProcedure"
    class_name: ClassVar[str] = "IsmsOperationalProcedure"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsOperationalProcedure

    isms_id: Union[str, IsmsOperationalProcedureIsmsId] = None
    title: str = None
    relevant_controls: Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]] = empty_list()
    procedure_scope: Optional[str] = None
    procedure_criteria: Optional[str] = None
    procedure_control_measures: Optional[Union[str, list[str]]] = empty_list()
    procedure_roles: Optional[Union[Union[str, IsmsRoleIsmsId], list[Union[str, IsmsRoleIsmsId]]]] = empty_list()
    procedure_change_control: Optional[str] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsOperationalProcedureIsmsId):
            self.isms_id = IsmsOperationalProcedureIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.relevant_controls, list):
            self.relevant_controls = [self.relevant_controls] if self.relevant_controls is not None else []
        self.relevant_controls = [v if isinstance(v, IsmsControlIsmsId) else IsmsControlIsmsId(v) for v in self.relevant_controls]

        if self.procedure_scope is not None and not isinstance(self.procedure_scope, str):
            self.procedure_scope = str(self.procedure_scope)

        if self.procedure_criteria is not None and not isinstance(self.procedure_criteria, str):
            self.procedure_criteria = str(self.procedure_criteria)

        if not isinstance(self.procedure_control_measures, list):
            self.procedure_control_measures = [self.procedure_control_measures] if self.procedure_control_measures is not None else []
        self.procedure_control_measures = [v if isinstance(v, str) else str(v) for v in self.procedure_control_measures]

        if not isinstance(self.procedure_roles, list):
            self.procedure_roles = [self.procedure_roles] if self.procedure_roles is not None else []
        self.procedure_roles = [v if isinstance(v, IsmsRoleIsmsId) else IsmsRoleIsmsId(v) for v in self.procedure_roles]

        if self.procedure_change_control is not None and not isinstance(self.procedure_change_control, str):
            self.procedure_change_control = str(self.procedure_change_control)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsMonitoringProgramme(YAMLRoot):
    """
    The programme of monitoring, measurement, analysis and evaluation of information security performance and of the
    ISMS's effectiveness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsMonitoringProgramme"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsMonitoringProgramme"
    class_name: ClassVar[str] = "IsmsMonitoringProgramme"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsMonitoringProgramme

    isms_id: Union[str, IsmsMonitoringProgrammeIsmsId] = None
    title: str = None
    monitoring_items: Optional[Union[Union[dict, "IsmsMonitoringItem"], list[Union[dict, "IsmsMonitoringItem"]]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsMonitoringProgrammeIsmsId):
            self.isms_id = IsmsMonitoringProgrammeIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="monitoring_items", slot_type=IsmsMonitoringItem, key_name="monitoring_metric", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsMonitoringItem(YAMLRoot):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and
    against what thresholds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsMonitoringItem"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsMonitoringItem"
    class_name: ClassVar[str] = "IsmsMonitoringItem"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsMonitoringItem

    monitoring_metric: str = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    monitoring_description: Optional[str] = None
    monitoring_method: Optional[str] = None
    monitoring_frequency: Optional[str] = None
    monitoring_analysis_frequency: Optional[str] = None
    monitoring_analyst: Optional[str] = None
    monitoring_target: Optional[str] = None
    monitoring_alert_threshold: Optional[str] = None
    monitoring_current_value: Optional[str] = None
    monitoring_trend: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.monitoring_metric):
            self.MissingRequiredField("monitoring_metric")
        if not isinstance(self.monitoring_metric, str):
            self.monitoring_metric = str(self.monitoring_metric)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if self.monitoring_description is not None and not isinstance(self.monitoring_description, str):
            self.monitoring_description = str(self.monitoring_description)

        if self.monitoring_method is not None and not isinstance(self.monitoring_method, str):
            self.monitoring_method = str(self.monitoring_method)

        if self.monitoring_frequency is not None and not isinstance(self.monitoring_frequency, str):
            self.monitoring_frequency = str(self.monitoring_frequency)

        if self.monitoring_analysis_frequency is not None and not isinstance(self.monitoring_analysis_frequency, str):
            self.monitoring_analysis_frequency = str(self.monitoring_analysis_frequency)

        if self.monitoring_analyst is not None and not isinstance(self.monitoring_analyst, str):
            self.monitoring_analyst = str(self.monitoring_analyst)

        if self.monitoring_target is not None and not isinstance(self.monitoring_target, str):
            self.monitoring_target = str(self.monitoring_target)

        if self.monitoring_alert_threshold is not None and not isinstance(self.monitoring_alert_threshold, str):
            self.monitoring_alert_threshold = str(self.monitoring_alert_threshold)

        if self.monitoring_current_value is not None and not isinstance(self.monitoring_current_value, str):
            self.monitoring_current_value = str(self.monitoring_current_value)

        if self.monitoring_trend is not None and not isinstance(self.monitoring_trend, str):
            self.monitoring_trend = str(self.monitoring_trend)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsAuditProgramme(YAMLRoot):
    """
    An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors
    they need.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsAuditProgramme"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsAuditProgramme"
    class_name: ClassVar[str] = "IsmsAuditProgramme"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsAuditProgramme

    isms_id: Union[str, IsmsAuditProgrammeIsmsId] = None
    title: str = None
    programme_period: Optional[str] = None
    programme_audits: Optional[Union[Union[str, IsmsAuditIsmsId], list[Union[str, IsmsAuditIsmsId]]]] = empty_list()
    programme_frequency_rationale: Optional[str] = None
    programme_resources: Optional[str] = None
    programme_auditor_qualifications: Optional[str] = None
    programme_status: Optional[str] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsAuditProgrammeIsmsId):
            self.isms_id = IsmsAuditProgrammeIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.programme_period is not None and not isinstance(self.programme_period, str):
            self.programme_period = str(self.programme_period)

        if not isinstance(self.programme_audits, list):
            self.programme_audits = [self.programme_audits] if self.programme_audits is not None else []
        self.programme_audits = [v if isinstance(v, IsmsAuditIsmsId) else IsmsAuditIsmsId(v) for v in self.programme_audits]

        if self.programme_frequency_rationale is not None and not isinstance(self.programme_frequency_rationale, str):
            self.programme_frequency_rationale = str(self.programme_frequency_rationale)

        if self.programme_resources is not None and not isinstance(self.programme_resources, str):
            self.programme_resources = str(self.programme_resources)

        if self.programme_auditor_qualifications is not None and not isinstance(self.programme_auditor_qualifications, str):
            self.programme_auditor_qualifications = str(self.programme_auditor_qualifications)

        if self.programme_status is not None and not isinstance(self.programme_status, str):
            self.programme_status = str(self.programme_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsAudit(YAMLRoot):
    """
    An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope,
    criteria, team, findings and conclusion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsAudit"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsAudit"
    class_name: ClassVar[str] = "IsmsAudit"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsAudit

    isms_id: Union[str, IsmsAuditIsmsId] = None
    audit_type: Union[str, "IsmsAuditType"] = None
    title: str = None
    audit_standards: Optional[Union[Union[str, "IsmsManagementSystemStandard"], list[Union[str, "IsmsManagementSystemStandard"]]]] = empty_list()
    audit_scope: Optional[str] = None
    audit_criteria: Optional[Union[str, list[str]]] = empty_list()
    audit_objectives: Optional[Union[str, list[str]]] = empty_list()
    audit_period_start: Optional[Union[str, XSDDate]] = None
    audit_period_end: Optional[Union[str, XSDDate]] = None
    audit_lead: Optional[str] = None
    audit_team: Optional[Union[str, list[str]]] = empty_list()
    audit_auditees: Optional[Union[str, list[str]]] = empty_list()
    audit_plan: Optional[Union[str, IsmsDocumentedInformationIsmsId]] = None
    audit_findings: Optional[Union[dict[Union[str, IsmsAuditFindingIsmsId], Union[dict, "IsmsAuditFinding"]], list[Union[dict, "IsmsAuditFinding"]]]] = empty_dict()
    audit_conclusion: Optional[str] = None
    audit_report_date: Optional[Union[str, XSDDate]] = None
    audit_report_distribution: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsAuditIsmsId):
            self.isms_id = IsmsAuditIsmsId(self.isms_id)

        if self._is_empty(self.audit_type):
            self.MissingRequiredField("audit_type")
        if not isinstance(self.audit_type, IsmsAuditType):
            self.audit_type = IsmsAuditType(self.audit_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.audit_standards, list):
            self.audit_standards = [self.audit_standards] if self.audit_standards is not None else []
        self.audit_standards = [v if isinstance(v, IsmsManagementSystemStandard) else IsmsManagementSystemStandard(v) for v in self.audit_standards]

        if self.audit_scope is not None and not isinstance(self.audit_scope, str):
            self.audit_scope = str(self.audit_scope)

        if not isinstance(self.audit_criteria, list):
            self.audit_criteria = [self.audit_criteria] if self.audit_criteria is not None else []
        self.audit_criteria = [v if isinstance(v, str) else str(v) for v in self.audit_criteria]

        if not isinstance(self.audit_objectives, list):
            self.audit_objectives = [self.audit_objectives] if self.audit_objectives is not None else []
        self.audit_objectives = [v if isinstance(v, str) else str(v) for v in self.audit_objectives]

        if self.audit_period_start is not None and not isinstance(self.audit_period_start, XSDDate):
            self.audit_period_start = XSDDate(self.audit_period_start)

        if self.audit_period_end is not None and not isinstance(self.audit_period_end, XSDDate):
            self.audit_period_end = XSDDate(self.audit_period_end)

        if self.audit_lead is not None and not isinstance(self.audit_lead, str):
            self.audit_lead = str(self.audit_lead)

        if not isinstance(self.audit_team, list):
            self.audit_team = [self.audit_team] if self.audit_team is not None else []
        self.audit_team = [v if isinstance(v, str) else str(v) for v in self.audit_team]

        if not isinstance(self.audit_auditees, list):
            self.audit_auditees = [self.audit_auditees] if self.audit_auditees is not None else []
        self.audit_auditees = [v if isinstance(v, str) else str(v) for v in self.audit_auditees]

        if self.audit_plan is not None and not isinstance(self.audit_plan, IsmsDocumentedInformationIsmsId):
            self.audit_plan = IsmsDocumentedInformationIsmsId(self.audit_plan)

        self._normalize_inlined_as_list(slot_name="audit_findings", slot_type=IsmsAuditFinding, key_name="isms_id", keyed=True)

        if self.audit_conclusion is not None and not isinstance(self.audit_conclusion, str):
            self.audit_conclusion = str(self.audit_conclusion)

        if self.audit_report_date is not None and not isinstance(self.audit_report_date, XSDDate):
            self.audit_report_date = XSDDate(self.audit_report_date)

        if not isinstance(self.audit_report_distribution, list):
            self.audit_report_distribution = [self.audit_report_distribution] if self.audit_report_distribution is not None else []
        self.audit_report_distribution = [v if isinstance(v, str) else str(v) for v in self.audit_report_distribution]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsAuditFinding(YAMLRoot):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it
    concerns, its evidence and how it is closed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsAuditFinding"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsAuditFinding"
    class_name: ClassVar[str] = "IsmsAuditFinding"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsAuditFinding

    isms_id: Union[str, IsmsAuditFindingIsmsId] = None
    finding_type: Union[str, "IsmsAuditFindingType"] = None
    title: str = None
    finding_requirement: Optional[Union[str, IsmsRequirementReference]] = None
    finding_control: Optional[Union[str, IsmsControlIsmsId]] = None
    finding_evidence: Optional[str] = None
    finding_root_cause: Optional[str] = None
    finding_risk: Optional[str] = None
    finding_recommendation: Optional[str] = None
    finding_auditee_response: Optional[str] = None
    finding_corrective_action: Optional[Union[str, IsmsCorrectiveActionIsmsId]] = None
    finding_closure_status: Optional[str] = None
    finding_closure_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsAuditFindingIsmsId):
            self.isms_id = IsmsAuditFindingIsmsId(self.isms_id)

        if self._is_empty(self.finding_type):
            self.MissingRequiredField("finding_type")
        if not isinstance(self.finding_type, IsmsAuditFindingType):
            self.finding_type = IsmsAuditFindingType(self.finding_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.finding_requirement is not None and not isinstance(self.finding_requirement, IsmsRequirementReference):
            self.finding_requirement = IsmsRequirementReference(self.finding_requirement)

        if self.finding_control is not None and not isinstance(self.finding_control, IsmsControlIsmsId):
            self.finding_control = IsmsControlIsmsId(self.finding_control)

        if self.finding_evidence is not None and not isinstance(self.finding_evidence, str):
            self.finding_evidence = str(self.finding_evidence)

        if self.finding_root_cause is not None and not isinstance(self.finding_root_cause, str):
            self.finding_root_cause = str(self.finding_root_cause)

        if self.finding_risk is not None and not isinstance(self.finding_risk, str):
            self.finding_risk = str(self.finding_risk)

        if self.finding_recommendation is not None and not isinstance(self.finding_recommendation, str):
            self.finding_recommendation = str(self.finding_recommendation)

        if self.finding_auditee_response is not None and not isinstance(self.finding_auditee_response, str):
            self.finding_auditee_response = str(self.finding_auditee_response)

        if self.finding_corrective_action is not None and not isinstance(self.finding_corrective_action, IsmsCorrectiveActionIsmsId):
            self.finding_corrective_action = IsmsCorrectiveActionIsmsId(self.finding_corrective_action)

        if self.finding_closure_status is not None and not isinstance(self.finding_closure_status, str):
            self.finding_closure_status = str(self.finding_closure_status)

        if self.finding_closure_date is not None and not isinstance(self.finding_closure_date, XSDDate):
            self.finding_closure_date = XSDDate(self.finding_closure_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsManagementReview(YAMLRoot):
    """
    A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsManagementReview"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsManagementReview"
    class_name: ClassVar[str] = "IsmsManagementReview"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsManagementReview

    isms_id: Union[str, IsmsManagementReviewIsmsId] = None
    review_held_on: Union[str, XSDDate] = None
    title: str = None
    review_attendees: Optional[Union[str, list[str]]] = empty_list()
    review_previous_actions: Optional[str] = None
    review_context_changes: Optional[str] = None
    review_interested_party_changes: Optional[str] = None
    review_interested_party_feedback: Optional[str] = None
    review_performance_trends: Optional[str] = None
    review_audit_results: Optional[str] = None
    review_risk_assessment_results: Optional[str] = None
    review_risk_treatment_status: Optional[str] = None
    review_risks_and_opportunities: Optional[str] = None
    review_improvement_opportunities: Optional[Union[str, list[str]]] = empty_list()
    review_decisions: Optional[Union[str, list[str]]] = empty_list()
    review_actions: Optional[Union[str, list[str]]] = empty_list()
    review_next_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    document_reference: Optional[str] = None
    document_version: Optional[str] = None
    document_author: Optional[str] = None
    document_owner: Optional[str] = None
    document_approver: Optional[str] = None
    document_approval_date: Optional[Union[str, XSDDate]] = None
    document_effective_date: Optional[Union[str, XSDDate]] = None
    document_last_review_date: Optional[Union[str, XSDDate]] = None
    document_next_review_date: Optional[Union[str, XSDDate]] = None
    document_status: Optional[str] = None
    document_classification: Optional[str] = None
    document_retention: Optional[Union[str, IsmsDuration]] = None
    document_distribution: Optional[Union[str, list[str]]] = empty_list()
    document_storage: Optional[str] = None
    document_change_control: Optional[str] = None
    document_external_origin: Optional[Union[bool, Bool]] = None
    document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsManagementReviewIsmsId):
            self.isms_id = IsmsManagementReviewIsmsId(self.isms_id)

        if self._is_empty(self.review_held_on):
            self.MissingRequiredField("review_held_on")
        if not isinstance(self.review_held_on, XSDDate):
            self.review_held_on = XSDDate(self.review_held_on)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.review_attendees, list):
            self.review_attendees = [self.review_attendees] if self.review_attendees is not None else []
        self.review_attendees = [v if isinstance(v, str) else str(v) for v in self.review_attendees]

        if self.review_previous_actions is not None and not isinstance(self.review_previous_actions, str):
            self.review_previous_actions = str(self.review_previous_actions)

        if self.review_context_changes is not None and not isinstance(self.review_context_changes, str):
            self.review_context_changes = str(self.review_context_changes)

        if self.review_interested_party_changes is not None and not isinstance(self.review_interested_party_changes, str):
            self.review_interested_party_changes = str(self.review_interested_party_changes)

        if self.review_interested_party_feedback is not None and not isinstance(self.review_interested_party_feedback, str):
            self.review_interested_party_feedback = str(self.review_interested_party_feedback)

        if self.review_performance_trends is not None and not isinstance(self.review_performance_trends, str):
            self.review_performance_trends = str(self.review_performance_trends)

        if self.review_audit_results is not None and not isinstance(self.review_audit_results, str):
            self.review_audit_results = str(self.review_audit_results)

        if self.review_risk_assessment_results is not None and not isinstance(self.review_risk_assessment_results, str):
            self.review_risk_assessment_results = str(self.review_risk_assessment_results)

        if self.review_risk_treatment_status is not None and not isinstance(self.review_risk_treatment_status, str):
            self.review_risk_treatment_status = str(self.review_risk_treatment_status)

        if self.review_risks_and_opportunities is not None and not isinstance(self.review_risks_and_opportunities, str):
            self.review_risks_and_opportunities = str(self.review_risks_and_opportunities)

        if not isinstance(self.review_improvement_opportunities, list):
            self.review_improvement_opportunities = [self.review_improvement_opportunities] if self.review_improvement_opportunities is not None else []
        self.review_improvement_opportunities = [v if isinstance(v, str) else str(v) for v in self.review_improvement_opportunities]

        if not isinstance(self.review_decisions, list):
            self.review_decisions = [self.review_decisions] if self.review_decisions is not None else []
        self.review_decisions = [v if isinstance(v, str) else str(v) for v in self.review_decisions]

        if not isinstance(self.review_actions, list):
            self.review_actions = [self.review_actions] if self.review_actions is not None else []
        self.review_actions = [v if isinstance(v, str) else str(v) for v in self.review_actions]

        if self.review_next_date is not None and not isinstance(self.review_next_date, XSDDate):
            self.review_next_date = XSDDate(self.review_next_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.document_version is not None and not isinstance(self.document_version, str):
            self.document_version = str(self.document_version)

        if self.document_author is not None and not isinstance(self.document_author, str):
            self.document_author = str(self.document_author)

        if self.document_owner is not None and not isinstance(self.document_owner, str):
            self.document_owner = str(self.document_owner)

        if self.document_approver is not None and not isinstance(self.document_approver, str):
            self.document_approver = str(self.document_approver)

        if self.document_approval_date is not None and not isinstance(self.document_approval_date, XSDDate):
            self.document_approval_date = XSDDate(self.document_approval_date)

        if self.document_effective_date is not None and not isinstance(self.document_effective_date, XSDDate):
            self.document_effective_date = XSDDate(self.document_effective_date)

        if self.document_last_review_date is not None and not isinstance(self.document_last_review_date, XSDDate):
            self.document_last_review_date = XSDDate(self.document_last_review_date)

        if self.document_next_review_date is not None and not isinstance(self.document_next_review_date, XSDDate):
            self.document_next_review_date = XSDDate(self.document_next_review_date)

        if self.document_status is not None and not isinstance(self.document_status, str):
            self.document_status = str(self.document_status)

        if self.document_classification is not None and not isinstance(self.document_classification, str):
            self.document_classification = str(self.document_classification)

        if self.document_retention is not None and not isinstance(self.document_retention, IsmsDuration):
            self.document_retention = IsmsDuration(self.document_retention)

        if not isinstance(self.document_distribution, list):
            self.document_distribution = [self.document_distribution] if self.document_distribution is not None else []
        self.document_distribution = [v if isinstance(v, str) else str(v) for v in self.document_distribution]

        if self.document_storage is not None and not isinstance(self.document_storage, str):
            self.document_storage = str(self.document_storage)

        if self.document_change_control is not None and not isinstance(self.document_change_control, str):
            self.document_change_control = str(self.document_change_control)

        if self.document_external_origin is not None and not isinstance(self.document_external_origin, Bool):
            self.document_external_origin = Bool(self.document_external_origin)

        if self.document_external_source is not None and not isinstance(self.document_external_source, str):
            self.document_external_source = str(self.document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsNonconformity(YAMLRoot):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was
    closed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsNonconformity"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsNonconformity"
    class_name: ClassVar[str] = "IsmsNonconformity"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsNonconformity

    isms_id: Union[str, IsmsNonconformityIsmsId] = None
    title: str = None
    nonconformity_source: Optional[str] = None
    nonconformity_detected_on: Optional[Union[str, XSDDate]] = None
    nonconformity_detected_by: Optional[str] = None
    nonconformity_requirement: Optional[str] = None
    nonconformity_immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    nonconformity_consequences: Optional[str] = None
    nonconformity_root_cause: Optional[str] = None
    nonconformity_similar_check: Optional[str] = None
    nonconformity_status: Optional[str] = None
    nonconformity_closure_date: Optional[Union[str, XSDDate]] = None
    nonconformity_closure_evidence: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsNonconformityIsmsId):
            self.isms_id = IsmsNonconformityIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.nonconformity_source is not None and not isinstance(self.nonconformity_source, str):
            self.nonconformity_source = str(self.nonconformity_source)

        if self.nonconformity_detected_on is not None and not isinstance(self.nonconformity_detected_on, XSDDate):
            self.nonconformity_detected_on = XSDDate(self.nonconformity_detected_on)

        if self.nonconformity_detected_by is not None and not isinstance(self.nonconformity_detected_by, str):
            self.nonconformity_detected_by = str(self.nonconformity_detected_by)

        if self.nonconformity_requirement is not None and not isinstance(self.nonconformity_requirement, str):
            self.nonconformity_requirement = str(self.nonconformity_requirement)

        if not isinstance(self.nonconformity_immediate_actions, list):
            self.nonconformity_immediate_actions = [self.nonconformity_immediate_actions] if self.nonconformity_immediate_actions is not None else []
        self.nonconformity_immediate_actions = [v if isinstance(v, str) else str(v) for v in self.nonconformity_immediate_actions]

        if self.nonconformity_consequences is not None and not isinstance(self.nonconformity_consequences, str):
            self.nonconformity_consequences = str(self.nonconformity_consequences)

        if self.nonconformity_root_cause is not None and not isinstance(self.nonconformity_root_cause, str):
            self.nonconformity_root_cause = str(self.nonconformity_root_cause)

        if self.nonconformity_similar_check is not None and not isinstance(self.nonconformity_similar_check, str):
            self.nonconformity_similar_check = str(self.nonconformity_similar_check)

        if self.nonconformity_status is not None and not isinstance(self.nonconformity_status, str):
            self.nonconformity_status = str(self.nonconformity_status)

        if self.nonconformity_closure_date is not None and not isinstance(self.nonconformity_closure_date, XSDDate):
            self.nonconformity_closure_date = XSDDate(self.nonconformity_closure_date)

        if self.nonconformity_closure_evidence is not None and not isinstance(self.nonconformity_closure_evidence, str):
            self.nonconformity_closure_evidence = str(self.nonconformity_closure_evidence)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsCorrectiveAction(YAMLRoot):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it
    worked.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsCorrectiveAction"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsCorrectiveAction"
    class_name: ClassVar[str] = "IsmsCorrectiveAction"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsCorrectiveAction

    isms_id: Union[str, IsmsCorrectiveActionIsmsId] = None
    title: str = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    action_nonconformities: Optional[Union[Union[str, IsmsNonconformityIsmsId], list[Union[str, IsmsNonconformityIsmsId]]]] = empty_list()
    action_root_cause: Optional[str] = None
    action_target_date: Optional[Union[str, XSDDate]] = None
    action_completion_date: Optional[Union[str, XSDDate]] = None
    action_resources: Optional[str] = None
    action_effectiveness_criteria: Optional[str] = None
    action_effectiveness_review_date: Optional[Union[str, XSDDate]] = None
    action_effective: Optional[Union[bool, Bool]] = None
    action_isms_changes: Optional[str] = None
    action_status: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsCorrectiveActionIsmsId):
            self.isms_id = IsmsCorrectiveActionIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if not isinstance(self.action_nonconformities, list):
            self.action_nonconformities = [self.action_nonconformities] if self.action_nonconformities is not None else []
        self.action_nonconformities = [v if isinstance(v, IsmsNonconformityIsmsId) else IsmsNonconformityIsmsId(v) for v in self.action_nonconformities]

        if self.action_root_cause is not None and not isinstance(self.action_root_cause, str):
            self.action_root_cause = str(self.action_root_cause)

        if self.action_target_date is not None and not isinstance(self.action_target_date, XSDDate):
            self.action_target_date = XSDDate(self.action_target_date)

        if self.action_completion_date is not None and not isinstance(self.action_completion_date, XSDDate):
            self.action_completion_date = XSDDate(self.action_completion_date)

        if self.action_resources is not None and not isinstance(self.action_resources, str):
            self.action_resources = str(self.action_resources)

        if self.action_effectiveness_criteria is not None and not isinstance(self.action_effectiveness_criteria, str):
            self.action_effectiveness_criteria = str(self.action_effectiveness_criteria)

        if self.action_effectiveness_review_date is not None and not isinstance(self.action_effectiveness_review_date, XSDDate):
            self.action_effectiveness_review_date = XSDDate(self.action_effectiveness_review_date)

        if self.action_effective is not None and not isinstance(self.action_effective, Bool):
            self.action_effective = Bool(self.action_effective)

        if self.action_isms_changes is not None and not isinstance(self.action_isms_changes, str):
            self.action_isms_changes = str(self.action_isms_changes)

        if self.action_status is not None and not isinstance(self.action_status, str):
            self.action_status = str(self.action_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsImprovementOpportunity(YAMLRoot):
    """
    An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsImprovementOpportunity"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsImprovementOpportunity"
    class_name: ClassVar[str] = "IsmsImprovementOpportunity"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsImprovementOpportunity

    isms_id: Union[str, IsmsImprovementOpportunityIsmsId] = None
    title: str = None
    responsible_role: Optional[Union[str, IsmsRoleIsmsId]] = None
    improvement_source: Optional[str] = None
    improvement_identified_on: Optional[Union[str, XSDDate]] = None
    improvement_identified_by: Optional[str] = None
    improvement_benefit: Optional[str] = None
    improvement_priority: Optional[str] = None
    improvement_plan: Optional[str] = None
    improvement_target_date: Optional[Union[str, XSDDate]] = None
    improvement_completion_date: Optional[Union[str, XSDDate]] = None
    improvement_outcome: Optional[str] = None
    improvement_status: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsImprovementOpportunityIsmsId):
            self.isms_id = IsmsImprovementOpportunityIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.responsible_role is not None and not isinstance(self.responsible_role, IsmsRoleIsmsId):
            self.responsible_role = IsmsRoleIsmsId(self.responsible_role)

        if self.improvement_source is not None and not isinstance(self.improvement_source, str):
            self.improvement_source = str(self.improvement_source)

        if self.improvement_identified_on is not None and not isinstance(self.improvement_identified_on, XSDDate):
            self.improvement_identified_on = XSDDate(self.improvement_identified_on)

        if self.improvement_identified_by is not None and not isinstance(self.improvement_identified_by, str):
            self.improvement_identified_by = str(self.improvement_identified_by)

        if self.improvement_benefit is not None and not isinstance(self.improvement_benefit, str):
            self.improvement_benefit = str(self.improvement_benefit)

        if self.improvement_priority is not None and not isinstance(self.improvement_priority, str):
            self.improvement_priority = str(self.improvement_priority)

        if self.improvement_plan is not None and not isinstance(self.improvement_plan, str):
            self.improvement_plan = str(self.improvement_plan)

        if self.improvement_target_date is not None and not isinstance(self.improvement_target_date, XSDDate):
            self.improvement_target_date = XSDDate(self.improvement_target_date)

        if self.improvement_completion_date is not None and not isinstance(self.improvement_completion_date, XSDDate):
            self.improvement_completion_date = XSDDate(self.improvement_completion_date)

        if self.improvement_outcome is not None and not isinstance(self.improvement_outcome, str):
            self.improvement_outcome = str(self.improvement_outcome)

        if self.improvement_status is not None and not isinstance(self.improvement_status, str):
            self.improvement_status = str(self.improvement_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsmsSecurityEvent(YAMLRoot):
    """
    An information security event someone reported, and the assessment of whether it is an incident. An event assessed
    as an incident is recorded as an IsmsSecurityIncident.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsSecurityEvent"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsSecurityEvent"
    class_name: ClassVar[str] = "IsmsSecurityEvent"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsSecurityEvent

    isms_id: Union[str, IsmsSecurityEventIsmsId] = None
    title: str = None
    affected_assets: Optional[Union[Union[str, IsmsAssetIsmsId], list[Union[str, IsmsAssetIsmsId]]]] = empty_list()
    event_type: Optional[str] = None
    event_occurred_at: Optional[Union[str, XSDDateTime]] = None
    event_reporter: Optional[str] = None
    event_assessment: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsSecurityEventIsmsId):
            self.isms_id = IsmsSecurityEventIsmsId(self.isms_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.affected_assets, list):
            self.affected_assets = [self.affected_assets] if self.affected_assets is not None else []
        self.affected_assets = [v if isinstance(v, IsmsAssetIsmsId) else IsmsAssetIsmsId(v) for v in self.affected_assets]

        self.event_type = str(self.class_name)

        if self.event_occurred_at is not None and not isinstance(self.event_occurred_at, XSDDateTime):
            self.event_occurred_at = XSDDateTime(self.event_occurred_at)

        if self.event_reporter is not None and not isinstance(self.event_reporter, str):
            self.event_reporter = str(self.event_reporter)

        if self.event_assessment is not None and not isinstance(self.event_assessment, str):
            self.event_assessment = str(self.event_assessment)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.unknown_event_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "event_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class IsmsSecurityIncident(IsmsSecurityEvent):
    """
    An information security event assessed as an incident: its category and severity, how it was detected, contained,
    eradicated and recovered from, the evidence collected, who was told, and what was learned.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["IsmsSecurityIncident"]
    class_class_curie: ClassVar[str] = "iso27001:IsmsSecurityIncident"
    class_name: ClassVar[str] = "IsmsSecurityIncident"
    class_model_uri: ClassVar[URIRef] = ISO27001.IsmsSecurityIncident

    isms_id: Union[str, IsmsSecurityIncidentIsmsId] = None
    title: str = None
    affected_security_properties: Optional[Union[Union[str, "IsmsSecurityProperty"], list[Union[str, "IsmsSecurityProperty"]]]] = empty_list()
    incident_category: Optional[Union[str, "IsmsIncidentCategory"]] = None
    incident_severity: Optional[Union[str, "IsmsRiskLevel"]] = None
    incident_detection_method: Optional[str] = None
    incident_response_actions: Optional[Union[str, list[str]]] = empty_list()
    incident_containment_actions: Optional[Union[str, list[str]]] = empty_list()
    incident_eradication_actions: Optional[Union[str, list[str]]] = empty_list()
    incident_recovery_actions: Optional[Union[str, list[str]]] = empty_list()
    incident_root_cause: Optional[str] = None
    incident_lessons_learned: Optional[Union[str, list[str]]] = empty_list()
    incident_evidence: Optional[Union[str, list[str]]] = empty_list()
    incident_notification_required: Optional[Union[bool, Bool]] = None
    incident_notifications: Optional[Union[str, list[str]]] = empty_list()
    incident_closed_at: Optional[Union[str, XSDDateTime]] = None
    incident_review: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.isms_id):
            self.MissingRequiredField("isms_id")
        if not isinstance(self.isms_id, IsmsSecurityIncidentIsmsId):
            self.isms_id = IsmsSecurityIncidentIsmsId(self.isms_id)

        if not isinstance(self.affected_security_properties, list):
            self.affected_security_properties = [self.affected_security_properties] if self.affected_security_properties is not None else []
        self.affected_security_properties = [v if isinstance(v, IsmsSecurityProperty) else IsmsSecurityProperty(v) for v in self.affected_security_properties]

        if self.incident_category is not None and not isinstance(self.incident_category, IsmsIncidentCategory):
            self.incident_category = IsmsIncidentCategory(self.incident_category)

        if self.incident_severity is not None and not isinstance(self.incident_severity, IsmsRiskLevel):
            self.incident_severity = IsmsRiskLevel(self.incident_severity)

        if self.incident_detection_method is not None and not isinstance(self.incident_detection_method, str):
            self.incident_detection_method = str(self.incident_detection_method)

        if not isinstance(self.incident_response_actions, list):
            self.incident_response_actions = [self.incident_response_actions] if self.incident_response_actions is not None else []
        self.incident_response_actions = [v if isinstance(v, str) else str(v) for v in self.incident_response_actions]

        if not isinstance(self.incident_containment_actions, list):
            self.incident_containment_actions = [self.incident_containment_actions] if self.incident_containment_actions is not None else []
        self.incident_containment_actions = [v if isinstance(v, str) else str(v) for v in self.incident_containment_actions]

        if not isinstance(self.incident_eradication_actions, list):
            self.incident_eradication_actions = [self.incident_eradication_actions] if self.incident_eradication_actions is not None else []
        self.incident_eradication_actions = [v if isinstance(v, str) else str(v) for v in self.incident_eradication_actions]

        if not isinstance(self.incident_recovery_actions, list):
            self.incident_recovery_actions = [self.incident_recovery_actions] if self.incident_recovery_actions is not None else []
        self.incident_recovery_actions = [v if isinstance(v, str) else str(v) for v in self.incident_recovery_actions]

        if self.incident_root_cause is not None and not isinstance(self.incident_root_cause, str):
            self.incident_root_cause = str(self.incident_root_cause)

        if not isinstance(self.incident_lessons_learned, list):
            self.incident_lessons_learned = [self.incident_lessons_learned] if self.incident_lessons_learned is not None else []
        self.incident_lessons_learned = [v if isinstance(v, str) else str(v) for v in self.incident_lessons_learned]

        if not isinstance(self.incident_evidence, list):
            self.incident_evidence = [self.incident_evidence] if self.incident_evidence is not None else []
        self.incident_evidence = [v if isinstance(v, str) else str(v) for v in self.incident_evidence]

        if self.incident_notification_required is not None and not isinstance(self.incident_notification_required, Bool):
            self.incident_notification_required = Bool(self.incident_notification_required)

        if not isinstance(self.incident_notifications, list):
            self.incident_notifications = [self.incident_notifications] if self.incident_notifications is not None else []
        self.incident_notifications = [v if isinstance(v, str) else str(v) for v in self.incident_notifications]

        if self.incident_closed_at is not None and not isinstance(self.incident_closed_at, XSDDateTime):
            self.incident_closed_at = XSDDateTime(self.incident_closed_at)

        if self.incident_review is not None and not isinstance(self.incident_review, str):
            self.incident_review = str(self.incident_review)

        super().__post_init__(**kwargs)
        self.unknown_event_type = str(self.class_name)


# Enumerations
class IsmsControlTheme(EnumDefinitionImpl):
    """
    The four themes Annex A sorts its controls into, which ISO/IEC 27002:2022 also uses.
    """
    organizational = PermissibleValue(
        text="organizational",
        description="The organizational controls, numbered A.5.1 to A.5.37.")
    people = PermissibleValue(
        text="people",
        description="The people controls, numbered A.6.1 to A.6.8.")
    physical = PermissibleValue(
        text="physical",
        description="The physical controls, numbered A.7.1 to A.7.14.")
    technological = PermissibleValue(
        text="technological",
        description="The technological controls, numbered A.8.1 to A.8.34.")

    _defn = EnumDefinition(
        name="IsmsControlTheme",
        description="The four themes Annex A sorts its controls into, which ISO/IEC 27002:2022 also uses.",
    )

class IsmsAnnexAControl(EnumDefinitionImpl):
    """
    The 93 reference controls of Annex A, by their numbers. The values carry no titles: the titles and the control
    text are ISO's.
    """
    a_5_1 = PermissibleValue(
        text="a_5_1",
        title="A.5.1")
    a_5_2 = PermissibleValue(
        text="a_5_2",
        title="A.5.2")
    a_5_3 = PermissibleValue(
        text="a_5_3",
        title="A.5.3")
    a_5_4 = PermissibleValue(
        text="a_5_4",
        title="A.5.4")
    a_5_5 = PermissibleValue(
        text="a_5_5",
        title="A.5.5")
    a_5_6 = PermissibleValue(
        text="a_5_6",
        title="A.5.6")
    a_5_7 = PermissibleValue(
        text="a_5_7",
        title="A.5.7")
    a_5_8 = PermissibleValue(
        text="a_5_8",
        title="A.5.8")
    a_5_9 = PermissibleValue(
        text="a_5_9",
        title="A.5.9")
    a_5_10 = PermissibleValue(
        text="a_5_10",
        title="A.5.10")
    a_5_11 = PermissibleValue(
        text="a_5_11",
        title="A.5.11")
    a_5_12 = PermissibleValue(
        text="a_5_12",
        title="A.5.12")
    a_5_13 = PermissibleValue(
        text="a_5_13",
        title="A.5.13")
    a_5_14 = PermissibleValue(
        text="a_5_14",
        title="A.5.14")
    a_5_15 = PermissibleValue(
        text="a_5_15",
        title="A.5.15")
    a_5_16 = PermissibleValue(
        text="a_5_16",
        title="A.5.16")
    a_5_17 = PermissibleValue(
        text="a_5_17",
        title="A.5.17")
    a_5_18 = PermissibleValue(
        text="a_5_18",
        title="A.5.18")
    a_5_19 = PermissibleValue(
        text="a_5_19",
        title="A.5.19")
    a_5_20 = PermissibleValue(
        text="a_5_20",
        title="A.5.20")
    a_5_21 = PermissibleValue(
        text="a_5_21",
        title="A.5.21")
    a_5_22 = PermissibleValue(
        text="a_5_22",
        title="A.5.22")
    a_5_23 = PermissibleValue(
        text="a_5_23",
        title="A.5.23")
    a_5_24 = PermissibleValue(
        text="a_5_24",
        title="A.5.24")
    a_5_25 = PermissibleValue(
        text="a_5_25",
        title="A.5.25")
    a_5_26 = PermissibleValue(
        text="a_5_26",
        title="A.5.26")
    a_5_27 = PermissibleValue(
        text="a_5_27",
        title="A.5.27")
    a_5_28 = PermissibleValue(
        text="a_5_28",
        title="A.5.28")
    a_5_29 = PermissibleValue(
        text="a_5_29",
        title="A.5.29")
    a_5_30 = PermissibleValue(
        text="a_5_30",
        title="A.5.30")
    a_5_31 = PermissibleValue(
        text="a_5_31",
        title="A.5.31")
    a_5_32 = PermissibleValue(
        text="a_5_32",
        title="A.5.32")
    a_5_33 = PermissibleValue(
        text="a_5_33",
        title="A.5.33")
    a_5_34 = PermissibleValue(
        text="a_5_34",
        title="A.5.34")
    a_5_35 = PermissibleValue(
        text="a_5_35",
        title="A.5.35")
    a_5_36 = PermissibleValue(
        text="a_5_36",
        title="A.5.36")
    a_5_37 = PermissibleValue(
        text="a_5_37",
        title="A.5.37")
    a_6_1 = PermissibleValue(
        text="a_6_1",
        title="A.6.1")
    a_6_2 = PermissibleValue(
        text="a_6_2",
        title="A.6.2")
    a_6_3 = PermissibleValue(
        text="a_6_3",
        title="A.6.3")
    a_6_4 = PermissibleValue(
        text="a_6_4",
        title="A.6.4")
    a_6_5 = PermissibleValue(
        text="a_6_5",
        title="A.6.5")
    a_6_6 = PermissibleValue(
        text="a_6_6",
        title="A.6.6")
    a_6_7 = PermissibleValue(
        text="a_6_7",
        title="A.6.7")
    a_6_8 = PermissibleValue(
        text="a_6_8",
        title="A.6.8")
    a_7_1 = PermissibleValue(
        text="a_7_1",
        title="A.7.1")
    a_7_2 = PermissibleValue(
        text="a_7_2",
        title="A.7.2")
    a_7_3 = PermissibleValue(
        text="a_7_3",
        title="A.7.3")
    a_7_4 = PermissibleValue(
        text="a_7_4",
        title="A.7.4")
    a_7_5 = PermissibleValue(
        text="a_7_5",
        title="A.7.5")
    a_7_6 = PermissibleValue(
        text="a_7_6",
        title="A.7.6")
    a_7_7 = PermissibleValue(
        text="a_7_7",
        title="A.7.7")
    a_7_8 = PermissibleValue(
        text="a_7_8",
        title="A.7.8")
    a_7_9 = PermissibleValue(
        text="a_7_9",
        title="A.7.9")
    a_7_10 = PermissibleValue(
        text="a_7_10",
        title="A.7.10")
    a_7_11 = PermissibleValue(
        text="a_7_11",
        title="A.7.11")
    a_7_12 = PermissibleValue(
        text="a_7_12",
        title="A.7.12")
    a_7_13 = PermissibleValue(
        text="a_7_13",
        title="A.7.13")
    a_7_14 = PermissibleValue(
        text="a_7_14",
        title="A.7.14")
    a_8_1 = PermissibleValue(
        text="a_8_1",
        title="A.8.1")
    a_8_2 = PermissibleValue(
        text="a_8_2",
        title="A.8.2")
    a_8_3 = PermissibleValue(
        text="a_8_3",
        title="A.8.3")
    a_8_4 = PermissibleValue(
        text="a_8_4",
        title="A.8.4")
    a_8_5 = PermissibleValue(
        text="a_8_5",
        title="A.8.5")
    a_8_6 = PermissibleValue(
        text="a_8_6",
        title="A.8.6")
    a_8_7 = PermissibleValue(
        text="a_8_7",
        title="A.8.7")
    a_8_8 = PermissibleValue(
        text="a_8_8",
        title="A.8.8")
    a_8_9 = PermissibleValue(
        text="a_8_9",
        title="A.8.9")
    a_8_10 = PermissibleValue(
        text="a_8_10",
        title="A.8.10")
    a_8_11 = PermissibleValue(
        text="a_8_11",
        title="A.8.11")
    a_8_12 = PermissibleValue(
        text="a_8_12",
        title="A.8.12")
    a_8_13 = PermissibleValue(
        text="a_8_13",
        title="A.8.13")
    a_8_14 = PermissibleValue(
        text="a_8_14",
        title="A.8.14")
    a_8_15 = PermissibleValue(
        text="a_8_15",
        title="A.8.15")
    a_8_16 = PermissibleValue(
        text="a_8_16",
        title="A.8.16")
    a_8_17 = PermissibleValue(
        text="a_8_17",
        title="A.8.17")
    a_8_18 = PermissibleValue(
        text="a_8_18",
        title="A.8.18")
    a_8_19 = PermissibleValue(
        text="a_8_19",
        title="A.8.19")
    a_8_20 = PermissibleValue(
        text="a_8_20",
        title="A.8.20")
    a_8_21 = PermissibleValue(
        text="a_8_21",
        title="A.8.21")
    a_8_22 = PermissibleValue(
        text="a_8_22",
        title="A.8.22")
    a_8_23 = PermissibleValue(
        text="a_8_23",
        title="A.8.23")
    a_8_24 = PermissibleValue(
        text="a_8_24",
        title="A.8.24")
    a_8_25 = PermissibleValue(
        text="a_8_25",
        title="A.8.25")
    a_8_26 = PermissibleValue(
        text="a_8_26",
        title="A.8.26")
    a_8_27 = PermissibleValue(
        text="a_8_27",
        title="A.8.27")
    a_8_28 = PermissibleValue(
        text="a_8_28",
        title="A.8.28")
    a_8_29 = PermissibleValue(
        text="a_8_29",
        title="A.8.29")
    a_8_30 = PermissibleValue(
        text="a_8_30",
        title="A.8.30")
    a_8_31 = PermissibleValue(
        text="a_8_31",
        title="A.8.31")
    a_8_32 = PermissibleValue(
        text="a_8_32",
        title="A.8.32")
    a_8_33 = PermissibleValue(
        text="a_8_33",
        title="A.8.33")
    a_8_34 = PermissibleValue(
        text="a_8_34",
        title="A.8.34")

    _defn = EnumDefinition(
        name="IsmsAnnexAControl",
        description="""The 93 reference controls of Annex A, by their numbers. The values carry no titles: the titles and the control text are ISO's.""",
    )

class IsmsImplementationStatus(EnumDefinitionImpl):
    """
    How far a control or a plan has been put into effect.
    """
    not_started = PermissibleValue(
        text="not_started",
        description="Nothing has been done yet.")
    planned = PermissibleValue(
        text="planned",
        description="The work is planned, with a timeline.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="The work is under way.")
    implemented = PermissibleValue(
        text="implemented",
        description="The work is done and in operation.")

    _defn = EnumDefinition(
        name="IsmsImplementationStatus",
        description="How far a control or a plan has been put into effect.",
    )

class IsmsRiskTreatmentOption(EnumDefinitionImpl):
    """
    The ways of treating a risk, by the names ISO/IEC 27005 gives them.
    """
    modify = PermissibleValue(
        text="modify",
        description="Change the risk with controls that lower its likelihood or its consequences.")
    retain = PermissibleValue(
        text="retain",
        description="Keep the risk as it is, with the risk owner's approval.")
    avoid = PermissibleValue(
        text="avoid",
        description="Remove the risk by stopping or changing what gives rise to it.")
    share = PermissibleValue(
        text="share",
        description="Share the risk with another party, such as an insurer or a supplier.")

    _defn = EnumDefinition(
        name="IsmsRiskTreatmentOption",
        description="The ways of treating a risk, by the names ISO/IEC 27005 gives them.",
    )

class IsmsRiskLevel(EnumDefinitionImpl):
    """
    A five-point scale of risk level, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the
    organization.
    """
    very_low = PermissibleValue(
        text="very_low",
        description="Small enough to need no action.")
    low = PermissibleValue(
        text="low",
        description="Managed by routine procedures.")
    medium = PermissibleValue(
        text="medium",
        description="Needs management's attention and planned controls.")
    high = PermissibleValue(
        text="high",
        description="Needs treatment first and escalation.")
    critical = PermissibleValue(
        text="critical",
        description="Threatens the organization's objectives and needs action at once.")

    _defn = EnumDefinition(
        name="IsmsRiskLevel",
        description="""A five-point scale of risk level, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.""",
    )

class IsmsLikelihood(EnumDefinitionImpl):
    """
    A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the
    organization.
    """
    rare = PermissibleValue(
        text="rare",
        description="Not expected to happen.")
    unlikely = PermissibleValue(
        text="unlikely",
        description="Could happen, but is not expected to.")
    possible = PermissibleValue(
        text="possible",
        description="Might happen at some point.")
    likely = PermissibleValue(
        text="likely",
        description="Will probably happen.")
    almost_certain = PermissibleValue(
        text="almost_certain",
        description="Expected to happen.")

    _defn = EnumDefinition(
        name="IsmsLikelihood",
        description="""A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.""",
    )

class IsmsImpact(EnumDefinitionImpl):
    """
    A five-point scale of consequence, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the
    organization.
    """
    negligible = PermissibleValue(
        text="negligible",
        description="No noticeable effect on operations or objectives.")
    minor = PermissibleValue(
        text="minor",
        description="An effect normal operations absorb.")
    moderate = PermissibleValue(
        text="moderate",
        description="An effect that needs management to step in.")
    major = PermissibleValue(
        text="major",
        description="A serious effect on objectives, reputation or compliance.")
    severe = PermissibleValue(
        text="severe",
        description="An effect that threatens the organization's survival.")

    _defn = EnumDefinition(
        name="IsmsImpact",
        description="""A five-point scale of consequence, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.""",
    )

class IsmsSecurityProperty(EnumDefinitionImpl):
    """
    The three properties of information that information security preserves, as ISO/IEC 27000 names them.
    """
    confidentiality = PermissibleValue(
        text="confidentiality",
        description="Only those allowed to see the information can see it.")
    integrity = PermissibleValue(
        text="integrity",
        description="The information is accurate and complete.")
    availability = PermissibleValue(
        text="availability",
        description="Those allowed to use the information can use it when they need it.")

    _defn = EnumDefinition(
        name="IsmsSecurityProperty",
        description="""The three properties of information that information security preserves, as ISO/IEC 27000 names them.""",
    )

class IsmsDocumentKind(EnumDefinitionImpl):
    """
    The kinds of documented information an IsmsDocumentedInformation record holds. Policies have records of their own.
    """
    procedure = PermissibleValue(
        text="procedure",
        description="The steps for carrying out an activity the same way each time.")
    standard = PermissibleValue(
        text="standard",
        description="Mandatory requirements for a technology or a process.")
    guideline = PermissibleValue(
        text="guideline",
        description="Recommended practice that supports a policy or a procedure.")
    record = PermissibleValue(
        text="record",
        description="Evidence of what was done or achieved.")
    plan = PermissibleValue(
        text="plan",
        description="How the organization means to reach an objective.")
    report = PermissibleValue(
        text="report",
        description="The formal output of an assessment, audit or review.")

    _defn = EnumDefinition(
        name="IsmsDocumentKind",
        description="""The kinds of documented information an IsmsDocumentedInformation record holds. Policies have records of their own.""",
    )

class IsmsAuditType(EnumDefinitionImpl):
    """
    Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
    """
    first_party = PermissibleValue(
        text="first_party",
        description="The organization audits itself; an internal audit.")
    second_party = PermissibleValue(
        text="second_party",
        description="A party with an interest in the organization audits it, such as a customer.")
    third_party = PermissibleValue(
        text="third_party",
        description="An independent body audits it, such as a certification body or a regulator.")

    _defn = EnumDefinition(
        name="IsmsAuditType",
        description="Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.",
    )

class IsmsAuditFindingType(EnumDefinitionImpl):
    """
    The kinds of audit finding.
    """
    major_nonconformity = PermissibleValue(
        text="major_nonconformity",
        description="A requirement not met in a way that puts the ISMS's intended results in doubt.")
    minor_nonconformity = PermissibleValue(
        text="minor_nonconformity",
        description="A requirement not met in an isolated way that leaves the ISMS's intended results in reach.")
    observation = PermissibleValue(
        text="observation",
        description="A condition that could lead to a nonconformity if left alone.")
    positive_finding = PermissibleValue(
        text="positive_finding",
        description="Evidence of practice that works well.")

    _defn = EnumDefinition(
        name="IsmsAuditFindingType",
        description="The kinds of audit finding.",
    )

class IsmsIncidentCategory(EnumDefinitionImpl):
    """
    Kinds of information security incident, for sorting incidents. ISO/IEC 27001 sets no list of its own.
    """
    malware = PermissibleValue(
        text="malware",
        description="Malicious software, such as a virus, a worm or a trojan.")
    ransomware = PermissibleValue(
        text="ransomware",
        description="Malware that encrypts or takes data to extort money.")
    phishing = PermissibleValue(
        text="phishing",
        description="A message that tries to trick someone into giving up credentials or acting.")
    social_engineering = PermissibleValue(
        text="social_engineering",
        description="Manipulating people into disclosing information or acting unsafely.")
    unauthorized_access = PermissibleValue(
        text="unauthorized_access",
        description="Access to systems or data by someone not allowed it.")
    account_compromise = PermissibleValue(
        text="account_compromise",
        description="Someone else taking control of a legitimate account.")
    privilege_misuse = PermissibleValue(
        text="privilege_misuse",
        description="An authorized user going beyond or misusing their privileges.")
    data_breach = PermissibleValue(
        text="data_breach",
        description="Confidential or personal information disclosed.")
    data_loss = PermissibleValue(
        text="data_loss",
        description="Information lost or corrupted, by accident or otherwise.")
    denial_of_service = PermissibleValue(
        text="denial_of_service",
        description="Systems made unavailable by flooding or attack.")
    web_application_attack = PermissibleValue(
        text="web_application_attack",
        description="An attack on a web application, such as an injection.")
    supply_chain = PermissibleValue(
        text="supply_chain",
        description="An incident that starts at a supplier, a partner or a third-party component.")
    insider_threat = PermissibleValue(
        text="insider_threat",
        description="Harm done by someone inside the organization, on purpose or by neglect.")
    physical_security = PermissibleValue(
        text="physical_security",
        description="Theft, loss or damage of physical assets, or physical access without permission.")
    configuration_error = PermissibleValue(
        text="configuration_error",
        description="A misconfiguration that exposes something.")
    cryptographic_failure = PermissibleValue(
        text="cryptographic_failure",
        description="Cryptography that is weak, broken or misused.")
    policy_violation = PermissibleValue(
        text="policy_violation",
        description="A breach of the organization's security policies or procedures.")
    other = PermissibleValue(
        text="other",
        description="Any incident the other categories do not fit.")

    _defn = EnumDefinition(
        name="IsmsIncidentCategory",
        description="""Kinds of information security incident, for sorting incidents. ISO/IEC 27001 sets no list of its own.""",
    )

class IsmsManagementSystemStandard(EnumDefinitionImpl):
    """
    Management system standards an ISMS may be integrated with or audited beside, each written to ISO's harmonized
    structure.
    """
    iso_iec_27001 = PermissibleValue(
        text="iso_iec_27001",
        description="Information security management systems.")
    iso_iec_27701 = PermissibleValue(
        text="iso_iec_27701",
        description="Privacy information management systems.")
    iso_iec_42001 = PermissibleValue(
        text="iso_iec_42001",
        description="Artificial intelligence management systems.")
    iso_9001 = PermissibleValue(
        text="iso_9001",
        description="Quality management systems.")
    iso_14001 = PermissibleValue(
        text="iso_14001",
        description="Environmental management systems.")
    iso_22301 = PermissibleValue(
        text="iso_22301",
        description="Business continuity management systems.")
    iso_iec_20000_1 = PermissibleValue(
        text="iso_iec_20000_1",
        description="Service management systems.")

    _defn = EnumDefinition(
        name="IsmsManagementSystemStandard",
        description="""Management system standards an ISMS may be integrated with or audited beside, each written to ISO's harmonized structure.""",
    )

# Slots
class slots:
    pass

slots.isms_id = Slot(uri=ISO27001.isms_id, name="isms_id", curie=ISO27001.curie('isms_id'),
                   model_uri=ISO27001.isms_id, domain=None, range=URIRef)

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=ISO27001.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ISO27001.description, domain=None, range=Optional[str])

slots.responsible_role = Slot(uri=ISO27001.responsible_role, name="responsible_role", curie=ISO27001.curie('responsible_role'),
                   model_uri=ISO27001.responsible_role, domain=None, range=Optional[Union[str, IsmsRoleIsmsId]])

slots.relevant_controls = Slot(uri=ISO27001.relevant_controls, name="relevant_controls", curie=ISO27001.curie('relevant_controls'),
                   model_uri=ISO27001.relevant_controls, domain=None, range=Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]])

slots.affected_assets = Slot(uri=ISO27001.affected_assets, name="affected_assets", curie=ISO27001.curie('affected_assets'),
                   model_uri=ISO27001.affected_assets, domain=None, range=Optional[Union[Union[str, IsmsAssetIsmsId], list[Union[str, IsmsAssetIsmsId]]]])

slots.affected_security_properties = Slot(uri=ISO27001.affected_security_properties, name="affected_security_properties", curie=ISO27001.curie('affected_security_properties'),
                   model_uri=ISO27001.affected_security_properties, domain=None, range=Optional[Union[Union[str, "IsmsSecurityProperty"], list[Union[str, "IsmsSecurityProperty"]]]])

slots.implementation_state = Slot(uri=ISO27001.implementation_state, name="implementation_state", curie=ISO27001.curie('implementation_state'),
                   model_uri=ISO27001.implementation_state, domain=None, range=Optional[Union[str, "IsmsImplementationStatus"]])

slots.entry_annex_a_control = Slot(uri=ISO27001.entry_annex_a_control, name="entry_annex_a_control", curie=ISO27001.curie('entry_annex_a_control'),
                   model_uri=ISO27001.entry_annex_a_control, domain=None, range=Optional[Union[str, "IsmsAnnexAControl"]])

slots.ismsDocumentControlMixin__document_reference = Slot(uri=ISO27001.document_reference, name="ismsDocumentControlMixin__document_reference", curie=ISO27001.curie('document_reference'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_reference, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_version = Slot(uri=ISO27001.document_version, name="ismsDocumentControlMixin__document_version", curie=ISO27001.curie('document_version'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_version, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_author = Slot(uri=ISO27001.document_author, name="ismsDocumentControlMixin__document_author", curie=ISO27001.curie('document_author'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_author, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_owner = Slot(uri=ISO27001.document_owner, name="ismsDocumentControlMixin__document_owner", curie=ISO27001.curie('document_owner'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_owner, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_approver = Slot(uri=ISO27001.document_approver, name="ismsDocumentControlMixin__document_approver", curie=ISO27001.curie('document_approver'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_approver, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_approval_date = Slot(uri=ISO27001.document_approval_date, name="ismsDocumentControlMixin__document_approval_date", curie=ISO27001.curie('document_approval_date'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_approval_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsDocumentControlMixin__document_effective_date = Slot(uri=ISO27001.document_effective_date, name="ismsDocumentControlMixin__document_effective_date", curie=ISO27001.curie('document_effective_date'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsDocumentControlMixin__document_last_review_date = Slot(uri=ISO27001.document_last_review_date, name="ismsDocumentControlMixin__document_last_review_date", curie=ISO27001.curie('document_last_review_date'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_last_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsDocumentControlMixin__document_next_review_date = Slot(uri=ISO27001.document_next_review_date, name="ismsDocumentControlMixin__document_next_review_date", curie=ISO27001.curie('document_next_review_date'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_next_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsDocumentControlMixin__document_status = Slot(uri=ISO27001.document_status, name="ismsDocumentControlMixin__document_status", curie=ISO27001.curie('document_status'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_status, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_classification = Slot(uri=ISO27001.document_classification, name="ismsDocumentControlMixin__document_classification", curie=ISO27001.curie('document_classification'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_classification, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_retention = Slot(uri=ISO27001.document_retention, name="ismsDocumentControlMixin__document_retention", curie=ISO27001.curie('document_retention'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_retention, domain=None, range=Optional[Union[str, IsmsDuration]])

slots.ismsDocumentControlMixin__document_distribution = Slot(uri=ISO27001.document_distribution, name="ismsDocumentControlMixin__document_distribution", curie=ISO27001.curie('document_distribution'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsDocumentControlMixin__document_storage = Slot(uri=ISO27001.document_storage, name="ismsDocumentControlMixin__document_storage", curie=ISO27001.curie('document_storage'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_storage, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_change_control = Slot(uri=ISO27001.document_change_control, name="ismsDocumentControlMixin__document_change_control", curie=ISO27001.curie('document_change_control'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_change_control, domain=None, range=Optional[str])

slots.ismsDocumentControlMixin__document_external_origin = Slot(uri=ISO27001.document_external_origin, name="ismsDocumentControlMixin__document_external_origin", curie=ISO27001.curie('document_external_origin'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_external_origin, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsDocumentControlMixin__document_external_source = Slot(uri=ISO27001.document_external_source, name="ismsDocumentControlMixin__document_external_source", curie=ISO27001.curie('document_external_source'),
                   model_uri=ISO27001.ismsDocumentControlMixin__document_external_source, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_organization = Slot(uri=ISO27001.isms_organization, name="ismsManagementSystem__isms_organization", curie=ISO27001.curie('isms_organization'),
                   model_uri=ISO27001.ismsManagementSystem__isms_organization, domain=None, range=Optional[Union[dict, IsmsOrganization]])

slots.ismsManagementSystem__isms_top_management = Slot(uri=ISO27001.isms_top_management, name="ismsManagementSystem__isms_top_management", curie=ISO27001.curie('isms_top_management'),
                   model_uri=ISO27001.ismsManagementSystem__isms_top_management, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_governing_body = Slot(uri=ISO27001.isms_governing_body, name="ismsManagementSystem__isms_governing_body", curie=ISO27001.curie('isms_governing_body'),
                   model_uri=ISO27001.ismsManagementSystem__isms_governing_body, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_leadership_evidence = Slot(uri=ISO27001.isms_leadership_evidence, name="ismsManagementSystem__isms_leadership_evidence", curie=ISO27001.curie('isms_leadership_evidence'),
                   model_uri=ISO27001.ismsManagementSystem__isms_leadership_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_scope = Slot(uri=ISO27001.isms_scope, name="ismsManagementSystem__isms_scope", curie=ISO27001.curie('isms_scope'),
                   model_uri=ISO27001.ismsManagementSystem__isms_scope, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_scope_boundaries = Slot(uri=ISO27001.isms_scope_boundaries, name="ismsManagementSystem__isms_scope_boundaries", curie=ISO27001.curie('isms_scope_boundaries'),
                   model_uri=ISO27001.ismsManagementSystem__isms_scope_boundaries, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_scope_exclusions = Slot(uri=ISO27001.isms_scope_exclusions, name="ismsManagementSystem__isms_scope_exclusions", curie=ISO27001.curie('isms_scope_exclusions'),
                   model_uri=ISO27001.ismsManagementSystem__isms_scope_exclusions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_interfaces = Slot(uri=ISO27001.isms_interfaces, name="ismsManagementSystem__isms_interfaces", curie=ISO27001.curie('isms_interfaces'),
                   model_uri=ISO27001.ismsManagementSystem__isms_interfaces, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_processes = Slot(uri=ISO27001.isms_processes, name="ismsManagementSystem__isms_processes", curie=ISO27001.curie('isms_processes'),
                   model_uri=ISO27001.ismsManagementSystem__isms_processes, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_internal_issues = Slot(uri=ISO27001.isms_internal_issues, name="ismsManagementSystem__isms_internal_issues", curie=ISO27001.curie('isms_internal_issues'),
                   model_uri=ISO27001.ismsManagementSystem__isms_internal_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_external_issues = Slot(uri=ISO27001.isms_external_issues, name="ismsManagementSystem__isms_external_issues", curie=ISO27001.curie('isms_external_issues'),
                   model_uri=ISO27001.ismsManagementSystem__isms_external_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_risk_and_opportunity_actions = Slot(uri=ISO27001.isms_risk_and_opportunity_actions, name="ismsManagementSystem__isms_risk_and_opportunity_actions", curie=ISO27001.curie('isms_risk_and_opportunity_actions'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risk_and_opportunity_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_planned_changes = Slot(uri=ISO27001.isms_planned_changes, name="ismsManagementSystem__isms_planned_changes", curie=ISO27001.curie('isms_planned_changes'),
                   model_uri=ISO27001.ismsManagementSystem__isms_planned_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_external_services = Slot(uri=ISO27001.isms_external_services, name="ismsManagementSystem__isms_external_services", curie=ISO27001.curie('isms_external_services'),
                   model_uri=ISO27001.ismsManagementSystem__isms_external_services, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementSystem__isms_certification_status = Slot(uri=ISO27001.isms_certification_status, name="ismsManagementSystem__isms_certification_status", curie=ISO27001.curie('isms_certification_status'),
                   model_uri=ISO27001.ismsManagementSystem__isms_certification_status, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_certification_body = Slot(uri=ISO27001.isms_certification_body, name="ismsManagementSystem__isms_certification_body", curie=ISO27001.curie('isms_certification_body'),
                   model_uri=ISO27001.ismsManagementSystem__isms_certification_body, domain=None, range=Optional[str])

slots.ismsManagementSystem__isms_certification_date = Slot(uri=ISO27001.isms_certification_date, name="ismsManagementSystem__isms_certification_date", curie=ISO27001.curie('isms_certification_date'),
                   model_uri=ISO27001.ismsManagementSystem__isms_certification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsManagementSystem__isms_recertification_date = Slot(uri=ISO27001.isms_recertification_date, name="ismsManagementSystem__isms_recertification_date", curie=ISO27001.curie('isms_recertification_date'),
                   model_uri=ISO27001.ismsManagementSystem__isms_recertification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsManagementSystem__isms_interested_parties = Slot(uri=ISO27001.isms_interested_parties, name="ismsManagementSystem__isms_interested_parties", curie=ISO27001.curie('isms_interested_parties'),
                   model_uri=ISO27001.ismsManagementSystem__isms_interested_parties, domain=None, range=Optional[Union[dict[Union[str, IsmsInterestedPartyIsmsId], Union[dict, IsmsInterestedParty]], list[Union[dict, IsmsInterestedParty]]]])

slots.ismsManagementSystem__isms_policy = Slot(uri=ISO27001.isms_policy, name="ismsManagementSystem__isms_policy", curie=ISO27001.curie('isms_policy'),
                   model_uri=ISO27001.ismsManagementSystem__isms_policy, domain=None, range=Optional[Union[dict, IsmsPolicy]])

slots.ismsManagementSystem__isms_topic_specific_policies = Slot(uri=ISO27001.isms_topic_specific_policies, name="ismsManagementSystem__isms_topic_specific_policies", curie=ISO27001.curie('isms_topic_specific_policies'),
                   model_uri=ISO27001.ismsManagementSystem__isms_topic_specific_policies, domain=None, range=Optional[Union[dict[Union[str, IsmsTopicSpecificPolicyIsmsId], Union[dict, IsmsTopicSpecificPolicy]], list[Union[dict, IsmsTopicSpecificPolicy]]]])

slots.ismsManagementSystem__isms_roles = Slot(uri=ISO27001.isms_roles, name="ismsManagementSystem__isms_roles", curie=ISO27001.curie('isms_roles'),
                   model_uri=ISO27001.ismsManagementSystem__isms_roles, domain=None, range=Optional[Union[dict[Union[str, IsmsRoleIsmsId], Union[dict, IsmsRole]], list[Union[dict, IsmsRole]]]])

slots.ismsManagementSystem__isms_objectives = Slot(uri=ISO27001.isms_objectives, name="ismsManagementSystem__isms_objectives", curie=ISO27001.curie('isms_objectives'),
                   model_uri=ISO27001.ismsManagementSystem__isms_objectives, domain=None, range=Optional[Union[dict[Union[str, IsmsObjectiveIsmsId], Union[dict, IsmsObjective]], list[Union[dict, IsmsObjective]]]])

slots.ismsManagementSystem__isms_risk_assessment_process = Slot(uri=ISO27001.isms_risk_assessment_process, name="ismsManagementSystem__isms_risk_assessment_process", curie=ISO27001.curie('isms_risk_assessment_process'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risk_assessment_process, domain=None, range=Optional[Union[dict, IsmsRiskAssessmentProcess]])

slots.ismsManagementSystem__isms_risk_treatment_process = Slot(uri=ISO27001.isms_risk_treatment_process, name="ismsManagementSystem__isms_risk_treatment_process", curie=ISO27001.curie('isms_risk_treatment_process'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risk_treatment_process, domain=None, range=Optional[Union[dict, IsmsRiskTreatmentProcess]])

slots.ismsManagementSystem__isms_risk_assessments = Slot(uri=ISO27001.isms_risk_assessments, name="ismsManagementSystem__isms_risk_assessments", curie=ISO27001.curie('isms_risk_assessments'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risk_assessments, domain=None, range=Optional[Union[dict[Union[str, IsmsRiskAssessmentIsmsId], Union[dict, IsmsRiskAssessment]], list[Union[dict, IsmsRiskAssessment]]]])

slots.ismsManagementSystem__isms_risks = Slot(uri=ISO27001.isms_risks, name="ismsManagementSystem__isms_risks", curie=ISO27001.curie('isms_risks'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risks, domain=None, range=Optional[Union[dict[Union[str, IsmsRiskIsmsId], Union[dict, IsmsRisk]], list[Union[dict, IsmsRisk]]]])

slots.ismsManagementSystem__isms_risk_treatment_plans = Slot(uri=ISO27001.isms_risk_treatment_plans, name="ismsManagementSystem__isms_risk_treatment_plans", curie=ISO27001.curie('isms_risk_treatment_plans'),
                   model_uri=ISO27001.ismsManagementSystem__isms_risk_treatment_plans, domain=None, range=Optional[Union[dict[Union[str, IsmsRiskTreatmentPlanIsmsId], Union[dict, IsmsRiskTreatmentPlan]], list[Union[dict, IsmsRiskTreatmentPlan]]]])

slots.ismsManagementSystem__isms_statement_of_applicability = Slot(uri=ISO27001.isms_statement_of_applicability, name="ismsManagementSystem__isms_statement_of_applicability", curie=ISO27001.curie('isms_statement_of_applicability'),
                   model_uri=ISO27001.ismsManagementSystem__isms_statement_of_applicability, domain=None, range=Optional[Union[dict, IsmsStatementOfApplicability]])

slots.ismsManagementSystem__isms_controls = Slot(uri=ISO27001.isms_controls, name="ismsManagementSystem__isms_controls", curie=ISO27001.curie('isms_controls'),
                   model_uri=ISO27001.ismsManagementSystem__isms_controls, domain=None, range=Optional[Union[dict[Union[str, IsmsControlIsmsId], Union[dict, IsmsControl]], list[Union[dict, IsmsControl]]]])

slots.ismsManagementSystem__isms_assets = Slot(uri=ISO27001.isms_assets, name="ismsManagementSystem__isms_assets", curie=ISO27001.curie('isms_assets'),
                   model_uri=ISO27001.ismsManagementSystem__isms_assets, domain=None, range=Optional[Union[dict[Union[str, IsmsAssetIsmsId], Union[dict, IsmsAsset]], list[Union[dict, IsmsAsset]]]])

slots.ismsManagementSystem__isms_resources = Slot(uri=ISO27001.isms_resources, name="ismsManagementSystem__isms_resources", curie=ISO27001.curie('isms_resources'),
                   model_uri=ISO27001.ismsManagementSystem__isms_resources, domain=None, range=Optional[Union[dict[Union[str, IsmsResourceIsmsId], Union[dict, IsmsResource]], list[Union[dict, IsmsResource]]]])

slots.ismsManagementSystem__isms_competence_records = Slot(uri=ISO27001.isms_competence_records, name="ismsManagementSystem__isms_competence_records", curie=ISO27001.curie('isms_competence_records'),
                   model_uri=ISO27001.ismsManagementSystem__isms_competence_records, domain=None, range=Optional[Union[dict[Union[str, IsmsCompetenceRecordIsmsId], Union[dict, IsmsCompetenceRecord]], list[Union[dict, IsmsCompetenceRecord]]]])

slots.ismsManagementSystem__isms_awareness_programme = Slot(uri=ISO27001.isms_awareness_programme, name="ismsManagementSystem__isms_awareness_programme", curie=ISO27001.curie('isms_awareness_programme'),
                   model_uri=ISO27001.ismsManagementSystem__isms_awareness_programme, domain=None, range=Optional[Union[dict, IsmsAwarenessProgramme]])

slots.ismsManagementSystem__isms_communication_plan = Slot(uri=ISO27001.isms_communication_plan, name="ismsManagementSystem__isms_communication_plan", curie=ISO27001.curie('isms_communication_plan'),
                   model_uri=ISO27001.ismsManagementSystem__isms_communication_plan, domain=None, range=Optional[Union[dict, IsmsCommunicationPlan]])

slots.ismsManagementSystem__isms_documented_information = Slot(uri=ISO27001.isms_documented_information, name="ismsManagementSystem__isms_documented_information", curie=ISO27001.curie('isms_documented_information'),
                   model_uri=ISO27001.ismsManagementSystem__isms_documented_information, domain=None, range=Optional[Union[dict[Union[str, IsmsDocumentedInformationIsmsId], Union[dict, IsmsDocumentedInformation]], list[Union[dict, IsmsDocumentedInformation]]]])

slots.ismsManagementSystem__isms_operational_procedures = Slot(uri=ISO27001.isms_operational_procedures, name="ismsManagementSystem__isms_operational_procedures", curie=ISO27001.curie('isms_operational_procedures'),
                   model_uri=ISO27001.ismsManagementSystem__isms_operational_procedures, domain=None, range=Optional[Union[dict[Union[str, IsmsOperationalProcedureIsmsId], Union[dict, IsmsOperationalProcedure]], list[Union[dict, IsmsOperationalProcedure]]]])

slots.ismsManagementSystem__isms_monitoring_programme = Slot(uri=ISO27001.isms_monitoring_programme, name="ismsManagementSystem__isms_monitoring_programme", curie=ISO27001.curie('isms_monitoring_programme'),
                   model_uri=ISO27001.ismsManagementSystem__isms_monitoring_programme, domain=None, range=Optional[Union[dict, IsmsMonitoringProgramme]])

slots.ismsManagementSystem__isms_audit_programmes = Slot(uri=ISO27001.isms_audit_programmes, name="ismsManagementSystem__isms_audit_programmes", curie=ISO27001.curie('isms_audit_programmes'),
                   model_uri=ISO27001.ismsManagementSystem__isms_audit_programmes, domain=None, range=Optional[Union[dict[Union[str, IsmsAuditProgrammeIsmsId], Union[dict, IsmsAuditProgramme]], list[Union[dict, IsmsAuditProgramme]]]])

slots.ismsManagementSystem__isms_audits = Slot(uri=ISO27001.isms_audits, name="ismsManagementSystem__isms_audits", curie=ISO27001.curie('isms_audits'),
                   model_uri=ISO27001.ismsManagementSystem__isms_audits, domain=None, range=Optional[Union[dict[Union[str, IsmsAuditIsmsId], Union[dict, IsmsAudit]], list[Union[dict, IsmsAudit]]]])

slots.ismsManagementSystem__isms_management_reviews = Slot(uri=ISO27001.isms_management_reviews, name="ismsManagementSystem__isms_management_reviews", curie=ISO27001.curie('isms_management_reviews'),
                   model_uri=ISO27001.ismsManagementSystem__isms_management_reviews, domain=None, range=Optional[Union[dict[Union[str, IsmsManagementReviewIsmsId], Union[dict, IsmsManagementReview]], list[Union[dict, IsmsManagementReview]]]])

slots.ismsManagementSystem__isms_nonconformities = Slot(uri=ISO27001.isms_nonconformities, name="ismsManagementSystem__isms_nonconformities", curie=ISO27001.curie('isms_nonconformities'),
                   model_uri=ISO27001.ismsManagementSystem__isms_nonconformities, domain=None, range=Optional[Union[dict[Union[str, IsmsNonconformityIsmsId], Union[dict, IsmsNonconformity]], list[Union[dict, IsmsNonconformity]]]])

slots.ismsManagementSystem__isms_corrective_actions = Slot(uri=ISO27001.isms_corrective_actions, name="ismsManagementSystem__isms_corrective_actions", curie=ISO27001.curie('isms_corrective_actions'),
                   model_uri=ISO27001.ismsManagementSystem__isms_corrective_actions, domain=None, range=Optional[Union[dict[Union[str, IsmsCorrectiveActionIsmsId], Union[dict, IsmsCorrectiveAction]], list[Union[dict, IsmsCorrectiveAction]]]])

slots.ismsManagementSystem__isms_improvements = Slot(uri=ISO27001.isms_improvements, name="ismsManagementSystem__isms_improvements", curie=ISO27001.curie('isms_improvements'),
                   model_uri=ISO27001.ismsManagementSystem__isms_improvements, domain=None, range=Optional[Union[dict[Union[str, IsmsImprovementOpportunityIsmsId], Union[dict, IsmsImprovementOpportunity]], list[Union[dict, IsmsImprovementOpportunity]]]])

slots.ismsManagementSystem__isms_security_events = Slot(uri=ISO27001.isms_security_events, name="ismsManagementSystem__isms_security_events", curie=ISO27001.curie('isms_security_events'),
                   model_uri=ISO27001.ismsManagementSystem__isms_security_events, domain=None, range=Optional[Union[dict[Union[str, IsmsSecurityEventIsmsId], Union[dict, IsmsSecurityEvent]], list[Union[dict, IsmsSecurityEvent]]]])

slots.ismsOrganization__organization_legal_name = Slot(uri=ISO27001.organization_legal_name, name="ismsOrganization__organization_legal_name", curie=ISO27001.curie('organization_legal_name'),
                   model_uri=ISO27001.ismsOrganization__organization_legal_name, domain=None, range=Optional[str])

slots.ismsOrganization__organization_trading_names = Slot(uri=ISO27001.organization_trading_names, name="ismsOrganization__organization_trading_names", curie=ISO27001.curie('organization_trading_names'),
                   model_uri=ISO27001.ismsOrganization__organization_trading_names, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsOrganization__organization_kind = Slot(uri=ISO27001.organization_kind, name="ismsOrganization__organization_kind", curie=ISO27001.curie('organization_kind'),
                   model_uri=ISO27001.ismsOrganization__organization_kind, domain=None, range=Optional[str])

slots.ismsOrganization__organization_sector = Slot(uri=ISO27001.organization_sector, name="ismsOrganization__organization_sector", curie=ISO27001.curie('organization_sector'),
                   model_uri=ISO27001.ismsOrganization__organization_sector, domain=None, range=Optional[str])

slots.ismsOrganization__organization_size = Slot(uri=ISO27001.organization_size, name="ismsOrganization__organization_size", curie=ISO27001.curie('organization_size'),
                   model_uri=ISO27001.ismsOrganization__organization_size, domain=None, range=Optional[str])

slots.ismsOrganization__organization_employee_count = Slot(uri=ISO27001.organization_employee_count, name="ismsOrganization__organization_employee_count", curie=ISO27001.curie('organization_employee_count'),
                   model_uri=ISO27001.ismsOrganization__organization_employee_count, domain=None, range=Optional[int])

slots.ismsOrganization__organization_locations = Slot(uri=ISO27001.organization_locations, name="ismsOrganization__organization_locations", curie=ISO27001.curie('organization_locations'),
                   model_uri=ISO27001.ismsOrganization__organization_locations, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsOrganization__organization_jurisdictions = Slot(uri=ISO27001.organization_jurisdictions, name="ismsOrganization__organization_jurisdictions", curie=ISO27001.curie('organization_jurisdictions'),
                   model_uri=ISO27001.ismsOrganization__organization_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsOrganization__organization_parent = Slot(uri=ISO27001.organization_parent, name="ismsOrganization__organization_parent", curie=ISO27001.curie('organization_parent'),
                   model_uri=ISO27001.ismsOrganization__organization_parent, domain=None, range=Optional[str])

slots.ismsOrganization__organization_subsidiaries = Slot(uri=ISO27001.organization_subsidiaries, name="ismsOrganization__organization_subsidiaries", curie=ISO27001.curie('organization_subsidiaries'),
                   model_uri=ISO27001.ismsOrganization__organization_subsidiaries, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsOrganization__organization_climate_change_relevant = Slot(uri=ISO27001.organization_climate_change_relevant, name="ismsOrganization__organization_climate_change_relevant", curie=ISO27001.curie('organization_climate_change_relevant'),
                   model_uri=ISO27001.ismsOrganization__organization_climate_change_relevant, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsInterestedParty__party_category = Slot(uri=ISO27001.party_category, name="ismsInterestedParty__party_category", curie=ISO27001.curie('party_category'),
                   model_uri=ISO27001.ismsInterestedParty__party_category, domain=None, range=Optional[str])

slots.ismsInterestedParty__party_relationship = Slot(uri=ISO27001.party_relationship, name="ismsInterestedParty__party_relationship", curie=ISO27001.curie('party_relationship'),
                   model_uri=ISO27001.ismsInterestedParty__party_relationship, domain=None, range=Optional[str])

slots.ismsInterestedParty__party_requirements = Slot(uri=ISO27001.party_requirements, name="ismsInterestedParty__party_requirements", curie=ISO27001.curie('party_requirements'),
                   model_uri=ISO27001.ismsInterestedParty__party_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsInterestedParty__party_addressed_requirements = Slot(uri=ISO27001.party_addressed_requirements, name="ismsInterestedParty__party_addressed_requirements", curie=ISO27001.curie('party_addressed_requirements'),
                   model_uri=ISO27001.ismsInterestedParty__party_addressed_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsInterestedParty__party_climate_change_requirements = Slot(uri=ISO27001.party_climate_change_requirements, name="ismsInterestedParty__party_climate_change_requirements", curie=ISO27001.curie('party_climate_change_requirements'),
                   model_uri=ISO27001.ismsInterestedParty__party_climate_change_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsInterestedParty__party_communication_needs = Slot(uri=ISO27001.party_communication_needs, name="ismsInterestedParty__party_communication_needs", curie=ISO27001.curie('party_communication_needs'),
                   model_uri=ISO27001.ismsInterestedParty__party_communication_needs, domain=None, range=Optional[str])

slots.ismsInterestedParty__party_contact = Slot(uri=ISO27001.party_contact, name="ismsInterestedParty__party_contact", curie=ISO27001.curie('party_contact'),
                   model_uri=ISO27001.ismsInterestedParty__party_contact, domain=None, range=Optional[str])

slots.ismsPolicy__policy_statement = Slot(uri=ISO27001.policy_statement, name="ismsPolicy__policy_statement", curie=ISO27001.curie('policy_statement'),
                   model_uri=ISO27001.ismsPolicy__policy_statement, domain=None, range=Optional[str])

slots.ismsPolicy__policy_objectives_framework = Slot(uri=ISO27001.policy_objectives_framework, name="ismsPolicy__policy_objectives_framework", curie=ISO27001.curie('policy_objectives_framework'),
                   model_uri=ISO27001.ismsPolicy__policy_objectives_framework, domain=None, range=Optional[str])

slots.ismsPolicy__policy_commitments = Slot(uri=ISO27001.policy_commitments, name="ismsPolicy__policy_commitments", curie=ISO27001.curie('policy_commitments'),
                   model_uri=ISO27001.ismsPolicy__policy_commitments, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsPolicy__policy_applicability = Slot(uri=ISO27001.policy_applicability, name="ismsPolicy__policy_applicability", curie=ISO27001.curie('policy_applicability'),
                   model_uri=ISO27001.ismsPolicy__policy_applicability, domain=None, range=Optional[str])

slots.ismsPolicy__policy_communication_date = Slot(uri=ISO27001.policy_communication_date, name="ismsPolicy__policy_communication_date", curie=ISO27001.curie('policy_communication_date'),
                   model_uri=ISO27001.ismsPolicy__policy_communication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsPolicy__policy_acknowledgement_required = Slot(uri=ISO27001.policy_acknowledgement_required, name="ismsPolicy__policy_acknowledgement_required", curie=ISO27001.curie('policy_acknowledgement_required'),
                   model_uri=ISO27001.ismsPolicy__policy_acknowledgement_required, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsPolicy__policy_management_systems = Slot(uri=ISO27001.policy_management_systems, name="ismsPolicy__policy_management_systems", curie=ISO27001.curie('policy_management_systems'),
                   model_uri=ISO27001.ismsPolicy__policy_management_systems, domain=None, range=Optional[Union[Union[str, "IsmsManagementSystemStandard"], list[Union[str, "IsmsManagementSystemStandard"]]]])

slots.ismsTopicSpecificPolicy__topic_policy_topic = Slot(uri=ISO27001.topic_policy_topic, name="ismsTopicSpecificPolicy__topic_policy_topic", curie=ISO27001.curie('topic_policy_topic'),
                   model_uri=ISO27001.ismsTopicSpecificPolicy__topic_policy_topic, domain=None, range=Optional[str])

slots.ismsTopicSpecificPolicy__topic_policy_parent = Slot(uri=ISO27001.topic_policy_parent, name="ismsTopicSpecificPolicy__topic_policy_parent", curie=ISO27001.curie('topic_policy_parent'),
                   model_uri=ISO27001.ismsTopicSpecificPolicy__topic_policy_parent, domain=None, range=Optional[Union[str, IsmsPolicyIsmsId]])

slots.ismsTopicSpecificPolicy__topic_policy_audience = Slot(uri=ISO27001.topic_policy_audience, name="ismsTopicSpecificPolicy__topic_policy_audience", curie=ISO27001.curie('topic_policy_audience'),
                   model_uri=ISO27001.ismsTopicSpecificPolicy__topic_policy_audience, domain=None, range=Optional[str])

slots.ismsRole__role_category = Slot(uri=ISO27001.role_category, name="ismsRole__role_category", curie=ISO27001.curie('role_category'),
                   model_uri=ISO27001.ismsRole__role_category, domain=None, range=Optional[str])

slots.ismsRole__role_responsibilities = Slot(uri=ISO27001.role_responsibilities, name="ismsRole__role_responsibilities", curie=ISO27001.curie('role_responsibilities'),
                   model_uri=ISO27001.ismsRole__role_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRole__role_authorities = Slot(uri=ISO27001.role_authorities, name="ismsRole__role_authorities", curie=ISO27001.curie('role_authorities'),
                   model_uri=ISO27001.ismsRole__role_authorities, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRole__role_accountability = Slot(uri=ISO27001.role_accountability, name="ismsRole__role_accountability", curie=ISO27001.curie('role_accountability'),
                   model_uri=ISO27001.ismsRole__role_accountability, domain=None, range=Optional[str])

slots.ismsRole__role_holders = Slot(uri=ISO27001.role_holders, name="ismsRole__role_holders", curie=ISO27001.curie('role_holders'),
                   model_uri=ISO27001.ismsRole__role_holders, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRole__role_delegation = Slot(uri=ISO27001.role_delegation, name="ismsRole__role_delegation", curie=ISO27001.curie('role_delegation'),
                   model_uri=ISO27001.ismsRole__role_delegation, domain=None, range=Optional[str])

slots.ismsRole__role_reports_to = Slot(uri=ISO27001.role_reports_to, name="ismsRole__role_reports_to", curie=ISO27001.curie('role_reports_to'),
                   model_uri=ISO27001.ismsRole__role_reports_to, domain=None, range=Optional[Union[str, IsmsRoleIsmsId]])

slots.ismsObjective__objective_statement = Slot(uri=ISO27001.objective_statement, name="ismsObjective__objective_statement", curie=ISO27001.curie('objective_statement'),
                   model_uri=ISO27001.ismsObjective__objective_statement, domain=None, range=Optional[str])

slots.ismsObjective__objective_target = Slot(uri=ISO27001.objective_target, name="ismsObjective__objective_target", curie=ISO27001.curie('objective_target'),
                   model_uri=ISO27001.ismsObjective__objective_target, domain=None, range=Optional[str])

slots.ismsObjective__objective_current_value = Slot(uri=ISO27001.objective_current_value, name="ismsObjective__objective_current_value", curie=ISO27001.curie('objective_current_value'),
                   model_uri=ISO27001.ismsObjective__objective_current_value, domain=None, range=Optional[str])

slots.ismsObjective__objective_metric = Slot(uri=ISO27001.objective_metric, name="ismsObjective__objective_metric", curie=ISO27001.curie('objective_metric'),
                   model_uri=ISO27001.ismsObjective__objective_metric, domain=None, range=Optional[str])

slots.ismsObjective__objective_measurement_method = Slot(uri=ISO27001.objective_measurement_method, name="ismsObjective__objective_measurement_method", curie=ISO27001.curie('objective_measurement_method'),
                   model_uri=ISO27001.ismsObjective__objective_measurement_method, domain=None, range=Optional[str])

slots.ismsObjective__objective_measurement_frequency = Slot(uri=ISO27001.objective_measurement_frequency, name="ismsObjective__objective_measurement_frequency", curie=ISO27001.curie('objective_measurement_frequency'),
                   model_uri=ISO27001.ismsObjective__objective_measurement_frequency, domain=None, range=Optional[str])

slots.ismsObjective__objective_target_date = Slot(uri=ISO27001.objective_target_date, name="ismsObjective__objective_target_date", curie=ISO27001.curie('objective_target_date'),
                   model_uri=ISO27001.ismsObjective__objective_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsObjective__objective_achievement = Slot(uri=ISO27001.objective_achievement, name="ismsObjective__objective_achievement", curie=ISO27001.curie('objective_achievement'),
                   model_uri=ISO27001.ismsObjective__objective_achievement, domain=None, range=Optional[str])

slots.ismsObjective__objective_risks = Slot(uri=ISO27001.objective_risks, name="ismsObjective__objective_risks", curie=ISO27001.curie('objective_risks'),
                   model_uri=ISO27001.ismsObjective__objective_risks, domain=None, range=Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]])

slots.ismsObjective__objective_action_plan = Slot(uri=ISO27001.objective_action_plan, name="ismsObjective__objective_action_plan", curie=ISO27001.curie('objective_action_plan'),
                   model_uri=ISO27001.ismsObjective__objective_action_plan, domain=None, range=Optional[str])

slots.ismsObjective__objective_resources = Slot(uri=ISO27001.objective_resources, name="ismsObjective__objective_resources", curie=ISO27001.curie('objective_resources'),
                   model_uri=ISO27001.ismsObjective__objective_resources, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_acceptance_criteria = Slot(uri=ISO27001.risk_acceptance_criteria, name="ismsRiskAssessmentProcess__risk_acceptance_criteria", curie=ISO27001.curie('risk_acceptance_criteria'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_acceptance_criteria, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_assessment_criteria = Slot(uri=ISO27001.risk_assessment_criteria, name="ismsRiskAssessmentProcess__risk_assessment_criteria", curie=ISO27001.curie('risk_assessment_criteria'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_assessment_criteria, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_assessment_method = Slot(uri=ISO27001.risk_assessment_method, name="ismsRiskAssessmentProcess__risk_assessment_method", curie=ISO27001.curie('risk_assessment_method'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_assessment_method, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_likelihood_scale = Slot(uri=ISO27001.risk_likelihood_scale, name="ismsRiskAssessmentProcess__risk_likelihood_scale", curie=ISO27001.curie('risk_likelihood_scale'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_likelihood_scale, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_impact_scale = Slot(uri=ISO27001.risk_impact_scale, name="ismsRiskAssessmentProcess__risk_impact_scale", curie=ISO27001.curie('risk_impact_scale'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_impact_scale, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_matrix = Slot(uri=ISO27001.risk_matrix, name="ismsRiskAssessmentProcess__risk_matrix", curie=ISO27001.curie('risk_matrix'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_matrix, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_assessment_frequency = Slot(uri=ISO27001.risk_assessment_frequency, name="ismsRiskAssessmentProcess__risk_assessment_frequency", curie=ISO27001.curie('risk_assessment_frequency'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_assessment_frequency, domain=None, range=Optional[str])

slots.ismsRiskAssessmentProcess__risk_assessment_triggers = Slot(uri=ISO27001.risk_assessment_triggers, name="ismsRiskAssessmentProcess__risk_assessment_triggers", curie=ISO27001.curie('risk_assessment_triggers'),
                   model_uri=ISO27001.ismsRiskAssessmentProcess__risk_assessment_triggers, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRiskAssessment__assessment_scope = Slot(uri=ISO27001.assessment_scope, name="ismsRiskAssessment__assessment_scope", curie=ISO27001.curie('assessment_scope'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_scope, domain=None, range=Optional[str])

slots.ismsRiskAssessment__assessment_date = Slot(uri=ISO27001.assessment_date, name="ismsRiskAssessment__assessment_date", curie=ISO27001.curie('assessment_date'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsRiskAssessment__assessment_assessor = Slot(uri=ISO27001.assessment_assessor, name="ismsRiskAssessment__assessment_assessor", curie=ISO27001.curie('assessment_assessor'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_assessor, domain=None, range=Optional[str])

slots.ismsRiskAssessment__assessment_method_used = Slot(uri=ISO27001.assessment_method_used, name="ismsRiskAssessment__assessment_method_used", curie=ISO27001.curie('assessment_method_used'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_method_used, domain=None, range=Optional[str])

slots.ismsRiskAssessment__assessment_risks = Slot(uri=ISO27001.assessment_risks, name="ismsRiskAssessment__assessment_risks", curie=ISO27001.curie('assessment_risks'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_risks, domain=None, range=Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]])

slots.ismsRiskAssessment__assessment_summary = Slot(uri=ISO27001.assessment_summary, name="ismsRiskAssessment__assessment_summary", curie=ISO27001.curie('assessment_summary'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_summary, domain=None, range=Optional[str])

slots.ismsRiskAssessment__assessment_recommendations = Slot(uri=ISO27001.assessment_recommendations, name="ismsRiskAssessment__assessment_recommendations", curie=ISO27001.curie('assessment_recommendations'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_recommendations, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRiskAssessment__assessment_next_date = Slot(uri=ISO27001.assessment_next_date, name="ismsRiskAssessment__assessment_next_date", curie=ISO27001.curie('assessment_next_date'),
                   model_uri=ISO27001.ismsRiskAssessment__assessment_next_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsRisk__risk_source = Slot(uri=ISO27001.risk_source, name="ismsRisk__risk_source", curie=ISO27001.curie('risk_source'),
                   model_uri=ISO27001.ismsRisk__risk_source, domain=None, range=Optional[str])

slots.ismsRisk__risk_threat = Slot(uri=ISO27001.risk_threat, name="ismsRisk__risk_threat", curie=ISO27001.curie('risk_threat'),
                   model_uri=ISO27001.ismsRisk__risk_threat, domain=None, range=Optional[str])

slots.ismsRisk__risk_vulnerability = Slot(uri=ISO27001.risk_vulnerability, name="ismsRisk__risk_vulnerability", curie=ISO27001.curie('risk_vulnerability'),
                   model_uri=ISO27001.ismsRisk__risk_vulnerability, domain=None, range=Optional[str])

slots.ismsRisk__risk_owner = Slot(uri=ISO27001.risk_owner, name="ismsRisk__risk_owner", curie=ISO27001.curie('risk_owner'),
                   model_uri=ISO27001.ismsRisk__risk_owner, domain=None, range=Optional[str])

slots.ismsRisk__risk_likelihood = Slot(uri=ISO27001.risk_likelihood, name="ismsRisk__risk_likelihood", curie=ISO27001.curie('risk_likelihood'),
                   model_uri=ISO27001.ismsRisk__risk_likelihood, domain=None, range=Optional[Union[str, "IsmsLikelihood"]])

slots.ismsRisk__risk_impact = Slot(uri=ISO27001.risk_impact, name="ismsRisk__risk_impact", curie=ISO27001.curie('risk_impact'),
                   model_uri=ISO27001.ismsRisk__risk_impact, domain=None, range=Optional[Union[str, "IsmsImpact"]])

slots.ismsRisk__risk_inherent_level = Slot(uri=ISO27001.risk_inherent_level, name="ismsRisk__risk_inherent_level", curie=ISO27001.curie('risk_inherent_level'),
                   model_uri=ISO27001.ismsRisk__risk_inherent_level, domain=None, range=Optional[Union[str, "IsmsRiskLevel"]])

slots.ismsRisk__risk_existing_controls = Slot(uri=ISO27001.risk_existing_controls, name="ismsRisk__risk_existing_controls", curie=ISO27001.curie('risk_existing_controls'),
                   model_uri=ISO27001.ismsRisk__risk_existing_controls, domain=None, range=Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]])

slots.ismsRisk__risk_residual_level = Slot(uri=ISO27001.risk_residual_level, name="ismsRisk__risk_residual_level", curie=ISO27001.curie('risk_residual_level'),
                   model_uri=ISO27001.ismsRisk__risk_residual_level, domain=None, range=Optional[Union[str, "IsmsRiskLevel"]])

slots.ismsRisk__risk_treatment_option = Slot(uri=ISO27001.risk_treatment_option, name="ismsRisk__risk_treatment_option", curie=ISO27001.curie('risk_treatment_option'),
                   model_uri=ISO27001.ismsRisk__risk_treatment_option, domain=None, range=Optional[Union[str, "IsmsRiskTreatmentOption"]])

slots.ismsRisk__risk_treatment_priority = Slot(uri=ISO27001.risk_treatment_priority, name="ismsRisk__risk_treatment_priority", curie=ISO27001.curie('risk_treatment_priority'),
                   model_uri=ISO27001.ismsRisk__risk_treatment_priority, domain=None, range=Optional[str])

slots.ismsRiskTreatmentProcess__treatment_options_guidance = Slot(uri=ISO27001.treatment_options_guidance, name="ismsRiskTreatmentProcess__treatment_options_guidance", curie=ISO27001.curie('treatment_options_guidance'),
                   model_uri=ISO27001.ismsRiskTreatmentProcess__treatment_options_guidance, domain=None, range=Optional[str])

slots.ismsRiskTreatmentProcess__treatment_control_selection = Slot(uri=ISO27001.treatment_control_selection, name="ismsRiskTreatmentProcess__treatment_control_selection", curie=ISO27001.curie('treatment_control_selection'),
                   model_uri=ISO27001.ismsRiskTreatmentProcess__treatment_control_selection, domain=None, range=Optional[str])

slots.ismsRiskTreatmentProcess__treatment_annex_a_comparison = Slot(uri=ISO27001.treatment_annex_a_comparison, name="ismsRiskTreatmentProcess__treatment_annex_a_comparison", curie=ISO27001.curie('treatment_annex_a_comparison'),
                   model_uri=ISO27001.ismsRiskTreatmentProcess__treatment_annex_a_comparison, domain=None, range=Optional[str])

slots.ismsRiskTreatmentProcess__treatment_soa_template = Slot(uri=ISO27001.treatment_soa_template, name="ismsRiskTreatmentProcess__treatment_soa_template", curie=ISO27001.curie('treatment_soa_template'),
                   model_uri=ISO27001.ismsRiskTreatmentProcess__treatment_soa_template, domain=None, range=Optional[str])

slots.ismsRiskTreatmentProcess__treatment_approval_workflow = Slot(uri=ISO27001.treatment_approval_workflow, name="ismsRiskTreatmentProcess__treatment_approval_workflow", curie=ISO27001.curie('treatment_approval_workflow'),
                   model_uri=ISO27001.ismsRiskTreatmentProcess__treatment_approval_workflow, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_scope = Slot(uri=ISO27001.plan_scope, name="ismsRiskTreatmentPlan__plan_scope", curie=ISO27001.curie('plan_scope'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_scope, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_risks = Slot(uri=ISO27001.plan_risks, name="ismsRiskTreatmentPlan__plan_risks", curie=ISO27001.curie('plan_risks'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_risks, domain=None, range=Optional[Union[Union[str, IsmsRiskIsmsId], list[Union[str, IsmsRiskIsmsId]]]])

slots.ismsRiskTreatmentPlan__plan_actions = Slot(uri=ISO27001.plan_actions, name="ismsRiskTreatmentPlan__plan_actions", curie=ISO27001.curie('plan_actions'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRiskTreatmentPlan__plan_controls = Slot(uri=ISO27001.plan_controls, name="ismsRiskTreatmentPlan__plan_controls", curie=ISO27001.curie('plan_controls'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_controls, domain=None, range=Optional[Union[Union[str, IsmsControlIsmsId], list[Union[str, IsmsControlIsmsId]]]])

slots.ismsRiskTreatmentPlan__plan_resources = Slot(uri=ISO27001.plan_resources, name="ismsRiskTreatmentPlan__plan_resources", curie=ISO27001.curie('plan_resources'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_resources, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_responsible_parties = Slot(uri=ISO27001.plan_responsible_parties, name="ismsRiskTreatmentPlan__plan_responsible_parties", curie=ISO27001.curie('plan_responsible_parties'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_responsible_parties, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsRiskTreatmentPlan__plan_timeline = Slot(uri=ISO27001.plan_timeline, name="ismsRiskTreatmentPlan__plan_timeline", curie=ISO27001.curie('plan_timeline'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_timeline, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_risk_owner_approval = Slot(uri=ISO27001.plan_risk_owner_approval, name="ismsRiskTreatmentPlan__plan_risk_owner_approval", curie=ISO27001.curie('plan_risk_owner_approval'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_risk_owner_approval, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_residual_risk_acceptance = Slot(uri=ISO27001.plan_residual_risk_acceptance, name="ismsRiskTreatmentPlan__plan_residual_risk_acceptance", curie=ISO27001.curie('plan_residual_risk_acceptance'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_residual_risk_acceptance, domain=None, range=Optional[str])

slots.ismsRiskTreatmentPlan__plan_completion_date = Slot(uri=ISO27001.plan_completion_date, name="ismsRiskTreatmentPlan__plan_completion_date", curie=ISO27001.curie('plan_completion_date'),
                   model_uri=ISO27001.ismsRiskTreatmentPlan__plan_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsStatementOfApplicability__soa_entries = Slot(uri=ISO27001.soa_entries, name="ismsStatementOfApplicability__soa_entries", curie=ISO27001.curie('soa_entries'),
                   model_uri=ISO27001.ismsStatementOfApplicability__soa_entries, domain=None, range=Optional[Union[Union[dict, IsmsApplicabilityEntry], list[Union[dict, IsmsApplicabilityEntry]]]])

slots.ismsApplicabilityEntry__entry_type = Slot(uri=ISO27001.entry_type, name="ismsApplicabilityEntry__entry_type", curie=ISO27001.curie('entry_type'),
                   model_uri=ISO27001.ismsApplicabilityEntry__entry_type, domain=None, range=Optional[str])

slots.ismsApplicabilityEntry__entry_justification = Slot(uri=ISO27001.entry_justification, name="ismsApplicabilityEntry__entry_justification", curie=ISO27001.curie('entry_justification'),
                   model_uri=ISO27001.ismsApplicabilityEntry__entry_justification, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.ismsIncludedControl__included_control = Slot(uri=ISO27001.included_control, name="ismsIncludedControl__included_control", curie=ISO27001.curie('included_control'),
                   model_uri=ISO27001.ismsIncludedControl__included_control, domain=None, range=Optional[Union[str, IsmsControlIsmsId]])

slots.ismsIncludedControl__included_evidence = Slot(uri=ISO27001.included_evidence, name="ismsIncludedControl__included_evidence", curie=ISO27001.curie('included_evidence'),
                   model_uri=ISO27001.ismsIncludedControl__included_evidence, domain=None, range=Optional[str])

slots.ismsIncludedControl__included_target_date = Slot(uri=ISO27001.included_target_date, name="ismsIncludedControl__included_target_date", curie=ISO27001.curie('included_target_date'),
                   model_uri=ISO27001.ismsIncludedControl__included_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsControl__control_annex_a_controls = Slot(uri=ISO27001.control_annex_a_controls, name="ismsControl__control_annex_a_controls", curie=ISO27001.curie('control_annex_a_controls'),
                   model_uri=ISO27001.ismsControl__control_annex_a_controls, domain=None, range=Optional[Union[Union[str, "IsmsAnnexAControl"], list[Union[str, "IsmsAnnexAControl"]]]])

slots.ismsControl__control_theme = Slot(uri=ISO27001.control_theme, name="ismsControl__control_theme", curie=ISO27001.curie('control_theme'),
                   model_uri=ISO27001.ismsControl__control_theme, domain=None, range=Optional[Union[str, "IsmsControlTheme"]])

slots.ismsControl__control_text = Slot(uri=ISO27001.control_text, name="ismsControl__control_text", curie=ISO27001.curie('control_text'),
                   model_uri=ISO27001.ismsControl__control_text, domain=None, range=Optional[str])

slots.ismsControl__control_guidance = Slot(uri=ISO27001.control_guidance, name="ismsControl__control_guidance", curie=ISO27001.curie('control_guidance'),
                   model_uri=ISO27001.ismsControl__control_guidance, domain=None, range=Optional[str])

slots.ismsControl__control_threats = Slot(uri=ISO27001.control_threats, name="ismsControl__control_threats", curie=ISO27001.curie('control_threats'),
                   model_uri=ISO27001.ismsControl__control_threats, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsControl__control_asset_types = Slot(uri=ISO27001.control_asset_types, name="ismsControl__control_asset_types", curie=ISO27001.curie('control_asset_types'),
                   model_uri=ISO27001.ismsControl__control_asset_types, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsControl__control_owner = Slot(uri=ISO27001.control_owner, name="ismsControl__control_owner", curie=ISO27001.curie('control_owner'),
                   model_uri=ISO27001.ismsControl__control_owner, domain=None, range=Optional[str])

slots.ismsControl__control_implementation_date = Slot(uri=ISO27001.control_implementation_date, name="ismsControl__control_implementation_date", curie=ISO27001.curie('control_implementation_date'),
                   model_uri=ISO27001.ismsControl__control_implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsControl__control_effectiveness = Slot(uri=ISO27001.control_effectiveness, name="ismsControl__control_effectiveness", curie=ISO27001.curie('control_effectiveness'),
                   model_uri=ISO27001.ismsControl__control_effectiveness, domain=None, range=Optional[str])

slots.ismsControl__control_last_tested = Slot(uri=ISO27001.control_last_tested, name="ismsControl__control_last_tested", curie=ISO27001.curie('control_last_tested'),
                   model_uri=ISO27001.ismsControl__control_last_tested, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsControl__control_evidence = Slot(uri=ISO27001.control_evidence, name="ismsControl__control_evidence", curie=ISO27001.curie('control_evidence'),
                   model_uri=ISO27001.ismsControl__control_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAsset__asset_category = Slot(uri=ISO27001.asset_category, name="ismsAsset__asset_category", curie=ISO27001.curie('asset_category'),
                   model_uri=ISO27001.ismsAsset__asset_category, domain=None, range=Optional[str])

slots.ismsAsset__asset_owner = Slot(uri=ISO27001.asset_owner, name="ismsAsset__asset_owner", curie=ISO27001.curie('asset_owner'),
                   model_uri=ISO27001.ismsAsset__asset_owner, domain=None, range=Optional[str])

slots.ismsAsset__asset_custodian = Slot(uri=ISO27001.asset_custodian, name="ismsAsset__asset_custodian", curie=ISO27001.curie('asset_custodian'),
                   model_uri=ISO27001.ismsAsset__asset_custodian, domain=None, range=Optional[str])

slots.ismsAsset__asset_classification = Slot(uri=ISO27001.asset_classification, name="ismsAsset__asset_classification", curie=ISO27001.curie('asset_classification'),
                   model_uri=ISO27001.ismsAsset__asset_classification, domain=None, range=Optional[str])

slots.ismsAsset__asset_location = Slot(uri=ISO27001.asset_location, name="ismsAsset__asset_location", curie=ISO27001.curie('asset_location'),
                   model_uri=ISO27001.ismsAsset__asset_location, domain=None, range=Optional[str])

slots.ismsAsset__asset_criticality = Slot(uri=ISO27001.asset_criticality, name="ismsAsset__asset_criticality", curie=ISO27001.curie('asset_criticality'),
                   model_uri=ISO27001.ismsAsset__asset_criticality, domain=None, range=Optional[str])

slots.ismsResource__resource_category = Slot(uri=ISO27001.resource_category, name="ismsResource__resource_category", curie=ISO27001.curie('resource_category'),
                   model_uri=ISO27001.ismsResource__resource_category, domain=None, range=Optional[str])

slots.ismsResource__resource_quantity = Slot(uri=ISO27001.resource_quantity, name="ismsResource__resource_quantity", curie=ISO27001.curie('resource_quantity'),
                   model_uri=ISO27001.ismsResource__resource_quantity, domain=None, range=Optional[str])

slots.ismsResource__resource_allocation_date = Slot(uri=ISO27001.resource_allocation_date, name="ismsResource__resource_allocation_date", curie=ISO27001.curie('resource_allocation_date'),
                   model_uri=ISO27001.ismsResource__resource_allocation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsResource__resource_allocated_to = Slot(uri=ISO27001.resource_allocated_to, name="ismsResource__resource_allocated_to", curie=ISO27001.curie('resource_allocated_to'),
                   model_uri=ISO27001.ismsResource__resource_allocated_to, domain=None, range=Optional[str])

slots.ismsResource__resource_cost = Slot(uri=ISO27001.resource_cost, name="ismsResource__resource_cost", curie=ISO27001.curie('resource_cost'),
                   model_uri=ISO27001.ismsResource__resource_cost, domain=None, range=Optional[str])

slots.ismsResource__resource_availability = Slot(uri=ISO27001.resource_availability, name="ismsResource__resource_availability", curie=ISO27001.curie('resource_availability'),
                   model_uri=ISO27001.ismsResource__resource_availability, domain=None, range=Optional[str])

slots.ismsCompetenceRecord__competence_person = Slot(uri=ISO27001.competence_person, name="ismsCompetenceRecord__competence_person", curie=ISO27001.curie('competence_person'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_person, domain=None, range=Optional[str])

slots.ismsCompetenceRecord__competence_role = Slot(uri=ISO27001.competence_role, name="ismsCompetenceRecord__competence_role", curie=ISO27001.curie('competence_role'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_role, domain=None, range=Optional[Union[str, IsmsRoleIsmsId]])

slots.ismsCompetenceRecord__competence_required = Slot(uri=ISO27001.competence_required, name="ismsCompetenceRecord__competence_required", curie=ISO27001.curie('competence_required'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_required, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsCompetenceRecord__competence_education = Slot(uri=ISO27001.competence_education, name="ismsCompetenceRecord__competence_education", curie=ISO27001.curie('competence_education'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_education, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsCompetenceRecord__competence_training = Slot(uri=ISO27001.competence_training, name="ismsCompetenceRecord__competence_training", curie=ISO27001.curie('competence_training'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_training, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsCompetenceRecord__competence_experience = Slot(uri=ISO27001.competence_experience, name="ismsCompetenceRecord__competence_experience", curie=ISO27001.curie('competence_experience'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_experience, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsCompetenceRecord__competence_assessment_date = Slot(uri=ISO27001.competence_assessment_date, name="ismsCompetenceRecord__competence_assessment_date", curie=ISO27001.curie('competence_assessment_date'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsCompetenceRecord__competence_gaps = Slot(uri=ISO27001.competence_gaps, name="ismsCompetenceRecord__competence_gaps", curie=ISO27001.curie('competence_gaps'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_gaps, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsCompetenceRecord__competence_actions = Slot(uri=ISO27001.competence_actions, name="ismsCompetenceRecord__competence_actions", curie=ISO27001.curie('competence_actions'),
                   model_uri=ISO27001.ismsCompetenceRecord__competence_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAwarenessProgramme__awareness_topics = Slot(uri=ISO27001.awareness_topics, name="ismsAwarenessProgramme__awareness_topics", curie=ISO27001.curie('awareness_topics'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAwarenessProgramme__awareness_methods = Slot(uri=ISO27001.awareness_methods, name="ismsAwarenessProgramme__awareness_methods", curie=ISO27001.curie('awareness_methods'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAwarenessProgramme__awareness_audience = Slot(uri=ISO27001.awareness_audience, name="ismsAwarenessProgramme__awareness_audience", curie=ISO27001.curie('awareness_audience'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_audience, domain=None, range=Optional[str])

slots.ismsAwarenessProgramme__awareness_frequency = Slot(uri=ISO27001.awareness_frequency, name="ismsAwarenessProgramme__awareness_frequency", curie=ISO27001.curie('awareness_frequency'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_frequency, domain=None, range=Optional[str])

slots.ismsAwarenessProgramme__awareness_completion_tracking = Slot(uri=ISO27001.awareness_completion_tracking, name="ismsAwarenessProgramme__awareness_completion_tracking", curie=ISO27001.curie('awareness_completion_tracking'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_completion_tracking, domain=None, range=Optional[str])

slots.ismsAwarenessProgramme__awareness_effectiveness = Slot(uri=ISO27001.awareness_effectiveness, name="ismsAwarenessProgramme__awareness_effectiveness", curie=ISO27001.curie('awareness_effectiveness'),
                   model_uri=ISO27001.ismsAwarenessProgramme__awareness_effectiveness, domain=None, range=Optional[str])

slots.ismsCommunicationPlan__communication_items = Slot(uri=ISO27001.communication_items, name="ismsCommunicationPlan__communication_items", curie=ISO27001.curie('communication_items'),
                   model_uri=ISO27001.ismsCommunicationPlan__communication_items, domain=None, range=Optional[Union[Union[dict, IsmsCommunication], list[Union[dict, IsmsCommunication]]]])

slots.ismsCommunication__communication_subject = Slot(uri=ISO27001.communication_subject, name="ismsCommunication__communication_subject", curie=ISO27001.curie('communication_subject'),
                   model_uri=ISO27001.ismsCommunication__communication_subject, domain=None, range=str)

slots.ismsCommunication__communication_purpose = Slot(uri=ISO27001.communication_purpose, name="ismsCommunication__communication_purpose", curie=ISO27001.curie('communication_purpose'),
                   model_uri=ISO27001.ismsCommunication__communication_purpose, domain=None, range=Optional[str])

slots.ismsCommunication__communication_audience = Slot(uri=ISO27001.communication_audience, name="ismsCommunication__communication_audience", curie=ISO27001.curie('communication_audience'),
                   model_uri=ISO27001.ismsCommunication__communication_audience, domain=None, range=Optional[str])

slots.ismsCommunication__communication_frequency = Slot(uri=ISO27001.communication_frequency, name="ismsCommunication__communication_frequency", curie=ISO27001.curie('communication_frequency'),
                   model_uri=ISO27001.ismsCommunication__communication_frequency, domain=None, range=Optional[str])

slots.ismsCommunication__communication_method = Slot(uri=ISO27001.communication_method, name="ismsCommunication__communication_method", curie=ISO27001.curie('communication_method'),
                   model_uri=ISO27001.ismsCommunication__communication_method, domain=None, range=Optional[str])

slots.ismsCommunication__communication_records_required = Slot(uri=ISO27001.communication_records_required, name="ismsCommunication__communication_records_required", curie=ISO27001.curie('communication_records_required'),
                   model_uri=ISO27001.ismsCommunication__communication_records_required, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsDocumentedInformation__document_kind = Slot(uri=ISO27001.document_kind, name="ismsDocumentedInformation__document_kind", curie=ISO27001.curie('document_kind'),
                   model_uri=ISO27001.ismsDocumentedInformation__document_kind, domain=None, range=Union[str, "IsmsDocumentKind"])

slots.ismsOperationalProcedure__procedure_scope = Slot(uri=ISO27001.procedure_scope, name="ismsOperationalProcedure__procedure_scope", curie=ISO27001.curie('procedure_scope'),
                   model_uri=ISO27001.ismsOperationalProcedure__procedure_scope, domain=None, range=Optional[str])

slots.ismsOperationalProcedure__procedure_criteria = Slot(uri=ISO27001.procedure_criteria, name="ismsOperationalProcedure__procedure_criteria", curie=ISO27001.curie('procedure_criteria'),
                   model_uri=ISO27001.ismsOperationalProcedure__procedure_criteria, domain=None, range=Optional[str])

slots.ismsOperationalProcedure__procedure_control_measures = Slot(uri=ISO27001.procedure_control_measures, name="ismsOperationalProcedure__procedure_control_measures", curie=ISO27001.curie('procedure_control_measures'),
                   model_uri=ISO27001.ismsOperationalProcedure__procedure_control_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsOperationalProcedure__procedure_roles = Slot(uri=ISO27001.procedure_roles, name="ismsOperationalProcedure__procedure_roles", curie=ISO27001.curie('procedure_roles'),
                   model_uri=ISO27001.ismsOperationalProcedure__procedure_roles, domain=None, range=Optional[Union[Union[str, IsmsRoleIsmsId], list[Union[str, IsmsRoleIsmsId]]]])

slots.ismsOperationalProcedure__procedure_change_control = Slot(uri=ISO27001.procedure_change_control, name="ismsOperationalProcedure__procedure_change_control", curie=ISO27001.curie('procedure_change_control'),
                   model_uri=ISO27001.ismsOperationalProcedure__procedure_change_control, domain=None, range=Optional[str])

slots.ismsMonitoringProgramme__monitoring_items = Slot(uri=ISO27001.monitoring_items, name="ismsMonitoringProgramme__monitoring_items", curie=ISO27001.curie('monitoring_items'),
                   model_uri=ISO27001.ismsMonitoringProgramme__monitoring_items, domain=None, range=Optional[Union[Union[dict, IsmsMonitoringItem], list[Union[dict, IsmsMonitoringItem]]]])

slots.ismsMonitoringItem__monitoring_metric = Slot(uri=ISO27001.monitoring_metric, name="ismsMonitoringItem__monitoring_metric", curie=ISO27001.curie('monitoring_metric'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_metric, domain=None, range=str)

slots.ismsMonitoringItem__monitoring_description = Slot(uri=ISO27001.monitoring_description, name="ismsMonitoringItem__monitoring_description", curie=ISO27001.curie('monitoring_description'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_description, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_method = Slot(uri=ISO27001.monitoring_method, name="ismsMonitoringItem__monitoring_method", curie=ISO27001.curie('monitoring_method'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_method, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_frequency = Slot(uri=ISO27001.monitoring_frequency, name="ismsMonitoringItem__monitoring_frequency", curie=ISO27001.curie('monitoring_frequency'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_frequency, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_analysis_frequency = Slot(uri=ISO27001.monitoring_analysis_frequency, name="ismsMonitoringItem__monitoring_analysis_frequency", curie=ISO27001.curie('monitoring_analysis_frequency'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_analysis_frequency, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_analyst = Slot(uri=ISO27001.monitoring_analyst, name="ismsMonitoringItem__monitoring_analyst", curie=ISO27001.curie('monitoring_analyst'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_analyst, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_target = Slot(uri=ISO27001.monitoring_target, name="ismsMonitoringItem__monitoring_target", curie=ISO27001.curie('monitoring_target'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_target, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_alert_threshold = Slot(uri=ISO27001.monitoring_alert_threshold, name="ismsMonitoringItem__monitoring_alert_threshold", curie=ISO27001.curie('monitoring_alert_threshold'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_alert_threshold, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_current_value = Slot(uri=ISO27001.monitoring_current_value, name="ismsMonitoringItem__monitoring_current_value", curie=ISO27001.curie('monitoring_current_value'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_current_value, domain=None, range=Optional[str])

slots.ismsMonitoringItem__monitoring_trend = Slot(uri=ISO27001.monitoring_trend, name="ismsMonitoringItem__monitoring_trend", curie=ISO27001.curie('monitoring_trend'),
                   model_uri=ISO27001.ismsMonitoringItem__monitoring_trend, domain=None, range=Optional[str])

slots.ismsAuditProgramme__programme_period = Slot(uri=ISO27001.programme_period, name="ismsAuditProgramme__programme_period", curie=ISO27001.curie('programme_period'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_period, domain=None, range=Optional[str])

slots.ismsAuditProgramme__programme_audits = Slot(uri=ISO27001.programme_audits, name="ismsAuditProgramme__programme_audits", curie=ISO27001.curie('programme_audits'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_audits, domain=None, range=Optional[Union[Union[str, IsmsAuditIsmsId], list[Union[str, IsmsAuditIsmsId]]]])

slots.ismsAuditProgramme__programme_frequency_rationale = Slot(uri=ISO27001.programme_frequency_rationale, name="ismsAuditProgramme__programme_frequency_rationale", curie=ISO27001.curie('programme_frequency_rationale'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_frequency_rationale, domain=None, range=Optional[str])

slots.ismsAuditProgramme__programme_resources = Slot(uri=ISO27001.programme_resources, name="ismsAuditProgramme__programme_resources", curie=ISO27001.curie('programme_resources'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_resources, domain=None, range=Optional[str])

slots.ismsAuditProgramme__programme_auditor_qualifications = Slot(uri=ISO27001.programme_auditor_qualifications, name="ismsAuditProgramme__programme_auditor_qualifications", curie=ISO27001.curie('programme_auditor_qualifications'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_auditor_qualifications, domain=None, range=Optional[str])

slots.ismsAuditProgramme__programme_status = Slot(uri=ISO27001.programme_status, name="ismsAuditProgramme__programme_status", curie=ISO27001.curie('programme_status'),
                   model_uri=ISO27001.ismsAuditProgramme__programme_status, domain=None, range=Optional[str])

slots.ismsAudit__audit_type = Slot(uri=ISO27001.audit_type, name="ismsAudit__audit_type", curie=ISO27001.curie('audit_type'),
                   model_uri=ISO27001.ismsAudit__audit_type, domain=None, range=Union[str, "IsmsAuditType"])

slots.ismsAudit__audit_standards = Slot(uri=ISO27001.audit_standards, name="ismsAudit__audit_standards", curie=ISO27001.curie('audit_standards'),
                   model_uri=ISO27001.ismsAudit__audit_standards, domain=None, range=Optional[Union[Union[str, "IsmsManagementSystemStandard"], list[Union[str, "IsmsManagementSystemStandard"]]]])

slots.ismsAudit__audit_scope = Slot(uri=ISO27001.audit_scope, name="ismsAudit__audit_scope", curie=ISO27001.curie('audit_scope'),
                   model_uri=ISO27001.ismsAudit__audit_scope, domain=None, range=Optional[str])

slots.ismsAudit__audit_criteria = Slot(uri=ISO27001.audit_criteria, name="ismsAudit__audit_criteria", curie=ISO27001.curie('audit_criteria'),
                   model_uri=ISO27001.ismsAudit__audit_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAudit__audit_objectives = Slot(uri=ISO27001.audit_objectives, name="ismsAudit__audit_objectives", curie=ISO27001.curie('audit_objectives'),
                   model_uri=ISO27001.ismsAudit__audit_objectives, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAudit__audit_period_start = Slot(uri=ISO27001.audit_period_start, name="ismsAudit__audit_period_start", curie=ISO27001.curie('audit_period_start'),
                   model_uri=ISO27001.ismsAudit__audit_period_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsAudit__audit_period_end = Slot(uri=ISO27001.audit_period_end, name="ismsAudit__audit_period_end", curie=ISO27001.curie('audit_period_end'),
                   model_uri=ISO27001.ismsAudit__audit_period_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsAudit__audit_lead = Slot(uri=ISO27001.audit_lead, name="ismsAudit__audit_lead", curie=ISO27001.curie('audit_lead'),
                   model_uri=ISO27001.ismsAudit__audit_lead, domain=None, range=Optional[str])

slots.ismsAudit__audit_team = Slot(uri=ISO27001.audit_team, name="ismsAudit__audit_team", curie=ISO27001.curie('audit_team'),
                   model_uri=ISO27001.ismsAudit__audit_team, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAudit__audit_auditees = Slot(uri=ISO27001.audit_auditees, name="ismsAudit__audit_auditees", curie=ISO27001.curie('audit_auditees'),
                   model_uri=ISO27001.ismsAudit__audit_auditees, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAudit__audit_plan = Slot(uri=ISO27001.audit_plan, name="ismsAudit__audit_plan", curie=ISO27001.curie('audit_plan'),
                   model_uri=ISO27001.ismsAudit__audit_plan, domain=None, range=Optional[Union[str, IsmsDocumentedInformationIsmsId]])

slots.ismsAudit__audit_findings = Slot(uri=ISO27001.audit_findings, name="ismsAudit__audit_findings", curie=ISO27001.curie('audit_findings'),
                   model_uri=ISO27001.ismsAudit__audit_findings, domain=None, range=Optional[Union[dict[Union[str, IsmsAuditFindingIsmsId], Union[dict, IsmsAuditFinding]], list[Union[dict, IsmsAuditFinding]]]])

slots.ismsAudit__audit_conclusion = Slot(uri=ISO27001.audit_conclusion, name="ismsAudit__audit_conclusion", curie=ISO27001.curie('audit_conclusion'),
                   model_uri=ISO27001.ismsAudit__audit_conclusion, domain=None, range=Optional[str])

slots.ismsAudit__audit_report_date = Slot(uri=ISO27001.audit_report_date, name="ismsAudit__audit_report_date", curie=ISO27001.curie('audit_report_date'),
                   model_uri=ISO27001.ismsAudit__audit_report_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsAudit__audit_report_distribution = Slot(uri=ISO27001.audit_report_distribution, name="ismsAudit__audit_report_distribution", curie=ISO27001.curie('audit_report_distribution'),
                   model_uri=ISO27001.ismsAudit__audit_report_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsAuditFinding__finding_type = Slot(uri=ISO27001.finding_type, name="ismsAuditFinding__finding_type", curie=ISO27001.curie('finding_type'),
                   model_uri=ISO27001.ismsAuditFinding__finding_type, domain=None, range=Union[str, "IsmsAuditFindingType"])

slots.ismsAuditFinding__finding_requirement = Slot(uri=ISO27001.finding_requirement, name="ismsAuditFinding__finding_requirement", curie=ISO27001.curie('finding_requirement'),
                   model_uri=ISO27001.ismsAuditFinding__finding_requirement, domain=None, range=Optional[Union[str, IsmsRequirementReference]])

slots.ismsAuditFinding__finding_control = Slot(uri=ISO27001.finding_control, name="ismsAuditFinding__finding_control", curie=ISO27001.curie('finding_control'),
                   model_uri=ISO27001.ismsAuditFinding__finding_control, domain=None, range=Optional[Union[str, IsmsControlIsmsId]])

slots.ismsAuditFinding__finding_evidence = Slot(uri=ISO27001.finding_evidence, name="ismsAuditFinding__finding_evidence", curie=ISO27001.curie('finding_evidence'),
                   model_uri=ISO27001.ismsAuditFinding__finding_evidence, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_root_cause = Slot(uri=ISO27001.finding_root_cause, name="ismsAuditFinding__finding_root_cause", curie=ISO27001.curie('finding_root_cause'),
                   model_uri=ISO27001.ismsAuditFinding__finding_root_cause, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_risk = Slot(uri=ISO27001.finding_risk, name="ismsAuditFinding__finding_risk", curie=ISO27001.curie('finding_risk'),
                   model_uri=ISO27001.ismsAuditFinding__finding_risk, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_recommendation = Slot(uri=ISO27001.finding_recommendation, name="ismsAuditFinding__finding_recommendation", curie=ISO27001.curie('finding_recommendation'),
                   model_uri=ISO27001.ismsAuditFinding__finding_recommendation, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_auditee_response = Slot(uri=ISO27001.finding_auditee_response, name="ismsAuditFinding__finding_auditee_response", curie=ISO27001.curie('finding_auditee_response'),
                   model_uri=ISO27001.ismsAuditFinding__finding_auditee_response, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_corrective_action = Slot(uri=ISO27001.finding_corrective_action, name="ismsAuditFinding__finding_corrective_action", curie=ISO27001.curie('finding_corrective_action'),
                   model_uri=ISO27001.ismsAuditFinding__finding_corrective_action, domain=None, range=Optional[Union[str, IsmsCorrectiveActionIsmsId]])

slots.ismsAuditFinding__finding_closure_status = Slot(uri=ISO27001.finding_closure_status, name="ismsAuditFinding__finding_closure_status", curie=ISO27001.curie('finding_closure_status'),
                   model_uri=ISO27001.ismsAuditFinding__finding_closure_status, domain=None, range=Optional[str])

slots.ismsAuditFinding__finding_closure_date = Slot(uri=ISO27001.finding_closure_date, name="ismsAuditFinding__finding_closure_date", curie=ISO27001.curie('finding_closure_date'),
                   model_uri=ISO27001.ismsAuditFinding__finding_closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsManagementReview__review_held_on = Slot(uri=ISO27001.review_held_on, name="ismsManagementReview__review_held_on", curie=ISO27001.curie('review_held_on'),
                   model_uri=ISO27001.ismsManagementReview__review_held_on, domain=None, range=Union[str, XSDDate])

slots.ismsManagementReview__review_attendees = Slot(uri=ISO27001.review_attendees, name="ismsManagementReview__review_attendees", curie=ISO27001.curie('review_attendees'),
                   model_uri=ISO27001.ismsManagementReview__review_attendees, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementReview__review_previous_actions = Slot(uri=ISO27001.review_previous_actions, name="ismsManagementReview__review_previous_actions", curie=ISO27001.curie('review_previous_actions'),
                   model_uri=ISO27001.ismsManagementReview__review_previous_actions, domain=None, range=Optional[str])

slots.ismsManagementReview__review_context_changes = Slot(uri=ISO27001.review_context_changes, name="ismsManagementReview__review_context_changes", curie=ISO27001.curie('review_context_changes'),
                   model_uri=ISO27001.ismsManagementReview__review_context_changes, domain=None, range=Optional[str])

slots.ismsManagementReview__review_interested_party_changes = Slot(uri=ISO27001.review_interested_party_changes, name="ismsManagementReview__review_interested_party_changes", curie=ISO27001.curie('review_interested_party_changes'),
                   model_uri=ISO27001.ismsManagementReview__review_interested_party_changes, domain=None, range=Optional[str])

slots.ismsManagementReview__review_interested_party_feedback = Slot(uri=ISO27001.review_interested_party_feedback, name="ismsManagementReview__review_interested_party_feedback", curie=ISO27001.curie('review_interested_party_feedback'),
                   model_uri=ISO27001.ismsManagementReview__review_interested_party_feedback, domain=None, range=Optional[str])

slots.ismsManagementReview__review_performance_trends = Slot(uri=ISO27001.review_performance_trends, name="ismsManagementReview__review_performance_trends", curie=ISO27001.curie('review_performance_trends'),
                   model_uri=ISO27001.ismsManagementReview__review_performance_trends, domain=None, range=Optional[str])

slots.ismsManagementReview__review_audit_results = Slot(uri=ISO27001.review_audit_results, name="ismsManagementReview__review_audit_results", curie=ISO27001.curie('review_audit_results'),
                   model_uri=ISO27001.ismsManagementReview__review_audit_results, domain=None, range=Optional[str])

slots.ismsManagementReview__review_risk_assessment_results = Slot(uri=ISO27001.review_risk_assessment_results, name="ismsManagementReview__review_risk_assessment_results", curie=ISO27001.curie('review_risk_assessment_results'),
                   model_uri=ISO27001.ismsManagementReview__review_risk_assessment_results, domain=None, range=Optional[str])

slots.ismsManagementReview__review_risk_treatment_status = Slot(uri=ISO27001.review_risk_treatment_status, name="ismsManagementReview__review_risk_treatment_status", curie=ISO27001.curie('review_risk_treatment_status'),
                   model_uri=ISO27001.ismsManagementReview__review_risk_treatment_status, domain=None, range=Optional[str])

slots.ismsManagementReview__review_risks_and_opportunities = Slot(uri=ISO27001.review_risks_and_opportunities, name="ismsManagementReview__review_risks_and_opportunities", curie=ISO27001.curie('review_risks_and_opportunities'),
                   model_uri=ISO27001.ismsManagementReview__review_risks_and_opportunities, domain=None, range=Optional[str])

slots.ismsManagementReview__review_improvement_opportunities = Slot(uri=ISO27001.review_improvement_opportunities, name="ismsManagementReview__review_improvement_opportunities", curie=ISO27001.curie('review_improvement_opportunities'),
                   model_uri=ISO27001.ismsManagementReview__review_improvement_opportunities, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementReview__review_decisions = Slot(uri=ISO27001.review_decisions, name="ismsManagementReview__review_decisions", curie=ISO27001.curie('review_decisions'),
                   model_uri=ISO27001.ismsManagementReview__review_decisions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementReview__review_actions = Slot(uri=ISO27001.review_actions, name="ismsManagementReview__review_actions", curie=ISO27001.curie('review_actions'),
                   model_uri=ISO27001.ismsManagementReview__review_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsManagementReview__review_next_date = Slot(uri=ISO27001.review_next_date, name="ismsManagementReview__review_next_date", curie=ISO27001.curie('review_next_date'),
                   model_uri=ISO27001.ismsManagementReview__review_next_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsNonconformity__nonconformity_source = Slot(uri=ISO27001.nonconformity_source, name="ismsNonconformity__nonconformity_source", curie=ISO27001.curie('nonconformity_source'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_source, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_detected_on = Slot(uri=ISO27001.nonconformity_detected_on, name="ismsNonconformity__nonconformity_detected_on", curie=ISO27001.curie('nonconformity_detected_on'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_detected_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsNonconformity__nonconformity_detected_by = Slot(uri=ISO27001.nonconformity_detected_by, name="ismsNonconformity__nonconformity_detected_by", curie=ISO27001.curie('nonconformity_detected_by'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_detected_by, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_requirement = Slot(uri=ISO27001.nonconformity_requirement, name="ismsNonconformity__nonconformity_requirement", curie=ISO27001.curie('nonconformity_requirement'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_requirement, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_immediate_actions = Slot(uri=ISO27001.nonconformity_immediate_actions, name="ismsNonconformity__nonconformity_immediate_actions", curie=ISO27001.curie('nonconformity_immediate_actions'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsNonconformity__nonconformity_consequences = Slot(uri=ISO27001.nonconformity_consequences, name="ismsNonconformity__nonconformity_consequences", curie=ISO27001.curie('nonconformity_consequences'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_consequences, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_root_cause = Slot(uri=ISO27001.nonconformity_root_cause, name="ismsNonconformity__nonconformity_root_cause", curie=ISO27001.curie('nonconformity_root_cause'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_root_cause, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_similar_check = Slot(uri=ISO27001.nonconformity_similar_check, name="ismsNonconformity__nonconformity_similar_check", curie=ISO27001.curie('nonconformity_similar_check'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_similar_check, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_status = Slot(uri=ISO27001.nonconformity_status, name="ismsNonconformity__nonconformity_status", curie=ISO27001.curie('nonconformity_status'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_status, domain=None, range=Optional[str])

slots.ismsNonconformity__nonconformity_closure_date = Slot(uri=ISO27001.nonconformity_closure_date, name="ismsNonconformity__nonconformity_closure_date", curie=ISO27001.curie('nonconformity_closure_date'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsNonconformity__nonconformity_closure_evidence = Slot(uri=ISO27001.nonconformity_closure_evidence, name="ismsNonconformity__nonconformity_closure_evidence", curie=ISO27001.curie('nonconformity_closure_evidence'),
                   model_uri=ISO27001.ismsNonconformity__nonconformity_closure_evidence, domain=None, range=Optional[str])

slots.ismsCorrectiveAction__action_nonconformities = Slot(uri=ISO27001.action_nonconformities, name="ismsCorrectiveAction__action_nonconformities", curie=ISO27001.curie('action_nonconformities'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_nonconformities, domain=None, range=Optional[Union[Union[str, IsmsNonconformityIsmsId], list[Union[str, IsmsNonconformityIsmsId]]]])

slots.ismsCorrectiveAction__action_root_cause = Slot(uri=ISO27001.action_root_cause, name="ismsCorrectiveAction__action_root_cause", curie=ISO27001.curie('action_root_cause'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_root_cause, domain=None, range=Optional[str])

slots.ismsCorrectiveAction__action_target_date = Slot(uri=ISO27001.action_target_date, name="ismsCorrectiveAction__action_target_date", curie=ISO27001.curie('action_target_date'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsCorrectiveAction__action_completion_date = Slot(uri=ISO27001.action_completion_date, name="ismsCorrectiveAction__action_completion_date", curie=ISO27001.curie('action_completion_date'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsCorrectiveAction__action_resources = Slot(uri=ISO27001.action_resources, name="ismsCorrectiveAction__action_resources", curie=ISO27001.curie('action_resources'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_resources, domain=None, range=Optional[str])

slots.ismsCorrectiveAction__action_effectiveness_criteria = Slot(uri=ISO27001.action_effectiveness_criteria, name="ismsCorrectiveAction__action_effectiveness_criteria", curie=ISO27001.curie('action_effectiveness_criteria'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_effectiveness_criteria, domain=None, range=Optional[str])

slots.ismsCorrectiveAction__action_effectiveness_review_date = Slot(uri=ISO27001.action_effectiveness_review_date, name="ismsCorrectiveAction__action_effectiveness_review_date", curie=ISO27001.curie('action_effectiveness_review_date'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_effectiveness_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsCorrectiveAction__action_effective = Slot(uri=ISO27001.action_effective, name="ismsCorrectiveAction__action_effective", curie=ISO27001.curie('action_effective'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_effective, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsCorrectiveAction__action_isms_changes = Slot(uri=ISO27001.action_isms_changes, name="ismsCorrectiveAction__action_isms_changes", curie=ISO27001.curie('action_isms_changes'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_isms_changes, domain=None, range=Optional[str])

slots.ismsCorrectiveAction__action_status = Slot(uri=ISO27001.action_status, name="ismsCorrectiveAction__action_status", curie=ISO27001.curie('action_status'),
                   model_uri=ISO27001.ismsCorrectiveAction__action_status, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_source = Slot(uri=ISO27001.improvement_source, name="ismsImprovementOpportunity__improvement_source", curie=ISO27001.curie('improvement_source'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_source, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_identified_on = Slot(uri=ISO27001.improvement_identified_on, name="ismsImprovementOpportunity__improvement_identified_on", curie=ISO27001.curie('improvement_identified_on'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_identified_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsImprovementOpportunity__improvement_identified_by = Slot(uri=ISO27001.improvement_identified_by, name="ismsImprovementOpportunity__improvement_identified_by", curie=ISO27001.curie('improvement_identified_by'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_identified_by, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_benefit = Slot(uri=ISO27001.improvement_benefit, name="ismsImprovementOpportunity__improvement_benefit", curie=ISO27001.curie('improvement_benefit'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_benefit, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_priority = Slot(uri=ISO27001.improvement_priority, name="ismsImprovementOpportunity__improvement_priority", curie=ISO27001.curie('improvement_priority'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_priority, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_plan = Slot(uri=ISO27001.improvement_plan, name="ismsImprovementOpportunity__improvement_plan", curie=ISO27001.curie('improvement_plan'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_plan, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_target_date = Slot(uri=ISO27001.improvement_target_date, name="ismsImprovementOpportunity__improvement_target_date", curie=ISO27001.curie('improvement_target_date'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsImprovementOpportunity__improvement_completion_date = Slot(uri=ISO27001.improvement_completion_date, name="ismsImprovementOpportunity__improvement_completion_date", curie=ISO27001.curie('improvement_completion_date'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ismsImprovementOpportunity__improvement_outcome = Slot(uri=ISO27001.improvement_outcome, name="ismsImprovementOpportunity__improvement_outcome", curie=ISO27001.curie('improvement_outcome'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_outcome, domain=None, range=Optional[str])

slots.ismsImprovementOpportunity__improvement_status = Slot(uri=ISO27001.improvement_status, name="ismsImprovementOpportunity__improvement_status", curie=ISO27001.curie('improvement_status'),
                   model_uri=ISO27001.ismsImprovementOpportunity__improvement_status, domain=None, range=Optional[str])

slots.ismsSecurityEvent__event_type = Slot(uri=ISO27001.event_type, name="ismsSecurityEvent__event_type", curie=ISO27001.curie('event_type'),
                   model_uri=ISO27001.ismsSecurityEvent__event_type, domain=None, range=Optional[str])

slots.ismsSecurityEvent__event_occurred_at = Slot(uri=ISO27001.event_occurred_at, name="ismsSecurityEvent__event_occurred_at", curie=ISO27001.curie('event_occurred_at'),
                   model_uri=ISO27001.ismsSecurityEvent__event_occurred_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.ismsSecurityEvent__event_reporter = Slot(uri=ISO27001.event_reporter, name="ismsSecurityEvent__event_reporter", curie=ISO27001.curie('event_reporter'),
                   model_uri=ISO27001.ismsSecurityEvent__event_reporter, domain=None, range=Optional[str])

slots.ismsSecurityEvent__event_assessment = Slot(uri=ISO27001.event_assessment, name="ismsSecurityEvent__event_assessment", curie=ISO27001.curie('event_assessment'),
                   model_uri=ISO27001.ismsSecurityEvent__event_assessment, domain=None, range=Optional[str])

slots.ismsSecurityIncident__incident_category = Slot(uri=ISO27001.incident_category, name="ismsSecurityIncident__incident_category", curie=ISO27001.curie('incident_category'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_category, domain=None, range=Optional[Union[str, "IsmsIncidentCategory"]])

slots.ismsSecurityIncident__incident_severity = Slot(uri=ISO27001.incident_severity, name="ismsSecurityIncident__incident_severity", curie=ISO27001.curie('incident_severity'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_severity, domain=None, range=Optional[Union[str, "IsmsRiskLevel"]])

slots.ismsSecurityIncident__incident_detection_method = Slot(uri=ISO27001.incident_detection_method, name="ismsSecurityIncident__incident_detection_method", curie=ISO27001.curie('incident_detection_method'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_detection_method, domain=None, range=Optional[str])

slots.ismsSecurityIncident__incident_response_actions = Slot(uri=ISO27001.incident_response_actions, name="ismsSecurityIncident__incident_response_actions", curie=ISO27001.curie('incident_response_actions'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_response_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_containment_actions = Slot(uri=ISO27001.incident_containment_actions, name="ismsSecurityIncident__incident_containment_actions", curie=ISO27001.curie('incident_containment_actions'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_containment_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_eradication_actions = Slot(uri=ISO27001.incident_eradication_actions, name="ismsSecurityIncident__incident_eradication_actions", curie=ISO27001.curie('incident_eradication_actions'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_eradication_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_recovery_actions = Slot(uri=ISO27001.incident_recovery_actions, name="ismsSecurityIncident__incident_recovery_actions", curie=ISO27001.curie('incident_recovery_actions'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_recovery_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_root_cause = Slot(uri=ISO27001.incident_root_cause, name="ismsSecurityIncident__incident_root_cause", curie=ISO27001.curie('incident_root_cause'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_root_cause, domain=None, range=Optional[str])

slots.ismsSecurityIncident__incident_lessons_learned = Slot(uri=ISO27001.incident_lessons_learned, name="ismsSecurityIncident__incident_lessons_learned", curie=ISO27001.curie('incident_lessons_learned'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_lessons_learned, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_evidence = Slot(uri=ISO27001.incident_evidence, name="ismsSecurityIncident__incident_evidence", curie=ISO27001.curie('incident_evidence'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_notification_required = Slot(uri=ISO27001.incident_notification_required, name="ismsSecurityIncident__incident_notification_required", curie=ISO27001.curie('incident_notification_required'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.ismsSecurityIncident__incident_notifications = Slot(uri=ISO27001.incident_notifications, name="ismsSecurityIncident__incident_notifications", curie=ISO27001.curie('incident_notifications'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_notifications, domain=None, range=Optional[Union[str, list[str]]])

slots.ismsSecurityIncident__incident_closed_at = Slot(uri=ISO27001.incident_closed_at, name="ismsSecurityIncident__incident_closed_at", curie=ISO27001.curie('incident_closed_at'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_closed_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.ismsSecurityIncident__incident_review = Slot(uri=ISO27001.incident_review, name="ismsSecurityIncident__incident_review", curie=ISO27001.curie('incident_review'),
                   model_uri=ISO27001.ismsSecurityIncident__incident_review, domain=None, range=Optional[str])

slots.IsmsRecordMixin_title = Slot(uri=SCHEMA.name, name="IsmsRecordMixin_title", curie=SCHEMA.curie('name'),
                   model_uri=ISO27001.IsmsRecordMixin_title, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.IsmsIncludedControl_implementation_state = Slot(uri=ISO27001.implementation_state, name="IsmsIncludedControl_implementation_state", curie=ISO27001.curie('implementation_state'),
                   model_uri=ISO27001.IsmsIncludedControl_implementation_state, domain=IsmsIncludedControl, range=Union[str, "IsmsImplementationStatus"])

slots.IsmsExcludedControl_entry_annex_a_control = Slot(uri=ISO27001.entry_annex_a_control, name="IsmsExcludedControl_entry_annex_a_control", curie=ISO27001.curie('entry_annex_a_control'),
                   model_uri=ISO27001.IsmsExcludedControl_entry_annex_a_control, domain=IsmsExcludedControl, range=Union[str, "IsmsAnnexAControl"])
