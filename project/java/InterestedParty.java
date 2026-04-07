package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A stakeholder whose needs and expectations are relevant to the ISMS per 4.2. Includes internal parties (employees, management) and external parties (customers, regulators, suppliers).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InterestedParty extends NamedEntity {

  private String partyType;
  private String relationship;
  private List<String> requirements;
  private String communicationNeeds;
  private String contactInformation;

}