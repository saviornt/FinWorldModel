---
type: lit-note
title: 'Time in XTDB: bitemporal SQL'
authors:
- JUXT
year: 2026
venue: Engineering documentation
source_url: https://docs.xtdb.com/about/time-in-xtdb.html
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.5
- RQ3.8
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# Time in XTDB: bitemporal SQL (JUXT, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** XTDB makes every table bitemporal: system time kept by the database and user-set valid time, queried with SQL:2011 `FOR SYSTEM_TIME AS OF` and `FOR VALID_TIME AS OF`; updates never erase old versions.

## Problem
How a database can answer both 'what was true then' and 'what did we know then'.

## Data and period
Not applicable.

## Method
Columns `_system_from/_system_to` (database-maintained) and `_valid_from/_valid_to` (user-editable); temporal clauses opt-in; inserts act as upserts that keep old versions; `UPDATE ... FOR PORTION OF VALID_TIME` for past or future corrections.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- System-time queries show what was known at a moment without later corrections: the property a look-ahead-free backtest needs.
- Valid-time queries show the corrected history.
- Standard SQL without temporal clauses behaves like an ordinary database.

## Limits and risks to validity
Documentation only; no performance data; licence not stated on the page (not checked). Smaller ecosystem than Postgres or DuckDB; a server to run (project reading).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "full temporal history" remains available after updates and deletes.
