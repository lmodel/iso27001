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
  A plan to treat one or more risks: the actions and controls, who carries them out and when, and the risk owner's approval of the plan and of the residual risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsRiskTreatmentPlan  {

  private String implementationState;
  private String planScope;
  private List<IsmsRisk> planRisks;
  private List<String> planActions;
  private List<IsmsControl> planControls;
  private String planResources;
  private List<String> planResponsibleParties;
  private String planTimeline;
  private String planRiskOwnerApproval;
  private String planResidualRiskAcceptance;
  private LocalDate planCompletionDate;
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