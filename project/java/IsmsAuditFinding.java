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
  One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsAuditFinding extends IsmsRecord {

  private String findingType;
  private String findingRequirement;
  private IsmsControl findingControl;
  private String findingEvidence;
  private String findingRootCause;
  private String findingRisk;
  private String findingRecommendation;
  private String findingAuditeeResponse;
  private IsmsCorrectiveAction findingCorrectiveAction;
  private String findingClosureStatus;
  private LocalDate findingClosureDate;


}