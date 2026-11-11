---
type: lit-note
title: "The Pre-FOMC Announcement Drift"
authors: [David O. Lucca, Emanuel Moench]
year: 2015
venue: Journal of Finance
source_url: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf
doi: 10.1111/jofi.12196
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series, information-diffusion]
---
# The Pre-FOMC Announcement Drift (Lucca, 2015)

**Basis:** FRBNY Staff Report 512 (rev. Aug 2013), read through a page-fetch summary; published in JF 70(1), 2015 (DOI from OpenAlex).

**Takeaway:** From 1994 to 2011 the S&P 500 rose on average 49 bp in the 24 hours before scheduled FOMC announcements (≈80% of the realised equity premium), with no reversal afterwards and no such drift before other US macro releases or in Treasuries; the move happens before any information is released. A later study shows the drift largely disappeared after 2015 ([[Kurov 2021 Disappearing Pre-FOMC Drift]]).

## Problem
Do stocks move ahead of scheduled monetary-policy announcements, and why?

## Data and period
Intraday S&P 500 Sept 1994–Mar 2011 (131 meetings); daily data 1960–2011; international indices; Treasuries and money-market futures (pp. 5–7, 10, 14–17).

## Method
Regressions of 2pm-to-2pm returns on pre-FOMC dummies; trading-strategy Sharpe; White reality check; rolling estimates; risk and leakage explanations tested (pp. 8–25).

## Baselines and validation
Non-FOMC windows, other macro releases, other assets, pre-1980 placebo, real-time learnability of the effect.

## Results (with page or section references)
- Pre-FOMC 2pm-to-2pm return 49 bp (t > 4.5) vs <0.5 bp otherwise; 36 bp (t 4.86) over 1980–2011 (pp. 8, 11).
- ≈3.89% a year of excess return in pre-FOMC windows vs 0.88% on all other days (p. 8); strategy Sharpe 1.14 (gross) (p. 9).
- None before 1980; none before nine other major US releases; none in Treasuries or money-market futures (pp. 10, 16–17).
- DAX, FTSE 100, CAC 40, IBEX, SMI show 29–52 bp pre-FOMC returns; their own central banks' announcements do not (p. 14).
- No reversal in the five days after; White reality check p < 0.02% (pp. 11–13).

## Limits and risks to validity
_My assessment:_ one index-level anomaly; costs ignored; later decay ([[Kurov 2021 Disappearing Pre-FOMC Drift]]). Shows that "priced in before release" can reflect risk or attention effects, not leaked content.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Subsamples and rolling estimates |
| Baselines | 1 | Non-event windows, other releases |
| Point-in-time and leakage controls | 2 | Intraday timing explicit |
| Costs and realism | 0 | Gross strategy returns |
| Sample breadth | 2 | Decades, several markets, stress periods |
| Statistical testing | 2 | White reality check |
| Reproducibility | 1 | Public data |
| **Total** | **9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "the pre-FOMC announcement drift is a puzzle" (p. 25)
