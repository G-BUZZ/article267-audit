# Article 267 Audit — Coding Manual v0.1

## 1. Purpose

This manual defines the coding rules for the Article 267 audit pilot corpus.

The purpose of the coding scheme is to distinguish:

1. whether an issue raises a question concerning EU law;
2. whether the national court made a preliminary reference;
3. where no reference was made, which non-referral ground was relied upon;
4. the extent and character of the court's substantive EU-law analysis;
5. the procedural and reasoning features relevant to the Article 267 analysis;
6. the provenance of the coded evidence.

The coding scheme is descriptive and evidence-based.

Coders must record what can be supported by the national decision and the identified source material. They must not infer a ground merely because a legal outcome appears obvious.

---

## 2. Unit of analysis

A "case" represents a national judicial decision.

An "issue" represents a distinct legal question for which the Article 267 preliminary-reference framework is relevant.

Issues must not be collapsed merely because they occur in the same decision.

If a decision expressly applies different reasoning to different EU-law questions, each question receives a separate issue record.

The issue is the primary unit of substantive coding.

---

## 3. EU-question status

The field `eu_question_status` records whether the issue raises a question concerning the interpretation or validity of EU law.

Allowed values:

- `EU_QUESTION`
- `NO_EU_QUESTION`

### 3.1 NO_EU_QUESTION

Use `NO_EU_QUESTION` where the national court determines that the relevant complaint, argument, or issue does not raise a question concerning the interpretation or validity of EU law.

This classification is conceptually prior to the analysis of whether a preliminary reference was necessary.

Do not use `NEC`, `ECL`, or `CLR` merely because the court rejects an argument that does not raise an EU-law question.

### 3.2 EU_QUESTION

Use `EU_QUESTION` where the issue concerns the interpretation or validity of EU law.

Once an issue is coded as `EU_QUESTION`, the coding must separately determine:

- whether a preliminary reference was made; and
- if no reference was made, which non-referral ground applies.

`eu_question_status` therefore does not itself identify the procedural outcome or the reason for non-referral.

---

## 4. Outcome

The field `outcome` records whether a preliminary reference was actually made for the issue.

Allowed values:

- `NO_REFERRAL`
- `REFERRAL`

### 4.1 NO_REFERRAL

Use `NO_REFERRAL` where the national court does not make a preliminary reference concerning the issue.

Where:

- `eu_question_status = EU_QUESTION`; and
- `outcome = NO_REFERRAL`;

the issue may be assigned a `non_referral_ground` where the decision provides sufficient evidence for one of the defined categories.

### 4.2 REFERRAL

Use `REFERRAL` where the national court actually makes a preliminary reference to the Court of Justice concerning the issue.

`REFERRAL` is an outcome.

It is not a value of `non_referral_ground`.

---

## 5. Non-referral ground

The field `non_referral_ground` records the operative ground where:

- `eu_question_status = EU_QUESTION`; and
- `outcome = NO_REFERRAL`.

Allowed values:

- `NEC`
- `ECL`
- `CLR`

The field must not be used for issues coded as `NO_EU_QUESTION`.

### 5.1 NEC — not necessary

Use `NEC` where an EU-law question exists, but the national court states that answering it is not necessary for resolving the dispute.

Typical indicators include an express statement that answering the EU-law question is unnecessary for the solution of the case.

A court's rejection of an argument does not by itself establish `NEC`.

### 5.2 ECL — existing case-law

Use `ECL` where the national court relies on existing Court of Justice case-law as sufficient to resolve the EU-law question.

The presence of a CJEU citation alone is not sufficient.

The decision should indicate that the question can be answered on the basis of existing case-law or otherwise substantively rely on existing CJEU jurisprudence to resolve the issue.

### 5.3 CLR — acte clair / no reasonable doubt

Use `CLR` where the national court expressly relies on the absence of reasonable doubt concerning the correct interpretation or answer.

The coding must be based on the court's own reasoning.

An analyst's independent conclusion that the law appears obvious is insufficient.

---

## 6. Decision rule

The coding process separates three questions:

1. Does the issue raise a question concerning EU law?
2. Was a preliminary reference made?
3. If no reference was made, what was the national court's operative non-referral ground?

The conceptual decision tree is:

    Does the issue raise an EU-law question?
        |
        +-- NO
        |     |
        |     +-- eu_question_status = NO_EU_QUESTION
        |     +-- non_referral_ground = null
        |
        +-- YES
              |
              +-- eu_question_status = EU_QUESTION
                    |
                    +-- Was a preliminary reference made?
                          |
                          +-- YES
                          |     |
                          |     +-- outcome = REFERRAL
                          |
                          +-- NO
                                |
                                +-- outcome = NO_REFERRAL
                                      |
                                      +-- NEC
                                      +-- ECL
                                      +-- CLR

When several non-referral grounds appear possible, code the ground that corresponds to the court's stated operative reason for not referring.

This is an analytical coding framework.

It is not presented as a claim that national courts themselves always organise their reasoning in this exact sequence.

---

## 7. Substantive EU analysis

The field `substantive_eu_analysis` records the extent to which the national court substantively analyses the underlying EU-law question.

Allowed values:

- `NONE`
- `MINIMAL`
- `MODERATE`
- `EXTENSIVE`

### 7.1 NONE

No substantive EU-law analysis relevant to the issue is identified.

### 7.2 MINIMAL

The decision contains limited substantive EU-law analysis.

### 7.3 MODERATE

The court applies one or more substantive EU-law authorities or propositions to resolve the issue.

### 7.4 EXTENSIVE

The EU-law issue receives substantial and developed analysis involving multiple legal propositions, authorities, distinctions, or interpretive steps.

This field is descriptive.

It does not determine the non-referral ground.

---

## 8. Article 267 reasoning

The field `article_267_reasoning` records the level of reasoning specifically concerning the preliminary-reference framework.

Allowed values:

- `NONE`
- `IMPLICIT`
- `EXPLICIT`

### 8.1 NONE

No identifiable Article 267 reasoning is recorded for the issue.

### 8.2 IMPLICIT

The Article 267 implications are identifiable from the reasoning, but the court does not expressly formulate the preliminary-reference analysis.

### 8.3 EXPLICIT

The court expressly addresses the preliminary-reference framework or the applicable Article 267 reasoning.

This field describes the form of the reasoning.

It does not replace `non_referral_ground` or `outcome`.

---

## 9. Procedural form

The field `procedural_form` records the form in which the relevant reasoning is presented.

Allowed values:

- `SUMMARY`
- `FULL`

### 9.1 SUMMARY

The relevant reasoning is presented briefly or in condensed form.

### 9.2 FULL

The relevant reasoning is presented through a developed judicial analysis.

---

## 10. Reasoning sequence

The field `reasoning_sequence` records the observed relationship between substantive EU-law analysis and Article 267 reasoning.

Allowed values:

- `SUBSTANCE_FIRST`
- `267_FIRST`
- `INTEGRATED`

### 10.1 SUBSTANCE_FIRST

The court first resolves or substantially analyses the underlying EU-law issue and subsequently addresses the Article 267 question.

### 10.2 267_FIRST

The court addresses the Article 267 or preliminary-reference question before developing the substantive EU-law analysis.

### 10.3 INTEGRATED

The substantive EU-law analysis and Article 267 reasoning are materially integrated.

This field is descriptive and should be coded from the structure of the reasoning.

It does not determine the applicable non-referral ground.

---

## 11. EU Court dialogue

The field `eu_court_dialogue` records the character of the national court's engagement with the Court of Justice and its jurisprudence.

Allowed values:

- `NONE`
- `CITATIONAL`
- `ANALYTICAL`
- `REFERRAL`

### 11.1 NONE

No relevant engagement with the Court of Justice is identified.

### 11.2 CITATIONAL

The decision cites CJEU authority without materially developing an analytical dialogue with that authority.

### 11.3 ANALYTICAL

The decision substantively engages with CJEU jurisprudence, including application, distinction, interpretation, or comparison.

### 11.4 REFERRAL

The issue involves an actual preliminary reference to the Court of Justice.

Where `eu_court_dialogue = REFERRAL`, the issue should also have:

- `outcome = REFERRAL`.

This field does not replace `outcome`.

---

## 12. Remling

The `remling` object records the temporal and analytical relationship between the national decision and the relevant Remling jurisprudence.

The field `temporal_relation` allows:

- `PRE_REMLING`
- `SAME_DAY`
- `POST_REMLING`

The field `reference` records whether Remling is expressly referenced.

The field `analytical_use` records whether Remling is substantively used in the reasoning.

The presence of a Remling citation alone does not establish analytical use.

### 12.1 PRE_REMLING

The national decision predates the relevant Remling decision.

### 12.2 SAME_DAY

The national decision and the relevant Remling decision have the same decision date.

### 12.3 POST_REMLING

The national decision postdates the relevant Remling decision.

The temporal classification must be based on the dates of the relevant decisions, not on the analyst's interpretation of their legal relationship.

---

## 13. Provenance

Each issue must contain provenance information identifying the source from which the coded evidence was obtained.

The provenance object contains:

- `source_id`
- `paragraph`
- `accessed`

### 13.1 source_id

`source_id` identifies the source in the source register.

The value must resolve to an existing entry in:

    sources/source_register.yaml

An unknown `source_id` must fail validation.

### 13.2 paragraph

`paragraph` identifies the paragraph, section, page, or other pinpoint location supporting the coded information.

The pinpoint should be sufficiently precise to allow another analyst to locate the evidence.

### 13.3 accessed

`accessed` records the date on which the source was accessed for coding.

Provenance is evidentiary metadata and does not determine the substantive coding.

---

## 14. Coding principles

### 14.1 Evidence before inference

Code only what can be supported by the decision and source material.

Do not infer an Article 267 ground solely from the final outcome.

### 14.2 Separate status, outcome, and ground

The following fields have distinct functions:

- `eu_question_status` — whether an EU-law question exists;
- `outcome` — whether a preliminary reference was actually made;
- `non_referral_ground` — why an EU-law question was not referred.

These fields must not be conflated.

### 14.3 Rejection is not NEC

A court's rejection of an argument does not automatically mean that answering the EU-law question was unnecessary.

`NEC` requires evidence that the EU-law question was unnecessary for resolving the dispute.

### 14.4 Citation is not automatically ECL

The mere presence of a CJEU citation does not automatically establish `ECL`.

The court must rely on existing case-law as sufficient to resolve the issue.

### 14.5 Clarity must come from the court

`CLR` requires evidence that the national court itself relies on the absence of reasonable doubt.

Analyst assessment of clarity is insufficient.

### 14.6 Referral is an outcome

`REFERRAL` belongs to `outcome`.

It is not a value of `non_referral_ground`.

### 14.7 Provenance is mandatory

Every coded issue must have traceable provenance.

The source identifier must resolve against the source register.

---

## 15. Pilot corpus examples

The pilot corpus currently contains examples of:

- `NO_EU_QUESTION`
- `NEC`
- `ECL`
- `CLR`
- `NO_REFERRAL`

The pilot corpus currently contains no issue with `outcome: REFERRAL`.

The absence of a referral in the pilot sample must not be interpreted as evidence that the coding framework cannot represent referrals.

---

## 16. Quality-control rules

Before accepting a coded case, verify that:

1. every issue has a valid `eu_question_status`;
2. every issue has a valid `outcome`;
3. `non_referral_ground` is one of `NEC`, `ECL`, or `CLR` when applicable;
4. `REFERRAL` is represented through `outcome`, not `non_referral_ground`;
5. `NO_EU_QUESTION` issues do not receive an Article 267 non-referral ground;
6. every provenance `source_id` resolves to the source register;
7. every provenance record contains a paragraph and access date;
8. coded values conform to the ontology;
9. no legacy field names are used;
10. the coded classification reflects the national court's reasoning rather than an analyst's independent legal conclusion.

---

## 17. Relationship between fields

The principal classification fields have distinct functions:

- `eu_question_status` answers whether an EU-law question exists;
- `outcome` records whether a preliminary reference was actually made;
- `non_referral_ground` records the applicable reason where an EU-law question exists but no reference was made.

These fields must not be conflated.

In particular:

    EU_QUESTION + REFERRAL
        => outcome = REFERRAL
        => non_referral_ground = null

    EU_QUESTION + NO_REFERRAL
        => outcome = NO_REFERRAL
        => non_referral_ground = NEC | ECL | CLR

    NO_EU_QUESTION
        => non_referral_ground = null

The `outcome` field records the procedural result independently of the EU-question classification.

---

## 18. Pilot corpus

The pilot corpus consists of the coded national decisions currently included in `data/cases/`.

The corpus is a pilot dataset and should not be treated as statistically representative.

Coding decisions should remain traceable to the underlying judicial text through provenance.

Changes to the coding ontology should be reflected consistently across:

- the ontology schema;
- the Pydantic data model;
- the case records;
- the validation logic;
- the tests;
- this coding manual.

---

## 19. Versioning

This document is version `0.1`.

Changes to field names, allowed values, decision rules, or coding semantics should be treated as ontology changes and reviewed across the complete project before acceptance.

The file:
