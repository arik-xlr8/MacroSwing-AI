"""Synthetic fixture values test metadata semantics only."""

from datetime import timedelta
from uuid import uuid4

import pytest
from pydantic import ValidationError

from macroswing.core.contracts import (
    AnalysisId,
    AnalysisTimestamp,
    AvailabilityTimestamp,
    DataAvailability,
    EducationalAction,
    HarnessState,
    MacroRegime,
    Observation,
    ObservationTimestamp,
    PublicationTimestamp,
    RetrievalTimestamp,
    RiskGateStatus,
    SourceMetadata,
    StockIdentity,
)


@pytest.mark.parametrize(
    ("enum", "words"),
    [
        (
            EducationalAction,
            "HOLD WATCH INVESTIGATE POTENTIAL_CATCH_UP_CANDIDATE TECHNICAL_REVERSAL_CANDIDATE FUNDAMENTAL_IMPROVEMENT_CANDIDATE REJECT_SIGNAL ANALYSIS_UNSAFE",
        ),
        (RiskGateStatus, "PASS PASS_WITH_WARNINGS INVESTIGATE ANALYSIS_UNSAFE HARD_BLOCK"),
        (MacroRegime, "EXPANSION LATE_CYCLE CONTRACTION RECOVERY UNCERTAIN"),
        (DataAvailability, "AVAILABLE MISSING UNAVAILABLE"),
        (
            HarnessState,
            "START SELECT_UNIVERSE LOAD_MARKET_DATA CHECK_DATA_QUALITY CALCULATE_TECHNICALS RUN_SECTOR_RELATIVE_ANALYSIS RUN_PATTERN_AND_REVERSAL_ANALYSIS LOAD_FUNDAMENTALS LOAD_MACRO_CONTEXT LOAD_NEWS_AND_SPEECH_CONTEXT BUILD_EVIDENCE PREVIEW_STRATEGIES RUN_BACKTEST RISK_GATE GENERATE_EXPLANATION HUMAN_REVIEW LOG_AND_CLOSE",
        ),
    ],
)
def test_vocabularies(enum, words):
    assert [value.value for value in enum] == words.split()
    with pytest.raises(ValueError):
        enum("UNKNOWN_LABEL")


@pytest.mark.parametrize(
    "kind",
    [
        ObservationTimestamp,
        PublicationTimestamp,
        AvailabilityTimestamp,
        RetrievalTimestamp,
        AnalysisTimestamp,
    ],
)
def test_timestamp_contract(kind):
    instant = kind("2024-02-01T10:30:00+03:00").root
    assert instant.hour == 7
    assert instant.utcoffset() == timedelta(0)
    for invalid in ["2024-02-01T07:30:00", "2024-02-01", "invalid"]:
        with pytest.raises(ValidationError):
            kind(invalid)


@pytest.fixture
def sample():
    return {
        "dataset": {
            "dataset_id": "synthetic",
            "version": "fixture-v1",
            "source": {
                "provider": "test fixture",
                "source_reference": "fixture/sample",
                "retrieved_at": "2024-03-20T10:00:00Z",
            },
        },
        "observed_at": "2023-12-31T20:00:00Z",
        "published_at": "2024-03-10T10:00:00Z",
        "available_at": "2024-03-10T10:05:00Z",
        "status": "AVAILABLE",
        "value": 0,
    }


def test_historical_access_requires_vintage_and_availability(sample):
    record = Observation[int](**sample)
    assert record.value_as_of(AnalysisTimestamp(sample["dataset"]["source"]["retrieved_at"])) == 0
    cutoff = AnalysisTimestamp(sample["available_at"])
    with pytest.raises(ValueError, match="vintage"):
        record.value_as_of(cutoff)
    archived = Observation[int](**sample, historical_vintage_reference="fixture/dated-vintage")
    assert archived.value_as_of(cutoff) == 0
    with pytest.raises(ValueError, match="unavailable"):
        archived.value_as_of(AnalysisTimestamp("2024-03-10T10:04:59Z"))


def test_revision_has_its_own_availability(sample):
    sample.update(
        published_at="2024-03-19T08:00:00Z",
        available_at="2024-03-19T08:00:00Z",
        historical_vintage_reference="fixture/revision-two",
    )
    sample["dataset"]["version"] = "fixture-v2"
    with pytest.raises(ValueError, match="unavailable"):
        Observation[int](**sample).value_as_of(AnalysisTimestamp("2024-03-15T12:00:00Z"))


@pytest.mark.parametrize("status", [DataAvailability.MISSING, DataAvailability.UNAVAILABLE])
def test_missing_values(sample, status):
    sample.update(status=status, value=None, available_at=None, missing_reason="fixture gap")
    assert Observation[int](**sample).value_as_of(AnalysisTimestamp(sample["observed_at"])) is None
    sample["value"] = 0
    with pytest.raises(ValidationError):
        Observation[int](**sample)
    sample.update(value=None, missing_reason=" ")
    with pytest.raises(ValidationError):
        Observation[int](**sample)


@pytest.mark.parametrize(
    "changes",
    [
        {"value": None},
        {"value": "not a number"},
        {"available_at": None},
        {"observed_at": "2025-01-01T00:00:00Z"},
        {"published_at": "2023-01-01T00:00:00Z"},
        {"available_at": "2023-12-31T20:00:00Z"},
        {"available_at": "2025-01-01T00:00:00Z"},
        {"missing_reason": "inconsistent"},
        {"unexpected": True},
    ],
)
def test_invalid_observations(sample, changes):
    with pytest.raises(ValidationError):
        Observation[int](**(sample | changes))


def test_identities(sample):
    case = uuid4()
    assert AnalysisId(str(case)).root == case
    with pytest.raises(ValidationError):
        AnalysisId("not-a-uuid")
    with pytest.raises(ValidationError):
        StockIdentity(ticker="wrong", yahoo_symbol="TEST.IS", sector={"label": "Test"})
    with pytest.raises(ValidationError):
        StockIdentity(ticker="TEST", yahoo_symbol="TEST.IS", sector={"label": ""})
    with pytest.raises(ValidationError):
        SourceMetadata(**(sample["dataset"]["source"] | {"provider": " "}))
