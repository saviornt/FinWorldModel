from __future__ import annotations

import pandas as pd

from fin_data.providers.alpaca.historical import normalize_bars
from fin_data.universe.instruments import CORPORATE_UNIVERSE, ETF_UNIVERSE, INITIAL_UNIVERSE
from fin_data.validation.bars import validate_bars


def test_initial_universe_contains_36_unique_instruments() -> None:
    assert len(ETF_UNIVERSE) == 10
    assert len(CORPORATE_UNIVERSE) == 26
    assert len(INITIAL_UNIVERSE) == 36
    assert len({instrument.symbol for instrument in INITIAL_UNIVERSE}) == 36


def test_normalize_bars_accepts_alpaca_symbol_timestamp_multiindex() -> None:
    index = pd.MultiIndex.from_tuples(
        [
            ("SPY", pd.Timestamp("2024-01-02", tz="UTC")),
            ("SPY", pd.Timestamp("2024-01-03", tz="UTC")),
        ],
        names=["symbol", "timestamp"],
    )
    source = pd.DataFrame(
        {
            "open": [470.0, 471.0],
            "high": [472.0, 473.0],
            "low": [469.0, 470.0],
            "close": [471.0, 472.0],
            "volume": [1000, 1200],
            "trade_count": [50, 60],
            "vwap": [470.5, 471.5],
        },
        index=index,
    )

    result = normalize_bars(source, "SPY")

    assert len(result) == 2
    assert isinstance(result.index, pd.DatetimeIndex)
    assert result.index.name == "timestamp"
    assert list(result.columns) == ["open", "high", "low", "close", "volume", "trade_count", "vwap"]


def test_validate_bars_accepts_valid_data() -> None:
    index = pd.date_range("2024-01-02", periods=2, tz="UTC", name="timestamp")
    frame = pd.DataFrame(
        {
            "open": [10.0, 11.0],
            "high": [12.0, 13.0],
            "low": [9.0, 10.0],
            "close": [11.0, 12.0],
            "volume": [100.0, 110.0],
            "trade_count": [5.0, 6.0],
            "vwap": [10.5, 11.5],
        },
        index=index,
    )
    assert validate_bars(frame, "TEST") == []


def test_validate_bars_flags_invalid_high_low_and_negative_volume() -> None:
    index = pd.date_range("2024-01-02", periods=1, tz="UTC", name="timestamp")
    frame = pd.DataFrame(
        {
            "open": [10.0],
            "high": [8.0],
            "low": [9.0],
            "close": [10.0],
            "volume": [-1.0],
            "trade_count": [1.0],
            "vwap": [10.0],
        },
        index=index,
    )
    issues = validate_bars(frame, "TEST")
    assert any("high is below low" in issue for issue in issues)
    assert any("negative volume" in issue for issue in issues)
