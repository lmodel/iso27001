


```mermaid
 classDiagram
    class IsmsRiskAssessmentProcess
    click IsmsRiskAssessmentProcess href "../IsmsRiskAssessmentProcess"
      IsmsRecordMixin <|-- IsmsRiskAssessmentProcess
        click IsmsRecordMixin href "../IsmsRecordMixin"
      IsmsDocumentControlMixin <|-- IsmsRiskAssessmentProcess
        click IsmsDocumentControlMixin href "../IsmsDocumentControlMixin"
      
      IsmsRiskAssessmentProcess : description
        
      IsmsRiskAssessmentProcess : document_approval_date
        
      IsmsRiskAssessmentProcess : document_approver
        
      IsmsRiskAssessmentProcess : document_author
        
      IsmsRiskAssessmentProcess : document_change_control
        
      IsmsRiskAssessmentProcess : document_classification
        
      IsmsRiskAssessmentProcess : document_distribution
        
      IsmsRiskAssessmentProcess : document_effective_date
        
      IsmsRiskAssessmentProcess : document_external_origin
        
      IsmsRiskAssessmentProcess : document_external_source
        
      IsmsRiskAssessmentProcess : document_last_review_date
        
      IsmsRiskAssessmentProcess : document_next_review_date
        
      IsmsRiskAssessmentProcess : document_owner
        
      IsmsRiskAssessmentProcess : document_reference
        
      IsmsRiskAssessmentProcess : document_retention
        
      IsmsRiskAssessmentProcess : document_status
        
      IsmsRiskAssessmentProcess : document_storage
        
      IsmsRiskAssessmentProcess : document_version
        
      IsmsRiskAssessmentProcess : isms_id
        
      IsmsRiskAssessmentProcess : risk_acceptance_criteria
        
      IsmsRiskAssessmentProcess : risk_assessment_criteria
        
      IsmsRiskAssessmentProcess : risk_assessment_frequency
        
      IsmsRiskAssessmentProcess : risk_assessment_method
        
      IsmsRiskAssessmentProcess : risk_assessment_triggers
        
      IsmsRiskAssessmentProcess : risk_impact_scale
        
      IsmsRiskAssessmentProcess : risk_likelihood_scale
        
      IsmsRiskAssessmentProcess : risk_matrix
        
      IsmsRiskAssessmentProcess : title
        
      
```
