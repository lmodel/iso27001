


```mermaid
 classDiagram
    class IsmsSecurityEvent
    click IsmsSecurityEvent href "../IsmsSecurityEvent"
      IsmsRecord <|-- IsmsSecurityEvent
        click IsmsRecord href "../IsmsRecord"
      

      IsmsSecurityEvent <|-- IsmsSecurityIncident
        click IsmsSecurityIncident href "../IsmsSecurityIncident"
      

      IsmsSecurityEvent : affected_assets
        
          
    
        
        
        IsmsSecurityEvent --> "*" IsmsAsset : affected_assets
        click IsmsAsset href "../IsmsAsset"
    

        
      IsmsSecurityEvent : description
        
      IsmsSecurityEvent : event_assessment
        
      IsmsSecurityEvent : event_occurred_at
        
      IsmsSecurityEvent : event_reporter
        
      IsmsSecurityEvent : event_type
        
      IsmsSecurityEvent : isms_id
        
      IsmsSecurityEvent : title
        
      
```
