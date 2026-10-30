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
  A role in the ISMS, with the responsibilities and authorities it carries and who holds it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsRole extends IsmsRecord {

  private String roleCategory;
  private List<String> roleResponsibilities;
  private List<String> roleAuthorities;
  private String roleAccountability;
  private List<String> roleHolders;
  private String roleDelegation;
  private IsmsRole roleReportsTo;


}