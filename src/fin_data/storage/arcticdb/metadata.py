"""Dataset and instrument metadata persistence"""

from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from fin_data.universe.instruments import Instrument


def instrument_frame(instruments: tuple[Instrument, ...]) -> pd.DataFrame:
    rows = [asdict(item) for item in instruments]
    return pd.DataFrame(rows).set_index("symbol")
