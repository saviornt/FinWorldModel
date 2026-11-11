---
type: lit-note
title: RocksDB overview
authors:
- Meta Platforms
year: 2026
venue: Engineering documentation
source_url: https://github.com/facebook/rocksdb/wiki/RocksDB-Overview
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
# RocksDB overview (Meta Platforms, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** RocksDB is an embeddable LSM key-value library (byte keys and values, sorted) with snapshots, column families and transactions, but no query language or time-series features; everything above key-value must be built, and compaction tuning is the main upkeep.

## Problem
Whether a raw key-value engine is a sensible base store for a solo researcher.

## Data and period
Not applicable.

## Method
Wiki overview: Get/Put/Delete/DeleteRange, atomic write batches, iterators and snapshots for point-in-time views, column families, optimistic and pessimistic transactions, WAL, Level/Universal/FIFO compaction, compaction filters, TTL via StackableDB.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Snapshots give point-in-time reads but do not survive restarts.
- No query language or time-series layer: indexing, as-of logic and schemas are the user's code.
- Operators tune compaction (write/space/read amplification), memtable flush threads and caches.

## Limits and risks to validity
Documentation only. Licence not stated on the page read. Relevant mainly as the engine under other systems (SurrealDB's former engine, many others), not as a research store on its own (project reading).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "efforts are also made to limit the number of knobs"
