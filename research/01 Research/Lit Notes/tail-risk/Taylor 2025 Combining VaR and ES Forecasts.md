---
type: lit-note
title: Combining a Large Pool of Forecasts of Value-at-Risk and Expected Shortfall
authors:
- James W. Taylor
- Chao Wang
year: 2025
venue: arXiv (q-fin.RM), v2 May 2026
source_url: https://arxiv.org/abs/2508.16919
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ1.6
- RQ4.2
family:
- tail-risk
evidence: Strong
score: 11
tags:
- lit-note
- family/tail-risk
---
# Combining a Large Pool of Forecasts of Value-at-Risk and Expected Shortfall (Taylor, 2025)

**Basis:** arXiv v2 pp. 1–5, 8, 10–13, 15, 19–21, 29, 32–33 via the alphaXiv PDF reader. Result tables (pp. 22–28) not in the pages returned.

**Takeaway:** Across six stock indices, combining 2.5% VaR and ES forecasts from up to 90 econometric methods works best with trimmed means, probability averaging and performance-based weights; the large pool tends to underestimate risk, a small diverse pool of six methods with performance weighting does best, and shorter estimation windows (900 vs 1,800 days) help all combiners.

## Problem
How to combine many VaR/ES forecasts, given little prior work on large pools (pp. 1–3).

## Data and period
Daily returns, ranges and 5-minute realised volatility for AORD, DAX, FTSE 100, Hang Seng, Nikkei, S&P 500; 5,400 days ending 19 May 2022 (p. 4).

## Method
90 individual methods: HS (4 windows), Gaussian, EWMA, GARCH/GJR with Gaussian, t, skew-t, each also with EVT and filtered HS, with range and RV variants; CAViaR and CARE families (pp. 5, 8, 33). 19 combiners: mean, median, mode, five trimmed means, probability averaging, depth-based, relative-score and minimum-score weights with regularisation, smooth transition, average of combiners (pp. 8–20). Parameters fitted with the asymmetric Laplace joint score (p. 5).

## Baselines and validation
Individual methods re-estimated daily on 1,800-day rolling windows → 3,600 out-of-sample forecasts; combiners re-estimated daily on 1,800-day windows → final 1,800 days evaluated (p. 4). Benchmark: dynamic selection of the best recent individual method (p. 21). Kupiec UC, Christoffersen CC, DQ with four lags, McNeil–Frey ES bootstrap test; five joint scores (p. 21).

## Results (with page or section references)
- Trimmed mean and probability averaging were among the most accurate combiners; both give more extreme VaR/ES than the simple average, "indicating that the large pool of forecasts tended to underestimate risk" (p. 29).
- Reducing the pool size to small, diverse pools improved performance-based combinations; shortening the window to 900 days improved all combiners (p. 29).
- Relative score and minimum score combining are "hard to beat" (p. 29).
- Symmetric trimming was sizeable in the first year of the pandemic (FTSE 100, p. 12, Fig. 4).

## Limits and risks to validity
_My assessment:_ one tail level (2.5%), indices only, no ML methods in the pool. I did not see the numeric result tables or a crisis-subperiod analysis.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Daily rolling re-estimation, two-stage out-of-sample |
| Baselines | 2 | 90 methods incl. HS, GARCH, EVT, FHS, CAViaR; dynamic selection |
| Point-in-time and leakage controls | 2 | Rolling past-only estimation at both stages |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 2 | 6 indices, 2015–2022 evaluation incl. COVID |
| Statistical testing | 1 | UC, CC, DQ, ES tests; multiple-testing correction not seen |
| Reproducibility | 0 | No code or data statement in pages read |
| **Total** | **9/12 → 11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "relative score and minimum score combining are hard to beat" (p. 29)
