package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The internal audit programme per 9.2.2, planning audit activities over a defined period.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuditProgramme extends DocumentedInformation {

  private String programmePeriod;
  private List<InternalAudit> plannedAudits;
  private String auditFrequencyRationale;
  private String resourceRequirements;
  private String auditorQualifications;
  private String programmeStatus;

}