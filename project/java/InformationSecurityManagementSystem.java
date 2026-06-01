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
  Top-level container representing an organization's complete ISMS per ISO 27001. Aggregates all components required to support the full ISMS lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationSecurityManagementSystem extends NamedEntity {

  private Organization organization;
  private String topManagement;
  private String governingBody;
  private List<String> leadershipCommitmentEvidence;
  private String scopeStatement;
  private List<String> scopeBoundaries;
  private List<String> scopeExclusions;
  private List<String> interfacesAndDependencies;
  private String processesAndInteractions;
  private List<String> contextInternalIssues;
  private List<String> contextExternalIssues;
  private List<InterestedParty> interestedParties;
  private InformationSecurityPolicy informationSecurityPolicy;
  private List<InformationSecurityObjective> objectives;
  private List<String> risksAndOpportunitiesActions;
  private List<String> plannedChanges;
  private List<String> externallyProvidedServices;
  private RiskAssessmentProcess riskAssessmentProcess;
  private RiskTreatmentProcess riskTreatmentProcess;
  private StatementOfApplicability statementOfApplicability;
  private List<SecurityControl> controls;
  private List<Role> roles;
  private List<Resource> resources;
  private List<CompetenceRecord> competenceRecords;
  private AwarenessProgram awarenessProgram;
  private CommunicationPlan communicationPlan;
  private List<DocumentedInformation> documentedInformationRegister;
  private List<OperationalProcedure> operationalProcedures;
  private List<RiskAssessment> riskAssessments;
  private List<RiskTreatmentPlan> riskTreatmentPlans;
  private MonitoringProgram monitoringProgram;
  private List<InternalAudit> internalAudits;
  private List<ManagementReview> managementReviews;
  private List<Nonconformity> nonconformities;
  private List<CorrectiveAction> correctiveActions;
  private List<ImprovementOpportunity> improvements;
  private String certificationStatus;
  private String certificationBody;
  private LocalDate certificationDate;
  private LocalDate recertificationDate;


}