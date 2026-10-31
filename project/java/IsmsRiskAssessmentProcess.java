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
  The organization's process for assessing information security risks: its criteria for accepting risk and for assessing it, its scales and method, and when it runs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsRiskAssessmentProcess  {

  private String riskAcceptanceCriteria;
  private String riskAssessmentCriteria;
  private String riskAssessmentMethod;
  private String riskLikelihoodScale;
  private String riskImpactScale;
  private String riskMatrix;
  private String riskAssessmentFrequency;
  private List<String> riskAssessmentTriggers;
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