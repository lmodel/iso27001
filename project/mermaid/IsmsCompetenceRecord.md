


```mermaid
 classDiagram
    class IsmsCompetenceRecord
    click IsmsCompetenceRecord href "../IsmsCompetenceRecord"
      IsmsRecordMixin <|-- IsmsCompetenceRecord
        click IsmsRecordMixin href "../IsmsRecordMixin"
      IsmsDocumentControlMixin <|-- IsmsCompetenceRecord
        click IsmsDocumentControlMixin href "../IsmsDocumentControlMixin"
      
      IsmsCompetenceRecord : competence_actions
        
      IsmsCompetenceRecord : competence_assessment_date
        
      IsmsCompetenceRecord : competence_education
        
      IsmsCompetenceRecord : competence_experience
        
      IsmsCompetenceRecord : competence_gaps
        
      IsmsCompetenceRecord : competence_person
        
      IsmsCompetenceRecord : competence_required
        
      IsmsCompetenceRecord : competence_role
        
          
    
        
        
        IsmsCompetenceRecord --> "0..1" IsmsRole : competence_role
        click IsmsRole href "../IsmsRole"
    

        
      IsmsCompetenceRecord : competence_training
        
      IsmsCompetenceRecord : description
        
      IsmsCompetenceRecord : document_approval_date
        
      IsmsCompetenceRecord : document_approver
        
      IsmsCompetenceRecord : document_author
        
      IsmsCompetenceRecord : document_change_control
        
      IsmsCompetenceRecord : document_classification
        
      IsmsCompetenceRecord : document_distribution
        
      IsmsCompetenceRecord : document_effective_date
        
      IsmsCompetenceRecord : document_external_origin
        
      IsmsCompetenceRecord : document_external_source
        
      IsmsCompetenceRecord : document_last_review_date
        
      IsmsCompetenceRecord : document_next_review_date
        
      IsmsCompetenceRecord : document_owner
        
      IsmsCompetenceRecord : document_reference
        
      IsmsCompetenceRecord : document_retention
        
      IsmsCompetenceRecord : document_status
        
      IsmsCompetenceRecord : document_storage
        
      IsmsCompetenceRecord : document_version
        
      IsmsCompetenceRecord : isms_id
        
      IsmsCompetenceRecord : title
        
      
```
