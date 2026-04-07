package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An information security incident per A.5.26, requiring response per documented procedures.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationSecurityIncident extends NamedEntity {

  private ZonedDateTime incidentDatetime;
  private String incidentCategory;
  private String severity;
  private List<Asset> affectedAssets;
  private List<String> affectedCia;
  private String incidentDescription;
  private String detectionMethod;
  private List<String> responseActions;
  private List<String> containmentActions;
  private List<String> eradicationActions;
  private List<String> recoveryActions;
  private String rootCause;
  private String lessonsLearned;
  private List<String> evidenceCollected;
  private boolean notificationRequired;
  private List<String> notificationsMade;
  private ZonedDateTime closureDatetime;
  private String postIncidentReview;

}