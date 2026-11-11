---
type: lit-note
title: 'Airbyte: incremental sync, append + deduped'
authors:
- Airbyte
year: 2026
venue: Engineering documentation
source_url: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped
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
# Airbyte: incremental sync, append + deduped (Airbyte, 2026)

**Basis:** documentation opened 2026-11-08.

**Takeaway:** Cursor-plus-primary-key incremental syncs keep a full append-only history table and a deduplicated final table; delivery is at-least-once, so duplicates must be expected, and records that change without moving the cursor are missed.

## Problem
Incremental, restartable ingestion and its failure modes.

## Data and period
Not applicable.

## Method
Cursor selects records above the last synced value; primary key deduplicates the final table by keeping the latest row by cursor; history table keeps every version.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- At-least-once delivery; sources should resend when a cursor is ambiguous (e.g. date-only cursors).
- Missed updates when the cursor is not bumped on change.

## Limits and risks to validity
Late-arriving records and cursor ties not addressed on the page.

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "appended to the existing history data in the data warehouse" (append + deduped page)
