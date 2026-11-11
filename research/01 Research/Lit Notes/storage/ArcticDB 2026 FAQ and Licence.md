---
type: lit-note
title: ArcticDB FAQ, Library API and licence
authors:
- Man Group
year: 2026
venue: Engineering documentation
source_url: https://docs.arcticdb.io/latest/faq/
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.5
- RQ2.4
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# ArcticDB FAQ, Library API and licence (Man Group, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** Embedded, Python-only DataFrame store on LMDB or S3-type object storage with versioning on by default (reads as of a version or snapshot); free to use, but production use needs a paid licence under BSL 1.1.

## Problem
Whether a versioned DataFrame store suits a solo researcher keeping point-in-time market data.

## Data and period
Not applicable.

## Method
No server; installs as a Python package. Backends verified: LMDB, in-memory, AWS S3, Azure Blob, MinIO, Ceph and others (FAQ). Every write creates a version; named snapshots pin versions across symbols; `prune_previous_versions` drops non-snapshotted old versions (Library API). Deduplication against the previous version is optional and works best for appends (FAQ).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Versioning on by default; supports daily appends and historical corrections, for point-in-time analysis (FAQ).
- Analytical (OLAP) design; last-writer-wins, no transaction isolation; one writer per symbol unless staged writes (FAQ).
- Python only, no SQL; streaming/tick support listed as roadmap (FAQ).
- Licence: Business Source License 1.1; source available and free to use, but not for production use or a database service without an agreement; each version converts to Apache 2.0 later (e.g. 6.21 on 2028-08-04) (GitHub README).
- No benchmark numbers on the FAQ or README; README claims a 20-year history of 400,000+ securities in one symbol.

## Limits and risks to validity
Vendor documentation; no independent performance figures. Whether a solo research project counts as 'production use' under the BSL is a licence question (RQ2.6), not answered here. Many versions grow storage; pruning tools are partly enterprise. The Library API page was read only in part (fetch truncated before the `read`/`as_of` detail).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "ArcticDB is an embedded database engine" (FAQ)
- "Changes to symbols are performed on a last-writer-wins principle." (FAQ)
