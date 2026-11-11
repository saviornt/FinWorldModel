---
type: lit-note
title: Dissecting the Asset Growth Anomaly
authors:
- Fangjian Fu
year: 2014
venue: Working paper, Singapore Management University
source_url: https://core.ac.uk/download/35456666.pdf
doi: 10.2139/ssrn.2533316
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.1
- RQ3.3
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- survivorship
- delisting
---
# Dissecting the Asset Growth Anomaly (Fu, 2014)

**Basis:** working paper PDF via CORE (SMU institutional repository), opened 2026-11-08 through a summarising page fetch; figures below are from that reading.

**Takeaway:** In CRSP's monthly file over 90% of delisted stocks (15,327 of 16,916) have no delisting-month return; adding the separately stored delisting returns cuts the low-asset-growth decile's equal-weight return by about 34 bp a month (about 4% a year) and removes the significance of the 1-6 spread, while value-weighted results barely move.

## Problem
Is the asset-growth anomaly real, or an artefact of omitted delisting returns and the external-financing anomaly?

## Data and period
Non-financial NYSE, AMEX and Nasdaq stocks from CRSP and Compustat, July 1968 – December 2013 (544 months), 20,857 stocks.

## Method
Decile portfolio sorts on asset growth, with and without CRSP delisting returns merged in; controls for external financing.

## Baselines and validation
Portfolio sorts with t-statistics; equal- and value-weighted versions.

## Results (with page or section references)
- 1,589 of 16,916 delisted stocks (9.39%) have a delisting-month return in CRSP.msf.
- Where both exist, the recorded monthly return is about 10% higher than the delisting return, 25% higher for performance-related delistings.
- Decile 1 (lowest growth) equal-weight return 1.79% → 1.45% a month; the 1-6 spread 0.53% → 0.24% (no longer significant); value-weighted 1-10 spread 0.81% → 0.80%.

## Limits and risks to validity
Working paper (journal status not checked). Read through a summarising fetch tool, so page numbers are not available. One anomaly; the size of the effect depends on how many distressed small stocks a strategy holds.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Bias measurement on portfolio sorts |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Delisting returns explicit |
| Costs and realism | N/A | |
| Sample breadth | 2 | All US stocks, 45 years |
| Statistical testing | 1 | t-statistics |
| Reproducibility | 0 | Licensed data; no code |
| **Total** | 5/8 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read through a summarising tool).
