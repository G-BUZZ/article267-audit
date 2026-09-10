from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, model_validator

EUQuestionStatus = Literal[
    "NO_EU_QUESTION",
    "EU_QUESTION",
]

NonReferralGround = Literal[
    "NEC",
    "ECL",
    "CLR",
]

AnalysisLevel = Literal[
    "NONE",
    "MINIMAL",
    "MODERATE",
    "EXTENSIVE",
]

ReasoningLevel = Literal[
    "NONE",
    "IMPLICIT",
    "EXPLICIT",
]

ProceduralForm = Literal[
    "SUMMARY",
    "FULL",
]

ReasoningSequence = Literal[
    "SUBSTANCE_FIRST",
    "267_FIRST",
    "INTEGRATED",
]

EUDialogue = Literal[
    "NONE",
    "CITATIONAL",
    "ANALYTICAL",
    "REFERRAL",
]

TemporalRelation = Literal[
    "PRE_REMLING",
    "SAME_DAY",
    "POST_REMLING",
]


class Authority(BaseModel):
    name: str
    paragraph: str | None = None


class Remling(BaseModel):
    temporal_relation: TemporalRelation
    reference: bool
    analytical_use: bool


class Provenance(BaseModel):
    source_id: str = Field(min_length=1)
    paragraph: str = Field(min_length=1)
    accessed: date


class Issue(BaseModel):
    issue_id: str
    eu_question: str
    eu_provision: str | None = None

    relevance: str

    ground_raw: str
    eu_question_status: EUQuestionStatus
    non_referral_ground: NonReferralGround | None = None

    substantive_eu_analysis: AnalysisLevel
    substantive_cjeu_authorities: list[Authority] = Field(default_factory=list)

    article_267_reasoning: ReasoningLevel
    article_267_authorities: list[Authority] = Field(default_factory=list)

    procedural_form: ProceduralForm
    reasoning_sequence: ReasoningSequence
    eu_court_dialogue: EUDialogue

    remling: Remling

    outcome: Literal["NO_REFERRAL", "REFERRAL"]

    provenance: Provenance

    confidence: Literal["LOW", "MEDIUM", "HIGH"]
    analyst_note: str | None = None

    @model_validator(mode="after")
    def validate_logical_consistency(self):
        if (
            self.eu_question_status == "NO_EU_QUESTION"
            and self.non_referral_ground is not None
        ):
            raise ValueError(
                "non_referral_ground requires "
                "eu_question_status=EU_QUESTION"
            )

        if (
            self.outcome == "REFERRAL"
            and self.non_referral_ground is not None
        ):
            raise ValueError(
                "REFERRAL outcome cannot have non_referral_ground"
            )

        if (
            self.outcome == "NO_REFERRAL"
            and self.eu_question_status == "EU_QUESTION"
            and self.non_referral_ground is None
        ):
            raise ValueError(
                "EU_QUESTION with NO_REFERRAL requires non_referral_ground"
            )

        if (
            self.outcome == "REFERRAL"
            and self.eu_court_dialogue != "REFERRAL"
        ):
            raise ValueError(
                "REFERRAL outcome requires eu_court_dialogue=REFERRAL"
            )

        return self


class Case(BaseModel):
    case_id: str
    court: str
    country: str
    decision_date: date
    ecli: str
    issues: list[Issue]
