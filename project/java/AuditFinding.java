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
  A finding from an internal audit, including nonconformities, observations, and positive findings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuditFinding extends NamedEntity {

  private String findingType;
  private String clauseReference;
  private SecurityControl controlReference;
  private String findingDescription;
  private String objectiveEvidence;
  private String rootCauseAnalysis;
  private String riskImplication;
  private String recommendedAction;
  private String auditeeResponse;
  private CorrectiveAction linkedCorrectiveAction;
  private String closureStatus;
  private LocalDate closureDate;


}