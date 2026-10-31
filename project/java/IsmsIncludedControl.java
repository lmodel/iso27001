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
  An entry that includes a control the organization needs, from Annex A or from elsewhere, and says whether it is in place.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsIncludedControl extends IsmsApplicabilityEntry {

  private String implementationState;
  private IsmsRole responsibleRole;
  private IsmsControl includedControl;
  private String includedEvidence;
  private LocalDate includedTargetDate;


}