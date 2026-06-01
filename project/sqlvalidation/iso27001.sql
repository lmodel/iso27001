-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.11.1
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'InformationSecurityManagementSystem' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityManagementSystem" 
WHERE "InformationSecurityManagementSystem".id IS NULL

UNION ALL

SELECT 'InformationSecurityManagementSystem' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InformationSecurityManagementSystem" 
WHERE "InformationSecurityManagementSystem".id IN (SELECT id 
FROM "InformationSecurityManagementSystem" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InformationSecurityManagementSystem' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityManagementSystem" 
WHERE "InformationSecurityManagementSystem".name IS NULL

UNION ALL

SELECT 'Organization' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Organization" 
WHERE "Organization".id IS NULL

UNION ALL

SELECT 'Organization' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Organization" 
WHERE "Organization".id IN (SELECT id 
FROM "Organization" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Organization' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Organization" 
WHERE "Organization".name IS NULL

UNION ALL

SELECT 'InterestedParty' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InterestedParty" 
WHERE "InterestedParty".id IS NULL

UNION ALL

SELECT 'InterestedParty' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InterestedParty" 
WHERE "InterestedParty".id IN (SELECT id 
FROM "InterestedParty" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InterestedParty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InterestedParty" 
WHERE "InterestedParty".name IS NULL

UNION ALL

SELECT 'InformationSecurityPolicy' AS table_name, 'integrated_management_systems' AS column_name, 'enum' AS constraint_type, id AS record_id, integrated_management_systems AS invalid_value 
FROM "InformationSecurityPolicy" 
WHERE "InformationSecurityPolicy".integrated_management_systems IS NOT NULL AND ("InformationSecurityPolicy".integrated_management_systems NOT IN ('iso_iec_27001', 'iso_iec_27701', 'iso_iec_27017', 'iso_iec_27018', 'iso_iec_42001', 'iso_9001', 'iso_14001', 'iso_22301', 'iso_iec_20000_1', 'iso_31000'))

UNION ALL

SELECT 'InformationSecurityPolicy' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "InformationSecurityPolicy" 
WHERE "InformationSecurityPolicy".document_type IS NOT NULL AND ("InformationSecurityPolicy".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'InformationSecurityPolicy' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityPolicy" 
WHERE "InformationSecurityPolicy".id IS NULL

UNION ALL

SELECT 'InformationSecurityPolicy' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InformationSecurityPolicy" 
WHERE "InformationSecurityPolicy".id IN (SELECT id 
FROM "InformationSecurityPolicy" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InformationSecurityPolicy' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityPolicy" 
WHERE "InformationSecurityPolicy".name IS NULL

UNION ALL

SELECT 'TopicSpecificPolicy' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "TopicSpecificPolicy" 
WHERE "TopicSpecificPolicy".document_type IS NOT NULL AND ("TopicSpecificPolicy".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'TopicSpecificPolicy' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TopicSpecificPolicy" 
WHERE "TopicSpecificPolicy".id IS NULL

UNION ALL

SELECT 'TopicSpecificPolicy' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "TopicSpecificPolicy" 
WHERE "TopicSpecificPolicy".id IN (SELECT id 
FROM "TopicSpecificPolicy" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'TopicSpecificPolicy' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TopicSpecificPolicy" 
WHERE "TopicSpecificPolicy".name IS NULL

UNION ALL

SELECT 'Role' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Role" 
WHERE "Role".id IS NULL

UNION ALL

SELECT 'Role' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Role" 
WHERE "Role".id IN (SELECT id 
FROM "Role" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Role' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Role" 
WHERE "Role".name IS NULL

UNION ALL

SELECT 'InformationSecurityObjective' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityObjective" 
WHERE "InformationSecurityObjective".id IS NULL

UNION ALL

SELECT 'InformationSecurityObjective' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InformationSecurityObjective" 
WHERE "InformationSecurityObjective".id IN (SELECT id 
FROM "InformationSecurityObjective" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InformationSecurityObjective' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityObjective" 
WHERE "InformationSecurityObjective".name IS NULL

UNION ALL

SELECT 'RiskAssessmentProcess' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "RiskAssessmentProcess" 
WHERE "RiskAssessmentProcess".document_type IS NOT NULL AND ("RiskAssessmentProcess".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'RiskAssessmentProcess' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskAssessmentProcess" 
WHERE "RiskAssessmentProcess".id IS NULL

UNION ALL

SELECT 'RiskAssessmentProcess' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RiskAssessmentProcess" 
WHERE "RiskAssessmentProcess".id IN (SELECT id 
FROM "RiskAssessmentProcess" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RiskAssessmentProcess' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskAssessmentProcess" 
WHERE "RiskAssessmentProcess".name IS NULL

UNION ALL

SELECT 'RiskAssessment' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "RiskAssessment" 
WHERE "RiskAssessment".document_type IS NOT NULL AND ("RiskAssessment".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'RiskAssessment' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskAssessment" 
WHERE "RiskAssessment".id IS NULL

UNION ALL

SELECT 'RiskAssessment' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RiskAssessment" 
WHERE "RiskAssessment".id IN (SELECT id 
FROM "RiskAssessment" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RiskAssessment' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskAssessment" 
WHERE "RiskAssessment".name IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'affected_cia_properties' AS column_name, 'enum' AS constraint_type, id AS record_id, affected_cia_properties AS invalid_value 
FROM "Risk" 
WHERE "Risk".affected_cia_properties IS NOT NULL AND ("Risk".affected_cia_properties NOT IN ('confidentiality', 'integrity', 'availability'))

UNION ALL

SELECT 'Risk' AS table_name, 'likelihood' AS column_name, 'enum' AS constraint_type, id AS record_id, likelihood AS invalid_value 
FROM "Risk" 
WHERE "Risk".likelihood IS NOT NULL AND ("Risk".likelihood NOT IN ('rare', 'unlikely', 'possible', 'likely', 'almost_certain'))

UNION ALL

SELECT 'Risk' AS table_name, 'impact' AS column_name, 'enum' AS constraint_type, id AS record_id, impact AS invalid_value 
FROM "Risk" 
WHERE "Risk".impact IS NOT NULL AND ("Risk".impact NOT IN ('negligible', 'minor', 'moderate', 'major', 'severe'))

UNION ALL

SELECT 'Risk' AS table_name, 'inherent_risk_level' AS column_name, 'enum' AS constraint_type, id AS record_id, inherent_risk_level AS invalid_value 
FROM "Risk" 
WHERE "Risk".inherent_risk_level IS NOT NULL AND ("Risk".inherent_risk_level NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'Risk' AS table_name, 'residual_risk_level' AS column_name, 'enum' AS constraint_type, id AS record_id, residual_risk_level AS invalid_value 
FROM "Risk" 
WHERE "Risk".residual_risk_level IS NOT NULL AND ("Risk".residual_risk_level NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'Risk' AS table_name, 'risk_treatment_option' AS column_name, 'enum' AS constraint_type, id AS record_id, risk_treatment_option AS invalid_value 
FROM "Risk" 
WHERE "Risk".risk_treatment_option IS NOT NULL AND ("Risk".risk_treatment_option NOT IN ('modify', 'accept', 'avoid', 'share'))

UNION ALL

SELECT 'Risk' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".id IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Risk" 
WHERE "Risk".id IN (SELECT id 
FROM "Risk" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Risk' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".name IS NULL

UNION ALL

SELECT 'RiskTreatmentProcess' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "RiskTreatmentProcess" 
WHERE "RiskTreatmentProcess".document_type IS NOT NULL AND ("RiskTreatmentProcess".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'RiskTreatmentProcess' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskTreatmentProcess" 
WHERE "RiskTreatmentProcess".id IS NULL

UNION ALL

SELECT 'RiskTreatmentProcess' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RiskTreatmentProcess" 
WHERE "RiskTreatmentProcess".id IN (SELECT id 
FROM "RiskTreatmentProcess" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RiskTreatmentProcess' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskTreatmentProcess" 
WHERE "RiskTreatmentProcess".name IS NULL

UNION ALL

SELECT 'RiskTreatmentPlan' AS table_name, 'implementation_status' AS column_name, 'enum' AS constraint_type, id AS record_id, implementation_status AS invalid_value 
FROM "RiskTreatmentPlan" 
WHERE "RiskTreatmentPlan".implementation_status IS NOT NULL AND ("RiskTreatmentPlan".implementation_status NOT IN ('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable'))

UNION ALL

SELECT 'RiskTreatmentPlan' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "RiskTreatmentPlan" 
WHERE "RiskTreatmentPlan".document_type IS NOT NULL AND ("RiskTreatmentPlan".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'RiskTreatmentPlan' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskTreatmentPlan" 
WHERE "RiskTreatmentPlan".id IS NULL

UNION ALL

SELECT 'RiskTreatmentPlan' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RiskTreatmentPlan" 
WHERE "RiskTreatmentPlan".id IN (SELECT id 
FROM "RiskTreatmentPlan" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RiskTreatmentPlan' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskTreatmentPlan" 
WHERE "RiskTreatmentPlan".name IS NULL

UNION ALL

SELECT 'StatementOfApplicability' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "StatementOfApplicability" 
WHERE "StatementOfApplicability".document_type IS NOT NULL AND ("StatementOfApplicability".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'StatementOfApplicability' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "StatementOfApplicability" 
WHERE "StatementOfApplicability".id IS NULL

UNION ALL

SELECT 'StatementOfApplicability' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "StatementOfApplicability" 
WHERE "StatementOfApplicability".id IN (SELECT id 
FROM "StatementOfApplicability" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'StatementOfApplicability' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "StatementOfApplicability" 
WHERE "StatementOfApplicability".name IS NULL

UNION ALL

SELECT 'SoAEntry' AS table_name, 'implementation_status' AS column_name, 'enum' AS constraint_type, id AS record_id, implementation_status AS invalid_value 
FROM "SoAEntry" 
WHERE "SoAEntry".implementation_status IS NOT NULL AND ("SoAEntry".implementation_status NOT IN ('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable'))

UNION ALL

SELECT 'SecurityControl' AS table_name, 'control_id' AS column_name, 'enum' AS constraint_type, id AS record_id, control_id AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".control_id IS NOT NULL AND ("SecurityControl".control_id NOT IN ('a_5_1', 'a_5_2', 'a_5_3', 'a_5_4', 'a_5_5', 'a_5_6', 'a_5_7', 'a_5_8', 'a_5_9', 'a_5_10', 'a_5_11', 'a_5_12', 'a_5_13', 'a_5_14', 'a_5_15', 'a_5_16', 'a_5_17', 'a_5_18', 'a_5_19', 'a_5_20', 'a_5_21', 'a_5_22', 'a_5_23', 'a_5_24', 'a_5_25', 'a_5_26', 'a_5_27', 'a_5_28', 'a_5_29', 'a_5_30', 'a_5_31', 'a_5_32', 'a_5_33', 'a_5_34', 'a_5_35', 'a_5_36', 'a_5_37', 'a_6_1', 'a_6_2', 'a_6_3', 'a_6_4', 'a_6_5', 'a_6_6', 'a_6_7', 'a_6_8', 'a_7_1', 'a_7_2', 'a_7_3', 'a_7_4', 'a_7_5', 'a_7_6', 'a_7_7', 'a_7_8', 'a_7_9', 'a_7_10', 'a_7_11', 'a_7_12', 'a_7_13', 'a_7_14', 'a_8_1', 'a_8_2', 'a_8_3', 'a_8_4', 'a_8_5', 'a_8_6', 'a_8_7', 'a_8_8', 'a_8_9', 'a_8_10', 'a_8_11', 'a_8_12', 'a_8_13', 'a_8_14', 'a_8_15', 'a_8_16', 'a_8_17', 'a_8_18', 'a_8_19', 'a_8_20', 'a_8_21', 'a_8_22', 'a_8_23', 'a_8_24', 'a_8_25', 'a_8_26', 'a_8_27', 'a_8_28', 'a_8_29', 'a_8_30', 'a_8_31', 'a_8_32', 'a_8_33', 'a_8_34'))

UNION ALL

SELECT 'SecurityControl' AS table_name, 'control_category' AS column_name, 'enum' AS constraint_type, id AS record_id, control_category AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".control_category IS NOT NULL AND ("SecurityControl".control_category NOT IN ('organizational', 'people', 'physical', 'technological'))

UNION ALL

SELECT 'SecurityControl' AS table_name, 'implementation_status' AS column_name, 'enum' AS constraint_type, id AS record_id, implementation_status AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".implementation_status IS NOT NULL AND ("SecurityControl".implementation_status NOT IN ('not_started', 'planned', 'in_progress', 'implemented', 'not_applicable'))

UNION ALL

SELECT 'SecurityControl' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".id IS NULL

UNION ALL

SELECT 'SecurityControl' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".id IN (SELECT id 
FROM "SecurityControl" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'SecurityControl' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SecurityControl" 
WHERE "SecurityControl".name IS NULL

UNION ALL

SELECT 'Resource' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Resource" 
WHERE "Resource".id IS NULL

UNION ALL

SELECT 'Resource' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Resource" 
WHERE "Resource".id IN (SELECT id 
FROM "Resource" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Resource' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Resource" 
WHERE "Resource".name IS NULL

UNION ALL

SELECT 'CompetenceRecord' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "CompetenceRecord" 
WHERE "CompetenceRecord".document_type IS NOT NULL AND ("CompetenceRecord".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'CompetenceRecord' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CompetenceRecord" 
WHERE "CompetenceRecord".id IS NULL

UNION ALL

SELECT 'CompetenceRecord' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "CompetenceRecord" 
WHERE "CompetenceRecord".id IN (SELECT id 
FROM "CompetenceRecord" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'CompetenceRecord' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CompetenceRecord" 
WHERE "CompetenceRecord".name IS NULL

UNION ALL

SELECT 'AwarenessProgram' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "AwarenessProgram" 
WHERE "AwarenessProgram".document_type IS NOT NULL AND ("AwarenessProgram".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'AwarenessProgram' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AwarenessProgram" 
WHERE "AwarenessProgram".id IS NULL

UNION ALL

SELECT 'AwarenessProgram' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "AwarenessProgram" 
WHERE "AwarenessProgram".id IN (SELECT id 
FROM "AwarenessProgram" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'AwarenessProgram' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AwarenessProgram" 
WHERE "AwarenessProgram".name IS NULL

UNION ALL

SELECT 'CommunicationPlan' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "CommunicationPlan" 
WHERE "CommunicationPlan".document_type IS NOT NULL AND ("CommunicationPlan".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'CommunicationPlan' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CommunicationPlan" 
WHERE "CommunicationPlan".id IS NULL

UNION ALL

SELECT 'CommunicationPlan' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "CommunicationPlan" 
WHERE "CommunicationPlan".id IN (SELECT id 
FROM "CommunicationPlan" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'CommunicationPlan' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CommunicationPlan" 
WHERE "CommunicationPlan".name IS NULL

UNION ALL

SELECT 'OperationalProcedure' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "OperationalProcedure" 
WHERE "OperationalProcedure".document_type IS NOT NULL AND ("OperationalProcedure".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'OperationalProcedure' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "OperationalProcedure" 
WHERE "OperationalProcedure".id IS NULL

UNION ALL

SELECT 'OperationalProcedure' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "OperationalProcedure" 
WHERE "OperationalProcedure".id IN (SELECT id 
FROM "OperationalProcedure" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'OperationalProcedure' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "OperationalProcedure" 
WHERE "OperationalProcedure".name IS NULL

UNION ALL

SELECT 'MonitoringProgram' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "MonitoringProgram" 
WHERE "MonitoringProgram".document_type IS NOT NULL AND ("MonitoringProgram".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'MonitoringProgram' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MonitoringProgram" 
WHERE "MonitoringProgram".id IS NULL

UNION ALL

SELECT 'MonitoringProgram' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "MonitoringProgram" 
WHERE "MonitoringProgram".id IN (SELECT id 
FROM "MonitoringProgram" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'MonitoringProgram' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MonitoringProgram" 
WHERE "MonitoringProgram".name IS NULL

UNION ALL

SELECT 'InternalAudit' AS table_name, 'audit_type' AS column_name, 'enum' AS constraint_type, id AS record_id, audit_type AS invalid_value 
FROM "InternalAudit" 
WHERE "InternalAudit".audit_type IS NOT NULL AND ("InternalAudit".audit_type NOT IN ('internal', 'external_second_party', 'external_third_party', 'surveillance', 'recertification', 'combined'))

UNION ALL

SELECT 'InternalAudit' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "InternalAudit" 
WHERE "InternalAudit".document_type IS NOT NULL AND ("InternalAudit".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'InternalAudit' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InternalAudit" 
WHERE "InternalAudit".id IS NULL

UNION ALL

SELECT 'InternalAudit' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InternalAudit" 
WHERE "InternalAudit".id IN (SELECT id 
FROM "InternalAudit" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InternalAudit' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InternalAudit" 
WHERE "InternalAudit".name IS NULL

UNION ALL

SELECT 'AuditProgramme' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "AuditProgramme" 
WHERE "AuditProgramme".document_type IS NOT NULL AND ("AuditProgramme".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'AuditProgramme' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuditProgramme" 
WHERE "AuditProgramme".id IS NULL

UNION ALL

SELECT 'AuditProgramme' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "AuditProgramme" 
WHERE "AuditProgramme".id IN (SELECT id 
FROM "AuditProgramme" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'AuditProgramme' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuditProgramme" 
WHERE "AuditProgramme".name IS NULL

UNION ALL

SELECT 'AuditFinding' AS table_name, 'finding_type' AS column_name, 'enum' AS constraint_type, id AS record_id, finding_type AS invalid_value 
FROM "AuditFinding" 
WHERE "AuditFinding".finding_type IS NOT NULL AND ("AuditFinding".finding_type NOT IN ('major_nonconformity', 'minor_nonconformity', 'observation', 'positive_finding'))

UNION ALL

SELECT 'AuditFinding' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuditFinding" 
WHERE "AuditFinding".id IS NULL

UNION ALL

SELECT 'AuditFinding' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "AuditFinding" 
WHERE "AuditFinding".id IN (SELECT id 
FROM "AuditFinding" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'AuditFinding' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuditFinding" 
WHERE "AuditFinding".name IS NULL

UNION ALL

SELECT 'ManagementReview' AS table_name, 'document_type' AS column_name, 'enum' AS constraint_type, id AS record_id, document_type AS invalid_value 
FROM "ManagementReview" 
WHERE "ManagementReview".document_type IS NOT NULL AND ("ManagementReview".document_type NOT IN ('policy', 'procedure', 'standard', 'guideline', 'record', 'plan', 'report'))

UNION ALL

SELECT 'ManagementReview' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ManagementReview" 
WHERE "ManagementReview".id IS NULL

UNION ALL

SELECT 'ManagementReview' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ManagementReview" 
WHERE "ManagementReview".id IN (SELECT id 
FROM "ManagementReview" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ManagementReview' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ManagementReview" 
WHERE "ManagementReview".name IS NULL

UNION ALL

SELECT 'Nonconformity' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Nonconformity" 
WHERE "Nonconformity".id IS NULL

UNION ALL

SELECT 'Nonconformity' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Nonconformity" 
WHERE "Nonconformity".id IN (SELECT id 
FROM "Nonconformity" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Nonconformity' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Nonconformity" 
WHERE "Nonconformity".name IS NULL

UNION ALL

SELECT 'CorrectiveAction' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CorrectiveAction" 
WHERE "CorrectiveAction".id IS NULL

UNION ALL

SELECT 'CorrectiveAction' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "CorrectiveAction" 
WHERE "CorrectiveAction".id IN (SELECT id 
FROM "CorrectiveAction" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'CorrectiveAction' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CorrectiveAction" 
WHERE "CorrectiveAction".name IS NULL

UNION ALL

SELECT 'ImprovementOpportunity' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImprovementOpportunity" 
WHERE "ImprovementOpportunity".id IS NULL

UNION ALL

SELECT 'ImprovementOpportunity' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ImprovementOpportunity" 
WHERE "ImprovementOpportunity".id IN (SELECT id 
FROM "ImprovementOpportunity" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ImprovementOpportunity' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImprovementOpportunity" 
WHERE "ImprovementOpportunity".name IS NULL

UNION ALL

SELECT 'Asset' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Asset" 
WHERE "Asset".id IS NULL

UNION ALL

SELECT 'Asset' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "Asset" 
WHERE "Asset".id IN (SELECT id 
FROM "Asset" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Asset' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Asset" 
WHERE "Asset".name IS NULL

UNION ALL

SELECT 'InformationSecurityEvent' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityEvent" 
WHERE "InformationSecurityEvent".id IS NULL

UNION ALL

SELECT 'InformationSecurityEvent' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InformationSecurityEvent" 
WHERE "InformationSecurityEvent".id IN (SELECT id 
FROM "InformationSecurityEvent" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InformationSecurityEvent' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityEvent" 
WHERE "InformationSecurityEvent".name IS NULL

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'incident_category' AS column_name, 'enum' AS constraint_type, id AS record_id, incident_category AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".incident_category IS NOT NULL AND ("InformationSecurityIncident".incident_category NOT IN ('malware', 'ransomware', 'phishing', 'social_engineering', 'unauthorized_access', 'account_compromise', 'privilege_misuse', 'data_breach', 'data_loss', 'denial_of_service', 'web_application_attack', 'supply_chain', 'insider_threat', 'physical_security', 'configuration_error', 'cryptographic_failure', 'policy_violation', 'other'))

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'severity' AS column_name, 'enum' AS constraint_type, id AS record_id, severity AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".severity IS NOT NULL AND ("InformationSecurityIncident".severity NOT IN ('very_low', 'low', 'medium', 'high', 'critical'))

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'affected_cia' AS column_name, 'enum' AS constraint_type, id AS record_id, affected_cia AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".affected_cia IS NOT NULL AND ("InformationSecurityIncident".affected_cia NOT IN ('confidentiality', 'integrity', 'availability'))

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".id IS NULL

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".id IN (SELECT id 
FROM "InformationSecurityIncident" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InformationSecurityIncident' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationSecurityIncident" 
WHERE "InformationSecurityIncident".name IS NULL;

