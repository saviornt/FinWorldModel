---
type: lit-note
title: "CRSP Names File for Historical Company Names, Tickers & CUSIPs (FAQ)"
authors: [Stanford GSB Library]
year: 2026
venue: Stanford GSB Research Help knowledge base
source_url: https://gsb-research-help.stanford.edu/library/faq/391109
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.8]
family: [data-sources]
evidence: Primary documentation
tags: [lit-note, family/data-sources, entity-identity]
---
# CRSP Names File FAQ (Stanford GSB)

**Basis:** FAQ page read via page fetch on 2026-11-08.

**Takeaway:** CRSP's Stock Events Names file gives each name/ticker/CUSIP spell with a start ("date of observation") and end date; tickers are reused (the ticker "S" went from Sears to Sprint Nextel in 2005 and to SentinelOne in 2021) and names change (Facebook → Meta), so joins must be on a permanent ID plus date range, never on ticker or name alone.

## Problem / Data / Method
Library guidance on matching names and tickers to CRSP over time.

## Baselines and validation
N/A.

## Results (with page or section references)
- Names records carry start and end dates (example table).
- Ticker "S" reassignment 2005 and 2021; Facebook → Meta 2021.

## Limits and risks to validity
Library guide, not CRSP's own manual.

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
