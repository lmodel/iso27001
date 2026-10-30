


```mermaid
 classDiagram
    class IsmsApplicabilityEntry
    click IsmsApplicabilityEntry href "../IsmsApplicabilityEntry"
      IsmsApplicabilityEntry <|-- IsmsIncludedControl
        click IsmsIncludedControl href "../IsmsIncludedControl"
      IsmsApplicabilityEntry <|-- IsmsExcludedControl
        click IsmsExcludedControl href "../IsmsExcludedControl"
      
      IsmsApplicabilityEntry : entry_annex_a_control
        
          
    
        
        
        IsmsApplicabilityEntry --> "0..1" IsmsAnnexAControl : entry_annex_a_control
        click IsmsAnnexAControl href "../IsmsAnnexAControl"
    

        
      IsmsApplicabilityEntry : entry_justification
        
      IsmsApplicabilityEntry : entry_type
        
      
```
