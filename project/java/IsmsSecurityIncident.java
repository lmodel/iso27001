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
  An information security event assessed as an incident: its category and severity, how it was detected, contained, eradicated and recovered from, the evidence collected, who was told, and what was learned.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsSecurityIncident extends IsmsSecurityEvent {

  private List<String> affectedSecurityProperties;
  private String incidentCategory;
  private String incidentSeverity;
  private String incidentDetectionMethod;
  private List<String> incidentResponseActions;
  private List<String> incidentContainmentActions;
  private List<String> incidentEradicationActions;
  private List<String> incidentRecoveryActions;
  private String incidentRootCause;
  private List<String> incidentLessonsLearned;
  private List<String> incidentEvidence;
  private Boolean incidentNotificationRequired;
  private List<String> incidentNotifications;
  private ZonedDateTime incidentClosedAt;
  private String incidentReview;


}