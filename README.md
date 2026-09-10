# Article 267 Audit

Issue-level comparative audit of national courts' reasoning under Article 267(3) TFEU.

## Scope

The project analyses selected decisions of courts of last instance and records how questions concerning the preliminary-reference obligation are reasoned.

## Research question

How can national-court reasoning concerning Article 267(3) TFEU be coded in a structured, reproducible and auditable way?

## Core dimensions

- EU-law question and relevance
- non-referral ground (CILFIT-derived categories: NEC, ECL, CLR)
- substantive EU-law analysis
- Article 267 reasoning
- procedural form and reasoning sequence
- EU Court dialogue
- provenance and source traceability

## Method

The project uses an issue-level coding framework rather than treating the existence or absence of a preliminary reference as the sole analytical variable. Each coded issue is represented through a formal data model and checked through semantic validation rules.

## Provenance

Every substantive coding decision is intended to be traceable to a primary source and, where possible, to a specific paragraph or pinpoint reference. Secondary sources may support discovery and contextualisation, but primary sources are preferred for the legal propositions recorded in the dataset.

## Reproducibility

Install the package and development dependencies with `python -m pip install -e ".[dev]"`. Run `pytest -q` for the test suite and `ruff check .` for linting. GitHub Actions runs the test and lint checks automatically on pushes and pull requests.

## Pilot corpus

Version 0.1.0 contains a four-case pilot corpus. The pilot is intended to demonstrate the coding framework, provenance architecture and validation approach; it is not presented as a statistically representative dataset.

## Status

Research prototype — methodological and technical framework under development.
