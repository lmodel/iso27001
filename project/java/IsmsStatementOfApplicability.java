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
  The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each Annex A control it leaves out, with why.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsStatementOfApplicability  {

  private List<IsmsApplicabilityEntry> soaEntries;
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