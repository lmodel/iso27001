package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A nonconformity identified per Clause 10.2, representing failure to fulfill a requirement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Nonconformity extends NamedEntity {

  private String nonconformitySource;
  private LocalDate detectionDate;
  private String detectedBy;
  private String requirementViolated;
  private String nonconformityDescription;
  private List<String> immediateActions;
  private String consequencesAddressed;
  private String rootCause;
  private String similarNonconformitiesCheck;
  private List<CorrectiveAction> linkedCorrectiveActions;
  private String status;
  private LocalDate closureDate;
  private String closureEvidence;

}