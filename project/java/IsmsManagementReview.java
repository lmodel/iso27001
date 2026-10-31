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
  A review of the ISMS by top management: what it considered, what it decided and what it asked to be done.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsManagementReview  {

  private LocalDate reviewHeldOn;
  private List<String> reviewAttendees;
  private String reviewPreviousActions;
  private String reviewContextChanges;
  private String reviewInterestedPartyChanges;
  private String reviewInterestedPartyFeedback;
  private String reviewPerformanceTrends;
  private String reviewAuditResults;
  private String reviewRiskAssessmentResults;
  private String reviewRiskTreatmentStatus;
  private String reviewRisksAndOpportunities;
  private List<String> reviewImprovementOpportunities;
  private List<String> reviewDecisions;
  private List<String> reviewActions;
  private LocalDate reviewNextDate;
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