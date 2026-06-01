#![allow(non_camel_case_types)]

#[cfg(feature = "serde")]
mod serde_utils;
pub mod poly;
pub mod poly_containers;
#[cfg(feature = "stubgen")]
pub mod stub_utils;

#[cfg(feature = "serde")]
use serde_yml as _ ;
use chrono::{NaiveDate,NaiveDateTime};
#[cfg(feature = "pyo3")]
use pyo3::{FromPyObject,prelude::*};
#[cfg(feature = "stubgen")]
use pyo3_stub_gen::{define_stub_info_gatherer,derive::gen_stub_pyclass,derive::gen_stub_pymethods};
#[cfg(feature = "serde")]
use serde::{Deserialize,Serialize,de::IntoDeserializer};
use serde_value::Value;
#[cfg(feature = "serde")]
use serde_path_to_error;
use std::collections::HashMap;
use std::collections::BTreeMap;

// Types

pub type string = String;
pub type integer = String;
pub type boolean = String;
pub type float = f64;
pub type double = f64;
pub type decimal = String;
pub type time = String;
pub type date = String;
pub type datetime = String;
pub type date_or_datetime = String;
pub type uriorcurie = String;
pub type curie = String;
pub type uri = String;
pub type ncname = String;
pub type objectidentifier = String;
pub type nodeidentifier = String;
pub type jsonpointer = String;
pub type jsonpath = String;
pub type sparqlpath = String;
pub type positive_integer_type = String;
pub type unsigned_short_type = String;
pub type duration_type = String;

// Slots

pub type id = uriorcurie;
pub type name = String;
pub type description = String;
pub type version = String;
pub type created_date = NaiveDate;
pub type modified_date = NaiveDate;
pub type document_type = DocumentType;
pub type document_reference = String;
pub type author = String;
pub type owner = String;
pub type approved_by = String;
pub type approved_date = NaiveDate;
pub type effective_date = NaiveDate;
pub type review_date = NaiveDate;
pub type status = String;
pub type classification = String;
pub type retention_period = String;
pub type distribution_controls = Vec<String>;
pub type storage_and_preservation = String;
pub type change_control_method = String;
pub type external_origin = bool;
pub type external_origin_source = String;
pub type organization = Organization;
pub type legal_name = String;
pub type trading_names = Vec<String>;
pub type organization_type = String;
pub type industry_sector = String;
pub type size_category = String;
pub type employee_count = isize;
pub type geographic_locations = Vec<String>;
pub type regulatory_jurisdictions = Vec<String>;
pub type parent_organization = String;
pub type subsidiaries = Vec<String>;
pub type scope_statement = String;
pub type scope_boundaries = Vec<String>;
pub type scope_exclusions = Vec<String>;
pub type context_internal_issues = Vec<String>;
pub type context_external_issues = Vec<String>;
pub type climate_change_relevant = bool;
pub type interested_parties = Vec<InterestedParty>;
pub type party_type = String;
pub type relationship = String;
pub type requirements = Vec<String>;
pub type addressed_requirements = Vec<String>;
pub type communication_needs = String;
pub type contact_information = String;
pub type climate_change_related_requirements = Vec<String>;
pub type information_security_policy = InformationSecurityPolicy;
pub type policy_statement = String;
pub type policy_objectives_framework = String;
pub type commitment_statements = Vec<String>;
pub type applicability_statement = String;
pub type communication_date = NaiveDate;
pub type acknowledgment_required = bool;
pub type last_policy_review_date = NaiveDate;
pub type next_policy_review_date = NaiveDate;
pub type integrated_management_systems = Vec<RelatedManagementSystem>;
pub type related_topic_policies = Vec<TopicSpecificPolicy>;
pub type topic_area = String;
pub type parent_policy = InformationSecurityPolicy;
pub type applicable_controls = Vec<SecurityControl>;
pub type target_audience = String;
pub type roles = Vec<Role>;
pub type role_type = String;
pub type responsibilities = Vec<String>;
pub type authorities = Vec<String>;
pub type accountability = String;
pub type assigned_to = Vec<String>;
pub type delegation_rules = String;
pub type reporting_line = String;
pub type objectives = Vec<InformationSecurityObjective>;
pub type objective_statement = String;
pub type target_value = String;
pub type current_value = String;
pub type metric_definition = String;
pub type measurement_method = String;
pub type measurement_frequency = String;
pub type responsible_role = Role;
pub type target_date = NaiveDate;
pub type achievement_status = String;
pub type action_plan = String;
pub type objective_resources_required = String;
pub type top_management = String;
pub type governing_body = String;
pub type leadership_commitment_evidence = Vec<String>;
pub type processes_and_interactions = String;
pub type interfaces_and_dependencies = Vec<String>;
pub type planned_changes = Vec<String>;
pub type externally_provided_services = Vec<String>;
pub type risks_and_opportunities_actions = Vec<String>;
pub type risk_assessment_process = RiskAssessmentProcess;
pub type risk_acceptance_criteria = String;
pub type assessment_criteria = String;
pub type assessment_methodology = String;
pub type likelihood_scale = String;
pub type impact_scale = String;
pub type risk_matrix = String;
pub type assessment_frequency = String;
pub type trigger_events = Vec<String>;
pub type risk_assessments = Vec<RiskAssessment>;
pub type assessment_scope = String;
pub type assessment_date = NaiveDate;
pub type assessor = String;
pub type methodology_used = String;
pub type risks_identified = Vec<Risk>;
pub type summary_findings = String;
pub type recommendations = Vec<String>;
pub type next_assessment_date = NaiveDate;
pub type related_risks = Vec<Risk>;
pub type risk_source = String;
pub type threat_description = String;
pub type vulnerability_description = String;
pub type affected_assets = Vec<Asset>;
pub type affected_cia_properties = Vec<CIAProperty>;
pub type risk_owner = String;
pub type likelihood = LikelihoodRating;
pub type impact = ImpactRating;
pub type inherent_risk_level = RiskLevel;
pub type existing_controls = Vec<SecurityControl>;
pub type residual_risk_level = RiskLevel;
pub type risk_treatment_option = RiskTreatmentOption;
pub type treatment_priority = String;
pub type related_treatment_plan = RiskTreatmentPlan;
pub type risk_treatment_process = RiskTreatmentProcess;
pub type treatment_options_guidance = String;
pub type control_selection_criteria = String;
pub type soa_template = String;
pub type annex_a_omission_verification = String;
pub type approval_workflow = String;
pub type risk_treatment_plans = Vec<RiskTreatmentPlan>;
pub type plan_scope = String;
pub type risks_addressed = Vec<Risk>;
pub type treatment_actions = Vec<String>;
pub type controls_to_implement = Vec<SecurityControl>;
pub type resources_required = String;
pub type responsible_parties = Vec<String>;
pub type implementation_timeline = String;
pub type risk_owner_approval = String;
pub type residual_risk_acceptance = String;
pub type implementation_status = ImplementationStatus;
pub type completion_date = NaiveDate;
pub type statement_of_applicability = StatementOfApplicability;
pub type soa_entries = Vec<SoAEntry>;
pub type total_controls = isize;
pub type implemented_count = isize;
pub type planned_count = isize;
pub type not_applicable_count = isize;
pub type last_review_date = NaiveDate;
pub type control_reference = SecurityControl;
pub type is_applicable = bool;
pub type inclusion_justification = String;
pub type exclusion_justification = String;
pub type implementation_evidence = String;
pub type target_implementation_date = NaiveDate;
pub type controls = Vec<SecurityControl>;
pub type control_id = AnnexAControlId;
pub type control_title = String;
pub type control_category = ControlCategory;
pub type control_text = String;
pub type implementation_guidance = String;
pub type related_controls = Vec<SecurityControl>;
pub type applicable_threats = Vec<String>;
pub type applicable_assets = Vec<String>;
pub type control_owner = String;
pub type implementation_date = NaiveDate;
pub type effectiveness_rating = String;
pub type last_test_date = NaiveDate;
pub type evidence_references = Vec<String>;
pub type resources = Vec<Resource>;
pub type resource_type = String;
pub type quantity = String;
pub type allocation_date = NaiveDate;
pub type allocated_to = String;
pub type cost = String;
pub type availability_status = String;
pub type competence_records = Vec<CompetenceRecord>;
pub type person_name = String;
pub type person_role = String;
pub type required_competencies = Vec<String>;
pub type education_records = Vec<String>;
pub type training_records = Vec<String>;
pub type experience_records = Vec<String>;
pub type competency_assessment_date = NaiveDate;
pub type competency_gaps = Vec<String>;
pub type development_actions = Vec<String>;
pub type awareness_program = AwarenessProgram;
pub type awareness_topics = Vec<String>;
pub type delivery_methods = Vec<String>;
pub type frequency = String;
pub type completion_tracking = String;
pub type effectiveness_measures = String;
pub type communication_plan = CommunicationPlan;
pub type communication_items = Vec<CommunicationItem>;
pub type subject = String;
pub type purpose = String;
pub type audience = String;
pub type method = String;
pub type responsible_party = String;
pub type records_required = bool;
pub type documented_information_register = Vec<DocumentedInformation>;
pub type operational_procedures = Vec<OperationalProcedure>;
pub type procedure_scope = String;
pub type process_criteria = String;
pub type control_measures = Vec<String>;
pub type responsible_roles = Vec<Role>;
pub type change_control_requirements = String;
pub type monitoring_program = MonitoringProgram;
pub type monitoring_items = Vec<MonitoringItem>;
pub type metric_name = String;
pub type metric_description = String;
pub type analysis_frequency = String;
pub type analyst = String;
pub type target_threshold = String;
pub type alert_threshold = String;
pub type trend = String;
pub type internal_audits = Vec<InternalAudit>;
pub type audit_reference = String;
pub type audit_type = AuditType;
pub type audit_scope = String;
pub type audit_criteria = Vec<String>;
pub type audit_objectives = Vec<String>;
pub type audit_period_start = NaiveDate;
pub type audit_period_end = NaiveDate;
pub type lead_auditor = String;
pub type audit_team = Vec<String>;
pub type auditee_representatives = Vec<String>;
pub type audit_plan = String;
pub type findings = Vec<AuditFinding>;
pub type positive_observations = Vec<String>;
pub type audit_conclusion = String;
pub type report_date = NaiveDate;
pub type report_distribution = Vec<String>;
pub type finding_type = AuditFindingType;
pub type clause_reference = String;
pub type finding_description = String;
pub type objective_evidence = String;
pub type root_cause_analysis = String;
pub type risk_implication = String;
pub type recommended_action = String;
pub type auditee_response = String;
pub type linked_corrective_action = CorrectiveAction;
pub type closure_status = String;
pub type closure_date = NaiveDate;
pub type management_reviews = Vec<ManagementReview>;
pub type attendees = Vec<String>;
pub type previous_actions_status = String;
pub type context_changes = String;
pub type interested_party_changes = String;
pub type performance_trends = String;
pub type audit_results_summary = String;
pub type risk_assessment_results = String;
pub type improvement_opportunities = Vec<String>;
pub type interested_party_feedback = String;
pub type risk_treatment_status = String;
pub type risks_and_opportunities_changes = String;
pub type decisions = Vec<String>;
pub type action_items = Vec<String>;
pub type next_review_date = NaiveDate;
pub type nonconformities = Vec<Nonconformity>;
pub type nonconformity_source = String;
pub type detection_date = NaiveDate;
pub type detected_by = String;
pub type requirement_violated = String;
pub type nonconformity_description = String;
pub type immediate_actions = Vec<String>;
pub type consequences_addressed = String;
pub type root_cause = String;
pub type similar_nonconformities_check = String;
pub type linked_corrective_actions = Vec<CorrectiveAction>;
pub type closure_evidence = String;
pub type corrective_actions = Vec<CorrectiveAction>;
pub type linked_nonconformity = Nonconformity;
pub type action_description = String;
pub type root_cause_addressed = String;
pub type target_completion_date = NaiveDate;
pub type actual_completion_date = NaiveDate;
pub type effectiveness_criteria = String;
pub type effectiveness_review_date = NaiveDate;
pub type effectiveness_verified = bool;
pub type isms_changes_required = String;
pub type improvements = Vec<ImprovementOpportunity>;
pub type improvement_source = String;
pub type identification_date = NaiveDate;
pub type identified_by = String;
pub type improvement_description = String;
pub type expected_benefit = String;
pub type priority = String;
pub type implementation_plan = String;
pub type outcome_assessment = String;
pub type asset_type = String;
pub type asset_owner = String;
pub type asset_custodian = String;
pub type location = String;
pub type criticality = String;
pub type event_datetime = NaiveDateTime;
pub type reporter = String;
pub type event_description = String;
pub type initial_assessment = String;
pub type categorized_as_incident = bool;
pub type linked_incident = InformationSecurityIncident;
pub type incident_datetime = NaiveDateTime;
pub type incident_category = SecurityIncidentCategory;
pub type severity = RiskLevel;
pub type affected_cia = Vec<CIAProperty>;
pub type incident_description = String;
pub type detection_method = String;
pub type response_actions = Vec<String>;
pub type containment_actions = Vec<String>;
pub type eradication_actions = Vec<String>;
pub type recovery_actions = Vec<String>;
pub type lessons_learned = Vec<String>;
pub type evidence_collected = Vec<String>;
pub type notification_required = bool;
pub type notifications_made = Vec<String>;
pub type closure_datetime = NaiveDateTime;
pub type post_incident_review = String;
pub type certification_status = String;
pub type certification_body = String;
pub type certification_date = NaiveDate;
pub type recertification_date = NaiveDate;
pub type programme_period = String;
pub type planned_audits = Vec<InternalAudit>;
pub type audit_frequency_rationale = String;
pub type resource_requirements = String;
pub type auditor_qualifications = String;
pub type programme_status = String;

// Enums

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ControlCategory {
    Organizational,
    People,
    Physical,
    Technological,
}

impl core::fmt::Display for ControlCategory {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ControlCategory::Organizational => f.write_str("organizational"),
            ControlCategory::People => f.write_str("people"),
            ControlCategory::Physical => f.write_str("physical"),
            ControlCategory::Technological => f.write_str("technological"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ControlCategory {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ControlCategory::Organizational => "organizational",
            ControlCategory::People => "people",
            ControlCategory::Physical => "physical",
            ControlCategory::Technological => "technological",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ControlCategory {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "organizational" | "Organizational" => Ok(ControlCategory::Organizational),
                "people" | "People" => Ok(ControlCategory::People),
                "physical" | "Physical" => Ok(ControlCategory::Physical),
                "technological" | "Technological" => Ok(ControlCategory::Technological),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ControlCategory: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ControlCategory)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ControlCategory {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['organizational', 'people', 'physical', 'technological']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ImplementationStatus {
    NotStarted,
    Planned,
    InProgress,
    Implemented,
    NotApplicable,
}

impl core::fmt::Display for ImplementationStatus {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ImplementationStatus::NotStarted => f.write_str("not_started"),
            ImplementationStatus::Planned => f.write_str("planned"),
            ImplementationStatus::InProgress => f.write_str("in_progress"),
            ImplementationStatus::Implemented => f.write_str("implemented"),
            ImplementationStatus::NotApplicable => f.write_str("not_applicable"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ImplementationStatus {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ImplementationStatus::NotStarted => "not_started",
            ImplementationStatus::Planned => "planned",
            ImplementationStatus::InProgress => "in_progress",
            ImplementationStatus::Implemented => "implemented",
            ImplementationStatus::NotApplicable => "not_applicable",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ImplementationStatus {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "not_started" | "NotStarted" => Ok(ImplementationStatus::NotStarted),
                "planned" | "Planned" => Ok(ImplementationStatus::Planned),
                "in_progress" | "InProgress" => Ok(ImplementationStatus::InProgress),
                "implemented" | "Implemented" => Ok(ImplementationStatus::Implemented),
                "not_applicable" | "NotApplicable" => Ok(ImplementationStatus::NotApplicable),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ImplementationStatus: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ImplementationStatus)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ImplementationStatus {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['not_started', 'planned', 'in_progress', 'implemented', 'not_applicable']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RiskTreatmentOption {
    Modify,
    Accept,
    Avoid,
    Share,
}

impl core::fmt::Display for RiskTreatmentOption {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RiskTreatmentOption::Modify => f.write_str("modify"),
            RiskTreatmentOption::Accept => f.write_str("accept"),
            RiskTreatmentOption::Avoid => f.write_str("avoid"),
            RiskTreatmentOption::Share => f.write_str("share"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RiskTreatmentOption {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RiskTreatmentOption::Modify => "modify",
            RiskTreatmentOption::Accept => "accept",
            RiskTreatmentOption::Avoid => "avoid",
            RiskTreatmentOption::Share => "share",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RiskTreatmentOption {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "modify" | "Modify" => Ok(RiskTreatmentOption::Modify),
                "accept" | "Accept" => Ok(RiskTreatmentOption::Accept),
                "avoid" | "Avoid" => Ok(RiskTreatmentOption::Avoid),
                "share" | "Share" => Ok(RiskTreatmentOption::Share),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RiskTreatmentOption: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RiskTreatmentOption)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RiskTreatmentOption {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['modify', 'accept', 'avoid', 'share']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RiskLevel {
    VeryLow,
    Low,
    Medium,
    High,
    Critical,
}

impl core::fmt::Display for RiskLevel {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RiskLevel::VeryLow => f.write_str("very_low"),
            RiskLevel::Low => f.write_str("low"),
            RiskLevel::Medium => f.write_str("medium"),
            RiskLevel::High => f.write_str("high"),
            RiskLevel::Critical => f.write_str("critical"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RiskLevel {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RiskLevel::VeryLow => "very_low",
            RiskLevel::Low => "low",
            RiskLevel::Medium => "medium",
            RiskLevel::High => "high",
            RiskLevel::Critical => "critical",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RiskLevel {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "very_low" | "VeryLow" => Ok(RiskLevel::VeryLow),
                "low" | "Low" => Ok(RiskLevel::Low),
                "medium" | "Medium" => Ok(RiskLevel::Medium),
                "high" | "High" => Ok(RiskLevel::High),
                "critical" | "Critical" => Ok(RiskLevel::Critical),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RiskLevel: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RiskLevel)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RiskLevel {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['very_low', 'low', 'medium', 'high', 'critical']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum DocumentType {
    Policy,
    Procedure,
    Standard,
    Guideline,
    Record,
    Plan,
    Report,
}

impl core::fmt::Display for DocumentType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            DocumentType::Policy => f.write_str("policy"),
            DocumentType::Procedure => f.write_str("procedure"),
            DocumentType::Standard => f.write_str("standard"),
            DocumentType::Guideline => f.write_str("guideline"),
            DocumentType::Record => f.write_str("record"),
            DocumentType::Plan => f.write_str("plan"),
            DocumentType::Report => f.write_str("report"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for DocumentType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            DocumentType::Policy => "policy",
            DocumentType::Procedure => "procedure",
            DocumentType::Standard => "standard",
            DocumentType::Guideline => "guideline",
            DocumentType::Record => "record",
            DocumentType::Plan => "plan",
            DocumentType::Report => "report",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for DocumentType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "policy" | "Policy" => Ok(DocumentType::Policy),
                "procedure" | "Procedure" => Ok(DocumentType::Procedure),
                "standard" | "Standard" => Ok(DocumentType::Standard),
                "guideline" | "Guideline" => Ok(DocumentType::Guideline),
                "record" | "Record" => Ok(DocumentType::Record),
                "plan" | "Plan" => Ok(DocumentType::Plan),
                "report" | "Report" => Ok(DocumentType::Report),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for DocumentType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(DocumentType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for DocumentType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AuditFindingType {
    MajorNonconformity,
    MinorNonconformity,
    Observation,
    PositiveFinding,
}

impl core::fmt::Display for AuditFindingType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AuditFindingType::MajorNonconformity => f.write_str("major_nonconformity"),
            AuditFindingType::MinorNonconformity => f.write_str("minor_nonconformity"),
            AuditFindingType::Observation => f.write_str("observation"),
            AuditFindingType::PositiveFinding => f.write_str("positive_finding"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AuditFindingType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AuditFindingType::MajorNonconformity => "major_nonconformity",
            AuditFindingType::MinorNonconformity => "minor_nonconformity",
            AuditFindingType::Observation => "observation",
            AuditFindingType::PositiveFinding => "positive_finding",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AuditFindingType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "major_nonconformity" | "MajorNonconformity" => Ok(AuditFindingType::MajorNonconformity),
                "minor_nonconformity" | "MinorNonconformity" => Ok(AuditFindingType::MinorNonconformity),
                "observation" | "Observation" => Ok(AuditFindingType::Observation),
                "positive_finding" | "PositiveFinding" => Ok(AuditFindingType::PositiveFinding),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AuditFindingType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AuditFindingType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AuditFindingType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum LikelihoodRating {
    Rare,
    Unlikely,
    Possible,
    Likely,
    AlmostCertain,
}

impl core::fmt::Display for LikelihoodRating {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            LikelihoodRating::Rare => f.write_str("rare"),
            LikelihoodRating::Unlikely => f.write_str("unlikely"),
            LikelihoodRating::Possible => f.write_str("possible"),
            LikelihoodRating::Likely => f.write_str("likely"),
            LikelihoodRating::AlmostCertain => f.write_str("almost_certain"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for LikelihoodRating {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            LikelihoodRating::Rare => "rare",
            LikelihoodRating::Unlikely => "unlikely",
            LikelihoodRating::Possible => "possible",
            LikelihoodRating::Likely => "likely",
            LikelihoodRating::AlmostCertain => "almost_certain",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for LikelihoodRating {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "rare" | "Rare" => Ok(LikelihoodRating::Rare),
                "unlikely" | "Unlikely" => Ok(LikelihoodRating::Unlikely),
                "possible" | "Possible" => Ok(LikelihoodRating::Possible),
                "likely" | "Likely" => Ok(LikelihoodRating::Likely),
                "almost_certain" | "AlmostCertain" => Ok(LikelihoodRating::AlmostCertain),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for LikelihoodRating: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(LikelihoodRating)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for LikelihoodRating {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['rare', 'unlikely', 'possible', 'likely', 'almost_certain']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum CIAProperty {
    Confidentiality,
    Integrity,
    Availability,
}

impl core::fmt::Display for CIAProperty {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            CIAProperty::Confidentiality => f.write_str("confidentiality"),
            CIAProperty::Integrity => f.write_str("integrity"),
            CIAProperty::Availability => f.write_str("availability"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for CIAProperty {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            CIAProperty::Confidentiality => "confidentiality",
            CIAProperty::Integrity => "integrity",
            CIAProperty::Availability => "availability",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for CIAProperty {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "confidentiality" | "Confidentiality" => Ok(CIAProperty::Confidentiality),
                "integrity" | "Integrity" => Ok(CIAProperty::Integrity),
                "availability" | "Availability" => Ok(CIAProperty::Availability),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for CIAProperty: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(CIAProperty)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for CIAProperty {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['confidentiality', 'integrity', 'availability']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AuditType {
    Internal,
    ExternalSecondParty,
    ExternalThirdParty,
    Surveillance,
    Recertification,
    Combined,
}

impl core::fmt::Display for AuditType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AuditType::Internal => f.write_str("internal"),
            AuditType::ExternalSecondParty => f.write_str("external_second_party"),
            AuditType::ExternalThirdParty => f.write_str("external_third_party"),
            AuditType::Surveillance => f.write_str("surveillance"),
            AuditType::Recertification => f.write_str("recertification"),
            AuditType::Combined => f.write_str("combined"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AuditType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AuditType::Internal => "internal",
            AuditType::ExternalSecondParty => "external_second_party",
            AuditType::ExternalThirdParty => "external_third_party",
            AuditType::Surveillance => "surveillance",
            AuditType::Recertification => "recertification",
            AuditType::Combined => "combined",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AuditType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "internal" | "Internal" => Ok(AuditType::Internal),
                "external_second_party" | "ExternalSecondParty" => Ok(AuditType::ExternalSecondParty),
                "external_third_party" | "ExternalThirdParty" => Ok(AuditType::ExternalThirdParty),
                "surveillance" | "Surveillance" => Ok(AuditType::Surveillance),
                "recertification" | "Recertification" => Ok(AuditType::Recertification),
                "combined" | "Combined" => Ok(AuditType::Combined),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AuditType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AuditType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AuditType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['internal', 'external_second_party', 'external_third_party', 'surveillance', 'recertification', 'combined']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AnnexAControlId {
    A51,
    A52,
    A53,
    A54,
    A55,
    A56,
    A57,
    A58,
    A59,
    A510,
    A511,
    A512,
    A513,
    A514,
    A515,
    A516,
    A517,
    A518,
    A519,
    A520,
    A521,
    A522,
    A523,
    A524,
    A525,
    A526,
    A527,
    A528,
    A529,
    A530,
    A531,
    A532,
    A533,
    A534,
    A535,
    A536,
    A537,
    A61,
    A62,
    A63,
    A64,
    A65,
    A66,
    A67,
    A68,
    A71,
    A72,
    A73,
    A74,
    A75,
    A76,
    A77,
    A78,
    A79,
    A710,
    A711,
    A712,
    A713,
    A714,
    A81,
    A82,
    A83,
    A84,
    A85,
    A86,
    A87,
    A88,
    A89,
    A810,
    A811,
    A812,
    A813,
    A814,
    A815,
    A816,
    A817,
    A818,
    A819,
    A820,
    A821,
    A822,
    A823,
    A824,
    A825,
    A826,
    A827,
    A828,
    A829,
    A830,
    A831,
    A832,
    A833,
    A834,
}

impl core::fmt::Display for AnnexAControlId {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AnnexAControlId::A51 => f.write_str("a_5_1"),
            AnnexAControlId::A52 => f.write_str("a_5_2"),
            AnnexAControlId::A53 => f.write_str("a_5_3"),
            AnnexAControlId::A54 => f.write_str("a_5_4"),
            AnnexAControlId::A55 => f.write_str("a_5_5"),
            AnnexAControlId::A56 => f.write_str("a_5_6"),
            AnnexAControlId::A57 => f.write_str("a_5_7"),
            AnnexAControlId::A58 => f.write_str("a_5_8"),
            AnnexAControlId::A59 => f.write_str("a_5_9"),
            AnnexAControlId::A510 => f.write_str("a_5_10"),
            AnnexAControlId::A511 => f.write_str("a_5_11"),
            AnnexAControlId::A512 => f.write_str("a_5_12"),
            AnnexAControlId::A513 => f.write_str("a_5_13"),
            AnnexAControlId::A514 => f.write_str("a_5_14"),
            AnnexAControlId::A515 => f.write_str("a_5_15"),
            AnnexAControlId::A516 => f.write_str("a_5_16"),
            AnnexAControlId::A517 => f.write_str("a_5_17"),
            AnnexAControlId::A518 => f.write_str("a_5_18"),
            AnnexAControlId::A519 => f.write_str("a_5_19"),
            AnnexAControlId::A520 => f.write_str("a_5_20"),
            AnnexAControlId::A521 => f.write_str("a_5_21"),
            AnnexAControlId::A522 => f.write_str("a_5_22"),
            AnnexAControlId::A523 => f.write_str("a_5_23"),
            AnnexAControlId::A524 => f.write_str("a_5_24"),
            AnnexAControlId::A525 => f.write_str("a_5_25"),
            AnnexAControlId::A526 => f.write_str("a_5_26"),
            AnnexAControlId::A527 => f.write_str("a_5_27"),
            AnnexAControlId::A528 => f.write_str("a_5_28"),
            AnnexAControlId::A529 => f.write_str("a_5_29"),
            AnnexAControlId::A530 => f.write_str("a_5_30"),
            AnnexAControlId::A531 => f.write_str("a_5_31"),
            AnnexAControlId::A532 => f.write_str("a_5_32"),
            AnnexAControlId::A533 => f.write_str("a_5_33"),
            AnnexAControlId::A534 => f.write_str("a_5_34"),
            AnnexAControlId::A535 => f.write_str("a_5_35"),
            AnnexAControlId::A536 => f.write_str("a_5_36"),
            AnnexAControlId::A537 => f.write_str("a_5_37"),
            AnnexAControlId::A61 => f.write_str("a_6_1"),
            AnnexAControlId::A62 => f.write_str("a_6_2"),
            AnnexAControlId::A63 => f.write_str("a_6_3"),
            AnnexAControlId::A64 => f.write_str("a_6_4"),
            AnnexAControlId::A65 => f.write_str("a_6_5"),
            AnnexAControlId::A66 => f.write_str("a_6_6"),
            AnnexAControlId::A67 => f.write_str("a_6_7"),
            AnnexAControlId::A68 => f.write_str("a_6_8"),
            AnnexAControlId::A71 => f.write_str("a_7_1"),
            AnnexAControlId::A72 => f.write_str("a_7_2"),
            AnnexAControlId::A73 => f.write_str("a_7_3"),
            AnnexAControlId::A74 => f.write_str("a_7_4"),
            AnnexAControlId::A75 => f.write_str("a_7_5"),
            AnnexAControlId::A76 => f.write_str("a_7_6"),
            AnnexAControlId::A77 => f.write_str("a_7_7"),
            AnnexAControlId::A78 => f.write_str("a_7_8"),
            AnnexAControlId::A79 => f.write_str("a_7_9"),
            AnnexAControlId::A710 => f.write_str("a_7_10"),
            AnnexAControlId::A711 => f.write_str("a_7_11"),
            AnnexAControlId::A712 => f.write_str("a_7_12"),
            AnnexAControlId::A713 => f.write_str("a_7_13"),
            AnnexAControlId::A714 => f.write_str("a_7_14"),
            AnnexAControlId::A81 => f.write_str("a_8_1"),
            AnnexAControlId::A82 => f.write_str("a_8_2"),
            AnnexAControlId::A83 => f.write_str("a_8_3"),
            AnnexAControlId::A84 => f.write_str("a_8_4"),
            AnnexAControlId::A85 => f.write_str("a_8_5"),
            AnnexAControlId::A86 => f.write_str("a_8_6"),
            AnnexAControlId::A87 => f.write_str("a_8_7"),
            AnnexAControlId::A88 => f.write_str("a_8_8"),
            AnnexAControlId::A89 => f.write_str("a_8_9"),
            AnnexAControlId::A810 => f.write_str("a_8_10"),
            AnnexAControlId::A811 => f.write_str("a_8_11"),
            AnnexAControlId::A812 => f.write_str("a_8_12"),
            AnnexAControlId::A813 => f.write_str("a_8_13"),
            AnnexAControlId::A814 => f.write_str("a_8_14"),
            AnnexAControlId::A815 => f.write_str("a_8_15"),
            AnnexAControlId::A816 => f.write_str("a_8_16"),
            AnnexAControlId::A817 => f.write_str("a_8_17"),
            AnnexAControlId::A818 => f.write_str("a_8_18"),
            AnnexAControlId::A819 => f.write_str("a_8_19"),
            AnnexAControlId::A820 => f.write_str("a_8_20"),
            AnnexAControlId::A821 => f.write_str("a_8_21"),
            AnnexAControlId::A822 => f.write_str("a_8_22"),
            AnnexAControlId::A823 => f.write_str("a_8_23"),
            AnnexAControlId::A824 => f.write_str("a_8_24"),
            AnnexAControlId::A825 => f.write_str("a_8_25"),
            AnnexAControlId::A826 => f.write_str("a_8_26"),
            AnnexAControlId::A827 => f.write_str("a_8_27"),
            AnnexAControlId::A828 => f.write_str("a_8_28"),
            AnnexAControlId::A829 => f.write_str("a_8_29"),
            AnnexAControlId::A830 => f.write_str("a_8_30"),
            AnnexAControlId::A831 => f.write_str("a_8_31"),
            AnnexAControlId::A832 => f.write_str("a_8_32"),
            AnnexAControlId::A833 => f.write_str("a_8_33"),
            AnnexAControlId::A834 => f.write_str("a_8_34"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AnnexAControlId {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AnnexAControlId::A51 => "a_5_1",
            AnnexAControlId::A52 => "a_5_2",
            AnnexAControlId::A53 => "a_5_3",
            AnnexAControlId::A54 => "a_5_4",
            AnnexAControlId::A55 => "a_5_5",
            AnnexAControlId::A56 => "a_5_6",
            AnnexAControlId::A57 => "a_5_7",
            AnnexAControlId::A58 => "a_5_8",
            AnnexAControlId::A59 => "a_5_9",
            AnnexAControlId::A510 => "a_5_10",
            AnnexAControlId::A511 => "a_5_11",
            AnnexAControlId::A512 => "a_5_12",
            AnnexAControlId::A513 => "a_5_13",
            AnnexAControlId::A514 => "a_5_14",
            AnnexAControlId::A515 => "a_5_15",
            AnnexAControlId::A516 => "a_5_16",
            AnnexAControlId::A517 => "a_5_17",
            AnnexAControlId::A518 => "a_5_18",
            AnnexAControlId::A519 => "a_5_19",
            AnnexAControlId::A520 => "a_5_20",
            AnnexAControlId::A521 => "a_5_21",
            AnnexAControlId::A522 => "a_5_22",
            AnnexAControlId::A523 => "a_5_23",
            AnnexAControlId::A524 => "a_5_24",
            AnnexAControlId::A525 => "a_5_25",
            AnnexAControlId::A526 => "a_5_26",
            AnnexAControlId::A527 => "a_5_27",
            AnnexAControlId::A528 => "a_5_28",
            AnnexAControlId::A529 => "a_5_29",
            AnnexAControlId::A530 => "a_5_30",
            AnnexAControlId::A531 => "a_5_31",
            AnnexAControlId::A532 => "a_5_32",
            AnnexAControlId::A533 => "a_5_33",
            AnnexAControlId::A534 => "a_5_34",
            AnnexAControlId::A535 => "a_5_35",
            AnnexAControlId::A536 => "a_5_36",
            AnnexAControlId::A537 => "a_5_37",
            AnnexAControlId::A61 => "a_6_1",
            AnnexAControlId::A62 => "a_6_2",
            AnnexAControlId::A63 => "a_6_3",
            AnnexAControlId::A64 => "a_6_4",
            AnnexAControlId::A65 => "a_6_5",
            AnnexAControlId::A66 => "a_6_6",
            AnnexAControlId::A67 => "a_6_7",
            AnnexAControlId::A68 => "a_6_8",
            AnnexAControlId::A71 => "a_7_1",
            AnnexAControlId::A72 => "a_7_2",
            AnnexAControlId::A73 => "a_7_3",
            AnnexAControlId::A74 => "a_7_4",
            AnnexAControlId::A75 => "a_7_5",
            AnnexAControlId::A76 => "a_7_6",
            AnnexAControlId::A77 => "a_7_7",
            AnnexAControlId::A78 => "a_7_8",
            AnnexAControlId::A79 => "a_7_9",
            AnnexAControlId::A710 => "a_7_10",
            AnnexAControlId::A711 => "a_7_11",
            AnnexAControlId::A712 => "a_7_12",
            AnnexAControlId::A713 => "a_7_13",
            AnnexAControlId::A714 => "a_7_14",
            AnnexAControlId::A81 => "a_8_1",
            AnnexAControlId::A82 => "a_8_2",
            AnnexAControlId::A83 => "a_8_3",
            AnnexAControlId::A84 => "a_8_4",
            AnnexAControlId::A85 => "a_8_5",
            AnnexAControlId::A86 => "a_8_6",
            AnnexAControlId::A87 => "a_8_7",
            AnnexAControlId::A88 => "a_8_8",
            AnnexAControlId::A89 => "a_8_9",
            AnnexAControlId::A810 => "a_8_10",
            AnnexAControlId::A811 => "a_8_11",
            AnnexAControlId::A812 => "a_8_12",
            AnnexAControlId::A813 => "a_8_13",
            AnnexAControlId::A814 => "a_8_14",
            AnnexAControlId::A815 => "a_8_15",
            AnnexAControlId::A816 => "a_8_16",
            AnnexAControlId::A817 => "a_8_17",
            AnnexAControlId::A818 => "a_8_18",
            AnnexAControlId::A819 => "a_8_19",
            AnnexAControlId::A820 => "a_8_20",
            AnnexAControlId::A821 => "a_8_21",
            AnnexAControlId::A822 => "a_8_22",
            AnnexAControlId::A823 => "a_8_23",
            AnnexAControlId::A824 => "a_8_24",
            AnnexAControlId::A825 => "a_8_25",
            AnnexAControlId::A826 => "a_8_26",
            AnnexAControlId::A827 => "a_8_27",
            AnnexAControlId::A828 => "a_8_28",
            AnnexAControlId::A829 => "a_8_29",
            AnnexAControlId::A830 => "a_8_30",
            AnnexAControlId::A831 => "a_8_31",
            AnnexAControlId::A832 => "a_8_32",
            AnnexAControlId::A833 => "a_8_33",
            AnnexAControlId::A834 => "a_8_34",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AnnexAControlId {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "a_5_1" | "A51" => Ok(AnnexAControlId::A51),
                "a_5_2" | "A52" => Ok(AnnexAControlId::A52),
                "a_5_3" | "A53" => Ok(AnnexAControlId::A53),
                "a_5_4" | "A54" => Ok(AnnexAControlId::A54),
                "a_5_5" | "A55" => Ok(AnnexAControlId::A55),
                "a_5_6" | "A56" => Ok(AnnexAControlId::A56),
                "a_5_7" | "A57" => Ok(AnnexAControlId::A57),
                "a_5_8" | "A58" => Ok(AnnexAControlId::A58),
                "a_5_9" | "A59" => Ok(AnnexAControlId::A59),
                "a_5_10" | "A510" => Ok(AnnexAControlId::A510),
                "a_5_11" | "A511" => Ok(AnnexAControlId::A511),
                "a_5_12" | "A512" => Ok(AnnexAControlId::A512),
                "a_5_13" | "A513" => Ok(AnnexAControlId::A513),
                "a_5_14" | "A514" => Ok(AnnexAControlId::A514),
                "a_5_15" | "A515" => Ok(AnnexAControlId::A515),
                "a_5_16" | "A516" => Ok(AnnexAControlId::A516),
                "a_5_17" | "A517" => Ok(AnnexAControlId::A517),
                "a_5_18" | "A518" => Ok(AnnexAControlId::A518),
                "a_5_19" | "A519" => Ok(AnnexAControlId::A519),
                "a_5_20" | "A520" => Ok(AnnexAControlId::A520),
                "a_5_21" | "A521" => Ok(AnnexAControlId::A521),
                "a_5_22" | "A522" => Ok(AnnexAControlId::A522),
                "a_5_23" | "A523" => Ok(AnnexAControlId::A523),
                "a_5_24" | "A524" => Ok(AnnexAControlId::A524),
                "a_5_25" | "A525" => Ok(AnnexAControlId::A525),
                "a_5_26" | "A526" => Ok(AnnexAControlId::A526),
                "a_5_27" | "A527" => Ok(AnnexAControlId::A527),
                "a_5_28" | "A528" => Ok(AnnexAControlId::A528),
                "a_5_29" | "A529" => Ok(AnnexAControlId::A529),
                "a_5_30" | "A530" => Ok(AnnexAControlId::A530),
                "a_5_31" | "A531" => Ok(AnnexAControlId::A531),
                "a_5_32" | "A532" => Ok(AnnexAControlId::A532),
                "a_5_33" | "A533" => Ok(AnnexAControlId::A533),
                "a_5_34" | "A534" => Ok(AnnexAControlId::A534),
                "a_5_35" | "A535" => Ok(AnnexAControlId::A535),
                "a_5_36" | "A536" => Ok(AnnexAControlId::A536),
                "a_5_37" | "A537" => Ok(AnnexAControlId::A537),
                "a_6_1" | "A61" => Ok(AnnexAControlId::A61),
                "a_6_2" | "A62" => Ok(AnnexAControlId::A62),
                "a_6_3" | "A63" => Ok(AnnexAControlId::A63),
                "a_6_4" | "A64" => Ok(AnnexAControlId::A64),
                "a_6_5" | "A65" => Ok(AnnexAControlId::A65),
                "a_6_6" | "A66" => Ok(AnnexAControlId::A66),
                "a_6_7" | "A67" => Ok(AnnexAControlId::A67),
                "a_6_8" | "A68" => Ok(AnnexAControlId::A68),
                "a_7_1" | "A71" => Ok(AnnexAControlId::A71),
                "a_7_2" | "A72" => Ok(AnnexAControlId::A72),
                "a_7_3" | "A73" => Ok(AnnexAControlId::A73),
                "a_7_4" | "A74" => Ok(AnnexAControlId::A74),
                "a_7_5" | "A75" => Ok(AnnexAControlId::A75),
                "a_7_6" | "A76" => Ok(AnnexAControlId::A76),
                "a_7_7" | "A77" => Ok(AnnexAControlId::A77),
                "a_7_8" | "A78" => Ok(AnnexAControlId::A78),
                "a_7_9" | "A79" => Ok(AnnexAControlId::A79),
                "a_7_10" | "A710" => Ok(AnnexAControlId::A710),
                "a_7_11" | "A711" => Ok(AnnexAControlId::A711),
                "a_7_12" | "A712" => Ok(AnnexAControlId::A712),
                "a_7_13" | "A713" => Ok(AnnexAControlId::A713),
                "a_7_14" | "A714" => Ok(AnnexAControlId::A714),
                "a_8_1" | "A81" => Ok(AnnexAControlId::A81),
                "a_8_2" | "A82" => Ok(AnnexAControlId::A82),
                "a_8_3" | "A83" => Ok(AnnexAControlId::A83),
                "a_8_4" | "A84" => Ok(AnnexAControlId::A84),
                "a_8_5" | "A85" => Ok(AnnexAControlId::A85),
                "a_8_6" | "A86" => Ok(AnnexAControlId::A86),
                "a_8_7" | "A87" => Ok(AnnexAControlId::A87),
                "a_8_8" | "A88" => Ok(AnnexAControlId::A88),
                "a_8_9" | "A89" => Ok(AnnexAControlId::A89),
                "a_8_10" | "A810" => Ok(AnnexAControlId::A810),
                "a_8_11" | "A811" => Ok(AnnexAControlId::A811),
                "a_8_12" | "A812" => Ok(AnnexAControlId::A812),
                "a_8_13" | "A813" => Ok(AnnexAControlId::A813),
                "a_8_14" | "A814" => Ok(AnnexAControlId::A814),
                "a_8_15" | "A815" => Ok(AnnexAControlId::A815),
                "a_8_16" | "A816" => Ok(AnnexAControlId::A816),
                "a_8_17" | "A817" => Ok(AnnexAControlId::A817),
                "a_8_18" | "A818" => Ok(AnnexAControlId::A818),
                "a_8_19" | "A819" => Ok(AnnexAControlId::A819),
                "a_8_20" | "A820" => Ok(AnnexAControlId::A820),
                "a_8_21" | "A821" => Ok(AnnexAControlId::A821),
                "a_8_22" | "A822" => Ok(AnnexAControlId::A822),
                "a_8_23" | "A823" => Ok(AnnexAControlId::A823),
                "a_8_24" | "A824" => Ok(AnnexAControlId::A824),
                "a_8_25" | "A825" => Ok(AnnexAControlId::A825),
                "a_8_26" | "A826" => Ok(AnnexAControlId::A826),
                "a_8_27" | "A827" => Ok(AnnexAControlId::A827),
                "a_8_28" | "A828" => Ok(AnnexAControlId::A828),
                "a_8_29" | "A829" => Ok(AnnexAControlId::A829),
                "a_8_30" | "A830" => Ok(AnnexAControlId::A830),
                "a_8_31" | "A831" => Ok(AnnexAControlId::A831),
                "a_8_32" | "A832" => Ok(AnnexAControlId::A832),
                "a_8_33" | "A833" => Ok(AnnexAControlId::A833),
                "a_8_34" | "A834" => Ok(AnnexAControlId::A834),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AnnexAControlId: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AnnexAControlId)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AnnexAControlId {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum SecurityIncidentCategory {
    Malware,
    Ransomware,
    Phishing,
    SocialEngineering,
    UnauthorizedAccess,
    AccountCompromise,
    PrivilegeMisuse,
    DataBreach,
    DataLoss,
    DenialOfService,
    WebApplicationAttack,
    SupplyChain,
    InsiderThreat,
    PhysicalSecurity,
    ConfigurationError,
    CryptographicFailure,
    PolicyViolation,
    Other,
}

impl core::fmt::Display for SecurityIncidentCategory {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            SecurityIncidentCategory::Malware => f.write_str("malware"),
            SecurityIncidentCategory::Ransomware => f.write_str("ransomware"),
            SecurityIncidentCategory::Phishing => f.write_str("phishing"),
            SecurityIncidentCategory::SocialEngineering => f.write_str("social_engineering"),
            SecurityIncidentCategory::UnauthorizedAccess => f.write_str("unauthorized_access"),
            SecurityIncidentCategory::AccountCompromise => f.write_str("account_compromise"),
            SecurityIncidentCategory::PrivilegeMisuse => f.write_str("privilege_misuse"),
            SecurityIncidentCategory::DataBreach => f.write_str("data_breach"),
            SecurityIncidentCategory::DataLoss => f.write_str("data_loss"),
            SecurityIncidentCategory::DenialOfService => f.write_str("denial_of_service"),
            SecurityIncidentCategory::WebApplicationAttack => f.write_str("web_application_attack"),
            SecurityIncidentCategory::SupplyChain => f.write_str("supply_chain"),
            SecurityIncidentCategory::InsiderThreat => f.write_str("insider_threat"),
            SecurityIncidentCategory::PhysicalSecurity => f.write_str("physical_security"),
            SecurityIncidentCategory::ConfigurationError => f.write_str("configuration_error"),
            SecurityIncidentCategory::CryptographicFailure => f.write_str("cryptographic_failure"),
            SecurityIncidentCategory::PolicyViolation => f.write_str("policy_violation"),
            SecurityIncidentCategory::Other => f.write_str("other"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for SecurityIncidentCategory {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            SecurityIncidentCategory::Malware => "malware",
            SecurityIncidentCategory::Ransomware => "ransomware",
            SecurityIncidentCategory::Phishing => "phishing",
            SecurityIncidentCategory::SocialEngineering => "social_engineering",
            SecurityIncidentCategory::UnauthorizedAccess => "unauthorized_access",
            SecurityIncidentCategory::AccountCompromise => "account_compromise",
            SecurityIncidentCategory::PrivilegeMisuse => "privilege_misuse",
            SecurityIncidentCategory::DataBreach => "data_breach",
            SecurityIncidentCategory::DataLoss => "data_loss",
            SecurityIncidentCategory::DenialOfService => "denial_of_service",
            SecurityIncidentCategory::WebApplicationAttack => "web_application_attack",
            SecurityIncidentCategory::SupplyChain => "supply_chain",
            SecurityIncidentCategory::InsiderThreat => "insider_threat",
            SecurityIncidentCategory::PhysicalSecurity => "physical_security",
            SecurityIncidentCategory::ConfigurationError => "configuration_error",
            SecurityIncidentCategory::CryptographicFailure => "cryptographic_failure",
            SecurityIncidentCategory::PolicyViolation => "policy_violation",
            SecurityIncidentCategory::Other => "other",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for SecurityIncidentCategory {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "malware" | "Malware" => Ok(SecurityIncidentCategory::Malware),
                "ransomware" | "Ransomware" => Ok(SecurityIncidentCategory::Ransomware),
                "phishing" | "Phishing" => Ok(SecurityIncidentCategory::Phishing),
                "social_engineering" | "SocialEngineering" => Ok(SecurityIncidentCategory::SocialEngineering),
                "unauthorized_access" | "UnauthorizedAccess" => Ok(SecurityIncidentCategory::UnauthorizedAccess),
                "account_compromise" | "AccountCompromise" => Ok(SecurityIncidentCategory::AccountCompromise),
                "privilege_misuse" | "PrivilegeMisuse" => Ok(SecurityIncidentCategory::PrivilegeMisuse),
                "data_breach" | "DataBreach" => Ok(SecurityIncidentCategory::DataBreach),
                "data_loss" | "DataLoss" => Ok(SecurityIncidentCategory::DataLoss),
                "denial_of_service" | "DenialOfService" => Ok(SecurityIncidentCategory::DenialOfService),
                "web_application_attack" | "WebApplicationAttack" => Ok(SecurityIncidentCategory::WebApplicationAttack),
                "supply_chain" | "SupplyChain" => Ok(SecurityIncidentCategory::SupplyChain),
                "insider_threat" | "InsiderThreat" => Ok(SecurityIncidentCategory::InsiderThreat),
                "physical_security" | "PhysicalSecurity" => Ok(SecurityIncidentCategory::PhysicalSecurity),
                "configuration_error" | "ConfigurationError" => Ok(SecurityIncidentCategory::ConfigurationError),
                "cryptographic_failure" | "CryptographicFailure" => Ok(SecurityIncidentCategory::CryptographicFailure),
                "policy_violation" | "PolicyViolation" => Ok(SecurityIncidentCategory::PolicyViolation),
                "other" | "Other" => Ok(SecurityIncidentCategory::Other),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for SecurityIncidentCategory: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(SecurityIncidentCategory)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for SecurityIncidentCategory {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RelatedManagementSystem {
    IsoIec27001,
    IsoIec27701,
    IsoIec27017,
    IsoIec27018,
    IsoIec42001,
    Iso9001,
    Iso14001,
    Iso22301,
    IsoIec200001,
    Iso31000,
}

impl core::fmt::Display for RelatedManagementSystem {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RelatedManagementSystem::IsoIec27001 => f.write_str("iso_iec_27001"),
            RelatedManagementSystem::IsoIec27701 => f.write_str("iso_iec_27701"),
            RelatedManagementSystem::IsoIec27017 => f.write_str("iso_iec_27017"),
            RelatedManagementSystem::IsoIec27018 => f.write_str("iso_iec_27018"),
            RelatedManagementSystem::IsoIec42001 => f.write_str("iso_iec_42001"),
            RelatedManagementSystem::Iso9001 => f.write_str("iso_9001"),
            RelatedManagementSystem::Iso14001 => f.write_str("iso_14001"),
            RelatedManagementSystem::Iso22301 => f.write_str("iso_22301"),
            RelatedManagementSystem::IsoIec200001 => f.write_str("iso_iec_20000_1"),
            RelatedManagementSystem::Iso31000 => f.write_str("iso_31000"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RelatedManagementSystem {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RelatedManagementSystem::IsoIec27001 => "iso_iec_27001",
            RelatedManagementSystem::IsoIec27701 => "iso_iec_27701",
            RelatedManagementSystem::IsoIec27017 => "iso_iec_27017",
            RelatedManagementSystem::IsoIec27018 => "iso_iec_27018",
            RelatedManagementSystem::IsoIec42001 => "iso_iec_42001",
            RelatedManagementSystem::Iso9001 => "iso_9001",
            RelatedManagementSystem::Iso14001 => "iso_14001",
            RelatedManagementSystem::Iso22301 => "iso_22301",
            RelatedManagementSystem::IsoIec200001 => "iso_iec_20000_1",
            RelatedManagementSystem::Iso31000 => "iso_31000",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RelatedManagementSystem {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "iso_iec_27001" | "IsoIec27001" => Ok(RelatedManagementSystem::IsoIec27001),
                "iso_iec_27701" | "IsoIec27701" => Ok(RelatedManagementSystem::IsoIec27701),
                "iso_iec_27017" | "IsoIec27017" => Ok(RelatedManagementSystem::IsoIec27017),
                "iso_iec_27018" | "IsoIec27018" => Ok(RelatedManagementSystem::IsoIec27018),
                "iso_iec_42001" | "IsoIec42001" => Ok(RelatedManagementSystem::IsoIec42001),
                "iso_9001" | "Iso9001" => Ok(RelatedManagementSystem::Iso9001),
                "iso_14001" | "Iso14001" => Ok(RelatedManagementSystem::Iso14001),
                "iso_22301" | "Iso22301" => Ok(RelatedManagementSystem::Iso22301),
                "iso_iec_20000_1" | "IsoIec200001" => Ok(RelatedManagementSystem::IsoIec200001),
                "iso_31000" | "Iso31000" => Ok(RelatedManagementSystem::Iso31000),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RelatedManagementSystem: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RelatedManagementSystem)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RelatedManagementSystem {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['iso_iec_27001', 'iso_iec_27701', 'iso_iec_27017', 'iso_iec_27018', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1', 'iso_31000']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ImpactRating {
    Negligible,
    Minor,
    Moderate,
    Major,
    Severe,
}

impl core::fmt::Display for ImpactRating {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ImpactRating::Negligible => f.write_str("negligible"),
            ImpactRating::Minor => f.write_str("minor"),
            ImpactRating::Moderate => f.write_str("moderate"),
            ImpactRating::Major => f.write_str("major"),
            ImpactRating::Severe => f.write_str("severe"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ImpactRating {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ImpactRating::Negligible => "negligible",
            ImpactRating::Minor => "minor",
            ImpactRating::Moderate => "moderate",
            ImpactRating::Major => "major",
            ImpactRating::Severe => "severe",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ImpactRating {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "negligible" | "Negligible" => Ok(ImpactRating::Negligible),
                "minor" | "Minor" => Ok(ImpactRating::Minor),
                "moderate" | "Moderate" => Ok(ImpactRating::Moderate),
                "major" | "Major" => Ok(ImpactRating::Major),
                "severe" | "Severe" => Ok(ImpactRating::Severe),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ImpactRating: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ImpactRating)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ImpactRating {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['negligible', 'minor', 'moderate', 'major', 'severe']",
            "typing".into(),
        )
    }
}

// Classes

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct NamedEntity {
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl NamedEntity {
    #[new]
    #[pyo3(signature = (id, name, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        NamedEntity{id, name, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NamedEntity>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NamedEntity> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NamedEntity>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedEntity",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NamedEntity {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a NamedEntity from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum NamedEntityOrSubtype {    DocumentedInformation(DocumentedInformation),     InformationSecurityManagementSystem(InformationSecurityManagementSystem),     Organization(Organization),     InterestedParty(InterestedParty),     Role(Role),     InformationSecurityObjective(InformationSecurityObjective),     Risk(Risk),     SecurityControl(SecurityControl),     Resource(Resource),     AuditFinding(AuditFinding),     Nonconformity(Nonconformity),     CorrectiveAction(CorrectiveAction),     ImprovementOpportunity(ImprovementOpportunity),     Asset(Asset),     InformationSecurityEvent(InformationSecurityEvent),     InformationSecurityIncident(InformationSecurityIncident),     InformationSecurityPolicy(InformationSecurityPolicy),     TopicSpecificPolicy(TopicSpecificPolicy),     RiskAssessmentProcess(RiskAssessmentProcess),     RiskAssessment(RiskAssessment),     RiskTreatmentProcess(RiskTreatmentProcess),     RiskTreatmentPlan(RiskTreatmentPlan),     StatementOfApplicability(StatementOfApplicability),     CompetenceRecord(CompetenceRecord),     AwarenessProgram(AwarenessProgram),     CommunicationPlan(CommunicationPlan),     OperationalProcedure(OperationalProcedure),     MonitoringProgram(MonitoringProgram),     InternalAudit(InternalAudit),     AuditProgramme(AuditProgramme),     ManagementReview(ManagementReview)}

impl From<DocumentedInformation>   for NamedEntityOrSubtype { fn from(x: DocumentedInformation)   -> Self { Self::DocumentedInformation(x) } }
impl From<InformationSecurityManagementSystem>   for NamedEntityOrSubtype { fn from(x: InformationSecurityManagementSystem)   -> Self { Self::InformationSecurityManagementSystem(x) } }
impl From<Organization>   for NamedEntityOrSubtype { fn from(x: Organization)   -> Self { Self::Organization(x) } }
impl From<InterestedParty>   for NamedEntityOrSubtype { fn from(x: InterestedParty)   -> Self { Self::InterestedParty(x) } }
impl From<Role>   for NamedEntityOrSubtype { fn from(x: Role)   -> Self { Self::Role(x) } }
impl From<InformationSecurityObjective>   for NamedEntityOrSubtype { fn from(x: InformationSecurityObjective)   -> Self { Self::InformationSecurityObjective(x) } }
impl From<Risk>   for NamedEntityOrSubtype { fn from(x: Risk)   -> Self { Self::Risk(x) } }
impl From<SecurityControl>   for NamedEntityOrSubtype { fn from(x: SecurityControl)   -> Self { Self::SecurityControl(x) } }
impl From<Resource>   for NamedEntityOrSubtype { fn from(x: Resource)   -> Self { Self::Resource(x) } }
impl From<AuditFinding>   for NamedEntityOrSubtype { fn from(x: AuditFinding)   -> Self { Self::AuditFinding(x) } }
impl From<Nonconformity>   for NamedEntityOrSubtype { fn from(x: Nonconformity)   -> Self { Self::Nonconformity(x) } }
impl From<CorrectiveAction>   for NamedEntityOrSubtype { fn from(x: CorrectiveAction)   -> Self { Self::CorrectiveAction(x) } }
impl From<ImprovementOpportunity>   for NamedEntityOrSubtype { fn from(x: ImprovementOpportunity)   -> Self { Self::ImprovementOpportunity(x) } }
impl From<Asset>   for NamedEntityOrSubtype { fn from(x: Asset)   -> Self { Self::Asset(x) } }
impl From<InformationSecurityEvent>   for NamedEntityOrSubtype { fn from(x: InformationSecurityEvent)   -> Self { Self::InformationSecurityEvent(x) } }
impl From<InformationSecurityIncident>   for NamedEntityOrSubtype { fn from(x: InformationSecurityIncident)   -> Self { Self::InformationSecurityIncident(x) } }
impl From<InformationSecurityPolicy>   for NamedEntityOrSubtype { fn from(x: InformationSecurityPolicy)   -> Self { Self::InformationSecurityPolicy(x) } }
impl From<TopicSpecificPolicy>   for NamedEntityOrSubtype { fn from(x: TopicSpecificPolicy)   -> Self { Self::TopicSpecificPolicy(x) } }
impl From<RiskAssessmentProcess>   for NamedEntityOrSubtype { fn from(x: RiskAssessmentProcess)   -> Self { Self::RiskAssessmentProcess(x) } }
impl From<RiskAssessment>   for NamedEntityOrSubtype { fn from(x: RiskAssessment)   -> Self { Self::RiskAssessment(x) } }
impl From<RiskTreatmentProcess>   for NamedEntityOrSubtype { fn from(x: RiskTreatmentProcess)   -> Self { Self::RiskTreatmentProcess(x) } }
impl From<RiskTreatmentPlan>   for NamedEntityOrSubtype { fn from(x: RiskTreatmentPlan)   -> Self { Self::RiskTreatmentPlan(x) } }
impl From<StatementOfApplicability>   for NamedEntityOrSubtype { fn from(x: StatementOfApplicability)   -> Self { Self::StatementOfApplicability(x) } }
impl From<CompetenceRecord>   for NamedEntityOrSubtype { fn from(x: CompetenceRecord)   -> Self { Self::CompetenceRecord(x) } }
impl From<AwarenessProgram>   for NamedEntityOrSubtype { fn from(x: AwarenessProgram)   -> Self { Self::AwarenessProgram(x) } }
impl From<CommunicationPlan>   for NamedEntityOrSubtype { fn from(x: CommunicationPlan)   -> Self { Self::CommunicationPlan(x) } }
impl From<OperationalProcedure>   for NamedEntityOrSubtype { fn from(x: OperationalProcedure)   -> Self { Self::OperationalProcedure(x) } }
impl From<MonitoringProgram>   for NamedEntityOrSubtype { fn from(x: MonitoringProgram)   -> Self { Self::MonitoringProgram(x) } }
impl From<InternalAudit>   for NamedEntityOrSubtype { fn from(x: InternalAudit)   -> Self { Self::InternalAudit(x) } }
impl From<AuditProgramme>   for NamedEntityOrSubtype { fn from(x: AuditProgramme)   -> Self { Self::AuditProgramme(x) } }
impl From<ManagementReview>   for NamedEntityOrSubtype { fn from(x: ManagementReview)   -> Self { Self::ManagementReview(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NamedEntityOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<DocumentedInformation>() {
            return Ok(NamedEntityOrSubtype::DocumentedInformation(val));
        }        if let Ok(val) = ob.extract::<InformationSecurityManagementSystem>() {
            return Ok(NamedEntityOrSubtype::InformationSecurityManagementSystem(val));
        }        if let Ok(val) = ob.extract::<Organization>() {
            return Ok(NamedEntityOrSubtype::Organization(val));
        }        if let Ok(val) = ob.extract::<InterestedParty>() {
            return Ok(NamedEntityOrSubtype::InterestedParty(val));
        }        if let Ok(val) = ob.extract::<Role>() {
            return Ok(NamedEntityOrSubtype::Role(val));
        }        if let Ok(val) = ob.extract::<InformationSecurityObjective>() {
            return Ok(NamedEntityOrSubtype::InformationSecurityObjective(val));
        }        if let Ok(val) = ob.extract::<Risk>() {
            return Ok(NamedEntityOrSubtype::Risk(val));
        }        if let Ok(val) = ob.extract::<SecurityControl>() {
            return Ok(NamedEntityOrSubtype::SecurityControl(val));
        }        if let Ok(val) = ob.extract::<Resource>() {
            return Ok(NamedEntityOrSubtype::Resource(val));
        }        if let Ok(val) = ob.extract::<AuditFinding>() {
            return Ok(NamedEntityOrSubtype::AuditFinding(val));
        }        if let Ok(val) = ob.extract::<Nonconformity>() {
            return Ok(NamedEntityOrSubtype::Nonconformity(val));
        }        if let Ok(val) = ob.extract::<CorrectiveAction>() {
            return Ok(NamedEntityOrSubtype::CorrectiveAction(val));
        }        if let Ok(val) = ob.extract::<ImprovementOpportunity>() {
            return Ok(NamedEntityOrSubtype::ImprovementOpportunity(val));
        }        if let Ok(val) = ob.extract::<Asset>() {
            return Ok(NamedEntityOrSubtype::Asset(val));
        }        if let Ok(val) = ob.extract::<InformationSecurityEvent>() {
            return Ok(NamedEntityOrSubtype::InformationSecurityEvent(val));
        }        if let Ok(val) = ob.extract::<InformationSecurityIncident>() {
            return Ok(NamedEntityOrSubtype::InformationSecurityIncident(val));
        }        if let Ok(val) = ob.extract::<InformationSecurityPolicy>() {
            return Ok(NamedEntityOrSubtype::InformationSecurityPolicy(val));
        }        if let Ok(val) = ob.extract::<TopicSpecificPolicy>() {
            return Ok(NamedEntityOrSubtype::TopicSpecificPolicy(val));
        }        if let Ok(val) = ob.extract::<RiskAssessmentProcess>() {
            return Ok(NamedEntityOrSubtype::RiskAssessmentProcess(val));
        }        if let Ok(val) = ob.extract::<RiskAssessment>() {
            return Ok(NamedEntityOrSubtype::RiskAssessment(val));
        }        if let Ok(val) = ob.extract::<RiskTreatmentProcess>() {
            return Ok(NamedEntityOrSubtype::RiskTreatmentProcess(val));
        }        if let Ok(val) = ob.extract::<RiskTreatmentPlan>() {
            return Ok(NamedEntityOrSubtype::RiskTreatmentPlan(val));
        }        if let Ok(val) = ob.extract::<StatementOfApplicability>() {
            return Ok(NamedEntityOrSubtype::StatementOfApplicability(val));
        }        if let Ok(val) = ob.extract::<CompetenceRecord>() {
            return Ok(NamedEntityOrSubtype::CompetenceRecord(val));
        }        if let Ok(val) = ob.extract::<AwarenessProgram>() {
            return Ok(NamedEntityOrSubtype::AwarenessProgram(val));
        }        if let Ok(val) = ob.extract::<CommunicationPlan>() {
            return Ok(NamedEntityOrSubtype::CommunicationPlan(val));
        }        if let Ok(val) = ob.extract::<OperationalProcedure>() {
            return Ok(NamedEntityOrSubtype::OperationalProcedure(val));
        }        if let Ok(val) = ob.extract::<MonitoringProgram>() {
            return Ok(NamedEntityOrSubtype::MonitoringProgram(val));
        }        if let Ok(val) = ob.extract::<InternalAudit>() {
            return Ok(NamedEntityOrSubtype::InternalAudit(val));
        }        if let Ok(val) = ob.extract::<AuditProgramme>() {
            return Ok(NamedEntityOrSubtype::AuditProgramme(val));
        }        if let Ok(val) = ob.extract::<ManagementReview>() {
            return Ok(NamedEntityOrSubtype::ManagementReview(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedEntityOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NamedEntityOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            NamedEntityOrSubtype::DocumentedInformation(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Organization(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InterestedParty(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Role(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InformationSecurityObjective(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Risk(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::SecurityControl(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Resource(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::AuditFinding(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Nonconformity(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::CorrectiveAction(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::ImprovementOpportunity(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::Asset(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InformationSecurityEvent(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InformationSecurityIncident(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::RiskAssessment(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::StatementOfApplicability(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::CompetenceRecord(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::AwarenessProgram(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::CommunicationPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::OperationalProcedure(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::MonitoringProgram(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::InternalAudit(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::AuditProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedEntityOrSubtype::ManagementReview(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NamedEntityOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NamedEntityOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NamedEntityOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedEntityOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NamedEntityOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = DocumentedInformation::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::DocumentedInformation(x));
        }
        if let Ok(x) = InformationSecurityManagementSystem::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityManagementSystem(x));
        }
        if let Ok(x) = Organization::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Organization(x));
        }
        if let Ok(x) = InterestedParty::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InterestedParty(x));
        }
        if let Ok(x) = Role::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Role(x));
        }
        if let Ok(x) = InformationSecurityObjective::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityObjective(x));
        }
        if let Ok(x) = Risk::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Risk(x));
        }
        if let Ok(x) = SecurityControl::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::SecurityControl(x));
        }
        if let Ok(x) = Resource::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Resource(x));
        }
        if let Ok(x) = AuditFinding::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AuditFinding(x));
        }
        if let Ok(x) = Nonconformity::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Nonconformity(x));
        }
        if let Ok(x) = CorrectiveAction::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CorrectiveAction(x));
        }
        if let Ok(x) = ImprovementOpportunity::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::ImprovementOpportunity(x));
        }
        if let Ok(x) = Asset::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Asset(x));
        }
        if let Ok(x) = InformationSecurityEvent::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityEvent(x));
        }
        if let Ok(x) = InformationSecurityIncident::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityIncident(x));
        }
        if let Ok(x) = InformationSecurityPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityPolicy(x));
        }
        if let Ok(x) = TopicSpecificPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::TopicSpecificPolicy(x));
        }
        if let Ok(x) = RiskAssessmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskAssessmentProcess(x));
        }
        if let Ok(x) = RiskAssessment::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskAssessment(x));
        }
        if let Ok(x) = RiskTreatmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskTreatmentProcess(x));
        }
        if let Ok(x) = RiskTreatmentPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskTreatmentPlan(x));
        }
        if let Ok(x) = StatementOfApplicability::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::StatementOfApplicability(x));
        }
        if let Ok(x) = CompetenceRecord::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CompetenceRecord(x));
        }
        if let Ok(x) = AwarenessProgram::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AwarenessProgram(x));
        }
        if let Ok(x) = CommunicationPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CommunicationPlan(x));
        }
        if let Ok(x) = OperationalProcedure::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::OperationalProcedure(x));
        }
        if let Ok(x) = MonitoringProgram::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::MonitoringProgram(x));
        }
        if let Ok(x) = InternalAudit::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InternalAudit(x));
        }
        if let Ok(x) = AuditProgramme::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AuditProgramme(x));
        }
        if let Ok(x) = ManagementReview::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::ManagementReview(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = DocumentedInformation::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::DocumentedInformation(x));
        }
        if let Ok(x) = InformationSecurityManagementSystem::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityManagementSystem(x));
        }
        if let Ok(x) = Organization::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Organization(x));
        }
        if let Ok(x) = InterestedParty::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InterestedParty(x));
        }
        if let Ok(x) = Role::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Role(x));
        }
        if let Ok(x) = InformationSecurityObjective::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityObjective(x));
        }
        if let Ok(x) = Risk::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Risk(x));
        }
        if let Ok(x) = SecurityControl::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::SecurityControl(x));
        }
        if let Ok(x) = Resource::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Resource(x));
        }
        if let Ok(x) = AuditFinding::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AuditFinding(x));
        }
        if let Ok(x) = Nonconformity::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Nonconformity(x));
        }
        if let Ok(x) = CorrectiveAction::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CorrectiveAction(x));
        }
        if let Ok(x) = ImprovementOpportunity::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::ImprovementOpportunity(x));
        }
        if let Ok(x) = Asset::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::Asset(x));
        }
        if let Ok(x) = InformationSecurityEvent::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityEvent(x));
        }
        if let Ok(x) = InformationSecurityIncident::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityIncident(x));
        }
        if let Ok(x) = InformationSecurityPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InformationSecurityPolicy(x));
        }
        if let Ok(x) = TopicSpecificPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::TopicSpecificPolicy(x));
        }
        if let Ok(x) = RiskAssessmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskAssessmentProcess(x));
        }
        if let Ok(x) = RiskAssessment::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskAssessment(x));
        }
        if let Ok(x) = RiskTreatmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskTreatmentProcess(x));
        }
        if let Ok(x) = RiskTreatmentPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::RiskTreatmentPlan(x));
        }
        if let Ok(x) = StatementOfApplicability::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::StatementOfApplicability(x));
        }
        if let Ok(x) = CompetenceRecord::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CompetenceRecord(x));
        }
        if let Ok(x) = AwarenessProgram::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AwarenessProgram(x));
        }
        if let Ok(x) = CommunicationPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::CommunicationPlan(x));
        }
        if let Ok(x) = OperationalProcedure::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::OperationalProcedure(x));
        }
        if let Ok(x) = MonitoringProgram::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::MonitoringProgram(x));
        }
        if let Ok(x) = InternalAudit::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::InternalAudit(x));
        }
        if let Ok(x) = AuditProgramme::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::AuditProgramme(x));
        }
        if let Ok(x) = ManagementReview::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedEntityOrSubtype::ManagementReview(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            NamedEntityOrSubtype::DocumentedInformation(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InformationSecurityManagementSystem(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Organization(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InterestedParty(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Role(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InformationSecurityObjective(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Risk(inner) => inner.extract_key(),
            NamedEntityOrSubtype::SecurityControl(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Resource(inner) => inner.extract_key(),
            NamedEntityOrSubtype::AuditFinding(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Nonconformity(inner) => inner.extract_key(),
            NamedEntityOrSubtype::CorrectiveAction(inner) => inner.extract_key(),
            NamedEntityOrSubtype::ImprovementOpportunity(inner) => inner.extract_key(),
            NamedEntityOrSubtype::Asset(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InformationSecurityEvent(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InformationSecurityIncident(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InformationSecurityPolicy(inner) => inner.extract_key(),
            NamedEntityOrSubtype::TopicSpecificPolicy(inner) => inner.extract_key(),
            NamedEntityOrSubtype::RiskAssessmentProcess(inner) => inner.extract_key(),
            NamedEntityOrSubtype::RiskAssessment(inner) => inner.extract_key(),
            NamedEntityOrSubtype::RiskTreatmentProcess(inner) => inner.extract_key(),
            NamedEntityOrSubtype::RiskTreatmentPlan(inner) => inner.extract_key(),
            NamedEntityOrSubtype::StatementOfApplicability(inner) => inner.extract_key(),
            NamedEntityOrSubtype::CompetenceRecord(inner) => inner.extract_key(),
            NamedEntityOrSubtype::AwarenessProgram(inner) => inner.extract_key(),
            NamedEntityOrSubtype::CommunicationPlan(inner) => inner.extract_key(),
            NamedEntityOrSubtype::OperationalProcedure(inner) => inner.extract_key(),
            NamedEntityOrSubtype::MonitoringProgram(inner) => inner.extract_key(),
            NamedEntityOrSubtype::InternalAudit(inner) => inner.extract_key(),
            NamedEntityOrSubtype::AuditProgramme(inner) => inner.extract_key(),
            NamedEntityOrSubtype::ManagementReview(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(NamedEntityOrSubtype = DocumentedInformation | InformationSecurityManagementSystem | Organization | InterestedParty | Role | InformationSecurityObjective | Risk | SecurityControl | Resource | AuditFinding | Nonconformity | CorrectiveAction | ImprovementOpportunity | Asset | InformationSecurityEvent | InformationSecurityIncident | InformationSecurityPolicy | TopicSpecificPolicy | RiskAssessmentProcess | RiskAssessment | RiskTreatmentProcess | RiskTreatmentPlan | StatementOfApplicability | CompetenceRecord | AwarenessProgram | CommunicationPlan | OperationalProcedure | MonitoringProgram | InternalAudit | AuditProgramme | ManagementReview);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct DocumentedInformation {
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl DocumentedInformation {
    #[new]
    #[pyo3(signature = (id, name, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        DocumentedInformation{id, name, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<DocumentedInformation>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<DocumentedInformation> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<DocumentedInformation>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid DocumentedInformation",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for DocumentedInformation {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a DocumentedInformation from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum DocumentedInformationOrSubtype {    InformationSecurityPolicy(InformationSecurityPolicy),     TopicSpecificPolicy(TopicSpecificPolicy),     RiskAssessmentProcess(RiskAssessmentProcess),     RiskAssessment(RiskAssessment),     RiskTreatmentProcess(RiskTreatmentProcess),     RiskTreatmentPlan(RiskTreatmentPlan),     StatementOfApplicability(StatementOfApplicability),     CompetenceRecord(CompetenceRecord),     AwarenessProgram(AwarenessProgram),     CommunicationPlan(CommunicationPlan),     OperationalProcedure(OperationalProcedure),     MonitoringProgram(MonitoringProgram),     InternalAudit(InternalAudit),     AuditProgramme(AuditProgramme),     ManagementReview(ManagementReview)}

impl From<InformationSecurityPolicy>   for DocumentedInformationOrSubtype { fn from(x: InformationSecurityPolicy)   -> Self { Self::InformationSecurityPolicy(x) } }
impl From<TopicSpecificPolicy>   for DocumentedInformationOrSubtype { fn from(x: TopicSpecificPolicy)   -> Self { Self::TopicSpecificPolicy(x) } }
impl From<RiskAssessmentProcess>   for DocumentedInformationOrSubtype { fn from(x: RiskAssessmentProcess)   -> Self { Self::RiskAssessmentProcess(x) } }
impl From<RiskAssessment>   for DocumentedInformationOrSubtype { fn from(x: RiskAssessment)   -> Self { Self::RiskAssessment(x) } }
impl From<RiskTreatmentProcess>   for DocumentedInformationOrSubtype { fn from(x: RiskTreatmentProcess)   -> Self { Self::RiskTreatmentProcess(x) } }
impl From<RiskTreatmentPlan>   for DocumentedInformationOrSubtype { fn from(x: RiskTreatmentPlan)   -> Self { Self::RiskTreatmentPlan(x) } }
impl From<StatementOfApplicability>   for DocumentedInformationOrSubtype { fn from(x: StatementOfApplicability)   -> Self { Self::StatementOfApplicability(x) } }
impl From<CompetenceRecord>   for DocumentedInformationOrSubtype { fn from(x: CompetenceRecord)   -> Self { Self::CompetenceRecord(x) } }
impl From<AwarenessProgram>   for DocumentedInformationOrSubtype { fn from(x: AwarenessProgram)   -> Self { Self::AwarenessProgram(x) } }
impl From<CommunicationPlan>   for DocumentedInformationOrSubtype { fn from(x: CommunicationPlan)   -> Self { Self::CommunicationPlan(x) } }
impl From<OperationalProcedure>   for DocumentedInformationOrSubtype { fn from(x: OperationalProcedure)   -> Self { Self::OperationalProcedure(x) } }
impl From<MonitoringProgram>   for DocumentedInformationOrSubtype { fn from(x: MonitoringProgram)   -> Self { Self::MonitoringProgram(x) } }
impl From<InternalAudit>   for DocumentedInformationOrSubtype { fn from(x: InternalAudit)   -> Self { Self::InternalAudit(x) } }
impl From<AuditProgramme>   for DocumentedInformationOrSubtype { fn from(x: AuditProgramme)   -> Self { Self::AuditProgramme(x) } }
impl From<ManagementReview>   for DocumentedInformationOrSubtype { fn from(x: ManagementReview)   -> Self { Self::ManagementReview(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for DocumentedInformationOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityPolicy>() {
            return Ok(DocumentedInformationOrSubtype::InformationSecurityPolicy(val));
        }        if let Ok(val) = ob.extract::<TopicSpecificPolicy>() {
            return Ok(DocumentedInformationOrSubtype::TopicSpecificPolicy(val));
        }        if let Ok(val) = ob.extract::<RiskAssessmentProcess>() {
            return Ok(DocumentedInformationOrSubtype::RiskAssessmentProcess(val));
        }        if let Ok(val) = ob.extract::<RiskAssessment>() {
            return Ok(DocumentedInformationOrSubtype::RiskAssessment(val));
        }        if let Ok(val) = ob.extract::<RiskTreatmentProcess>() {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentProcess(val));
        }        if let Ok(val) = ob.extract::<RiskTreatmentPlan>() {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentPlan(val));
        }        if let Ok(val) = ob.extract::<StatementOfApplicability>() {
            return Ok(DocumentedInformationOrSubtype::StatementOfApplicability(val));
        }        if let Ok(val) = ob.extract::<CompetenceRecord>() {
            return Ok(DocumentedInformationOrSubtype::CompetenceRecord(val));
        }        if let Ok(val) = ob.extract::<AwarenessProgram>() {
            return Ok(DocumentedInformationOrSubtype::AwarenessProgram(val));
        }        if let Ok(val) = ob.extract::<CommunicationPlan>() {
            return Ok(DocumentedInformationOrSubtype::CommunicationPlan(val));
        }        if let Ok(val) = ob.extract::<OperationalProcedure>() {
            return Ok(DocumentedInformationOrSubtype::OperationalProcedure(val));
        }        if let Ok(val) = ob.extract::<MonitoringProgram>() {
            return Ok(DocumentedInformationOrSubtype::MonitoringProgram(val));
        }        if let Ok(val) = ob.extract::<InternalAudit>() {
            return Ok(DocumentedInformationOrSubtype::InternalAudit(val));
        }        if let Ok(val) = ob.extract::<AuditProgramme>() {
            return Ok(DocumentedInformationOrSubtype::AuditProgramme(val));
        }        if let Ok(val) = ob.extract::<ManagementReview>() {
            return Ok(DocumentedInformationOrSubtype::ManagementReview(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid DocumentedInformationOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for DocumentedInformationOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::RiskAssessment(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::CompetenceRecord(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::AwarenessProgram(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::CommunicationPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::OperationalProcedure(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::MonitoringProgram(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::InternalAudit(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::AuditProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            DocumentedInformationOrSubtype::ManagementReview(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<DocumentedInformationOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<DocumentedInformationOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<DocumentedInformationOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid DocumentedInformationOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for DocumentedInformationOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = InformationSecurityPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::InformationSecurityPolicy(x));
        }
        if let Ok(x) = TopicSpecificPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::TopicSpecificPolicy(x));
        }
        if let Ok(x) = RiskAssessmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskAssessmentProcess(x));
        }
        if let Ok(x) = RiskAssessment::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskAssessment(x));
        }
        if let Ok(x) = RiskTreatmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentProcess(x));
        }
        if let Ok(x) = RiskTreatmentPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentPlan(x));
        }
        if let Ok(x) = StatementOfApplicability::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::StatementOfApplicability(x));
        }
        if let Ok(x) = CompetenceRecord::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::CompetenceRecord(x));
        }
        if let Ok(x) = AwarenessProgram::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::AwarenessProgram(x));
        }
        if let Ok(x) = CommunicationPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::CommunicationPlan(x));
        }
        if let Ok(x) = OperationalProcedure::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::OperationalProcedure(x));
        }
        if let Ok(x) = MonitoringProgram::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::MonitoringProgram(x));
        }
        if let Ok(x) = InternalAudit::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::InternalAudit(x));
        }
        if let Ok(x) = AuditProgramme::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::AuditProgramme(x));
        }
        if let Ok(x) = ManagementReview::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::ManagementReview(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = InformationSecurityPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::InformationSecurityPolicy(x));
        }
        if let Ok(x) = TopicSpecificPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::TopicSpecificPolicy(x));
        }
        if let Ok(x) = RiskAssessmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskAssessmentProcess(x));
        }
        if let Ok(x) = RiskAssessment::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskAssessment(x));
        }
        if let Ok(x) = RiskTreatmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentProcess(x));
        }
        if let Ok(x) = RiskTreatmentPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::RiskTreatmentPlan(x));
        }
        if let Ok(x) = StatementOfApplicability::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::StatementOfApplicability(x));
        }
        if let Ok(x) = CompetenceRecord::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::CompetenceRecord(x));
        }
        if let Ok(x) = AwarenessProgram::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::AwarenessProgram(x));
        }
        if let Ok(x) = CommunicationPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::CommunicationPlan(x));
        }
        if let Ok(x) = OperationalProcedure::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::OperationalProcedure(x));
        }
        if let Ok(x) = MonitoringProgram::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::MonitoringProgram(x));
        }
        if let Ok(x) = InternalAudit::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::InternalAudit(x));
        }
        if let Ok(x) = AuditProgramme::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::AuditProgramme(x));
        }
        if let Ok(x) = ManagementReview::from_pair_simple(k.clone(), v.clone()) {
            return Ok(DocumentedInformationOrSubtype::ManagementReview(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            DocumentedInformationOrSubtype::InformationSecurityPolicy(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::TopicSpecificPolicy(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::RiskAssessmentProcess(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::RiskAssessment(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::RiskTreatmentProcess(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::RiskTreatmentPlan(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::StatementOfApplicability(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::CompetenceRecord(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::AwarenessProgram(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::CommunicationPlan(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::OperationalProcedure(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::MonitoringProgram(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::InternalAudit(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::AuditProgramme(inner) => inner.extract_key(),
            DocumentedInformationOrSubtype::ManagementReview(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(DocumentedInformationOrSubtype = InformationSecurityPolicy | TopicSpecificPolicy | RiskAssessmentProcess | RiskAssessment | RiskTreatmentProcess | RiskTreatmentPlan | StatementOfApplicability | CompetenceRecord | AwarenessProgram | CommunicationPlan | OperationalProcedure | MonitoringProgram | InternalAudit | AuditProgramme | ManagementReview);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InformationSecurityManagementSystem {
    #[cfg_attr(feature = "serde", serde(default))]
    pub organization: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub top_management: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub governing_body: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub leadership_commitment_evidence: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub scope_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub scope_boundaries: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub scope_exclusions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub interfaces_and_dependencies: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub processes_and_interactions: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub context_internal_issues: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub context_external_issues: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub interested_parties: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub information_security_policy: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub objectives: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub risks_and_opportunities_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub planned_changes: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub externally_provided_services: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_assessment_process: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_treatment_process: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub statement_of_applicability: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub roles: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub resources: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub competence_records: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub awareness_program: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub communication_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub documented_information_register: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub operational_procedures: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_assessments: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_treatment_plans: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub monitoring_program: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub internal_audits: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub management_reviews: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nonconformities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub corrective_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub improvements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub certification_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub certification_body: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub certification_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub recertification_date: Option<NaiveDate>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InformationSecurityManagementSystem {
    #[new]
    #[pyo3(signature = (id, name, organization=None, top_management=None, governing_body=None, leadership_commitment_evidence=None, scope_statement=None, scope_boundaries=None, scope_exclusions=None, interfaces_and_dependencies=None, processes_and_interactions=None, context_internal_issues=None, context_external_issues=None, interested_parties=None, information_security_policy=None, objectives=None, risks_and_opportunities_actions=None, planned_changes=None, externally_provided_services=None, risk_assessment_process=None, risk_treatment_process=None, statement_of_applicability=None, controls=None, roles=None, resources=None, competence_records=None, awareness_program=None, communication_plan=None, documented_information_register=None, operational_procedures=None, risk_assessments=None, risk_treatment_plans=None, monitoring_program=None, internal_audits=None, management_reviews=None, nonconformities=None, corrective_actions=None, improvements=None, certification_status=None, certification_body=None, certification_date=None, recertification_date=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, organization: Option<String>, top_management: Option<String>, governing_body: Option<String>, leadership_commitment_evidence: Option<Vec<String>>, scope_statement: Option<String>, scope_boundaries: Option<Vec<String>>, scope_exclusions: Option<Vec<String>>, interfaces_and_dependencies: Option<Vec<String>>, processes_and_interactions: Option<String>, context_internal_issues: Option<Vec<String>>, context_external_issues: Option<Vec<String>>, interested_parties: Option<Vec<String>>, information_security_policy: Option<String>, objectives: Option<Vec<String>>, risks_and_opportunities_actions: Option<Vec<String>>, planned_changes: Option<Vec<String>>, externally_provided_services: Option<Vec<String>>, risk_assessment_process: Option<String>, risk_treatment_process: Option<String>, statement_of_applicability: Option<String>, controls: Option<Vec<String>>, roles: Option<Vec<String>>, resources: Option<Vec<String>>, competence_records: Option<Vec<String>>, awareness_program: Option<String>, communication_plan: Option<String>, documented_information_register: Option<Vec<String>>, operational_procedures: Option<Vec<String>>, risk_assessments: Option<Vec<String>>, risk_treatment_plans: Option<Vec<String>>, monitoring_program: Option<String>, internal_audits: Option<Vec<String>>, management_reviews: Option<Vec<String>>, nonconformities: Option<Vec<String>>, corrective_actions: Option<Vec<String>>, improvements: Option<Vec<String>>, certification_status: Option<String>, certification_body: Option<String>, certification_date: Option<NaiveDate>, recertification_date: Option<NaiveDate>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InformationSecurityManagementSystem{id, name, organization, top_management, governing_body, leadership_commitment_evidence, scope_statement, scope_boundaries, scope_exclusions, interfaces_and_dependencies, processes_and_interactions, context_internal_issues, context_external_issues, interested_parties, information_security_policy, objectives, risks_and_opportunities_actions, planned_changes, externally_provided_services, risk_assessment_process, risk_treatment_process, statement_of_applicability, controls, roles, resources, competence_records, awareness_program, communication_plan, documented_information_register, operational_procedures, risk_assessments, risk_treatment_plans, monitoring_program, internal_audits, management_reviews, nonconformities, corrective_actions, improvements, certification_status, certification_body, certification_date, recertification_date, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InformationSecurityManagementSystem>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InformationSecurityManagementSystem> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityManagementSystem>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InformationSecurityManagementSystem",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InformationSecurityManagementSystem {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InformationSecurityManagementSystem from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Organization {
    #[cfg_attr(feature = "serde", serde(default))]
    pub legal_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trading_names: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub organization_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub industry_sector: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub size_category: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub employee_count: Option<isize>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub geographic_locations: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub regulatory_jurisdictions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub parent_organization: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub subsidiaries: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub climate_change_relevant: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Organization {
    #[new]
    #[pyo3(signature = (id, name, legal_name=None, trading_names=None, organization_type=None, industry_sector=None, size_category=None, employee_count=None, geographic_locations=None, regulatory_jurisdictions=None, parent_organization=None, subsidiaries=None, climate_change_relevant=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, legal_name: Option<String>, trading_names: Option<Vec<String>>, organization_type: Option<String>, industry_sector: Option<String>, size_category: Option<String>, employee_count: Option<isize>, geographic_locations: Option<Vec<String>>, regulatory_jurisdictions: Option<Vec<String>>, parent_organization: Option<String>, subsidiaries: Option<Vec<String>>, climate_change_relevant: Option<bool>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Organization{id, name, legal_name, trading_names, organization_type, industry_sector, size_category, employee_count, geographic_locations, regulatory_jurisdictions, parent_organization, subsidiaries, climate_change_relevant, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Organization>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Organization> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Organization>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Organization",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Organization {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Organization from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InterestedParty {
    #[cfg_attr(feature = "serde", serde(default))]
    pub party_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub relationship: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub addressed_requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub climate_change_related_requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub communication_needs: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub contact_information: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InterestedParty {
    #[new]
    #[pyo3(signature = (id, name, party_type=None, relationship=None, requirements=None, addressed_requirements=None, climate_change_related_requirements=None, communication_needs=None, contact_information=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, party_type: Option<String>, relationship: Option<String>, requirements: Option<Vec<String>>, addressed_requirements: Option<Vec<String>>, climate_change_related_requirements: Option<Vec<String>>, communication_needs: Option<String>, contact_information: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InterestedParty{id, name, party_type, relationship, requirements, addressed_requirements, climate_change_related_requirements, communication_needs, contact_information, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InterestedParty>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InterestedParty> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InterestedParty>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InterestedParty",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InterestedParty {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InterestedParty from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InformationSecurityPolicy {
    #[cfg_attr(feature = "serde", serde(default))]
    pub policy_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub policy_objectives_framework: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub commitment_statements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applicability_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub communication_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub acknowledgment_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub last_policy_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub next_policy_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_topic_policies: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub integrated_management_systems: Option<Vec<RelatedManagementSystem>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InformationSecurityPolicy {
    #[new]
    #[pyo3(signature = (id, name, policy_statement=None, policy_objectives_framework=None, commitment_statements=None, applicability_statement=None, communication_date=None, acknowledgment_required=None, last_policy_review_date=None, next_policy_review_date=None, related_topic_policies=None, integrated_management_systems=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, policy_statement: Option<String>, policy_objectives_framework: Option<String>, commitment_statements: Option<Vec<String>>, applicability_statement: Option<String>, communication_date: Option<NaiveDate>, acknowledgment_required: Option<bool>, last_policy_review_date: Option<NaiveDate>, next_policy_review_date: Option<NaiveDate>, related_topic_policies: Option<Vec<String>>, integrated_management_systems: Option<Vec<RelatedManagementSystem>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InformationSecurityPolicy{id, name, policy_statement, policy_objectives_framework, commitment_statements, applicability_statement, communication_date, acknowledgment_required, last_policy_review_date, next_policy_review_date, related_topic_policies, integrated_management_systems, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InformationSecurityPolicy>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InformationSecurityPolicy> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityPolicy>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InformationSecurityPolicy",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InformationSecurityPolicy {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InformationSecurityPolicy from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TopicSpecificPolicy {
    #[cfg_attr(feature = "serde", serde(default))]
    pub topic_area: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub parent_policy: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applicable_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_audience: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TopicSpecificPolicy {
    #[new]
    #[pyo3(signature = (id, name, topic_area=None, parent_policy=None, applicable_controls=None, target_audience=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, topic_area: Option<String>, parent_policy: Option<String>, applicable_controls: Option<Vec<String>>, target_audience: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        TopicSpecificPolicy{id, name, topic_area, parent_policy, applicable_controls, target_audience, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TopicSpecificPolicy>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TopicSpecificPolicy> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TopicSpecificPolicy>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TopicSpecificPolicy",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TopicSpecificPolicy {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TopicSpecificPolicy from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Role {
    #[cfg_attr(feature = "serde", serde(default))]
    pub role_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsibilities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub authorities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub accountability: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub assigned_to: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub delegation_rules: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub reporting_line: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Role {
    #[new]
    #[pyo3(signature = (id, name, role_type=None, responsibilities=None, authorities=None, accountability=None, assigned_to=None, delegation_rules=None, reporting_line=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, role_type: Option<String>, responsibilities: Option<Vec<String>>, authorities: Option<Vec<String>>, accountability: Option<String>, assigned_to: Option<Vec<String>>, delegation_rules: Option<String>, reporting_line: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Role{id, name, role_type, responsibilities, authorities, accountability, assigned_to, delegation_rules, reporting_line, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Role>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Role> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Role>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Role",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Role {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Role from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InformationSecurityObjective {
    #[cfg_attr(feature = "serde", serde(default))]
    pub objective_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_value: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub current_value: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metric_definition: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub measurement_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub measurement_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub achievement_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_risks: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub action_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub objective_resources_required: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InformationSecurityObjective {
    #[new]
    #[pyo3(signature = (id, name, objective_statement=None, target_value=None, current_value=None, metric_definition=None, measurement_method=None, measurement_frequency=None, responsible_role=None, target_date=None, achievement_status=None, related_risks=None, related_controls=None, action_plan=None, objective_resources_required=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, objective_statement: Option<String>, target_value: Option<String>, current_value: Option<String>, metric_definition: Option<String>, measurement_method: Option<String>, measurement_frequency: Option<String>, responsible_role: Option<String>, target_date: Option<NaiveDate>, achievement_status: Option<String>, related_risks: Option<Vec<String>>, related_controls: Option<Vec<String>>, action_plan: Option<String>, objective_resources_required: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InformationSecurityObjective{id, name, objective_statement, target_value, current_value, metric_definition, measurement_method, measurement_frequency, responsible_role, target_date, achievement_status, related_risks, related_controls, action_plan, objective_resources_required, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InformationSecurityObjective>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InformationSecurityObjective> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityObjective>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InformationSecurityObjective",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InformationSecurityObjective {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InformationSecurityObjective from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RiskAssessmentProcess {
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_acceptance_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessment_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessment_methodology: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub likelihood_scale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub impact_scale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_matrix: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessment_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trigger_events: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RiskAssessmentProcess {
    #[new]
    #[pyo3(signature = (id, name, risk_acceptance_criteria=None, assessment_criteria=None, assessment_methodology=None, likelihood_scale=None, impact_scale=None, risk_matrix=None, assessment_frequency=None, trigger_events=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, risk_acceptance_criteria: Option<String>, assessment_criteria: Option<String>, assessment_methodology: Option<String>, likelihood_scale: Option<String>, impact_scale: Option<String>, risk_matrix: Option<String>, assessment_frequency: Option<String>, trigger_events: Option<Vec<String>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        RiskAssessmentProcess{id, name, risk_acceptance_criteria, assessment_criteria, assessment_methodology, likelihood_scale, impact_scale, risk_matrix, assessment_frequency, trigger_events, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RiskAssessmentProcess>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RiskAssessmentProcess> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RiskAssessmentProcess>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RiskAssessmentProcess",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RiskAssessmentProcess {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RiskAssessmentProcess from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RiskAssessment {
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessment_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessment_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub assessor: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub methodology_used: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risks_identified: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub summary_findings: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub recommendations: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub next_assessment_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RiskAssessment {
    #[new]
    #[pyo3(signature = (id, name, assessment_scope=None, assessment_date=None, assessor=None, methodology_used=None, risks_identified=None, summary_findings=None, recommendations=None, next_assessment_date=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, assessment_scope: Option<String>, assessment_date: Option<NaiveDate>, assessor: Option<String>, methodology_used: Option<String>, risks_identified: Option<Vec<String>>, summary_findings: Option<String>, recommendations: Option<Vec<String>>, next_assessment_date: Option<NaiveDate>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        RiskAssessment{id, name, assessment_scope, assessment_date, assessor, methodology_used, risks_identified, summary_findings, recommendations, next_assessment_date, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RiskAssessment>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RiskAssessment> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RiskAssessment>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RiskAssessment",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RiskAssessment {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RiskAssessment from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Risk {
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub threat_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub vulnerability_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub affected_cia_properties: Option<Vec<CIAProperty>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub likelihood: Option<LikelihoodRating>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub impact: Option<ImpactRating>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub inherent_risk_level: Option<RiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub existing_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub residual_risk_level: Option<RiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_treatment_option: Option<RiskTreatmentOption>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub treatment_priority: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_treatment_plan: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Risk {
    #[new]
    #[pyo3(signature = (id, name, risk_source=None, threat_description=None, vulnerability_description=None, affected_assets=None, affected_cia_properties=None, risk_owner=None, likelihood=None, impact=None, inherent_risk_level=None, existing_controls=None, residual_risk_level=None, risk_treatment_option=None, treatment_priority=None, related_treatment_plan=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, risk_source: Option<String>, threat_description: Option<String>, vulnerability_description: Option<String>, affected_assets: Option<Vec<String>>, affected_cia_properties: Option<Vec<CIAProperty>>, risk_owner: Option<String>, likelihood: Option<LikelihoodRating>, impact: Option<ImpactRating>, inherent_risk_level: Option<RiskLevel>, existing_controls: Option<Vec<String>>, residual_risk_level: Option<RiskLevel>, risk_treatment_option: Option<RiskTreatmentOption>, treatment_priority: Option<String>, related_treatment_plan: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Risk{id, name, risk_source, threat_description, vulnerability_description, affected_assets, affected_cia_properties, risk_owner, likelihood, impact, inherent_risk_level, existing_controls, residual_risk_level, risk_treatment_option, treatment_priority, related_treatment_plan, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Risk>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Risk> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Risk>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Risk",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Risk {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Risk from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RiskTreatmentProcess {
    #[cfg_attr(feature = "serde", serde(default))]
    pub treatment_options_guidance: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_selection_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub annex_a_omission_verification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub soa_template: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approval_workflow: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RiskTreatmentProcess {
    #[new]
    #[pyo3(signature = (id, name, treatment_options_guidance=None, control_selection_criteria=None, annex_a_omission_verification=None, soa_template=None, approval_workflow=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, treatment_options_guidance: Option<String>, control_selection_criteria: Option<String>, annex_a_omission_verification: Option<String>, soa_template: Option<String>, approval_workflow: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        RiskTreatmentProcess{id, name, treatment_options_guidance, control_selection_criteria, annex_a_omission_verification, soa_template, approval_workflow, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RiskTreatmentProcess>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RiskTreatmentProcess> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RiskTreatmentProcess>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RiskTreatmentProcess",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RiskTreatmentProcess {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RiskTreatmentProcess from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RiskTreatmentPlan {
    #[cfg_attr(feature = "serde", serde(default))]
    pub plan_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risks_addressed: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub treatment_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls_to_implement: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub resources_required: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_parties: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_timeline: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_owner_approval: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub residual_risk_acceptance: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_status: Option<ImplementationStatus>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RiskTreatmentPlan {
    #[new]
    #[pyo3(signature = (id, name, plan_scope=None, risks_addressed=None, treatment_actions=None, controls_to_implement=None, resources_required=None, responsible_parties=None, implementation_timeline=None, risk_owner_approval=None, approved_date=None, residual_risk_acceptance=None, implementation_status=None, completion_date=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, plan_scope: Option<String>, risks_addressed: Option<Vec<String>>, treatment_actions: Option<Vec<String>>, controls_to_implement: Option<Vec<String>>, resources_required: Option<String>, responsible_parties: Option<Vec<String>>, implementation_timeline: Option<String>, risk_owner_approval: Option<String>, approved_date: Option<NaiveDate>, residual_risk_acceptance: Option<String>, implementation_status: Option<ImplementationStatus>, completion_date: Option<NaiveDate>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        RiskTreatmentPlan{id, name, plan_scope, risks_addressed, treatment_actions, controls_to_implement, resources_required, responsible_parties, implementation_timeline, risk_owner_approval, approved_date, residual_risk_acceptance, implementation_status, completion_date, document_type, document_reference, author, owner, approved_by, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RiskTreatmentPlan>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RiskTreatmentPlan> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RiskTreatmentPlan>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RiskTreatmentPlan",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RiskTreatmentPlan {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RiskTreatmentPlan from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct StatementOfApplicability {
    #[cfg_attr(feature = "serde", serde(default))]
    pub soa_entries: Option<Vec<SoAEntry>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub total_controls: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implemented_count: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub planned_count: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub not_applicable_count: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl StatementOfApplicability {
    #[new]
    #[pyo3(signature = (id, name, soa_entries=None, total_controls=None, implemented_count=None, planned_count=None, not_applicable_count=None, last_review_date=None, approved_by=None, document_type=None, document_reference=None, author=None, owner=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, soa_entries: Option<serde_utils::PyValue<Vec<SoAEntry>>>, total_controls: Option<isize>, implemented_count: Option<isize>, planned_count: Option<isize>, not_applicable_count: Option<isize>, last_review_date: Option<NaiveDate>, approved_by: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        let soa_entries = soa_entries.map(|v| v.into_inner());
        StatementOfApplicability{id, name, soa_entries, total_controls, implemented_count, planned_count, not_applicable_count, last_review_date, approved_by, document_type, document_reference, author, owner, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<StatementOfApplicability>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<StatementOfApplicability> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<StatementOfApplicability>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid StatementOfApplicability",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for StatementOfApplicability {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a StatementOfApplicability from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct SoAEntry {
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_applicable: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub inclusion_justification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub exclusion_justification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_status: Option<ImplementationStatus>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_evidence: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_implementation_date: Option<NaiveDate>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl SoAEntry {
    #[new]
    #[pyo3(signature = (control_reference=None, is_applicable=None, inclusion_justification=None, exclusion_justification=None, implementation_status=None, implementation_evidence=None, responsible_role=None, target_implementation_date=None))]
    pub fn new(control_reference: Option<String>, is_applicable: Option<bool>, inclusion_justification: Option<String>, exclusion_justification: Option<String>, implementation_status: Option<ImplementationStatus>, implementation_evidence: Option<String>, responsible_role: Option<String>, target_implementation_date: Option<NaiveDate>) -> Self {
        SoAEntry{control_reference, is_applicable, inclusion_justification, exclusion_justification, implementation_status, implementation_evidence, responsible_role, target_implementation_date}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<SoAEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<SoAEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<SoAEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid SoAEntry",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct SecurityControl {
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_id: Option<AnnexAControlId>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_category: Option<ControlCategory>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_text: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_guidance: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub applicable_threats: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub applicable_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_status: Option<ImplementationStatus>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effectiveness_rating: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub last_test_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub evidence_references: Option<Vec<String>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl SecurityControl {
    #[new]
    #[pyo3(signature = (id, name, control_id=None, control_title=None, control_category=None, control_text=None, implementation_guidance=None, related_controls=None, applicable_threats=None, applicable_assets=None, control_owner=None, implementation_status=None, implementation_date=None, effectiveness_rating=None, last_test_date=None, evidence_references=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, control_id: Option<AnnexAControlId>, control_title: Option<String>, control_category: Option<ControlCategory>, control_text: Option<String>, implementation_guidance: Option<String>, related_controls: Option<Vec<String>>, applicable_threats: Option<Vec<String>>, applicable_assets: Option<Vec<String>>, control_owner: Option<String>, implementation_status: Option<ImplementationStatus>, implementation_date: Option<NaiveDate>, effectiveness_rating: Option<String>, last_test_date: Option<NaiveDate>, evidence_references: Option<Vec<String>>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        SecurityControl{id, name, control_id, control_title, control_category, control_text, implementation_guidance, related_controls, applicable_threats, applicable_assets, control_owner, implementation_status, implementation_date, effectiveness_rating, last_test_date, evidence_references, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<SecurityControl>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<SecurityControl> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<SecurityControl>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid SecurityControl",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for SecurityControl {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a SecurityControl from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Resource {
    #[cfg_attr(feature = "serde", serde(default))]
    pub resource_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub quantity: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub allocation_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub allocated_to: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub cost: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub availability_status: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Resource {
    #[new]
    #[pyo3(signature = (id, name, resource_type=None, quantity=None, allocation_date=None, allocated_to=None, cost=None, availability_status=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, resource_type: Option<String>, quantity: Option<String>, allocation_date: Option<NaiveDate>, allocated_to: Option<String>, cost: Option<String>, availability_status: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Resource{id, name, resource_type, quantity, allocation_date, allocated_to, cost, availability_status, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Resource>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Resource> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Resource>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Resource",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Resource {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Resource from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CompetenceRecord {
    #[cfg_attr(feature = "serde", serde(default))]
    pub person_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub person_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub required_competencies: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub education_records: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub training_records: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub experience_records: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub competency_assessment_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub competency_gaps: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub development_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CompetenceRecord {
    #[new]
    #[pyo3(signature = (id, name, person_name=None, person_role=None, required_competencies=None, education_records=None, training_records=None, experience_records=None, competency_assessment_date=None, competency_gaps=None, development_actions=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, person_name: Option<String>, person_role: Option<String>, required_competencies: Option<Vec<String>>, education_records: Option<Vec<String>>, training_records: Option<Vec<String>>, experience_records: Option<Vec<String>>, competency_assessment_date: Option<NaiveDate>, competency_gaps: Option<Vec<String>>, development_actions: Option<Vec<String>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        CompetenceRecord{id, name, person_name, person_role, required_competencies, education_records, training_records, experience_records, competency_assessment_date, competency_gaps, development_actions, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CompetenceRecord>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CompetenceRecord> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CompetenceRecord>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CompetenceRecord",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CompetenceRecord {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a CompetenceRecord from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct AwarenessProgram {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub awareness_topics: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub delivery_methods: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_audience: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub completion_tracking: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effectiveness_measures: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl AwarenessProgram {
    #[new]
    #[pyo3(signature = (id, name, awareness_topics=None, delivery_methods=None, target_audience=None, frequency=None, completion_tracking=None, effectiveness_measures=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, awareness_topics: Option<Vec<String>>, delivery_methods: Option<Vec<String>>, target_audience: Option<String>, frequency: Option<String>, completion_tracking: Option<String>, effectiveness_measures: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        AwarenessProgram{id, name, awareness_topics, delivery_methods, target_audience, frequency, completion_tracking, effectiveness_measures, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<AwarenessProgram>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<AwarenessProgram> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<AwarenessProgram>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid AwarenessProgram",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for AwarenessProgram {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a AwarenessProgram from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CommunicationPlan {
    #[cfg_attr(feature = "serde", serde(default))]
    pub communication_items: Option<Vec<CommunicationItem>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CommunicationPlan {
    #[new]
    #[pyo3(signature = (id, name, communication_items=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, communication_items: Option<serde_utils::PyValue<Vec<CommunicationItem>>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        let communication_items = communication_items.map(|v| v.into_inner());
        CommunicationPlan{id, name, communication_items, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CommunicationPlan>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CommunicationPlan> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CommunicationPlan>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CommunicationPlan",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CommunicationPlan {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a CommunicationPlan from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CommunicationItem {
    #[cfg_attr(feature = "serde", serde(default))]
    pub subject: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub purpose: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audience: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_party: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub records_required: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CommunicationItem {
    #[new]
    #[pyo3(signature = (subject=None, purpose=None, audience=None, frequency=None, method=None, responsible_party=None, records_required=None))]
    pub fn new(subject: Option<String>, purpose: Option<String>, audience: Option<String>, frequency: Option<String>, method: Option<String>, responsible_party: Option<String>, records_required: Option<bool>) -> Self {
        CommunicationItem{subject, purpose, audience, frequency, method, responsible_party, records_required}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CommunicationItem>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CommunicationItem> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CommunicationItem>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CommunicationItem",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct OperationalProcedure {
    #[cfg_attr(feature = "serde", serde(default))]
    pub procedure_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub process_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_measures: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_roles: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_requirements: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl OperationalProcedure {
    #[new]
    #[pyo3(signature = (id, name, procedure_scope=None, process_criteria=None, control_measures=None, responsible_roles=None, related_controls=None, change_control_requirements=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, procedure_scope: Option<String>, process_criteria: Option<String>, control_measures: Option<Vec<String>>, responsible_roles: Option<Vec<String>>, related_controls: Option<Vec<String>>, change_control_requirements: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        OperationalProcedure{id, name, procedure_scope, process_criteria, control_measures, responsible_roles, related_controls, change_control_requirements, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<OperationalProcedure>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<OperationalProcedure> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<OperationalProcedure>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid OperationalProcedure",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for OperationalProcedure {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a OperationalProcedure from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct MonitoringProgram {
    #[cfg_attr(feature = "serde", serde(default))]
    pub monitoring_items: Option<Vec<MonitoringItem>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl MonitoringProgram {
    #[new]
    #[pyo3(signature = (id, name, monitoring_items=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, monitoring_items: Option<serde_utils::PyValue<Vec<MonitoringItem>>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        let monitoring_items = monitoring_items.map(|v| v.into_inner());
        MonitoringProgram{id, name, monitoring_items, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<MonitoringProgram>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<MonitoringProgram> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<MonitoringProgram>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid MonitoringProgram",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for MonitoringProgram {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a MonitoringProgram from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct MonitoringItem {
    #[cfg_attr(feature = "serde", serde(default))]
    pub metric_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metric_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub measurement_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub measurement_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_party: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub analysis_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub analyst: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_threshold: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub alert_threshold: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub current_value: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trend: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl MonitoringItem {
    #[new]
    #[pyo3(signature = (metric_name=None, metric_description=None, measurement_method=None, measurement_frequency=None, responsible_party=None, analysis_frequency=None, analyst=None, target_threshold=None, alert_threshold=None, current_value=None, trend=None))]
    pub fn new(metric_name: Option<String>, metric_description: Option<String>, measurement_method: Option<String>, measurement_frequency: Option<String>, responsible_party: Option<String>, analysis_frequency: Option<String>, analyst: Option<String>, target_threshold: Option<String>, alert_threshold: Option<String>, current_value: Option<String>, trend: Option<String>) -> Self {
        MonitoringItem{metric_name, metric_description, measurement_method, measurement_frequency, responsible_party, analysis_frequency, analyst, target_threshold, alert_threshold, current_value, trend}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<MonitoringItem>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<MonitoringItem> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<MonitoringItem>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid MonitoringItem",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InternalAudit {
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_type: Option<AuditType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_criteria: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_objectives: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_period_start: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_period_end: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub lead_auditor: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_team: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub auditee_representatives: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub findings: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub positive_observations: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_conclusion: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub report_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub report_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InternalAudit {
    #[new]
    #[pyo3(signature = (id, name, audit_reference=None, audit_type=None, audit_scope=None, audit_criteria=None, audit_objectives=None, audit_period_start=None, audit_period_end=None, lead_auditor=None, audit_team=None, auditee_representatives=None, audit_plan=None, findings=None, positive_observations=None, audit_conclusion=None, report_date=None, report_distribution=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, audit_reference: Option<String>, audit_type: Option<AuditType>, audit_scope: Option<String>, audit_criteria: Option<Vec<String>>, audit_objectives: Option<Vec<String>>, audit_period_start: Option<NaiveDate>, audit_period_end: Option<NaiveDate>, lead_auditor: Option<String>, audit_team: Option<Vec<String>>, auditee_representatives: Option<Vec<String>>, audit_plan: Option<String>, findings: Option<Vec<String>>, positive_observations: Option<Vec<String>>, audit_conclusion: Option<String>, report_date: Option<NaiveDate>, report_distribution: Option<Vec<String>>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InternalAudit{id, name, audit_reference, audit_type, audit_scope, audit_criteria, audit_objectives, audit_period_start, audit_period_end, lead_auditor, audit_team, auditee_representatives, audit_plan, findings, positive_observations, audit_conclusion, report_date, report_distribution, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InternalAudit>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InternalAudit> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InternalAudit>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InternalAudit",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InternalAudit {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InternalAudit from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct AuditProgramme {
    #[cfg_attr(feature = "serde", serde(default))]
    pub programme_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub planned_audits: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_frequency_rationale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub resource_requirements: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub auditor_qualifications: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub programme_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl AuditProgramme {
    #[new]
    #[pyo3(signature = (id, name, programme_period=None, planned_audits=None, audit_frequency_rationale=None, resource_requirements=None, auditor_qualifications=None, programme_status=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, review_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, programme_period: Option<String>, planned_audits: Option<Vec<String>>, audit_frequency_rationale: Option<String>, resource_requirements: Option<String>, auditor_qualifications: Option<String>, programme_status: Option<String>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, review_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        AuditProgramme{id, name, programme_period, planned_audits, audit_frequency_rationale, resource_requirements, auditor_qualifications, programme_status, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, review_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<AuditProgramme>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<AuditProgramme> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<AuditProgramme>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid AuditProgramme",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for AuditProgramme {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a AuditProgramme from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct AuditFinding {
    #[cfg_attr(feature = "serde", serde(default))]
    pub finding_type: Option<AuditFindingType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub clause_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub control_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub finding_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub objective_evidence: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub root_cause_analysis: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_implication: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub recommended_action: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub auditee_response: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub linked_corrective_action: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub closure_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub closure_date: Option<NaiveDate>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl AuditFinding {
    #[new]
    #[pyo3(signature = (id, name, finding_type=None, clause_reference=None, control_reference=None, finding_description=None, objective_evidence=None, root_cause_analysis=None, risk_implication=None, recommended_action=None, auditee_response=None, linked_corrective_action=None, closure_status=None, closure_date=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, finding_type: Option<AuditFindingType>, clause_reference: Option<String>, control_reference: Option<String>, finding_description: Option<String>, objective_evidence: Option<String>, root_cause_analysis: Option<String>, risk_implication: Option<String>, recommended_action: Option<String>, auditee_response: Option<String>, linked_corrective_action: Option<String>, closure_status: Option<String>, closure_date: Option<NaiveDate>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        AuditFinding{id, name, finding_type, clause_reference, control_reference, finding_description, objective_evidence, root_cause_analysis, risk_implication, recommended_action, auditee_response, linked_corrective_action, closure_status, closure_date, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<AuditFinding>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<AuditFinding> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<AuditFinding>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid AuditFinding",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for AuditFinding {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a AuditFinding from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ManagementReview {
    #[cfg_attr(feature = "serde", serde(default))]
    pub review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub attendees: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub previous_actions_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub context_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub interested_party_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub interested_party_feedback: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub performance_trends: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub audit_results_summary: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_assessment_results: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risk_treatment_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub risks_and_opportunities_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub improvement_opportunities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub decisions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub action_items: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_type: Option<DocumentType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub approved_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub retention_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub distribution_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub storage_and_preservation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub change_control_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_origin_source: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ManagementReview {
    #[new]
    #[pyo3(signature = (id, name, review_date=None, attendees=None, previous_actions_status=None, context_changes=None, interested_party_changes=None, interested_party_feedback=None, performance_trends=None, audit_results_summary=None, risk_assessment_results=None, risk_treatment_status=None, risks_and_opportunities_changes=None, improvement_opportunities=None, decisions=None, action_items=None, next_review_date=None, document_type=None, document_reference=None, author=None, owner=None, approved_by=None, approved_date=None, effective_date=None, status=None, classification=None, retention_period=None, distribution_controls=None, storage_and_preservation=None, change_control_method=None, external_origin=None, external_origin_source=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, review_date: Option<NaiveDate>, attendees: Option<Vec<String>>, previous_actions_status: Option<String>, context_changes: Option<String>, interested_party_changes: Option<String>, interested_party_feedback: Option<String>, performance_trends: Option<String>, audit_results_summary: Option<String>, risk_assessment_results: Option<String>, risk_treatment_status: Option<String>, risks_and_opportunities_changes: Option<String>, improvement_opportunities: Option<Vec<String>>, decisions: Option<Vec<String>>, action_items: Option<Vec<String>>, next_review_date: Option<NaiveDate>, document_type: Option<DocumentType>, document_reference: Option<String>, author: Option<String>, owner: Option<String>, approved_by: Option<String>, approved_date: Option<NaiveDate>, effective_date: Option<NaiveDate>, status: Option<String>, classification: Option<String>, retention_period: Option<String>, distribution_controls: Option<Vec<String>>, storage_and_preservation: Option<String>, change_control_method: Option<String>, external_origin: Option<bool>, external_origin_source: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        ManagementReview{id, name, review_date, attendees, previous_actions_status, context_changes, interested_party_changes, interested_party_feedback, performance_trends, audit_results_summary, risk_assessment_results, risk_treatment_status, risks_and_opportunities_changes, improvement_opportunities, decisions, action_items, next_review_date, document_type, document_reference, author, owner, approved_by, approved_date, effective_date, status, classification, retention_period, distribution_controls, storage_and_preservation, change_control_method, external_origin, external_origin_source, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ManagementReview>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ManagementReview> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ManagementReview>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ManagementReview",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ManagementReview {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ManagementReview from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Nonconformity {
    #[cfg_attr(feature = "serde", serde(default))]
    pub nonconformity_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub detection_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub detected_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub requirement_violated: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nonconformity_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub immediate_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub consequences_addressed: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub similar_nonconformities_check: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub linked_corrective_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub closure_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub closure_evidence: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Nonconformity {
    #[new]
    #[pyo3(signature = (id, name, nonconformity_source=None, detection_date=None, detected_by=None, requirement_violated=None, nonconformity_description=None, immediate_actions=None, consequences_addressed=None, root_cause=None, similar_nonconformities_check=None, linked_corrective_actions=None, status=None, closure_date=None, closure_evidence=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, nonconformity_source: Option<String>, detection_date: Option<NaiveDate>, detected_by: Option<String>, requirement_violated: Option<String>, nonconformity_description: Option<String>, immediate_actions: Option<Vec<String>>, consequences_addressed: Option<String>, root_cause: Option<String>, similar_nonconformities_check: Option<String>, linked_corrective_actions: Option<Vec<String>>, status: Option<String>, closure_date: Option<NaiveDate>, closure_evidence: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Nonconformity{id, name, nonconformity_source, detection_date, detected_by, requirement_violated, nonconformity_description, immediate_actions, consequences_addressed, root_cause, similar_nonconformities_check, linked_corrective_actions, status, closure_date, closure_evidence, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Nonconformity>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Nonconformity> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Nonconformity>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Nonconformity",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Nonconformity {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Nonconformity from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CorrectiveAction {
    #[cfg_attr(feature = "serde", serde(default))]
    pub linked_nonconformity: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub action_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub root_cause_addressed: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_party: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub actual_completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub resources_required: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effectiveness_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effectiveness_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub effectiveness_verified: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub isms_changes_required: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CorrectiveAction {
    #[new]
    #[pyo3(signature = (id, name, linked_nonconformity=None, action_description=None, root_cause_addressed=None, responsible_party=None, target_completion_date=None, actual_completion_date=None, resources_required=None, effectiveness_criteria=None, effectiveness_review_date=None, effectiveness_verified=None, isms_changes_required=None, status=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, linked_nonconformity: Option<String>, action_description: Option<String>, root_cause_addressed: Option<String>, responsible_party: Option<String>, target_completion_date: Option<NaiveDate>, actual_completion_date: Option<NaiveDate>, resources_required: Option<String>, effectiveness_criteria: Option<String>, effectiveness_review_date: Option<NaiveDate>, effectiveness_verified: Option<bool>, isms_changes_required: Option<String>, status: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        CorrectiveAction{id, name, linked_nonconformity, action_description, root_cause_addressed, responsible_party, target_completion_date, actual_completion_date, resources_required, effectiveness_criteria, effectiveness_review_date, effectiveness_verified, isms_changes_required, status, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CorrectiveAction>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CorrectiveAction> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CorrectiveAction>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CorrectiveAction",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CorrectiveAction {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a CorrectiveAction from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ImprovementOpportunity {
    #[cfg_attr(feature = "serde", serde(default))]
    pub improvement_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub identification_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub identified_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub improvement_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub expected_benefit: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub priority: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub implementation_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub responsible_party: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub actual_completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub outcome_assessment: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub status: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ImprovementOpportunity {
    #[new]
    #[pyo3(signature = (id, name, improvement_source=None, identification_date=None, identified_by=None, improvement_description=None, expected_benefit=None, priority=None, implementation_plan=None, responsible_party=None, target_date=None, actual_completion_date=None, outcome_assessment=None, status=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, improvement_source: Option<String>, identification_date: Option<NaiveDate>, identified_by: Option<String>, improvement_description: Option<String>, expected_benefit: Option<String>, priority: Option<String>, implementation_plan: Option<String>, responsible_party: Option<String>, target_date: Option<NaiveDate>, actual_completion_date: Option<NaiveDate>, outcome_assessment: Option<String>, status: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        ImprovementOpportunity{id, name, improvement_source, identification_date, identified_by, improvement_description, expected_benefit, priority, implementation_plan, responsible_party, target_date, actual_completion_date, outcome_assessment, status, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ImprovementOpportunity>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ImprovementOpportunity> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ImprovementOpportunity>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ImprovementOpportunity",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ImprovementOpportunity {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ImprovementOpportunity from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Asset {
    #[cfg_attr(feature = "serde", serde(default))]
    pub asset_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub asset_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub asset_custodian: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub location: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub criticality: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub related_risks: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applicable_controls: Option<Vec<String>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Asset {
    #[new]
    #[pyo3(signature = (id, name, asset_type=None, asset_owner=None, asset_custodian=None, classification=None, location=None, criticality=None, related_risks=None, applicable_controls=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, asset_type: Option<String>, asset_owner: Option<String>, asset_custodian: Option<String>, classification: Option<String>, location: Option<String>, criticality: Option<String>, related_risks: Option<Vec<String>>, applicable_controls: Option<Vec<String>>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        Asset{id, name, asset_type, asset_owner, asset_custodian, classification, location, criticality, related_risks, applicable_controls, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Asset>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Asset> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Asset>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Asset",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Asset {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Asset from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InformationSecurityEvent {
    #[cfg_attr(feature = "serde", serde(default))]
    pub event_datetime: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub reporter: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub event_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub initial_assessment: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub categorized_as_incident: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub linked_incident: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InformationSecurityEvent {
    #[new]
    #[pyo3(signature = (id, name, event_datetime=None, reporter=None, event_description=None, affected_assets=None, initial_assessment=None, categorized_as_incident=None, linked_incident=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, event_datetime: Option<NaiveDateTime>, reporter: Option<String>, event_description: Option<String>, affected_assets: Option<Vec<String>>, initial_assessment: Option<String>, categorized_as_incident: Option<bool>, linked_incident: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InformationSecurityEvent{id, name, event_datetime, reporter, event_description, affected_assets, initial_assessment, categorized_as_incident, linked_incident, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InformationSecurityEvent>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InformationSecurityEvent> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityEvent>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InformationSecurityEvent",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InformationSecurityEvent {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InformationSecurityEvent from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InformationSecurityIncident {
    #[cfg_attr(feature = "serde", serde(default))]
    pub incident_datetime: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub incident_category: Option<SecurityIncidentCategory>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub severity: Option<RiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub affected_cia: Option<Vec<CIAProperty>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub incident_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub detection_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub response_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub containment_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub eradication_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub recovery_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub lessons_learned: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub evidence_collected: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub notification_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub notifications_made: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub closure_datetime: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_incident_review: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub created_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub modified_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InformationSecurityIncident {
    #[new]
    #[pyo3(signature = (id, name, incident_datetime=None, incident_category=None, severity=None, affected_assets=None, affected_cia=None, incident_description=None, detection_method=None, response_actions=None, containment_actions=None, eradication_actions=None, recovery_actions=None, root_cause=None, lessons_learned=None, evidence_collected=None, notification_required=None, notifications_made=None, closure_datetime=None, post_incident_review=None, description=None, created_date=None, modified_date=None, version=None))]
    pub fn new(id: uriorcurie, name: String, incident_datetime: Option<NaiveDateTime>, incident_category: Option<SecurityIncidentCategory>, severity: Option<RiskLevel>, affected_assets: Option<Vec<String>>, affected_cia: Option<Vec<CIAProperty>>, incident_description: Option<String>, detection_method: Option<String>, response_actions: Option<Vec<String>>, containment_actions: Option<Vec<String>>, eradication_actions: Option<Vec<String>>, recovery_actions: Option<Vec<String>>, root_cause: Option<String>, lessons_learned: Option<Vec<String>>, evidence_collected: Option<Vec<String>>, notification_required: Option<bool>, notifications_made: Option<Vec<String>>, closure_datetime: Option<NaiveDateTime>, post_incident_review: Option<String>, description: Option<String>, created_date: Option<NaiveDate>, modified_date: Option<NaiveDate>, version: Option<String>) -> Self {
        InformationSecurityIncident{id, name, incident_datetime, incident_category, severity, affected_assets, affected_cia, incident_description, detection_method, response_actions, containment_actions, eradication_actions, recovery_actions, root_cause, lessons_learned, evidence_collected, notification_required, notifications_made, closure_datetime, post_incident_review, description, created_date, modified_date, version}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InformationSecurityIncident>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InformationSecurityIncident> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InformationSecurityIncident>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InformationSecurityIncident",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InformationSecurityIncident {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InformationSecurityIncident from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}




#[cfg(feature = "stubgen")]
define_stub_info_gatherer!(stub_info);
