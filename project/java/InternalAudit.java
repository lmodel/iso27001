package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An internal audit instance per Clause 9.2, assessing ISMS conformance and effectiveness.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InternalAudit extends DocumentedInformation {

  private String auditReference;
  private String auditType;
  private String auditScope;
  private List<String> auditCriteria;
  private List<String> auditObjectives;
  private LocalDate auditPeriodStart;
  private LocalDate auditPeriodEnd;
  private String leadAuditor;
  private List<String> auditTeam;
  private List<String> auditeeRepresentatives;
  private String auditPlan;
  private List<AuditFinding> findings;
  private List<String> positiveObservations;
  private String auditConclusion;
  private LocalDate reportDate;
  private List<String> reportDistribution;

}