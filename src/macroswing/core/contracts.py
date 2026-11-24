"""Identities and time-aware contracts shared by offline research modules."""

from datetime import datetime, timezone
from enum import StrEnum
from typing import Annotated, Generic, Self, TypeVar
from uuid import UUID

from pydantic import (
    AfterValidator,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    RootModel,
    StringConstraints,
    model_validator,
)

Text = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Ticker = Annotated[str, StringConstraints(pattern=r"^[A-Z][A-Z0-9]{2,7}$")]
ValueT = TypeVar("ValueT")


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)


class SectorIdentity(Contract):
    label: Text


class StockIdentity(Contract):
    ticker: Ticker
    yahoo_symbol: Text
    sector: SectorIdentity

    @model_validator(mode="after")
    def check_symbol(self) -> Self:
        if self.yahoo_symbol != f"{self.ticker}.IS":
            raise ValueError("Yahoo symbol must match the BIST ticker with .IS suffix")
        return self


class AnalysisId(RootModel[UUID]):
    model_config = ConfigDict(frozen=True)


def _utc(value: datetime) -> datetime:
    return value.astimezone(timezone.utc)


class Timestamp(RootModel[Annotated[AwareDatetime, AfterValidator(_utc)]]):
    """Timezone-aware instant normalized to UTC."""

    model_config = ConfigDict(frozen=True)


class ObservationTimestamp(Timestamp):
    """Instant or end of the period that the observation describes."""


class PublicationTimestamp(Timestamp):
    """When the source released this version."""


class AvailabilityTimestamp(Timestamp):
    """Earliest documented access to this version."""


class RetrievalTimestamp(Timestamp):
    """When this snapshot was actually acquired."""


class AnalysisTimestamp(Timestamp):
    """Simulated or actual decision cutoff."""


class DataAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    MISSING = "MISSING"
    UNAVAILABLE = "UNAVAILABLE"


class EducationalAction(StrEnum):
    HOLD = "HOLD"
    WATCH = "WATCH"
    INVESTIGATE = "INVESTIGATE"
    POTENTIAL_CATCH_UP_CANDIDATE = "POTENTIAL_CATCH_UP_CANDIDATE"
    TECHNICAL_REVERSAL_CANDIDATE = "TECHNICAL_REVERSAL_CANDIDATE"
    FUNDAMENTAL_IMPROVEMENT_CANDIDATE = "FUNDAMENTAL_IMPROVEMENT_CANDIDATE"
    REJECT_SIGNAL = "REJECT_SIGNAL"
    ANALYSIS_UNSAFE = "ANALYSIS_UNSAFE"


class HarnessState(StrEnum):
    START = "START"
    SELECT_UNIVERSE = "SELECT_UNIVERSE"
    LOAD_MARKET_DATA = "LOAD_MARKET_DATA"
    CHECK_DATA_QUALITY = "CHECK_DATA_QUALITY"
    CALCULATE_TECHNICALS = "CALCULATE_TECHNICALS"
    RUN_SECTOR_RELATIVE_ANALYSIS = "RUN_SECTOR_RELATIVE_ANALYSIS"
    RUN_PATTERN_AND_REVERSAL_ANALYSIS = "RUN_PATTERN_AND_REVERSAL_ANALYSIS"
    LOAD_FUNDAMENTALS = "LOAD_FUNDAMENTALS"
    LOAD_MACRO_CONTEXT = "LOAD_MACRO_CONTEXT"
    LOAD_NEWS_AND_SPEECH_CONTEXT = "LOAD_NEWS_AND_SPEECH_CONTEXT"
    BUILD_EVIDENCE = "BUILD_EVIDENCE"
    PREVIEW_STRATEGIES = "PREVIEW_STRATEGIES"
    RUN_BACKTEST = "RUN_BACKTEST"
    RISK_GATE = "RISK_GATE"
    GENERATE_EXPLANATION = "GENERATE_EXPLANATION"
    HUMAN_REVIEW = "HUMAN_REVIEW"
    LOG_AND_CLOSE = "LOG_AND_CLOSE"


class RiskGateStatus(StrEnum):
    PASS = "PASS"
    PASS_WITH_WARNINGS = "PASS_WITH_WARNINGS"
    INVESTIGATE = "INVESTIGATE"
    ANALYSIS_UNSAFE = "ANALYSIS_UNSAFE"
    HARD_BLOCK = "HARD_BLOCK"


class MacroRegime(StrEnum):
    EXPANSION = "EXPANSION"
    LATE_CYCLE = "LATE_CYCLE"
    CONTRACTION = "CONTRACTION"
    RECOVERY = "RECOVERY"
    UNCERTAIN = "UNCERTAIN"


class SourceMetadata(Contract):
    provider: Text
    source_reference: Text
    retrieved_at: RetrievalTimestamp


class DatasetMetadata(Contract):
    dataset_id: Text
    version: Text
    source: SourceMetadata


class Observation(Contract, Generic[ValueT]):
    """One version of a realized observation, with explicit missingness."""

    dataset: DatasetMetadata
    observed_at: ObservationTimestamp
    published_at: PublicationTimestamp | None = None
    available_at: AvailabilityTimestamp | None = None
    historical_vintage_reference: Text | None = None
    status: DataAvailability
    value: ValueT | None = None
    missing_reason: Text | None = None

    @model_validator(mode="after")
    def check_record(self) -> Self:
        if self.status == DataAvailability.AVAILABLE:
            if self.value is None or self.available_at is None or self.missing_reason is not None:
                raise ValueError(
                    "available observations require value, availability and no missing reason"
                )
        elif self.value is not None or self.missing_reason is None:
            raise ValueError("missing or unavailable observations require a reason and no value")

        retrieved = self.dataset.source.retrieved_at.root
        if self.observed_at.root > retrieved:
            raise ValueError("realized observation falls after retrieval")
        if self.published_at and not self.observed_at.root <= self.published_at.root <= retrieved:
            raise ValueError("publication must fall between observation and retrieval")
        if self.available_at:
            earliest = self.published_at or self.observed_at
            if not earliest.root <= self.available_at.root <= retrieved:
                raise ValueError(
                    "availability must follow observation/publication and precede or equal retrieval"
                )
        return self

    def value_as_of(self, decision_at: AnalysisTimestamp) -> ValueT | None:
        """Only release a value supported at the decision cutoff."""
        if self.status != DataAvailability.AVAILABLE:
            return None
        if self.available_at is None or self.available_at.root > decision_at.root:
            raise ValueError("this version was unavailable at the decision timestamp")
        if (
            self.dataset.source.retrieved_at.root > decision_at.root
            and not self.historical_vintage_reference
        ):
            raise ValueError("later retrieval requires dated historical vintage evidence")
        return self.value
