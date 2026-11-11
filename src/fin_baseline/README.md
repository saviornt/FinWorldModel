# Initial Alpaca historical dataset

This bundle adds the initial Alpaca-to-ArcticDB ingestion pipeline to the
`fin_baseline` section of the project. It does not add a third `src/` package.

## Dataset scope

- 10 ETFs and 26 listed corporations (36 instruments total).
- Daily bars beginning 2016-01-01.
- Alpaca IEX feed.
- Raw bars and `all`-adjusted bars are stored separately.
- Corporate actions are retrieved separately and stored in ArcticDB.
- The default end date is yesterday in `America/New_York`, avoiding an incomplete
  current-day daily candle.

IEX is an exchange-specific feed, not consolidated US market coverage. The
feed selection is intentional because it is the requested configuration.

## Files

- `src/fin_baseline/data/universe.py`: the instrument universe.
- `src/fin_baseline/data/alpaca.py`: API acquisition, validation and ArcticDB writes.
- `scripts/ingest_alpaca.py`: CLI entry point.
- `tests/data/test_alpaca_ingestion.py`: offline unit tests.

## Install

From the project root:

```fish
uv add alpaca-py
```

The project already has ArcticDB, pandas and pytest in its dependency set.

If pytest cannot import the `src/` package, add `pythonpath = ["src"]` to the
existing `[tool.pytest.ini_options]` table in `pyproject.toml`.

## Credentials (fish)

Set your Alpaca credentials in the current shell. Do not commit them or place
them in source files:

```fish
set -x APCA_API_KEY_ID "your-key-id"
set -x APCA_API_SECRET_KEY "your-secret-key"
```

## Run tests

```fish
uv run --all-groups pytest -v tests/data/test_alpaca_ingestion.py
```

## Run the initial backfill

```fish
uv run --all-groups python scripts/ingest_alpaca.py
```

Explicitly restating the agreed settings:

```fish
uv run --all-groups python scripts/ingest_alpaca.py --start 2016-01-01 --feed iex
```

To choose a specific completed end date:

```fish
uv run --all-groups python scripts/ingest_alpaca.py --start 2016-01-01 --end 2026-11-09
```

The default ArcticDB location is `data/arcticdb`. Override it with:

```fish
set -x FINWORLDMODEL_ARCTICDB_PATH "/absolute/path/to/arcticdb"
```

## ArcticDB layout

The pipeline creates these local libraries:

- `bars_daily_raw`: one symbol per ticker, raw OHLCV.
- `bars_daily_all_adjusted`: one symbol per ticker, Alpaca `all`-adjusted OHLCV.
- `corporate_actions`: one `all_actions` symbol, with event type and original
  process date retained as columns.
- `dataset_metadata`: the `initial_universe` instrument metadata table.

The `all`-adjusted data is not a substitute for point-in-time data. It is
provided as a convenience series for conventional total-return-style
benchmarking. For leakage-sensitive experiments, use raw observations plus
corporate-action records and construct features using only information
available at each prediction timestamp.

## Restart and repeat behavior

The script writes a local completion manifest to
`data/metadata/alpaca_ingestion_manifest.json`, updating it after each
symbol/adjustment pair. A rerun skips completed pairs with the same date range
and feed. If interrupted while processing a symbol, that symbol is retried.

Writes use ArcticDB `update(..., upsert=True)` rather than `append`, so
overlapping timestamps are replaced instead of duplicated. Use `--no-resume`
to re-fetch the requested range for every symbol.

The corporate-actions request is re-run on each invocation and the stored
`all_actions` symbol is replaced with the current response.

## Important limitations

1. Alpaca IEX data is not consolidated SIP data. It represents IEX activity
   only, so volume and bar availability can differ materially from market-wide
   observations.
2. Alpaca's corporate-actions endpoint is a separate source endpoint; it is not
   governed by the stock-bar `feed` selection.
3. The corporate-actions endpoint may have processing delays. Treat it as a
   provider snapshot, not proof that every event was known to the market at
   announcement time.
4. This first ingestion does not include fundamentals, news, macroeconomic
   series, entity relationships, or point-in-time executive/board history.
5. The initial universe contains 26 corporations, not 25, as in the supplied
   instrument table.
6. Review Alpaca's current data-use terms before redistributing data or
   incorporating it into a commercial data product.
