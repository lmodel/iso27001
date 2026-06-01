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
  Plan for internal and external communications relevant to the ISMS per Clause 7.4.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CommunicationPlan extends DocumentedInformation {

  private List<CommunicationItem> communicationItems;


}