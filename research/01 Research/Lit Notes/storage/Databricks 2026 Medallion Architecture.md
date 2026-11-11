---
type: lit-note
title: What is the medallion lakehouse architecture?
authors:
- Databricks
year: 2026
venue: Engineering documentation
source_url: https://docs.databricks.com/aws/en/lakehouse/medallion
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.4
- RQ2.5
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# What is the medallion lakehouse architecture? (Databricks, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** Keep a bronze layer that stores source data raw and as-is, append-only, with provenance columns, so everything downstream can be rebuilt; validation and schema evolution happen in silver, never at ingestion.

## Problem
How to layer raw and cleaned data so ingestion is done once and processing can be replayed.

## Data and period
Not applicable.

## Method
Bronze: "raw, unvalidated data", kept "in its original formats", "appended incrementally", with provenance metadata (e.g. source file name). Store most fields as string, VARIANT or binary to survive schema changes. Silver: validated, cleaned, enriched; schema evolution. Gold: refined views. Streaming (incremental) reads from append-only bronze; do not write silver directly from ingestion.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Bronze "Enables reprocessing and auditing by retaining all historical data."

## Limits and risks to validity
Vendor-oriented (Databricks); the pattern is generic. Ingestion time as a column is not mentioned (only provenance), which matters for knowledge-time (RQ3.8).

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Enables reprocessing and auditing by retaining all historical data." (medallion page)
