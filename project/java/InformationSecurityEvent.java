package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An information security event per A.5.25, which may or may not be categorized as an incident.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationSecurityEvent extends NamedEntity {

  private ZonedDateTime eventDatetime;
  private String reporter;
  private String eventDescription;
  private List<Asset> affectedAssets;
  private String initialAssessment;
  private Boolean categorizedAsIncident;
  private InformationSecurityIncident linkedIncident;


}