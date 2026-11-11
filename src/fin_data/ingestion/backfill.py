"""Coordinates historical ingestion"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from collections.abc import Sequence

    from fin_data.universe.instruments import Instrument


class InstrumentMetadataWriter(Protocol):
    def __call__(
        self,
        instruments: tuple[Instrument, ...],
    ) -> None: ...


class SymbolIngester(Protocol):
    def __call__(
        self,
        instrument: Instrument,
        adjustment: str,
        *,
        resume: bool,
    ) -> dict[str, Any]: ...


def run_backfill(
    instruments: tuple[Instrument, ...],
    *,
    resume: bool,
    write_metadata: InstrumentMetadataWriter,
    ingest_symbol: SymbolIngester,
    adjustments: Sequence[str] = ("raw", "all"),
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []

    write_metadata(instruments)

    for instrument in instruments:
        for adjustment in adjustments:
            results.append(
                ingest_symbol(
                    instrument,
                    adjustment,
                    resume=resume,
                )
            )

    return results
