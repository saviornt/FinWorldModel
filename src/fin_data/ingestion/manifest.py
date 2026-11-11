"""Ingestion state, completion tracking, resume behavior"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from datetime import date
    from pathlib import Path

LOGGER = logging.getLogger(__name__)


class IngestionManifest:
    def __init__(
        self,
        path: Path,
        feed_name: str,
        start: date,
        end: date,
    ) -> None:
        self.path = path.expanduser().resolve()
        self.feed_name = feed_name
        self.start = start
        self.end = end

        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"completed": {}}

        try:
            manifest = json.loads(self.path.read_text(encoding="utf-8"))
        except OSError, json.JSONDecodeError:
            LOGGER.warning("Manifest could not be read; starting a new manifest.")
            return {"completed": {}}

        if not isinstance(manifest, dict):
            LOGGER.warning("Manifest has an invalid structure; starting a new manifest.")
            return {"completed": {}}

        if not isinstance(manifest.get("completed"), dict):
            LOGGER.warning("Manifest completion records are invalid; starting a new manifest.")
            return {"completed": {}}

        return manifest

    def save(self) -> None:
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(self.data, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        temporary.replace(self.path)

    def key(self, symbol: str, adjustment: str) -> str:
        return f"{symbol}:{adjustment}:{self.feed_name}:1Day:{self.start}:{self.end}"

    def already_complete(
        self,
        symbol: str,
        adjustment: str,
        resume: bool,
    ) -> bool:
        return resume and self.key(symbol, adjustment) in self.data["completed"]

    def get_result(
        self,
        symbol: str,
        adjustment: str,
    ) -> dict[str, Any]:
        return self.data["completed"][self.key(symbol, adjustment)]

    def record(
        self,
        symbol: str,
        adjustment: str,
        result: dict[str, Any],
    ) -> None:
        self.data["completed"][self.key(symbol, adjustment)] = result
        self.save()
