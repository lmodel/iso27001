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
  The organization establishing and operating the ISMS. Captures context needed for Clause 4.1 (understanding the organization).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organization extends NamedEntity {

  private String legalName;
  private List<String> tradingNames;
  private String organizationType;
  private String industrySector;
  private String sizeCategory;
  private String employeeCount;
  private List<String> geographicLocations;
  private List<String> regulatoryJurisdictions;
  private String parentOrganization;
  private List<String> subsidiaries;
  private Boolean climateChangeRelevant;


}