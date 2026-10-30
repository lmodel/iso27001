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
  An internal audit programme: the audits planned over a period, how often and why, and the resources and auditors they need.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsAuditProgramme extends IsmsRecord {

  private String programmePeriod;
  private List<IsmsAudit> programmeAudits;
  private String programmeFrequencyRationale;
  private String programmeResources;
  private String programmeAuditorQualifications;
  private String programmeStatus;
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