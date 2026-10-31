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
  An audit of the ISMS: an internal audit, or an audit by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsAudit  {

  private String auditType;
  private List<String> auditStandards;
  private String auditScope;
  private List<String> auditCriteria;
  private List<String> auditObjectives;
  private LocalDate auditPeriodStart;
  private LocalDate auditPeriodEnd;
  private String auditLead;
  private List<String> auditTeam;
  private List<String> auditAuditees;
  private IsmsDocumentedInformation auditPlan;
  private List<IsmsAuditFinding> auditFindings;
  private String auditConclusion;
  private LocalDate auditReportDate;
  private List<String> auditReportDistribution;
  private URI ismsId;
  private String title;
  private String description;
  private String documentReference;
  private String documentVersion;
  private String documentAuthor;
  private String documentOwner;
  private String documentApprover;
  private LocalDate documentApprovalDate;
  private LocalDate documentEffectiveDate;
  private LocalDate documentLastReviewDate;
  private LocalDate documentNextReviewDate;
  private String documentStatus;
  private String documentClassification;
  private String documentRetention;
  private List<String> documentDistribution;
  private String documentStorage;
  private String documentChangeControl;
  private Boolean documentExternalOrigin;
  private String documentExternalSource;


}