package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A management review per Clause 9.3, conducted by top management to ensure ISMS suitability, adequacy, and effectiveness.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ManagementReview extends DocumentedInformation {

  private List<String> attendees;
  private String previousActionsStatus;
  private String contextChanges;
  private String interestedPartyChanges;
  private String performanceTrends;
  private String auditResultsSummary;
  private String riskAssessmentResults;
  private List<String> improvementOpportunities;
  private List<String> decisions;
  private List<String> actionItems;
  private LocalDate nextReviewDate;

}