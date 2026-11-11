"""ArcticDB connection and library initialization"""

from __future__ import annotations

from typing import TYPE_CHECKING

from arcticdb import Arctic

if TYPE_CHECKING:
    from pathlib import Path

    from arcticdb.version_store.library import Library


class ArcticDBClient:
    def __init__(self, store_path: Path) -> None:
        self.store_path = store_path.expanduser().resolve()
        self.store_path.mkdir(parents=True, exist_ok=True)

        uri = f"lmdb://{self.store_path}"
        self.arctic = Arctic(uri)

        self.raw_library: Library = self.arctic.get_library(
            "bars_daily_raw",
            create_if_missing=True,
        )

        self.adjusted_library: Library = self.arctic.get_library(
            "bars_daily_all_adjusted",
            create_if_missing=True,
        )

        self.actions_library: Library = self.arctic.get_library(
            "corporate_actions",
            create_if_missing=True,
        )

        self.metadata_library: Library = self.arctic.get_library(
            "dataset_metadata",
            create_if_missing=True,
        )
