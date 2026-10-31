
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class IsmsRecordMixin(Base):
    """
    What every record of the ISMS has, so that other records can refer to it: an identifier, a title and a description.
    """
    __tablename__ = 'IsmsRecordMixin'

    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    

    def __repr__(self):
        return f"IsmsRecordMixin(isms_id={self.isms_id},title={self.title},description={self.description},)"



    


class IsmsDocumentControlMixin(Base):
    """
    The control that documented information is kept under: who wrote, owns and approved it, when it takes effect and is reviewed, how it is classified, distributed, stored and changed, how long it is retained, and whether it came from outside the organization.
    """
    __tablename__ = 'IsmsDocumentControlMixin'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    document_distribution_rel = relationship( "IsmsDocumentControlMixinDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsDocumentControlMixinDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsDocumentControlMixin(id={self.id},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsManagementSystem(Base):
    """
    One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
    """
    __tablename__ = 'IsmsManagementSystem'

    isms_top_management = Column(Text())
    isms_governing_body = Column(Text())
    isms_scope = Column(Text())
    isms_processes = Column(Text())
    isms_certification_status = Column(Text())
    isms_certification_body = Column(Text())
    isms_certification_date = Column(Date())
    isms_recertification_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    isms_organization_isms_id = Column(Text(), ForeignKey('IsmsOrganization.isms_id'))
    isms_organization = relationship("IsmsOrganization", uselist=False, foreign_keys=[isms_organization_isms_id])
    isms_policy_isms_id = Column(Text(), ForeignKey('IsmsPolicy.isms_id'))
    isms_policy = relationship("IsmsPolicy", uselist=False, foreign_keys=[isms_policy_isms_id])
    isms_risk_assessment_process_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessmentProcess.isms_id'))
    isms_risk_assessment_process = relationship("IsmsRiskAssessmentProcess", uselist=False, foreign_keys=[isms_risk_assessment_process_isms_id])
    isms_risk_treatment_process_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentProcess.isms_id'))
    isms_risk_treatment_process = relationship("IsmsRiskTreatmentProcess", uselist=False, foreign_keys=[isms_risk_treatment_process_isms_id])
    isms_statement_of_applicability_isms_id = Column(Text(), ForeignKey('IsmsStatementOfApplicability.isms_id'))
    isms_statement_of_applicability = relationship("IsmsStatementOfApplicability", uselist=False, foreign_keys=[isms_statement_of_applicability_isms_id])
    isms_awareness_programme_isms_id = Column(Text(), ForeignKey('IsmsAwarenessProgramme.isms_id'))
    isms_awareness_programme = relationship("IsmsAwarenessProgramme", uselist=False, foreign_keys=[isms_awareness_programme_isms_id])
    isms_communication_plan_isms_id = Column(Text(), ForeignKey('IsmsCommunicationPlan.isms_id'))
    isms_communication_plan = relationship("IsmsCommunicationPlan", uselist=False, foreign_keys=[isms_communication_plan_isms_id])
    isms_monitoring_programme_isms_id = Column(Text(), ForeignKey('IsmsMonitoringProgramme.isms_id'))
    isms_monitoring_programme = relationship("IsmsMonitoringProgramme", uselist=False, foreign_keys=[isms_monitoring_programme_isms_id])
    
    
    isms_leadership_evidence_rel = relationship( "IsmsManagementSystemIsmsLeadershipEvidence" )
    isms_leadership_evidence = association_proxy("isms_leadership_evidence_rel", "isms_leadership_evidence",
                                  creator=lambda x_: IsmsManagementSystemIsmsLeadershipEvidence(isms_leadership_evidence=x_))
    
    
    isms_scope_boundaries_rel = relationship( "IsmsManagementSystemIsmsScopeBoundaries" )
    isms_scope_boundaries = association_proxy("isms_scope_boundaries_rel", "isms_scope_boundaries",
                                  creator=lambda x_: IsmsManagementSystemIsmsScopeBoundaries(isms_scope_boundaries=x_))
    
    
    isms_scope_exclusions_rel = relationship( "IsmsManagementSystemIsmsScopeExclusions" )
    isms_scope_exclusions = association_proxy("isms_scope_exclusions_rel", "isms_scope_exclusions",
                                  creator=lambda x_: IsmsManagementSystemIsmsScopeExclusions(isms_scope_exclusions=x_))
    
    
    isms_interfaces_rel = relationship( "IsmsManagementSystemIsmsInterfaces" )
    isms_interfaces = association_proxy("isms_interfaces_rel", "isms_interfaces",
                                  creator=lambda x_: IsmsManagementSystemIsmsInterfaces(isms_interfaces=x_))
    
    
    isms_internal_issues_rel = relationship( "IsmsManagementSystemIsmsInternalIssues" )
    isms_internal_issues = association_proxy("isms_internal_issues_rel", "isms_internal_issues",
                                  creator=lambda x_: IsmsManagementSystemIsmsInternalIssues(isms_internal_issues=x_))
    
    
    isms_external_issues_rel = relationship( "IsmsManagementSystemIsmsExternalIssues" )
    isms_external_issues = association_proxy("isms_external_issues_rel", "isms_external_issues",
                                  creator=lambda x_: IsmsManagementSystemIsmsExternalIssues(isms_external_issues=x_))
    
    
    isms_risk_and_opportunity_actions_rel = relationship( "IsmsManagementSystemIsmsRiskAndOpportunityActions" )
    isms_risk_and_opportunity_actions = association_proxy("isms_risk_and_opportunity_actions_rel", "isms_risk_and_opportunity_actions",
                                  creator=lambda x_: IsmsManagementSystemIsmsRiskAndOpportunityActions(isms_risk_and_opportunity_actions=x_))
    
    
    isms_planned_changes_rel = relationship( "IsmsManagementSystemIsmsPlannedChanges" )
    isms_planned_changes = association_proxy("isms_planned_changes_rel", "isms_planned_changes",
                                  creator=lambda x_: IsmsManagementSystemIsmsPlannedChanges(isms_planned_changes=x_))
    
    
    isms_external_services_rel = relationship( "IsmsManagementSystemIsmsExternalServices" )
    isms_external_services = association_proxy("isms_external_services_rel", "isms_external_services",
                                  creator=lambda x_: IsmsManagementSystemIsmsExternalServices(isms_external_services=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_interested_parties', mapping_type=None, target_class='IsmsInterestedParty', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_interested_parties = relationship( "IsmsInterestedParty", foreign_keys="[IsmsInterestedParty.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_topic_specific_policies', mapping_type=None, target_class='IsmsTopicSpecificPolicy', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_topic_specific_policies = relationship( "IsmsTopicSpecificPolicy", foreign_keys="[IsmsTopicSpecificPolicy.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_roles', mapping_type=None, target_class='IsmsRole', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_roles = relationship( "IsmsRole", foreign_keys="[IsmsRole.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_objectives', mapping_type=None, target_class='IsmsObjective', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_objectives = relationship( "IsmsObjective", foreign_keys="[IsmsObjective.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_risk_assessments', mapping_type=None, target_class='IsmsRiskAssessment', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_risk_assessments = relationship( "IsmsRiskAssessment", foreign_keys="[IsmsRiskAssessment.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_risks', mapping_type=None, target_class='IsmsRisk', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_risks = relationship( "IsmsRisk", foreign_keys="[IsmsRisk.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_risk_treatment_plans', mapping_type=None, target_class='IsmsRiskTreatmentPlan', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_risk_treatment_plans = relationship( "IsmsRiskTreatmentPlan", foreign_keys="[IsmsRiskTreatmentPlan.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_controls', mapping_type=None, target_class='IsmsControl', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_controls = relationship( "IsmsControl", foreign_keys="[IsmsControl.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_assets', mapping_type=None, target_class='IsmsAsset', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_assets = relationship( "IsmsAsset", foreign_keys="[IsmsAsset.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_resources', mapping_type=None, target_class='IsmsResource', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_resources = relationship( "IsmsResource", foreign_keys="[IsmsResource.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_competence_records', mapping_type=None, target_class='IsmsCompetenceRecord', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_competence_records = relationship( "IsmsCompetenceRecord", foreign_keys="[IsmsCompetenceRecord.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_documented_information', mapping_type=None, target_class='IsmsDocumentedInformation', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_documented_information = relationship( "IsmsDocumentedInformation", foreign_keys="[IsmsDocumentedInformation.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_operational_procedures', mapping_type=None, target_class='IsmsOperationalProcedure', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_operational_procedures = relationship( "IsmsOperationalProcedure", foreign_keys="[IsmsOperationalProcedure.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_audit_programmes', mapping_type=None, target_class='IsmsAuditProgramme', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_audit_programmes = relationship( "IsmsAuditProgramme", foreign_keys="[IsmsAuditProgramme.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_audits', mapping_type=None, target_class='IsmsAudit', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_audits = relationship( "IsmsAudit", foreign_keys="[IsmsAudit.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_management_reviews', mapping_type=None, target_class='IsmsManagementReview', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_management_reviews = relationship( "IsmsManagementReview", foreign_keys="[IsmsManagementReview.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_nonconformities', mapping_type=None, target_class='IsmsNonconformity', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_nonconformities = relationship( "IsmsNonconformity", foreign_keys="[IsmsNonconformity.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_corrective_actions', mapping_type=None, target_class='IsmsCorrectiveAction', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_corrective_actions = relationship( "IsmsCorrectiveAction", foreign_keys="[IsmsCorrectiveAction.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_improvements', mapping_type=None, target_class='IsmsImprovementOpportunity', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_improvements = relationship( "IsmsImprovementOpportunity", foreign_keys="[IsmsImprovementOpportunity.IsmsManagementSystem_isms_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsManagementSystem', source_slot='isms_security_events', mapping_type=None, target_class='IsmsSecurityEvent', target_slot='IsmsManagementSystem_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    isms_security_events = relationship( "IsmsSecurityEvent", foreign_keys="[IsmsSecurityEvent.IsmsManagementSystem_isms_id]")
    

    def __repr__(self):
        return f"IsmsManagementSystem(isms_top_management={self.isms_top_management},isms_governing_body={self.isms_governing_body},isms_scope={self.isms_scope},isms_processes={self.isms_processes},isms_certification_status={self.isms_certification_status},isms_certification_body={self.isms_certification_body},isms_certification_date={self.isms_certification_date},isms_recertification_date={self.isms_recertification_date},isms_id={self.isms_id},title={self.title},description={self.description},isms_organization_isms_id={self.isms_organization_isms_id},isms_policy_isms_id={self.isms_policy_isms_id},isms_risk_assessment_process_isms_id={self.isms_risk_assessment_process_isms_id},isms_risk_treatment_process_isms_id={self.isms_risk_treatment_process_isms_id},isms_statement_of_applicability_isms_id={self.isms_statement_of_applicability_isms_id},isms_awareness_programme_isms_id={self.isms_awareness_programme_isms_id},isms_communication_plan_isms_id={self.isms_communication_plan_isms_id},isms_monitoring_programme_isms_id={self.isms_monitoring_programme_isms_id},)"



    


class IsmsOrganization(Base):
    """
    The organization that runs the ISMS, with what it needs to know about itself to understand its context.
    """
    __tablename__ = 'IsmsOrganization'

    organization_legal_name = Column(Text())
    organization_kind = Column(Text())
    organization_sector = Column(Text())
    organization_size = Column(Text())
    organization_employee_count = Column(Integer())
    organization_parent = Column(Text())
    organization_climate_change_relevant = Column(Boolean())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    
    
    organization_trading_names_rel = relationship( "IsmsOrganizationOrganizationTradingNames" )
    organization_trading_names = association_proxy("organization_trading_names_rel", "organization_trading_names",
                                  creator=lambda x_: IsmsOrganizationOrganizationTradingNames(organization_trading_names=x_))
    
    
    organization_locations_rel = relationship( "IsmsOrganizationOrganizationLocations" )
    organization_locations = association_proxy("organization_locations_rel", "organization_locations",
                                  creator=lambda x_: IsmsOrganizationOrganizationLocations(organization_locations=x_))
    
    
    organization_jurisdictions_rel = relationship( "IsmsOrganizationOrganizationJurisdictions" )
    organization_jurisdictions = association_proxy("organization_jurisdictions_rel", "organization_jurisdictions",
                                  creator=lambda x_: IsmsOrganizationOrganizationJurisdictions(organization_jurisdictions=x_))
    
    
    organization_subsidiaries_rel = relationship( "IsmsOrganizationOrganizationSubsidiaries" )
    organization_subsidiaries = association_proxy("organization_subsidiaries_rel", "organization_subsidiaries",
                                  creator=lambda x_: IsmsOrganizationOrganizationSubsidiaries(organization_subsidiaries=x_))
    

    def __repr__(self):
        return f"IsmsOrganization(organization_legal_name={self.organization_legal_name},organization_kind={self.organization_kind},organization_sector={self.organization_sector},organization_size={self.organization_size},organization_employee_count={self.organization_employee_count},organization_parent={self.organization_parent},organization_climate_change_relevant={self.organization_climate_change_relevant},isms_id={self.isms_id},title={self.title},description={self.description},)"



    


class IsmsInterestedParty(Base):
    """
    A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
    """
    __tablename__ = 'IsmsInterestedParty'

    party_category = Column(Text())
    party_relationship = Column(Text())
    party_communication_needs = Column(Text())
    party_contact = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    party_requirements_rel = relationship( "IsmsInterestedPartyPartyRequirements" )
    party_requirements = association_proxy("party_requirements_rel", "party_requirements",
                                  creator=lambda x_: IsmsInterestedPartyPartyRequirements(party_requirements=x_))
    
    
    party_addressed_requirements_rel = relationship( "IsmsInterestedPartyPartyAddressedRequirements" )
    party_addressed_requirements = association_proxy("party_addressed_requirements_rel", "party_addressed_requirements",
                                  creator=lambda x_: IsmsInterestedPartyPartyAddressedRequirements(party_addressed_requirements=x_))
    
    
    party_climate_change_requirements_rel = relationship( "IsmsInterestedPartyPartyClimateChangeRequirements" )
    party_climate_change_requirements = association_proxy("party_climate_change_requirements_rel", "party_climate_change_requirements",
                                  creator=lambda x_: IsmsInterestedPartyPartyClimateChangeRequirements(party_climate_change_requirements=x_))
    

    def __repr__(self):
        return f"IsmsInterestedParty(party_category={self.party_category},party_relationship={self.party_relationship},party_communication_needs={self.party_communication_needs},party_contact={self.party_contact},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsPolicy(Base):
    """
    The information security policy that top management sets: the organization's commitment and the frame for its information security objectives.
    """
    __tablename__ = 'IsmsPolicy'

    policy_statement = Column(Text())
    policy_objectives_framework = Column(Text())
    policy_applicability = Column(Text())
    policy_communication_date = Column(Date())
    policy_acknowledgement_required = Column(Boolean())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    policy_commitments_rel = relationship( "IsmsPolicyPolicyCommitments" )
    policy_commitments = association_proxy("policy_commitments_rel", "policy_commitments",
                                  creator=lambda x_: IsmsPolicyPolicyCommitments(policy_commitments=x_))
    
    
    policy_management_systems_rel = relationship( "IsmsPolicyPolicyManagementSystems" )
    policy_management_systems = association_proxy("policy_management_systems_rel", "policy_management_systems",
                                  creator=lambda x_: IsmsPolicyPolicyManagementSystems(policy_management_systems=x_))
    
    
    document_distribution_rel = relationship( "IsmsPolicyDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsPolicyDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsPolicy(policy_statement={self.policy_statement},policy_objectives_framework={self.policy_objectives_framework},policy_applicability={self.policy_applicability},policy_communication_date={self.policy_communication_date},policy_acknowledgement_required={self.policy_acknowledgement_required},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsTopicSpecificPolicy(Base):
    """
    A policy on one topic of information security, such as access control or backup, that supports the information security policy.
    """
    __tablename__ = 'IsmsTopicSpecificPolicy'

    topic_policy_topic = Column(Text())
    topic_policy_parent = Column(Text(), ForeignKey('IsmsPolicy.isms_id'))
    topic_policy_audience = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    relevant_controls = relationship( "IsmsControl", secondary="IsmsTopicSpecificPolicy_relevant_controls")
    
    
    document_distribution_rel = relationship( "IsmsTopicSpecificPolicyDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsTopicSpecificPolicyDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsTopicSpecificPolicy(topic_policy_topic={self.topic_policy_topic},topic_policy_parent={self.topic_policy_parent},topic_policy_audience={self.topic_policy_audience},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsRole(Base):
    """
    A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
    """
    __tablename__ = 'IsmsRole'

    role_category = Column(Text())
    role_accountability = Column(Text())
    role_delegation = Column(Text())
    role_reports_to = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    role_responsibilities_rel = relationship( "IsmsRoleRoleResponsibilities" )
    role_responsibilities = association_proxy("role_responsibilities_rel", "role_responsibilities",
                                  creator=lambda x_: IsmsRoleRoleResponsibilities(role_responsibilities=x_))
    
    
    role_authorities_rel = relationship( "IsmsRoleRoleAuthorities" )
    role_authorities = association_proxy("role_authorities_rel", "role_authorities",
                                  creator=lambda x_: IsmsRoleRoleAuthorities(role_authorities=x_))
    
    
    role_holders_rel = relationship( "IsmsRoleRoleHolders" )
    role_holders = association_proxy("role_holders_rel", "role_holders",
                                  creator=lambda x_: IsmsRoleRoleHolders(role_holders=x_))
    

    def __repr__(self):
        return f"IsmsRole(role_category={self.role_category},role_accountability={self.role_accountability},role_delegation={self.role_delegation},role_reports_to={self.role_reports_to},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsObjective(Base):
    """
    An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
    """
    __tablename__ = 'IsmsObjective'

    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    objective_statement = Column(Text())
    objective_target = Column(Text())
    objective_current_value = Column(Text())
    objective_metric = Column(Text())
    objective_measurement_method = Column(Text())
    objective_measurement_frequency = Column(Text())
    objective_target_date = Column(Date())
    objective_achievement = Column(Text())
    objective_action_plan = Column(Text())
    objective_resources = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    relevant_controls = relationship( "IsmsControl", secondary="IsmsObjective_relevant_controls")
    
    
    # ManyToMany
    objective_risks = relationship( "IsmsRisk", secondary="IsmsObjective_objective_risks")
    

    def __repr__(self):
        return f"IsmsObjective(responsible_role={self.responsible_role},objective_statement={self.objective_statement},objective_target={self.objective_target},objective_current_value={self.objective_current_value},objective_metric={self.objective_metric},objective_measurement_method={self.objective_measurement_method},objective_measurement_frequency={self.objective_measurement_frequency},objective_target_date={self.objective_target_date},objective_achievement={self.objective_achievement},objective_action_plan={self.objective_action_plan},objective_resources={self.objective_resources},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsRiskAssessmentProcess(Base):
    """
    The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
    """
    __tablename__ = 'IsmsRiskAssessmentProcess'

    risk_acceptance_criteria = Column(Text())
    risk_assessment_criteria = Column(Text())
    risk_assessment_method = Column(Text())
    risk_likelihood_scale = Column(Text())
    risk_impact_scale = Column(Text())
    risk_matrix = Column(Text())
    risk_assessment_frequency = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    risk_assessment_triggers_rel = relationship( "IsmsRiskAssessmentProcessRiskAssessmentTriggers" )
    risk_assessment_triggers = association_proxy("risk_assessment_triggers_rel", "risk_assessment_triggers",
                                  creator=lambda x_: IsmsRiskAssessmentProcessRiskAssessmentTriggers(risk_assessment_triggers=x_))
    
    
    document_distribution_rel = relationship( "IsmsRiskAssessmentProcessDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsRiskAssessmentProcessDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsRiskAssessmentProcess(risk_acceptance_criteria={self.risk_acceptance_criteria},risk_assessment_criteria={self.risk_assessment_criteria},risk_assessment_method={self.risk_assessment_method},risk_likelihood_scale={self.risk_likelihood_scale},risk_impact_scale={self.risk_impact_scale},risk_matrix={self.risk_matrix},risk_assessment_frequency={self.risk_assessment_frequency},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsRiskAssessment(Base):
    """
    One risk assessment carried out under the risk assessment process, and what it found.
    """
    __tablename__ = 'IsmsRiskAssessment'

    assessment_scope = Column(Text())
    assessment_date = Column(Date())
    assessment_assessor = Column(Text())
    assessment_method_used = Column(Text())
    assessment_summary = Column(Text())
    assessment_next_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    assessment_risks = relationship( "IsmsRisk", secondary="IsmsRiskAssessment_assessment_risks")
    
    
    assessment_recommendations_rel = relationship( "IsmsRiskAssessmentAssessmentRecommendations" )
    assessment_recommendations = association_proxy("assessment_recommendations_rel", "assessment_recommendations",
                                  creator=lambda x_: IsmsRiskAssessmentAssessmentRecommendations(assessment_recommendations=x_))
    
    
    document_distribution_rel = relationship( "IsmsRiskAssessmentDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsRiskAssessmentDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsRiskAssessment(assessment_scope={self.assessment_scope},assessment_date={self.assessment_date},assessment_assessor={self.assessment_assessor},assessment_method_used={self.assessment_method_used},assessment_summary={self.assessment_summary},assessment_next_date={self.assessment_next_date},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsRisk(Base):
    """
    An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
    """
    __tablename__ = 'IsmsRisk'

    risk_source = Column(Text())
    risk_threat = Column(Text())
    risk_vulnerability = Column(Text())
    risk_owner = Column(Text())
    risk_likelihood = Column(Enum('rare', 'unlikely', 'possible', 'likely', 'almost_certain', name='IsmsLikelihood'))
    risk_impact = Column(Enum('negligible', 'minor', 'moderate', 'major', 'severe', name='IsmsImpact'))
    risk_inherent_level = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='IsmsRiskLevel'))
    risk_residual_level = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='IsmsRiskLevel'))
    risk_treatment_option = Column(Enum('modify', 'retain', 'avoid', 'share', name='IsmsRiskTreatmentOption'))
    risk_treatment_priority = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    affected_assets = relationship( "IsmsAsset", secondary="IsmsRisk_affected_assets")
    
    
    affected_security_properties_rel = relationship( "IsmsRiskAffectedSecurityProperties" )
    affected_security_properties = association_proxy("affected_security_properties_rel", "affected_security_properties",
                                  creator=lambda x_: IsmsRiskAffectedSecurityProperties(affected_security_properties=x_))
    
    
    # ManyToMany
    risk_existing_controls = relationship( "IsmsControl", secondary="IsmsRisk_risk_existing_controls")
    

    def __repr__(self):
        return f"IsmsRisk(risk_source={self.risk_source},risk_threat={self.risk_threat},risk_vulnerability={self.risk_vulnerability},risk_owner={self.risk_owner},risk_likelihood={self.risk_likelihood},risk_impact={self.risk_impact},risk_inherent_level={self.risk_inherent_level},risk_residual_level={self.risk_residual_level},risk_treatment_option={self.risk_treatment_option},risk_treatment_priority={self.risk_treatment_priority},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsRiskTreatmentProcess(Base):
    """
    The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
    """
    __tablename__ = 'IsmsRiskTreatmentProcess'

    treatment_options_guidance = Column(Text())
    treatment_control_selection = Column(Text())
    treatment_annex_a_comparison = Column(Text())
    treatment_soa_template = Column(Text())
    treatment_approval_workflow = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    document_distribution_rel = relationship( "IsmsRiskTreatmentProcessDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsRiskTreatmentProcessDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsRiskTreatmentProcess(treatment_options_guidance={self.treatment_options_guidance},treatment_control_selection={self.treatment_control_selection},treatment_annex_a_comparison={self.treatment_annex_a_comparison},treatment_soa_template={self.treatment_soa_template},treatment_approval_workflow={self.treatment_approval_workflow},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsRiskTreatmentPlan(Base):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
    """
    __tablename__ = 'IsmsRiskTreatmentPlan'

    implementation_state = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', name='IsmsImplementationStatus'))
    plan_scope = Column(Text())
    plan_resources = Column(Text())
    plan_timeline = Column(Text())
    plan_risk_owner_approval = Column(Text())
    plan_residual_risk_acceptance = Column(Text())
    plan_completion_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    plan_risks = relationship( "IsmsRisk", secondary="IsmsRiskTreatmentPlan_plan_risks")
    
    
    plan_actions_rel = relationship( "IsmsRiskTreatmentPlanPlanActions" )
    plan_actions = association_proxy("plan_actions_rel", "plan_actions",
                                  creator=lambda x_: IsmsRiskTreatmentPlanPlanActions(plan_actions=x_))
    
    
    # ManyToMany
    plan_controls = relationship( "IsmsControl", secondary="IsmsRiskTreatmentPlan_plan_controls")
    
    
    plan_responsible_parties_rel = relationship( "IsmsRiskTreatmentPlanPlanResponsibleParties" )
    plan_responsible_parties = association_proxy("plan_responsible_parties_rel", "plan_responsible_parties",
                                  creator=lambda x_: IsmsRiskTreatmentPlanPlanResponsibleParties(plan_responsible_parties=x_))
    
    
    document_distribution_rel = relationship( "IsmsRiskTreatmentPlanDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsRiskTreatmentPlanDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan(implementation_state={self.implementation_state},plan_scope={self.plan_scope},plan_resources={self.plan_resources},plan_timeline={self.plan_timeline},plan_risk_owner_approval={self.plan_risk_owner_approval},plan_residual_risk_acceptance={self.plan_residual_risk_acceptance},plan_completion_date={self.plan_completion_date},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsStatementOfApplicability(Base):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
    """
    __tablename__ = 'IsmsStatementOfApplicability'

    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsStatementOfApplicability', source_slot='soa_entries', mapping_type=None, target_class='IsmsApplicabilityEntry', target_slot='IsmsStatementOfApplicability_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    soa_entries = relationship( "IsmsApplicabilityEntry", foreign_keys="[IsmsApplicabilityEntry.IsmsStatementOfApplicability_isms_id]")
    
    
    document_distribution_rel = relationship( "IsmsStatementOfApplicabilityDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsStatementOfApplicabilityDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsStatementOfApplicability(isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsApplicabilityEntry(Base):
    """
    One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
    """
    __tablename__ = 'IsmsApplicabilityEntry'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    entry_annex_a_control = Column(Enum('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34', name='IsmsAnnexAControl'))
    entry_type = Column(Text())
    entry_justification = Column(Text(), nullable=False )
    IsmsStatementOfApplicability_isms_id = Column(Text(), ForeignKey('IsmsStatementOfApplicability.isms_id'))
    

    def __repr__(self):
        return f"IsmsApplicabilityEntry(id={self.id},entry_annex_a_control={self.entry_annex_a_control},entry_type={self.entry_type},entry_justification={self.entry_justification},IsmsStatementOfApplicability_isms_id={self.IsmsStatementOfApplicability_isms_id},)"



    


class IsmsControl(Base):
    """
    A control the organization has determined it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
    """
    __tablename__ = 'IsmsControl'

    implementation_state = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', name='IsmsImplementationStatus'))
    control_theme = Column(Enum('organizational', 'people', 'physical', 'technological', name='IsmsControlTheme'))
    control_text = Column(Text())
    control_guidance = Column(Text())
    control_owner = Column(Text())
    control_implementation_date = Column(Date())
    control_effectiveness = Column(Text())
    control_last_tested = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    relevant_controls = relationship( "IsmsControl", secondary="IsmsControl_relevant_controls")
    
    
    control_annex_a_controls_rel = relationship( "IsmsControlControlAnnexAControls" )
    control_annex_a_controls = association_proxy("control_annex_a_controls_rel", "control_annex_a_controls",
                                  creator=lambda x_: IsmsControlControlAnnexAControls(control_annex_a_controls=x_))
    
    
    control_threats_rel = relationship( "IsmsControlControlThreats" )
    control_threats = association_proxy("control_threats_rel", "control_threats",
                                  creator=lambda x_: IsmsControlControlThreats(control_threats=x_))
    
    
    control_asset_types_rel = relationship( "IsmsControlControlAssetTypes" )
    control_asset_types = association_proxy("control_asset_types_rel", "control_asset_types",
                                  creator=lambda x_: IsmsControlControlAssetTypes(control_asset_types=x_))
    
    
    control_evidence_rel = relationship( "IsmsControlControlEvidence" )
    control_evidence = association_proxy("control_evidence_rel", "control_evidence",
                                  creator=lambda x_: IsmsControlControlEvidence(control_evidence=x_))
    

    def __repr__(self):
        return f"IsmsControl(implementation_state={self.implementation_state},control_theme={self.control_theme},control_text={self.control_text},control_guidance={self.control_guidance},control_owner={self.control_owner},control_implementation_date={self.control_implementation_date},control_effectiveness={self.control_effectiveness},control_last_tested={self.control_last_tested},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsAsset(Base):
    """
    An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
    """
    __tablename__ = 'IsmsAsset'

    asset_category = Column(Text())
    asset_owner = Column(Text())
    asset_custodian = Column(Text())
    asset_classification = Column(Text())
    asset_location = Column(Text())
    asset_criticality = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    relevant_controls = relationship( "IsmsControl", secondary="IsmsAsset_relevant_controls")
    

    def __repr__(self):
        return f"IsmsAsset(asset_category={self.asset_category},asset_owner={self.asset_owner},asset_custodian={self.asset_custodian},asset_classification={self.asset_classification},asset_location={self.asset_location},asset_criticality={self.asset_criticality},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsResource(Base):
    """
    A resource provided for the ISMS, such as people, time, tools or budget.
    """
    __tablename__ = 'IsmsResource'

    resource_category = Column(Text())
    resource_quantity = Column(Text())
    resource_allocation_date = Column(Date())
    resource_allocated_to = Column(Text())
    resource_cost = Column(Text())
    resource_availability = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    

    def __repr__(self):
        return f"IsmsResource(resource_category={self.resource_category},resource_quantity={self.resource_quantity},resource_allocation_date={self.resource_allocation_date},resource_allocated_to={self.resource_allocated_to},resource_cost={self.resource_cost},resource_availability={self.resource_availability},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsCompetenceRecord(Base):
    """
    The evidence of one person's competence for work that affects information security, and what is done to close any gap.
    """
    __tablename__ = 'IsmsCompetenceRecord'

    competence_person = Column(Text())
    competence_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    competence_assessment_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    competence_required_rel = relationship( "IsmsCompetenceRecordCompetenceRequired" )
    competence_required = association_proxy("competence_required_rel", "competence_required",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceRequired(competence_required=x_))
    
    
    competence_education_rel = relationship( "IsmsCompetenceRecordCompetenceEducation" )
    competence_education = association_proxy("competence_education_rel", "competence_education",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceEducation(competence_education=x_))
    
    
    competence_training_rel = relationship( "IsmsCompetenceRecordCompetenceTraining" )
    competence_training = association_proxy("competence_training_rel", "competence_training",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceTraining(competence_training=x_))
    
    
    competence_experience_rel = relationship( "IsmsCompetenceRecordCompetenceExperience" )
    competence_experience = association_proxy("competence_experience_rel", "competence_experience",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceExperience(competence_experience=x_))
    
    
    competence_gaps_rel = relationship( "IsmsCompetenceRecordCompetenceGaps" )
    competence_gaps = association_proxy("competence_gaps_rel", "competence_gaps",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceGaps(competence_gaps=x_))
    
    
    competence_actions_rel = relationship( "IsmsCompetenceRecordCompetenceActions" )
    competence_actions = association_proxy("competence_actions_rel", "competence_actions",
                                  creator=lambda x_: IsmsCompetenceRecordCompetenceActions(competence_actions=x_))
    
    
    document_distribution_rel = relationship( "IsmsCompetenceRecordDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsCompetenceRecordDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsCompetenceRecord(competence_person={self.competence_person},competence_role={self.competence_role},competence_assessment_date={self.competence_assessment_date},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsAwarenessProgramme(Base):
    """
    The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
    """
    __tablename__ = 'IsmsAwarenessProgramme'

    awareness_audience = Column(Text())
    awareness_frequency = Column(Text())
    awareness_completion_tracking = Column(Text())
    awareness_effectiveness = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    awareness_topics_rel = relationship( "IsmsAwarenessProgrammeAwarenessTopics" )
    awareness_topics = association_proxy("awareness_topics_rel", "awareness_topics",
                                  creator=lambda x_: IsmsAwarenessProgrammeAwarenessTopics(awareness_topics=x_))
    
    
    awareness_methods_rel = relationship( "IsmsAwarenessProgrammeAwarenessMethods" )
    awareness_methods = association_proxy("awareness_methods_rel", "awareness_methods",
                                  creator=lambda x_: IsmsAwarenessProgrammeAwarenessMethods(awareness_methods=x_))
    
    
    document_distribution_rel = relationship( "IsmsAwarenessProgrammeDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsAwarenessProgrammeDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsAwarenessProgramme(awareness_audience={self.awareness_audience},awareness_frequency={self.awareness_frequency},awareness_completion_tracking={self.awareness_completion_tracking},awareness_effectiveness={self.awareness_effectiveness},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsCommunicationPlan(Base):
    """
    The plan for communication about the ISMS, inside the organization and outside it.
    """
    __tablename__ = 'IsmsCommunicationPlan'

    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsCommunicationPlan', source_slot='communication_items', mapping_type=None, target_class='IsmsCommunication', target_slot='IsmsCommunicationPlan_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    communication_items = relationship( "IsmsCommunication", foreign_keys="[IsmsCommunication.IsmsCommunicationPlan_isms_id]")
    
    
    document_distribution_rel = relationship( "IsmsCommunicationPlanDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsCommunicationPlanDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsCommunicationPlan(isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsCommunication(Base):
    """
    One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
    """
    __tablename__ = 'IsmsCommunication'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    communication_subject = Column(Text(), nullable=False )
    communication_purpose = Column(Text())
    communication_audience = Column(Text())
    communication_frequency = Column(Text())
    communication_method = Column(Text())
    communication_records_required = Column(Boolean())
    IsmsCommunicationPlan_isms_id = Column(Text(), ForeignKey('IsmsCommunicationPlan.isms_id'))
    

    def __repr__(self):
        return f"IsmsCommunication(id={self.id},responsible_role={self.responsible_role},communication_subject={self.communication_subject},communication_purpose={self.communication_purpose},communication_audience={self.communication_audience},communication_frequency={self.communication_frequency},communication_method={self.communication_method},communication_records_required={self.communication_records_required},IsmsCommunicationPlan_isms_id={self.IsmsCommunicationPlan_isms_id},)"



    


class IsmsDocumentedInformation(Base):
    """
    A piece of documented information the ISMS keeps under control that no more specific record describes, such as a procedure, a standard, a plan or a report.
    """
    __tablename__ = 'IsmsDocumentedInformation'

    document_kind = Column(Enum('procedure', 'standard', 'guideline', 'record', 'plan', 'report', name='IsmsDocumentKind'), nullable=False )
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    document_distribution_rel = relationship( "IsmsDocumentedInformationDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsDocumentedInformationDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsDocumentedInformation(document_kind={self.document_kind},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsOperationalProcedure(Base):
    """
    A procedure by which the organization plans and controls the processes that meet its information security requirements.
    """
    __tablename__ = 'IsmsOperationalProcedure'

    procedure_scope = Column(Text())
    procedure_criteria = Column(Text())
    procedure_change_control = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    relevant_controls = relationship( "IsmsControl", secondary="IsmsOperationalProcedure_relevant_controls")
    
    
    procedure_control_measures_rel = relationship( "IsmsOperationalProcedureProcedureControlMeasures" )
    procedure_control_measures = association_proxy("procedure_control_measures_rel", "procedure_control_measures",
                                  creator=lambda x_: IsmsOperationalProcedureProcedureControlMeasures(procedure_control_measures=x_))
    
    
    # ManyToMany
    procedure_roles = relationship( "IsmsRole", secondary="IsmsOperationalProcedure_procedure_roles")
    
    
    document_distribution_rel = relationship( "IsmsOperationalProcedureDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsOperationalProcedureDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsOperationalProcedure(procedure_scope={self.procedure_scope},procedure_criteria={self.procedure_criteria},procedure_change_control={self.procedure_change_control},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsMonitoringProgramme(Base):
    """
    The programme of monitoring, measurement, analysis and evaluation of information security performance and of the ISMS's effectiveness.
    """
    __tablename__ = 'IsmsMonitoringProgramme'

    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsMonitoringProgramme', source_slot='monitoring_items', mapping_type=None, target_class='IsmsMonitoringItem', target_slot='IsmsMonitoringProgramme_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    monitoring_items = relationship( "IsmsMonitoringItem", foreign_keys="[IsmsMonitoringItem.IsmsMonitoringProgramme_isms_id]")
    
    
    document_distribution_rel = relationship( "IsmsMonitoringProgrammeDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsMonitoringProgrammeDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsMonitoringProgramme(isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},)"



    


class IsmsMonitoringItem(Base):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
    """
    __tablename__ = 'IsmsMonitoringItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    monitoring_metric = Column(Text(), nullable=False )
    monitoring_description = Column(Text())
    monitoring_method = Column(Text())
    monitoring_frequency = Column(Text())
    monitoring_analysis_frequency = Column(Text())
    monitoring_analyst = Column(Text())
    monitoring_target = Column(Text())
    monitoring_alert_threshold = Column(Text())
    monitoring_current_value = Column(Text())
    monitoring_trend = Column(Text())
    IsmsMonitoringProgramme_isms_id = Column(Text(), ForeignKey('IsmsMonitoringProgramme.isms_id'))
    

    def __repr__(self):
        return f"IsmsMonitoringItem(id={self.id},responsible_role={self.responsible_role},monitoring_metric={self.monitoring_metric},monitoring_description={self.monitoring_description},monitoring_method={self.monitoring_method},monitoring_frequency={self.monitoring_frequency},monitoring_analysis_frequency={self.monitoring_analysis_frequency},monitoring_analyst={self.monitoring_analyst},monitoring_target={self.monitoring_target},monitoring_alert_threshold={self.monitoring_alert_threshold},monitoring_current_value={self.monitoring_current_value},monitoring_trend={self.monitoring_trend},IsmsMonitoringProgramme_isms_id={self.IsmsMonitoringProgramme_isms_id},)"



    


class IsmsAuditProgramme(Base):
    """
    An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
    """
    __tablename__ = 'IsmsAuditProgramme'

    programme_period = Column(Text())
    programme_frequency_rationale = Column(Text())
    programme_resources = Column(Text())
    programme_auditor_qualifications = Column(Text())
    programme_status = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    programme_audits = relationship( "IsmsAudit", secondary="IsmsAuditProgramme_programme_audits")
    
    
    document_distribution_rel = relationship( "IsmsAuditProgrammeDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsAuditProgrammeDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsAuditProgramme(programme_period={self.programme_period},programme_frequency_rationale={self.programme_frequency_rationale},programme_resources={self.programme_resources},programme_auditor_qualifications={self.programme_auditor_qualifications},programme_status={self.programme_status},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsAudit(Base):
    """
    An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
    """
    __tablename__ = 'IsmsAudit'

    audit_type = Column(Enum('first_party', 'second_party', 'third_party', name='IsmsAuditType'), nullable=False )
    audit_scope = Column(Text())
    audit_period_start = Column(Date())
    audit_period_end = Column(Date())
    audit_lead = Column(Text())
    audit_plan = Column(Text(), ForeignKey('IsmsDocumentedInformation.isms_id'))
    audit_conclusion = Column(Text())
    audit_report_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    audit_standards_rel = relationship( "IsmsAuditAuditStandards" )
    audit_standards = association_proxy("audit_standards_rel", "audit_standards",
                                  creator=lambda x_: IsmsAuditAuditStandards(audit_standards=x_))
    
    
    audit_criteria_rel = relationship( "IsmsAuditAuditCriteria" )
    audit_criteria = association_proxy("audit_criteria_rel", "audit_criteria",
                                  creator=lambda x_: IsmsAuditAuditCriteria(audit_criteria=x_))
    
    
    audit_objectives_rel = relationship( "IsmsAuditAuditObjectives" )
    audit_objectives = association_proxy("audit_objectives_rel", "audit_objectives",
                                  creator=lambda x_: IsmsAuditAuditObjectives(audit_objectives=x_))
    
    
    audit_team_rel = relationship( "IsmsAuditAuditTeam" )
    audit_team = association_proxy("audit_team_rel", "audit_team",
                                  creator=lambda x_: IsmsAuditAuditTeam(audit_team=x_))
    
    
    audit_auditees_rel = relationship( "IsmsAuditAuditAuditees" )
    audit_auditees = association_proxy("audit_auditees_rel", "audit_auditees",
                                  creator=lambda x_: IsmsAuditAuditAuditees(audit_auditees=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='IsmsAudit', source_slot='audit_findings', mapping_type=None, target_class='IsmsAuditFinding', target_slot='IsmsAudit_isms_id', join_class=None, uses_join_table=None, multivalued=False)
    audit_findings = relationship( "IsmsAuditFinding", foreign_keys="[IsmsAuditFinding.IsmsAudit_isms_id]")
    
    
    audit_report_distribution_rel = relationship( "IsmsAuditAuditReportDistribution" )
    audit_report_distribution = association_proxy("audit_report_distribution_rel", "audit_report_distribution",
                                  creator=lambda x_: IsmsAuditAuditReportDistribution(audit_report_distribution=x_))
    
    
    document_distribution_rel = relationship( "IsmsAuditDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsAuditDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsAudit(audit_type={self.audit_type},audit_scope={self.audit_scope},audit_period_start={self.audit_period_start},audit_period_end={self.audit_period_end},audit_lead={self.audit_lead},audit_plan={self.audit_plan},audit_conclusion={self.audit_conclusion},audit_report_date={self.audit_report_date},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsAuditFinding(Base):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
    """
    __tablename__ = 'IsmsAuditFinding'

    finding_type = Column(Enum('major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding', name='IsmsAuditFindingType'), nullable=False )
    finding_requirement = Column(Text())
    finding_control = Column(Text(), ForeignKey('IsmsControl.isms_id'))
    finding_evidence = Column(Text())
    finding_root_cause = Column(Text())
    finding_risk = Column(Text())
    finding_recommendation = Column(Text())
    finding_auditee_response = Column(Text())
    finding_corrective_action = Column(Text(), ForeignKey('IsmsCorrectiveAction.isms_id'))
    finding_closure_status = Column(Text())
    finding_closure_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'))
    

    def __repr__(self):
        return f"IsmsAuditFinding(finding_type={self.finding_type},finding_requirement={self.finding_requirement},finding_control={self.finding_control},finding_evidence={self.finding_evidence},finding_root_cause={self.finding_root_cause},finding_risk={self.finding_risk},finding_recommendation={self.finding_recommendation},finding_auditee_response={self.finding_auditee_response},finding_corrective_action={self.finding_corrective_action},finding_closure_status={self.finding_closure_status},finding_closure_date={self.finding_closure_date},isms_id={self.isms_id},title={self.title},description={self.description},IsmsAudit_isms_id={self.IsmsAudit_isms_id},)"



    


class IsmsManagementReview(Base):
    """
    A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
    """
    __tablename__ = 'IsmsManagementReview'

    review_held_on = Column(Date(), nullable=False )
    review_previous_actions = Column(Text())
    review_context_changes = Column(Text())
    review_interested_party_changes = Column(Text())
    review_interested_party_feedback = Column(Text())
    review_performance_trends = Column(Text())
    review_audit_results = Column(Text())
    review_risk_assessment_results = Column(Text())
    review_risk_treatment_status = Column(Text())
    review_risks_and_opportunities = Column(Text())
    review_next_date = Column(Date())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    document_reference = Column(Text())
    document_version = Column(Text())
    document_author = Column(Text())
    document_owner = Column(Text())
    document_approver = Column(Text())
    document_approval_date = Column(Date())
    document_effective_date = Column(Date())
    document_last_review_date = Column(Date())
    document_next_review_date = Column(Date())
    document_status = Column(Text())
    document_classification = Column(Text())
    document_retention = Column(Text())
    document_storage = Column(Text())
    document_change_control = Column(Text())
    document_external_origin = Column(Boolean())
    document_external_source = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    review_attendees_rel = relationship( "IsmsManagementReviewReviewAttendees" )
    review_attendees = association_proxy("review_attendees_rel", "review_attendees",
                                  creator=lambda x_: IsmsManagementReviewReviewAttendees(review_attendees=x_))
    
    
    review_improvement_opportunities_rel = relationship( "IsmsManagementReviewReviewImprovementOpportunities" )
    review_improvement_opportunities = association_proxy("review_improvement_opportunities_rel", "review_improvement_opportunities",
                                  creator=lambda x_: IsmsManagementReviewReviewImprovementOpportunities(review_improvement_opportunities=x_))
    
    
    review_decisions_rel = relationship( "IsmsManagementReviewReviewDecisions" )
    review_decisions = association_proxy("review_decisions_rel", "review_decisions",
                                  creator=lambda x_: IsmsManagementReviewReviewDecisions(review_decisions=x_))
    
    
    review_actions_rel = relationship( "IsmsManagementReviewReviewActions" )
    review_actions = association_proxy("review_actions_rel", "review_actions",
                                  creator=lambda x_: IsmsManagementReviewReviewActions(review_actions=x_))
    
    
    document_distribution_rel = relationship( "IsmsManagementReviewDocumentDistribution" )
    document_distribution = association_proxy("document_distribution_rel", "document_distribution",
                                  creator=lambda x_: IsmsManagementReviewDocumentDistribution(document_distribution=x_))
    

    def __repr__(self):
        return f"IsmsManagementReview(review_held_on={self.review_held_on},review_previous_actions={self.review_previous_actions},review_context_changes={self.review_context_changes},review_interested_party_changes={self.review_interested_party_changes},review_interested_party_feedback={self.review_interested_party_feedback},review_performance_trends={self.review_performance_trends},review_audit_results={self.review_audit_results},review_risk_assessment_results={self.review_risk_assessment_results},review_risk_treatment_status={self.review_risk_treatment_status},review_risks_and_opportunities={self.review_risks_and_opportunities},review_next_date={self.review_next_date},isms_id={self.isms_id},title={self.title},description={self.description},document_reference={self.document_reference},document_version={self.document_version},document_author={self.document_author},document_owner={self.document_owner},document_approver={self.document_approver},document_approval_date={self.document_approval_date},document_effective_date={self.document_effective_date},document_last_review_date={self.document_last_review_date},document_next_review_date={self.document_next_review_date},document_status={self.document_status},document_classification={self.document_classification},document_retention={self.document_retention},document_storage={self.document_storage},document_change_control={self.document_change_control},document_external_origin={self.document_external_origin},document_external_source={self.document_external_source},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsNonconformity(Base):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
    """
    __tablename__ = 'IsmsNonconformity'

    nonconformity_source = Column(Text())
    nonconformity_detected_on = Column(Date())
    nonconformity_detected_by = Column(Text())
    nonconformity_requirement = Column(Text())
    nonconformity_consequences = Column(Text())
    nonconformity_root_cause = Column(Text())
    nonconformity_similar_check = Column(Text())
    nonconformity_status = Column(Text())
    nonconformity_closure_date = Column(Date())
    nonconformity_closure_evidence = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    nonconformity_immediate_actions_rel = relationship( "IsmsNonconformityNonconformityImmediateActions" )
    nonconformity_immediate_actions = association_proxy("nonconformity_immediate_actions_rel", "nonconformity_immediate_actions",
                                  creator=lambda x_: IsmsNonconformityNonconformityImmediateActions(nonconformity_immediate_actions=x_))
    

    def __repr__(self):
        return f"IsmsNonconformity(nonconformity_source={self.nonconformity_source},nonconformity_detected_on={self.nonconformity_detected_on},nonconformity_detected_by={self.nonconformity_detected_by},nonconformity_requirement={self.nonconformity_requirement},nonconformity_consequences={self.nonconformity_consequences},nonconformity_root_cause={self.nonconformity_root_cause},nonconformity_similar_check={self.nonconformity_similar_check},nonconformity_status={self.nonconformity_status},nonconformity_closure_date={self.nonconformity_closure_date},nonconformity_closure_evidence={self.nonconformity_closure_evidence},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsCorrectiveAction(Base):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
    """
    __tablename__ = 'IsmsCorrectiveAction'

    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    action_root_cause = Column(Text())
    action_target_date = Column(Date())
    action_completion_date = Column(Date())
    action_resources = Column(Text())
    action_effectiveness_criteria = Column(Text())
    action_effectiveness_review_date = Column(Date())
    action_effective = Column(Boolean())
    action_isms_changes = Column(Text())
    action_status = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    action_nonconformities = relationship( "IsmsNonconformity", secondary="IsmsCorrectiveAction_action_nonconformities")
    

    def __repr__(self):
        return f"IsmsCorrectiveAction(responsible_role={self.responsible_role},action_root_cause={self.action_root_cause},action_target_date={self.action_target_date},action_completion_date={self.action_completion_date},action_resources={self.action_resources},action_effectiveness_criteria={self.action_effectiveness_criteria},action_effectiveness_review_date={self.action_effectiveness_review_date},action_effective={self.action_effective},action_isms_changes={self.action_isms_changes},action_status={self.action_status},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsImprovementOpportunity(Base):
    """
    An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
    """
    __tablename__ = 'IsmsImprovementOpportunity'

    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    improvement_source = Column(Text())
    improvement_identified_on = Column(Date())
    improvement_identified_by = Column(Text())
    improvement_benefit = Column(Text())
    improvement_priority = Column(Text())
    improvement_plan = Column(Text())
    improvement_target_date = Column(Date())
    improvement_completion_date = Column(Date())
    improvement_outcome = Column(Text())
    improvement_status = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    

    def __repr__(self):
        return f"IsmsImprovementOpportunity(responsible_role={self.responsible_role},improvement_source={self.improvement_source},improvement_identified_on={self.improvement_identified_on},improvement_identified_by={self.improvement_identified_by},improvement_benefit={self.improvement_benefit},improvement_priority={self.improvement_priority},improvement_plan={self.improvement_plan},improvement_target_date={self.improvement_target_date},improvement_completion_date={self.improvement_completion_date},improvement_outcome={self.improvement_outcome},improvement_status={self.improvement_status},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsSecurityEvent(Base):
    """
    An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
    """
    __tablename__ = 'IsmsSecurityEvent'

    event_type = Column(Text())
    event_occurred_at = Column(DateTime())
    event_reporter = Column(Text())
    event_assessment = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'))
    
    
    # ManyToMany
    affected_assets = relationship( "IsmsAsset", secondary="IsmsSecurityEvent_affected_assets")
    

    def __repr__(self):
        return f"IsmsSecurityEvent(event_type={self.event_type},event_occurred_at={self.event_occurred_at},event_reporter={self.event_reporter},event_assessment={self.event_assessment},isms_id={self.isms_id},title={self.title},description={self.description},IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},)"



    


class IsmsDocumentControlMixinDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsDocumentControlMixin_document_distribution'

    IsmsDocumentControlMixin_id = Column(Integer(), ForeignKey('IsmsDocumentControlMixin.id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsDocumentControlMixin_document_distribution(IsmsDocumentControlMixin_id={self.IsmsDocumentControlMixin_id},document_distribution={self.document_distribution},)"



    


class IsmsManagementSystemIsmsLeadershipEvidence(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_leadership_evidence'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_leadership_evidence = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_leadership_evidence(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_leadership_evidence={self.isms_leadership_evidence},)"



    


class IsmsManagementSystemIsmsScopeBoundaries(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_scope_boundaries'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_scope_boundaries = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_scope_boundaries(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_scope_boundaries={self.isms_scope_boundaries},)"



    


class IsmsManagementSystemIsmsScopeExclusions(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_scope_exclusions'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_scope_exclusions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_scope_exclusions(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_scope_exclusions={self.isms_scope_exclusions},)"



    


class IsmsManagementSystemIsmsInterfaces(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_interfaces'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_interfaces = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_interfaces(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_interfaces={self.isms_interfaces},)"



    


class IsmsManagementSystemIsmsInternalIssues(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_internal_issues'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_internal_issues = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_internal_issues(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_internal_issues={self.isms_internal_issues},)"



    


class IsmsManagementSystemIsmsExternalIssues(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_external_issues'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_external_issues = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_external_issues(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_external_issues={self.isms_external_issues},)"



    


class IsmsManagementSystemIsmsRiskAndOpportunityActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_risk_and_opportunity_actions'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_risk_and_opportunity_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_risk_and_opportunity_actions(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_risk_and_opportunity_actions={self.isms_risk_and_opportunity_actions},)"



    


class IsmsManagementSystemIsmsPlannedChanges(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_planned_changes'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_planned_changes = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_planned_changes(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_planned_changes={self.isms_planned_changes},)"



    


class IsmsManagementSystemIsmsExternalServices(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementSystem_isms_external_services'

    IsmsManagementSystem_isms_id = Column(Text(), ForeignKey('IsmsManagementSystem.isms_id'), primary_key=True)
    isms_external_services = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementSystem_isms_external_services(IsmsManagementSystem_isms_id={self.IsmsManagementSystem_isms_id},isms_external_services={self.isms_external_services},)"



    


class IsmsOrganizationOrganizationTradingNames(Base):
    """
    None
    """
    __tablename__ = 'IsmsOrganization_organization_trading_names'

    IsmsOrganization_isms_id = Column(Text(), ForeignKey('IsmsOrganization.isms_id'), primary_key=True)
    organization_trading_names = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOrganization_organization_trading_names(IsmsOrganization_isms_id={self.IsmsOrganization_isms_id},organization_trading_names={self.organization_trading_names},)"



    


class IsmsOrganizationOrganizationLocations(Base):
    """
    None
    """
    __tablename__ = 'IsmsOrganization_organization_locations'

    IsmsOrganization_isms_id = Column(Text(), ForeignKey('IsmsOrganization.isms_id'), primary_key=True)
    organization_locations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOrganization_organization_locations(IsmsOrganization_isms_id={self.IsmsOrganization_isms_id},organization_locations={self.organization_locations},)"



    


class IsmsOrganizationOrganizationJurisdictions(Base):
    """
    None
    """
    __tablename__ = 'IsmsOrganization_organization_jurisdictions'

    IsmsOrganization_isms_id = Column(Text(), ForeignKey('IsmsOrganization.isms_id'), primary_key=True)
    organization_jurisdictions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOrganization_organization_jurisdictions(IsmsOrganization_isms_id={self.IsmsOrganization_isms_id},organization_jurisdictions={self.organization_jurisdictions},)"



    


class IsmsOrganizationOrganizationSubsidiaries(Base):
    """
    None
    """
    __tablename__ = 'IsmsOrganization_organization_subsidiaries'

    IsmsOrganization_isms_id = Column(Text(), ForeignKey('IsmsOrganization.isms_id'), primary_key=True)
    organization_subsidiaries = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOrganization_organization_subsidiaries(IsmsOrganization_isms_id={self.IsmsOrganization_isms_id},organization_subsidiaries={self.organization_subsidiaries},)"



    


class IsmsInterestedPartyPartyRequirements(Base):
    """
    None
    """
    __tablename__ = 'IsmsInterestedParty_party_requirements'

    IsmsInterestedParty_isms_id = Column(Text(), ForeignKey('IsmsInterestedParty.isms_id'), primary_key=True)
    party_requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsInterestedParty_party_requirements(IsmsInterestedParty_isms_id={self.IsmsInterestedParty_isms_id},party_requirements={self.party_requirements},)"



    


class IsmsInterestedPartyPartyAddressedRequirements(Base):
    """
    None
    """
    __tablename__ = 'IsmsInterestedParty_party_addressed_requirements'

    IsmsInterestedParty_isms_id = Column(Text(), ForeignKey('IsmsInterestedParty.isms_id'), primary_key=True)
    party_addressed_requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsInterestedParty_party_addressed_requirements(IsmsInterestedParty_isms_id={self.IsmsInterestedParty_isms_id},party_addressed_requirements={self.party_addressed_requirements},)"



    


class IsmsInterestedPartyPartyClimateChangeRequirements(Base):
    """
    None
    """
    __tablename__ = 'IsmsInterestedParty_party_climate_change_requirements'

    IsmsInterestedParty_isms_id = Column(Text(), ForeignKey('IsmsInterestedParty.isms_id'), primary_key=True)
    party_climate_change_requirements = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsInterestedParty_party_climate_change_requirements(IsmsInterestedParty_isms_id={self.IsmsInterestedParty_isms_id},party_climate_change_requirements={self.party_climate_change_requirements},)"



    


class IsmsPolicyPolicyCommitments(Base):
    """
    None
    """
    __tablename__ = 'IsmsPolicy_policy_commitments'

    IsmsPolicy_isms_id = Column(Text(), ForeignKey('IsmsPolicy.isms_id'), primary_key=True)
    policy_commitments = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsPolicy_policy_commitments(IsmsPolicy_isms_id={self.IsmsPolicy_isms_id},policy_commitments={self.policy_commitments},)"



    


class IsmsPolicyPolicyManagementSystems(Base):
    """
    None
    """
    __tablename__ = 'IsmsPolicy_policy_management_systems'

    IsmsPolicy_isms_id = Column(Text(), ForeignKey('IsmsPolicy.isms_id'), primary_key=True)
    policy_management_systems = Column(Enum('iso_iec_27001', 'iso_iec_27701', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1', name='IsmsManagementSystemStandard'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsPolicy_policy_management_systems(IsmsPolicy_isms_id={self.IsmsPolicy_isms_id},policy_management_systems={self.policy_management_systems},)"



    


class IsmsPolicyDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsPolicy_document_distribution'

    IsmsPolicy_isms_id = Column(Text(), ForeignKey('IsmsPolicy.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsPolicy_document_distribution(IsmsPolicy_isms_id={self.IsmsPolicy_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsTopicSpecificPolicyRelevantControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsTopicSpecificPolicy_relevant_controls'

    IsmsTopicSpecificPolicy_isms_id = Column(Text(), ForeignKey('IsmsTopicSpecificPolicy.isms_id'), primary_key=True)
    relevant_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsTopicSpecificPolicy_relevant_controls(IsmsTopicSpecificPolicy_isms_id={self.IsmsTopicSpecificPolicy_isms_id},relevant_controls_isms_id={self.relevant_controls_isms_id},)"



    


class IsmsTopicSpecificPolicyDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsTopicSpecificPolicy_document_distribution'

    IsmsTopicSpecificPolicy_isms_id = Column(Text(), ForeignKey('IsmsTopicSpecificPolicy.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsTopicSpecificPolicy_document_distribution(IsmsTopicSpecificPolicy_isms_id={self.IsmsTopicSpecificPolicy_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsRoleRoleResponsibilities(Base):
    """
    None
    """
    __tablename__ = 'IsmsRole_role_responsibilities'

    IsmsRole_isms_id = Column(Text(), ForeignKey('IsmsRole.isms_id'), primary_key=True)
    role_responsibilities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRole_role_responsibilities(IsmsRole_isms_id={self.IsmsRole_isms_id},role_responsibilities={self.role_responsibilities},)"



    


class IsmsRoleRoleAuthorities(Base):
    """
    None
    """
    __tablename__ = 'IsmsRole_role_authorities'

    IsmsRole_isms_id = Column(Text(), ForeignKey('IsmsRole.isms_id'), primary_key=True)
    role_authorities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRole_role_authorities(IsmsRole_isms_id={self.IsmsRole_isms_id},role_authorities={self.role_authorities},)"



    


class IsmsRoleRoleHolders(Base):
    """
    None
    """
    __tablename__ = 'IsmsRole_role_holders'

    IsmsRole_isms_id = Column(Text(), ForeignKey('IsmsRole.isms_id'), primary_key=True)
    role_holders = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRole_role_holders(IsmsRole_isms_id={self.IsmsRole_isms_id},role_holders={self.role_holders},)"



    


class IsmsObjectiveRelevantControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsObjective_relevant_controls'

    IsmsObjective_isms_id = Column(Text(), ForeignKey('IsmsObjective.isms_id'), primary_key=True)
    relevant_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsObjective_relevant_controls(IsmsObjective_isms_id={self.IsmsObjective_isms_id},relevant_controls_isms_id={self.relevant_controls_isms_id},)"



    


class IsmsObjectiveObjectiveRisks(Base):
    """
    None
    """
    __tablename__ = 'IsmsObjective_objective_risks'

    IsmsObjective_isms_id = Column(Text(), ForeignKey('IsmsObjective.isms_id'), primary_key=True)
    objective_risks_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsObjective_objective_risks(IsmsObjective_isms_id={self.IsmsObjective_isms_id},objective_risks_isms_id={self.objective_risks_isms_id},)"



    


class IsmsRiskAssessmentProcessRiskAssessmentTriggers(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskAssessmentProcess_risk_assessment_triggers'

    IsmsRiskAssessmentProcess_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessmentProcess.isms_id'), primary_key=True)
    risk_assessment_triggers = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskAssessmentProcess_risk_assessment_triggers(IsmsRiskAssessmentProcess_isms_id={self.IsmsRiskAssessmentProcess_isms_id},risk_assessment_triggers={self.risk_assessment_triggers},)"



    


class IsmsRiskAssessmentProcessDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskAssessmentProcess_document_distribution'

    IsmsRiskAssessmentProcess_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessmentProcess.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskAssessmentProcess_document_distribution(IsmsRiskAssessmentProcess_isms_id={self.IsmsRiskAssessmentProcess_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsRiskAssessmentAssessmentRisks(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskAssessment_assessment_risks'

    IsmsRiskAssessment_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessment.isms_id'), primary_key=True)
    assessment_risks_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskAssessment_assessment_risks(IsmsRiskAssessment_isms_id={self.IsmsRiskAssessment_isms_id},assessment_risks_isms_id={self.assessment_risks_isms_id},)"



    


class IsmsRiskAssessmentAssessmentRecommendations(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskAssessment_assessment_recommendations'

    IsmsRiskAssessment_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessment.isms_id'), primary_key=True)
    assessment_recommendations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskAssessment_assessment_recommendations(IsmsRiskAssessment_isms_id={self.IsmsRiskAssessment_isms_id},assessment_recommendations={self.assessment_recommendations},)"



    


class IsmsRiskAssessmentDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskAssessment_document_distribution'

    IsmsRiskAssessment_isms_id = Column(Text(), ForeignKey('IsmsRiskAssessment.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskAssessment_document_distribution(IsmsRiskAssessment_isms_id={self.IsmsRiskAssessment_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsRiskAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'IsmsRisk_affected_assets'

    IsmsRisk_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    affected_assets_isms_id = Column(Text(), ForeignKey('IsmsAsset.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRisk_affected_assets(IsmsRisk_isms_id={self.IsmsRisk_isms_id},affected_assets_isms_id={self.affected_assets_isms_id},)"



    


class IsmsRiskAffectedSecurityProperties(Base):
    """
    None
    """
    __tablename__ = 'IsmsRisk_affected_security_properties'

    IsmsRisk_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    affected_security_properties = Column(Enum('confidentiality', 'integrity', 'availability', name='IsmsSecurityProperty'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRisk_affected_security_properties(IsmsRisk_isms_id={self.IsmsRisk_isms_id},affected_security_properties={self.affected_security_properties},)"



    


class IsmsRiskRiskExistingControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsRisk_risk_existing_controls'

    IsmsRisk_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    risk_existing_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRisk_risk_existing_controls(IsmsRisk_isms_id={self.IsmsRisk_isms_id},risk_existing_controls_isms_id={self.risk_existing_controls_isms_id},)"



    


class IsmsRiskTreatmentProcessDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentProcess_document_distribution'

    IsmsRiskTreatmentProcess_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentProcess.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentProcess_document_distribution(IsmsRiskTreatmentProcess_isms_id={self.IsmsRiskTreatmentProcess_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsRiskTreatmentPlanPlanRisks(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentPlan_plan_risks'

    IsmsRiskTreatmentPlan_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentPlan.isms_id'), primary_key=True)
    plan_risks_isms_id = Column(Text(), ForeignKey('IsmsRisk.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan_plan_risks(IsmsRiskTreatmentPlan_isms_id={self.IsmsRiskTreatmentPlan_isms_id},plan_risks_isms_id={self.plan_risks_isms_id},)"



    


class IsmsRiskTreatmentPlanPlanActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentPlan_plan_actions'

    IsmsRiskTreatmentPlan_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentPlan.isms_id'), primary_key=True)
    plan_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan_plan_actions(IsmsRiskTreatmentPlan_isms_id={self.IsmsRiskTreatmentPlan_isms_id},plan_actions={self.plan_actions},)"



    


class IsmsRiskTreatmentPlanPlanControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentPlan_plan_controls'

    IsmsRiskTreatmentPlan_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentPlan.isms_id'), primary_key=True)
    plan_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan_plan_controls(IsmsRiskTreatmentPlan_isms_id={self.IsmsRiskTreatmentPlan_isms_id},plan_controls_isms_id={self.plan_controls_isms_id},)"



    


class IsmsRiskTreatmentPlanPlanResponsibleParties(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentPlan_plan_responsible_parties'

    IsmsRiskTreatmentPlan_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentPlan.isms_id'), primary_key=True)
    plan_responsible_parties = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan_plan_responsible_parties(IsmsRiskTreatmentPlan_isms_id={self.IsmsRiskTreatmentPlan_isms_id},plan_responsible_parties={self.plan_responsible_parties},)"



    


class IsmsRiskTreatmentPlanDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsRiskTreatmentPlan_document_distribution'

    IsmsRiskTreatmentPlan_isms_id = Column(Text(), ForeignKey('IsmsRiskTreatmentPlan.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsRiskTreatmentPlan_document_distribution(IsmsRiskTreatmentPlan_isms_id={self.IsmsRiskTreatmentPlan_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsStatementOfApplicabilityDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsStatementOfApplicability_document_distribution'

    IsmsStatementOfApplicability_isms_id = Column(Text(), ForeignKey('IsmsStatementOfApplicability.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsStatementOfApplicability_document_distribution(IsmsStatementOfApplicability_isms_id={self.IsmsStatementOfApplicability_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsControlRelevantControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsControl_relevant_controls'

    IsmsControl_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    relevant_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsControl_relevant_controls(IsmsControl_isms_id={self.IsmsControl_isms_id},relevant_controls_isms_id={self.relevant_controls_isms_id},)"



    


class IsmsControlControlAnnexAControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsControl_control_annex_a_controls'

    IsmsControl_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    control_annex_a_controls = Column(Enum('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34', name='IsmsAnnexAControl'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsControl_control_annex_a_controls(IsmsControl_isms_id={self.IsmsControl_isms_id},control_annex_a_controls={self.control_annex_a_controls},)"



    


class IsmsControlControlThreats(Base):
    """
    None
    """
    __tablename__ = 'IsmsControl_control_threats'

    IsmsControl_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    control_threats = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsControl_control_threats(IsmsControl_isms_id={self.IsmsControl_isms_id},control_threats={self.control_threats},)"



    


class IsmsControlControlAssetTypes(Base):
    """
    None
    """
    __tablename__ = 'IsmsControl_control_asset_types'

    IsmsControl_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    control_asset_types = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsControl_control_asset_types(IsmsControl_isms_id={self.IsmsControl_isms_id},control_asset_types={self.control_asset_types},)"



    


class IsmsControlControlEvidence(Base):
    """
    None
    """
    __tablename__ = 'IsmsControl_control_evidence'

    IsmsControl_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    control_evidence = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsControl_control_evidence(IsmsControl_isms_id={self.IsmsControl_isms_id},control_evidence={self.control_evidence},)"



    


class IsmsAssetRelevantControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsAsset_relevant_controls'

    IsmsAsset_isms_id = Column(Text(), ForeignKey('IsmsAsset.isms_id'), primary_key=True)
    relevant_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAsset_relevant_controls(IsmsAsset_isms_id={self.IsmsAsset_isms_id},relevant_controls_isms_id={self.relevant_controls_isms_id},)"



    


class IsmsCompetenceRecordCompetenceRequired(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_required'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_required = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_required(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_required={self.competence_required},)"



    


class IsmsCompetenceRecordCompetenceEducation(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_education'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_education = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_education(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_education={self.competence_education},)"



    


class IsmsCompetenceRecordCompetenceTraining(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_training'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_training = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_training(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_training={self.competence_training},)"



    


class IsmsCompetenceRecordCompetenceExperience(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_experience'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_experience = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_experience(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_experience={self.competence_experience},)"



    


class IsmsCompetenceRecordCompetenceGaps(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_gaps'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_gaps = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_gaps(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_gaps={self.competence_gaps},)"



    


class IsmsCompetenceRecordCompetenceActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_competence_actions'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    competence_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_competence_actions(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},competence_actions={self.competence_actions},)"



    


class IsmsCompetenceRecordDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsCompetenceRecord_document_distribution'

    IsmsCompetenceRecord_isms_id = Column(Text(), ForeignKey('IsmsCompetenceRecord.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCompetenceRecord_document_distribution(IsmsCompetenceRecord_isms_id={self.IsmsCompetenceRecord_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsAwarenessProgrammeAwarenessTopics(Base):
    """
    None
    """
    __tablename__ = 'IsmsAwarenessProgramme_awareness_topics'

    IsmsAwarenessProgramme_isms_id = Column(Text(), ForeignKey('IsmsAwarenessProgramme.isms_id'), primary_key=True)
    awareness_topics = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAwarenessProgramme_awareness_topics(IsmsAwarenessProgramme_isms_id={self.IsmsAwarenessProgramme_isms_id},awareness_topics={self.awareness_topics},)"



    


class IsmsAwarenessProgrammeAwarenessMethods(Base):
    """
    None
    """
    __tablename__ = 'IsmsAwarenessProgramme_awareness_methods'

    IsmsAwarenessProgramme_isms_id = Column(Text(), ForeignKey('IsmsAwarenessProgramme.isms_id'), primary_key=True)
    awareness_methods = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAwarenessProgramme_awareness_methods(IsmsAwarenessProgramme_isms_id={self.IsmsAwarenessProgramme_isms_id},awareness_methods={self.awareness_methods},)"



    


class IsmsAwarenessProgrammeDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsAwarenessProgramme_document_distribution'

    IsmsAwarenessProgramme_isms_id = Column(Text(), ForeignKey('IsmsAwarenessProgramme.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAwarenessProgramme_document_distribution(IsmsAwarenessProgramme_isms_id={self.IsmsAwarenessProgramme_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsCommunicationPlanDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsCommunicationPlan_document_distribution'

    IsmsCommunicationPlan_isms_id = Column(Text(), ForeignKey('IsmsCommunicationPlan.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCommunicationPlan_document_distribution(IsmsCommunicationPlan_isms_id={self.IsmsCommunicationPlan_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsDocumentedInformationDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsDocumentedInformation_document_distribution'

    IsmsDocumentedInformation_isms_id = Column(Text(), ForeignKey('IsmsDocumentedInformation.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsDocumentedInformation_document_distribution(IsmsDocumentedInformation_isms_id={self.IsmsDocumentedInformation_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsOperationalProcedureRelevantControls(Base):
    """
    None
    """
    __tablename__ = 'IsmsOperationalProcedure_relevant_controls'

    IsmsOperationalProcedure_isms_id = Column(Text(), ForeignKey('IsmsOperationalProcedure.isms_id'), primary_key=True)
    relevant_controls_isms_id = Column(Text(), ForeignKey('IsmsControl.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOperationalProcedure_relevant_controls(IsmsOperationalProcedure_isms_id={self.IsmsOperationalProcedure_isms_id},relevant_controls_isms_id={self.relevant_controls_isms_id},)"



    


class IsmsOperationalProcedureProcedureControlMeasures(Base):
    """
    None
    """
    __tablename__ = 'IsmsOperationalProcedure_procedure_control_measures'

    IsmsOperationalProcedure_isms_id = Column(Text(), ForeignKey('IsmsOperationalProcedure.isms_id'), primary_key=True)
    procedure_control_measures = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOperationalProcedure_procedure_control_measures(IsmsOperationalProcedure_isms_id={self.IsmsOperationalProcedure_isms_id},procedure_control_measures={self.procedure_control_measures},)"



    


class IsmsOperationalProcedureProcedureRoles(Base):
    """
    None
    """
    __tablename__ = 'IsmsOperationalProcedure_procedure_roles'

    IsmsOperationalProcedure_isms_id = Column(Text(), ForeignKey('IsmsOperationalProcedure.isms_id'), primary_key=True)
    procedure_roles_isms_id = Column(Text(), ForeignKey('IsmsRole.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOperationalProcedure_procedure_roles(IsmsOperationalProcedure_isms_id={self.IsmsOperationalProcedure_isms_id},procedure_roles_isms_id={self.procedure_roles_isms_id},)"



    


class IsmsOperationalProcedureDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsOperationalProcedure_document_distribution'

    IsmsOperationalProcedure_isms_id = Column(Text(), ForeignKey('IsmsOperationalProcedure.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsOperationalProcedure_document_distribution(IsmsOperationalProcedure_isms_id={self.IsmsOperationalProcedure_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsMonitoringProgrammeDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsMonitoringProgramme_document_distribution'

    IsmsMonitoringProgramme_isms_id = Column(Text(), ForeignKey('IsmsMonitoringProgramme.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsMonitoringProgramme_document_distribution(IsmsMonitoringProgramme_isms_id={self.IsmsMonitoringProgramme_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsAuditProgrammeProgrammeAudits(Base):
    """
    None
    """
    __tablename__ = 'IsmsAuditProgramme_programme_audits'

    IsmsAuditProgramme_isms_id = Column(Text(), ForeignKey('IsmsAuditProgramme.isms_id'), primary_key=True)
    programme_audits_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAuditProgramme_programme_audits(IsmsAuditProgramme_isms_id={self.IsmsAuditProgramme_isms_id},programme_audits_isms_id={self.programme_audits_isms_id},)"



    


class IsmsAuditProgrammeDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsAuditProgramme_document_distribution'

    IsmsAuditProgramme_isms_id = Column(Text(), ForeignKey('IsmsAuditProgramme.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAuditProgramme_document_distribution(IsmsAuditProgramme_isms_id={self.IsmsAuditProgramme_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsAuditAuditStandards(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_standards'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_standards = Column(Enum('iso_iec_27001', 'iso_iec_27701', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1', name='IsmsManagementSystemStandard'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_standards(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_standards={self.audit_standards},)"



    


class IsmsAuditAuditCriteria(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_criteria'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_criteria = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_criteria(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_criteria={self.audit_criteria},)"



    


class IsmsAuditAuditObjectives(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_objectives'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_objectives = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_objectives(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_objectives={self.audit_objectives},)"



    


class IsmsAuditAuditTeam(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_team'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_team = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_team(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_team={self.audit_team},)"



    


class IsmsAuditAuditAuditees(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_auditees'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_auditees = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_auditees(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_auditees={self.audit_auditees},)"



    


class IsmsAuditAuditReportDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_audit_report_distribution'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    audit_report_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_audit_report_distribution(IsmsAudit_isms_id={self.IsmsAudit_isms_id},audit_report_distribution={self.audit_report_distribution},)"



    


class IsmsAuditDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsAudit_document_distribution'

    IsmsAudit_isms_id = Column(Text(), ForeignKey('IsmsAudit.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsAudit_document_distribution(IsmsAudit_isms_id={self.IsmsAudit_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsManagementReviewReviewAttendees(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementReview_review_attendees'

    IsmsManagementReview_isms_id = Column(Text(), ForeignKey('IsmsManagementReview.isms_id'), primary_key=True)
    review_attendees = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementReview_review_attendees(IsmsManagementReview_isms_id={self.IsmsManagementReview_isms_id},review_attendees={self.review_attendees},)"



    


class IsmsManagementReviewReviewImprovementOpportunities(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementReview_review_improvement_opportunities'

    IsmsManagementReview_isms_id = Column(Text(), ForeignKey('IsmsManagementReview.isms_id'), primary_key=True)
    review_improvement_opportunities = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementReview_review_improvement_opportunities(IsmsManagementReview_isms_id={self.IsmsManagementReview_isms_id},review_improvement_opportunities={self.review_improvement_opportunities},)"



    


class IsmsManagementReviewReviewDecisions(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementReview_review_decisions'

    IsmsManagementReview_isms_id = Column(Text(), ForeignKey('IsmsManagementReview.isms_id'), primary_key=True)
    review_decisions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementReview_review_decisions(IsmsManagementReview_isms_id={self.IsmsManagementReview_isms_id},review_decisions={self.review_decisions},)"



    


class IsmsManagementReviewReviewActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementReview_review_actions'

    IsmsManagementReview_isms_id = Column(Text(), ForeignKey('IsmsManagementReview.isms_id'), primary_key=True)
    review_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementReview_review_actions(IsmsManagementReview_isms_id={self.IsmsManagementReview_isms_id},review_actions={self.review_actions},)"



    


class IsmsManagementReviewDocumentDistribution(Base):
    """
    None
    """
    __tablename__ = 'IsmsManagementReview_document_distribution'

    IsmsManagementReview_isms_id = Column(Text(), ForeignKey('IsmsManagementReview.isms_id'), primary_key=True)
    document_distribution = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsManagementReview_document_distribution(IsmsManagementReview_isms_id={self.IsmsManagementReview_isms_id},document_distribution={self.document_distribution},)"



    


class IsmsNonconformityNonconformityImmediateActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsNonconformity_nonconformity_immediate_actions'

    IsmsNonconformity_isms_id = Column(Text(), ForeignKey('IsmsNonconformity.isms_id'), primary_key=True)
    nonconformity_immediate_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsNonconformity_nonconformity_immediate_actions(IsmsNonconformity_isms_id={self.IsmsNonconformity_isms_id},nonconformity_immediate_actions={self.nonconformity_immediate_actions},)"



    


class IsmsCorrectiveActionActionNonconformities(Base):
    """
    None
    """
    __tablename__ = 'IsmsCorrectiveAction_action_nonconformities'

    IsmsCorrectiveAction_isms_id = Column(Text(), ForeignKey('IsmsCorrectiveAction.isms_id'), primary_key=True)
    action_nonconformities_isms_id = Column(Text(), ForeignKey('IsmsNonconformity.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsCorrectiveAction_action_nonconformities(IsmsCorrectiveAction_isms_id={self.IsmsCorrectiveAction_isms_id},action_nonconformities_isms_id={self.action_nonconformities_isms_id},)"



    


class IsmsSecurityEventAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityEvent_affected_assets'

    IsmsSecurityEvent_isms_id = Column(Text(), ForeignKey('IsmsSecurityEvent.isms_id'), primary_key=True)
    affected_assets_isms_id = Column(Text(), ForeignKey('IsmsAsset.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityEvent_affected_assets(IsmsSecurityEvent_isms_id={self.IsmsSecurityEvent_isms_id},affected_assets_isms_id={self.affected_assets_isms_id},)"



    


class IsmsSecurityIncidentAffectedSecurityProperties(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_affected_security_properties'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    affected_security_properties = Column(Enum('confidentiality', 'integrity', 'availability', name='IsmsSecurityProperty'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_affected_security_properties(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},affected_security_properties={self.affected_security_properties},)"



    


class IsmsSecurityIncidentIncidentResponseActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_response_actions'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_response_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_response_actions(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_response_actions={self.incident_response_actions},)"



    


class IsmsSecurityIncidentIncidentContainmentActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_containment_actions'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_containment_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_containment_actions(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_containment_actions={self.incident_containment_actions},)"



    


class IsmsSecurityIncidentIncidentEradicationActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_eradication_actions'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_eradication_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_eradication_actions(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_eradication_actions={self.incident_eradication_actions},)"



    


class IsmsSecurityIncidentIncidentRecoveryActions(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_recovery_actions'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_recovery_actions = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_recovery_actions(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_recovery_actions={self.incident_recovery_actions},)"



    


class IsmsSecurityIncidentIncidentLessonsLearned(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_lessons_learned'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_lessons_learned = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_lessons_learned(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_lessons_learned={self.incident_lessons_learned},)"



    


class IsmsSecurityIncidentIncidentEvidence(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_evidence'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_evidence = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_evidence(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_evidence={self.incident_evidence},)"



    


class IsmsSecurityIncidentIncidentNotifications(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_incident_notifications'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    incident_notifications = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_incident_notifications(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},incident_notifications={self.incident_notifications},)"



    


class IsmsSecurityIncidentAffectedAssets(Base):
    """
    None
    """
    __tablename__ = 'IsmsSecurityIncident_affected_assets'

    IsmsSecurityIncident_isms_id = Column(Text(), ForeignKey('IsmsSecurityIncident.isms_id'), primary_key=True)
    affected_assets_isms_id = Column(Text(), ForeignKey('IsmsAsset.isms_id'), primary_key=True)
    

    def __repr__(self):
        return f"IsmsSecurityIncident_affected_assets(IsmsSecurityIncident_isms_id={self.IsmsSecurityIncident_isms_id},affected_assets_isms_id={self.affected_assets_isms_id},)"



    


class IsmsIncludedControl(IsmsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
    """
    __tablename__ = 'IsmsIncludedControl'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    implementation_state = Column(Enum('not_started', 'planned', 'in_progress', 'implemented', name='IsmsImplementationStatus'), nullable=False )
    responsible_role = Column(Text(), ForeignKey('IsmsRole.isms_id'))
    included_control = Column(Text(), ForeignKey('IsmsControl.isms_id'))
    included_evidence = Column(Text())
    included_target_date = Column(Date())
    entry_annex_a_control = Column(Enum('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34', name='IsmsAnnexAControl'))
    entry_type = Column(Text())
    entry_justification = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"IsmsIncludedControl(id={self.id},implementation_state={self.implementation_state},responsible_role={self.responsible_role},included_control={self.included_control},included_evidence={self.included_evidence},included_target_date={self.included_target_date},entry_annex_a_control={self.entry_annex_a_control},entry_type={self.entry_type},entry_justification={self.entry_justification},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IsmsExcludedControl(IsmsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """
    __tablename__ = 'IsmsExcludedControl'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    entry_annex_a_control = Column(Enum('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34', name='IsmsAnnexAControl'), nullable=False )
    entry_type = Column(Text())
    entry_justification = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"IsmsExcludedControl(id={self.id},entry_annex_a_control={self.entry_annex_a_control},entry_type={self.entry_type},entry_justification={self.entry_justification},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IsmsSecurityIncident(IsmsSecurityEvent):
    """
    An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
    """
    __tablename__ = 'IsmsSecurityIncident'

    incident_category = Column(Enum('malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other', name='IsmsIncidentCategory'))
    incident_severity = Column(Enum('very_low', 'low', 'medium', 'high', 'critical', name='IsmsRiskLevel'))
    incident_detection_method = Column(Text())
    incident_root_cause = Column(Text())
    incident_notification_required = Column(Boolean())
    incident_closed_at = Column(DateTime())
    incident_review = Column(Text())
    event_type = Column(Text())
    event_occurred_at = Column(DateTime())
    event_reporter = Column(Text())
    event_assessment = Column(Text())
    isms_id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    
    
    affected_security_properties_rel = relationship( "IsmsSecurityIncidentAffectedSecurityProperties" )
    affected_security_properties = association_proxy("affected_security_properties_rel", "affected_security_properties",
                                  creator=lambda x_: IsmsSecurityIncidentAffectedSecurityProperties(affected_security_properties=x_))
    
    
    incident_response_actions_rel = relationship( "IsmsSecurityIncidentIncidentResponseActions" )
    incident_response_actions = association_proxy("incident_response_actions_rel", "incident_response_actions",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentResponseActions(incident_response_actions=x_))
    
    
    incident_containment_actions_rel = relationship( "IsmsSecurityIncidentIncidentContainmentActions" )
    incident_containment_actions = association_proxy("incident_containment_actions_rel", "incident_containment_actions",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentContainmentActions(incident_containment_actions=x_))
    
    
    incident_eradication_actions_rel = relationship( "IsmsSecurityIncidentIncidentEradicationActions" )
    incident_eradication_actions = association_proxy("incident_eradication_actions_rel", "incident_eradication_actions",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentEradicationActions(incident_eradication_actions=x_))
    
    
    incident_recovery_actions_rel = relationship( "IsmsSecurityIncidentIncidentRecoveryActions" )
    incident_recovery_actions = association_proxy("incident_recovery_actions_rel", "incident_recovery_actions",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentRecoveryActions(incident_recovery_actions=x_))
    
    
    incident_lessons_learned_rel = relationship( "IsmsSecurityIncidentIncidentLessonsLearned" )
    incident_lessons_learned = association_proxy("incident_lessons_learned_rel", "incident_lessons_learned",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentLessonsLearned(incident_lessons_learned=x_))
    
    
    incident_evidence_rel = relationship( "IsmsSecurityIncidentIncidentEvidence" )
    incident_evidence = association_proxy("incident_evidence_rel", "incident_evidence",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentEvidence(incident_evidence=x_))
    
    
    incident_notifications_rel = relationship( "IsmsSecurityIncidentIncidentNotifications" )
    incident_notifications = association_proxy("incident_notifications_rel", "incident_notifications",
                                  creator=lambda x_: IsmsSecurityIncidentIncidentNotifications(incident_notifications=x_))
    
    
    # ManyToMany
    affected_assets = relationship( "IsmsAsset", secondary="IsmsSecurityIncident_affected_assets")
    

    def __repr__(self):
        return f"IsmsSecurityIncident(incident_category={self.incident_category},incident_severity={self.incident_severity},incident_detection_method={self.incident_detection_method},incident_root_cause={self.incident_root_cause},incident_notification_required={self.incident_notification_required},incident_closed_at={self.incident_closed_at},incident_review={self.incident_review},event_type={self.event_type},event_occurred_at={self.event_occurred_at},event_reporter={self.event_reporter},event_assessment={self.event_assessment},isms_id={self.isms_id},title={self.title},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


