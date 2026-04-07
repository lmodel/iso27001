package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An information asset or associated asset requiring protection, per Annex A control 5.9.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Asset extends NamedEntity {

  private String assetType;
  private String assetOwner;
  private String assetCustodian;
  private String classification;
  private String location;
  private String criticality;
  private List<Risk> relatedRisks;
  private List<SecurityControl> applicableControls;

}