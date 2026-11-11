---
type: lit-note
title: MongoDB time series collection limitations
authors:
- MongoDB
year: 2026
venue: Engineering documentation
source_url: https://www.mongodb.com/docs/manual/core/timeseries/timeseries-limitations/
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
# MongoDB time series collection limitations (MongoDB, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** MongoDB time series collections bucket measurements for compression but restrict updates (metaField only), forbid writes in transactions, unique and text indexes, and schema validation, so corrections and point-in-time versioning must be designed around them.

## Problem
Whether MongoDB time series collections fit a research store that must record corrections.

## Data and period
Not applicable.

## Method
Official limitations page (MongoDB 8.x).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Updates may only match and modify the `metaField`; no upsert.
- No writes in transactions; reads allowed.
- No unique or text indexes; no schema validation; `timeField`/`metaField` fixed at creation.
- Buckets hold at most 1,000 measurements or 125 KB.
- Change streams and triggers not supported.

## Limits and risks to validity
Documentation of limits, not performance. No versioned/as-of read feature; history would need explicit version fields or separate collections (project reading). Server upkeep. Licence (SSPL) not read this session.

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- None kept (page read through a summarising fetch tool; no exact wording confirmed).
