


```mermaid
 classDiagram
    class StatementOfApplicability
    click StatementOfApplicability href "../StatementOfApplicability"
      DocumentedInformation <|-- StatementOfApplicability
        click DocumentedInformation href "../DocumentedInformation"
      
      StatementOfApplicability : approved_by
        
      StatementOfApplicability : approved_date
        
      StatementOfApplicability : author
        
      StatementOfApplicability : change_control_method
        
      StatementOfApplicability : classification
        
      StatementOfApplicability : created_date
        
      StatementOfApplicability : description
        
      StatementOfApplicability : distribution_controls
        
      StatementOfApplicability : document_reference
        
      StatementOfApplicability : document_type
        
          
    
        
        
        StatementOfApplicability --> "0..1" DocumentType : document_type
        click DocumentType href "../DocumentType"
    

        
      StatementOfApplicability : effective_date
        
      StatementOfApplicability : external_origin
        
      StatementOfApplicability : external_origin_source
        
      StatementOfApplicability : id
        
      StatementOfApplicability : implemented_count
        
      StatementOfApplicability : last_review_date
        
      StatementOfApplicability : modified_date
        
      StatementOfApplicability : name
        
      StatementOfApplicability : not_applicable_count
        
      StatementOfApplicability : owner
        
      StatementOfApplicability : planned_count
        
      StatementOfApplicability : retention_period
        
      StatementOfApplicability : review_date
        
      StatementOfApplicability : soa_entries
        
          
    
        
        
        StatementOfApplicability --> "*" SoAEntry : soa_entries
        click SoAEntry href "../SoAEntry"
    

        
      StatementOfApplicability : status
        
      StatementOfApplicability : storage_and_preservation
        
      StatementOfApplicability : total_controls
        
      StatementOfApplicability : version
        
      
```
