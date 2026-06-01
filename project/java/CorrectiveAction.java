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
  A corrective action per Clause 10.2 to address the root cause of a nonconformity and reduce the likelihood of recurrence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CorrectiveAction extends NamedEntity {

  private Nonconformity linkedNonconformity;
  private String actionDescription;
  private String rootCauseAddressed;
  private String responsibleParty;
  private LocalDate targetCompletionDate;
  private LocalDate actualCompletionDate;
  private String resourcesRequired;
  private String effectivenessCriteria;
  private LocalDate effectivenessReviewDate;
  private Boolean effectivenessVerified;
  private String ismsChangesRequired;
  private String status;


}