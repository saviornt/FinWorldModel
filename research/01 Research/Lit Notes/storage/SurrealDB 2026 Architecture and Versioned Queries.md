---
type: lit-note
title: SurrealDB architecture and SELECT VERSION
authors:
- SurrealDB
year: 2026
venue: Engineering documentation
source_url: https://surrealdb.com/docs/surrealdb/introduction/architecture
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
# SurrealDB architecture and SELECT VERSION (SurrealDB, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** SurrealDB 4.0 puts document, graph (RELATE edges), vector, full-text and time-ordered records on one transactional key-value layer; time-travel `SELECT ... VERSION` works only on the SurrealKV engine with versioning enabled.

## Problem
Whether one multi-model database could hold documents, company graph, embeddings and time-versioned records.

## Data and period
Not applicable.

## Method
Architecture page: one query engine with snapshot isolation; swappable storage (SurrealKV single-node/embedded, SurrealMX in-memory, SurrealDS distributed enterprise); RocksDB is the predecessor engine, migrated by SurrealKV 1.0. SELECT page: `VERSION` clause for time-travel queries, SurrealKV only.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- One engine covers documents, graph edges, vectors and time-range scans.
- Time travel is engine-specific (SurrealKV with versioning); in-memory engine rejects it.
- Engines changed across major versions (pre-4.0 table differs), a sign of a fast-moving product.

## Limits and risks to validity
Documentation only; no performance data; licence not stated on the pages read (licence FAQ not opened). Maturity: engine line-up changed in 4.0; on-disk format stability claimed only for SurrealKV 1.0. VERSION reads give transaction-time (as-stored) views, not valid time (project reading).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Each engine must support transactional read and write of individual keys and key ranges." (architecture page)
