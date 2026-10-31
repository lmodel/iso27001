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
  One organization's information security management system: its scope and context, and every record it keeps, each kind in a list of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsManagementSystem  {

  private IsmsOrganization ismsOrganization;
  private String ismsTopManagement;
  private String ismsGoverningBody;
  private List<String> ismsLeadershipEvidence;
  private String ismsScope;
  private List<String> ismsScopeBoundaries;
  private List<String> ismsScopeExclusions;
  private List<String> ismsInterfaces;
  private String ismsProcesses;
  private List<String> ismsInternalIssues;
  private List<String> ismsExternalIssues;
  private List<String> ismsRiskAndOpportunityActions;
  private List<String> ismsPlannedChanges;
  private List<String> ismsExternalServices;
  private String ismsCertificationStatus;
  private String ismsCertificationBody;
  private LocalDate ismsCertificationDate;
  private LocalDate ismsRecertificationDate;
  private List<IsmsInterestedParty> ismsInterestedParties;
  private IsmsPolicy ismsPolicy;
  private List<IsmsTopicSpecificPolicy> ismsTopicSpecificPolicies;
  private List<IsmsRole> ismsRoles;
  private List<IsmsObjective> ismsObjectives;
  private IsmsRiskAssessmentProcess ismsRiskAssessmentProcess;
  private IsmsRiskTreatmentProcess ismsRiskTreatmentProcess;
  private List<IsmsRiskAssessment> ismsRiskAssessments;
  private List<IsmsRisk> ismsRisks;
  private List<IsmsRiskTreatmentPlan> ismsRiskTreatmentPlans;
  private IsmsStatementOfApplicability ismsStatementOfApplicability;
  private List<IsmsControl> ismsControls;
  private List<IsmsAsset> ismsAssets;
  private List<IsmsResource> ismsResources;
  private List<IsmsCompetenceRecord> ismsCompetenceRecords;
  private IsmsAwarenessProgramme ismsAwarenessProgramme;
  private IsmsCommunicationPlan ismsCommunicationPlan;
  private List<IsmsDocumentedInformation> ismsDocumentedInformation;
  private List<IsmsOperationalProcedure> ismsOperationalProcedures;
  private IsmsMonitoringProgramme ismsMonitoringProgramme;
  private List<IsmsAuditProgramme> ismsAuditProgrammes;
  private List<IsmsAudit> ismsAudits;
  private List<IsmsManagementReview> ismsManagementReviews;
  private List<IsmsNonconformity> ismsNonconformities;
  private List<IsmsCorrectiveAction> ismsCorrectiveActions;
  private List<IsmsImprovementOpportunity> ismsImprovements;
  private List<IsmsSecurityEvent> ismsSecurityEvents;
  private URI ismsId;
  private String title;
  private String description;


}