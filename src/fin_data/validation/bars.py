"""Provider-independent OHLCV validation"""

import pandas as pd


def validate_bars(
    frame: pd.DataFrame,
    symbol: str,
) -> list[str]:
    """Validate normalized OHLCV bar data.

    Returns a list of validation issues. An empty list indicates
    that no validation problems were detected.
    """
    issues: list[str] = []

    required_columns = (
        "open",
        "high",
        "low",
        "close",
        "volume",
    )

    if frame.empty:
        return [f"{symbol}: no bars returned."]

    missing_columns = [column for column in required_columns if column not in frame.columns]

    if missing_columns:
        return [f"{symbol}: missing required columns: {', '.join(missing_columns)}."]

    # Ensure required fields contain numeric values.
    numeric = frame.loc[:, required_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    for column in required_columns:
        if numeric[column].isna().any():
            issues.append(f"{symbol}: {column} contains missing or non-numeric values.")

    # Evaluate OHLCV constraints using vectorized Pandas operations.
    checks = {
        "high is below low": numeric["high"] < numeric["low"],
        "negative volume": numeric["volume"] < 0,
        "high is below open": numeric["high"] < numeric["open"],
        "high is below close": numeric["high"] < numeric["close"],
        "low is above open": numeric["low"] > numeric["open"],
        "low is above close": numeric["low"] > numeric["close"],
        "non-positive open": numeric["open"] <= 0,
        "non-positive high": numeric["high"] <= 0,
        "non-positive low": numeric["low"] <= 0,
        "non-positive close": numeric["close"] <= 0,
    }

    for message, violations in checks.items():
        if violations.any():
            issues.append(f"{symbol}: {message}.")

    # Timestamp integrity.
    if frame.index.has_duplicates:
        issues.append(f"{symbol}: duplicate timestamps detected.")

    if not frame.index.is_monotonic_increasing:
        issues.append(f"{symbol}: timestamps are not chronologically ordered.")

    return issues
