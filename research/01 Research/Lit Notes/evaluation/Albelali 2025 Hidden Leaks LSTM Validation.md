---
type: lit-note
title: 'Hidden Leaks in Time Series Forecasting: How Data Leakage Affects LSTM Evaluation Across Configurations and Validation Strategies'
authors:
- Salma Albelali
- Moataz Ahmed
year: 2025
venue: arXiv (cs.LG) 2512.06932
source_url: https://arxiv.org/abs/2512.06932
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Moderate
score: 6
tags:
- lit-note
- family/evaluation
- cross-validation
- leakage
---
# Hidden Leaks in Time Series Forecasting (Albelali & Ahmed, 2025)

**Basis:** Full text via alphaXiv (v1), pp. 1–15, read 2026-11-08.

**Takeaway:** Building input windows before splitting the data leaks future values into training; with unshuffled 10-fold CV this made LSTM error look up to 20.5% lower, while chronological 2-way and 3-way splits stayed within about 5% (mostly under 3%).

## Problem
How much does pre-split sequence construction inflate measured accuracy under different validation schemes?

## Data and period
Daily Delhi climate data, 1,462 days, 2013–2017, mean temperature (Table 2, §3.1); 480 runs.

## Method
Univariate LSTM; leaky (windows built on the full series, then split) vs clean (split first) pipelines under 80/20, 70/10/20 and unshuffled 10-fold CV; window 3–10, lag 1–3 (§3).

## Baselines and validation
Same model under clean vs leaky setups.

## Results (with page or section references)
- 10-fold CV: RMSE gain from leakage 3.7% (base), 7.2% (window 7), 19.3% (lag 2), 20.5% (lag 3) (Table 5, p. 13).
- 2-way split: 0.2% (base), at most 2.6%; 3-way: up to 5.0% (Table 5).
- Longer horizons and smaller windows raise leakage sensitivity (pp. 9–12).

## Limits and risks to validity
_My assessment:_ one non-financial series and one model; the 10-fold scheme is contiguous blocks without purging, so it shows the cost of no purge rather than of purged CV; the clean 10-fold result also has a wide CI at lag 2.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single splits and plain folds |
| Baselines | 0 | No baseline forecaster |
| Point-in-time and leakage controls | 2 | Leakage isolated by design |
| Costs and realism | N/A |  |
| Sample breadth | 0 | One climate series |
| Statistical testing | 1 | Confidence intervals over repeated runs |
| Reproducibility | 1 | Public data |
| **Total** | 5/12 → **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
