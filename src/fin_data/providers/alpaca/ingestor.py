"""Alpaca-specific ingestion orchestration."""

from __future__ import annotations

import logging
import os
from dataclasses import asdict
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd
from alpaca.data.enums import Adjustment, DataFeed
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.corporate_actions import CorporateActionsClient

from fin_data.ingestion.backfill import run_backfill
from fin_data.ingestion.manifest import IngestionManifest
from fin_data.providers.alpaca.corporate_actions import (
    AlpacaCorporateActionsProvider,
)
from fin_data.providers.alpaca.historical import AlpacaHistoricalDataProvider
from fin_data.storage.arcticdb.client import ArcticDBClient
from fin_data.storage.arcticdb.metadata import instrument_frame
from fin_data.storage.arcticdb.repositories import ArcticDBRepository
from fin_data.universe.instruments import INITIAL_UNIVERSE, Instrument
from fin_data.validation.bars import validate_bars

LOGGER = logging.getLogger(__name__)

BAR_COLUMNS = ("open", "high", "low", "close", "volume", "trade_count", "vwap")
ADJUSTMENTS = {
    "raw": Adjustment.RAW,
    "all": Adjustment.ALL,
}


def default_end_date() -> date:
    """Return the previous calendar day in the US Eastern timezone."""
    return datetime.now(ZoneInfo("America/New_York")).date() - timedelta(days=1)


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


def _instrument_frame(instruments: tuple[Instrument, ...]) -> pd.DataFrame:
    rows = [asdict(item) for item in instruments]
    return pd.DataFrame(rows).set_index("symbol")


class AlpacaDatasetIngestor:
    """Download Alpaca daily bars and persist them in a local ArcticDB store."""

    def __init__(
        self,
        *,
        api_key: str,
        secret_key: str,
        store_path: Path,
        feed: str = "iex",
        start: date = date(2016, 1, 1),
        end: date | None = None,
        manifest_path: Path | None = None,
    ) -> None:
        if feed.lower() != "iex":
            raise ValueError("This prototype is configured for the IEX feed only.")
        if end is None:
            end = default_end_date()
        if start > end:
            raise ValueError("The start date must be on or before the end date.")

        self.start = start
        self.end = end
        self.feed_name = feed.lower()
        self.store_path = store_path.expanduser().resolve()
        self.manifest_path = (
            manifest_path.expanduser().resolve()
            if manifest_path
            else Path("data/metadata/alpaca_ingestion_manifest.json").resolve()
        )

        self.historical_provider = AlpacaHistoricalDataProvider(
            stock_client=StockHistoricalDataClient(api_key, secret_key),
            feed=DataFeed.IEX,
        )
        self.corporate_actions_provider = AlpacaCorporateActionsProvider(
            actions_client=CorporateActionsClient(api_key, secret_key),
        )

        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)

        self.storage_client = ArcticDBClient(self.store_path)
        self.repository = ArcticDBRepository(self.storage_client)
        self.manifest = IngestionManifest(
            path=self.manifest_path,
            feed_name=self.feed_name,
            start=self.start,
            end=self.end,
        )

    def _write_bars(
        self,
        symbol: str,
        adjustment: str,
        frame: pd.DataFrame,
    ) -> None:
        if frame.empty:
            LOGGER.warning(
                "%s (%s): no bars returned; nothing written.",
                symbol,
                adjustment,
            )
            return

        self.repository.write_bars(
            symbol=symbol,
            adjustment=adjustment,
            frame=frame,
            feed=self.feed_name,
            start=self.start,
            end=self.end,
        )

    def _write_instrument_metadata(
        self,
        instruments: tuple[Instrument, ...],
    ) -> None:
        frame = instrument_frame(instruments)

        self.repository.write_instrument_metadata(
            frame=frame,
            instrument_count=len(instruments),
            etf_count=sum(item.asset_class == "etf" for item in instruments),
            corporate_count=sum(item.asset_class == "equity" for item in instruments),
        )

    def _ingest_symbol(
        self,
        instrument: Instrument,
        adjustment: str,
        *,
        resume: bool,
    ) -> dict[str, Any]:
        symbol = instrument.symbol

        if self.manifest.already_complete(symbol, adjustment, resume):
            LOGGER.info(
                "%s (%s): already complete; skipping.",
                symbol,
                adjustment,
            )
            return self.manifest.get_result(symbol, adjustment)

        frame = self.historical_provider.fetch_daily_bars(
            symbol=symbol,
            start=self.start,
            end=self.end,
            adjustment=adjustment,
        )

        issues = validate_bars(frame, symbol)
        fatal = [issue for issue in issues if "no bars returned" not in issue]

        if fatal:
            raise ValueError("; ".join(fatal))

        self._write_bars(symbol, adjustment, frame)

        result = {
            "symbol": symbol,
            "adjustment": adjustment,
            "rows": len(frame),
            "first_timestamp": (frame.index.min().isoformat() if not frame.empty else None),
            "last_timestamp": (frame.index.max().isoformat() if not frame.empty else None),
            "status": "empty" if frame.empty else "complete",
            "completed_at_utc": datetime.now(UTC).isoformat(),
            "quality_issues": issues,
        }

        self.manifest.record(symbol, adjustment, result)

        LOGGER.info(
            "%s (%s): %d rows (%s to %s)",
            symbol,
            adjustment,
            result["rows"],
            result["first_timestamp"],
            result["last_timestamp"],
        )

        return result

    def ingest_bars(
        self,
        instruments: tuple[Instrument, ...] = INITIAL_UNIVERSE,
        *,
        resume: bool = True,
    ) -> list[dict[str, Any]]:
        return run_backfill(
            instruments,
            resume=resume,
            write_metadata=self._write_instrument_metadata,
            ingest_symbol=self._ingest_symbol,
        )

    def ingest_corporate_actions(
        self,
        instruments: tuple[Instrument, ...] = INITIAL_UNIVERSE,
    ) -> int:
        symbols = [item.symbol for item in instruments]

        frame = self.corporate_actions_provider.fetch_corporate_actions(
            symbols=symbols,
            start=self.start,
            end=self.end,
        )

        if frame.empty:
            LOGGER.info("No corporate actions returned for the selected universe.")
            return 0

        process_dates = pd.to_datetime(
            frame["process_date"],
            utc=True,
            errors="coerce",
        )

        # ArcticDB needs a sortable time index. Nanosecond offsets make same-day
        # events unique while preserving the unmodified process_date in a column.
        frame["_process_timestamp"] = process_dates
        frame = frame.sort_values(
            ["_process_timestamp", "symbol", "action_type"],
            kind="stable",
        )

        offsets = frame.groupby("_process_timestamp", sort=False).cumcount()

        frame.index = pd.DatetimeIndex(
            frame["_process_timestamp"] + pd.to_timedelta(offsets, unit="ns"),
            name="event_timestamp",
        )

        frame = frame.drop(columns=["_process_timestamp"]).sort_index()

        return self.repository.write_corporate_actions(
            frame=frame,
            metadata={
                "provider": "Alpaca",
                "endpoint": "corporate_actions",
                "requested_start": self.start.isoformat(),
                "requested_end": self.end.isoformat(),
                "symbol_count": len(symbols),
                "retrieved_at_utc": datetime.now(UTC).isoformat(),
            },
        )

    def run(self, *, resume: bool = True, include_corporate_actions: bool = True) -> None:
        self.ingest_bars(resume=resume)
        action_count = 0
        if include_corporate_actions:
            action_count = self.ingest_corporate_actions()

        LOGGER.info(
            "Ingestion finished: %d instruments, %d corporate actions. Store: %s",
            len(INITIAL_UNIVERSE),
            action_count,
            self.store_path,
        )


def create_ingestor_from_environment(
    *,
    store_path: Path | None = None,
    start: date = date(2016, 1, 1),
    end: date | None = None,
    feed: str = "iex",
) -> AlpacaDatasetIngestor:
    api_key = os.getenv("APCA_API_KEY_ID")
    secret_key = os.getenv("APCA_API_SECRET_KEY")
    if not api_key or not secret_key:
        raise RuntimeError("Set APCA_API_KEY_ID and APCA_API_SECRET_KEY in the environment.")

    if store_path is None:
        configured_path = os.getenv("FINWORLDMODEL_ARCTICDB_PATH")
        store_path = Path(configured_path) if configured_path else Path("data/arcticdb")

    return AlpacaDatasetIngestor(
        api_key=api_key,
        secret_key=secret_key,
        store_path=store_path,
        feed=feed,
        start=start,
        end=end,
    )
