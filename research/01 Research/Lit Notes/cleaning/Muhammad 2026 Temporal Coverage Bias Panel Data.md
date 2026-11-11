---
type: lit-note
title: 'Temporal Coverage Bias in Financial Panel Data: A Coverage-Aware Structuring Framework with Evidence from the Dhaka Stock Exchange'
authors:
- Tashreef Muhammad
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2603.20237
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ3.3
- RQ3.4
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- panel-construction
---
# Temporal Coverage Bias in Financial Panel Data (Muhammad, 2026)

**Basis:** arXiv 2603.20237v1 read via alphaXiv on 2026-11-08 (pp. 1–12).

**Takeaway:** Forcing instruments with different listing dates onto one calendar and back-filling the first price before listing creates zero-return stretches that cut measured return volatility by about 20% (every one of 53 instruments, all above 10%) and GARCH conditional variance by about 26%, sometimes flipping its direction; each series must carry its own valid window.

## Problem
What happens when panels treat every instrument as existing for the whole sample?

## Data and period
Dhaka Stock Exchange end-of-day data, October 2012 – January 2026, 486 instruments; 53 instruments listed after 2016 with ≥400 days for the robustness test (pp. 4, 9).

## Method
Availability matrix of valid [first, last] trading dates per instrument; compare coverage-aware series with naive back-filled series in ARIMA and GARCH(1,1).

## Baselines and validation
Coverage-aware vs naive construction, per instrument.

## Results (with page or section references)
- Example: 1,081 padded days; return SD 0.0262 → 0.0210 (−19.7%); RMSE and MAE fall only because variability was washed out (Table 2).
- Across 53 instruments: mean volatility suppression 20.0% (median 19.7%); GARCH variance distortion mean 26.2%, present in >90% (§5.2, Fig. 5).
- Extreme GARCH outliers where padding is long relative to real history (Fig. 6).

## Limits and risks to validity
One emerging market; daily data; descriptive (no tests). The mechanism (padding creates zero returns) is general and also applies to forward-filled gaps.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Data-construction study |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Coverage windows explicit |
| Costs and realism | N/A | |
| Sample breadth | 1 | One exchange, 53 instruments, 2012–2026 incl. 2020 |
| Statistical testing | 0 | Descriptive |
| Reproducibility | 2 | Data (Mendeley) and code (GitHub) |
| **Total** | 5/8 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Instrument listing coverage, in short, is not a minor preprocessing consideration" (abstract)
