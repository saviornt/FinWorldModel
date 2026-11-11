---
type: lit-note
title: 'DuckDB: Reading and Writing Parquet Files'
authors:
- DuckDB Foundation
year: 2026
venue: Engineering documentation
source_url: https://duckdb.org/docs/2.0/data/parquet/overview.html
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.5
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# DuckDB: Reading and Writing Parquet Files (DuckDB Foundation, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** DuckDB queries Parquet files in place with column and filter pushdown (zonemaps), reads many files or Hive-partitioned folders as one table, and writes Parquet with chosen compression; versioning is not part of this layer.

## Problem
Whether plain Parquet files plus an embedded SQL engine can serve as the research store.

## Data and period
Not applicable.

## Method
`SELECT * FROM 'file.parquet'` or `read_parquet()`; projection pushdown reads only needed columns; filter pushdown skips row groups using zonemaps; globs and directory paths read many files; `hive_partitioning`, `filename` and `union_by_name` options; `COPY ... (FORMAT parquet)` with Snappy default, zstd and others.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Parquet described as compressed columnar files "efficient to load and process".
- Filters can skip parts of a file using built-in zonemaps if present.
- Many files read as one table; `union_by_name` unifies differing schemas.
- Page does not describe update or append limits: Parquet files are written whole, so history is kept by writing new files (project reading, not stated on the page).

## Limits and risks to validity
Documentation only; no speed figures on this page. Point-in-time reads must be built by the user (e.g. ingestion-dated partitions or a table format); DuckDB itself is MIT-licensed (not stated on this page; not checked).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Parquet files are compressed columnar files that are efficient to load and process."
