"""Historical bar requests and normalization"""

from __future__ import annotations

from datetime import UTC, date, datetime, time
from typing import TYPE_CHECKING, cast

import pandas as pd
from alpaca.data.enums import DataFeed
from alpaca.data.models.bars import BarSet
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

if TYPE_CHECKING:
    from alpaca.data.historical import StockHistoricalDataClient

from fin_data.providers.alpaca.constants import ADJUSTMENTS, BAR_COLUMNS


def normalize_bars(frame: pd.DataFrame, symbol: str) -> pd.DataFrame:
    """Normalize an Alpaca BarSet DataFrame to a timestamp-indexed frame."""
    if frame.empty:
        return pd.DataFrame(columns=list(BAR_COLUMNS), index=pd.DatetimeIndex([], name="timestamp"))

    normalized = frame.copy()

    if isinstance(normalized.index, pd.MultiIndex):
        index_names = normalized.index.names

        symbol_level = index_names.index("symbol") if "symbol" in index_names else 0

        timestamp_level = index_names.index("timestamp") if "timestamp" in index_names else 1 - symbol_level

        symbol_mask = normalized.index.get_level_values(symbol_level) == symbol

        normalized = normalized.loc[symbol_mask].copy()

        normalized.index = pd.DatetimeIndex(normalized.index.get_level_values(timestamp_level))

    normalized.index = pd.DatetimeIndex(
        pd.to_datetime(normalized.index, utc=True),
        name="timestamp",
    )
    normalized = normalized.sort_index()
    normalized = normalized.loc[~normalized.index.duplicated(keep="last")]

    for column in BAR_COLUMNS:
        if column not in normalized.columns:
            normalized[column] = pd.NA

    normalized = normalized.loc[:, list(BAR_COLUMNS)]
    for column in BAR_COLUMNS:
        normalized[column] = pd.to_numeric(normalized[column], errors="coerce")

    normalized["volume"] = normalized["volume"].astype("float64")
    normalized["trade_count"] = normalized["trade_count"].astype("float64")
    return normalized


class AlpacaHistoricalDataProvider:
    def __init__(
        self,
        stock_client: StockHistoricalDataClient,
        feed: DataFeed = DataFeed.IEX,
    ) -> None:
        self.stock_client = stock_client
        self.feed = feed

    def fetch_daily_bars(
        self,
        symbol: str,
        start: date,
        end: date,
        adjustment: str,
    ) -> pd.DataFrame:
        if start > end:
            raise ValueError("Start date cannot be later than end date.")

        if adjustment not in ADJUSTMENTS:
            raise ValueError(f"Unsupported adjustment: {adjustment}. Expected one of: {', '.join(ADJUSTMENTS)}.")

        start_dt = datetime.combine(start, time.min, tzinfo=UTC)
        end_dt = datetime.combine(end, time.max, tzinfo=UTC)

        request = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=cast("TimeFrame", TimeFrame.Day),
            start=start_dt,
            end=end_dt,
            limit=10_000,
            adjustment=ADJUSTMENTS[adjustment],
            feed=self.feed,
        )

        response = self.stock_client.get_stock_bars(request)

        if not isinstance(response, BarSet):
            raise TypeError(f"Expected Alpaca BarSet response, received {type(response).__name__}.")

        return normalize_bars(response.df, symbol)
