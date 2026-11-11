---
type: lit-note
title: 'QuestDB: ASOF JOIN, deduplication and licence'
authors:
- QuestDB
year: 2026
venue: Engineering documentation
source_url: https://questdb.com/docs/reference/sql/asof-join/
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
# QuestDB: ASOF JOIN, deduplication and licence (QuestDB, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** QuestDB (Apache 2.0) is a time-series SQL server with a native ASOF JOIN (latest row at or before each timestamp, optionally per key with a tolerance) and upsert-key deduplication that makes reloads idempotent; its speed figures are vendor-reported.

## Problem
Whether a dedicated time-series database gives point-in-time joins and idempotent loads out of the box.

## Data and period
Not applicable.

## Method
ASOF JOIN matches each left row to the most recent right row at or before its timestamp; `ON` restricts to equal keys (e.g. symbol); `TOLERANCE` rejects stale matches; inputs must be time-ordered (ASOF JOIN page). Deduplication on WAL tables with UPSERT KEYS that must include the designated timestamp: identical rows are skipped, different rows replace the old one (last write wins) (deduplication page). GitHub README for licence and benchmarks.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- ASOF JOIN is the point-in-time join needed to attach the prevailing value (e.g. last quote) to each event.
- Dedup makes re-ingesting a snapshot cheap; only affects new inserts.
- Last write wins: deduplication overwrites, so it does not keep knowledge-time history by itself.
- Licence: Apache-2.0 (README); Enterprise adds replication, tiering to object storage, RBAC.
- Vendor TSBS result (one AWS instance, 100k hosts): QuestDB 8.59M rows/s vs ClickHouse 1.75M, TimescaleDB 1.08M, InfluxDB 541K (README); page itself asks readers to run their own benchmarks.

## Limits and risks to validity
Vendor benchmarks only; no independent QuestDB benchmark was found this session. Using the `timestamp()` hint on unsorted data gives wrong results (ASOF page).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "designated timestamp must always be included in UPSERT KEYS" (deduplication page)
- "As always, we encourage you to run your own benchmarks." (README)
