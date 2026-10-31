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
  One communication the plan provides for: what about, why, to whom, how often, how, and who communicates.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsCommunication  {

  private IsmsRole responsibleRole;
  private String communicationSubject;
  private String communicationPurpose;
  private String communicationAudience;
  private String communicationFrequency;
  private String communicationMethod;
  private Boolean communicationRecordsRequired;


}