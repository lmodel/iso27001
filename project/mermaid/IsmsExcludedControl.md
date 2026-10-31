


```mermaid
 classDiagram
    class IsmsExcludedControl
    click IsmsExcludedControl href "../IsmsExcludedControl"
      IsmsApplicabilityEntry <|-- IsmsExcludedControl
        click IsmsApplicabilityEntry href "../IsmsApplicabilityEntry"
      
      IsmsExcludedControl : entry_annex_a_control
        
          
    
        
        
        IsmsExcludedControl --> "1" IsmsAnnexAControl : entry_annex_a_control
        click IsmsAnnexAControl href "../IsmsAnnexAControl"
    

        
      IsmsExcludedControl : entry_justification
        
      IsmsExcludedControl : entry_type
        
      
```
