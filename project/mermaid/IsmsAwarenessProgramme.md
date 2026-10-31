


```mermaid
 classDiagram
    class IsmsAwarenessProgramme
    click IsmsAwarenessProgramme href "../IsmsAwarenessProgramme"
      IsmsRecordMixin <|-- IsmsAwarenessProgramme
        click IsmsRecordMixin href "../IsmsRecordMixin"
      IsmsDocumentControlMixin <|-- IsmsAwarenessProgramme
        click IsmsDocumentControlMixin href "../IsmsDocumentControlMixin"
      
      IsmsAwarenessProgramme : awareness_audience
        
      IsmsAwarenessProgramme : awareness_completion_tracking
        
      IsmsAwarenessProgramme : awareness_effectiveness
        
      IsmsAwarenessProgramme : awareness_frequency
        
      IsmsAwarenessProgramme : awareness_methods
        
      IsmsAwarenessProgramme : awareness_topics
        
      IsmsAwarenessProgramme : description
        
      IsmsAwarenessProgramme : document_approval_date
        
      IsmsAwarenessProgramme : document_approver
        
      IsmsAwarenessProgramme : document_author
        
      IsmsAwarenessProgramme : document_change_control
        
      IsmsAwarenessProgramme : document_classification
        
      IsmsAwarenessProgramme : document_distribution
        
      IsmsAwarenessProgramme : document_effective_date
        
      IsmsAwarenessProgramme : document_external_origin
        
      IsmsAwarenessProgramme : document_external_source
        
      IsmsAwarenessProgramme : document_last_review_date
        
      IsmsAwarenessProgramme : document_next_review_date
        
      IsmsAwarenessProgramme : document_owner
        
      IsmsAwarenessProgramme : document_reference
        
      IsmsAwarenessProgramme : document_retention
        
      IsmsAwarenessProgramme : document_status
        
      IsmsAwarenessProgramme : document_storage
        
      IsmsAwarenessProgramme : document_version
        
      IsmsAwarenessProgramme : isms_id
        
      IsmsAwarenessProgramme : title
        
      
```
