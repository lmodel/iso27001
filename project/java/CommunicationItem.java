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
  A single communication requirement within the communication plan.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CommunicationItem  {

  private String subject;
  private String purpose;
  private String audience;
  private String frequency;
  private String method;
  private String responsibleParty;
  private Boolean recordsRequired;


}