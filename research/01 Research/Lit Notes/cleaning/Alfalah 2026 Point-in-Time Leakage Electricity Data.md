---
type: lit-note
title: 'The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data'
authors:
- Abdelkrim Alfalah
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2610.25389
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.1
- RQ3.2
- RQ3.8
family:
- cleaning
evidence: Moderate
score: 7
tags:
- lit-note
- family/cleaning
- timestamps
- leakage
---
# The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data (Alfalah, 2026)

**Basis:** full text via alphaXiv, opened 2026-11-08 (abstract, introduction, timestamp-validation section).

**Takeaway:** Choosing "the latest forecast run issued before the gate" by its issue time picks a run that was not yet published at the gate on more than 99% of days for six of ten weather-model configurations at one gate, because runs appear hours after their label time and keep changing; the leak's apparent accuracy gain ranges from −9% to +24%, so it must be measured, not assumed.

## Problem
Are "information available at decision time" claims true for vendor archives with several timestamps per record?

## Data and period
Timestamps of 128,656 weather-forecast runs (ten configurations) from a commercial energy-data vendor, matched to Great Britain day-ahead and intraday auction gates, 2022–2026.

## Method
Separate issue time, first-availability time and completion time; the author polled the vendor interface every 60 s for one evening to validate the field meanings; compare inputs selected by issue time with inputs truly available at each gate.

## Baselines and validation
Correct (available-at-gate) inputs vs naive (issue-time) inputs; accuracy compared across variables, models, gates and seasons.

## Results (with page or section references)
- Naive selection uses an unpublished run on >99% of days for 6 of 10 configurations at one gate; for GFS at the day-ahead gate, 0.6% in winter and 99.8% in summer (abstract).
- Exposure drifts as publication delays change; a few minutes' margin can cost a six-hour cycle (abstract).
- Other pitfalls: local-clock gates vs UTC archives; outturn series revised without keeping old values (abstract).

## Limits and risks to validity
Electricity and weather, not equities, but the failure (issue time vs availability time; revisions overwritten) transfers directly to news, filings and vendor macro data. One vendor, one market. Statistical testing not seen in the parts read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Data-timing audit |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Subject of the paper; field meanings validated |
| Costs and realism | N/A | |
| Sample breadth | 1 | One market, ten models, four years |
| Statistical testing | 0 | Not seen in parts read |
| Reproducibility | 1 | Audit protocol described; vendor data licensed |
| **Total** | 4/8 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "point-in-time correctness is a dynamic property of the data pipeline" (abstract)
