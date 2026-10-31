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
  A person or organization whose needs and expectations bear on the ISMS, inside the organization or outside it, such as staff, customers, regulators or suppliers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsInterestedParty  {

  private String partyCategory;
  private String partyRelationship;
  private List<String> partyRequirements;
  private List<String> partyAddressedRequirements;
  private List<String> partyClimateChangeRequirements;
  private String partyCommunicationNeeds;
  private String partyContact;
  private URI ismsId;
  private String title;
  private String description;


}