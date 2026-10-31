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
pub type isms_duration = String;
pub type isms_requirement_reference = String;

// Slots

pub type isms_id = uriorcurie;
pub type title = String;
pub type description = String;
pub type responsible_role = IsmsRole;
pub type relevant_controls = Vec<IsmsControl>;
pub type affected_assets = Vec<IsmsAsset>;
pub type affected_security_properties = Vec<IsmsSecurityProperty>;
pub type implementation_state = IsmsImplementationStatus;
pub type entry_annex_a_control = IsmsAnnexAControl;
pub type document_reference = String;
pub type document_version = String;
pub type document_author = String;
pub type document_owner = String;
pub type document_approver = String;
pub type document_approval_date = NaiveDate;
pub type document_effective_date = NaiveDate;
pub type document_last_review_date = NaiveDate;
pub type document_next_review_date = NaiveDate;
pub type document_status = String;
pub type document_classification = String;
pub type document_retention = String;
pub type document_distribution = Vec<String>;
pub type document_storage = String;
pub type document_change_control = String;
pub type document_external_origin = bool;
pub type document_external_source = String;
pub type isms_organization = IsmsOrganization;
pub type isms_top_management = String;
pub type isms_governing_body = String;
pub type isms_leadership_evidence = Vec<String>;
pub type isms_scope = String;
pub type isms_scope_boundaries = Vec<String>;
pub type isms_scope_exclusions = Vec<String>;
pub type isms_interfaces = Vec<String>;
pub type isms_processes = String;
pub type isms_internal_issues = Vec<String>;
pub type isms_external_issues = Vec<String>;
pub type isms_risk_and_opportunity_actions = Vec<String>;
pub type isms_planned_changes = Vec<String>;
pub type isms_external_services = Vec<String>;
pub type isms_certification_status = String;
pub type isms_certification_body = String;
pub type isms_certification_date = NaiveDate;
pub type isms_recertification_date = NaiveDate;
pub type isms_interested_parties = Vec<IsmsInterestedParty>;
pub type isms_policy = IsmsPolicy;
pub type isms_topic_specific_policies = Vec<IsmsTopicSpecificPolicy>;
pub type isms_roles = Vec<IsmsRole>;
pub type isms_objectives = Vec<IsmsObjective>;
pub type isms_risk_assessment_process = IsmsRiskAssessmentProcess;
pub type isms_risk_treatment_process = IsmsRiskTreatmentProcess;
pub type isms_risk_assessments = Vec<IsmsRiskAssessment>;
pub type isms_risks = Vec<IsmsRisk>;
pub type isms_risk_treatment_plans = Vec<IsmsRiskTreatmentPlan>;
pub type isms_statement_of_applicability = IsmsStatementOfApplicability;
pub type isms_controls = Vec<IsmsControl>;
pub type isms_assets = Vec<IsmsAsset>;
pub type isms_resources = Vec<IsmsResource>;
pub type isms_competence_records = Vec<IsmsCompetenceRecord>;
pub type isms_awareness_programme = IsmsAwarenessProgramme;
pub type isms_communication_plan = IsmsCommunicationPlan;
pub type isms_documented_information = Vec<IsmsDocumentedInformation>;
pub type isms_operational_procedures = Vec<IsmsOperationalProcedure>;
pub type isms_monitoring_programme = IsmsMonitoringProgramme;
pub type isms_audit_programmes = Vec<IsmsAuditProgramme>;
pub type isms_audits = Vec<IsmsAudit>;
pub type isms_management_reviews = Vec<IsmsManagementReview>;
pub type isms_nonconformities = Vec<IsmsNonconformity>;
pub type isms_corrective_actions = Vec<IsmsCorrectiveAction>;
pub type isms_improvements = Vec<IsmsImprovementOpportunity>;
pub type isms_security_events = Vec<IsmsSecurityEvent>;
pub type organization_legal_name = String;
pub type organization_trading_names = Vec<String>;
pub type organization_kind = String;
pub type organization_sector = String;
pub type organization_size = String;
pub type organization_employee_count = isize;
pub type organization_locations = Vec<String>;
pub type organization_jurisdictions = Vec<String>;
pub type organization_parent = String;
pub type organization_subsidiaries = Vec<String>;
pub type organization_climate_change_relevant = bool;
pub type party_category = String;
pub type party_relationship = String;
pub type party_requirements = Vec<String>;
pub type party_addressed_requirements = Vec<String>;
pub type party_climate_change_requirements = Vec<String>;
pub type party_communication_needs = String;
pub type party_contact = String;
pub type policy_statement = String;
pub type policy_objectives_framework = String;
pub type policy_commitments = Vec<String>;
pub type policy_applicability = String;
pub type policy_communication_date = NaiveDate;
pub type policy_acknowledgement_required = bool;
pub type policy_management_systems = Vec<IsmsManagementSystemStandard>;
pub type topic_policy_topic = String;
pub type topic_policy_parent = IsmsPolicy;
pub type topic_policy_audience = String;
pub type role_category = String;
pub type role_responsibilities = Vec<String>;
pub type role_authorities = Vec<String>;
pub type role_accountability = String;
pub type role_holders = Vec<String>;
pub type role_delegation = String;
pub type role_reports_to = IsmsRole;
pub type objective_statement = String;
pub type objective_target = String;
pub type objective_current_value = String;
pub type objective_metric = String;
pub type objective_measurement_method = String;
pub type objective_measurement_frequency = String;
pub type objective_target_date = NaiveDate;
pub type objective_achievement = String;
pub type objective_risks = Vec<IsmsRisk>;
pub type objective_action_plan = String;
pub type objective_resources = String;
pub type risk_acceptance_criteria = String;
pub type risk_assessment_criteria = String;
pub type risk_assessment_method = String;
pub type risk_likelihood_scale = String;
pub type risk_impact_scale = String;
pub type risk_matrix = String;
pub type risk_assessment_frequency = String;
pub type risk_assessment_triggers = Vec<String>;
pub type assessment_scope = String;
pub type assessment_date = NaiveDate;
pub type assessment_assessor = String;
pub type assessment_method_used = String;
pub type assessment_risks = Vec<IsmsRisk>;
pub type assessment_summary = String;
pub type assessment_recommendations = Vec<String>;
pub type assessment_next_date = NaiveDate;
pub type risk_source = String;
pub type risk_threat = String;
pub type risk_vulnerability = String;
pub type risk_owner = String;
pub type risk_likelihood = IsmsLikelihood;
pub type risk_impact = IsmsImpact;
pub type risk_inherent_level = IsmsRiskLevel;
pub type risk_existing_controls = Vec<IsmsControl>;
pub type risk_residual_level = IsmsRiskLevel;
pub type risk_treatment_option = IsmsRiskTreatmentOption;
pub type risk_treatment_priority = String;
pub type treatment_options_guidance = String;
pub type treatment_control_selection = String;
pub type treatment_annex_a_comparison = String;
pub type treatment_soa_template = String;
pub type treatment_approval_workflow = String;
pub type plan_scope = String;
pub type plan_risks = Vec<IsmsRisk>;
pub type plan_actions = Vec<String>;
pub type plan_controls = Vec<IsmsControl>;
pub type plan_resources = String;
pub type plan_responsible_parties = Vec<String>;
pub type plan_timeline = String;
pub type plan_risk_owner_approval = String;
pub type plan_residual_risk_acceptance = String;
pub type plan_completion_date = NaiveDate;
pub type soa_entries = Vec<IsmsApplicabilityEntry>;
pub type entry_type = String;
pub type entry_justification = String;
pub type included_control = IsmsControl;
pub type included_evidence = String;
pub type included_target_date = NaiveDate;
pub type control_annex_a_controls = Vec<IsmsAnnexAControl>;
pub type control_theme = IsmsControlTheme;
pub type control_text = String;
pub type control_guidance = String;
pub type control_threats = Vec<String>;
pub type control_asset_types = Vec<String>;
pub type control_owner = String;
pub type control_implementation_date = NaiveDate;
pub type control_effectiveness = String;
pub type control_last_tested = NaiveDate;
pub type control_evidence = Vec<String>;
pub type asset_category = String;
pub type asset_owner = String;
pub type asset_custodian = String;
pub type asset_classification = String;
pub type asset_location = String;
pub type asset_criticality = String;
pub type resource_category = String;
pub type resource_quantity = String;
pub type resource_allocation_date = NaiveDate;
pub type resource_allocated_to = String;
pub type resource_cost = String;
pub type resource_availability = String;
pub type competence_person = String;
pub type competence_role = IsmsRole;
pub type competence_required = Vec<String>;
pub type competence_education = Vec<String>;
pub type competence_training = Vec<String>;
pub type competence_experience = Vec<String>;
pub type competence_assessment_date = NaiveDate;
pub type competence_gaps = Vec<String>;
pub type competence_actions = Vec<String>;
pub type awareness_topics = Vec<String>;
pub type awareness_methods = Vec<String>;
pub type awareness_audience = String;
pub type awareness_frequency = String;
pub type awareness_completion_tracking = String;
pub type awareness_effectiveness = String;
pub type communication_items = Vec<IsmsCommunication>;
pub type communication_subject = String;
pub type communication_purpose = String;
pub type communication_audience = String;
pub type communication_frequency = String;
pub type communication_method = String;
pub type communication_records_required = bool;
pub type document_kind = IsmsDocumentKind;
pub type procedure_scope = String;
pub type procedure_criteria = String;
pub type procedure_control_measures = Vec<String>;
pub type procedure_roles = Vec<IsmsRole>;
pub type procedure_change_control = String;
pub type monitoring_items = Vec<IsmsMonitoringItem>;
pub type monitoring_metric = String;
pub type monitoring_description = String;
pub type monitoring_method = String;
pub type monitoring_frequency = String;
pub type monitoring_analysis_frequency = String;
pub type monitoring_analyst = String;
pub type monitoring_target = String;
pub type monitoring_alert_threshold = String;
pub type monitoring_current_value = String;
pub type monitoring_trend = String;
pub type programme_period = String;
pub type programme_audits = Vec<IsmsAudit>;
pub type programme_frequency_rationale = String;
pub type programme_resources = String;
pub type programme_auditor_qualifications = String;
pub type programme_status = String;
pub type audit_type = IsmsAuditType;
pub type audit_standards = Vec<IsmsManagementSystemStandard>;
pub type audit_scope = String;
pub type audit_criteria = Vec<String>;
pub type audit_objectives = Vec<String>;
pub type audit_period_start = NaiveDate;
pub type audit_period_end = NaiveDate;
pub type audit_lead = String;
pub type audit_team = Vec<String>;
pub type audit_auditees = Vec<String>;
pub type audit_plan = IsmsDocumentedInformation;
pub type audit_findings = Vec<IsmsAuditFinding>;
pub type audit_conclusion = String;
pub type audit_report_date = NaiveDate;
pub type audit_report_distribution = Vec<String>;
pub type finding_type = IsmsAuditFindingType;
pub type finding_requirement = String;
pub type finding_control = IsmsControl;
pub type finding_evidence = String;
pub type finding_root_cause = String;
pub type finding_risk = String;
pub type finding_recommendation = String;
pub type finding_auditee_response = String;
pub type finding_corrective_action = IsmsCorrectiveAction;
pub type finding_closure_status = String;
pub type finding_closure_date = NaiveDate;
pub type review_held_on = NaiveDate;
pub type review_attendees = Vec<String>;
pub type review_previous_actions = String;
pub type review_context_changes = String;
pub type review_interested_party_changes = String;
pub type review_interested_party_feedback = String;
pub type review_performance_trends = String;
pub type review_audit_results = String;
pub type review_risk_assessment_results = String;
pub type review_risk_treatment_status = String;
pub type review_risks_and_opportunities = String;
pub type review_improvement_opportunities = Vec<String>;
pub type review_decisions = Vec<String>;
pub type review_actions = Vec<String>;
pub type review_next_date = NaiveDate;
pub type nonconformity_source = String;
pub type nonconformity_detected_on = NaiveDate;
pub type nonconformity_detected_by = String;
pub type nonconformity_requirement = String;
pub type nonconformity_immediate_actions = Vec<String>;
pub type nonconformity_consequences = String;
pub type nonconformity_root_cause = String;
pub type nonconformity_similar_check = String;
pub type nonconformity_status = String;
pub type nonconformity_closure_date = NaiveDate;
pub type nonconformity_closure_evidence = String;
pub type action_nonconformities = Vec<IsmsNonconformity>;
pub type action_root_cause = String;
pub type action_target_date = NaiveDate;
pub type action_completion_date = NaiveDate;
pub type action_resources = String;
pub type action_effectiveness_criteria = String;
pub type action_effectiveness_review_date = NaiveDate;
pub type action_effective = bool;
pub type action_isms_changes = String;
pub type action_status = String;
pub type improvement_source = String;
pub type improvement_identified_on = NaiveDate;
pub type improvement_identified_by = String;
pub type improvement_benefit = String;
pub type improvement_priority = String;
pub type improvement_plan = String;
pub type improvement_target_date = NaiveDate;
pub type improvement_completion_date = NaiveDate;
pub type improvement_outcome = String;
pub type improvement_status = String;
pub type event_type = String;
pub type event_occurred_at = NaiveDateTime;
pub type event_reporter = String;
pub type event_assessment = String;
pub type incident_category = IsmsIncidentCategory;
pub type incident_severity = IsmsRiskLevel;
pub type incident_detection_method = String;
pub type incident_response_actions = Vec<String>;
pub type incident_containment_actions = Vec<String>;
pub type incident_eradication_actions = Vec<String>;
pub type incident_recovery_actions = Vec<String>;
pub type incident_root_cause = String;
pub type incident_lessons_learned = Vec<String>;
pub type incident_evidence = Vec<String>;
pub type incident_notification_required = bool;
pub type incident_notifications = Vec<String>;
pub type incident_closed_at = NaiveDateTime;
pub type incident_review = String;

// Enums

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsControlTheme {
    Organizational,
    People,
    Physical,
    Technological,
}

impl core::fmt::Display for IsmsControlTheme {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsControlTheme::Organizational => f.write_str("organizational"),
            IsmsControlTheme::People => f.write_str("people"),
            IsmsControlTheme::Physical => f.write_str("physical"),
            IsmsControlTheme::Technological => f.write_str("technological"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsControlTheme {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsControlTheme::Organizational => "organizational",
            IsmsControlTheme::People => "people",
            IsmsControlTheme::Physical => "physical",
            IsmsControlTheme::Technological => "technological",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsControlTheme {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "organizational" | "Organizational" => Ok(IsmsControlTheme::Organizational),
                "people" | "People" => Ok(IsmsControlTheme::People),
                "physical" | "Physical" => Ok(IsmsControlTheme::Physical),
                "technological" | "Technological" => Ok(IsmsControlTheme::Technological),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsControlTheme: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsControlTheme)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsControlTheme {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['organizational', 'people', 'physical', 'technological']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsAnnexAControl {
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

impl core::fmt::Display for IsmsAnnexAControl {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsAnnexAControl::A51 => f.write_str("a_5_1"),
            IsmsAnnexAControl::A52 => f.write_str("a_5_2"),
            IsmsAnnexAControl::A53 => f.write_str("a_5_3"),
            IsmsAnnexAControl::A54 => f.write_str("a_5_4"),
            IsmsAnnexAControl::A55 => f.write_str("a_5_5"),
            IsmsAnnexAControl::A56 => f.write_str("a_5_6"),
            IsmsAnnexAControl::A57 => f.write_str("a_5_7"),
            IsmsAnnexAControl::A58 => f.write_str("a_5_8"),
            IsmsAnnexAControl::A59 => f.write_str("a_5_9"),
            IsmsAnnexAControl::A510 => f.write_str("a_5_10"),
            IsmsAnnexAControl::A511 => f.write_str("a_5_11"),
            IsmsAnnexAControl::A512 => f.write_str("a_5_12"),
            IsmsAnnexAControl::A513 => f.write_str("a_5_13"),
            IsmsAnnexAControl::A514 => f.write_str("a_5_14"),
            IsmsAnnexAControl::A515 => f.write_str("a_5_15"),
            IsmsAnnexAControl::A516 => f.write_str("a_5_16"),
            IsmsAnnexAControl::A517 => f.write_str("a_5_17"),
            IsmsAnnexAControl::A518 => f.write_str("a_5_18"),
            IsmsAnnexAControl::A519 => f.write_str("a_5_19"),
            IsmsAnnexAControl::A520 => f.write_str("a_5_20"),
            IsmsAnnexAControl::A521 => f.write_str("a_5_21"),
            IsmsAnnexAControl::A522 => f.write_str("a_5_22"),
            IsmsAnnexAControl::A523 => f.write_str("a_5_23"),
            IsmsAnnexAControl::A524 => f.write_str("a_5_24"),
            IsmsAnnexAControl::A525 => f.write_str("a_5_25"),
            IsmsAnnexAControl::A526 => f.write_str("a_5_26"),
            IsmsAnnexAControl::A527 => f.write_str("a_5_27"),
            IsmsAnnexAControl::A528 => f.write_str("a_5_28"),
            IsmsAnnexAControl::A529 => f.write_str("a_5_29"),
            IsmsAnnexAControl::A530 => f.write_str("a_5_30"),
            IsmsAnnexAControl::A531 => f.write_str("a_5_31"),
            IsmsAnnexAControl::A532 => f.write_str("a_5_32"),
            IsmsAnnexAControl::A533 => f.write_str("a_5_33"),
            IsmsAnnexAControl::A534 => f.write_str("a_5_34"),
            IsmsAnnexAControl::A535 => f.write_str("a_5_35"),
            IsmsAnnexAControl::A536 => f.write_str("a_5_36"),
            IsmsAnnexAControl::A537 => f.write_str("a_5_37"),
            IsmsAnnexAControl::A61 => f.write_str("a_6_1"),
            IsmsAnnexAControl::A62 => f.write_str("a_6_2"),
            IsmsAnnexAControl::A63 => f.write_str("a_6_3"),
            IsmsAnnexAControl::A64 => f.write_str("a_6_4"),
            IsmsAnnexAControl::A65 => f.write_str("a_6_5"),
            IsmsAnnexAControl::A66 => f.write_str("a_6_6"),
            IsmsAnnexAControl::A67 => f.write_str("a_6_7"),
            IsmsAnnexAControl::A68 => f.write_str("a_6_8"),
            IsmsAnnexAControl::A71 => f.write_str("a_7_1"),
            IsmsAnnexAControl::A72 => f.write_str("a_7_2"),
            IsmsAnnexAControl::A73 => f.write_str("a_7_3"),
            IsmsAnnexAControl::A74 => f.write_str("a_7_4"),
            IsmsAnnexAControl::A75 => f.write_str("a_7_5"),
            IsmsAnnexAControl::A76 => f.write_str("a_7_6"),
            IsmsAnnexAControl::A77 => f.write_str("a_7_7"),
            IsmsAnnexAControl::A78 => f.write_str("a_7_8"),
            IsmsAnnexAControl::A79 => f.write_str("a_7_9"),
            IsmsAnnexAControl::A710 => f.write_str("a_7_10"),
            IsmsAnnexAControl::A711 => f.write_str("a_7_11"),
            IsmsAnnexAControl::A712 => f.write_str("a_7_12"),
            IsmsAnnexAControl::A713 => f.write_str("a_7_13"),
            IsmsAnnexAControl::A714 => f.write_str("a_7_14"),
            IsmsAnnexAControl::A81 => f.write_str("a_8_1"),
            IsmsAnnexAControl::A82 => f.write_str("a_8_2"),
            IsmsAnnexAControl::A83 => f.write_str("a_8_3"),
            IsmsAnnexAControl::A84 => f.write_str("a_8_4"),
            IsmsAnnexAControl::A85 => f.write_str("a_8_5"),
            IsmsAnnexAControl::A86 => f.write_str("a_8_6"),
            IsmsAnnexAControl::A87 => f.write_str("a_8_7"),
            IsmsAnnexAControl::A88 => f.write_str("a_8_8"),
            IsmsAnnexAControl::A89 => f.write_str("a_8_9"),
            IsmsAnnexAControl::A810 => f.write_str("a_8_10"),
            IsmsAnnexAControl::A811 => f.write_str("a_8_11"),
            IsmsAnnexAControl::A812 => f.write_str("a_8_12"),
            IsmsAnnexAControl::A813 => f.write_str("a_8_13"),
            IsmsAnnexAControl::A814 => f.write_str("a_8_14"),
            IsmsAnnexAControl::A815 => f.write_str("a_8_15"),
            IsmsAnnexAControl::A816 => f.write_str("a_8_16"),
            IsmsAnnexAControl::A817 => f.write_str("a_8_17"),
            IsmsAnnexAControl::A818 => f.write_str("a_8_18"),
            IsmsAnnexAControl::A819 => f.write_str("a_8_19"),
            IsmsAnnexAControl::A820 => f.write_str("a_8_20"),
            IsmsAnnexAControl::A821 => f.write_str("a_8_21"),
            IsmsAnnexAControl::A822 => f.write_str("a_8_22"),
            IsmsAnnexAControl::A823 => f.write_str("a_8_23"),
            IsmsAnnexAControl::A824 => f.write_str("a_8_24"),
            IsmsAnnexAControl::A825 => f.write_str("a_8_25"),
            IsmsAnnexAControl::A826 => f.write_str("a_8_26"),
            IsmsAnnexAControl::A827 => f.write_str("a_8_27"),
            IsmsAnnexAControl::A828 => f.write_str("a_8_28"),
            IsmsAnnexAControl::A829 => f.write_str("a_8_29"),
            IsmsAnnexAControl::A830 => f.write_str("a_8_30"),
            IsmsAnnexAControl::A831 => f.write_str("a_8_31"),
            IsmsAnnexAControl::A832 => f.write_str("a_8_32"),
            IsmsAnnexAControl::A833 => f.write_str("a_8_33"),
            IsmsAnnexAControl::A834 => f.write_str("a_8_34"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsAnnexAControl {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsAnnexAControl::A51 => "a_5_1",
            IsmsAnnexAControl::A52 => "a_5_2",
            IsmsAnnexAControl::A53 => "a_5_3",
            IsmsAnnexAControl::A54 => "a_5_4",
            IsmsAnnexAControl::A55 => "a_5_5",
            IsmsAnnexAControl::A56 => "a_5_6",
            IsmsAnnexAControl::A57 => "a_5_7",
            IsmsAnnexAControl::A58 => "a_5_8",
            IsmsAnnexAControl::A59 => "a_5_9",
            IsmsAnnexAControl::A510 => "a_5_10",
            IsmsAnnexAControl::A511 => "a_5_11",
            IsmsAnnexAControl::A512 => "a_5_12",
            IsmsAnnexAControl::A513 => "a_5_13",
            IsmsAnnexAControl::A514 => "a_5_14",
            IsmsAnnexAControl::A515 => "a_5_15",
            IsmsAnnexAControl::A516 => "a_5_16",
            IsmsAnnexAControl::A517 => "a_5_17",
            IsmsAnnexAControl::A518 => "a_5_18",
            IsmsAnnexAControl::A519 => "a_5_19",
            IsmsAnnexAControl::A520 => "a_5_20",
            IsmsAnnexAControl::A521 => "a_5_21",
            IsmsAnnexAControl::A522 => "a_5_22",
            IsmsAnnexAControl::A523 => "a_5_23",
            IsmsAnnexAControl::A524 => "a_5_24",
            IsmsAnnexAControl::A525 => "a_5_25",
            IsmsAnnexAControl::A526 => "a_5_26",
            IsmsAnnexAControl::A527 => "a_5_27",
            IsmsAnnexAControl::A528 => "a_5_28",
            IsmsAnnexAControl::A529 => "a_5_29",
            IsmsAnnexAControl::A530 => "a_5_30",
            IsmsAnnexAControl::A531 => "a_5_31",
            IsmsAnnexAControl::A532 => "a_5_32",
            IsmsAnnexAControl::A533 => "a_5_33",
            IsmsAnnexAControl::A534 => "a_5_34",
            IsmsAnnexAControl::A535 => "a_5_35",
            IsmsAnnexAControl::A536 => "a_5_36",
            IsmsAnnexAControl::A537 => "a_5_37",
            IsmsAnnexAControl::A61 => "a_6_1",
            IsmsAnnexAControl::A62 => "a_6_2",
            IsmsAnnexAControl::A63 => "a_6_3",
            IsmsAnnexAControl::A64 => "a_6_4",
            IsmsAnnexAControl::A65 => "a_6_5",
            IsmsAnnexAControl::A66 => "a_6_6",
            IsmsAnnexAControl::A67 => "a_6_7",
            IsmsAnnexAControl::A68 => "a_6_8",
            IsmsAnnexAControl::A71 => "a_7_1",
            IsmsAnnexAControl::A72 => "a_7_2",
            IsmsAnnexAControl::A73 => "a_7_3",
            IsmsAnnexAControl::A74 => "a_7_4",
            IsmsAnnexAControl::A75 => "a_7_5",
            IsmsAnnexAControl::A76 => "a_7_6",
            IsmsAnnexAControl::A77 => "a_7_7",
            IsmsAnnexAControl::A78 => "a_7_8",
            IsmsAnnexAControl::A79 => "a_7_9",
            IsmsAnnexAControl::A710 => "a_7_10",
            IsmsAnnexAControl::A711 => "a_7_11",
            IsmsAnnexAControl::A712 => "a_7_12",
            IsmsAnnexAControl::A713 => "a_7_13",
            IsmsAnnexAControl::A714 => "a_7_14",
            IsmsAnnexAControl::A81 => "a_8_1",
            IsmsAnnexAControl::A82 => "a_8_2",
            IsmsAnnexAControl::A83 => "a_8_3",
            IsmsAnnexAControl::A84 => "a_8_4",
            IsmsAnnexAControl::A85 => "a_8_5",
            IsmsAnnexAControl::A86 => "a_8_6",
            IsmsAnnexAControl::A87 => "a_8_7",
            IsmsAnnexAControl::A88 => "a_8_8",
            IsmsAnnexAControl::A89 => "a_8_9",
            IsmsAnnexAControl::A810 => "a_8_10",
            IsmsAnnexAControl::A811 => "a_8_11",
            IsmsAnnexAControl::A812 => "a_8_12",
            IsmsAnnexAControl::A813 => "a_8_13",
            IsmsAnnexAControl::A814 => "a_8_14",
            IsmsAnnexAControl::A815 => "a_8_15",
            IsmsAnnexAControl::A816 => "a_8_16",
            IsmsAnnexAControl::A817 => "a_8_17",
            IsmsAnnexAControl::A818 => "a_8_18",
            IsmsAnnexAControl::A819 => "a_8_19",
            IsmsAnnexAControl::A820 => "a_8_20",
            IsmsAnnexAControl::A821 => "a_8_21",
            IsmsAnnexAControl::A822 => "a_8_22",
            IsmsAnnexAControl::A823 => "a_8_23",
            IsmsAnnexAControl::A824 => "a_8_24",
            IsmsAnnexAControl::A825 => "a_8_25",
            IsmsAnnexAControl::A826 => "a_8_26",
            IsmsAnnexAControl::A827 => "a_8_27",
            IsmsAnnexAControl::A828 => "a_8_28",
            IsmsAnnexAControl::A829 => "a_8_29",
            IsmsAnnexAControl::A830 => "a_8_30",
            IsmsAnnexAControl::A831 => "a_8_31",
            IsmsAnnexAControl::A832 => "a_8_32",
            IsmsAnnexAControl::A833 => "a_8_33",
            IsmsAnnexAControl::A834 => "a_8_34",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsAnnexAControl {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "a_5_1" | "A51" => Ok(IsmsAnnexAControl::A51),
                "a_5_2" | "A52" => Ok(IsmsAnnexAControl::A52),
                "a_5_3" | "A53" => Ok(IsmsAnnexAControl::A53),
                "a_5_4" | "A54" => Ok(IsmsAnnexAControl::A54),
                "a_5_5" | "A55" => Ok(IsmsAnnexAControl::A55),
                "a_5_6" | "A56" => Ok(IsmsAnnexAControl::A56),
                "a_5_7" | "A57" => Ok(IsmsAnnexAControl::A57),
                "a_5_8" | "A58" => Ok(IsmsAnnexAControl::A58),
                "a_5_9" | "A59" => Ok(IsmsAnnexAControl::A59),
                "a_5_10" | "A510" => Ok(IsmsAnnexAControl::A510),
                "a_5_11" | "A511" => Ok(IsmsAnnexAControl::A511),
                "a_5_12" | "A512" => Ok(IsmsAnnexAControl::A512),
                "a_5_13" | "A513" => Ok(IsmsAnnexAControl::A513),
                "a_5_14" | "A514" => Ok(IsmsAnnexAControl::A514),
                "a_5_15" | "A515" => Ok(IsmsAnnexAControl::A515),
                "a_5_16" | "A516" => Ok(IsmsAnnexAControl::A516),
                "a_5_17" | "A517" => Ok(IsmsAnnexAControl::A517),
                "a_5_18" | "A518" => Ok(IsmsAnnexAControl::A518),
                "a_5_19" | "A519" => Ok(IsmsAnnexAControl::A519),
                "a_5_20" | "A520" => Ok(IsmsAnnexAControl::A520),
                "a_5_21" | "A521" => Ok(IsmsAnnexAControl::A521),
                "a_5_22" | "A522" => Ok(IsmsAnnexAControl::A522),
                "a_5_23" | "A523" => Ok(IsmsAnnexAControl::A523),
                "a_5_24" | "A524" => Ok(IsmsAnnexAControl::A524),
                "a_5_25" | "A525" => Ok(IsmsAnnexAControl::A525),
                "a_5_26" | "A526" => Ok(IsmsAnnexAControl::A526),
                "a_5_27" | "A527" => Ok(IsmsAnnexAControl::A527),
                "a_5_28" | "A528" => Ok(IsmsAnnexAControl::A528),
                "a_5_29" | "A529" => Ok(IsmsAnnexAControl::A529),
                "a_5_30" | "A530" => Ok(IsmsAnnexAControl::A530),
                "a_5_31" | "A531" => Ok(IsmsAnnexAControl::A531),
                "a_5_32" | "A532" => Ok(IsmsAnnexAControl::A532),
                "a_5_33" | "A533" => Ok(IsmsAnnexAControl::A533),
                "a_5_34" | "A534" => Ok(IsmsAnnexAControl::A534),
                "a_5_35" | "A535" => Ok(IsmsAnnexAControl::A535),
                "a_5_36" | "A536" => Ok(IsmsAnnexAControl::A536),
                "a_5_37" | "A537" => Ok(IsmsAnnexAControl::A537),
                "a_6_1" | "A61" => Ok(IsmsAnnexAControl::A61),
                "a_6_2" | "A62" => Ok(IsmsAnnexAControl::A62),
                "a_6_3" | "A63" => Ok(IsmsAnnexAControl::A63),
                "a_6_4" | "A64" => Ok(IsmsAnnexAControl::A64),
                "a_6_5" | "A65" => Ok(IsmsAnnexAControl::A65),
                "a_6_6" | "A66" => Ok(IsmsAnnexAControl::A66),
                "a_6_7" | "A67" => Ok(IsmsAnnexAControl::A67),
                "a_6_8" | "A68" => Ok(IsmsAnnexAControl::A68),
                "a_7_1" | "A71" => Ok(IsmsAnnexAControl::A71),
                "a_7_2" | "A72" => Ok(IsmsAnnexAControl::A72),
                "a_7_3" | "A73" => Ok(IsmsAnnexAControl::A73),
                "a_7_4" | "A74" => Ok(IsmsAnnexAControl::A74),
                "a_7_5" | "A75" => Ok(IsmsAnnexAControl::A75),
                "a_7_6" | "A76" => Ok(IsmsAnnexAControl::A76),
                "a_7_7" | "A77" => Ok(IsmsAnnexAControl::A77),
                "a_7_8" | "A78" => Ok(IsmsAnnexAControl::A78),
                "a_7_9" | "A79" => Ok(IsmsAnnexAControl::A79),
                "a_7_10" | "A710" => Ok(IsmsAnnexAControl::A710),
                "a_7_11" | "A711" => Ok(IsmsAnnexAControl::A711),
                "a_7_12" | "A712" => Ok(IsmsAnnexAControl::A712),
                "a_7_13" | "A713" => Ok(IsmsAnnexAControl::A713),
                "a_7_14" | "A714" => Ok(IsmsAnnexAControl::A714),
                "a_8_1" | "A81" => Ok(IsmsAnnexAControl::A81),
                "a_8_2" | "A82" => Ok(IsmsAnnexAControl::A82),
                "a_8_3" | "A83" => Ok(IsmsAnnexAControl::A83),
                "a_8_4" | "A84" => Ok(IsmsAnnexAControl::A84),
                "a_8_5" | "A85" => Ok(IsmsAnnexAControl::A85),
                "a_8_6" | "A86" => Ok(IsmsAnnexAControl::A86),
                "a_8_7" | "A87" => Ok(IsmsAnnexAControl::A87),
                "a_8_8" | "A88" => Ok(IsmsAnnexAControl::A88),
                "a_8_9" | "A89" => Ok(IsmsAnnexAControl::A89),
                "a_8_10" | "A810" => Ok(IsmsAnnexAControl::A810),
                "a_8_11" | "A811" => Ok(IsmsAnnexAControl::A811),
                "a_8_12" | "A812" => Ok(IsmsAnnexAControl::A812),
                "a_8_13" | "A813" => Ok(IsmsAnnexAControl::A813),
                "a_8_14" | "A814" => Ok(IsmsAnnexAControl::A814),
                "a_8_15" | "A815" => Ok(IsmsAnnexAControl::A815),
                "a_8_16" | "A816" => Ok(IsmsAnnexAControl::A816),
                "a_8_17" | "A817" => Ok(IsmsAnnexAControl::A817),
                "a_8_18" | "A818" => Ok(IsmsAnnexAControl::A818),
                "a_8_19" | "A819" => Ok(IsmsAnnexAControl::A819),
                "a_8_20" | "A820" => Ok(IsmsAnnexAControl::A820),
                "a_8_21" | "A821" => Ok(IsmsAnnexAControl::A821),
                "a_8_22" | "A822" => Ok(IsmsAnnexAControl::A822),
                "a_8_23" | "A823" => Ok(IsmsAnnexAControl::A823),
                "a_8_24" | "A824" => Ok(IsmsAnnexAControl::A824),
                "a_8_25" | "A825" => Ok(IsmsAnnexAControl::A825),
                "a_8_26" | "A826" => Ok(IsmsAnnexAControl::A826),
                "a_8_27" | "A827" => Ok(IsmsAnnexAControl::A827),
                "a_8_28" | "A828" => Ok(IsmsAnnexAControl::A828),
                "a_8_29" | "A829" => Ok(IsmsAnnexAControl::A829),
                "a_8_30" | "A830" => Ok(IsmsAnnexAControl::A830),
                "a_8_31" | "A831" => Ok(IsmsAnnexAControl::A831),
                "a_8_32" | "A832" => Ok(IsmsAnnexAControl::A832),
                "a_8_33" | "A833" => Ok(IsmsAnnexAControl::A833),
                "a_8_34" | "A834" => Ok(IsmsAnnexAControl::A834),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsAnnexAControl: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsAnnexAControl)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsAnnexAControl {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsImplementationStatus {
    NotStarted,
    Planned,
    InProgress,
    Implemented,
}

impl core::fmt::Display for IsmsImplementationStatus {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsImplementationStatus::NotStarted => f.write_str("not_started"),
            IsmsImplementationStatus::Planned => f.write_str("planned"),
            IsmsImplementationStatus::InProgress => f.write_str("in_progress"),
            IsmsImplementationStatus::Implemented => f.write_str("implemented"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsImplementationStatus {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsImplementationStatus::NotStarted => "not_started",
            IsmsImplementationStatus::Planned => "planned",
            IsmsImplementationStatus::InProgress => "in_progress",
            IsmsImplementationStatus::Implemented => "implemented",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsImplementationStatus {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "not_started" | "NotStarted" => Ok(IsmsImplementationStatus::NotStarted),
                "planned" | "Planned" => Ok(IsmsImplementationStatus::Planned),
                "in_progress" | "InProgress" => Ok(IsmsImplementationStatus::InProgress),
                "implemented" | "Implemented" => Ok(IsmsImplementationStatus::Implemented),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsImplementationStatus: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsImplementationStatus)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsImplementationStatus {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['not_started', 'planned', 'in_progress', 'implemented']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsRiskTreatmentOption {
    Modify,
    Retain,
    Avoid,
    Share,
}

impl core::fmt::Display for IsmsRiskTreatmentOption {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsRiskTreatmentOption::Modify => f.write_str("modify"),
            IsmsRiskTreatmentOption::Retain => f.write_str("retain"),
            IsmsRiskTreatmentOption::Avoid => f.write_str("avoid"),
            IsmsRiskTreatmentOption::Share => f.write_str("share"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsRiskTreatmentOption {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsRiskTreatmentOption::Modify => "modify",
            IsmsRiskTreatmentOption::Retain => "retain",
            IsmsRiskTreatmentOption::Avoid => "avoid",
            IsmsRiskTreatmentOption::Share => "share",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsRiskTreatmentOption {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "modify" | "Modify" => Ok(IsmsRiskTreatmentOption::Modify),
                "retain" | "Retain" => Ok(IsmsRiskTreatmentOption::Retain),
                "avoid" | "Avoid" => Ok(IsmsRiskTreatmentOption::Avoid),
                "share" | "Share" => Ok(IsmsRiskTreatmentOption::Share),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsRiskTreatmentOption: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsRiskTreatmentOption)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsRiskTreatmentOption {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['modify', 'retain', 'avoid', 'share']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsRiskLevel {
    VeryLow,
    Low,
    Medium,
    High,
    Critical,
}

impl core::fmt::Display for IsmsRiskLevel {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsRiskLevel::VeryLow => f.write_str("very_low"),
            IsmsRiskLevel::Low => f.write_str("low"),
            IsmsRiskLevel::Medium => f.write_str("medium"),
            IsmsRiskLevel::High => f.write_str("high"),
            IsmsRiskLevel::Critical => f.write_str("critical"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsRiskLevel {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsRiskLevel::VeryLow => "very_low",
            IsmsRiskLevel::Low => "low",
            IsmsRiskLevel::Medium => "medium",
            IsmsRiskLevel::High => "high",
            IsmsRiskLevel::Critical => "critical",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsRiskLevel {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "very_low" | "VeryLow" => Ok(IsmsRiskLevel::VeryLow),
                "low" | "Low" => Ok(IsmsRiskLevel::Low),
                "medium" | "Medium" => Ok(IsmsRiskLevel::Medium),
                "high" | "High" => Ok(IsmsRiskLevel::High),
                "critical" | "Critical" => Ok(IsmsRiskLevel::Critical),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsRiskLevel: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsRiskLevel)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsRiskLevel {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['very_low', 'low', 'medium', 'high', 'critical']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsLikelihood {
    Rare,
    Unlikely,
    Possible,
    Likely,
    AlmostCertain,
}

impl core::fmt::Display for IsmsLikelihood {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsLikelihood::Rare => f.write_str("rare"),
            IsmsLikelihood::Unlikely => f.write_str("unlikely"),
            IsmsLikelihood::Possible => f.write_str("possible"),
            IsmsLikelihood::Likely => f.write_str("likely"),
            IsmsLikelihood::AlmostCertain => f.write_str("almost_certain"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsLikelihood {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsLikelihood::Rare => "rare",
            IsmsLikelihood::Unlikely => "unlikely",
            IsmsLikelihood::Possible => "possible",
            IsmsLikelihood::Likely => "likely",
            IsmsLikelihood::AlmostCertain => "almost_certain",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsLikelihood {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "rare" | "Rare" => Ok(IsmsLikelihood::Rare),
                "unlikely" | "Unlikely" => Ok(IsmsLikelihood::Unlikely),
                "possible" | "Possible" => Ok(IsmsLikelihood::Possible),
                "likely" | "Likely" => Ok(IsmsLikelihood::Likely),
                "almost_certain" | "AlmostCertain" => Ok(IsmsLikelihood::AlmostCertain),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsLikelihood: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsLikelihood)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsLikelihood {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['rare', 'unlikely', 'possible', 'likely', 'almost_certain']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsImpact {
    Negligible,
    Minor,
    Moderate,
    Major,
    Severe,
}

impl core::fmt::Display for IsmsImpact {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsImpact::Negligible => f.write_str("negligible"),
            IsmsImpact::Minor => f.write_str("minor"),
            IsmsImpact::Moderate => f.write_str("moderate"),
            IsmsImpact::Major => f.write_str("major"),
            IsmsImpact::Severe => f.write_str("severe"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsImpact {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsImpact::Negligible => "negligible",
            IsmsImpact::Minor => "minor",
            IsmsImpact::Moderate => "moderate",
            IsmsImpact::Major => "major",
            IsmsImpact::Severe => "severe",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsImpact {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "negligible" | "Negligible" => Ok(IsmsImpact::Negligible),
                "minor" | "Minor" => Ok(IsmsImpact::Minor),
                "moderate" | "Moderate" => Ok(IsmsImpact::Moderate),
                "major" | "Major" => Ok(IsmsImpact::Major),
                "severe" | "Severe" => Ok(IsmsImpact::Severe),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsImpact: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsImpact)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsImpact {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['negligible', 'minor', 'moderate', 'major', 'severe']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsSecurityProperty {
    Confidentiality,
    Integrity,
    Availability,
}

impl core::fmt::Display for IsmsSecurityProperty {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsSecurityProperty::Confidentiality => f.write_str("confidentiality"),
            IsmsSecurityProperty::Integrity => f.write_str("integrity"),
            IsmsSecurityProperty::Availability => f.write_str("availability"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsSecurityProperty {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsSecurityProperty::Confidentiality => "confidentiality",
            IsmsSecurityProperty::Integrity => "integrity",
            IsmsSecurityProperty::Availability => "availability",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsSecurityProperty {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "confidentiality" | "Confidentiality" => Ok(IsmsSecurityProperty::Confidentiality),
                "integrity" | "Integrity" => Ok(IsmsSecurityProperty::Integrity),
                "availability" | "Availability" => Ok(IsmsSecurityProperty::Availability),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsSecurityProperty: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsSecurityProperty)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsSecurityProperty {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['confidentiality', 'integrity', 'availability']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsDocumentKind {
    Procedure,
    Standard,
    Guideline,
    Record,
    Plan,
    Report,
}

impl core::fmt::Display for IsmsDocumentKind {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsDocumentKind::Procedure => f.write_str("procedure"),
            IsmsDocumentKind::Standard => f.write_str("standard"),
            IsmsDocumentKind::Guideline => f.write_str("guideline"),
            IsmsDocumentKind::Record => f.write_str("record"),
            IsmsDocumentKind::Plan => f.write_str("plan"),
            IsmsDocumentKind::Report => f.write_str("report"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsDocumentKind {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsDocumentKind::Procedure => "procedure",
            IsmsDocumentKind::Standard => "standard",
            IsmsDocumentKind::Guideline => "guideline",
            IsmsDocumentKind::Record => "record",
            IsmsDocumentKind::Plan => "plan",
            IsmsDocumentKind::Report => "report",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsDocumentKind {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "procedure" | "Procedure" => Ok(IsmsDocumentKind::Procedure),
                "standard" | "Standard" => Ok(IsmsDocumentKind::Standard),
                "guideline" | "Guideline" => Ok(IsmsDocumentKind::Guideline),
                "record" | "Record" => Ok(IsmsDocumentKind::Record),
                "plan" | "Plan" => Ok(IsmsDocumentKind::Plan),
                "report" | "Report" => Ok(IsmsDocumentKind::Report),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsDocumentKind: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsDocumentKind)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsDocumentKind {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['procedure', 'standard', 'guideline', 'record', 'plan', 'report']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsAuditType {
    FirstParty,
    SecondParty,
    ThirdParty,
}

impl core::fmt::Display for IsmsAuditType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsAuditType::FirstParty => f.write_str("first_party"),
            IsmsAuditType::SecondParty => f.write_str("second_party"),
            IsmsAuditType::ThirdParty => f.write_str("third_party"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsAuditType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsAuditType::FirstParty => "first_party",
            IsmsAuditType::SecondParty => "second_party",
            IsmsAuditType::ThirdParty => "third_party",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsAuditType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "first_party" | "FirstParty" => Ok(IsmsAuditType::FirstParty),
                "second_party" | "SecondParty" => Ok(IsmsAuditType::SecondParty),
                "third_party" | "ThirdParty" => Ok(IsmsAuditType::ThirdParty),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsAuditType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsAuditType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsAuditType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['first_party', 'second_party', 'third_party']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsAuditFindingType {
    MajorNonconformity,
    MinorNonconformity,
    Observation,
    PositiveFinding,
}

impl core::fmt::Display for IsmsAuditFindingType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsAuditFindingType::MajorNonconformity => f.write_str("major_nonconformity"),
            IsmsAuditFindingType::MinorNonconformity => f.write_str("minor_nonconformity"),
            IsmsAuditFindingType::Observation => f.write_str("observation"),
            IsmsAuditFindingType::PositiveFinding => f.write_str("positive_finding"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsAuditFindingType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsAuditFindingType::MajorNonconformity => "major_nonconformity",
            IsmsAuditFindingType::MinorNonconformity => "minor_nonconformity",
            IsmsAuditFindingType::Observation => "observation",
            IsmsAuditFindingType::PositiveFinding => "positive_finding",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsAuditFindingType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "major_nonconformity" | "MajorNonconformity" => Ok(IsmsAuditFindingType::MajorNonconformity),
                "minor_nonconformity" | "MinorNonconformity" => Ok(IsmsAuditFindingType::MinorNonconformity),
                "observation" | "Observation" => Ok(IsmsAuditFindingType::Observation),
                "positive_finding" | "PositiveFinding" => Ok(IsmsAuditFindingType::PositiveFinding),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsAuditFindingType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsAuditFindingType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsAuditFindingType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsIncidentCategory {
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

impl core::fmt::Display for IsmsIncidentCategory {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsIncidentCategory::Malware => f.write_str("malware"),
            IsmsIncidentCategory::Ransomware => f.write_str("ransomware"),
            IsmsIncidentCategory::Phishing => f.write_str("phishing"),
            IsmsIncidentCategory::SocialEngineering => f.write_str("social_engineering"),
            IsmsIncidentCategory::UnauthorizedAccess => f.write_str("unauthorized_access"),
            IsmsIncidentCategory::AccountCompromise => f.write_str("account_compromise"),
            IsmsIncidentCategory::PrivilegeMisuse => f.write_str("privilege_misuse"),
            IsmsIncidentCategory::DataBreach => f.write_str("data_breach"),
            IsmsIncidentCategory::DataLoss => f.write_str("data_loss"),
            IsmsIncidentCategory::DenialOfService => f.write_str("denial_of_service"),
            IsmsIncidentCategory::WebApplicationAttack => f.write_str("web_application_attack"),
            IsmsIncidentCategory::SupplyChain => f.write_str("supply_chain"),
            IsmsIncidentCategory::InsiderThreat => f.write_str("insider_threat"),
            IsmsIncidentCategory::PhysicalSecurity => f.write_str("physical_security"),
            IsmsIncidentCategory::ConfigurationError => f.write_str("configuration_error"),
            IsmsIncidentCategory::CryptographicFailure => f.write_str("cryptographic_failure"),
            IsmsIncidentCategory::PolicyViolation => f.write_str("policy_violation"),
            IsmsIncidentCategory::Other => f.write_str("other"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsIncidentCategory {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsIncidentCategory::Malware => "malware",
            IsmsIncidentCategory::Ransomware => "ransomware",
            IsmsIncidentCategory::Phishing => "phishing",
            IsmsIncidentCategory::SocialEngineering => "social_engineering",
            IsmsIncidentCategory::UnauthorizedAccess => "unauthorized_access",
            IsmsIncidentCategory::AccountCompromise => "account_compromise",
            IsmsIncidentCategory::PrivilegeMisuse => "privilege_misuse",
            IsmsIncidentCategory::DataBreach => "data_breach",
            IsmsIncidentCategory::DataLoss => "data_loss",
            IsmsIncidentCategory::DenialOfService => "denial_of_service",
            IsmsIncidentCategory::WebApplicationAttack => "web_application_attack",
            IsmsIncidentCategory::SupplyChain => "supply_chain",
            IsmsIncidentCategory::InsiderThreat => "insider_threat",
            IsmsIncidentCategory::PhysicalSecurity => "physical_security",
            IsmsIncidentCategory::ConfigurationError => "configuration_error",
            IsmsIncidentCategory::CryptographicFailure => "cryptographic_failure",
            IsmsIncidentCategory::PolicyViolation => "policy_violation",
            IsmsIncidentCategory::Other => "other",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsIncidentCategory {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "malware" | "Malware" => Ok(IsmsIncidentCategory::Malware),
                "ransomware" | "Ransomware" => Ok(IsmsIncidentCategory::Ransomware),
                "phishing" | "Phishing" => Ok(IsmsIncidentCategory::Phishing),
                "social_engineering" | "SocialEngineering" => Ok(IsmsIncidentCategory::SocialEngineering),
                "unauthorized_access" | "UnauthorizedAccess" => Ok(IsmsIncidentCategory::UnauthorizedAccess),
                "account_compromise" | "AccountCompromise" => Ok(IsmsIncidentCategory::AccountCompromise),
                "privilege_misuse" | "PrivilegeMisuse" => Ok(IsmsIncidentCategory::PrivilegeMisuse),
                "data_breach" | "DataBreach" => Ok(IsmsIncidentCategory::DataBreach),
                "data_loss" | "DataLoss" => Ok(IsmsIncidentCategory::DataLoss),
                "denial_of_service" | "DenialOfService" => Ok(IsmsIncidentCategory::DenialOfService),
                "web_application_attack" | "WebApplicationAttack" => Ok(IsmsIncidentCategory::WebApplicationAttack),
                "supply_chain" | "SupplyChain" => Ok(IsmsIncidentCategory::SupplyChain),
                "insider_threat" | "InsiderThreat" => Ok(IsmsIncidentCategory::InsiderThreat),
                "physical_security" | "PhysicalSecurity" => Ok(IsmsIncidentCategory::PhysicalSecurity),
                "configuration_error" | "ConfigurationError" => Ok(IsmsIncidentCategory::ConfigurationError),
                "cryptographic_failure" | "CryptographicFailure" => Ok(IsmsIncidentCategory::CryptographicFailure),
                "policy_violation" | "PolicyViolation" => Ok(IsmsIncidentCategory::PolicyViolation),
                "other" | "Other" => Ok(IsmsIncidentCategory::Other),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsIncidentCategory: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsIncidentCategory)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsIncidentCategory {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum IsmsManagementSystemStandard {
    IsoIec27001,
    IsoIec27701,
    IsoIec42001,
    Iso9001,
    Iso14001,
    Iso22301,
    IsoIec200001,
}

impl core::fmt::Display for IsmsManagementSystemStandard {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            IsmsManagementSystemStandard::IsoIec27001 => f.write_str("iso_iec_27001"),
            IsmsManagementSystemStandard::IsoIec27701 => f.write_str("iso_iec_27701"),
            IsmsManagementSystemStandard::IsoIec42001 => f.write_str("iso_iec_42001"),
            IsmsManagementSystemStandard::Iso9001 => f.write_str("iso_9001"),
            IsmsManagementSystemStandard::Iso14001 => f.write_str("iso_14001"),
            IsmsManagementSystemStandard::Iso22301 => f.write_str("iso_22301"),
            IsmsManagementSystemStandard::IsoIec200001 => f.write_str("iso_iec_20000_1"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsManagementSystemStandard {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            IsmsManagementSystemStandard::IsoIec27001 => "iso_iec_27001",
            IsmsManagementSystemStandard::IsoIec27701 => "iso_iec_27701",
            IsmsManagementSystemStandard::IsoIec42001 => "iso_iec_42001",
            IsmsManagementSystemStandard::Iso9001 => "iso_9001",
            IsmsManagementSystemStandard::Iso14001 => "iso_14001",
            IsmsManagementSystemStandard::Iso22301 => "iso_22301",
            IsmsManagementSystemStandard::IsoIec200001 => "iso_iec_20000_1",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsManagementSystemStandard {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "iso_iec_27001" | "IsoIec27001" => Ok(IsmsManagementSystemStandard::IsoIec27001),
                "iso_iec_27701" | "IsoIec27701" => Ok(IsmsManagementSystemStandard::IsoIec27701),
                "iso_iec_42001" | "IsoIec42001" => Ok(IsmsManagementSystemStandard::IsoIec42001),
                "iso_9001" | "Iso9001" => Ok(IsmsManagementSystemStandard::Iso9001),
                "iso_14001" | "Iso14001" => Ok(IsmsManagementSystemStandard::Iso14001),
                "iso_22301" | "Iso22301" => Ok(IsmsManagementSystemStandard::Iso22301),
                "iso_iec_20000_1" | "IsoIec200001" => Ok(IsmsManagementSystemStandard::IsoIec200001),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for IsmsManagementSystemStandard: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(IsmsManagementSystemStandard)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for IsmsManagementSystemStandard {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['iso_iec_27001', 'iso_iec_27701', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1']",
            "typing".into(),
        )
    }
}

// Classes

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsRecordMixin {
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRecordMixin {
    #[new]
    #[pyo3(signature = (isms_id, title, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, description: Option<String>) -> Self {
        IsmsRecordMixin{isms_id, title, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRecordMixin>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRecordMixin> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRecordMixin>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRecordMixin",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRecordMixin {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum IsmsRecordMixinOrSubtype {    IsmsManagementSystem(IsmsManagementSystem),     IsmsOrganization(IsmsOrganization),     IsmsInterestedParty(IsmsInterestedParty),     IsmsPolicy(IsmsPolicy),     IsmsTopicSpecificPolicy(IsmsTopicSpecificPolicy),     IsmsRole(IsmsRole),     IsmsObjective(IsmsObjective),     IsmsRiskAssessmentProcess(IsmsRiskAssessmentProcess),     IsmsRiskAssessment(IsmsRiskAssessment),     IsmsRisk(IsmsRisk),     IsmsRiskTreatmentProcess(IsmsRiskTreatmentProcess),     IsmsRiskTreatmentPlan(IsmsRiskTreatmentPlan),     IsmsStatementOfApplicability(IsmsStatementOfApplicability),     IsmsControl(IsmsControl),     IsmsAsset(IsmsAsset),     IsmsResource(IsmsResource),     IsmsCompetenceRecord(IsmsCompetenceRecord),     IsmsAwarenessProgramme(IsmsAwarenessProgramme),     IsmsCommunicationPlan(IsmsCommunicationPlan),     IsmsDocumentedInformation(IsmsDocumentedInformation),     IsmsOperationalProcedure(IsmsOperationalProcedure),     IsmsMonitoringProgramme(IsmsMonitoringProgramme),     IsmsAuditProgramme(IsmsAuditProgramme),     IsmsAudit(IsmsAudit),     IsmsAuditFinding(IsmsAuditFinding),     IsmsManagementReview(IsmsManagementReview),     IsmsNonconformity(IsmsNonconformity),     IsmsCorrectiveAction(IsmsCorrectiveAction),     IsmsImprovementOpportunity(IsmsImprovementOpportunity),     IsmsSecurityEvent(IsmsSecurityEvent),     IsmsSecurityIncident(IsmsSecurityIncident)}

impl From<IsmsManagementSystem>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsManagementSystem)   -> Self { Self::IsmsManagementSystem(x) } }
impl From<IsmsOrganization>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsOrganization)   -> Self { Self::IsmsOrganization(x) } }
impl From<IsmsInterestedParty>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsInterestedParty)   -> Self { Self::IsmsInterestedParty(x) } }
impl From<IsmsPolicy>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsPolicy)   -> Self { Self::IsmsPolicy(x) } }
impl From<IsmsTopicSpecificPolicy>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsTopicSpecificPolicy)   -> Self { Self::IsmsTopicSpecificPolicy(x) } }
impl From<IsmsRole>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRole)   -> Self { Self::IsmsRole(x) } }
impl From<IsmsObjective>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsObjective)   -> Self { Self::IsmsObjective(x) } }
impl From<IsmsRiskAssessmentProcess>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRiskAssessmentProcess)   -> Self { Self::IsmsRiskAssessmentProcess(x) } }
impl From<IsmsRiskAssessment>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRiskAssessment)   -> Self { Self::IsmsRiskAssessment(x) } }
impl From<IsmsRisk>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRisk)   -> Self { Self::IsmsRisk(x) } }
impl From<IsmsRiskTreatmentProcess>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRiskTreatmentProcess)   -> Self { Self::IsmsRiskTreatmentProcess(x) } }
impl From<IsmsRiskTreatmentPlan>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsRiskTreatmentPlan)   -> Self { Self::IsmsRiskTreatmentPlan(x) } }
impl From<IsmsStatementOfApplicability>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsStatementOfApplicability)   -> Self { Self::IsmsStatementOfApplicability(x) } }
impl From<IsmsControl>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsControl)   -> Self { Self::IsmsControl(x) } }
impl From<IsmsAsset>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsAsset)   -> Self { Self::IsmsAsset(x) } }
impl From<IsmsResource>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsResource)   -> Self { Self::IsmsResource(x) } }
impl From<IsmsCompetenceRecord>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsCompetenceRecord)   -> Self { Self::IsmsCompetenceRecord(x) } }
impl From<IsmsAwarenessProgramme>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsAwarenessProgramme)   -> Self { Self::IsmsAwarenessProgramme(x) } }
impl From<IsmsCommunicationPlan>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsCommunicationPlan)   -> Self { Self::IsmsCommunicationPlan(x) } }
impl From<IsmsDocumentedInformation>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsDocumentedInformation)   -> Self { Self::IsmsDocumentedInformation(x) } }
impl From<IsmsOperationalProcedure>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsOperationalProcedure)   -> Self { Self::IsmsOperationalProcedure(x) } }
impl From<IsmsMonitoringProgramme>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsMonitoringProgramme)   -> Self { Self::IsmsMonitoringProgramme(x) } }
impl From<IsmsAuditProgramme>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsAuditProgramme)   -> Self { Self::IsmsAuditProgramme(x) } }
impl From<IsmsAudit>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsAudit)   -> Self { Self::IsmsAudit(x) } }
impl From<IsmsAuditFinding>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsAuditFinding)   -> Self { Self::IsmsAuditFinding(x) } }
impl From<IsmsManagementReview>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsManagementReview)   -> Self { Self::IsmsManagementReview(x) } }
impl From<IsmsNonconformity>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsNonconformity)   -> Self { Self::IsmsNonconformity(x) } }
impl From<IsmsCorrectiveAction>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsCorrectiveAction)   -> Self { Self::IsmsCorrectiveAction(x) } }
impl From<IsmsImprovementOpportunity>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsImprovementOpportunity)   -> Self { Self::IsmsImprovementOpportunity(x) } }
impl From<IsmsSecurityEvent>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsSecurityEvent)   -> Self { Self::IsmsSecurityEvent(x) } }
impl From<IsmsSecurityIncident>   for IsmsRecordMixinOrSubtype { fn from(x: IsmsSecurityIncident)   -> Self { Self::IsmsSecurityIncident(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsRecordMixinOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsManagementSystem>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementSystem(val));
        }        if let Ok(val) = ob.extract::<IsmsOrganization>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOrganization(val));
        }        if let Ok(val) = ob.extract::<IsmsInterestedParty>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsInterestedParty(val));
        }        if let Ok(val) = ob.extract::<IsmsPolicy>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsPolicy(val));
        }        if let Ok(val) = ob.extract::<IsmsTopicSpecificPolicy>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsTopicSpecificPolicy(val));
        }        if let Ok(val) = ob.extract::<IsmsRole>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRole(val));
        }        if let Ok(val) = ob.extract::<IsmsObjective>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsObjective(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskAssessmentProcess>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessmentProcess(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskAssessment>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessment(val));
        }        if let Ok(val) = ob.extract::<IsmsRisk>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRisk(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskTreatmentProcess>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentProcess(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskTreatmentPlan>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentPlan(val));
        }        if let Ok(val) = ob.extract::<IsmsStatementOfApplicability>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsStatementOfApplicability(val));
        }        if let Ok(val) = ob.extract::<IsmsControl>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsControl(val));
        }        if let Ok(val) = ob.extract::<IsmsAsset>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAsset(val));
        }        if let Ok(val) = ob.extract::<IsmsResource>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsResource(val));
        }        if let Ok(val) = ob.extract::<IsmsCompetenceRecord>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCompetenceRecord(val));
        }        if let Ok(val) = ob.extract::<IsmsAwarenessProgramme>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAwarenessProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsCommunicationPlan>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCommunicationPlan(val));
        }        if let Ok(val) = ob.extract::<IsmsDocumentedInformation>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsDocumentedInformation(val));
        }        if let Ok(val) = ob.extract::<IsmsOperationalProcedure>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOperationalProcedure(val));
        }        if let Ok(val) = ob.extract::<IsmsMonitoringProgramme>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsMonitoringProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsAuditProgramme>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsAudit>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAudit(val));
        }        if let Ok(val) = ob.extract::<IsmsAuditFinding>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditFinding(val));
        }        if let Ok(val) = ob.extract::<IsmsManagementReview>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementReview(val));
        }        if let Ok(val) = ob.extract::<IsmsNonconformity>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsNonconformity(val));
        }        if let Ok(val) = ob.extract::<IsmsCorrectiveAction>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCorrectiveAction(val));
        }        if let Ok(val) = ob.extract::<IsmsImprovementOpportunity>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsImprovementOpportunity(val));
        }        if let Ok(val) = ob.extract::<IsmsSecurityEvent>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityEvent(val));
        }        if let Ok(val) = ob.extract::<IsmsSecurityIncident>() {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityIncident(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRecordMixinOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsRecordMixinOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            IsmsRecordMixinOrSubtype::IsmsManagementSystem(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsOrganization(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsInterestedParty(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRole(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsObjective(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRiskAssessment(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRisk(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsStatementOfApplicability(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsControl(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsAsset(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsResource(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsCompetenceRecord(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsAwarenessProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsCommunicationPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsDocumentedInformation(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsOperationalProcedure(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsMonitoringProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsAuditProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsAudit(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsAuditFinding(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsManagementReview(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsNonconformity(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsCorrectiveAction(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsImprovementOpportunity(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsSecurityEvent(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsRecordMixinOrSubtype::IsmsSecurityIncident(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRecordMixinOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRecordMixinOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRecordMixinOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRecordMixinOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRecordMixinOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = IsmsManagementSystem::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementSystem(x));
        }
        if let Ok(x) = IsmsOrganization::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOrganization(x));
        }
        if let Ok(x) = IsmsInterestedParty::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsInterestedParty(x));
        }
        if let Ok(x) = IsmsPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsPolicy(x));
        }
        if let Ok(x) = IsmsTopicSpecificPolicy::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsTopicSpecificPolicy(x));
        }
        if let Ok(x) = IsmsRole::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRole(x));
        }
        if let Ok(x) = IsmsObjective::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsObjective(x));
        }
        if let Ok(x) = IsmsRiskAssessmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessmentProcess(x));
        }
        if let Ok(x) = IsmsRiskAssessment::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessment(x));
        }
        if let Ok(x) = IsmsRisk::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRisk(x));
        }
        if let Ok(x) = IsmsRiskTreatmentProcess::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentProcess(x));
        }
        if let Ok(x) = IsmsRiskTreatmentPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentPlan(x));
        }
        if let Ok(x) = IsmsStatementOfApplicability::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsStatementOfApplicability(x));
        }
        if let Ok(x) = IsmsControl::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsControl(x));
        }
        if let Ok(x) = IsmsAsset::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAsset(x));
        }
        if let Ok(x) = IsmsResource::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsResource(x));
        }
        if let Ok(x) = IsmsCompetenceRecord::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCompetenceRecord(x));
        }
        if let Ok(x) = IsmsAwarenessProgramme::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAwarenessProgramme(x));
        }
        if let Ok(x) = IsmsCommunicationPlan::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCommunicationPlan(x));
        }
        if let Ok(x) = IsmsDocumentedInformation::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsDocumentedInformation(x));
        }
        if let Ok(x) = IsmsOperationalProcedure::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOperationalProcedure(x));
        }
        if let Ok(x) = IsmsMonitoringProgramme::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsMonitoringProgramme(x));
        }
        if let Ok(x) = IsmsAuditProgramme::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditProgramme(x));
        }
        if let Ok(x) = IsmsAudit::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAudit(x));
        }
        if let Ok(x) = IsmsAuditFinding::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditFinding(x));
        }
        if let Ok(x) = IsmsManagementReview::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementReview(x));
        }
        if let Ok(x) = IsmsNonconformity::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsNonconformity(x));
        }
        if let Ok(x) = IsmsCorrectiveAction::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCorrectiveAction(x));
        }
        if let Ok(x) = IsmsImprovementOpportunity::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsImprovementOpportunity(x));
        }
        if let Ok(x) = IsmsSecurityEvent::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityEvent(x));
        }
        if let Ok(x) = IsmsSecurityIncident::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityIncident(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = IsmsManagementSystem::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementSystem(x));
        }
        if let Ok(x) = IsmsOrganization::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOrganization(x));
        }
        if let Ok(x) = IsmsInterestedParty::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsInterestedParty(x));
        }
        if let Ok(x) = IsmsPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsPolicy(x));
        }
        if let Ok(x) = IsmsTopicSpecificPolicy::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsTopicSpecificPolicy(x));
        }
        if let Ok(x) = IsmsRole::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRole(x));
        }
        if let Ok(x) = IsmsObjective::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsObjective(x));
        }
        if let Ok(x) = IsmsRiskAssessmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessmentProcess(x));
        }
        if let Ok(x) = IsmsRiskAssessment::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskAssessment(x));
        }
        if let Ok(x) = IsmsRisk::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRisk(x));
        }
        if let Ok(x) = IsmsRiskTreatmentProcess::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentProcess(x));
        }
        if let Ok(x) = IsmsRiskTreatmentPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsRiskTreatmentPlan(x));
        }
        if let Ok(x) = IsmsStatementOfApplicability::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsStatementOfApplicability(x));
        }
        if let Ok(x) = IsmsControl::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsControl(x));
        }
        if let Ok(x) = IsmsAsset::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAsset(x));
        }
        if let Ok(x) = IsmsResource::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsResource(x));
        }
        if let Ok(x) = IsmsCompetenceRecord::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCompetenceRecord(x));
        }
        if let Ok(x) = IsmsAwarenessProgramme::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAwarenessProgramme(x));
        }
        if let Ok(x) = IsmsCommunicationPlan::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCommunicationPlan(x));
        }
        if let Ok(x) = IsmsDocumentedInformation::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsDocumentedInformation(x));
        }
        if let Ok(x) = IsmsOperationalProcedure::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsOperationalProcedure(x));
        }
        if let Ok(x) = IsmsMonitoringProgramme::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsMonitoringProgramme(x));
        }
        if let Ok(x) = IsmsAuditProgramme::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditProgramme(x));
        }
        if let Ok(x) = IsmsAudit::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAudit(x));
        }
        if let Ok(x) = IsmsAuditFinding::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsAuditFinding(x));
        }
        if let Ok(x) = IsmsManagementReview::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsManagementReview(x));
        }
        if let Ok(x) = IsmsNonconformity::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsNonconformity(x));
        }
        if let Ok(x) = IsmsCorrectiveAction::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsCorrectiveAction(x));
        }
        if let Ok(x) = IsmsImprovementOpportunity::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsImprovementOpportunity(x));
        }
        if let Ok(x) = IsmsSecurityEvent::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityEvent(x));
        }
        if let Ok(x) = IsmsSecurityIncident::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsRecordMixinOrSubtype::IsmsSecurityIncident(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            IsmsRecordMixinOrSubtype::IsmsManagementSystem(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsOrganization(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsInterestedParty(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsPolicy(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsTopicSpecificPolicy(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRole(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsObjective(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRiskAssessmentProcess(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRiskAssessment(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRisk(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRiskTreatmentProcess(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsRiskTreatmentPlan(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsStatementOfApplicability(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsControl(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsAsset(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsResource(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsCompetenceRecord(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsAwarenessProgramme(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsCommunicationPlan(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsDocumentedInformation(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsOperationalProcedure(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsMonitoringProgramme(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsAuditProgramme(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsAudit(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsAuditFinding(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsManagementReview(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsNonconformity(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsCorrectiveAction(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsImprovementOpportunity(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsSecurityEvent(inner) => inner.extract_key(),
            IsmsRecordMixinOrSubtype::IsmsSecurityIncident(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(IsmsRecordMixinOrSubtype = IsmsManagementSystem | IsmsOrganization | IsmsInterestedParty | IsmsPolicy | IsmsTopicSpecificPolicy | IsmsRole | IsmsObjective | IsmsRiskAssessmentProcess | IsmsRiskAssessment | IsmsRisk | IsmsRiskTreatmentProcess | IsmsRiskTreatmentPlan | IsmsStatementOfApplicability | IsmsControl | IsmsAsset | IsmsResource | IsmsCompetenceRecord | IsmsAwarenessProgramme | IsmsCommunicationPlan | IsmsDocumentedInformation | IsmsOperationalProcedure | IsmsMonitoringProgramme | IsmsAuditProgramme | IsmsAudit | IsmsAuditFinding | IsmsManagementReview | IsmsNonconformity | IsmsCorrectiveAction | IsmsImprovementOpportunity | IsmsSecurityEvent | IsmsSecurityIncident);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsDocumentControlMixin {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsDocumentControlMixin {
    #[new]
    #[pyo3(signature = (document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsDocumentControlMixin{document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsDocumentControlMixin>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsDocumentControlMixin> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsDocumentControlMixin>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsDocumentControlMixin",
        ))
    }
}


#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum IsmsDocumentControlMixinOrSubtype {    IsmsPolicy(IsmsPolicy),     IsmsTopicSpecificPolicy(IsmsTopicSpecificPolicy),     IsmsRiskAssessmentProcess(IsmsRiskAssessmentProcess),     IsmsRiskAssessment(IsmsRiskAssessment),     IsmsRiskTreatmentProcess(IsmsRiskTreatmentProcess),     IsmsRiskTreatmentPlan(IsmsRiskTreatmentPlan),     IsmsStatementOfApplicability(IsmsStatementOfApplicability),     IsmsCompetenceRecord(IsmsCompetenceRecord),     IsmsAwarenessProgramme(IsmsAwarenessProgramme),     IsmsCommunicationPlan(IsmsCommunicationPlan),     IsmsDocumentedInformation(IsmsDocumentedInformation),     IsmsOperationalProcedure(IsmsOperationalProcedure),     IsmsMonitoringProgramme(IsmsMonitoringProgramme),     IsmsAuditProgramme(IsmsAuditProgramme),     IsmsAudit(IsmsAudit),     IsmsManagementReview(IsmsManagementReview)}

impl From<IsmsPolicy>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsPolicy)   -> Self { Self::IsmsPolicy(x) } }
impl From<IsmsTopicSpecificPolicy>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsTopicSpecificPolicy)   -> Self { Self::IsmsTopicSpecificPolicy(x) } }
impl From<IsmsRiskAssessmentProcess>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsRiskAssessmentProcess)   -> Self { Self::IsmsRiskAssessmentProcess(x) } }
impl From<IsmsRiskAssessment>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsRiskAssessment)   -> Self { Self::IsmsRiskAssessment(x) } }
impl From<IsmsRiskTreatmentProcess>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsRiskTreatmentProcess)   -> Self { Self::IsmsRiskTreatmentProcess(x) } }
impl From<IsmsRiskTreatmentPlan>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsRiskTreatmentPlan)   -> Self { Self::IsmsRiskTreatmentPlan(x) } }
impl From<IsmsStatementOfApplicability>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsStatementOfApplicability)   -> Self { Self::IsmsStatementOfApplicability(x) } }
impl From<IsmsCompetenceRecord>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsCompetenceRecord)   -> Self { Self::IsmsCompetenceRecord(x) } }
impl From<IsmsAwarenessProgramme>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsAwarenessProgramme)   -> Self { Self::IsmsAwarenessProgramme(x) } }
impl From<IsmsCommunicationPlan>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsCommunicationPlan)   -> Self { Self::IsmsCommunicationPlan(x) } }
impl From<IsmsDocumentedInformation>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsDocumentedInformation)   -> Self { Self::IsmsDocumentedInformation(x) } }
impl From<IsmsOperationalProcedure>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsOperationalProcedure)   -> Self { Self::IsmsOperationalProcedure(x) } }
impl From<IsmsMonitoringProgramme>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsMonitoringProgramme)   -> Self { Self::IsmsMonitoringProgramme(x) } }
impl From<IsmsAuditProgramme>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsAuditProgramme)   -> Self { Self::IsmsAuditProgramme(x) } }
impl From<IsmsAudit>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsAudit)   -> Self { Self::IsmsAudit(x) } }
impl From<IsmsManagementReview>   for IsmsDocumentControlMixinOrSubtype { fn from(x: IsmsManagementReview)   -> Self { Self::IsmsManagementReview(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsDocumentControlMixinOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsPolicy>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val));
        }        if let Ok(val) = ob.extract::<IsmsTopicSpecificPolicy>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskAssessmentProcess>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskAssessment>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskTreatmentProcess>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val));
        }        if let Ok(val) = ob.extract::<IsmsRiskTreatmentPlan>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val));
        }        if let Ok(val) = ob.extract::<IsmsStatementOfApplicability>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val));
        }        if let Ok(val) = ob.extract::<IsmsCompetenceRecord>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val));
        }        if let Ok(val) = ob.extract::<IsmsAwarenessProgramme>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsCommunicationPlan>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val));
        }        if let Ok(val) = ob.extract::<IsmsDocumentedInformation>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val));
        }        if let Ok(val) = ob.extract::<IsmsOperationalProcedure>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val));
        }        if let Ok(val) = ob.extract::<IsmsMonitoringProgramme>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsAuditProgramme>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val));
        }        if let Ok(val) = ob.extract::<IsmsAudit>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsAudit(val));
        }        if let Ok(val) = ob.extract::<IsmsManagementReview>() {
            return Ok(IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsDocumentControlMixinOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsDocumentControlMixinOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsDocumentControlMixinOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsDocumentControlMixinOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsDocumentControlMixinOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsDocumentControlMixinOrSubtype",
        ))
    }
}


#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(IsmsDocumentControlMixinOrSubtype = IsmsPolicy | IsmsTopicSpecificPolicy | IsmsRiskAssessmentProcess | IsmsRiskAssessment | IsmsRiskTreatmentProcess | IsmsRiskTreatmentPlan | IsmsStatementOfApplicability | IsmsCompetenceRecord | IsmsAwarenessProgramme | IsmsCommunicationPlan | IsmsDocumentedInformation | IsmsOperationalProcedure | IsmsMonitoringProgramme | IsmsAuditProgramme | IsmsAudit | IsmsManagementReview);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsManagementSystem {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_organization: Option<IsmsOrganization>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_top_management: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_governing_body: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_leadership_evidence: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_scope_boundaries: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_scope_exclusions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_interfaces: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_processes: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_internal_issues: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_external_issues: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risk_and_opportunity_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_planned_changes: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_external_services: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_certification_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_certification_body: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_certification_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_recertification_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_interested_parties: Option<Vec<IsmsInterestedParty>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_policy: Option<IsmsPolicy>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_topic_specific_policies: Option<Vec<IsmsTopicSpecificPolicy>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_roles: Option<Vec<IsmsRole>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_objectives: Option<Vec<IsmsObjective>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risk_assessment_process: Option<IsmsRiskAssessmentProcess>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risk_treatment_process: Option<IsmsRiskTreatmentProcess>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risk_assessments: Option<Vec<IsmsRiskAssessment>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risks: Option<Vec<IsmsRisk>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_risk_treatment_plans: Option<Vec<IsmsRiskTreatmentPlan>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_statement_of_applicability: Option<IsmsStatementOfApplicability>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_controls: Option<Vec<IsmsControl>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_assets: Option<Vec<IsmsAsset>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_resources: Option<Vec<IsmsResource>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_competence_records: Option<Vec<IsmsCompetenceRecord>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_awareness_programme: Option<IsmsAwarenessProgramme>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_communication_plan: Option<IsmsCommunicationPlan>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_documented_information: Option<Vec<IsmsDocumentedInformation>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_operational_procedures: Option<Vec<IsmsOperationalProcedure>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_monitoring_programme: Option<IsmsMonitoringProgramme>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_audit_programmes: Option<Vec<IsmsAuditProgramme>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_audits: Option<Vec<IsmsAudit>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_management_reviews: Option<Vec<IsmsManagementReview>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_nonconformities: Option<Vec<IsmsNonconformity>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_corrective_actions: Option<Vec<IsmsCorrectiveAction>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_improvements: Option<Vec<IsmsImprovementOpportunity>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub isms_security_events: Option<Vec<IsmsSecurityEventOrSubtype>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsManagementSystem {
    #[new]
    #[pyo3(signature = (isms_id, title, isms_organization=None, isms_top_management=None, isms_governing_body=None, isms_leadership_evidence=None, isms_scope=None, isms_scope_boundaries=None, isms_scope_exclusions=None, isms_interfaces=None, isms_processes=None, isms_internal_issues=None, isms_external_issues=None, isms_risk_and_opportunity_actions=None, isms_planned_changes=None, isms_external_services=None, isms_certification_status=None, isms_certification_body=None, isms_certification_date=None, isms_recertification_date=None, isms_interested_parties=None, isms_policy=None, isms_topic_specific_policies=None, isms_roles=None, isms_objectives=None, isms_risk_assessment_process=None, isms_risk_treatment_process=None, isms_risk_assessments=None, isms_risks=None, isms_risk_treatment_plans=None, isms_statement_of_applicability=None, isms_controls=None, isms_assets=None, isms_resources=None, isms_competence_records=None, isms_awareness_programme=None, isms_communication_plan=None, isms_documented_information=None, isms_operational_procedures=None, isms_monitoring_programme=None, isms_audit_programmes=None, isms_audits=None, isms_management_reviews=None, isms_nonconformities=None, isms_corrective_actions=None, isms_improvements=None, isms_security_events=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, isms_organization: Option<serde_utils::PyValue<IsmsOrganization>>, isms_top_management: Option<String>, isms_governing_body: Option<String>, isms_leadership_evidence: Option<Vec<String>>, isms_scope: Option<String>, isms_scope_boundaries: Option<Vec<String>>, isms_scope_exclusions: Option<Vec<String>>, isms_interfaces: Option<Vec<String>>, isms_processes: Option<String>, isms_internal_issues: Option<Vec<String>>, isms_external_issues: Option<Vec<String>>, isms_risk_and_opportunity_actions: Option<Vec<String>>, isms_planned_changes: Option<Vec<String>>, isms_external_services: Option<Vec<String>>, isms_certification_status: Option<String>, isms_certification_body: Option<String>, isms_certification_date: Option<NaiveDate>, isms_recertification_date: Option<NaiveDate>, isms_interested_parties: Option<serde_utils::PyValue<Vec<IsmsInterestedParty>>>, isms_policy: Option<serde_utils::PyValue<IsmsPolicy>>, isms_topic_specific_policies: Option<serde_utils::PyValue<Vec<IsmsTopicSpecificPolicy>>>, isms_roles: Option<serde_utils::PyValue<Vec<IsmsRole>>>, isms_objectives: Option<serde_utils::PyValue<Vec<IsmsObjective>>>, isms_risk_assessment_process: Option<serde_utils::PyValue<IsmsRiskAssessmentProcess>>, isms_risk_treatment_process: Option<serde_utils::PyValue<IsmsRiskTreatmentProcess>>, isms_risk_assessments: Option<serde_utils::PyValue<Vec<IsmsRiskAssessment>>>, isms_risks: Option<serde_utils::PyValue<Vec<IsmsRisk>>>, isms_risk_treatment_plans: Option<serde_utils::PyValue<Vec<IsmsRiskTreatmentPlan>>>, isms_statement_of_applicability: Option<serde_utils::PyValue<IsmsStatementOfApplicability>>, isms_controls: Option<serde_utils::PyValue<Vec<IsmsControl>>>, isms_assets: Option<serde_utils::PyValue<Vec<IsmsAsset>>>, isms_resources: Option<serde_utils::PyValue<Vec<IsmsResource>>>, isms_competence_records: Option<serde_utils::PyValue<Vec<IsmsCompetenceRecord>>>, isms_awareness_programme: Option<serde_utils::PyValue<IsmsAwarenessProgramme>>, isms_communication_plan: Option<serde_utils::PyValue<IsmsCommunicationPlan>>, isms_documented_information: Option<serde_utils::PyValue<Vec<IsmsDocumentedInformation>>>, isms_operational_procedures: Option<serde_utils::PyValue<Vec<IsmsOperationalProcedure>>>, isms_monitoring_programme: Option<serde_utils::PyValue<IsmsMonitoringProgramme>>, isms_audit_programmes: Option<serde_utils::PyValue<Vec<IsmsAuditProgramme>>>, isms_audits: Option<serde_utils::PyValue<Vec<IsmsAudit>>>, isms_management_reviews: Option<serde_utils::PyValue<Vec<IsmsManagementReview>>>, isms_nonconformities: Option<serde_utils::PyValue<Vec<IsmsNonconformity>>>, isms_corrective_actions: Option<serde_utils::PyValue<Vec<IsmsCorrectiveAction>>>, isms_improvements: Option<serde_utils::PyValue<Vec<IsmsImprovementOpportunity>>>, isms_security_events: Option<serde_utils::PyValue<Vec<IsmsSecurityEventOrSubtype>>>, description: Option<String>) -> Self {
        let isms_organization = isms_organization.map(|v| v.into_inner());
        let isms_interested_parties = isms_interested_parties.map(|v| v.into_inner());
        let isms_policy = isms_policy.map(|v| v.into_inner());
        let isms_topic_specific_policies = isms_topic_specific_policies.map(|v| v.into_inner());
        let isms_roles = isms_roles.map(|v| v.into_inner());
        let isms_objectives = isms_objectives.map(|v| v.into_inner());
        let isms_risk_assessment_process = isms_risk_assessment_process.map(|v| v.into_inner());
        let isms_risk_treatment_process = isms_risk_treatment_process.map(|v| v.into_inner());
        let isms_risk_assessments = isms_risk_assessments.map(|v| v.into_inner());
        let isms_risks = isms_risks.map(|v| v.into_inner());
        let isms_risk_treatment_plans = isms_risk_treatment_plans.map(|v| v.into_inner());
        let isms_statement_of_applicability = isms_statement_of_applicability.map(|v| v.into_inner());
        let isms_controls = isms_controls.map(|v| v.into_inner());
        let isms_assets = isms_assets.map(|v| v.into_inner());
        let isms_resources = isms_resources.map(|v| v.into_inner());
        let isms_competence_records = isms_competence_records.map(|v| v.into_inner());
        let isms_awareness_programme = isms_awareness_programme.map(|v| v.into_inner());
        let isms_communication_plan = isms_communication_plan.map(|v| v.into_inner());
        let isms_documented_information = isms_documented_information.map(|v| v.into_inner());
        let isms_operational_procedures = isms_operational_procedures.map(|v| v.into_inner());
        let isms_monitoring_programme = isms_monitoring_programme.map(|v| v.into_inner());
        let isms_audit_programmes = isms_audit_programmes.map(|v| v.into_inner());
        let isms_audits = isms_audits.map(|v| v.into_inner());
        let isms_management_reviews = isms_management_reviews.map(|v| v.into_inner());
        let isms_nonconformities = isms_nonconformities.map(|v| v.into_inner());
        let isms_corrective_actions = isms_corrective_actions.map(|v| v.into_inner());
        let isms_improvements = isms_improvements.map(|v| v.into_inner());
        let isms_security_events = isms_security_events.map(|v| v.into_inner());
        IsmsManagementSystem{isms_id, title, isms_organization, isms_top_management, isms_governing_body, isms_leadership_evidence, isms_scope, isms_scope_boundaries, isms_scope_exclusions, isms_interfaces, isms_processes, isms_internal_issues, isms_external_issues, isms_risk_and_opportunity_actions, isms_planned_changes, isms_external_services, isms_certification_status, isms_certification_body, isms_certification_date, isms_recertification_date, isms_interested_parties, isms_policy, isms_topic_specific_policies, isms_roles, isms_objectives, isms_risk_assessment_process, isms_risk_treatment_process, isms_risk_assessments, isms_risks, isms_risk_treatment_plans, isms_statement_of_applicability, isms_controls, isms_assets, isms_resources, isms_competence_records, isms_awareness_programme, isms_communication_plan, isms_documented_information, isms_operational_procedures, isms_monitoring_programme, isms_audit_programmes, isms_audits, isms_management_reviews, isms_nonconformities, isms_corrective_actions, isms_improvements, isms_security_events, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsManagementSystem>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsManagementSystem> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsManagementSystem>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsManagementSystem",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsManagementSystem {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsOrganization {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_legal_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_trading_names: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_kind: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_sector: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_size: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_employee_count: Option<isize>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_locations: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_jurisdictions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_parent: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_subsidiaries: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub organization_climate_change_relevant: Option<bool>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsOrganization {
    #[new]
    #[pyo3(signature = (isms_id, title, organization_legal_name=None, organization_trading_names=None, organization_kind=None, organization_sector=None, organization_size=None, organization_employee_count=None, organization_locations=None, organization_jurisdictions=None, organization_parent=None, organization_subsidiaries=None, organization_climate_change_relevant=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, organization_legal_name: Option<String>, organization_trading_names: Option<Vec<String>>, organization_kind: Option<String>, organization_sector: Option<String>, organization_size: Option<String>, organization_employee_count: Option<isize>, organization_locations: Option<Vec<String>>, organization_jurisdictions: Option<Vec<String>>, organization_parent: Option<String>, organization_subsidiaries: Option<Vec<String>>, organization_climate_change_relevant: Option<bool>, description: Option<String>) -> Self {
        IsmsOrganization{isms_id, title, organization_legal_name, organization_trading_names, organization_kind, organization_sector, organization_size, organization_employee_count, organization_locations, organization_jurisdictions, organization_parent, organization_subsidiaries, organization_climate_change_relevant, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsOrganization>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsOrganization> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsOrganization>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsOrganization",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsOrganization {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsInterestedParty {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_category: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_relationship: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_addressed_requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_climate_change_requirements: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_communication_needs: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub party_contact: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsInterestedParty {
    #[new]
    #[pyo3(signature = (isms_id, title, party_category=None, party_relationship=None, party_requirements=None, party_addressed_requirements=None, party_climate_change_requirements=None, party_communication_needs=None, party_contact=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, party_category: Option<String>, party_relationship: Option<String>, party_requirements: Option<Vec<String>>, party_addressed_requirements: Option<Vec<String>>, party_climate_change_requirements: Option<Vec<String>>, party_communication_needs: Option<String>, party_contact: Option<String>, description: Option<String>) -> Self {
        IsmsInterestedParty{isms_id, title, party_category, party_relationship, party_requirements, party_addressed_requirements, party_climate_change_requirements, party_communication_needs, party_contact, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsInterestedParty>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsInterestedParty> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsInterestedParty>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsInterestedParty",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsInterestedParty {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsPolicy {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_objectives_framework: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_commitments: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_applicability: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_communication_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_acknowledgement_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub policy_management_systems: Option<Vec<IsmsManagementSystemStandard>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsPolicy {
    #[new]
    #[pyo3(signature = (isms_id, title, policy_statement=None, policy_objectives_framework=None, policy_commitments=None, policy_applicability=None, policy_communication_date=None, policy_acknowledgement_required=None, policy_management_systems=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, policy_statement: Option<String>, policy_objectives_framework: Option<String>, policy_commitments: Option<Vec<String>>, policy_applicability: Option<String>, policy_communication_date: Option<NaiveDate>, policy_acknowledgement_required: Option<bool>, policy_management_systems: Option<Vec<IsmsManagementSystemStandard>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsPolicy{isms_id, title, policy_statement, policy_objectives_framework, policy_commitments, policy_applicability, policy_communication_date, policy_acknowledgement_required, policy_management_systems, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsPolicy>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsPolicy> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsPolicy>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsPolicy",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsPolicy {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsTopicSpecificPolicy {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub relevant_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub topic_policy_topic: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub topic_policy_parent: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub topic_policy_audience: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsTopicSpecificPolicy {
    #[new]
    #[pyo3(signature = (isms_id, title, relevant_controls=None, topic_policy_topic=None, topic_policy_parent=None, topic_policy_audience=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, relevant_controls: Option<Vec<String>>, topic_policy_topic: Option<String>, topic_policy_parent: Option<String>, topic_policy_audience: Option<String>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsTopicSpecificPolicy{isms_id, title, relevant_controls, topic_policy_topic, topic_policy_parent, topic_policy_audience, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsTopicSpecificPolicy>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsTopicSpecificPolicy> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsTopicSpecificPolicy>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsTopicSpecificPolicy",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsTopicSpecificPolicy {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRole {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_category: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_responsibilities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_authorities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_accountability: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_holders: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_delegation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub role_reports_to: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRole {
    #[new]
    #[pyo3(signature = (isms_id, title, role_category=None, role_responsibilities=None, role_authorities=None, role_accountability=None, role_holders=None, role_delegation=None, role_reports_to=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, role_category: Option<String>, role_responsibilities: Option<Vec<String>>, role_authorities: Option<Vec<String>>, role_accountability: Option<String>, role_holders: Option<Vec<String>>, role_delegation: Option<String>, role_reports_to: Option<String>, description: Option<String>) -> Self {
        IsmsRole{isms_id, title, role_category, role_responsibilities, role_authorities, role_accountability, role_holders, role_delegation, role_reports_to, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRole>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRole> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRole>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRole",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRole {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsObjective {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub relevant_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_statement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_target: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_current_value: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_metric: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_measurement_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_measurement_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_achievement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_risks: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_action_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub objective_resources: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsObjective {
    #[new]
    #[pyo3(signature = (isms_id, title, responsible_role=None, relevant_controls=None, objective_statement=None, objective_target=None, objective_current_value=None, objective_metric=None, objective_measurement_method=None, objective_measurement_frequency=None, objective_target_date=None, objective_achievement=None, objective_risks=None, objective_action_plan=None, objective_resources=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, responsible_role: Option<String>, relevant_controls: Option<Vec<String>>, objective_statement: Option<String>, objective_target: Option<String>, objective_current_value: Option<String>, objective_metric: Option<String>, objective_measurement_method: Option<String>, objective_measurement_frequency: Option<String>, objective_target_date: Option<NaiveDate>, objective_achievement: Option<String>, objective_risks: Option<Vec<String>>, objective_action_plan: Option<String>, objective_resources: Option<String>, description: Option<String>) -> Self {
        IsmsObjective{isms_id, title, responsible_role, relevant_controls, objective_statement, objective_target, objective_current_value, objective_metric, objective_measurement_method, objective_measurement_frequency, objective_target_date, objective_achievement, objective_risks, objective_action_plan, objective_resources, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsObjective>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsObjective> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsObjective>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsObjective",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsObjective {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRiskAssessmentProcess {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_acceptance_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_assessment_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_assessment_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_likelihood_scale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_impact_scale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_matrix: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_assessment_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_assessment_triggers: Option<Vec<String>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRiskAssessmentProcess {
    #[new]
    #[pyo3(signature = (isms_id, title, risk_acceptance_criteria=None, risk_assessment_criteria=None, risk_assessment_method=None, risk_likelihood_scale=None, risk_impact_scale=None, risk_matrix=None, risk_assessment_frequency=None, risk_assessment_triggers=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, risk_acceptance_criteria: Option<String>, risk_assessment_criteria: Option<String>, risk_assessment_method: Option<String>, risk_likelihood_scale: Option<String>, risk_impact_scale: Option<String>, risk_matrix: Option<String>, risk_assessment_frequency: Option<String>, risk_assessment_triggers: Option<Vec<String>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsRiskAssessmentProcess{isms_id, title, risk_acceptance_criteria, risk_assessment_criteria, risk_assessment_method, risk_likelihood_scale, risk_impact_scale, risk_matrix, risk_assessment_frequency, risk_assessment_triggers, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRiskAssessmentProcess>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRiskAssessmentProcess> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRiskAssessmentProcess>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRiskAssessmentProcess",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRiskAssessmentProcess {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRiskAssessment {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_assessor: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_method_used: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_risks: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_summary: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_recommendations: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub assessment_next_date: Option<NaiveDate>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRiskAssessment {
    #[new]
    #[pyo3(signature = (isms_id, title, assessment_scope=None, assessment_date=None, assessment_assessor=None, assessment_method_used=None, assessment_risks=None, assessment_summary=None, assessment_recommendations=None, assessment_next_date=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, assessment_scope: Option<String>, assessment_date: Option<NaiveDate>, assessment_assessor: Option<String>, assessment_method_used: Option<String>, assessment_risks: Option<Vec<String>>, assessment_summary: Option<String>, assessment_recommendations: Option<Vec<String>>, assessment_next_date: Option<NaiveDate>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsRiskAssessment{isms_id, title, assessment_scope, assessment_date, assessment_assessor, assessment_method_used, assessment_risks, assessment_summary, assessment_recommendations, assessment_next_date, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRiskAssessment>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRiskAssessment> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRiskAssessment>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRiskAssessment",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRiskAssessment {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRisk {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub affected_security_properties: Option<Vec<IsmsSecurityProperty>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_threat: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_vulnerability: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_likelihood: Option<IsmsLikelihood>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_impact: Option<IsmsImpact>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_inherent_level: Option<IsmsRiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_existing_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_residual_level: Option<IsmsRiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_treatment_option: Option<IsmsRiskTreatmentOption>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub risk_treatment_priority: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRisk {
    #[new]
    #[pyo3(signature = (isms_id, title, affected_assets=None, affected_security_properties=None, risk_source=None, risk_threat=None, risk_vulnerability=None, risk_owner=None, risk_likelihood=None, risk_impact=None, risk_inherent_level=None, risk_existing_controls=None, risk_residual_level=None, risk_treatment_option=None, risk_treatment_priority=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, affected_assets: Option<Vec<String>>, affected_security_properties: Option<Vec<IsmsSecurityProperty>>, risk_source: Option<String>, risk_threat: Option<String>, risk_vulnerability: Option<String>, risk_owner: Option<String>, risk_likelihood: Option<IsmsLikelihood>, risk_impact: Option<IsmsImpact>, risk_inherent_level: Option<IsmsRiskLevel>, risk_existing_controls: Option<Vec<String>>, risk_residual_level: Option<IsmsRiskLevel>, risk_treatment_option: Option<IsmsRiskTreatmentOption>, risk_treatment_priority: Option<String>, description: Option<String>) -> Self {
        IsmsRisk{isms_id, title, affected_assets, affected_security_properties, risk_source, risk_threat, risk_vulnerability, risk_owner, risk_likelihood, risk_impact, risk_inherent_level, risk_existing_controls, risk_residual_level, risk_treatment_option, risk_treatment_priority, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRisk>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRisk> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRisk>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRisk",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRisk {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRiskTreatmentProcess {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub treatment_options_guidance: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub treatment_control_selection: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub treatment_annex_a_comparison: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub treatment_soa_template: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub treatment_approval_workflow: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRiskTreatmentProcess {
    #[new]
    #[pyo3(signature = (isms_id, title, treatment_options_guidance=None, treatment_control_selection=None, treatment_annex_a_comparison=None, treatment_soa_template=None, treatment_approval_workflow=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, treatment_options_guidance: Option<String>, treatment_control_selection: Option<String>, treatment_annex_a_comparison: Option<String>, treatment_soa_template: Option<String>, treatment_approval_workflow: Option<String>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsRiskTreatmentProcess{isms_id, title, treatment_options_guidance, treatment_control_selection, treatment_annex_a_comparison, treatment_soa_template, treatment_approval_workflow, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRiskTreatmentProcess>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRiskTreatmentProcess> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRiskTreatmentProcess>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRiskTreatmentProcess",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRiskTreatmentProcess {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsRiskTreatmentPlan {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub implementation_state: Option<IsmsImplementationStatus>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_risks: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_resources: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_responsible_parties: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_timeline: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_risk_owner_approval: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_residual_risk_acceptance: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub plan_completion_date: Option<NaiveDate>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsRiskTreatmentPlan {
    #[new]
    #[pyo3(signature = (isms_id, title, implementation_state=None, plan_scope=None, plan_risks=None, plan_actions=None, plan_controls=None, plan_resources=None, plan_responsible_parties=None, plan_timeline=None, plan_risk_owner_approval=None, plan_residual_risk_acceptance=None, plan_completion_date=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, implementation_state: Option<IsmsImplementationStatus>, plan_scope: Option<String>, plan_risks: Option<Vec<String>>, plan_actions: Option<Vec<String>>, plan_controls: Option<Vec<String>>, plan_resources: Option<String>, plan_responsible_parties: Option<Vec<String>>, plan_timeline: Option<String>, plan_risk_owner_approval: Option<String>, plan_residual_risk_acceptance: Option<String>, plan_completion_date: Option<NaiveDate>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsRiskTreatmentPlan{isms_id, title, implementation_state, plan_scope, plan_risks, plan_actions, plan_controls, plan_resources, plan_responsible_parties, plan_timeline, plan_risk_owner_approval, plan_residual_risk_acceptance, plan_completion_date, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsRiskTreatmentPlan>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsRiskTreatmentPlan> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsRiskTreatmentPlan>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsRiskTreatmentPlan",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsRiskTreatmentPlan {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsStatementOfApplicability {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub soa_entries: Option<Vec<IsmsApplicabilityEntryOrSubtype>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsStatementOfApplicability {
    #[new]
    #[pyo3(signature = (isms_id, title, soa_entries=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, soa_entries: Option<serde_utils::PyValue<Vec<IsmsApplicabilityEntryOrSubtype>>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        let soa_entries = soa_entries.map(|v| v.into_inner());
        IsmsStatementOfApplicability{isms_id, title, soa_entries, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsStatementOfApplicability>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsStatementOfApplicability> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsStatementOfApplicability>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsStatementOfApplicability",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsStatementOfApplicability {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsApplicabilityEntry {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub entry_annex_a_control: Option<IsmsAnnexAControl>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub entry_type: Option<String>,
    pub entry_justification: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsApplicabilityEntry {
    #[new]
    #[pyo3(signature = (entry_justification, entry_annex_a_control=None, entry_type=None))]
    pub fn new(entry_justification: String, entry_annex_a_control: Option<IsmsAnnexAControl>, entry_type: Option<String>) -> Self {
        IsmsApplicabilityEntry{entry_justification, entry_annex_a_control, entry_type}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsApplicabilityEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsApplicabilityEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsApplicabilityEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsApplicabilityEntry",
        ))
    }
}


#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(tag = "entry_type"))]
pub enum IsmsApplicabilityEntryOrSubtype {    #[serde(rename = "IsmsIncludedControl",   )]
    IsmsIncludedControl(IsmsIncludedControl),     #[serde(rename = "IsmsExcludedControl",   )]
    IsmsExcludedControl(IsmsExcludedControl)}

impl From<IsmsIncludedControl>   for IsmsApplicabilityEntryOrSubtype { fn from(x: IsmsIncludedControl)   -> Self { Self::IsmsIncludedControl(x) } }
impl From<IsmsExcludedControl>   for IsmsApplicabilityEntryOrSubtype { fn from(x: IsmsExcludedControl)   -> Self { Self::IsmsExcludedControl(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsApplicabilityEntryOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsIncludedControl>() {
            return Ok(IsmsApplicabilityEntryOrSubtype::IsmsIncludedControl(val));
        }        if let Ok(val) = ob.extract::<IsmsExcludedControl>() {
            return Ok(IsmsApplicabilityEntryOrSubtype::IsmsExcludedControl(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsApplicabilityEntryOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsApplicabilityEntryOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            IsmsApplicabilityEntryOrSubtype::IsmsIncludedControl(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            IsmsApplicabilityEntryOrSubtype::IsmsExcludedControl(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsApplicabilityEntryOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsApplicabilityEntryOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsApplicabilityEntryOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsApplicabilityEntryOrSubtype",
        ))
    }
}


#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(IsmsApplicabilityEntryOrSubtype = IsmsIncludedControl | IsmsExcludedControl);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsIncludedControl {
    pub implementation_state: IsmsImplementationStatus,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub included_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub included_evidence: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub included_target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub entry_annex_a_control: Option<IsmsAnnexAControl>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub entry_type: Option<String>,
    pub entry_justification: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsIncludedControl {
    #[new]
    #[pyo3(signature = (implementation_state, entry_justification, responsible_role=None, included_control=None, included_evidence=None, included_target_date=None, entry_annex_a_control=None, entry_type=None))]
    pub fn new(implementation_state: IsmsImplementationStatus, entry_justification: String, responsible_role: Option<String>, included_control: Option<String>, included_evidence: Option<String>, included_target_date: Option<NaiveDate>, entry_annex_a_control: Option<IsmsAnnexAControl>, entry_type: Option<String>) -> Self {
        IsmsIncludedControl{implementation_state, entry_justification, responsible_role, included_control, included_evidence, included_target_date, entry_annex_a_control, entry_type}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsIncludedControl>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsIncludedControl> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsIncludedControl>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsIncludedControl",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsExcludedControl {
    pub entry_annex_a_control: IsmsAnnexAControl,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub entry_type: Option<String>,
    pub entry_justification: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsExcludedControl {
    #[new]
    #[pyo3(signature = (entry_annex_a_control, entry_justification, entry_type=None))]
    pub fn new(entry_annex_a_control: IsmsAnnexAControl, entry_justification: String, entry_type: Option<String>) -> Self {
        IsmsExcludedControl{entry_annex_a_control, entry_justification, entry_type}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsExcludedControl>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsExcludedControl> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsExcludedControl>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsExcludedControl",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsControl {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub relevant_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub implementation_state: Option<IsmsImplementationStatus>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_annex_a_controls: Option<Vec<IsmsAnnexAControl>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_theme: Option<IsmsControlTheme>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_text: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_guidance: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_threats: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_asset_types: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_implementation_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_effectiveness: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_last_tested: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub control_evidence: Option<Vec<String>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsControl {
    #[new]
    #[pyo3(signature = (isms_id, title, relevant_controls=None, implementation_state=None, control_annex_a_controls=None, control_theme=None, control_text=None, control_guidance=None, control_threats=None, control_asset_types=None, control_owner=None, control_implementation_date=None, control_effectiveness=None, control_last_tested=None, control_evidence=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, relevant_controls: Option<Vec<String>>, implementation_state: Option<IsmsImplementationStatus>, control_annex_a_controls: Option<Vec<IsmsAnnexAControl>>, control_theme: Option<IsmsControlTheme>, control_text: Option<String>, control_guidance: Option<String>, control_threats: Option<Vec<String>>, control_asset_types: Option<Vec<String>>, control_owner: Option<String>, control_implementation_date: Option<NaiveDate>, control_effectiveness: Option<String>, control_last_tested: Option<NaiveDate>, control_evidence: Option<Vec<String>>, description: Option<String>) -> Self {
        IsmsControl{isms_id, title, relevant_controls, implementation_state, control_annex_a_controls, control_theme, control_text, control_guidance, control_threats, control_asset_types, control_owner, control_implementation_date, control_effectiveness, control_last_tested, control_evidence, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsControl>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsControl> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsControl>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsControl",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsControl {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsAsset {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub relevant_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_category: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_custodian: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_location: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub asset_criticality: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsAsset {
    #[new]
    #[pyo3(signature = (isms_id, title, relevant_controls=None, asset_category=None, asset_owner=None, asset_custodian=None, asset_classification=None, asset_location=None, asset_criticality=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, relevant_controls: Option<Vec<String>>, asset_category: Option<String>, asset_owner: Option<String>, asset_custodian: Option<String>, asset_classification: Option<String>, asset_location: Option<String>, asset_criticality: Option<String>, description: Option<String>) -> Self {
        IsmsAsset{isms_id, title, relevant_controls, asset_category, asset_owner, asset_custodian, asset_classification, asset_location, asset_criticality, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsAsset>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsAsset> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsAsset>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsAsset",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsAsset {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsResource {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_category: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_quantity: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_allocation_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_allocated_to: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_cost: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub resource_availability: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsResource {
    #[new]
    #[pyo3(signature = (isms_id, title, resource_category=None, resource_quantity=None, resource_allocation_date=None, resource_allocated_to=None, resource_cost=None, resource_availability=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, resource_category: Option<String>, resource_quantity: Option<String>, resource_allocation_date: Option<NaiveDate>, resource_allocated_to: Option<String>, resource_cost: Option<String>, resource_availability: Option<String>, description: Option<String>) -> Self {
        IsmsResource{isms_id, title, resource_category, resource_quantity, resource_allocation_date, resource_allocated_to, resource_cost, resource_availability, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsResource>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsResource> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsResource>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsResource",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsResource {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsCompetenceRecord {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_person: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_required: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_education: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_training: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_experience: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_assessment_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_gaps: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub competence_actions: Option<Vec<String>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsCompetenceRecord {
    #[new]
    #[pyo3(signature = (isms_id, title, competence_person=None, competence_role=None, competence_required=None, competence_education=None, competence_training=None, competence_experience=None, competence_assessment_date=None, competence_gaps=None, competence_actions=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, competence_person: Option<String>, competence_role: Option<String>, competence_required: Option<Vec<String>>, competence_education: Option<Vec<String>>, competence_training: Option<Vec<String>>, competence_experience: Option<Vec<String>>, competence_assessment_date: Option<NaiveDate>, competence_gaps: Option<Vec<String>>, competence_actions: Option<Vec<String>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsCompetenceRecord{isms_id, title, competence_person, competence_role, competence_required, competence_education, competence_training, competence_experience, competence_assessment_date, competence_gaps, competence_actions, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsCompetenceRecord>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsCompetenceRecord> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsCompetenceRecord>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsCompetenceRecord",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsCompetenceRecord {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsAwarenessProgramme {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_topics: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_methods: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_audience: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_completion_tracking: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub awareness_effectiveness: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsAwarenessProgramme {
    #[new]
    #[pyo3(signature = (isms_id, title, awareness_topics=None, awareness_methods=None, awareness_audience=None, awareness_frequency=None, awareness_completion_tracking=None, awareness_effectiveness=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, awareness_topics: Option<Vec<String>>, awareness_methods: Option<Vec<String>>, awareness_audience: Option<String>, awareness_frequency: Option<String>, awareness_completion_tracking: Option<String>, awareness_effectiveness: Option<String>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsAwarenessProgramme{isms_id, title, awareness_topics, awareness_methods, awareness_audience, awareness_frequency, awareness_completion_tracking, awareness_effectiveness, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsAwarenessProgramme>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsAwarenessProgramme> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsAwarenessProgramme>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsAwarenessProgramme",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsAwarenessProgramme {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsCommunicationPlan {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_items: Option<Vec<IsmsCommunication>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsCommunicationPlan {
    #[new]
    #[pyo3(signature = (isms_id, title, communication_items=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, communication_items: Option<serde_utils::PyValue<Vec<IsmsCommunication>>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        let communication_items = communication_items.map(|v| v.into_inner());
        IsmsCommunicationPlan{isms_id, title, communication_items, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsCommunicationPlan>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsCommunicationPlan> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsCommunicationPlan>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsCommunicationPlan",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsCommunicationPlan {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsCommunication {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    pub communication_subject: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_purpose: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_audience: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub communication_records_required: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsCommunication {
    #[new]
    #[pyo3(signature = (communication_subject, responsible_role=None, communication_purpose=None, communication_audience=None, communication_frequency=None, communication_method=None, communication_records_required=None))]
    pub fn new(communication_subject: String, responsible_role: Option<String>, communication_purpose: Option<String>, communication_audience: Option<String>, communication_frequency: Option<String>, communication_method: Option<String>, communication_records_required: Option<bool>) -> Self {
        IsmsCommunication{communication_subject, responsible_role, communication_purpose, communication_audience, communication_frequency, communication_method, communication_records_required}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsCommunication>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsCommunication> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsCommunication>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsCommunication",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsDocumentedInformation {
    pub document_kind: IsmsDocumentKind,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsDocumentedInformation {
    #[new]
    #[pyo3(signature = (document_kind, isms_id, title, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(document_kind: IsmsDocumentKind, isms_id: uriorcurie, title: String, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsDocumentedInformation{document_kind, isms_id, title, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsDocumentedInformation>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsDocumentedInformation> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsDocumentedInformation>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsDocumentedInformation",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsDocumentedInformation {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a IsmsDocumentedInformation from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsOperationalProcedure {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub relevant_controls: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub procedure_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub procedure_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub procedure_control_measures: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub procedure_roles: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub procedure_change_control: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsOperationalProcedure {
    #[new]
    #[pyo3(signature = (isms_id, title, relevant_controls=None, procedure_scope=None, procedure_criteria=None, procedure_control_measures=None, procedure_roles=None, procedure_change_control=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, relevant_controls: Option<Vec<String>>, procedure_scope: Option<String>, procedure_criteria: Option<String>, procedure_control_measures: Option<Vec<String>>, procedure_roles: Option<Vec<String>>, procedure_change_control: Option<String>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsOperationalProcedure{isms_id, title, relevant_controls, procedure_scope, procedure_criteria, procedure_control_measures, procedure_roles, procedure_change_control, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsOperationalProcedure>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsOperationalProcedure> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsOperationalProcedure>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsOperationalProcedure",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsOperationalProcedure {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsMonitoringProgramme {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_items: Option<Vec<IsmsMonitoringItem>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsMonitoringProgramme {
    #[new]
    #[pyo3(signature = (isms_id, title, monitoring_items=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, monitoring_items: Option<serde_utils::PyValue<Vec<IsmsMonitoringItem>>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        let monitoring_items = monitoring_items.map(|v| v.into_inner());
        IsmsMonitoringProgramme{isms_id, title, monitoring_items, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsMonitoringProgramme>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsMonitoringProgramme> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsMonitoringProgramme>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsMonitoringProgramme",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsMonitoringProgramme {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsMonitoringItem {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    pub monitoring_metric: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_analysis_frequency: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_analyst: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_target: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_alert_threshold: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_current_value: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub monitoring_trend: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsMonitoringItem {
    #[new]
    #[pyo3(signature = (monitoring_metric, responsible_role=None, monitoring_description=None, monitoring_method=None, monitoring_frequency=None, monitoring_analysis_frequency=None, monitoring_analyst=None, monitoring_target=None, monitoring_alert_threshold=None, monitoring_current_value=None, monitoring_trend=None))]
    pub fn new(monitoring_metric: String, responsible_role: Option<String>, monitoring_description: Option<String>, monitoring_method: Option<String>, monitoring_frequency: Option<String>, monitoring_analysis_frequency: Option<String>, monitoring_analyst: Option<String>, monitoring_target: Option<String>, monitoring_alert_threshold: Option<String>, monitoring_current_value: Option<String>, monitoring_trend: Option<String>) -> Self {
        IsmsMonitoringItem{monitoring_metric, responsible_role, monitoring_description, monitoring_method, monitoring_frequency, monitoring_analysis_frequency, monitoring_analyst, monitoring_target, monitoring_alert_threshold, monitoring_current_value, monitoring_trend}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsMonitoringItem>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsMonitoringItem> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsMonitoringItem>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsMonitoringItem",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsAuditProgramme {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_period: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_audits: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_frequency_rationale: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_resources: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_auditor_qualifications: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub programme_status: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsAuditProgramme {
    #[new]
    #[pyo3(signature = (isms_id, title, programme_period=None, programme_audits=None, programme_frequency_rationale=None, programme_resources=None, programme_auditor_qualifications=None, programme_status=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(isms_id: uriorcurie, title: String, programme_period: Option<String>, programme_audits: Option<Vec<String>>, programme_frequency_rationale: Option<String>, programme_resources: Option<String>, programme_auditor_qualifications: Option<String>, programme_status: Option<String>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsAuditProgramme{isms_id, title, programme_period, programme_audits, programme_frequency_rationale, programme_resources, programme_auditor_qualifications, programme_status, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsAuditProgramme>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsAuditProgramme> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsAuditProgramme>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsAuditProgramme",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsAuditProgramme {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsAudit {
    pub audit_type: IsmsAuditType,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_standards: Option<Vec<IsmsManagementSystemStandard>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_scope: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_criteria: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_objectives: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_period_start: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_period_end: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_lead: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_team: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_auditees: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_findings: Option<Vec<IsmsAuditFinding>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_conclusion: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_report_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub audit_report_distribution: Option<Vec<String>>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsAudit {
    #[new]
    #[pyo3(signature = (audit_type, isms_id, title, audit_standards=None, audit_scope=None, audit_criteria=None, audit_objectives=None, audit_period_start=None, audit_period_end=None, audit_lead=None, audit_team=None, audit_auditees=None, audit_plan=None, audit_findings=None, audit_conclusion=None, audit_report_date=None, audit_report_distribution=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(audit_type: IsmsAuditType, isms_id: uriorcurie, title: String, audit_standards: Option<Vec<IsmsManagementSystemStandard>>, audit_scope: Option<String>, audit_criteria: Option<Vec<String>>, audit_objectives: Option<Vec<String>>, audit_period_start: Option<NaiveDate>, audit_period_end: Option<NaiveDate>, audit_lead: Option<String>, audit_team: Option<Vec<String>>, audit_auditees: Option<Vec<String>>, audit_plan: Option<String>, audit_findings: Option<serde_utils::PyValue<Vec<IsmsAuditFinding>>>, audit_conclusion: Option<String>, audit_report_date: Option<NaiveDate>, audit_report_distribution: Option<Vec<String>>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        let audit_findings = audit_findings.map(|v| v.into_inner());
        IsmsAudit{audit_type, isms_id, title, audit_standards, audit_scope, audit_criteria, audit_objectives, audit_period_start, audit_period_end, audit_lead, audit_team, audit_auditees, audit_plan, audit_findings, audit_conclusion, audit_report_date, audit_report_distribution, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsAudit>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsAudit> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsAudit>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsAudit",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsAudit {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a IsmsAudit from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsAuditFinding {
    pub finding_type: IsmsAuditFindingType,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_requirement: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_evidence: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_risk: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_recommendation: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_auditee_response: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_corrective_action: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_closure_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub finding_closure_date: Option<NaiveDate>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsAuditFinding {
    #[new]
    #[pyo3(signature = (finding_type, isms_id, title, finding_requirement=None, finding_control=None, finding_evidence=None, finding_root_cause=None, finding_risk=None, finding_recommendation=None, finding_auditee_response=None, finding_corrective_action=None, finding_closure_status=None, finding_closure_date=None, description=None))]
    pub fn new(finding_type: IsmsAuditFindingType, isms_id: uriorcurie, title: String, finding_requirement: Option<String>, finding_control: Option<String>, finding_evidence: Option<String>, finding_root_cause: Option<String>, finding_risk: Option<String>, finding_recommendation: Option<String>, finding_auditee_response: Option<String>, finding_corrective_action: Option<String>, finding_closure_status: Option<String>, finding_closure_date: Option<NaiveDate>, description: Option<String>) -> Self {
        IsmsAuditFinding{finding_type, isms_id, title, finding_requirement, finding_control, finding_evidence, finding_root_cause, finding_risk, finding_recommendation, finding_auditee_response, finding_corrective_action, finding_closure_status, finding_closure_date, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsAuditFinding>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsAuditFinding> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsAuditFinding>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsAuditFinding",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsAuditFinding {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a IsmsAuditFinding from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsManagementReview {
    pub review_held_on: NaiveDate,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_attendees: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_previous_actions: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_context_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_interested_party_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_interested_party_feedback: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_performance_trends: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_audit_results: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_risk_assessment_results: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_risk_treatment_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_risks_and_opportunities: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_improvement_opportunities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_decisions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub review_next_date: Option<NaiveDate>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_reference: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_author: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_owner: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approver: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_approval_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_effective_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_last_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_next_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_classification: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_retention: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_distribution: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_storage: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_change_control: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_origin: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub document_external_source: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsManagementReview {
    #[new]
    #[pyo3(signature = (review_held_on, isms_id, title, review_attendees=None, review_previous_actions=None, review_context_changes=None, review_interested_party_changes=None, review_interested_party_feedback=None, review_performance_trends=None, review_audit_results=None, review_risk_assessment_results=None, review_risk_treatment_status=None, review_risks_and_opportunities=None, review_improvement_opportunities=None, review_decisions=None, review_actions=None, review_next_date=None, description=None, document_reference=None, document_version=None, document_author=None, document_owner=None, document_approver=None, document_approval_date=None, document_effective_date=None, document_last_review_date=None, document_next_review_date=None, document_status=None, document_classification=None, document_retention=None, document_distribution=None, document_storage=None, document_change_control=None, document_external_origin=None, document_external_source=None))]
    pub fn new(review_held_on: NaiveDate, isms_id: uriorcurie, title: String, review_attendees: Option<Vec<String>>, review_previous_actions: Option<String>, review_context_changes: Option<String>, review_interested_party_changes: Option<String>, review_interested_party_feedback: Option<String>, review_performance_trends: Option<String>, review_audit_results: Option<String>, review_risk_assessment_results: Option<String>, review_risk_treatment_status: Option<String>, review_risks_and_opportunities: Option<String>, review_improvement_opportunities: Option<Vec<String>>, review_decisions: Option<Vec<String>>, review_actions: Option<Vec<String>>, review_next_date: Option<NaiveDate>, description: Option<String>, document_reference: Option<String>, document_version: Option<String>, document_author: Option<String>, document_owner: Option<String>, document_approver: Option<String>, document_approval_date: Option<NaiveDate>, document_effective_date: Option<NaiveDate>, document_last_review_date: Option<NaiveDate>, document_next_review_date: Option<NaiveDate>, document_status: Option<String>, document_classification: Option<String>, document_retention: Option<String>, document_distribution: Option<Vec<String>>, document_storage: Option<String>, document_change_control: Option<String>, document_external_origin: Option<bool>, document_external_source: Option<String>) -> Self {
        IsmsManagementReview{review_held_on, isms_id, title, review_attendees, review_previous_actions, review_context_changes, review_interested_party_changes, review_interested_party_feedback, review_performance_trends, review_audit_results, review_risk_assessment_results, review_risk_treatment_status, review_risks_and_opportunities, review_improvement_opportunities, review_decisions, review_actions, review_next_date, description, document_reference, document_version, document_author, document_owner, document_approver, document_approval_date, document_effective_date, document_last_review_date, document_next_review_date, document_status, document_classification, document_retention, document_distribution, document_storage, document_change_control, document_external_origin, document_external_source}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsManagementReview>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsManagementReview> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsManagementReview>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsManagementReview",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsManagementReview {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a IsmsManagementReview from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsNonconformity {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_detected_on: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_detected_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_requirement: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_immediate_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_consequences: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_similar_check: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_status: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_closure_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub nonconformity_closure_evidence: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsNonconformity {
    #[new]
    #[pyo3(signature = (isms_id, title, nonconformity_source=None, nonconformity_detected_on=None, nonconformity_detected_by=None, nonconformity_requirement=None, nonconformity_immediate_actions=None, nonconformity_consequences=None, nonconformity_root_cause=None, nonconformity_similar_check=None, nonconformity_status=None, nonconformity_closure_date=None, nonconformity_closure_evidence=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, nonconformity_source: Option<String>, nonconformity_detected_on: Option<NaiveDate>, nonconformity_detected_by: Option<String>, nonconformity_requirement: Option<String>, nonconformity_immediate_actions: Option<Vec<String>>, nonconformity_consequences: Option<String>, nonconformity_root_cause: Option<String>, nonconformity_similar_check: Option<String>, nonconformity_status: Option<String>, nonconformity_closure_date: Option<NaiveDate>, nonconformity_closure_evidence: Option<String>, description: Option<String>) -> Self {
        IsmsNonconformity{isms_id, title, nonconformity_source, nonconformity_detected_on, nonconformity_detected_by, nonconformity_requirement, nonconformity_immediate_actions, nonconformity_consequences, nonconformity_root_cause, nonconformity_similar_check, nonconformity_status, nonconformity_closure_date, nonconformity_closure_evidence, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsNonconformity>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsNonconformity> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsNonconformity>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsNonconformity",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsNonconformity {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsCorrectiveAction {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_nonconformities: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_resources: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_effectiveness_criteria: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_effectiveness_review_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_effective: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_isms_changes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub action_status: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsCorrectiveAction {
    #[new]
    #[pyo3(signature = (isms_id, title, responsible_role=None, action_nonconformities=None, action_root_cause=None, action_target_date=None, action_completion_date=None, action_resources=None, action_effectiveness_criteria=None, action_effectiveness_review_date=None, action_effective=None, action_isms_changes=None, action_status=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, responsible_role: Option<String>, action_nonconformities: Option<Vec<String>>, action_root_cause: Option<String>, action_target_date: Option<NaiveDate>, action_completion_date: Option<NaiveDate>, action_resources: Option<String>, action_effectiveness_criteria: Option<String>, action_effectiveness_review_date: Option<NaiveDate>, action_effective: Option<bool>, action_isms_changes: Option<String>, action_status: Option<String>, description: Option<String>) -> Self {
        IsmsCorrectiveAction{isms_id, title, responsible_role, action_nonconformities, action_root_cause, action_target_date, action_completion_date, action_resources, action_effectiveness_criteria, action_effectiveness_review_date, action_effective, action_isms_changes, action_status, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsCorrectiveAction>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsCorrectiveAction> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsCorrectiveAction>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsCorrectiveAction",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsCorrectiveAction {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsImprovementOpportunity {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub responsible_role: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_source: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_identified_on: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_identified_by: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_benefit: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_priority: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_plan: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_target_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_completion_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_outcome: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub improvement_status: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsImprovementOpportunity {
    #[new]
    #[pyo3(signature = (isms_id, title, responsible_role=None, improvement_source=None, improvement_identified_on=None, improvement_identified_by=None, improvement_benefit=None, improvement_priority=None, improvement_plan=None, improvement_target_date=None, improvement_completion_date=None, improvement_outcome=None, improvement_status=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, responsible_role: Option<String>, improvement_source: Option<String>, improvement_identified_on: Option<NaiveDate>, improvement_identified_by: Option<String>, improvement_benefit: Option<String>, improvement_priority: Option<String>, improvement_plan: Option<String>, improvement_target_date: Option<NaiveDate>, improvement_completion_date: Option<NaiveDate>, improvement_outcome: Option<String>, improvement_status: Option<String>, description: Option<String>) -> Self {
        IsmsImprovementOpportunity{isms_id, title, responsible_role, improvement_source, improvement_identified_on, improvement_identified_by, improvement_benefit, improvement_priority, improvement_plan, improvement_target_date, improvement_completion_date, improvement_outcome, improvement_status, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsImprovementOpportunity>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsImprovementOpportunity> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsImprovementOpportunity>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsImprovementOpportunity",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsImprovementOpportunity {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
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
pub struct IsmsSecurityEvent {
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_occurred_at: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_reporter: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_assessment: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsSecurityEvent {
    #[new]
    #[pyo3(signature = (isms_id, title, affected_assets=None, event_type=None, event_occurred_at=None, event_reporter=None, event_assessment=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, affected_assets: Option<Vec<String>>, event_type: Option<String>, event_occurred_at: Option<NaiveDateTime>, event_reporter: Option<String>, event_assessment: Option<String>, description: Option<String>) -> Self {
        IsmsSecurityEvent{isms_id, title, affected_assets, event_type, event_occurred_at, event_reporter, event_assessment, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsSecurityEvent>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsSecurityEvent> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsSecurityEvent>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsSecurityEvent",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsSecurityEvent {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(tag = "event_type"))]
pub enum IsmsSecurityEventOrSubtype {    #[serde(rename = "IsmsSecurityIncident",   )]
    IsmsSecurityIncident(IsmsSecurityIncident)}

impl From<IsmsSecurityIncident>   for IsmsSecurityEventOrSubtype { fn from(x: IsmsSecurityIncident)   -> Self { Self::IsmsSecurityIncident(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for IsmsSecurityEventOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsSecurityIncident>() {
            return Ok(IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsSecurityEventOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for IsmsSecurityEventOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsSecurityEventOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsSecurityEventOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsSecurityEventOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsSecurityEventOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsSecurityEventOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = IsmsSecurityIncident::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(IsmsSecurityEventOrSubtype::IsmsSecurityIncident(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = IsmsSecurityIncident::from_pair_simple(k.clone(), v.clone()) {
            return Ok(IsmsSecurityEventOrSubtype::IsmsSecurityIncident(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            IsmsSecurityEventOrSubtype::IsmsSecurityIncident(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(IsmsSecurityEventOrSubtype = IsmsSecurityIncident);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IsmsSecurityIncident {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub affected_security_properties: Option<Vec<IsmsSecurityProperty>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_category: Option<IsmsIncidentCategory>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_severity: Option<IsmsRiskLevel>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_detection_method: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_response_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_containment_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_eradication_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_recovery_actions: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_root_cause: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_lessons_learned: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_evidence: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_notification_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_notifications: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_closed_at: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub incident_review: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub affected_assets: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_occurred_at: Option<NaiveDateTime>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_reporter: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub event_assessment: Option<String>,
    pub isms_id: uriorcurie,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(skip_serializing_if = "Option::is_none"))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IsmsSecurityIncident {
    #[new]
    #[pyo3(signature = (isms_id, title, affected_security_properties=None, incident_category=None, incident_severity=None, incident_detection_method=None, incident_response_actions=None, incident_containment_actions=None, incident_eradication_actions=None, incident_recovery_actions=None, incident_root_cause=None, incident_lessons_learned=None, incident_evidence=None, incident_notification_required=None, incident_notifications=None, incident_closed_at=None, incident_review=None, affected_assets=None, event_type=None, event_occurred_at=None, event_reporter=None, event_assessment=None, description=None))]
    pub fn new(isms_id: uriorcurie, title: String, affected_security_properties: Option<Vec<IsmsSecurityProperty>>, incident_category: Option<IsmsIncidentCategory>, incident_severity: Option<IsmsRiskLevel>, incident_detection_method: Option<String>, incident_response_actions: Option<Vec<String>>, incident_containment_actions: Option<Vec<String>>, incident_eradication_actions: Option<Vec<String>>, incident_recovery_actions: Option<Vec<String>>, incident_root_cause: Option<String>, incident_lessons_learned: Option<Vec<String>>, incident_evidence: Option<Vec<String>>, incident_notification_required: Option<bool>, incident_notifications: Option<Vec<String>>, incident_closed_at: Option<NaiveDateTime>, incident_review: Option<String>, affected_assets: Option<Vec<String>>, event_type: Option<String>, event_occurred_at: Option<NaiveDateTime>, event_reporter: Option<String>, event_assessment: Option<String>, description: Option<String>) -> Self {
        IsmsSecurityIncident{isms_id, title, affected_security_properties, incident_category, incident_severity, incident_detection_method, incident_response_actions, incident_containment_actions, incident_eradication_actions, incident_recovery_actions, incident_root_cause, incident_lessons_learned, incident_evidence, incident_notification_required, incident_notifications, incident_closed_at, incident_review, affected_assets, event_type, event_occurred_at, event_reporter, event_assessment, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IsmsSecurityIncident>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IsmsSecurityIncident> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IsmsSecurityIncident>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IsmsSecurityIncident",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IsmsSecurityIncident {
    type Key   = uriorcurie;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.isms_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        // Only inject the inferred key if the inner map does not already carry it
        // under its canonical name or any accepted alias. Injecting unconditionally
        // would produce a duplicate field once serde resolves aliases.
        let already_keyed = map.contains_key(&Value::String("isms_id".into()));
        if !already_keyed {
            map.insert(Value::String("isms_id".into()), key_value);
        }
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("isms_id".into()), key_value);
        map.insert(Value::String("title".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.title)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("isms_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}





#[cfg(feature = "stubgen")]
define_stub_info_gatherer!(stub_info);
