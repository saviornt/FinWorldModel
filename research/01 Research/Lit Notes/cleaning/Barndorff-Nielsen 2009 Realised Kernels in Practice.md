---
type: lit-note
title: 'Realised Kernels in Practice: Trades and Quotes'
authors:
- Ole E. Barndorff-Nielsen
- Peter Reinhard Hansen
- Asger Lunde
- Neil Shephard
year: 2009
venue: Econometrics Journal 12(3), C1–C32
source_url: https://scholar.harvard.edu/sites/scholar.harvard.edu/files/RKpractice-ECTJ.pdf
doi: 10.1111/j.1368-423X.2008.00275.x
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.3
family:
- cleaning
evidence: Weak
score: 5
tags:
- lit-note
- family/cleaning
- high-frequency
---
# Realised Kernels in Practice: Trades and Quotes (Barndorff-Nielsen, Hansen, Lunde & Shephard, 2009)

**Basis:** authors' accepted version (Harvard page), read through a summarising page fetch on 2026-11-08; pp. 6–8 for the cleaning rules. DOI not confirmed on the pages read.

**Takeaway:** The standard TAQ cleaning recipe: keep 9:30–16:00 records from one exchange with non-zero prices; for quotes, collapse same-timestamp quotes to the median, drop negative spreads, spreads over 50× the daily median, and mid-quotes more than 10 mean absolute deviations from a 50-observation centred rolling median; for trades, drop corrected and abnormal-condition trades, median same-timestamp trades, and drop trades outside the quote by more than one spread. With it, trade- and quote-based volatility estimates agree closely.

## Problem
How to implement realised-kernel volatility estimators on messy trade and quote data.

## Data and period
TAQ for one NYSE stock (Alcoa), 123 days, January–June 2007 (pp. 6, 9).

## Method
Rules P1–P3 (all data), Q1–Q4 (quotes), T1–T4 (trades); realised kernel with end-effect and bandwidth choices.

## Baselines and validation
Trade-based vs quote-based estimates of the same stock.

## Results (with page or section references)
- P3 (one exchange), T3 and Q1 (same-timestamp merging) remove the most records; T4 is rarely triggered (pp. 7–8).
- Trade and quote estimates agree closely; local 10-minute trends are the hard case (abstract).

## Limits and risks to validity
One stock, six months; the centred rolling median (Q4) uses future quotes, which is fine for after-the-fact volatility measurement but must be replaced by a trailing window in any real-time feature pipeline (project reading; compare [[Zhang 2026 When Alpha Disappears Decision-Time Leakage]]).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Measurement method |
| Baselines | N/A | |
| Point-in-time and leakage controls | N/A | |
| Costs and realism | N/A | |
| Sample breadth | 0 | One stock |
| Statistical testing | 1 | Estimator comparisons |
| Reproducibility | 1 | Rules fully specified; implemented in the R highfrequency package |
| **Total** | 2/6 → **5/14** | Weak (on breadth; still the standard reference) |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read through a summarising tool).
