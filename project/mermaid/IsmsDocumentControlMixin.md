


```mermaid
 classDiagram
    class IsmsDocumentControlMixin
    click IsmsDocumentControlMixin href "../IsmsDocumentControlMixin"
      IsmsDocumentControlMixin <|-- IsmsPolicy
        click IsmsPolicy href "../IsmsPolicy"
      IsmsDocumentControlMixin <|-- IsmsTopicSpecificPolicy
        click IsmsTopicSpecificPolicy href "../IsmsTopicSpecificPolicy"
      IsmsDocumentControlMixin <|-- IsmsRiskAssessmentProcess
        click IsmsRiskAssessmentProcess href "../IsmsRiskAssessmentProcess"
      IsmsDocumentControlMixin <|-- IsmsRiskAssessment
        click IsmsRiskAssessment href "../IsmsRiskAssessment"
      IsmsDocumentControlMixin <|-- IsmsRiskTreatmentProcess
        click IsmsRiskTreatmentProcess href "../IsmsRiskTreatmentProcess"
      IsmsDocumentControlMixin <|-- IsmsRiskTreatmentPlan
        click IsmsRiskTreatmentPlan href "../IsmsRiskTreatmentPlan"
      IsmsDocumentControlMixin <|-- IsmsStatementOfApplicability
        click IsmsStatementOfApplicability href "../IsmsStatementOfApplicability"
      IsmsDocumentControlMixin <|-- IsmsCompetenceRecord
        click IsmsCompetenceRecord href "../IsmsCompetenceRecord"
      IsmsDocumentControlMixin <|-- IsmsAwarenessProgramme
        click IsmsAwarenessProgramme href "../IsmsAwarenessProgramme"
      IsmsDocumentControlMixin <|-- IsmsCommunicationPlan
        click IsmsCommunicationPlan href "../IsmsCommunicationPlan"
      IsmsDocumentControlMixin <|-- IsmsDocumentedInformation
        click IsmsDocumentedInformation href "../IsmsDocumentedInformation"
      IsmsDocumentControlMixin <|-- IsmsOperationalProcedure
        click IsmsOperationalProcedure href "../IsmsOperationalProcedure"
      IsmsDocumentControlMixin <|-- IsmsMonitoringProgramme
        click IsmsMonitoringProgramme href "../IsmsMonitoringProgramme"
      IsmsDocumentControlMixin <|-- IsmsAuditProgramme
        click IsmsAuditProgramme href "../IsmsAuditProgramme"
      IsmsDocumentControlMixin <|-- IsmsAudit
        click IsmsAudit href "../IsmsAudit"
      IsmsDocumentControlMixin <|-- IsmsManagementReview
        click IsmsManagementReview href "../IsmsManagementReview"
      
      IsmsDocumentControlMixin : document_approval_date
        
      IsmsDocumentControlMixin : document_approver
        
      IsmsDocumentControlMixin : document_author
        
      IsmsDocumentControlMixin : document_change_control
        
      IsmsDocumentControlMixin : document_classification
        
      IsmsDocumentControlMixin : document_distribution
        
      IsmsDocumentControlMixin : document_effective_date
        
      IsmsDocumentControlMixin : document_external_origin
        
      IsmsDocumentControlMixin : document_external_source
        
      IsmsDocumentControlMixin : document_last_review_date
        
      IsmsDocumentControlMixin : document_next_review_date
        
      IsmsDocumentControlMixin : document_owner
        
      IsmsDocumentControlMixin : document_reference
        
      IsmsDocumentControlMixin : document_retention
        
      IsmsDocumentControlMixin : document_status
        
      IsmsDocumentControlMixin : document_storage
        
      IsmsDocumentControlMixin : document_version
        
      
```
