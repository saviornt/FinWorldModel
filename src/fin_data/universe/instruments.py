"""Initial Alpaca instruments & equities universe for the baseline prototype."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Instrument:
    """Instrument data class."""

    symbol: str
    asset_class: str
    role: str
    sector: str | None = None
    industry: str | None = None


ETF_UNIVERSE: tuple[Instrument, ...] = (
    Instrument("SPY", "etf", "Broad Equity Market"),
    Instrument("QQQ", "etf", "Technology Equity Market"),
    Instrument("IWM", "etf", "Small Cap Equity Market"),
    Instrument("DIA", "etf", "Large Cap Equity Market"),
    Instrument("TLT", "etf", "Treasury Bond Market"),
    Instrument("GLD", "etf", "Gold Market"),
    Instrument("USO", "etf", "Oil Exposure"),
    Instrument("XLF", "etf", "Financial Sector"),
    Instrument("XLK", "etf", "Technology Sector"),
    Instrument("XLE", "etf", "Energy Sector"),
)

CORPORATE_UNIVERSE: tuple[Instrument, ...] = (
    Instrument("MSFT", "equity", "Corporate entity", "Technology", "Software - Infrastructure"),
    Instrument("AAPL", "equity", "Corporate entity", "Technology", "Consumer Electronics"),
    Instrument("NVDA", "equity", "Corporate entity", "Technology", "Semiconductors"),
    Instrument("ASML", "equity", "Corporate entity", "Technology", "Semiconductor Equipment & Materials"),
    Instrument(
        "GOOGL",
        "equity",
        "Corporate entity",
        "Communication Services",
        "Internet Content & Information",
    ),
    Instrument("VZ", "equity", "Corporate entity", "Communication Services", "Telecom Services"),
    Instrument("AMZN", "equity", "Corporate entity", "Consumer Cyclical", "Internet Retail"),
    Instrument("TSLA", "equity", "Corporate entity", "Consumer Cyclical", "Auto Manufacturers"),
    Instrument("MCD", "equity", "Corporate entity", "Consumer Cyclical", "Restaurants"),
    Instrument("PG", "equity", "Corporate entity", "Consumer Defensive", "Household & Personal Products"),
    Instrument("WMT", "equity", "Corporate entity", "Consumer Defensive", "Discount Stores"),
    Instrument("XOM", "equity", "Corporate entity", "Energy", "Oil & Gas Integrated"),
    Instrument("SLB", "equity", "Corporate entity", "Energy", "Oil & Gas Equipment & Services"),
    Instrument("JPM", "equity", "Corporate entity", "Financial Services", "Banks - Diversified"),
    Instrument("V", "equity", "Corporate entity", "Financial Services", "Credit Services"),
    Instrument("CB", "equity", "Corporate entity", "Financial Services", "Insurance - Property & Casualty"),
    Instrument("JNJ", "equity", "Corporate entity", "Healthcare", "Drug Manufacturers - General"),
    Instrument("LLY", "equity", "Corporate entity", "Healthcare", "Drug Manufacturers - General"),
    Instrument("ISRG", "equity", "Corporate entity", "Healthcare", "Medical Instruments & Supplies"),
    Instrument("CAT", "equity", "Corporate entity", "Industrials", "Farm & Heavy Construction Machinery"),
    Instrument("UPS", "equity", "Corporate entity", "Industrials", "Integrated Freight & Logistics"),
    Instrument("RTX", "equity", "Corporate entity", "Industrials", "Aerospace & Defense"),
    Instrument("LIN", "equity", "Corporate entity", "Basic Materials", "Specialty Chemicals"),
    Instrument("FCX", "equity", "Corporate entity", "Basic Materials", "Copper"),
    Instrument("PLD", "equity", "Corporate entity", "Real Estate", "REIT - Industrial"),
    Instrument("NEE", "equity", "Corporate entity", "Utilities", "Utilities - Regulated Electric"),
)

INITIAL_UNIVERSE: tuple[Instrument, ...] = ETF_UNIVERSE + CORPORATE_UNIVERSE
etf_count = len(ETF_UNIVERSE)


def _validate_universe_size(name: str, universe: tuple[Instrument, ...], expected_count: int) -> None:
    """Validate that a universe matches the expected instrument count."""
    if len(universe) != expected_count:
        raise RuntimeError(f"{name} must contain {expected_count} instruments.")


def _validate_unique_symbols(universe: tuple[Instrument, ...]) -> None:
    """Validate that every instrument symbol is unique within the universe."""
    if len({item.symbol for item in universe}) != len(universe):
        raise RuntimeError("Duplicate symbols found in INITIAL_UNIVERSE.")


_validate_unique_symbols(INITIAL_UNIVERSE)
_validate_universe_size("ETF_UNIVERSE", ETF_UNIVERSE, 10)
_validate_universe_size("CORPORATE_UNIVERSE", CORPORATE_UNIVERSE, 26)
