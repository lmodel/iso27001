-- # Abstract Class: NamedEntity Description: Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Abstract Class: DocumentedInformation Description: Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityManagementSystem Description: Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required to support the full ISMS lifecycle.
--     * Slot: organization Description: Reference to the organization operating the ISMS.
--     * Slot: scope_statement Description: Documented statement of ISMS scope per 4.3.
--     * Slot: information_security_policy Description: Reference to the information security policy.
--     * Slot: risk_assessment_process Description: Reference to the risk assessment process.
--     * Slot: risk_treatment_process Description: Reference to the risk treatment process.
--     * Slot: statement_of_applicability Description: Reference to the Statement of Applicability.
--     * Slot: awareness_program Description: Reference to the awareness program.
--     * Slot: communication_plan Description: Reference to the communication plan.
--     * Slot: monitoring_program Description: Reference to the monitoring program.
--     * Slot: certification_status Description: Current certification status.
--     * Slot: certification_body Description: Accredited certification body.
--     * Slot: certification_date Description: Date certification was achieved.
--     * Slot: recertification_date Description: Date recertification is due.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Organization Description: The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
--     * Slot: legal_name Description: Legal registered name of the organization.
--     * Slot: organization_type Description: Type of organization (e.g., corporation, government, nonprofit).
--     * Slot: industry_sector Description: Primary industry sector of the organization.
--     * Slot: size_category Description: Organization size classification.
--     * Slot: employee_count Description: Approximate number of employees.
--     * Slot: parent_organization Description: Parent organization if applicable.
--     * Slot: climate_change_relevant Description: Whether climate change has been determined to be a relevant issue for the organization's context, per Clause 4.1 as amended by Amd. 1:2024.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InterestedParty Description: A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
--     * Slot: party_type Description: Category of interested party.
--     * Slot: relationship Description: Nature of the relationship with the organization.
--     * Slot: communication_needs Description: Communication requirements for this party.
--     * Slot: contact_information Description: Contact details for the party.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityPolicy Description: The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
--     * Slot: policy_statement Description: The core policy statement text.
--     * Slot: policy_objectives_framework Description: Framework for setting information security objectives.
--     * Slot: applicability_statement Description: Statement of policy applicability.
--     * Slot: communication_date Description: Date when the policy was communicated.
--     * Slot: acknowledgment_required Description: Whether acknowledgment is required from personnel.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: TopicSpecificPolicy Description: A policy addressing a specific information security topic, supporting the overarching information security policy.
--     * Slot: topic_area Description: The specific topic addressed by the policy.
--     * Slot: parent_policy Description: The parent policy this topic-specific policy supports.
--     * Slot: target_audience Description: Intended audience for the policy or document.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Role Description: An information security role with defined responsibilities and authorities per Clause 5.3.
--     * Slot: role_type Description: Category of the role.
--     * Slot: accountability Description: What the role is accountable for.
--     * Slot: delegation_rules Description: Rules for delegating responsibilities.
--     * Slot: reporting_line Description: To whom this role reports.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityObjective Description: A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
--     * Slot: objective_statement Description: Clear statement of the objective.
--     * Slot: target_value Description: Target value for the objective metric.
--     * Slot: current_value Description: Current measured value.
--     * Slot: metric_definition Description: Definition of how the objective is measured.
--     * Slot: measurement_method Description: Method used to measure the metric.
--     * Slot: measurement_frequency Description: How often measurement is performed.
--     * Slot: responsible_role Description: Role responsible for the objective or control.
--     * Slot: target_date Description: Target date for achieving the objective.
--     * Slot: achievement_status Description: Current status of objective achievement.
--     * Slot: action_plan Description: Plan for achieving the objective.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: RiskAssessmentProcess Description: The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
--     * Slot: risk_acceptance_criteria Description: Criteria for accepting risks.
--     * Slot: assessment_criteria Description: Criteria for performing risk assessments.
--     * Slot: assessment_methodology Description: Methodology used for risk assessment.
--     * Slot: likelihood_scale Description: Scale used for likelihood rating.
--     * Slot: impact_scale Description: Scale used for impact rating.
--     * Slot: risk_matrix Description: Risk matrix or calculation method.
--     * Slot: assessment_frequency Description: Planned frequency of risk assessments.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: RiskAssessment Description: An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
--     * Slot: assessment_scope Description: Scope of the assessment.
--     * Slot: assessment_date Description: Date the assessment was conducted.
--     * Slot: assessor Description: Person or team who conducted the assessment.
--     * Slot: methodology_used Description: Specific methodology applied in this assessment.
--     * Slot: summary_findings Description: Summary of assessment findings.
--     * Slot: next_assessment_date Description: Planned date for next assessment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Risk Description: An identified information security risk that may affect information security properties within the ISMS scope.
--     * Slot: risk_source Description: Source or origin of the risk.
--     * Slot: threat_description Description: Description of the threat exploiting the vulnerability.
--     * Slot: vulnerability_description Description: Description of the vulnerability that could be exploited.
--     * Slot: risk_owner Description: Person accountable for managing the risk.
--     * Slot: likelihood Description: Assessed likelihood of risk occurrence.
--     * Slot: impact Description: Assessed impact if risk materializes.
--     * Slot: inherent_risk_level Description: Risk level before controls are applied.
--     * Slot: residual_risk_level Description: Risk level after controls are applied.
--     * Slot: risk_treatment_option Description: Selected treatment option for the risk.
--     * Slot: treatment_priority Description: Priority for treating this risk.
--     * Slot: related_treatment_plan Description: Risk treatment plan addressing this risk.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: RiskTreatmentProcess Description: The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
--     * Slot: treatment_options_guidance Description: Guidance on selecting treatment options.
--     * Slot: control_selection_criteria Description: Criteria for selecting controls.
--     * Slot: soa_template Description: Template used for Statement of Applicability.
--     * Slot: approval_workflow Description: Workflow for approving risk treatment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: RiskTreatmentPlan Description: A risk treatment plan documenting planned actions to address identified risks through selected controls.
--     * Slot: plan_scope Description: Scope of the plan.
--     * Slot: resources_required Description: Resources required for implementation.
--     * Slot: implementation_timeline Description: Timeline for implementation.
--     * Slot: risk_owner_approval Description: Risk owner who approved the plan.
--     * Slot: approved_date Description: Date when the risk treatment plan was approved.
--     * Slot: residual_risk_acceptance Description: Documentation of residual risk acceptance.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: completion_date Description: Date when implementation was completed.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: StatementOfApplicability Description: The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation state.
--     * Slot: total_controls Description: Total number of controls in scope.
--     * Slot: implemented_count Description: Number of implemented controls.
--     * Slot: planned_count Description: Number of controls planned for implementation.
--     * Slot: not_applicable_count Description: Number of controls marked not applicable.
--     * Slot: last_review_date Description: Date of last review.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: SoAEntry Description: A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
--     * Slot: id
--     * Slot: control_reference Description: Reference to the control (e.g., A.5.1).
--     * Slot: is_applicable Description: Whether the control is applicable.
--     * Slot: inclusion_justification Description: Justification for including the control.
--     * Slot: exclusion_justification Description: Justification for excluding the control.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: implementation_evidence Description: Evidence of control implementation.
--     * Slot: responsible_role Description: Role responsible for the objective or control.
--     * Slot: target_implementation_date Description: Target date for implementing the control.
-- # Class: SecurityControl Description: A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
--     * Slot: control_id Description: Control identifier from Annex A (e.g., 5.1, 8.24).
--     * Slot: control_title Description: Title of the control.
--     * Slot: control_category Description: Domain category of the control.
--     * Slot: control_text Description: Organization-authored control statement or external control summary.
--     * Slot: implementation_guidance Description: Organization-authored implementation notes for the control.
--     * Slot: control_owner Description: Person responsible for the control.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: implementation_date Description: Date the control was implemented.
--     * Slot: effectiveness_rating Description: Rating of control effectiveness.
--     * Slot: last_test_date Description: Date the control was last tested.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Resource Description: A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
--     * Slot: resource_type Description: Type of resource.
--     * Slot: quantity Description: Quantity of the resource.
--     * Slot: allocation_date Description: Date the resource was allocated.
--     * Slot: allocated_to Description: What the resource is allocated to.
--     * Slot: cost Description: Cost of the resource.
--     * Slot: availability_status Description: Current availability of the resource.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CompetenceRecord Description: Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
--     * Slot: person_name Description: Name of the person.
--     * Slot: person_role Description: Role of the person.
--     * Slot: competency_assessment_date Description: Date of last competency assessment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AwarenessProgram Description: The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
--     * Slot: target_audience Description: Intended audience for the policy or document.
--     * Slot: frequency Description: Frequency of the activity.
--     * Slot: completion_tracking Description: How completion is tracked.
--     * Slot: effectiveness_measures Description: How effectiveness is measured.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CommunicationPlan Description: Plan for internal and external communications relevant to the ISMS per Clause 7.4.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CommunicationItem Description: A single communication requirement within the communication plan.
--     * Slot: id
--     * Slot: subject Description: Subject of the communication.
--     * Slot: purpose Description: Purpose of the communication.
--     * Slot: audience Description: Target audience.
--     * Slot: frequency Description: Frequency of the activity.
--     * Slot: method Description: Method of communication.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: records_required Description: Whether records are required.
-- # Class: OperationalProcedure Description: A documented procedure for operational planning and control per Clause 8.1.
--     * Slot: procedure_scope Description: Scope of the procedure.
--     * Slot: process_criteria Description: Criteria established for the process.
--     * Slot: change_control_requirements Description: Requirements for controlling changes.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: MonitoringProgram Description: The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: MonitoringItem Description: A single item to be monitored and measured per 9.1.
--     * Slot: id
--     * Slot: metric_name Description: Name of the metric.
--     * Slot: metric_description Description: Description of what is measured.
--     * Slot: measurement_method Description: Method used to measure the metric.
--     * Slot: measurement_frequency Description: How often measurement is performed.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: analysis_frequency Description: How often analysis is performed.
--     * Slot: analyst Description: Person performing analysis.
--     * Slot: target_threshold Description: Target threshold value.
--     * Slot: alert_threshold Description: Threshold triggering alerts.
--     * Slot: current_value Description: Current measured value.
--     * Slot: trend Description: Current trend direction.
-- # Class: InternalAudit Description: An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
--     * Slot: audit_reference Description: Reference identifier for the audit.
--     * Slot: audit_type Description: Type of audit.
--     * Slot: audit_scope Description: Scope of the audit.
--     * Slot: audit_period_start Description: Start date of audit period.
--     * Slot: audit_period_end Description: End date of audit period.
--     * Slot: lead_auditor Description: Lead auditor for the audit.
--     * Slot: audit_plan Description: Audit plan document reference.
--     * Slot: audit_conclusion Description: Overall audit conclusion.
--     * Slot: report_date Description: Date the report was issued.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AuditProgramme Description: The internal audit programme per 9.2.2, planning audit activities over a defined period.
--     * Slot: programme_period Description: Period covered by the audit programme.
--     * Slot: audit_frequency_rationale Description: Rationale for audit frequency decisions.
--     * Slot: resource_requirements Description: Resource requirements for the programme.
--     * Slot: auditor_qualifications Description: Required qualifications for auditors.
--     * Slot: programme_status Description: Current status of the programme.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AuditFinding Description: A finding from an internal audit, including nonconformities, observations, and positive findings.
--     * Slot: finding_type Description: Type of audit finding.
--     * Slot: clause_reference Description: Reference to standard clause.
--     * Slot: control_reference Description: Reference to the control (e.g., A.5.1).
--     * Slot: finding_description Description: Description of the finding.
--     * Slot: objective_evidence Description: Evidence supporting the finding.
--     * Slot: root_cause_analysis Description: Analysis of root cause.
--     * Slot: risk_implication Description: Risk implications of the finding.
--     * Slot: recommended_action Description: Recommended action to address finding.
--     * Slot: auditee_response Description: Response from the auditee.
--     * Slot: linked_corrective_action Description: Corrective action linked to this finding.
--     * Slot: closure_status Description: Status of finding closure.
--     * Slot: closure_date Description: Date the finding was closed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ManagementReview Description: A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness for purpose.
--     * Slot: review_date Description: Date when the management review was conducted.
--     * Slot: previous_actions_status Description: Status of actions from previous reviews.
--     * Slot: context_changes Description: Changes in context since last review.
--     * Slot: interested_party_changes Description: Changes in interested party requirements.
--     * Slot: performance_trends Description: Trends in information security performance.
--     * Slot: audit_results_summary Description: Summary of audit results.
--     * Slot: risk_assessment_results Description: Results of risk assessment.
--     * Slot: next_review_date Description: Planned date for next review.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Nonconformity Description: A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
--     * Slot: nonconformity_source Description: Source of nonconformity detection.
--     * Slot: detection_date Description: Date the nonconformity was detected.
--     * Slot: detected_by Description: Person or process that detected the nonconformity.
--     * Slot: requirement_violated Description: Requirement that was not fulfilled.
--     * Slot: nonconformity_description Description: Description of the nonconformity.
--     * Slot: consequences_addressed Description: How consequences were dealt with.
--     * Slot: root_cause Description: Root cause of the nonconformity.
--     * Slot: similar_nonconformities_check Description: Check for similar nonconformities elsewhere.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: closure_date Description: Date the finding was closed.
--     * Slot: closure_evidence Description: Evidence supporting closure.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CorrectiveAction Description: A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of recurrence.
--     * Slot: linked_nonconformity Description: Nonconformity this action addresses.
--     * Slot: action_description Description: Description of the action.
--     * Slot: root_cause_addressed Description: Root cause this action addresses.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: target_completion_date Description: Target date for completing the action.
--     * Slot: actual_completion_date Description: Actual date the action was completed.
--     * Slot: resources_required Description: Resources required for implementation.
--     * Slot: effectiveness_criteria Description: Criteria for evaluating effectiveness.
--     * Slot: effectiveness_review_date Description: Date effectiveness was reviewed.
--     * Slot: effectiveness_verified Description: Whether effectiveness was verified.
--     * Slot: isms_changes_required Description: Changes to ISMS required as a result.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ImprovementOpportunity Description: An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
--     * Slot: improvement_source Description: Source of the improvement opportunity.
--     * Slot: identification_date Description: Date identified.
--     * Slot: identified_by Description: Person who identified it.
--     * Slot: improvement_description Description: Description of the improvement.
--     * Slot: expected_benefit Description: Expected benefit from implementation.
--     * Slot: priority Description: Priority level.
--     * Slot: implementation_plan Description: Plan for implementing the improvement.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: target_date Description: Target date for achieving the objective.
--     * Slot: actual_completion_date Description: Actual date the action was completed.
--     * Slot: outcome_assessment Description: Assessment of actual outcomes.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Asset Description: An information asset or associated asset requiring protection, per Annex A control 5.9.
--     * Slot: asset_type Description: Type of asset.
--     * Slot: asset_owner Description: Owner of the asset.
--     * Slot: asset_custodian Description: Custodian responsible for day-to-day protection.
--     * Slot: classification Description: Information classification level.
--     * Slot: location Description: Physical or logical location.
--     * Slot: criticality Description: Criticality rating of the asset.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityEvent Description: An information security event per A.5.25, which may or may not be categorized as an incident.
--     * Slot: event_datetime Description: Date and time of the event.
--     * Slot: reporter Description: Person who reported the event.
--     * Slot: event_description Description: Description of the event.
--     * Slot: initial_assessment Description: Initial assessment of the event.
--     * Slot: categorized_as_incident Description: Whether the event was categorized as an incident.
--     * Slot: linked_incident Description: Linked incident if categorized.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityIncident Description: An information security incident per A.5.26, requiring response per documented procedures.
--     * Slot: incident_datetime Description: Date and time the incident occurred or was detected.
--     * Slot: incident_category Description: Category of incident.
--     * Slot: severity Description: Severity rating.
--     * Slot: incident_description Description: Description of the incident.
--     * Slot: detection_method Description: How the incident was detected.
--     * Slot: root_cause Description: Root cause of the nonconformity.
--     * Slot: lessons_learned Description: Lessons learned from the incident.
--     * Slot: notification_required Description: Whether notification to authorities/parties was required.
--     * Slot: closure_datetime Description: Date and time of incident closure.
--     * Slot: post_incident_review Description: Post-incident review findings.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InformationSecurityManagementSystem_scope_boundaries
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: scope_boundaries Description: Defined boundaries of the ISMS scope.
-- # Class: InformationSecurityManagementSystem_scope_exclusions
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: scope_exclusions Description: Any exclusions from scope with justification.
-- # Class: InformationSecurityManagementSystem_context_internal_issues
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: context_internal_issues Description: Internal issues relevant to ISMS per 4.1.
-- # Class: InformationSecurityManagementSystem_context_external_issues
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: context_external_issues Description: External issues relevant to ISMS per 4.1.
-- # Class: InformationSecurityManagementSystem_interested_parties
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: interested_parties_id Description: Stakeholders relevant to the ISMS.
-- # Class: InformationSecurityManagementSystem_objectives
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: objectives_id Description: Information security objectives.
-- # Class: InformationSecurityManagementSystem_controls
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: controls_id Description: Security controls applied in the ISMS.
-- # Class: InformationSecurityManagementSystem_roles
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: roles_id Description: Information security roles defined in the ISMS.
-- # Class: InformationSecurityManagementSystem_resources
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: resources_id Description: Resources provided for the ISMS.
-- # Class: InformationSecurityManagementSystem_competence_records
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: competence_records_id Description: Competence records for personnel.
-- # Class: InformationSecurityManagementSystem_documented_information_register
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: documented_information_register_id Description: Register of documented information.
-- # Class: InformationSecurityManagementSystem_operational_procedures
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: operational_procedures_id Description: Operational procedures.
-- # Class: InformationSecurityManagementSystem_risk_assessments
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: risk_assessments_id Description: Risk assessment instances.
-- # Class: InformationSecurityManagementSystem_risk_treatment_plans
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: risk_treatment_plans_id Description: Risk treatment plans.
-- # Class: InformationSecurityManagementSystem_internal_audits
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: internal_audits_id Description: Internal audit instances.
-- # Class: InformationSecurityManagementSystem_management_reviews
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: management_reviews_id Description: Management review instances.
-- # Class: InformationSecurityManagementSystem_nonconformities
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: nonconformities_id Description: Nonconformities identified.
-- # Class: InformationSecurityManagementSystem_corrective_actions
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: corrective_actions_id Description: Corrective actions.
-- # Class: InformationSecurityManagementSystem_improvements
--     * Slot: InformationSecurityManagementSystem_id Description: Autocreated FK slot
--     * Slot: improvements_id Description: Improvement opportunities tracked.
-- # Class: Organization_trading_names
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: trading_names Description: Names under which the organization conducts business.
-- # Class: Organization_geographic_locations
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: geographic_locations Description: Countries or regions where the organization operates.
-- # Class: Organization_regulatory_jurisdictions
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: regulatory_jurisdictions Description: Jurisdictions whose regulations apply to the organization.
-- # Class: Organization_subsidiaries
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: subsidiaries Description: Subsidiary organizations if applicable.
-- # Class: InterestedParty_requirements
--     * Slot: InterestedParty_id Description: Autocreated FK slot
--     * Slot: requirements Description: Requirements of the interested party.
-- # Class: InformationSecurityPolicy_commitment_statements
--     * Slot: InformationSecurityPolicy_id Description: Autocreated FK slot
--     * Slot: commitment_statements Description: Statements of commitment included in the policy.
-- # Class: InformationSecurityPolicy_related_topic_policies
--     * Slot: InformationSecurityPolicy_id Description: Autocreated FK slot
--     * Slot: related_topic_policies_id Description: Topic-specific policies supporting this policy.
-- # Class: TopicSpecificPolicy_applicable_controls
--     * Slot: TopicSpecificPolicy_id Description: Autocreated FK slot
--     * Slot: applicable_controls_id Description: Controls related to this policy.
-- # Class: Role_responsibilities
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Responsibilities assigned to the role.
-- # Class: Role_authorities
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: authorities Description: Authorities granted to the role.
-- # Class: Role_assigned_to
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: assigned_to Description: Person(s) assigned to this role.
-- # Class: InformationSecurityObjective_related_risks
--     * Slot: InformationSecurityObjective_id Description: Autocreated FK slot
--     * Slot: related_risks_id Description: Associated risks.
-- # Class: InformationSecurityObjective_related_controls
--     * Slot: InformationSecurityObjective_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other controls related to this one.
-- # Class: RiskAssessmentProcess_trigger_events
--     * Slot: RiskAssessmentProcess_id Description: Autocreated FK slot
--     * Slot: trigger_events Description: Events that trigger risk assessment outside planned schedule.
-- # Class: RiskAssessment_risks_identified
--     * Slot: RiskAssessment_id Description: Autocreated FK slot
--     * Slot: risks_identified_id Description: Risks identified in this assessment.
-- # Class: RiskAssessment_recommendations
--     * Slot: RiskAssessment_id Description: Autocreated FK slot
--     * Slot: recommendations Description: Recommendations from the assessment.
-- # Class: Risk_affected_assets
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: affected_assets_id Description: Assets affected by this risk or incident.
-- # Class: Risk_affected_cia_properties
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: affected_cia_properties Description: Which CIA properties are affected (confidentiality, integrity, availability).
-- # Class: Risk_existing_controls
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: existing_controls_id Description: Controls currently in place affecting this risk.
-- # Class: RiskTreatmentPlan_risks_addressed
--     * Slot: RiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: risks_addressed_id Description: Risks addressed by this plan.
-- # Class: RiskTreatmentPlan_treatment_actions
--     * Slot: RiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: treatment_actions Description: Actions to be taken for treatment.
-- # Class: RiskTreatmentPlan_controls_to_implement
--     * Slot: RiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: controls_to_implement_id Description: Controls to be implemented as part of treatment.
-- # Class: RiskTreatmentPlan_responsible_parties
--     * Slot: RiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: responsible_parties Description: Parties responsible for implementation.
-- # Class: StatementOfApplicability_soa_entries
--     * Slot: StatementOfApplicability_id Description: Autocreated FK slot
--     * Slot: soa_entries_id Description: Individual control entries in the SoA.
-- # Class: SecurityControl_related_controls
--     * Slot: SecurityControl_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other controls related to this one.
-- # Class: SecurityControl_applicable_threats
--     * Slot: SecurityControl_id Description: Autocreated FK slot
--     * Slot: applicable_threats Description: Threats this control addresses.
-- # Class: SecurityControl_applicable_assets
--     * Slot: SecurityControl_id Description: Autocreated FK slot
--     * Slot: applicable_assets Description: Asset types this control applies to.
-- # Class: SecurityControl_evidence_references
--     * Slot: SecurityControl_id Description: Autocreated FK slot
--     * Slot: evidence_references Description: References to evidence of implementation.
-- # Class: CompetenceRecord_required_competencies
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: required_competencies Description: Competencies required for the role.
-- # Class: CompetenceRecord_education_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: education_records Description: Education qualifications.
-- # Class: CompetenceRecord_training_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: training_records Description: Training completed.
-- # Class: CompetenceRecord_experience_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: experience_records Description: Relevant experience.
-- # Class: CompetenceRecord_competency_gaps
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: competency_gaps Description: Identified competency gaps.
-- # Class: CompetenceRecord_development_actions
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: development_actions Description: Actions to address competency gaps.
-- # Class: AwarenessProgram_awareness_topics
--     * Slot: AwarenessProgram_id Description: Autocreated FK slot
--     * Slot: awareness_topics Description: Topics covered in awareness program.
-- # Class: AwarenessProgram_delivery_methods
--     * Slot: AwarenessProgram_id Description: Autocreated FK slot
--     * Slot: delivery_methods Description: Methods used to deliver awareness content.
-- # Class: CommunicationPlan_communication_items
--     * Slot: CommunicationPlan_id Description: Autocreated FK slot
--     * Slot: communication_items_id Description: Communication items in the plan.
-- # Class: OperationalProcedure_control_measures
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: control_measures Description: Control measures implemented.
-- # Class: OperationalProcedure_responsible_roles
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: responsible_roles_id Description: Roles responsible for the procedure.
-- # Class: OperationalProcedure_related_controls
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other controls related to this one.
-- # Class: MonitoringProgram_monitoring_items
--     * Slot: MonitoringProgram_id Description: Autocreated FK slot
--     * Slot: monitoring_items_id Description: Items to be monitored.
-- # Class: InternalAudit_audit_criteria
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: audit_criteria Description: Criteria against which audit is conducted.
-- # Class: InternalAudit_audit_objectives
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: audit_objectives Description: Objectives of the audit.
-- # Class: InternalAudit_audit_team
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: audit_team Description: Audit team members.
-- # Class: InternalAudit_auditee_representatives
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: auditee_representatives Description: Representatives from audited areas.
-- # Class: InternalAudit_findings
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: findings_id Description: Audit findings.
-- # Class: InternalAudit_positive_observations
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: positive_observations Description: Positive observations noted.
-- # Class: InternalAudit_report_distribution
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: report_distribution Description: Distribution list for the report.
-- # Class: AuditProgramme_planned_audits
--     * Slot: AuditProgramme_id Description: Autocreated FK slot
--     * Slot: planned_audits_id Description: Audits planned in this programme.
-- # Class: ManagementReview_attendees
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: attendees Description: Attendees of the review.
-- # Class: ManagementReview_improvement_opportunities
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: improvement_opportunities Description: Opportunities for improvement identified.
-- # Class: ManagementReview_decisions
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: decisions Description: Decisions made in the review.
-- # Class: ManagementReview_action_items
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: action_items Description: Action items from the review.
-- # Class: Nonconformity_immediate_actions
--     * Slot: Nonconformity_id Description: Autocreated FK slot
--     * Slot: immediate_actions Description: Immediate actions taken to control/correct.
-- # Class: Nonconformity_linked_corrective_actions
--     * Slot: Nonconformity_id Description: Autocreated FK slot
--     * Slot: linked_corrective_actions_id Description: Corrective actions addressing this nonconformity.
-- # Class: Asset_related_risks
--     * Slot: Asset_id Description: Autocreated FK slot
--     * Slot: related_risks_id Description: Associated risks.
-- # Class: Asset_applicable_controls
--     * Slot: Asset_id Description: Autocreated FK slot
--     * Slot: applicable_controls_id Description: Controls related to this policy.
-- # Class: InformationSecurityEvent_affected_assets
--     * Slot: InformationSecurityEvent_id Description: Autocreated FK slot
--     * Slot: affected_assets_id Description: Assets affected by this risk or incident.
-- # Class: InformationSecurityIncident_affected_assets
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: affected_assets_id Description: Assets affected by this risk or incident.
-- # Class: InformationSecurityIncident_affected_cia
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: affected_cia Description: CIA properties affected.
-- # Class: InformationSecurityIncident_response_actions
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: response_actions Description: Actions taken in response.
-- # Class: InformationSecurityIncident_containment_actions
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: containment_actions Description: Actions to contain the incident.
-- # Class: InformationSecurityIncident_eradication_actions
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: eradication_actions Description: Actions to eradicate the cause.
-- # Class: InformationSecurityIncident_recovery_actions
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: recovery_actions Description: Actions to recover normal operations.
-- # Class: InformationSecurityIncident_evidence_collected
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: evidence_collected Description: Evidence collected.
-- # Class: InformationSecurityIncident_notifications_made
--     * Slot: InformationSecurityIncident_id Description: Autocreated FK slot
--     * Slot: notifications_made Description: Notifications that were made.

CREATE TABLE "NamedEntity" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedEntity_id" ON "NamedEntity" (id);

CREATE TABLE "DocumentedInformation" (
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DocumentedInformation_id" ON "DocumentedInformation" (id);

CREATE TABLE "Organization" (
	legal_name TEXT,
	organization_type TEXT,
	industry_sector TEXT,
	size_category TEXT,
	employee_count INTEGER,
	parent_organization TEXT,
	climate_change_relevant BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Organization_id" ON "Organization" (id);

CREATE TABLE "InterestedParty" (
	party_type TEXT,
	relationship TEXT,
	communication_needs TEXT,
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InterestedParty_id" ON "InterestedParty" (id);

CREATE TABLE "InformationSecurityPolicy" (
	policy_statement TEXT,
	policy_objectives_framework TEXT,
	applicability_statement TEXT,
	communication_date DATE,
	acknowledgment_required BOOLEAN,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InformationSecurityPolicy_id" ON "InformationSecurityPolicy" (id);

CREATE TABLE "Role" (
	role_type TEXT,
	accountability TEXT,
	delegation_rules TEXT,
	reporting_line TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Role_id" ON "Role" (id);

CREATE TABLE "RiskAssessmentProcess" (
	risk_acceptance_criteria TEXT,
	assessment_criteria TEXT,
	assessment_methodology TEXT,
	likelihood_scale TEXT,
	impact_scale TEXT,
	risk_matrix TEXT,
	assessment_frequency TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskAssessmentProcess_id" ON "RiskAssessmentProcess" (id);

CREATE TABLE "RiskAssessment" (
	assessment_scope TEXT,
	assessment_date DATE,
	assessor TEXT,
	methodology_used TEXT,
	summary_findings TEXT,
	next_assessment_date DATE,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskAssessment_id" ON "RiskAssessment" (id);

CREATE TABLE "RiskTreatmentProcess" (
	treatment_options_guidance TEXT,
	control_selection_criteria TEXT,
	soa_template TEXT,
	approval_workflow TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskTreatmentProcess_id" ON "RiskTreatmentProcess" (id);

CREATE TABLE "RiskTreatmentPlan" (
	plan_scope TEXT,
	resources_required TEXT,
	implementation_timeline TEXT,
	risk_owner_approval TEXT,
	approved_date DATE,
	residual_risk_acceptance TEXT,
	implementation_status VARCHAR(14),
	completion_date DATE,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskTreatmentPlan_id" ON "RiskTreatmentPlan" (id);

CREATE TABLE "StatementOfApplicability" (
	total_controls INTEGER,
	implemented_count INTEGER,
	planned_count INTEGER,
	not_applicable_count INTEGER,
	last_review_date DATE,
	approved_by TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StatementOfApplicability_id" ON "StatementOfApplicability" (id);

CREATE TABLE "SecurityControl" (
	control_id TEXT,
	control_title TEXT,
	control_category VARCHAR(14),
	control_text TEXT,
	implementation_guidance TEXT,
	control_owner TEXT,
	implementation_status VARCHAR(14),
	implementation_date DATE,
	effectiveness_rating TEXT,
	last_test_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SecurityControl_id" ON "SecurityControl" (id);

CREATE TABLE "Resource" (
	resource_type TEXT,
	quantity TEXT,
	allocation_date DATE,
	allocated_to TEXT,
	cost TEXT,
	availability_status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "CompetenceRecord" (
	person_name TEXT,
	person_role TEXT,
	competency_assessment_date DATE,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CompetenceRecord_id" ON "CompetenceRecord" (id);

CREATE TABLE "AwarenessProgram" (
	target_audience TEXT,
	frequency TEXT,
	completion_tracking TEXT,
	effectiveness_measures TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AwarenessProgram_id" ON "AwarenessProgram" (id);

CREATE TABLE "CommunicationPlan" (
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CommunicationPlan_id" ON "CommunicationPlan" (id);

CREATE TABLE "CommunicationItem" (
	id INTEGER NOT NULL,
	subject TEXT,
	purpose TEXT,
	audience TEXT,
	frequency TEXT,
	method TEXT,
	responsible_party TEXT,
	records_required BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CommunicationItem_id" ON "CommunicationItem" (id);

CREATE TABLE "OperationalProcedure" (
	procedure_scope TEXT,
	process_criteria TEXT,
	change_control_requirements TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OperationalProcedure_id" ON "OperationalProcedure" (id);

CREATE TABLE "MonitoringProgram" (
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MonitoringProgram_id" ON "MonitoringProgram" (id);

CREATE TABLE "MonitoringItem" (
	id INTEGER NOT NULL,
	metric_name TEXT,
	metric_description TEXT,
	measurement_method TEXT,
	measurement_frequency TEXT,
	responsible_party TEXT,
	analysis_frequency TEXT,
	analyst TEXT,
	target_threshold TEXT,
	alert_threshold TEXT,
	current_value TEXT,
	trend TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MonitoringItem_id" ON "MonitoringItem" (id);

CREATE TABLE "InternalAudit" (
	audit_reference TEXT,
	audit_type TEXT,
	audit_scope TEXT,
	audit_period_start DATE,
	audit_period_end DATE,
	lead_auditor TEXT,
	audit_plan TEXT,
	audit_conclusion TEXT,
	report_date DATE,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InternalAudit_id" ON "InternalAudit" (id);

CREATE TABLE "AuditProgramme" (
	programme_period TEXT,
	audit_frequency_rationale TEXT,
	resource_requirements TEXT,
	auditor_qualifications TEXT,
	programme_status TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AuditProgramme_id" ON "AuditProgramme" (id);

CREATE TABLE "ManagementReview" (
	review_date DATE,
	previous_actions_status TEXT,
	context_changes TEXT,
	interested_party_changes TEXT,
	performance_trends TEXT,
	audit_results_summary TEXT,
	risk_assessment_results TEXT,
	next_review_date DATE,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ManagementReview_id" ON "ManagementReview" (id);

CREATE TABLE "Nonconformity" (
	nonconformity_source TEXT,
	detection_date DATE,
	detected_by TEXT,
	requirement_violated TEXT,
	nonconformity_description TEXT,
	consequences_addressed TEXT,
	root_cause TEXT,
	similar_nonconformities_check TEXT,
	status TEXT,
	closure_date DATE,
	closure_evidence TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Nonconformity_id" ON "Nonconformity" (id);

CREATE TABLE "ImprovementOpportunity" (
	improvement_source TEXT,
	identification_date DATE,
	identified_by TEXT,
	improvement_description TEXT,
	expected_benefit TEXT,
	priority TEXT,
	implementation_plan TEXT,
	responsible_party TEXT,
	target_date DATE,
	actual_completion_date DATE,
	outcome_assessment TEXT,
	status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ImprovementOpportunity_id" ON "ImprovementOpportunity" (id);

CREATE TABLE "Asset" (
	asset_type TEXT,
	asset_owner TEXT,
	asset_custodian TEXT,
	classification TEXT,
	location TEXT,
	criticality TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Asset_id" ON "Asset" (id);

CREATE TABLE "InformationSecurityIncident" (
	incident_datetime DATETIME,
	incident_category TEXT,
	severity TEXT,
	incident_description TEXT,
	detection_method TEXT,
	root_cause TEXT,
	lessons_learned TEXT,
	notification_required BOOLEAN,
	closure_datetime DATETIME,
	post_incident_review TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InformationSecurityIncident_id" ON "InformationSecurityIncident" (id);

CREATE TABLE "InformationSecurityManagementSystem" (
	organization TEXT,
	scope_statement TEXT,
	information_security_policy TEXT,
	risk_assessment_process TEXT,
	risk_treatment_process TEXT,
	statement_of_applicability TEXT,
	awareness_program TEXT,
	communication_plan TEXT,
	monitoring_program TEXT,
	certification_status TEXT,
	certification_body TEXT,
	certification_date DATE,
	recertification_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(organization) REFERENCES "Organization" (id),
	FOREIGN KEY(information_security_policy) REFERENCES "InformationSecurityPolicy" (id),
	FOREIGN KEY(risk_assessment_process) REFERENCES "RiskAssessmentProcess" (id),
	FOREIGN KEY(risk_treatment_process) REFERENCES "RiskTreatmentProcess" (id),
	FOREIGN KEY(statement_of_applicability) REFERENCES "StatementOfApplicability" (id),
	FOREIGN KEY(awareness_program) REFERENCES "AwarenessProgram" (id),
	FOREIGN KEY(communication_plan) REFERENCES "CommunicationPlan" (id),
	FOREIGN KEY(monitoring_program) REFERENCES "MonitoringProgram" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem" (id);

CREATE TABLE "TopicSpecificPolicy" (
	topic_area TEXT,
	parent_policy TEXT,
	target_audience TEXT,
	document_type VARCHAR(9),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(parent_policy) REFERENCES "InformationSecurityPolicy" (id)
);
CREATE INDEX "ix_TopicSpecificPolicy_id" ON "TopicSpecificPolicy" (id);

CREATE TABLE "InformationSecurityObjective" (
	objective_statement TEXT,
	target_value TEXT,
	current_value TEXT,
	metric_definition TEXT,
	measurement_method TEXT,
	measurement_frequency TEXT,
	responsible_role TEXT,
	target_date DATE,
	achievement_status TEXT,
	action_plan TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(responsible_role) REFERENCES "Role" (id)
);
CREATE INDEX "ix_InformationSecurityObjective_id" ON "InformationSecurityObjective" (id);

CREATE TABLE "Risk" (
	risk_source TEXT,
	threat_description TEXT,
	vulnerability_description TEXT,
	risk_owner TEXT,
	likelihood VARCHAR(14),
	impact VARCHAR(10),
	inherent_risk_level VARCHAR(8),
	residual_risk_level VARCHAR(8),
	risk_treatment_option VARCHAR(6),
	treatment_priority TEXT,
	related_treatment_plan TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(related_treatment_plan) REFERENCES "RiskTreatmentPlan" (id)
);
CREATE INDEX "ix_Risk_id" ON "Risk" (id);

CREATE TABLE "SoAEntry" (
	id INTEGER NOT NULL,
	control_reference TEXT,
	is_applicable BOOLEAN,
	inclusion_justification TEXT,
	exclusion_justification TEXT,
	implementation_status VARCHAR(14),
	implementation_evidence TEXT,
	responsible_role TEXT,
	target_implementation_date DATE,
	PRIMARY KEY (id),
	FOREIGN KEY(control_reference) REFERENCES "SecurityControl" (id),
	FOREIGN KEY(responsible_role) REFERENCES "Role" (id)
);
CREATE INDEX "ix_SoAEntry_id" ON "SoAEntry" (id);

CREATE TABLE "CorrectiveAction" (
	linked_nonconformity TEXT,
	action_description TEXT,
	root_cause_addressed TEXT,
	responsible_party TEXT,
	target_completion_date DATE,
	actual_completion_date DATE,
	resources_required TEXT,
	effectiveness_criteria TEXT,
	effectiveness_review_date DATE,
	effectiveness_verified BOOLEAN,
	isms_changes_required TEXT,
	status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(linked_nonconformity) REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_CorrectiveAction_id" ON "CorrectiveAction" (id);

CREATE TABLE "InformationSecurityEvent" (
	event_datetime DATETIME,
	reporter TEXT,
	event_description TEXT,
	initial_assessment TEXT,
	categorized_as_incident BOOLEAN,
	linked_incident TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(linked_incident) REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityEvent_id" ON "InformationSecurityEvent" (id);

CREATE TABLE "Organization_trading_names" (
	"Organization_id" TEXT,
	trading_names TEXT,
	PRIMARY KEY ("Organization_id", trading_names),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_trading_names_trading_names" ON "Organization_trading_names" (trading_names);
CREATE INDEX "ix_Organization_trading_names_Organization_id" ON "Organization_trading_names" ("Organization_id");

CREATE TABLE "Organization_geographic_locations" (
	"Organization_id" TEXT,
	geographic_locations TEXT,
	PRIMARY KEY ("Organization_id", geographic_locations),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_geographic_locations_Organization_id" ON "Organization_geographic_locations" ("Organization_id");
CREATE INDEX "ix_Organization_geographic_locations_geographic_locations" ON "Organization_geographic_locations" (geographic_locations);

CREATE TABLE "Organization_regulatory_jurisdictions" (
	"Organization_id" TEXT,
	regulatory_jurisdictions TEXT,
	PRIMARY KEY ("Organization_id", regulatory_jurisdictions),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_regulatory_jurisdictions_regulatory_jurisdictions" ON "Organization_regulatory_jurisdictions" (regulatory_jurisdictions);
CREATE INDEX "ix_Organization_regulatory_jurisdictions_Organization_id" ON "Organization_regulatory_jurisdictions" ("Organization_id");

CREATE TABLE "Organization_subsidiaries" (
	"Organization_id" TEXT,
	subsidiaries TEXT,
	PRIMARY KEY ("Organization_id", subsidiaries),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_subsidiaries_subsidiaries" ON "Organization_subsidiaries" (subsidiaries);
CREATE INDEX "ix_Organization_subsidiaries_Organization_id" ON "Organization_subsidiaries" ("Organization_id");

CREATE TABLE "InterestedParty_requirements" (
	"InterestedParty_id" TEXT,
	requirements TEXT,
	PRIMARY KEY ("InterestedParty_id", requirements),
	FOREIGN KEY("InterestedParty_id") REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_InterestedParty_requirements_requirements" ON "InterestedParty_requirements" (requirements);
CREATE INDEX "ix_InterestedParty_requirements_InterestedParty_id" ON "InterestedParty_requirements" ("InterestedParty_id");

CREATE TABLE "InformationSecurityPolicy_commitment_statements" (
	"InformationSecurityPolicy_id" TEXT,
	commitment_statements TEXT,
	PRIMARY KEY ("InformationSecurityPolicy_id", commitment_statements),
	FOREIGN KEY("InformationSecurityPolicy_id") REFERENCES "InformationSecurityPolicy" (id)
);
CREATE INDEX "ix_InformationSecurityPolicy_commitment_statements_InformationSecurityPolicy_id" ON "InformationSecurityPolicy_commitment_statements" ("InformationSecurityPolicy_id");
CREATE INDEX "ix_InformationSecurityPolicy_commitment_statements_commitment_statements" ON "InformationSecurityPolicy_commitment_statements" (commitment_statements);

CREATE TABLE "Role_responsibilities" (
	"Role_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("Role_id", responsibilities),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_responsibilities_responsibilities" ON "Role_responsibilities" (responsibilities);
CREATE INDEX "ix_Role_responsibilities_Role_id" ON "Role_responsibilities" ("Role_id");

CREATE TABLE "Role_authorities" (
	"Role_id" TEXT,
	authorities TEXT,
	PRIMARY KEY ("Role_id", authorities),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_authorities_authorities" ON "Role_authorities" (authorities);
CREATE INDEX "ix_Role_authorities_Role_id" ON "Role_authorities" ("Role_id");

CREATE TABLE "Role_assigned_to" (
	"Role_id" TEXT,
	assigned_to TEXT,
	PRIMARY KEY ("Role_id", assigned_to),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_assigned_to_Role_id" ON "Role_assigned_to" ("Role_id");
CREATE INDEX "ix_Role_assigned_to_assigned_to" ON "Role_assigned_to" (assigned_to);

CREATE TABLE "RiskAssessmentProcess_trigger_events" (
	"RiskAssessmentProcess_id" TEXT,
	trigger_events TEXT,
	PRIMARY KEY ("RiskAssessmentProcess_id", trigger_events),
	FOREIGN KEY("RiskAssessmentProcess_id") REFERENCES "RiskAssessmentProcess" (id)
);
CREATE INDEX "ix_RiskAssessmentProcess_trigger_events_trigger_events" ON "RiskAssessmentProcess_trigger_events" (trigger_events);
CREATE INDEX "ix_RiskAssessmentProcess_trigger_events_RiskAssessmentProcess_id" ON "RiskAssessmentProcess_trigger_events" ("RiskAssessmentProcess_id");

CREATE TABLE "RiskAssessment_recommendations" (
	"RiskAssessment_id" TEXT,
	recommendations TEXT,
	PRIMARY KEY ("RiskAssessment_id", recommendations),
	FOREIGN KEY("RiskAssessment_id") REFERENCES "RiskAssessment" (id)
);
CREATE INDEX "ix_RiskAssessment_recommendations_recommendations" ON "RiskAssessment_recommendations" (recommendations);
CREATE INDEX "ix_RiskAssessment_recommendations_RiskAssessment_id" ON "RiskAssessment_recommendations" ("RiskAssessment_id");

CREATE TABLE "RiskTreatmentPlan_treatment_actions" (
	"RiskTreatmentPlan_id" TEXT,
	treatment_actions TEXT,
	PRIMARY KEY ("RiskTreatmentPlan_id", treatment_actions),
	FOREIGN KEY("RiskTreatmentPlan_id") REFERENCES "RiskTreatmentPlan" (id)
);
CREATE INDEX "ix_RiskTreatmentPlan_treatment_actions_treatment_actions" ON "RiskTreatmentPlan_treatment_actions" (treatment_actions);
CREATE INDEX "ix_RiskTreatmentPlan_treatment_actions_RiskTreatmentPlan_id" ON "RiskTreatmentPlan_treatment_actions" ("RiskTreatmentPlan_id");

CREATE TABLE "RiskTreatmentPlan_controls_to_implement" (
	"RiskTreatmentPlan_id" TEXT,
	controls_to_implement_id TEXT,
	PRIMARY KEY ("RiskTreatmentPlan_id", controls_to_implement_id),
	FOREIGN KEY("RiskTreatmentPlan_id") REFERENCES "RiskTreatmentPlan" (id),
	FOREIGN KEY(controls_to_implement_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_RiskTreatmentPlan_controls_to_implement_controls_to_implement_id" ON "RiskTreatmentPlan_controls_to_implement" (controls_to_implement_id);
CREATE INDEX "ix_RiskTreatmentPlan_controls_to_implement_RiskTreatmentPlan_id" ON "RiskTreatmentPlan_controls_to_implement" ("RiskTreatmentPlan_id");

CREATE TABLE "RiskTreatmentPlan_responsible_parties" (
	"RiskTreatmentPlan_id" TEXT,
	responsible_parties TEXT,
	PRIMARY KEY ("RiskTreatmentPlan_id", responsible_parties),
	FOREIGN KEY("RiskTreatmentPlan_id") REFERENCES "RiskTreatmentPlan" (id)
);
CREATE INDEX "ix_RiskTreatmentPlan_responsible_parties_RiskTreatmentPlan_id" ON "RiskTreatmentPlan_responsible_parties" ("RiskTreatmentPlan_id");
CREATE INDEX "ix_RiskTreatmentPlan_responsible_parties_responsible_parties" ON "RiskTreatmentPlan_responsible_parties" (responsible_parties);

CREATE TABLE "SecurityControl_related_controls" (
	"SecurityControl_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("SecurityControl_id", related_controls_id),
	FOREIGN KEY("SecurityControl_id") REFERENCES "SecurityControl" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_SecurityControl_related_controls_SecurityControl_id" ON "SecurityControl_related_controls" ("SecurityControl_id");
CREATE INDEX "ix_SecurityControl_related_controls_related_controls_id" ON "SecurityControl_related_controls" (related_controls_id);

CREATE TABLE "SecurityControl_applicable_threats" (
	"SecurityControl_id" TEXT,
	applicable_threats TEXT,
	PRIMARY KEY ("SecurityControl_id", applicable_threats),
	FOREIGN KEY("SecurityControl_id") REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_SecurityControl_applicable_threats_applicable_threats" ON "SecurityControl_applicable_threats" (applicable_threats);
CREATE INDEX "ix_SecurityControl_applicable_threats_SecurityControl_id" ON "SecurityControl_applicable_threats" ("SecurityControl_id");

CREATE TABLE "SecurityControl_applicable_assets" (
	"SecurityControl_id" TEXT,
	applicable_assets TEXT,
	PRIMARY KEY ("SecurityControl_id", applicable_assets),
	FOREIGN KEY("SecurityControl_id") REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_SecurityControl_applicable_assets_SecurityControl_id" ON "SecurityControl_applicable_assets" ("SecurityControl_id");
CREATE INDEX "ix_SecurityControl_applicable_assets_applicable_assets" ON "SecurityControl_applicable_assets" (applicable_assets);

CREATE TABLE "SecurityControl_evidence_references" (
	"SecurityControl_id" TEXT,
	evidence_references TEXT,
	PRIMARY KEY ("SecurityControl_id", evidence_references),
	FOREIGN KEY("SecurityControl_id") REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_SecurityControl_evidence_references_SecurityControl_id" ON "SecurityControl_evidence_references" ("SecurityControl_id");
CREATE INDEX "ix_SecurityControl_evidence_references_evidence_references" ON "SecurityControl_evidence_references" (evidence_references);

CREATE TABLE "CompetenceRecord_required_competencies" (
	"CompetenceRecord_id" TEXT,
	required_competencies TEXT,
	PRIMARY KEY ("CompetenceRecord_id", required_competencies),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_required_competencies_required_competencies" ON "CompetenceRecord_required_competencies" (required_competencies);
CREATE INDEX "ix_CompetenceRecord_required_competencies_CompetenceRecord_id" ON "CompetenceRecord_required_competencies" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_education_records" (
	"CompetenceRecord_id" TEXT,
	education_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", education_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_education_records_CompetenceRecord_id" ON "CompetenceRecord_education_records" ("CompetenceRecord_id");
CREATE INDEX "ix_CompetenceRecord_education_records_education_records" ON "CompetenceRecord_education_records" (education_records);

CREATE TABLE "CompetenceRecord_training_records" (
	"CompetenceRecord_id" TEXT,
	training_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", training_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_training_records_CompetenceRecord_id" ON "CompetenceRecord_training_records" ("CompetenceRecord_id");
CREATE INDEX "ix_CompetenceRecord_training_records_training_records" ON "CompetenceRecord_training_records" (training_records);

CREATE TABLE "CompetenceRecord_experience_records" (
	"CompetenceRecord_id" TEXT,
	experience_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", experience_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_experience_records_experience_records" ON "CompetenceRecord_experience_records" (experience_records);
CREATE INDEX "ix_CompetenceRecord_experience_records_CompetenceRecord_id" ON "CompetenceRecord_experience_records" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_competency_gaps" (
	"CompetenceRecord_id" TEXT,
	competency_gaps TEXT,
	PRIMARY KEY ("CompetenceRecord_id", competency_gaps),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_competency_gaps_competency_gaps" ON "CompetenceRecord_competency_gaps" (competency_gaps);
CREATE INDEX "ix_CompetenceRecord_competency_gaps_CompetenceRecord_id" ON "CompetenceRecord_competency_gaps" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_development_actions" (
	"CompetenceRecord_id" TEXT,
	development_actions TEXT,
	PRIMARY KEY ("CompetenceRecord_id", development_actions),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_development_actions_development_actions" ON "CompetenceRecord_development_actions" (development_actions);
CREATE INDEX "ix_CompetenceRecord_development_actions_CompetenceRecord_id" ON "CompetenceRecord_development_actions" ("CompetenceRecord_id");

CREATE TABLE "AwarenessProgram_awareness_topics" (
	"AwarenessProgram_id" TEXT,
	awareness_topics TEXT,
	PRIMARY KEY ("AwarenessProgram_id", awareness_topics),
	FOREIGN KEY("AwarenessProgram_id") REFERENCES "AwarenessProgram" (id)
);
CREATE INDEX "ix_AwarenessProgram_awareness_topics_AwarenessProgram_id" ON "AwarenessProgram_awareness_topics" ("AwarenessProgram_id");
CREATE INDEX "ix_AwarenessProgram_awareness_topics_awareness_topics" ON "AwarenessProgram_awareness_topics" (awareness_topics);

CREATE TABLE "AwarenessProgram_delivery_methods" (
	"AwarenessProgram_id" TEXT,
	delivery_methods TEXT,
	PRIMARY KEY ("AwarenessProgram_id", delivery_methods),
	FOREIGN KEY("AwarenessProgram_id") REFERENCES "AwarenessProgram" (id)
);
CREATE INDEX "ix_AwarenessProgram_delivery_methods_AwarenessProgram_id" ON "AwarenessProgram_delivery_methods" ("AwarenessProgram_id");
CREATE INDEX "ix_AwarenessProgram_delivery_methods_delivery_methods" ON "AwarenessProgram_delivery_methods" (delivery_methods);

CREATE TABLE "CommunicationPlan_communication_items" (
	"CommunicationPlan_id" TEXT,
	communication_items_id INTEGER,
	PRIMARY KEY ("CommunicationPlan_id", communication_items_id),
	FOREIGN KEY("CommunicationPlan_id") REFERENCES "CommunicationPlan" (id),
	FOREIGN KEY(communication_items_id) REFERENCES "CommunicationItem" (id)
);
CREATE INDEX "ix_CommunicationPlan_communication_items_communication_items_id" ON "CommunicationPlan_communication_items" (communication_items_id);
CREATE INDEX "ix_CommunicationPlan_communication_items_CommunicationPlan_id" ON "CommunicationPlan_communication_items" ("CommunicationPlan_id");

CREATE TABLE "OperationalProcedure_control_measures" (
	"OperationalProcedure_id" TEXT,
	control_measures TEXT,
	PRIMARY KEY ("OperationalProcedure_id", control_measures),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id)
);
CREATE INDEX "ix_OperationalProcedure_control_measures_control_measures" ON "OperationalProcedure_control_measures" (control_measures);
CREATE INDEX "ix_OperationalProcedure_control_measures_OperationalProcedure_id" ON "OperationalProcedure_control_measures" ("OperationalProcedure_id");

CREATE TABLE "OperationalProcedure_responsible_roles" (
	"OperationalProcedure_id" TEXT,
	responsible_roles_id TEXT,
	PRIMARY KEY ("OperationalProcedure_id", responsible_roles_id),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id),
	FOREIGN KEY(responsible_roles_id) REFERENCES "Role" (id)
);
CREATE INDEX "ix_OperationalProcedure_responsible_roles_OperationalProcedure_id" ON "OperationalProcedure_responsible_roles" ("OperationalProcedure_id");
CREATE INDEX "ix_OperationalProcedure_responsible_roles_responsible_roles_id" ON "OperationalProcedure_responsible_roles" (responsible_roles_id);

CREATE TABLE "OperationalProcedure_related_controls" (
	"OperationalProcedure_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("OperationalProcedure_id", related_controls_id),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_OperationalProcedure_related_controls_OperationalProcedure_id" ON "OperationalProcedure_related_controls" ("OperationalProcedure_id");
CREATE INDEX "ix_OperationalProcedure_related_controls_related_controls_id" ON "OperationalProcedure_related_controls" (related_controls_id);

CREATE TABLE "MonitoringProgram_monitoring_items" (
	"MonitoringProgram_id" TEXT,
	monitoring_items_id INTEGER,
	PRIMARY KEY ("MonitoringProgram_id", monitoring_items_id),
	FOREIGN KEY("MonitoringProgram_id") REFERENCES "MonitoringProgram" (id),
	FOREIGN KEY(monitoring_items_id) REFERENCES "MonitoringItem" (id)
);
CREATE INDEX "ix_MonitoringProgram_monitoring_items_monitoring_items_id" ON "MonitoringProgram_monitoring_items" (monitoring_items_id);
CREATE INDEX "ix_MonitoringProgram_monitoring_items_MonitoringProgram_id" ON "MonitoringProgram_monitoring_items" ("MonitoringProgram_id");

CREATE TABLE "InternalAudit_audit_criteria" (
	"InternalAudit_id" TEXT,
	audit_criteria TEXT,
	PRIMARY KEY ("InternalAudit_id", audit_criteria),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_audit_criteria_audit_criteria" ON "InternalAudit_audit_criteria" (audit_criteria);
CREATE INDEX "ix_InternalAudit_audit_criteria_InternalAudit_id" ON "InternalAudit_audit_criteria" ("InternalAudit_id");

CREATE TABLE "InternalAudit_audit_objectives" (
	"InternalAudit_id" TEXT,
	audit_objectives TEXT,
	PRIMARY KEY ("InternalAudit_id", audit_objectives),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_audit_objectives_InternalAudit_id" ON "InternalAudit_audit_objectives" ("InternalAudit_id");
CREATE INDEX "ix_InternalAudit_audit_objectives_audit_objectives" ON "InternalAudit_audit_objectives" (audit_objectives);

CREATE TABLE "InternalAudit_audit_team" (
	"InternalAudit_id" TEXT,
	audit_team TEXT,
	PRIMARY KEY ("InternalAudit_id", audit_team),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_audit_team_audit_team" ON "InternalAudit_audit_team" (audit_team);
CREATE INDEX "ix_InternalAudit_audit_team_InternalAudit_id" ON "InternalAudit_audit_team" ("InternalAudit_id");

CREATE TABLE "InternalAudit_auditee_representatives" (
	"InternalAudit_id" TEXT,
	auditee_representatives TEXT,
	PRIMARY KEY ("InternalAudit_id", auditee_representatives),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_auditee_representatives_InternalAudit_id" ON "InternalAudit_auditee_representatives" ("InternalAudit_id");
CREATE INDEX "ix_InternalAudit_auditee_representatives_auditee_representatives" ON "InternalAudit_auditee_representatives" (auditee_representatives);

CREATE TABLE "InternalAudit_positive_observations" (
	"InternalAudit_id" TEXT,
	positive_observations TEXT,
	PRIMARY KEY ("InternalAudit_id", positive_observations),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_positive_observations_positive_observations" ON "InternalAudit_positive_observations" (positive_observations);
CREATE INDEX "ix_InternalAudit_positive_observations_InternalAudit_id" ON "InternalAudit_positive_observations" ("InternalAudit_id");

CREATE TABLE "InternalAudit_report_distribution" (
	"InternalAudit_id" TEXT,
	report_distribution TEXT,
	PRIMARY KEY ("InternalAudit_id", report_distribution),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_report_distribution_report_distribution" ON "InternalAudit_report_distribution" (report_distribution);
CREATE INDEX "ix_InternalAudit_report_distribution_InternalAudit_id" ON "InternalAudit_report_distribution" ("InternalAudit_id");

CREATE TABLE "AuditProgramme_planned_audits" (
	"AuditProgramme_id" TEXT,
	planned_audits_id TEXT,
	PRIMARY KEY ("AuditProgramme_id", planned_audits_id),
	FOREIGN KEY("AuditProgramme_id") REFERENCES "AuditProgramme" (id),
	FOREIGN KEY(planned_audits_id) REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_AuditProgramme_planned_audits_planned_audits_id" ON "AuditProgramme_planned_audits" (planned_audits_id);
CREATE INDEX "ix_AuditProgramme_planned_audits_AuditProgramme_id" ON "AuditProgramme_planned_audits" ("AuditProgramme_id");

CREATE TABLE "ManagementReview_attendees" (
	"ManagementReview_id" TEXT,
	attendees TEXT,
	PRIMARY KEY ("ManagementReview_id", attendees),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_attendees_ManagementReview_id" ON "ManagementReview_attendees" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_attendees_attendees" ON "ManagementReview_attendees" (attendees);

CREATE TABLE "ManagementReview_improvement_opportunities" (
	"ManagementReview_id" TEXT,
	improvement_opportunities TEXT,
	PRIMARY KEY ("ManagementReview_id", improvement_opportunities),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_improvement_opportunities_ManagementReview_id" ON "ManagementReview_improvement_opportunities" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_improvement_opportunities_improvement_opportunities" ON "ManagementReview_improvement_opportunities" (improvement_opportunities);

CREATE TABLE "ManagementReview_decisions" (
	"ManagementReview_id" TEXT,
	decisions TEXT,
	PRIMARY KEY ("ManagementReview_id", decisions),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_decisions_ManagementReview_id" ON "ManagementReview_decisions" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_decisions_decisions" ON "ManagementReview_decisions" (decisions);

CREATE TABLE "ManagementReview_action_items" (
	"ManagementReview_id" TEXT,
	action_items TEXT,
	PRIMARY KEY ("ManagementReview_id", action_items),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_action_items_ManagementReview_id" ON "ManagementReview_action_items" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_action_items_action_items" ON "ManagementReview_action_items" (action_items);

CREATE TABLE "Nonconformity_immediate_actions" (
	"Nonconformity_id" TEXT,
	immediate_actions TEXT,
	PRIMARY KEY ("Nonconformity_id", immediate_actions),
	FOREIGN KEY("Nonconformity_id") REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_Nonconformity_immediate_actions_Nonconformity_id" ON "Nonconformity_immediate_actions" ("Nonconformity_id");
CREATE INDEX "ix_Nonconformity_immediate_actions_immediate_actions" ON "Nonconformity_immediate_actions" (immediate_actions);

CREATE TABLE "Asset_applicable_controls" (
	"Asset_id" TEXT,
	applicable_controls_id TEXT,
	PRIMARY KEY ("Asset_id", applicable_controls_id),
	FOREIGN KEY("Asset_id") REFERENCES "Asset" (id),
	FOREIGN KEY(applicable_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_Asset_applicable_controls_Asset_id" ON "Asset_applicable_controls" ("Asset_id");
CREATE INDEX "ix_Asset_applicable_controls_applicable_controls_id" ON "Asset_applicable_controls" (applicable_controls_id);

CREATE TABLE "InformationSecurityIncident_affected_assets" (
	"InformationSecurityIncident_id" TEXT,
	affected_assets_id TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", affected_assets_id),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id),
	FOREIGN KEY(affected_assets_id) REFERENCES "Asset" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_affected_assets_affected_assets_id" ON "InformationSecurityIncident_affected_assets" (affected_assets_id);
CREATE INDEX "ix_InformationSecurityIncident_affected_assets_InformationSecurityIncident_id" ON "InformationSecurityIncident_affected_assets" ("InformationSecurityIncident_id");

CREATE TABLE "InformationSecurityIncident_affected_cia" (
	"InformationSecurityIncident_id" TEXT,
	affected_cia TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", affected_cia),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_affected_cia_affected_cia" ON "InformationSecurityIncident_affected_cia" (affected_cia);
CREATE INDEX "ix_InformationSecurityIncident_affected_cia_InformationSecurityIncident_id" ON "InformationSecurityIncident_affected_cia" ("InformationSecurityIncident_id");

CREATE TABLE "InformationSecurityIncident_response_actions" (
	"InformationSecurityIncident_id" TEXT,
	response_actions TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", response_actions),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_response_actions_InformationSecurityIncident_id" ON "InformationSecurityIncident_response_actions" ("InformationSecurityIncident_id");
CREATE INDEX "ix_InformationSecurityIncident_response_actions_response_actions" ON "InformationSecurityIncident_response_actions" (response_actions);

CREATE TABLE "InformationSecurityIncident_containment_actions" (
	"InformationSecurityIncident_id" TEXT,
	containment_actions TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", containment_actions),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_containment_actions_containment_actions" ON "InformationSecurityIncident_containment_actions" (containment_actions);
CREATE INDEX "ix_InformationSecurityIncident_containment_actions_InformationSecurityIncident_id" ON "InformationSecurityIncident_containment_actions" ("InformationSecurityIncident_id");

CREATE TABLE "InformationSecurityIncident_eradication_actions" (
	"InformationSecurityIncident_id" TEXT,
	eradication_actions TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", eradication_actions),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_eradication_actions_eradication_actions" ON "InformationSecurityIncident_eradication_actions" (eradication_actions);
CREATE INDEX "ix_InformationSecurityIncident_eradication_actions_InformationSecurityIncident_id" ON "InformationSecurityIncident_eradication_actions" ("InformationSecurityIncident_id");

CREATE TABLE "InformationSecurityIncident_recovery_actions" (
	"InformationSecurityIncident_id" TEXT,
	recovery_actions TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", recovery_actions),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_recovery_actions_recovery_actions" ON "InformationSecurityIncident_recovery_actions" (recovery_actions);
CREATE INDEX "ix_InformationSecurityIncident_recovery_actions_InformationSecurityIncident_id" ON "InformationSecurityIncident_recovery_actions" ("InformationSecurityIncident_id");

CREATE TABLE "InformationSecurityIncident_evidence_collected" (
	"InformationSecurityIncident_id" TEXT,
	evidence_collected TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", evidence_collected),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_evidence_collected_InformationSecurityIncident_id" ON "InformationSecurityIncident_evidence_collected" ("InformationSecurityIncident_id");
CREATE INDEX "ix_InformationSecurityIncident_evidence_collected_evidence_collected" ON "InformationSecurityIncident_evidence_collected" (evidence_collected);

CREATE TABLE "InformationSecurityIncident_notifications_made" (
	"InformationSecurityIncident_id" TEXT,
	notifications_made TEXT,
	PRIMARY KEY ("InformationSecurityIncident_id", notifications_made),
	FOREIGN KEY("InformationSecurityIncident_id") REFERENCES "InformationSecurityIncident" (id)
);
CREATE INDEX "ix_InformationSecurityIncident_notifications_made_notifications_made" ON "InformationSecurityIncident_notifications_made" (notifications_made);
CREATE INDEX "ix_InformationSecurityIncident_notifications_made_InformationSecurityIncident_id" ON "InformationSecurityIncident_notifications_made" ("InformationSecurityIncident_id");

CREATE TABLE "AuditFinding" (
	finding_type VARCHAR(19),
	clause_reference TEXT,
	control_reference TEXT,
	finding_description TEXT,
	objective_evidence TEXT,
	root_cause_analysis TEXT,
	risk_implication TEXT,
	recommended_action TEXT,
	auditee_response TEXT,
	linked_corrective_action TEXT,
	closure_status TEXT,
	closure_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(control_reference) REFERENCES "SecurityControl" (id),
	FOREIGN KEY(linked_corrective_action) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_AuditFinding_id" ON "AuditFinding" (id);

CREATE TABLE "InformationSecurityManagementSystem_scope_boundaries" (
	"InformationSecurityManagementSystem_id" TEXT,
	scope_boundaries TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", scope_boundaries),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_scope_boundaries_scope_boundaries" ON "InformationSecurityManagementSystem_scope_boundaries" (scope_boundaries);
CREATE INDEX "ix_InformationSecurityManagementSystem_scope_boundaries_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_scope_boundaries" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_scope_exclusions" (
	"InformationSecurityManagementSystem_id" TEXT,
	scope_exclusions TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", scope_exclusions),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_scope_exclusions_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_scope_exclusions" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_scope_exclusions_scope_exclusions" ON "InformationSecurityManagementSystem_scope_exclusions" (scope_exclusions);

CREATE TABLE "InformationSecurityManagementSystem_context_internal_issues" (
	"InformationSecurityManagementSystem_id" TEXT,
	context_internal_issues TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", context_internal_issues),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_context_internal_issues_context_internal_issues" ON "InformationSecurityManagementSystem_context_internal_issues" (context_internal_issues);
CREATE INDEX "ix_InformationSecurityManagementSystem_context_internal_issues_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_context_internal_issues" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_context_external_issues" (
	"InformationSecurityManagementSystem_id" TEXT,
	context_external_issues TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", context_external_issues),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_context_external_issues_context_external_issues" ON "InformationSecurityManagementSystem_context_external_issues" (context_external_issues);
CREATE INDEX "ix_InformationSecurityManagementSystem_context_external_issues_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_context_external_issues" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_interested_parties" (
	"InformationSecurityManagementSystem_id" TEXT,
	interested_parties_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", interested_parties_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(interested_parties_id) REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_interested_parties_interested_parties_id" ON "InformationSecurityManagementSystem_interested_parties" (interested_parties_id);
CREATE INDEX "ix_InformationSecurityManagementSystem_interested_parties_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_interested_parties" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_objectives" (
	"InformationSecurityManagementSystem_id" TEXT,
	objectives_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", objectives_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(objectives_id) REFERENCES "InformationSecurityObjective" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_objectives_objectives_id" ON "InformationSecurityManagementSystem_objectives" (objectives_id);
CREATE INDEX "ix_InformationSecurityManagementSystem_objectives_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_objectives" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_controls" (
	"InformationSecurityManagementSystem_id" TEXT,
	controls_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", controls_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_controls_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_controls" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_controls_controls_id" ON "InformationSecurityManagementSystem_controls" (controls_id);

CREATE TABLE "InformationSecurityManagementSystem_roles" (
	"InformationSecurityManagementSystem_id" TEXT,
	roles_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", roles_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(roles_id) REFERENCES "Role" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_roles_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_roles" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_roles_roles_id" ON "InformationSecurityManagementSystem_roles" (roles_id);

CREATE TABLE "InformationSecurityManagementSystem_resources" (
	"InformationSecurityManagementSystem_id" TEXT,
	resources_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", resources_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(resources_id) REFERENCES "Resource" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_resources_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_resources" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_resources_resources_id" ON "InformationSecurityManagementSystem_resources" (resources_id);

CREATE TABLE "InformationSecurityManagementSystem_competence_records" (
	"InformationSecurityManagementSystem_id" TEXT,
	competence_records_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", competence_records_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(competence_records_id) REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_competence_records_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_competence_records" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_competence_records_competence_records_id" ON "InformationSecurityManagementSystem_competence_records" (competence_records_id);

CREATE TABLE "InformationSecurityManagementSystem_documented_information_register" (
	"InformationSecurityManagementSystem_id" TEXT,
	documented_information_register_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", documented_information_register_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(documented_information_register_id) REFERENCES "DocumentedInformation" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_documented_information_register_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_documented_information_register" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_documented_information_register_documented_information_register_id" ON "InformationSecurityManagementSystem_documented_information_register" (documented_information_register_id);

CREATE TABLE "InformationSecurityManagementSystem_operational_procedures" (
	"InformationSecurityManagementSystem_id" TEXT,
	operational_procedures_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", operational_procedures_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(operational_procedures_id) REFERENCES "OperationalProcedure" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_operational_procedures_operational_procedures_id" ON "InformationSecurityManagementSystem_operational_procedures" (operational_procedures_id);
CREATE INDEX "ix_InformationSecurityManagementSystem_operational_procedures_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_operational_procedures" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_risk_assessments" (
	"InformationSecurityManagementSystem_id" TEXT,
	risk_assessments_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", risk_assessments_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(risk_assessments_id) REFERENCES "RiskAssessment" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_risk_assessments_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_risk_assessments" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_risk_assessments_risk_assessments_id" ON "InformationSecurityManagementSystem_risk_assessments" (risk_assessments_id);

CREATE TABLE "InformationSecurityManagementSystem_risk_treatment_plans" (
	"InformationSecurityManagementSystem_id" TEXT,
	risk_treatment_plans_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", risk_treatment_plans_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(risk_treatment_plans_id) REFERENCES "RiskTreatmentPlan" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_risk_treatment_plans_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_risk_treatment_plans" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_risk_treatment_plans_risk_treatment_plans_id" ON "InformationSecurityManagementSystem_risk_treatment_plans" (risk_treatment_plans_id);

CREATE TABLE "InformationSecurityManagementSystem_internal_audits" (
	"InformationSecurityManagementSystem_id" TEXT,
	internal_audits_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", internal_audits_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(internal_audits_id) REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_internal_audits_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_internal_audits" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_internal_audits_internal_audits_id" ON "InformationSecurityManagementSystem_internal_audits" (internal_audits_id);

CREATE TABLE "InformationSecurityManagementSystem_management_reviews" (
	"InformationSecurityManagementSystem_id" TEXT,
	management_reviews_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", management_reviews_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(management_reviews_id) REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_management_reviews_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_management_reviews" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_management_reviews_management_reviews_id" ON "InformationSecurityManagementSystem_management_reviews" (management_reviews_id);

CREATE TABLE "InformationSecurityManagementSystem_nonconformities" (
	"InformationSecurityManagementSystem_id" TEXT,
	nonconformities_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", nonconformities_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(nonconformities_id) REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_nonconformities_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_nonconformities" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_nonconformities_nonconformities_id" ON "InformationSecurityManagementSystem_nonconformities" (nonconformities_id);

CREATE TABLE "InformationSecurityManagementSystem_corrective_actions" (
	"InformationSecurityManagementSystem_id" TEXT,
	corrective_actions_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", corrective_actions_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(corrective_actions_id) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_corrective_actions_corrective_actions_id" ON "InformationSecurityManagementSystem_corrective_actions" (corrective_actions_id);
CREATE INDEX "ix_InformationSecurityManagementSystem_corrective_actions_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_corrective_actions" ("InformationSecurityManagementSystem_id");

CREATE TABLE "InformationSecurityManagementSystem_improvements" (
	"InformationSecurityManagementSystem_id" TEXT,
	improvements_id TEXT,
	PRIMARY KEY ("InformationSecurityManagementSystem_id", improvements_id),
	FOREIGN KEY("InformationSecurityManagementSystem_id") REFERENCES "InformationSecurityManagementSystem" (id),
	FOREIGN KEY(improvements_id) REFERENCES "ImprovementOpportunity" (id)
);
CREATE INDEX "ix_InformationSecurityManagementSystem_improvements_InformationSecurityManagementSystem_id" ON "InformationSecurityManagementSystem_improvements" ("InformationSecurityManagementSystem_id");
CREATE INDEX "ix_InformationSecurityManagementSystem_improvements_improvements_id" ON "InformationSecurityManagementSystem_improvements" (improvements_id);

CREATE TABLE "InformationSecurityPolicy_related_topic_policies" (
	"InformationSecurityPolicy_id" TEXT,
	related_topic_policies_id TEXT,
	PRIMARY KEY ("InformationSecurityPolicy_id", related_topic_policies_id),
	FOREIGN KEY("InformationSecurityPolicy_id") REFERENCES "InformationSecurityPolicy" (id),
	FOREIGN KEY(related_topic_policies_id) REFERENCES "TopicSpecificPolicy" (id)
);
CREATE INDEX "ix_InformationSecurityPolicy_related_topic_policies_InformationSecurityPolicy_id" ON "InformationSecurityPolicy_related_topic_policies" ("InformationSecurityPolicy_id");
CREATE INDEX "ix_InformationSecurityPolicy_related_topic_policies_related_topic_policies_id" ON "InformationSecurityPolicy_related_topic_policies" (related_topic_policies_id);

CREATE TABLE "TopicSpecificPolicy_applicable_controls" (
	"TopicSpecificPolicy_id" TEXT,
	applicable_controls_id TEXT,
	PRIMARY KEY ("TopicSpecificPolicy_id", applicable_controls_id),
	FOREIGN KEY("TopicSpecificPolicy_id") REFERENCES "TopicSpecificPolicy" (id),
	FOREIGN KEY(applicable_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_TopicSpecificPolicy_applicable_controls_applicable_controls_id" ON "TopicSpecificPolicy_applicable_controls" (applicable_controls_id);
CREATE INDEX "ix_TopicSpecificPolicy_applicable_controls_TopicSpecificPolicy_id" ON "TopicSpecificPolicy_applicable_controls" ("TopicSpecificPolicy_id");

CREATE TABLE "InformationSecurityObjective_related_risks" (
	"InformationSecurityObjective_id" TEXT,
	related_risks_id TEXT,
	PRIMARY KEY ("InformationSecurityObjective_id", related_risks_id),
	FOREIGN KEY("InformationSecurityObjective_id") REFERENCES "InformationSecurityObjective" (id),
	FOREIGN KEY(related_risks_id) REFERENCES "Risk" (id)
);
CREATE INDEX "ix_InformationSecurityObjective_related_risks_related_risks_id" ON "InformationSecurityObjective_related_risks" (related_risks_id);
CREATE INDEX "ix_InformationSecurityObjective_related_risks_InformationSecurityObjective_id" ON "InformationSecurityObjective_related_risks" ("InformationSecurityObjective_id");

CREATE TABLE "InformationSecurityObjective_related_controls" (
	"InformationSecurityObjective_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("InformationSecurityObjective_id", related_controls_id),
	FOREIGN KEY("InformationSecurityObjective_id") REFERENCES "InformationSecurityObjective" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_InformationSecurityObjective_related_controls_InformationSecurityObjective_id" ON "InformationSecurityObjective_related_controls" ("InformationSecurityObjective_id");
CREATE INDEX "ix_InformationSecurityObjective_related_controls_related_controls_id" ON "InformationSecurityObjective_related_controls" (related_controls_id);

CREATE TABLE "RiskAssessment_risks_identified" (
	"RiskAssessment_id" TEXT,
	risks_identified_id TEXT,
	PRIMARY KEY ("RiskAssessment_id", risks_identified_id),
	FOREIGN KEY("RiskAssessment_id") REFERENCES "RiskAssessment" (id),
	FOREIGN KEY(risks_identified_id) REFERENCES "Risk" (id)
);
CREATE INDEX "ix_RiskAssessment_risks_identified_risks_identified_id" ON "RiskAssessment_risks_identified" (risks_identified_id);
CREATE INDEX "ix_RiskAssessment_risks_identified_RiskAssessment_id" ON "RiskAssessment_risks_identified" ("RiskAssessment_id");

CREATE TABLE "Risk_affected_assets" (
	"Risk_id" TEXT,
	affected_assets_id TEXT,
	PRIMARY KEY ("Risk_id", affected_assets_id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY(affected_assets_id) REFERENCES "Asset" (id)
);
CREATE INDEX "ix_Risk_affected_assets_affected_assets_id" ON "Risk_affected_assets" (affected_assets_id);
CREATE INDEX "ix_Risk_affected_assets_Risk_id" ON "Risk_affected_assets" ("Risk_id");

CREATE TABLE "Risk_affected_cia_properties" (
	"Risk_id" TEXT,
	affected_cia_properties TEXT,
	PRIMARY KEY ("Risk_id", affected_cia_properties),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Risk_affected_cia_properties_affected_cia_properties" ON "Risk_affected_cia_properties" (affected_cia_properties);
CREATE INDEX "ix_Risk_affected_cia_properties_Risk_id" ON "Risk_affected_cia_properties" ("Risk_id");

CREATE TABLE "Risk_existing_controls" (
	"Risk_id" TEXT,
	existing_controls_id TEXT,
	PRIMARY KEY ("Risk_id", existing_controls_id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY(existing_controls_id) REFERENCES "SecurityControl" (id)
);
CREATE INDEX "ix_Risk_existing_controls_existing_controls_id" ON "Risk_existing_controls" (existing_controls_id);
CREATE INDEX "ix_Risk_existing_controls_Risk_id" ON "Risk_existing_controls" ("Risk_id");

CREATE TABLE "RiskTreatmentPlan_risks_addressed" (
	"RiskTreatmentPlan_id" TEXT,
	risks_addressed_id TEXT,
	PRIMARY KEY ("RiskTreatmentPlan_id", risks_addressed_id),
	FOREIGN KEY("RiskTreatmentPlan_id") REFERENCES "RiskTreatmentPlan" (id),
	FOREIGN KEY(risks_addressed_id) REFERENCES "Risk" (id)
);
CREATE INDEX "ix_RiskTreatmentPlan_risks_addressed_RiskTreatmentPlan_id" ON "RiskTreatmentPlan_risks_addressed" ("RiskTreatmentPlan_id");
CREATE INDEX "ix_RiskTreatmentPlan_risks_addressed_risks_addressed_id" ON "RiskTreatmentPlan_risks_addressed" (risks_addressed_id);

CREATE TABLE "StatementOfApplicability_soa_entries" (
	"StatementOfApplicability_id" TEXT,
	soa_entries_id INTEGER,
	PRIMARY KEY ("StatementOfApplicability_id", soa_entries_id),
	FOREIGN KEY("StatementOfApplicability_id") REFERENCES "StatementOfApplicability" (id),
	FOREIGN KEY(soa_entries_id) REFERENCES "SoAEntry" (id)
);
CREATE INDEX "ix_StatementOfApplicability_soa_entries_StatementOfApplicability_id" ON "StatementOfApplicability_soa_entries" ("StatementOfApplicability_id");
CREATE INDEX "ix_StatementOfApplicability_soa_entries_soa_entries_id" ON "StatementOfApplicability_soa_entries" (soa_entries_id);

CREATE TABLE "Nonconformity_linked_corrective_actions" (
	"Nonconformity_id" TEXT,
	linked_corrective_actions_id TEXT,
	PRIMARY KEY ("Nonconformity_id", linked_corrective_actions_id),
	FOREIGN KEY("Nonconformity_id") REFERENCES "Nonconformity" (id),
	FOREIGN KEY(linked_corrective_actions_id) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_Nonconformity_linked_corrective_actions_linked_corrective_actions_id" ON "Nonconformity_linked_corrective_actions" (linked_corrective_actions_id);
CREATE INDEX "ix_Nonconformity_linked_corrective_actions_Nonconformity_id" ON "Nonconformity_linked_corrective_actions" ("Nonconformity_id");

CREATE TABLE "Asset_related_risks" (
	"Asset_id" TEXT,
	related_risks_id TEXT,
	PRIMARY KEY ("Asset_id", related_risks_id),
	FOREIGN KEY("Asset_id") REFERENCES "Asset" (id),
	FOREIGN KEY(related_risks_id) REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Asset_related_risks_Asset_id" ON "Asset_related_risks" ("Asset_id");
CREATE INDEX "ix_Asset_related_risks_related_risks_id" ON "Asset_related_risks" (related_risks_id);

CREATE TABLE "InformationSecurityEvent_affected_assets" (
	"InformationSecurityEvent_id" TEXT,
	affected_assets_id TEXT,
	PRIMARY KEY ("InformationSecurityEvent_id", affected_assets_id),
	FOREIGN KEY("InformationSecurityEvent_id") REFERENCES "InformationSecurityEvent" (id),
	FOREIGN KEY(affected_assets_id) REFERENCES "Asset" (id)
);
CREATE INDEX "ix_InformationSecurityEvent_affected_assets_affected_assets_id" ON "InformationSecurityEvent_affected_assets" (affected_assets_id);
CREATE INDEX "ix_InformationSecurityEvent_affected_assets_InformationSecurityEvent_id" ON "InformationSecurityEvent_affected_assets" ("InformationSecurityEvent_id");

CREATE TABLE "InternalAudit_findings" (
	"InternalAudit_id" TEXT,
	findings_id TEXT,
	PRIMARY KEY ("InternalAudit_id", findings_id),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id),
	FOREIGN KEY(findings_id) REFERENCES "AuditFinding" (id)
);
CREATE INDEX "ix_InternalAudit_findings_findings_id" ON "InternalAudit_findings" (findings_id);
CREATE INDEX "ix_InternalAudit_findings_InternalAudit_id" ON "InternalAudit_findings" ("InternalAudit_id");
