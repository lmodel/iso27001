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
  A management review per Clause 9.3, conducted by top management to evaluate ongoing ISMS performance and fitness for purpose.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ManagementReview extends DocumentedInformation {

  private List<String> attendees;
  private String previousActionsStatus;
  private String contextChanges;
  private String interestedPartyChanges;
  private String interestedPartyFeedback;
  private String performanceTrends;
  private String auditResultsSummary;
  private String riskAssessmentResults;
  private String riskTreatmentStatus;
  private String risksAndOpportunitiesChanges;
  private List<String> improvementOpportunities;
  private List<String> decisions;
  private List<String> actionItems;
  private LocalDate nextReviewDate;


}