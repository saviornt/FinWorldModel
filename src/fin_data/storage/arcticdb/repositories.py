"""Reading and writing market data"""

from __future__ import annotations

import json
from datetime import UTC, date, datetime
from typing import TYPE_CHECKING, Any

import pandas as pd

if TYPE_CHECKING:
    from fin_data.storage.arcticdb.client import ArcticDBClient


class ArcticDBRepository:
    def __init__(self, client: ArcticDBClient) -> None:
        self.client = client

    def write_bars(
        self,
        symbol: str,
        adjustment: str,
        frame: pd.DataFrame,
        feed: str,
        start: date,
        end: date,
    ) -> None:
        if frame.empty:
            return

        if adjustment == "raw":
            library = self.client.raw_library
        elif adjustment == "all":
            library = self.client.adjusted_library
        else:
            raise ValueError(f"Unsupported adjustment: {adjustment}")

        metadata = {
            "provider": "Alpaca",
            "feed": feed,
            "timeframe": "1Day",
            "adjustment": adjustment,
            "symbol": symbol,
            "requested_start": start.isoformat(),
            "requested_end": end.isoformat(),
            "retrieved_at_utc": datetime.now(UTC).isoformat(),
        }

        library.update(
            symbol,
            frame,
            metadata=metadata,
            upsert=True,
        )

    def write_corporate_actions(
        self,
        frame: pd.DataFrame,
        metadata: dict[str, Any],
    ) -> int:
        if frame.empty:
            return 0

        if "process_date" not in frame.columns:
            raise ValueError("Corporate actions are missing process_date.")

        incoming = frame.copy()

        if self.client.actions_library.has_symbol("all_actions"):
            existing = self.client.actions_library.read("all_actions").data

            if not isinstance(existing, pd.DataFrame):
                raise TypeError("Expected the existing corporate actions dataset to be a DataFrame.")

            combined = pd.concat([existing, incoming])
        else:
            combined = incoming

        process_dates = pd.to_datetime(
            combined["process_date"],
            utc=True,
            errors="coerce",
        )

        if process_dates.isna().any():
            raise ValueError("Corporate actions contain invalid process_date values.")

        combined["_process_timestamp"] = process_dates

        # Remove exact duplicate records before rebuilding the event index.
        combined = combined.drop_duplicates()

        # Produce a deterministic ordering for actions sharing a process date.
        combined["_action_key"] = combined.apply(
            lambda row: json.dumps(
                row.drop(
                    labels=["_process_timestamp"],
                    errors="ignore",
                ).to_dict(),
                sort_keys=True,
                default=str,
            ),
            axis=1,
        )

        sort_columns = [
            "_process_timestamp",
            "_action_key",
        ]

        combined = combined.sort_values(
            sort_columns,
            kind="stable",
        )

        offsets = combined.groupby(
            "_process_timestamp",
            sort=False,
        ).cumcount()

        combined.index = pd.DatetimeIndex(
            combined["_process_timestamp"] + pd.to_timedelta(offsets, unit="ns"),
            name="event_timestamp",
        )

        combined = combined.drop(
            columns=["_process_timestamp", "_action_key"],
        ).sort_index()

        self.client.actions_library.write(
            "all_actions",
            combined,
            metadata=metadata,
        )

        return len(combined)

    def write_instrument_metadata(
        self,
        frame: pd.DataFrame,
        instrument_count: int,
        etf_count: int,
        corporate_count: int,
    ) -> None:
        metadata_frame = frame.copy()
        metadata_frame.index.name = "symbol"

        self.client.metadata_library.write(
            "initial_universe",
            metadata_frame,
            metadata={
                "provider": "project-defined",
                "instrument_count": instrument_count,
                "etf_count": etf_count,
                "corporate_count": corporate_count,
            },
        )
