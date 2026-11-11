---
type: lit-note
title: 'LanceDB tables: versioning, time travel and tags'
authors:
- LanceDB
year: 2026
venue: Engineering documentation
source_url: https://docs.lancedb.com/management/table.md
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
# LanceDB tables: versioning, time travel and tags (LanceDB, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** LanceDB (on the Lance columnar format) commits a new version on every write, lets you check out or restore any version or tag, and prunes untagged versions older than a retention window (7 days by default) during optimize.

## Problem
Whether an embedded vector store keeps point-in-time copies of embeddings and features.

## Data and period
Not applicable.

## Method
Every write commits a version; `checkout(version)` or a tag reads a past version; `restore(version)` writes a new version; tags label versions and tagged versions are never pruned; `optimize()` prunes by `cleanup_older_than` (7 days default) (table management page). Lance format guide: datasets immutable, deletes via deletion files, compaction keeps old versions, rewritten files drop out of ANN indexes until rebuilt.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Version-per-write gives free time travel for embeddings and feature tables.
- Default 7-day retention means old versions vanish unless tagged: point-in-time copies must be tagged deliberately.
- Rewriting/compacting files invalidates parts of ANN indexes (Lance guide).

## Limits and risks to validity
Documentation only; licence not stated on the pages read (Lance is described elsewhere as Apache 2.0; not confirmed this session). No performance figures.

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "tagged versions are never pruned" (table management page)
- "Each write operation creates a new version of the dataset" (Lance guide)
