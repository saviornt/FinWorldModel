"""Constants for Alpaca data provider."""

from alpaca.data.enums import Adjustment

BAR_COLUMNS = ("open", "high", "low", "close", "volume", "trade_count", "vwap")
ADJUSTMENTS = {
    "raw": Adjustment.RAW,
    "all": Adjustment.ALL,
}
