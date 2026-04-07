from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'aligned_standard': {'tag': 'aligned_standard',
                                          'value': 'ISO/IEC 27002:2022 (Annex A '
                                                   'control guidance)'},
                     'amendment_date': {'tag': 'amendment_date',
                                        'value': '2024-02'},
                     'amendment_reference': {'tag': 'amendment_reference',
                                             'value': 'ISO/IEC 27001:2022/Amd. '
                                                      '1:2024(E)'},
                     'amendment_title': {'tag': 'amendment_title',
                                         'value': 'Climate action changes'},
                     'normative_reference': {'tag': 'normative_reference',
                                             'value': 'ISO/IEC 27000 (vocabulary '
                                                      'and overview)'},
                     'rights_notice': {'tag': 'rights_notice',
                                       'value': 'This project is licensed under '
                                                'Apache-2.0 for original code and '
                                                'schema structure. ISO/IEC '
                                                'standards text is owned by ISO '
                                                'and is not redistributed by this '
                                                'project license.'},
                     'risk_framework_alignment': {'tag': 'risk_framework_alignment',
                                                  'value': 'ISO 31000:2018'},
                     'schema_maintainer': {'tag': 'schema_maintainer',
                                           'value': 'noel.mcloughlin@gmail.com'},
                     'schema_status': {'tag': 'schema_status', 'value': 'stable'},
                     'standard_date': {'tag': 'standard_date', 'value': '2022-10'},
                     'standard_edition': {'tag': 'standard_edition',
                                          'value': 'Third edition'},
                     'standard_reference': {'tag': 'standard_reference',
                                            'value': 'ISO/IEC 27001:2022(E)'},
                     'standard_title': {'tag': 'standard_title',
                                        'value': 'Information security, '
                                                 'cybersecurity and privacy '
                                                 'protection -  Information '
                                                 'security management systems - '
                                                 'Requirements'}},
     'default_prefix': 'iso27001',
     'default_range': 'string',
     'description': 'A comprehensive LinkML schema modeling ISMS entities, '
                    'workflows, and traceability links aligned to ISO/IEC '
                    '27001:2022 clause and Annex references. Designed for open '
                    'data publication, automated validation, and integration with '
                    'governance, risk, and compliance (GRC) systems.\n'
                    'This schema captures: - ISMS lifecycle (establish, implement, '
                    'maintain, improve) - Risk assessment and treatment processes '
                    '(Clause 6.1) - Annex A control catalog structures organized '
                    'by domain - Audit, measurement, and continual improvement '
                    'artifacts',
     'id': 'https://w3id.org/lmodel/iso27001',
     'imports': ['linkml:types'],
     'license': 'https://www.apache.org/licenses/LICENSE-2.0',
     'name': 'iso27001',
     'prefixes': {'cis_controls': {'prefix_prefix': 'cis_controls',
                                   'prefix_reference': 'https://w3id.org/lmodel/cis-controls/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'iso': {'prefix_prefix': 'iso',
                          'prefix_reference': 'https://www.iso.org/standard/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso27002': {'prefix_prefix': 'iso27002',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27002/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'source_file': 'src/iso27001/schema/iso27001.yaml',
     'subsets': {'annex_a_controls': {'annotations': {'control_count': {'tag': 'control_count',
                                                                        'value': '93'}},
                                      'comments': ['Derived from ISO/IEC '
                                                   '27002:2022 Clauses 5-8',
                                                   'Used in Statement of '
                                                   'Applicability (SoA) '
                                                   'generation'],
                                      'description': 'Classes and enumerations '
                                                     'representing the 93 controls '
                                                     'in Annex A, organized into '
                                                     'four domains: '
                                                     'organizational, people, '
                                                     'physical, technological.',
                                      'from_schema': 'https://w3id.org/lmodel/iso27001',
                                      'name': 'annex_a_controls'},
                 'continual_improvement': {'comments': ['Links nonconformities to '
                                                        'root causes and '
                                                        'corrective actions',
                                                        'Tracks improvement '
                                                        'opportunities'],
                                           'description': 'Elements for '
                                                          'nonconformity '
                                                          'management, corrective '
                                                          'actions, and '
                                                          'improvement tracking '
                                                          'per Clause 10.',
                                           'from_schema': 'https://w3id.org/lmodel/iso27001',
                                           'name': 'continual_improvement'},
                 'documented_information': {'comments': ['Includes policies, '
                                                         'procedures, records, and '
                                                         'evidence',
                                                         'Tracks version control '
                                                         'and approval status'],
                                            'description': 'Classes representing '
                                                           'required documented '
                                                           'information per Clause '
                                                           '7.5. Supports document '
                                                           'control and retention '
                                                           'requirements.',
                                            'from_schema': 'https://w3id.org/lmodel/iso27001',
                                            'name': 'documented_information'},
                 'isms_core': {'comments': ['Mandatory for any ISO 27001 '
                                            'conformance dataset',
                                            'Maps to requirement statements in the '
                                            'standard'],
                               'description': 'Core ISMS structural elements '
                                              'required for conformity with '
                                              'Clauses 4-10. These classes '
                                              'represent the minimum viable data '
                                              'model for ISMS documentation.',
                               'from_schema': 'https://w3id.org/lmodel/iso27001',
                               'name': 'isms_core'},
                 'performance_evaluation': {'comments': ['Captures audit programs, '
                                                         'findings, and KPIs',
                                                         'Supports evidence '
                                                         'retention requirements'],
                                            'description': 'Classes for '
                                                           'monitoring, '
                                                           'measurement, internal '
                                                           'audit, and management '
                                                           'review per Clauses '
                                                           '9.1-9.3.',
                                            'from_schema': 'https://w3id.org/lmodel/iso27001',
                                            'name': 'performance_evaluation'},
                 'risk_management': {'comments': ['Includes risk identification, '
                                                  'analysis, evaluation, and '
                                                  'treatment',
                                                  'Links risks to controls and '
                                                  'residual risk acceptance'],
                                     'description': 'Elements supporting risk '
                                                    'assessment (6.1.2) and risk '
                                                    'treatment (6.1.3). Aligned '
                                                    'with ISO 31000:2018 '
                                                    'principles.',
                                     'from_schema': 'https://w3id.org/lmodel/iso27001',
                                     'name': 'risk_management'}},
     'title': 'ISO 27001 / ISMS: LinkML Schema',
     'types': {'duration type': {'base': 'str',
                                 'description': 'ISO 8601 duration value such as '
                                                'P1Y, P30D, or PT4H',
                                 'from_schema': 'https://w3id.org/lmodel/iso27001',
                                 'name': 'duration type',
                                 'uri': 'xsd:duration'},
               'positive integer type': {'base': 'int',
                                         'description': 'integer greater than '
                                                        'zero; natural number '
                                                        'explicitly excluding zero',
                                         'exact_mappings': ['wikidata:Q28920044'],
                                         'from_schema': 'https://w3id.org/lmodel/iso27001',
                                         'name': 'positive integer type',
                                         'uri': 'xsd:positiveInteger'},
               'unsigned short type': {'base': 'int',
                                       'description': 'data type for non-negative '
                                                      'integers that can be '
                                                      'represented with 16 bits',
                                       'exact_mappings': ['wikidata:Q110650833'],
                                       'from_schema': 'https://w3id.org/lmodel/iso27001',
                                       'name': 'unsigned short type',
                                       'uri': 'xsd:unsignedShort'}}} )

class ControlCategory(str, Enum):
    """
    The four control domains defined in ISO/IEC 27001:2022 Annex A, corresponding to Clauses 5-8 of ISO/IEC 27002:2022.
    """
    organizational = "organizational"
    """
    Organizational controls (Annex A.5) - policies, roles, asset management, access control, supplier relationships, incident management, compliance.
    """
    people = "people"
    """
    People controls (Annex A.6) - screening, employment terms, awareness, disciplinary process, termination responsibilities, remote working.
    """
    physical = "physical"
    """
    Physical controls (Annex A.7) - perimeters, entry controls, equipment protection, secure areas, media handling, cabling, maintenance.
    """
    technological = "technological"
    """
    Technological controls (Annex A.8) - endpoint security, access restrictions, authentication, malware protection, logging, cryptography, secure development.
    """


class ImplementationStatus(str, Enum):
    """
    Lifecycle status of a security control, used in Statement of Applicability and control tracking.
    """
    not_started = "not_started"
    """
    Control identified but no implementation activities begun.
    """
    planned = "planned"
    """
    Control scheduled for implementation with defined timeline.
    """
    in_progress = "in_progress"
    """
    Implementation actively underway but not yet complete.
    """
    implemented = "implemented"
    """
    Control fully implemented and operational.
    """
    not_applicable = "not_applicable"
    """
    Control excluded from scope with documented justification per 6.1.3 d).
    """


class RiskTreatmentOption(str, Enum):
    """
    Standard risk treatment options per ISO 31000 and ISO 27005.
    """
    modify = "modify"
    """
    Apply controls to change the risk level (reduce likelihood or impact).
    """
    accept = "accept"
    """
    Accept the risk without further treatment, within risk appetite. Requires risk owner approval.
    """
    avoid = "avoid"
    """
    Eliminate the risk by removing the activity or asset that creates it.
    """
    share = "share"
    """
    Transfer or share risk with external parties (e.g., insurance, outsourcing).
    """


class RiskLevel(str, Enum):
    """
    Qualitative risk rating derived from likelihood x impact analysis.
    """
    very_low = "very_low"
    """
    Negligible risk requiring no immediate action.
    """
    low = "low"
    """
    Minor risk manageable through routine procedures.
    """
    medium = "medium"
    """
    Moderate risk requiring management attention and planned controls.
    """
    high = "high"
    """
    Significant risk requiring priority treatment and escalation.
    """
    critical = "critical"
    """
    Severe risk threatening organizational objectives; requires immediate executive action and resource allocation.
    """


class DocumentType(str, Enum):
    """
    Categories of documented information required or recommended by ISO 27001.
    """
    policy = "policy"
    """
    High-level statement of intent and direction (e.g., IS policy per 5.2).
    """
    procedure = "procedure"
    """
    Documented steps for performing activities consistently.
    """
    standard = "standard"
    """
    Mandatory requirements for specific technologies or processes.
    """
    guideline = "guideline"
    """
    Recommended practices that support policies and procedures.
    """
    record = "record"
    """
    Evidence of activities performed or results achieved.
    """
    plan = "plan"
    """
    Documented approach for achieving objectives (e.g., risk treatment plan).
    """
    report = "report"
    """
    Formal output of assessment, audit, or review activities.
    """


class AuditFindingType(str, Enum):
    """
    Classification of internal audit findings.
    """
    major_nonconformity = "major_nonconformity"
    """
    Significant failure to fulfill a requirement that affects ISMS capability to achieve intended outcomes.
    """
    minor_nonconformity = "minor_nonconformity"
    """
    Isolated lapse that does not significantly affect ISMS effectiveness.
    """
    observation = "observation"
    """
    Noted condition that could lead to nonconformity if not addressed.
    """
    positive_finding = "positive_finding"
    """
    Evidence of effective implementation exceeding requirements.
    """


class LikelihoodRating(str, Enum):
    """
    Qualitative likelihood scale for risk assessment.
    """
    rare = "rare"
    """
    Highly unlikely to occur (< 5% probability).
    """
    unlikely = "unlikely"
    """
    Not expected but possible (5-20% probability).
    """
    possible = "possible"
    """
    May occur at some point (20-50% probability).
    """
    likely = "likely"
    """
    Probably will occur (50-80% probability).
    """
    almost_certain = "almost_certain"
    """
    Expected to occur in most circumstances (> 80% probability).
    """


class ImpactRating(str, Enum):
    """
    Qualitative impact scale for risk assessment.
    """
    negligible = "negligible"
    """
    No significant impact on operations or objectives.
    """
    minor = "minor"
    """
    Limited impact, easily absorbed by normal operations.
    """
    moderate = "moderate"
    """
    Noticeable impact requiring management intervention.
    """
    major = "major"
    """
    Serious impact on objectives, reputation, or compliance.
    """
    severe = "severe"
    """
    Catastrophic impact threatening organizational viability.
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ['All concrete classes should inherit from this or a subclass',
                      'Ensures consistent identification across the schema'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'slot_usage': {'id': {'description': 'Unique identifier for this entity '
                                              'instance.',
                               'identifier': True,
                               'name': 'id',
                               'required': True}}})

    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.5'}},
         'comments': ['Supports identification and control metadata for managed '
                      'documents',
                      'Supports lifecycle, protection, and retention tracking'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['documented_information']})

    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InformationSecurityManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required to support the full ISMS lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.4'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['This is the root entity for any ISMS conformance dataset',
                      'Aggregates ISMS processes and their relationships',
                      'Includes explicit scope metadata and related governance '
                      'artifacts',
                      'Reference: ISO/IEC 27001:2022 Clause 4.4. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'related_mappings': ['cis_controls:CISControlsDocument']})

    organization: Optional[str] = Field(default=None, description="""Reference to the organization operating the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    scope_statement: Optional[str] = Field(default=None, description="""Documented statement of ISMS scope per 4.3.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.3'}},
         'comments': ['Available as documented information'],
         'domain_of': ['InformationSecurityManagementSystem']} })
    scope_boundaries: Optional[list[str]] = Field(default=None, description="""Defined boundaries of the ISMS scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    scope_exclusions: Optional[list[str]] = Field(default=None, description="""Any exclusions from scope with justification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    context_internal_issues: Optional[list[str]] = Field(default=None, description="""Internal issues relevant to ISMS per 4.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    context_external_issues: Optional[list[str]] = Field(default=None, description="""External issues relevant to ISMS per 4.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    interested_parties: Optional[list[str]] = Field(default=None, description="""Stakeholders relevant to the ISMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.2'}},
         'domain_of': ['InformationSecurityManagementSystem']} })
    information_security_policy: Optional[str] = Field(default=None, description="""Reference to the information security policy.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.2'}},
         'domain_of': ['InformationSecurityManagementSystem']} })
    objectives: Optional[list[str]] = Field(default=None, description="""Information security objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    risk_assessment_process: Optional[str] = Field(default=None, description="""Reference to the risk assessment process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    risk_treatment_process: Optional[str] = Field(default=None, description="""Reference to the risk treatment process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    statement_of_applicability: Optional[str] = Field(default=None, description="""Reference to the Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    controls: Optional[list[str]] = Field(default=None, description="""Security controls applied in the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    roles: Optional[list[str]] = Field(default=None, description="""Information security roles defined in the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    resources: Optional[list[str]] = Field(default=None, description="""Resources provided for the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    competence_records: Optional[list[str]] = Field(default=None, description="""Competence records for personnel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    awareness_program: Optional[str] = Field(default=None, description="""Reference to the awareness program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    communication_plan: Optional[str] = Field(default=None, description="""Reference to the communication plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    documented_information_register: Optional[list[str]] = Field(default=None, description="""Register of documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    operational_procedures: Optional[list[str]] = Field(default=None, description="""Operational procedures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    risk_assessments: Optional[list[str]] = Field(default=None, description="""Risk assessment instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    risk_treatment_plans: Optional[list[str]] = Field(default=None, description="""Risk treatment plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    monitoring_program: Optional[str] = Field(default=None, description="""Reference to the monitoring program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    internal_audits: Optional[list[str]] = Field(default=None, description="""Internal audit instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    management_reviews: Optional[list[str]] = Field(default=None, description="""Management review instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    nonconformities: Optional[list[str]] = Field(default=None, description="""Nonconformities identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    corrective_actions: Optional[list[str]] = Field(default=None, description="""Corrective actions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    improvements: Optional[list[str]] = Field(default=None, description="""Improvement opportunities tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    certification_status: Optional[str] = Field(default=None, description="""Current certification status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem'],
         'examples': [{'value': 'not_certified'},
                      {'value': 'in_progress'},
                      {'value': 'certified'}]} })
    certification_body: Optional[str] = Field(default=None, description="""Accredited certification body.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    certification_date: Optional[date] = Field(default=None, description="""Date certification was achieved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    recertification_date: Optional[date] = Field(default=None, description="""Date recertification is due.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityManagementSystem']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Organization(NamedEntity):
    """
    The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_amendment': {'tag': 'iso27001_amendment',
                                                'value': 'Amd. 1:2024'},
                         'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'comments': ['Context determination per 4.1 feeds into ISMS planning',
                      'Climate change relevance determination added by Amd. 1:2024 to '
                      'Clause 4.1',
                      'Reference: ISO/IEC 27001:2022 Clause 4.1 and Amd. 1:2024. '
                      'ISO/IEC standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    legal_name: Optional[str] = Field(default=None, description="""Legal registered name of the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    trading_names: Optional[list[str]] = Field(default=None, description="""Names under which the organization conducts business.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    organization_type: Optional[str] = Field(default=None, description="""Type of organization (e.g., corporation, government, nonprofit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    industry_sector: Optional[str] = Field(default=None, description="""Primary industry sector of the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization'],
         'examples': [{'value': 'Financial Services'},
                      {'value': 'Healthcare'},
                      {'value': 'Technology'}]} })
    size_category: Optional[str] = Field(default=None, description="""Organization size classification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization'],
         'examples': [{'value': 'SME'}, {'value': 'Enterprise'}]} })
    employee_count: Optional[int] = Field(default=None, description="""Approximate number of employees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    geographic_locations: Optional[list[str]] = Field(default=None, description="""Countries or regions where the organization operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    regulatory_jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions whose regulations apply to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    parent_organization: Optional[str] = Field(default=None, description="""Parent organization if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    subsidiaries: Optional[list[str]] = Field(default=None, description="""Subsidiary organizations if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    climate_change_relevant: Optional[bool] = Field(default=None, description="""Whether climate change has been determined to be a relevant issue for the organization's context, per Clause 4.1 as amended by Amd. 1:2024.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_amendment': {'tag': 'iso27001_amendment',
                                                'value': 'Amd. 1:2024'},
                         'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'comments': ['Set true if climate change is identified as a relevant external '
                      'or internal issue',
                      'When true, capture details in context_external_issues or '
                      'context_internal_issues'],
         'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_amendment': {'tag': 'iso27001_amendment',
                                                'value': 'Amd. 1:2024'},
                         'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.2'}},
         'comments': ['Captures stakeholder needs and expectations relevant to ISMS '
                      'scope',
                      'Requirements may include legal, regulatory, and contractual '
                      'obligations',
                      'Relevant interested parties can have requirements related to '
                      'climate change (Amd. 1:2024 Clause 4.2 Note 2)',
                      'Reference: ISO/IEC 27001:2022 Clause 4.2 and Amd. 1:2024. '
                      'ISO/IEC standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    party_type: Optional[str] = Field(default=None, description="""Category of interested party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty'],
         'examples': [{'value': 'internal'},
                      {'value': 'external'},
                      {'value': 'regulatory'}]} })
    relationship: Optional[str] = Field(default=None, description="""Nature of the relationship with the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    requirements: Optional[list[str]] = Field(default=None, description="""Requirements of the interested party.""", json_schema_extra = { "linkml_meta": {'comments': ['May include legal, regulatory, and contractual requirements'],
         'domain_of': ['InterestedParty']} })
    communication_needs: Optional[str] = Field(default=None, description="""Communication requirements for this party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InformationSecurityPolicy(DocumentedInformation):
    """
    The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.2'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['Captures policy intent and governance commitments',
                      'Supports communication and acknowledgement tracking',
                      'Reference: ISO/IEC 27001:2022 Clause 5.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'documented_information']})

    policy_statement: Optional[str] = Field(default=None, description="""The core policy statement text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityPolicy']} })
    policy_objectives_framework: Optional[str] = Field(default=None, description="""Framework for setting information security objectives.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 5.2 b)'], 'domain_of': ['InformationSecurityPolicy']} })
    commitment_statements: Optional[list[str]] = Field(default=None, description="""Statements of commitment included in the policy.""", json_schema_extra = { "linkml_meta": {'comments': ['Includes commitment to satisfy requirements per 5.2 c)',
                      'Includes commitment to continual improvement per 5.2 d)'],
         'domain_of': ['InformationSecurityPolicy']} })
    applicability_statement: Optional[str] = Field(default=None, description="""Statement of policy applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityPolicy']} })
    communication_date: Optional[date] = Field(default=None, description="""Date when the policy was communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityPolicy']} })
    acknowledgment_required: Optional[bool] = Field(default=None, description="""Whether acknowledgment is required from personnel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityPolicy']} })
    related_topic_policies: Optional[list[str]] = Field(default=None, description="""Topic-specific policies supporting this policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityPolicy']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class TopicSpecificPolicy(DocumentedInformation):
    """
    A policy addressing a specific information security topic, supporting the overarching information security policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': '5.1'}},
         'comments': ['Examples include access control policy, cryptography policy, '
                      'backup policy',
                      'Referenced throughout Annex A controls'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['documented_information']})

    topic_area: Optional[str] = Field(default=None, description="""The specific topic addressed by the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy'],
         'examples': [{'value': 'Access Control'},
                      {'value': 'Cryptography'},
                      {'value': 'Backup'}]} })
    parent_policy: Optional[str] = Field(default=None, description="""The parent policy this topic-specific policy supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy']} })
    applicable_controls: Optional[list[str]] = Field(default=None, description="""Controls related to this policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'Asset']} })
    target_audience: Optional[str] = Field(default=None, description="""Intended audience for the policy or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AwarenessProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Role(NamedEntity):
    """
    An information security role with defined responsibilities and authorities per Clause 5.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.3'}},
         'comments': ['Used to assign ISMS responsibilities, authorities, and '
                      'accountability',
                      'Supports reporting-line and delegation modeling',
                      'Reference: ISO/IEC 27001:2022 Clause 5.3. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    role_type: Optional[str] = Field(default=None, description="""Category of the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role'],
         'examples': [{'value': 'CISO'},
                      {'value': 'Risk Owner'},
                      {'value': 'Asset Owner'},
                      {'value': 'Auditor'}]} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Responsibilities assigned to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    authorities: Optional[list[str]] = Field(default=None, description="""Authorities granted to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    accountability: Optional[str] = Field(default=None, description="""What the role is accountable for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    assigned_to: Optional[list[str]] = Field(default=None, description="""Person(s) assigned to this role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    delegation_rules: Optional[str] = Field(default=None, description="""Rules for delegating responsibilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    reporting_line: Optional[str] = Field(default=None, description="""To whom this role reports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InformationSecurityObjective(NamedEntity):
    """
    A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '6.2'}},
         'comments': ['Designed for measurable objective tracking and periodic review',
                      'Links objectives to related risks, controls, and action plans',
                      'Reference: ISO/IEC 27001:2022 Clause 6.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    objective_statement: Optional[str] = Field(default=None, description="""Clear statement of the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective']} })
    target_value: Optional[str] = Field(default=None, description="""Target value for the objective metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective']} })
    current_value: Optional[str] = Field(default=None, description="""Current measured value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    metric_definition: Optional[str] = Field(default=None, description="""Definition of how the objective is measured.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 6.2 b) objectives are measurable where practicable'],
         'domain_of': ['InformationSecurityObjective']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used to measure the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    measurement_frequency: Optional[str] = Field(default=None, description="""How often measurement is performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    responsible_role: Optional[str] = Field(default=None, description="""Role responsible for the objective or control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'SoAEntry']} })
    target_date: Optional[date] = Field(default=None, description="""Target date for achieving the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'ImprovementOpportunity']} })
    achievement_status: Optional[str] = Field(default=None, description="""Current status of objective achievement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective']} })
    related_risks: Optional[list[str]] = Field(default=None, description="""Associated risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'Asset']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective',
                       'SecurityControl',
                       'OperationalProcedure']} })
    action_plan: Optional[str] = Field(default=None, description="""Plan for achieving the objective.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 6.2 h-l) planning to achieve objectives'],
         'domain_of': ['InformationSecurityObjective']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class RiskAssessmentProcess(DocumentedInformation):
    """
    The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['Defines reusable criteria, scales, and methods for risk '
                      'assessments',
                      'Supports repeatable assessment execution over time',
                      'Reference: ISO/IEC 27001:2022 Clause 6.1.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['risk_management', 'documented_information']})

    risk_acceptance_criteria: Optional[str] = Field(default=None, description="""Criteria for accepting risks.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2 a) 1)'}},
         'domain_of': ['RiskAssessmentProcess']} })
    assessment_criteria: Optional[str] = Field(default=None, description="""Criteria for performing risk assessments.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2 a) 2)'}},
         'domain_of': ['RiskAssessmentProcess']} })
    assessment_methodology: Optional[str] = Field(default=None, description="""Methodology used for risk assessment.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports consistent, valid, and comparable results per 6.1.2 '
                      'b)'],
         'domain_of': ['RiskAssessmentProcess']} })
    likelihood_scale: Optional[str] = Field(default=None, description="""Scale used for likelihood rating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessmentProcess']} })
    impact_scale: Optional[str] = Field(default=None, description="""Scale used for impact rating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessmentProcess']} })
    risk_matrix: Optional[str] = Field(default=None, description="""Risk matrix or calculation method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessmentProcess']} })
    assessment_frequency: Optional[str] = Field(default=None, description="""Planned frequency of risk assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessmentProcess']} })
    trigger_events: Optional[list[str]] = Field(default=None, description="""Events that trigger risk assessment outside planned schedule.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 8.2, when significant changes are proposed or occur'],
         'domain_of': ['RiskAssessmentProcess']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class RiskAssessment(DocumentedInformation):
    """
    An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '8.2'}},
         'comments': ['Performed at planned intervals or when significant changes '
                      'occur',
                      'Results are retained as documented information',
                      'Reference: ISO/IEC 27001:2022 Clause 8.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['risk_management']})

    assessment_scope: Optional[str] = Field(default=None, description="""Scope of the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    assessment_date: Optional[date] = Field(default=None, description="""Date the assessment was conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    assessor: Optional[str] = Field(default=None, description="""Person or team who conducted the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    methodology_used: Optional[str] = Field(default=None, description="""Specific methodology applied in this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    risks_identified: Optional[list[str]] = Field(default=None, description="""Risks identified in this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    summary_findings: Optional[str] = Field(default=None, description="""Summary of assessment findings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    recommendations: Optional[list[str]] = Field(default=None, description="""Recommendations from the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    next_assessment_date: Optional[date] = Field(default=None, description="""Planned date for next assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskAssessment']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Risk(NamedEntity):
    """
    An identified information security risk that may affect information security properties within the ISMS scope.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2'}},
         'comments': ['Links threat, vulnerability, and affected assets to risk '
                      'ownership',
                      'Supports likelihood, impact, treatment, and residual risk '
                      'tracking',
                      'Reference: ISO/IEC 27001:2022 Clause 6.1.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['risk_management']})

    risk_source: Optional[str] = Field(default=None, description="""Source or origin of the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    threat_description: Optional[str] = Field(default=None, description="""Description of the threat exploiting the vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    vulnerability_description: Optional[str] = Field(default=None, description="""Description of the vulnerability that could be exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    affected_assets: Optional[list[str]] = Field(default=None, description="""Assets affected by this risk or incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk',
                       'InformationSecurityEvent',
                       'InformationSecurityIncident']} })
    affected_cia_properties: Optional[list[str]] = Field(default=None, description="""Which CIA properties are affected (confidentiality, integrity, availability).""", json_schema_extra = { "linkml_meta": {'comments': ['Per 6.1.2 c) 1) risks associated with loss of CIA'],
         'domain_of': ['Risk']} })
    risk_owner: Optional[str] = Field(default=None, description="""Person accountable for managing the risk.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2 c) 2)'}},
         'domain_of': ['Risk']} })
    likelihood: Optional[LikelihoodRating] = Field(default=None, description="""Assessed likelihood of risk occurrence.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2 d) 2)'}},
         'domain_of': ['Risk']} })
    impact: Optional[ImpactRating] = Field(default=None, description="""Assessed impact if risk materializes.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2 d) 1)'}},
         'domain_of': ['Risk']} })
    inherent_risk_level: Optional[RiskLevel] = Field(default=None, description="""Risk level before controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    existing_controls: Optional[list[str]] = Field(default=None, description="""Controls currently in place affecting this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    residual_risk_level: Optional[RiskLevel] = Field(default=None, description="""Risk level after controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    risk_treatment_option: Optional[RiskTreatmentOption] = Field(default=None, description="""Selected treatment option for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    treatment_priority: Optional[str] = Field(default=None, description="""Priority for treating this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    related_treatment_plan: Optional[str] = Field(default=None, description="""Risk treatment plan addressing this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class RiskTreatmentProcess(DocumentedInformation):
    """
    The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['Defines how treatment options and controls are selected',
                      'Supports Statement of Applicability generation workflows',
                      'Reference: ISO/IEC 27001:2022 Clause 6.1.3. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['risk_management', 'documented_information']})

    treatment_options_guidance: Optional[str] = Field(default=None, description="""Guidance on selecting treatment options.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentProcess']} })
    control_selection_criteria: Optional[str] = Field(default=None, description="""Criteria for selecting controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentProcess']} })
    soa_template: Optional[str] = Field(default=None, description="""Template used for Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentProcess']} })
    approval_workflow: Optional[str] = Field(default=None, description="""Workflow for approving risk treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentProcess']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class RiskTreatmentPlan(DocumentedInformation):
    """
    A risk treatment plan documenting planned actions to address identified risks through selected controls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'comments': ['Captures treatment execution plans with approval and acceptance '
                      'metadata',
                      'Supports implementation status and completion tracking',
                      'Reference: ISO/IEC 27001:2022 Clause 6.1.3. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['risk_management', 'documented_information'],
         'slot_usage': {'approved_date': {'description': 'Date when the risk treatment '
                                                         'plan was approved.',
                                          'name': 'approved_date'}}})

    plan_scope: Optional[str] = Field(default=None, description="""Scope of the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    risks_addressed: Optional[list[str]] = Field(default=None, description="""Risks addressed by this plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    treatment_actions: Optional[list[str]] = Field(default=None, description="""Actions to be taken for treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    controls_to_implement: Optional[list[str]] = Field(default=None, description="""Controls to be implemented as part of treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    resources_required: Optional[str] = Field(default=None, description="""Resources required for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan', 'CorrectiveAction']} })
    responsible_parties: Optional[list[str]] = Field(default=None, description="""Parties responsible for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    implementation_timeline: Optional[str] = Field(default=None, description="""Timeline for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    risk_owner_approval: Optional[str] = Field(default=None, description="""Risk owner who approved the plan.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3 f)'}},
         'domain_of': ['RiskTreatmentPlan']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the risk treatment plan was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    residual_risk_acceptance: Optional[str] = Field(default=None, description="""Documentation of residual risk acceptance.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3 f)'}},
         'domain_of': ['RiskTreatmentPlan']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan', 'SoAEntry', 'SecurityControl']} })
    completion_date: Optional[date] = Field(default=None, description="""Date when implementation was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3 d)'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['Records control applicability and implementation state',
                      'Captures inclusion or exclusion rationale for each control '
                      'entry',
                      'Reference: ISO/IEC 27001:2022 Clause 6.1.3 d). ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'annex_a_controls', 'documented_information']})

    soa_entries: Optional[list[SoAEntry]] = Field(default=None, description="""Individual control entries in the SoA.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    total_controls: Optional[int] = Field(default=None, description="""Total number of controls in scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    implemented_count: Optional[int] = Field(default=None, description="""Number of implemented controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    planned_count: Optional[int] = Field(default=None, description="""Number of controls planned for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    not_applicable_count: Optional[int] = Field(default=None, description="""Number of controls marked not applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    last_review_date: Optional[date] = Field(default=None, description="""Date of last review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class SoAEntry(ConfiguredBaseModel):
    """
    A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Each Annex A control should have a corresponding SoA entry',
                      'Exclusions require documented justification'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['annex_a_controls']})

    control_reference: Optional[str] = Field(default=None, description="""Reference to the control (e.g., A.5.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry', 'AuditFinding']} })
    is_applicable: Optional[bool] = Field(default=None, description="""Whether the control is applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })
    inclusion_justification: Optional[str] = Field(default=None, description="""Justification for including the control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3 d)'}},
         'domain_of': ['SoAEntry']} })
    exclusion_justification: Optional[str] = Field(default=None, description="""Justification for excluding the control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3 d)'}},
         'domain_of': ['SoAEntry']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan', 'SoAEntry', 'SecurityControl']} })
    implementation_evidence: Optional[str] = Field(default=None, description="""Evidence of control implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })
    responsible_role: Optional[str] = Field(default=None, description="""Role responsible for the objective or control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'SoAEntry']} })
    target_implementation_date: Optional[date] = Field(default=None, description="""Target date for implementing the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })


class SecurityControl(NamedEntity):
    """
    A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_reference': {'tag': 'annex_reference',
                                             'value': 'Annex A'},
                         'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'comments': ['93 controls organized in four domains (organizational, people, '
                      'physical, technological)',
                      'Controls are referenced in risk treatment and SoA',
                      'Supports organization-authored control statements and evidence '
                      'links',
                      'Reference: ISO/IEC 27001:2022 Annex A; ISO/IEC 27002:2022 '
                      'Clauses 5-8. ISO/IEC standards text is copyright ISO - not '
                      'reproduced here.',
                      'The control_text slot must contain organization-authored '
                      'content only, not ISO standards text.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['annex_a_controls'],
         'related_mappings': ['cis_controls:Safeguard']})

    control_id: Optional[str] = Field(default=None, description="""Control identifier from Annex A (e.g., 5.1, 8.24).""", json_schema_extra = { "linkml_meta": {'comments': ['Format matches Annex A numbering'],
         'domain_of': ['SecurityControl']} })
    control_title: Optional[str] = Field(default=None, description="""Title of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    control_category: Optional[ControlCategory] = Field(default=None, description="""Domain category of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    control_text: Optional[str] = Field(default=None, description="""Organization-authored control statement or external control summary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    implementation_guidance: Optional[str] = Field(default=None, description="""Organization-authored implementation notes for the control.""", json_schema_extra = { "linkml_meta": {'comments': ['May reference internal standards, procedures, or external '
                      'licensed sources'],
         'domain_of': ['SecurityControl']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective',
                       'SecurityControl',
                       'OperationalProcedure']} })
    applicable_threats: Optional[list[str]] = Field(default=None, description="""Threats this control addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    applicable_assets: Optional[list[str]] = Field(default=None, description="""Asset types this control applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    control_owner: Optional[str] = Field(default=None, description="""Person responsible for the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan', 'SoAEntry', 'SecurityControl']} })
    implementation_date: Optional[date] = Field(default=None, description="""Date the control was implemented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    effectiveness_rating: Optional[str] = Field(default=None, description="""Rating of control effectiveness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    last_test_date: Optional[date] = Field(default=None, description="""Date the control was last tested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    evidence_references: Optional[list[str]] = Field(default=None, description="""References to evidence of implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SecurityControl']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })

    @field_validator('control_id')
    def pattern_control_id(cls, v):
        pattern=re.compile(r"^[5-8]\.[0-9]{1,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid control_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid control_id format: {v}"
            raise ValueError(err_msg)
        return v


class Resource(NamedEntity):
    """
    A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.1'}},
         'comments': ['Reference: ISO/IEC 27001:2022 Clause 7.1. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    resource_type: Optional[str] = Field(default=None, description="""Type of resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource'],
         'examples': [{'value': 'personnel'},
                      {'value': 'technology'},
                      {'value': 'budget'},
                      {'value': 'infrastructure'}]} })
    quantity: Optional[str] = Field(default=None, description="""Quantity of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    allocation_date: Optional[date] = Field(default=None, description="""Date the resource was allocated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    allocated_to: Optional[str] = Field(default=None, description="""What the resource is allocated to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    cost: Optional[str] = Field(default=None, description="""Cost of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    availability_status: Optional[str] = Field(default=None, description="""Current availability of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.2'}},
         'comments': ['Documents personnel qualifications and development activities',
                      'Actions to acquire competence are evaluated for effectiveness',
                      'Reference: ISO/IEC 27001:2022 Clause 7.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'documented_information']})

    person_name: Optional[str] = Field(default=None, description="""Name of the person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    person_role: Optional[str] = Field(default=None, description="""Role of the person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    required_competencies: Optional[list[str]] = Field(default=None, description="""Competencies required for the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    education_records: Optional[list[str]] = Field(default=None, description="""Education qualifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    training_records: Optional[list[str]] = Field(default=None, description="""Training completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    experience_records: Optional[list[str]] = Field(default=None, description="""Relevant experience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    competency_assessment_date: Optional[date] = Field(default=None, description="""Date of last competency assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    competency_gaps: Optional[list[str]] = Field(default=None, description="""Identified competency gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    development_actions: Optional[list[str]] = Field(default=None, description="""Actions to address competency gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.3'}},
         'comments': ['Tracks security awareness coverage, delivery, and personnel '
                      'completion records',
                      'Reference: ISO/IEC 27001:2022 Clause 7.3. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    awareness_topics: Optional[list[str]] = Field(default=None, description="""Topics covered in awareness program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    delivery_methods: Optional[list[str]] = Field(default=None, description="""Methods used to deliver awareness content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    target_audience: Optional[str] = Field(default=None, description="""Intended audience for the policy or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AwarenessProgram']} })
    frequency: Optional[str] = Field(default=None, description="""Frequency of the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram', 'CommunicationItem']} })
    completion_tracking: Optional[str] = Field(default=None, description="""How completion is tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    effectiveness_measures: Optional[str] = Field(default=None, description="""How effectiveness is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the ISMS per Clause 7.4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.4'}},
         'comments': ['Captures communication scope, timing, audience, and channels',
                      'Reference: ISO/IEC 27001:2022 Clause 7.4. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'documented_information']})

    communication_items: Optional[list[CommunicationItem]] = Field(default=None, description="""Communication items in the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationPlan']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CommunicationItem(ConfiguredBaseModel):
    """
    A single communication requirement within the communication plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    subject: Optional[str] = Field(default=None, description="""Subject of the communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    purpose: Optional[str] = Field(default=None, description="""Purpose of the communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    audience: Optional[str] = Field(default=None, description="""Target audience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    frequency: Optional[str] = Field(default=None, description="""Frequency of the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram', 'CommunicationItem']} })
    method: Optional[str] = Field(default=None, description="""Method of communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    records_required: Optional[bool] = Field(default=None, description="""Whether records are required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })


class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control per Clause 8.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '8.1'}},
         'comments': ['Captures process criteria, controls, and accountable roles',
                      'Reference: ISO/IEC 27001:2022 Clause 8.1. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['documented_information']})

    procedure_scope: Optional[str] = Field(default=None, description="""Scope of the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    process_criteria: Optional[str] = Field(default=None, description="""Criteria established for the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    control_measures: Optional[list[str]] = Field(default=None, description="""Control measures implemented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    responsible_roles: Optional[list[str]] = Field(default=None, description="""Roles responsible for the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective',
                       'SecurityControl',
                       'OperationalProcedure']} })
    change_control_requirements: Optional[str] = Field(default=None, description="""Requirements for controlling changes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.1'}},
         'comments': ['Captures metrics, methods, and analysis cadence',
                      'Supports reproducible monitoring and evaluation records',
                      'Reference: ISO/IEC 27001:2022 Clause 9.1. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    monitoring_items: Optional[list[MonitoringItem]] = Field(default=None, description="""Items to be monitored.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class MonitoringItem(ConfiguredBaseModel):
    """
    A single item to be monitored and measured per 9.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation']})

    metric_name: Optional[str] = Field(default=None, description="""Name of the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    metric_description: Optional[str] = Field(default=None, description="""Description of what is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used to measure the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    measurement_frequency: Optional[str] = Field(default=None, description="""How often measurement is performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    analysis_frequency: Optional[str] = Field(default=None, description="""How often analysis is performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    analyst: Optional[str] = Field(default=None, description="""Person performing analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    target_threshold: Optional[str] = Field(default=None, description="""Target threshold value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    alert_threshold: Optional[str] = Field(default=None, description="""Threshold triggering alerts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    current_value: Optional[str] = Field(default=None, description="""Current measured value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'MonitoringItem']} })
    trend: Optional[str] = Field(default=None, description="""Current trend direction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })


class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.2'}},
         'comments': ['Captures audit scope, criteria, findings, and conclusions',
                      'Supports periodic conformance and effectiveness assessment '
                      'records',
                      'Reference: ISO/IEC 27001:2022 Clause 9.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    audit_reference: Optional[str] = Field(default=None, description="""Reference identifier for the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_type: Optional[str] = Field(default=None, description="""Type of audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit'],
         'examples': [{'value': 'full'}, {'value': 'partial'}, {'value': 'follow-up'}]} })
    audit_scope: Optional[str] = Field(default=None, description="""Scope of the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_criteria: Optional[list[str]] = Field(default=None, description="""Criteria against which audit is conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_objectives: Optional[list[str]] = Field(default=None, description="""Objectives of the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_period_start: Optional[date] = Field(default=None, description="""Start date of audit period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_period_end: Optional[date] = Field(default=None, description="""End date of audit period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    lead_auditor: Optional[str] = Field(default=None, description="""Lead auditor for the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_team: Optional[list[str]] = Field(default=None, description="""Audit team members.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    auditee_representatives: Optional[list[str]] = Field(default=None, description="""Representatives from audited areas.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_plan: Optional[str] = Field(default=None, description="""Audit plan document reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    findings: Optional[list[str]] = Field(default=None, description="""Audit findings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    positive_observations: Optional[list[str]] = Field(default=None, description="""Positive observations noted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_conclusion: Optional[str] = Field(default=None, description="""Overall audit conclusion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    report_date: Optional[date] = Field(default=None, description="""Date the report was issued.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    report_distribution: Optional[list[str]] = Field(default=None, description="""Distribution list for the report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per 9.2.2, planning audit activities over a defined period.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.2.2'}},
         'comments': ['Captures planned audit activities over a defined period',
                      'Includes cadence rationale, resources, and qualification '
                      'metadata',
                      'Reference: ISO/IEC 27001:2022 Clause 9.2.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    programme_period: Optional[str] = Field(default=None, description="""Period covered by the audit programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    planned_audits: Optional[list[str]] = Field(default=None, description="""Audits planned in this programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    audit_frequency_rationale: Optional[str] = Field(default=None, description="""Rationale for audit frequency decisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    resource_requirements: Optional[str] = Field(default=None, description="""Resource requirements for the programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    auditor_qualifications: Optional[str] = Field(default=None, description="""Required qualifications for auditors.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    programme_status: Optional[str] = Field(default=None, description="""Current status of the programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AuditFinding(NamedEntity):
    """
    A finding from an internal audit, including nonconformities, observations, and positive findings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation']})

    finding_type: Optional[AuditFindingType] = Field(default=None, description="""Type of audit finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    clause_reference: Optional[str] = Field(default=None, description="""Reference to standard clause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    control_reference: Optional[str] = Field(default=None, description="""Reference to the control (e.g., A.5.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry', 'AuditFinding']} })
    finding_description: Optional[str] = Field(default=None, description="""Description of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    objective_evidence: Optional[str] = Field(default=None, description="""Evidence supporting the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    root_cause_analysis: Optional[str] = Field(default=None, description="""Analysis of root cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    risk_implication: Optional[str] = Field(default=None, description="""Risk implications of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    recommended_action: Optional[str] = Field(default=None, description="""Recommended action to address finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    auditee_response: Optional[str] = Field(default=None, description="""Response from the auditee.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    linked_corrective_action: Optional[str] = Field(default=None, description="""Corrective action linked to this finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    closure_status: Optional[str] = Field(default=None, description="""Status of finding closure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    closure_date: Optional[date] = Field(default=None, description="""Date the finding was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding', 'Nonconformity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness for purpose.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.3'}},
         'comments': ['Captures periodic management review inputs, outputs, and '
                      'follow-up actions',
                      'Reference: ISO/IEC 27001:2022 Clause 9.3. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['performance_evaluation', 'documented_information'],
         'slot_usage': {'review_date': {'description': 'Date when the management '
                                                       'review was conducted.',
                                        'name': 'review_date'}}})

    review_date: Optional[date] = Field(default=None, description="""Date when the management review was conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    attendees: Optional[list[str]] = Field(default=None, description="""Attendees of the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    previous_actions_status: Optional[str] = Field(default=None, description="""Status of actions from previous reviews.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 a)'}},
         'domain_of': ['ManagementReview']} })
    context_changes: Optional[str] = Field(default=None, description="""Changes in context since last review.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 b)'}},
         'domain_of': ['ManagementReview']} })
    interested_party_changes: Optional[str] = Field(default=None, description="""Changes in interested party requirements.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 c)'}},
         'domain_of': ['ManagementReview']} })
    performance_trends: Optional[str] = Field(default=None, description="""Trends in information security performance.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 d)'}},
         'domain_of': ['ManagementReview']} })
    audit_results_summary: Optional[str] = Field(default=None, description="""Summary of audit results.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 d) 3)'}},
         'domain_of': ['ManagementReview']} })
    risk_assessment_results: Optional[str] = Field(default=None, description="""Results of risk assessment.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 f)'}},
         'domain_of': ['ManagementReview']} })
    improvement_opportunities: Optional[list[str]] = Field(default=None, description="""Opportunities for improvement identified.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.2 g)'}},
         'domain_of': ['ManagementReview']} })
    decisions: Optional[list[str]] = Field(default=None, description="""Decisions made in the review.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.3.3'}},
         'domain_of': ['ManagementReview']} })
    action_items: Optional[list[str]] = Field(default=None, description="""Action items from the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    next_review_date: Optional[date] = Field(default=None, description="""Planned date for next review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 a) identification and description'],
         'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'ISMS-POL-001'}, {'value': 'RA-2024-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.2 c) review and approval'],
         'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'RiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 7.5.3 f) retention and disposition',
                      'Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2'}},
         'comments': ['Captures detection, correction, consequence handling, and '
                      'root-cause data',
                      'Reference: ISO/IEC 27001:2022 Clause 10.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['continual_improvement']})

    nonconformity_source: Optional[str] = Field(default=None, description="""Source of nonconformity detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity'],
         'examples': [{'value': 'internal_audit'},
                      {'value': 'external_audit'},
                      {'value': 'incident'},
                      {'value': 'management_review'}]} })
    detection_date: Optional[date] = Field(default=None, description="""Date the nonconformity was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    detected_by: Optional[str] = Field(default=None, description="""Person or process that detected the nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    requirement_violated: Optional[str] = Field(default=None, description="""Requirement that was not fulfilled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    nonconformity_description: Optional[str] = Field(default=None, description="""Description of the nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    immediate_actions: Optional[list[str]] = Field(default=None, description="""Immediate actions taken to control/correct.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 a) 1)'}},
         'domain_of': ['Nonconformity']} })
    consequences_addressed: Optional[str] = Field(default=None, description="""How consequences were dealt with.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 a) 2)'}},
         'domain_of': ['Nonconformity']} })
    root_cause: Optional[str] = Field(default=None, description="""Root cause of the nonconformity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 b) 2)'}},
         'domain_of': ['Nonconformity', 'InformationSecurityIncident']} })
    similar_nonconformities_check: Optional[str] = Field(default=None, description="""Check for similar nonconformities elsewhere.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 b) 3)'}},
         'domain_of': ['Nonconformity']} })
    linked_corrective_actions: Optional[list[str]] = Field(default=None, description="""Corrective actions addressing this nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    closure_date: Optional[date] = Field(default=None, description="""Date the finding was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding', 'Nonconformity']} })
    closure_evidence: Optional[str] = Field(default=None, description="""Evidence supporting closure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of recurrence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2'}},
         'comments': ['Tracks actions intended to prevent recurrence of '
                      'nonconformities',
                      'Supports effectiveness review and related ISMS change tracking',
                      'Reference: ISO/IEC 27001:2022 Clause 10.2. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['continual_improvement']})

    linked_nonconformity: Optional[str] = Field(default=None, description="""Nonconformity this action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    action_description: Optional[str] = Field(default=None, description="""Description of the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    root_cause_addressed: Optional[str] = Field(default=None, description="""Root cause this action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    target_completion_date: Optional[date] = Field(default=None, description="""Target date for completing the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    actual_completion_date: Optional[date] = Field(default=None, description="""Actual date the action was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction', 'ImprovementOpportunity']} })
    resources_required: Optional[str] = Field(default=None, description="""Resources required for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTreatmentPlan', 'CorrectiveAction']} })
    effectiveness_criteria: Optional[str] = Field(default=None, description="""Criteria for evaluating effectiveness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    effectiveness_review_date: Optional[date] = Field(default=None, description="""Date effectiveness was reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 d)'}},
         'domain_of': ['CorrectiveAction']} })
    effectiveness_verified: Optional[bool] = Field(default=None, description="""Whether effectiveness was verified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    isms_changes_required: Optional[str] = Field(default=None, description="""Changes to ISMS required as a result.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 e)'}},
         'domain_of': ['CorrectiveAction']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.1'}},
         'comments': ['May arise from management reviews, audits, or operational '
                      'experience',
                      'Distinct from corrective actions (proactive vs. reactive)',
                      'Reference: ISO/IEC 27001:2022 Clause 10.1. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['continual_improvement']})

    improvement_source: Optional[str] = Field(default=None, description="""Source of the improvement opportunity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    identification_date: Optional[date] = Field(default=None, description="""Date identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    identified_by: Optional[str] = Field(default=None, description="""Person who identified it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    improvement_description: Optional[str] = Field(default=None, description="""Description of the improvement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    expected_benefit: Optional[str] = Field(default=None, description="""Expected benefit from implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    priority: Optional[str] = Field(default=None, description="""Priority level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    implementation_plan: Optional[str] = Field(default=None, description="""Plan for implementing the improvement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    target_date: Optional[date] = Field(default=None, description="""Target date for achieving the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'ImprovementOpportunity']} })
    actual_completion_date: Optional[date] = Field(default=None, description="""Actual date the action was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction', 'ImprovementOpportunity']} })
    outcome_assessment: Optional[str] = Field(default=None, description="""Assessment of actual outcomes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Asset(NamedEntity):
    """
    An information asset or associated asset requiring protection, per Annex A control 5.9.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control', 'value': '5.9'}},
         'comments': ['Supports asset inventory, ownership, classification, and '
                      'related controls',
                      'Reference: ISO/IEC 27001:2022 Annex A control 5.9; ISO/IEC '
                      '27002:2022 Clause 5.9. ISO/IEC standards text is copyright ISO '
                      '- not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['annex_a_controls']})

    asset_type: Optional[str] = Field(default=None, description="""Type of asset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asset'],
         'examples': [{'value': 'information'},
                      {'value': 'software'},
                      {'value': 'hardware'},
                      {'value': 'service'},
                      {'value': 'personnel'}]} })
    asset_owner: Optional[str] = Field(default=None, description="""Owner of the asset.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control', 'value': '5.9'}},
         'domain_of': ['Asset']} })
    asset_custodian: Optional[str] = Field(default=None, description="""Custodian responsible for day-to-day protection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asset']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'comments': ['Per A.5.12, classification based on confidentiality, integrity, '
                      'availability'],
         'domain_of': ['DocumentedInformation', 'Asset'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    location: Optional[str] = Field(default=None, description="""Physical or logical location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asset']} })
    criticality: Optional[str] = Field(default=None, description="""Criticality rating of the asset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asset']} })
    related_risks: Optional[list[str]] = Field(default=None, description="""Associated risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityObjective', 'Asset']} })
    applicable_controls: Optional[list[str]] = Field(default=None, description="""Controls related to this policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'Asset']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InformationSecurityEvent(NamedEntity):
    """
    An information security event per A.5.25, which may or may not be categorized as an incident.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.25'}},
         'comments': ['Reference: ISO/IEC 27001:2022 Annex A control 5.25; ISO/IEC '
                      '27002:2022 Clause 5.25. ISO/IEC standards text is copyright ISO '
                      '- not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['annex_a_controls']})

    event_datetime: Optional[datetime ] = Field(default=None, description="""Date and time of the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    reporter: Optional[str] = Field(default=None, description="""Person who reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    event_description: Optional[str] = Field(default=None, description="""Description of the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    affected_assets: Optional[list[str]] = Field(default=None, description="""Assets affected by this risk or incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk',
                       'InformationSecurityEvent',
                       'InformationSecurityIncident']} })
    initial_assessment: Optional[str] = Field(default=None, description="""Initial assessment of the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    categorized_as_incident: Optional[bool] = Field(default=None, description="""Whether the event was categorized as an incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    linked_incident: Optional[str] = Field(default=None, description="""Linked incident if categorized.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityEvent']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InformationSecurityIncident(NamedEntity):
    """
    An information security incident per A.5.26, requiring response per documented procedures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.26'}},
         'comments': ['Captures response lifecycle, evidence references, and lessons '
                      'learned',
                      'Reference: ISO/IEC 27001:2022 Annex A control 5.26; ISO/IEC '
                      '27002:2022 Clause 5.26. ISO/IEC standards text is copyright ISO '
                      '- not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['annex_a_controls']})

    incident_datetime: Optional[datetime ] = Field(default=None, description="""Date and time the incident occurred or was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    incident_category: Optional[str] = Field(default=None, description="""Category of incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    severity: Optional[str] = Field(default=None, description="""Severity rating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    affected_assets: Optional[list[str]] = Field(default=None, description="""Assets affected by this risk or incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk',
                       'InformationSecurityEvent',
                       'InformationSecurityIncident']} })
    affected_cia: Optional[list[str]] = Field(default=None, description="""CIA properties affected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    incident_description: Optional[str] = Field(default=None, description="""Description of the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    detection_method: Optional[str] = Field(default=None, description="""How the incident was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    response_actions: Optional[list[str]] = Field(default=None, description="""Actions taken in response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    containment_actions: Optional[list[str]] = Field(default=None, description="""Actions to contain the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    eradication_actions: Optional[list[str]] = Field(default=None, description="""Actions to eradicate the cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    recovery_actions: Optional[list[str]] = Field(default=None, description="""Actions to recover normal operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    root_cause: Optional[str] = Field(default=None, description="""Root cause of the nonconformity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2 b) 2)'}},
         'domain_of': ['Nonconformity', 'InformationSecurityIncident']} })
    lessons_learned: Optional[str] = Field(default=None, description="""Lessons learned from the incident.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.27'}},
         'domain_of': ['InformationSecurityIncident']} })
    evidence_collected: Optional[list[str]] = Field(default=None, description="""Evidence collected.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.28'}},
         'domain_of': ['InformationSecurityIncident']} })
    notification_required: Optional[bool] = Field(default=None, description="""Whether notification to authorities/parties was required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    notifications_made: Optional[list[str]] = Field(default=None, description="""Notifications that were made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    closure_datetime: Optional[datetime ] = Field(default=None, description="""Date and time of incident closure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    post_incident_review: Optional[str] = Field(default=None, description="""Post-incident review findings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationSecurityIncident']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'comments': ['Should use consistent URI/CURIE format across the dataset'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso27001:risk-001'},
                      {'value': 'iso27001:control-5.1'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Supports document control requirements per 7.5.3 e)'],
         'domain_of': ['NamedEntity'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
DocumentedInformation.model_rebuild()
InformationSecurityManagementSystem.model_rebuild()
Organization.model_rebuild()
InterestedParty.model_rebuild()
InformationSecurityPolicy.model_rebuild()
TopicSpecificPolicy.model_rebuild()
Role.model_rebuild()
InformationSecurityObjective.model_rebuild()
RiskAssessmentProcess.model_rebuild()
RiskAssessment.model_rebuild()
Risk.model_rebuild()
RiskTreatmentProcess.model_rebuild()
RiskTreatmentPlan.model_rebuild()
StatementOfApplicability.model_rebuild()
SoAEntry.model_rebuild()
SecurityControl.model_rebuild()
Resource.model_rebuild()
CompetenceRecord.model_rebuild()
AwarenessProgram.model_rebuild()
CommunicationPlan.model_rebuild()
CommunicationItem.model_rebuild()
OperationalProcedure.model_rebuild()
MonitoringProgram.model_rebuild()
MonitoringItem.model_rebuild()
InternalAudit.model_rebuild()
AuditProgramme.model_rebuild()
AuditFinding.model_rebuild()
ManagementReview.model_rebuild()
Nonconformity.model_rebuild()
CorrectiveAction.model_rebuild()
ImprovementOpportunity.model_rebuild()
Asset.model_rebuild()
InformationSecurityEvent.model_rebuild()
InformationSecurityIncident.model_rebuild()
