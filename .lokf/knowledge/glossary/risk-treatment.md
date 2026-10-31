---
type: GlossaryTerm
id: https://w3id.org/lmodel/iso27001/knowledge/glossary/risk-treatment
genre: reference
title: Risk treatment
description: "Choosing and carrying out how to deal with an information security risk: modify it with controls, retain it, avoid it or share it; the schema records the choice on `IsmsRisk` and the work in `IsmsRiskTreatmentPlan`."
definition: "Choosing and carrying out a way of dealing with a risk: modifying, retaining, avoiding or sharing it."
resource: src/iso27001/schema/iso27001.yaml
relatedTo:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: iso27001.yaml
    resource: src/iso27001/schema/iso27001.yaml
    title: the classes IsmsRisk, IsmsRiskTreatmentPlan and IsmsRiskTreatmentProcess, and the enum IsmsRiskTreatmentOption
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Risk treatment

Risk treatment is how an organization deals with a risk it has assessed. The schema offers four options in `IsmsRiskTreatmentOption`, by the names ISO/IEC 27005 gives them: modify the risk with controls, retain it, avoid it, or share it with another party. A risk records the option chosen in `risk_treatment_option`, and an `IsmsRiskTreatmentPlan` records the risks it treats, the actions and controls, who carries them out and when, and the risk owner's approval. `IsmsRiskTreatmentProcess` records how treatments are chosen.[^iso27001.yaml]

[^iso27001.yaml]: src/iso27001/schema/iso27001.yaml, the classes IsmsRisk, IsmsRiskTreatmentPlan and IsmsRiskTreatmentProcess, and the enum IsmsRiskTreatmentOption
