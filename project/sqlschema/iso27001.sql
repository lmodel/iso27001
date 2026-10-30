-- # Abstract Class: IsmsRecord Description: Anything the ISMS keeps a record of that other records can refer to: it has an identifier, a title and a description.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsDocumentControlMixin Description: The control that documented information is kept under: who wrote, owns and approved it, when it takes effect and is reviewed, how it is classified, distributed, stored and changed, how long it is retained, and whether it came from outside the organization.
--     * Slot: id
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: IsmsManagementSystem Description: One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
--     * Slot: isms_top_management Description: The person or group that directs and controls the organization at the highest level.
--     * Slot: isms_governing_body Description: The body top management answers to, such as a board, where there is one.
--     * Slot: isms_scope Description: The scope of the ISMS, as the organization states it.
--     * Slot: isms_processes Description: The processes the ISMS needs and how they interact.
--     * Slot: isms_certification_status Description: Where the ISMS stands with certification, in the organization's own terms.
--     * Slot: isms_certification_body Description: The body that certifies the ISMS.
--     * Slot: isms_certification_date Description: When the ISMS was certified.
--     * Slot: isms_recertification_date Description: When the ISMS is next due for recertification.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: isms_organization_isms_id Description: The organization that runs the ISMS.
--     * Slot: isms_policy_isms_id Description: The information security policy.
--     * Slot: isms_risk_assessment_process_isms_id Description: The information security risk assessment process.
--     * Slot: isms_risk_treatment_process_isms_id Description: The information security risk treatment process.
--     * Slot: isms_statement_of_applicability_isms_id Description: The Statement of Applicability.
--     * Slot: isms_awareness_programme_isms_id Description: The awareness programme.
--     * Slot: isms_communication_plan_isms_id Description: The plan for communication about the ISMS.
--     * Slot: isms_monitoring_programme_isms_id Description: The programme of monitoring and measurement.
-- # Class: IsmsOrganization Description: The organization that runs the ISMS, with what it needs to know about itself to understand its context.
--     * Slot: organization_legal_name Description: The organization's registered legal name.
--     * Slot: organization_kind Description: What kind of organization it is, such as a company, an agency or a charity.
--     * Slot: organization_sector Description: The organization's main industry sector.
--     * Slot: organization_size Description: How the organization classes its own size.
--     * Slot: organization_employee_count Description: About how many people the organization employs.
--     * Slot: organization_parent Description: The organization's parent, if it has one.
--     * Slot: organization_climate_change_relevant Description: Whether the organization has determined that climate change is a relevant issue for its ISMS.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsInterestedParty Description: A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
--     * Slot: party_category Description: What kind of interested party it is, in the organization's own terms.
--     * Slot: party_relationship Description: How the party relates to the organization.
--     * Slot: party_communication_needs Description: What the party needs to be told, and how.
--     * Slot: party_contact Description: How to reach the party.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsPolicy Description: The information security policy that top management sets: the organization's commitment and the frame for its information security objectives.
--     * Slot: policy_statement Description: The policy's own statement, in the organization's words.
--     * Slot: policy_objectives_framework Description: How the policy frames the setting of information security objectives.
--     * Slot: policy_applicability Description: To whom and to what the policy applies.
--     * Slot: policy_communication_date Description: When the policy was communicated within the organization.
--     * Slot: policy_acknowledgement_required Description: Whether staff must acknowledge the policy.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsTopicSpecificPolicy Description: A policy on one topic of information security, such as access control or backup, that supports the information security policy.
--     * Slot: topic_policy_topic Description: The topic the policy covers.
--     * Slot: topic_policy_parent Description: The information security policy this policy supports.
--     * Slot: topic_policy_audience Description: Whom the policy is written for.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsRole Description: A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
--     * Slot: role_category Description: What kind of role it is, in the organization's own terms.
--     * Slot: role_accountability Description: What the role is accountable for.
--     * Slot: role_delegation Description: How the role may delegate its responsibilities.
--     * Slot: role_reports_to Description: The role this role reports to.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsObjective Description: An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: objective_statement Description: The objective, as the organization states it.
--     * Slot: objective_target Description: The value the objective aims for.
--     * Slot: objective_current_value Description: The value last measured.
--     * Slot: objective_metric Description: How the objective's value is defined.
--     * Slot: objective_measurement_method Description: How the value is measured.
--     * Slot: objective_measurement_frequency Description: How often the value is measured.
--     * Slot: objective_target_date Description: When the objective is to be reached.
--     * Slot: objective_achievement Description: How far the objective has been reached, in the organization's own terms.
--     * Slot: objective_action_plan Description: What will be done to reach the objective.
--     * Slot: objective_resources Description: The resources needed to reach the objective.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsRiskAssessmentProcess Description: The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
--     * Slot: risk_acceptance_criteria Description: The criteria for accepting a risk.
--     * Slot: risk_assessment_criteria Description: The criteria for carrying out a risk assessment.
--     * Slot: risk_assessment_method Description: The method used to identify, analyse and evaluate risks.
--     * Slot: risk_likelihood_scale Description: The scale for rating likelihood.
--     * Slot: risk_impact_scale Description: The scale for rating consequences.
--     * Slot: risk_matrix Description: How likelihood and consequence combine into a risk level.
--     * Slot: risk_assessment_frequency Description: How often risks are assessed.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsRiskAssessment Description: One risk assessment carried out under the risk assessment process, and what it found.
--     * Slot: assessment_scope Description: What the assessment covered.
--     * Slot: assessment_date Description: When the assessment was carried out.
--     * Slot: assessment_assessor Description: Who carried out the assessment.
--     * Slot: assessment_method_used Description: The method this assessment applied.
--     * Slot: assessment_summary Description: A summary of what the assessment found.
--     * Slot: assessment_next_date Description: When the next assessment is planned.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsRisk Description: An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
--     * Slot: risk_source Description: Where the risk comes from.
--     * Slot: risk_threat Description: The threat that could cause harm.
--     * Slot: risk_vulnerability Description: The weakness the threat could exploit.
--     * Slot: risk_owner Description: The person who is accountable for the risk and has the authority to manage it.
--     * Slot: risk_likelihood Description: How likely the risk is.
--     * Slot: risk_impact Description: How severe the consequences would be.
--     * Slot: risk_inherent_level Description: The risk's level before controls.
--     * Slot: risk_residual_level Description: The risk's level after controls.
--     * Slot: risk_treatment_option Description: The treatment chosen for the risk.
--     * Slot: risk_treatment_priority Description: How soon the risk is to be treated, in the organization's own terms.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsRiskTreatmentProcess Description: The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
--     * Slot: treatment_options_guidance Description: How a treatment option is chosen for a risk.
--     * Slot: treatment_control_selection Description: How the controls a treatment needs are chosen.
--     * Slot: treatment_annex_a_comparison Description: How the chosen controls are compared with Annex A, so that no necessary control is left out.
--     * Slot: treatment_soa_template Description: The template the Statement of Applicability follows.
--     * Slot: treatment_approval_workflow Description: How a treatment plan and its residual risks are approved.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsRiskTreatmentPlan Description: A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
--     * Slot: implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: plan_scope Description: What the plan covers.
--     * Slot: plan_resources Description: The resources the plan needs.
--     * Slot: plan_timeline Description: When the plan's actions are to happen.
--     * Slot: plan_risk_owner_approval Description: The risk owner who approved the plan.
--     * Slot: plan_residual_risk_acceptance Description: How the risk owners accepted the risk that remains.
--     * Slot: plan_completion_date Description: When the plan was completed.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsStatementOfApplicability Description: The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Abstract Class: IsmsApplicabilityEntry Description: One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
--     * Slot: id
--     * Slot: entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: entry_type Description: The kind of entry: IsmsIncludedControl or IsmsExcludedControl.
--     * Slot: entry_justification Description: Why the control is included or excluded.
--     * Slot: IsmsStatementOfApplicability_isms_id Description: Autocreated FK slot
-- # Class: IsmsIncludedControl Description: An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
--     * Slot: id
--     * Slot: implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: included_control Description: The organization's control the entry includes.
--     * Slot: included_evidence Description: What shows that the control is in place.
--     * Slot: included_target_date Description: When the control is to be in place, if it is not yet.
--     * Slot: entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: entry_type Description: The kind of entry: IsmsIncludedControl or IsmsExcludedControl.
--     * Slot: entry_justification Description: Why the control is included or excluded.
-- # Class: IsmsExcludedControl Description: An entry that leaves out an Annex A control the organization does not need, and says why.
--     * Slot: id
--     * Slot: entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: entry_type Description: The kind of entry: IsmsIncludedControl or IsmsExcludedControl.
--     * Slot: entry_justification Description: Why the control is included or excluded.
-- # Class: IsmsControl Description: A control the organization has determined it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
--     * Slot: implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: control_theme Description: Which of Annex A's four themes the control belongs to.
--     * Slot: control_text Description: What the control does, in the organization's own words.
--     * Slot: control_guidance Description: The organization's notes on putting the control in place.
--     * Slot: control_owner Description: The person who owns the control.
--     * Slot: control_implementation_date Description: When the control was put in place.
--     * Slot: control_effectiveness Description: How well the control works, in the organization's own terms.
--     * Slot: control_last_tested Description: When the control was last tested.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsAsset Description: An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
--     * Slot: asset_category Description: What kind of asset it is, such as information, software, hardware or a service.
--     * Slot: asset_owner Description: Who owns the asset.
--     * Slot: asset_custodian Description: Who looks after the asset from day to day.
--     * Slot: asset_classification Description: The information classification the asset carries.
--     * Slot: asset_location Description: Where the asset is, physically or logically.
--     * Slot: asset_criticality Description: How much the asset matters, in the organization's own terms.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsResource Description: A resource provided for the ISMS, such as people, time, tools or budget.
--     * Slot: resource_category Description: What kind of resource it is.
--     * Slot: resource_quantity Description: How much of the resource is provided.
--     * Slot: resource_allocation_date Description: When the resource was allocated.
--     * Slot: resource_allocated_to Description: What the resource is allocated to.
--     * Slot: resource_cost Description: What the resource costs.
--     * Slot: resource_availability Description: Whether the resource is available now, in the organization's own terms.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsCompetenceRecord Description: The evidence of one person's competence for work that affects information security, and what is done to close any gap.
--     * Slot: competence_person Description: The person the record is about.
--     * Slot: competence_role Description: The role the person holds.
--     * Slot: competence_assessment_date Description: When the person's competence was last assessed.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsAwarenessProgramme Description: The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
--     * Slot: awareness_audience Description: Whom the programme is for.
--     * Slot: awareness_frequency Description: How often the programme runs.
--     * Slot: awareness_completion_tracking Description: How completion is tracked.
--     * Slot: awareness_effectiveness Description: How the programme's effect is measured.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsCommunicationPlan Description: The plan for communication about the ISMS, inside the organization and outside it.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsCommunication Description: One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
--     * Slot: id
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: communication_subject Description: What the communication is about.
--     * Slot: communication_purpose Description: Why it is communicated.
--     * Slot: communication_audience Description: To whom it is communicated.
--     * Slot: communication_frequency Description: How often it is communicated.
--     * Slot: communication_method Description: How it is communicated.
--     * Slot: communication_records_required Description: Whether a record of the communication is kept.
--     * Slot: IsmsCommunicationPlan_isms_id Description: Autocreated FK slot
-- # Class: IsmsDocumentedInformation Description: A piece of documented information the ISMS keeps under control that no more specific record describes, such as a procedure, a standard, a plan or a report.
--     * Slot: document_kind Description: What kind of documented information it is.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsOperationalProcedure Description: A procedure by which the organization plans and controls the processes that meet its information security requirements.
--     * Slot: procedure_scope Description: What the procedure covers.
--     * Slot: procedure_criteria Description: The criteria the processes are run to.
--     * Slot: procedure_change_control Description: How changes to the processes are controlled.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsMonitoringProgramme Description: The programme of monitoring, measurement, analysis and evaluation of information security performance and of the ISMS's effectiveness.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsMonitoringItem Description: One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
--     * Slot: id
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: monitoring_metric Description: The name of what is measured.
--     * Slot: monitoring_description Description: What the measurement shows.
--     * Slot: monitoring_method Description: How it is measured.
--     * Slot: monitoring_frequency Description: How often it is measured.
--     * Slot: monitoring_analysis_frequency Description: How often the results are analysed and evaluated.
--     * Slot: monitoring_analyst Description: Who analyses and evaluates the results.
--     * Slot: monitoring_target Description: The value aimed for.
--     * Slot: monitoring_alert_threshold Description: The value that calls for action.
--     * Slot: monitoring_current_value Description: The value last measured.
--     * Slot: monitoring_trend Description: Which way the value is moving.
--     * Slot: IsmsMonitoringProgramme_isms_id Description: Autocreated FK slot
-- # Class: IsmsAuditProgramme Description: An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
--     * Slot: programme_period Description: The period the programme covers.
--     * Slot: programme_frequency_rationale Description: Why the audits happen as often as they do.
--     * Slot: programme_resources Description: The resources the programme needs.
--     * Slot: programme_auditor_qualifications Description: The qualifications the auditors need.
--     * Slot: programme_status Description: Where the programme stands, in the organization's own terms.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsAudit Description: An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
--     * Slot: audit_type Description: Who carries out the audit, relative to the organization.
--     * Slot: audit_scope Description: What the audit covers.
--     * Slot: audit_period_start Description: When the audit began.
--     * Slot: audit_period_end Description: When the audit ended.
--     * Slot: audit_lead Description: Who led the audit.
--     * Slot: audit_plan Description: The documented information that holds the audit plan.
--     * Slot: audit_conclusion Description: The audit's overall conclusion.
--     * Slot: audit_report_date Description: When the audit report was issued.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsAuditFinding Description: One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
--     * Slot: finding_type Description: What kind of finding it is.
--     * Slot: finding_requirement Description: The clause or Annex A control of ISO/IEC 27001:2022 the finding concerns, by number.
--     * Slot: finding_control Description: The organization's control the finding concerns.
--     * Slot: finding_evidence Description: The objective evidence for the finding.
--     * Slot: finding_root_cause Description: What the analysis of the finding's cause found.
--     * Slot: finding_risk Description: What the finding means for risk.
--     * Slot: finding_recommendation Description: What the auditor recommends.
--     * Slot: finding_auditee_response Description: How the auditee responded.
--     * Slot: finding_corrective_action Description: The corrective action the finding led to.
--     * Slot: finding_closure_status Description: Whether the finding is closed, in the organization's own terms.
--     * Slot: finding_closure_date Description: When the finding was closed.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
-- # Class: IsmsManagementReview Description: A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
--     * Slot: review_held_on Description: When the review was held.
--     * Slot: review_previous_actions Description: Where the actions from earlier reviews stand.
--     * Slot: review_context_changes Description: How the issues that bear on the ISMS have changed.
--     * Slot: review_interested_party_changes Description: How interested parties' needs and expectations have changed.
--     * Slot: review_interested_party_feedback Description: What interested parties said.
--     * Slot: review_performance_trends Description: The trends in information security performance.
--     * Slot: review_audit_results Description: What the audits found.
--     * Slot: review_risk_assessment_results Description: What the risk assessments found.
--     * Slot: review_risk_treatment_status Description: Where risk treatment stands.
--     * Slot: review_risks_and_opportunities Description: How risks and opportunities have changed.
--     * Slot: review_next_date Description: When the next review is planned.
--     * Slot: document_reference Description: The reference the organization's document control gives it.
--     * Slot: document_version Description: The version of the document.
--     * Slot: document_author Description: Who wrote the document.
--     * Slot: document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: document_approver Description: Who approved the document.
--     * Slot: document_approval_date Description: When the document was approved.
--     * Slot: document_effective_date Description: When the document takes effect.
--     * Slot: document_last_review_date Description: When the document was last reviewed.
--     * Slot: document_next_review_date Description: When the document is next due for review.
--     * Slot: document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: document_classification Description: The information classification the document carries.
--     * Slot: document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: document_storage Description: How the document is stored and preserved, so that it stays legible.
--     * Slot: document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: document_external_origin Description: Whether the document comes from outside the organization and is kept because the ISMS needs it.
--     * Slot: document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsNonconformity Description: A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
--     * Slot: nonconformity_source Description: How the nonconformity came to light, such as an audit, a review or an incident.
--     * Slot: nonconformity_detected_on Description: When the nonconformity was found.
--     * Slot: nonconformity_detected_by Description: Who or what found it.
--     * Slot: nonconformity_requirement Description: The requirement that was not met, of ISO/IEC 27001, of the organization or of an interested party.
--     * Slot: nonconformity_consequences Description: How its consequences were dealt with.
--     * Slot: nonconformity_root_cause Description: What caused it.
--     * Slot: nonconformity_similar_check Description: Whether similar nonconformities exist or could occur, and where.
--     * Slot: nonconformity_status Description: Where the nonconformity stands, in the organization's own terms.
--     * Slot: nonconformity_closure_date Description: When it was closed.
--     * Slot: nonconformity_closure_evidence Description: What shows that it is closed.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsCorrectiveAction Description: An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: action_root_cause Description: The cause the action removes.
--     * Slot: action_target_date Description: When the action is to be complete.
--     * Slot: action_completion_date Description: When the action was complete.
--     * Slot: action_resources Description: The resources the action needs.
--     * Slot: action_effectiveness_criteria Description: How the action's effect will be judged.
--     * Slot: action_effectiveness_review_date Description: When the action's effect was reviewed.
--     * Slot: action_effective Description: Whether the review found the action effective.
--     * Slot: action_isms_changes Description: The changes to the ISMS the action needs.
--     * Slot: action_status Description: Where the action stands, in the organization's own terms.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsImprovementOpportunity Description: An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
--     * Slot: responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: improvement_source Description: Where the opportunity came from, such as a review, an audit or daily work.
--     * Slot: improvement_identified_on Description: When the opportunity was identified.
--     * Slot: improvement_identified_by Description: Who identified it.
--     * Slot: improvement_benefit Description: What the improvement is expected to bring.
--     * Slot: improvement_priority Description: How soon it is to be acted on, in the organization's own terms.
--     * Slot: improvement_plan Description: How the improvement is to be made.
--     * Slot: improvement_target_date Description: When the improvement is to be made.
--     * Slot: improvement_completion_date Description: When it was made.
--     * Slot: improvement_outcome Description: What the improvement brought.
--     * Slot: improvement_status Description: Where it stands, in the organization's own terms.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsSecurityEvent Description: An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
--     * Slot: event_type Description: The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident.
--     * Slot: event_occurred_at Description: When the event happened, or when it was first noticed.
--     * Slot: event_reporter Description: Who reported the event.
--     * Slot: event_assessment Description: What the assessment of the event found.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
-- # Class: IsmsSecurityIncident Description: An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
--     * Slot: incident_category Description: What kind of incident it is.
--     * Slot: incident_severity Description: How severe the incident is.
--     * Slot: incident_detection_method Description: How the incident was detected.
--     * Slot: incident_root_cause Description: What caused the incident.
--     * Slot: incident_notification_required Description: Whether authorities or other parties had to be told.
--     * Slot: incident_closed_at Description: When the incident was closed.
--     * Slot: incident_review Description: What the review after the incident found.
--     * Slot: event_type Description: The kind of record: IsmsSecurityEvent, or IsmsSecurityIncident for an event assessed as an incident.
--     * Slot: event_occurred_at Description: When the event happened, or when it was first noticed.
--     * Slot: event_reporter Description: Who reported the event.
--     * Slot: event_assessment Description: What the assessment of the event found.
--     * Slot: isms_id Description: The record's identifier, unique among the ISMS's records, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: IsmsDocumentControlMixin_document_distribution
--     * Slot: IsmsDocumentControlMixin_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsManagementSystem_isms_leadership_evidence
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_leadership_evidence Description: What shows that top management leads and commits to the ISMS.
-- # Class: IsmsManagementSystem_isms_scope_boundaries
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_scope_boundaries Description: Where the scope of the ISMS ends.
-- # Class: IsmsManagementSystem_isms_scope_exclusions
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_scope_exclusions Description: What the scope leaves out, each with the reason.
-- # Class: IsmsManagementSystem_isms_interfaces
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_interfaces Description: The interfaces and dependencies between what the organization does and what other organizations do, which the scope takes into account.
-- # Class: IsmsManagementSystem_isms_internal_issues
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_internal_issues Description: The internal issues that bear on the ISMS.
-- # Class: IsmsManagementSystem_isms_external_issues
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_external_issues Description: The external issues that bear on the ISMS.
-- # Class: IsmsManagementSystem_isms_risk_and_opportunity_actions
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_risk_and_opportunity_actions Description: The actions planned to address the ISMS's risks and opportunities, and how they fit into its processes.
-- # Class: IsmsManagementSystem_isms_planned_changes
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_planned_changes Description: The changes to the ISMS that are planned.
-- # Class: IsmsManagementSystem_isms_external_services
--     * Slot: IsmsManagementSystem_isms_id Description: Autocreated FK slot
--     * Slot: isms_external_services Description: The processes, products or services from outside the organization that the ISMS relies on and controls.
-- # Class: IsmsOrganization_organization_trading_names
--     * Slot: IsmsOrganization_isms_id Description: Autocreated FK slot
--     * Slot: organization_trading_names Description: Other names the organization trades under.
-- # Class: IsmsOrganization_organization_locations
--     * Slot: IsmsOrganization_isms_id Description: Autocreated FK slot
--     * Slot: organization_locations Description: The countries or regions the organization works in.
-- # Class: IsmsOrganization_organization_jurisdictions
--     * Slot: IsmsOrganization_isms_id Description: Autocreated FK slot
--     * Slot: organization_jurisdictions Description: The jurisdictions whose laws and regulations apply to the organization.
-- # Class: IsmsOrganization_organization_subsidiaries
--     * Slot: IsmsOrganization_isms_id Description: Autocreated FK slot
--     * Slot: organization_subsidiaries Description: The organization's subsidiaries, if it has any.
-- # Class: IsmsInterestedParty_party_requirements
--     * Slot: IsmsInterestedParty_isms_id Description: Autocreated FK slot
--     * Slot: party_requirements Description: The party's requirements that bear on information security.
-- # Class: IsmsInterestedParty_party_addressed_requirements
--     * Slot: IsmsInterestedParty_isms_id Description: Autocreated FK slot
--     * Slot: party_addressed_requirements Description: Which of those requirements the ISMS addresses.
-- # Class: IsmsInterestedParty_party_climate_change_requirements
--     * Slot: IsmsInterestedParty_isms_id Description: Autocreated FK slot
--     * Slot: party_climate_change_requirements Description: The party's requirements that concern climate change.
-- # Class: IsmsPolicy_policy_commitments
--     * Slot: IsmsPolicy_isms_id Description: Autocreated FK slot
--     * Slot: policy_commitments Description: The commitments the policy makes.
-- # Class: IsmsPolicy_policy_management_systems
--     * Slot: IsmsPolicy_isms_id Description: Autocreated FK slot
--     * Slot: policy_management_systems Description: The other management system standards the ISMS is integrated with under the same policy.
-- # Class: IsmsPolicy_document_distribution
--     * Slot: IsmsPolicy_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsTopicSpecificPolicy_relevant_controls
--     * Slot: IsmsTopicSpecificPolicy_isms_id Description: Autocreated FK slot
--     * Slot: relevant_controls_isms_id Description: The organization's controls that the record concerns.
-- # Class: IsmsTopicSpecificPolicy_document_distribution
--     * Slot: IsmsTopicSpecificPolicy_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsRole_role_responsibilities
--     * Slot: IsmsRole_isms_id Description: Autocreated FK slot
--     * Slot: role_responsibilities Description: The responsibilities assigned to the role.
-- # Class: IsmsRole_role_authorities
--     * Slot: IsmsRole_isms_id Description: Autocreated FK slot
--     * Slot: role_authorities Description: The authorities the role carries.
-- # Class: IsmsRole_role_holders
--     * Slot: IsmsRole_isms_id Description: Autocreated FK slot
--     * Slot: role_holders Description: The people who hold the role.
-- # Class: IsmsObjective_relevant_controls
--     * Slot: IsmsObjective_isms_id Description: Autocreated FK slot
--     * Slot: relevant_controls_isms_id Description: The organization's controls that the record concerns.
-- # Class: IsmsObjective_objective_risks
--     * Slot: IsmsObjective_isms_id Description: Autocreated FK slot
--     * Slot: objective_risks_isms_id Description: The risks the objective concerns.
-- # Class: IsmsRiskAssessmentProcess_risk_assessment_triggers
--     * Slot: IsmsRiskAssessmentProcess_isms_id Description: Autocreated FK slot
--     * Slot: risk_assessment_triggers Description: The events that start a risk assessment outside the planned ones.
-- # Class: IsmsRiskAssessmentProcess_document_distribution
--     * Slot: IsmsRiskAssessmentProcess_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsRiskAssessment_assessment_risks
--     * Slot: IsmsRiskAssessment_isms_id Description: Autocreated FK slot
--     * Slot: assessment_risks_isms_id Description: The risks the assessment identified.
-- # Class: IsmsRiskAssessment_assessment_recommendations
--     * Slot: IsmsRiskAssessment_isms_id Description: Autocreated FK slot
--     * Slot: assessment_recommendations Description: What the assessment recommends.
-- # Class: IsmsRiskAssessment_document_distribution
--     * Slot: IsmsRiskAssessment_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsRisk_affected_assets
--     * Slot: IsmsRisk_isms_id Description: Autocreated FK slot
--     * Slot: affected_assets_isms_id Description: The assets the risk, event or incident affects.
-- # Class: IsmsRisk_affected_security_properties
--     * Slot: IsmsRisk_isms_id Description: Autocreated FK slot
--     * Slot: affected_security_properties Description: Which of confidentiality, integrity and availability the risk or incident threatens.
-- # Class: IsmsRisk_risk_existing_controls
--     * Slot: IsmsRisk_isms_id Description: Autocreated FK slot
--     * Slot: risk_existing_controls_isms_id Description: The organization's controls already acting on the risk.
-- # Class: IsmsRiskTreatmentProcess_document_distribution
--     * Slot: IsmsRiskTreatmentProcess_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsRiskTreatmentPlan_plan_risks
--     * Slot: IsmsRiskTreatmentPlan_isms_id Description: Autocreated FK slot
--     * Slot: plan_risks_isms_id Description: The risks the plan treats.
-- # Class: IsmsRiskTreatmentPlan_plan_actions
--     * Slot: IsmsRiskTreatmentPlan_isms_id Description: Autocreated FK slot
--     * Slot: plan_actions Description: The actions the plan takes.
-- # Class: IsmsRiskTreatmentPlan_plan_controls
--     * Slot: IsmsRiskTreatmentPlan_isms_id Description: Autocreated FK slot
--     * Slot: plan_controls_isms_id Description: The controls the plan puts in place.
-- # Class: IsmsRiskTreatmentPlan_plan_responsible_parties
--     * Slot: IsmsRiskTreatmentPlan_isms_id Description: Autocreated FK slot
--     * Slot: plan_responsible_parties Description: Who carries out the plan.
-- # Class: IsmsRiskTreatmentPlan_document_distribution
--     * Slot: IsmsRiskTreatmentPlan_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsStatementOfApplicability_document_distribution
--     * Slot: IsmsStatementOfApplicability_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsControl_relevant_controls
--     * Slot: IsmsControl_isms_id Description: Autocreated FK slot
--     * Slot: relevant_controls_isms_id Description: The organization's controls that the record concerns.
-- # Class: IsmsControl_control_annex_a_controls
--     * Slot: IsmsControl_isms_id Description: Autocreated FK slot
--     * Slot: control_annex_a_controls Description: The Annex A controls the control answers to.
-- # Class: IsmsControl_control_threats
--     * Slot: IsmsControl_isms_id Description: Autocreated FK slot
--     * Slot: control_threats Description: The threats the control acts against.
-- # Class: IsmsControl_control_asset_types
--     * Slot: IsmsControl_isms_id Description: Autocreated FK slot
--     * Slot: control_asset_types Description: The kinds of asset the control applies to.
-- # Class: IsmsControl_control_evidence
--     * Slot: IsmsControl_isms_id Description: Autocreated FK slot
--     * Slot: control_evidence Description: Where the evidence that the control is in place is kept.
-- # Class: IsmsAsset_relevant_controls
--     * Slot: IsmsAsset_isms_id Description: Autocreated FK slot
--     * Slot: relevant_controls_isms_id Description: The organization's controls that the record concerns.
-- # Class: IsmsCompetenceRecord_competence_required
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_required Description: The competences the role needs.
-- # Class: IsmsCompetenceRecord_competence_education
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_education Description: The person's relevant education.
-- # Class: IsmsCompetenceRecord_competence_training
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_training Description: The training the person has completed.
-- # Class: IsmsCompetenceRecord_competence_experience
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_experience Description: The person's relevant experience.
-- # Class: IsmsCompetenceRecord_competence_gaps
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_gaps Description: The gaps the assessment found.
-- # Class: IsmsCompetenceRecord_competence_actions
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: competence_actions Description: What is done to close the gaps.
-- # Class: IsmsCompetenceRecord_document_distribution
--     * Slot: IsmsCompetenceRecord_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsAwarenessProgramme_awareness_topics
--     * Slot: IsmsAwarenessProgramme_isms_id Description: Autocreated FK slot
--     * Slot: awareness_topics Description: The topics the programme covers.
-- # Class: IsmsAwarenessProgramme_awareness_methods
--     * Slot: IsmsAwarenessProgramme_isms_id Description: Autocreated FK slot
--     * Slot: awareness_methods Description: How the programme is delivered.
-- # Class: IsmsAwarenessProgramme_document_distribution
--     * Slot: IsmsAwarenessProgramme_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsCommunicationPlan_document_distribution
--     * Slot: IsmsCommunicationPlan_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsDocumentedInformation_document_distribution
--     * Slot: IsmsDocumentedInformation_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsOperationalProcedure_relevant_controls
--     * Slot: IsmsOperationalProcedure_isms_id Description: Autocreated FK slot
--     * Slot: relevant_controls_isms_id Description: The organization's controls that the record concerns.
-- # Class: IsmsOperationalProcedure_procedure_control_measures
--     * Slot: IsmsOperationalProcedure_isms_id Description: Autocreated FK slot
--     * Slot: procedure_control_measures Description: The measures that control the processes.
-- # Class: IsmsOperationalProcedure_procedure_roles
--     * Slot: IsmsOperationalProcedure_isms_id Description: Autocreated FK slot
--     * Slot: procedure_roles_isms_id Description: The roles that carry out the procedure.
-- # Class: IsmsOperationalProcedure_document_distribution
--     * Slot: IsmsOperationalProcedure_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsMonitoringProgramme_document_distribution
--     * Slot: IsmsMonitoringProgramme_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsAuditProgramme_programme_audits
--     * Slot: IsmsAuditProgramme_isms_id Description: Autocreated FK slot
--     * Slot: programme_audits_isms_id Description: The audits the programme plans.
-- # Class: IsmsAuditProgramme_document_distribution
--     * Slot: IsmsAuditProgramme_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsAudit_audit_standards
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_standards Description: The management system standards the audit covers.
-- # Class: IsmsAudit_audit_criteria
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_criteria Description: What the audit compares the ISMS against.
-- # Class: IsmsAudit_audit_objectives
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_objectives Description: What the audit sets out to establish.
-- # Class: IsmsAudit_audit_team
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_team Description: Who else audited.
-- # Class: IsmsAudit_audit_auditees
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_auditees Description: Who represented the parts of the organization audited.
-- # Class: IsmsAudit_audit_report_distribution
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: audit_report_distribution Description: Who received the audit report.
-- # Class: IsmsAudit_document_distribution
--     * Slot: IsmsAudit_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsManagementReview_review_attendees
--     * Slot: IsmsManagementReview_isms_id Description: Autocreated FK slot
--     * Slot: review_attendees Description: Who attended the review.
-- # Class: IsmsManagementReview_review_improvement_opportunities
--     * Slot: IsmsManagementReview_isms_id Description: Autocreated FK slot
--     * Slot: review_improvement_opportunities Description: The opportunities for improvement raised.
-- # Class: IsmsManagementReview_review_decisions
--     * Slot: IsmsManagementReview_isms_id Description: Autocreated FK slot
--     * Slot: review_decisions Description: What the review decided.
-- # Class: IsmsManagementReview_review_actions
--     * Slot: IsmsManagementReview_isms_id Description: Autocreated FK slot
--     * Slot: review_actions Description: What the review asked to be done.
-- # Class: IsmsManagementReview_document_distribution
--     * Slot: IsmsManagementReview_isms_id Description: Autocreated FK slot
--     * Slot: document_distribution Description: How the document is distributed, accessed, retrieved and used.
-- # Class: IsmsNonconformity_nonconformity_immediate_actions
--     * Slot: IsmsNonconformity_isms_id Description: Autocreated FK slot
--     * Slot: nonconformity_immediate_actions Description: What was done at once to control and correct it.
-- # Class: IsmsCorrectiveAction_action_nonconformities
--     * Slot: IsmsCorrectiveAction_isms_id Description: Autocreated FK slot
--     * Slot: action_nonconformities_isms_id Description: The nonconformities the action addresses.
-- # Class: IsmsSecurityEvent_affected_assets
--     * Slot: IsmsSecurityEvent_isms_id Description: Autocreated FK slot
--     * Slot: affected_assets_isms_id Description: The assets the risk, event or incident affects.
-- # Class: IsmsSecurityIncident_affected_security_properties
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: affected_security_properties Description: Which of confidentiality, integrity and availability the risk or incident threatens.
-- # Class: IsmsSecurityIncident_incident_response_actions
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_response_actions Description: What was done in response.
-- # Class: IsmsSecurityIncident_incident_containment_actions
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_containment_actions Description: What was done to contain it.
-- # Class: IsmsSecurityIncident_incident_eradication_actions
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_eradication_actions Description: What was done to remove its cause.
-- # Class: IsmsSecurityIncident_incident_recovery_actions
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_recovery_actions Description: What was done to restore normal operation.
-- # Class: IsmsSecurityIncident_incident_lessons_learned
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_lessons_learned Description: What the organization learned from it.
-- # Class: IsmsSecurityIncident_incident_evidence
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_evidence Description: The evidence collected about it.
-- # Class: IsmsSecurityIncident_incident_notifications
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: incident_notifications Description: Whom the organization told, and when.
-- # Class: IsmsSecurityIncident_affected_assets
--     * Slot: IsmsSecurityIncident_isms_id Description: Autocreated FK slot
--     * Slot: affected_assets_isms_id Description: The assets the risk, event or incident affects.

CREATE TABLE "IsmsRecord" (
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsRecord_isms_id" ON "IsmsRecord" (isms_id);

CREATE TABLE "IsmsDocumentControlMixin" (
	id INTEGER NOT NULL,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IsmsDocumentControlMixin_id" ON "IsmsDocumentControlMixin" (id);

CREATE TABLE "IsmsOrganization" (
	organization_legal_name TEXT,
	organization_kind TEXT,
	organization_sector TEXT,
	organization_size TEXT,
	organization_employee_count INTEGER,
	organization_parent TEXT,
	organization_climate_change_relevant BOOLEAN,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsOrganization_isms_id" ON "IsmsOrganization" (isms_id);

CREATE TABLE "IsmsPolicy" (
	policy_statement TEXT,
	policy_objectives_framework TEXT,
	policy_applicability TEXT,
	policy_communication_date DATE,
	policy_acknowledgement_required BOOLEAN,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsPolicy_isms_id" ON "IsmsPolicy" (isms_id);

CREATE TABLE "IsmsRiskAssessmentProcess" (
	risk_acceptance_criteria TEXT,
	risk_assessment_criteria TEXT,
	risk_assessment_method TEXT,
	risk_likelihood_scale TEXT,
	risk_impact_scale TEXT,
	risk_matrix TEXT,
	risk_assessment_frequency TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessmentProcess_isms_id" ON "IsmsRiskAssessmentProcess" (isms_id);

CREATE TABLE "IsmsRiskTreatmentProcess" (
	treatment_options_guidance TEXT,
	treatment_control_selection TEXT,
	treatment_annex_a_comparison TEXT,
	treatment_soa_template TEXT,
	treatment_approval_workflow TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentProcess_isms_id" ON "IsmsRiskTreatmentProcess" (isms_id);

CREATE TABLE "IsmsStatementOfApplicability" (
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsStatementOfApplicability_isms_id" ON "IsmsStatementOfApplicability" (isms_id);

CREATE TABLE "IsmsExcludedControl" (
	id INTEGER NOT NULL,
	entry_annex_a_control VARCHAR(6) NOT NULL,
	entry_type TEXT,
	entry_justification TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IsmsExcludedControl_id" ON "IsmsExcludedControl" (id);

CREATE TABLE "IsmsAwarenessProgramme" (
	awareness_audience TEXT,
	awareness_frequency TEXT,
	awareness_completion_tracking TEXT,
	awareness_effectiveness TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsAwarenessProgramme_isms_id" ON "IsmsAwarenessProgramme" (isms_id);

CREATE TABLE "IsmsCommunicationPlan" (
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsCommunicationPlan_isms_id" ON "IsmsCommunicationPlan" (isms_id);

CREATE TABLE "IsmsMonitoringProgramme" (
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsMonitoringProgramme_isms_id" ON "IsmsMonitoringProgramme" (isms_id);

CREATE TABLE "IsmsSecurityIncident" (
	incident_category VARCHAR(22),
	incident_severity VARCHAR(8),
	incident_detection_method TEXT,
	incident_root_cause TEXT,
	incident_notification_required BOOLEAN,
	incident_closed_at DATETIME,
	incident_review TEXT,
	event_type TEXT,
	event_occurred_at DATETIME,
	event_reporter TEXT,
	event_assessment TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident" (isms_id);

CREATE TABLE "IsmsManagementSystem" (
	isms_top_management TEXT,
	isms_governing_body TEXT,
	isms_scope TEXT,
	isms_processes TEXT,
	isms_certification_status TEXT,
	isms_certification_body TEXT,
	isms_certification_date DATE,
	isms_recertification_date DATE,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	isms_organization_isms_id TEXT,
	isms_policy_isms_id TEXT,
	isms_risk_assessment_process_isms_id TEXT,
	isms_risk_treatment_process_isms_id TEXT,
	isms_statement_of_applicability_isms_id TEXT,
	isms_awareness_programme_isms_id TEXT,
	isms_communication_plan_isms_id TEXT,
	isms_monitoring_programme_isms_id TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(isms_organization_isms_id) REFERENCES "IsmsOrganization" (isms_id),
	FOREIGN KEY(isms_policy_isms_id) REFERENCES "IsmsPolicy" (isms_id),
	FOREIGN KEY(isms_risk_assessment_process_isms_id) REFERENCES "IsmsRiskAssessmentProcess" (isms_id),
	FOREIGN KEY(isms_risk_treatment_process_isms_id) REFERENCES "IsmsRiskTreatmentProcess" (isms_id),
	FOREIGN KEY(isms_statement_of_applicability_isms_id) REFERENCES "IsmsStatementOfApplicability" (isms_id),
	FOREIGN KEY(isms_awareness_programme_isms_id) REFERENCES "IsmsAwarenessProgramme" (isms_id),
	FOREIGN KEY(isms_communication_plan_isms_id) REFERENCES "IsmsCommunicationPlan" (isms_id),
	FOREIGN KEY(isms_monitoring_programme_isms_id) REFERENCES "IsmsMonitoringProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem" (isms_id);

CREATE TABLE "IsmsApplicabilityEntry" (
	id INTEGER NOT NULL,
	entry_annex_a_control VARCHAR(6),
	entry_type TEXT,
	entry_justification TEXT NOT NULL,
	"IsmsStatementOfApplicability_isms_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("IsmsStatementOfApplicability_isms_id") REFERENCES "IsmsStatementOfApplicability" (isms_id)
);
CREATE INDEX "ix_IsmsApplicabilityEntry_id" ON "IsmsApplicabilityEntry" (id);

CREATE TABLE "IsmsDocumentControlMixin_document_distribution" (
	"IsmsDocumentControlMixin_id" INTEGER,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsDocumentControlMixin_id", document_distribution),
	FOREIGN KEY("IsmsDocumentControlMixin_id") REFERENCES "IsmsDocumentControlMixin" (id)
);
CREATE INDEX "ix_IsmsDocumentControlMixin_document_distribution_document_distribution" ON "IsmsDocumentControlMixin_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsDocumentControlMixin_document_distribution_IsmsDocumentControlMixin_id" ON "IsmsDocumentControlMixin_document_distribution" ("IsmsDocumentControlMixin_id");

CREATE TABLE "IsmsOrganization_organization_trading_names" (
	"IsmsOrganization_isms_id" TEXT,
	organization_trading_names TEXT,
	PRIMARY KEY ("IsmsOrganization_isms_id", organization_trading_names),
	FOREIGN KEY("IsmsOrganization_isms_id") REFERENCES "IsmsOrganization" (isms_id)
);
CREATE INDEX "ix_IsmsOrganization_organization_trading_names_organization_trading_names" ON "IsmsOrganization_organization_trading_names" (organization_trading_names);
CREATE INDEX "ix_IsmsOrganization_organization_trading_names_IsmsOrganization_isms_id" ON "IsmsOrganization_organization_trading_names" ("IsmsOrganization_isms_id");

CREATE TABLE "IsmsOrganization_organization_locations" (
	"IsmsOrganization_isms_id" TEXT,
	organization_locations TEXT,
	PRIMARY KEY ("IsmsOrganization_isms_id", organization_locations),
	FOREIGN KEY("IsmsOrganization_isms_id") REFERENCES "IsmsOrganization" (isms_id)
);
CREATE INDEX "ix_IsmsOrganization_organization_locations_IsmsOrganization_isms_id" ON "IsmsOrganization_organization_locations" ("IsmsOrganization_isms_id");
CREATE INDEX "ix_IsmsOrganization_organization_locations_organization_locations" ON "IsmsOrganization_organization_locations" (organization_locations);

CREATE TABLE "IsmsOrganization_organization_jurisdictions" (
	"IsmsOrganization_isms_id" TEXT,
	organization_jurisdictions TEXT,
	PRIMARY KEY ("IsmsOrganization_isms_id", organization_jurisdictions),
	FOREIGN KEY("IsmsOrganization_isms_id") REFERENCES "IsmsOrganization" (isms_id)
);
CREATE INDEX "ix_IsmsOrganization_organization_jurisdictions_IsmsOrganization_isms_id" ON "IsmsOrganization_organization_jurisdictions" ("IsmsOrganization_isms_id");
CREATE INDEX "ix_IsmsOrganization_organization_jurisdictions_organization_jurisdictions" ON "IsmsOrganization_organization_jurisdictions" (organization_jurisdictions);

CREATE TABLE "IsmsOrganization_organization_subsidiaries" (
	"IsmsOrganization_isms_id" TEXT,
	organization_subsidiaries TEXT,
	PRIMARY KEY ("IsmsOrganization_isms_id", organization_subsidiaries),
	FOREIGN KEY("IsmsOrganization_isms_id") REFERENCES "IsmsOrganization" (isms_id)
);
CREATE INDEX "ix_IsmsOrganization_organization_subsidiaries_organization_subsidiaries" ON "IsmsOrganization_organization_subsidiaries" (organization_subsidiaries);
CREATE INDEX "ix_IsmsOrganization_organization_subsidiaries_IsmsOrganization_isms_id" ON "IsmsOrganization_organization_subsidiaries" ("IsmsOrganization_isms_id");

CREATE TABLE "IsmsPolicy_policy_commitments" (
	"IsmsPolicy_isms_id" TEXT,
	policy_commitments TEXT,
	PRIMARY KEY ("IsmsPolicy_isms_id", policy_commitments),
	FOREIGN KEY("IsmsPolicy_isms_id") REFERENCES "IsmsPolicy" (isms_id)
);
CREATE INDEX "ix_IsmsPolicy_policy_commitments_policy_commitments" ON "IsmsPolicy_policy_commitments" (policy_commitments);
CREATE INDEX "ix_IsmsPolicy_policy_commitments_IsmsPolicy_isms_id" ON "IsmsPolicy_policy_commitments" ("IsmsPolicy_isms_id");

CREATE TABLE "IsmsPolicy_policy_management_systems" (
	"IsmsPolicy_isms_id" TEXT,
	policy_management_systems VARCHAR(15),
	PRIMARY KEY ("IsmsPolicy_isms_id", policy_management_systems),
	FOREIGN KEY("IsmsPolicy_isms_id") REFERENCES "IsmsPolicy" (isms_id)
);
CREATE INDEX "ix_IsmsPolicy_policy_management_systems_IsmsPolicy_isms_id" ON "IsmsPolicy_policy_management_systems" ("IsmsPolicy_isms_id");
CREATE INDEX "ix_IsmsPolicy_policy_management_systems_policy_management_systems" ON "IsmsPolicy_policy_management_systems" (policy_management_systems);

CREATE TABLE "IsmsPolicy_document_distribution" (
	"IsmsPolicy_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsPolicy_isms_id", document_distribution),
	FOREIGN KEY("IsmsPolicy_isms_id") REFERENCES "IsmsPolicy" (isms_id)
);
CREATE INDEX "ix_IsmsPolicy_document_distribution_IsmsPolicy_isms_id" ON "IsmsPolicy_document_distribution" ("IsmsPolicy_isms_id");
CREATE INDEX "ix_IsmsPolicy_document_distribution_document_distribution" ON "IsmsPolicy_document_distribution" (document_distribution);

CREATE TABLE "IsmsRiskAssessmentProcess_risk_assessment_triggers" (
	"IsmsRiskAssessmentProcess_isms_id" TEXT,
	risk_assessment_triggers TEXT,
	PRIMARY KEY ("IsmsRiskAssessmentProcess_isms_id", risk_assessment_triggers),
	FOREIGN KEY("IsmsRiskAssessmentProcess_isms_id") REFERENCES "IsmsRiskAssessmentProcess" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessmentProcess_risk_assessment_triggers_IsmsRiskAssessmentProcess_isms_id" ON "IsmsRiskAssessmentProcess_risk_assessment_triggers" ("IsmsRiskAssessmentProcess_isms_id");
CREATE INDEX "ix_IsmsRiskAssessmentProcess_risk_assessment_triggers_risk_assessment_triggers" ON "IsmsRiskAssessmentProcess_risk_assessment_triggers" (risk_assessment_triggers);

CREATE TABLE "IsmsRiskAssessmentProcess_document_distribution" (
	"IsmsRiskAssessmentProcess_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsRiskAssessmentProcess_isms_id", document_distribution),
	FOREIGN KEY("IsmsRiskAssessmentProcess_isms_id") REFERENCES "IsmsRiskAssessmentProcess" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessmentProcess_document_distribution_document_distribution" ON "IsmsRiskAssessmentProcess_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsRiskAssessmentProcess_document_distribution_IsmsRiskAssessmentProcess_isms_id" ON "IsmsRiskAssessmentProcess_document_distribution" ("IsmsRiskAssessmentProcess_isms_id");

CREATE TABLE "IsmsRiskTreatmentProcess_document_distribution" (
	"IsmsRiskTreatmentProcess_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentProcess_isms_id", document_distribution),
	FOREIGN KEY("IsmsRiskTreatmentProcess_isms_id") REFERENCES "IsmsRiskTreatmentProcess" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentProcess_document_distribution_document_distribution" ON "IsmsRiskTreatmentProcess_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsRiskTreatmentProcess_document_distribution_IsmsRiskTreatmentProcess_isms_id" ON "IsmsRiskTreatmentProcess_document_distribution" ("IsmsRiskTreatmentProcess_isms_id");

CREATE TABLE "IsmsStatementOfApplicability_document_distribution" (
	"IsmsStatementOfApplicability_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsStatementOfApplicability_isms_id", document_distribution),
	FOREIGN KEY("IsmsStatementOfApplicability_isms_id") REFERENCES "IsmsStatementOfApplicability" (isms_id)
);
CREATE INDEX "ix_IsmsStatementOfApplicability_document_distribution_IsmsStatementOfApplicability_isms_id" ON "IsmsStatementOfApplicability_document_distribution" ("IsmsStatementOfApplicability_isms_id");
CREATE INDEX "ix_IsmsStatementOfApplicability_document_distribution_document_distribution" ON "IsmsStatementOfApplicability_document_distribution" (document_distribution);

CREATE TABLE "IsmsAwarenessProgramme_awareness_topics" (
	"IsmsAwarenessProgramme_isms_id" TEXT,
	awareness_topics TEXT,
	PRIMARY KEY ("IsmsAwarenessProgramme_isms_id", awareness_topics),
	FOREIGN KEY("IsmsAwarenessProgramme_isms_id") REFERENCES "IsmsAwarenessProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsAwarenessProgramme_awareness_topics_awareness_topics" ON "IsmsAwarenessProgramme_awareness_topics" (awareness_topics);
CREATE INDEX "ix_IsmsAwarenessProgramme_awareness_topics_IsmsAwarenessProgramme_isms_id" ON "IsmsAwarenessProgramme_awareness_topics" ("IsmsAwarenessProgramme_isms_id");

CREATE TABLE "IsmsAwarenessProgramme_awareness_methods" (
	"IsmsAwarenessProgramme_isms_id" TEXT,
	awareness_methods TEXT,
	PRIMARY KEY ("IsmsAwarenessProgramme_isms_id", awareness_methods),
	FOREIGN KEY("IsmsAwarenessProgramme_isms_id") REFERENCES "IsmsAwarenessProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsAwarenessProgramme_awareness_methods_awareness_methods" ON "IsmsAwarenessProgramme_awareness_methods" (awareness_methods);
CREATE INDEX "ix_IsmsAwarenessProgramme_awareness_methods_IsmsAwarenessProgramme_isms_id" ON "IsmsAwarenessProgramme_awareness_methods" ("IsmsAwarenessProgramme_isms_id");

CREATE TABLE "IsmsAwarenessProgramme_document_distribution" (
	"IsmsAwarenessProgramme_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsAwarenessProgramme_isms_id", document_distribution),
	FOREIGN KEY("IsmsAwarenessProgramme_isms_id") REFERENCES "IsmsAwarenessProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsAwarenessProgramme_document_distribution_document_distribution" ON "IsmsAwarenessProgramme_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsAwarenessProgramme_document_distribution_IsmsAwarenessProgramme_isms_id" ON "IsmsAwarenessProgramme_document_distribution" ("IsmsAwarenessProgramme_isms_id");

CREATE TABLE "IsmsCommunicationPlan_document_distribution" (
	"IsmsCommunicationPlan_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsCommunicationPlan_isms_id", document_distribution),
	FOREIGN KEY("IsmsCommunicationPlan_isms_id") REFERENCES "IsmsCommunicationPlan" (isms_id)
);
CREATE INDEX "ix_IsmsCommunicationPlan_document_distribution_IsmsCommunicationPlan_isms_id" ON "IsmsCommunicationPlan_document_distribution" ("IsmsCommunicationPlan_isms_id");
CREATE INDEX "ix_IsmsCommunicationPlan_document_distribution_document_distribution" ON "IsmsCommunicationPlan_document_distribution" (document_distribution);

CREATE TABLE "IsmsMonitoringProgramme_document_distribution" (
	"IsmsMonitoringProgramme_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsMonitoringProgramme_isms_id", document_distribution),
	FOREIGN KEY("IsmsMonitoringProgramme_isms_id") REFERENCES "IsmsMonitoringProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsMonitoringProgramme_document_distribution_document_distribution" ON "IsmsMonitoringProgramme_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsMonitoringProgramme_document_distribution_IsmsMonitoringProgramme_isms_id" ON "IsmsMonitoringProgramme_document_distribution" ("IsmsMonitoringProgramme_isms_id");

CREATE TABLE "IsmsSecurityIncident_affected_security_properties" (
	"IsmsSecurityIncident_isms_id" TEXT,
	affected_security_properties VARCHAR(15),
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", affected_security_properties),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_affected_security_properties_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_affected_security_properties" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_affected_security_properties_affected_security_properties" ON "IsmsSecurityIncident_affected_security_properties" (affected_security_properties);

CREATE TABLE "IsmsSecurityIncident_incident_response_actions" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_response_actions TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_response_actions),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_response_actions_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_response_actions" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_response_actions_incident_response_actions" ON "IsmsSecurityIncident_incident_response_actions" (incident_response_actions);

CREATE TABLE "IsmsSecurityIncident_incident_containment_actions" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_containment_actions TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_containment_actions),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_containment_actions_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_containment_actions" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_containment_actions_incident_containment_actions" ON "IsmsSecurityIncident_incident_containment_actions" (incident_containment_actions);

CREATE TABLE "IsmsSecurityIncident_incident_eradication_actions" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_eradication_actions TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_eradication_actions),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_eradication_actions_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_eradication_actions" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_eradication_actions_incident_eradication_actions" ON "IsmsSecurityIncident_incident_eradication_actions" (incident_eradication_actions);

CREATE TABLE "IsmsSecurityIncident_incident_recovery_actions" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_recovery_actions TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_recovery_actions),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_recovery_actions_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_recovery_actions" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_recovery_actions_incident_recovery_actions" ON "IsmsSecurityIncident_incident_recovery_actions" (incident_recovery_actions);

CREATE TABLE "IsmsSecurityIncident_incident_lessons_learned" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_lessons_learned TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_lessons_learned),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_lessons_learned_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_lessons_learned" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_lessons_learned_incident_lessons_learned" ON "IsmsSecurityIncident_incident_lessons_learned" (incident_lessons_learned);

CREATE TABLE "IsmsSecurityIncident_incident_evidence" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_evidence TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_evidence),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_evidence_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_evidence" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_evidence_incident_evidence" ON "IsmsSecurityIncident_incident_evidence" (incident_evidence);

CREATE TABLE "IsmsSecurityIncident_incident_notifications" (
	"IsmsSecurityIncident_isms_id" TEXT,
	incident_notifications TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", incident_notifications),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_incident_notifications_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_incident_notifications" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_incident_notifications_incident_notifications" ON "IsmsSecurityIncident_incident_notifications" (incident_notifications);

CREATE TABLE "IsmsInterestedParty" (
	party_category TEXT,
	party_relationship TEXT,
	party_communication_needs TEXT,
	party_contact TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsInterestedParty_isms_id" ON "IsmsInterestedParty" (isms_id);

CREATE TABLE "IsmsTopicSpecificPolicy" (
	topic_policy_topic TEXT,
	topic_policy_parent TEXT,
	topic_policy_audience TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(topic_policy_parent) REFERENCES "IsmsPolicy" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsTopicSpecificPolicy_isms_id" ON "IsmsTopicSpecificPolicy" (isms_id);

CREATE TABLE "IsmsRole" (
	role_category TEXT,
	role_accountability TEXT,
	role_delegation TEXT,
	role_reports_to TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(role_reports_to) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsRole_isms_id" ON "IsmsRole" (isms_id);

CREATE TABLE "IsmsRiskAssessment" (
	assessment_scope TEXT,
	assessment_date DATE,
	assessment_assessor TEXT,
	assessment_method_used TEXT,
	assessment_summary TEXT,
	assessment_next_date DATE,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessment_isms_id" ON "IsmsRiskAssessment" (isms_id);

CREATE TABLE "IsmsRisk" (
	risk_source TEXT,
	risk_threat TEXT,
	risk_vulnerability TEXT,
	risk_owner TEXT,
	risk_likelihood VARCHAR(14),
	risk_impact VARCHAR(10),
	risk_inherent_level VARCHAR(8),
	risk_residual_level VARCHAR(8),
	risk_treatment_option VARCHAR(6),
	risk_treatment_priority TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsRisk_isms_id" ON "IsmsRisk" (isms_id);

CREATE TABLE "IsmsRiskTreatmentPlan" (
	implementation_state VARCHAR(11),
	plan_scope TEXT,
	plan_resources TEXT,
	plan_timeline TEXT,
	plan_risk_owner_approval TEXT,
	plan_residual_risk_acceptance TEXT,
	plan_completion_date DATE,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan" (isms_id);

CREATE TABLE "IsmsControl" (
	implementation_state VARCHAR(11),
	control_theme VARCHAR(14),
	control_text TEXT,
	control_guidance TEXT,
	control_owner TEXT,
	control_implementation_date DATE,
	control_effectiveness TEXT,
	control_last_tested DATE,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsControl_isms_id" ON "IsmsControl" (isms_id);

CREATE TABLE "IsmsAsset" (
	asset_category TEXT,
	asset_owner TEXT,
	asset_custodian TEXT,
	asset_classification TEXT,
	asset_location TEXT,
	asset_criticality TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsAsset_isms_id" ON "IsmsAsset" (isms_id);

CREATE TABLE "IsmsResource" (
	resource_category TEXT,
	resource_quantity TEXT,
	resource_allocation_date DATE,
	resource_allocated_to TEXT,
	resource_cost TEXT,
	resource_availability TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsResource_isms_id" ON "IsmsResource" (isms_id);

CREATE TABLE "IsmsDocumentedInformation" (
	document_kind VARCHAR(9) NOT NULL,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsDocumentedInformation_isms_id" ON "IsmsDocumentedInformation" (isms_id);

CREATE TABLE "IsmsOperationalProcedure" (
	procedure_scope TEXT,
	procedure_criteria TEXT,
	procedure_change_control TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsOperationalProcedure_isms_id" ON "IsmsOperationalProcedure" (isms_id);

CREATE TABLE "IsmsAuditProgramme" (
	programme_period TEXT,
	programme_frequency_rationale TEXT,
	programme_resources TEXT,
	programme_auditor_qualifications TEXT,
	programme_status TEXT,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsAuditProgramme_isms_id" ON "IsmsAuditProgramme" (isms_id);

CREATE TABLE "IsmsManagementReview" (
	review_held_on DATE NOT NULL,
	review_previous_actions TEXT,
	review_context_changes TEXT,
	review_interested_party_changes TEXT,
	review_interested_party_feedback TEXT,
	review_performance_trends TEXT,
	review_audit_results TEXT,
	review_risk_assessment_results TEXT,
	review_risk_treatment_status TEXT,
	review_risks_and_opportunities TEXT,
	review_next_date DATE,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_isms_id" ON "IsmsManagementReview" (isms_id);

CREATE TABLE "IsmsNonconformity" (
	nonconformity_source TEXT,
	nonconformity_detected_on DATE,
	nonconformity_detected_by TEXT,
	nonconformity_requirement TEXT,
	nonconformity_consequences TEXT,
	nonconformity_root_cause TEXT,
	nonconformity_similar_check TEXT,
	nonconformity_status TEXT,
	nonconformity_closure_date DATE,
	nonconformity_closure_evidence TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsNonconformity_isms_id" ON "IsmsNonconformity" (isms_id);

CREATE TABLE "IsmsSecurityEvent" (
	event_type TEXT,
	event_occurred_at DATETIME,
	event_reporter TEXT,
	event_assessment TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityEvent_isms_id" ON "IsmsSecurityEvent" (isms_id);

CREATE TABLE "IsmsManagementSystem_isms_leadership_evidence" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_leadership_evidence TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_leadership_evidence),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_leadership_evidence_isms_leadership_evidence" ON "IsmsManagementSystem_isms_leadership_evidence" (isms_leadership_evidence);
CREATE INDEX "ix_IsmsManagementSystem_isms_leadership_evidence_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_leadership_evidence" ("IsmsManagementSystem_isms_id");

CREATE TABLE "IsmsManagementSystem_isms_scope_boundaries" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_scope_boundaries TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_scope_boundaries),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_scope_boundaries_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_scope_boundaries" ("IsmsManagementSystem_isms_id");
CREATE INDEX "ix_IsmsManagementSystem_isms_scope_boundaries_isms_scope_boundaries" ON "IsmsManagementSystem_isms_scope_boundaries" (isms_scope_boundaries);

CREATE TABLE "IsmsManagementSystem_isms_scope_exclusions" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_scope_exclusions TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_scope_exclusions),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_scope_exclusions_isms_scope_exclusions" ON "IsmsManagementSystem_isms_scope_exclusions" (isms_scope_exclusions);
CREATE INDEX "ix_IsmsManagementSystem_isms_scope_exclusions_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_scope_exclusions" ("IsmsManagementSystem_isms_id");

CREATE TABLE "IsmsManagementSystem_isms_interfaces" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_interfaces TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_interfaces),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_interfaces_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_interfaces" ("IsmsManagementSystem_isms_id");
CREATE INDEX "ix_IsmsManagementSystem_isms_interfaces_isms_interfaces" ON "IsmsManagementSystem_isms_interfaces" (isms_interfaces);

CREATE TABLE "IsmsManagementSystem_isms_internal_issues" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_internal_issues TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_internal_issues),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_internal_issues_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_internal_issues" ("IsmsManagementSystem_isms_id");
CREATE INDEX "ix_IsmsManagementSystem_isms_internal_issues_isms_internal_issues" ON "IsmsManagementSystem_isms_internal_issues" (isms_internal_issues);

CREATE TABLE "IsmsManagementSystem_isms_external_issues" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_external_issues TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_external_issues),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_external_issues_isms_external_issues" ON "IsmsManagementSystem_isms_external_issues" (isms_external_issues);
CREATE INDEX "ix_IsmsManagementSystem_isms_external_issues_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_external_issues" ("IsmsManagementSystem_isms_id");

CREATE TABLE "IsmsManagementSystem_isms_risk_and_opportunity_actions" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_risk_and_opportunity_actions TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_risk_and_opportunity_actions),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_risk_and_opportunity_actions_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_risk_and_opportunity_actions" ("IsmsManagementSystem_isms_id");
CREATE INDEX "ix_IsmsManagementSystem_isms_risk_and_opportunity_actions_isms_risk_and_opportunity_actions" ON "IsmsManagementSystem_isms_risk_and_opportunity_actions" (isms_risk_and_opportunity_actions);

CREATE TABLE "IsmsManagementSystem_isms_planned_changes" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_planned_changes TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_planned_changes),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_planned_changes_isms_planned_changes" ON "IsmsManagementSystem_isms_planned_changes" (isms_planned_changes);
CREATE INDEX "ix_IsmsManagementSystem_isms_planned_changes_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_planned_changes" ("IsmsManagementSystem_isms_id");

CREATE TABLE "IsmsManagementSystem_isms_external_services" (
	"IsmsManagementSystem_isms_id" TEXT,
	isms_external_services TEXT,
	PRIMARY KEY ("IsmsManagementSystem_isms_id", isms_external_services),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsManagementSystem_isms_external_services_isms_external_services" ON "IsmsManagementSystem_isms_external_services" (isms_external_services);
CREATE INDEX "ix_IsmsManagementSystem_isms_external_services_IsmsManagementSystem_isms_id" ON "IsmsManagementSystem_isms_external_services" ("IsmsManagementSystem_isms_id");

CREATE TABLE "IsmsObjective" (
	responsible_role TEXT,
	objective_statement TEXT,
	objective_target TEXT,
	objective_current_value TEXT,
	objective_metric TEXT,
	objective_measurement_method TEXT,
	objective_measurement_frequency TEXT,
	objective_target_date DATE,
	objective_achievement TEXT,
	objective_action_plan TEXT,
	objective_resources TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsObjective_isms_id" ON "IsmsObjective" (isms_id);

CREATE TABLE "IsmsIncludedControl" (
	id INTEGER NOT NULL,
	implementation_state VARCHAR(11) NOT NULL,
	responsible_role TEXT,
	included_control TEXT,
	included_evidence TEXT,
	included_target_date DATE,
	entry_annex_a_control VARCHAR(6),
	entry_type TEXT,
	entry_justification TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY(included_control) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsIncludedControl_id" ON "IsmsIncludedControl" (id);

CREATE TABLE "IsmsCompetenceRecord" (
	competence_person TEXT,
	competence_role TEXT,
	competence_assessment_date DATE,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(competence_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord" (isms_id);

CREATE TABLE "IsmsCommunication" (
	id INTEGER NOT NULL,
	responsible_role TEXT,
	communication_subject TEXT NOT NULL,
	communication_purpose TEXT,
	communication_audience TEXT,
	communication_frequency TEXT,
	communication_method TEXT,
	communication_records_required BOOLEAN,
	"IsmsCommunicationPlan_isms_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsCommunicationPlan_isms_id") REFERENCES "IsmsCommunicationPlan" (isms_id)
);
CREATE INDEX "ix_IsmsCommunication_id" ON "IsmsCommunication" (id);

CREATE TABLE "IsmsMonitoringItem" (
	id INTEGER NOT NULL,
	responsible_role TEXT,
	monitoring_metric TEXT NOT NULL,
	monitoring_description TEXT,
	monitoring_method TEXT,
	monitoring_frequency TEXT,
	monitoring_analysis_frequency TEXT,
	monitoring_analyst TEXT,
	monitoring_target TEXT,
	monitoring_alert_threshold TEXT,
	monitoring_current_value TEXT,
	monitoring_trend TEXT,
	"IsmsMonitoringProgramme_isms_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsMonitoringProgramme_isms_id") REFERENCES "IsmsMonitoringProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsMonitoringItem_id" ON "IsmsMonitoringItem" (id);

CREATE TABLE "IsmsAudit" (
	audit_type VARCHAR(12) NOT NULL,
	audit_scope TEXT,
	audit_period_start DATE,
	audit_period_end DATE,
	audit_lead TEXT,
	audit_plan TEXT,
	audit_conclusion TEXT,
	audit_report_date DATE,
	document_reference TEXT,
	document_version TEXT,
	document_author TEXT,
	document_owner TEXT,
	document_approver TEXT,
	document_approval_date DATE,
	document_effective_date DATE,
	document_last_review_date DATE,
	document_next_review_date DATE,
	document_status TEXT,
	document_classification TEXT,
	document_retention TEXT,
	document_storage TEXT,
	document_change_control TEXT,
	document_external_origin BOOLEAN,
	document_external_source TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(audit_plan) REFERENCES "IsmsDocumentedInformation" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_isms_id" ON "IsmsAudit" (isms_id);

CREATE TABLE "IsmsCorrectiveAction" (
	responsible_role TEXT,
	action_root_cause TEXT,
	action_target_date DATE,
	action_completion_date DATE,
	action_resources TEXT,
	action_effectiveness_criteria TEXT,
	action_effectiveness_review_date DATE,
	action_effective BOOLEAN,
	action_isms_changes TEXT,
	action_status TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsCorrectiveAction_isms_id" ON "IsmsCorrectiveAction" (isms_id);

CREATE TABLE "IsmsImprovementOpportunity" (
	responsible_role TEXT,
	improvement_source TEXT,
	improvement_identified_on DATE,
	improvement_identified_by TEXT,
	improvement_benefit TEXT,
	improvement_priority TEXT,
	improvement_plan TEXT,
	improvement_target_date DATE,
	improvement_completion_date DATE,
	improvement_outcome TEXT,
	improvement_status TEXT,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsManagementSystem_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(responsible_role) REFERENCES "IsmsRole" (isms_id),
	FOREIGN KEY("IsmsManagementSystem_isms_id") REFERENCES "IsmsManagementSystem" (isms_id)
);
CREATE INDEX "ix_IsmsImprovementOpportunity_isms_id" ON "IsmsImprovementOpportunity" (isms_id);

CREATE TABLE "IsmsInterestedParty_party_requirements" (
	"IsmsInterestedParty_isms_id" TEXT,
	party_requirements TEXT,
	PRIMARY KEY ("IsmsInterestedParty_isms_id", party_requirements),
	FOREIGN KEY("IsmsInterestedParty_isms_id") REFERENCES "IsmsInterestedParty" (isms_id)
);
CREATE INDEX "ix_IsmsInterestedParty_party_requirements_IsmsInterestedParty_isms_id" ON "IsmsInterestedParty_party_requirements" ("IsmsInterestedParty_isms_id");
CREATE INDEX "ix_IsmsInterestedParty_party_requirements_party_requirements" ON "IsmsInterestedParty_party_requirements" (party_requirements);

CREATE TABLE "IsmsInterestedParty_party_addressed_requirements" (
	"IsmsInterestedParty_isms_id" TEXT,
	party_addressed_requirements TEXT,
	PRIMARY KEY ("IsmsInterestedParty_isms_id", party_addressed_requirements),
	FOREIGN KEY("IsmsInterestedParty_isms_id") REFERENCES "IsmsInterestedParty" (isms_id)
);
CREATE INDEX "ix_IsmsInterestedParty_party_addressed_requirements_party_addressed_requirements" ON "IsmsInterestedParty_party_addressed_requirements" (party_addressed_requirements);
CREATE INDEX "ix_IsmsInterestedParty_party_addressed_requirements_IsmsInterestedParty_isms_id" ON "IsmsInterestedParty_party_addressed_requirements" ("IsmsInterestedParty_isms_id");

CREATE TABLE "IsmsInterestedParty_party_climate_change_requirements" (
	"IsmsInterestedParty_isms_id" TEXT,
	party_climate_change_requirements TEXT,
	PRIMARY KEY ("IsmsInterestedParty_isms_id", party_climate_change_requirements),
	FOREIGN KEY("IsmsInterestedParty_isms_id") REFERENCES "IsmsInterestedParty" (isms_id)
);
CREATE INDEX "ix_IsmsInterestedParty_party_climate_change_requirements_IsmsInterestedParty_isms_id" ON "IsmsInterestedParty_party_climate_change_requirements" ("IsmsInterestedParty_isms_id");
CREATE INDEX "ix_IsmsInterestedParty_party_climate_change_requirements_party_climate_change_requirements" ON "IsmsInterestedParty_party_climate_change_requirements" (party_climate_change_requirements);

CREATE TABLE "IsmsTopicSpecificPolicy_relevant_controls" (
	"IsmsTopicSpecificPolicy_isms_id" TEXT,
	relevant_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsTopicSpecificPolicy_isms_id", relevant_controls_isms_id),
	FOREIGN KEY("IsmsTopicSpecificPolicy_isms_id") REFERENCES "IsmsTopicSpecificPolicy" (isms_id),
	FOREIGN KEY(relevant_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsTopicSpecificPolicy_relevant_controls_IsmsTopicSpecificPolicy_isms_id" ON "IsmsTopicSpecificPolicy_relevant_controls" ("IsmsTopicSpecificPolicy_isms_id");
CREATE INDEX "ix_IsmsTopicSpecificPolicy_relevant_controls_relevant_controls_isms_id" ON "IsmsTopicSpecificPolicy_relevant_controls" (relevant_controls_isms_id);

CREATE TABLE "IsmsTopicSpecificPolicy_document_distribution" (
	"IsmsTopicSpecificPolicy_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsTopicSpecificPolicy_isms_id", document_distribution),
	FOREIGN KEY("IsmsTopicSpecificPolicy_isms_id") REFERENCES "IsmsTopicSpecificPolicy" (isms_id)
);
CREATE INDEX "ix_IsmsTopicSpecificPolicy_document_distribution_IsmsTopicSpecificPolicy_isms_id" ON "IsmsTopicSpecificPolicy_document_distribution" ("IsmsTopicSpecificPolicy_isms_id");
CREATE INDEX "ix_IsmsTopicSpecificPolicy_document_distribution_document_distribution" ON "IsmsTopicSpecificPolicy_document_distribution" (document_distribution);

CREATE TABLE "IsmsRole_role_responsibilities" (
	"IsmsRole_isms_id" TEXT,
	role_responsibilities TEXT,
	PRIMARY KEY ("IsmsRole_isms_id", role_responsibilities),
	FOREIGN KEY("IsmsRole_isms_id") REFERENCES "IsmsRole" (isms_id)
);
CREATE INDEX "ix_IsmsRole_role_responsibilities_IsmsRole_isms_id" ON "IsmsRole_role_responsibilities" ("IsmsRole_isms_id");
CREATE INDEX "ix_IsmsRole_role_responsibilities_role_responsibilities" ON "IsmsRole_role_responsibilities" (role_responsibilities);

CREATE TABLE "IsmsRole_role_authorities" (
	"IsmsRole_isms_id" TEXT,
	role_authorities TEXT,
	PRIMARY KEY ("IsmsRole_isms_id", role_authorities),
	FOREIGN KEY("IsmsRole_isms_id") REFERENCES "IsmsRole" (isms_id)
);
CREATE INDEX "ix_IsmsRole_role_authorities_role_authorities" ON "IsmsRole_role_authorities" (role_authorities);
CREATE INDEX "ix_IsmsRole_role_authorities_IsmsRole_isms_id" ON "IsmsRole_role_authorities" ("IsmsRole_isms_id");

CREATE TABLE "IsmsRole_role_holders" (
	"IsmsRole_isms_id" TEXT,
	role_holders TEXT,
	PRIMARY KEY ("IsmsRole_isms_id", role_holders),
	FOREIGN KEY("IsmsRole_isms_id") REFERENCES "IsmsRole" (isms_id)
);
CREATE INDEX "ix_IsmsRole_role_holders_role_holders" ON "IsmsRole_role_holders" (role_holders);
CREATE INDEX "ix_IsmsRole_role_holders_IsmsRole_isms_id" ON "IsmsRole_role_holders" ("IsmsRole_isms_id");

CREATE TABLE "IsmsRiskAssessment_assessment_risks" (
	"IsmsRiskAssessment_isms_id" TEXT,
	assessment_risks_isms_id TEXT,
	PRIMARY KEY ("IsmsRiskAssessment_isms_id", assessment_risks_isms_id),
	FOREIGN KEY("IsmsRiskAssessment_isms_id") REFERENCES "IsmsRiskAssessment" (isms_id),
	FOREIGN KEY(assessment_risks_isms_id) REFERENCES "IsmsRisk" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessment_assessment_risks_IsmsRiskAssessment_isms_id" ON "IsmsRiskAssessment_assessment_risks" ("IsmsRiskAssessment_isms_id");
CREATE INDEX "ix_IsmsRiskAssessment_assessment_risks_assessment_risks_isms_id" ON "IsmsRiskAssessment_assessment_risks" (assessment_risks_isms_id);

CREATE TABLE "IsmsRiskAssessment_assessment_recommendations" (
	"IsmsRiskAssessment_isms_id" TEXT,
	assessment_recommendations TEXT,
	PRIMARY KEY ("IsmsRiskAssessment_isms_id", assessment_recommendations),
	FOREIGN KEY("IsmsRiskAssessment_isms_id") REFERENCES "IsmsRiskAssessment" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessment_assessment_recommendations_IsmsRiskAssessment_isms_id" ON "IsmsRiskAssessment_assessment_recommendations" ("IsmsRiskAssessment_isms_id");
CREATE INDEX "ix_IsmsRiskAssessment_assessment_recommendations_assessment_recommendations" ON "IsmsRiskAssessment_assessment_recommendations" (assessment_recommendations);

CREATE TABLE "IsmsRiskAssessment_document_distribution" (
	"IsmsRiskAssessment_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsRiskAssessment_isms_id", document_distribution),
	FOREIGN KEY("IsmsRiskAssessment_isms_id") REFERENCES "IsmsRiskAssessment" (isms_id)
);
CREATE INDEX "ix_IsmsRiskAssessment_document_distribution_document_distribution" ON "IsmsRiskAssessment_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsRiskAssessment_document_distribution_IsmsRiskAssessment_isms_id" ON "IsmsRiskAssessment_document_distribution" ("IsmsRiskAssessment_isms_id");

CREATE TABLE "IsmsRisk_affected_assets" (
	"IsmsRisk_isms_id" TEXT,
	affected_assets_isms_id TEXT,
	PRIMARY KEY ("IsmsRisk_isms_id", affected_assets_isms_id),
	FOREIGN KEY("IsmsRisk_isms_id") REFERENCES "IsmsRisk" (isms_id),
	FOREIGN KEY(affected_assets_isms_id) REFERENCES "IsmsAsset" (isms_id)
);
CREATE INDEX "ix_IsmsRisk_affected_assets_affected_assets_isms_id" ON "IsmsRisk_affected_assets" (affected_assets_isms_id);
CREATE INDEX "ix_IsmsRisk_affected_assets_IsmsRisk_isms_id" ON "IsmsRisk_affected_assets" ("IsmsRisk_isms_id");

CREATE TABLE "IsmsRisk_affected_security_properties" (
	"IsmsRisk_isms_id" TEXT,
	affected_security_properties VARCHAR(15),
	PRIMARY KEY ("IsmsRisk_isms_id", affected_security_properties),
	FOREIGN KEY("IsmsRisk_isms_id") REFERENCES "IsmsRisk" (isms_id)
);
CREATE INDEX "ix_IsmsRisk_affected_security_properties_affected_security_properties" ON "IsmsRisk_affected_security_properties" (affected_security_properties);
CREATE INDEX "ix_IsmsRisk_affected_security_properties_IsmsRisk_isms_id" ON "IsmsRisk_affected_security_properties" ("IsmsRisk_isms_id");

CREATE TABLE "IsmsRisk_risk_existing_controls" (
	"IsmsRisk_isms_id" TEXT,
	risk_existing_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsRisk_isms_id", risk_existing_controls_isms_id),
	FOREIGN KEY("IsmsRisk_isms_id") REFERENCES "IsmsRisk" (isms_id),
	FOREIGN KEY(risk_existing_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsRisk_risk_existing_controls_risk_existing_controls_isms_id" ON "IsmsRisk_risk_existing_controls" (risk_existing_controls_isms_id);
CREATE INDEX "ix_IsmsRisk_risk_existing_controls_IsmsRisk_isms_id" ON "IsmsRisk_risk_existing_controls" ("IsmsRisk_isms_id");

CREATE TABLE "IsmsRiskTreatmentPlan_plan_risks" (
	"IsmsRiskTreatmentPlan_isms_id" TEXT,
	plan_risks_isms_id TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentPlan_isms_id", plan_risks_isms_id),
	FOREIGN KEY("IsmsRiskTreatmentPlan_isms_id") REFERENCES "IsmsRiskTreatmentPlan" (isms_id),
	FOREIGN KEY(plan_risks_isms_id) REFERENCES "IsmsRisk" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_risks_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan_plan_risks" ("IsmsRiskTreatmentPlan_isms_id");
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_risks_plan_risks_isms_id" ON "IsmsRiskTreatmentPlan_plan_risks" (plan_risks_isms_id);

CREATE TABLE "IsmsRiskTreatmentPlan_plan_actions" (
	"IsmsRiskTreatmentPlan_isms_id" TEXT,
	plan_actions TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentPlan_isms_id", plan_actions),
	FOREIGN KEY("IsmsRiskTreatmentPlan_isms_id") REFERENCES "IsmsRiskTreatmentPlan" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_actions_plan_actions" ON "IsmsRiskTreatmentPlan_plan_actions" (plan_actions);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_actions_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan_plan_actions" ("IsmsRiskTreatmentPlan_isms_id");

CREATE TABLE "IsmsRiskTreatmentPlan_plan_controls" (
	"IsmsRiskTreatmentPlan_isms_id" TEXT,
	plan_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentPlan_isms_id", plan_controls_isms_id),
	FOREIGN KEY("IsmsRiskTreatmentPlan_isms_id") REFERENCES "IsmsRiskTreatmentPlan" (isms_id),
	FOREIGN KEY(plan_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_controls_plan_controls_isms_id" ON "IsmsRiskTreatmentPlan_plan_controls" (plan_controls_isms_id);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_controls_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan_plan_controls" ("IsmsRiskTreatmentPlan_isms_id");

CREATE TABLE "IsmsRiskTreatmentPlan_plan_responsible_parties" (
	"IsmsRiskTreatmentPlan_isms_id" TEXT,
	plan_responsible_parties TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentPlan_isms_id", plan_responsible_parties),
	FOREIGN KEY("IsmsRiskTreatmentPlan_isms_id") REFERENCES "IsmsRiskTreatmentPlan" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_responsible_parties_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan_plan_responsible_parties" ("IsmsRiskTreatmentPlan_isms_id");
CREATE INDEX "ix_IsmsRiskTreatmentPlan_plan_responsible_parties_plan_responsible_parties" ON "IsmsRiskTreatmentPlan_plan_responsible_parties" (plan_responsible_parties);

CREATE TABLE "IsmsRiskTreatmentPlan_document_distribution" (
	"IsmsRiskTreatmentPlan_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsRiskTreatmentPlan_isms_id", document_distribution),
	FOREIGN KEY("IsmsRiskTreatmentPlan_isms_id") REFERENCES "IsmsRiskTreatmentPlan" (isms_id)
);
CREATE INDEX "ix_IsmsRiskTreatmentPlan_document_distribution_IsmsRiskTreatmentPlan_isms_id" ON "IsmsRiskTreatmentPlan_document_distribution" ("IsmsRiskTreatmentPlan_isms_id");
CREATE INDEX "ix_IsmsRiskTreatmentPlan_document_distribution_document_distribution" ON "IsmsRiskTreatmentPlan_document_distribution" (document_distribution);

CREATE TABLE "IsmsControl_relevant_controls" (
	"IsmsControl_isms_id" TEXT,
	relevant_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsControl_isms_id", relevant_controls_isms_id),
	FOREIGN KEY("IsmsControl_isms_id") REFERENCES "IsmsControl" (isms_id),
	FOREIGN KEY(relevant_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsControl_relevant_controls_IsmsControl_isms_id" ON "IsmsControl_relevant_controls" ("IsmsControl_isms_id");
CREATE INDEX "ix_IsmsControl_relevant_controls_relevant_controls_isms_id" ON "IsmsControl_relevant_controls" (relevant_controls_isms_id);

CREATE TABLE "IsmsControl_control_annex_a_controls" (
	"IsmsControl_isms_id" TEXT,
	control_annex_a_controls VARCHAR(6),
	PRIMARY KEY ("IsmsControl_isms_id", control_annex_a_controls),
	FOREIGN KEY("IsmsControl_isms_id") REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsControl_control_annex_a_controls_IsmsControl_isms_id" ON "IsmsControl_control_annex_a_controls" ("IsmsControl_isms_id");
CREATE INDEX "ix_IsmsControl_control_annex_a_controls_control_annex_a_controls" ON "IsmsControl_control_annex_a_controls" (control_annex_a_controls);

CREATE TABLE "IsmsControl_control_threats" (
	"IsmsControl_isms_id" TEXT,
	control_threats TEXT,
	PRIMARY KEY ("IsmsControl_isms_id", control_threats),
	FOREIGN KEY("IsmsControl_isms_id") REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsControl_control_threats_IsmsControl_isms_id" ON "IsmsControl_control_threats" ("IsmsControl_isms_id");
CREATE INDEX "ix_IsmsControl_control_threats_control_threats" ON "IsmsControl_control_threats" (control_threats);

CREATE TABLE "IsmsControl_control_asset_types" (
	"IsmsControl_isms_id" TEXT,
	control_asset_types TEXT,
	PRIMARY KEY ("IsmsControl_isms_id", control_asset_types),
	FOREIGN KEY("IsmsControl_isms_id") REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsControl_control_asset_types_IsmsControl_isms_id" ON "IsmsControl_control_asset_types" ("IsmsControl_isms_id");
CREATE INDEX "ix_IsmsControl_control_asset_types_control_asset_types" ON "IsmsControl_control_asset_types" (control_asset_types);

CREATE TABLE "IsmsControl_control_evidence" (
	"IsmsControl_isms_id" TEXT,
	control_evidence TEXT,
	PRIMARY KEY ("IsmsControl_isms_id", control_evidence),
	FOREIGN KEY("IsmsControl_isms_id") REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsControl_control_evidence_control_evidence" ON "IsmsControl_control_evidence" (control_evidence);
CREATE INDEX "ix_IsmsControl_control_evidence_IsmsControl_isms_id" ON "IsmsControl_control_evidence" ("IsmsControl_isms_id");

CREATE TABLE "IsmsAsset_relevant_controls" (
	"IsmsAsset_isms_id" TEXT,
	relevant_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsAsset_isms_id", relevant_controls_isms_id),
	FOREIGN KEY("IsmsAsset_isms_id") REFERENCES "IsmsAsset" (isms_id),
	FOREIGN KEY(relevant_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsAsset_relevant_controls_IsmsAsset_isms_id" ON "IsmsAsset_relevant_controls" ("IsmsAsset_isms_id");
CREATE INDEX "ix_IsmsAsset_relevant_controls_relevant_controls_isms_id" ON "IsmsAsset_relevant_controls" (relevant_controls_isms_id);

CREATE TABLE "IsmsDocumentedInformation_document_distribution" (
	"IsmsDocumentedInformation_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsDocumentedInformation_isms_id", document_distribution),
	FOREIGN KEY("IsmsDocumentedInformation_isms_id") REFERENCES "IsmsDocumentedInformation" (isms_id)
);
CREATE INDEX "ix_IsmsDocumentedInformation_document_distribution_document_distribution" ON "IsmsDocumentedInformation_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsDocumentedInformation_document_distribution_IsmsDocumentedInformation_isms_id" ON "IsmsDocumentedInformation_document_distribution" ("IsmsDocumentedInformation_isms_id");

CREATE TABLE "IsmsOperationalProcedure_relevant_controls" (
	"IsmsOperationalProcedure_isms_id" TEXT,
	relevant_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsOperationalProcedure_isms_id", relevant_controls_isms_id),
	FOREIGN KEY("IsmsOperationalProcedure_isms_id") REFERENCES "IsmsOperationalProcedure" (isms_id),
	FOREIGN KEY(relevant_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsOperationalProcedure_relevant_controls_IsmsOperationalProcedure_isms_id" ON "IsmsOperationalProcedure_relevant_controls" ("IsmsOperationalProcedure_isms_id");
CREATE INDEX "ix_IsmsOperationalProcedure_relevant_controls_relevant_controls_isms_id" ON "IsmsOperationalProcedure_relevant_controls" (relevant_controls_isms_id);

CREATE TABLE "IsmsOperationalProcedure_procedure_control_measures" (
	"IsmsOperationalProcedure_isms_id" TEXT,
	procedure_control_measures TEXT,
	PRIMARY KEY ("IsmsOperationalProcedure_isms_id", procedure_control_measures),
	FOREIGN KEY("IsmsOperationalProcedure_isms_id") REFERENCES "IsmsOperationalProcedure" (isms_id)
);
CREATE INDEX "ix_IsmsOperationalProcedure_procedure_control_measures_procedure_control_measures" ON "IsmsOperationalProcedure_procedure_control_measures" (procedure_control_measures);
CREATE INDEX "ix_IsmsOperationalProcedure_procedure_control_measures_IsmsOperationalProcedure_isms_id" ON "IsmsOperationalProcedure_procedure_control_measures" ("IsmsOperationalProcedure_isms_id");

CREATE TABLE "IsmsOperationalProcedure_procedure_roles" (
	"IsmsOperationalProcedure_isms_id" TEXT,
	procedure_roles_isms_id TEXT,
	PRIMARY KEY ("IsmsOperationalProcedure_isms_id", procedure_roles_isms_id),
	FOREIGN KEY("IsmsOperationalProcedure_isms_id") REFERENCES "IsmsOperationalProcedure" (isms_id),
	FOREIGN KEY(procedure_roles_isms_id) REFERENCES "IsmsRole" (isms_id)
);
CREATE INDEX "ix_IsmsOperationalProcedure_procedure_roles_procedure_roles_isms_id" ON "IsmsOperationalProcedure_procedure_roles" (procedure_roles_isms_id);
CREATE INDEX "ix_IsmsOperationalProcedure_procedure_roles_IsmsOperationalProcedure_isms_id" ON "IsmsOperationalProcedure_procedure_roles" ("IsmsOperationalProcedure_isms_id");

CREATE TABLE "IsmsOperationalProcedure_document_distribution" (
	"IsmsOperationalProcedure_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsOperationalProcedure_isms_id", document_distribution),
	FOREIGN KEY("IsmsOperationalProcedure_isms_id") REFERENCES "IsmsOperationalProcedure" (isms_id)
);
CREATE INDEX "ix_IsmsOperationalProcedure_document_distribution_IsmsOperationalProcedure_isms_id" ON "IsmsOperationalProcedure_document_distribution" ("IsmsOperationalProcedure_isms_id");
CREATE INDEX "ix_IsmsOperationalProcedure_document_distribution_document_distribution" ON "IsmsOperationalProcedure_document_distribution" (document_distribution);

CREATE TABLE "IsmsAuditProgramme_document_distribution" (
	"IsmsAuditProgramme_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsAuditProgramme_isms_id", document_distribution),
	FOREIGN KEY("IsmsAuditProgramme_isms_id") REFERENCES "IsmsAuditProgramme" (isms_id)
);
CREATE INDEX "ix_IsmsAuditProgramme_document_distribution_document_distribution" ON "IsmsAuditProgramme_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsAuditProgramme_document_distribution_IsmsAuditProgramme_isms_id" ON "IsmsAuditProgramme_document_distribution" ("IsmsAuditProgramme_isms_id");

CREATE TABLE "IsmsManagementReview_review_attendees" (
	"IsmsManagementReview_isms_id" TEXT,
	review_attendees TEXT,
	PRIMARY KEY ("IsmsManagementReview_isms_id", review_attendees),
	FOREIGN KEY("IsmsManagementReview_isms_id") REFERENCES "IsmsManagementReview" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_review_attendees_IsmsManagementReview_isms_id" ON "IsmsManagementReview_review_attendees" ("IsmsManagementReview_isms_id");
CREATE INDEX "ix_IsmsManagementReview_review_attendees_review_attendees" ON "IsmsManagementReview_review_attendees" (review_attendees);

CREATE TABLE "IsmsManagementReview_review_improvement_opportunities" (
	"IsmsManagementReview_isms_id" TEXT,
	review_improvement_opportunities TEXT,
	PRIMARY KEY ("IsmsManagementReview_isms_id", review_improvement_opportunities),
	FOREIGN KEY("IsmsManagementReview_isms_id") REFERENCES "IsmsManagementReview" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_review_improvement_opportunities_IsmsManagementReview_isms_id" ON "IsmsManagementReview_review_improvement_opportunities" ("IsmsManagementReview_isms_id");
CREATE INDEX "ix_IsmsManagementReview_review_improvement_opportunities_review_improvement_opportunities" ON "IsmsManagementReview_review_improvement_opportunities" (review_improvement_opportunities);

CREATE TABLE "IsmsManagementReview_review_decisions" (
	"IsmsManagementReview_isms_id" TEXT,
	review_decisions TEXT,
	PRIMARY KEY ("IsmsManagementReview_isms_id", review_decisions),
	FOREIGN KEY("IsmsManagementReview_isms_id") REFERENCES "IsmsManagementReview" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_review_decisions_IsmsManagementReview_isms_id" ON "IsmsManagementReview_review_decisions" ("IsmsManagementReview_isms_id");
CREATE INDEX "ix_IsmsManagementReview_review_decisions_review_decisions" ON "IsmsManagementReview_review_decisions" (review_decisions);

CREATE TABLE "IsmsManagementReview_review_actions" (
	"IsmsManagementReview_isms_id" TEXT,
	review_actions TEXT,
	PRIMARY KEY ("IsmsManagementReview_isms_id", review_actions),
	FOREIGN KEY("IsmsManagementReview_isms_id") REFERENCES "IsmsManagementReview" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_review_actions_IsmsManagementReview_isms_id" ON "IsmsManagementReview_review_actions" ("IsmsManagementReview_isms_id");
CREATE INDEX "ix_IsmsManagementReview_review_actions_review_actions" ON "IsmsManagementReview_review_actions" (review_actions);

CREATE TABLE "IsmsManagementReview_document_distribution" (
	"IsmsManagementReview_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsManagementReview_isms_id", document_distribution),
	FOREIGN KEY("IsmsManagementReview_isms_id") REFERENCES "IsmsManagementReview" (isms_id)
);
CREATE INDEX "ix_IsmsManagementReview_document_distribution_IsmsManagementReview_isms_id" ON "IsmsManagementReview_document_distribution" ("IsmsManagementReview_isms_id");
CREATE INDEX "ix_IsmsManagementReview_document_distribution_document_distribution" ON "IsmsManagementReview_document_distribution" (document_distribution);

CREATE TABLE "IsmsNonconformity_nonconformity_immediate_actions" (
	"IsmsNonconformity_isms_id" TEXT,
	nonconformity_immediate_actions TEXT,
	PRIMARY KEY ("IsmsNonconformity_isms_id", nonconformity_immediate_actions),
	FOREIGN KEY("IsmsNonconformity_isms_id") REFERENCES "IsmsNonconformity" (isms_id)
);
CREATE INDEX "ix_IsmsNonconformity_nonconformity_immediate_actions_IsmsNonconformity_isms_id" ON "IsmsNonconformity_nonconformity_immediate_actions" ("IsmsNonconformity_isms_id");
CREATE INDEX "ix_IsmsNonconformity_nonconformity_immediate_actions_nonconformity_immediate_actions" ON "IsmsNonconformity_nonconformity_immediate_actions" (nonconformity_immediate_actions);

CREATE TABLE "IsmsSecurityEvent_affected_assets" (
	"IsmsSecurityEvent_isms_id" TEXT,
	affected_assets_isms_id TEXT,
	PRIMARY KEY ("IsmsSecurityEvent_isms_id", affected_assets_isms_id),
	FOREIGN KEY("IsmsSecurityEvent_isms_id") REFERENCES "IsmsSecurityEvent" (isms_id),
	FOREIGN KEY(affected_assets_isms_id) REFERENCES "IsmsAsset" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityEvent_affected_assets_affected_assets_isms_id" ON "IsmsSecurityEvent_affected_assets" (affected_assets_isms_id);
CREATE INDEX "ix_IsmsSecurityEvent_affected_assets_IsmsSecurityEvent_isms_id" ON "IsmsSecurityEvent_affected_assets" ("IsmsSecurityEvent_isms_id");

CREATE TABLE "IsmsSecurityIncident_affected_assets" (
	"IsmsSecurityIncident_isms_id" TEXT,
	affected_assets_isms_id TEXT,
	PRIMARY KEY ("IsmsSecurityIncident_isms_id", affected_assets_isms_id),
	FOREIGN KEY("IsmsSecurityIncident_isms_id") REFERENCES "IsmsSecurityIncident" (isms_id),
	FOREIGN KEY(affected_assets_isms_id) REFERENCES "IsmsAsset" (isms_id)
);
CREATE INDEX "ix_IsmsSecurityIncident_affected_assets_IsmsSecurityIncident_isms_id" ON "IsmsSecurityIncident_affected_assets" ("IsmsSecurityIncident_isms_id");
CREATE INDEX "ix_IsmsSecurityIncident_affected_assets_affected_assets_isms_id" ON "IsmsSecurityIncident_affected_assets" (affected_assets_isms_id);

CREATE TABLE "IsmsAuditFinding" (
	finding_type VARCHAR(19) NOT NULL,
	finding_requirement TEXT,
	finding_control TEXT,
	finding_evidence TEXT,
	finding_root_cause TEXT,
	finding_risk TEXT,
	finding_recommendation TEXT,
	finding_auditee_response TEXT,
	finding_corrective_action TEXT,
	finding_closure_status TEXT,
	finding_closure_date DATE,
	isms_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"IsmsAudit_isms_id" TEXT,
	PRIMARY KEY (isms_id),
	FOREIGN KEY(finding_control) REFERENCES "IsmsControl" (isms_id),
	FOREIGN KEY(finding_corrective_action) REFERENCES "IsmsCorrectiveAction" (isms_id),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAuditFinding_isms_id" ON "IsmsAuditFinding" (isms_id);

CREATE TABLE "IsmsObjective_relevant_controls" (
	"IsmsObjective_isms_id" TEXT,
	relevant_controls_isms_id TEXT,
	PRIMARY KEY ("IsmsObjective_isms_id", relevant_controls_isms_id),
	FOREIGN KEY("IsmsObjective_isms_id") REFERENCES "IsmsObjective" (isms_id),
	FOREIGN KEY(relevant_controls_isms_id) REFERENCES "IsmsControl" (isms_id)
);
CREATE INDEX "ix_IsmsObjective_relevant_controls_IsmsObjective_isms_id" ON "IsmsObjective_relevant_controls" ("IsmsObjective_isms_id");
CREATE INDEX "ix_IsmsObjective_relevant_controls_relevant_controls_isms_id" ON "IsmsObjective_relevant_controls" (relevant_controls_isms_id);

CREATE TABLE "IsmsObjective_objective_risks" (
	"IsmsObjective_isms_id" TEXT,
	objective_risks_isms_id TEXT,
	PRIMARY KEY ("IsmsObjective_isms_id", objective_risks_isms_id),
	FOREIGN KEY("IsmsObjective_isms_id") REFERENCES "IsmsObjective" (isms_id),
	FOREIGN KEY(objective_risks_isms_id) REFERENCES "IsmsRisk" (isms_id)
);
CREATE INDEX "ix_IsmsObjective_objective_risks_IsmsObjective_isms_id" ON "IsmsObjective_objective_risks" ("IsmsObjective_isms_id");
CREATE INDEX "ix_IsmsObjective_objective_risks_objective_risks_isms_id" ON "IsmsObjective_objective_risks" (objective_risks_isms_id);

CREATE TABLE "IsmsCompetenceRecord_competence_required" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_required TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_required),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_required_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_required" ("IsmsCompetenceRecord_isms_id");
CREATE INDEX "ix_IsmsCompetenceRecord_competence_required_competence_required" ON "IsmsCompetenceRecord_competence_required" (competence_required);

CREATE TABLE "IsmsCompetenceRecord_competence_education" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_education TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_education),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_education_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_education" ("IsmsCompetenceRecord_isms_id");
CREATE INDEX "ix_IsmsCompetenceRecord_competence_education_competence_education" ON "IsmsCompetenceRecord_competence_education" (competence_education);

CREATE TABLE "IsmsCompetenceRecord_competence_training" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_training TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_training),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_training_competence_training" ON "IsmsCompetenceRecord_competence_training" (competence_training);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_training_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_training" ("IsmsCompetenceRecord_isms_id");

CREATE TABLE "IsmsCompetenceRecord_competence_experience" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_experience TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_experience),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_experience_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_experience" ("IsmsCompetenceRecord_isms_id");
CREATE INDEX "ix_IsmsCompetenceRecord_competence_experience_competence_experience" ON "IsmsCompetenceRecord_competence_experience" (competence_experience);

CREATE TABLE "IsmsCompetenceRecord_competence_gaps" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_gaps TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_gaps),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_gaps_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_gaps" ("IsmsCompetenceRecord_isms_id");
CREATE INDEX "ix_IsmsCompetenceRecord_competence_gaps_competence_gaps" ON "IsmsCompetenceRecord_competence_gaps" (competence_gaps);

CREATE TABLE "IsmsCompetenceRecord_competence_actions" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	competence_actions TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", competence_actions),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_competence_actions_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_competence_actions" ("IsmsCompetenceRecord_isms_id");
CREATE INDEX "ix_IsmsCompetenceRecord_competence_actions_competence_actions" ON "IsmsCompetenceRecord_competence_actions" (competence_actions);

CREATE TABLE "IsmsCompetenceRecord_document_distribution" (
	"IsmsCompetenceRecord_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsCompetenceRecord_isms_id", document_distribution),
	FOREIGN KEY("IsmsCompetenceRecord_isms_id") REFERENCES "IsmsCompetenceRecord" (isms_id)
);
CREATE INDEX "ix_IsmsCompetenceRecord_document_distribution_document_distribution" ON "IsmsCompetenceRecord_document_distribution" (document_distribution);
CREATE INDEX "ix_IsmsCompetenceRecord_document_distribution_IsmsCompetenceRecord_isms_id" ON "IsmsCompetenceRecord_document_distribution" ("IsmsCompetenceRecord_isms_id");

CREATE TABLE "IsmsAuditProgramme_programme_audits" (
	"IsmsAuditProgramme_isms_id" TEXT,
	programme_audits_isms_id TEXT,
	PRIMARY KEY ("IsmsAuditProgramme_isms_id", programme_audits_isms_id),
	FOREIGN KEY("IsmsAuditProgramme_isms_id") REFERENCES "IsmsAuditProgramme" (isms_id),
	FOREIGN KEY(programme_audits_isms_id) REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAuditProgramme_programme_audits_programme_audits_isms_id" ON "IsmsAuditProgramme_programme_audits" (programme_audits_isms_id);
CREATE INDEX "ix_IsmsAuditProgramme_programme_audits_IsmsAuditProgramme_isms_id" ON "IsmsAuditProgramme_programme_audits" ("IsmsAuditProgramme_isms_id");

CREATE TABLE "IsmsAudit_audit_standards" (
	"IsmsAudit_isms_id" TEXT,
	audit_standards VARCHAR(15),
	PRIMARY KEY ("IsmsAudit_isms_id", audit_standards),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_standards_audit_standards" ON "IsmsAudit_audit_standards" (audit_standards);
CREATE INDEX "ix_IsmsAudit_audit_standards_IsmsAudit_isms_id" ON "IsmsAudit_audit_standards" ("IsmsAudit_isms_id");

CREATE TABLE "IsmsAudit_audit_criteria" (
	"IsmsAudit_isms_id" TEXT,
	audit_criteria TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", audit_criteria),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_criteria_audit_criteria" ON "IsmsAudit_audit_criteria" (audit_criteria);
CREATE INDEX "ix_IsmsAudit_audit_criteria_IsmsAudit_isms_id" ON "IsmsAudit_audit_criteria" ("IsmsAudit_isms_id");

CREATE TABLE "IsmsAudit_audit_objectives" (
	"IsmsAudit_isms_id" TEXT,
	audit_objectives TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", audit_objectives),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_objectives_audit_objectives" ON "IsmsAudit_audit_objectives" (audit_objectives);
CREATE INDEX "ix_IsmsAudit_audit_objectives_IsmsAudit_isms_id" ON "IsmsAudit_audit_objectives" ("IsmsAudit_isms_id");

CREATE TABLE "IsmsAudit_audit_team" (
	"IsmsAudit_isms_id" TEXT,
	audit_team TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", audit_team),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_team_IsmsAudit_isms_id" ON "IsmsAudit_audit_team" ("IsmsAudit_isms_id");
CREATE INDEX "ix_IsmsAudit_audit_team_audit_team" ON "IsmsAudit_audit_team" (audit_team);

CREATE TABLE "IsmsAudit_audit_auditees" (
	"IsmsAudit_isms_id" TEXT,
	audit_auditees TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", audit_auditees),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_auditees_IsmsAudit_isms_id" ON "IsmsAudit_audit_auditees" ("IsmsAudit_isms_id");
CREATE INDEX "ix_IsmsAudit_audit_auditees_audit_auditees" ON "IsmsAudit_audit_auditees" (audit_auditees);

CREATE TABLE "IsmsAudit_audit_report_distribution" (
	"IsmsAudit_isms_id" TEXT,
	audit_report_distribution TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", audit_report_distribution),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_audit_report_distribution_IsmsAudit_isms_id" ON "IsmsAudit_audit_report_distribution" ("IsmsAudit_isms_id");
CREATE INDEX "ix_IsmsAudit_audit_report_distribution_audit_report_distribution" ON "IsmsAudit_audit_report_distribution" (audit_report_distribution);

CREATE TABLE "IsmsAudit_document_distribution" (
	"IsmsAudit_isms_id" TEXT,
	document_distribution TEXT,
	PRIMARY KEY ("IsmsAudit_isms_id", document_distribution),
	FOREIGN KEY("IsmsAudit_isms_id") REFERENCES "IsmsAudit" (isms_id)
);
CREATE INDEX "ix_IsmsAudit_document_distribution_IsmsAudit_isms_id" ON "IsmsAudit_document_distribution" ("IsmsAudit_isms_id");
CREATE INDEX "ix_IsmsAudit_document_distribution_document_distribution" ON "IsmsAudit_document_distribution" (document_distribution);

CREATE TABLE "IsmsCorrectiveAction_action_nonconformities" (
	"IsmsCorrectiveAction_isms_id" TEXT,
	action_nonconformities_isms_id TEXT,
	PRIMARY KEY ("IsmsCorrectiveAction_isms_id", action_nonconformities_isms_id),
	FOREIGN KEY("IsmsCorrectiveAction_isms_id") REFERENCES "IsmsCorrectiveAction" (isms_id),
	FOREIGN KEY(action_nonconformities_isms_id) REFERENCES "IsmsNonconformity" (isms_id)
);
CREATE INDEX "ix_IsmsCorrectiveAction_action_nonconformities_action_nonconformities_isms_id" ON "IsmsCorrectiveAction_action_nonconformities" (action_nonconformities_isms_id);
CREATE INDEX "ix_IsmsCorrectiveAction_action_nonconformities_IsmsCorrectiveAction_isms_id" ON "IsmsCorrectiveAction_action_nonconformities" ("IsmsCorrectiveAction_isms_id");
