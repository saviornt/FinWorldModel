from __future__ import annotations

import json
from datetime import date, datetime
from typing import TYPE_CHECKING, Any

import pandas as pd
from alpaca.data.models.corporate_actions import CorporateActionsSet
from alpaca.data.requests import CorporateActionsRequest

if TYPE_CHECKING:
    from collections.abc import Sequence

    from alpaca.data.historical.corporate_actions import CorporateActionsClient


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, (date, datetime, pd.Timestamp)):
        return value.isoformat()

    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")

    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}

    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]

    return str(value)


def _flatten_action(action_type: str, action: Any) -> dict[str, Any]:
    if hasattr(action, "model_dump"):
        payload = action.model_dump(mode="json")
    elif isinstance(action, dict):
        payload = action
    else:
        payload = vars(action)

    record = {"action_type": action_type}
    record.update({key: _json_safe(value) for key, value in payload.items()})

    for key, value in tuple(record.items()):
        if isinstance(value, (dict, list)):
            record[key] = json.dumps(value, sort_keys=True)

    return record


class AlpacaCorporateActionsProvider:
    def __init__(
        self,
        actions_client: CorporateActionsClient,
    ) -> None:
        self.actions_client = actions_client

    def fetch_corporate_actions(
        self,
        symbols: Sequence[str],
        start: date,
        end: date,
    ) -> pd.DataFrame:
        if start > end:
            raise ValueError("Start date cannot be later than end date.")

        request = CorporateActionsRequest(
            symbols=list(symbols),
            start=start,
            end=end,
            limit=1000,
        )

        response = self.actions_client.get_corporate_actions(request)

        if not isinstance(response, CorporateActionsSet):
            raise TypeError(f"Expected Alpaca CorporateActionsSet response, received {type(response).__name__}.")

        records: list[dict[str, Any]] = []

        for action_type, actions in response.data.items():
            for action in actions:
                records.append(_flatten_action(action_type, action))

        if not records:
            return pd.DataFrame()

        frame = pd.DataFrame.from_records(records)

        if "process_date" not in frame:
            raise ValueError("Corporate action response did not contain process_date.")

        process_dates = pd.to_datetime(
            frame["process_date"],
            utc=True,
            errors="coerce",
        )

        if process_dates.isna().any():
            raise ValueError("One or more corporate actions have invalid process_date.")

        return frame
