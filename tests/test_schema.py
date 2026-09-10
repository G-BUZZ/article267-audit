from datetime import date

import pytest
from pydantic import ValidationError

from article267_audit.models import Case


def valid_case() -> dict:
    return {
        "case_id": "TEST-001",
        "court": "Test Court",
        "country": "XX",
        "decision_date": date(2026, 9, 5),
        "ecli": "TEST:ECLI:001",
        "issues": [
            {
                "issue_id": "TEST-001-A",
                "eu_question": "Synthetic EU-law question",
                "eu_provision": "Article 267 TFEU",
                "relevance": "Relevant",
                "ground_raw": "already answered",
                "eu_question_status": "EU_QUESTION",
                "non_referral_ground": "ECL",
                "substantive_eu_analysis": "MINIMAL",
                "substantive_cjeu_authorities": [],
                "article_267_reasoning": "EXPLICIT",
                "article_267_authorities": [],
                "procedural_form": "FULL",
                "reasoning_sequence": "INTEGRATED",
                "eu_court_dialogue": "ANALYTICAL",
                "remling": {
                    "temporal_relation": "POST_REMLING",
                    "reference": True,
                    "analytical_use": True,
                },
                "outcome": "NO_REFERRAL",
                "provenance": {
                    "source_id": "SRC-TEST-001",
                    "paragraph": "§ 1",
                    "accessed": date(2026, 9, 5),
                },
                "confidence": "HIGH",
            }
        ],
    }


def test_valid_case_is_accepted():
    case = Case.model_validate(valid_case())

    assert case.case_id == "TEST-001"
    assert case.issues[0].eu_question_status == "EU_QUESTION"
    assert case.issues[0].non_referral_ground == "ECL"


def test_missing_source_id_is_rejected():
    data = valid_case()
    del data["issues"][0]["provenance"]["source_id"]

    with pytest.raises(ValidationError):
        Case.model_validate(data)


def test_missing_pinpoint_is_rejected():
    data = valid_case()
    del data["issues"][0]["provenance"]["paragraph"]

    with pytest.raises(ValidationError):
        Case.model_validate(data)


def test_no_eu_question_cannot_have_non_referral_ground():
    data = valid_case()
    data["issues"][0]["eu_question_status"] = "NO_EU_QUESTION"
    data["issues"][0]["non_referral_ground"] = "ECL"

    with pytest.raises(ValidationError):
        Case.model_validate(data)


def test_referral_cannot_have_non_referral_ground():
    data = valid_case()
    data["issues"][0]["outcome"] = "REFERRAL"
    data["issues"][0]["eu_court_dialogue"] = "REFERRAL"
    data["issues"][0]["non_referral_ground"] = "ECL"

    with pytest.raises(ValidationError):
        Case.model_validate(data)


def test_eu_question_no_referral_requires_ground():
    data = valid_case()
    data["issues"][0]["non_referral_ground"] = None

    with pytest.raises(ValidationError):
        Case.model_validate(data)


def test_referral_requires_referral_dialogue():
    data = valid_case()
    data["issues"][0]["outcome"] = "REFERRAL"

    with pytest.raises(ValidationError):
        Case.model_validate(data)
