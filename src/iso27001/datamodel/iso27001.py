# Auto generated from iso27001.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-15T23:08:27
# Schema: iso27001
#
# id: https://w3id.org/lmodel/iso27001
# description: A comprehensive LinkML schema modeling ISMS entities, workflows, and traceability links aligned to ISO/IEC 27001:2022 clause and Annex references. Designed for open data publication, automated validation, and integration with governance, risk, and compliance (GRC) systems.
#   This schema captures: - ISMS lifecycle (establish, implement, maintain, improve) - Risk assessment and treatment processes (Clause 6.1) - Annex A control catalog structures organized by domain - Audit, measurement, and continual improvement artifacts
# license: https://www.apache.org/licenses/LICENSE-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "1.0.0"

# Namespaces
CIS_CONTROLS = CurieNamespace('cis_controls', 'https://w3id.org/lmodel/cis-controls/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
ISO = CurieNamespace('iso', 'https://www.iso.org/standard/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO27002 = CurieNamespace('iso27002', 'https://w3id.org/lmodel/iso27002/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO27001


# Types
class PositiveIntegerType(int):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer type"
    type_model_uri = ISO27001.PositiveIntegerType


class UnsignedShortType(int):
    """ data type for non-negative integers that can be represented with 16 bits """
    type_class_uri = XSD["unsignedShort"]
    type_class_curie = "xsd:unsignedShort"
    type_name = "unsigned short type"
    type_model_uri = ISO27001.UnsignedShortType


class DurationType(str):
    """ ISO 8601 duration value such as P1Y, P30D, or PT4H """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration type"
    type_model_uri = ISO27001.DurationType


# Class references
class NamedEntityId(URIorCURIE):
    pass


class DocumentedInformationId(NamedEntityId):
    pass


class InformationSecurityManagementSystemId(NamedEntityId):
    pass


class OrganizationId(NamedEntityId):
    pass


class InterestedPartyId(NamedEntityId):
    pass


class InformationSecurityPolicyId(DocumentedInformationId):
    pass


class TopicSpecificPolicyId(DocumentedInformationId):
    pass


class RoleId(NamedEntityId):
    pass


class InformationSecurityObjectiveId(NamedEntityId):
    pass


class RiskAssessmentProcessId(DocumentedInformationId):
    pass


class RiskAssessmentId(DocumentedInformationId):
    pass


class RiskId(NamedEntityId):
    pass


class RiskTreatmentProcessId(DocumentedInformationId):
    pass


class RiskTreatmentPlanId(DocumentedInformationId):
    pass


class StatementOfApplicabilityId(DocumentedInformationId):
    pass


class SecurityControlId(NamedEntityId):
    pass


class ResourceId(NamedEntityId):
    pass


class CompetenceRecordId(DocumentedInformationId):
    pass


class AwarenessProgramId(DocumentedInformationId):
    pass


class CommunicationPlanId(DocumentedInformationId):
    pass


class OperationalProcedureId(DocumentedInformationId):
    pass


class MonitoringProgramId(DocumentedInformationId):
    pass


class InternalAuditId(DocumentedInformationId):
    pass


class AuditProgrammeId(DocumentedInformationId):
    pass


class AuditFindingId(NamedEntityId):
    pass


class ManagementReviewId(DocumentedInformationId):
    pass


class NonconformityId(NamedEntityId):
    pass


class CorrectiveActionId(NamedEntityId):
    pass


class ImprovementOpportunityId(NamedEntityId):
    pass


class AssetId(NamedEntityId):
    pass


class InformationSecurityEventId(NamedEntityId):
    pass


class InformationSecurityIncidentId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and
    documentation slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["NamedEntity"]
    class_class_curie: ClassVar[str] = "iso27001:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ISO27001.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: str = None
    description: Optional[str] = None
    created_date: Optional[Union[str, XSDDate]] = None
    modified_date: Optional[Union[str, XSDDate]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.created_date is not None and not isinstance(self.created_date, XSDDate):
            self.created_date = XSDDate(self.created_date)

        if self.modified_date is not None and not isinstance(self.modified_date, XSDDate):
            self.modified_date = XSDDate(self.modified_date)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["DocumentedInformation"]
    class_class_curie: ClassVar[str] = "iso27001:DocumentedInformation"
    class_name: ClassVar[str] = "DocumentedInformation"
    class_model_uri: ClassVar[URIRef] = ISO27001.DocumentedInformation

    id: Union[str, DocumentedInformationId] = None
    name: str = None
    document_type: Optional[Union[str, "DocumentType"]] = None
    document_reference: Optional[str] = None
    author: Optional[str] = None
    owner: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[Union[str, XSDDate]] = None
    effective_date: Optional[Union[str, XSDDate]] = None
    review_date: Optional[Union[str, XSDDate]] = None
    status: Optional[str] = None
    classification: Optional[str] = None
    retention_period: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.document_type is not None and not isinstance(self.document_type, DocumentType):
            self.document_type = DocumentType(self.document_type)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.owner is not None and not isinstance(self.owner, str):
            self.owner = str(self.owner)

        if self.approved_by is not None and not isinstance(self.approved_by, str):
            self.approved_by = str(self.approved_by)

        if self.approved_date is not None and not isinstance(self.approved_date, XSDDate):
            self.approved_date = XSDDate(self.approved_date)

        if self.effective_date is not None and not isinstance(self.effective_date, XSDDate):
            self.effective_date = XSDDate(self.effective_date)

        if self.review_date is not None and not isinstance(self.review_date, XSDDate):
            self.review_date = XSDDate(self.review_date)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if self.retention_period is not None and not isinstance(self.retention_period, str):
            self.retention_period = str(self.retention_period)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required
    to support the full ISMS lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InformationSecurityManagementSystem"]
    class_class_curie: ClassVar[str] = "iso27001:InformationSecurityManagementSystem"
    class_name: ClassVar[str] = "InformationSecurityManagementSystem"
    class_model_uri: ClassVar[URIRef] = ISO27001.InformationSecurityManagementSystem

    id: Union[str, InformationSecurityManagementSystemId] = None
    name: str = None
    organization: Optional[Union[str, OrganizationId]] = None
    scope_statement: Optional[str] = None
    scope_boundaries: Optional[Union[str, list[str]]] = empty_list()
    scope_exclusions: Optional[Union[str, list[str]]] = empty_list()
    context_internal_issues: Optional[Union[str, list[str]]] = empty_list()
    context_external_issues: Optional[Union[str, list[str]]] = empty_list()
    interested_parties: Optional[Union[Union[str, InterestedPartyId], list[Union[str, InterestedPartyId]]]] = empty_list()
    information_security_policy: Optional[Union[str, InformationSecurityPolicyId]] = None
    objectives: Optional[Union[Union[str, InformationSecurityObjectiveId], list[Union[str, InformationSecurityObjectiveId]]]] = empty_list()
    risk_assessment_process: Optional[Union[str, RiskAssessmentProcessId]] = None
    risk_treatment_process: Optional[Union[str, RiskTreatmentProcessId]] = None
    statement_of_applicability: Optional[Union[str, StatementOfApplicabilityId]] = None
    controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    roles: Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]] = empty_list()
    resources: Optional[Union[Union[str, ResourceId], list[Union[str, ResourceId]]]] = empty_list()
    competence_records: Optional[Union[Union[str, CompetenceRecordId], list[Union[str, CompetenceRecordId]]]] = empty_list()
    awareness_program: Optional[Union[str, AwarenessProgramId]] = None
    communication_plan: Optional[Union[str, CommunicationPlanId]] = None
    documented_information_register: Optional[Union[Union[str, DocumentedInformationId], list[Union[str, DocumentedInformationId]]]] = empty_list()
    operational_procedures: Optional[Union[Union[str, OperationalProcedureId], list[Union[str, OperationalProcedureId]]]] = empty_list()
    risk_assessments: Optional[Union[Union[str, RiskAssessmentId], list[Union[str, RiskAssessmentId]]]] = empty_list()
    risk_treatment_plans: Optional[Union[Union[str, RiskTreatmentPlanId], list[Union[str, RiskTreatmentPlanId]]]] = empty_list()
    monitoring_program: Optional[Union[str, MonitoringProgramId]] = None
    internal_audits: Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]] = empty_list()
    management_reviews: Optional[Union[Union[str, ManagementReviewId], list[Union[str, ManagementReviewId]]]] = empty_list()
    nonconformities: Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]] = empty_list()
    corrective_actions: Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]] = empty_list()
    improvements: Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]] = empty_list()
    certification_status: Optional[str] = None
    certification_body: Optional[str] = None
    certification_date: Optional[Union[str, XSDDate]] = None
    recertification_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityManagementSystemId):
            self.id = InformationSecurityManagementSystemId(self.id)

        if self.organization is not None and not isinstance(self.organization, OrganizationId):
            self.organization = OrganizationId(self.organization)

        if self.scope_statement is not None and not isinstance(self.scope_statement, str):
            self.scope_statement = str(self.scope_statement)

        if not isinstance(self.scope_boundaries, list):
            self.scope_boundaries = [self.scope_boundaries] if self.scope_boundaries is not None else []
        self.scope_boundaries = [v if isinstance(v, str) else str(v) for v in self.scope_boundaries]

        if not isinstance(self.scope_exclusions, list):
            self.scope_exclusions = [self.scope_exclusions] if self.scope_exclusions is not None else []
        self.scope_exclusions = [v if isinstance(v, str) else str(v) for v in self.scope_exclusions]

        if not isinstance(self.context_internal_issues, list):
            self.context_internal_issues = [self.context_internal_issues] if self.context_internal_issues is not None else []
        self.context_internal_issues = [v if isinstance(v, str) else str(v) for v in self.context_internal_issues]

        if not isinstance(self.context_external_issues, list):
            self.context_external_issues = [self.context_external_issues] if self.context_external_issues is not None else []
        self.context_external_issues = [v if isinstance(v, str) else str(v) for v in self.context_external_issues]

        if not isinstance(self.interested_parties, list):
            self.interested_parties = [self.interested_parties] if self.interested_parties is not None else []
        self.interested_parties = [v if isinstance(v, InterestedPartyId) else InterestedPartyId(v) for v in self.interested_parties]

        if self.information_security_policy is not None and not isinstance(self.information_security_policy, InformationSecurityPolicyId):
            self.information_security_policy = InformationSecurityPolicyId(self.information_security_policy)

        if not isinstance(self.objectives, list):
            self.objectives = [self.objectives] if self.objectives is not None else []
        self.objectives = [v if isinstance(v, InformationSecurityObjectiveId) else InformationSecurityObjectiveId(v) for v in self.objectives]

        if self.risk_assessment_process is not None and not isinstance(self.risk_assessment_process, RiskAssessmentProcessId):
            self.risk_assessment_process = RiskAssessmentProcessId(self.risk_assessment_process)

        if self.risk_treatment_process is not None and not isinstance(self.risk_treatment_process, RiskTreatmentProcessId):
            self.risk_treatment_process = RiskTreatmentProcessId(self.risk_treatment_process)

        if self.statement_of_applicability is not None and not isinstance(self.statement_of_applicability, StatementOfApplicabilityId):
            self.statement_of_applicability = StatementOfApplicabilityId(self.statement_of_applicability)

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.controls]

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, RoleId) else RoleId(v) for v in self.roles]

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, ResourceId) else ResourceId(v) for v in self.resources]

        if not isinstance(self.competence_records, list):
            self.competence_records = [self.competence_records] if self.competence_records is not None else []
        self.competence_records = [v if isinstance(v, CompetenceRecordId) else CompetenceRecordId(v) for v in self.competence_records]

        if self.awareness_program is not None and not isinstance(self.awareness_program, AwarenessProgramId):
            self.awareness_program = AwarenessProgramId(self.awareness_program)

        if self.communication_plan is not None and not isinstance(self.communication_plan, CommunicationPlanId):
            self.communication_plan = CommunicationPlanId(self.communication_plan)

        if not isinstance(self.documented_information_register, list):
            self.documented_information_register = [self.documented_information_register] if self.documented_information_register is not None else []
        self.documented_information_register = [v if isinstance(v, DocumentedInformationId) else DocumentedInformationId(v) for v in self.documented_information_register]

        if not isinstance(self.operational_procedures, list):
            self.operational_procedures = [self.operational_procedures] if self.operational_procedures is not None else []
        self.operational_procedures = [v if isinstance(v, OperationalProcedureId) else OperationalProcedureId(v) for v in self.operational_procedures]

        if not isinstance(self.risk_assessments, list):
            self.risk_assessments = [self.risk_assessments] if self.risk_assessments is not None else []
        self.risk_assessments = [v if isinstance(v, RiskAssessmentId) else RiskAssessmentId(v) for v in self.risk_assessments]

        if not isinstance(self.risk_treatment_plans, list):
            self.risk_treatment_plans = [self.risk_treatment_plans] if self.risk_treatment_plans is not None else []
        self.risk_treatment_plans = [v if isinstance(v, RiskTreatmentPlanId) else RiskTreatmentPlanId(v) for v in self.risk_treatment_plans]

        if self.monitoring_program is not None and not isinstance(self.monitoring_program, MonitoringProgramId):
            self.monitoring_program = MonitoringProgramId(self.monitoring_program)

        if not isinstance(self.internal_audits, list):
            self.internal_audits = [self.internal_audits] if self.internal_audits is not None else []
        self.internal_audits = [v if isinstance(v, InternalAuditId) else InternalAuditId(v) for v in self.internal_audits]

        if not isinstance(self.management_reviews, list):
            self.management_reviews = [self.management_reviews] if self.management_reviews is not None else []
        self.management_reviews = [v if isinstance(v, ManagementReviewId) else ManagementReviewId(v) for v in self.management_reviews]

        if not isinstance(self.nonconformities, list):
            self.nonconformities = [self.nonconformities] if self.nonconformities is not None else []
        self.nonconformities = [v if isinstance(v, NonconformityId) else NonconformityId(v) for v in self.nonconformities]

        if not isinstance(self.corrective_actions, list):
            self.corrective_actions = [self.corrective_actions] if self.corrective_actions is not None else []
        self.corrective_actions = [v if isinstance(v, CorrectiveActionId) else CorrectiveActionId(v) for v in self.corrective_actions]

        if not isinstance(self.improvements, list):
            self.improvements = [self.improvements] if self.improvements is not None else []
        self.improvements = [v if isinstance(v, ImprovementOpportunityId) else ImprovementOpportunityId(v) for v in self.improvements]

        if self.certification_status is not None and not isinstance(self.certification_status, str):
            self.certification_status = str(self.certification_status)

        if self.certification_body is not None and not isinstance(self.certification_body, str):
            self.certification_body = str(self.certification_body)

        if self.certification_date is not None and not isinstance(self.certification_date, XSDDate):
            self.certification_date = XSDDate(self.certification_date)

        if self.recertification_date is not None and not isinstance(self.recertification_date, XSDDate):
            self.recertification_date = XSDDate(self.recertification_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(NamedEntity):
    """
    The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the
    organization).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Organization"]
    class_class_curie: ClassVar[str] = "iso27001:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ISO27001.Organization

    id: Union[str, OrganizationId] = None
    name: str = None
    legal_name: Optional[str] = None
    trading_names: Optional[Union[str, list[str]]] = empty_list()
    organization_type: Optional[str] = None
    industry_sector: Optional[str] = None
    size_category: Optional[str] = None
    employee_count: Optional[int] = None
    geographic_locations: Optional[Union[str, list[str]]] = empty_list()
    regulatory_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    parent_organization: Optional[str] = None
    subsidiaries: Optional[Union[str, list[str]]] = empty_list()
    climate_change_relevant: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.legal_name is not None and not isinstance(self.legal_name, str):
            self.legal_name = str(self.legal_name)

        if not isinstance(self.trading_names, list):
            self.trading_names = [self.trading_names] if self.trading_names is not None else []
        self.trading_names = [v if isinstance(v, str) else str(v) for v in self.trading_names]

        if self.organization_type is not None and not isinstance(self.organization_type, str):
            self.organization_type = str(self.organization_type)

        if self.industry_sector is not None and not isinstance(self.industry_sector, str):
            self.industry_sector = str(self.industry_sector)

        if self.size_category is not None and not isinstance(self.size_category, str):
            self.size_category = str(self.size_category)

        if self.employee_count is not None and not isinstance(self.employee_count, int):
            self.employee_count = int(self.employee_count)

        if not isinstance(self.geographic_locations, list):
            self.geographic_locations = [self.geographic_locations] if self.geographic_locations is not None else []
        self.geographic_locations = [v if isinstance(v, str) else str(v) for v in self.geographic_locations]

        if not isinstance(self.regulatory_jurisdictions, list):
            self.regulatory_jurisdictions = [self.regulatory_jurisdictions] if self.regulatory_jurisdictions is not None else []
        self.regulatory_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.regulatory_jurisdictions]

        if self.parent_organization is not None and not isinstance(self.parent_organization, str):
            self.parent_organization = str(self.parent_organization)

        if not isinstance(self.subsidiaries, list):
            self.subsidiaries = [self.subsidiaries] if self.subsidiaries is not None else []
        self.subsidiaries = [v if isinstance(v, str) else str(v) for v in self.subsidiaries]

        if self.climate_change_relevant is not None and not isinstance(self.climate_change_relevant, Bool):
            self.climate_change_relevant = Bool(self.climate_change_relevant)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees,
    management) and external parties (customers, regulators, suppliers).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InterestedParty"]
    class_class_curie: ClassVar[str] = "iso27001:InterestedParty"
    class_name: ClassVar[str] = "InterestedParty"
    class_model_uri: ClassVar[URIRef] = ISO27001.InterestedParty

    id: Union[str, InterestedPartyId] = None
    name: str = None
    party_type: Optional[str] = None
    relationship: Optional[str] = None
    requirements: Optional[Union[str, list[str]]] = empty_list()
    communication_needs: Optional[str] = None
    contact_information: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InterestedPartyId):
            self.id = InterestedPartyId(self.id)

        if self.party_type is not None and not isinstance(self.party_type, str):
            self.party_type = str(self.party_type)

        if self.relationship is not None and not isinstance(self.relationship, str):
            self.relationship = str(self.relationship)

        if not isinstance(self.requirements, list):
            self.requirements = [self.requirements] if self.requirements is not None else []
        self.requirements = [v if isinstance(v, str) else str(v) for v in self.requirements]

        if self.communication_needs is not None and not isinstance(self.communication_needs, str):
            self.communication_needs = str(self.communication_needs)

        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityPolicy(DocumentedInformation):
    """
    The information security policy established by top management per Clause 5.2. Provides framework for setting
    objectives and demonstrates commitment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InformationSecurityPolicy"]
    class_class_curie: ClassVar[str] = "iso27001:InformationSecurityPolicy"
    class_name: ClassVar[str] = "InformationSecurityPolicy"
    class_model_uri: ClassVar[URIRef] = ISO27001.InformationSecurityPolicy

    id: Union[str, InformationSecurityPolicyId] = None
    name: str = None
    policy_statement: Optional[str] = None
    policy_objectives_framework: Optional[str] = None
    commitment_statements: Optional[Union[str, list[str]]] = empty_list()
    applicability_statement: Optional[str] = None
    communication_date: Optional[Union[str, XSDDate]] = None
    acknowledgment_required: Optional[Union[bool, Bool]] = None
    related_topic_policies: Optional[Union[Union[str, TopicSpecificPolicyId], list[Union[str, TopicSpecificPolicyId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityPolicyId):
            self.id = InformationSecurityPolicyId(self.id)

        if self.policy_statement is not None and not isinstance(self.policy_statement, str):
            self.policy_statement = str(self.policy_statement)

        if self.policy_objectives_framework is not None and not isinstance(self.policy_objectives_framework, str):
            self.policy_objectives_framework = str(self.policy_objectives_framework)

        if not isinstance(self.commitment_statements, list):
            self.commitment_statements = [self.commitment_statements] if self.commitment_statements is not None else []
        self.commitment_statements = [v if isinstance(v, str) else str(v) for v in self.commitment_statements]

        if self.applicability_statement is not None and not isinstance(self.applicability_statement, str):
            self.applicability_statement = str(self.applicability_statement)

        if self.communication_date is not None and not isinstance(self.communication_date, XSDDate):
            self.communication_date = XSDDate(self.communication_date)

        if self.acknowledgment_required is not None and not isinstance(self.acknowledgment_required, Bool):
            self.acknowledgment_required = Bool(self.acknowledgment_required)

        if not isinstance(self.related_topic_policies, list):
            self.related_topic_policies = [self.related_topic_policies] if self.related_topic_policies is not None else []
        self.related_topic_policies = [v if isinstance(v, TopicSpecificPolicyId) else TopicSpecificPolicyId(v) for v in self.related_topic_policies]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TopicSpecificPolicy(DocumentedInformation):
    """
    A policy addressing a specific information security topic, supporting the overarching information security policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["TopicSpecificPolicy"]
    class_class_curie: ClassVar[str] = "iso27001:TopicSpecificPolicy"
    class_name: ClassVar[str] = "TopicSpecificPolicy"
    class_model_uri: ClassVar[URIRef] = ISO27001.TopicSpecificPolicy

    id: Union[str, TopicSpecificPolicyId] = None
    name: str = None
    topic_area: Optional[str] = None
    parent_policy: Optional[Union[str, InformationSecurityPolicyId]] = None
    applicable_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    target_audience: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TopicSpecificPolicyId):
            self.id = TopicSpecificPolicyId(self.id)

        if self.topic_area is not None and not isinstance(self.topic_area, str):
            self.topic_area = str(self.topic_area)

        if self.parent_policy is not None and not isinstance(self.parent_policy, InformationSecurityPolicyId):
            self.parent_policy = InformationSecurityPolicyId(self.parent_policy)

        if not isinstance(self.applicable_controls, list):
            self.applicable_controls = [self.applicable_controls] if self.applicable_controls is not None else []
        self.applicable_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.applicable_controls]

        if self.target_audience is not None and not isinstance(self.target_audience, str):
            self.target_audience = str(self.target_audience)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(NamedEntity):
    """
    An information security role with defined responsibilities and authorities per Clause 5.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Role"]
    class_class_curie: ClassVar[str] = "iso27001:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = ISO27001.Role

    id: Union[str, RoleId] = None
    name: str = None
    role_type: Optional[str] = None
    responsibilities: Optional[Union[str, list[str]]] = empty_list()
    authorities: Optional[Union[str, list[str]]] = empty_list()
    accountability: Optional[str] = None
    assigned_to: Optional[Union[str, list[str]]] = empty_list()
    delegation_rules: Optional[str] = None
    reporting_line: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RoleId):
            self.id = RoleId(self.id)

        if self.role_type is not None and not isinstance(self.role_type, str):
            self.role_type = str(self.role_type)

        if not isinstance(self.responsibilities, list):
            self.responsibilities = [self.responsibilities] if self.responsibilities is not None else []
        self.responsibilities = [v if isinstance(v, str) else str(v) for v in self.responsibilities]

        if not isinstance(self.authorities, list):
            self.authorities = [self.authorities] if self.authorities is not None else []
        self.authorities = [v if isinstance(v, str) else str(v) for v in self.authorities]

        if self.accountability is not None and not isinstance(self.accountability, str):
            self.accountability = str(self.accountability)

        if not isinstance(self.assigned_to, list):
            self.assigned_to = [self.assigned_to] if self.assigned_to is not None else []
        self.assigned_to = [v if isinstance(v, str) else str(v) for v in self.assigned_to]

        if self.delegation_rules is not None and not isinstance(self.delegation_rules, str):
            self.delegation_rules = str(self.delegation_rules)

        if self.reporting_line is not None and not isinstance(self.reporting_line, str):
            self.reporting_line = str(self.reporting_line)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityObjective(NamedEntity):
    """
    A measurable information security objective per Clause 6.2, established at relevant functions and levels of the
    organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InformationSecurityObjective"]
    class_class_curie: ClassVar[str] = "iso27001:InformationSecurityObjective"
    class_name: ClassVar[str] = "InformationSecurityObjective"
    class_model_uri: ClassVar[URIRef] = ISO27001.InformationSecurityObjective

    id: Union[str, InformationSecurityObjectiveId] = None
    name: str = None
    objective_statement: Optional[str] = None
    target_value: Optional[str] = None
    current_value: Optional[str] = None
    metric_definition: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_frequency: Optional[str] = None
    responsible_role: Optional[Union[str, RoleId]] = None
    target_date: Optional[Union[str, XSDDate]] = None
    achievement_status: Optional[str] = None
    related_risks: Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]] = empty_list()
    related_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    action_plan: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityObjectiveId):
            self.id = InformationSecurityObjectiveId(self.id)

        if self.objective_statement is not None and not isinstance(self.objective_statement, str):
            self.objective_statement = str(self.objective_statement)

        if self.target_value is not None and not isinstance(self.target_value, str):
            self.target_value = str(self.target_value)

        if self.current_value is not None and not isinstance(self.current_value, str):
            self.current_value = str(self.current_value)

        if self.metric_definition is not None and not isinstance(self.metric_definition, str):
            self.metric_definition = str(self.metric_definition)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_frequency is not None and not isinstance(self.measurement_frequency, str):
            self.measurement_frequency = str(self.measurement_frequency)

        if self.responsible_role is not None and not isinstance(self.responsible_role, RoleId):
            self.responsible_role = RoleId(self.responsible_role)

        if self.target_date is not None and not isinstance(self.target_date, XSDDate):
            self.target_date = XSDDate(self.target_date)

        if self.achievement_status is not None and not isinstance(self.achievement_status, str):
            self.achievement_status = str(self.achievement_status)

        if not isinstance(self.related_risks, list):
            self.related_risks = [self.related_risks] if self.related_risks is not None else []
        self.related_risks = [v if isinstance(v, RiskId) else RiskId(v) for v in self.related_risks]

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.related_controls]

        if self.action_plan is not None and not isinstance(self.action_plan, str):
            self.action_plan = str(self.action_plan)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskAssessmentProcess(DocumentedInformation):
    """
    The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying,
    analyzing, and evaluating risks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["RiskAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso27001:RiskAssessmentProcess"
    class_name: ClassVar[str] = "RiskAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO27001.RiskAssessmentProcess

    id: Union[str, RiskAssessmentProcessId] = None
    name: str = None
    risk_acceptance_criteria: Optional[str] = None
    assessment_criteria: Optional[str] = None
    assessment_methodology: Optional[str] = None
    likelihood_scale: Optional[str] = None
    impact_scale: Optional[str] = None
    risk_matrix: Optional[str] = None
    assessment_frequency: Optional[str] = None
    trigger_events: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskAssessmentProcessId):
            self.id = RiskAssessmentProcessId(self.id)

        if self.risk_acceptance_criteria is not None and not isinstance(self.risk_acceptance_criteria, str):
            self.risk_acceptance_criteria = str(self.risk_acceptance_criteria)

        if self.assessment_criteria is not None and not isinstance(self.assessment_criteria, str):
            self.assessment_criteria = str(self.assessment_criteria)

        if self.assessment_methodology is not None and not isinstance(self.assessment_methodology, str):
            self.assessment_methodology = str(self.assessment_methodology)

        if self.likelihood_scale is not None and not isinstance(self.likelihood_scale, str):
            self.likelihood_scale = str(self.likelihood_scale)

        if self.impact_scale is not None and not isinstance(self.impact_scale, str):
            self.impact_scale = str(self.impact_scale)

        if self.risk_matrix is not None and not isinstance(self.risk_matrix, str):
            self.risk_matrix = str(self.risk_matrix)

        if self.assessment_frequency is not None and not isinstance(self.assessment_frequency, str):
            self.assessment_frequency = str(self.assessment_frequency)

        if not isinstance(self.trigger_events, list):
            self.trigger_events = [self.trigger_events] if self.trigger_events is not None else []
        self.trigger_events = [v if isinstance(v, str) else str(v) for v in self.trigger_events]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskAssessment(DocumentedInformation):
    """
    An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["RiskAssessment"]
    class_class_curie: ClassVar[str] = "iso27001:RiskAssessment"
    class_name: ClassVar[str] = "RiskAssessment"
    class_model_uri: ClassVar[URIRef] = ISO27001.RiskAssessment

    id: Union[str, RiskAssessmentId] = None
    name: str = None
    assessment_scope: Optional[str] = None
    assessment_date: Optional[Union[str, XSDDate]] = None
    assessor: Optional[str] = None
    methodology_used: Optional[str] = None
    risks_identified: Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]] = empty_list()
    summary_findings: Optional[str] = None
    recommendations: Optional[Union[str, list[str]]] = empty_list()
    next_assessment_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskAssessmentId):
            self.id = RiskAssessmentId(self.id)

        if self.assessment_scope is not None and not isinstance(self.assessment_scope, str):
            self.assessment_scope = str(self.assessment_scope)

        if self.assessment_date is not None and not isinstance(self.assessment_date, XSDDate):
            self.assessment_date = XSDDate(self.assessment_date)

        if self.assessor is not None and not isinstance(self.assessor, str):
            self.assessor = str(self.assessor)

        if self.methodology_used is not None and not isinstance(self.methodology_used, str):
            self.methodology_used = str(self.methodology_used)

        if not isinstance(self.risks_identified, list):
            self.risks_identified = [self.risks_identified] if self.risks_identified is not None else []
        self.risks_identified = [v if isinstance(v, RiskId) else RiskId(v) for v in self.risks_identified]

        if self.summary_findings is not None and not isinstance(self.summary_findings, str):
            self.summary_findings = str(self.summary_findings)

        if not isinstance(self.recommendations, list):
            self.recommendations = [self.recommendations] if self.recommendations is not None else []
        self.recommendations = [v if isinstance(v, str) else str(v) for v in self.recommendations]

        if self.next_assessment_date is not None and not isinstance(self.next_assessment_date, XSDDate):
            self.next_assessment_date = XSDDate(self.next_assessment_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Risk(NamedEntity):
    """
    An identified information security risk that may affect information security properties within the ISMS scope.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Risk"]
    class_class_curie: ClassVar[str] = "iso27001:Risk"
    class_name: ClassVar[str] = "Risk"
    class_model_uri: ClassVar[URIRef] = ISO27001.Risk

    id: Union[str, RiskId] = None
    name: str = None
    risk_source: Optional[str] = None
    threat_description: Optional[str] = None
    vulnerability_description: Optional[str] = None
    affected_assets: Optional[Union[Union[str, AssetId], list[Union[str, AssetId]]]] = empty_list()
    affected_cia_properties: Optional[Union[str, list[str]]] = empty_list()
    risk_owner: Optional[str] = None
    likelihood: Optional[Union[str, "LikelihoodRating"]] = None
    impact: Optional[Union[str, "ImpactRating"]] = None
    inherent_risk_level: Optional[Union[str, "RiskLevel"]] = None
    existing_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    residual_risk_level: Optional[Union[str, "RiskLevel"]] = None
    risk_treatment_option: Optional[Union[str, "RiskTreatmentOption"]] = None
    treatment_priority: Optional[str] = None
    related_treatment_plan: Optional[Union[str, RiskTreatmentPlanId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskId):
            self.id = RiskId(self.id)

        if self.risk_source is not None and not isinstance(self.risk_source, str):
            self.risk_source = str(self.risk_source)

        if self.threat_description is not None and not isinstance(self.threat_description, str):
            self.threat_description = str(self.threat_description)

        if self.vulnerability_description is not None and not isinstance(self.vulnerability_description, str):
            self.vulnerability_description = str(self.vulnerability_description)

        if not isinstance(self.affected_assets, list):
            self.affected_assets = [self.affected_assets] if self.affected_assets is not None else []
        self.affected_assets = [v if isinstance(v, AssetId) else AssetId(v) for v in self.affected_assets]

        if not isinstance(self.affected_cia_properties, list):
            self.affected_cia_properties = [self.affected_cia_properties] if self.affected_cia_properties is not None else []
        self.affected_cia_properties = [v if isinstance(v, str) else str(v) for v in self.affected_cia_properties]

        if self.risk_owner is not None and not isinstance(self.risk_owner, str):
            self.risk_owner = str(self.risk_owner)

        if self.likelihood is not None and not isinstance(self.likelihood, LikelihoodRating):
            self.likelihood = LikelihoodRating(self.likelihood)

        if self.impact is not None and not isinstance(self.impact, ImpactRating):
            self.impact = ImpactRating(self.impact)

        if self.inherent_risk_level is not None and not isinstance(self.inherent_risk_level, RiskLevel):
            self.inherent_risk_level = RiskLevel(self.inherent_risk_level)

        if not isinstance(self.existing_controls, list):
            self.existing_controls = [self.existing_controls] if self.existing_controls is not None else []
        self.existing_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.existing_controls]

        if self.residual_risk_level is not None and not isinstance(self.residual_risk_level, RiskLevel):
            self.residual_risk_level = RiskLevel(self.residual_risk_level)

        if self.risk_treatment_option is not None and not isinstance(self.risk_treatment_option, RiskTreatmentOption):
            self.risk_treatment_option = RiskTreatmentOption(self.risk_treatment_option)

        if self.treatment_priority is not None and not isinstance(self.treatment_priority, str):
            self.treatment_priority = str(self.treatment_priority)

        if self.related_treatment_plan is not None and not isinstance(self.related_treatment_plan, RiskTreatmentPlanId):
            self.related_treatment_plan = RiskTreatmentPlanId(self.related_treatment_plan)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskTreatmentProcess(DocumentedInformation):
    """
    The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls
    determined.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["RiskTreatmentProcess"]
    class_class_curie: ClassVar[str] = "iso27001:RiskTreatmentProcess"
    class_name: ClassVar[str] = "RiskTreatmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO27001.RiskTreatmentProcess

    id: Union[str, RiskTreatmentProcessId] = None
    name: str = None
    treatment_options_guidance: Optional[str] = None
    control_selection_criteria: Optional[str] = None
    soa_template: Optional[str] = None
    approval_workflow: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskTreatmentProcessId):
            self.id = RiskTreatmentProcessId(self.id)

        if self.treatment_options_guidance is not None and not isinstance(self.treatment_options_guidance, str):
            self.treatment_options_guidance = str(self.treatment_options_guidance)

        if self.control_selection_criteria is not None and not isinstance(self.control_selection_criteria, str):
            self.control_selection_criteria = str(self.control_selection_criteria)

        if self.soa_template is not None and not isinstance(self.soa_template, str):
            self.soa_template = str(self.soa_template)

        if self.approval_workflow is not None and not isinstance(self.approval_workflow, str):
            self.approval_workflow = str(self.approval_workflow)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskTreatmentPlan(DocumentedInformation):
    """
    A risk treatment plan documenting planned actions to address identified risks through selected controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["RiskTreatmentPlan"]
    class_class_curie: ClassVar[str] = "iso27001:RiskTreatmentPlan"
    class_name: ClassVar[str] = "RiskTreatmentPlan"
    class_model_uri: ClassVar[URIRef] = ISO27001.RiskTreatmentPlan

    id: Union[str, RiskTreatmentPlanId] = None
    name: str = None
    plan_scope: Optional[str] = None
    risks_addressed: Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]] = empty_list()
    treatment_actions: Optional[Union[str, list[str]]] = empty_list()
    controls_to_implement: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    resources_required: Optional[str] = None
    responsible_parties: Optional[Union[str, list[str]]] = empty_list()
    implementation_timeline: Optional[str] = None
    risk_owner_approval: Optional[str] = None
    approved_date: Optional[Union[str, XSDDate]] = None
    residual_risk_acceptance: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    completion_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskTreatmentPlanId):
            self.id = RiskTreatmentPlanId(self.id)

        if self.plan_scope is not None and not isinstance(self.plan_scope, str):
            self.plan_scope = str(self.plan_scope)

        if not isinstance(self.risks_addressed, list):
            self.risks_addressed = [self.risks_addressed] if self.risks_addressed is not None else []
        self.risks_addressed = [v if isinstance(v, RiskId) else RiskId(v) for v in self.risks_addressed]

        if not isinstance(self.treatment_actions, list):
            self.treatment_actions = [self.treatment_actions] if self.treatment_actions is not None else []
        self.treatment_actions = [v if isinstance(v, str) else str(v) for v in self.treatment_actions]

        if not isinstance(self.controls_to_implement, list):
            self.controls_to_implement = [self.controls_to_implement] if self.controls_to_implement is not None else []
        self.controls_to_implement = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.controls_to_implement]

        if self.resources_required is not None and not isinstance(self.resources_required, str):
            self.resources_required = str(self.resources_required)

        if not isinstance(self.responsible_parties, list):
            self.responsible_parties = [self.responsible_parties] if self.responsible_parties is not None else []
        self.responsible_parties = [v if isinstance(v, str) else str(v) for v in self.responsible_parties]

        if self.implementation_timeline is not None and not isinstance(self.implementation_timeline, str):
            self.implementation_timeline = str(self.implementation_timeline)

        if self.risk_owner_approval is not None and not isinstance(self.risk_owner_approval, str):
            self.risk_owner_approval = str(self.risk_owner_approval)

        if self.approved_date is not None and not isinstance(self.approved_date, XSDDate):
            self.approved_date = XSDDate(self.approved_date)

        if self.residual_risk_acceptance is not None and not isinstance(self.residual_risk_acceptance, str):
            self.residual_risk_acceptance = str(self.residual_risk_acceptance)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.completion_date is not None and not isinstance(self.completion_date, XSDDate):
            self.completion_date = XSDDate(self.completion_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation
    state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["StatementOfApplicability"]
    class_class_curie: ClassVar[str] = "iso27001:StatementOfApplicability"
    class_name: ClassVar[str] = "StatementOfApplicability"
    class_model_uri: ClassVar[URIRef] = ISO27001.StatementOfApplicability

    id: Union[str, StatementOfApplicabilityId] = None
    name: str = None
    soa_entries: Optional[Union[Union[dict, "SoAEntry"], list[Union[dict, "SoAEntry"]]]] = empty_list()
    total_controls: Optional[int] = None
    implemented_count: Optional[int] = None
    planned_count: Optional[int] = None
    not_applicable_count: Optional[int] = None
    last_review_date: Optional[Union[str, XSDDate]] = None
    approved_by: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatementOfApplicabilityId):
            self.id = StatementOfApplicabilityId(self.id)

        if not isinstance(self.soa_entries, list):
            self.soa_entries = [self.soa_entries] if self.soa_entries is not None else []
        self.soa_entries = [v if isinstance(v, SoAEntry) else SoAEntry(**as_dict(v)) for v in self.soa_entries]

        if self.total_controls is not None and not isinstance(self.total_controls, int):
            self.total_controls = int(self.total_controls)

        if self.implemented_count is not None and not isinstance(self.implemented_count, int):
            self.implemented_count = int(self.implemented_count)

        if self.planned_count is not None and not isinstance(self.planned_count, int):
            self.planned_count = int(self.planned_count)

        if self.not_applicable_count is not None and not isinstance(self.not_applicable_count, int):
            self.not_applicable_count = int(self.not_applicable_count)

        if self.last_review_date is not None and not isinstance(self.last_review_date, XSDDate):
            self.last_review_date = XSDDate(self.last_review_date)

        if self.approved_by is not None and not isinstance(self.approved_by, str):
            self.approved_by = str(self.approved_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoAEntry(YAMLRoot):
    """
    A single entry in the Statement of Applicability, documenting the applicability and implementation status of one
    control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["SoAEntry"]
    class_class_curie: ClassVar[str] = "iso27001:SoAEntry"
    class_name: ClassVar[str] = "SoAEntry"
    class_model_uri: ClassVar[URIRef] = ISO27001.SoAEntry

    control_reference: Optional[Union[str, SecurityControlId]] = None
    is_applicable: Optional[Union[bool, Bool]] = None
    inclusion_justification: Optional[str] = None
    exclusion_justification: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    implementation_evidence: Optional[str] = None
    responsible_role: Optional[Union[str, RoleId]] = None
    target_implementation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.control_reference is not None and not isinstance(self.control_reference, SecurityControlId):
            self.control_reference = SecurityControlId(self.control_reference)

        if self.is_applicable is not None and not isinstance(self.is_applicable, Bool):
            self.is_applicable = Bool(self.is_applicable)

        if self.inclusion_justification is not None and not isinstance(self.inclusion_justification, str):
            self.inclusion_justification = str(self.inclusion_justification)

        if self.exclusion_justification is not None and not isinstance(self.exclusion_justification, str):
            self.exclusion_justification = str(self.exclusion_justification)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.implementation_evidence is not None and not isinstance(self.implementation_evidence, str):
            self.implementation_evidence = str(self.implementation_evidence)

        if self.responsible_role is not None and not isinstance(self.responsible_role, RoleId):
            self.responsible_role = RoleId(self.responsible_role)

        if self.target_implementation_date is not None and not isinstance(self.target_implementation_date, XSDDate):
            self.target_implementation_date = XSDDate(self.target_implementation_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityControl(NamedEntity):
    """
    A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that
    modifies risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["SecurityControl"]
    class_class_curie: ClassVar[str] = "iso27001:SecurityControl"
    class_name: ClassVar[str] = "SecurityControl"
    class_model_uri: ClassVar[URIRef] = ISO27001.SecurityControl

    id: Union[str, SecurityControlId] = None
    name: str = None
    control_id: Optional[str] = None
    control_title: Optional[str] = None
    control_category: Optional[Union[str, "ControlCategory"]] = None
    control_text: Optional[str] = None
    implementation_guidance: Optional[str] = None
    related_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    applicable_threats: Optional[Union[str, list[str]]] = empty_list()
    applicable_assets: Optional[Union[str, list[str]]] = empty_list()
    control_owner: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    implementation_date: Optional[Union[str, XSDDate]] = None
    effectiveness_rating: Optional[str] = None
    last_test_date: Optional[Union[str, XSDDate]] = None
    evidence_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityControlId):
            self.id = SecurityControlId(self.id)

        if self.control_id is not None and not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if self.control_title is not None and not isinstance(self.control_title, str):
            self.control_title = str(self.control_title)

        if self.control_category is not None and not isinstance(self.control_category, ControlCategory):
            self.control_category = ControlCategory(self.control_category)

        if self.control_text is not None and not isinstance(self.control_text, str):
            self.control_text = str(self.control_text)

        if self.implementation_guidance is not None and not isinstance(self.implementation_guidance, str):
            self.implementation_guidance = str(self.implementation_guidance)

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.related_controls]

        if not isinstance(self.applicable_threats, list):
            self.applicable_threats = [self.applicable_threats] if self.applicable_threats is not None else []
        self.applicable_threats = [v if isinstance(v, str) else str(v) for v in self.applicable_threats]

        if not isinstance(self.applicable_assets, list):
            self.applicable_assets = [self.applicable_assets] if self.applicable_assets is not None else []
        self.applicable_assets = [v if isinstance(v, str) else str(v) for v in self.applicable_assets]

        if self.control_owner is not None and not isinstance(self.control_owner, str):
            self.control_owner = str(self.control_owner)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.implementation_date is not None and not isinstance(self.implementation_date, XSDDate):
            self.implementation_date = XSDDate(self.implementation_date)

        if self.effectiveness_rating is not None and not isinstance(self.effectiveness_rating, str):
            self.effectiveness_rating = str(self.effectiveness_rating)

        if self.last_test_date is not None and not isinstance(self.last_test_date, XSDDate):
            self.last_test_date = XSDDate(self.last_test_date)

        if not isinstance(self.evidence_references, list):
            self.evidence_references = [self.evidence_references] if self.evidence_references is not None else []
        self.evidence_references = [v if isinstance(v, str) else str(v) for v in self.evidence_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(NamedEntity):
    """
    A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Resource"]
    class_class_curie: ClassVar[str] = "iso27001:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ISO27001.Resource

    id: Union[str, ResourceId] = None
    name: str = None
    resource_type: Optional[str] = None
    quantity: Optional[str] = None
    allocation_date: Optional[Union[str, XSDDate]] = None
    allocated_to: Optional[str] = None
    cost: Optional[str] = None
    availability_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.resource_type is not None and not isinstance(self.resource_type, str):
            self.resource_type = str(self.resource_type)

        if self.quantity is not None and not isinstance(self.quantity, str):
            self.quantity = str(self.quantity)

        if self.allocation_date is not None and not isinstance(self.allocation_date, XSDDate):
            self.allocation_date = XSDDate(self.allocation_date)

        if self.allocated_to is not None and not isinstance(self.allocated_to, str):
            self.allocated_to = str(self.allocated_to)

        if self.cost is not None and not isinstance(self.cost, str):
            self.cost = str(self.cost)

        if self.availability_status is not None and not isinstance(self.availability_status, str):
            self.availability_status = str(self.availability_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["CompetenceRecord"]
    class_class_curie: ClassVar[str] = "iso27001:CompetenceRecord"
    class_name: ClassVar[str] = "CompetenceRecord"
    class_model_uri: ClassVar[URIRef] = ISO27001.CompetenceRecord

    id: Union[str, CompetenceRecordId] = None
    name: str = None
    person_name: Optional[str] = None
    person_role: Optional[str] = None
    required_competencies: Optional[Union[str, list[str]]] = empty_list()
    education_records: Optional[Union[str, list[str]]] = empty_list()
    training_records: Optional[Union[str, list[str]]] = empty_list()
    experience_records: Optional[Union[str, list[str]]] = empty_list()
    competency_assessment_date: Optional[Union[str, XSDDate]] = None
    competency_gaps: Optional[Union[str, list[str]]] = empty_list()
    development_actions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompetenceRecordId):
            self.id = CompetenceRecordId(self.id)

        if self.person_name is not None and not isinstance(self.person_name, str):
            self.person_name = str(self.person_name)

        if self.person_role is not None and not isinstance(self.person_role, str):
            self.person_role = str(self.person_role)

        if not isinstance(self.required_competencies, list):
            self.required_competencies = [self.required_competencies] if self.required_competencies is not None else []
        self.required_competencies = [v if isinstance(v, str) else str(v) for v in self.required_competencies]

        if not isinstance(self.education_records, list):
            self.education_records = [self.education_records] if self.education_records is not None else []
        self.education_records = [v if isinstance(v, str) else str(v) for v in self.education_records]

        if not isinstance(self.training_records, list):
            self.training_records = [self.training_records] if self.training_records is not None else []
        self.training_records = [v if isinstance(v, str) else str(v) for v in self.training_records]

        if not isinstance(self.experience_records, list):
            self.experience_records = [self.experience_records] if self.experience_records is not None else []
        self.experience_records = [v if isinstance(v, str) else str(v) for v in self.experience_records]

        if self.competency_assessment_date is not None and not isinstance(self.competency_assessment_date, XSDDate):
            self.competency_assessment_date = XSDDate(self.competency_assessment_date)

        if not isinstance(self.competency_gaps, list):
            self.competency_gaps = [self.competency_gaps] if self.competency_gaps is not None else []
        self.competency_gaps = [v if isinstance(v, str) else str(v) for v in self.competency_gaps]

        if not isinstance(self.development_actions, list):
            self.development_actions = [self.development_actions] if self.development_actions is not None else []
        self.development_actions = [v if isinstance(v, str) else str(v) for v in self.development_actions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["AwarenessProgram"]
    class_class_curie: ClassVar[str] = "iso27001:AwarenessProgram"
    class_name: ClassVar[str] = "AwarenessProgram"
    class_model_uri: ClassVar[URIRef] = ISO27001.AwarenessProgram

    id: Union[str, AwarenessProgramId] = None
    name: str = None
    awareness_topics: Optional[Union[str, list[str]]] = empty_list()
    delivery_methods: Optional[Union[str, list[str]]] = empty_list()
    target_audience: Optional[str] = None
    frequency: Optional[str] = None
    completion_tracking: Optional[str] = None
    effectiveness_measures: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AwarenessProgramId):
            self.id = AwarenessProgramId(self.id)

        if not isinstance(self.awareness_topics, list):
            self.awareness_topics = [self.awareness_topics] if self.awareness_topics is not None else []
        self.awareness_topics = [v if isinstance(v, str) else str(v) for v in self.awareness_topics]

        if not isinstance(self.delivery_methods, list):
            self.delivery_methods = [self.delivery_methods] if self.delivery_methods is not None else []
        self.delivery_methods = [v if isinstance(v, str) else str(v) for v in self.delivery_methods]

        if self.target_audience is not None and not isinstance(self.target_audience, str):
            self.target_audience = str(self.target_audience)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.completion_tracking is not None and not isinstance(self.completion_tracking, str):
            self.completion_tracking = str(self.completion_tracking)

        if self.effectiveness_measures is not None and not isinstance(self.effectiveness_measures, str):
            self.effectiveness_measures = str(self.effectiveness_measures)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the ISMS per Clause 7.4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["CommunicationPlan"]
    class_class_curie: ClassVar[str] = "iso27001:CommunicationPlan"
    class_name: ClassVar[str] = "CommunicationPlan"
    class_model_uri: ClassVar[URIRef] = ISO27001.CommunicationPlan

    id: Union[str, CommunicationPlanId] = None
    name: str = None
    communication_items: Optional[Union[Union[dict, "CommunicationItem"], list[Union[dict, "CommunicationItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommunicationPlanId):
            self.id = CommunicationPlanId(self.id)

        if not isinstance(self.communication_items, list):
            self.communication_items = [self.communication_items] if self.communication_items is not None else []
        self.communication_items = [v if isinstance(v, CommunicationItem) else CommunicationItem(**as_dict(v)) for v in self.communication_items]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationItem(YAMLRoot):
    """
    A single communication requirement within the communication plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["CommunicationItem"]
    class_class_curie: ClassVar[str] = "iso27001:CommunicationItem"
    class_name: ClassVar[str] = "CommunicationItem"
    class_model_uri: ClassVar[URIRef] = ISO27001.CommunicationItem

    subject: Optional[str] = None
    purpose: Optional[str] = None
    audience: Optional[str] = None
    frequency: Optional[str] = None
    method: Optional[str] = None
    responsible_party: Optional[str] = None
    records_required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.records_required is not None and not isinstance(self.records_required, Bool):
            self.records_required = Bool(self.records_required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control per Clause 8.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["OperationalProcedure"]
    class_class_curie: ClassVar[str] = "iso27001:OperationalProcedure"
    class_name: ClassVar[str] = "OperationalProcedure"
    class_model_uri: ClassVar[URIRef] = ISO27001.OperationalProcedure

    id: Union[str, OperationalProcedureId] = None
    name: str = None
    procedure_scope: Optional[str] = None
    process_criteria: Optional[str] = None
    control_measures: Optional[Union[str, list[str]]] = empty_list()
    responsible_roles: Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]] = empty_list()
    related_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()
    change_control_requirements: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalProcedureId):
            self.id = OperationalProcedureId(self.id)

        if self.procedure_scope is not None and not isinstance(self.procedure_scope, str):
            self.procedure_scope = str(self.procedure_scope)

        if self.process_criteria is not None and not isinstance(self.process_criteria, str):
            self.process_criteria = str(self.process_criteria)

        if not isinstance(self.control_measures, list):
            self.control_measures = [self.control_measures] if self.control_measures is not None else []
        self.control_measures = [v if isinstance(v, str) else str(v) for v in self.control_measures]

        if not isinstance(self.responsible_roles, list):
            self.responsible_roles = [self.responsible_roles] if self.responsible_roles is not None else []
        self.responsible_roles = [v if isinstance(v, RoleId) else RoleId(v) for v in self.responsible_roles]

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.related_controls]

        if self.change_control_requirements is not None and not isinstance(self.change_control_requirements, str):
            self.change_control_requirements = str(self.change_control_requirements)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["MonitoringProgram"]
    class_class_curie: ClassVar[str] = "iso27001:MonitoringProgram"
    class_name: ClassVar[str] = "MonitoringProgram"
    class_model_uri: ClassVar[URIRef] = ISO27001.MonitoringProgram

    id: Union[str, MonitoringProgramId] = None
    name: str = None
    monitoring_items: Optional[Union[Union[dict, "MonitoringItem"], list[Union[dict, "MonitoringItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonitoringProgramId):
            self.id = MonitoringProgramId(self.id)

        if not isinstance(self.monitoring_items, list):
            self.monitoring_items = [self.monitoring_items] if self.monitoring_items is not None else []
        self.monitoring_items = [v if isinstance(v, MonitoringItem) else MonitoringItem(**as_dict(v)) for v in self.monitoring_items]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonitoringItem(YAMLRoot):
    """
    A single item to be monitored and measured per 9.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["MonitoringItem"]
    class_class_curie: ClassVar[str] = "iso27001:MonitoringItem"
    class_name: ClassVar[str] = "MonitoringItem"
    class_model_uri: ClassVar[URIRef] = ISO27001.MonitoringItem

    metric_name: Optional[str] = None
    metric_description: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_frequency: Optional[str] = None
    responsible_party: Optional[str] = None
    analysis_frequency: Optional[str] = None
    analyst: Optional[str] = None
    target_threshold: Optional[str] = None
    alert_threshold: Optional[str] = None
    current_value: Optional[str] = None
    trend: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.metric_name is not None and not isinstance(self.metric_name, str):
            self.metric_name = str(self.metric_name)

        if self.metric_description is not None and not isinstance(self.metric_description, str):
            self.metric_description = str(self.metric_description)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_frequency is not None and not isinstance(self.measurement_frequency, str):
            self.measurement_frequency = str(self.measurement_frequency)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.analysis_frequency is not None and not isinstance(self.analysis_frequency, str):
            self.analysis_frequency = str(self.analysis_frequency)

        if self.analyst is not None and not isinstance(self.analyst, str):
            self.analyst = str(self.analyst)

        if self.target_threshold is not None and not isinstance(self.target_threshold, str):
            self.target_threshold = str(self.target_threshold)

        if self.alert_threshold is not None and not isinstance(self.alert_threshold, str):
            self.alert_threshold = str(self.alert_threshold)

        if self.current_value is not None and not isinstance(self.current_value, str):
            self.current_value = str(self.current_value)

        if self.trend is not None and not isinstance(self.trend, str):
            self.trend = str(self.trend)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InternalAudit"]
    class_class_curie: ClassVar[str] = "iso27001:InternalAudit"
    class_name: ClassVar[str] = "InternalAudit"
    class_model_uri: ClassVar[URIRef] = ISO27001.InternalAudit

    id: Union[str, InternalAuditId] = None
    name: str = None
    audit_reference: Optional[str] = None
    audit_type: Optional[str] = None
    audit_scope: Optional[str] = None
    audit_criteria: Optional[Union[str, list[str]]] = empty_list()
    audit_objectives: Optional[Union[str, list[str]]] = empty_list()
    audit_period_start: Optional[Union[str, XSDDate]] = None
    audit_period_end: Optional[Union[str, XSDDate]] = None
    lead_auditor: Optional[str] = None
    audit_team: Optional[Union[str, list[str]]] = empty_list()
    auditee_representatives: Optional[Union[str, list[str]]] = empty_list()
    audit_plan: Optional[str] = None
    findings: Optional[Union[Union[str, AuditFindingId], list[Union[str, AuditFindingId]]]] = empty_list()
    positive_observations: Optional[Union[str, list[str]]] = empty_list()
    audit_conclusion: Optional[str] = None
    report_date: Optional[Union[str, XSDDate]] = None
    report_distribution: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternalAuditId):
            self.id = InternalAuditId(self.id)

        if self.audit_reference is not None and not isinstance(self.audit_reference, str):
            self.audit_reference = str(self.audit_reference)

        if self.audit_type is not None and not isinstance(self.audit_type, str):
            self.audit_type = str(self.audit_type)

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

        if self.lead_auditor is not None and not isinstance(self.lead_auditor, str):
            self.lead_auditor = str(self.lead_auditor)

        if not isinstance(self.audit_team, list):
            self.audit_team = [self.audit_team] if self.audit_team is not None else []
        self.audit_team = [v if isinstance(v, str) else str(v) for v in self.audit_team]

        if not isinstance(self.auditee_representatives, list):
            self.auditee_representatives = [self.auditee_representatives] if self.auditee_representatives is not None else []
        self.auditee_representatives = [v if isinstance(v, str) else str(v) for v in self.auditee_representatives]

        if self.audit_plan is not None and not isinstance(self.audit_plan, str):
            self.audit_plan = str(self.audit_plan)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, AuditFindingId) else AuditFindingId(v) for v in self.findings]

        if not isinstance(self.positive_observations, list):
            self.positive_observations = [self.positive_observations] if self.positive_observations is not None else []
        self.positive_observations = [v if isinstance(v, str) else str(v) for v in self.positive_observations]

        if self.audit_conclusion is not None and not isinstance(self.audit_conclusion, str):
            self.audit_conclusion = str(self.audit_conclusion)

        if self.report_date is not None and not isinstance(self.report_date, XSDDate):
            self.report_date = XSDDate(self.report_date)

        if not isinstance(self.report_distribution, list):
            self.report_distribution = [self.report_distribution] if self.report_distribution is not None else []
        self.report_distribution = [v if isinstance(v, str) else str(v) for v in self.report_distribution]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per 9.2.2, planning audit activities over a defined period.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["AuditProgramme"]
    class_class_curie: ClassVar[str] = "iso27001:AuditProgramme"
    class_name: ClassVar[str] = "AuditProgramme"
    class_model_uri: ClassVar[URIRef] = ISO27001.AuditProgramme

    id: Union[str, AuditProgrammeId] = None
    name: str = None
    programme_period: Optional[str] = None
    planned_audits: Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]] = empty_list()
    audit_frequency_rationale: Optional[str] = None
    resource_requirements: Optional[str] = None
    auditor_qualifications: Optional[str] = None
    programme_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditProgrammeId):
            self.id = AuditProgrammeId(self.id)

        if self.programme_period is not None and not isinstance(self.programme_period, str):
            self.programme_period = str(self.programme_period)

        if not isinstance(self.planned_audits, list):
            self.planned_audits = [self.planned_audits] if self.planned_audits is not None else []
        self.planned_audits = [v if isinstance(v, InternalAuditId) else InternalAuditId(v) for v in self.planned_audits]

        if self.audit_frequency_rationale is not None and not isinstance(self.audit_frequency_rationale, str):
            self.audit_frequency_rationale = str(self.audit_frequency_rationale)

        if self.resource_requirements is not None and not isinstance(self.resource_requirements, str):
            self.resource_requirements = str(self.resource_requirements)

        if self.auditor_qualifications is not None and not isinstance(self.auditor_qualifications, str):
            self.auditor_qualifications = str(self.auditor_qualifications)

        if self.programme_status is not None and not isinstance(self.programme_status, str):
            self.programme_status = str(self.programme_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditFinding(NamedEntity):
    """
    A finding from an internal audit, including nonconformities, observations, and positive findings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["AuditFinding"]
    class_class_curie: ClassVar[str] = "iso27001:AuditFinding"
    class_name: ClassVar[str] = "AuditFinding"
    class_model_uri: ClassVar[URIRef] = ISO27001.AuditFinding

    id: Union[str, AuditFindingId] = None
    name: str = None
    finding_type: Optional[Union[str, "AuditFindingType"]] = None
    clause_reference: Optional[str] = None
    control_reference: Optional[Union[str, SecurityControlId]] = None
    finding_description: Optional[str] = None
    objective_evidence: Optional[str] = None
    root_cause_analysis: Optional[str] = None
    risk_implication: Optional[str] = None
    recommended_action: Optional[str] = None
    auditee_response: Optional[str] = None
    linked_corrective_action: Optional[Union[str, CorrectiveActionId]] = None
    closure_status: Optional[str] = None
    closure_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditFindingId):
            self.id = AuditFindingId(self.id)

        if self.finding_type is not None and not isinstance(self.finding_type, AuditFindingType):
            self.finding_type = AuditFindingType(self.finding_type)

        if self.clause_reference is not None and not isinstance(self.clause_reference, str):
            self.clause_reference = str(self.clause_reference)

        if self.control_reference is not None and not isinstance(self.control_reference, SecurityControlId):
            self.control_reference = SecurityControlId(self.control_reference)

        if self.finding_description is not None and not isinstance(self.finding_description, str):
            self.finding_description = str(self.finding_description)

        if self.objective_evidence is not None and not isinstance(self.objective_evidence, str):
            self.objective_evidence = str(self.objective_evidence)

        if self.root_cause_analysis is not None and not isinstance(self.root_cause_analysis, str):
            self.root_cause_analysis = str(self.root_cause_analysis)

        if self.risk_implication is not None and not isinstance(self.risk_implication, str):
            self.risk_implication = str(self.risk_implication)

        if self.recommended_action is not None and not isinstance(self.recommended_action, str):
            self.recommended_action = str(self.recommended_action)

        if self.auditee_response is not None and not isinstance(self.auditee_response, str):
            self.auditee_response = str(self.auditee_response)

        if self.linked_corrective_action is not None and not isinstance(self.linked_corrective_action, CorrectiveActionId):
            self.linked_corrective_action = CorrectiveActionId(self.linked_corrective_action)

        if self.closure_status is not None and not isinstance(self.closure_status, str):
            self.closure_status = str(self.closure_status)

        if self.closure_date is not None and not isinstance(self.closure_date, XSDDate):
            self.closure_date = XSDDate(self.closure_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness
    for purpose.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["ManagementReview"]
    class_class_curie: ClassVar[str] = "iso27001:ManagementReview"
    class_name: ClassVar[str] = "ManagementReview"
    class_model_uri: ClassVar[URIRef] = ISO27001.ManagementReview

    id: Union[str, ManagementReviewId] = None
    name: str = None
    review_date: Optional[Union[str, XSDDate]] = None
    attendees: Optional[Union[str, list[str]]] = empty_list()
    previous_actions_status: Optional[str] = None
    context_changes: Optional[str] = None
    interested_party_changes: Optional[str] = None
    performance_trends: Optional[str] = None
    audit_results_summary: Optional[str] = None
    risk_assessment_results: Optional[str] = None
    improvement_opportunities: Optional[Union[str, list[str]]] = empty_list()
    decisions: Optional[Union[str, list[str]]] = empty_list()
    action_items: Optional[Union[str, list[str]]] = empty_list()
    next_review_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManagementReviewId):
            self.id = ManagementReviewId(self.id)

        if self.review_date is not None and not isinstance(self.review_date, XSDDate):
            self.review_date = XSDDate(self.review_date)

        if not isinstance(self.attendees, list):
            self.attendees = [self.attendees] if self.attendees is not None else []
        self.attendees = [v if isinstance(v, str) else str(v) for v in self.attendees]

        if self.previous_actions_status is not None and not isinstance(self.previous_actions_status, str):
            self.previous_actions_status = str(self.previous_actions_status)

        if self.context_changes is not None and not isinstance(self.context_changes, str):
            self.context_changes = str(self.context_changes)

        if self.interested_party_changes is not None and not isinstance(self.interested_party_changes, str):
            self.interested_party_changes = str(self.interested_party_changes)

        if self.performance_trends is not None and not isinstance(self.performance_trends, str):
            self.performance_trends = str(self.performance_trends)

        if self.audit_results_summary is not None and not isinstance(self.audit_results_summary, str):
            self.audit_results_summary = str(self.audit_results_summary)

        if self.risk_assessment_results is not None and not isinstance(self.risk_assessment_results, str):
            self.risk_assessment_results = str(self.risk_assessment_results)

        if not isinstance(self.improvement_opportunities, list):
            self.improvement_opportunities = [self.improvement_opportunities] if self.improvement_opportunities is not None else []
        self.improvement_opportunities = [v if isinstance(v, str) else str(v) for v in self.improvement_opportunities]

        if not isinstance(self.decisions, list):
            self.decisions = [self.decisions] if self.decisions is not None else []
        self.decisions = [v if isinstance(v, str) else str(v) for v in self.decisions]

        if not isinstance(self.action_items, list):
            self.action_items = [self.action_items] if self.action_items is not None else []
        self.action_items = [v if isinstance(v, str) else str(v) for v in self.action_items]

        if self.next_review_date is not None and not isinstance(self.next_review_date, XSDDate):
            self.next_review_date = XSDDate(self.next_review_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Nonconformity"]
    class_class_curie: ClassVar[str] = "iso27001:Nonconformity"
    class_name: ClassVar[str] = "Nonconformity"
    class_model_uri: ClassVar[URIRef] = ISO27001.Nonconformity

    id: Union[str, NonconformityId] = None
    name: str = None
    nonconformity_source: Optional[str] = None
    detection_date: Optional[Union[str, XSDDate]] = None
    detected_by: Optional[str] = None
    requirement_violated: Optional[str] = None
    nonconformity_description: Optional[str] = None
    immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    consequences_addressed: Optional[str] = None
    root_cause: Optional[str] = None
    similar_nonconformities_check: Optional[str] = None
    linked_corrective_actions: Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]] = empty_list()
    status: Optional[str] = None
    closure_date: Optional[Union[str, XSDDate]] = None
    closure_evidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonconformityId):
            self.id = NonconformityId(self.id)

        if self.nonconformity_source is not None and not isinstance(self.nonconformity_source, str):
            self.nonconformity_source = str(self.nonconformity_source)

        if self.detection_date is not None and not isinstance(self.detection_date, XSDDate):
            self.detection_date = XSDDate(self.detection_date)

        if self.detected_by is not None and not isinstance(self.detected_by, str):
            self.detected_by = str(self.detected_by)

        if self.requirement_violated is not None and not isinstance(self.requirement_violated, str):
            self.requirement_violated = str(self.requirement_violated)

        if self.nonconformity_description is not None and not isinstance(self.nonconformity_description, str):
            self.nonconformity_description = str(self.nonconformity_description)

        if not isinstance(self.immediate_actions, list):
            self.immediate_actions = [self.immediate_actions] if self.immediate_actions is not None else []
        self.immediate_actions = [v if isinstance(v, str) else str(v) for v in self.immediate_actions]

        if self.consequences_addressed is not None and not isinstance(self.consequences_addressed, str):
            self.consequences_addressed = str(self.consequences_addressed)

        if self.root_cause is not None and not isinstance(self.root_cause, str):
            self.root_cause = str(self.root_cause)

        if self.similar_nonconformities_check is not None and not isinstance(self.similar_nonconformities_check, str):
            self.similar_nonconformities_check = str(self.similar_nonconformities_check)

        if not isinstance(self.linked_corrective_actions, list):
            self.linked_corrective_actions = [self.linked_corrective_actions] if self.linked_corrective_actions is not None else []
        self.linked_corrective_actions = [v if isinstance(v, CorrectiveActionId) else CorrectiveActionId(v) for v in self.linked_corrective_actions]

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.closure_date is not None and not isinstance(self.closure_date, XSDDate):
            self.closure_date = XSDDate(self.closure_date)

        if self.closure_evidence is not None and not isinstance(self.closure_evidence, str):
            self.closure_evidence = str(self.closure_evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of
    recurrence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["CorrectiveAction"]
    class_class_curie: ClassVar[str] = "iso27001:CorrectiveAction"
    class_name: ClassVar[str] = "CorrectiveAction"
    class_model_uri: ClassVar[URIRef] = ISO27001.CorrectiveAction

    id: Union[str, CorrectiveActionId] = None
    name: str = None
    linked_nonconformity: Optional[Union[str, NonconformityId]] = None
    action_description: Optional[str] = None
    root_cause_addressed: Optional[str] = None
    responsible_party: Optional[str] = None
    target_completion_date: Optional[Union[str, XSDDate]] = None
    actual_completion_date: Optional[Union[str, XSDDate]] = None
    resources_required: Optional[str] = None
    effectiveness_criteria: Optional[str] = None
    effectiveness_review_date: Optional[Union[str, XSDDate]] = None
    effectiveness_verified: Optional[Union[bool, Bool]] = None
    isms_changes_required: Optional[str] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrectiveActionId):
            self.id = CorrectiveActionId(self.id)

        if self.linked_nonconformity is not None and not isinstance(self.linked_nonconformity, NonconformityId):
            self.linked_nonconformity = NonconformityId(self.linked_nonconformity)

        if self.action_description is not None and not isinstance(self.action_description, str):
            self.action_description = str(self.action_description)

        if self.root_cause_addressed is not None and not isinstance(self.root_cause_addressed, str):
            self.root_cause_addressed = str(self.root_cause_addressed)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.target_completion_date is not None and not isinstance(self.target_completion_date, XSDDate):
            self.target_completion_date = XSDDate(self.target_completion_date)

        if self.actual_completion_date is not None and not isinstance(self.actual_completion_date, XSDDate):
            self.actual_completion_date = XSDDate(self.actual_completion_date)

        if self.resources_required is not None and not isinstance(self.resources_required, str):
            self.resources_required = str(self.resources_required)

        if self.effectiveness_criteria is not None and not isinstance(self.effectiveness_criteria, str):
            self.effectiveness_criteria = str(self.effectiveness_criteria)

        if self.effectiveness_review_date is not None and not isinstance(self.effectiveness_review_date, XSDDate):
            self.effectiveness_review_date = XSDDate(self.effectiveness_review_date)

        if self.effectiveness_verified is not None and not isinstance(self.effectiveness_verified, Bool):
            self.effectiveness_verified = Bool(self.effectiveness_verified)

        if self.isms_changes_required is not None and not isinstance(self.isms_changes_required, str):
            self.isms_changes_required = str(self.isms_changes_required)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["ImprovementOpportunity"]
    class_class_curie: ClassVar[str] = "iso27001:ImprovementOpportunity"
    class_name: ClassVar[str] = "ImprovementOpportunity"
    class_model_uri: ClassVar[URIRef] = ISO27001.ImprovementOpportunity

    id: Union[str, ImprovementOpportunityId] = None
    name: str = None
    improvement_source: Optional[str] = None
    identification_date: Optional[Union[str, XSDDate]] = None
    identified_by: Optional[str] = None
    improvement_description: Optional[str] = None
    expected_benefit: Optional[str] = None
    priority: Optional[str] = None
    implementation_plan: Optional[str] = None
    responsible_party: Optional[str] = None
    target_date: Optional[Union[str, XSDDate]] = None
    actual_completion_date: Optional[Union[str, XSDDate]] = None
    outcome_assessment: Optional[str] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImprovementOpportunityId):
            self.id = ImprovementOpportunityId(self.id)

        if self.improvement_source is not None and not isinstance(self.improvement_source, str):
            self.improvement_source = str(self.improvement_source)

        if self.identification_date is not None and not isinstance(self.identification_date, XSDDate):
            self.identification_date = XSDDate(self.identification_date)

        if self.identified_by is not None and not isinstance(self.identified_by, str):
            self.identified_by = str(self.identified_by)

        if self.improvement_description is not None and not isinstance(self.improvement_description, str):
            self.improvement_description = str(self.improvement_description)

        if self.expected_benefit is not None and not isinstance(self.expected_benefit, str):
            self.expected_benefit = str(self.expected_benefit)

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if self.implementation_plan is not None and not isinstance(self.implementation_plan, str):
            self.implementation_plan = str(self.implementation_plan)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.target_date is not None and not isinstance(self.target_date, XSDDate):
            self.target_date = XSDDate(self.target_date)

        if self.actual_completion_date is not None and not isinstance(self.actual_completion_date, XSDDate):
            self.actual_completion_date = XSDDate(self.actual_completion_date)

        if self.outcome_assessment is not None and not isinstance(self.outcome_assessment, str):
            self.outcome_assessment = str(self.outcome_assessment)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Asset(NamedEntity):
    """
    An information asset or associated asset requiring protection, per Annex A control 5.9.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["Asset"]
    class_class_curie: ClassVar[str] = "iso27001:Asset"
    class_name: ClassVar[str] = "Asset"
    class_model_uri: ClassVar[URIRef] = ISO27001.Asset

    id: Union[str, AssetId] = None
    name: str = None
    asset_type: Optional[str] = None
    asset_owner: Optional[str] = None
    asset_custodian: Optional[str] = None
    classification: Optional[str] = None
    location: Optional[str] = None
    criticality: Optional[str] = None
    related_risks: Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]] = empty_list()
    applicable_controls: Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssetId):
            self.id = AssetId(self.id)

        if self.asset_type is not None and not isinstance(self.asset_type, str):
            self.asset_type = str(self.asset_type)

        if self.asset_owner is not None and not isinstance(self.asset_owner, str):
            self.asset_owner = str(self.asset_owner)

        if self.asset_custodian is not None and not isinstance(self.asset_custodian, str):
            self.asset_custodian = str(self.asset_custodian)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.criticality is not None and not isinstance(self.criticality, str):
            self.criticality = str(self.criticality)

        if not isinstance(self.related_risks, list):
            self.related_risks = [self.related_risks] if self.related_risks is not None else []
        self.related_risks = [v if isinstance(v, RiskId) else RiskId(v) for v in self.related_risks]

        if not isinstance(self.applicable_controls, list):
            self.applicable_controls = [self.applicable_controls] if self.applicable_controls is not None else []
        self.applicable_controls = [v if isinstance(v, SecurityControlId) else SecurityControlId(v) for v in self.applicable_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityEvent(NamedEntity):
    """
    An information security event per A.5.25, which may or may not be categorized as an incident.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InformationSecurityEvent"]
    class_class_curie: ClassVar[str] = "iso27001:InformationSecurityEvent"
    class_name: ClassVar[str] = "InformationSecurityEvent"
    class_model_uri: ClassVar[URIRef] = ISO27001.InformationSecurityEvent

    id: Union[str, InformationSecurityEventId] = None
    name: str = None
    event_datetime: Optional[Union[str, XSDDateTime]] = None
    reporter: Optional[str] = None
    event_description: Optional[str] = None
    affected_assets: Optional[Union[Union[str, AssetId], list[Union[str, AssetId]]]] = empty_list()
    initial_assessment: Optional[str] = None
    categorized_as_incident: Optional[Union[bool, Bool]] = None
    linked_incident: Optional[Union[str, InformationSecurityIncidentId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityEventId):
            self.id = InformationSecurityEventId(self.id)

        if self.event_datetime is not None and not isinstance(self.event_datetime, XSDDateTime):
            self.event_datetime = XSDDateTime(self.event_datetime)

        if self.reporter is not None and not isinstance(self.reporter, str):
            self.reporter = str(self.reporter)

        if self.event_description is not None and not isinstance(self.event_description, str):
            self.event_description = str(self.event_description)

        if not isinstance(self.affected_assets, list):
            self.affected_assets = [self.affected_assets] if self.affected_assets is not None else []
        self.affected_assets = [v if isinstance(v, AssetId) else AssetId(v) for v in self.affected_assets]

        if self.initial_assessment is not None and not isinstance(self.initial_assessment, str):
            self.initial_assessment = str(self.initial_assessment)

        if self.categorized_as_incident is not None and not isinstance(self.categorized_as_incident, Bool):
            self.categorized_as_incident = Bool(self.categorized_as_incident)

        if self.linked_incident is not None and not isinstance(self.linked_incident, InformationSecurityIncidentId):
            self.linked_incident = InformationSecurityIncidentId(self.linked_incident)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityIncident(NamedEntity):
    """
    An information security incident per A.5.26, requiring response per documented procedures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO27001["InformationSecurityIncident"]
    class_class_curie: ClassVar[str] = "iso27001:InformationSecurityIncident"
    class_name: ClassVar[str] = "InformationSecurityIncident"
    class_model_uri: ClassVar[URIRef] = ISO27001.InformationSecurityIncident

    id: Union[str, InformationSecurityIncidentId] = None
    name: str = None
    incident_datetime: Optional[Union[str, XSDDateTime]] = None
    incident_category: Optional[str] = None
    severity: Optional[str] = None
    affected_assets: Optional[Union[Union[str, AssetId], list[Union[str, AssetId]]]] = empty_list()
    affected_cia: Optional[Union[str, list[str]]] = empty_list()
    incident_description: Optional[str] = None
    detection_method: Optional[str] = None
    response_actions: Optional[Union[str, list[str]]] = empty_list()
    containment_actions: Optional[Union[str, list[str]]] = empty_list()
    eradication_actions: Optional[Union[str, list[str]]] = empty_list()
    recovery_actions: Optional[Union[str, list[str]]] = empty_list()
    root_cause: Optional[str] = None
    lessons_learned: Optional[str] = None
    evidence_collected: Optional[Union[str, list[str]]] = empty_list()
    notification_required: Optional[Union[bool, Bool]] = None
    notifications_made: Optional[Union[str, list[str]]] = empty_list()
    closure_datetime: Optional[Union[str, XSDDateTime]] = None
    post_incident_review: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityIncidentId):
            self.id = InformationSecurityIncidentId(self.id)

        if self.incident_datetime is not None and not isinstance(self.incident_datetime, XSDDateTime):
            self.incident_datetime = XSDDateTime(self.incident_datetime)

        if self.incident_category is not None and not isinstance(self.incident_category, str):
            self.incident_category = str(self.incident_category)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if not isinstance(self.affected_assets, list):
            self.affected_assets = [self.affected_assets] if self.affected_assets is not None else []
        self.affected_assets = [v if isinstance(v, AssetId) else AssetId(v) for v in self.affected_assets]

        if not isinstance(self.affected_cia, list):
            self.affected_cia = [self.affected_cia] if self.affected_cia is not None else []
        self.affected_cia = [v if isinstance(v, str) else str(v) for v in self.affected_cia]

        if self.incident_description is not None and not isinstance(self.incident_description, str):
            self.incident_description = str(self.incident_description)

        if self.detection_method is not None and not isinstance(self.detection_method, str):
            self.detection_method = str(self.detection_method)

        if not isinstance(self.response_actions, list):
            self.response_actions = [self.response_actions] if self.response_actions is not None else []
        self.response_actions = [v if isinstance(v, str) else str(v) for v in self.response_actions]

        if not isinstance(self.containment_actions, list):
            self.containment_actions = [self.containment_actions] if self.containment_actions is not None else []
        self.containment_actions = [v if isinstance(v, str) else str(v) for v in self.containment_actions]

        if not isinstance(self.eradication_actions, list):
            self.eradication_actions = [self.eradication_actions] if self.eradication_actions is not None else []
        self.eradication_actions = [v if isinstance(v, str) else str(v) for v in self.eradication_actions]

        if not isinstance(self.recovery_actions, list):
            self.recovery_actions = [self.recovery_actions] if self.recovery_actions is not None else []
        self.recovery_actions = [v if isinstance(v, str) else str(v) for v in self.recovery_actions]

        if self.root_cause is not None and not isinstance(self.root_cause, str):
            self.root_cause = str(self.root_cause)

        if self.lessons_learned is not None and not isinstance(self.lessons_learned, str):
            self.lessons_learned = str(self.lessons_learned)

        if not isinstance(self.evidence_collected, list):
            self.evidence_collected = [self.evidence_collected] if self.evidence_collected is not None else []
        self.evidence_collected = [v if isinstance(v, str) else str(v) for v in self.evidence_collected]

        if self.notification_required is not None and not isinstance(self.notification_required, Bool):
            self.notification_required = Bool(self.notification_required)

        if not isinstance(self.notifications_made, list):
            self.notifications_made = [self.notifications_made] if self.notifications_made is not None else []
        self.notifications_made = [v if isinstance(v, str) else str(v) for v in self.notifications_made]

        if self.closure_datetime is not None and not isinstance(self.closure_datetime, XSDDateTime):
            self.closure_datetime = XSDDateTime(self.closure_datetime)

        if self.post_incident_review is not None and not isinstance(self.post_incident_review, str):
            self.post_incident_review = str(self.post_incident_review)

        super().__post_init__(**kwargs)


# Enumerations
class ControlCategory(EnumDefinitionImpl):
    """
    The four control domains defined in ISO/IEC 27001:2022 Annex A, corresponding to Clauses 5-8 of ISO/IEC 27002:2022.
    """
    organizational = PermissibleValue(
        text="organizational",
        description="""Organizational controls (Annex A.5) - policies, roles, asset management, access control, supplier relationships, incident management, compliance.""")
    people = PermissibleValue(
        text="people",
        description="""People controls (Annex A.6) - screening, employment terms, awareness, disciplinary process, termination responsibilities, remote working.""")
    physical = PermissibleValue(
        text="physical",
        description="""Physical controls (Annex A.7) - perimeters, entry controls, equipment protection, secure areas, media handling, cabling, maintenance.""")
    technological = PermissibleValue(
        text="technological",
        description="""Technological controls (Annex A.8) - endpoint security, access restrictions, authentication, malware protection, logging, cryptography, secure development.""")

    _defn = EnumDefinition(
        name="ControlCategory",
        description="""The four control domains defined in ISO/IEC 27001:2022 Annex A, corresponding to Clauses 5-8 of ISO/IEC 27002:2022.""",
    )

class ImplementationStatus(EnumDefinitionImpl):
    """
    Lifecycle status of a security control, used in Statement of Applicability and control tracking.
    """
    not_started = PermissibleValue(
        text="not_started",
        description="Control identified but no implementation activities begun.")
    planned = PermissibleValue(
        text="planned",
        description="Control scheduled for implementation with defined timeline.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="Implementation actively underway but not yet complete.")
    implemented = PermissibleValue(
        text="implemented",
        description="Control fully implemented and operational.")
    not_applicable = PermissibleValue(
        text="not_applicable",
        description="Control excluded from scope with documented justification per 6.1.3 d).")

    _defn = EnumDefinition(
        name="ImplementationStatus",
        description="Lifecycle status of a security control, used in Statement of Applicability and control tracking.",
    )

class RiskTreatmentOption(EnumDefinitionImpl):
    """
    Standard risk treatment options per ISO 31000 and ISO 27005.
    """
    modify = PermissibleValue(
        text="modify",
        description="Apply controls to change the risk level (reduce likelihood or impact).")
    accept = PermissibleValue(
        text="accept",
        description="Accept the risk without further treatment, within risk appetite. Requires risk owner approval.")
    avoid = PermissibleValue(
        text="avoid",
        description="Eliminate the risk by removing the activity or asset that creates it.")
    share = PermissibleValue(
        text="share",
        description="Transfer or share risk with external parties (e.g., insurance, outsourcing).")

    _defn = EnumDefinition(
        name="RiskTreatmentOption",
        description="Standard risk treatment options per ISO 31000 and ISO 27005.",
    )

class RiskLevel(EnumDefinitionImpl):
    """
    Qualitative risk rating derived from likelihood x impact analysis.
    """
    very_low = PermissibleValue(
        text="very_low",
        description="Negligible risk requiring no immediate action.")
    low = PermissibleValue(
        text="low",
        description="Minor risk manageable through routine procedures.")
    medium = PermissibleValue(
        text="medium",
        description="Moderate risk requiring management attention and planned controls.")
    high = PermissibleValue(
        text="high",
        description="Significant risk requiring priority treatment and escalation.")
    critical = PermissibleValue(
        text="critical",
        description="""Severe risk threatening organizational objectives; requires immediate executive action and resource allocation.""")

    _defn = EnumDefinition(
        name="RiskLevel",
        description="Qualitative risk rating derived from likelihood x impact analysis.",
    )

class DocumentType(EnumDefinitionImpl):
    """
    Categories of documented information required or recommended by ISO 27001.
    """
    policy = PermissibleValue(
        text="policy",
        description="High-level statement of intent and direction (e.g., IS policy per 5.2).")
    procedure = PermissibleValue(
        text="procedure",
        description="Documented steps for performing activities consistently.")
    standard = PermissibleValue(
        text="standard",
        description="Mandatory requirements for specific technologies or processes.")
    guideline = PermissibleValue(
        text="guideline",
        description="Recommended practices that support policies and procedures.")
    record = PermissibleValue(
        text="record",
        description="Evidence of activities performed or results achieved.")
    plan = PermissibleValue(
        text="plan",
        description="Documented approach for achieving objectives (e.g., risk treatment plan).")
    report = PermissibleValue(
        text="report",
        description="Formal output of assessment, audit, or review activities.")

    _defn = EnumDefinition(
        name="DocumentType",
        description="Categories of documented information required or recommended by ISO 27001.",
    )

class AuditFindingType(EnumDefinitionImpl):
    """
    Classification of internal audit findings.
    """
    major_nonconformity = PermissibleValue(
        text="major_nonconformity",
        description="""Significant failure to fulfill a requirement that affects ISMS capability to achieve intended outcomes.""")
    minor_nonconformity = PermissibleValue(
        text="minor_nonconformity",
        description="Isolated lapse that does not significantly affect ISMS effectiveness.")
    observation = PermissibleValue(
        text="observation",
        description="Noted condition that could lead to nonconformity if not addressed.")
    positive_finding = PermissibleValue(
        text="positive_finding",
        description="Evidence of effective implementation exceeding requirements.")

    _defn = EnumDefinition(
        name="AuditFindingType",
        description="Classification of internal audit findings.",
    )

class LikelihoodRating(EnumDefinitionImpl):
    """
    Qualitative likelihood scale for risk assessment.
    """
    rare = PermissibleValue(
        text="rare",
        description="Highly unlikely to occur (< 5% probability).")
    unlikely = PermissibleValue(
        text="unlikely",
        description="Not expected but possible (5-20% probability).")
    possible = PermissibleValue(
        text="possible",
        description="May occur at some point (20-50% probability).")
    likely = PermissibleValue(
        text="likely",
        description="Probably will occur (50-80% probability).")
    almost_certain = PermissibleValue(
        text="almost_certain",
        description="Expected to occur in most circumstances (> 80% probability).")

    _defn = EnumDefinition(
        name="LikelihoodRating",
        description="Qualitative likelihood scale for risk assessment.",
    )

class ImpactRating(EnumDefinitionImpl):
    """
    Qualitative impact scale for risk assessment.
    """
    negligible = PermissibleValue(
        text="negligible",
        description="No significant impact on operations or objectives.")
    minor = PermissibleValue(
        text="minor",
        description="Limited impact, easily absorbed by normal operations.")
    moderate = PermissibleValue(
        text="moderate",
        description="Noticeable impact requiring management intervention.")
    major = PermissibleValue(
        text="major",
        description="Serious impact on objectives, reputation, or compliance.")
    severe = PermissibleValue(
        text="severe",
        description="Catastrophic impact threatening organizational viability.")

    _defn = EnumDefinition(
        name="ImpactRating",
        description="Qualitative impact scale for risk assessment.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ISO27001.id, name="id", curie=ISO27001.curie('id'),
                   model_uri=ISO27001.id, domain=None, range=URIRef)

slots.name = Slot(uri=ISO27001.name, name="name", curie=ISO27001.curie('name'),
                   model_uri=ISO27001.name, domain=None, range=str)

slots.description = Slot(uri=ISO27001.description, name="description", curie=ISO27001.curie('description'),
                   model_uri=ISO27001.description, domain=None, range=Optional[str])

slots.version = Slot(uri=ISO27001.version, name="version", curie=ISO27001.curie('version'),
                   model_uri=ISO27001.version, domain=None, range=Optional[str])

slots.created_date = Slot(uri=ISO27001.created_date, name="created_date", curie=ISO27001.curie('created_date'),
                   model_uri=ISO27001.created_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modified_date = Slot(uri=ISO27001.modified_date, name="modified_date", curie=ISO27001.curie('modified_date'),
                   model_uri=ISO27001.modified_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.document_type = Slot(uri=ISO27001.document_type, name="document_type", curie=ISO27001.curie('document_type'),
                   model_uri=ISO27001.document_type, domain=None, range=Optional[Union[str, "DocumentType"]])

slots.document_reference = Slot(uri=ISO27001.document_reference, name="document_reference", curie=ISO27001.curie('document_reference'),
                   model_uri=ISO27001.document_reference, domain=None, range=Optional[str])

slots.author = Slot(uri=ISO27001.author, name="author", curie=ISO27001.curie('author'),
                   model_uri=ISO27001.author, domain=None, range=Optional[str])

slots.owner = Slot(uri=ISO27001.owner, name="owner", curie=ISO27001.curie('owner'),
                   model_uri=ISO27001.owner, domain=None, range=Optional[str])

slots.approved_by = Slot(uri=ISO27001.approved_by, name="approved_by", curie=ISO27001.curie('approved_by'),
                   model_uri=ISO27001.approved_by, domain=None, range=Optional[str])

slots.approved_date = Slot(uri=ISO27001.approved_date, name="approved_date", curie=ISO27001.curie('approved_date'),
                   model_uri=ISO27001.approved_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effective_date = Slot(uri=ISO27001.effective_date, name="effective_date", curie=ISO27001.curie('effective_date'),
                   model_uri=ISO27001.effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.review_date = Slot(uri=ISO27001.review_date, name="review_date", curie=ISO27001.curie('review_date'),
                   model_uri=ISO27001.review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.status = Slot(uri=ISO27001.status, name="status", curie=ISO27001.curie('status'),
                   model_uri=ISO27001.status, domain=None, range=Optional[str])

slots.classification = Slot(uri=ISO27001.classification, name="classification", curie=ISO27001.curie('classification'),
                   model_uri=ISO27001.classification, domain=None, range=Optional[str])

slots.retention_period = Slot(uri=ISO27001.retention_period, name="retention_period", curie=ISO27001.curie('retention_period'),
                   model_uri=ISO27001.retention_period, domain=None, range=Optional[str])

slots.organization = Slot(uri=ISO27001.organization, name="organization", curie=ISO27001.curie('organization'),
                   model_uri=ISO27001.organization, domain=None, range=Optional[Union[str, OrganizationId]])

slots.legal_name = Slot(uri=ISO27001.legal_name, name="legal_name", curie=ISO27001.curie('legal_name'),
                   model_uri=ISO27001.legal_name, domain=None, range=Optional[str])

slots.trading_names = Slot(uri=ISO27001.trading_names, name="trading_names", curie=ISO27001.curie('trading_names'),
                   model_uri=ISO27001.trading_names, domain=None, range=Optional[Union[str, list[str]]])

slots.organization_type = Slot(uri=ISO27001.organization_type, name="organization_type", curie=ISO27001.curie('organization_type'),
                   model_uri=ISO27001.organization_type, domain=None, range=Optional[str])

slots.industry_sector = Slot(uri=ISO27001.industry_sector, name="industry_sector", curie=ISO27001.curie('industry_sector'),
                   model_uri=ISO27001.industry_sector, domain=None, range=Optional[str])

slots.size_category = Slot(uri=ISO27001.size_category, name="size_category", curie=ISO27001.curie('size_category'),
                   model_uri=ISO27001.size_category, domain=None, range=Optional[str])

slots.employee_count = Slot(uri=ISO27001.employee_count, name="employee_count", curie=ISO27001.curie('employee_count'),
                   model_uri=ISO27001.employee_count, domain=None, range=Optional[int])

slots.geographic_locations = Slot(uri=ISO27001.geographic_locations, name="geographic_locations", curie=ISO27001.curie('geographic_locations'),
                   model_uri=ISO27001.geographic_locations, domain=None, range=Optional[Union[str, list[str]]])

slots.regulatory_jurisdictions = Slot(uri=ISO27001.regulatory_jurisdictions, name="regulatory_jurisdictions", curie=ISO27001.curie('regulatory_jurisdictions'),
                   model_uri=ISO27001.regulatory_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.parent_organization = Slot(uri=ISO27001.parent_organization, name="parent_organization", curie=ISO27001.curie('parent_organization'),
                   model_uri=ISO27001.parent_organization, domain=None, range=Optional[str])

slots.subsidiaries = Slot(uri=ISO27001.subsidiaries, name="subsidiaries", curie=ISO27001.curie('subsidiaries'),
                   model_uri=ISO27001.subsidiaries, domain=None, range=Optional[Union[str, list[str]]])

slots.scope_statement = Slot(uri=ISO27001.scope_statement, name="scope_statement", curie=ISO27001.curie('scope_statement'),
                   model_uri=ISO27001.scope_statement, domain=None, range=Optional[str])

slots.scope_boundaries = Slot(uri=ISO27001.scope_boundaries, name="scope_boundaries", curie=ISO27001.curie('scope_boundaries'),
                   model_uri=ISO27001.scope_boundaries, domain=None, range=Optional[Union[str, list[str]]])

slots.scope_exclusions = Slot(uri=ISO27001.scope_exclusions, name="scope_exclusions", curie=ISO27001.curie('scope_exclusions'),
                   model_uri=ISO27001.scope_exclusions, domain=None, range=Optional[Union[str, list[str]]])

slots.context_internal_issues = Slot(uri=ISO27001.context_internal_issues, name="context_internal_issues", curie=ISO27001.curie('context_internal_issues'),
                   model_uri=ISO27001.context_internal_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.context_external_issues = Slot(uri=ISO27001.context_external_issues, name="context_external_issues", curie=ISO27001.curie('context_external_issues'),
                   model_uri=ISO27001.context_external_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.climate_change_relevant = Slot(uri=ISO27001.climate_change_relevant, name="climate_change_relevant", curie=ISO27001.curie('climate_change_relevant'),
                   model_uri=ISO27001.climate_change_relevant, domain=None, range=Optional[Union[bool, Bool]])

slots.interested_parties = Slot(uri=ISO27001.interested_parties, name="interested_parties", curie=ISO27001.curie('interested_parties'),
                   model_uri=ISO27001.interested_parties, domain=None, range=Optional[Union[Union[str, InterestedPartyId], list[Union[str, InterestedPartyId]]]])

slots.party_type = Slot(uri=ISO27001.party_type, name="party_type", curie=ISO27001.curie('party_type'),
                   model_uri=ISO27001.party_type, domain=None, range=Optional[str])

slots.relationship = Slot(uri=ISO27001.relationship, name="relationship", curie=ISO27001.curie('relationship'),
                   model_uri=ISO27001.relationship, domain=None, range=Optional[str])

slots.requirements = Slot(uri=ISO27001.requirements, name="requirements", curie=ISO27001.curie('requirements'),
                   model_uri=ISO27001.requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.communication_needs = Slot(uri=ISO27001.communication_needs, name="communication_needs", curie=ISO27001.curie('communication_needs'),
                   model_uri=ISO27001.communication_needs, domain=None, range=Optional[str])

slots.contact_information = Slot(uri=ISO27001.contact_information, name="contact_information", curie=ISO27001.curie('contact_information'),
                   model_uri=ISO27001.contact_information, domain=None, range=Optional[str])

slots.information_security_policy = Slot(uri=ISO27001.information_security_policy, name="information_security_policy", curie=ISO27001.curie('information_security_policy'),
                   model_uri=ISO27001.information_security_policy, domain=None, range=Optional[Union[str, InformationSecurityPolicyId]])

slots.policy_statement = Slot(uri=ISO27001.policy_statement, name="policy_statement", curie=ISO27001.curie('policy_statement'),
                   model_uri=ISO27001.policy_statement, domain=None, range=Optional[str])

slots.policy_objectives_framework = Slot(uri=ISO27001.policy_objectives_framework, name="policy_objectives_framework", curie=ISO27001.curie('policy_objectives_framework'),
                   model_uri=ISO27001.policy_objectives_framework, domain=None, range=Optional[str])

slots.commitment_statements = Slot(uri=ISO27001.commitment_statements, name="commitment_statements", curie=ISO27001.curie('commitment_statements'),
                   model_uri=ISO27001.commitment_statements, domain=None, range=Optional[Union[str, list[str]]])

slots.applicability_statement = Slot(uri=ISO27001.applicability_statement, name="applicability_statement", curie=ISO27001.curie('applicability_statement'),
                   model_uri=ISO27001.applicability_statement, domain=None, range=Optional[str])

slots.communication_date = Slot(uri=ISO27001.communication_date, name="communication_date", curie=ISO27001.curie('communication_date'),
                   model_uri=ISO27001.communication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.acknowledgment_required = Slot(uri=ISO27001.acknowledgment_required, name="acknowledgment_required", curie=ISO27001.curie('acknowledgment_required'),
                   model_uri=ISO27001.acknowledgment_required, domain=None, range=Optional[Union[bool, Bool]])

slots.related_topic_policies = Slot(uri=ISO27001.related_topic_policies, name="related_topic_policies", curie=ISO27001.curie('related_topic_policies'),
                   model_uri=ISO27001.related_topic_policies, domain=None, range=Optional[Union[Union[str, TopicSpecificPolicyId], list[Union[str, TopicSpecificPolicyId]]]])

slots.topic_area = Slot(uri=ISO27001.topic_area, name="topic_area", curie=ISO27001.curie('topic_area'),
                   model_uri=ISO27001.topic_area, domain=None, range=Optional[str])

slots.parent_policy = Slot(uri=ISO27001.parent_policy, name="parent_policy", curie=ISO27001.curie('parent_policy'),
                   model_uri=ISO27001.parent_policy, domain=None, range=Optional[Union[str, InformationSecurityPolicyId]])

slots.applicable_controls = Slot(uri=ISO27001.applicable_controls, name="applicable_controls", curie=ISO27001.curie('applicable_controls'),
                   model_uri=ISO27001.applicable_controls, domain=None, range=Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]])

slots.target_audience = Slot(uri=ISO27001.target_audience, name="target_audience", curie=ISO27001.curie('target_audience'),
                   model_uri=ISO27001.target_audience, domain=None, range=Optional[str])

slots.roles = Slot(uri=ISO27001.roles, name="roles", curie=ISO27001.curie('roles'),
                   model_uri=ISO27001.roles, domain=None, range=Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]])

slots.role_type = Slot(uri=ISO27001.role_type, name="role_type", curie=ISO27001.curie('role_type'),
                   model_uri=ISO27001.role_type, domain=None, range=Optional[str])

slots.responsibilities = Slot(uri=ISO27001.responsibilities, name="responsibilities", curie=ISO27001.curie('responsibilities'),
                   model_uri=ISO27001.responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.authorities = Slot(uri=ISO27001.authorities, name="authorities", curie=ISO27001.curie('authorities'),
                   model_uri=ISO27001.authorities, domain=None, range=Optional[Union[str, list[str]]])

slots.accountability = Slot(uri=ISO27001.accountability, name="accountability", curie=ISO27001.curie('accountability'),
                   model_uri=ISO27001.accountability, domain=None, range=Optional[str])

slots.assigned_to = Slot(uri=ISO27001.assigned_to, name="assigned_to", curie=ISO27001.curie('assigned_to'),
                   model_uri=ISO27001.assigned_to, domain=None, range=Optional[Union[str, list[str]]])

slots.delegation_rules = Slot(uri=ISO27001.delegation_rules, name="delegation_rules", curie=ISO27001.curie('delegation_rules'),
                   model_uri=ISO27001.delegation_rules, domain=None, range=Optional[str])

slots.reporting_line = Slot(uri=ISO27001.reporting_line, name="reporting_line", curie=ISO27001.curie('reporting_line'),
                   model_uri=ISO27001.reporting_line, domain=None, range=Optional[str])

slots.objectives = Slot(uri=ISO27001.objectives, name="objectives", curie=ISO27001.curie('objectives'),
                   model_uri=ISO27001.objectives, domain=None, range=Optional[Union[Union[str, InformationSecurityObjectiveId], list[Union[str, InformationSecurityObjectiveId]]]])

slots.objective_statement = Slot(uri=ISO27001.objective_statement, name="objective_statement", curie=ISO27001.curie('objective_statement'),
                   model_uri=ISO27001.objective_statement, domain=None, range=Optional[str])

slots.target_value = Slot(uri=ISO27001.target_value, name="target_value", curie=ISO27001.curie('target_value'),
                   model_uri=ISO27001.target_value, domain=None, range=Optional[str])

slots.current_value = Slot(uri=ISO27001.current_value, name="current_value", curie=ISO27001.curie('current_value'),
                   model_uri=ISO27001.current_value, domain=None, range=Optional[str])

slots.metric_definition = Slot(uri=ISO27001.metric_definition, name="metric_definition", curie=ISO27001.curie('metric_definition'),
                   model_uri=ISO27001.metric_definition, domain=None, range=Optional[str])

slots.measurement_method = Slot(uri=ISO27001.measurement_method, name="measurement_method", curie=ISO27001.curie('measurement_method'),
                   model_uri=ISO27001.measurement_method, domain=None, range=Optional[str])

slots.measurement_frequency = Slot(uri=ISO27001.measurement_frequency, name="measurement_frequency", curie=ISO27001.curie('measurement_frequency'),
                   model_uri=ISO27001.measurement_frequency, domain=None, range=Optional[str])

slots.responsible_role = Slot(uri=ISO27001.responsible_role, name="responsible_role", curie=ISO27001.curie('responsible_role'),
                   model_uri=ISO27001.responsible_role, domain=None, range=Optional[Union[str, RoleId]])

slots.target_date = Slot(uri=ISO27001.target_date, name="target_date", curie=ISO27001.curie('target_date'),
                   model_uri=ISO27001.target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.achievement_status = Slot(uri=ISO27001.achievement_status, name="achievement_status", curie=ISO27001.curie('achievement_status'),
                   model_uri=ISO27001.achievement_status, domain=None, range=Optional[str])

slots.action_plan = Slot(uri=ISO27001.action_plan, name="action_plan", curie=ISO27001.curie('action_plan'),
                   model_uri=ISO27001.action_plan, domain=None, range=Optional[str])

slots.risk_assessment_process = Slot(uri=ISO27001.risk_assessment_process, name="risk_assessment_process", curie=ISO27001.curie('risk_assessment_process'),
                   model_uri=ISO27001.risk_assessment_process, domain=None, range=Optional[Union[str, RiskAssessmentProcessId]])

slots.risk_acceptance_criteria = Slot(uri=ISO27001.risk_acceptance_criteria, name="risk_acceptance_criteria", curie=ISO27001.curie('risk_acceptance_criteria'),
                   model_uri=ISO27001.risk_acceptance_criteria, domain=None, range=Optional[str])

slots.assessment_criteria = Slot(uri=ISO27001.assessment_criteria, name="assessment_criteria", curie=ISO27001.curie('assessment_criteria'),
                   model_uri=ISO27001.assessment_criteria, domain=None, range=Optional[str])

slots.assessment_methodology = Slot(uri=ISO27001.assessment_methodology, name="assessment_methodology", curie=ISO27001.curie('assessment_methodology'),
                   model_uri=ISO27001.assessment_methodology, domain=None, range=Optional[str])

slots.likelihood_scale = Slot(uri=ISO27001.likelihood_scale, name="likelihood_scale", curie=ISO27001.curie('likelihood_scale'),
                   model_uri=ISO27001.likelihood_scale, domain=None, range=Optional[str])

slots.impact_scale = Slot(uri=ISO27001.impact_scale, name="impact_scale", curie=ISO27001.curie('impact_scale'),
                   model_uri=ISO27001.impact_scale, domain=None, range=Optional[str])

slots.risk_matrix = Slot(uri=ISO27001.risk_matrix, name="risk_matrix", curie=ISO27001.curie('risk_matrix'),
                   model_uri=ISO27001.risk_matrix, domain=None, range=Optional[str])

slots.assessment_frequency = Slot(uri=ISO27001.assessment_frequency, name="assessment_frequency", curie=ISO27001.curie('assessment_frequency'),
                   model_uri=ISO27001.assessment_frequency, domain=None, range=Optional[str])

slots.trigger_events = Slot(uri=ISO27001.trigger_events, name="trigger_events", curie=ISO27001.curie('trigger_events'),
                   model_uri=ISO27001.trigger_events, domain=None, range=Optional[Union[str, list[str]]])

slots.risk_assessments = Slot(uri=ISO27001.risk_assessments, name="risk_assessments", curie=ISO27001.curie('risk_assessments'),
                   model_uri=ISO27001.risk_assessments, domain=None, range=Optional[Union[Union[str, RiskAssessmentId], list[Union[str, RiskAssessmentId]]]])

slots.assessment_scope = Slot(uri=ISO27001.assessment_scope, name="assessment_scope", curie=ISO27001.curie('assessment_scope'),
                   model_uri=ISO27001.assessment_scope, domain=None, range=Optional[str])

slots.assessment_date = Slot(uri=ISO27001.assessment_date, name="assessment_date", curie=ISO27001.curie('assessment_date'),
                   model_uri=ISO27001.assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.assessor = Slot(uri=ISO27001.assessor, name="assessor", curie=ISO27001.curie('assessor'),
                   model_uri=ISO27001.assessor, domain=None, range=Optional[str])

slots.methodology_used = Slot(uri=ISO27001.methodology_used, name="methodology_used", curie=ISO27001.curie('methodology_used'),
                   model_uri=ISO27001.methodology_used, domain=None, range=Optional[str])

slots.risks_identified = Slot(uri=ISO27001.risks_identified, name="risks_identified", curie=ISO27001.curie('risks_identified'),
                   model_uri=ISO27001.risks_identified, domain=None, range=Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]])

slots.summary_findings = Slot(uri=ISO27001.summary_findings, name="summary_findings", curie=ISO27001.curie('summary_findings'),
                   model_uri=ISO27001.summary_findings, domain=None, range=Optional[str])

slots.recommendations = Slot(uri=ISO27001.recommendations, name="recommendations", curie=ISO27001.curie('recommendations'),
                   model_uri=ISO27001.recommendations, domain=None, range=Optional[Union[str, list[str]]])

slots.next_assessment_date = Slot(uri=ISO27001.next_assessment_date, name="next_assessment_date", curie=ISO27001.curie('next_assessment_date'),
                   model_uri=ISO27001.next_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.related_risks = Slot(uri=ISO27001.related_risks, name="related_risks", curie=ISO27001.curie('related_risks'),
                   model_uri=ISO27001.related_risks, domain=None, range=Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]])

slots.risk_source = Slot(uri=ISO27001.risk_source, name="risk_source", curie=ISO27001.curie('risk_source'),
                   model_uri=ISO27001.risk_source, domain=None, range=Optional[str])

slots.threat_description = Slot(uri=ISO27001.threat_description, name="threat_description", curie=ISO27001.curie('threat_description'),
                   model_uri=ISO27001.threat_description, domain=None, range=Optional[str])

slots.vulnerability_description = Slot(uri=ISO27001.vulnerability_description, name="vulnerability_description", curie=ISO27001.curie('vulnerability_description'),
                   model_uri=ISO27001.vulnerability_description, domain=None, range=Optional[str])

slots.affected_assets = Slot(uri=ISO27001.affected_assets, name="affected_assets", curie=ISO27001.curie('affected_assets'),
                   model_uri=ISO27001.affected_assets, domain=None, range=Optional[Union[Union[str, AssetId], list[Union[str, AssetId]]]])

slots.affected_cia_properties = Slot(uri=ISO27001.affected_cia_properties, name="affected_cia_properties", curie=ISO27001.curie('affected_cia_properties'),
                   model_uri=ISO27001.affected_cia_properties, domain=None, range=Optional[Union[str, list[str]]])

slots.risk_owner = Slot(uri=ISO27001.risk_owner, name="risk_owner", curie=ISO27001.curie('risk_owner'),
                   model_uri=ISO27001.risk_owner, domain=None, range=Optional[str])

slots.likelihood = Slot(uri=ISO27001.likelihood, name="likelihood", curie=ISO27001.curie('likelihood'),
                   model_uri=ISO27001.likelihood, domain=None, range=Optional[Union[str, "LikelihoodRating"]])

slots.impact = Slot(uri=ISO27001.impact, name="impact", curie=ISO27001.curie('impact'),
                   model_uri=ISO27001.impact, domain=None, range=Optional[Union[str, "ImpactRating"]])

slots.inherent_risk_level = Slot(uri=ISO27001.inherent_risk_level, name="inherent_risk_level", curie=ISO27001.curie('inherent_risk_level'),
                   model_uri=ISO27001.inherent_risk_level, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.existing_controls = Slot(uri=ISO27001.existing_controls, name="existing_controls", curie=ISO27001.curie('existing_controls'),
                   model_uri=ISO27001.existing_controls, domain=None, range=Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]])

slots.residual_risk_level = Slot(uri=ISO27001.residual_risk_level, name="residual_risk_level", curie=ISO27001.curie('residual_risk_level'),
                   model_uri=ISO27001.residual_risk_level, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.risk_treatment_option = Slot(uri=ISO27001.risk_treatment_option, name="risk_treatment_option", curie=ISO27001.curie('risk_treatment_option'),
                   model_uri=ISO27001.risk_treatment_option, domain=None, range=Optional[Union[str, "RiskTreatmentOption"]])

slots.treatment_priority = Slot(uri=ISO27001.treatment_priority, name="treatment_priority", curie=ISO27001.curie('treatment_priority'),
                   model_uri=ISO27001.treatment_priority, domain=None, range=Optional[str])

slots.related_treatment_plan = Slot(uri=ISO27001.related_treatment_plan, name="related_treatment_plan", curie=ISO27001.curie('related_treatment_plan'),
                   model_uri=ISO27001.related_treatment_plan, domain=None, range=Optional[Union[str, RiskTreatmentPlanId]])

slots.risk_treatment_process = Slot(uri=ISO27001.risk_treatment_process, name="risk_treatment_process", curie=ISO27001.curie('risk_treatment_process'),
                   model_uri=ISO27001.risk_treatment_process, domain=None, range=Optional[Union[str, RiskTreatmentProcessId]])

slots.treatment_options_guidance = Slot(uri=ISO27001.treatment_options_guidance, name="treatment_options_guidance", curie=ISO27001.curie('treatment_options_guidance'),
                   model_uri=ISO27001.treatment_options_guidance, domain=None, range=Optional[str])

slots.control_selection_criteria = Slot(uri=ISO27001.control_selection_criteria, name="control_selection_criteria", curie=ISO27001.curie('control_selection_criteria'),
                   model_uri=ISO27001.control_selection_criteria, domain=None, range=Optional[str])

slots.soa_template = Slot(uri=ISO27001.soa_template, name="soa_template", curie=ISO27001.curie('soa_template'),
                   model_uri=ISO27001.soa_template, domain=None, range=Optional[str])

slots.approval_workflow = Slot(uri=ISO27001.approval_workflow, name="approval_workflow", curie=ISO27001.curie('approval_workflow'),
                   model_uri=ISO27001.approval_workflow, domain=None, range=Optional[str])

slots.risk_treatment_plans = Slot(uri=ISO27001.risk_treatment_plans, name="risk_treatment_plans", curie=ISO27001.curie('risk_treatment_plans'),
                   model_uri=ISO27001.risk_treatment_plans, domain=None, range=Optional[Union[Union[str, RiskTreatmentPlanId], list[Union[str, RiskTreatmentPlanId]]]])

slots.plan_scope = Slot(uri=ISO27001.plan_scope, name="plan_scope", curie=ISO27001.curie('plan_scope'),
                   model_uri=ISO27001.plan_scope, domain=None, range=Optional[str])

slots.risks_addressed = Slot(uri=ISO27001.risks_addressed, name="risks_addressed", curie=ISO27001.curie('risks_addressed'),
                   model_uri=ISO27001.risks_addressed, domain=None, range=Optional[Union[Union[str, RiskId], list[Union[str, RiskId]]]])

slots.treatment_actions = Slot(uri=ISO27001.treatment_actions, name="treatment_actions", curie=ISO27001.curie('treatment_actions'),
                   model_uri=ISO27001.treatment_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.controls_to_implement = Slot(uri=ISO27001.controls_to_implement, name="controls_to_implement", curie=ISO27001.curie('controls_to_implement'),
                   model_uri=ISO27001.controls_to_implement, domain=None, range=Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]])

slots.resources_required = Slot(uri=ISO27001.resources_required, name="resources_required", curie=ISO27001.curie('resources_required'),
                   model_uri=ISO27001.resources_required, domain=None, range=Optional[str])

slots.responsible_parties = Slot(uri=ISO27001.responsible_parties, name="responsible_parties", curie=ISO27001.curie('responsible_parties'),
                   model_uri=ISO27001.responsible_parties, domain=None, range=Optional[Union[str, list[str]]])

slots.implementation_timeline = Slot(uri=ISO27001.implementation_timeline, name="implementation_timeline", curie=ISO27001.curie('implementation_timeline'),
                   model_uri=ISO27001.implementation_timeline, domain=None, range=Optional[str])

slots.risk_owner_approval = Slot(uri=ISO27001.risk_owner_approval, name="risk_owner_approval", curie=ISO27001.curie('risk_owner_approval'),
                   model_uri=ISO27001.risk_owner_approval, domain=None, range=Optional[str])

slots.residual_risk_acceptance = Slot(uri=ISO27001.residual_risk_acceptance, name="residual_risk_acceptance", curie=ISO27001.curie('residual_risk_acceptance'),
                   model_uri=ISO27001.residual_risk_acceptance, domain=None, range=Optional[str])

slots.implementation_status = Slot(uri=ISO27001.implementation_status, name="implementation_status", curie=ISO27001.curie('implementation_status'),
                   model_uri=ISO27001.implementation_status, domain=None, range=Optional[Union[str, "ImplementationStatus"]])

slots.completion_date = Slot(uri=ISO27001.completion_date, name="completion_date", curie=ISO27001.curie('completion_date'),
                   model_uri=ISO27001.completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.statement_of_applicability = Slot(uri=ISO27001.statement_of_applicability, name="statement_of_applicability", curie=ISO27001.curie('statement_of_applicability'),
                   model_uri=ISO27001.statement_of_applicability, domain=None, range=Optional[Union[str, StatementOfApplicabilityId]])

slots.soa_entries = Slot(uri=ISO27001.soa_entries, name="soa_entries", curie=ISO27001.curie('soa_entries'),
                   model_uri=ISO27001.soa_entries, domain=None, range=Optional[Union[Union[dict, SoAEntry], list[Union[dict, SoAEntry]]]])

slots.total_controls = Slot(uri=ISO27001.total_controls, name="total_controls", curie=ISO27001.curie('total_controls'),
                   model_uri=ISO27001.total_controls, domain=None, range=Optional[int])

slots.implemented_count = Slot(uri=ISO27001.implemented_count, name="implemented_count", curie=ISO27001.curie('implemented_count'),
                   model_uri=ISO27001.implemented_count, domain=None, range=Optional[int])

slots.planned_count = Slot(uri=ISO27001.planned_count, name="planned_count", curie=ISO27001.curie('planned_count'),
                   model_uri=ISO27001.planned_count, domain=None, range=Optional[int])

slots.not_applicable_count = Slot(uri=ISO27001.not_applicable_count, name="not_applicable_count", curie=ISO27001.curie('not_applicable_count'),
                   model_uri=ISO27001.not_applicable_count, domain=None, range=Optional[int])

slots.last_review_date = Slot(uri=ISO27001.last_review_date, name="last_review_date", curie=ISO27001.curie('last_review_date'),
                   model_uri=ISO27001.last_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.control_reference = Slot(uri=ISO27001.control_reference, name="control_reference", curie=ISO27001.curie('control_reference'),
                   model_uri=ISO27001.control_reference, domain=None, range=Optional[Union[str, SecurityControlId]])

slots.is_applicable = Slot(uri=ISO27001.is_applicable, name="is_applicable", curie=ISO27001.curie('is_applicable'),
                   model_uri=ISO27001.is_applicable, domain=None, range=Optional[Union[bool, Bool]])

slots.inclusion_justification = Slot(uri=ISO27001.inclusion_justification, name="inclusion_justification", curie=ISO27001.curie('inclusion_justification'),
                   model_uri=ISO27001.inclusion_justification, domain=None, range=Optional[str])

slots.exclusion_justification = Slot(uri=ISO27001.exclusion_justification, name="exclusion_justification", curie=ISO27001.curie('exclusion_justification'),
                   model_uri=ISO27001.exclusion_justification, domain=None, range=Optional[str])

slots.implementation_evidence = Slot(uri=ISO27001.implementation_evidence, name="implementation_evidence", curie=ISO27001.curie('implementation_evidence'),
                   model_uri=ISO27001.implementation_evidence, domain=None, range=Optional[str])

slots.target_implementation_date = Slot(uri=ISO27001.target_implementation_date, name="target_implementation_date", curie=ISO27001.curie('target_implementation_date'),
                   model_uri=ISO27001.target_implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.controls = Slot(uri=ISO27001.controls, name="controls", curie=ISO27001.curie('controls'),
                   model_uri=ISO27001.controls, domain=None, range=Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]])

slots.control_id = Slot(uri=ISO27001.control_id, name="control_id", curie=ISO27001.curie('control_id'),
                   model_uri=ISO27001.control_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[5-8]\.[0-9]{1,2}$'))

slots.control_title = Slot(uri=ISO27001.control_title, name="control_title", curie=ISO27001.curie('control_title'),
                   model_uri=ISO27001.control_title, domain=None, range=Optional[str])

slots.control_category = Slot(uri=ISO27001.control_category, name="control_category", curie=ISO27001.curie('control_category'),
                   model_uri=ISO27001.control_category, domain=None, range=Optional[Union[str, "ControlCategory"]])

slots.control_text = Slot(uri=ISO27001.control_text, name="control_text", curie=ISO27001.curie('control_text'),
                   model_uri=ISO27001.control_text, domain=None, range=Optional[str])

slots.implementation_guidance = Slot(uri=ISO27001.implementation_guidance, name="implementation_guidance", curie=ISO27001.curie('implementation_guidance'),
                   model_uri=ISO27001.implementation_guidance, domain=None, range=Optional[str])

slots.related_controls = Slot(uri=ISO27001.related_controls, name="related_controls", curie=ISO27001.curie('related_controls'),
                   model_uri=ISO27001.related_controls, domain=None, range=Optional[Union[Union[str, SecurityControlId], list[Union[str, SecurityControlId]]]])

slots.applicable_threats = Slot(uri=ISO27001.applicable_threats, name="applicable_threats", curie=ISO27001.curie('applicable_threats'),
                   model_uri=ISO27001.applicable_threats, domain=None, range=Optional[Union[str, list[str]]])

slots.applicable_assets = Slot(uri=ISO27001.applicable_assets, name="applicable_assets", curie=ISO27001.curie('applicable_assets'),
                   model_uri=ISO27001.applicable_assets, domain=None, range=Optional[Union[str, list[str]]])

slots.control_owner = Slot(uri=ISO27001.control_owner, name="control_owner", curie=ISO27001.curie('control_owner'),
                   model_uri=ISO27001.control_owner, domain=None, range=Optional[str])

slots.implementation_date = Slot(uri=ISO27001.implementation_date, name="implementation_date", curie=ISO27001.curie('implementation_date'),
                   model_uri=ISO27001.implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_rating = Slot(uri=ISO27001.effectiveness_rating, name="effectiveness_rating", curie=ISO27001.curie('effectiveness_rating'),
                   model_uri=ISO27001.effectiveness_rating, domain=None, range=Optional[str])

slots.last_test_date = Slot(uri=ISO27001.last_test_date, name="last_test_date", curie=ISO27001.curie('last_test_date'),
                   model_uri=ISO27001.last_test_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.evidence_references = Slot(uri=ISO27001.evidence_references, name="evidence_references", curie=ISO27001.curie('evidence_references'),
                   model_uri=ISO27001.evidence_references, domain=None, range=Optional[Union[str, list[str]]])

slots.resources = Slot(uri=ISO27001.resources, name="resources", curie=ISO27001.curie('resources'),
                   model_uri=ISO27001.resources, domain=None, range=Optional[Union[Union[str, ResourceId], list[Union[str, ResourceId]]]])

slots.resource_type = Slot(uri=ISO27001.resource_type, name="resource_type", curie=ISO27001.curie('resource_type'),
                   model_uri=ISO27001.resource_type, domain=None, range=Optional[str])

slots.quantity = Slot(uri=ISO27001.quantity, name="quantity", curie=ISO27001.curie('quantity'),
                   model_uri=ISO27001.quantity, domain=None, range=Optional[str])

slots.allocation_date = Slot(uri=ISO27001.allocation_date, name="allocation_date", curie=ISO27001.curie('allocation_date'),
                   model_uri=ISO27001.allocation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.allocated_to = Slot(uri=ISO27001.allocated_to, name="allocated_to", curie=ISO27001.curie('allocated_to'),
                   model_uri=ISO27001.allocated_to, domain=None, range=Optional[str])

slots.cost = Slot(uri=ISO27001.cost, name="cost", curie=ISO27001.curie('cost'),
                   model_uri=ISO27001.cost, domain=None, range=Optional[str])

slots.availability_status = Slot(uri=ISO27001.availability_status, name="availability_status", curie=ISO27001.curie('availability_status'),
                   model_uri=ISO27001.availability_status, domain=None, range=Optional[str])

slots.competence_records = Slot(uri=ISO27001.competence_records, name="competence_records", curie=ISO27001.curie('competence_records'),
                   model_uri=ISO27001.competence_records, domain=None, range=Optional[Union[Union[str, CompetenceRecordId], list[Union[str, CompetenceRecordId]]]])

slots.person_name = Slot(uri=ISO27001.person_name, name="person_name", curie=ISO27001.curie('person_name'),
                   model_uri=ISO27001.person_name, domain=None, range=Optional[str])

slots.person_role = Slot(uri=ISO27001.person_role, name="person_role", curie=ISO27001.curie('person_role'),
                   model_uri=ISO27001.person_role, domain=None, range=Optional[str])

slots.required_competencies = Slot(uri=ISO27001.required_competencies, name="required_competencies", curie=ISO27001.curie('required_competencies'),
                   model_uri=ISO27001.required_competencies, domain=None, range=Optional[Union[str, list[str]]])

slots.education_records = Slot(uri=ISO27001.education_records, name="education_records", curie=ISO27001.curie('education_records'),
                   model_uri=ISO27001.education_records, domain=None, range=Optional[Union[str, list[str]]])

slots.training_records = Slot(uri=ISO27001.training_records, name="training_records", curie=ISO27001.curie('training_records'),
                   model_uri=ISO27001.training_records, domain=None, range=Optional[Union[str, list[str]]])

slots.experience_records = Slot(uri=ISO27001.experience_records, name="experience_records", curie=ISO27001.curie('experience_records'),
                   model_uri=ISO27001.experience_records, domain=None, range=Optional[Union[str, list[str]]])

slots.competency_assessment_date = Slot(uri=ISO27001.competency_assessment_date, name="competency_assessment_date", curie=ISO27001.curie('competency_assessment_date'),
                   model_uri=ISO27001.competency_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.competency_gaps = Slot(uri=ISO27001.competency_gaps, name="competency_gaps", curie=ISO27001.curie('competency_gaps'),
                   model_uri=ISO27001.competency_gaps, domain=None, range=Optional[Union[str, list[str]]])

slots.development_actions = Slot(uri=ISO27001.development_actions, name="development_actions", curie=ISO27001.curie('development_actions'),
                   model_uri=ISO27001.development_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.awareness_program = Slot(uri=ISO27001.awareness_program, name="awareness_program", curie=ISO27001.curie('awareness_program'),
                   model_uri=ISO27001.awareness_program, domain=None, range=Optional[Union[str, AwarenessProgramId]])

slots.awareness_topics = Slot(uri=ISO27001.awareness_topics, name="awareness_topics", curie=ISO27001.curie('awareness_topics'),
                   model_uri=ISO27001.awareness_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.delivery_methods = Slot(uri=ISO27001.delivery_methods, name="delivery_methods", curie=ISO27001.curie('delivery_methods'),
                   model_uri=ISO27001.delivery_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.frequency = Slot(uri=ISO27001.frequency, name="frequency", curie=ISO27001.curie('frequency'),
                   model_uri=ISO27001.frequency, domain=None, range=Optional[str])

slots.completion_tracking = Slot(uri=ISO27001.completion_tracking, name="completion_tracking", curie=ISO27001.curie('completion_tracking'),
                   model_uri=ISO27001.completion_tracking, domain=None, range=Optional[str])

slots.effectiveness_measures = Slot(uri=ISO27001.effectiveness_measures, name="effectiveness_measures", curie=ISO27001.curie('effectiveness_measures'),
                   model_uri=ISO27001.effectiveness_measures, domain=None, range=Optional[str])

slots.communication_plan = Slot(uri=ISO27001.communication_plan, name="communication_plan", curie=ISO27001.curie('communication_plan'),
                   model_uri=ISO27001.communication_plan, domain=None, range=Optional[Union[str, CommunicationPlanId]])

slots.communication_items = Slot(uri=ISO27001.communication_items, name="communication_items", curie=ISO27001.curie('communication_items'),
                   model_uri=ISO27001.communication_items, domain=None, range=Optional[Union[Union[dict, CommunicationItem], list[Union[dict, CommunicationItem]]]])

slots.subject = Slot(uri=ISO27001.subject, name="subject", curie=ISO27001.curie('subject'),
                   model_uri=ISO27001.subject, domain=None, range=Optional[str])

slots.purpose = Slot(uri=ISO27001.purpose, name="purpose", curie=ISO27001.curie('purpose'),
                   model_uri=ISO27001.purpose, domain=None, range=Optional[str])

slots.audience = Slot(uri=ISO27001.audience, name="audience", curie=ISO27001.curie('audience'),
                   model_uri=ISO27001.audience, domain=None, range=Optional[str])

slots.method = Slot(uri=ISO27001.method, name="method", curie=ISO27001.curie('method'),
                   model_uri=ISO27001.method, domain=None, range=Optional[str])

slots.responsible_party = Slot(uri=ISO27001.responsible_party, name="responsible_party", curie=ISO27001.curie('responsible_party'),
                   model_uri=ISO27001.responsible_party, domain=None, range=Optional[str])

slots.records_required = Slot(uri=ISO27001.records_required, name="records_required", curie=ISO27001.curie('records_required'),
                   model_uri=ISO27001.records_required, domain=None, range=Optional[Union[bool, Bool]])

slots.documented_information_register = Slot(uri=ISO27001.documented_information_register, name="documented_information_register", curie=ISO27001.curie('documented_information_register'),
                   model_uri=ISO27001.documented_information_register, domain=None, range=Optional[Union[Union[str, DocumentedInformationId], list[Union[str, DocumentedInformationId]]]])

slots.operational_procedures = Slot(uri=ISO27001.operational_procedures, name="operational_procedures", curie=ISO27001.curie('operational_procedures'),
                   model_uri=ISO27001.operational_procedures, domain=None, range=Optional[Union[Union[str, OperationalProcedureId], list[Union[str, OperationalProcedureId]]]])

slots.procedure_scope = Slot(uri=ISO27001.procedure_scope, name="procedure_scope", curie=ISO27001.curie('procedure_scope'),
                   model_uri=ISO27001.procedure_scope, domain=None, range=Optional[str])

slots.process_criteria = Slot(uri=ISO27001.process_criteria, name="process_criteria", curie=ISO27001.curie('process_criteria'),
                   model_uri=ISO27001.process_criteria, domain=None, range=Optional[str])

slots.control_measures = Slot(uri=ISO27001.control_measures, name="control_measures", curie=ISO27001.curie('control_measures'),
                   model_uri=ISO27001.control_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.responsible_roles = Slot(uri=ISO27001.responsible_roles, name="responsible_roles", curie=ISO27001.curie('responsible_roles'),
                   model_uri=ISO27001.responsible_roles, domain=None, range=Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]])

slots.change_control_requirements = Slot(uri=ISO27001.change_control_requirements, name="change_control_requirements", curie=ISO27001.curie('change_control_requirements'),
                   model_uri=ISO27001.change_control_requirements, domain=None, range=Optional[str])

slots.monitoring_program = Slot(uri=ISO27001.monitoring_program, name="monitoring_program", curie=ISO27001.curie('monitoring_program'),
                   model_uri=ISO27001.monitoring_program, domain=None, range=Optional[Union[str, MonitoringProgramId]])

slots.monitoring_items = Slot(uri=ISO27001.monitoring_items, name="monitoring_items", curie=ISO27001.curie('monitoring_items'),
                   model_uri=ISO27001.monitoring_items, domain=None, range=Optional[Union[Union[dict, MonitoringItem], list[Union[dict, MonitoringItem]]]])

slots.metric_name = Slot(uri=ISO27001.metric_name, name="metric_name", curie=ISO27001.curie('metric_name'),
                   model_uri=ISO27001.metric_name, domain=None, range=Optional[str])

slots.metric_description = Slot(uri=ISO27001.metric_description, name="metric_description", curie=ISO27001.curie('metric_description'),
                   model_uri=ISO27001.metric_description, domain=None, range=Optional[str])

slots.analysis_frequency = Slot(uri=ISO27001.analysis_frequency, name="analysis_frequency", curie=ISO27001.curie('analysis_frequency'),
                   model_uri=ISO27001.analysis_frequency, domain=None, range=Optional[str])

slots.analyst = Slot(uri=ISO27001.analyst, name="analyst", curie=ISO27001.curie('analyst'),
                   model_uri=ISO27001.analyst, domain=None, range=Optional[str])

slots.target_threshold = Slot(uri=ISO27001.target_threshold, name="target_threshold", curie=ISO27001.curie('target_threshold'),
                   model_uri=ISO27001.target_threshold, domain=None, range=Optional[str])

slots.alert_threshold = Slot(uri=ISO27001.alert_threshold, name="alert_threshold", curie=ISO27001.curie('alert_threshold'),
                   model_uri=ISO27001.alert_threshold, domain=None, range=Optional[str])

slots.trend = Slot(uri=ISO27001.trend, name="trend", curie=ISO27001.curie('trend'),
                   model_uri=ISO27001.trend, domain=None, range=Optional[str])

slots.internal_audits = Slot(uri=ISO27001.internal_audits, name="internal_audits", curie=ISO27001.curie('internal_audits'),
                   model_uri=ISO27001.internal_audits, domain=None, range=Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]])

slots.audit_reference = Slot(uri=ISO27001.audit_reference, name="audit_reference", curie=ISO27001.curie('audit_reference'),
                   model_uri=ISO27001.audit_reference, domain=None, range=Optional[str])

slots.audit_type = Slot(uri=ISO27001.audit_type, name="audit_type", curie=ISO27001.curie('audit_type'),
                   model_uri=ISO27001.audit_type, domain=None, range=Optional[str])

slots.audit_scope = Slot(uri=ISO27001.audit_scope, name="audit_scope", curie=ISO27001.curie('audit_scope'),
                   model_uri=ISO27001.audit_scope, domain=None, range=Optional[str])

slots.audit_criteria = Slot(uri=ISO27001.audit_criteria, name="audit_criteria", curie=ISO27001.curie('audit_criteria'),
                   model_uri=ISO27001.audit_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_objectives = Slot(uri=ISO27001.audit_objectives, name="audit_objectives", curie=ISO27001.curie('audit_objectives'),
                   model_uri=ISO27001.audit_objectives, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_period_start = Slot(uri=ISO27001.audit_period_start, name="audit_period_start", curie=ISO27001.curie('audit_period_start'),
                   model_uri=ISO27001.audit_period_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.audit_period_end = Slot(uri=ISO27001.audit_period_end, name="audit_period_end", curie=ISO27001.curie('audit_period_end'),
                   model_uri=ISO27001.audit_period_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.lead_auditor = Slot(uri=ISO27001.lead_auditor, name="lead_auditor", curie=ISO27001.curie('lead_auditor'),
                   model_uri=ISO27001.lead_auditor, domain=None, range=Optional[str])

slots.audit_team = Slot(uri=ISO27001.audit_team, name="audit_team", curie=ISO27001.curie('audit_team'),
                   model_uri=ISO27001.audit_team, domain=None, range=Optional[Union[str, list[str]]])

slots.auditee_representatives = Slot(uri=ISO27001.auditee_representatives, name="auditee_representatives", curie=ISO27001.curie('auditee_representatives'),
                   model_uri=ISO27001.auditee_representatives, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_plan = Slot(uri=ISO27001.audit_plan, name="audit_plan", curie=ISO27001.curie('audit_plan'),
                   model_uri=ISO27001.audit_plan, domain=None, range=Optional[str])

slots.findings = Slot(uri=ISO27001.findings, name="findings", curie=ISO27001.curie('findings'),
                   model_uri=ISO27001.findings, domain=None, range=Optional[Union[Union[str, AuditFindingId], list[Union[str, AuditFindingId]]]])

slots.positive_observations = Slot(uri=ISO27001.positive_observations, name="positive_observations", curie=ISO27001.curie('positive_observations'),
                   model_uri=ISO27001.positive_observations, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_conclusion = Slot(uri=ISO27001.audit_conclusion, name="audit_conclusion", curie=ISO27001.curie('audit_conclusion'),
                   model_uri=ISO27001.audit_conclusion, domain=None, range=Optional[str])

slots.report_date = Slot(uri=ISO27001.report_date, name="report_date", curie=ISO27001.curie('report_date'),
                   model_uri=ISO27001.report_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.report_distribution = Slot(uri=ISO27001.report_distribution, name="report_distribution", curie=ISO27001.curie('report_distribution'),
                   model_uri=ISO27001.report_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.finding_type = Slot(uri=ISO27001.finding_type, name="finding_type", curie=ISO27001.curie('finding_type'),
                   model_uri=ISO27001.finding_type, domain=None, range=Optional[Union[str, "AuditFindingType"]])

slots.clause_reference = Slot(uri=ISO27001.clause_reference, name="clause_reference", curie=ISO27001.curie('clause_reference'),
                   model_uri=ISO27001.clause_reference, domain=None, range=Optional[str])

slots.finding_description = Slot(uri=ISO27001.finding_description, name="finding_description", curie=ISO27001.curie('finding_description'),
                   model_uri=ISO27001.finding_description, domain=None, range=Optional[str])

slots.objective_evidence = Slot(uri=ISO27001.objective_evidence, name="objective_evidence", curie=ISO27001.curie('objective_evidence'),
                   model_uri=ISO27001.objective_evidence, domain=None, range=Optional[str])

slots.root_cause_analysis = Slot(uri=ISO27001.root_cause_analysis, name="root_cause_analysis", curie=ISO27001.curie('root_cause_analysis'),
                   model_uri=ISO27001.root_cause_analysis, domain=None, range=Optional[str])

slots.risk_implication = Slot(uri=ISO27001.risk_implication, name="risk_implication", curie=ISO27001.curie('risk_implication'),
                   model_uri=ISO27001.risk_implication, domain=None, range=Optional[str])

slots.recommended_action = Slot(uri=ISO27001.recommended_action, name="recommended_action", curie=ISO27001.curie('recommended_action'),
                   model_uri=ISO27001.recommended_action, domain=None, range=Optional[str])

slots.auditee_response = Slot(uri=ISO27001.auditee_response, name="auditee_response", curie=ISO27001.curie('auditee_response'),
                   model_uri=ISO27001.auditee_response, domain=None, range=Optional[str])

slots.linked_corrective_action = Slot(uri=ISO27001.linked_corrective_action, name="linked_corrective_action", curie=ISO27001.curie('linked_corrective_action'),
                   model_uri=ISO27001.linked_corrective_action, domain=None, range=Optional[Union[str, CorrectiveActionId]])

slots.closure_status = Slot(uri=ISO27001.closure_status, name="closure_status", curie=ISO27001.curie('closure_status'),
                   model_uri=ISO27001.closure_status, domain=None, range=Optional[str])

slots.closure_date = Slot(uri=ISO27001.closure_date, name="closure_date", curie=ISO27001.curie('closure_date'),
                   model_uri=ISO27001.closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.management_reviews = Slot(uri=ISO27001.management_reviews, name="management_reviews", curie=ISO27001.curie('management_reviews'),
                   model_uri=ISO27001.management_reviews, domain=None, range=Optional[Union[Union[str, ManagementReviewId], list[Union[str, ManagementReviewId]]]])

slots.attendees = Slot(uri=ISO27001.attendees, name="attendees", curie=ISO27001.curie('attendees'),
                   model_uri=ISO27001.attendees, domain=None, range=Optional[Union[str, list[str]]])

slots.previous_actions_status = Slot(uri=ISO27001.previous_actions_status, name="previous_actions_status", curie=ISO27001.curie('previous_actions_status'),
                   model_uri=ISO27001.previous_actions_status, domain=None, range=Optional[str])

slots.context_changes = Slot(uri=ISO27001.context_changes, name="context_changes", curie=ISO27001.curie('context_changes'),
                   model_uri=ISO27001.context_changes, domain=None, range=Optional[str])

slots.interested_party_changes = Slot(uri=ISO27001.interested_party_changes, name="interested_party_changes", curie=ISO27001.curie('interested_party_changes'),
                   model_uri=ISO27001.interested_party_changes, domain=None, range=Optional[str])

slots.performance_trends = Slot(uri=ISO27001.performance_trends, name="performance_trends", curie=ISO27001.curie('performance_trends'),
                   model_uri=ISO27001.performance_trends, domain=None, range=Optional[str])

slots.audit_results_summary = Slot(uri=ISO27001.audit_results_summary, name="audit_results_summary", curie=ISO27001.curie('audit_results_summary'),
                   model_uri=ISO27001.audit_results_summary, domain=None, range=Optional[str])

slots.risk_assessment_results = Slot(uri=ISO27001.risk_assessment_results, name="risk_assessment_results", curie=ISO27001.curie('risk_assessment_results'),
                   model_uri=ISO27001.risk_assessment_results, domain=None, range=Optional[str])

slots.improvement_opportunities = Slot(uri=ISO27001.improvement_opportunities, name="improvement_opportunities", curie=ISO27001.curie('improvement_opportunities'),
                   model_uri=ISO27001.improvement_opportunities, domain=None, range=Optional[Union[str, list[str]]])

slots.decisions = Slot(uri=ISO27001.decisions, name="decisions", curie=ISO27001.curie('decisions'),
                   model_uri=ISO27001.decisions, domain=None, range=Optional[Union[str, list[str]]])

slots.action_items = Slot(uri=ISO27001.action_items, name="action_items", curie=ISO27001.curie('action_items'),
                   model_uri=ISO27001.action_items, domain=None, range=Optional[Union[str, list[str]]])

slots.next_review_date = Slot(uri=ISO27001.next_review_date, name="next_review_date", curie=ISO27001.curie('next_review_date'),
                   model_uri=ISO27001.next_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.nonconformities = Slot(uri=ISO27001.nonconformities, name="nonconformities", curie=ISO27001.curie('nonconformities'),
                   model_uri=ISO27001.nonconformities, domain=None, range=Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]])

slots.nonconformity_source = Slot(uri=ISO27001.nonconformity_source, name="nonconformity_source", curie=ISO27001.curie('nonconformity_source'),
                   model_uri=ISO27001.nonconformity_source, domain=None, range=Optional[str])

slots.detection_date = Slot(uri=ISO27001.detection_date, name="detection_date", curie=ISO27001.curie('detection_date'),
                   model_uri=ISO27001.detection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.detected_by = Slot(uri=ISO27001.detected_by, name="detected_by", curie=ISO27001.curie('detected_by'),
                   model_uri=ISO27001.detected_by, domain=None, range=Optional[str])

slots.requirement_violated = Slot(uri=ISO27001.requirement_violated, name="requirement_violated", curie=ISO27001.curie('requirement_violated'),
                   model_uri=ISO27001.requirement_violated, domain=None, range=Optional[str])

slots.nonconformity_description = Slot(uri=ISO27001.nonconformity_description, name="nonconformity_description", curie=ISO27001.curie('nonconformity_description'),
                   model_uri=ISO27001.nonconformity_description, domain=None, range=Optional[str])

slots.immediate_actions = Slot(uri=ISO27001.immediate_actions, name="immediate_actions", curie=ISO27001.curie('immediate_actions'),
                   model_uri=ISO27001.immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.consequences_addressed = Slot(uri=ISO27001.consequences_addressed, name="consequences_addressed", curie=ISO27001.curie('consequences_addressed'),
                   model_uri=ISO27001.consequences_addressed, domain=None, range=Optional[str])

slots.root_cause = Slot(uri=ISO27001.root_cause, name="root_cause", curie=ISO27001.curie('root_cause'),
                   model_uri=ISO27001.root_cause, domain=None, range=Optional[str])

slots.similar_nonconformities_check = Slot(uri=ISO27001.similar_nonconformities_check, name="similar_nonconformities_check", curie=ISO27001.curie('similar_nonconformities_check'),
                   model_uri=ISO27001.similar_nonconformities_check, domain=None, range=Optional[str])

slots.linked_corrective_actions = Slot(uri=ISO27001.linked_corrective_actions, name="linked_corrective_actions", curie=ISO27001.curie('linked_corrective_actions'),
                   model_uri=ISO27001.linked_corrective_actions, domain=None, range=Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]])

slots.closure_evidence = Slot(uri=ISO27001.closure_evidence, name="closure_evidence", curie=ISO27001.curie('closure_evidence'),
                   model_uri=ISO27001.closure_evidence, domain=None, range=Optional[str])

slots.corrective_actions = Slot(uri=ISO27001.corrective_actions, name="corrective_actions", curie=ISO27001.curie('corrective_actions'),
                   model_uri=ISO27001.corrective_actions, domain=None, range=Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]])

slots.linked_nonconformity = Slot(uri=ISO27001.linked_nonconformity, name="linked_nonconformity", curie=ISO27001.curie('linked_nonconformity'),
                   model_uri=ISO27001.linked_nonconformity, domain=None, range=Optional[Union[str, NonconformityId]])

slots.action_description = Slot(uri=ISO27001.action_description, name="action_description", curie=ISO27001.curie('action_description'),
                   model_uri=ISO27001.action_description, domain=None, range=Optional[str])

slots.root_cause_addressed = Slot(uri=ISO27001.root_cause_addressed, name="root_cause_addressed", curie=ISO27001.curie('root_cause_addressed'),
                   model_uri=ISO27001.root_cause_addressed, domain=None, range=Optional[str])

slots.target_completion_date = Slot(uri=ISO27001.target_completion_date, name="target_completion_date", curie=ISO27001.curie('target_completion_date'),
                   model_uri=ISO27001.target_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.actual_completion_date = Slot(uri=ISO27001.actual_completion_date, name="actual_completion_date", curie=ISO27001.curie('actual_completion_date'),
                   model_uri=ISO27001.actual_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_criteria = Slot(uri=ISO27001.effectiveness_criteria, name="effectiveness_criteria", curie=ISO27001.curie('effectiveness_criteria'),
                   model_uri=ISO27001.effectiveness_criteria, domain=None, range=Optional[str])

slots.effectiveness_review_date = Slot(uri=ISO27001.effectiveness_review_date, name="effectiveness_review_date", curie=ISO27001.curie('effectiveness_review_date'),
                   model_uri=ISO27001.effectiveness_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_verified = Slot(uri=ISO27001.effectiveness_verified, name="effectiveness_verified", curie=ISO27001.curie('effectiveness_verified'),
                   model_uri=ISO27001.effectiveness_verified, domain=None, range=Optional[Union[bool, Bool]])

slots.isms_changes_required = Slot(uri=ISO27001.isms_changes_required, name="isms_changes_required", curie=ISO27001.curie('isms_changes_required'),
                   model_uri=ISO27001.isms_changes_required, domain=None, range=Optional[str])

slots.improvements = Slot(uri=ISO27001.improvements, name="improvements", curie=ISO27001.curie('improvements'),
                   model_uri=ISO27001.improvements, domain=None, range=Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]])

slots.improvement_source = Slot(uri=ISO27001.improvement_source, name="improvement_source", curie=ISO27001.curie('improvement_source'),
                   model_uri=ISO27001.improvement_source, domain=None, range=Optional[str])

slots.identification_date = Slot(uri=ISO27001.identification_date, name="identification_date", curie=ISO27001.curie('identification_date'),
                   model_uri=ISO27001.identification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.identified_by = Slot(uri=ISO27001.identified_by, name="identified_by", curie=ISO27001.curie('identified_by'),
                   model_uri=ISO27001.identified_by, domain=None, range=Optional[str])

slots.improvement_description = Slot(uri=ISO27001.improvement_description, name="improvement_description", curie=ISO27001.curie('improvement_description'),
                   model_uri=ISO27001.improvement_description, domain=None, range=Optional[str])

slots.expected_benefit = Slot(uri=ISO27001.expected_benefit, name="expected_benefit", curie=ISO27001.curie('expected_benefit'),
                   model_uri=ISO27001.expected_benefit, domain=None, range=Optional[str])

slots.priority = Slot(uri=ISO27001.priority, name="priority", curie=ISO27001.curie('priority'),
                   model_uri=ISO27001.priority, domain=None, range=Optional[str])

slots.implementation_plan = Slot(uri=ISO27001.implementation_plan, name="implementation_plan", curie=ISO27001.curie('implementation_plan'),
                   model_uri=ISO27001.implementation_plan, domain=None, range=Optional[str])

slots.outcome_assessment = Slot(uri=ISO27001.outcome_assessment, name="outcome_assessment", curie=ISO27001.curie('outcome_assessment'),
                   model_uri=ISO27001.outcome_assessment, domain=None, range=Optional[str])

slots.asset_type = Slot(uri=ISO27001.asset_type, name="asset_type", curie=ISO27001.curie('asset_type'),
                   model_uri=ISO27001.asset_type, domain=None, range=Optional[str])

slots.asset_owner = Slot(uri=ISO27001.asset_owner, name="asset_owner", curie=ISO27001.curie('asset_owner'),
                   model_uri=ISO27001.asset_owner, domain=None, range=Optional[str])

slots.asset_custodian = Slot(uri=ISO27001.asset_custodian, name="asset_custodian", curie=ISO27001.curie('asset_custodian'),
                   model_uri=ISO27001.asset_custodian, domain=None, range=Optional[str])

slots.location = Slot(uri=ISO27001.location, name="location", curie=ISO27001.curie('location'),
                   model_uri=ISO27001.location, domain=None, range=Optional[str])

slots.criticality = Slot(uri=ISO27001.criticality, name="criticality", curie=ISO27001.curie('criticality'),
                   model_uri=ISO27001.criticality, domain=None, range=Optional[str])

slots.event_datetime = Slot(uri=ISO27001.event_datetime, name="event_datetime", curie=ISO27001.curie('event_datetime'),
                   model_uri=ISO27001.event_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.reporter = Slot(uri=ISO27001.reporter, name="reporter", curie=ISO27001.curie('reporter'),
                   model_uri=ISO27001.reporter, domain=None, range=Optional[str])

slots.event_description = Slot(uri=ISO27001.event_description, name="event_description", curie=ISO27001.curie('event_description'),
                   model_uri=ISO27001.event_description, domain=None, range=Optional[str])

slots.initial_assessment = Slot(uri=ISO27001.initial_assessment, name="initial_assessment", curie=ISO27001.curie('initial_assessment'),
                   model_uri=ISO27001.initial_assessment, domain=None, range=Optional[str])

slots.categorized_as_incident = Slot(uri=ISO27001.categorized_as_incident, name="categorized_as_incident", curie=ISO27001.curie('categorized_as_incident'),
                   model_uri=ISO27001.categorized_as_incident, domain=None, range=Optional[Union[bool, Bool]])

slots.linked_incident = Slot(uri=ISO27001.linked_incident, name="linked_incident", curie=ISO27001.curie('linked_incident'),
                   model_uri=ISO27001.linked_incident, domain=None, range=Optional[Union[str, InformationSecurityIncidentId]])

slots.incident_datetime = Slot(uri=ISO27001.incident_datetime, name="incident_datetime", curie=ISO27001.curie('incident_datetime'),
                   model_uri=ISO27001.incident_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.incident_category = Slot(uri=ISO27001.incident_category, name="incident_category", curie=ISO27001.curie('incident_category'),
                   model_uri=ISO27001.incident_category, domain=None, range=Optional[str])

slots.severity = Slot(uri=ISO27001.severity, name="severity", curie=ISO27001.curie('severity'),
                   model_uri=ISO27001.severity, domain=None, range=Optional[str])

slots.affected_cia = Slot(uri=ISO27001.affected_cia, name="affected_cia", curie=ISO27001.curie('affected_cia'),
                   model_uri=ISO27001.affected_cia, domain=None, range=Optional[Union[str, list[str]]])

slots.incident_description = Slot(uri=ISO27001.incident_description, name="incident_description", curie=ISO27001.curie('incident_description'),
                   model_uri=ISO27001.incident_description, domain=None, range=Optional[str])

slots.detection_method = Slot(uri=ISO27001.detection_method, name="detection_method", curie=ISO27001.curie('detection_method'),
                   model_uri=ISO27001.detection_method, domain=None, range=Optional[str])

slots.response_actions = Slot(uri=ISO27001.response_actions, name="response_actions", curie=ISO27001.curie('response_actions'),
                   model_uri=ISO27001.response_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.containment_actions = Slot(uri=ISO27001.containment_actions, name="containment_actions", curie=ISO27001.curie('containment_actions'),
                   model_uri=ISO27001.containment_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.eradication_actions = Slot(uri=ISO27001.eradication_actions, name="eradication_actions", curie=ISO27001.curie('eradication_actions'),
                   model_uri=ISO27001.eradication_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.recovery_actions = Slot(uri=ISO27001.recovery_actions, name="recovery_actions", curie=ISO27001.curie('recovery_actions'),
                   model_uri=ISO27001.recovery_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.lessons_learned = Slot(uri=ISO27001.lessons_learned, name="lessons_learned", curie=ISO27001.curie('lessons_learned'),
                   model_uri=ISO27001.lessons_learned, domain=None, range=Optional[str])

slots.evidence_collected = Slot(uri=ISO27001.evidence_collected, name="evidence_collected", curie=ISO27001.curie('evidence_collected'),
                   model_uri=ISO27001.evidence_collected, domain=None, range=Optional[Union[str, list[str]]])

slots.notification_required = Slot(uri=ISO27001.notification_required, name="notification_required", curie=ISO27001.curie('notification_required'),
                   model_uri=ISO27001.notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.notifications_made = Slot(uri=ISO27001.notifications_made, name="notifications_made", curie=ISO27001.curie('notifications_made'),
                   model_uri=ISO27001.notifications_made, domain=None, range=Optional[Union[str, list[str]]])

slots.closure_datetime = Slot(uri=ISO27001.closure_datetime, name="closure_datetime", curie=ISO27001.curie('closure_datetime'),
                   model_uri=ISO27001.closure_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.post_incident_review = Slot(uri=ISO27001.post_incident_review, name="post_incident_review", curie=ISO27001.curie('post_incident_review'),
                   model_uri=ISO27001.post_incident_review, domain=None, range=Optional[str])

slots.certification_status = Slot(uri=ISO27001.certification_status, name="certification_status", curie=ISO27001.curie('certification_status'),
                   model_uri=ISO27001.certification_status, domain=None, range=Optional[str])

slots.certification_body = Slot(uri=ISO27001.certification_body, name="certification_body", curie=ISO27001.curie('certification_body'),
                   model_uri=ISO27001.certification_body, domain=None, range=Optional[str])

slots.certification_date = Slot(uri=ISO27001.certification_date, name="certification_date", curie=ISO27001.curie('certification_date'),
                   model_uri=ISO27001.certification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.recertification_date = Slot(uri=ISO27001.recertification_date, name="recertification_date", curie=ISO27001.curie('recertification_date'),
                   model_uri=ISO27001.recertification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.programme_period = Slot(uri=ISO27001.programme_period, name="programme_period", curie=ISO27001.curie('programme_period'),
                   model_uri=ISO27001.programme_period, domain=None, range=Optional[str])

slots.planned_audits = Slot(uri=ISO27001.planned_audits, name="planned_audits", curie=ISO27001.curie('planned_audits'),
                   model_uri=ISO27001.planned_audits, domain=None, range=Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]])

slots.audit_frequency_rationale = Slot(uri=ISO27001.audit_frequency_rationale, name="audit_frequency_rationale", curie=ISO27001.curie('audit_frequency_rationale'),
                   model_uri=ISO27001.audit_frequency_rationale, domain=None, range=Optional[str])

slots.resource_requirements = Slot(uri=ISO27001.resource_requirements, name="resource_requirements", curie=ISO27001.curie('resource_requirements'),
                   model_uri=ISO27001.resource_requirements, domain=None, range=Optional[str])

slots.auditor_qualifications = Slot(uri=ISO27001.auditor_qualifications, name="auditor_qualifications", curie=ISO27001.curie('auditor_qualifications'),
                   model_uri=ISO27001.auditor_qualifications, domain=None, range=Optional[str])

slots.programme_status = Slot(uri=ISO27001.programme_status, name="programme_status", curie=ISO27001.curie('programme_status'),
                   model_uri=ISO27001.programme_status, domain=None, range=Optional[str])

slots.NamedEntity_id = Slot(uri=ISO27001.id, name="NamedEntity_id", curie=ISO27001.curie('id'),
                   model_uri=ISO27001.NamedEntity_id, domain=NamedEntity, range=Union[str, NamedEntityId])

slots.RiskTreatmentPlan_approved_date = Slot(uri=ISO27001.approved_date, name="RiskTreatmentPlan_approved_date", curie=ISO27001.curie('approved_date'),
                   model_uri=ISO27001.RiskTreatmentPlan_approved_date, domain=RiskTreatmentPlan, range=Optional[Union[str, XSDDate]])

slots.ManagementReview_review_date = Slot(uri=ISO27001.review_date, name="ManagementReview_review_date", curie=ISO27001.curie('review_date'),
                   model_uri=ISO27001.ManagementReview_review_date, domain=ManagementReview, range=Optional[Union[str, XSDDate]])
