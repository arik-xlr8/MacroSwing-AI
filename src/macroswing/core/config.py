"""Load and validate the seven version-controlled Phase 01 configuration files."""

from collections.abc import Hashable
from datetime import date
from hashlib import sha256
from pathlib import Path
from typing import Annotated, Literal, Self

import yaml
from pydantic import AfterValidator, Field, PositiveInt, model_validator

from .contracts import (
    Contract,
    EducationalAction,
    HarnessState,
    MacroRegime,
    RiskGateStatus,
    SectorIdentity,
    StockIdentity,
    Text,
)


def exactly(*required: Hashable) -> AfterValidator:
    """A collection of required entries in any order, each appearing once."""

    def validate(values: tuple[Hashable, ...]) -> tuple[Hashable, ...]:
        if len(values) != len(required) or set(values) != set(required):
            raise ValueError(f"expected each of {required} once")
        return values

    return AfterValidator(validate)


class ExternalBenchmark(Contract):
    sector: SectorIdentity
    reference: Text


class UniverseConfig(Contract):
    study_universe: Literal["fixed"]
    recheck_membership_each_run: Literal[True]
    historical_membership_reference: Text | None
    external_sector_benchmarks: tuple[ExternalBenchmark, ...]
    external_sector_peers: tuple[StockIdentity, ...]
    stocks: Annotated[tuple[StockIdentity, ...], Field(min_length=30, max_length=30)]

    @model_validator(mode="after")
    def verify_roster(self) -> Self:
        # SHA-256 of the PDF §5 rows: sorted ticker, symbol and sector, tab-separated.
        records = sorted(f"{s.ticker}\t{s.yahoo_symbol}\t{s.sector.label}\n" for s in self.stocks)
        checksum = sha256("".join(records).encode()).hexdigest()
        if checksum != "6f3e5476a28ce364a297c12d2446c4574f869865eff40a918b9e612c979b3984":
            raise ValueError("fixed study universe differs from assignment §5")
        external = [s.ticker for s in self.external_sector_peers]
        if len(set(external)) != len(external) or set(external) & {s.ticker for s in self.stocks}:
            raise ValueError("external tickers must be unique and outside the fixed universe")
        return self


class MarketConfig(Contract):
    provider: Literal["yahoo_finance"]
    index: Literal["XU100"]
    fields: Annotated[
        tuple[str, ...], exactly("open", "high", "low", "close", "volume", "adjusted_close")
    ]
    start_date: date | None


class MacroConfig(Contract):
    required_series: Annotated[
        tuple[str, ...],
        exactly(
            "USD/TRY",
            "EUR/TRY",
            "TCMB_policy_rate",
            "Fed_target_range",
            "TUIK_CPI_monthly",
            "TUIK_CPI_annual",
        ),
    ]
    regime_scopes: Annotated[tuple[str, ...], exactly("global", "turkish")]
    regime_labels: Annotated[tuple[MacroRegime, ...], exactly(*MacroRegime)]
    classification_rules: None
    provider_access: None


class IndicatorsConfig(Contract):
    groups: Annotated[
        tuple[str, ...],
        exactly(
            "SMA",
            "EMA",
            "KAMA",
            "RSI",
            "MACD",
            "Bollinger Bands",
            "ATR",
            "Supertrend",
            "Ichimoku Cloud",
            "Support/Resistance",
            "Volume/turnover",
        ),
    ]


class StrategiesConfig(Contract):
    variants: Annotated[tuple[str, ...], exactly("A", "B", "C", "D", "E")]
    entry_rules: None
    exit_rules: None
    factor_weights: None


class BacktestConfig(Contract):
    reversal_days: Annotated[tuple[PositiveInt, ...], exactly(1, 3, 5, 10)]
    catch_up_days: Annotated[tuple[PositiveInt, ...], exactly(5, 10, 20)]
    disclosure_days: Annotated[tuple[PositiveInt, ...], exactly(1, 5, 20)]
    additional_days: tuple[PositiveInt, ...]
    benchmarks: Annotated[
        tuple[str, ...], exactly("buy_and_hold", "XU100", "sector_when_available")
    ]
    cost_assumptions: None
    slippage_assumptions: None
    position_sizing: None
    risk_constraints: None


class HarnessConfig(Contract):
    states: tuple[HarnessState, ...]
    actions: Annotated[tuple[EducationalAction, ...], exactly(*EducationalAction)]
    gate_statuses: Annotated[tuple[RiskGateStatus, ...], exactly(*RiskGateStatus)]

    @model_validator(mode="after")
    def check_order(self) -> Self:
        if self.states != tuple(HarnessState):
            raise ValueError("state order must match assignment §23")
        return self


class ProjectConfig(Contract):
    universe: UniverseConfig
    market: MarketConfig
    macro: MacroConfig
    indicators: IndicatorsConfig
    strategies: StrategiesConfig
    backtest: BacktestConfig
    harness: HarnessConfig


class ConfigurationError(ValueError):
    """Invalid or unreadable project configuration."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently overriding earlier settings."""

    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep)
        if len(mapping) != len(node.value):
            raise ValueError(f"duplicate YAML key near line {node.start_mark.line + 1}")
        return mapping


def load_config(directory: str | Path) -> ProjectConfig:
    """Load a complete configuration or raise with the offending file/field."""
    sections = {}
    for name in ProjectConfig.model_fields:
        path = Path(directory) / f"{name}.yaml"
        try:
            with path.open(encoding="utf-8") as stream:
                sections[name] = yaml.load(stream, Loader=_UniqueKeyLoader)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            raise ConfigurationError(f"{path}: {exc}") from exc
    try:
        return ProjectConfig.model_validate(sections)
    except ValueError as exc:
        raise ConfigurationError(f"{directory}: {exc}") from exc
