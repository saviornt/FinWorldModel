---
type: lit-note
title: 'pgvector: open-source vector similarity search for Postgres'
authors:
- pgvector contributors
year: 2026
venue: Engineering documentation
source_url: https://github.com/pgvector/pgvector
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
# pgvector: open-source vector similarity search for Postgres (pgvector contributors, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** pgvector stores embeddings next to relational data in Postgres, with exact search by default and HNSW or IVFFlat approximate indexes; filtered approximate queries can return too few rows unless iterative index scans (0.8.0+) are used.

## Problem
Whether text embeddings can live in the same Postgres database as other research data.

## Data and period
Not applicable.

## Method
Extension adding `vector`, `halfvec`, `bit` and `sparsevec` types. HNSW: better speed-recall, slower build, more memory, no training step. IVFFlat: faster build, lower recall at equal speed, build after data is loaded. Iterative scans continue until enough filtered rows are found, up to limits such as `hnsw.max_scan_tuples` (20,000).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Indexed `vector` up to 2,000 dimensions (`halfvec` 4,000); storage up to 16,000.
- Exact nearest neighbour by default; adding an approximate index can change results.
- With approximate indexes, WHERE filters apply after the scan: a 10% filter with default `ef_search` 40 returns about 4 rows.
- For very selective filters, B-tree, partial indexes or partitioning may work better.

## Limits and risks to validity
Project README; licence name not shown in the fetched text (not confirmed here). No speed figures. A 3,080-value embedding (sentiment module design) exceeds the 2,000-dimension HNSW limit for `vector` unless reduced (e.g. the 264-feature PCA output) or stored as `halfvec` (project reading).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Open-source vector similarity search for Postgres"
