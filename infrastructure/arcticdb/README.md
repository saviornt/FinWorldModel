
# ArcticDB Infrastructure

## Backend

- Engine: ArcticDB
- Storage backend: LMDB
- Deployment: Embedded Python library
- Initialization: scripts/initialize_arcticdb.py

## Storage

Default location:

    data/arcticdb/

Override with:

    FINWORLDMODEL_ARCTICDB_PATH

## Initial Libraries

- market_data: Historical and current market observations.
- macro_data: Economic indicators and macroeconomic time series.

Additional libraries will be introduced as data requirements evolve.

## Health Verification

Run:

    uv run python scripts/initialize_arcticdb.py

The script verifies initialization, library accessibility,
write/read functionality, data integrity, and cleanup.
