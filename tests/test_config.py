"""Offline checks against the instructor's PDF, including the complete section 5 table."""

from pathlib import Path
from shutil import copytree

import pytest
import yaml

from macroswing.core.config import ConfigurationError, load_config

ROOT = Path(__file__).resolve().parents[1]
# Transcription of PDF p. 3. Order is checked independently of the config digest.
ROSTER = """
ASELS ASELS.IS Technology / Defense
TUPRS TUPRS.IS Petroleum / Refining
BIMAS BIMAS.IS Retail Trade
THYAO THYAO.IS Transportation / Airlines
AKBNK AKBNK.IS Banking
KCHOL KCHOL.IS Holding / Investment
EREGL EREGL.IS Basic Metals / Steel
TCELL TCELL.IS Telecommunications
CCOLA CCOLA.IS Food & Beverage
MGROS MGROS.IS Retail Trade
SASA SASA.IS Chemicals / Plastics
TRALT TRALT.IS Mining
FROTO FROTO.IS Automotive
ENKAI ENKAI.IS Construction
PGSUS PGSUS.IS Transportation / Airlines
MPARK MPARK.IS Healthcare
EKGYO EKGYO.IS Real Estate Investment Trust
GUBRF GUBRF.IS Chemicals / Fertilizer
TURSG TURSG.IS Insurance
ENJSA ENJSA.IS Electric Utilities
TTKOM TTKOM.IS Telecommunications
OYAKC OYAKC.IS Cement
AKSEN AKSEN.IS Electric Utilities
ISMEN ISMEN.IS Brokerage / Capital Markets
ARCLK ARCLK.IS Durables / Machinery
ECILC ECILC.IS Healthcare / Pharmaceuticals
MAVI MAVI.IS Retail / Apparel
PETKM PETKM.IS Petrochemicals
TOASO TOASO.IS Automotive
KRDMD KRDMD.IS Basic Metals / Steel
""".strip()


def test_all_templates_and_pdf_roster():
    config = load_config(ROOT / "configs")
    expected = [tuple(line.split(maxsplit=2)) for line in ROSTER.splitlines()]
    actual = [(s.ticker, s.yahoo_symbol, s.sector.label) for s in config.universe.stocks]
    assert actual == expected
    assert len({row[0] for row in actual}) == len(actual) == 30
    assert config.market.start_date is None
    assert config.backtest.reversal_days == (1, 3, 5, 10)
    assert config.backtest.catch_up_days == (5, 10, 20)
    assert config.backtest.disclosure_days == (1, 5, 20)
    assert config.harness.states[3].value == "CHECK_DATA_QUALITY"


@pytest.fixture
def directory(tmp_path):
    return copytree(ROOT / "configs", tmp_path / "config")


@pytest.mark.parametrize(
    ("file", "field", "value"),
    [
        ("market", "index", "OTHER"),
        ("macro", "unrecognized_key", 1),
        ("macro", "regime_labels", ["UNCERTAIN"]),
        ("indicators", "groups", ["SMA"]),
        ("strategies", "variants", ["A", "B", "C", "D"]),
        ("strategies", "factor_weights", {"x": 1}),
        ("backtest", "catch_up_days", [5, 10]),
        ("backtest", "additional_days", [-1]),
        ("harness", "actions", ["BUY"]),
        ("harness", "gate_statuses", ["PASS"]),
        ("universe", "recheck_membership_each_run", False),
    ],
)
def test_reject_invalid_template(directory, file, field, value):
    path = directory / f"{file}.yaml"
    data = yaml.safe_load(path.read_text())
    data[field] = value
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(ConfigurationError, match=field):
        load_config(directory)


@pytest.mark.parametrize("change", ["duplicate", "remove", "add", "rename", "symbol", "sector"])
def test_reject_modified_roster(directory, change):
    path = directory / "universe.yaml"
    data = yaml.safe_load(path.read_text())
    stocks = data["stocks"]
    if change == "duplicate":
        stocks[1] = stocks[0]
    elif change == "remove":
        stocks.pop()
    elif change == "add":
        stocks.append(stocks[0])
    elif change == "rename":
        stocks[0].update(ticker="ZZZZ", yahoo_symbol="ZZZZ.IS")
    elif change == "symbol":
        stocks[0]["yahoo_symbol"] = "OTHER.IS"
    else:
        stocks[0]["sector"]["label"] = "Defense"
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(ConfigurationError):
        load_config(directory)


def test_comparison_peer_is_separate(directory):
    path = directory / "universe.yaml"
    data = yaml.safe_load(path.read_text())
    # Synthetic identity for schema testing only.
    data["external_sector_peers"] = [
        {"ticker": "TEST", "yahoo_symbol": "TEST.IS", "sector": {"label": "Banking"}}
    ]
    path.write_text(yaml.safe_dump(data))
    assert len(load_config(directory).universe.stocks) == 30
    data["external_sector_peers"] = data["stocks"][:1]
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(ConfigurationError, match="external tickers"):
        load_config(directory)


@pytest.mark.parametrize("change", ["omit", "reorder"])
def test_mandatory_workflow(directory, change):
    path = directory / "harness.yaml"
    data = yaml.safe_load(path.read_text())
    states = data["states"]
    if change == "omit":
        states.remove("RUN_BACKTEST")
    else:
        states[2], states[3] = states[3], states[2]
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(ConfigurationError, match="state order"):
        load_config(directory)


@pytest.mark.parametrize(
    "content", [None, "", "[", "provider: one\nprovider: two\n", "!!python/tuple []"]
)
def test_file_errors(directory, content):
    path = directory / "market.yaml"
    if content is None:
        path.unlink()
    else:
        path.write_text(content)
    with pytest.raises(ConfigurationError, match="market"):
        load_config(directory)
