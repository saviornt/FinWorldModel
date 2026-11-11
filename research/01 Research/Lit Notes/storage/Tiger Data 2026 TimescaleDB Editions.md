---
type: lit-note
title: TimescaleDB editions (Apache 2 vs Community/TSL)
authors:
- Tiger Data
year: 2026
venue: Engineering documentation
source_url: https://www.tigerdata.com/docs/get-started/choose-your-path/timescaledb-editions
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
# TimescaleDB editions (Apache 2 vs Community/TSL) (Tiger Data, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** TimescaleDB's columnstore (compression), continuous aggregates and retention policies are only in the free Community Edition (Timescale License), which may be self-hosted but not sold as a service; the Apache 2 edition has core hypertables only.

## Problem
What a solo researcher gets from TimescaleDB for free and what licence applies.

## Data and period
Not applicable.

## Method
Feature table comparing the Apache 2 Edition with the Community Edition (TSL); `SHOW timescaledb.license;` reports the active edition.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Community-only: columnstore (Hypercore), continuous aggregates, retention policies, jobs, SkipScan, `time_bucket_gapfill`.
- Apache 2 has hypertables, `time_bucket`, basic hyperfunctions.
- TSL: free to self-host and modify; cannot be offered as a service.
- Community Edition described as "completely free if you manage your own service".

## Limits and risks to validity
Vendor page. Upkeep is that of a Postgres server (backups, upgrades, extension versions). Independent benchmarks (Barez 2023; Mostafa 2026) find TimescaleDB slow on several query types and with disk amplification; see those notes.

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "completely free if you manage your own service"
