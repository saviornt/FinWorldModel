---
type: lit-note
title: 'dlt: incremental loading'
authors:
- dltHub
year: 2026
venue: Engineering documentation
source_url: https://dlthub.com/docs/general-usage/incremental-loading
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.4
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# dlt: incremental loading (dltHub, 2026)

**Basis:** documentation opened 2026-11-08 (overview page; the state and lag sub-pages were not opened).

**Takeaway:** An open-source Python loader that tracks a cursor (timestamp or ID) in pipeline state and offers append, replace and merge (upsert by primary key) dispositions; a failed extract does not touch destination data.

## Problem
Load only new or changed records from an API.

## Data and period
Not applicable.

## Method
Write dispositions: replace, append, merge (`merge_key` and/or `primary_key`). Cursor field tracks progress; lag option re-reads a recent window for late data. Full refresh does not deduplicate.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Loads are staged: "a failed extract or normalization does not affect destination data".

## Limits and risks to validity
State persistence and lag behaviour are on pages not read. A merge disposition overwrites history unless raw rows are kept separately.

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Track changes using a cursor field (like timestamp or ID)." (incremental loading)
