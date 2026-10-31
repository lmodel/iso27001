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
  The organization's process for treating information security risks: how it chooses treatments and controls, checks them against Annex A, and produces the Statement of Applicability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsRiskTreatmentProcess  {

  private String treatmentOptionsGuidance;
  private String treatmentControlSelection;
  private String treatmentAnnexAComparison;
  private String treatmentSoaTemplate;
  private String treatmentApprovalWorkflow;
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