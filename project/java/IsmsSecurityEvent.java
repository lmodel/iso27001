package example;

/* metamodel_version: 1.12.0 */
/* version: 2022/Amd 1:2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An information security event someone reported, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an IsmsSecurityIncident.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsSecurityEvent  {

  private List<IsmsAsset> affectedAssets;
  private String eventType;
  private ZonedDateTime eventOccurredAt;
  private String eventReporter;
  private String eventAssessment;
  private URI ismsId;
  private String title;
  private String description;


}