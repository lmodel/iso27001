


```mermaid
 classDiagram
    class IsmsRole
    click IsmsRole href "../IsmsRole"
      IsmsRecord <|-- IsmsRole
        click IsmsRecord href "../IsmsRecord"
      
      IsmsRole : description
        
      IsmsRole : isms_id
        
      IsmsRole : role_accountability
        
      IsmsRole : role_authorities
        
      IsmsRole : role_category
        
      IsmsRole : role_delegation
        
      IsmsRole : role_holders
        
      IsmsRole : role_reports_to
        
          
    
        
        
        IsmsRole --> "0..1" IsmsRole : role_reports_to
        click IsmsRole href "../IsmsRole"
    

        
      IsmsRole : role_responsibilities
        
      IsmsRole : title
        
      
```
