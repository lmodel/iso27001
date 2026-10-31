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
  An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsCorrectiveAction  {

  private IsmsRole responsibleRole;
  private List<IsmsNonconformity> actionNonconformities;
  private String actionRootCause;
  private LocalDate actionTargetDate;
  private LocalDate actionCompletionDate;
  private String actionResources;
  private String actionEffectivenessCriteria;
  private LocalDate actionEffectivenessReviewDate;
  private Boolean actionEffective;
  private String actionIsmsChanges;
  private String actionStatus;
  private URI ismsId;
  private String title;
  private String description;


}