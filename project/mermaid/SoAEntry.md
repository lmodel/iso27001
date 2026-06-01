


```mermaid
 classDiagram
    class SoAEntry
    click SoAEntry href "../SoAEntry"
      SoAEntry : control_reference
        
          
    
        
        
        SoAEntry --> "0..1" SecurityControl : control_reference
        click SecurityControl href "../SecurityControl"
    

        
      SoAEntry : exclusion_justification
        
      SoAEntry : implementation_evidence
        
      SoAEntry : implementation_status
        
          
    
        
        
        SoAEntry --> "0..1" ImplementationStatus : implementation_status
        click ImplementationStatus href "../ImplementationStatus"
    

        
      SoAEntry : inclusion_justification
        
      SoAEntry : is_applicable
        
      SoAEntry : responsible_role
        
          
    
        
        
        SoAEntry --> "0..1" Role : responsible_role
        click Role href "../Role"
    

        
      SoAEntry : target_implementation_date
        
      
```
