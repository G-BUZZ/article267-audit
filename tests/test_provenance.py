from pathlib import Path

import pytest
from pydantic import ValidationError

from article267_audit.provenance import (
    load_source_register,
    validate_source_ids,
)
from article267_audit.validation import load_case

ROOT = Path(__file__).resolve().parents[1]


def test_nl2934_loads():
    case = load_case(ROOT / "data/cases/NL-2934.yaml")

    assert case.case_id == "NL-2934"
    assert case.ecli == "ECLI:NL:RVS:2026:2934"


def test_nl2934_has_valid_source_id():
    case = load_case(ROOT / "data/cases/NL-2934.yaml")
    sources = load_source_register(ROOT / "sources/source_register.yaml")

    validate_source_ids(case, sources)


def test_unknown_source_id_is_rejected():
    case = load_case(ROOT / "data/cases/NL-2934.yaml")
    sources = load_source_register(ROOT / "sources/source_register.yaml")

    case.issues[0].provenance.source_id = "SRC-DOES-NOT-EXIST"

    with pytest.raises(ValueError, match="Unknown source_id"):
        validate_source_ids(case, sources)


def test_missing_provenance_is_rejected():
    case_data = {
        "case_id": "TEST",
        "court": "Test Court",
        "country": "XX",
        "decision_date": "2026-09-05",
        "ecli": "TEST:ECLI",
        "issues": [
            {
                "issue_id": "TEST-A",
                "eu_question": "Synthetic question",
                "relevance": "Relevant",
                "ground_raw": "test",
                "eu_question_status": "EU_QUESTION",
                "non_referral_ground": "ECL",
                "substantive_eu_analysis": "NONE",
                "article_267_reasoning": "EXPLICIT",
                "procedural_form": "FULL",
                "reasoning_sequence": "INTEGRATED",
                "eu_court_dialogue": "ANALYTICAL",
                "remling": {
                    "temporal_relation": "POST_REMLING",
                    "reference": False,
                    "analytical_use": False,
                },
                "outcome": "NO_REFERRAL",
                "confidence": "HIGH",
            }
        ],
    }

    with pytest.raises(ValidationError):
        from article267_audit.models import Case

        Case.model_validate(case_data)
