#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait IsmsRecord   {

    fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie;
    // fn isms_id_mut(&mut self) -> &mut &'a crate::uriorcurie;
    // fn set_isms_id(&mut self, value: uriorcurie);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl IsmsRecord for crate::IsmsRecord {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsManagementSystem {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsOrganization {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsInterestedParty {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsPolicy {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsTopicSpecificPolicy {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRole {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsObjective {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRiskAssessmentProcess {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRiskAssessment {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRisk {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRiskTreatmentProcess {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsRiskTreatmentPlan {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsStatementOfApplicability {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsControl {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsAsset {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsResource {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsCompetenceRecord {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsAwarenessProgramme {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsCommunicationPlan {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsDocumentedInformation {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsOperationalProcedure {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsMonitoringProgramme {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsAuditProgramme {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsAudit {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsAuditFinding {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsManagementReview {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsNonconformity {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsCorrectiveAction {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsImprovementOpportunity {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsSecurityEvent {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}
impl IsmsRecord for crate::IsmsSecurityIncident {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.isms_id;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}

impl IsmsRecord for crate::IsmsRecordOrSubtype {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                IsmsRecordOrSubtype::IsmsManagementSystem(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsOrganization(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsInterestedParty(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsPolicy(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsTopicSpecificPolicy(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRole(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsObjective(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRiskAssessmentProcess(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRiskAssessment(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRisk(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentProcess(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentPlan(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsStatementOfApplicability(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsControl(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsAsset(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsResource(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsCompetenceRecord(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsAwarenessProgramme(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsCommunicationPlan(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsDocumentedInformation(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsOperationalProcedure(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsMonitoringProgramme(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsAuditProgramme(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsAudit(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsAuditFinding(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsManagementReview(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsNonconformity(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsCorrectiveAction(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsImprovementOpportunity(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsSecurityEvent(val) => val.isms_id(),
                IsmsRecordOrSubtype::IsmsSecurityIncident(val) => val.isms_id(),

        }
    }
        fn title<'a>(&'a self) -> &'a str {
        match self {
                IsmsRecordOrSubtype::IsmsManagementSystem(val) => val.title(),
                IsmsRecordOrSubtype::IsmsOrganization(val) => val.title(),
                IsmsRecordOrSubtype::IsmsInterestedParty(val) => val.title(),
                IsmsRecordOrSubtype::IsmsPolicy(val) => val.title(),
                IsmsRecordOrSubtype::IsmsTopicSpecificPolicy(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRole(val) => val.title(),
                IsmsRecordOrSubtype::IsmsObjective(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRiskAssessmentProcess(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRiskAssessment(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRisk(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentProcess(val) => val.title(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentPlan(val) => val.title(),
                IsmsRecordOrSubtype::IsmsStatementOfApplicability(val) => val.title(),
                IsmsRecordOrSubtype::IsmsControl(val) => val.title(),
                IsmsRecordOrSubtype::IsmsAsset(val) => val.title(),
                IsmsRecordOrSubtype::IsmsResource(val) => val.title(),
                IsmsRecordOrSubtype::IsmsCompetenceRecord(val) => val.title(),
                IsmsRecordOrSubtype::IsmsAwarenessProgramme(val) => val.title(),
                IsmsRecordOrSubtype::IsmsCommunicationPlan(val) => val.title(),
                IsmsRecordOrSubtype::IsmsDocumentedInformation(val) => val.title(),
                IsmsRecordOrSubtype::IsmsOperationalProcedure(val) => val.title(),
                IsmsRecordOrSubtype::IsmsMonitoringProgramme(val) => val.title(),
                IsmsRecordOrSubtype::IsmsAuditProgramme(val) => val.title(),
                IsmsRecordOrSubtype::IsmsAudit(val) => val.title(),
                IsmsRecordOrSubtype::IsmsAuditFinding(val) => val.title(),
                IsmsRecordOrSubtype::IsmsManagementReview(val) => val.title(),
                IsmsRecordOrSubtype::IsmsNonconformity(val) => val.title(),
                IsmsRecordOrSubtype::IsmsCorrectiveAction(val) => val.title(),
                IsmsRecordOrSubtype::IsmsImprovementOpportunity(val) => val.title(),
                IsmsRecordOrSubtype::IsmsSecurityEvent(val) => val.title(),
                IsmsRecordOrSubtype::IsmsSecurityIncident(val) => val.title(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsRecordOrSubtype::IsmsManagementSystem(val) => val.description(),
                IsmsRecordOrSubtype::IsmsOrganization(val) => val.description(),
                IsmsRecordOrSubtype::IsmsInterestedParty(val) => val.description(),
                IsmsRecordOrSubtype::IsmsPolicy(val) => val.description(),
                IsmsRecordOrSubtype::IsmsTopicSpecificPolicy(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRole(val) => val.description(),
                IsmsRecordOrSubtype::IsmsObjective(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRiskAssessmentProcess(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRiskAssessment(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRisk(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentProcess(val) => val.description(),
                IsmsRecordOrSubtype::IsmsRiskTreatmentPlan(val) => val.description(),
                IsmsRecordOrSubtype::IsmsStatementOfApplicability(val) => val.description(),
                IsmsRecordOrSubtype::IsmsControl(val) => val.description(),
                IsmsRecordOrSubtype::IsmsAsset(val) => val.description(),
                IsmsRecordOrSubtype::IsmsResource(val) => val.description(),
                IsmsRecordOrSubtype::IsmsCompetenceRecord(val) => val.description(),
                IsmsRecordOrSubtype::IsmsAwarenessProgramme(val) => val.description(),
                IsmsRecordOrSubtype::IsmsCommunicationPlan(val) => val.description(),
                IsmsRecordOrSubtype::IsmsDocumentedInformation(val) => val.description(),
                IsmsRecordOrSubtype::IsmsOperationalProcedure(val) => val.description(),
                IsmsRecordOrSubtype::IsmsMonitoringProgramme(val) => val.description(),
                IsmsRecordOrSubtype::IsmsAuditProgramme(val) => val.description(),
                IsmsRecordOrSubtype::IsmsAudit(val) => val.description(),
                IsmsRecordOrSubtype::IsmsAuditFinding(val) => val.description(),
                IsmsRecordOrSubtype::IsmsManagementReview(val) => val.description(),
                IsmsRecordOrSubtype::IsmsNonconformity(val) => val.description(),
                IsmsRecordOrSubtype::IsmsCorrectiveAction(val) => val.description(),
                IsmsRecordOrSubtype::IsmsImprovementOpportunity(val) => val.description(),
                IsmsRecordOrSubtype::IsmsSecurityEvent(val) => val.description(),
                IsmsRecordOrSubtype::IsmsSecurityIncident(val) => val.description(),

        }
    }
}
impl IsmsRecord for crate::IsmsSecurityEventOrSubtype {
        fn isms_id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.isms_id(),

        }
    }
        fn title<'a>(&'a self) -> &'a str {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.title(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.description(),

        }
    }
}

pub trait IsmsDocumentControlMixin   {

    fn document_reference<'a>(&'a self) -> Option<&'a str>;
    // fn document_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_reference(&mut self, value: Option<&'a str>);

    fn document_version<'a>(&'a self) -> Option<&'a str>;
    // fn document_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_version(&mut self, value: Option<&'a str>);

    fn document_author<'a>(&'a self) -> Option<&'a str>;
    // fn document_author_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_author(&mut self, value: Option<&'a str>);

    fn document_owner<'a>(&'a self) -> Option<&'a str>;
    // fn document_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_owner(&mut self, value: Option<&'a str>);

    fn document_approver<'a>(&'a self) -> Option<&'a str>;
    // fn document_approver_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_approver(&mut self, value: Option<&'a str>);

    fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn document_approval_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_document_approval_date(&mut self, value: Option<&'a NaiveDate>);

    fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn document_effective_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_document_effective_date(&mut self, value: Option<&'a NaiveDate>);

    fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn document_last_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_document_last_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn document_next_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_document_next_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn document_status<'a>(&'a self) -> Option<&'a str>;
    // fn document_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_status(&mut self, value: Option<&'a str>);

    fn document_classification<'a>(&'a self) -> Option<&'a str>;
    // fn document_classification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_classification(&mut self, value: Option<&'a str>);

    fn document_retention<'a>(&'a self) -> Option<&'a str>;
    // fn document_retention_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_retention(&mut self, value: Option<&'a str>);

    fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn document_distribution_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_document_distribution(&mut self, value: Option<&Vec<String>>);

    fn document_storage<'a>(&'a self) -> Option<&'a str>;
    // fn document_storage_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_storage(&mut self, value: Option<&'a str>);

    fn document_change_control<'a>(&'a self) -> Option<&'a str>;
    // fn document_change_control_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_change_control(&mut self, value: Option<&'a str>);

    fn document_external_origin(&self) -> Option<bool>;
    // fn document_external_origin_mut(&mut self) -> &mut Option<bool>;
    // fn set_document_external_origin(&mut self, value: Option<bool>);

    fn document_external_source<'a>(&'a self) -> Option<&'a str>;
    // fn document_external_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_external_source(&mut self, value: Option<&'a str>);


}

impl IsmsDocumentControlMixin for crate::IsmsDocumentControlMixin {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsPolicy {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsTopicSpecificPolicy {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsRiskAssessmentProcess {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsRiskAssessment {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsRiskTreatmentProcess {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsRiskTreatmentPlan {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsStatementOfApplicability {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsCompetenceRecord {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsAwarenessProgramme {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsCommunicationPlan {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsDocumentedInformation {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsOperationalProcedure {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsMonitoringProgramme {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsAuditProgramme {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsAudit {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}
impl IsmsDocumentControlMixin for crate::IsmsManagementReview {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        return self.document_version.as_deref();
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        return self.document_author.as_deref();
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        return self.document_owner.as_deref();
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        return self.document_approver.as_deref();
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_approval_date.as_ref();
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_effective_date.as_ref();
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_last_review_date.as_ref();
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.document_next_review_date.as_ref();
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        return self.document_status.as_deref();
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        return self.document_classification.as_deref();
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        return self.document_retention.as_deref();
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.document_distribution.as_ref();
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        return self.document_storage.as_deref();
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.document_change_control.as_deref();
    }
        fn document_external_origin(&self) -> Option<bool> {
        return self.document_external_origin;
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        return self.document_external_source.as_deref();
    }
}

impl IsmsDocumentControlMixin for crate::IsmsDocumentControlMixinOrSubtype {
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_reference(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_reference(),

        }
    }
        fn document_version<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_version(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_version(),

        }
    }
        fn document_author<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_author(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_author(),

        }
    }
        fn document_owner<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_owner(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_owner(),

        }
    }
        fn document_approver<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_approver(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_approver(),

        }
    }
        fn document_approval_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_approval_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_approval_date(),

        }
    }
        fn document_effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_effective_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_effective_date(),

        }
    }
        fn document_last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_last_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_last_review_date(),

        }
    }
        fn document_next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_next_review_date(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_next_review_date(),

        }
    }
        fn document_status<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_status(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_status(),

        }
    }
        fn document_classification<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_classification(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_classification(),

        }
    }
        fn document_retention<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_retention(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_retention(),

        }
    }
        fn document_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_distribution().map(|x| x.to_any()),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_distribution().map(|x| x.to_any()),

        }
    }
        fn document_storage<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_storage(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_storage(),

        }
    }
        fn document_change_control<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_change_control(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_change_control(),

        }
    }
        fn document_external_origin(&self) -> Option<bool> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_external_origin(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_external_origin(),

        }
    }
        fn document_external_source<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsDocumentControlMixinOrSubtype::IsmsPolicy(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsTopicSpecificPolicy(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessmentProcess(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskAssessment(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentProcess(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsRiskTreatmentPlan(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsStatementOfApplicability(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsCompetenceRecord(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsAwarenessProgramme(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsCommunicationPlan(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsDocumentedInformation(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsOperationalProcedure(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsMonitoringProgramme(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsAuditProgramme(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsAudit(val) => val.document_external_source(),
                IsmsDocumentControlMixinOrSubtype::IsmsManagementReview(val) => val.document_external_source(),

        }
    }
}

pub trait IsmsManagementSystem : IsmsRecord   {

    fn isms_organization<'a>(&'a self) -> Option<&'a crate::IsmsOrganization>;
    // fn isms_organization_mut(&mut self) -> &mut Option<&'a crate::IsmsOrganization>;
    // fn set_isms_organization<E>(&mut self, value: Option<E>) where E: Into<IsmsOrganization>;

    fn isms_top_management<'a>(&'a self) -> Option<&'a str>;
    // fn isms_top_management_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_top_management(&mut self, value: Option<&'a str>);

    fn isms_governing_body<'a>(&'a self) -> Option<&'a str>;
    // fn isms_governing_body_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_governing_body(&mut self, value: Option<&'a str>);

    fn isms_leadership_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_leadership_evidence_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_leadership_evidence(&mut self, value: Option<&Vec<String>>);

    fn isms_scope<'a>(&'a self) -> Option<&'a str>;
    // fn isms_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_scope(&mut self, value: Option<&'a str>);

    fn isms_scope_boundaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_scope_boundaries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_scope_boundaries(&mut self, value: Option<&Vec<String>>);

    fn isms_scope_exclusions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_scope_exclusions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_scope_exclusions(&mut self, value: Option<&Vec<String>>);

    fn isms_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_interfaces_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_interfaces(&mut self, value: Option<&Vec<String>>);

    fn isms_processes<'a>(&'a self) -> Option<&'a str>;
    // fn isms_processes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_processes(&mut self, value: Option<&'a str>);

    fn isms_internal_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_internal_issues_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_internal_issues(&mut self, value: Option<&Vec<String>>);

    fn isms_external_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_external_issues_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_external_issues(&mut self, value: Option<&Vec<String>>);

    fn isms_risk_and_opportunity_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_risk_and_opportunity_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_risk_and_opportunity_actions(&mut self, value: Option<&Vec<String>>);

    fn isms_planned_changes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_planned_changes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_planned_changes(&mut self, value: Option<&Vec<String>>);

    fn isms_external_services<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn isms_external_services_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_isms_external_services(&mut self, value: Option<&Vec<String>>);

    fn isms_certification_status<'a>(&'a self) -> Option<&'a str>;
    // fn isms_certification_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_certification_status(&mut self, value: Option<&'a str>);

    fn isms_certification_body<'a>(&'a self) -> Option<&'a str>;
    // fn isms_certification_body_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_certification_body(&mut self, value: Option<&'a str>);

    fn isms_certification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn isms_certification_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_isms_certification_date(&mut self, value: Option<&'a NaiveDate>);

    fn isms_recertification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn isms_recertification_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_isms_recertification_date(&mut self, value: Option<&'a NaiveDate>);

    fn isms_interested_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsInterestedParty>>;
    // fn isms_interested_parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsInterestedParty>>;
    // fn set_isms_interested_parties<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsInterestedParty>;

    fn isms_policy<'a>(&'a self) -> Option<&'a crate::IsmsPolicy>;
    // fn isms_policy_mut(&mut self) -> &mut Option<&'a crate::IsmsPolicy>;
    // fn set_isms_policy<E>(&mut self, value: Option<E>) where E: Into<IsmsPolicy>;

    fn isms_topic_specific_policies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsTopicSpecificPolicy>>;
    // fn isms_topic_specific_policies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsTopicSpecificPolicy>>;
    // fn set_isms_topic_specific_policies<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsTopicSpecificPolicy>;

    fn isms_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRole>>;
    // fn isms_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsRole>>;
    // fn set_isms_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsRole>;

    fn isms_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsObjective>>;
    // fn isms_objectives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsObjective>>;
    // fn set_isms_objectives<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsObjective>;

    fn isms_risk_assessment_process<'a>(&'a self) -> Option<&'a crate::IsmsRiskAssessmentProcess>;
    // fn isms_risk_assessment_process_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskAssessmentProcess>;
    // fn set_isms_risk_assessment_process<E>(&mut self, value: Option<E>) where E: Into<IsmsRiskAssessmentProcess>;

    fn isms_risk_treatment_process<'a>(&'a self) -> Option<&'a crate::IsmsRiskTreatmentProcess>;
    // fn isms_risk_treatment_process_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskTreatmentProcess>;
    // fn set_isms_risk_treatment_process<E>(&mut self, value: Option<E>) where E: Into<IsmsRiskTreatmentProcess>;

    fn isms_risk_assessments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskAssessment>>;
    // fn isms_risk_assessments_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskAssessment>>;
    // fn set_isms_risk_assessments<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsRiskAssessment>;

    fn isms_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRisk>>;
    // fn isms_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsRisk>>;
    // fn set_isms_risks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsRisk>;

    fn isms_risk_treatment_plans<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskTreatmentPlan>>;
    // fn isms_risk_treatment_plans_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskTreatmentPlan>>;
    // fn set_isms_risk_treatment_plans<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsRiskTreatmentPlan>;

    fn isms_statement_of_applicability<'a>(&'a self) -> Option<&'a crate::IsmsStatementOfApplicability>;
    // fn isms_statement_of_applicability_mut(&mut self) -> &mut Option<&'a crate::IsmsStatementOfApplicability>;
    // fn set_isms_statement_of_applicability<E>(&mut self, value: Option<E>) where E: Into<IsmsStatementOfApplicability>;

    fn isms_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsControl>>;
    // fn isms_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsControl>>;
    // fn set_isms_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsControl>;

    fn isms_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAsset>>;
    // fn isms_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsAsset>>;
    // fn set_isms_assets<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsAsset>;

    fn isms_resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsResource>>;
    // fn isms_resources_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsResource>>;
    // fn set_isms_resources<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsResource>;

    fn isms_competence_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCompetenceRecord>>;
    // fn isms_competence_records_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsCompetenceRecord>>;
    // fn set_isms_competence_records<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsCompetenceRecord>;

    fn isms_awareness_programme<'a>(&'a self) -> Option<&'a crate::IsmsAwarenessProgramme>;
    // fn isms_awareness_programme_mut(&mut self) -> &mut Option<&'a crate::IsmsAwarenessProgramme>;
    // fn set_isms_awareness_programme<E>(&mut self, value: Option<E>) where E: Into<IsmsAwarenessProgramme>;

    fn isms_communication_plan<'a>(&'a self) -> Option<&'a crate::IsmsCommunicationPlan>;
    // fn isms_communication_plan_mut(&mut self) -> &mut Option<&'a crate::IsmsCommunicationPlan>;
    // fn set_isms_communication_plan<E>(&mut self, value: Option<E>) where E: Into<IsmsCommunicationPlan>;

    fn isms_documented_information<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsDocumentedInformation>>;
    // fn isms_documented_information_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsDocumentedInformation>>;
    // fn set_isms_documented_information<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsDocumentedInformation>;

    fn isms_operational_procedures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsOperationalProcedure>>;
    // fn isms_operational_procedures_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsOperationalProcedure>>;
    // fn set_isms_operational_procedures<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsOperationalProcedure>;

    fn isms_monitoring_programme<'a>(&'a self) -> Option<&'a crate::IsmsMonitoringProgramme>;
    // fn isms_monitoring_programme_mut(&mut self) -> &mut Option<&'a crate::IsmsMonitoringProgramme>;
    // fn set_isms_monitoring_programme<E>(&mut self, value: Option<E>) where E: Into<IsmsMonitoringProgramme>;

    fn isms_audit_programmes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditProgramme>>;
    // fn isms_audit_programmes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditProgramme>>;
    // fn set_isms_audit_programmes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsAuditProgramme>;

    fn isms_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAudit>>;
    // fn isms_audits_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsAudit>>;
    // fn set_isms_audits<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsAudit>;

    fn isms_management_reviews<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementReview>>;
    // fn isms_management_reviews_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementReview>>;
    // fn set_isms_management_reviews<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsManagementReview>;

    fn isms_nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsNonconformity>>;
    // fn isms_nonconformities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsNonconformity>>;
    // fn set_isms_nonconformities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsNonconformity>;

    fn isms_corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCorrectiveAction>>;
    // fn isms_corrective_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsCorrectiveAction>>;
    // fn set_isms_corrective_actions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsCorrectiveAction>;

    fn isms_improvements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsImprovementOpportunity>>;
    // fn isms_improvements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsImprovementOpportunity>>;
    // fn set_isms_improvements<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsImprovementOpportunity>;

    fn isms_security_events<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, IsmsSecurityEventOrSubtype>>;
    // fn isms_security_events_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, IsmsSecurityEventOrSubtype>>;
    // fn set_isms_security_events<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsSecurityEvent>;


}

impl IsmsManagementSystem for crate::IsmsManagementSystem {
        fn isms_organization<'a>(&'a self) -> Option<&'a crate::IsmsOrganization> {
        return self.isms_organization.as_ref();
    }
        fn isms_top_management<'a>(&'a self) -> Option<&'a str> {
        return self.isms_top_management.as_deref();
    }
        fn isms_governing_body<'a>(&'a self) -> Option<&'a str> {
        return self.isms_governing_body.as_deref();
    }
        fn isms_leadership_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_leadership_evidence.as_ref();
    }
        fn isms_scope<'a>(&'a self) -> Option<&'a str> {
        return self.isms_scope.as_deref();
    }
        fn isms_scope_boundaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_scope_boundaries.as_ref();
    }
        fn isms_scope_exclusions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_scope_exclusions.as_ref();
    }
        fn isms_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_interfaces.as_ref();
    }
        fn isms_processes<'a>(&'a self) -> Option<&'a str> {
        return self.isms_processes.as_deref();
    }
        fn isms_internal_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_internal_issues.as_ref();
    }
        fn isms_external_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_external_issues.as_ref();
    }
        fn isms_risk_and_opportunity_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_risk_and_opportunity_actions.as_ref();
    }
        fn isms_planned_changes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_planned_changes.as_ref();
    }
        fn isms_external_services<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.isms_external_services.as_ref();
    }
        fn isms_certification_status<'a>(&'a self) -> Option<&'a str> {
        return self.isms_certification_status.as_deref();
    }
        fn isms_certification_body<'a>(&'a self) -> Option<&'a str> {
        return self.isms_certification_body.as_deref();
    }
        fn isms_certification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.isms_certification_date.as_ref();
    }
        fn isms_recertification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.isms_recertification_date.as_ref();
    }
        fn isms_interested_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsInterestedParty>> {
        return self.isms_interested_parties.as_ref();
    }
        fn isms_policy<'a>(&'a self) -> Option<&'a crate::IsmsPolicy> {
        return self.isms_policy.as_ref();
    }
        fn isms_topic_specific_policies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsTopicSpecificPolicy>> {
        return self.isms_topic_specific_policies.as_ref();
    }
        fn isms_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRole>> {
        return self.isms_roles.as_ref();
    }
        fn isms_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsObjective>> {
        return self.isms_objectives.as_ref();
    }
        fn isms_risk_assessment_process<'a>(&'a self) -> Option<&'a crate::IsmsRiskAssessmentProcess> {
        return self.isms_risk_assessment_process.as_ref();
    }
        fn isms_risk_treatment_process<'a>(&'a self) -> Option<&'a crate::IsmsRiskTreatmentProcess> {
        return self.isms_risk_treatment_process.as_ref();
    }
        fn isms_risk_assessments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskAssessment>> {
        return self.isms_risk_assessments.as_ref();
    }
        fn isms_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRisk>> {
        return self.isms_risks.as_ref();
    }
        fn isms_risk_treatment_plans<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsRiskTreatmentPlan>> {
        return self.isms_risk_treatment_plans.as_ref();
    }
        fn isms_statement_of_applicability<'a>(&'a self) -> Option<&'a crate::IsmsStatementOfApplicability> {
        return self.isms_statement_of_applicability.as_ref();
    }
        fn isms_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsControl>> {
        return self.isms_controls.as_ref();
    }
        fn isms_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAsset>> {
        return self.isms_assets.as_ref();
    }
        fn isms_resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsResource>> {
        return self.isms_resources.as_ref();
    }
        fn isms_competence_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCompetenceRecord>> {
        return self.isms_competence_records.as_ref();
    }
        fn isms_awareness_programme<'a>(&'a self) -> Option<&'a crate::IsmsAwarenessProgramme> {
        return self.isms_awareness_programme.as_ref();
    }
        fn isms_communication_plan<'a>(&'a self) -> Option<&'a crate::IsmsCommunicationPlan> {
        return self.isms_communication_plan.as_ref();
    }
        fn isms_documented_information<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsDocumentedInformation>> {
        return self.isms_documented_information.as_ref();
    }
        fn isms_operational_procedures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsOperationalProcedure>> {
        return self.isms_operational_procedures.as_ref();
    }
        fn isms_monitoring_programme<'a>(&'a self) -> Option<&'a crate::IsmsMonitoringProgramme> {
        return self.isms_monitoring_programme.as_ref();
    }
        fn isms_audit_programmes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditProgramme>> {
        return self.isms_audit_programmes.as_ref();
    }
        fn isms_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAudit>> {
        return self.isms_audits.as_ref();
    }
        fn isms_management_reviews<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementReview>> {
        return self.isms_management_reviews.as_ref();
    }
        fn isms_nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsNonconformity>> {
        return self.isms_nonconformities.as_ref();
    }
        fn isms_corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCorrectiveAction>> {
        return self.isms_corrective_actions.as_ref();
    }
        fn isms_improvements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsImprovementOpportunity>> {
        return self.isms_improvements.as_ref();
    }
        fn isms_security_events<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, IsmsSecurityEventOrSubtype>> {
        return self.isms_security_events.as_ref();
    }
}


pub trait IsmsOrganization : IsmsRecord   {

    fn organization_legal_name<'a>(&'a self) -> Option<&'a str>;
    // fn organization_legal_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_legal_name(&mut self, value: Option<&'a str>);

    fn organization_trading_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn organization_trading_names_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_organization_trading_names(&mut self, value: Option<&Vec<String>>);

    fn organization_kind<'a>(&'a self) -> Option<&'a str>;
    // fn organization_kind_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_kind(&mut self, value: Option<&'a str>);

    fn organization_sector<'a>(&'a self) -> Option<&'a str>;
    // fn organization_sector_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_sector(&mut self, value: Option<&'a str>);

    fn organization_size<'a>(&'a self) -> Option<&'a str>;
    // fn organization_size_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_size(&mut self, value: Option<&'a str>);

    fn organization_employee_count(&self) -> Option<isize>;
    // fn organization_employee_count_mut(&mut self) -> &mut Option<isize>;
    // fn set_organization_employee_count(&mut self, value: Option<isize>);

    fn organization_locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn organization_locations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_organization_locations(&mut self, value: Option<&Vec<String>>);

    fn organization_jurisdictions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn organization_jurisdictions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_organization_jurisdictions(&mut self, value: Option<&Vec<String>>);

    fn organization_parent<'a>(&'a self) -> Option<&'a str>;
    // fn organization_parent_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_parent(&mut self, value: Option<&'a str>);

    fn organization_subsidiaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn organization_subsidiaries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_organization_subsidiaries(&mut self, value: Option<&Vec<String>>);

    fn organization_climate_change_relevant(&self) -> Option<bool>;
    // fn organization_climate_change_relevant_mut(&mut self) -> &mut Option<bool>;
    // fn set_organization_climate_change_relevant(&mut self, value: Option<bool>);


}

impl IsmsOrganization for crate::IsmsOrganization {
        fn organization_legal_name<'a>(&'a self) -> Option<&'a str> {
        return self.organization_legal_name.as_deref();
    }
        fn organization_trading_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.organization_trading_names.as_ref();
    }
        fn organization_kind<'a>(&'a self) -> Option<&'a str> {
        return self.organization_kind.as_deref();
    }
        fn organization_sector<'a>(&'a self) -> Option<&'a str> {
        return self.organization_sector.as_deref();
    }
        fn organization_size<'a>(&'a self) -> Option<&'a str> {
        return self.organization_size.as_deref();
    }
        fn organization_employee_count(&self) -> Option<isize> {
        return self.organization_employee_count;
    }
        fn organization_locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.organization_locations.as_ref();
    }
        fn organization_jurisdictions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.organization_jurisdictions.as_ref();
    }
        fn organization_parent<'a>(&'a self) -> Option<&'a str> {
        return self.organization_parent.as_deref();
    }
        fn organization_subsidiaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.organization_subsidiaries.as_ref();
    }
        fn organization_climate_change_relevant(&self) -> Option<bool> {
        return self.organization_climate_change_relevant;
    }
}


pub trait IsmsInterestedParty : IsmsRecord   {

    fn party_category<'a>(&'a self) -> Option<&'a str>;
    // fn party_category_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_party_category(&mut self, value: Option<&'a str>);

    fn party_relationship<'a>(&'a self) -> Option<&'a str>;
    // fn party_relationship_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_party_relationship(&mut self, value: Option<&'a str>);

    fn party_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn party_requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_party_requirements(&mut self, value: Option<&Vec<String>>);

    fn party_addressed_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn party_addressed_requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_party_addressed_requirements(&mut self, value: Option<&Vec<String>>);

    fn party_climate_change_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn party_climate_change_requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_party_climate_change_requirements(&mut self, value: Option<&Vec<String>>);

    fn party_communication_needs<'a>(&'a self) -> Option<&'a str>;
    // fn party_communication_needs_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_party_communication_needs(&mut self, value: Option<&'a str>);

    fn party_contact<'a>(&'a self) -> Option<&'a str>;
    // fn party_contact_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_party_contact(&mut self, value: Option<&'a str>);


}

impl IsmsInterestedParty for crate::IsmsInterestedParty {
        fn party_category<'a>(&'a self) -> Option<&'a str> {
        return self.party_category.as_deref();
    }
        fn party_relationship<'a>(&'a self) -> Option<&'a str> {
        return self.party_relationship.as_deref();
    }
        fn party_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_requirements.as_ref();
    }
        fn party_addressed_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_addressed_requirements.as_ref();
    }
        fn party_climate_change_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_climate_change_requirements.as_ref();
    }
        fn party_communication_needs<'a>(&'a self) -> Option<&'a str> {
        return self.party_communication_needs.as_deref();
    }
        fn party_contact<'a>(&'a self) -> Option<&'a str> {
        return self.party_contact.as_deref();
    }
}


pub trait IsmsPolicy : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn policy_statement<'a>(&'a self) -> Option<&'a str>;
    // fn policy_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_policy_statement(&mut self, value: Option<&'a str>);

    fn policy_objectives_framework<'a>(&'a self) -> Option<&'a str>;
    // fn policy_objectives_framework_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_policy_objectives_framework(&mut self, value: Option<&'a str>);

    fn policy_commitments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn policy_commitments_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_policy_commitments(&mut self, value: Option<&Vec<String>>);

    fn policy_applicability<'a>(&'a self) -> Option<&'a str>;
    // fn policy_applicability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_policy_applicability(&mut self, value: Option<&'a str>);

    fn policy_communication_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn policy_communication_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_policy_communication_date(&mut self, value: Option<&'a NaiveDate>);

    fn policy_acknowledgement_required(&self) -> Option<bool>;
    // fn policy_acknowledgement_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_policy_acknowledgement_required(&mut self, value: Option<bool>);

    fn policy_management_systems<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>>;
    // fn policy_management_systems_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>>;
    // fn set_policy_management_systems(&mut self, value: Option<&Vec<IsmsManagementSystemStandard>>);


}

impl IsmsPolicy for crate::IsmsPolicy {
        fn policy_statement<'a>(&'a self) -> Option<&'a str> {
        return self.policy_statement.as_deref();
    }
        fn policy_objectives_framework<'a>(&'a self) -> Option<&'a str> {
        return self.policy_objectives_framework.as_deref();
    }
        fn policy_commitments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.policy_commitments.as_ref();
    }
        fn policy_applicability<'a>(&'a self) -> Option<&'a str> {
        return self.policy_applicability.as_deref();
    }
        fn policy_communication_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.policy_communication_date.as_ref();
    }
        fn policy_acknowledgement_required(&self) -> Option<bool> {
        return self.policy_acknowledgement_required;
    }
        fn policy_management_systems<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>> {
        return self.policy_management_systems.as_ref();
    }
}


pub trait IsmsTopicSpecificPolicy : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn relevant_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_relevant_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn topic_policy_topic<'a>(&'a self) -> Option<&'a str>;
    // fn topic_policy_topic_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_topic_policy_topic(&mut self, value: Option<&'a str>);

    fn topic_policy_parent<'a>(&'a self) -> Option<&'a str>;
    // fn topic_policy_parent_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_topic_policy_parent<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn topic_policy_audience<'a>(&'a self) -> Option<&'a str>;
    // fn topic_policy_audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_topic_policy_audience(&mut self, value: Option<&'a str>);


}

impl IsmsTopicSpecificPolicy for crate::IsmsTopicSpecificPolicy {
        fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.relevant_controls.as_ref();
    }
        fn topic_policy_topic<'a>(&'a self) -> Option<&'a str> {
        return self.topic_policy_topic.as_deref();
    }
        fn topic_policy_parent<'a>(&'a self) -> Option<&'a str> {
        return self.topic_policy_parent.as_deref();
    }
        fn topic_policy_audience<'a>(&'a self) -> Option<&'a str> {
        return self.topic_policy_audience.as_deref();
    }
}


pub trait IsmsRole : IsmsRecord   {

    fn role_category<'a>(&'a self) -> Option<&'a str>;
    // fn role_category_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_category(&mut self, value: Option<&'a str>);

    fn role_responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn role_responsibilities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_role_responsibilities(&mut self, value: Option<&Vec<String>>);

    fn role_authorities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn role_authorities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_role_authorities(&mut self, value: Option<&Vec<String>>);

    fn role_accountability<'a>(&'a self) -> Option<&'a str>;
    // fn role_accountability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_accountability(&mut self, value: Option<&'a str>);

    fn role_holders<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn role_holders_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_role_holders(&mut self, value: Option<&Vec<String>>);

    fn role_delegation<'a>(&'a self) -> Option<&'a str>;
    // fn role_delegation_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_delegation(&mut self, value: Option<&'a str>);

    fn role_reports_to<'a>(&'a self) -> Option<&'a str>;
    // fn role_reports_to_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_reports_to<E>(&mut self, value: Option<&'a str>) where E: Into<String>;


}

impl IsmsRole for crate::IsmsRole {
        fn role_category<'a>(&'a self) -> Option<&'a str> {
        return self.role_category.as_deref();
    }
        fn role_responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.role_responsibilities.as_ref();
    }
        fn role_authorities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.role_authorities.as_ref();
    }
        fn role_accountability<'a>(&'a self) -> Option<&'a str> {
        return self.role_accountability.as_deref();
    }
        fn role_holders<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.role_holders.as_ref();
    }
        fn role_delegation<'a>(&'a self) -> Option<&'a str> {
        return self.role_delegation.as_deref();
    }
        fn role_reports_to<'a>(&'a self) -> Option<&'a str> {
        return self.role_reports_to.as_deref();
    }
}


pub trait IsmsObjective : IsmsRecord   {

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn relevant_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_relevant_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn objective_statement<'a>(&'a self) -> Option<&'a str>;
    // fn objective_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_statement(&mut self, value: Option<&'a str>);

    fn objective_target<'a>(&'a self) -> Option<&'a str>;
    // fn objective_target_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_target(&mut self, value: Option<&'a str>);

    fn objective_current_value<'a>(&'a self) -> Option<&'a str>;
    // fn objective_current_value_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_current_value(&mut self, value: Option<&'a str>);

    fn objective_metric<'a>(&'a self) -> Option<&'a str>;
    // fn objective_metric_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_metric(&mut self, value: Option<&'a str>);

    fn objective_measurement_method<'a>(&'a self) -> Option<&'a str>;
    // fn objective_measurement_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_measurement_method(&mut self, value: Option<&'a str>);

    fn objective_measurement_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn objective_measurement_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_measurement_frequency(&mut self, value: Option<&'a str>);

    fn objective_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn objective_target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_objective_target_date(&mut self, value: Option<&'a NaiveDate>);

    fn objective_achievement<'a>(&'a self) -> Option<&'a str>;
    // fn objective_achievement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_achievement(&mut self, value: Option<&'a str>);

    fn objective_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn objective_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_objective_risks<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn objective_action_plan<'a>(&'a self) -> Option<&'a str>;
    // fn objective_action_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_action_plan(&mut self, value: Option<&'a str>);

    fn objective_resources<'a>(&'a self) -> Option<&'a str>;
    // fn objective_resources_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_resources(&mut self, value: Option<&'a str>);


}

impl IsmsObjective for crate::IsmsObjective {
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.relevant_controls.as_ref();
    }
        fn objective_statement<'a>(&'a self) -> Option<&'a str> {
        return self.objective_statement.as_deref();
    }
        fn objective_target<'a>(&'a self) -> Option<&'a str> {
        return self.objective_target.as_deref();
    }
        fn objective_current_value<'a>(&'a self) -> Option<&'a str> {
        return self.objective_current_value.as_deref();
    }
        fn objective_metric<'a>(&'a self) -> Option<&'a str> {
        return self.objective_metric.as_deref();
    }
        fn objective_measurement_method<'a>(&'a self) -> Option<&'a str> {
        return self.objective_measurement_method.as_deref();
    }
        fn objective_measurement_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.objective_measurement_frequency.as_deref();
    }
        fn objective_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.objective_target_date.as_ref();
    }
        fn objective_achievement<'a>(&'a self) -> Option<&'a str> {
        return self.objective_achievement.as_deref();
    }
        fn objective_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.objective_risks.as_ref();
    }
        fn objective_action_plan<'a>(&'a self) -> Option<&'a str> {
        return self.objective_action_plan.as_deref();
    }
        fn objective_resources<'a>(&'a self) -> Option<&'a str> {
        return self.objective_resources.as_deref();
    }
}


pub trait IsmsRiskAssessmentProcess : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn risk_acceptance_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn risk_acceptance_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_acceptance_criteria(&mut self, value: Option<&'a str>);

    fn risk_assessment_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn risk_assessment_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_assessment_criteria(&mut self, value: Option<&'a str>);

    fn risk_assessment_method<'a>(&'a self) -> Option<&'a str>;
    // fn risk_assessment_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_assessment_method(&mut self, value: Option<&'a str>);

    fn risk_likelihood_scale<'a>(&'a self) -> Option<&'a str>;
    // fn risk_likelihood_scale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_likelihood_scale(&mut self, value: Option<&'a str>);

    fn risk_impact_scale<'a>(&'a self) -> Option<&'a str>;
    // fn risk_impact_scale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_impact_scale(&mut self, value: Option<&'a str>);

    fn risk_matrix<'a>(&'a self) -> Option<&'a str>;
    // fn risk_matrix_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_matrix(&mut self, value: Option<&'a str>);

    fn risk_assessment_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn risk_assessment_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_assessment_frequency(&mut self, value: Option<&'a str>);

    fn risk_assessment_triggers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risk_assessment_triggers_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risk_assessment_triggers(&mut self, value: Option<&Vec<String>>);


}

impl IsmsRiskAssessmentProcess for crate::IsmsRiskAssessmentProcess {
        fn risk_acceptance_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.risk_acceptance_criteria.as_deref();
    }
        fn risk_assessment_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.risk_assessment_criteria.as_deref();
    }
        fn risk_assessment_method<'a>(&'a self) -> Option<&'a str> {
        return self.risk_assessment_method.as_deref();
    }
        fn risk_likelihood_scale<'a>(&'a self) -> Option<&'a str> {
        return self.risk_likelihood_scale.as_deref();
    }
        fn risk_impact_scale<'a>(&'a self) -> Option<&'a str> {
        return self.risk_impact_scale.as_deref();
    }
        fn risk_matrix<'a>(&'a self) -> Option<&'a str> {
        return self.risk_matrix.as_deref();
    }
        fn risk_assessment_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.risk_assessment_frequency.as_deref();
    }
        fn risk_assessment_triggers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risk_assessment_triggers.as_ref();
    }
}


pub trait IsmsRiskAssessment : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn assessment_scope<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_scope(&mut self, value: Option<&'a str>);

    fn assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn assessment_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_assessment_date(&mut self, value: Option<&'a NaiveDate>);

    fn assessment_assessor<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_assessor_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_assessor(&mut self, value: Option<&'a str>);

    fn assessment_method_used<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_method_used_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_method_used(&mut self, value: Option<&'a str>);

    fn assessment_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn assessment_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_assessment_risks<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn assessment_summary<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_summary_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_summary(&mut self, value: Option<&'a str>);

    fn assessment_recommendations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn assessment_recommendations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_assessment_recommendations(&mut self, value: Option<&Vec<String>>);

    fn assessment_next_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn assessment_next_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_assessment_next_date(&mut self, value: Option<&'a NaiveDate>);


}

impl IsmsRiskAssessment for crate::IsmsRiskAssessment {
        fn assessment_scope<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_scope.as_deref();
    }
        fn assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.assessment_date.as_ref();
    }
        fn assessment_assessor<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_assessor.as_deref();
    }
        fn assessment_method_used<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_method_used.as_deref();
    }
        fn assessment_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.assessment_risks.as_ref();
    }
        fn assessment_summary<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_summary.as_deref();
    }
        fn assessment_recommendations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.assessment_recommendations.as_ref();
    }
        fn assessment_next_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.assessment_next_date.as_ref();
    }
}


pub trait IsmsRisk : IsmsRecord   {

    fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn affected_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_affected_assets<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn affected_security_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>>;
    // fn affected_security_properties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>>;
    // fn set_affected_security_properties(&mut self, value: Option<&Vec<IsmsSecurityProperty>>);

    fn risk_source<'a>(&'a self) -> Option<&'a str>;
    // fn risk_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_source(&mut self, value: Option<&'a str>);

    fn risk_threat<'a>(&'a self) -> Option<&'a str>;
    // fn risk_threat_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_threat(&mut self, value: Option<&'a str>);

    fn risk_vulnerability<'a>(&'a self) -> Option<&'a str>;
    // fn risk_vulnerability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_vulnerability(&mut self, value: Option<&'a str>);

    fn risk_owner<'a>(&'a self) -> Option<&'a str>;
    // fn risk_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_owner(&mut self, value: Option<&'a str>);

    fn risk_likelihood<'a>(&'a self) -> Option<&'a crate::IsmsLikelihood>;
    // fn risk_likelihood_mut(&mut self) -> &mut Option<&'a crate::IsmsLikelihood>;
    // fn set_risk_likelihood(&mut self, value: Option<&'a IsmsLikelihood>);

    fn risk_impact<'a>(&'a self) -> Option<&'a crate::IsmsImpact>;
    // fn risk_impact_mut(&mut self) -> &mut Option<&'a crate::IsmsImpact>;
    // fn set_risk_impact(&mut self, value: Option<&'a IsmsImpact>);

    fn risk_inherent_level<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel>;
    // fn risk_inherent_level_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskLevel>;
    // fn set_risk_inherent_level(&mut self, value: Option<&'a IsmsRiskLevel>);

    fn risk_existing_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risk_existing_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risk_existing_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn risk_residual_level<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel>;
    // fn risk_residual_level_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskLevel>;
    // fn set_risk_residual_level(&mut self, value: Option<&'a IsmsRiskLevel>);

    fn risk_treatment_option<'a>(&'a self) -> Option<&'a crate::IsmsRiskTreatmentOption>;
    // fn risk_treatment_option_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskTreatmentOption>;
    // fn set_risk_treatment_option(&mut self, value: Option<&'a IsmsRiskTreatmentOption>);

    fn risk_treatment_priority<'a>(&'a self) -> Option<&'a str>;
    // fn risk_treatment_priority_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_treatment_priority(&mut self, value: Option<&'a str>);


}

impl IsmsRisk for crate::IsmsRisk {
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn affected_security_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>> {
        return self.affected_security_properties.as_ref();
    }
        fn risk_source<'a>(&'a self) -> Option<&'a str> {
        return self.risk_source.as_deref();
    }
        fn risk_threat<'a>(&'a self) -> Option<&'a str> {
        return self.risk_threat.as_deref();
    }
        fn risk_vulnerability<'a>(&'a self) -> Option<&'a str> {
        return self.risk_vulnerability.as_deref();
    }
        fn risk_owner<'a>(&'a self) -> Option<&'a str> {
        return self.risk_owner.as_deref();
    }
        fn risk_likelihood<'a>(&'a self) -> Option<&'a crate::IsmsLikelihood> {
        return self.risk_likelihood.as_ref();
    }
        fn risk_impact<'a>(&'a self) -> Option<&'a crate::IsmsImpact> {
        return self.risk_impact.as_ref();
    }
        fn risk_inherent_level<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel> {
        return self.risk_inherent_level.as_ref();
    }
        fn risk_existing_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risk_existing_controls.as_ref();
    }
        fn risk_residual_level<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel> {
        return self.risk_residual_level.as_ref();
    }
        fn risk_treatment_option<'a>(&'a self) -> Option<&'a crate::IsmsRiskTreatmentOption> {
        return self.risk_treatment_option.as_ref();
    }
        fn risk_treatment_priority<'a>(&'a self) -> Option<&'a str> {
        return self.risk_treatment_priority.as_deref();
    }
}


pub trait IsmsRiskTreatmentProcess : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn treatment_options_guidance<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_options_guidance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_options_guidance(&mut self, value: Option<&'a str>);

    fn treatment_control_selection<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_control_selection_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_control_selection(&mut self, value: Option<&'a str>);

    fn treatment_annex_a_comparison<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_annex_a_comparison_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_annex_a_comparison(&mut self, value: Option<&'a str>);

    fn treatment_soa_template<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_soa_template_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_soa_template(&mut self, value: Option<&'a str>);

    fn treatment_approval_workflow<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_approval_workflow_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_approval_workflow(&mut self, value: Option<&'a str>);


}

impl IsmsRiskTreatmentProcess for crate::IsmsRiskTreatmentProcess {
        fn treatment_options_guidance<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_options_guidance.as_deref();
    }
        fn treatment_control_selection<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_control_selection.as_deref();
    }
        fn treatment_annex_a_comparison<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_annex_a_comparison.as_deref();
    }
        fn treatment_soa_template<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_soa_template.as_deref();
    }
        fn treatment_approval_workflow<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_approval_workflow.as_deref();
    }
}


pub trait IsmsRiskTreatmentPlan : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn implementation_state<'a>(&'a self) -> Option<&'a crate::IsmsImplementationStatus>;
    // fn implementation_state_mut(&mut self) -> &mut Option<&'a crate::IsmsImplementationStatus>;
    // fn set_implementation_state(&mut self, value: Option<&'a IsmsImplementationStatus>);

    fn plan_scope<'a>(&'a self) -> Option<&'a str>;
    // fn plan_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_scope(&mut self, value: Option<&'a str>);

    fn plan_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn plan_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_plan_risks<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn plan_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn plan_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_plan_actions(&mut self, value: Option<&Vec<String>>);

    fn plan_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn plan_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_plan_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn plan_resources<'a>(&'a self) -> Option<&'a str>;
    // fn plan_resources_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_resources(&mut self, value: Option<&'a str>);

    fn plan_responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn plan_responsible_parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_plan_responsible_parties(&mut self, value: Option<&Vec<String>>);

    fn plan_timeline<'a>(&'a self) -> Option<&'a str>;
    // fn plan_timeline_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_timeline(&mut self, value: Option<&'a str>);

    fn plan_risk_owner_approval<'a>(&'a self) -> Option<&'a str>;
    // fn plan_risk_owner_approval_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_risk_owner_approval(&mut self, value: Option<&'a str>);

    fn plan_residual_risk_acceptance<'a>(&'a self) -> Option<&'a str>;
    // fn plan_residual_risk_acceptance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_residual_risk_acceptance(&mut self, value: Option<&'a str>);

    fn plan_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn plan_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_plan_completion_date(&mut self, value: Option<&'a NaiveDate>);


}

impl IsmsRiskTreatmentPlan for crate::IsmsRiskTreatmentPlan {
        fn implementation_state<'a>(&'a self) -> Option<&'a crate::IsmsImplementationStatus> {
        return self.implementation_state.as_ref();
    }
        fn plan_scope<'a>(&'a self) -> Option<&'a str> {
        return self.plan_scope.as_deref();
    }
        fn plan_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.plan_risks.as_ref();
    }
        fn plan_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.plan_actions.as_ref();
    }
        fn plan_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.plan_controls.as_ref();
    }
        fn plan_resources<'a>(&'a self) -> Option<&'a str> {
        return self.plan_resources.as_deref();
    }
        fn plan_responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.plan_responsible_parties.as_ref();
    }
        fn plan_timeline<'a>(&'a self) -> Option<&'a str> {
        return self.plan_timeline.as_deref();
    }
        fn plan_risk_owner_approval<'a>(&'a self) -> Option<&'a str> {
        return self.plan_risk_owner_approval.as_deref();
    }
        fn plan_residual_risk_acceptance<'a>(&'a self) -> Option<&'a str> {
        return self.plan_residual_risk_acceptance.as_deref();
    }
        fn plan_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.plan_completion_date.as_ref();
    }
}


pub trait IsmsStatementOfApplicability : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn soa_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, IsmsApplicabilityEntryOrSubtype>>;
    // fn soa_entries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, IsmsApplicabilityEntryOrSubtype>>;
    // fn set_soa_entries<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsApplicabilityEntry>;


}

impl IsmsStatementOfApplicability for crate::IsmsStatementOfApplicability {
        fn soa_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, IsmsApplicabilityEntryOrSubtype>> {
        return self.soa_entries.as_ref();
    }
}


pub trait IsmsApplicabilityEntry   {

    fn entry_annex_a_control<'a>(&'a self) -> Option<&'a crate::IsmsAnnexAControl>;
    // fn entry_annex_a_control_mut(&mut self) -> &mut Option<&'a crate::IsmsAnnexAControl>;
    // fn set_entry_annex_a_control(&mut self, value: Option<&'a IsmsAnnexAControl>);

    fn entry_type<'a>(&'a self) -> Option<&'a str>;
    // fn entry_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_entry_type(&mut self, value: Option<&'a str>);

    fn entry_justification<'a>(&'a self) -> &'a str;
    // fn entry_justification_mut(&mut self) -> &mut &'a str;
    // fn set_entry_justification(&mut self, value: String);


}

impl IsmsApplicabilityEntry for crate::IsmsApplicabilityEntry {
        fn entry_annex_a_control<'a>(&'a self) -> Option<&'a crate::IsmsAnnexAControl> {
        return self.entry_annex_a_control.as_ref();
    }
        fn entry_type<'a>(&'a self) -> Option<&'a str> {
        return self.entry_type.as_deref();
    }
        fn entry_justification<'a>(&'a self) -> &'a str {
        return &self.entry_justification[..];
    }
}
impl IsmsApplicabilityEntry for crate::IsmsIncludedControl {
        fn entry_annex_a_control<'a>(&'a self) -> Option<&'a crate::IsmsAnnexAControl> {
        return self.entry_annex_a_control.as_ref();
    }
        fn entry_type<'a>(&'a self) -> Option<&'a str> {
        return self.entry_type.as_deref();
    }
        fn entry_justification<'a>(&'a self) -> &'a str {
        return &self.entry_justification[..];
    }
}
impl IsmsApplicabilityEntry for crate::IsmsExcludedControl {
        fn entry_annex_a_control<'a>(&'a self) -> Option<&'a crate::IsmsAnnexAControl> {
        return Some(&self.entry_annex_a_control);
    }
        fn entry_type<'a>(&'a self) -> Option<&'a str> {
        return self.entry_type.as_deref();
    }
        fn entry_justification<'a>(&'a self) -> &'a str {
        return &self.entry_justification[..];
    }
}

impl IsmsApplicabilityEntry for crate::IsmsApplicabilityEntryOrSubtype {
        fn entry_annex_a_control<'a>(&'a self) -> Option<&'a crate::IsmsAnnexAControl> {
        match self {
                IsmsApplicabilityEntryOrSubtype::IsmsIncludedControl(val) => val.entry_annex_a_control(),
                IsmsApplicabilityEntryOrSubtype::IsmsExcludedControl(val) => val.entry_annex_a_control(),

        }
    }
        fn entry_type<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsApplicabilityEntryOrSubtype::IsmsIncludedControl(val) => val.entry_type(),
                IsmsApplicabilityEntryOrSubtype::IsmsExcludedControl(val) => val.entry_type(),

        }
    }
        fn entry_justification<'a>(&'a self) -> &'a str {
        match self {
                IsmsApplicabilityEntryOrSubtype::IsmsIncludedControl(val) => val.entry_justification(),
                IsmsApplicabilityEntryOrSubtype::IsmsExcludedControl(val) => val.entry_justification(),

        }
    }
}

pub trait IsmsIncludedControl : IsmsApplicabilityEntry   {

    fn implementation_state<'a>(&'a self) -> &'a crate::IsmsImplementationStatus;
    // fn implementation_state_mut(&mut self) -> &mut &'a crate::IsmsImplementationStatus;
    // fn set_implementation_state(&mut self, value: IsmsImplementationStatus);

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn included_control<'a>(&'a self) -> Option<&'a str>;
    // fn included_control_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_included_control<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn included_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn included_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_included_evidence(&mut self, value: Option<&'a str>);

    fn included_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn included_target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_included_target_date(&mut self, value: Option<&'a NaiveDate>);


}

impl IsmsIncludedControl for crate::IsmsIncludedControl {
        fn implementation_state<'a>(&'a self) -> &'a crate::IsmsImplementationStatus {
        return &self.implementation_state;
    }
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn included_control<'a>(&'a self) -> Option<&'a str> {
        return self.included_control.as_deref();
    }
        fn included_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.included_evidence.as_deref();
    }
        fn included_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.included_target_date.as_ref();
    }
}


pub trait IsmsExcludedControl : IsmsApplicabilityEntry   {


}

impl IsmsExcludedControl for crate::IsmsExcludedControl {
}


pub trait IsmsControl : IsmsRecord   {

    fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn relevant_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_relevant_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn implementation_state<'a>(&'a self) -> Option<&'a crate::IsmsImplementationStatus>;
    // fn implementation_state_mut(&mut self) -> &mut Option<&'a crate::IsmsImplementationStatus>;
    // fn set_implementation_state(&mut self, value: Option<&'a IsmsImplementationStatus>);

    fn control_annex_a_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAnnexAControl>>;
    // fn control_annex_a_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsAnnexAControl>>;
    // fn set_control_annex_a_controls(&mut self, value: Option<&Vec<IsmsAnnexAControl>>);

    fn control_theme<'a>(&'a self) -> Option<&'a crate::IsmsControlTheme>;
    // fn control_theme_mut(&mut self) -> &mut Option<&'a crate::IsmsControlTheme>;
    // fn set_control_theme(&mut self, value: Option<&'a IsmsControlTheme>);

    fn control_text<'a>(&'a self) -> Option<&'a str>;
    // fn control_text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_text(&mut self, value: Option<&'a str>);

    fn control_guidance<'a>(&'a self) -> Option<&'a str>;
    // fn control_guidance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_guidance(&mut self, value: Option<&'a str>);

    fn control_threats<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn control_threats_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_control_threats(&mut self, value: Option<&Vec<String>>);

    fn control_asset_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn control_asset_types_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_control_asset_types(&mut self, value: Option<&Vec<String>>);

    fn control_owner<'a>(&'a self) -> Option<&'a str>;
    // fn control_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_owner(&mut self, value: Option<&'a str>);

    fn control_implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn control_implementation_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_control_implementation_date(&mut self, value: Option<&'a NaiveDate>);

    fn control_effectiveness<'a>(&'a self) -> Option<&'a str>;
    // fn control_effectiveness_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_effectiveness(&mut self, value: Option<&'a str>);

    fn control_last_tested<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn control_last_tested_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_control_last_tested(&mut self, value: Option<&'a NaiveDate>);

    fn control_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn control_evidence_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_control_evidence(&mut self, value: Option<&Vec<String>>);


}

impl IsmsControl for crate::IsmsControl {
        fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.relevant_controls.as_ref();
    }
        fn implementation_state<'a>(&'a self) -> Option<&'a crate::IsmsImplementationStatus> {
        return self.implementation_state.as_ref();
    }
        fn control_annex_a_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAnnexAControl>> {
        return self.control_annex_a_controls.as_ref();
    }
        fn control_theme<'a>(&'a self) -> Option<&'a crate::IsmsControlTheme> {
        return self.control_theme.as_ref();
    }
        fn control_text<'a>(&'a self) -> Option<&'a str> {
        return self.control_text.as_deref();
    }
        fn control_guidance<'a>(&'a self) -> Option<&'a str> {
        return self.control_guidance.as_deref();
    }
        fn control_threats<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.control_threats.as_ref();
    }
        fn control_asset_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.control_asset_types.as_ref();
    }
        fn control_owner<'a>(&'a self) -> Option<&'a str> {
        return self.control_owner.as_deref();
    }
        fn control_implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.control_implementation_date.as_ref();
    }
        fn control_effectiveness<'a>(&'a self) -> Option<&'a str> {
        return self.control_effectiveness.as_deref();
    }
        fn control_last_tested<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.control_last_tested.as_ref();
    }
        fn control_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.control_evidence.as_ref();
    }
}


pub trait IsmsAsset : IsmsRecord   {

    fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn relevant_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_relevant_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn asset_category<'a>(&'a self) -> Option<&'a str>;
    // fn asset_category_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_category(&mut self, value: Option<&'a str>);

    fn asset_owner<'a>(&'a self) -> Option<&'a str>;
    // fn asset_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_owner(&mut self, value: Option<&'a str>);

    fn asset_custodian<'a>(&'a self) -> Option<&'a str>;
    // fn asset_custodian_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_custodian(&mut self, value: Option<&'a str>);

    fn asset_classification<'a>(&'a self) -> Option<&'a str>;
    // fn asset_classification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_classification(&mut self, value: Option<&'a str>);

    fn asset_location<'a>(&'a self) -> Option<&'a str>;
    // fn asset_location_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_location(&mut self, value: Option<&'a str>);

    fn asset_criticality<'a>(&'a self) -> Option<&'a str>;
    // fn asset_criticality_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_criticality(&mut self, value: Option<&'a str>);


}

impl IsmsAsset for crate::IsmsAsset {
        fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.relevant_controls.as_ref();
    }
        fn asset_category<'a>(&'a self) -> Option<&'a str> {
        return self.asset_category.as_deref();
    }
        fn asset_owner<'a>(&'a self) -> Option<&'a str> {
        return self.asset_owner.as_deref();
    }
        fn asset_custodian<'a>(&'a self) -> Option<&'a str> {
        return self.asset_custodian.as_deref();
    }
        fn asset_classification<'a>(&'a self) -> Option<&'a str> {
        return self.asset_classification.as_deref();
    }
        fn asset_location<'a>(&'a self) -> Option<&'a str> {
        return self.asset_location.as_deref();
    }
        fn asset_criticality<'a>(&'a self) -> Option<&'a str> {
        return self.asset_criticality.as_deref();
    }
}


pub trait IsmsResource : IsmsRecord   {

    fn resource_category<'a>(&'a self) -> Option<&'a str>;
    // fn resource_category_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_category(&mut self, value: Option<&'a str>);

    fn resource_quantity<'a>(&'a self) -> Option<&'a str>;
    // fn resource_quantity_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_quantity(&mut self, value: Option<&'a str>);

    fn resource_allocation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn resource_allocation_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_resource_allocation_date(&mut self, value: Option<&'a NaiveDate>);

    fn resource_allocated_to<'a>(&'a self) -> Option<&'a str>;
    // fn resource_allocated_to_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_allocated_to(&mut self, value: Option<&'a str>);

    fn resource_cost<'a>(&'a self) -> Option<&'a str>;
    // fn resource_cost_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_cost(&mut self, value: Option<&'a str>);

    fn resource_availability<'a>(&'a self) -> Option<&'a str>;
    // fn resource_availability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_availability(&mut self, value: Option<&'a str>);


}

impl IsmsResource for crate::IsmsResource {
        fn resource_category<'a>(&'a self) -> Option<&'a str> {
        return self.resource_category.as_deref();
    }
        fn resource_quantity<'a>(&'a self) -> Option<&'a str> {
        return self.resource_quantity.as_deref();
    }
        fn resource_allocation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.resource_allocation_date.as_ref();
    }
        fn resource_allocated_to<'a>(&'a self) -> Option<&'a str> {
        return self.resource_allocated_to.as_deref();
    }
        fn resource_cost<'a>(&'a self) -> Option<&'a str> {
        return self.resource_cost.as_deref();
    }
        fn resource_availability<'a>(&'a self) -> Option<&'a str> {
        return self.resource_availability.as_deref();
    }
}


pub trait IsmsCompetenceRecord : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn competence_person<'a>(&'a self) -> Option<&'a str>;
    // fn competence_person_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_competence_person(&mut self, value: Option<&'a str>);

    fn competence_role<'a>(&'a self) -> Option<&'a str>;
    // fn competence_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_competence_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn competence_required<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_required_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_required(&mut self, value: Option<&Vec<String>>);

    fn competence_education<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_education_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_education(&mut self, value: Option<&Vec<String>>);

    fn competence_training<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_training_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_training(&mut self, value: Option<&Vec<String>>);

    fn competence_experience<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_experience_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_experience(&mut self, value: Option<&Vec<String>>);

    fn competence_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn competence_assessment_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_competence_assessment_date(&mut self, value: Option<&'a NaiveDate>);

    fn competence_gaps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_gaps_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_gaps(&mut self, value: Option<&Vec<String>>);

    fn competence_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_actions(&mut self, value: Option<&Vec<String>>);


}

impl IsmsCompetenceRecord for crate::IsmsCompetenceRecord {
        fn competence_person<'a>(&'a self) -> Option<&'a str> {
        return self.competence_person.as_deref();
    }
        fn competence_role<'a>(&'a self) -> Option<&'a str> {
        return self.competence_role.as_deref();
    }
        fn competence_required<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_required.as_ref();
    }
        fn competence_education<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_education.as_ref();
    }
        fn competence_training<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_training.as_ref();
    }
        fn competence_experience<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_experience.as_ref();
    }
        fn competence_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.competence_assessment_date.as_ref();
    }
        fn competence_gaps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_gaps.as_ref();
    }
        fn competence_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_actions.as_ref();
    }
}


pub trait IsmsAwarenessProgramme : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn awareness_topics<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn awareness_topics_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_awareness_topics(&mut self, value: Option<&Vec<String>>);

    fn awareness_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn awareness_methods_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_awareness_methods(&mut self, value: Option<&Vec<String>>);

    fn awareness_audience<'a>(&'a self) -> Option<&'a str>;
    // fn awareness_audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_awareness_audience(&mut self, value: Option<&'a str>);

    fn awareness_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn awareness_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_awareness_frequency(&mut self, value: Option<&'a str>);

    fn awareness_completion_tracking<'a>(&'a self) -> Option<&'a str>;
    // fn awareness_completion_tracking_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_awareness_completion_tracking(&mut self, value: Option<&'a str>);

    fn awareness_effectiveness<'a>(&'a self) -> Option<&'a str>;
    // fn awareness_effectiveness_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_awareness_effectiveness(&mut self, value: Option<&'a str>);


}

impl IsmsAwarenessProgramme for crate::IsmsAwarenessProgramme {
        fn awareness_topics<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.awareness_topics.as_ref();
    }
        fn awareness_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.awareness_methods.as_ref();
    }
        fn awareness_audience<'a>(&'a self) -> Option<&'a str> {
        return self.awareness_audience.as_deref();
    }
        fn awareness_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.awareness_frequency.as_deref();
    }
        fn awareness_completion_tracking<'a>(&'a self) -> Option<&'a str> {
        return self.awareness_completion_tracking.as_deref();
    }
        fn awareness_effectiveness<'a>(&'a self) -> Option<&'a str> {
        return self.awareness_effectiveness.as_deref();
    }
}


pub trait IsmsCommunicationPlan : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn communication_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCommunication>>;
    // fn communication_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsCommunication>>;
    // fn set_communication_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsCommunication>;


}

impl IsmsCommunicationPlan for crate::IsmsCommunicationPlan {
        fn communication_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsCommunication>> {
        return self.communication_items.as_ref();
    }
}


pub trait IsmsCommunication   {

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn communication_subject<'a>(&'a self) -> &'a str;
    // fn communication_subject_mut(&mut self) -> &mut &'a str;
    // fn set_communication_subject(&mut self, value: String);

    fn communication_purpose<'a>(&'a self) -> Option<&'a str>;
    // fn communication_purpose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_purpose(&mut self, value: Option<&'a str>);

    fn communication_audience<'a>(&'a self) -> Option<&'a str>;
    // fn communication_audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_audience(&mut self, value: Option<&'a str>);

    fn communication_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn communication_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_frequency(&mut self, value: Option<&'a str>);

    fn communication_method<'a>(&'a self) -> Option<&'a str>;
    // fn communication_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_method(&mut self, value: Option<&'a str>);

    fn communication_records_required(&self) -> Option<bool>;
    // fn communication_records_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_communication_records_required(&mut self, value: Option<bool>);


}

impl IsmsCommunication for crate::IsmsCommunication {
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn communication_subject<'a>(&'a self) -> &'a str {
        return &self.communication_subject[..];
    }
        fn communication_purpose<'a>(&'a self) -> Option<&'a str> {
        return self.communication_purpose.as_deref();
    }
        fn communication_audience<'a>(&'a self) -> Option<&'a str> {
        return self.communication_audience.as_deref();
    }
        fn communication_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.communication_frequency.as_deref();
    }
        fn communication_method<'a>(&'a self) -> Option<&'a str> {
        return self.communication_method.as_deref();
    }
        fn communication_records_required(&self) -> Option<bool> {
        return self.communication_records_required;
    }
}


pub trait IsmsDocumentedInformation : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn document_kind<'a>(&'a self) -> &'a crate::IsmsDocumentKind;
    // fn document_kind_mut(&mut self) -> &mut &'a crate::IsmsDocumentKind;
    // fn set_document_kind(&mut self, value: IsmsDocumentKind);


}

impl IsmsDocumentedInformation for crate::IsmsDocumentedInformation {
        fn document_kind<'a>(&'a self) -> &'a crate::IsmsDocumentKind {
        return &self.document_kind;
    }
}


pub trait IsmsOperationalProcedure : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn relevant_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_relevant_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn procedure_scope<'a>(&'a self) -> Option<&'a str>;
    // fn procedure_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_procedure_scope(&mut self, value: Option<&'a str>);

    fn procedure_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn procedure_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_procedure_criteria(&mut self, value: Option<&'a str>);

    fn procedure_control_measures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn procedure_control_measures_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_procedure_control_measures(&mut self, value: Option<&Vec<String>>);

    fn procedure_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn procedure_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_procedure_roles<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn procedure_change_control<'a>(&'a self) -> Option<&'a str>;
    // fn procedure_change_control_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_procedure_change_control(&mut self, value: Option<&'a str>);


}

impl IsmsOperationalProcedure for crate::IsmsOperationalProcedure {
        fn relevant_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.relevant_controls.as_ref();
    }
        fn procedure_scope<'a>(&'a self) -> Option<&'a str> {
        return self.procedure_scope.as_deref();
    }
        fn procedure_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.procedure_criteria.as_deref();
    }
        fn procedure_control_measures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.procedure_control_measures.as_ref();
    }
        fn procedure_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.procedure_roles.as_ref();
    }
        fn procedure_change_control<'a>(&'a self) -> Option<&'a str> {
        return self.procedure_change_control.as_deref();
    }
}


pub trait IsmsMonitoringProgramme : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn monitoring_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsMonitoringItem>>;
    // fn monitoring_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsMonitoringItem>>;
    // fn set_monitoring_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsMonitoringItem>;


}

impl IsmsMonitoringProgramme for crate::IsmsMonitoringProgramme {
        fn monitoring_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsMonitoringItem>> {
        return self.monitoring_items.as_ref();
    }
}


pub trait IsmsMonitoringItem   {

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn monitoring_metric<'a>(&'a self) -> &'a str;
    // fn monitoring_metric_mut(&mut self) -> &mut &'a str;
    // fn set_monitoring_metric(&mut self, value: String);

    fn monitoring_description<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_description(&mut self, value: Option<&'a str>);

    fn monitoring_method<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_method(&mut self, value: Option<&'a str>);

    fn monitoring_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_frequency(&mut self, value: Option<&'a str>);

    fn monitoring_analysis_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_analysis_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_analysis_frequency(&mut self, value: Option<&'a str>);

    fn monitoring_analyst<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_analyst_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_analyst(&mut self, value: Option<&'a str>);

    fn monitoring_target<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_target_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_target(&mut self, value: Option<&'a str>);

    fn monitoring_alert_threshold<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_alert_threshold_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_alert_threshold(&mut self, value: Option<&'a str>);

    fn monitoring_current_value<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_current_value_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_current_value(&mut self, value: Option<&'a str>);

    fn monitoring_trend<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_trend_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_trend(&mut self, value: Option<&'a str>);


}

impl IsmsMonitoringItem for crate::IsmsMonitoringItem {
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn monitoring_metric<'a>(&'a self) -> &'a str {
        return &self.monitoring_metric[..];
    }
        fn monitoring_description<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_description.as_deref();
    }
        fn monitoring_method<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_method.as_deref();
    }
        fn monitoring_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_frequency.as_deref();
    }
        fn monitoring_analysis_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_analysis_frequency.as_deref();
    }
        fn monitoring_analyst<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_analyst.as_deref();
    }
        fn monitoring_target<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_target.as_deref();
    }
        fn monitoring_alert_threshold<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_alert_threshold.as_deref();
    }
        fn monitoring_current_value<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_current_value.as_deref();
    }
        fn monitoring_trend<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_trend.as_deref();
    }
}


pub trait IsmsAuditProgramme : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn programme_period<'a>(&'a self) -> Option<&'a str>;
    // fn programme_period_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_period(&mut self, value: Option<&'a str>);

    fn programme_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn programme_audits_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_programme_audits<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn programme_frequency_rationale<'a>(&'a self) -> Option<&'a str>;
    // fn programme_frequency_rationale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_frequency_rationale(&mut self, value: Option<&'a str>);

    fn programme_resources<'a>(&'a self) -> Option<&'a str>;
    // fn programme_resources_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_resources(&mut self, value: Option<&'a str>);

    fn programme_auditor_qualifications<'a>(&'a self) -> Option<&'a str>;
    // fn programme_auditor_qualifications_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_auditor_qualifications(&mut self, value: Option<&'a str>);

    fn programme_status<'a>(&'a self) -> Option<&'a str>;
    // fn programme_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_status(&mut self, value: Option<&'a str>);


}

impl IsmsAuditProgramme for crate::IsmsAuditProgramme {
        fn programme_period<'a>(&'a self) -> Option<&'a str> {
        return self.programme_period.as_deref();
    }
        fn programme_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.programme_audits.as_ref();
    }
        fn programme_frequency_rationale<'a>(&'a self) -> Option<&'a str> {
        return self.programme_frequency_rationale.as_deref();
    }
        fn programme_resources<'a>(&'a self) -> Option<&'a str> {
        return self.programme_resources.as_deref();
    }
        fn programme_auditor_qualifications<'a>(&'a self) -> Option<&'a str> {
        return self.programme_auditor_qualifications.as_deref();
    }
        fn programme_status<'a>(&'a self) -> Option<&'a str> {
        return self.programme_status.as_deref();
    }
}


pub trait IsmsAudit : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn audit_type<'a>(&'a self) -> &'a crate::IsmsAuditType;
    // fn audit_type_mut(&mut self) -> &mut &'a crate::IsmsAuditType;
    // fn set_audit_type(&mut self, value: IsmsAuditType);

    fn audit_standards<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>>;
    // fn audit_standards_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>>;
    // fn set_audit_standards(&mut self, value: Option<&Vec<IsmsManagementSystemStandard>>);

    fn audit_scope<'a>(&'a self) -> Option<&'a str>;
    // fn audit_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_scope(&mut self, value: Option<&'a str>);

    fn audit_criteria<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_criteria_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_criteria(&mut self, value: Option<&Vec<String>>);

    fn audit_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_objectives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_objectives(&mut self, value: Option<&Vec<String>>);

    fn audit_period_start<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn audit_period_start_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_audit_period_start(&mut self, value: Option<&'a NaiveDate>);

    fn audit_period_end<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn audit_period_end_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_audit_period_end(&mut self, value: Option<&'a NaiveDate>);

    fn audit_lead<'a>(&'a self) -> Option<&'a str>;
    // fn audit_lead_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_lead(&mut self, value: Option<&'a str>);

    fn audit_team<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_team_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_team(&mut self, value: Option<&Vec<String>>);

    fn audit_auditees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_auditees_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_auditees(&mut self, value: Option<&Vec<String>>);

    fn audit_plan<'a>(&'a self) -> Option<&'a str>;
    // fn audit_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_plan<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn audit_findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditFinding>>;
    // fn audit_findings_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditFinding>>;
    // fn set_audit_findings<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IsmsAuditFinding>;

    fn audit_conclusion<'a>(&'a self) -> Option<&'a str>;
    // fn audit_conclusion_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_conclusion(&mut self, value: Option<&'a str>);

    fn audit_report_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn audit_report_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_audit_report_date(&mut self, value: Option<&'a NaiveDate>);

    fn audit_report_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_report_distribution_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_report_distribution(&mut self, value: Option<&Vec<String>>);


}

impl IsmsAudit for crate::IsmsAudit {
        fn audit_type<'a>(&'a self) -> &'a crate::IsmsAuditType {
        return &self.audit_type;
    }
        fn audit_standards<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsManagementSystemStandard>> {
        return self.audit_standards.as_ref();
    }
        fn audit_scope<'a>(&'a self) -> Option<&'a str> {
        return self.audit_scope.as_deref();
    }
        fn audit_criteria<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_criteria.as_ref();
    }
        fn audit_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_objectives.as_ref();
    }
        fn audit_period_start<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.audit_period_start.as_ref();
    }
        fn audit_period_end<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.audit_period_end.as_ref();
    }
        fn audit_lead<'a>(&'a self) -> Option<&'a str> {
        return self.audit_lead.as_deref();
    }
        fn audit_team<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_team.as_ref();
    }
        fn audit_auditees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_auditees.as_ref();
    }
        fn audit_plan<'a>(&'a self) -> Option<&'a str> {
        return self.audit_plan.as_deref();
    }
        fn audit_findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsAuditFinding>> {
        return self.audit_findings.as_ref();
    }
        fn audit_conclusion<'a>(&'a self) -> Option<&'a str> {
        return self.audit_conclusion.as_deref();
    }
        fn audit_report_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.audit_report_date.as_ref();
    }
        fn audit_report_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_report_distribution.as_ref();
    }
}


pub trait IsmsAuditFinding : IsmsRecord   {

    fn finding_type<'a>(&'a self) -> &'a crate::IsmsAuditFindingType;
    // fn finding_type_mut(&mut self) -> &mut &'a crate::IsmsAuditFindingType;
    // fn set_finding_type(&mut self, value: IsmsAuditFindingType);

    fn finding_requirement<'a>(&'a self) -> Option<&'a str>;
    // fn finding_requirement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_requirement(&mut self, value: Option<&'a str>);

    fn finding_control<'a>(&'a self) -> Option<&'a str>;
    // fn finding_control_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_control<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn finding_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn finding_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_evidence(&mut self, value: Option<&'a str>);

    fn finding_root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn finding_root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_root_cause(&mut self, value: Option<&'a str>);

    fn finding_risk<'a>(&'a self) -> Option<&'a str>;
    // fn finding_risk_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_risk(&mut self, value: Option<&'a str>);

    fn finding_recommendation<'a>(&'a self) -> Option<&'a str>;
    // fn finding_recommendation_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_recommendation(&mut self, value: Option<&'a str>);

    fn finding_auditee_response<'a>(&'a self) -> Option<&'a str>;
    // fn finding_auditee_response_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_auditee_response(&mut self, value: Option<&'a str>);

    fn finding_corrective_action<'a>(&'a self) -> Option<&'a str>;
    // fn finding_corrective_action_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_corrective_action<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn finding_closure_status<'a>(&'a self) -> Option<&'a str>;
    // fn finding_closure_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_closure_status(&mut self, value: Option<&'a str>);

    fn finding_closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn finding_closure_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_finding_closure_date(&mut self, value: Option<&'a NaiveDate>);


}

impl IsmsAuditFinding for crate::IsmsAuditFinding {
        fn finding_type<'a>(&'a self) -> &'a crate::IsmsAuditFindingType {
        return &self.finding_type;
    }
        fn finding_requirement<'a>(&'a self) -> Option<&'a str> {
        return self.finding_requirement.as_deref();
    }
        fn finding_control<'a>(&'a self) -> Option<&'a str> {
        return self.finding_control.as_deref();
    }
        fn finding_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.finding_evidence.as_deref();
    }
        fn finding_root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.finding_root_cause.as_deref();
    }
        fn finding_risk<'a>(&'a self) -> Option<&'a str> {
        return self.finding_risk.as_deref();
    }
        fn finding_recommendation<'a>(&'a self) -> Option<&'a str> {
        return self.finding_recommendation.as_deref();
    }
        fn finding_auditee_response<'a>(&'a self) -> Option<&'a str> {
        return self.finding_auditee_response.as_deref();
    }
        fn finding_corrective_action<'a>(&'a self) -> Option<&'a str> {
        return self.finding_corrective_action.as_deref();
    }
        fn finding_closure_status<'a>(&'a self) -> Option<&'a str> {
        return self.finding_closure_status.as_deref();
    }
        fn finding_closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.finding_closure_date.as_ref();
    }
}


pub trait IsmsManagementReview : IsmsRecord  +  IsmsDocumentControlMixin   {

    fn review_held_on<'a>(&'a self) -> &'a crate::NaiveDate;
    // fn review_held_on_mut(&mut self) -> &mut &'a crate::NaiveDate;
    // fn set_review_held_on(&mut self, value: NaiveDate);

    fn review_attendees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn review_attendees_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_review_attendees(&mut self, value: Option<&Vec<String>>);

    fn review_previous_actions<'a>(&'a self) -> Option<&'a str>;
    // fn review_previous_actions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_previous_actions(&mut self, value: Option<&'a str>);

    fn review_context_changes<'a>(&'a self) -> Option<&'a str>;
    // fn review_context_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_context_changes(&mut self, value: Option<&'a str>);

    fn review_interested_party_changes<'a>(&'a self) -> Option<&'a str>;
    // fn review_interested_party_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_interested_party_changes(&mut self, value: Option<&'a str>);

    fn review_interested_party_feedback<'a>(&'a self) -> Option<&'a str>;
    // fn review_interested_party_feedback_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_interested_party_feedback(&mut self, value: Option<&'a str>);

    fn review_performance_trends<'a>(&'a self) -> Option<&'a str>;
    // fn review_performance_trends_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_performance_trends(&mut self, value: Option<&'a str>);

    fn review_audit_results<'a>(&'a self) -> Option<&'a str>;
    // fn review_audit_results_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_audit_results(&mut self, value: Option<&'a str>);

    fn review_risk_assessment_results<'a>(&'a self) -> Option<&'a str>;
    // fn review_risk_assessment_results_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_risk_assessment_results(&mut self, value: Option<&'a str>);

    fn review_risk_treatment_status<'a>(&'a self) -> Option<&'a str>;
    // fn review_risk_treatment_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_risk_treatment_status(&mut self, value: Option<&'a str>);

    fn review_risks_and_opportunities<'a>(&'a self) -> Option<&'a str>;
    // fn review_risks_and_opportunities_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_review_risks_and_opportunities(&mut self, value: Option<&'a str>);

    fn review_improvement_opportunities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn review_improvement_opportunities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_review_improvement_opportunities(&mut self, value: Option<&Vec<String>>);

    fn review_decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn review_decisions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_review_decisions(&mut self, value: Option<&Vec<String>>);

    fn review_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn review_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_review_actions(&mut self, value: Option<&Vec<String>>);

    fn review_next_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn review_next_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_review_next_date(&mut self, value: Option<&'a NaiveDate>);


}

impl IsmsManagementReview for crate::IsmsManagementReview {
        fn review_held_on<'a>(&'a self) -> &'a crate::NaiveDate {
        return &self.review_held_on;
    }
        fn review_attendees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.review_attendees.as_ref();
    }
        fn review_previous_actions<'a>(&'a self) -> Option<&'a str> {
        return self.review_previous_actions.as_deref();
    }
        fn review_context_changes<'a>(&'a self) -> Option<&'a str> {
        return self.review_context_changes.as_deref();
    }
        fn review_interested_party_changes<'a>(&'a self) -> Option<&'a str> {
        return self.review_interested_party_changes.as_deref();
    }
        fn review_interested_party_feedback<'a>(&'a self) -> Option<&'a str> {
        return self.review_interested_party_feedback.as_deref();
    }
        fn review_performance_trends<'a>(&'a self) -> Option<&'a str> {
        return self.review_performance_trends.as_deref();
    }
        fn review_audit_results<'a>(&'a self) -> Option<&'a str> {
        return self.review_audit_results.as_deref();
    }
        fn review_risk_assessment_results<'a>(&'a self) -> Option<&'a str> {
        return self.review_risk_assessment_results.as_deref();
    }
        fn review_risk_treatment_status<'a>(&'a self) -> Option<&'a str> {
        return self.review_risk_treatment_status.as_deref();
    }
        fn review_risks_and_opportunities<'a>(&'a self) -> Option<&'a str> {
        return self.review_risks_and_opportunities.as_deref();
    }
        fn review_improvement_opportunities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.review_improvement_opportunities.as_ref();
    }
        fn review_decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.review_decisions.as_ref();
    }
        fn review_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.review_actions.as_ref();
    }
        fn review_next_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_next_date.as_ref();
    }
}


pub trait IsmsNonconformity : IsmsRecord   {

    fn nonconformity_source<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_source(&mut self, value: Option<&'a str>);

    fn nonconformity_detected_on<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn nonconformity_detected_on_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_nonconformity_detected_on(&mut self, value: Option<&'a NaiveDate>);

    fn nonconformity_detected_by<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_detected_by_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_detected_by(&mut self, value: Option<&'a str>);

    fn nonconformity_requirement<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_requirement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_requirement(&mut self, value: Option<&'a str>);

    fn nonconformity_immediate_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn nonconformity_immediate_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_nonconformity_immediate_actions(&mut self, value: Option<&Vec<String>>);

    fn nonconformity_consequences<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_consequences_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_consequences(&mut self, value: Option<&'a str>);

    fn nonconformity_root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_root_cause(&mut self, value: Option<&'a str>);

    fn nonconformity_similar_check<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_similar_check_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_similar_check(&mut self, value: Option<&'a str>);

    fn nonconformity_status<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_status(&mut self, value: Option<&'a str>);

    fn nonconformity_closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn nonconformity_closure_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_nonconformity_closure_date(&mut self, value: Option<&'a NaiveDate>);

    fn nonconformity_closure_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_closure_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_closure_evidence(&mut self, value: Option<&'a str>);


}

impl IsmsNonconformity for crate::IsmsNonconformity {
        fn nonconformity_source<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_source.as_deref();
    }
        fn nonconformity_detected_on<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.nonconformity_detected_on.as_ref();
    }
        fn nonconformity_detected_by<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_detected_by.as_deref();
    }
        fn nonconformity_requirement<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_requirement.as_deref();
    }
        fn nonconformity_immediate_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nonconformity_immediate_actions.as_ref();
    }
        fn nonconformity_consequences<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_consequences.as_deref();
    }
        fn nonconformity_root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_root_cause.as_deref();
    }
        fn nonconformity_similar_check<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_similar_check.as_deref();
    }
        fn nonconformity_status<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_status.as_deref();
    }
        fn nonconformity_closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.nonconformity_closure_date.as_ref();
    }
        fn nonconformity_closure_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_closure_evidence.as_deref();
    }
}


pub trait IsmsCorrectiveAction : IsmsRecord   {

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn action_nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn action_nonconformities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_action_nonconformities<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn action_root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn action_root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_root_cause(&mut self, value: Option<&'a str>);

    fn action_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn action_target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_action_target_date(&mut self, value: Option<&'a NaiveDate>);

    fn action_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn action_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_action_completion_date(&mut self, value: Option<&'a NaiveDate>);

    fn action_resources<'a>(&'a self) -> Option<&'a str>;
    // fn action_resources_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_resources(&mut self, value: Option<&'a str>);

    fn action_effectiveness_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn action_effectiveness_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_effectiveness_criteria(&mut self, value: Option<&'a str>);

    fn action_effectiveness_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn action_effectiveness_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_action_effectiveness_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn action_effective(&self) -> Option<bool>;
    // fn action_effective_mut(&mut self) -> &mut Option<bool>;
    // fn set_action_effective(&mut self, value: Option<bool>);

    fn action_isms_changes<'a>(&'a self) -> Option<&'a str>;
    // fn action_isms_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_isms_changes(&mut self, value: Option<&'a str>);

    fn action_status<'a>(&'a self) -> Option<&'a str>;
    // fn action_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_status(&mut self, value: Option<&'a str>);


}

impl IsmsCorrectiveAction for crate::IsmsCorrectiveAction {
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn action_nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.action_nonconformities.as_ref();
    }
        fn action_root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.action_root_cause.as_deref();
    }
        fn action_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.action_target_date.as_ref();
    }
        fn action_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.action_completion_date.as_ref();
    }
        fn action_resources<'a>(&'a self) -> Option<&'a str> {
        return self.action_resources.as_deref();
    }
        fn action_effectiveness_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.action_effectiveness_criteria.as_deref();
    }
        fn action_effectiveness_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.action_effectiveness_review_date.as_ref();
    }
        fn action_effective(&self) -> Option<bool> {
        return self.action_effective;
    }
        fn action_isms_changes<'a>(&'a self) -> Option<&'a str> {
        return self.action_isms_changes.as_deref();
    }
        fn action_status<'a>(&'a self) -> Option<&'a str> {
        return self.action_status.as_deref();
    }
}


pub trait IsmsImprovementOpportunity : IsmsRecord   {

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn improvement_source<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_source(&mut self, value: Option<&'a str>);

    fn improvement_identified_on<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn improvement_identified_on_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_improvement_identified_on(&mut self, value: Option<&'a NaiveDate>);

    fn improvement_identified_by<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_identified_by_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_identified_by(&mut self, value: Option<&'a str>);

    fn improvement_benefit<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_benefit_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_benefit(&mut self, value: Option<&'a str>);

    fn improvement_priority<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_priority_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_priority(&mut self, value: Option<&'a str>);

    fn improvement_plan<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_plan(&mut self, value: Option<&'a str>);

    fn improvement_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn improvement_target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_improvement_target_date(&mut self, value: Option<&'a NaiveDate>);

    fn improvement_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn improvement_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_improvement_completion_date(&mut self, value: Option<&'a NaiveDate>);

    fn improvement_outcome<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_outcome_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_outcome(&mut self, value: Option<&'a str>);

    fn improvement_status<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_status(&mut self, value: Option<&'a str>);


}

impl IsmsImprovementOpportunity for crate::IsmsImprovementOpportunity {
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn improvement_source<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_source.as_deref();
    }
        fn improvement_identified_on<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.improvement_identified_on.as_ref();
    }
        fn improvement_identified_by<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_identified_by.as_deref();
    }
        fn improvement_benefit<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_benefit.as_deref();
    }
        fn improvement_priority<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_priority.as_deref();
    }
        fn improvement_plan<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_plan.as_deref();
    }
        fn improvement_target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.improvement_target_date.as_ref();
    }
        fn improvement_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.improvement_completion_date.as_ref();
    }
        fn improvement_outcome<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_outcome.as_deref();
    }
        fn improvement_status<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_status.as_deref();
    }
}


pub trait IsmsSecurityEvent : IsmsRecord   {

    fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn affected_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_affected_assets<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn event_type<'a>(&'a self) -> Option<&'a str>;
    // fn event_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_event_type(&mut self, value: Option<&'a str>);

    fn event_occurred_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime>;
    // fn event_occurred_at_mut(&mut self) -> &mut Option<&'a crate::NaiveDateTime>;
    // fn set_event_occurred_at(&mut self, value: Option<&'a NaiveDateTime>);

    fn event_reporter<'a>(&'a self) -> Option<&'a str>;
    // fn event_reporter_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_event_reporter(&mut self, value: Option<&'a str>);

    fn event_assessment<'a>(&'a self) -> Option<&'a str>;
    // fn event_assessment_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_event_assessment(&mut self, value: Option<&'a str>);


}

impl IsmsSecurityEvent for crate::IsmsSecurityEvent {
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn event_type<'a>(&'a self) -> Option<&'a str> {
        return self.event_type.as_deref();
    }
        fn event_occurred_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.event_occurred_at.as_ref();
    }
        fn event_reporter<'a>(&'a self) -> Option<&'a str> {
        return self.event_reporter.as_deref();
    }
        fn event_assessment<'a>(&'a self) -> Option<&'a str> {
        return self.event_assessment.as_deref();
    }
}
impl IsmsSecurityEvent for crate::IsmsSecurityIncident {
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn event_type<'a>(&'a self) -> Option<&'a str> {
        return self.event_type.as_deref();
    }
        fn event_occurred_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.event_occurred_at.as_ref();
    }
        fn event_reporter<'a>(&'a self) -> Option<&'a str> {
        return self.event_reporter.as_deref();
    }
        fn event_assessment<'a>(&'a self) -> Option<&'a str> {
        return self.event_assessment.as_deref();
    }
}

impl IsmsSecurityEvent for crate::IsmsSecurityEventOrSubtype {
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.affected_assets().map(|x| x.to_any()),

        }
    }
        fn event_type<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.event_type(),

        }
    }
        fn event_occurred_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.event_occurred_at(),

        }
    }
        fn event_reporter<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.event_reporter(),

        }
    }
        fn event_assessment<'a>(&'a self) -> Option<&'a str> {
        match self {
                IsmsSecurityEventOrSubtype::IsmsSecurityIncident(val) => val.event_assessment(),

        }
    }
}

pub trait IsmsSecurityIncident : IsmsSecurityEvent   {

    fn affected_security_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>>;
    // fn affected_security_properties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>>;
    // fn set_affected_security_properties(&mut self, value: Option<&Vec<IsmsSecurityProperty>>);

    fn incident_category<'a>(&'a self) -> Option<&'a crate::IsmsIncidentCategory>;
    // fn incident_category_mut(&mut self) -> &mut Option<&'a crate::IsmsIncidentCategory>;
    // fn set_incident_category(&mut self, value: Option<&'a IsmsIncidentCategory>);

    fn incident_severity<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel>;
    // fn incident_severity_mut(&mut self) -> &mut Option<&'a crate::IsmsRiskLevel>;
    // fn set_incident_severity(&mut self, value: Option<&'a IsmsRiskLevel>);

    fn incident_detection_method<'a>(&'a self) -> Option<&'a str>;
    // fn incident_detection_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_incident_detection_method(&mut self, value: Option<&'a str>);

    fn incident_response_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_response_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_response_actions(&mut self, value: Option<&Vec<String>>);

    fn incident_containment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_containment_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_containment_actions(&mut self, value: Option<&Vec<String>>);

    fn incident_eradication_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_eradication_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_eradication_actions(&mut self, value: Option<&Vec<String>>);

    fn incident_recovery_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_recovery_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_recovery_actions(&mut self, value: Option<&Vec<String>>);

    fn incident_root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn incident_root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_incident_root_cause(&mut self, value: Option<&'a str>);

    fn incident_lessons_learned<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_lessons_learned_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_lessons_learned(&mut self, value: Option<&Vec<String>>);

    fn incident_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_evidence_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_evidence(&mut self, value: Option<&Vec<String>>);

    fn incident_notification_required(&self) -> Option<bool>;
    // fn incident_notification_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_incident_notification_required(&mut self, value: Option<bool>);

    fn incident_notifications<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn incident_notifications_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_incident_notifications(&mut self, value: Option<&Vec<String>>);

    fn incident_closed_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime>;
    // fn incident_closed_at_mut(&mut self) -> &mut Option<&'a crate::NaiveDateTime>;
    // fn set_incident_closed_at(&mut self, value: Option<&'a NaiveDateTime>);

    fn incident_review<'a>(&'a self) -> Option<&'a str>;
    // fn incident_review_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_incident_review(&mut self, value: Option<&'a str>);


}

impl IsmsSecurityIncident for crate::IsmsSecurityIncident {
        fn affected_security_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IsmsSecurityProperty>> {
        return self.affected_security_properties.as_ref();
    }
        fn incident_category<'a>(&'a self) -> Option<&'a crate::IsmsIncidentCategory> {
        return self.incident_category.as_ref();
    }
        fn incident_severity<'a>(&'a self) -> Option<&'a crate::IsmsRiskLevel> {
        return self.incident_severity.as_ref();
    }
        fn incident_detection_method<'a>(&'a self) -> Option<&'a str> {
        return self.incident_detection_method.as_deref();
    }
        fn incident_response_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_response_actions.as_ref();
    }
        fn incident_containment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_containment_actions.as_ref();
    }
        fn incident_eradication_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_eradication_actions.as_ref();
    }
        fn incident_recovery_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_recovery_actions.as_ref();
    }
        fn incident_root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.incident_root_cause.as_deref();
    }
        fn incident_lessons_learned<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_lessons_learned.as_ref();
    }
        fn incident_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_evidence.as_ref();
    }
        fn incident_notification_required(&self) -> Option<bool> {
        return self.incident_notification_required;
    }
        fn incident_notifications<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.incident_notifications.as_ref();
    }
        fn incident_closed_at<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.incident_closed_at.as_ref();
    }
        fn incident_review<'a>(&'a self) -> Option<&'a str> {
        return self.incident_review.as_deref();
    }
}
