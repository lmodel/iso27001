
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class NamedEntity(Base):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
    """
    __tablename__ = 'NamedEntity'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    

    def __repr__(self):
        return f"NamedEntity(id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    


class SoAEntry(Base):
    """
    A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
    """
    __tablename__ = 'SoAEntry'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    control_reference = Column(Text(), ForeignKey('SecurityControl.id'))
    is_applicable = Column(Boolean())
    inclusion_justification = Column(Text())
    exclusion_justification = Column(Text())
    implementation_status = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable', name='ImplementationStatus'))
    implementation_evidence = Column(Text())
    responsible_role = Column(Text(), ForeignKey('Role.id'))
    target_implementation_date = Column(Date())
    

    def __repr__(self):
        return f"SoAEntry(id={self.id},control_reference={self.control_reference},is_applicable={self.is_applicable},inclusion_justification={self.inclusion_justification},exclusion_justification={self.exclusion_justification},implementation_status={self.implementation_status},implementation_evidence={self.implementation_evidence},responsible_role={self.responsible_role},target_implementation_date={self.target_implementation_date},)"



    


class CommunicationItem(Base):
    """
    A single communication requirement within the communication plan.
    """
    __tablename__ = 'CommunicationItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    subject = Column(Text())
    purpose = Column(Text())
    audience = Column(Text())
    frequency = Column(Text())
    method = Column(Text())
    responsible_party = Column(Text())
    records_required = Column(Boolean())
    

    def __repr__(self):
        return f"CommunicationItem(id={self.id},subject={self.subject},purpose={self.purpose},audience={self.audience},frequency={self.frequency},method={self.method},responsible_party={self.responsible_party},records_required={self.records_required},)"



    


class MonitoringItem(Base):
    """
    A single item to be monitored and measured per 9.1.
    """
    __tablename__ = 'MonitoringItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    metric_name = Column(Text())
    metric_description = Column(Text())
    measurement_method = Column(Text())
    measurement_frequency = Column(Text())
    responsible_party = Column(Text())
    analysis_frequency = Column(Text())
    analyst = Column(Text())
    target_threshold = Column(Text())
    alert_threshold = Column(Text())
    current_value = Column(Text())
    trend = Column(Text())
    

    def __repr__(self):
        return f"MonitoringItem(id={self.id},metric_name={self.metric_name},metric_description={self.metric_description},measurement_method={self.measurement_method},measurement_frequency={self.measurement_frequency},responsible_party={self.responsible_party},analysis_frequency={self.analysis_frequency},analyst={self.analyst},target_threshold={self.target_threshold},alert_threshold={self.alert_threshold},current_value={self.current_value},trend={self.trend},)"



    


class DocumentedInformationDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'DocumentedInformation_distribution_controls'

    DocumentedInformation_id = Column(Text(), ForeignKey('DocumentedInformation.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"DocumentedInformation_distribution_controls(DocumentedInformation_id={self.DocumentedInformation_id},distribution_controls={self.distribution_controls},)"



    


class InformationSecurityManagementSystemLeadershipCommitmentEvidence(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_leadership_commitment_evidence'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    leadership_commitment_evidence = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_leadership_commitment_evidence(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},leadership_commitment_evidence={self.leadership_commitment_evidence},)"



    


class InformationSecurityManagementSystemScopeBoundaries(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_scope_boundaries'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    scope_boundaries = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_scope_boundaries(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},scope_boundaries={self.scope_boundaries},)"



    


class InformationSecurityManagementSystemScopeExclusions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_scope_exclusions'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    scope_exclusions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_scope_exclusions(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},scope_exclusions={self.scope_exclusions},)"



    


class InformationSecurityManagementSystemInterfacesAndDependencies(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_interfaces_and_dependencies'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    interfaces_and_dependencies = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_interfaces_and_dependencies(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},interfaces_and_dependencies={self.interfaces_and_dependencies},)"



    


class InformationSecurityManagementSystemContextInternalIssues(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_context_internal_issues'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    context_internal_issues = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_context_internal_issues(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},context_internal_issues={self.context_internal_issues},)"



    


class InformationSecurityManagementSystemContextExternalIssues(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_context_external_issues'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    context_external_issues = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_context_external_issues(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},context_external_issues={self.context_external_issues},)"



    


class InformationSecurityManagementSystemInterestedParties(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_interested_parties'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    interested_parties_id = Column(Text(), ForeignKey('InterestedParty.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_interested_parties(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},interested_parties_id={self.interested_parties_id},)"



    


class InformationSecurityManagementSystemObjectives(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_objectives'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    objectives_id = Column(Text(), ForeignKey('InformationSecurityObjective.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_objectives(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},objectives_id={self.objectives_id},)"



    


class InformationSecurityManagementSystemRisksAndOpportunitiesActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_risks_and_opportunities_actions'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    risks_and_opportunities_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_risks_and_opportunities_actions(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},risks_and_opportunities_actions={self.risks_and_opportunities_actions},)"



    


class InformationSecurityManagementSystemPlannedChanges(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_planned_changes'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    planned_changes = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_planned_changes(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},planned_changes={self.planned_changes},)"



    


class InformationSecurityManagementSystemExternallyProvidedServices(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_externally_provided_services'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    externally_provided_services = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_externally_provided_services(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},externally_provided_services={self.externally_provided_services},)"



    


class InformationSecurityManagementSystemControls(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_controls'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_controls(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},controls_id={self.controls_id},)"



    


class InformationSecurityManagementSystemRoles(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_roles'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    roles_id = Column(Text(), ForeignKey('Role.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_roles(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},roles_id={self.roles_id},)"



    


class InformationSecurityManagementSystemResources(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_resources'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    resources_id = Column(Text(), ForeignKey('Resource.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_resources(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},resources_id={self.resources_id},)"



    


class InformationSecurityManagementSystemCompetenceRecords(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_competence_records'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    competence_records_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_competence_records(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},competence_records_id={self.competence_records_id},)"



    


class InformationSecurityManagementSystemDocumentedInformationRegister(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_documented_information_register'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    documented_information_register_id = Column(Text(), ForeignKey('DocumentedInformation.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_documented_information_register(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},documented_information_register_id={self.documented_information_register_id},)"



    


class InformationSecurityManagementSystemOperationalProcedures(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_operational_procedures'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    operational_procedures_id = Column(Text(), ForeignKey('OperationalProcedure.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_operational_procedures(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},operational_procedures_id={self.operational_procedures_id},)"



    


class InformationSecurityManagementSystemRiskAssessments(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_risk_assessments'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    risk_assessments_id = Column(Text(), ForeignKey('RiskAssessment.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_risk_assessments(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},risk_assessments_id={self.risk_assessments_id},)"



    


class InformationSecurityManagementSystemRiskTreatmentPlans(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_risk_treatment_plans'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    risk_treatment_plans_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_risk_treatment_plans(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},risk_treatment_plans_id={self.risk_treatment_plans_id},)"



    


class InformationSecurityManagementSystemInternalAudits(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_internal_audits'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    internal_audits_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_internal_audits(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},internal_audits_id={self.internal_audits_id},)"



    


class InformationSecurityManagementSystemManagementReviews(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_management_reviews'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    management_reviews_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_management_reviews(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},management_reviews_id={self.management_reviews_id},)"



    


class InformationSecurityManagementSystemNonconformities(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_nonconformities'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    nonconformities_id = Column(Text(), ForeignKey('Nonconformity.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_nonconformities(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},nonconformities_id={self.nonconformities_id},)"



    


class InformationSecurityManagementSystemCorrectiveActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_corrective_actions'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    corrective_actions_id = Column(Text(), ForeignKey('CorrectiveAction.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_corrective_actions(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},corrective_actions_id={self.corrective_actions_id},)"



    


class InformationSecurityManagementSystemImprovements(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityManagementSystem_improvements'

    InformationSecurityManagementSystem_id = Column(Text(), ForeignKey('InformationSecurityManagementSystem.id'), primary_key=True)
    improvements_id = Column(Text(), ForeignKey('ImprovementOpportunity.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem_improvements(InformationSecurityManagementSystem_id={self.InformationSecurityManagementSystem_id},improvements_id={self.improvements_id},)"



    


class OrganizationTradingNames(Base):
    """
    None
    """
    __tablename__ = 'Organization_trading_names'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    trading_names = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_trading_names(Organization_id={self.Organization_id},trading_names={self.trading_names},)"



    


class OrganizationGeographicLocations(Base):
    """
    None
    """
    __tablename__ = 'Organization_geographic_locations'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    geographic_locations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_geographic_locations(Organization_id={self.Organization_id},geographic_locations={self.geographic_locations},)"



    


class OrganizationRegulatoryJurisdictions(Base):
    """
    None
    """
    __tablename__ = 'Organization_regulatory_jurisdictions'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    regulatory_jurisdictions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_regulatory_jurisdictions(Organization_id={self.Organization_id},regulatory_jurisdictions={self.regulatory_jurisdictions},)"



    


class OrganizationSubsidiaries(Base):
    """
    None
    """
    __tablename__ = 'Organization_subsidiaries'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    subsidiaries = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_subsidiaries(Organization_id={self.Organization_id},subsidiaries={self.subsidiaries},)"



    


class InterestedPartyRequirements(Base):
    """
    None
    """
    __tablename__ = 'InterestedParty_requirements'

    InterestedParty_id = Column(Text(), ForeignKey('InterestedParty.id'), primary_key=True)
    requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InterestedParty_requirements(InterestedParty_id={self.InterestedParty_id},requirements={self.requirements},)"



    


class InterestedPartyAddressedRequirements(Base):
    """
    None
    """
    __tablename__ = 'InterestedParty_addressed_requirements'

    InterestedParty_id = Column(Text(), ForeignKey('InterestedParty.id'), primary_key=True)
    addressed_requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InterestedParty_addressed_requirements(InterestedParty_id={self.InterestedParty_id},addressed_requirements={self.addressed_requirements},)"



    


class InterestedPartyClimateChangeRelatedRequirements(Base):
    """
    None
    """
    __tablename__ = 'InterestedParty_climate_change_related_requirements'

    InterestedParty_id = Column(Text(), ForeignKey('InterestedParty.id'), primary_key=True)
    climate_change_related_requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InterestedParty_climate_change_related_requirements(InterestedParty_id={self.InterestedParty_id},climate_change_related_requirements={self.climate_change_related_requirements},)"



    


class InformationSecurityPolicyCommitmentStatements(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityPolicy_commitment_statements'

    InformationSecurityPolicy_id = Column(Text(), ForeignKey('InformationSecurityPolicy.id'), primary_key=True)
    commitment_statements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityPolicy_commitment_statements(InformationSecurityPolicy_id={self.InformationSecurityPolicy_id},commitment_statements={self.commitment_statements},)"



    


class InformationSecurityPolicyRelatedTopicPolicies(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityPolicy_related_topic_policies'

    InformationSecurityPolicy_id = Column(Text(), ForeignKey('InformationSecurityPolicy.id'), primary_key=True)
    related_topic_policies_id = Column(Text(), ForeignKey('TopicSpecificPolicy.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityPolicy_related_topic_policies(InformationSecurityPolicy_id={self.InformationSecurityPolicy_id},related_topic_policies_id={self.related_topic_policies_id},)"



    


class InformationSecurityPolicyIntegratedManagementSystems(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityPolicy_integrated_management_systems'

    InformationSecurityPolicy_id = Column(Text(), ForeignKey('InformationSecurityPolicy.id'), primary_key=True)
    integrated_management_systems = Column(Enum('iso_iec_27001', 'iso_iec_27701', 'iso_iec_27017', 'iso_iec_27018', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1', 'iso_31000', name='RelatedManagementSystem'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityPolicy_integrated_management_systems(InformationSecurityPolicy_id={self.InformationSecurityPolicy_id},integrated_management_systems={self.integrated_management_systems},)"



    


class InformationSecurityPolicyDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityPolicy_distribution_controls'

    InformationSecurityPolicy_id = Column(Text(), ForeignKey('InformationSecurityPolicy.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityPolicy_distribution_controls(InformationSecurityPolicy_id={self.InformationSecurityPolicy_id},distribution_controls={self.distribution_controls},)"



    


class TopicSpecificPolicyApplicableControls(Base):
    """
    None
    """
    __tablename__ = 'TopicSpecificPolicy_applicable_controls'

    TopicSpecificPolicy_id = Column(Text(), ForeignKey('TopicSpecificPolicy.id'), primary_key=True)
    applicable_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"TopicSpecificPolicy_applicable_controls(TopicSpecificPolicy_id={self.TopicSpecificPolicy_id},applicable_controls_id={self.applicable_controls_id},)"



    


class TopicSpecificPolicyDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'TopicSpecificPolicy_distribution_controls'

    TopicSpecificPolicy_id = Column(Text(), ForeignKey('TopicSpecificPolicy.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"TopicSpecificPolicy_distribution_controls(TopicSpecificPolicy_id={self.TopicSpecificPolicy_id},distribution_controls={self.distribution_controls},)"



    


class RoleResponsibilities(Base):
    """
    None
    """
    __tablename__ = 'Role_responsibilities'

    Role_id = Column(Text(), ForeignKey('Role.id'), primary_key=True)
    responsibilities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Role_responsibilities(Role_id={self.Role_id},responsibilities={self.responsibilities},)"



    


class RoleAuthorities(Base):
    """
    None
    """
    __tablename__ = 'Role_authorities'

    Role_id = Column(Text(), ForeignKey('Role.id'), primary_key=True)
    authorities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Role_authorities(Role_id={self.Role_id},authorities={self.authorities},)"



    


class RoleAssignedTo(Base):
    """
    None
    """
    __tablename__ = 'Role_assigned_to'

    Role_id = Column(Text(), ForeignKey('Role.id'), primary_key=True)
    assigned_to = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Role_assigned_to(Role_id={self.Role_id},assigned_to={self.assigned_to},)"



    


class InformationSecurityObjectiveRelatedRisks(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityObjective_related_risks'

    InformationSecurityObjective_id = Column(Text(), ForeignKey('InformationSecurityObjective.id'), primary_key=True)
    related_risks_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityObjective_related_risks(InformationSecurityObjective_id={self.InformationSecurityObjective_id},related_risks_id={self.related_risks_id},)"



    


class InformationSecurityObjectiveRelatedControls(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityObjective_related_controls'

    InformationSecurityObjective_id = Column(Text(), ForeignKey('InformationSecurityObjective.id'), primary_key=True)
    related_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityObjective_related_controls(InformationSecurityObjective_id={self.InformationSecurityObjective_id},related_controls_id={self.related_controls_id},)"



    


class RiskAssessmentProcessTriggerEvents(Base):
    """
    None
    """
    __tablename__ = 'RiskAssessmentProcess_trigger_events'

    RiskAssessmentProcess_id = Column(Text(), ForeignKey('RiskAssessmentProcess.id'), primary_key=True)
    trigger_events = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskAssessmentProcess_trigger_events(RiskAssessmentProcess_id={self.RiskAssessmentProcess_id},trigger_events={self.trigger_events},)"



    


class RiskAssessmentProcessDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'RiskAssessmentProcess_distribution_controls'

    RiskAssessmentProcess_id = Column(Text(), ForeignKey('RiskAssessmentProcess.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskAssessmentProcess_distribution_controls(RiskAssessmentProcess_id={self.RiskAssessmentProcess_id},distribution_controls={self.distribution_controls},)"



    


class RiskAssessmentRisksIdentified(Base):
    """
    None
    """
    __tablename__ = 'RiskAssessment_risks_identified'

    RiskAssessment_id = Column(Text(), ForeignKey('RiskAssessment.id'), primary_key=True)
    risks_identified_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    

    def __repr__(self):
        return f"RiskAssessment_risks_identified(RiskAssessment_id={self.RiskAssessment_id},risks_identified_id={self.risks_identified_id},)"



    


class RiskAssessmentRecommendations(Base):
    """
    None
    """
    __tablename__ = 'RiskAssessment_recommendations'

    RiskAssessment_id = Column(Text(), ForeignKey('RiskAssessment.id'), primary_key=True)
    recommendations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskAssessment_recommendations(RiskAssessment_id={self.RiskAssessment_id},recommendations={self.recommendations},)"



    


class RiskAssessmentDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'RiskAssessment_distribution_controls'

    RiskAssessment_id = Column(Text(), ForeignKey('RiskAssessment.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskAssessment_distribution_controls(RiskAssessment_id={self.RiskAssessment_id},distribution_controls={self.distribution_controls},)"



    


class RiskAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'Risk_affected_assets'

    Risk_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    affected_assets_id = Column(Text(), ForeignKey('Asset.id'), primary_key=True)
    

    def __repr__(self):
        return f"Risk_affected_assets(Risk_id={self.Risk_id},affected_assets_id={self.affected_assets_id},)"



    


class RiskAffectedCiaProperties(Base):
    """
    None
    """
    __tablename__ = 'Risk_affected_cia_properties'

    Risk_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    affected_cia_properties = Column(Enum('confidentiality', 'integrity', 'availability', name='CIAProperty'), primary_key=True)
    

    def __repr__(self):
        return f"Risk_affected_cia_properties(Risk_id={self.Risk_id},affected_cia_properties={self.affected_cia_properties},)"



    


class RiskExistingControls(Base):
    """
    None
    """
    __tablename__ = 'Risk_existing_controls'

    Risk_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    existing_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"Risk_existing_controls(Risk_id={self.Risk_id},existing_controls_id={self.existing_controls_id},)"



    


class RiskTreatmentProcessDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentProcess_distribution_controls'

    RiskTreatmentProcess_id = Column(Text(), ForeignKey('RiskTreatmentProcess.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentProcess_distribution_controls(RiskTreatmentProcess_id={self.RiskTreatmentProcess_id},distribution_controls={self.distribution_controls},)"



    


class RiskTreatmentPlanRisksAddressed(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentPlan_risks_addressed'

    RiskTreatmentPlan_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    risks_addressed_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentPlan_risks_addressed(RiskTreatmentPlan_id={self.RiskTreatmentPlan_id},risks_addressed_id={self.risks_addressed_id},)"



    


class RiskTreatmentPlanTreatmentActions(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentPlan_treatment_actions'

    RiskTreatmentPlan_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    treatment_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentPlan_treatment_actions(RiskTreatmentPlan_id={self.RiskTreatmentPlan_id},treatment_actions={self.treatment_actions},)"



    


class RiskTreatmentPlanControlsToImplement(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentPlan_controls_to_implement'

    RiskTreatmentPlan_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    controls_to_implement_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentPlan_controls_to_implement(RiskTreatmentPlan_id={self.RiskTreatmentPlan_id},controls_to_implement_id={self.controls_to_implement_id},)"



    


class RiskTreatmentPlanResponsibleParties(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentPlan_responsible_parties'

    RiskTreatmentPlan_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    responsible_parties = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentPlan_responsible_parties(RiskTreatmentPlan_id={self.RiskTreatmentPlan_id},responsible_parties={self.responsible_parties},)"



    


class RiskTreatmentPlanDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'RiskTreatmentPlan_distribution_controls'

    RiskTreatmentPlan_id = Column(Text(), ForeignKey('RiskTreatmentPlan.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RiskTreatmentPlan_distribution_controls(RiskTreatmentPlan_id={self.RiskTreatmentPlan_id},distribution_controls={self.distribution_controls},)"



    


class StatementOfApplicabilitySoaEntries(Base):
    """
    None
    """
    __tablename__ = 'StatementOfApplicability_soa_entries'

    StatementOfApplicability_id = Column(Text(), ForeignKey('StatementOfApplicability.id'), primary_key=True)
    soa_entries_id = Column(Integer(), ForeignKey('SoAEntry.id'), primary_key=True)
    

    def __repr__(self):
        return f"StatementOfApplicability_soa_entries(StatementOfApplicability_id={self.StatementOfApplicability_id},soa_entries_id={self.soa_entries_id},)"



    


class StatementOfApplicabilityDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'StatementOfApplicability_distribution_controls'

    StatementOfApplicability_id = Column(Text(), ForeignKey('StatementOfApplicability.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"StatementOfApplicability_distribution_controls(StatementOfApplicability_id={self.StatementOfApplicability_id},distribution_controls={self.distribution_controls},)"



    


class SecurityControlRelatedControls(Base):
    """
    None
    """
    __tablename__ = 'SecurityControl_related_controls'

    SecurityControl_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    related_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"SecurityControl_related_controls(SecurityControl_id={self.SecurityControl_id},related_controls_id={self.related_controls_id},)"



    


class SecurityControlApplicableThreats(Base):
    """
    None
    """
    __tablename__ = 'SecurityControl_applicable_threats'

    SecurityControl_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    applicable_threats = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SecurityControl_applicable_threats(SecurityControl_id={self.SecurityControl_id},applicable_threats={self.applicable_threats},)"



    


class SecurityControlApplicableAssets(Base):
    """
    None
    """
    __tablename__ = 'SecurityControl_applicable_assets'

    SecurityControl_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    applicable_assets = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SecurityControl_applicable_assets(SecurityControl_id={self.SecurityControl_id},applicable_assets={self.applicable_assets},)"



    


class SecurityControlEvidenceReferences(Base):
    """
    None
    """
    __tablename__ = 'SecurityControl_evidence_references'

    SecurityControl_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    evidence_references = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SecurityControl_evidence_references(SecurityControl_id={self.SecurityControl_id},evidence_references={self.evidence_references},)"



    


class CompetenceRecordRequiredCompetencies(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_required_competencies'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    required_competencies = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_required_competencies(CompetenceRecord_id={self.CompetenceRecord_id},required_competencies={self.required_competencies},)"



    


class CompetenceRecordEducationRecords(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_education_records'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    education_records = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_education_records(CompetenceRecord_id={self.CompetenceRecord_id},education_records={self.education_records},)"



    


class CompetenceRecordTrainingRecords(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_training_records'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    training_records = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_training_records(CompetenceRecord_id={self.CompetenceRecord_id},training_records={self.training_records},)"



    


class CompetenceRecordExperienceRecords(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_experience_records'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    experience_records = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_experience_records(CompetenceRecord_id={self.CompetenceRecord_id},experience_records={self.experience_records},)"



    


class CompetenceRecordCompetencyGaps(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_competency_gaps'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    competency_gaps = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_competency_gaps(CompetenceRecord_id={self.CompetenceRecord_id},competency_gaps={self.competency_gaps},)"



    


class CompetenceRecordDevelopmentActions(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_development_actions'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    development_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_development_actions(CompetenceRecord_id={self.CompetenceRecord_id},development_actions={self.development_actions},)"



    


class CompetenceRecordDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'CompetenceRecord_distribution_controls'

    CompetenceRecord_id = Column(Text(), ForeignKey('CompetenceRecord.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CompetenceRecord_distribution_controls(CompetenceRecord_id={self.CompetenceRecord_id},distribution_controls={self.distribution_controls},)"



    


class AwarenessProgramAwarenessTopics(Base):
    """
    None
    """
    __tablename__ = 'AwarenessProgram_awareness_topics'

    AwarenessProgram_id = Column(Text(), ForeignKey('AwarenessProgram.id'), primary_key=True)
    awareness_topics = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AwarenessProgram_awareness_topics(AwarenessProgram_id={self.AwarenessProgram_id},awareness_topics={self.awareness_topics},)"



    


class AwarenessProgramDeliveryMethods(Base):
    """
    None
    """
    __tablename__ = 'AwarenessProgram_delivery_methods'

    AwarenessProgram_id = Column(Text(), ForeignKey('AwarenessProgram.id'), primary_key=True)
    delivery_methods = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AwarenessProgram_delivery_methods(AwarenessProgram_id={self.AwarenessProgram_id},delivery_methods={self.delivery_methods},)"



    


class AwarenessProgramDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'AwarenessProgram_distribution_controls'

    AwarenessProgram_id = Column(Text(), ForeignKey('AwarenessProgram.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AwarenessProgram_distribution_controls(AwarenessProgram_id={self.AwarenessProgram_id},distribution_controls={self.distribution_controls},)"



    


class CommunicationPlanCommunicationItems(Base):
    """
    None
    """
    __tablename__ = 'CommunicationPlan_communication_items'

    CommunicationPlan_id = Column(Text(), ForeignKey('CommunicationPlan.id'), primary_key=True)
    communication_items_id = Column(Integer(), ForeignKey('CommunicationItem.id'), primary_key=True)
    

    def __repr__(self):
        return f"CommunicationPlan_communication_items(CommunicationPlan_id={self.CommunicationPlan_id},communication_items_id={self.communication_items_id},)"



    


class CommunicationPlanDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'CommunicationPlan_distribution_controls'

    CommunicationPlan_id = Column(Text(), ForeignKey('CommunicationPlan.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CommunicationPlan_distribution_controls(CommunicationPlan_id={self.CommunicationPlan_id},distribution_controls={self.distribution_controls},)"



    


class OperationalProcedureControlMeasures(Base):
    """
    None
    """
    __tablename__ = 'OperationalProcedure_control_measures'

    OperationalProcedure_id = Column(Text(), ForeignKey('OperationalProcedure.id'), primary_key=True)
    control_measures = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"OperationalProcedure_control_measures(OperationalProcedure_id={self.OperationalProcedure_id},control_measures={self.control_measures},)"



    


class OperationalProcedureResponsibleRoles(Base):
    """
    None
    """
    __tablename__ = 'OperationalProcedure_responsible_roles'

    OperationalProcedure_id = Column(Text(), ForeignKey('OperationalProcedure.id'), primary_key=True)
    responsible_roles_id = Column(Text(), ForeignKey('Role.id'), primary_key=True)
    

    def __repr__(self):
        return f"OperationalProcedure_responsible_roles(OperationalProcedure_id={self.OperationalProcedure_id},responsible_roles_id={self.responsible_roles_id},)"



    


class OperationalProcedureRelatedControls(Base):
    """
    None
    """
    __tablename__ = 'OperationalProcedure_related_controls'

    OperationalProcedure_id = Column(Text(), ForeignKey('OperationalProcedure.id'), primary_key=True)
    related_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"OperationalProcedure_related_controls(OperationalProcedure_id={self.OperationalProcedure_id},related_controls_id={self.related_controls_id},)"



    


class OperationalProcedureDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'OperationalProcedure_distribution_controls'

    OperationalProcedure_id = Column(Text(), ForeignKey('OperationalProcedure.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"OperationalProcedure_distribution_controls(OperationalProcedure_id={self.OperationalProcedure_id},distribution_controls={self.distribution_controls},)"



    


class MonitoringProgramMonitoringItems(Base):
    """
    None
    """
    __tablename__ = 'MonitoringProgram_monitoring_items'

    MonitoringProgram_id = Column(Text(), ForeignKey('MonitoringProgram.id'), primary_key=True)
    monitoring_items_id = Column(Integer(), ForeignKey('MonitoringItem.id'), primary_key=True)
    

    def __repr__(self):
        return f"MonitoringProgram_monitoring_items(MonitoringProgram_id={self.MonitoringProgram_id},monitoring_items_id={self.monitoring_items_id},)"



    


class MonitoringProgramDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'MonitoringProgram_distribution_controls'

    MonitoringProgram_id = Column(Text(), ForeignKey('MonitoringProgram.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"MonitoringProgram_distribution_controls(MonitoringProgram_id={self.MonitoringProgram_id},distribution_controls={self.distribution_controls},)"



    


class InternalAuditAuditCriteria(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_audit_criteria'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    audit_criteria = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_audit_criteria(InternalAudit_id={self.InternalAudit_id},audit_criteria={self.audit_criteria},)"



    


class InternalAuditAuditObjectives(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_audit_objectives'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    audit_objectives = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_audit_objectives(InternalAudit_id={self.InternalAudit_id},audit_objectives={self.audit_objectives},)"



    


class InternalAuditAuditTeam(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_audit_team'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    audit_team = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_audit_team(InternalAudit_id={self.InternalAudit_id},audit_team={self.audit_team},)"



    


class InternalAuditAuditeeRepresentatives(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_auditee_representatives'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    auditee_representatives = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_auditee_representatives(InternalAudit_id={self.InternalAudit_id},auditee_representatives={self.auditee_representatives},)"



    


class InternalAuditFindings(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_findings'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    findings_id = Column(Text(), ForeignKey('AuditFinding.id'), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_findings(InternalAudit_id={self.InternalAudit_id},findings_id={self.findings_id},)"



    


class InternalAuditPositiveObservations(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_positive_observations'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    positive_observations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_positive_observations(InternalAudit_id={self.InternalAudit_id},positive_observations={self.positive_observations},)"



    


class InternalAuditReportDistribution(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_report_distribution'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    report_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_report_distribution(InternalAudit_id={self.InternalAudit_id},report_distribution={self.report_distribution},)"



    


class InternalAuditDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'InternalAudit_distribution_controls'

    InternalAudit_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InternalAudit_distribution_controls(InternalAudit_id={self.InternalAudit_id},distribution_controls={self.distribution_controls},)"



    


class AuditProgrammePlannedAudits(Base):
    """
    None
    """
    __tablename__ = 'AuditProgramme_planned_audits'

    AuditProgramme_id = Column(Text(), ForeignKey('AuditProgramme.id'), primary_key=True)
    planned_audits_id = Column(Text(), ForeignKey('InternalAudit.id'), primary_key=True)
    

    def __repr__(self):
        return f"AuditProgramme_planned_audits(AuditProgramme_id={self.AuditProgramme_id},planned_audits_id={self.planned_audits_id},)"



    


class AuditProgrammeDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'AuditProgramme_distribution_controls'

    AuditProgramme_id = Column(Text(), ForeignKey('AuditProgramme.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AuditProgramme_distribution_controls(AuditProgramme_id={self.AuditProgramme_id},distribution_controls={self.distribution_controls},)"



    


class ManagementReviewAttendees(Base):
    """
    None
    """
    __tablename__ = 'ManagementReview_attendees'

    ManagementReview_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    attendees = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ManagementReview_attendees(ManagementReview_id={self.ManagementReview_id},attendees={self.attendees},)"



    


class ManagementReviewImprovementOpportunities(Base):
    """
    None
    """
    __tablename__ = 'ManagementReview_improvement_opportunities'

    ManagementReview_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    improvement_opportunities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ManagementReview_improvement_opportunities(ManagementReview_id={self.ManagementReview_id},improvement_opportunities={self.improvement_opportunities},)"



    


class ManagementReviewDecisions(Base):
    """
    None
    """
    __tablename__ = 'ManagementReview_decisions'

    ManagementReview_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    decisions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ManagementReview_decisions(ManagementReview_id={self.ManagementReview_id},decisions={self.decisions},)"



    


class ManagementReviewActionItems(Base):
    """
    None
    """
    __tablename__ = 'ManagementReview_action_items'

    ManagementReview_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    action_items = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ManagementReview_action_items(ManagementReview_id={self.ManagementReview_id},action_items={self.action_items},)"



    


class ManagementReviewDistributionControls(Base):
    """
    None
    """
    __tablename__ = 'ManagementReview_distribution_controls'

    ManagementReview_id = Column(Text(), ForeignKey('ManagementReview.id'), primary_key=True)
    distribution_controls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ManagementReview_distribution_controls(ManagementReview_id={self.ManagementReview_id},distribution_controls={self.distribution_controls},)"



    


class NonconformityImmediateActions(Base):
    """
    None
    """
    __tablename__ = 'Nonconformity_immediate_actions'

    Nonconformity_id = Column(Text(), ForeignKey('Nonconformity.id'), primary_key=True)
    immediate_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Nonconformity_immediate_actions(Nonconformity_id={self.Nonconformity_id},immediate_actions={self.immediate_actions},)"



    


class NonconformityLinkedCorrectiveActions(Base):
    """
    None
    """
    __tablename__ = 'Nonconformity_linked_corrective_actions'

    Nonconformity_id = Column(Text(), ForeignKey('Nonconformity.id'), primary_key=True)
    linked_corrective_actions_id = Column(Text(), ForeignKey('CorrectiveAction.id'), primary_key=True)
    

    def __repr__(self):
        return f"Nonconformity_linked_corrective_actions(Nonconformity_id={self.Nonconformity_id},linked_corrective_actions_id={self.linked_corrective_actions_id},)"



    


class AssetRelatedRisks(Base):
    """
    None
    """
    __tablename__ = 'Asset_related_risks'

    Asset_id = Column(Text(), ForeignKey('Asset.id'), primary_key=True)
    related_risks_id = Column(Text(), ForeignKey('Risk.id'), primary_key=True)
    

    def __repr__(self):
        return f"Asset_related_risks(Asset_id={self.Asset_id},related_risks_id={self.related_risks_id},)"



    


class AssetApplicableControls(Base):
    """
    None
    """
    __tablename__ = 'Asset_applicable_controls'

    Asset_id = Column(Text(), ForeignKey('Asset.id'), primary_key=True)
    applicable_controls_id = Column(Text(), ForeignKey('SecurityControl.id'), primary_key=True)
    

    def __repr__(self):
        return f"Asset_applicable_controls(Asset_id={self.Asset_id},applicable_controls_id={self.applicable_controls_id},)"



    


class InformationSecurityEventAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityEvent_affected_assets'

    InformationSecurityEvent_id = Column(Text(), ForeignKey('InformationSecurityEvent.id'), primary_key=True)
    affected_assets_id = Column(Text(), ForeignKey('Asset.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityEvent_affected_assets(InformationSecurityEvent_id={self.InformationSecurityEvent_id},affected_assets_id={self.affected_assets_id},)"



    


class InformationSecurityIncidentAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_affected_assets'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    affected_assets_id = Column(Text(), ForeignKey('Asset.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_affected_assets(InformationSecurityIncident_id={self.InformationSecurityIncident_id},affected_assets_id={self.affected_assets_id},)"



    


class InformationSecurityIncidentAffectedCia(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_affected_cia'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    affected_cia = Column(Enum('confidentiality', 'integrity', 'availability', name='CIAProperty'), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_affected_cia(InformationSecurityIncident_id={self.InformationSecurityIncident_id},affected_cia={self.affected_cia},)"



    


class InformationSecurityIncidentResponseActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_response_actions'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    response_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_response_actions(InformationSecurityIncident_id={self.InformationSecurityIncident_id},response_actions={self.response_actions},)"



    


class InformationSecurityIncidentContainmentActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_containment_actions'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    containment_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_containment_actions(InformationSecurityIncident_id={self.InformationSecurityIncident_id},containment_actions={self.containment_actions},)"



    


class InformationSecurityIncidentEradicationActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_eradication_actions'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    eradication_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_eradication_actions(InformationSecurityIncident_id={self.InformationSecurityIncident_id},eradication_actions={self.eradication_actions},)"



    


class InformationSecurityIncidentRecoveryActions(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_recovery_actions'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    recovery_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_recovery_actions(InformationSecurityIncident_id={self.InformationSecurityIncident_id},recovery_actions={self.recovery_actions},)"



    


class InformationSecurityIncidentLessonsLearned(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_lessons_learned'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    lessons_learned = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_lessons_learned(InformationSecurityIncident_id={self.InformationSecurityIncident_id},lessons_learned={self.lessons_learned},)"



    


class InformationSecurityIncidentEvidenceCollected(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_evidence_collected'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    evidence_collected = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_evidence_collected(InformationSecurityIncident_id={self.InformationSecurityIncident_id},evidence_collected={self.evidence_collected},)"



    


class InformationSecurityIncidentNotificationsMade(Base):
    """
    None
    """
    __tablename__ = 'InformationSecurityIncident_notifications_made'

    InformationSecurityIncident_id = Column(Text(), ForeignKey('InformationSecurityIncident.id'), primary_key=True)
    notifications_made = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationSecurityIncident_notifications_made(InformationSecurityIncident_id={self.InformationSecurityIncident_id},notifications_made={self.notifications_made},)"



    


class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
    """
    __tablename__ = 'DocumentedInformation'

    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    distribution_controls_rel = relationship( "DocumentedInformationDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: DocumentedInformationDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"DocumentedInformation(document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationSecurityManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required to support the full ISMS lifecycle.
    """
    __tablename__ = 'InformationSecurityManagementSystem'

    organization = Column(Text(), ForeignKey('Organization.id'))
    top_management = Column(Text())
    governing_body = Column(Text())
    scope_statement = Column(Text())
    processes_and_interactions = Column(Text())
    information_security_policy = Column(Text(), ForeignKey('InformationSecurityPolicy.id'))
    risk_assessment_process = Column(Text(), ForeignKey('RiskAssessmentProcess.id'))
    risk_treatment_process = Column(Text(), ForeignKey('RiskTreatmentProcess.id'))
    statement_of_applicability = Column(Text(), ForeignKey('StatementOfApplicability.id'))
    awareness_program = Column(Text(), ForeignKey('AwarenessProgram.id'))
    communication_plan = Column(Text(), ForeignKey('CommunicationPlan.id'))
    monitoring_program = Column(Text(), ForeignKey('MonitoringProgram.id'))
    certification_status = Column(Text())
    certification_body = Column(Text())
    certification_date = Column(Date())
    recertification_date = Column(Date())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    leadership_commitment_evidence_rel = relationship( "InformationSecurityManagementSystemLeadershipCommitmentEvidence" )
    leadership_commitment_evidence = association_proxy("leadership_commitment_evidence_rel", "leadership_commitment_evidence",
                                  creator=lambda x_: InformationSecurityManagementSystemLeadershipCommitmentEvidence(leadership_commitment_evidence=x_))
    
    
    scope_boundaries_rel = relationship( "InformationSecurityManagementSystemScopeBoundaries" )
    scope_boundaries = association_proxy("scope_boundaries_rel", "scope_boundaries",
                                  creator=lambda x_: InformationSecurityManagementSystemScopeBoundaries(scope_boundaries=x_))
    
    
    scope_exclusions_rel = relationship( "InformationSecurityManagementSystemScopeExclusions" )
    scope_exclusions = association_proxy("scope_exclusions_rel", "scope_exclusions",
                                  creator=lambda x_: InformationSecurityManagementSystemScopeExclusions(scope_exclusions=x_))
    
    
    interfaces_and_dependencies_rel = relationship( "InformationSecurityManagementSystemInterfacesAndDependencies" )
    interfaces_and_dependencies = association_proxy("interfaces_and_dependencies_rel", "interfaces_and_dependencies",
                                  creator=lambda x_: InformationSecurityManagementSystemInterfacesAndDependencies(interfaces_and_dependencies=x_))
    
    
    context_internal_issues_rel = relationship( "InformationSecurityManagementSystemContextInternalIssues" )
    context_internal_issues = association_proxy("context_internal_issues_rel", "context_internal_issues",
                                  creator=lambda x_: InformationSecurityManagementSystemContextInternalIssues(context_internal_issues=x_))
    
    
    context_external_issues_rel = relationship( "InformationSecurityManagementSystemContextExternalIssues" )
    context_external_issues = association_proxy("context_external_issues_rel", "context_external_issues",
                                  creator=lambda x_: InformationSecurityManagementSystemContextExternalIssues(context_external_issues=x_))
    
    
    # ManyToMany
    interested_parties = relationship( "InterestedParty", secondary="InformationSecurityManagementSystem_interested_parties")
    
    
    # ManyToMany
    objectives = relationship( "InformationSecurityObjective", secondary="InformationSecurityManagementSystem_objectives")
    
    
    risks_and_opportunities_actions_rel = relationship( "InformationSecurityManagementSystemRisksAndOpportunitiesActions" )
    risks_and_opportunities_actions = association_proxy("risks_and_opportunities_actions_rel", "risks_and_opportunities_actions",
                                  creator=lambda x_: InformationSecurityManagementSystemRisksAndOpportunitiesActions(risks_and_opportunities_actions=x_))
    
    
    planned_changes_rel = relationship( "InformationSecurityManagementSystemPlannedChanges" )
    planned_changes = association_proxy("planned_changes_rel", "planned_changes",
                                  creator=lambda x_: InformationSecurityManagementSystemPlannedChanges(planned_changes=x_))
    
    
    externally_provided_services_rel = relationship( "InformationSecurityManagementSystemExternallyProvidedServices" )
    externally_provided_services = association_proxy("externally_provided_services_rel", "externally_provided_services",
                                  creator=lambda x_: InformationSecurityManagementSystemExternallyProvidedServices(externally_provided_services=x_))
    
    
    # ManyToMany
    controls = relationship( "SecurityControl", secondary="InformationSecurityManagementSystem_controls")
    
    
    # ManyToMany
    roles = relationship( "Role", secondary="InformationSecurityManagementSystem_roles")
    
    
    # ManyToMany
    resources = relationship( "Resource", secondary="InformationSecurityManagementSystem_resources")
    
    
    # ManyToMany
    competence_records = relationship( "CompetenceRecord", secondary="InformationSecurityManagementSystem_competence_records")
    
    
    # ManyToMany
    documented_information_register = relationship( "DocumentedInformation", secondary="InformationSecurityManagementSystem_documented_information_register")
    
    
    # ManyToMany
    operational_procedures = relationship( "OperationalProcedure", secondary="InformationSecurityManagementSystem_operational_procedures")
    
    
    # ManyToMany
    risk_assessments = relationship( "RiskAssessment", secondary="InformationSecurityManagementSystem_risk_assessments")
    
    
    # ManyToMany
    risk_treatment_plans = relationship( "RiskTreatmentPlan", secondary="InformationSecurityManagementSystem_risk_treatment_plans")
    
    
    # ManyToMany
    internal_audits = relationship( "InternalAudit", secondary="InformationSecurityManagementSystem_internal_audits")
    
    
    # ManyToMany
    management_reviews = relationship( "ManagementReview", secondary="InformationSecurityManagementSystem_management_reviews")
    
    
    # ManyToMany
    nonconformities = relationship( "Nonconformity", secondary="InformationSecurityManagementSystem_nonconformities")
    
    
    # ManyToMany
    corrective_actions = relationship( "CorrectiveAction", secondary="InformationSecurityManagementSystem_corrective_actions")
    
    
    # ManyToMany
    improvements = relationship( "ImprovementOpportunity", secondary="InformationSecurityManagementSystem_improvements")
    

    def __repr__(self):
        return f"InformationSecurityManagementSystem(organization={self.organization},top_management={self.top_management},governing_body={self.governing_body},scope_statement={self.scope_statement},processes_and_interactions={self.processes_and_interactions},information_security_policy={self.information_security_policy},risk_assessment_process={self.risk_assessment_process},risk_treatment_process={self.risk_treatment_process},statement_of_applicability={self.statement_of_applicability},awareness_program={self.awareness_program},communication_plan={self.communication_plan},monitoring_program={self.monitoring_program},certification_status={self.certification_status},certification_body={self.certification_body},certification_date={self.certification_date},recertification_date={self.recertification_date},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Organization(NamedEntity):
    """
    The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
    """
    __tablename__ = 'Organization'

    legal_name = Column(Text())
    organization_type = Column(Text())
    industry_sector = Column(Text())
    size_category = Column(Text())
    employee_count = Column(Integer())
    parent_organization = Column(Text())
    climate_change_relevant = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    trading_names_rel = relationship( "OrganizationTradingNames" )
    trading_names = association_proxy("trading_names_rel", "trading_names",
                                  creator=lambda x_: OrganizationTradingNames(trading_names=x_))
    
    
    geographic_locations_rel = relationship( "OrganizationGeographicLocations" )
    geographic_locations = association_proxy("geographic_locations_rel", "geographic_locations",
                                  creator=lambda x_: OrganizationGeographicLocations(geographic_locations=x_))
    
    
    regulatory_jurisdictions_rel = relationship( "OrganizationRegulatoryJurisdictions" )
    regulatory_jurisdictions = association_proxy("regulatory_jurisdictions_rel", "regulatory_jurisdictions",
                                  creator=lambda x_: OrganizationRegulatoryJurisdictions(regulatory_jurisdictions=x_))
    
    
    subsidiaries_rel = relationship( "OrganizationSubsidiaries" )
    subsidiaries = association_proxy("subsidiaries_rel", "subsidiaries",
                                  creator=lambda x_: OrganizationSubsidiaries(subsidiaries=x_))
    

    def __repr__(self):
        return f"Organization(legal_name={self.legal_name},organization_type={self.organization_type},industry_sector={self.industry_sector},size_category={self.size_category},employee_count={self.employee_count},parent_organization={self.parent_organization},climate_change_relevant={self.climate_change_relevant},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
    """
    __tablename__ = 'InterestedParty'

    party_type = Column(Text())
    relationship = Column(Text())
    communication_needs = Column(Text())
    contact_information = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    requirements_rel = relationship( "InterestedPartyRequirements" )
    requirements = association_proxy("requirements_rel", "requirements",
                                  creator=lambda x_: InterestedPartyRequirements(requirements=x_))
    
    
    addressed_requirements_rel = relationship( "InterestedPartyAddressedRequirements" )
    addressed_requirements = association_proxy("addressed_requirements_rel", "addressed_requirements",
                                  creator=lambda x_: InterestedPartyAddressedRequirements(addressed_requirements=x_))
    
    
    climate_change_related_requirements_rel = relationship( "InterestedPartyClimateChangeRelatedRequirements" )
    climate_change_related_requirements = association_proxy("climate_change_related_requirements_rel", "climate_change_related_requirements",
                                  creator=lambda x_: InterestedPartyClimateChangeRelatedRequirements(climate_change_related_requirements=x_))
    

    def __repr__(self):
        return f"InterestedParty(party_type={self.party_type},relationship={self.relationship},communication_needs={self.communication_needs},contact_information={self.contact_information},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Role(NamedEntity):
    """
    An information security role with defined responsibilities and authorities per Clause 5.3.
    """
    __tablename__ = 'Role'

    role_type = Column(Text())
    accountability = Column(Text())
    delegation_rules = Column(Text())
    reporting_line = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    responsibilities_rel = relationship( "RoleResponsibilities" )
    responsibilities = association_proxy("responsibilities_rel", "responsibilities",
                                  creator=lambda x_: RoleResponsibilities(responsibilities=x_))
    
    
    authorities_rel = relationship( "RoleAuthorities" )
    authorities = association_proxy("authorities_rel", "authorities",
                                  creator=lambda x_: RoleAuthorities(authorities=x_))
    
    
    assigned_to_rel = relationship( "RoleAssignedTo" )
    assigned_to = association_proxy("assigned_to_rel", "assigned_to",
                                  creator=lambda x_: RoleAssignedTo(assigned_to=x_))
    

    def __repr__(self):
        return f"Role(role_type={self.role_type},accountability={self.accountability},delegation_rules={self.delegation_rules},reporting_line={self.reporting_line},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationSecurityObjective(NamedEntity):
    """
    A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
    """
    __tablename__ = 'InformationSecurityObjective'

    objective_statement = Column(Text())
    target_value = Column(Text())
    current_value = Column(Text())
    metric_definition = Column(Text())
    measurement_method = Column(Text())
    measurement_frequency = Column(Text())
    responsible_role = Column(Text(), ForeignKey('Role.id'))
    target_date = Column(Date())
    achievement_status = Column(Text())
    action_plan = Column(Text())
    objective_resources_required = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    related_risks = relationship( "Risk", secondary="InformationSecurityObjective_related_risks")
    
    
    # ManyToMany
    related_controls = relationship( "SecurityControl", secondary="InformationSecurityObjective_related_controls")
    

    def __repr__(self):
        return f"InformationSecurityObjective(objective_statement={self.objective_statement},target_value={self.target_value},current_value={self.current_value},metric_definition={self.metric_definition},measurement_method={self.measurement_method},measurement_frequency={self.measurement_frequency},responsible_role={self.responsible_role},target_date={self.target_date},achievement_status={self.achievement_status},action_plan={self.action_plan},objective_resources_required={self.objective_resources_required},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Risk(NamedEntity):
    """
    An identified information security risk that may affect information security properties within the ISMS scope.
    """
    __tablename__ = 'Risk'

    risk_source = Column(Text())
    threat_description = Column(Text())
    vulnerability_description = Column(Text())
    risk_owner = Column(Text())
    likelihood = Column(Enum('rare', 'unlikely', 'possible', 'likely', 'almost_certain', name='LikelihoodRating'))
    impact = Column(Enum('negligible', 'minor', 'moderate', 'major', 'severe', name='ImpactRating'))
    inherent_risk_level = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='RiskLevel'))
    residual_risk_level = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='RiskLevel'))
    risk_treatment_option = Column(Enum('modify', 'accept', 'avoid', 'share', name='RiskTreatmentOption'))
    treatment_priority = Column(Text())
    related_treatment_plan = Column(Text(), ForeignKey('RiskTreatmentPlan.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    affected_assets = relationship( "Asset", secondary="Risk_affected_assets")
    
    
    affected_cia_properties_rel = relationship( "RiskAffectedCiaProperties" )
    affected_cia_properties = association_proxy("affected_cia_properties_rel", "affected_cia_properties",
                                  creator=lambda x_: RiskAffectedCiaProperties(affected_cia_properties=x_))
    
    
    # ManyToMany
    existing_controls = relationship( "SecurityControl", secondary="Risk_existing_controls")
    

    def __repr__(self):
        return f"Risk(risk_source={self.risk_source},threat_description={self.threat_description},vulnerability_description={self.vulnerability_description},risk_owner={self.risk_owner},likelihood={self.likelihood},impact={self.impact},inherent_risk_level={self.inherent_risk_level},residual_risk_level={self.residual_risk_level},risk_treatment_option={self.risk_treatment_option},treatment_priority={self.treatment_priority},related_treatment_plan={self.related_treatment_plan},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SecurityControl(NamedEntity):
    """
    A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
    """
    __tablename__ = 'SecurityControl'

    control_id = Column(Enum('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34', name='AnnexAControlId'))
    control_title = Column(Text())
    control_category = Column(Enum('organizational', 'people', 'physical', 'technological', name='ControlCategory'))
    control_text = Column(Text())
    implementation_guidance = Column(Text())
    control_owner = Column(Text())
    implementation_status = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable', name='ImplementationStatus'))
    implementation_date = Column(Date())
    effectiveness_rating = Column(Text())
    last_test_date = Column(Date())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    related_controls = relationship( "SecurityControl", secondary="SecurityControl_related_controls")
    
    
    applicable_threats_rel = relationship( "SecurityControlApplicableThreats" )
    applicable_threats = association_proxy("applicable_threats_rel", "applicable_threats",
                                  creator=lambda x_: SecurityControlApplicableThreats(applicable_threats=x_))
    
    
    applicable_assets_rel = relationship( "SecurityControlApplicableAssets" )
    applicable_assets = association_proxy("applicable_assets_rel", "applicable_assets",
                                  creator=lambda x_: SecurityControlApplicableAssets(applicable_assets=x_))
    
    
    evidence_references_rel = relationship( "SecurityControlEvidenceReferences" )
    evidence_references = association_proxy("evidence_references_rel", "evidence_references",
                                  creator=lambda x_: SecurityControlEvidenceReferences(evidence_references=x_))
    

    def __repr__(self):
        return f"SecurityControl(control_id={self.control_id},control_title={self.control_title},control_category={self.control_category},control_text={self.control_text},implementation_guidance={self.implementation_guidance},control_owner={self.control_owner},implementation_status={self.implementation_status},implementation_date={self.implementation_date},effectiveness_rating={self.effectiveness_rating},last_test_date={self.last_test_date},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Resource(NamedEntity):
    """
    A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
    """
    __tablename__ = 'Resource'

    resource_type = Column(Text())
    quantity = Column(Text())
    allocation_date = Column(Date())
    allocated_to = Column(Text())
    cost = Column(Text())
    availability_status = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    

    def __repr__(self):
        return f"Resource(resource_type={self.resource_type},quantity={self.quantity},allocation_date={self.allocation_date},allocated_to={self.allocated_to},cost={self.cost},availability_status={self.availability_status},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AuditFinding(NamedEntity):
    """
    A finding from an internal audit, including nonconformities, observations, and positive findings.
    """
    __tablename__ = 'AuditFinding'

    finding_type = Column(Enum('major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding', name='AuditFindingType'))
    clause_reference = Column(Text())
    control_reference = Column(Text(), ForeignKey('SecurityControl.id'))
    finding_description = Column(Text())
    objective_evidence = Column(Text())
    root_cause_analysis = Column(Text())
    risk_implication = Column(Text())
    recommended_action = Column(Text())
    auditee_response = Column(Text())
    linked_corrective_action = Column(Text(), ForeignKey('CorrectiveAction.id'))
    closure_status = Column(Text())
    closure_date = Column(Date())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    

    def __repr__(self):
        return f"AuditFinding(finding_type={self.finding_type},clause_reference={self.clause_reference},control_reference={self.control_reference},finding_description={self.finding_description},objective_evidence={self.objective_evidence},root_cause_analysis={self.root_cause_analysis},risk_implication={self.risk_implication},recommended_action={self.recommended_action},auditee_response={self.auditee_response},linked_corrective_action={self.linked_corrective_action},closure_status={self.closure_status},closure_date={self.closure_date},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
    """
    __tablename__ = 'Nonconformity'

    nonconformity_source = Column(Text())
    detection_date = Column(Date())
    detected_by = Column(Text())
    requirement_violated = Column(Text())
    nonconformity_description = Column(Text())
    consequences_addressed = Column(Text())
    root_cause = Column(Text())
    similar_nonconformities_check = Column(Text())
    status = Column(Text())
    closure_date = Column(Date())
    closure_evidence = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    immediate_actions_rel = relationship( "NonconformityImmediateActions" )
    immediate_actions = association_proxy("immediate_actions_rel", "immediate_actions",
                                  creator=lambda x_: NonconformityImmediateActions(immediate_actions=x_))
    
    
    # ManyToMany
    linked_corrective_actions = relationship( "CorrectiveAction", secondary="Nonconformity_linked_corrective_actions")
    

    def __repr__(self):
        return f"Nonconformity(nonconformity_source={self.nonconformity_source},detection_date={self.detection_date},detected_by={self.detected_by},requirement_violated={self.requirement_violated},nonconformity_description={self.nonconformity_description},consequences_addressed={self.consequences_addressed},root_cause={self.root_cause},similar_nonconformities_check={self.similar_nonconformities_check},status={self.status},closure_date={self.closure_date},closure_evidence={self.closure_evidence},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of recurrence.
    """
    __tablename__ = 'CorrectiveAction'

    linked_nonconformity = Column(Text(), ForeignKey('Nonconformity.id'))
    action_description = Column(Text())
    root_cause_addressed = Column(Text())
    responsible_party = Column(Text())
    target_completion_date = Column(Date())
    actual_completion_date = Column(Date())
    resources_required = Column(Text())
    effectiveness_criteria = Column(Text())
    effectiveness_review_date = Column(Date())
    effectiveness_verified = Column(Boolean())
    isms_changes_required = Column(Text())
    status = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    

    def __repr__(self):
        return f"CorrectiveAction(linked_nonconformity={self.linked_nonconformity},action_description={self.action_description},root_cause_addressed={self.root_cause_addressed},responsible_party={self.responsible_party},target_completion_date={self.target_completion_date},actual_completion_date={self.actual_completion_date},resources_required={self.resources_required},effectiveness_criteria={self.effectiveness_criteria},effectiveness_review_date={self.effectiveness_review_date},effectiveness_verified={self.effectiveness_verified},isms_changes_required={self.isms_changes_required},status={self.status},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
    """
    __tablename__ = 'ImprovementOpportunity'

    improvement_source = Column(Text())
    identification_date = Column(Date())
    identified_by = Column(Text())
    improvement_description = Column(Text())
    expected_benefit = Column(Text())
    priority = Column(Text())
    implementation_plan = Column(Text())
    responsible_party = Column(Text())
    target_date = Column(Date())
    actual_completion_date = Column(Date())
    outcome_assessment = Column(Text())
    status = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    

    def __repr__(self):
        return f"ImprovementOpportunity(improvement_source={self.improvement_source},identification_date={self.identification_date},identified_by={self.identified_by},improvement_description={self.improvement_description},expected_benefit={self.expected_benefit},priority={self.priority},implementation_plan={self.implementation_plan},responsible_party={self.responsible_party},target_date={self.target_date},actual_completion_date={self.actual_completion_date},outcome_assessment={self.outcome_assessment},status={self.status},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Asset(NamedEntity):
    """
    An information asset or associated asset requiring protection, per Annex A control 5.9.
    """
    __tablename__ = 'Asset'

    asset_type = Column(Text())
    asset_owner = Column(Text())
    asset_custodian = Column(Text())
    classification = Column(Text())
    location = Column(Text())
    criticality = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    related_risks = relationship( "Risk", secondary="Asset_related_risks")
    
    
    # ManyToMany
    applicable_controls = relationship( "SecurityControl", secondary="Asset_applicable_controls")
    

    def __repr__(self):
        return f"Asset(asset_type={self.asset_type},asset_owner={self.asset_owner},asset_custodian={self.asset_custodian},classification={self.classification},location={self.location},criticality={self.criticality},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationSecurityEvent(NamedEntity):
    """
    An information security event per A.5.25, which may or may not be categorized as an incident.
    """
    __tablename__ = 'InformationSecurityEvent'

    event_datetime = Column(DateTime())
    reporter = Column(Text())
    event_description = Column(Text())
    initial_assessment = Column(Text())
    categorized_as_incident = Column(Boolean())
    linked_incident = Column(Text(), ForeignKey('InformationSecurityIncident.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    affected_assets = relationship( "Asset", secondary="InformationSecurityEvent_affected_assets")
    

    def __repr__(self):
        return f"InformationSecurityEvent(event_datetime={self.event_datetime},reporter={self.reporter},event_description={self.event_description},initial_assessment={self.initial_assessment},categorized_as_incident={self.categorized_as_incident},linked_incident={self.linked_incident},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationSecurityIncident(NamedEntity):
    """
    An information security incident per A.5.26, requiring response per documented procedures.
    """
    __tablename__ = 'InformationSecurityIncident'

    incident_datetime = Column(DateTime())
    incident_category = Column(Enum('malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other', name='SecurityIncidentCategory'))
    severity = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='RiskLevel'))
    incident_description = Column(Text())
    detection_method = Column(Text())
    root_cause = Column(Text())
    notification_required = Column(Boolean())
    closure_datetime = Column(DateTime())
    post_incident_review = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    affected_assets = relationship( "Asset", secondary="InformationSecurityIncident_affected_assets")
    
    
    affected_cia_rel = relationship( "InformationSecurityIncidentAffectedCia" )
    affected_cia = association_proxy("affected_cia_rel", "affected_cia",
                                  creator=lambda x_: InformationSecurityIncidentAffectedCia(affected_cia=x_))
    
    
    response_actions_rel = relationship( "InformationSecurityIncidentResponseActions" )
    response_actions = association_proxy("response_actions_rel", "response_actions",
                                  creator=lambda x_: InformationSecurityIncidentResponseActions(response_actions=x_))
    
    
    containment_actions_rel = relationship( "InformationSecurityIncidentContainmentActions" )
    containment_actions = association_proxy("containment_actions_rel", "containment_actions",
                                  creator=lambda x_: InformationSecurityIncidentContainmentActions(containment_actions=x_))
    
    
    eradication_actions_rel = relationship( "InformationSecurityIncidentEradicationActions" )
    eradication_actions = association_proxy("eradication_actions_rel", "eradication_actions",
                                  creator=lambda x_: InformationSecurityIncidentEradicationActions(eradication_actions=x_))
    
    
    recovery_actions_rel = relationship( "InformationSecurityIncidentRecoveryActions" )
    recovery_actions = association_proxy("recovery_actions_rel", "recovery_actions",
                                  creator=lambda x_: InformationSecurityIncidentRecoveryActions(recovery_actions=x_))
    
    
    lessons_learned_rel = relationship( "InformationSecurityIncidentLessonsLearned" )
    lessons_learned = association_proxy("lessons_learned_rel", "lessons_learned",
                                  creator=lambda x_: InformationSecurityIncidentLessonsLearned(lessons_learned=x_))
    
    
    evidence_collected_rel = relationship( "InformationSecurityIncidentEvidenceCollected" )
    evidence_collected = association_proxy("evidence_collected_rel", "evidence_collected",
                                  creator=lambda x_: InformationSecurityIncidentEvidenceCollected(evidence_collected=x_))
    
    
    notifications_made_rel = relationship( "InformationSecurityIncidentNotificationsMade" )
    notifications_made = association_proxy("notifications_made_rel", "notifications_made",
                                  creator=lambda x_: InformationSecurityIncidentNotificationsMade(notifications_made=x_))
    

    def __repr__(self):
        return f"InformationSecurityIncident(incident_datetime={self.incident_datetime},incident_category={self.incident_category},severity={self.severity},incident_description={self.incident_description},detection_method={self.detection_method},root_cause={self.root_cause},notification_required={self.notification_required},closure_datetime={self.closure_datetime},post_incident_review={self.post_incident_review},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationSecurityPolicy(DocumentedInformation):
    """
    The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
    """
    __tablename__ = 'InformationSecurityPolicy'

    policy_statement = Column(Text())
    policy_objectives_framework = Column(Text())
    applicability_statement = Column(Text())
    communication_date = Column(Date())
    acknowledgment_required = Column(Boolean())
    last_policy_review_date = Column(Date())
    next_policy_review_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    commitment_statements_rel = relationship( "InformationSecurityPolicyCommitmentStatements" )
    commitment_statements = association_proxy("commitment_statements_rel", "commitment_statements",
                                  creator=lambda x_: InformationSecurityPolicyCommitmentStatements(commitment_statements=x_))
    
    
    # ManyToMany
    related_topic_policies = relationship( "TopicSpecificPolicy", secondary="InformationSecurityPolicy_related_topic_policies")
    
    
    integrated_management_systems_rel = relationship( "InformationSecurityPolicyIntegratedManagementSystems" )
    integrated_management_systems = association_proxy("integrated_management_systems_rel", "integrated_management_systems",
                                  creator=lambda x_: InformationSecurityPolicyIntegratedManagementSystems(integrated_management_systems=x_))
    
    
    distribution_controls_rel = relationship( "InformationSecurityPolicyDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: InformationSecurityPolicyDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"InformationSecurityPolicy(policy_statement={self.policy_statement},policy_objectives_framework={self.policy_objectives_framework},applicability_statement={self.applicability_statement},communication_date={self.communication_date},acknowledgment_required={self.acknowledgment_required},last_policy_review_date={self.last_policy_review_date},next_policy_review_date={self.next_policy_review_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TopicSpecificPolicy(DocumentedInformation):
    """
    A policy addressing a specific information security topic, supporting the overarching information security policy.
    """
    __tablename__ = 'TopicSpecificPolicy'

    topic_area = Column(Text())
    parent_policy = Column(Text(), ForeignKey('InformationSecurityPolicy.id'))
    target_audience = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    applicable_controls = relationship( "SecurityControl", secondary="TopicSpecificPolicy_applicable_controls")
    
    
    distribution_controls_rel = relationship( "TopicSpecificPolicyDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: TopicSpecificPolicyDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"TopicSpecificPolicy(topic_area={self.topic_area},parent_policy={self.parent_policy},target_audience={self.target_audience},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RiskAssessmentProcess(DocumentedInformation):
    """
    The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
    """
    __tablename__ = 'RiskAssessmentProcess'

    risk_acceptance_criteria = Column(Text())
    assessment_criteria = Column(Text())
    assessment_methodology = Column(Text())
    likelihood_scale = Column(Text())
    impact_scale = Column(Text())
    risk_matrix = Column(Text())
    assessment_frequency = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    trigger_events_rel = relationship( "RiskAssessmentProcessTriggerEvents" )
    trigger_events = association_proxy("trigger_events_rel", "trigger_events",
                                  creator=lambda x_: RiskAssessmentProcessTriggerEvents(trigger_events=x_))
    
    
    distribution_controls_rel = relationship( "RiskAssessmentProcessDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: RiskAssessmentProcessDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"RiskAssessmentProcess(risk_acceptance_criteria={self.risk_acceptance_criteria},assessment_criteria={self.assessment_criteria},assessment_methodology={self.assessment_methodology},likelihood_scale={self.likelihood_scale},impact_scale={self.impact_scale},risk_matrix={self.risk_matrix},assessment_frequency={self.assessment_frequency},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RiskAssessment(DocumentedInformation):
    """
    An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
    """
    __tablename__ = 'RiskAssessment'

    assessment_scope = Column(Text())
    assessment_date = Column(Date())
    assessor = Column(Text())
    methodology_used = Column(Text())
    summary_findings = Column(Text())
    next_assessment_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    risks_identified = relationship( "Risk", secondary="RiskAssessment_risks_identified")
    
    
    recommendations_rel = relationship( "RiskAssessmentRecommendations" )
    recommendations = association_proxy("recommendations_rel", "recommendations",
                                  creator=lambda x_: RiskAssessmentRecommendations(recommendations=x_))
    
    
    distribution_controls_rel = relationship( "RiskAssessmentDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: RiskAssessmentDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"RiskAssessment(assessment_scope={self.assessment_scope},assessment_date={self.assessment_date},assessor={self.assessor},methodology_used={self.methodology_used},summary_findings={self.summary_findings},next_assessment_date={self.next_assessment_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RiskTreatmentProcess(DocumentedInformation):
    """
    The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
    """
    __tablename__ = 'RiskTreatmentProcess'

    treatment_options_guidance = Column(Text())
    control_selection_criteria = Column(Text())
    annex_a_omission_verification = Column(Text())
    soa_template = Column(Text())
    approval_workflow = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    distribution_controls_rel = relationship( "RiskTreatmentProcessDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: RiskTreatmentProcessDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"RiskTreatmentProcess(treatment_options_guidance={self.treatment_options_guidance},control_selection_criteria={self.control_selection_criteria},annex_a_omission_verification={self.annex_a_omission_verification},soa_template={self.soa_template},approval_workflow={self.approval_workflow},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RiskTreatmentPlan(DocumentedInformation):
    """
    A risk treatment plan documenting planned actions to address identified risks through selected controls.
    """
    __tablename__ = 'RiskTreatmentPlan'

    plan_scope = Column(Text())
    resources_required = Column(Text())
    implementation_timeline = Column(Text())
    risk_owner_approval = Column(Text())
    approved_date = Column(Date())
    residual_risk_acceptance = Column(Text())
    implementation_status = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable', name='ImplementationStatus'))
    completion_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    risks_addressed = relationship( "Risk", secondary="RiskTreatmentPlan_risks_addressed")
    
    
    treatment_actions_rel = relationship( "RiskTreatmentPlanTreatmentActions" )
    treatment_actions = association_proxy("treatment_actions_rel", "treatment_actions",
                                  creator=lambda x_: RiskTreatmentPlanTreatmentActions(treatment_actions=x_))
    
    
    # ManyToMany
    controls_to_implement = relationship( "SecurityControl", secondary="RiskTreatmentPlan_controls_to_implement")
    
    
    responsible_parties_rel = relationship( "RiskTreatmentPlanResponsibleParties" )
    responsible_parties = association_proxy("responsible_parties_rel", "responsible_parties",
                                  creator=lambda x_: RiskTreatmentPlanResponsibleParties(responsible_parties=x_))
    
    
    distribution_controls_rel = relationship( "RiskTreatmentPlanDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: RiskTreatmentPlanDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"RiskTreatmentPlan(plan_scope={self.plan_scope},resources_required={self.resources_required},implementation_timeline={self.implementation_timeline},risk_owner_approval={self.risk_owner_approval},approved_date={self.approved_date},residual_risk_acceptance={self.residual_risk_acceptance},implementation_status={self.implementation_status},completion_date={self.completion_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation state.
    """
    __tablename__ = 'StatementOfApplicability'

    total_controls = Column(Integer())
    implemented_count = Column(Integer())
    planned_count = Column(Integer())
    not_applicable_count = Column(Integer())
    last_review_date = Column(Date())
    approved_by = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    soa_entries = relationship( "SoAEntry", secondary="StatementOfApplicability_soa_entries")
    
    
    distribution_controls_rel = relationship( "StatementOfApplicabilityDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: StatementOfApplicabilityDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"StatementOfApplicability(total_controls={self.total_controls},implemented_count={self.implemented_count},planned_count={self.planned_count},not_applicable_count={self.not_applicable_count},last_review_date={self.last_review_date},approved_by={self.approved_by},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
    """
    __tablename__ = 'CompetenceRecord'

    person_name = Column(Text())
    person_role = Column(Text())
    competency_assessment_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    required_competencies_rel = relationship( "CompetenceRecordRequiredCompetencies" )
    required_competencies = association_proxy("required_competencies_rel", "required_competencies",
                                  creator=lambda x_: CompetenceRecordRequiredCompetencies(required_competencies=x_))
    
    
    education_records_rel = relationship( "CompetenceRecordEducationRecords" )
    education_records = association_proxy("education_records_rel", "education_records",
                                  creator=lambda x_: CompetenceRecordEducationRecords(education_records=x_))
    
    
    training_records_rel = relationship( "CompetenceRecordTrainingRecords" )
    training_records = association_proxy("training_records_rel", "training_records",
                                  creator=lambda x_: CompetenceRecordTrainingRecords(training_records=x_))
    
    
    experience_records_rel = relationship( "CompetenceRecordExperienceRecords" )
    experience_records = association_proxy("experience_records_rel", "experience_records",
                                  creator=lambda x_: CompetenceRecordExperienceRecords(experience_records=x_))
    
    
    competency_gaps_rel = relationship( "CompetenceRecordCompetencyGaps" )
    competency_gaps = association_proxy("competency_gaps_rel", "competency_gaps",
                                  creator=lambda x_: CompetenceRecordCompetencyGaps(competency_gaps=x_))
    
    
    development_actions_rel = relationship( "CompetenceRecordDevelopmentActions" )
    development_actions = association_proxy("development_actions_rel", "development_actions",
                                  creator=lambda x_: CompetenceRecordDevelopmentActions(development_actions=x_))
    
    
    distribution_controls_rel = relationship( "CompetenceRecordDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: CompetenceRecordDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"CompetenceRecord(person_name={self.person_name},person_role={self.person_role},competency_assessment_date={self.competency_assessment_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
    """
    __tablename__ = 'AwarenessProgram'

    target_audience = Column(Text())
    frequency = Column(Text())
    completion_tracking = Column(Text())
    effectiveness_measures = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    awareness_topics_rel = relationship( "AwarenessProgramAwarenessTopics" )
    awareness_topics = association_proxy("awareness_topics_rel", "awareness_topics",
                                  creator=lambda x_: AwarenessProgramAwarenessTopics(awareness_topics=x_))
    
    
    delivery_methods_rel = relationship( "AwarenessProgramDeliveryMethods" )
    delivery_methods = association_proxy("delivery_methods_rel", "delivery_methods",
                                  creator=lambda x_: AwarenessProgramDeliveryMethods(delivery_methods=x_))
    
    
    distribution_controls_rel = relationship( "AwarenessProgramDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: AwarenessProgramDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"AwarenessProgram(target_audience={self.target_audience},frequency={self.frequency},completion_tracking={self.completion_tracking},effectiveness_measures={self.effectiveness_measures},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the ISMS per Clause 7.4.
    """
    __tablename__ = 'CommunicationPlan'

    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    communication_items = relationship( "CommunicationItem", secondary="CommunicationPlan_communication_items")
    
    
    distribution_controls_rel = relationship( "CommunicationPlanDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: CommunicationPlanDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"CommunicationPlan(document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control per Clause 8.1.
    """
    __tablename__ = 'OperationalProcedure'

    procedure_scope = Column(Text())
    process_criteria = Column(Text())
    change_control_requirements = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    control_measures_rel = relationship( "OperationalProcedureControlMeasures" )
    control_measures = association_proxy("control_measures_rel", "control_measures",
                                  creator=lambda x_: OperationalProcedureControlMeasures(control_measures=x_))
    
    
    # ManyToMany
    responsible_roles = relationship( "Role", secondary="OperationalProcedure_responsible_roles")
    
    
    # ManyToMany
    related_controls = relationship( "SecurityControl", secondary="OperationalProcedure_related_controls")
    
    
    distribution_controls_rel = relationship( "OperationalProcedureDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: OperationalProcedureDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"OperationalProcedure(procedure_scope={self.procedure_scope},process_criteria={self.process_criteria},change_control_requirements={self.change_control_requirements},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
    """
    __tablename__ = 'MonitoringProgram'

    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    monitoring_items = relationship( "MonitoringItem", secondary="MonitoringProgram_monitoring_items")
    
    
    distribution_controls_rel = relationship( "MonitoringProgramDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: MonitoringProgramDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"MonitoringProgram(document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
    """
    __tablename__ = 'InternalAudit'

    audit_reference = Column(Text())
    audit_type = Column(Enum('internal', 'external_second_party', 'external_third_party', 'surveillance', 'recertification', 'combined', name='AuditType'))
    audit_scope = Column(Text())
    audit_period_start = Column(Date())
    audit_period_end = Column(Date())
    lead_auditor = Column(Text())
    audit_plan = Column(Text())
    audit_conclusion = Column(Text())
    report_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    audit_criteria_rel = relationship( "InternalAuditAuditCriteria" )
    audit_criteria = association_proxy("audit_criteria_rel", "audit_criteria",
                                  creator=lambda x_: InternalAuditAuditCriteria(audit_criteria=x_))
    
    
    audit_objectives_rel = relationship( "InternalAuditAuditObjectives" )
    audit_objectives = association_proxy("audit_objectives_rel", "audit_objectives",
                                  creator=lambda x_: InternalAuditAuditObjectives(audit_objectives=x_))
    
    
    audit_team_rel = relationship( "InternalAuditAuditTeam" )
    audit_team = association_proxy("audit_team_rel", "audit_team",
                                  creator=lambda x_: InternalAuditAuditTeam(audit_team=x_))
    
    
    auditee_representatives_rel = relationship( "InternalAuditAuditeeRepresentatives" )
    auditee_representatives = association_proxy("auditee_representatives_rel", "auditee_representatives",
                                  creator=lambda x_: InternalAuditAuditeeRepresentatives(auditee_representatives=x_))
    
    
    # ManyToMany
    findings = relationship( "AuditFinding", secondary="InternalAudit_findings")
    
    
    positive_observations_rel = relationship( "InternalAuditPositiveObservations" )
    positive_observations = association_proxy("positive_observations_rel", "positive_observations",
                                  creator=lambda x_: InternalAuditPositiveObservations(positive_observations=x_))
    
    
    report_distribution_rel = relationship( "InternalAuditReportDistribution" )
    report_distribution = association_proxy("report_distribution_rel", "report_distribution",
                                  creator=lambda x_: InternalAuditReportDistribution(report_distribution=x_))
    
    
    distribution_controls_rel = relationship( "InternalAuditDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: InternalAuditDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"InternalAudit(audit_reference={self.audit_reference},audit_type={self.audit_type},audit_scope={self.audit_scope},audit_period_start={self.audit_period_start},audit_period_end={self.audit_period_end},lead_auditor={self.lead_auditor},audit_plan={self.audit_plan},audit_conclusion={self.audit_conclusion},report_date={self.report_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per 9.2.2, planning audit activities over a defined period.
    """
    __tablename__ = 'AuditProgramme'

    programme_period = Column(Text())
    audit_frequency_rationale = Column(Text())
    resource_requirements = Column(Text())
    auditor_qualifications = Column(Text())
    programme_status = Column(Text())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    review_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    # ManyToMany
    planned_audits = relationship( "InternalAudit", secondary="AuditProgramme_planned_audits")
    
    
    distribution_controls_rel = relationship( "AuditProgrammeDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: AuditProgrammeDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"AuditProgramme(programme_period={self.programme_period},audit_frequency_rationale={self.audit_frequency_rationale},resource_requirements={self.resource_requirements},auditor_qualifications={self.auditor_qualifications},programme_status={self.programme_status},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},review_date={self.review_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness for purpose.
    """
    __tablename__ = 'ManagementReview'

    review_date = Column(Date())
    previous_actions_status = Column(Text())
    context_changes = Column(Text())
    interested_party_changes = Column(Text())
    interested_party_feedback = Column(Text())
    performance_trends = Column(Text())
    audit_results_summary = Column(Text())
    risk_assessment_results = Column(Text())
    risk_treatment_status = Column(Text())
    risks_and_opportunities_changes = Column(Text())
    next_review_date = Column(Date())
    document_type = Column(Enum('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='DocumentType'))
    document_reference = Column(Text())
    author = Column(Text())
    owner = Column(Text())
    approved_by = Column(Text())
    approved_date = Column(Date())
    effective_date = Column(Date())
    status = Column(Text())
    classification = Column(Text())
    retention_period = Column(Text())
    storage_and_preservation = Column(Text())
    change_control_method = Column(Text())
    external_origin = Column(Boolean())
    external_origin_source = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    created_date = Column(Date())
    modified_date = Column(Date())
    version = Column(Text())
    
    
    attendees_rel = relationship( "ManagementReviewAttendees" )
    attendees = association_proxy("attendees_rel", "attendees",
                                  creator=lambda x_: ManagementReviewAttendees(attendees=x_))
    
    
    improvement_opportunities_rel = relationship( "ManagementReviewImprovementOpportunities" )
    improvement_opportunities = association_proxy("improvement_opportunities_rel", "improvement_opportunities",
                                  creator=lambda x_: ManagementReviewImprovementOpportunities(improvement_opportunities=x_))
    
    
    decisions_rel = relationship( "ManagementReviewDecisions" )
    decisions = association_proxy("decisions_rel", "decisions",
                                  creator=lambda x_: ManagementReviewDecisions(decisions=x_))
    
    
    action_items_rel = relationship( "ManagementReviewActionItems" )
    action_items = association_proxy("action_items_rel", "action_items",
                                  creator=lambda x_: ManagementReviewActionItems(action_items=x_))
    
    
    distribution_controls_rel = relationship( "ManagementReviewDistributionControls" )
    distribution_controls = association_proxy("distribution_controls_rel", "distribution_controls",
                                  creator=lambda x_: ManagementReviewDistributionControls(distribution_controls=x_))
    

    def __repr__(self):
        return f"ManagementReview(review_date={self.review_date},previous_actions_status={self.previous_actions_status},context_changes={self.context_changes},interested_party_changes={self.interested_party_changes},interested_party_feedback={self.interested_party_feedback},performance_trends={self.performance_trends},audit_results_summary={self.audit_results_summary},risk_assessment_results={self.risk_assessment_results},risk_treatment_status={self.risk_treatment_status},risks_and_opportunities_changes={self.risks_and_opportunities_changes},next_review_date={self.next_review_date},document_type={self.document_type},document_reference={self.document_reference},author={self.author},owner={self.owner},approved_by={self.approved_by},approved_date={self.approved_date},effective_date={self.effective_date},status={self.status},classification={self.classification},retention_period={self.retention_period},storage_and_preservation={self.storage_and_preservation},change_control_method={self.change_control_method},external_origin={self.external_origin},external_origin_source={self.external_origin_source},id={self.id},name={self.name},description={self.description},created_date={self.created_date},modified_date={self.modified_date},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


