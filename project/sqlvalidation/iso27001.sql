-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.12.1
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'IsmsManagementSystem' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsManagementSystem" 
WHERE "IsmsManagementSystem".isms_id IS NULL

UNION ALL

SELECT 'IsmsManagementSystem' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsManagementSystem" 
WHERE "IsmsManagementSystem".isms_id IN (SELECT isms_id 
FROM "IsmsManagementSystem" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsManagementSystem' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsManagementSystem" 
WHERE "IsmsManagementSystem".title IS NULL

UNION ALL

SELECT 'IsmsManagementSystem' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsManagementSystem" 
WHERE "IsmsManagementSystem".title IS NOT NULL AND "IsmsManagementSystem".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsOrganization' AS table_name, 'organization_employee_count' AS column_name, 'range' AS constraint_type, isms_id AS record_id, organization_employee_count AS invalid_value 
FROM "IsmsOrganization" 
WHERE "IsmsOrganization".organization_employee_count < 1

UNION ALL

SELECT 'IsmsOrganization' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsOrganization" 
WHERE "IsmsOrganization".isms_id IS NULL

UNION ALL

SELECT 'IsmsOrganization' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsOrganization" 
WHERE "IsmsOrganization".isms_id IN (SELECT isms_id 
FROM "IsmsOrganization" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsOrganization' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsOrganization" 
WHERE "IsmsOrganization".title IS NULL

UNION ALL

SELECT 'IsmsOrganization' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsOrganization" 
WHERE "IsmsOrganization".title IS NOT NULL AND "IsmsOrganization".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsInterestedParty' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsInterestedParty" 
WHERE "IsmsInterestedParty".isms_id IS NULL

UNION ALL

SELECT 'IsmsInterestedParty' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsInterestedParty" 
WHERE "IsmsInterestedParty".isms_id IN (SELECT isms_id 
FROM "IsmsInterestedParty" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsInterestedParty' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsInterestedParty" 
WHERE "IsmsInterestedParty".title IS NULL

UNION ALL

SELECT 'IsmsInterestedParty' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsInterestedParty" 
WHERE "IsmsInterestedParty".title IS NOT NULL AND "IsmsInterestedParty".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsPolicy' AS table_name, 'policy_management_systems' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, policy_management_systems AS invalid_value 
FROM "IsmsPolicy" 
WHERE "IsmsPolicy".policy_management_systems IS NOT NULL AND ("IsmsPolicy".policy_management_systems NOT IN ('iso_iec_27001', 'iso_iec_27701', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1'))

UNION ALL

SELECT 'IsmsPolicy' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsPolicy" 
WHERE "IsmsPolicy".isms_id IS NULL

UNION ALL

SELECT 'IsmsPolicy' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsPolicy" 
WHERE "IsmsPolicy".isms_id IN (SELECT isms_id 
FROM "IsmsPolicy" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsPolicy' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsPolicy" 
WHERE "IsmsPolicy".title IS NULL

UNION ALL

SELECT 'IsmsPolicy' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsPolicy" 
WHERE "IsmsPolicy".title IS NOT NULL AND "IsmsPolicy".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsTopicSpecificPolicy' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsTopicSpecificPolicy" 
WHERE "IsmsTopicSpecificPolicy".isms_id IS NULL

UNION ALL

SELECT 'IsmsTopicSpecificPolicy' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsTopicSpecificPolicy" 
WHERE "IsmsTopicSpecificPolicy".isms_id IN (SELECT isms_id 
FROM "IsmsTopicSpecificPolicy" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsTopicSpecificPolicy' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsTopicSpecificPolicy" 
WHERE "IsmsTopicSpecificPolicy".title IS NULL

UNION ALL

SELECT 'IsmsTopicSpecificPolicy' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsTopicSpecificPolicy" 
WHERE "IsmsTopicSpecificPolicy".title IS NOT NULL AND "IsmsTopicSpecificPolicy".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRole' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRole" 
WHERE "IsmsRole".isms_id IS NULL

UNION ALL

SELECT 'IsmsRole' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRole" 
WHERE "IsmsRole".isms_id IN (SELECT isms_id 
FROM "IsmsRole" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRole' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRole" 
WHERE "IsmsRole".title IS NULL

UNION ALL

SELECT 'IsmsRole' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRole" 
WHERE "IsmsRole".title IS NOT NULL AND "IsmsRole".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsObjective' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsObjective" 
WHERE "IsmsObjective".isms_id IS NULL

UNION ALL

SELECT 'IsmsObjective' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsObjective" 
WHERE "IsmsObjective".isms_id IN (SELECT isms_id 
FROM "IsmsObjective" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsObjective' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsObjective" 
WHERE "IsmsObjective".title IS NULL

UNION ALL

SELECT 'IsmsObjective' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsObjective" 
WHERE "IsmsObjective".title IS NOT NULL AND "IsmsObjective".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRiskAssessmentProcess' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskAssessmentProcess" 
WHERE "IsmsRiskAssessmentProcess".isms_id IS NULL

UNION ALL

SELECT 'IsmsRiskAssessmentProcess' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRiskAssessmentProcess" 
WHERE "IsmsRiskAssessmentProcess".isms_id IN (SELECT isms_id 
FROM "IsmsRiskAssessmentProcess" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRiskAssessmentProcess' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskAssessmentProcess" 
WHERE "IsmsRiskAssessmentProcess".title IS NULL

UNION ALL

SELECT 'IsmsRiskAssessmentProcess' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRiskAssessmentProcess" 
WHERE "IsmsRiskAssessmentProcess".title IS NOT NULL AND "IsmsRiskAssessmentProcess".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRiskAssessment' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskAssessment" 
WHERE "IsmsRiskAssessment".isms_id IS NULL

UNION ALL

SELECT 'IsmsRiskAssessment' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRiskAssessment" 
WHERE "IsmsRiskAssessment".isms_id IN (SELECT isms_id 
FROM "IsmsRiskAssessment" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRiskAssessment' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskAssessment" 
WHERE "IsmsRiskAssessment".title IS NULL

UNION ALL

SELECT 'IsmsRiskAssessment' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRiskAssessment" 
WHERE "IsmsRiskAssessment".title IS NOT NULL AND "IsmsRiskAssessment".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'affected_security_properties' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, affected_security_properties AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".affected_security_properties IS NOT NULL AND ("IsmsRisk".affected_security_properties NOT IN ('confidentiality', 'integrity', 'availability'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'risk_likelihood' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, risk_likelihood AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".risk_likelihood IS NOT NULL AND ("IsmsRisk".risk_likelihood NOT IN ('rare', 'unlikely', 'possible', 'likely', 'almost_certain'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'risk_impact' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, risk_impact AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".risk_impact IS NOT NULL AND ("IsmsRisk".risk_impact NOT IN ('negligible', 'minor', 'moderate', 'major', 'severe'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'risk_inherent_level' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, risk_inherent_level AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".risk_inherent_level IS NOT NULL AND ("IsmsRisk".risk_inherent_level NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'risk_residual_level' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, risk_residual_level AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".risk_residual_level IS NOT NULL AND ("IsmsRisk".risk_residual_level NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'risk_treatment_option' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, risk_treatment_option AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".risk_treatment_option IS NOT NULL AND ("IsmsRisk".risk_treatment_option NOT IN ('modify', 'retain', 'avoid', 'share'))

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".isms_id IS NULL

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".isms_id IN (SELECT isms_id 
FROM "IsmsRisk" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".title IS NULL

UNION ALL

SELECT 'IsmsRisk' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRisk" 
WHERE "IsmsRisk".title IS NOT NULL AND "IsmsRisk".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRiskTreatmentProcess' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskTreatmentProcess" 
WHERE "IsmsRiskTreatmentProcess".isms_id IS NULL

UNION ALL

SELECT 'IsmsRiskTreatmentProcess' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRiskTreatmentProcess" 
WHERE "IsmsRiskTreatmentProcess".isms_id IN (SELECT isms_id 
FROM "IsmsRiskTreatmentProcess" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRiskTreatmentProcess' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskTreatmentProcess" 
WHERE "IsmsRiskTreatmentProcess".title IS NULL

UNION ALL

SELECT 'IsmsRiskTreatmentProcess' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRiskTreatmentProcess" 
WHERE "IsmsRiskTreatmentProcess".title IS NOT NULL AND "IsmsRiskTreatmentProcess".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsRiskTreatmentPlan' AS table_name, 'implementation_state' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, implementation_state AS invalid_value 
FROM "IsmsRiskTreatmentPlan" 
WHERE "IsmsRiskTreatmentPlan".implementation_state IS NOT NULL AND ("IsmsRiskTreatmentPlan".implementation_state NOT IN ('not_started', 'planned', 'in_progress', 'implemented'))

UNION ALL

SELECT 'IsmsRiskTreatmentPlan' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskTreatmentPlan" 
WHERE "IsmsRiskTreatmentPlan".isms_id IS NULL

UNION ALL

SELECT 'IsmsRiskTreatmentPlan' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsRiskTreatmentPlan" 
WHERE "IsmsRiskTreatmentPlan".isms_id IN (SELECT isms_id 
FROM "IsmsRiskTreatmentPlan" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsRiskTreatmentPlan' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsRiskTreatmentPlan" 
WHERE "IsmsRiskTreatmentPlan".title IS NULL

UNION ALL

SELECT 'IsmsRiskTreatmentPlan' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsRiskTreatmentPlan" 
WHERE "IsmsRiskTreatmentPlan".title IS NOT NULL AND "IsmsRiskTreatmentPlan".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsStatementOfApplicability' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsStatementOfApplicability" 
WHERE "IsmsStatementOfApplicability".isms_id IS NULL

UNION ALL

SELECT 'IsmsStatementOfApplicability' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsStatementOfApplicability" 
WHERE "IsmsStatementOfApplicability".isms_id IN (SELECT isms_id 
FROM "IsmsStatementOfApplicability" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsStatementOfApplicability' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsStatementOfApplicability" 
WHERE "IsmsStatementOfApplicability".title IS NULL

UNION ALL

SELECT 'IsmsStatementOfApplicability' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsStatementOfApplicability" 
WHERE "IsmsStatementOfApplicability".title IS NOT NULL AND "IsmsStatementOfApplicability".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsIncludedControl' AS table_name, 'implementation_state' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsIncludedControl" 
WHERE "IsmsIncludedControl".implementation_state IS NULL

UNION ALL

SELECT 'IsmsIncludedControl' AS table_name, 'implementation_state' AS column_name, 'enum' AS constraint_type, NULL AS record_id, implementation_state AS invalid_value 
FROM "IsmsIncludedControl" 
WHERE "IsmsIncludedControl".implementation_state IS NOT NULL AND ("IsmsIncludedControl".implementation_state NOT IN ('not_started', 'planned', 'in_progress', 'implemented'))

UNION ALL

SELECT 'IsmsIncludedControl' AS table_name, 'entry_annex_a_control' AS column_name, 'enum' AS constraint_type, NULL AS record_id, entry_annex_a_control AS invalid_value 
FROM "IsmsIncludedControl" 
WHERE "IsmsIncludedControl".entry_annex_a_control IS NOT NULL AND ("IsmsIncludedControl".entry_annex_a_control NOT IN ('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34'))

UNION ALL

SELECT 'IsmsIncludedControl' AS table_name, 'entry_justification' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsIncludedControl" 
WHERE "IsmsIncludedControl".entry_justification IS NULL

UNION ALL

SELECT 'IsmsIncludedControl' AS table_name, 'entry_justification' AS column_name, 'pattern' AS constraint_type, NULL AS record_id, entry_justification AS invalid_value 
FROM "IsmsIncludedControl" 
WHERE "IsmsIncludedControl".entry_justification IS NOT NULL AND "IsmsIncludedControl".entry_justification NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsExcludedControl' AS table_name, 'entry_annex_a_control' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsExcludedControl" 
WHERE "IsmsExcludedControl".entry_annex_a_control IS NULL

UNION ALL

SELECT 'IsmsExcludedControl' AS table_name, 'entry_annex_a_control' AS column_name, 'enum' AS constraint_type, NULL AS record_id, entry_annex_a_control AS invalid_value 
FROM "IsmsExcludedControl" 
WHERE "IsmsExcludedControl".entry_annex_a_control IS NOT NULL AND ("IsmsExcludedControl".entry_annex_a_control NOT IN ('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34'))

UNION ALL

SELECT 'IsmsExcludedControl' AS table_name, 'entry_justification' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsExcludedControl" 
WHERE "IsmsExcludedControl".entry_justification IS NULL

UNION ALL

SELECT 'IsmsExcludedControl' AS table_name, 'entry_justification' AS column_name, 'pattern' AS constraint_type, NULL AS record_id, entry_justification AS invalid_value 
FROM "IsmsExcludedControl" 
WHERE "IsmsExcludedControl".entry_justification IS NOT NULL AND "IsmsExcludedControl".entry_justification NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsControl' AS table_name, 'implementation_state' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, implementation_state AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".implementation_state IS NOT NULL AND ("IsmsControl".implementation_state NOT IN ('not_started', 'planned', 'in_progress', 'implemented'))

UNION ALL

SELECT 'IsmsControl' AS table_name, 'control_annex_a_controls' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, control_annex_a_controls AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".control_annex_a_controls IS NOT NULL AND ("IsmsControl".control_annex_a_controls NOT IN ('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34'))

UNION ALL

SELECT 'IsmsControl' AS table_name, 'control_theme' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, control_theme AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".control_theme IS NOT NULL AND ("IsmsControl".control_theme NOT IN ('organizational', 'people', 'physical', 'technological'))

UNION ALL

SELECT 'IsmsControl' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".isms_id IS NULL

UNION ALL

SELECT 'IsmsControl' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".isms_id IN (SELECT isms_id 
FROM "IsmsControl" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsControl' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".title IS NULL

UNION ALL

SELECT 'IsmsControl' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsControl" 
WHERE "IsmsControl".title IS NOT NULL AND "IsmsControl".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsAsset' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAsset" 
WHERE "IsmsAsset".isms_id IS NULL

UNION ALL

SELECT 'IsmsAsset' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsAsset" 
WHERE "IsmsAsset".isms_id IN (SELECT isms_id 
FROM "IsmsAsset" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsAsset' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAsset" 
WHERE "IsmsAsset".title IS NULL

UNION ALL

SELECT 'IsmsAsset' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsAsset" 
WHERE "IsmsAsset".title IS NOT NULL AND "IsmsAsset".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsResource' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsResource" 
WHERE "IsmsResource".isms_id IS NULL

UNION ALL

SELECT 'IsmsResource' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsResource" 
WHERE "IsmsResource".isms_id IN (SELECT isms_id 
FROM "IsmsResource" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsResource' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsResource" 
WHERE "IsmsResource".title IS NULL

UNION ALL

SELECT 'IsmsResource' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsResource" 
WHERE "IsmsResource".title IS NOT NULL AND "IsmsResource".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsCompetenceRecord' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCompetenceRecord" 
WHERE "IsmsCompetenceRecord".isms_id IS NULL

UNION ALL

SELECT 'IsmsCompetenceRecord' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsCompetenceRecord" 
WHERE "IsmsCompetenceRecord".isms_id IN (SELECT isms_id 
FROM "IsmsCompetenceRecord" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsCompetenceRecord' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCompetenceRecord" 
WHERE "IsmsCompetenceRecord".title IS NULL

UNION ALL

SELECT 'IsmsCompetenceRecord' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsCompetenceRecord" 
WHERE "IsmsCompetenceRecord".title IS NOT NULL AND "IsmsCompetenceRecord".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsAwarenessProgramme' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAwarenessProgramme" 
WHERE "IsmsAwarenessProgramme".isms_id IS NULL

UNION ALL

SELECT 'IsmsAwarenessProgramme' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsAwarenessProgramme" 
WHERE "IsmsAwarenessProgramme".isms_id IN (SELECT isms_id 
FROM "IsmsAwarenessProgramme" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsAwarenessProgramme' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAwarenessProgramme" 
WHERE "IsmsAwarenessProgramme".title IS NULL

UNION ALL

SELECT 'IsmsAwarenessProgramme' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsAwarenessProgramme" 
WHERE "IsmsAwarenessProgramme".title IS NOT NULL AND "IsmsAwarenessProgramme".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsCommunicationPlan' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCommunicationPlan" 
WHERE "IsmsCommunicationPlan".isms_id IS NULL

UNION ALL

SELECT 'IsmsCommunicationPlan' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsCommunicationPlan" 
WHERE "IsmsCommunicationPlan".isms_id IN (SELECT isms_id 
FROM "IsmsCommunicationPlan" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsCommunicationPlan' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCommunicationPlan" 
WHERE "IsmsCommunicationPlan".title IS NULL

UNION ALL

SELECT 'IsmsCommunicationPlan' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsCommunicationPlan" 
WHERE "IsmsCommunicationPlan".title IS NOT NULL AND "IsmsCommunicationPlan".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsCommunication' AS table_name, 'communication_subject' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsCommunication" 
WHERE "IsmsCommunication".communication_subject IS NULL

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'document_kind' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".document_kind IS NULL

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'document_kind' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, document_kind AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".document_kind IS NOT NULL AND ("IsmsDocumentedInformation".document_kind NOT IN ('procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".isms_id IS NULL

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".isms_id IN (SELECT isms_id 
FROM "IsmsDocumentedInformation" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".title IS NULL

UNION ALL

SELECT 'IsmsDocumentedInformation' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsDocumentedInformation" 
WHERE "IsmsDocumentedInformation".title IS NOT NULL AND "IsmsDocumentedInformation".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsOperationalProcedure' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsOperationalProcedure" 
WHERE "IsmsOperationalProcedure".isms_id IS NULL

UNION ALL

SELECT 'IsmsOperationalProcedure' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsOperationalProcedure" 
WHERE "IsmsOperationalProcedure".isms_id IN (SELECT isms_id 
FROM "IsmsOperationalProcedure" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsOperationalProcedure' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsOperationalProcedure" 
WHERE "IsmsOperationalProcedure".title IS NULL

UNION ALL

SELECT 'IsmsOperationalProcedure' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsOperationalProcedure" 
WHERE "IsmsOperationalProcedure".title IS NOT NULL AND "IsmsOperationalProcedure".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsMonitoringProgramme' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsMonitoringProgramme" 
WHERE "IsmsMonitoringProgramme".isms_id IS NULL

UNION ALL

SELECT 'IsmsMonitoringProgramme' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsMonitoringProgramme" 
WHERE "IsmsMonitoringProgramme".isms_id IN (SELECT isms_id 
FROM "IsmsMonitoringProgramme" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsMonitoringProgramme' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsMonitoringProgramme" 
WHERE "IsmsMonitoringProgramme".title IS NULL

UNION ALL

SELECT 'IsmsMonitoringProgramme' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsMonitoringProgramme" 
WHERE "IsmsMonitoringProgramme".title IS NOT NULL AND "IsmsMonitoringProgramme".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsMonitoringItem' AS table_name, 'monitoring_metric' AS column_name, 'required' AS constraint_type, NULL AS record_id, NULL AS invalid_value 
FROM "IsmsMonitoringItem" 
WHERE "IsmsMonitoringItem".monitoring_metric IS NULL

UNION ALL

SELECT 'IsmsAuditProgramme' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAuditProgramme" 
WHERE "IsmsAuditProgramme".isms_id IS NULL

UNION ALL

SELECT 'IsmsAuditProgramme' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsAuditProgramme" 
WHERE "IsmsAuditProgramme".isms_id IN (SELECT isms_id 
FROM "IsmsAuditProgramme" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsAuditProgramme' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAuditProgramme" 
WHERE "IsmsAuditProgramme".title IS NULL

UNION ALL

SELECT 'IsmsAuditProgramme' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsAuditProgramme" 
WHERE "IsmsAuditProgramme".title IS NOT NULL AND "IsmsAuditProgramme".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'audit_type' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".audit_type IS NULL

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'audit_type' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, audit_type AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".audit_type IS NOT NULL AND ("IsmsAudit".audit_type NOT IN ('first_party', 'second_party', 'third_party'))

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'audit_standards' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, audit_standards AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".audit_standards IS NOT NULL AND ("IsmsAudit".audit_standards NOT IN ('iso_iec_27001', 'iso_iec_27701', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1'))

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".isms_id IS NULL

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".isms_id IN (SELECT isms_id 
FROM "IsmsAudit" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".title IS NULL

UNION ALL

SELECT 'IsmsAudit' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsAudit" 
WHERE "IsmsAudit".title IS NOT NULL AND "IsmsAudit".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'finding_type' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".finding_type IS NULL

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'finding_type' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, finding_type AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".finding_type IS NOT NULL AND ("IsmsAuditFinding".finding_type NOT IN ('major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding'))

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".isms_id IS NULL

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".isms_id IN (SELECT isms_id 
FROM "IsmsAuditFinding" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".title IS NULL

UNION ALL

SELECT 'IsmsAuditFinding' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsAuditFinding" 
WHERE "IsmsAuditFinding".title IS NOT NULL AND "IsmsAuditFinding".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsManagementReview' AS table_name, 'review_held_on' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsManagementReview" 
WHERE "IsmsManagementReview".review_held_on IS NULL

UNION ALL

SELECT 'IsmsManagementReview' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsManagementReview" 
WHERE "IsmsManagementReview".isms_id IS NULL

UNION ALL

SELECT 'IsmsManagementReview' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsManagementReview" 
WHERE "IsmsManagementReview".isms_id IN (SELECT isms_id 
FROM "IsmsManagementReview" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsManagementReview' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsManagementReview" 
WHERE "IsmsManagementReview".title IS NULL

UNION ALL

SELECT 'IsmsManagementReview' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsManagementReview" 
WHERE "IsmsManagementReview".title IS NOT NULL AND "IsmsManagementReview".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsNonconformity' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsNonconformity" 
WHERE "IsmsNonconformity".isms_id IS NULL

UNION ALL

SELECT 'IsmsNonconformity' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsNonconformity" 
WHERE "IsmsNonconformity".isms_id IN (SELECT isms_id 
FROM "IsmsNonconformity" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsNonconformity' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsNonconformity" 
WHERE "IsmsNonconformity".title IS NULL

UNION ALL

SELECT 'IsmsNonconformity' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsNonconformity" 
WHERE "IsmsNonconformity".title IS NOT NULL AND "IsmsNonconformity".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsCorrectiveAction' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCorrectiveAction" 
WHERE "IsmsCorrectiveAction".isms_id IS NULL

UNION ALL

SELECT 'IsmsCorrectiveAction' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsCorrectiveAction" 
WHERE "IsmsCorrectiveAction".isms_id IN (SELECT isms_id 
FROM "IsmsCorrectiveAction" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsCorrectiveAction' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsCorrectiveAction" 
WHERE "IsmsCorrectiveAction".title IS NULL

UNION ALL

SELECT 'IsmsCorrectiveAction' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsCorrectiveAction" 
WHERE "IsmsCorrectiveAction".title IS NOT NULL AND "IsmsCorrectiveAction".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsImprovementOpportunity' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsImprovementOpportunity" 
WHERE "IsmsImprovementOpportunity".isms_id IS NULL

UNION ALL

SELECT 'IsmsImprovementOpportunity' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsImprovementOpportunity" 
WHERE "IsmsImprovementOpportunity".isms_id IN (SELECT isms_id 
FROM "IsmsImprovementOpportunity" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsImprovementOpportunity' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsImprovementOpportunity" 
WHERE "IsmsImprovementOpportunity".title IS NULL

UNION ALL

SELECT 'IsmsImprovementOpportunity' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsImprovementOpportunity" 
WHERE "IsmsImprovementOpportunity".title IS NOT NULL AND "IsmsImprovementOpportunity".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsSecurityEvent' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsSecurityEvent" 
WHERE "IsmsSecurityEvent".isms_id IS NULL

UNION ALL

SELECT 'IsmsSecurityEvent' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsSecurityEvent" 
WHERE "IsmsSecurityEvent".isms_id IN (SELECT isms_id 
FROM "IsmsSecurityEvent" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsSecurityEvent' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsSecurityEvent" 
WHERE "IsmsSecurityEvent".title IS NULL

UNION ALL

SELECT 'IsmsSecurityEvent' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsSecurityEvent" 
WHERE "IsmsSecurityEvent".title IS NOT NULL AND "IsmsSecurityEvent".title NOT REGEXP '^\s*\S'

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'affected_security_properties' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, affected_security_properties AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".affected_security_properties IS NOT NULL AND ("IsmsSecurityIncident".affected_security_properties NOT IN ('confidentiality', 'integrity', 'availability'))

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'incident_category' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, incident_category AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".incident_category IS NOT NULL AND ("IsmsSecurityIncident".incident_category NOT IN ('malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other'))

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'incident_severity' AS column_name, 'enum' AS constraint_type, isms_id AS record_id, incident_severity AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".incident_severity IS NOT NULL AND ("IsmsSecurityIncident".incident_severity NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'isms_id' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".isms_id IS NULL

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'isms_id' AS column_name, 'identifier' AS constraint_type, isms_id AS record_id, isms_id AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".isms_id IN (SELECT isms_id 
FROM "IsmsSecurityIncident" GROUP BY isms_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'title' AS column_name, 'required' AS constraint_type, isms_id AS record_id, NULL AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".title IS NULL

UNION ALL

SELECT 'IsmsSecurityIncident' AS table_name, 'title' AS column_name, 'pattern' AS constraint_type, isms_id AS record_id, title AS invalid_value 
FROM "IsmsSecurityIncident" 
WHERE "IsmsSecurityIncident".title IS NOT NULL AND "IsmsSecurityIncident".title NOT REGEXP '^\s*\S';

