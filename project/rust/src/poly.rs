#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait NamedEntity   {

    fn id<'a>(&'a self) -> &'a crate::uriorcurie;
    // fn id_mut(&mut self) -> &mut &'a crate::uriorcurie;
    // fn set_id(&mut self, value: uriorcurie);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn created_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_created_date(&mut self, value: Option<&'a NaiveDate>);

    fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn modified_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_modified_date(&mut self, value: Option<&'a NaiveDate>);

    fn version<'a>(&'a self) -> Option<&'a str>;
    // fn version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_version(&mut self, value: Option<&'a str>);


}

impl NamedEntity for crate::NamedEntity {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::DocumentedInformation {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InformationSecurityManagementSystem {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Organization {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InterestedParty {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Role {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InformationSecurityObjective {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Risk {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::SecurityControl {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Resource {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::AuditFinding {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Nonconformity {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::CorrectiveAction {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::ImprovementOpportunity {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::Asset {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InformationSecurityEvent {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InformationSecurityIncident {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InformationSecurityPolicy {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::TopicSpecificPolicy {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::RiskAssessmentProcess {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::RiskAssessment {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::RiskTreatmentProcess {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::RiskTreatmentPlan {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::StatementOfApplicability {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::CompetenceRecord {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::AwarenessProgram {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::CommunicationPlan {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::OperationalProcedure {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::MonitoringProgram {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::InternalAudit {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::AuditProgramme {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}
impl NamedEntity for crate::ManagementReview {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.created_date.as_ref();
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.modified_date.as_ref();
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
}

impl NamedEntity for crate::NamedEntityOrSubtype {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.id(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.id(),
                NamedEntityOrSubtype::Organization(val) => val.id(),
                NamedEntityOrSubtype::InterestedParty(val) => val.id(),
                NamedEntityOrSubtype::Role(val) => val.id(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.id(),
                NamedEntityOrSubtype::Risk(val) => val.id(),
                NamedEntityOrSubtype::SecurityControl(val) => val.id(),
                NamedEntityOrSubtype::Resource(val) => val.id(),
                NamedEntityOrSubtype::AuditFinding(val) => val.id(),
                NamedEntityOrSubtype::Nonconformity(val) => val.id(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.id(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.id(),
                NamedEntityOrSubtype::Asset(val) => val.id(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.id(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.id(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.id(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.id(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.id(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.id(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.id(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.id(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.id(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.id(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.id(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.id(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.id(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.id(),
                NamedEntityOrSubtype::InternalAudit(val) => val.id(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.id(),
                NamedEntityOrSubtype::ManagementReview(val) => val.id(),

        }
    }
        fn name<'a>(&'a self) -> &'a str {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.name(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.name(),
                NamedEntityOrSubtype::Organization(val) => val.name(),
                NamedEntityOrSubtype::InterestedParty(val) => val.name(),
                NamedEntityOrSubtype::Role(val) => val.name(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.name(),
                NamedEntityOrSubtype::Risk(val) => val.name(),
                NamedEntityOrSubtype::SecurityControl(val) => val.name(),
                NamedEntityOrSubtype::Resource(val) => val.name(),
                NamedEntityOrSubtype::AuditFinding(val) => val.name(),
                NamedEntityOrSubtype::Nonconformity(val) => val.name(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.name(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.name(),
                NamedEntityOrSubtype::Asset(val) => val.name(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.name(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.name(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.name(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.name(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.name(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.name(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.name(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.name(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.name(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.name(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.name(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.name(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.name(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.name(),
                NamedEntityOrSubtype::InternalAudit(val) => val.name(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.name(),
                NamedEntityOrSubtype::ManagementReview(val) => val.name(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.description(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.description(),
                NamedEntityOrSubtype::Organization(val) => val.description(),
                NamedEntityOrSubtype::InterestedParty(val) => val.description(),
                NamedEntityOrSubtype::Role(val) => val.description(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.description(),
                NamedEntityOrSubtype::Risk(val) => val.description(),
                NamedEntityOrSubtype::SecurityControl(val) => val.description(),
                NamedEntityOrSubtype::Resource(val) => val.description(),
                NamedEntityOrSubtype::AuditFinding(val) => val.description(),
                NamedEntityOrSubtype::Nonconformity(val) => val.description(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.description(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.description(),
                NamedEntityOrSubtype::Asset(val) => val.description(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.description(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.description(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.description(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.description(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.description(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.description(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.description(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.description(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.description(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.description(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.description(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.description(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.description(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.description(),
                NamedEntityOrSubtype::InternalAudit(val) => val.description(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.description(),
                NamedEntityOrSubtype::ManagementReview(val) => val.description(),

        }
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.created_date(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.created_date(),
                NamedEntityOrSubtype::Organization(val) => val.created_date(),
                NamedEntityOrSubtype::InterestedParty(val) => val.created_date(),
                NamedEntityOrSubtype::Role(val) => val.created_date(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.created_date(),
                NamedEntityOrSubtype::Risk(val) => val.created_date(),
                NamedEntityOrSubtype::SecurityControl(val) => val.created_date(),
                NamedEntityOrSubtype::Resource(val) => val.created_date(),
                NamedEntityOrSubtype::AuditFinding(val) => val.created_date(),
                NamedEntityOrSubtype::Nonconformity(val) => val.created_date(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.created_date(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.created_date(),
                NamedEntityOrSubtype::Asset(val) => val.created_date(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.created_date(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.created_date(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.created_date(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.created_date(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.created_date(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.created_date(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.created_date(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.created_date(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.created_date(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.created_date(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.created_date(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.created_date(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.created_date(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.created_date(),
                NamedEntityOrSubtype::InternalAudit(val) => val.created_date(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.created_date(),
                NamedEntityOrSubtype::ManagementReview(val) => val.created_date(),

        }
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.modified_date(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.modified_date(),
                NamedEntityOrSubtype::Organization(val) => val.modified_date(),
                NamedEntityOrSubtype::InterestedParty(val) => val.modified_date(),
                NamedEntityOrSubtype::Role(val) => val.modified_date(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.modified_date(),
                NamedEntityOrSubtype::Risk(val) => val.modified_date(),
                NamedEntityOrSubtype::SecurityControl(val) => val.modified_date(),
                NamedEntityOrSubtype::Resource(val) => val.modified_date(),
                NamedEntityOrSubtype::AuditFinding(val) => val.modified_date(),
                NamedEntityOrSubtype::Nonconformity(val) => val.modified_date(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.modified_date(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.modified_date(),
                NamedEntityOrSubtype::Asset(val) => val.modified_date(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.modified_date(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.modified_date(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.modified_date(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.modified_date(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.modified_date(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.modified_date(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.modified_date(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.modified_date(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.modified_date(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.modified_date(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.modified_date(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.modified_date(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.modified_date(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.modified_date(),
                NamedEntityOrSubtype::InternalAudit(val) => val.modified_date(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.modified_date(),
                NamedEntityOrSubtype::ManagementReview(val) => val.modified_date(),

        }
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        match self {
                NamedEntityOrSubtype::DocumentedInformation(val) => val.version(),
                NamedEntityOrSubtype::InformationSecurityManagementSystem(val) => val.version(),
                NamedEntityOrSubtype::Organization(val) => val.version(),
                NamedEntityOrSubtype::InterestedParty(val) => val.version(),
                NamedEntityOrSubtype::Role(val) => val.version(),
                NamedEntityOrSubtype::InformationSecurityObjective(val) => val.version(),
                NamedEntityOrSubtype::Risk(val) => val.version(),
                NamedEntityOrSubtype::SecurityControl(val) => val.version(),
                NamedEntityOrSubtype::Resource(val) => val.version(),
                NamedEntityOrSubtype::AuditFinding(val) => val.version(),
                NamedEntityOrSubtype::Nonconformity(val) => val.version(),
                NamedEntityOrSubtype::CorrectiveAction(val) => val.version(),
                NamedEntityOrSubtype::ImprovementOpportunity(val) => val.version(),
                NamedEntityOrSubtype::Asset(val) => val.version(),
                NamedEntityOrSubtype::InformationSecurityEvent(val) => val.version(),
                NamedEntityOrSubtype::InformationSecurityIncident(val) => val.version(),
                NamedEntityOrSubtype::InformationSecurityPolicy(val) => val.version(),
                NamedEntityOrSubtype::TopicSpecificPolicy(val) => val.version(),
                NamedEntityOrSubtype::RiskAssessmentProcess(val) => val.version(),
                NamedEntityOrSubtype::RiskAssessment(val) => val.version(),
                NamedEntityOrSubtype::RiskTreatmentProcess(val) => val.version(),
                NamedEntityOrSubtype::RiskTreatmentPlan(val) => val.version(),
                NamedEntityOrSubtype::StatementOfApplicability(val) => val.version(),
                NamedEntityOrSubtype::CompetenceRecord(val) => val.version(),
                NamedEntityOrSubtype::AwarenessProgram(val) => val.version(),
                NamedEntityOrSubtype::CommunicationPlan(val) => val.version(),
                NamedEntityOrSubtype::OperationalProcedure(val) => val.version(),
                NamedEntityOrSubtype::MonitoringProgram(val) => val.version(),
                NamedEntityOrSubtype::InternalAudit(val) => val.version(),
                NamedEntityOrSubtype::AuditProgramme(val) => val.version(),
                NamedEntityOrSubtype::ManagementReview(val) => val.version(),

        }
    }
}
impl NamedEntity for crate::DocumentedInformationOrSubtype {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.id(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.id(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.id(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.id(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.id(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.id(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.id(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.id(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.id(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.id(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.id(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.id(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.id(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.id(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.id(),

        }
    }
        fn name<'a>(&'a self) -> &'a str {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.name(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.name(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.name(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.name(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.name(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.name(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.name(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.name(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.name(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.name(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.name(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.name(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.name(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.name(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.name(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.description(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.description(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.description(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.description(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.description(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.description(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.description(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.description(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.description(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.description(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.description(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.description(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.description(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.description(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.description(),

        }
    }
        fn created_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.created_date(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.created_date(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.created_date(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.created_date(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.created_date(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.created_date(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.created_date(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.created_date(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.created_date(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.created_date(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.created_date(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.created_date(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.created_date(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.created_date(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.created_date(),

        }
    }
        fn modified_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.modified_date(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.modified_date(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.modified_date(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.modified_date(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.modified_date(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.modified_date(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.modified_date(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.modified_date(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.modified_date(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.modified_date(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.modified_date(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.modified_date(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.modified_date(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.modified_date(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.modified_date(),

        }
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.version(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.version(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.version(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.version(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.version(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.version(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.version(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.version(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.version(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.version(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.version(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.version(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.version(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.version(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.version(),

        }
    }
}

pub trait DocumentedInformation : NamedEntity   {

    fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType>;
    // fn document_type_mut(&mut self) -> &mut Option<&'a crate::DocumentType>;
    // fn set_document_type(&mut self, value: Option<&'a DocumentType>);

    fn document_reference<'a>(&'a self) -> Option<&'a str>;
    // fn document_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_document_reference(&mut self, value: Option<&'a str>);

    fn author<'a>(&'a self) -> Option<&'a str>;
    // fn author_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_author(&mut self, value: Option<&'a str>);

    fn owner<'a>(&'a self) -> Option<&'a str>;
    // fn owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_owner(&mut self, value: Option<&'a str>);

    fn approved_by<'a>(&'a self) -> Option<&'a str>;
    // fn approved_by_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_approved_by(&mut self, value: Option<&'a str>);

    fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn approved_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_approved_date(&mut self, value: Option<&'a NaiveDate>);

    fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn effective_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_effective_date(&mut self, value: Option<&'a NaiveDate>);

    fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn status<'a>(&'a self) -> Option<&'a str>;
    // fn status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_status(&mut self, value: Option<&'a str>);

    fn classification<'a>(&'a self) -> Option<&'a str>;
    // fn classification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_classification(&mut self, value: Option<&'a str>);

    fn retention_period<'a>(&'a self) -> Option<&'a str>;
    // fn retention_period_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_retention_period(&mut self, value: Option<&'a str>);

    fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn distribution_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_distribution_controls(&mut self, value: Option<&Vec<String>>);

    fn storage_and_preservation<'a>(&'a self) -> Option<&'a str>;
    // fn storage_and_preservation_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_storage_and_preservation(&mut self, value: Option<&'a str>);

    fn change_control_method<'a>(&'a self) -> Option<&'a str>;
    // fn change_control_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_change_control_method(&mut self, value: Option<&'a str>);

    fn external_origin(&self) -> Option<bool>;
    // fn external_origin_mut(&mut self) -> &mut Option<bool>;
    // fn set_external_origin(&mut self, value: Option<bool>);

    fn external_origin_source<'a>(&'a self) -> Option<&'a str>;
    // fn external_origin_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_external_origin_source(&mut self, value: Option<&'a str>);


}

impl DocumentedInformation for crate::DocumentedInformation {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::InformationSecurityPolicy {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::TopicSpecificPolicy {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::RiskAssessmentProcess {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::RiskAssessment {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::RiskTreatmentProcess {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::RiskTreatmentPlan {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::StatementOfApplicability {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::CompetenceRecord {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::AwarenessProgram {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::CommunicationPlan {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::OperationalProcedure {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::MonitoringProgram {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::InternalAudit {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::AuditProgramme {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}
impl DocumentedInformation for crate::ManagementReview {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        return self.document_type.as_ref();
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        return self.document_reference.as_deref();
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        return self.author.as_deref();
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        return self.owner.as_deref();
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        return self.approved_by.as_deref();
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.approved_date.as_ref();
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effective_date.as_ref();
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.review_date.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        return self.retention_period.as_deref();
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.distribution_controls.as_ref();
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        return self.storage_and_preservation.as_deref();
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_method.as_deref();
    }
        fn external_origin(&self) -> Option<bool> {
        return self.external_origin;
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        return self.external_origin_source.as_deref();
    }
}

impl DocumentedInformation for crate::DocumentedInformationOrSubtype {
        fn document_type<'a>(&'a self) -> Option<&'a crate::DocumentType> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.document_type(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.document_type(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.document_type(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.document_type(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.document_type(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.document_type(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.document_type(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.document_type(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.document_type(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.document_type(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.document_type(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.document_type(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.document_type(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.document_type(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.document_type(),

        }
    }
        fn document_reference<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.document_reference(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.document_reference(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.document_reference(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.document_reference(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.document_reference(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.document_reference(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.document_reference(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.document_reference(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.document_reference(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.document_reference(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.document_reference(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.document_reference(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.document_reference(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.document_reference(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.document_reference(),

        }
    }
        fn author<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.author(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.author(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.author(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.author(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.author(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.author(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.author(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.author(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.author(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.author(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.author(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.author(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.author(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.author(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.author(),

        }
    }
        fn owner<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.owner(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.owner(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.owner(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.owner(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.owner(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.owner(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.owner(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.owner(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.owner(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.owner(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.owner(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.owner(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.owner(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.owner(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.owner(),

        }
    }
        fn approved_by<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.approved_by(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.approved_by(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.approved_by(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.approved_by(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.approved_by(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.approved_by(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.approved_by(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.approved_by(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.approved_by(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.approved_by(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.approved_by(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.approved_by(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.approved_by(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.approved_by(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.approved_by(),

        }
    }
        fn approved_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.approved_date(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.approved_date(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.approved_date(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.approved_date(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.approved_date(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.approved_date(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.approved_date(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.approved_date(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.approved_date(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.approved_date(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.approved_date(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.approved_date(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.approved_date(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.approved_date(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.approved_date(),

        }
    }
        fn effective_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.effective_date(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.effective_date(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.effective_date(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.effective_date(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.effective_date(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.effective_date(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.effective_date(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.effective_date(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.effective_date(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.effective_date(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.effective_date(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.effective_date(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.effective_date(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.effective_date(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.effective_date(),

        }
    }
        fn review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.review_date(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.review_date(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.review_date(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.review_date(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.review_date(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.review_date(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.review_date(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.review_date(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.review_date(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.review_date(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.review_date(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.review_date(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.review_date(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.review_date(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.review_date(),

        }
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.status(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.status(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.status(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.status(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.status(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.status(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.status(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.status(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.status(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.status(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.status(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.status(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.status(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.status(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.status(),

        }
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.classification(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.classification(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.classification(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.classification(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.classification(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.classification(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.classification(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.classification(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.classification(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.classification(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.classification(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.classification(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.classification(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.classification(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.classification(),

        }
    }
        fn retention_period<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.retention_period(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.retention_period(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.retention_period(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.retention_period(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.retention_period(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.retention_period(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.retention_period(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.retention_period(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.retention_period(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.retention_period(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.retention_period(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.retention_period(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.retention_period(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.retention_period(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.retention_period(),

        }
    }
        fn distribution_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.distribution_controls().map(|x| x.to_any()),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.distribution_controls().map(|x| x.to_any()),

        }
    }
        fn storage_and_preservation<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.storage_and_preservation(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.storage_and_preservation(),

        }
    }
        fn change_control_method<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.change_control_method(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.change_control_method(),

        }
    }
        fn external_origin(&self) -> Option<bool> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.external_origin(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.external_origin(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.external_origin(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.external_origin(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.external_origin(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.external_origin(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.external_origin(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.external_origin(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.external_origin(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.external_origin(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.external_origin(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.external_origin(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.external_origin(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.external_origin(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.external_origin(),

        }
    }
        fn external_origin_source<'a>(&'a self) -> Option<&'a str> {
        match self {
                DocumentedInformationOrSubtype::InformationSecurityPolicy(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::TopicSpecificPolicy(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::RiskAssessmentProcess(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::RiskAssessment(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::RiskTreatmentProcess(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::RiskTreatmentPlan(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::StatementOfApplicability(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::CompetenceRecord(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::AwarenessProgram(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::CommunicationPlan(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::OperationalProcedure(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::MonitoringProgram(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::InternalAudit(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::AuditProgramme(val) => val.external_origin_source(),
                DocumentedInformationOrSubtype::ManagementReview(val) => val.external_origin_source(),

        }
    }
}

pub trait InformationSecurityManagementSystem : NamedEntity   {

    fn organization<'a>(&'a self) -> Option<&'a str>;
    // fn organization_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn top_management<'a>(&'a self) -> Option<&'a str>;
    // fn top_management_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_top_management(&mut self, value: Option<&'a str>);

    fn governing_body<'a>(&'a self) -> Option<&'a str>;
    // fn governing_body_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_governing_body(&mut self, value: Option<&'a str>);

    fn leadership_commitment_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn leadership_commitment_evidence_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_leadership_commitment_evidence(&mut self, value: Option<&Vec<String>>);

    fn scope_statement<'a>(&'a self) -> Option<&'a str>;
    // fn scope_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_scope_statement(&mut self, value: Option<&'a str>);

    fn scope_boundaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn scope_boundaries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_scope_boundaries(&mut self, value: Option<&Vec<String>>);

    fn scope_exclusions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn scope_exclusions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_scope_exclusions(&mut self, value: Option<&Vec<String>>);

    fn interfaces_and_dependencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn interfaces_and_dependencies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_interfaces_and_dependencies(&mut self, value: Option<&Vec<String>>);

    fn processes_and_interactions<'a>(&'a self) -> Option<&'a str>;
    // fn processes_and_interactions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_processes_and_interactions(&mut self, value: Option<&'a str>);

    fn context_internal_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn context_internal_issues_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_context_internal_issues(&mut self, value: Option<&Vec<String>>);

    fn context_external_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn context_external_issues_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_context_external_issues(&mut self, value: Option<&Vec<String>>);

    fn interested_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn interested_parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_interested_parties<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn information_security_policy<'a>(&'a self) -> Option<&'a str>;
    // fn information_security_policy_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_information_security_policy<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn objectives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_objectives<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn risks_and_opportunities_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risks_and_opportunities_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risks_and_opportunities_actions(&mut self, value: Option<&Vec<String>>);

    fn planned_changes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn planned_changes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_planned_changes(&mut self, value: Option<&Vec<String>>);

    fn externally_provided_services<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn externally_provided_services_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_externally_provided_services(&mut self, value: Option<&Vec<String>>);

    fn risk_assessment_process<'a>(&'a self) -> Option<&'a str>;
    // fn risk_assessment_process_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_assessment_process<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn risk_treatment_process<'a>(&'a self) -> Option<&'a str>;
    // fn risk_treatment_process_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_treatment_process<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn statement_of_applicability<'a>(&'a self) -> Option<&'a str>;
    // fn statement_of_applicability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_statement_of_applicability<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_roles<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn resources_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_resources<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn competence_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competence_records_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competence_records<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn awareness_program<'a>(&'a self) -> Option<&'a str>;
    // fn awareness_program_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_awareness_program<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn communication_plan<'a>(&'a self) -> Option<&'a str>;
    // fn communication_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_plan<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn documented_information_register<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn documented_information_register_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_documented_information_register<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn operational_procedures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn operational_procedures_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_operational_procedures<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn risk_assessments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risk_assessments_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risk_assessments<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn risk_treatment_plans<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risk_treatment_plans_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risk_treatment_plans<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn monitoring_program<'a>(&'a self) -> Option<&'a str>;
    // fn monitoring_program_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_monitoring_program<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn internal_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn internal_audits_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_internal_audits<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn management_reviews<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn management_reviews_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_management_reviews<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn nonconformities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_nonconformities<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn corrective_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_corrective_actions<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn improvements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn improvements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_improvements<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn certification_status<'a>(&'a self) -> Option<&'a str>;
    // fn certification_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_certification_status(&mut self, value: Option<&'a str>);

    fn certification_body<'a>(&'a self) -> Option<&'a str>;
    // fn certification_body_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_certification_body(&mut self, value: Option<&'a str>);

    fn certification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn certification_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_certification_date(&mut self, value: Option<&'a NaiveDate>);

    fn recertification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn recertification_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_recertification_date(&mut self, value: Option<&'a NaiveDate>);


}

impl InformationSecurityManagementSystem for crate::InformationSecurityManagementSystem {
        fn organization<'a>(&'a self) -> Option<&'a str> {
        return self.organization.as_deref();
    }
        fn top_management<'a>(&'a self) -> Option<&'a str> {
        return self.top_management.as_deref();
    }
        fn governing_body<'a>(&'a self) -> Option<&'a str> {
        return self.governing_body.as_deref();
    }
        fn leadership_commitment_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.leadership_commitment_evidence.as_ref();
    }
        fn scope_statement<'a>(&'a self) -> Option<&'a str> {
        return self.scope_statement.as_deref();
    }
        fn scope_boundaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.scope_boundaries.as_ref();
    }
        fn scope_exclusions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.scope_exclusions.as_ref();
    }
        fn interfaces_and_dependencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.interfaces_and_dependencies.as_ref();
    }
        fn processes_and_interactions<'a>(&'a self) -> Option<&'a str> {
        return self.processes_and_interactions.as_deref();
    }
        fn context_internal_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.context_internal_issues.as_ref();
    }
        fn context_external_issues<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.context_external_issues.as_ref();
    }
        fn interested_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.interested_parties.as_ref();
    }
        fn information_security_policy<'a>(&'a self) -> Option<&'a str> {
        return self.information_security_policy.as_deref();
    }
        fn objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.objectives.as_ref();
    }
        fn risks_and_opportunities_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risks_and_opportunities_actions.as_ref();
    }
        fn planned_changes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.planned_changes.as_ref();
    }
        fn externally_provided_services<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.externally_provided_services.as_ref();
    }
        fn risk_assessment_process<'a>(&'a self) -> Option<&'a str> {
        return self.risk_assessment_process.as_deref();
    }
        fn risk_treatment_process<'a>(&'a self) -> Option<&'a str> {
        return self.risk_treatment_process.as_deref();
    }
        fn statement_of_applicability<'a>(&'a self) -> Option<&'a str> {
        return self.statement_of_applicability.as_deref();
    }
        fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.controls.as_ref();
    }
        fn roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.roles.as_ref();
    }
        fn resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.resources.as_ref();
    }
        fn competence_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competence_records.as_ref();
    }
        fn awareness_program<'a>(&'a self) -> Option<&'a str> {
        return self.awareness_program.as_deref();
    }
        fn communication_plan<'a>(&'a self) -> Option<&'a str> {
        return self.communication_plan.as_deref();
    }
        fn documented_information_register<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.documented_information_register.as_ref();
    }
        fn operational_procedures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.operational_procedures.as_ref();
    }
        fn risk_assessments<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risk_assessments.as_ref();
    }
        fn risk_treatment_plans<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risk_treatment_plans.as_ref();
    }
        fn monitoring_program<'a>(&'a self) -> Option<&'a str> {
        return self.monitoring_program.as_deref();
    }
        fn internal_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.internal_audits.as_ref();
    }
        fn management_reviews<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.management_reviews.as_ref();
    }
        fn nonconformities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nonconformities.as_ref();
    }
        fn corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.corrective_actions.as_ref();
    }
        fn improvements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.improvements.as_ref();
    }
        fn certification_status<'a>(&'a self) -> Option<&'a str> {
        return self.certification_status.as_deref();
    }
        fn certification_body<'a>(&'a self) -> Option<&'a str> {
        return self.certification_body.as_deref();
    }
        fn certification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.certification_date.as_ref();
    }
        fn recertification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.recertification_date.as_ref();
    }
}


pub trait Organization : NamedEntity   {

    fn legal_name<'a>(&'a self) -> Option<&'a str>;
    // fn legal_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_legal_name(&mut self, value: Option<&'a str>);

    fn trading_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn trading_names_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_trading_names(&mut self, value: Option<&Vec<String>>);

    fn organization_type<'a>(&'a self) -> Option<&'a str>;
    // fn organization_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_organization_type(&mut self, value: Option<&'a str>);

    fn industry_sector<'a>(&'a self) -> Option<&'a str>;
    // fn industry_sector_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_industry_sector(&mut self, value: Option<&'a str>);

    fn size_category<'a>(&'a self) -> Option<&'a str>;
    // fn size_category_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_size_category(&mut self, value: Option<&'a str>);

    fn employee_count(&self) -> Option<isize>;
    // fn employee_count_mut(&mut self) -> &mut Option<isize>;
    // fn set_employee_count(&mut self, value: Option<isize>);

    fn geographic_locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn geographic_locations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_geographic_locations(&mut self, value: Option<&Vec<String>>);

    fn regulatory_jurisdictions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn regulatory_jurisdictions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_regulatory_jurisdictions(&mut self, value: Option<&Vec<String>>);

    fn parent_organization<'a>(&'a self) -> Option<&'a str>;
    // fn parent_organization_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_parent_organization(&mut self, value: Option<&'a str>);

    fn subsidiaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn subsidiaries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_subsidiaries(&mut self, value: Option<&Vec<String>>);

    fn climate_change_relevant(&self) -> Option<bool>;
    // fn climate_change_relevant_mut(&mut self) -> &mut Option<bool>;
    // fn set_climate_change_relevant(&mut self, value: Option<bool>);


}

impl Organization for crate::Organization {
        fn legal_name<'a>(&'a self) -> Option<&'a str> {
        return self.legal_name.as_deref();
    }
        fn trading_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.trading_names.as_ref();
    }
        fn organization_type<'a>(&'a self) -> Option<&'a str> {
        return self.organization_type.as_deref();
    }
        fn industry_sector<'a>(&'a self) -> Option<&'a str> {
        return self.industry_sector.as_deref();
    }
        fn size_category<'a>(&'a self) -> Option<&'a str> {
        return self.size_category.as_deref();
    }
        fn employee_count(&self) -> Option<isize> {
        return self.employee_count;
    }
        fn geographic_locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.geographic_locations.as_ref();
    }
        fn regulatory_jurisdictions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.regulatory_jurisdictions.as_ref();
    }
        fn parent_organization<'a>(&'a self) -> Option<&'a str> {
        return self.parent_organization.as_deref();
    }
        fn subsidiaries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.subsidiaries.as_ref();
    }
        fn climate_change_relevant(&self) -> Option<bool> {
        return self.climate_change_relevant;
    }
}


pub trait InterestedParty : NamedEntity   {

    fn party_type<'a>(&'a self) -> Option<&'a str>;
    // fn party_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_party_type(&mut self, value: Option<&'a str>);

    fn relationship<'a>(&'a self) -> Option<&'a str>;
    // fn relationship_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_relationship(&mut self, value: Option<&'a str>);

    fn requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_requirements(&mut self, value: Option<&Vec<String>>);

    fn addressed_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn addressed_requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_addressed_requirements(&mut self, value: Option<&Vec<String>>);

    fn climate_change_related_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn climate_change_related_requirements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_climate_change_related_requirements(&mut self, value: Option<&Vec<String>>);

    fn communication_needs<'a>(&'a self) -> Option<&'a str>;
    // fn communication_needs_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_communication_needs(&mut self, value: Option<&'a str>);

    fn contact_information<'a>(&'a self) -> Option<&'a str>;
    // fn contact_information_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_contact_information(&mut self, value: Option<&'a str>);


}

impl InterestedParty for crate::InterestedParty {
        fn party_type<'a>(&'a self) -> Option<&'a str> {
        return self.party_type.as_deref();
    }
        fn relationship<'a>(&'a self) -> Option<&'a str> {
        return self.relationship.as_deref();
    }
        fn requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.requirements.as_ref();
    }
        fn addressed_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.addressed_requirements.as_ref();
    }
        fn climate_change_related_requirements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.climate_change_related_requirements.as_ref();
    }
        fn communication_needs<'a>(&'a self) -> Option<&'a str> {
        return self.communication_needs.as_deref();
    }
        fn contact_information<'a>(&'a self) -> Option<&'a str> {
        return self.contact_information.as_deref();
    }
}


pub trait InformationSecurityPolicy : DocumentedInformation   {

    fn policy_statement<'a>(&'a self) -> Option<&'a str>;
    // fn policy_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_policy_statement(&mut self, value: Option<&'a str>);

    fn policy_objectives_framework<'a>(&'a self) -> Option<&'a str>;
    // fn policy_objectives_framework_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_policy_objectives_framework(&mut self, value: Option<&'a str>);

    fn commitment_statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn commitment_statements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_commitment_statements(&mut self, value: Option<&Vec<String>>);

    fn applicability_statement<'a>(&'a self) -> Option<&'a str>;
    // fn applicability_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_applicability_statement(&mut self, value: Option<&'a str>);

    fn communication_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn communication_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_communication_date(&mut self, value: Option<&'a NaiveDate>);

    fn acknowledgment_required(&self) -> Option<bool>;
    // fn acknowledgment_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_acknowledgment_required(&mut self, value: Option<bool>);

    fn last_policy_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn last_policy_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_last_policy_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn next_policy_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn next_policy_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_next_policy_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn related_topic_policies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_topic_policies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_topic_policies<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn integrated_management_systems<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedManagementSystem>>;
    // fn integrated_management_systems_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedManagementSystem>>;
    // fn set_integrated_management_systems(&mut self, value: Option<&Vec<RelatedManagementSystem>>);


}

impl InformationSecurityPolicy for crate::InformationSecurityPolicy {
        fn policy_statement<'a>(&'a self) -> Option<&'a str> {
        return self.policy_statement.as_deref();
    }
        fn policy_objectives_framework<'a>(&'a self) -> Option<&'a str> {
        return self.policy_objectives_framework.as_deref();
    }
        fn commitment_statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.commitment_statements.as_ref();
    }
        fn applicability_statement<'a>(&'a self) -> Option<&'a str> {
        return self.applicability_statement.as_deref();
    }
        fn communication_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.communication_date.as_ref();
    }
        fn acknowledgment_required(&self) -> Option<bool> {
        return self.acknowledgment_required;
    }
        fn last_policy_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.last_policy_review_date.as_ref();
    }
        fn next_policy_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.next_policy_review_date.as_ref();
    }
        fn related_topic_policies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_topic_policies.as_ref();
    }
        fn integrated_management_systems<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedManagementSystem>> {
        return self.integrated_management_systems.as_ref();
    }
}


pub trait TopicSpecificPolicy : DocumentedInformation   {

    fn topic_area<'a>(&'a self) -> Option<&'a str>;
    // fn topic_area_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_topic_area(&mut self, value: Option<&'a str>);

    fn parent_policy<'a>(&'a self) -> Option<&'a str>;
    // fn parent_policy_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_parent_policy<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn applicable_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn applicable_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_applicable_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn target_audience<'a>(&'a self) -> Option<&'a str>;
    // fn target_audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_target_audience(&mut self, value: Option<&'a str>);


}

impl TopicSpecificPolicy for crate::TopicSpecificPolicy {
        fn topic_area<'a>(&'a self) -> Option<&'a str> {
        return self.topic_area.as_deref();
    }
        fn parent_policy<'a>(&'a self) -> Option<&'a str> {
        return self.parent_policy.as_deref();
    }
        fn applicable_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.applicable_controls.as_ref();
    }
        fn target_audience<'a>(&'a self) -> Option<&'a str> {
        return self.target_audience.as_deref();
    }
}


pub trait Role : NamedEntity   {

    fn role_type<'a>(&'a self) -> Option<&'a str>;
    // fn role_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_type(&mut self, value: Option<&'a str>);

    fn responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn responsibilities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_responsibilities(&mut self, value: Option<&Vec<String>>);

    fn authorities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn authorities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_authorities(&mut self, value: Option<&Vec<String>>);

    fn accountability<'a>(&'a self) -> Option<&'a str>;
    // fn accountability_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_accountability(&mut self, value: Option<&'a str>);

    fn assigned_to<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn assigned_to_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_assigned_to(&mut self, value: Option<&Vec<String>>);

    fn delegation_rules<'a>(&'a self) -> Option<&'a str>;
    // fn delegation_rules_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_delegation_rules(&mut self, value: Option<&'a str>);

    fn reporting_line<'a>(&'a self) -> Option<&'a str>;
    // fn reporting_line_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_reporting_line(&mut self, value: Option<&'a str>);


}

impl Role for crate::Role {
        fn role_type<'a>(&'a self) -> Option<&'a str> {
        return self.role_type.as_deref();
    }
        fn responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.responsibilities.as_ref();
    }
        fn authorities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.authorities.as_ref();
    }
        fn accountability<'a>(&'a self) -> Option<&'a str> {
        return self.accountability.as_deref();
    }
        fn assigned_to<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.assigned_to.as_ref();
    }
        fn delegation_rules<'a>(&'a self) -> Option<&'a str> {
        return self.delegation_rules.as_deref();
    }
        fn reporting_line<'a>(&'a self) -> Option<&'a str> {
        return self.reporting_line.as_deref();
    }
}


pub trait InformationSecurityObjective : NamedEntity   {

    fn objective_statement<'a>(&'a self) -> Option<&'a str>;
    // fn objective_statement_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_statement(&mut self, value: Option<&'a str>);

    fn target_value<'a>(&'a self) -> Option<&'a str>;
    // fn target_value_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_target_value(&mut self, value: Option<&'a str>);

    fn current_value<'a>(&'a self) -> Option<&'a str>;
    // fn current_value_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_current_value(&mut self, value: Option<&'a str>);

    fn metric_definition<'a>(&'a self) -> Option<&'a str>;
    // fn metric_definition_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metric_definition(&mut self, value: Option<&'a str>);

    fn measurement_method<'a>(&'a self) -> Option<&'a str>;
    // fn measurement_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_measurement_method(&mut self, value: Option<&'a str>);

    fn measurement_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn measurement_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_measurement_frequency(&mut self, value: Option<&'a str>);

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_target_date(&mut self, value: Option<&'a NaiveDate>);

    fn achievement_status<'a>(&'a self) -> Option<&'a str>;
    // fn achievement_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_achievement_status(&mut self, value: Option<&'a str>);

    fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_risks<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn action_plan<'a>(&'a self) -> Option<&'a str>;
    // fn action_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_plan(&mut self, value: Option<&'a str>);

    fn objective_resources_required<'a>(&'a self) -> Option<&'a str>;
    // fn objective_resources_required_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_resources_required(&mut self, value: Option<&'a str>);


}

impl InformationSecurityObjective for crate::InformationSecurityObjective {
        fn objective_statement<'a>(&'a self) -> Option<&'a str> {
        return self.objective_statement.as_deref();
    }
        fn target_value<'a>(&'a self) -> Option<&'a str> {
        return self.target_value.as_deref();
    }
        fn current_value<'a>(&'a self) -> Option<&'a str> {
        return self.current_value.as_deref();
    }
        fn metric_definition<'a>(&'a self) -> Option<&'a str> {
        return self.metric_definition.as_deref();
    }
        fn measurement_method<'a>(&'a self) -> Option<&'a str> {
        return self.measurement_method.as_deref();
    }
        fn measurement_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.measurement_frequency.as_deref();
    }
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.target_date.as_ref();
    }
        fn achievement_status<'a>(&'a self) -> Option<&'a str> {
        return self.achievement_status.as_deref();
    }
        fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_risks.as_ref();
    }
        fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_controls.as_ref();
    }
        fn action_plan<'a>(&'a self) -> Option<&'a str> {
        return self.action_plan.as_deref();
    }
        fn objective_resources_required<'a>(&'a self) -> Option<&'a str> {
        return self.objective_resources_required.as_deref();
    }
}


pub trait RiskAssessmentProcess : DocumentedInformation   {

    fn risk_acceptance_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn risk_acceptance_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_acceptance_criteria(&mut self, value: Option<&'a str>);

    fn assessment_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_criteria(&mut self, value: Option<&'a str>);

    fn assessment_methodology<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_methodology_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_methodology(&mut self, value: Option<&'a str>);

    fn likelihood_scale<'a>(&'a self) -> Option<&'a str>;
    // fn likelihood_scale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_likelihood_scale(&mut self, value: Option<&'a str>);

    fn impact_scale<'a>(&'a self) -> Option<&'a str>;
    // fn impact_scale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_impact_scale(&mut self, value: Option<&'a str>);

    fn risk_matrix<'a>(&'a self) -> Option<&'a str>;
    // fn risk_matrix_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_matrix(&mut self, value: Option<&'a str>);

    fn assessment_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_frequency(&mut self, value: Option<&'a str>);

    fn trigger_events<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn trigger_events_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_trigger_events(&mut self, value: Option<&Vec<String>>);


}

impl RiskAssessmentProcess for crate::RiskAssessmentProcess {
        fn risk_acceptance_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.risk_acceptance_criteria.as_deref();
    }
        fn assessment_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_criteria.as_deref();
    }
        fn assessment_methodology<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_methodology.as_deref();
    }
        fn likelihood_scale<'a>(&'a self) -> Option<&'a str> {
        return self.likelihood_scale.as_deref();
    }
        fn impact_scale<'a>(&'a self) -> Option<&'a str> {
        return self.impact_scale.as_deref();
    }
        fn risk_matrix<'a>(&'a self) -> Option<&'a str> {
        return self.risk_matrix.as_deref();
    }
        fn assessment_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_frequency.as_deref();
    }
        fn trigger_events<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.trigger_events.as_ref();
    }
}


pub trait RiskAssessment : DocumentedInformation   {

    fn assessment_scope<'a>(&'a self) -> Option<&'a str>;
    // fn assessment_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessment_scope(&mut self, value: Option<&'a str>);

    fn assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn assessment_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_assessment_date(&mut self, value: Option<&'a NaiveDate>);

    fn assessor<'a>(&'a self) -> Option<&'a str>;
    // fn assessor_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_assessor(&mut self, value: Option<&'a str>);

    fn methodology_used<'a>(&'a self) -> Option<&'a str>;
    // fn methodology_used_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_methodology_used(&mut self, value: Option<&'a str>);

    fn risks_identified<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risks_identified_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risks_identified<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn summary_findings<'a>(&'a self) -> Option<&'a str>;
    // fn summary_findings_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_summary_findings(&mut self, value: Option<&'a str>);

    fn recommendations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn recommendations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_recommendations(&mut self, value: Option<&Vec<String>>);

    fn next_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn next_assessment_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_next_assessment_date(&mut self, value: Option<&'a NaiveDate>);


}

impl RiskAssessment for crate::RiskAssessment {
        fn assessment_scope<'a>(&'a self) -> Option<&'a str> {
        return self.assessment_scope.as_deref();
    }
        fn assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.assessment_date.as_ref();
    }
        fn assessor<'a>(&'a self) -> Option<&'a str> {
        return self.assessor.as_deref();
    }
        fn methodology_used<'a>(&'a self) -> Option<&'a str> {
        return self.methodology_used.as_deref();
    }
        fn risks_identified<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risks_identified.as_ref();
    }
        fn summary_findings<'a>(&'a self) -> Option<&'a str> {
        return self.summary_findings.as_deref();
    }
        fn recommendations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.recommendations.as_ref();
    }
        fn next_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.next_assessment_date.as_ref();
    }
}


pub trait Risk : NamedEntity   {

    fn risk_source<'a>(&'a self) -> Option<&'a str>;
    // fn risk_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_source(&mut self, value: Option<&'a str>);

    fn threat_description<'a>(&'a self) -> Option<&'a str>;
    // fn threat_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_threat_description(&mut self, value: Option<&'a str>);

    fn vulnerability_description<'a>(&'a self) -> Option<&'a str>;
    // fn vulnerability_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_vulnerability_description(&mut self, value: Option<&'a str>);

    fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn affected_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_affected_assets<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn affected_cia_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>>;
    // fn affected_cia_properties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>>;
    // fn set_affected_cia_properties(&mut self, value: Option<&Vec<CIAProperty>>);

    fn risk_owner<'a>(&'a self) -> Option<&'a str>;
    // fn risk_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_owner(&mut self, value: Option<&'a str>);

    fn likelihood<'a>(&'a self) -> Option<&'a crate::LikelihoodRating>;
    // fn likelihood_mut(&mut self) -> &mut Option<&'a crate::LikelihoodRating>;
    // fn set_likelihood(&mut self, value: Option<&'a LikelihoodRating>);

    fn impact<'a>(&'a self) -> Option<&'a crate::ImpactRating>;
    // fn impact_mut(&mut self) -> &mut Option<&'a crate::ImpactRating>;
    // fn set_impact(&mut self, value: Option<&'a ImpactRating>);

    fn inherent_risk_level<'a>(&'a self) -> Option<&'a crate::RiskLevel>;
    // fn inherent_risk_level_mut(&mut self) -> &mut Option<&'a crate::RiskLevel>;
    // fn set_inherent_risk_level(&mut self, value: Option<&'a RiskLevel>);

    fn existing_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn existing_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_existing_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn residual_risk_level<'a>(&'a self) -> Option<&'a crate::RiskLevel>;
    // fn residual_risk_level_mut(&mut self) -> &mut Option<&'a crate::RiskLevel>;
    // fn set_residual_risk_level(&mut self, value: Option<&'a RiskLevel>);

    fn risk_treatment_option<'a>(&'a self) -> Option<&'a crate::RiskTreatmentOption>;
    // fn risk_treatment_option_mut(&mut self) -> &mut Option<&'a crate::RiskTreatmentOption>;
    // fn set_risk_treatment_option(&mut self, value: Option<&'a RiskTreatmentOption>);

    fn treatment_priority<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_priority_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_priority(&mut self, value: Option<&'a str>);

    fn related_treatment_plan<'a>(&'a self) -> Option<&'a str>;
    // fn related_treatment_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_related_treatment_plan<E>(&mut self, value: Option<&'a str>) where E: Into<String>;


}

impl Risk for crate::Risk {
        fn risk_source<'a>(&'a self) -> Option<&'a str> {
        return self.risk_source.as_deref();
    }
        fn threat_description<'a>(&'a self) -> Option<&'a str> {
        return self.threat_description.as_deref();
    }
        fn vulnerability_description<'a>(&'a self) -> Option<&'a str> {
        return self.vulnerability_description.as_deref();
    }
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn affected_cia_properties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>> {
        return self.affected_cia_properties.as_ref();
    }
        fn risk_owner<'a>(&'a self) -> Option<&'a str> {
        return self.risk_owner.as_deref();
    }
        fn likelihood<'a>(&'a self) -> Option<&'a crate::LikelihoodRating> {
        return self.likelihood.as_ref();
    }
        fn impact<'a>(&'a self) -> Option<&'a crate::ImpactRating> {
        return self.impact.as_ref();
    }
        fn inherent_risk_level<'a>(&'a self) -> Option<&'a crate::RiskLevel> {
        return self.inherent_risk_level.as_ref();
    }
        fn existing_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.existing_controls.as_ref();
    }
        fn residual_risk_level<'a>(&'a self) -> Option<&'a crate::RiskLevel> {
        return self.residual_risk_level.as_ref();
    }
        fn risk_treatment_option<'a>(&'a self) -> Option<&'a crate::RiskTreatmentOption> {
        return self.risk_treatment_option.as_ref();
    }
        fn treatment_priority<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_priority.as_deref();
    }
        fn related_treatment_plan<'a>(&'a self) -> Option<&'a str> {
        return self.related_treatment_plan.as_deref();
    }
}


pub trait RiskTreatmentProcess : DocumentedInformation   {

    fn treatment_options_guidance<'a>(&'a self) -> Option<&'a str>;
    // fn treatment_options_guidance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_treatment_options_guidance(&mut self, value: Option<&'a str>);

    fn control_selection_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn control_selection_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_selection_criteria(&mut self, value: Option<&'a str>);

    fn annex_a_omission_verification<'a>(&'a self) -> Option<&'a str>;
    // fn annex_a_omission_verification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_annex_a_omission_verification(&mut self, value: Option<&'a str>);

    fn soa_template<'a>(&'a self) -> Option<&'a str>;
    // fn soa_template_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_soa_template(&mut self, value: Option<&'a str>);

    fn approval_workflow<'a>(&'a self) -> Option<&'a str>;
    // fn approval_workflow_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_approval_workflow(&mut self, value: Option<&'a str>);


}

impl RiskTreatmentProcess for crate::RiskTreatmentProcess {
        fn treatment_options_guidance<'a>(&'a self) -> Option<&'a str> {
        return self.treatment_options_guidance.as_deref();
    }
        fn control_selection_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.control_selection_criteria.as_deref();
    }
        fn annex_a_omission_verification<'a>(&'a self) -> Option<&'a str> {
        return self.annex_a_omission_verification.as_deref();
    }
        fn soa_template<'a>(&'a self) -> Option<&'a str> {
        return self.soa_template.as_deref();
    }
        fn approval_workflow<'a>(&'a self) -> Option<&'a str> {
        return self.approval_workflow.as_deref();
    }
}


pub trait RiskTreatmentPlan : DocumentedInformation   {

    fn plan_scope<'a>(&'a self) -> Option<&'a str>;
    // fn plan_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_plan_scope(&mut self, value: Option<&'a str>);

    fn risks_addressed<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn risks_addressed_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_risks_addressed<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn treatment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn treatment_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_treatment_actions(&mut self, value: Option<&Vec<String>>);

    fn controls_to_implement<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn controls_to_implement_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_controls_to_implement<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn resources_required<'a>(&'a self) -> Option<&'a str>;
    // fn resources_required_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resources_required(&mut self, value: Option<&'a str>);

    fn responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn responsible_parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_responsible_parties(&mut self, value: Option<&Vec<String>>);

    fn implementation_timeline<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_timeline_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_timeline(&mut self, value: Option<&'a str>);

    fn risk_owner_approval<'a>(&'a self) -> Option<&'a str>;
    // fn risk_owner_approval_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_owner_approval(&mut self, value: Option<&'a str>);

    fn residual_risk_acceptance<'a>(&'a self) -> Option<&'a str>;
    // fn residual_risk_acceptance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_residual_risk_acceptance(&mut self, value: Option<&'a str>);

    fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus>;
    // fn implementation_status_mut(&mut self) -> &mut Option<&'a crate::ImplementationStatus>;
    // fn set_implementation_status(&mut self, value: Option<&'a ImplementationStatus>);

    fn completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_completion_date(&mut self, value: Option<&'a NaiveDate>);


}

impl RiskTreatmentPlan for crate::RiskTreatmentPlan {
        fn plan_scope<'a>(&'a self) -> Option<&'a str> {
        return self.plan_scope.as_deref();
    }
        fn risks_addressed<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.risks_addressed.as_ref();
    }
        fn treatment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.treatment_actions.as_ref();
    }
        fn controls_to_implement<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.controls_to_implement.as_ref();
    }
        fn resources_required<'a>(&'a self) -> Option<&'a str> {
        return self.resources_required.as_deref();
    }
        fn responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.responsible_parties.as_ref();
    }
        fn implementation_timeline<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_timeline.as_deref();
    }
        fn risk_owner_approval<'a>(&'a self) -> Option<&'a str> {
        return self.risk_owner_approval.as_deref();
    }
        fn residual_risk_acceptance<'a>(&'a self) -> Option<&'a str> {
        return self.residual_risk_acceptance.as_deref();
    }
        fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus> {
        return self.implementation_status.as_ref();
    }
        fn completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.completion_date.as_ref();
    }
}


pub trait StatementOfApplicability : DocumentedInformation   {

    fn soa_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SoAEntry>>;
    // fn soa_entries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SoAEntry>>;
    // fn set_soa_entries<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SoAEntry>;

    fn total_controls(&self) -> Option<isize>;
    // fn total_controls_mut(&mut self) -> &mut Option<isize>;
    // fn set_total_controls(&mut self, value: Option<isize>);

    fn implemented_count(&self) -> Option<isize>;
    // fn implemented_count_mut(&mut self) -> &mut Option<isize>;
    // fn set_implemented_count(&mut self, value: Option<isize>);

    fn planned_count(&self) -> Option<isize>;
    // fn planned_count_mut(&mut self) -> &mut Option<isize>;
    // fn set_planned_count(&mut self, value: Option<isize>);

    fn not_applicable_count(&self) -> Option<isize>;
    // fn not_applicable_count_mut(&mut self) -> &mut Option<isize>;
    // fn set_not_applicable_count(&mut self, value: Option<isize>);

    fn last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn last_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_last_review_date(&mut self, value: Option<&'a NaiveDate>);


}

impl StatementOfApplicability for crate::StatementOfApplicability {
        fn soa_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SoAEntry>> {
        return self.soa_entries.as_ref();
    }
        fn total_controls(&self) -> Option<isize> {
        return self.total_controls;
    }
        fn implemented_count(&self) -> Option<isize> {
        return self.implemented_count;
    }
        fn planned_count(&self) -> Option<isize> {
        return self.planned_count;
    }
        fn not_applicable_count(&self) -> Option<isize> {
        return self.not_applicable_count;
    }
        fn last_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.last_review_date.as_ref();
    }
}


pub trait SoAEntry   {

    fn control_reference<'a>(&'a self) -> Option<&'a str>;
    // fn control_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_reference<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn is_applicable(&self) -> Option<bool>;
    // fn is_applicable_mut(&mut self) -> &mut Option<bool>;
    // fn set_is_applicable(&mut self, value: Option<bool>);

    fn inclusion_justification<'a>(&'a self) -> Option<&'a str>;
    // fn inclusion_justification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_inclusion_justification(&mut self, value: Option<&'a str>);

    fn exclusion_justification<'a>(&'a self) -> Option<&'a str>;
    // fn exclusion_justification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_exclusion_justification(&mut self, value: Option<&'a str>);

    fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus>;
    // fn implementation_status_mut(&mut self) -> &mut Option<&'a crate::ImplementationStatus>;
    // fn set_implementation_status(&mut self, value: Option<&'a ImplementationStatus>);

    fn implementation_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_evidence(&mut self, value: Option<&'a str>);

    fn responsible_role<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_role<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn target_implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn target_implementation_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_target_implementation_date(&mut self, value: Option<&'a NaiveDate>);


}

impl SoAEntry for crate::SoAEntry {
        fn control_reference<'a>(&'a self) -> Option<&'a str> {
        return self.control_reference.as_deref();
    }
        fn is_applicable(&self) -> Option<bool> {
        return self.is_applicable;
    }
        fn inclusion_justification<'a>(&'a self) -> Option<&'a str> {
        return self.inclusion_justification.as_deref();
    }
        fn exclusion_justification<'a>(&'a self) -> Option<&'a str> {
        return self.exclusion_justification.as_deref();
    }
        fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus> {
        return self.implementation_status.as_ref();
    }
        fn implementation_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_evidence.as_deref();
    }
        fn responsible_role<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_role.as_deref();
    }
        fn target_implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.target_implementation_date.as_ref();
    }
}


pub trait SecurityControl : NamedEntity   {

    fn control_id<'a>(&'a self) -> Option<&'a crate::AnnexAControlId>;
    // fn control_id_mut(&mut self) -> &mut Option<&'a crate::AnnexAControlId>;
    // fn set_control_id(&mut self, value: Option<&'a AnnexAControlId>);

    fn control_title<'a>(&'a self) -> Option<&'a str>;
    // fn control_title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_title(&mut self, value: Option<&'a str>);

    fn control_category<'a>(&'a self) -> Option<&'a crate::ControlCategory>;
    // fn control_category_mut(&mut self) -> &mut Option<&'a crate::ControlCategory>;
    // fn set_control_category(&mut self, value: Option<&'a ControlCategory>);

    fn control_text<'a>(&'a self) -> Option<&'a str>;
    // fn control_text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_text(&mut self, value: Option<&'a str>);

    fn implementation_guidance<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_guidance_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_guidance(&mut self, value: Option<&'a str>);

    fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn applicable_threats<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn applicable_threats_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_applicable_threats(&mut self, value: Option<&Vec<String>>);

    fn applicable_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn applicable_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_applicable_assets(&mut self, value: Option<&Vec<String>>);

    fn control_owner<'a>(&'a self) -> Option<&'a str>;
    // fn control_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_owner(&mut self, value: Option<&'a str>);

    fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus>;
    // fn implementation_status_mut(&mut self) -> &mut Option<&'a crate::ImplementationStatus>;
    // fn set_implementation_status(&mut self, value: Option<&'a ImplementationStatus>);

    fn implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn implementation_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_implementation_date(&mut self, value: Option<&'a NaiveDate>);

    fn effectiveness_rating<'a>(&'a self) -> Option<&'a str>;
    // fn effectiveness_rating_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_effectiveness_rating(&mut self, value: Option<&'a str>);

    fn last_test_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn last_test_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_last_test_date(&mut self, value: Option<&'a NaiveDate>);

    fn evidence_references<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn evidence_references_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_evidence_references(&mut self, value: Option<&Vec<String>>);


}

impl SecurityControl for crate::SecurityControl {
        fn control_id<'a>(&'a self) -> Option<&'a crate::AnnexAControlId> {
        return self.control_id.as_ref();
    }
        fn control_title<'a>(&'a self) -> Option<&'a str> {
        return self.control_title.as_deref();
    }
        fn control_category<'a>(&'a self) -> Option<&'a crate::ControlCategory> {
        return self.control_category.as_ref();
    }
        fn control_text<'a>(&'a self) -> Option<&'a str> {
        return self.control_text.as_deref();
    }
        fn implementation_guidance<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_guidance.as_deref();
    }
        fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_controls.as_ref();
    }
        fn applicable_threats<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.applicable_threats.as_ref();
    }
        fn applicable_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.applicable_assets.as_ref();
    }
        fn control_owner<'a>(&'a self) -> Option<&'a str> {
        return self.control_owner.as_deref();
    }
        fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus> {
        return self.implementation_status.as_ref();
    }
        fn implementation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.implementation_date.as_ref();
    }
        fn effectiveness_rating<'a>(&'a self) -> Option<&'a str> {
        return self.effectiveness_rating.as_deref();
    }
        fn last_test_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.last_test_date.as_ref();
    }
        fn evidence_references<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.evidence_references.as_ref();
    }
}


pub trait Resource : NamedEntity   {

    fn resource_type<'a>(&'a self) -> Option<&'a str>;
    // fn resource_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_type(&mut self, value: Option<&'a str>);

    fn quantity<'a>(&'a self) -> Option<&'a str>;
    // fn quantity_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_quantity(&mut self, value: Option<&'a str>);

    fn allocation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn allocation_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_allocation_date(&mut self, value: Option<&'a NaiveDate>);

    fn allocated_to<'a>(&'a self) -> Option<&'a str>;
    // fn allocated_to_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_allocated_to(&mut self, value: Option<&'a str>);

    fn cost<'a>(&'a self) -> Option<&'a str>;
    // fn cost_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_cost(&mut self, value: Option<&'a str>);

    fn availability_status<'a>(&'a self) -> Option<&'a str>;
    // fn availability_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_availability_status(&mut self, value: Option<&'a str>);


}

impl Resource for crate::Resource {
        fn resource_type<'a>(&'a self) -> Option<&'a str> {
        return self.resource_type.as_deref();
    }
        fn quantity<'a>(&'a self) -> Option<&'a str> {
        return self.quantity.as_deref();
    }
        fn allocation_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.allocation_date.as_ref();
    }
        fn allocated_to<'a>(&'a self) -> Option<&'a str> {
        return self.allocated_to.as_deref();
    }
        fn cost<'a>(&'a self) -> Option<&'a str> {
        return self.cost.as_deref();
    }
        fn availability_status<'a>(&'a self) -> Option<&'a str> {
        return self.availability_status.as_deref();
    }
}


pub trait CompetenceRecord : DocumentedInformation   {

    fn person_name<'a>(&'a self) -> Option<&'a str>;
    // fn person_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_person_name(&mut self, value: Option<&'a str>);

    fn person_role<'a>(&'a self) -> Option<&'a str>;
    // fn person_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_person_role(&mut self, value: Option<&'a str>);

    fn required_competencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn required_competencies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_required_competencies(&mut self, value: Option<&Vec<String>>);

    fn education_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn education_records_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_education_records(&mut self, value: Option<&Vec<String>>);

    fn training_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn training_records_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_training_records(&mut self, value: Option<&Vec<String>>);

    fn experience_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn experience_records_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_experience_records(&mut self, value: Option<&Vec<String>>);

    fn competency_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn competency_assessment_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_competency_assessment_date(&mut self, value: Option<&'a NaiveDate>);

    fn competency_gaps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn competency_gaps_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_competency_gaps(&mut self, value: Option<&Vec<String>>);

    fn development_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn development_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_development_actions(&mut self, value: Option<&Vec<String>>);


}

impl CompetenceRecord for crate::CompetenceRecord {
        fn person_name<'a>(&'a self) -> Option<&'a str> {
        return self.person_name.as_deref();
    }
        fn person_role<'a>(&'a self) -> Option<&'a str> {
        return self.person_role.as_deref();
    }
        fn required_competencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.required_competencies.as_ref();
    }
        fn education_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.education_records.as_ref();
    }
        fn training_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.training_records.as_ref();
    }
        fn experience_records<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.experience_records.as_ref();
    }
        fn competency_assessment_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.competency_assessment_date.as_ref();
    }
        fn competency_gaps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.competency_gaps.as_ref();
    }
        fn development_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.development_actions.as_ref();
    }
}


pub trait AwarenessProgram : DocumentedInformation   {

    fn awareness_topics<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn awareness_topics_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_awareness_topics(&mut self, value: Option<&Vec<String>>);

    fn delivery_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn delivery_methods_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_delivery_methods(&mut self, value: Option<&Vec<String>>);

    fn target_audience<'a>(&'a self) -> Option<&'a str>;
    // fn target_audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_target_audience(&mut self, value: Option<&'a str>);

    fn frequency<'a>(&'a self) -> Option<&'a str>;
    // fn frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_frequency(&mut self, value: Option<&'a str>);

    fn completion_tracking<'a>(&'a self) -> Option<&'a str>;
    // fn completion_tracking_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_completion_tracking(&mut self, value: Option<&'a str>);

    fn effectiveness_measures<'a>(&'a self) -> Option<&'a str>;
    // fn effectiveness_measures_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_effectiveness_measures(&mut self, value: Option<&'a str>);


}

impl AwarenessProgram for crate::AwarenessProgram {
        fn awareness_topics<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.awareness_topics.as_ref();
    }
        fn delivery_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.delivery_methods.as_ref();
    }
        fn target_audience<'a>(&'a self) -> Option<&'a str> {
        return self.target_audience.as_deref();
    }
        fn frequency<'a>(&'a self) -> Option<&'a str> {
        return self.frequency.as_deref();
    }
        fn completion_tracking<'a>(&'a self) -> Option<&'a str> {
        return self.completion_tracking.as_deref();
    }
        fn effectiveness_measures<'a>(&'a self) -> Option<&'a str> {
        return self.effectiveness_measures.as_deref();
    }
}


pub trait CommunicationPlan : DocumentedInformation   {

    fn communication_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CommunicationItem>>;
    // fn communication_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CommunicationItem>>;
    // fn set_communication_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<CommunicationItem>;


}

impl CommunicationPlan for crate::CommunicationPlan {
        fn communication_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CommunicationItem>> {
        return self.communication_items.as_ref();
    }
}


pub trait CommunicationItem   {

    fn subject<'a>(&'a self) -> Option<&'a str>;
    // fn subject_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_subject(&mut self, value: Option<&'a str>);

    fn purpose<'a>(&'a self) -> Option<&'a str>;
    // fn purpose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_purpose(&mut self, value: Option<&'a str>);

    fn audience<'a>(&'a self) -> Option<&'a str>;
    // fn audience_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audience(&mut self, value: Option<&'a str>);

    fn frequency<'a>(&'a self) -> Option<&'a str>;
    // fn frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_frequency(&mut self, value: Option<&'a str>);

    fn method<'a>(&'a self) -> Option<&'a str>;
    // fn method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_method(&mut self, value: Option<&'a str>);

    fn responsible_party<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_party_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_party(&mut self, value: Option<&'a str>);

    fn records_required(&self) -> Option<bool>;
    // fn records_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_records_required(&mut self, value: Option<bool>);


}

impl CommunicationItem for crate::CommunicationItem {
        fn subject<'a>(&'a self) -> Option<&'a str> {
        return self.subject.as_deref();
    }
        fn purpose<'a>(&'a self) -> Option<&'a str> {
        return self.purpose.as_deref();
    }
        fn audience<'a>(&'a self) -> Option<&'a str> {
        return self.audience.as_deref();
    }
        fn frequency<'a>(&'a self) -> Option<&'a str> {
        return self.frequency.as_deref();
    }
        fn method<'a>(&'a self) -> Option<&'a str> {
        return self.method.as_deref();
    }
        fn responsible_party<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_party.as_deref();
    }
        fn records_required(&self) -> Option<bool> {
        return self.records_required;
    }
}


pub trait OperationalProcedure : DocumentedInformation   {

    fn procedure_scope<'a>(&'a self) -> Option<&'a str>;
    // fn procedure_scope_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_procedure_scope(&mut self, value: Option<&'a str>);

    fn process_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn process_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_process_criteria(&mut self, value: Option<&'a str>);

    fn control_measures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn control_measures_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_control_measures(&mut self, value: Option<&Vec<String>>);

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn change_control_requirements<'a>(&'a self) -> Option<&'a str>;
    // fn change_control_requirements_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_change_control_requirements(&mut self, value: Option<&'a str>);


}

impl OperationalProcedure for crate::OperationalProcedure {
        fn procedure_scope<'a>(&'a self) -> Option<&'a str> {
        return self.procedure_scope.as_deref();
    }
        fn process_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.process_criteria.as_deref();
    }
        fn control_measures<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.control_measures.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.responsible_roles.as_ref();
    }
        fn related_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_controls.as_ref();
    }
        fn change_control_requirements<'a>(&'a self) -> Option<&'a str> {
        return self.change_control_requirements.as_deref();
    }
}


pub trait MonitoringProgram : DocumentedInformation   {

    fn monitoring_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MonitoringItem>>;
    // fn monitoring_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MonitoringItem>>;
    // fn set_monitoring_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MonitoringItem>;


}

impl MonitoringProgram for crate::MonitoringProgram {
        fn monitoring_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MonitoringItem>> {
        return self.monitoring_items.as_ref();
    }
}


pub trait MonitoringItem   {

    fn metric_name<'a>(&'a self) -> Option<&'a str>;
    // fn metric_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metric_name(&mut self, value: Option<&'a str>);

    fn metric_description<'a>(&'a self) -> Option<&'a str>;
    // fn metric_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metric_description(&mut self, value: Option<&'a str>);

    fn measurement_method<'a>(&'a self) -> Option<&'a str>;
    // fn measurement_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_measurement_method(&mut self, value: Option<&'a str>);

    fn measurement_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn measurement_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_measurement_frequency(&mut self, value: Option<&'a str>);

    fn responsible_party<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_party_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_party(&mut self, value: Option<&'a str>);

    fn analysis_frequency<'a>(&'a self) -> Option<&'a str>;
    // fn analysis_frequency_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_analysis_frequency(&mut self, value: Option<&'a str>);

    fn analyst<'a>(&'a self) -> Option<&'a str>;
    // fn analyst_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_analyst(&mut self, value: Option<&'a str>);

    fn target_threshold<'a>(&'a self) -> Option<&'a str>;
    // fn target_threshold_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_target_threshold(&mut self, value: Option<&'a str>);

    fn alert_threshold<'a>(&'a self) -> Option<&'a str>;
    // fn alert_threshold_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_alert_threshold(&mut self, value: Option<&'a str>);

    fn current_value<'a>(&'a self) -> Option<&'a str>;
    // fn current_value_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_current_value(&mut self, value: Option<&'a str>);

    fn trend<'a>(&'a self) -> Option<&'a str>;
    // fn trend_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trend(&mut self, value: Option<&'a str>);


}

impl MonitoringItem for crate::MonitoringItem {
        fn metric_name<'a>(&'a self) -> Option<&'a str> {
        return self.metric_name.as_deref();
    }
        fn metric_description<'a>(&'a self) -> Option<&'a str> {
        return self.metric_description.as_deref();
    }
        fn measurement_method<'a>(&'a self) -> Option<&'a str> {
        return self.measurement_method.as_deref();
    }
        fn measurement_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.measurement_frequency.as_deref();
    }
        fn responsible_party<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_party.as_deref();
    }
        fn analysis_frequency<'a>(&'a self) -> Option<&'a str> {
        return self.analysis_frequency.as_deref();
    }
        fn analyst<'a>(&'a self) -> Option<&'a str> {
        return self.analyst.as_deref();
    }
        fn target_threshold<'a>(&'a self) -> Option<&'a str> {
        return self.target_threshold.as_deref();
    }
        fn alert_threshold<'a>(&'a self) -> Option<&'a str> {
        return self.alert_threshold.as_deref();
    }
        fn current_value<'a>(&'a self) -> Option<&'a str> {
        return self.current_value.as_deref();
    }
        fn trend<'a>(&'a self) -> Option<&'a str> {
        return self.trend.as_deref();
    }
}


pub trait InternalAudit : DocumentedInformation   {

    fn audit_reference<'a>(&'a self) -> Option<&'a str>;
    // fn audit_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_reference(&mut self, value: Option<&'a str>);

    fn audit_type<'a>(&'a self) -> Option<&'a crate::AuditType>;
    // fn audit_type_mut(&mut self) -> &mut Option<&'a crate::AuditType>;
    // fn set_audit_type(&mut self, value: Option<&'a AuditType>);

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

    fn lead_auditor<'a>(&'a self) -> Option<&'a str>;
    // fn lead_auditor_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_lead_auditor(&mut self, value: Option<&'a str>);

    fn audit_team<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn audit_team_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_audit_team(&mut self, value: Option<&Vec<String>>);

    fn auditee_representatives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn auditee_representatives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_auditee_representatives(&mut self, value: Option<&Vec<String>>);

    fn audit_plan<'a>(&'a self) -> Option<&'a str>;
    // fn audit_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_plan(&mut self, value: Option<&'a str>);

    fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn findings_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_findings<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn positive_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn positive_observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_positive_observations(&mut self, value: Option<&Vec<String>>);

    fn audit_conclusion<'a>(&'a self) -> Option<&'a str>;
    // fn audit_conclusion_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_conclusion(&mut self, value: Option<&'a str>);

    fn report_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn report_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_report_date(&mut self, value: Option<&'a NaiveDate>);

    fn report_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn report_distribution_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_report_distribution(&mut self, value: Option<&Vec<String>>);


}

impl InternalAudit for crate::InternalAudit {
        fn audit_reference<'a>(&'a self) -> Option<&'a str> {
        return self.audit_reference.as_deref();
    }
        fn audit_type<'a>(&'a self) -> Option<&'a crate::AuditType> {
        return self.audit_type.as_ref();
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
        fn lead_auditor<'a>(&'a self) -> Option<&'a str> {
        return self.lead_auditor.as_deref();
    }
        fn audit_team<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.audit_team.as_ref();
    }
        fn auditee_representatives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.auditee_representatives.as_ref();
    }
        fn audit_plan<'a>(&'a self) -> Option<&'a str> {
        return self.audit_plan.as_deref();
    }
        fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.findings.as_ref();
    }
        fn positive_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.positive_observations.as_ref();
    }
        fn audit_conclusion<'a>(&'a self) -> Option<&'a str> {
        return self.audit_conclusion.as_deref();
    }
        fn report_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.report_date.as_ref();
    }
        fn report_distribution<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.report_distribution.as_ref();
    }
}


pub trait AuditProgramme : DocumentedInformation   {

    fn programme_period<'a>(&'a self) -> Option<&'a str>;
    // fn programme_period_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_period(&mut self, value: Option<&'a str>);

    fn planned_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn planned_audits_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_planned_audits<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn audit_frequency_rationale<'a>(&'a self) -> Option<&'a str>;
    // fn audit_frequency_rationale_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_frequency_rationale(&mut self, value: Option<&'a str>);

    fn resource_requirements<'a>(&'a self) -> Option<&'a str>;
    // fn resource_requirements_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_requirements(&mut self, value: Option<&'a str>);

    fn auditor_qualifications<'a>(&'a self) -> Option<&'a str>;
    // fn auditor_qualifications_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_auditor_qualifications(&mut self, value: Option<&'a str>);

    fn programme_status<'a>(&'a self) -> Option<&'a str>;
    // fn programme_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_programme_status(&mut self, value: Option<&'a str>);


}

impl AuditProgramme for crate::AuditProgramme {
        fn programme_period<'a>(&'a self) -> Option<&'a str> {
        return self.programme_period.as_deref();
    }
        fn planned_audits<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.planned_audits.as_ref();
    }
        fn audit_frequency_rationale<'a>(&'a self) -> Option<&'a str> {
        return self.audit_frequency_rationale.as_deref();
    }
        fn resource_requirements<'a>(&'a self) -> Option<&'a str> {
        return self.resource_requirements.as_deref();
    }
        fn auditor_qualifications<'a>(&'a self) -> Option<&'a str> {
        return self.auditor_qualifications.as_deref();
    }
        fn programme_status<'a>(&'a self) -> Option<&'a str> {
        return self.programme_status.as_deref();
    }
}


pub trait AuditFinding : NamedEntity   {

    fn finding_type<'a>(&'a self) -> Option<&'a crate::AuditFindingType>;
    // fn finding_type_mut(&mut self) -> &mut Option<&'a crate::AuditFindingType>;
    // fn set_finding_type(&mut self, value: Option<&'a AuditFindingType>);

    fn clause_reference<'a>(&'a self) -> Option<&'a str>;
    // fn clause_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_clause_reference(&mut self, value: Option<&'a str>);

    fn control_reference<'a>(&'a self) -> Option<&'a str>;
    // fn control_reference_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_control_reference<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn finding_description<'a>(&'a self) -> Option<&'a str>;
    // fn finding_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_finding_description(&mut self, value: Option<&'a str>);

    fn objective_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn objective_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_objective_evidence(&mut self, value: Option<&'a str>);

    fn root_cause_analysis<'a>(&'a self) -> Option<&'a str>;
    // fn root_cause_analysis_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_root_cause_analysis(&mut self, value: Option<&'a str>);

    fn risk_implication<'a>(&'a self) -> Option<&'a str>;
    // fn risk_implication_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_implication(&mut self, value: Option<&'a str>);

    fn recommended_action<'a>(&'a self) -> Option<&'a str>;
    // fn recommended_action_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_recommended_action(&mut self, value: Option<&'a str>);

    fn auditee_response<'a>(&'a self) -> Option<&'a str>;
    // fn auditee_response_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_auditee_response(&mut self, value: Option<&'a str>);

    fn linked_corrective_action<'a>(&'a self) -> Option<&'a str>;
    // fn linked_corrective_action_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_linked_corrective_action<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn closure_status<'a>(&'a self) -> Option<&'a str>;
    // fn closure_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_closure_status(&mut self, value: Option<&'a str>);

    fn closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn closure_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_closure_date(&mut self, value: Option<&'a NaiveDate>);


}

impl AuditFinding for crate::AuditFinding {
        fn finding_type<'a>(&'a self) -> Option<&'a crate::AuditFindingType> {
        return self.finding_type.as_ref();
    }
        fn clause_reference<'a>(&'a self) -> Option<&'a str> {
        return self.clause_reference.as_deref();
    }
        fn control_reference<'a>(&'a self) -> Option<&'a str> {
        return self.control_reference.as_deref();
    }
        fn finding_description<'a>(&'a self) -> Option<&'a str> {
        return self.finding_description.as_deref();
    }
        fn objective_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.objective_evidence.as_deref();
    }
        fn root_cause_analysis<'a>(&'a self) -> Option<&'a str> {
        return self.root_cause_analysis.as_deref();
    }
        fn risk_implication<'a>(&'a self) -> Option<&'a str> {
        return self.risk_implication.as_deref();
    }
        fn recommended_action<'a>(&'a self) -> Option<&'a str> {
        return self.recommended_action.as_deref();
    }
        fn auditee_response<'a>(&'a self) -> Option<&'a str> {
        return self.auditee_response.as_deref();
    }
        fn linked_corrective_action<'a>(&'a self) -> Option<&'a str> {
        return self.linked_corrective_action.as_deref();
    }
        fn closure_status<'a>(&'a self) -> Option<&'a str> {
        return self.closure_status.as_deref();
    }
        fn closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.closure_date.as_ref();
    }
}


pub trait ManagementReview : DocumentedInformation   {

    fn attendees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn attendees_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_attendees(&mut self, value: Option<&Vec<String>>);

    fn previous_actions_status<'a>(&'a self) -> Option<&'a str>;
    // fn previous_actions_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_previous_actions_status(&mut self, value: Option<&'a str>);

    fn context_changes<'a>(&'a self) -> Option<&'a str>;
    // fn context_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_context_changes(&mut self, value: Option<&'a str>);

    fn interested_party_changes<'a>(&'a self) -> Option<&'a str>;
    // fn interested_party_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_interested_party_changes(&mut self, value: Option<&'a str>);

    fn interested_party_feedback<'a>(&'a self) -> Option<&'a str>;
    // fn interested_party_feedback_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_interested_party_feedback(&mut self, value: Option<&'a str>);

    fn performance_trends<'a>(&'a self) -> Option<&'a str>;
    // fn performance_trends_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_performance_trends(&mut self, value: Option<&'a str>);

    fn audit_results_summary<'a>(&'a self) -> Option<&'a str>;
    // fn audit_results_summary_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_audit_results_summary(&mut self, value: Option<&'a str>);

    fn risk_assessment_results<'a>(&'a self) -> Option<&'a str>;
    // fn risk_assessment_results_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_assessment_results(&mut self, value: Option<&'a str>);

    fn risk_treatment_status<'a>(&'a self) -> Option<&'a str>;
    // fn risk_treatment_status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risk_treatment_status(&mut self, value: Option<&'a str>);

    fn risks_and_opportunities_changes<'a>(&'a self) -> Option<&'a str>;
    // fn risks_and_opportunities_changes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_risks_and_opportunities_changes(&mut self, value: Option<&'a str>);

    fn improvement_opportunities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn improvement_opportunities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_improvement_opportunities(&mut self, value: Option<&Vec<String>>);

    fn decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn decisions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_decisions(&mut self, value: Option<&Vec<String>>);

    fn action_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn action_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_action_items(&mut self, value: Option<&Vec<String>>);

    fn next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn next_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_next_review_date(&mut self, value: Option<&'a NaiveDate>);


}

impl ManagementReview for crate::ManagementReview {
        fn attendees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.attendees.as_ref();
    }
        fn previous_actions_status<'a>(&'a self) -> Option<&'a str> {
        return self.previous_actions_status.as_deref();
    }
        fn context_changes<'a>(&'a self) -> Option<&'a str> {
        return self.context_changes.as_deref();
    }
        fn interested_party_changes<'a>(&'a self) -> Option<&'a str> {
        return self.interested_party_changes.as_deref();
    }
        fn interested_party_feedback<'a>(&'a self) -> Option<&'a str> {
        return self.interested_party_feedback.as_deref();
    }
        fn performance_trends<'a>(&'a self) -> Option<&'a str> {
        return self.performance_trends.as_deref();
    }
        fn audit_results_summary<'a>(&'a self) -> Option<&'a str> {
        return self.audit_results_summary.as_deref();
    }
        fn risk_assessment_results<'a>(&'a self) -> Option<&'a str> {
        return self.risk_assessment_results.as_deref();
    }
        fn risk_treatment_status<'a>(&'a self) -> Option<&'a str> {
        return self.risk_treatment_status.as_deref();
    }
        fn risks_and_opportunities_changes<'a>(&'a self) -> Option<&'a str> {
        return self.risks_and_opportunities_changes.as_deref();
    }
        fn improvement_opportunities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.improvement_opportunities.as_ref();
    }
        fn decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.decisions.as_ref();
    }
        fn action_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.action_items.as_ref();
    }
        fn next_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.next_review_date.as_ref();
    }
}


pub trait Nonconformity : NamedEntity   {

    fn nonconformity_source<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_source(&mut self, value: Option<&'a str>);

    fn detection_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn detection_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_detection_date(&mut self, value: Option<&'a NaiveDate>);

    fn detected_by<'a>(&'a self) -> Option<&'a str>;
    // fn detected_by_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_detected_by(&mut self, value: Option<&'a str>);

    fn requirement_violated<'a>(&'a self) -> Option<&'a str>;
    // fn requirement_violated_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_requirement_violated(&mut self, value: Option<&'a str>);

    fn nonconformity_description<'a>(&'a self) -> Option<&'a str>;
    // fn nonconformity_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_nonconformity_description(&mut self, value: Option<&'a str>);

    fn immediate_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn immediate_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_immediate_actions(&mut self, value: Option<&Vec<String>>);

    fn consequences_addressed<'a>(&'a self) -> Option<&'a str>;
    // fn consequences_addressed_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_consequences_addressed(&mut self, value: Option<&'a str>);

    fn root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_root_cause(&mut self, value: Option<&'a str>);

    fn similar_nonconformities_check<'a>(&'a self) -> Option<&'a str>;
    // fn similar_nonconformities_check_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_similar_nonconformities_check(&mut self, value: Option<&'a str>);

    fn linked_corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn linked_corrective_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_linked_corrective_actions<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn status<'a>(&'a self) -> Option<&'a str>;
    // fn status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_status(&mut self, value: Option<&'a str>);

    fn closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn closure_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_closure_date(&mut self, value: Option<&'a NaiveDate>);

    fn closure_evidence<'a>(&'a self) -> Option<&'a str>;
    // fn closure_evidence_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_closure_evidence(&mut self, value: Option<&'a str>);


}

impl Nonconformity for crate::Nonconformity {
        fn nonconformity_source<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_source.as_deref();
    }
        fn detection_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.detection_date.as_ref();
    }
        fn detected_by<'a>(&'a self) -> Option<&'a str> {
        return self.detected_by.as_deref();
    }
        fn requirement_violated<'a>(&'a self) -> Option<&'a str> {
        return self.requirement_violated.as_deref();
    }
        fn nonconformity_description<'a>(&'a self) -> Option<&'a str> {
        return self.nonconformity_description.as_deref();
    }
        fn immediate_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.immediate_actions.as_ref();
    }
        fn consequences_addressed<'a>(&'a self) -> Option<&'a str> {
        return self.consequences_addressed.as_deref();
    }
        fn root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.root_cause.as_deref();
    }
        fn similar_nonconformities_check<'a>(&'a self) -> Option<&'a str> {
        return self.similar_nonconformities_check.as_deref();
    }
        fn linked_corrective_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.linked_corrective_actions.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
        fn closure_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.closure_date.as_ref();
    }
        fn closure_evidence<'a>(&'a self) -> Option<&'a str> {
        return self.closure_evidence.as_deref();
    }
}


pub trait CorrectiveAction : NamedEntity   {

    fn linked_nonconformity<'a>(&'a self) -> Option<&'a str>;
    // fn linked_nonconformity_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_linked_nonconformity<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn action_description<'a>(&'a self) -> Option<&'a str>;
    // fn action_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_action_description(&mut self, value: Option<&'a str>);

    fn root_cause_addressed<'a>(&'a self) -> Option<&'a str>;
    // fn root_cause_addressed_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_root_cause_addressed(&mut self, value: Option<&'a str>);

    fn responsible_party<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_party_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_party(&mut self, value: Option<&'a str>);

    fn target_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn target_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_target_completion_date(&mut self, value: Option<&'a NaiveDate>);

    fn actual_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn actual_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_actual_completion_date(&mut self, value: Option<&'a NaiveDate>);

    fn resources_required<'a>(&'a self) -> Option<&'a str>;
    // fn resources_required_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resources_required(&mut self, value: Option<&'a str>);

    fn effectiveness_criteria<'a>(&'a self) -> Option<&'a str>;
    // fn effectiveness_criteria_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_effectiveness_criteria(&mut self, value: Option<&'a str>);

    fn effectiveness_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn effectiveness_review_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_effectiveness_review_date(&mut self, value: Option<&'a NaiveDate>);

    fn effectiveness_verified(&self) -> Option<bool>;
    // fn effectiveness_verified_mut(&mut self) -> &mut Option<bool>;
    // fn set_effectiveness_verified(&mut self, value: Option<bool>);

    fn isms_changes_required<'a>(&'a self) -> Option<&'a str>;
    // fn isms_changes_required_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_isms_changes_required(&mut self, value: Option<&'a str>);

    fn status<'a>(&'a self) -> Option<&'a str>;
    // fn status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_status(&mut self, value: Option<&'a str>);


}

impl CorrectiveAction for crate::CorrectiveAction {
        fn linked_nonconformity<'a>(&'a self) -> Option<&'a str> {
        return self.linked_nonconformity.as_deref();
    }
        fn action_description<'a>(&'a self) -> Option<&'a str> {
        return self.action_description.as_deref();
    }
        fn root_cause_addressed<'a>(&'a self) -> Option<&'a str> {
        return self.root_cause_addressed.as_deref();
    }
        fn responsible_party<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_party.as_deref();
    }
        fn target_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.target_completion_date.as_ref();
    }
        fn actual_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.actual_completion_date.as_ref();
    }
        fn resources_required<'a>(&'a self) -> Option<&'a str> {
        return self.resources_required.as_deref();
    }
        fn effectiveness_criteria<'a>(&'a self) -> Option<&'a str> {
        return self.effectiveness_criteria.as_deref();
    }
        fn effectiveness_review_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.effectiveness_review_date.as_ref();
    }
        fn effectiveness_verified(&self) -> Option<bool> {
        return self.effectiveness_verified;
    }
        fn isms_changes_required<'a>(&'a self) -> Option<&'a str> {
        return self.isms_changes_required.as_deref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
}


pub trait ImprovementOpportunity : NamedEntity   {

    fn improvement_source<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_source_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_source(&mut self, value: Option<&'a str>);

    fn identification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn identification_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_identification_date(&mut self, value: Option<&'a NaiveDate>);

    fn identified_by<'a>(&'a self) -> Option<&'a str>;
    // fn identified_by_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_identified_by(&mut self, value: Option<&'a str>);

    fn improvement_description<'a>(&'a self) -> Option<&'a str>;
    // fn improvement_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_improvement_description(&mut self, value: Option<&'a str>);

    fn expected_benefit<'a>(&'a self) -> Option<&'a str>;
    // fn expected_benefit_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_expected_benefit(&mut self, value: Option<&'a str>);

    fn priority<'a>(&'a self) -> Option<&'a str>;
    // fn priority_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_priority(&mut self, value: Option<&'a str>);

    fn implementation_plan<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_plan_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_plan(&mut self, value: Option<&'a str>);

    fn responsible_party<'a>(&'a self) -> Option<&'a str>;
    // fn responsible_party_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsible_party(&mut self, value: Option<&'a str>);

    fn target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn target_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_target_date(&mut self, value: Option<&'a NaiveDate>);

    fn actual_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn actual_completion_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_actual_completion_date(&mut self, value: Option<&'a NaiveDate>);

    fn outcome_assessment<'a>(&'a self) -> Option<&'a str>;
    // fn outcome_assessment_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_outcome_assessment(&mut self, value: Option<&'a str>);

    fn status<'a>(&'a self) -> Option<&'a str>;
    // fn status_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_status(&mut self, value: Option<&'a str>);


}

impl ImprovementOpportunity for crate::ImprovementOpportunity {
        fn improvement_source<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_source.as_deref();
    }
        fn identification_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.identification_date.as_ref();
    }
        fn identified_by<'a>(&'a self) -> Option<&'a str> {
        return self.identified_by.as_deref();
    }
        fn improvement_description<'a>(&'a self) -> Option<&'a str> {
        return self.improvement_description.as_deref();
    }
        fn expected_benefit<'a>(&'a self) -> Option<&'a str> {
        return self.expected_benefit.as_deref();
    }
        fn priority<'a>(&'a self) -> Option<&'a str> {
        return self.priority.as_deref();
    }
        fn implementation_plan<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_plan.as_deref();
    }
        fn responsible_party<'a>(&'a self) -> Option<&'a str> {
        return self.responsible_party.as_deref();
    }
        fn target_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.target_date.as_ref();
    }
        fn actual_completion_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.actual_completion_date.as_ref();
    }
        fn outcome_assessment<'a>(&'a self) -> Option<&'a str> {
        return self.outcome_assessment.as_deref();
    }
        fn status<'a>(&'a self) -> Option<&'a str> {
        return self.status.as_deref();
    }
}


pub trait Asset : NamedEntity   {

    fn asset_type<'a>(&'a self) -> Option<&'a str>;
    // fn asset_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_type(&mut self, value: Option<&'a str>);

    fn asset_owner<'a>(&'a self) -> Option<&'a str>;
    // fn asset_owner_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_owner(&mut self, value: Option<&'a str>);

    fn asset_custodian<'a>(&'a self) -> Option<&'a str>;
    // fn asset_custodian_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_asset_custodian(&mut self, value: Option<&'a str>);

    fn classification<'a>(&'a self) -> Option<&'a str>;
    // fn classification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_classification(&mut self, value: Option<&'a str>);

    fn location<'a>(&'a self) -> Option<&'a str>;
    // fn location_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_location(&mut self, value: Option<&'a str>);

    fn criticality<'a>(&'a self) -> Option<&'a str>;
    // fn criticality_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_criticality(&mut self, value: Option<&'a str>);

    fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn related_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_related_risks<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn applicable_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn applicable_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_applicable_controls<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl Asset for crate::Asset {
        fn asset_type<'a>(&'a self) -> Option<&'a str> {
        return self.asset_type.as_deref();
    }
        fn asset_owner<'a>(&'a self) -> Option<&'a str> {
        return self.asset_owner.as_deref();
    }
        fn asset_custodian<'a>(&'a self) -> Option<&'a str> {
        return self.asset_custodian.as_deref();
    }
        fn classification<'a>(&'a self) -> Option<&'a str> {
        return self.classification.as_deref();
    }
        fn location<'a>(&'a self) -> Option<&'a str> {
        return self.location.as_deref();
    }
        fn criticality<'a>(&'a self) -> Option<&'a str> {
        return self.criticality.as_deref();
    }
        fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.related_risks.as_ref();
    }
        fn applicable_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.applicable_controls.as_ref();
    }
}


pub trait InformationSecurityEvent : NamedEntity   {

    fn event_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime>;
    // fn event_datetime_mut(&mut self) -> &mut Option<&'a crate::NaiveDateTime>;
    // fn set_event_datetime(&mut self, value: Option<&'a NaiveDateTime>);

    fn reporter<'a>(&'a self) -> Option<&'a str>;
    // fn reporter_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_reporter(&mut self, value: Option<&'a str>);

    fn event_description<'a>(&'a self) -> Option<&'a str>;
    // fn event_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_event_description(&mut self, value: Option<&'a str>);

    fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn affected_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_affected_assets<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn initial_assessment<'a>(&'a self) -> Option<&'a str>;
    // fn initial_assessment_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_initial_assessment(&mut self, value: Option<&'a str>);

    fn categorized_as_incident(&self) -> Option<bool>;
    // fn categorized_as_incident_mut(&mut self) -> &mut Option<bool>;
    // fn set_categorized_as_incident(&mut self, value: Option<bool>);

    fn linked_incident<'a>(&'a self) -> Option<&'a str>;
    // fn linked_incident_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_linked_incident<E>(&mut self, value: Option<&'a str>) where E: Into<String>;


}

impl InformationSecurityEvent for crate::InformationSecurityEvent {
        fn event_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.event_datetime.as_ref();
    }
        fn reporter<'a>(&'a self) -> Option<&'a str> {
        return self.reporter.as_deref();
    }
        fn event_description<'a>(&'a self) -> Option<&'a str> {
        return self.event_description.as_deref();
    }
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn initial_assessment<'a>(&'a self) -> Option<&'a str> {
        return self.initial_assessment.as_deref();
    }
        fn categorized_as_incident(&self) -> Option<bool> {
        return self.categorized_as_incident;
    }
        fn linked_incident<'a>(&'a self) -> Option<&'a str> {
        return self.linked_incident.as_deref();
    }
}


pub trait InformationSecurityIncident : NamedEntity   {

    fn incident_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime>;
    // fn incident_datetime_mut(&mut self) -> &mut Option<&'a crate::NaiveDateTime>;
    // fn set_incident_datetime(&mut self, value: Option<&'a NaiveDateTime>);

    fn incident_category<'a>(&'a self) -> Option<&'a crate::SecurityIncidentCategory>;
    // fn incident_category_mut(&mut self) -> &mut Option<&'a crate::SecurityIncidentCategory>;
    // fn set_incident_category(&mut self, value: Option<&'a SecurityIncidentCategory>);

    fn severity<'a>(&'a self) -> Option<&'a crate::RiskLevel>;
    // fn severity_mut(&mut self) -> &mut Option<&'a crate::RiskLevel>;
    // fn set_severity(&mut self, value: Option<&'a RiskLevel>);

    fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn affected_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_affected_assets<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;

    fn affected_cia<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>>;
    // fn affected_cia_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>>;
    // fn set_affected_cia(&mut self, value: Option<&Vec<CIAProperty>>);

    fn incident_description<'a>(&'a self) -> Option<&'a str>;
    // fn incident_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_incident_description(&mut self, value: Option<&'a str>);

    fn detection_method<'a>(&'a self) -> Option<&'a str>;
    // fn detection_method_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_detection_method(&mut self, value: Option<&'a str>);

    fn response_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn response_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_response_actions(&mut self, value: Option<&Vec<String>>);

    fn containment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn containment_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_containment_actions(&mut self, value: Option<&Vec<String>>);

    fn eradication_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn eradication_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_eradication_actions(&mut self, value: Option<&Vec<String>>);

    fn recovery_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn recovery_actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_recovery_actions(&mut self, value: Option<&Vec<String>>);

    fn root_cause<'a>(&'a self) -> Option<&'a str>;
    // fn root_cause_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_root_cause(&mut self, value: Option<&'a str>);

    fn lessons_learned<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn lessons_learned_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_lessons_learned(&mut self, value: Option<&Vec<String>>);

    fn evidence_collected<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn evidence_collected_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_evidence_collected(&mut self, value: Option<&Vec<String>>);

    fn notification_required(&self) -> Option<bool>;
    // fn notification_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_notification_required(&mut self, value: Option<bool>);

    fn notifications_made<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn notifications_made_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_notifications_made(&mut self, value: Option<&Vec<String>>);

    fn closure_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime>;
    // fn closure_datetime_mut(&mut self) -> &mut Option<&'a crate::NaiveDateTime>;
    // fn set_closure_datetime(&mut self, value: Option<&'a NaiveDateTime>);

    fn post_incident_review<'a>(&'a self) -> Option<&'a str>;
    // fn post_incident_review_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_post_incident_review(&mut self, value: Option<&'a str>);


}

impl InformationSecurityIncident for crate::InformationSecurityIncident {
        fn incident_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.incident_datetime.as_ref();
    }
        fn incident_category<'a>(&'a self) -> Option<&'a crate::SecurityIncidentCategory> {
        return self.incident_category.as_ref();
    }
        fn severity<'a>(&'a self) -> Option<&'a crate::RiskLevel> {
        return self.severity.as_ref();
    }
        fn affected_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.affected_assets.as_ref();
    }
        fn affected_cia<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CIAProperty>> {
        return self.affected_cia.as_ref();
    }
        fn incident_description<'a>(&'a self) -> Option<&'a str> {
        return self.incident_description.as_deref();
    }
        fn detection_method<'a>(&'a self) -> Option<&'a str> {
        return self.detection_method.as_deref();
    }
        fn response_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.response_actions.as_ref();
    }
        fn containment_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.containment_actions.as_ref();
    }
        fn eradication_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.eradication_actions.as_ref();
    }
        fn recovery_actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.recovery_actions.as_ref();
    }
        fn root_cause<'a>(&'a self) -> Option<&'a str> {
        return self.root_cause.as_deref();
    }
        fn lessons_learned<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.lessons_learned.as_ref();
    }
        fn evidence_collected<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.evidence_collected.as_ref();
    }
        fn notification_required(&self) -> Option<bool> {
        return self.notification_required;
    }
        fn notifications_made<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.notifications_made.as_ref();
    }
        fn closure_datetime<'a>(&'a self) -> Option<&'a crate::NaiveDateTime> {
        return self.closure_datetime.as_ref();
    }
        fn post_incident_review<'a>(&'a self) -> Option<&'a str> {
        return self.post_incident_review.as_deref();
    }
}
