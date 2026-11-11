---
type: lit-note
title: Tick Data US equities historical intraday
authors:
- Tick Data LLC
year: 2026
venue: Vendor product page
source_url: https://tickdata.com/product/us-equities
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.1
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# Tick Data US equities historical intraday (Tick Data LLC, 2026)

**Basis:** opened 2026-11-08: [US equities product page](https://tickdata.com/product/us-equities).

**Takeaway:** Consolidated-tape tick trades and quotes for all CTA participants since 1993 (NBBO and quote bars since 2004), including delisted and merged symbols, with corporate-action files and ticker mapping; delivered as text files; price only on request.

## Problem
Long tick history with survivorship handling.

## Data and period
Trades and quotes since 1993-01-01; NBBO quotes and 1-minute quote bars from 2004-01-01.

## Method
Tick-by-tick Level I quotes, trades, NBBO; 1-minute trade and quote bars; custom bars via TickWrite. Inactive symbols included; splits, dividends, spin-offs files; ticker mapping; adjustment on request. Zipped CSV via TickWrite or TickAPI.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Longest tick history read (1993).
- Survivorship handled at order time (inactive symbols included).

## Limits and risks to validity
No public price (quote form). File delivery, not an incremental API: a fetch-once design would treat it as a one-off bulk purchase.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- None needed.
