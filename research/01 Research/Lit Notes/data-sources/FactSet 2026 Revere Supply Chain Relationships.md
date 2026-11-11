---
type: lit-note
title: FactSet Revere Supply Chain Relationships (WRDS and Aalto data guide)
authors:
- FactSet
year: 2026
venue: Vendor and library documentation
source_url: https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/factset/
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.8
- RQ3.7
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# FactSet Revere Supply Chain Relationships (WRDS and Aalto data guide) (FactSet, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** FactSet Revere links global companies to customers, suppliers, partners and competitors from 2003, with start and end dates per relationship and weekly updates, but only under subscription (academic licences: non-commercial research only).

## Problem
A commercial, dated source of company relationships.

## Data and period
Not applicable.

## Method
WRDS FactSet vendor page (product table) and the Aalto University data-hub entry (licence, fields), both opened 2026-11-08.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- WRDS: date range from 2003-04-03; weekly updates; customers, suppliers, partners, competitors.
- Aalto: relationship start and end dates; 2003–present; CSV/Parquet; licence "Academic and non-commercial research purposes only".
- FactSet Ownership on WRDS: institutional and insider ownership, 17+ years, 120 countries.

## Limits and risks to validity
Price not public. Start/end dates give valid time, but not when FactSet learned of a link (knowledge time), so back-filled links may leak (project reading; RQ3.7). Independent coverage check: [[Bacilieri 2023 Firm-level Production Networks]].

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Academic and non-commercial research purposes only" (Aalto data hub)
