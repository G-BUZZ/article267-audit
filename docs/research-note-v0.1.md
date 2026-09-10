# Research Note — Article 267 Audit

## 1. Research question

This project asks how national-court reasoning concerning the preliminary-reference obligation under Article 267(3) TFEU can be represented in a structured, reproducible and auditable form.

The central methodological choice is to analyse reasoning at issue level rather than reducing the analysis to the binary question of whether a preliminary reference was ultimately made.

## 2. Research and methodological approach

The project develops a coding framework for selected decisions of courts of last instance. The framework separates the identification of an EU-law question from the subsequent reasoning concerning relevance, non-referral and referral.

The approach is designed to make the analytical steps explicit and comparable across cases. It therefore treats the coding scheme itself as part of the research method rather than as a purely technical data-entry structure.

## 3. Coding framework

The data model distinguishes several dimensions of the judicial reasoning, including:

- EU-law question and relevance;
- non-referral ground;
- substantive EU-law analysis;
- Article 267 reasoning;
- procedural form;
- reasoning sequence;
- EU Court dialogue;
- provenance and source traceability.

The pilot uses three CILFIT-derived non-referral categories:

- NEC — the EU-law issue is not necessary for the decision;
- ECL — an existing body of CJEU case-law provides the relevant answer;
- CLR — acte clair / absence of reasonable doubt.

The framework deliberately keeps the procedural outcome distinct from the legal ground for non-referral. In particular, REFERRAL is treated as an outcome rather than as a non-referral ground.

## 4. Issue-level analysis

An issue-level approach makes it possible to distinguish between different EU-law questions arising within the same decision and to record the reasoning attached to each question.

This is important for comparative research because a single judgment may contain several EU-law issues with different levels of relevance, different reasoning sequences and different relationships with CJEU case-law.

## 5. Provenance and source traceability

A central design principle is that substantive coding decisions should be traceable to their sources. Where possible, the dataset records a specific paragraph or pinpoint reference.

Secondary materials may assist discovery and contextualisation, but the legal propositions represented in the dataset are intended to rely on primary sources whenever these are available.

This provenance structure is intended to make the coding process auditable and facilitate later verification or recoding.

## 6. Pilot corpus

Version 0.1.0 contains four pilot cases. The cases are used to demonstrate the coding framework, the provenance architecture and the semantic validation approach.

The pilot corpus is methodological rather than statistically representative. Its purpose at this stage is to test whether the analytical categories can be applied consistently and represented in a machine-readable structure.

## 7. Semantic validation and reproducibility

The project combines a formal Pydantic data model with semantic validation rules. These rules are intended to prevent logically inconsistent combinations of fields.

Examples include preventing a NO_EU_QUESTION classification from simultaneously carrying a non-referral ground, preventing REFERRAL from being coded as a non-referral ground, and requiring an appropriate non-referral ground when an EU-law question is identified but no referral is made.

The repository also contains automated tests and a GitHub Actions workflow. The current test suite passes locally, and the same test and linting checks are configured for continuous integration.

## 8. Methodological value

The main contribution of the project is the combination of legal analysis with explicit data structures, provenance and validation. This makes the research process more transparent than an unstructured collection of case summaries and provides a basis for subsequent expansion of the corpus.

The framework is also designed so that future cases can be coded using the same categories and validation rules, making methodological changes visible rather than implicit.

## 9. Limitations

The present version has a small pilot corpus and therefore cannot support broad statistical or generalised empirical conclusions about national-court behaviour.

The coding categories also require continued testing against a larger and more diverse set of judgments. In particular, borderline cases may require refinement of the operational distinctions between the non-referral categories.

## 10. Next steps

The next stage is to expand the corpus while preserving the existing provenance and validation requirements, test inter-case consistency, and refine the coding manual where recurring borderline patterns emerge.

The repository is therefore presented as a methodological research prototype rather than as a completed empirical dataset.
