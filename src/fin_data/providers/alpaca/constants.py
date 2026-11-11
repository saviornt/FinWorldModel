"""Constants for Alpaca data provider."""

from alpaca.data.enums import Adjustment

BAR_COLUMNS = ("open", "high", "low", "close", "volume")
ADJUSTMENTS = {
    "raw": Adjustment.RAW,
    "all": Adjustment.ALL,
}
