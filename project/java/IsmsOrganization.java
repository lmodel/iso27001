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
  The organization that runs the ISMS, with what it needs to know about itself to understand its context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsOrganization  {

  private String organizationLegalName;
  private List<String> organizationTradingNames;
  private String organizationKind;
  private String organizationSector;
  private String organizationSize;
  private Integer organizationEmployeeCount;
  private List<String> organizationLocations;
  private List<String> organizationJurisdictions;
  private String organizationParent;
  private List<String> organizationSubsidiaries;
  private Boolean organizationClimateChangeRelevant;
  private URI ismsId;
  private String title;
  private String description;


}