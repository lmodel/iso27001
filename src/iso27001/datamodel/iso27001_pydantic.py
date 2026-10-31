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


metamodel_version = "1.12.0"
version = "2022/Amd 1:2024"


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


linkml_meta = LinkMLMeta({'annotations': {'amendment': {'tag': 'amendment',
                                   'value': 'ISO/IEC 27001:2022/Amd 1:2024'},
                     'amendment_publication_date': {'tag': 'amendment_publication_date',
                                                    'value': '2024-02-23'},
                     'edition': {'tag': 'edition', 'value': '3'},
                     'iso_open_data_date': {'tag': 'iso_open_data_date',
                                            'value': '2026-10-28'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2022-10-25'},
                     'standard': {'tag': 'standard', 'value': 'ISO/IEC 27001:2022'},
                     'terms_reference': {'tag': 'terms_reference',
                                         'value': 'ISO/IEC 27000:2026'}},
     'comments': ['The version is the edition the schema models, 2022, with its '
                  "one amendment, Amd 1:2024, and source is ISO's page for that "
                  "edition. ISO Open Data's records of both, and of ISO/IEC "
                  '27002:2022 and ISO/IEC 27000:2026, are copied to '
                  'src/iso27001/schema/iso-open-data/ as of the date in the '
                  'annotations. scripts/check_upstream_release.py reports when ISO '
                  'publishes another supplement or edition. The release tags are '
                  "the schema's own versions.",
                  'ISO/IEC 27001 is copyright ISO and IEC, and none of its text is '
                  'reproduced here. Each element cites the clause or Annex A '
                  'control it models by number, in the iso27001_clause or '
                  'annex_a_control annotation, and its description is this '
                  "project's own words. A licence holder can merge the standard's "
                  'wording into a private copy with the overlay that '
                  'src/iso27001/schema/OVERLAY.md describes.',
                  'The terms follow ISO/IEC 27000, which ISO/IEC 27001 refers to '
                  'for them. On the pinned date its current edition is ISO/IEC '
                  "27000:2026, which ISO's record titles an overview, where every "
                  'earlier edition was an overview and vocabulary. Whether that '
                  'edition still defines the terms has not been checked against '
                  'its text.',
                  'Every record that other records refer to has an isms_id, and a '
                  'reference holds that identifier. IsmsManagementSystem holds '
                  'each kind of record in a list of its own.',
                  'The mappings name terms of the released lmodel/oscal, '
                  'lmodel/spdx and lmodel/nist-sp-800-53 schemas, and come from '
                  'the SSSOM files in src/iso27001/mappings/.'],
     'default_prefix': 'iso27001',
     'default_range': 'string',
     'description': 'A LinkML model of the records an organization keeps to run an '
                    'information security management system (ISMS) to ISO/IEC '
                    '27001:2022 with Amendment 1:2024. The records cover the '
                    "ISMS's context and scope, policies, roles and objectives, "
                    'risks and their treatment, and its controls and Statement of '
                    'Applicability. They also cover the support and operation it '
                    'needs, its audits and management reviews, and its '
                    'nonconformities, corrective actions and improvements. The 93 '
                    'reference controls of Annex A appear by their numbers alone.',
     'id': 'https://w3id.org/lmodel/iso27001',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'iso27001',
     'prefixes': {'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx_core': {'prefix_prefix': 'spdx_core',
                                'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Core/'},
                  'spdx_software': {'prefix_prefix': 'spdx_software',
                                    'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Software/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/iso27001',
                  'https://www.iso.org/standard/82875.html',
                  'https://www.iso.org/standard/88435.html'],
     'source': 'https://www.iso.org/standard/82875.html',
     'source_file': 'src/iso27001/schema/iso27001.yaml',
     'subsets': {'isms_annex_a': {'description': 'The Annex A reference controls, '
                                                 "the organization's controls and "
                                                 'the Statement of Applicability, '
                                                 'and the records Annex A controls '
                                                 'call for.',
                                  'from_schema': 'https://w3id.org/lmodel/iso27001',
                                  'name': 'isms_annex_a'},
                 'isms_core': {'description': "The records of the ISMS's context, "
                                              'leadership, planning and support '
                                              '(clauses 4 to 7).',
                               'from_schema': 'https://w3id.org/lmodel/iso27001',
                               'name': 'isms_core'},
                 'isms_documented_information': {'description': 'The records that '
                                                                'are documented '
                                                                'information under '
                                                                'document control '
                                                                '(clause 7.5).',
                                                 'from_schema': 'https://w3id.org/lmodel/iso27001',
                                                 'name': 'isms_documented_information'},
                 'isms_improvement': {'description': 'The records of continual '
                                                     'improvement, nonconformity '
                                                     'and corrective action '
                                                     '(clause 10).',
                                      'from_schema': 'https://w3id.org/lmodel/iso27001',
                                      'name': 'isms_improvement'},
                 'isms_performance_evaluation': {'description': 'The records of '
                                                                'monitoring, '
                                                                'internal audit '
                                                                'and management '
                                                                'review (clause '
                                                                '9).',
                                                 'from_schema': 'https://w3id.org/lmodel/iso27001',
                                                 'name': 'isms_performance_evaluation'},
                 'isms_risk_management': {'description': 'The records of risk '
                                                         'assessment and risk '
                                                         'treatment (clauses '
                                                         '6.1.2, 6.1.3, 8.2 and '
                                                         '8.3).',
                                          'from_schema': 'https://w3id.org/lmodel/iso27001',
                                          'name': 'isms_risk_management'}},
     'title': 'ISO/IEC 27001:2022 information security management system records',
     'types': {'isms_duration': {'base': 'str',
                                 'description': 'A length of time as ISO 8601 '
                                                'writes it, such as P7Y for seven '
                                                'years or P30D for thirty days.',
                                 'from_schema': 'https://w3id.org/lmodel/iso27001',
                                 'name': 'isms_duration',
                                 'pattern': '^P(?=[0-9T])([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T(?=[0-9])([0-9]+H)?([0-9]+M)?([0-9]+S)?)?$',
                                 'typeof': 'string',
                                 'uri': 'xsd:duration'},
               'isms_requirement_reference': {'base': 'str',
                                              'description': 'The number of a '
                                                             'clause of ISO/IEC '
                                                             '27001:2022, from 4 '
                                                             'to 10, such as '
                                                             '6.1.2, or of an '
                                                             'Annex A control, '
                                                             'such as A.5.9.',
                                              'from_schema': 'https://w3id.org/lmodel/iso27001',
                                              'name': 'isms_requirement_reference',
                                              'pattern': '^(([4-9]|10)(\\.[0-9]{1,2}){0,2}|A\\.[5-8]\\.[0-9]{1,2})$',
                                              'typeof': 'string',
                                              'uri': 'xsd:string'}}} )

class IsmsControlTheme(str, Enum):
    """
    The four themes Annex A sorts its controls into, which ISO/IEC 27002:2022 also uses.
    """
    organizational = "organizational"
    """
    The organizational controls, numbered A.5.1 to A.5.37.
    """
    people = "people"
    """
    The people controls, numbered A.6.1 to A.6.8.
    """
    physical = "physical"
    """
    The physical controls, numbered A.7.1 to A.7.14.
    """
    technological = "technological"
    """
    The technological controls, numbered A.8.1 to A.8.34.
    """


class IsmsAnnexAControl(str, Enum):
    """
    The 93 reference controls of Annex A, by their numbers. The values carry no titles: the titles and the control text are ISO's.
    """
    AFULL_STOP5FULL_STOP1 = "a_5_1"
    AFULL_STOP5FULL_STOP2 = "a_5_2"
    AFULL_STOP5FULL_STOP3 = "a_5_3"
    AFULL_STOP5FULL_STOP4 = "a_5_4"
    AFULL_STOP5FULL_STOP5 = "a_5_5"
    AFULL_STOP5FULL_STOP6 = "a_5_6"
    AFULL_STOP5FULL_STOP7 = "a_5_7"
    AFULL_STOP5FULL_STOP8 = "a_5_8"
    AFULL_STOP5FULL_STOP9 = "a_5_9"
    AFULL_STOP5FULL_STOP10 = "a_5_10"
    AFULL_STOP5FULL_STOP11 = "a_5_11"
    AFULL_STOP5FULL_STOP12 = "a_5_12"
    AFULL_STOP5FULL_STOP13 = "a_5_13"
    AFULL_STOP5FULL_STOP14 = "a_5_14"
    AFULL_STOP5FULL_STOP15 = "a_5_15"
    AFULL_STOP5FULL_STOP16 = "a_5_16"
    AFULL_STOP5FULL_STOP17 = "a_5_17"
    AFULL_STOP5FULL_STOP18 = "a_5_18"
    AFULL_STOP5FULL_STOP19 = "a_5_19"
    AFULL_STOP5FULL_STOP20 = "a_5_20"
    AFULL_STOP5FULL_STOP21 = "a_5_21"
    AFULL_STOP5FULL_STOP22 = "a_5_22"
    AFULL_STOP5FULL_STOP23 = "a_5_23"
    AFULL_STOP5FULL_STOP24 = "a_5_24"
    AFULL_STOP5FULL_STOP25 = "a_5_25"
    AFULL_STOP5FULL_STOP26 = "a_5_26"
    AFULL_STOP5FULL_STOP27 = "a_5_27"
    AFULL_STOP5FULL_STOP28 = "a_5_28"
    AFULL_STOP5FULL_STOP29 = "a_5_29"
    AFULL_STOP5FULL_STOP30 = "a_5_30"
    AFULL_STOP5FULL_STOP31 = "a_5_31"
    AFULL_STOP5FULL_STOP32 = "a_5_32"
    AFULL_STOP5FULL_STOP33 = "a_5_33"
    AFULL_STOP5FULL_STOP34 = "a_5_34"
    AFULL_STOP5FULL_STOP35 = "a_5_35"
    AFULL_STOP5FULL_STOP36 = "a_5_36"
    AFULL_STOP5FULL_STOP37 = "a_5_37"
    AFULL_STOP6FULL_STOP1 = "a_6_1"
    AFULL_STOP6FULL_STOP2 = "a_6_2"
    AFULL_STOP6FULL_STOP3 = "a_6_3"
    AFULL_STOP6FULL_STOP4 = "a_6_4"
    AFULL_STOP6FULL_STOP5 = "a_6_5"
    AFULL_STOP6FULL_STOP6 = "a_6_6"
    AFULL_STOP6FULL_STOP7 = "a_6_7"
    AFULL_STOP6FULL_STOP8 = "a_6_8"
    AFULL_STOP7FULL_STOP1 = "a_7_1"
    AFULL_STOP7FULL_STOP2 = "a_7_2"
    AFULL_STOP7FULL_STOP3 = "a_7_3"
    AFULL_STOP7FULL_STOP4 = "a_7_4"
    AFULL_STOP7FULL_STOP5 = "a_7_5"
    AFULL_STOP7FULL_STOP6 = "a_7_6"
    AFULL_STOP7FULL_STOP7 = "a_7_7"
    AFULL_STOP7FULL_STOP8 = "a_7_8"
    AFULL_STOP7FULL_STOP9 = "a_7_9"
    AFULL_STOP7FULL_STOP10 = "a_7_10"
    AFULL_STOP7FULL_STOP11 = "a_7_11"
    AFULL_STOP7FULL_STOP12 = "a_7_12"
    AFULL_STOP7FULL_STOP13 = "a_7_13"
    AFULL_STOP7FULL_STOP14 = "a_7_14"
    AFULL_STOP8FULL_STOP1 = "a_8_1"
    AFULL_STOP8FULL_STOP2 = "a_8_2"
    AFULL_STOP8FULL_STOP3 = "a_8_3"
    AFULL_STOP8FULL_STOP4 = "a_8_4"
    AFULL_STOP8FULL_STOP5 = "a_8_5"
    AFULL_STOP8FULL_STOP6 = "a_8_6"
    AFULL_STOP8FULL_STOP7 = "a_8_7"
    AFULL_STOP8FULL_STOP8 = "a_8_8"
    AFULL_STOP8FULL_STOP9 = "a_8_9"
    AFULL_STOP8FULL_STOP10 = "a_8_10"
    AFULL_STOP8FULL_STOP11 = "a_8_11"
    AFULL_STOP8FULL_STOP12 = "a_8_12"
    AFULL_STOP8FULL_STOP13 = "a_8_13"
    AFULL_STOP8FULL_STOP14 = "a_8_14"
    AFULL_STOP8FULL_STOP15 = "a_8_15"
    AFULL_STOP8FULL_STOP16 = "a_8_16"
    AFULL_STOP8FULL_STOP17 = "a_8_17"
    AFULL_STOP8FULL_STOP18 = "a_8_18"
    AFULL_STOP8FULL_STOP19 = "a_8_19"
    AFULL_STOP8FULL_STOP20 = "a_8_20"
    AFULL_STOP8FULL_STOP21 = "a_8_21"
    AFULL_STOP8FULL_STOP22 = "a_8_22"
    AFULL_STOP8FULL_STOP23 = "a_8_23"
    AFULL_STOP8FULL_STOP24 = "a_8_24"
    AFULL_STOP8FULL_STOP25 = "a_8_25"
    AFULL_STOP8FULL_STOP26 = "a_8_26"
    AFULL_STOP8FULL_STOP27 = "a_8_27"
    AFULL_STOP8FULL_STOP28 = "a_8_28"
    AFULL_STOP8FULL_STOP29 = "a_8_29"
    AFULL_STOP8FULL_STOP30 = "a_8_30"
    AFULL_STOP8FULL_STOP31 = "a_8_31"
    AFULL_STOP8FULL_STOP32 = "a_8_32"
    AFULL_STOP8FULL_STOP33 = "a_8_33"
    AFULL_STOP8FULL_STOP34 = "a_8_34"


class IsmsImplementationStatus(str, Enum):
    """
    How far a control or a plan has been put into effect.
    """
    not_started = "not_started"
    """
    Nothing has been done yet.
    """
    planned = "planned"
    """
    The work is planned, with a timeline.
    """
    in_progress = "in_progress"
    """
    The work is under way.
    """
    implemented = "implemented"
    """
    The work is done and in operation.
    """


class IsmsRiskTreatmentOption(str, Enum):
    """
    The ways of treating a risk, by the names ISO/IEC 27005 gives them.
    """
    modify = "modify"
    """
    Change the risk with controls that lower its likelihood or its consequences.
    """
    retain = "retain"
    """
    Keep the risk as it is, with the risk owner's approval.
    """
    avoid = "avoid"
    """
    Remove the risk by stopping or changing what gives rise to it.
    """
    share = "share"
    """
    Share the risk with another party, such as an insurer or a supplier.
    """


class IsmsRiskLevel(str, Enum):
    """
    A five-point scale of risk level, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
    """
    very_low = "very_low"
    """
    Small enough to need no action.
    """
    low = "low"
    """
    Managed by routine procedures.
    """
    medium = "medium"
    """
    Needs management's attention and planned controls.
    """
    high = "high"
    """
    Needs treatment first and escalation.
    """
    critical = "critical"
    """
    Threatens the organization's objectives and needs action at once.
    """


class IsmsLikelihood(str, Enum):
    """
    A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
    """
    rare = "rare"
    """
    Not expected to happen.
    """
    unlikely = "unlikely"
    """
    Could happen, but is not expected to.
    """
    possible = "possible"
    """
    Might happen at some point.
    """
    likely = "likely"
    """
    Will probably happen.
    """
    almost_certain = "almost_certain"
    """
    Expected to happen.
    """


class IsmsImpact(str, Enum):
    """
    A five-point scale of consequence, for an organization that adopts it. ISO/IEC 27001 leaves the scale to the organization.
    """
    negligible = "negligible"
    """
    No noticeable effect on operations or objectives.
    """
    minor = "minor"
    """
    An effect normal operations absorb.
    """
    moderate = "moderate"
    """
    An effect that needs management to step in.
    """
    major = "major"
    """
    A serious effect on objectives, reputation or compliance.
    """
    severe = "severe"
    """
    An effect that threatens the organization's survival.
    """


class IsmsSecurityProperty(str, Enum):
    """
    The three properties of information that information security preserves, as ISO/IEC 27000 names them.
    """
    confidentiality = "confidentiality"
    """
    Only those allowed to see the information can see it.
    """
    integrity = "integrity"
    """
    The information is accurate and complete.
    """
    availability = "availability"
    """
    Those allowed to use the information can use it when they need it.
    """


class IsmsDocumentKind(str, Enum):
    """
    The kinds of documented information an IsmsDocumentedInformation record holds. Policies have records of their own.
    """
    procedure = "procedure"
    """
    The steps for carrying out an activity the same way each time.
    """
    standard = "standard"
    """
    Mandatory requirements for a technology or a process.
    """
    guideline = "guideline"
    """
    Recommended practice that supports a policy or a procedure.
    """
    record = "record"
    """
    Evidence of what was done or achieved.
    """
    plan = "plan"
    """
    How the organization means to reach an objective.
    """
    report = "report"
    """
    The formal output of an assessment, audit or review.
    """


class IsmsAuditType(str, Enum):
    """
    Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
    """
    first_party = "first_party"
    """
    The organization audits itself; an internal audit.
    """
    second_party = "second_party"
    """
    A party with an interest in the organization audits it, such as a customer.
    """
    third_party = "third_party"
    """
    An independent body audits it, such as a certification body or a regulator.
    """


class IsmsAuditFindingType(str, Enum):
    """
    The kinds of audit finding.
    """
    major_nonconformity = "major_nonconformity"
    """
    A requirement not met in a way that puts the ISMS's intended results in doubt.
    """
    minor_nonconformity = "minor_nonconformity"
    """
    A requirement not met in an isolated way that leaves the ISMS's intended results in reach.
    """
    observation = "observation"
    """
    A condition that could lead to a nonconformity if left alone.
    """
    positive_finding = "positive_finding"
    """
    Evidence of practice that works well.
    """


class IsmsIncidentCategory(str, Enum):
    """
    Kinds of information security incident, for sorting incidents. ISO/IEC 27001 sets no list of its own.
    """
    malware = "malware"
    """
    Malicious software, such as a virus, a worm or a trojan.
    """
    ransomware = "ransomware"
    """
    Malware that encrypts or takes data to extort money.
    """
    phishing = "phishing"
    """
    A message that tries to trick someone into giving up credentials or acting.
    """
    social_engineering = "social_engineering"
    """
    Manipulating people into disclosing information or acting unsafely.
    """
    unauthorized_access = "unauthorized_access"
    """
    Access to systems or data by someone not allowed it.
    """
    account_compromise = "account_compromise"
    """
    Someone else taking control of a legitimate account.
    """
    privilege_misuse = "privilege_misuse"
    """
    An authorized user going beyond or misusing their privileges.
    """
    data_breach = "data_breach"
    """
    Confidential or personal information disclosed.
    """
    data_loss = "data_loss"
    """
    Information lost or corrupted, by accident or otherwise.
    """
    denial_of_service = "denial_of_service"
    """
    Systems made unavailable by flooding or attack.
    """
    web_application_attack = "web_application_attack"
    """
    An attack on a web application, such as an injection.
    """
    supply_chain = "supply_chain"
    """
    An incident that starts at a supplier, a partner or a third-party component.
    """
    insider_threat = "insider_threat"
    """
    Harm done by someone inside the organization, on purpose or by neglect.
    """
    physical_security = "physical_security"
    """
    Theft, loss or damage of physical assets, or physical access without permission.
    """
    configuration_error = "configuration_error"
    """
    A misconfiguration that exposes something.
    """
    cryptographic_failure = "cryptographic_failure"
    """
    Cryptography that is weak, broken or misused.
    """
    policy_violation = "policy_violation"
    """
    A breach of the organization's security policies or procedures.
    """
    other = "other"
    """
    Any incident the other categories do not fit.
    """


class IsmsManagementSystemStandard(str, Enum):
    """
    Management system standards an ISMS may be integrated with or audited beside, each written to ISO's harmonized structure.
    """
    iso_iec_27001 = "iso_iec_27001"
    """
    Information security management systems.
    """
    iso_iec_27701 = "iso_iec_27701"
    """
    Privacy information management systems.
    """
    iso_iec_42001 = "iso_iec_42001"
    """
    Artificial intelligence management systems.
    """
    iso_9001 = "iso_9001"
    """
    Quality management systems.
    """
    iso_14001 = "iso_14001"
    """
    Environmental management systems.
    """
    iso_22301 = "iso_22301"
    """
    Business continuity management systems.
    """
    iso_iec_20000_1 = "iso_iec_20000_1"
    """
    Service management systems.
    """



class IsmsRecordMixin(ConfiguredBaseModel):
    """
    What every record of the ISMS has, so that other records can refer to it: an identifier, a title and a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['It is a mixin, not a base class, so that the adapt copy can '
                      "re-root some record classes on LOKF's Concept and leave the "
                      "others as they are. lokf adapt replaces isms_id with LOKF's id, "
                      'and a class that declares id itself must descend from Concept.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'mixin': True,
         'slot_usage': {'title': {'name': 'title',
                                  'pattern': '^\\s*\\S',
                                  'required': True}}})

    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsDocumentControlMixin(ConfiguredBaseModel):
    """
    The control that documented information is kept under. It records who wrote, owns and approved the information, when it takes effect and is reviewed, and how it is classified, distributed, stored and changed. It also records how long it is retained, and whether it came from outside the organization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_documented_information'],
         'mixin': True})

    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })


class IsmsManagementSystem(IsmsRecordMixin):
    """
    One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin'],
         'related_mappings': ['oscal:SystemSecurityPlan'],
         'tree_root': True})

    isms_organization: Optional[IsmsOrganization] = Field(default=None, description="""The organization that runs the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_top_management: Optional[str] = Field(default=None, description="""The person or group that directs and controls the organization at the highest level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_governing_body: Optional[str] = Field(default=None, description="""The body top management answers to, such as a board, where there is one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_leadership_evidence: Optional[list[str]] = Field(default=None, description="""What shows that top management leads and commits to the ISMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.1'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_scope: Optional[str] = Field(default=None, description="""The scope of the ISMS, as the organization states it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.3'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_scope_boundaries: Optional[list[str]] = Field(default=None, description="""Where the scope of the ISMS ends.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.3'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_scope_exclusions: Optional[list[str]] = Field(default=None, description="""What the scope leaves out, each with the reason.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.3'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_interfaces: Optional[list[str]] = Field(default=None, description="""The interfaces and dependencies between what the organization does and what other organizations do, which the scope takes into account.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.3'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_processes: Optional[str] = Field(default=None, description="""The processes the ISMS needs and how they interact.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.4'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_internal_issues: Optional[list[str]] = Field(default=None, description="""The internal issues that bear on the ISMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_external_issues: Optional[list[str]] = Field(default=None, description="""The external issues that bear on the ISMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_risk_and_opportunity_actions: Optional[list[str]] = Field(default=None, description="""The actions planned to address the ISMS's risks and opportunities, and how they fit into its processes.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.1'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_planned_changes: Optional[list[str]] = Field(default=None, description="""The changes to the ISMS that are planned.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '6.3'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_external_services: Optional[list[str]] = Field(default=None, description="""The processes, products or services from outside the organization that the ISMS relies on and controls.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '8.1'}},
         'domain_of': ['IsmsManagementSystem']} })
    isms_certification_status: Optional[str] = Field(default=None, description="""Where the ISMS stands with certification, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_certification_body: Optional[str] = Field(default=None, description="""The body that certifies the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_certification_date: Optional[date] = Field(default=None, description="""When the ISMS was certified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_recertification_date: Optional[date] = Field(default=None, description="""When the ISMS is next due for recertification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_interested_parties: Optional[list[IsmsInterestedParty]] = Field(default=None, description="""The interested parties the ISMS takes into account.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_policy: Optional[IsmsPolicy] = Field(default=None, description="""The information security policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_topic_specific_policies: Optional[list[IsmsTopicSpecificPolicy]] = Field(default=None, description="""The topic-specific policies under the information security policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_roles: Optional[list[IsmsRole]] = Field(default=None, description="""The roles that carry the ISMS's responsibilities and authorities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_objectives: Optional[list[IsmsObjective]] = Field(default=None, description="""The information security objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_risk_assessment_process: Optional[IsmsRiskAssessmentProcess] = Field(default=None, description="""The information security risk assessment process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_risk_treatment_process: Optional[IsmsRiskTreatmentProcess] = Field(default=None, description="""The information security risk treatment process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_risk_assessments: Optional[list[IsmsRiskAssessment]] = Field(default=None, description="""The risk assessments carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_risks: Optional[list[IsmsRisk]] = Field(default=None, description="""The risks identified, the risk register.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_risk_treatment_plans: Optional[list[IsmsRiskTreatmentPlan]] = Field(default=None, description="""The risk treatment plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_statement_of_applicability: Optional[IsmsStatementOfApplicability] = Field(default=None, description="""The Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_controls: Optional[list[IsmsControl]] = Field(default=None, description="""The controls the organization has determined it needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_assets: Optional[list[IsmsAsset]] = Field(default=None, description="""The inventory of information and other associated assets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_resources: Optional[list[IsmsResource]] = Field(default=None, description="""The resources provided for the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_competence_records: Optional[list[IsmsCompetenceRecord]] = Field(default=None, description="""The records of competence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_awareness_programme: Optional[IsmsAwarenessProgramme] = Field(default=None, description="""The awareness programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_communication_plan: Optional[IsmsCommunicationPlan] = Field(default=None, description="""The plan for communication about the ISMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_documented_information: Optional[list[IsmsDocumentedInformation]] = Field(default=None, description="""The documented information the ISMS keeps that no more specific list holds, such as procedures, plans and reports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_operational_procedures: Optional[list[IsmsOperationalProcedure]] = Field(default=None, description="""The procedures for operational planning and control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_monitoring_programme: Optional[IsmsMonitoringProgramme] = Field(default=None, description="""The programme of monitoring and measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_audit_programmes: Optional[list[IsmsAuditProgramme]] = Field(default=None, description="""The audit programmes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_audits: Optional[list[IsmsAudit]] = Field(default=None, description="""The audits of the ISMS, internal and external.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_management_reviews: Optional[list[IsmsManagementReview]] = Field(default=None, description="""The management reviews.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_nonconformities: Optional[list[IsmsNonconformity]] = Field(default=None, description="""The nonconformities found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_corrective_actions: Optional[list[IsmsCorrectiveAction]] = Field(default=None, description="""The corrective actions taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_improvements: Optional[list[IsmsImprovementOpportunity]] = Field(default=None, description="""The opportunities for improvement identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_security_events: Optional[list[Union[IsmsSecurityEvent,IsmsSecurityIncident]]] = Field(default=None, description="""The information security events reported, the incidents among them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementSystem']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsOrganization(IsmsRecordMixin):
    """
    The organization that runs the ISMS, with what it needs to know about itself to understand its context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'broad_mappings': ['oscal:Party'],
         'close_mappings': ['spdx_core:Organization'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin']})

    organization_legal_name: Optional[str] = Field(default=None, description="""The organization's registered legal name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_trading_names: Optional[list[str]] = Field(default=None, description="""Other names the organization trades under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_kind: Optional[str] = Field(default=None, description="""What kind of organization it is, such as a company, an agency or a charity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_sector: Optional[str] = Field(default=None, description="""The organization's main industry sector.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_size: Optional[str] = Field(default=None, description="""How the organization classes its own size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_employee_count: Optional[int] = Field(default=None, description="""About how many people the organization employs.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_locations: Optional[list[str]] = Field(default=None, description="""The countries or regions the organization works in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_jurisdictions: Optional[list[str]] = Field(default=None, description="""The jurisdictions whose laws and regulations apply to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_parent: Optional[str] = Field(default=None, description="""The organization's parent, if it has one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_subsidiaries: Optional[list[str]] = Field(default=None, description="""The organization's subsidiaries, if it has any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOrganization']} })
    organization_climate_change_relevant: Optional[bool] = Field(default=None, description="""Whether the organization has determined that climate change is a relevant issue for its ISMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_amendment': {'tag': 'iso27001_amendment',
                                                'value': 'ISO/IEC 27001:2022/Amd '
                                                         '1:2024'},
                         'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.1'}},
         'domain_of': ['IsmsOrganization']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsInterestedParty(IsmsRecordMixin):
    """
    A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin']})

    party_category: Optional[str] = Field(default=None, description="""What kind of interested party it is, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    party_relationship: Optional[str] = Field(default=None, description="""How the party relates to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    party_requirements: Optional[list[str]] = Field(default=None, description="""The party's requirements that bear on information security.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    party_addressed_requirements: Optional[list[str]] = Field(default=None, description="""Which of those requirements the ISMS addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    party_climate_change_requirements: Optional[list[str]] = Field(default=None, description="""The party's requirements that concern climate change.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso27001_amendment': {'tag': 'iso27001_amendment',
                                                'value': 'ISO/IEC 27001:2022/Amd '
                                                         '1:2024'},
                         'iso27001_clause': {'tag': 'iso27001_clause', 'value': '4.2'}},
         'domain_of': ['IsmsInterestedParty']} })
    party_communication_needs: Optional[str] = Field(default=None, description="""What the party needs to be told, and how.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    party_contact: Optional[str] = Field(default=None, description="""How to reach the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsInterestedParty']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsPolicy(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The information security policy that top management sets: the organization's commitment and the frame for its information security objectives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    policy_statement: Optional[str] = Field(default=None, description="""The policy's own statement, in the organization's words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_objectives_framework: Optional[str] = Field(default=None, description="""How the policy frames the setting of information security objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_commitments: Optional[list[str]] = Field(default=None, description="""The commitments the policy makes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_applicability: Optional[str] = Field(default=None, description="""To whom and to what the policy applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_communication_date: Optional[date] = Field(default=None, description="""When the policy was communicated within the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_acknowledgement_required: Optional[bool] = Field(default=None, description="""Whether staff must acknowledge the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    policy_management_systems: Optional[list[IsmsManagementSystemStandard]] = Field(default=None, description="""The other management system standards the ISMS is integrated with under the same policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsPolicy']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsTopicSpecificPolicy(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    A policy on one topic of information security, such as access control or backup, that supports the information security policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control', 'value': '5.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy',
                       'IsmsObjective',
                       'IsmsControl',
                       'IsmsAsset',
                       'IsmsOperationalProcedure']} })
    topic_policy_topic: Optional[str] = Field(default=None, description="""The topic the policy covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy']} })
    topic_policy_parent: Optional[str] = Field(default=None, description="""The information security policy this policy supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy']} })
    topic_policy_audience: Optional[str] = Field(default=None, description="""Whom the policy is written for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRole(IsmsRecordMixin):
    """
    A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '5.3'}},
         'close_mappings': ['oscal:Role'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin']})

    role_category: Optional[str] = Field(default=None, description="""What kind of role it is, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_responsibilities: Optional[list[str]] = Field(default=None, description="""The responsibilities assigned to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_authorities: Optional[list[str]] = Field(default=None, description="""The authorities the role carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_accountability: Optional[str] = Field(default=None, description="""What the role is accountable for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_holders: Optional[list[str]] = Field(default=None, description="""The people who hold the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_delegation: Optional[str] = Field(default=None, description="""How the role may delegate its responsibilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    role_reports_to: Optional[str] = Field(default=None, description="""The role this role reports to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRole']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsObjective(IsmsRecordMixin):
    """
    An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '6.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin']})

    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy',
                       'IsmsObjective',
                       'IsmsControl',
                       'IsmsAsset',
                       'IsmsOperationalProcedure']} })
    objective_statement: Optional[str] = Field(default=None, description="""The objective, as the organization states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_target: Optional[str] = Field(default=None, description="""The value the objective aims for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_current_value: Optional[str] = Field(default=None, description="""The value last measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_metric: Optional[str] = Field(default=None, description="""How the objective's value is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_measurement_method: Optional[str] = Field(default=None, description="""How the value is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_measurement_frequency: Optional[str] = Field(default=None, description="""How often the value is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_target_date: Optional[date] = Field(default=None, description="""When the objective is to be reached.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_achievement: Optional[str] = Field(default=None, description="""How far the objective has been reached, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_risks: Optional[list[str]] = Field(default=None, description="""The risks the objective concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_action_plan: Optional[str] = Field(default=None, description="""What will be done to reach the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    objective_resources: Optional[str] = Field(default=None, description="""The resources needed to reach the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRiskAssessmentProcess(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_risk_management', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    risk_acceptance_criteria: Optional[str] = Field(default=None, description="""The criteria for accepting a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_assessment_criteria: Optional[str] = Field(default=None, description="""The criteria for carrying out a risk assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_assessment_method: Optional[str] = Field(default=None, description="""The method used to identify, analyse and evaluate risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_likelihood_scale: Optional[str] = Field(default=None, description="""The scale for rating likelihood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_impact_scale: Optional[str] = Field(default=None, description="""The scale for rating consequences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_matrix: Optional[str] = Field(default=None, description="""How likelihood and consequence combine into a risk level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_assessment_frequency: Optional[str] = Field(default=None, description="""How often risks are assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    risk_assessment_triggers: Optional[list[str]] = Field(default=None, description="""The events that start a risk assessment outside the planned ones.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessmentProcess']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRiskAssessment(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    One risk assessment carried out under the risk assessment process, and what it found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '8.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_risk_management'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    assessment_scope: Optional[str] = Field(default=None, description="""What the assessment covered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_date: Optional[date] = Field(default=None, description="""When the assessment was carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_assessor: Optional[str] = Field(default=None, description="""Who carried out the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_method_used: Optional[str] = Field(default=None, description="""The method this assessment applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_risks: Optional[list[str]] = Field(default=None, description="""The risks the assessment identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_summary: Optional[str] = Field(default=None, description="""A summary of what the assessment found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_recommendations: Optional[list[str]] = Field(default=None, description="""What the assessment recommends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    assessment_next_date: Optional[date] = Field(default=None, description="""When the next assessment is planned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskAssessment']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRisk(IsmsRecordMixin):
    """
    An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_risk_management'],
         'mixins': ['IsmsRecordMixin']})

    affected_assets: Optional[list[str]] = Field(default=None, description="""The assets the risk, event or incident affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk', 'IsmsSecurityEvent']} })
    affected_security_properties: Optional[list[IsmsSecurityProperty]] = Field(default=None, description="""Which of confidentiality, integrity and availability the risk or incident threatens.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk', 'IsmsSecurityIncident']} })
    risk_source: Optional[str] = Field(default=None, description="""Where the risk comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_threat: Optional[str] = Field(default=None, description="""The threat that could cause harm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_vulnerability: Optional[str] = Field(default=None, description="""The weakness the threat could exploit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_owner: Optional[str] = Field(default=None, description="""The person who is accountable for the risk and has the authority to manage it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_likelihood: Optional[IsmsLikelihood] = Field(default=None, description="""How likely the risk is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_impact: Optional[IsmsImpact] = Field(default=None, description="""How severe the consequences would be.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_inherent_level: Optional[IsmsRiskLevel] = Field(default=None, description="""The risk's level before controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_existing_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls already acting on the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_residual_level: Optional[IsmsRiskLevel] = Field(default=None, description="""The risk's level after controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_treatment_option: Optional[IsmsRiskTreatmentOption] = Field(default=None, description="""The treatment chosen for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    risk_treatment_priority: Optional[str] = Field(default=None, description="""How soon the risk is to be treated, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRiskTreatmentProcess(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_risk_management', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    treatment_options_guidance: Optional[str] = Field(default=None, description="""How a treatment option is chosen for a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentProcess']} })
    treatment_control_selection: Optional[str] = Field(default=None, description="""How the controls a treatment needs are chosen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentProcess']} })
    treatment_annex_a_comparison: Optional[str] = Field(default=None, description="""How the chosen controls are compared with Annex A, so that no necessary control is left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentProcess']} })
    treatment_soa_template: Optional[str] = Field(default=None, description="""The template the Statement of Applicability follows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentProcess']} })
    treatment_approval_workflow: Optional[str] = Field(default=None, description="""How a treatment plan and its residual risks are approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentProcess']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsRiskTreatmentPlan(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_risk_management', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin'],
         'related_mappings': ['oscal:PlanOfActionAndMilestones']})

    implementation_state: Optional[IsmsImplementationStatus] = Field(default=None, description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan', 'IsmsIncludedControl', 'IsmsControl']} })
    plan_scope: Optional[str] = Field(default=None, description="""What the plan covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_risks: Optional[list[str]] = Field(default=None, description="""The risks the plan treats.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_actions: Optional[list[str]] = Field(default=None, description="""The actions the plan takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_controls: Optional[list[str]] = Field(default=None, description="""The controls the plan puts in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_resources: Optional[str] = Field(default=None, description="""The resources the plan needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_responsible_parties: Optional[list[str]] = Field(default=None, description="""Who carries out the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_timeline: Optional[str] = Field(default=None, description="""When the plan's actions are to happen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_risk_owner_approval: Optional[str] = Field(default=None, description="""The risk owner who approved the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_residual_risk_acceptance: Optional[str] = Field(default=None, description="""How the risk owners accepted the risk that remains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    plan_completion_date: Optional[date] = Field(default=None, description="""When the plan was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsStatementOfApplicability(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin'],
         'related_mappings': ['oscal:SspControlImplementation']})

    soa_entries: Optional[list[Union[IsmsIncludedControl,IsmsExcludedControl]]] = Field(default=None, description="""The statement's entries, one for each control included or Annex A control excluded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsStatementOfApplicability']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsApplicabilityEntry(ConfiguredBaseModel):
    """
    One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a']})

    entry_annex_a_control: Optional[IsmsAnnexAControl] = Field(default=None, description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })
    entry_type: Literal["IsmsApplicabilityEntry"] = Field(default="IsmsApplicabilityEntry", description="""The kind of entry: IsmsIncludedControl or IsmsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['IsmsApplicabilityEntry']} })
    entry_justification: str = Field(default=..., description="""Why the control is included or excluded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })

    @field_validator('entry_justification')
    def pattern_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsIncludedControl(IsmsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'entry_annex_a_control': {'name': 'entry_annex_a_control',
                                                                   'required': True}}},
                    {'slot_conditions': {'included_control': {'name': 'included_control',
                                                              'required': True}}}],
         'close_mappings': ['oscal:SspImplementedRequirement'],
         'comments': ['An included control names an Annex A control, one of the '
                      "organization's controls, or both."],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a'],
         'slot_usage': {'implementation_state': {'name': 'implementation_state',
                                                 'required': True}}})

    implementation_state: IsmsImplementationStatus = Field(default=..., description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan', 'IsmsIncludedControl', 'IsmsControl']} })
    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    included_control: Optional[str] = Field(default=None, description="""The organization's control the entry includes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsIncludedControl']} })
    included_evidence: Optional[str] = Field(default=None, description="""What shows that the control is in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsIncludedControl']} })
    included_target_date: Optional[date] = Field(default=None, description="""When the control is to be in place, if it is not yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsIncludedControl']} })
    entry_annex_a_control: Optional[IsmsAnnexAControl] = Field(default=None, description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })
    entry_type: Literal["IsmsIncludedControl"] = Field(default="IsmsIncludedControl", description="""The kind of entry: IsmsIncludedControl or IsmsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['IsmsApplicabilityEntry']} })
    entry_justification: str = Field(default=..., description="""Why the control is included or excluded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })

    @field_validator('entry_justification')
    def pattern_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsExcludedControl(IsmsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a'],
         'slot_usage': {'entry_annex_a_control': {'name': 'entry_annex_a_control',
                                                  'required': True}}})

    entry_annex_a_control: IsmsAnnexAControl = Field(default=..., description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })
    entry_type: Literal["IsmsExcludedControl"] = Field(default="IsmsExcludedControl", description="""The kind of entry: IsmsIncludedControl or IsmsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['IsmsApplicabilityEntry']} })
    entry_justification: str = Field(default=..., description="""Why the control is included or excluded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsApplicabilityEntry']} })

    @field_validator('entry_justification')
    def pattern_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsControl(IsmsRecordMixin):
    """
    A control the organization has determined it needs to treat its risks. It records what the control does in the organization's words and which Annex A controls it answers to. It also records who owns it, how far it is in place and how well it works.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '6.1.3'}},
         'comments': ["The text and guidance are the organization's own words, never "
                      'the text of ISO/IEC 27001 or ISO/IEC 27002. A control from '
                      'another source names no Annex A control.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a'],
         'mixins': ['IsmsRecordMixin'],
         'related_mappings': ['oscal:Control', 'nist_sp_800_53:Control']})

    relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy',
                       'IsmsObjective',
                       'IsmsControl',
                       'IsmsAsset',
                       'IsmsOperationalProcedure']} })
    implementation_state: Optional[IsmsImplementationStatus] = Field(default=None, description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRiskTreatmentPlan', 'IsmsIncludedControl', 'IsmsControl']} })
    control_annex_a_controls: Optional[list[IsmsAnnexAControl]] = Field(default=None, description="""The Annex A controls the control answers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_theme: Optional[IsmsControlTheme] = Field(default=None, description="""Which of Annex A's four themes the control belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_text: Optional[str] = Field(default=None, description="""What the control does, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_guidance: Optional[str] = Field(default=None, description="""The organization's notes on putting the control in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_threats: Optional[list[str]] = Field(default=None, description="""The threats the control acts against.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_asset_types: Optional[list[str]] = Field(default=None, description="""The kinds of asset the control applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_owner: Optional[str] = Field(default=None, description="""The person who owns the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_implementation_date: Optional[date] = Field(default=None, description="""When the control was put in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_effectiveness: Optional[str] = Field(default=None, description="""How well the control works, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_last_tested: Optional[date] = Field(default=None, description="""When the control was last tested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    control_evidence: Optional[list[str]] = Field(default=None, description="""Where the evidence that the control is in place is kept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsControl']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsAsset(IsmsRecordMixin):
    """
    An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control', 'value': '5.9'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a'],
         'mixins': ['IsmsRecordMixin'],
         'related_mappings': ['oscal:SspInventoryItem', 'spdx_software:Package']})

    relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy',
                       'IsmsObjective',
                       'IsmsControl',
                       'IsmsAsset',
                       'IsmsOperationalProcedure']} })
    asset_category: Optional[str] = Field(default=None, description="""What kind of asset it is, such as information, software, hardware or a service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    asset_owner: Optional[str] = Field(default=None, description="""Who owns the asset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    asset_custodian: Optional[str] = Field(default=None, description="""Who looks after the asset from day to day.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    asset_classification: Optional[str] = Field(default=None, description="""The information classification the asset carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    asset_location: Optional[str] = Field(default=None, description="""Where the asset is, physically or logically.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    asset_criticality: Optional[str] = Field(default=None, description="""How much the asset matters, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAsset']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsResource(IsmsRecordMixin):
    """
    A resource provided for the ISMS, such as people, time, tools or budget.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin']})

    resource_category: Optional[str] = Field(default=None, description="""What kind of resource it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    resource_quantity: Optional[str] = Field(default=None, description="""How much of the resource is provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    resource_allocation_date: Optional[date] = Field(default=None, description="""When the resource was allocated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    resource_allocated_to: Optional[str] = Field(default=None, description="""What the resource is allocated to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    resource_cost: Optional[str] = Field(default=None, description="""What the resource costs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    resource_availability: Optional[str] = Field(default=None, description="""Whether the resource is available now, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsResource']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsCompetenceRecord(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The evidence of one person's competence for work that affects information security, and what is done to close any gap.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    competence_person: Optional[str] = Field(default=None, description="""The person the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_role: Optional[str] = Field(default=None, description="""The role the person holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_required: Optional[list[str]] = Field(default=None, description="""The competences the role needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_education: Optional[list[str]] = Field(default=None, description="""The person's relevant education.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_training: Optional[list[str]] = Field(default=None, description="""The training the person has completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_experience: Optional[list[str]] = Field(default=None, description="""The person's relevant experience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_assessment_date: Optional[date] = Field(default=None, description="""When the person's competence was last assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_gaps: Optional[list[str]] = Field(default=None, description="""The gaps the assessment found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    competence_actions: Optional[list[str]] = Field(default=None, description="""What is done to close the gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCompetenceRecord']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsAwarenessProgramme(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    awareness_topics: Optional[list[str]] = Field(default=None, description="""The topics the programme covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    awareness_methods: Optional[list[str]] = Field(default=None, description="""How the programme is delivered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    awareness_audience: Optional[str] = Field(default=None, description="""Whom the programme is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    awareness_frequency: Optional[str] = Field(default=None, description="""How often the programme runs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    awareness_completion_tracking: Optional[str] = Field(default=None, description="""How completion is tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    awareness_effectiveness: Optional[str] = Field(default=None, description="""How the programme's effect is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAwarenessProgramme']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsCommunicationPlan(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The plan for communication about the ISMS, inside the organization and outside it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    communication_items: Optional[list[IsmsCommunication]] = Field(default=None, description="""The communications the plan provides for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunicationPlan']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsCommunication(ConfiguredBaseModel):
    """
    One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_core']})

    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    communication_subject: str = Field(default=..., description="""What the communication is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })
    communication_purpose: Optional[str] = Field(default=None, description="""Why it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })
    communication_audience: Optional[str] = Field(default=None, description="""To whom it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })
    communication_frequency: Optional[str] = Field(default=None, description="""How often it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })
    communication_method: Optional[str] = Field(default=None, description="""How it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })
    communication_records_required: Optional[bool] = Field(default=None, description="""Whether a record of the communication is kept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCommunication']} })


class IsmsDocumentedInformation(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    A piece of documented information the ISMS keeps under control that no more specific record describes, such as a procedure, a standard, a plan or a report.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '7.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    document_kind: IsmsDocumentKind = Field(default=..., description="""What kind of documented information it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentedInformation']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsOperationalProcedure(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    A procedure by which the organization plans and controls the processes that meet its information security requirements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '8.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsTopicSpecificPolicy',
                       'IsmsObjective',
                       'IsmsControl',
                       'IsmsAsset',
                       'IsmsOperationalProcedure']} })
    procedure_scope: Optional[str] = Field(default=None, description="""What the procedure covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOperationalProcedure']} })
    procedure_criteria: Optional[str] = Field(default=None, description="""The criteria the processes are run to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOperationalProcedure']} })
    procedure_control_measures: Optional[list[str]] = Field(default=None, description="""The measures that control the processes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOperationalProcedure']} })
    procedure_roles: Optional[list[str]] = Field(default=None, description="""The roles that carry out the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOperationalProcedure']} })
    procedure_change_control: Optional[str] = Field(default=None, description="""How changes to the processes are controlled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsOperationalProcedure']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsMonitoringProgramme(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    The programme of monitoring, measurement, analysis and evaluation of information security performance and of the ISMS's effectiveness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    monitoring_items: Optional[list[IsmsMonitoringItem]] = Field(default=None, description="""What the programme monitors and measures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringProgramme']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsMonitoringItem(ConfiguredBaseModel):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation']})

    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    monitoring_metric: str = Field(default=..., description="""The name of what is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_description: Optional[str] = Field(default=None, description="""What the measurement shows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_method: Optional[str] = Field(default=None, description="""How it is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_frequency: Optional[str] = Field(default=None, description="""How often it is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_analysis_frequency: Optional[str] = Field(default=None, description="""How often the results are analysed and evaluated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_analyst: Optional[str] = Field(default=None, description="""Who analyses and evaluates the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_target: Optional[str] = Field(default=None, description="""The value aimed for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_alert_threshold: Optional[str] = Field(default=None, description="""The value that calls for action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_current_value: Optional[str] = Field(default=None, description="""The value last measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })
    monitoring_trend: Optional[str] = Field(default=None, description="""Which way the value is moving.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsMonitoringItem']} })


class IsmsAuditProgramme(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '9.2.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin'],
         'related_mappings': ['oscal:AssessmentPlan']})

    programme_period: Optional[str] = Field(default=None, description="""The period the programme covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    programme_audits: Optional[list[str]] = Field(default=None, description="""The audits the programme plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    programme_frequency_rationale: Optional[str] = Field(default=None, description="""Why the audits happen as often as they do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    programme_resources: Optional[str] = Field(default=None, description="""The resources the programme needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    programme_auditor_qualifications: Optional[str] = Field(default=None, description="""The qualifications the auditors need.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    programme_status: Optional[str] = Field(default=None, description="""Where the programme stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditProgramme']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsAudit(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.2'}},
         'comments': ['An audit of several management systems at once lists each '
                      'standard in audit_standards.'],
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin'],
         'related_mappings': ['oscal:AssessmentPlan']})

    audit_type: IsmsAuditType = Field(default=..., description="""Who carries out the audit, relative to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_standards: Optional[list[IsmsManagementSystemStandard]] = Field(default=None, description="""The management system standards the audit covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_scope: Optional[str] = Field(default=None, description="""What the audit covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_criteria: Optional[list[str]] = Field(default=None, description="""What the audit compares the ISMS against.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_objectives: Optional[list[str]] = Field(default=None, description="""What the audit sets out to establish.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_period_start: Optional[date] = Field(default=None, description="""When the audit began.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_period_end: Optional[date] = Field(default=None, description="""When the audit ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_lead: Optional[str] = Field(default=None, description="""Who led the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_team: Optional[list[str]] = Field(default=None, description="""Who else audited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_auditees: Optional[list[str]] = Field(default=None, description="""Who represented the parts of the organization audited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_plan: Optional[str] = Field(default=None, description="""The documented information that holds the audit plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_findings: Optional[list[IsmsAuditFinding]] = Field(default=None, description="""What the audit found, good and bad.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_conclusion: Optional[str] = Field(default=None, description="""The audit's overall conclusion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_report_date: Optional[date] = Field(default=None, description="""When the audit report was issued.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    audit_report_distribution: Optional[list[str]] = Field(default=None, description="""Who received the audit report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAudit']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsAuditFinding(IsmsRecordMixin):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation'],
         'mixins': ['IsmsRecordMixin']})

    finding_type: IsmsAuditFindingType = Field(default=..., description="""What kind of finding it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_requirement: Optional[str] = Field(default=None, description="""The clause or Annex A control of ISO/IEC 27001:2022 the finding concerns, by number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_control: Optional[str] = Field(default=None, description="""The organization's control the finding concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_evidence: Optional[str] = Field(default=None, description="""The objective evidence for the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_root_cause: Optional[str] = Field(default=None, description="""What the analysis of the finding's cause found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_risk: Optional[str] = Field(default=None, description="""What the finding means for risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_recommendation: Optional[str] = Field(default=None, description="""What the auditor recommends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_auditee_response: Optional[str] = Field(default=None, description="""How the auditee responded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_corrective_action: Optional[str] = Field(default=None, description="""The corrective action the finding led to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_closure_status: Optional[str] = Field(default=None, description="""Whether the finding is closed, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    finding_closure_date: Optional[date] = Field(default=None, description="""When the finding was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsAuditFinding']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsManagementReview(IsmsDocumentControlMixin, IsmsRecordMixin):
    """
    A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause', 'value': '9.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_performance_evaluation', 'isms_documented_information'],
         'mixins': ['IsmsRecordMixin', 'IsmsDocumentControlMixin']})

    review_held_on: date = Field(default=..., description="""When the review was held.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_attendees: Optional[list[str]] = Field(default=None, description="""Who attended the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_previous_actions: Optional[str] = Field(default=None, description="""Where the actions from earlier reviews stand.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_context_changes: Optional[str] = Field(default=None, description="""How the issues that bear on the ISMS have changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_interested_party_changes: Optional[str] = Field(default=None, description="""How interested parties' needs and expectations have changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_interested_party_feedback: Optional[str] = Field(default=None, description="""What interested parties said.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_performance_trends: Optional[str] = Field(default=None, description="""The trends in information security performance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_audit_results: Optional[str] = Field(default=None, description="""What the audits found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_risk_assessment_results: Optional[str] = Field(default=None, description="""What the risk assessments found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_risk_treatment_status: Optional[str] = Field(default=None, description="""Where risk treatment stands.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_risks_and_opportunities: Optional[str] = Field(default=None, description="""How risks and opportunities have changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_improvement_opportunities: Optional[list[str]] = Field(default=None, description="""The opportunities for improvement raised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_decisions: Optional[list[str]] = Field(default=None, description="""What the review decided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_actions: Optional[list[str]] = Field(default=None, description="""What the review asked to be done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    review_next_date: Optional[date] = Field(default=None, description="""When the next review is planned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsManagementReview']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })
    document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_distribution: Optional[list[str]] = Field(default=None, description="""How the document is distributed, accessed, retrieved and used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_storage: Optional[str] = Field(default=None, description="""How the document is stored and preserved, so that it stays legible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the ISMS needs it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })
    document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsNonconformity(IsmsRecordMixin):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_improvement'],
         'mixins': ['IsmsRecordMixin']})

    nonconformity_source: Optional[str] = Field(default=None, description="""How the nonconformity came to light, such as an audit, a review or an incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_detected_on: Optional[date] = Field(default=None, description="""When the nonconformity was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_detected_by: Optional[str] = Field(default=None, description="""Who or what found it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_requirement: Optional[str] = Field(default=None, description="""The requirement that was not met, of ISO/IEC 27001, of the organization or of an interested party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_immediate_actions: Optional[list[str]] = Field(default=None, description="""What was done at once to control and correct it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_consequences: Optional[str] = Field(default=None, description="""How its consequences were dealt with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_root_cause: Optional[str] = Field(default=None, description="""What caused it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_similar_check: Optional[str] = Field(default=None, description="""Whether similar nonconformities exist or could occur, and where.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_status: Optional[str] = Field(default=None, description="""Where the nonconformity stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_closure_date: Optional[date] = Field(default=None, description="""When it was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    nonconformity_closure_evidence: Optional[str] = Field(default=None, description="""What shows that it is closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsNonconformity']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsCorrectiveAction(IsmsRecordMixin):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_improvement'],
         'mixins': ['IsmsRecordMixin'],
         'related_mappings': ['oscal:PoamItem']})

    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    action_nonconformities: Optional[list[str]] = Field(default=None, description="""The nonconformities the action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_root_cause: Optional[str] = Field(default=None, description="""The cause the action removes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_target_date: Optional[date] = Field(default=None, description="""When the action is to be complete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_completion_date: Optional[date] = Field(default=None, description="""When the action was complete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_resources: Optional[str] = Field(default=None, description="""The resources the action needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_effectiveness_criteria: Optional[str] = Field(default=None, description="""How the action's effect will be judged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_effectiveness_review_date: Optional[date] = Field(default=None, description="""When the action's effect was reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_effective: Optional[bool] = Field(default=None, description="""Whether the review found the action effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_isms_changes: Optional[str] = Field(default=None, description="""The changes to the ISMS the action needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    action_status: Optional[str] = Field(default=None, description="""Where the action stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsCorrectiveAction']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsImprovementOpportunity(IsmsRecordMixin):
    """
    An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso27001_clause': {'tag': 'iso27001_clause',
                                             'value': '10.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_improvement'],
         'mixins': ['IsmsRecordMixin']})

    responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsObjective',
                       'IsmsIncludedControl',
                       'IsmsCommunication',
                       'IsmsMonitoringItem',
                       'IsmsCorrectiveAction',
                       'IsmsImprovementOpportunity']} })
    improvement_source: Optional[str] = Field(default=None, description="""Where the opportunity came from, such as a review, an audit or daily work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_identified_on: Optional[date] = Field(default=None, description="""When the opportunity was identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_identified_by: Optional[str] = Field(default=None, description="""Who identified it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_benefit: Optional[str] = Field(default=None, description="""What the improvement is expected to bring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_priority: Optional[str] = Field(default=None, description="""How soon it is to be acted on, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_plan: Optional[str] = Field(default=None, description="""How the improvement is to be made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_target_date: Optional[date] = Field(default=None, description="""When the improvement is to be made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_completion_date: Optional[date] = Field(default=None, description="""When it was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_outcome: Optional[str] = Field(default=None, description="""What the improvement brought.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    improvement_status: Optional[str] = Field(default=None, description="""Where it stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsImprovementOpportunity']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsSecurityEvent(IsmsRecordMixin):
    """
    An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.25'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a'],
         'mixins': ['IsmsRecordMixin']})

    affected_assets: Optional[list[str]] = Field(default=None, description="""The assets the risk, event or incident affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk', 'IsmsSecurityEvent']} })
    event_type: Literal["IsmsSecurityEvent"] = Field(default="IsmsSecurityEvent", description="""The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['IsmsSecurityEvent']} })
    event_occurred_at: Optional[datetime ] = Field(default=None, description="""When the event happened, or when it was first noticed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    event_reporter: Optional[str] = Field(default=None, description="""Who reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    event_assessment: Optional[str] = Field(default=None, description="""What the assessment of the event found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class IsmsSecurityIncident(IsmsSecurityEvent):
    """
    An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.26'}},
         'from_schema': 'https://w3id.org/lmodel/iso27001',
         'in_subset': ['isms_annex_a']})

    affected_security_properties: Optional[list[IsmsSecurityProperty]] = Field(default=None, description="""Which of confidentiality, integrity and availability the risk or incident threatens.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk', 'IsmsSecurityIncident']} })
    incident_category: Optional[IsmsIncidentCategory] = Field(default=None, description="""What kind of incident it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_severity: Optional[IsmsRiskLevel] = Field(default=None, description="""How severe the incident is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_detection_method: Optional[str] = Field(default=None, description="""How the incident was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_response_actions: Optional[list[str]] = Field(default=None, description="""What was done in response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_containment_actions: Optional[list[str]] = Field(default=None, description="""What was done to contain it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_eradication_actions: Optional[list[str]] = Field(default=None, description="""What was done to remove its cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_recovery_actions: Optional[list[str]] = Field(default=None, description="""What was done to restore normal operation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_root_cause: Optional[str] = Field(default=None, description="""What caused the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_lessons_learned: Optional[list[str]] = Field(default=None, description="""What the organization learned from it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.27'}},
         'domain_of': ['IsmsSecurityIncident']} })
    incident_evidence: Optional[list[str]] = Field(default=None, description="""The evidence collected about it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': '5.28'}},
         'domain_of': ['IsmsSecurityIncident']} })
    incident_notification_required: Optional[bool] = Field(default=None, description="""Whether authorities or other parties had to be told.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_notifications: Optional[list[str]] = Field(default=None, description="""Whom the organization told, and when.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_closed_at: Optional[datetime ] = Field(default=None, description="""When the incident was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    incident_review: Optional[str] = Field(default=None, description="""What the review after the incident found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityIncident']} })
    affected_assets: Optional[list[str]] = Field(default=None, description="""The assets the risk, event or incident affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRisk', 'IsmsSecurityEvent']} })
    event_type: Literal["IsmsSecurityIncident"] = Field(default="IsmsSecurityIncident", description="""The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['IsmsSecurityEvent']} })
    event_occurred_at: Optional[datetime ] = Field(default=None, description="""When the event happened, or when it was first noticed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    event_reporter: Optional[str] = Field(default=None, description="""Who reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    event_assessment: Optional[str] = Field(default=None, description="""What the assessment of the event found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsSecurityEvent']} })
    isms_id: str = Field(default=..., description="""The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IsmsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['IsmsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
IsmsRecordMixin.model_rebuild()
IsmsDocumentControlMixin.model_rebuild()
IsmsManagementSystem.model_rebuild()
IsmsOrganization.model_rebuild()
IsmsInterestedParty.model_rebuild()
IsmsPolicy.model_rebuild()
IsmsTopicSpecificPolicy.model_rebuild()
IsmsRole.model_rebuild()
IsmsObjective.model_rebuild()
IsmsRiskAssessmentProcess.model_rebuild()
IsmsRiskAssessment.model_rebuild()
IsmsRisk.model_rebuild()
IsmsRiskTreatmentProcess.model_rebuild()
IsmsRiskTreatmentPlan.model_rebuild()
IsmsStatementOfApplicability.model_rebuild()
IsmsApplicabilityEntry.model_rebuild()
IsmsIncludedControl.model_rebuild()
IsmsExcludedControl.model_rebuild()
IsmsControl.model_rebuild()
IsmsAsset.model_rebuild()
IsmsResource.model_rebuild()
IsmsCompetenceRecord.model_rebuild()
IsmsAwarenessProgramme.model_rebuild()
IsmsCommunicationPlan.model_rebuild()
IsmsCommunication.model_rebuild()
IsmsDocumentedInformation.model_rebuild()
IsmsOperationalProcedure.model_rebuild()
IsmsMonitoringProgramme.model_rebuild()
IsmsMonitoringItem.model_rebuild()
IsmsAuditProgramme.model_rebuild()
IsmsAudit.model_rebuild()
IsmsAuditFinding.model_rebuild()
IsmsManagementReview.model_rebuild()
IsmsNonconformity.model_rebuild()
IsmsCorrectiveAction.model_rebuild()
IsmsImprovementOpportunity.model_rebuild()
IsmsSecurityEvent.model_rebuild()
IsmsSecurityIncident.model_rebuild()
