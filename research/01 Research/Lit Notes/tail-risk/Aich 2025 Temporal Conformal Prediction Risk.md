---
type: lit-note
title: 'Temporal Conformal Prediction (TCP): A Distribution-Free Statistical and Machine Learning Framework for Adaptive Risk Forecasting'
authors:
- Agnideep Aich
- Ashit Baran Aich
- Dipak C. Jain
year: 2025
venue: arXiv (stat.ML), v6 Jan 2026
source_url: https://arxiv.org/abs/2507.05470
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ1.6
- RQ4.3
family:
- tail-risk
evidence: Moderate
score: 9
tags:
- lit-note
- family/tail-risk
---
# Temporal Conformal Prediction (Aich, 2025)

**Basis:** arXiv v6 (22 Jan 2026) pages 1–4, 7–11, 13–15, 18 via the alphaXiv PDF reader. Guide seed source.

**Takeaway:** A LightGBM quantile forecaster wrapped in rolling split-conformal calibration reaches near-nominal 95% coverage on S&P 500, Bitcoin and gold (2017–2025) and is the only method passing Kupiec/Christoffersen tests, but in the COVID crash window (Feb–Apr 2020) it covers only 80% on the S&P 500, the same as a fixed-parameter GARCH; every method under-covers at the shock.

## Problem
Calibrated prediction intervals for daily returns under nonstationarity (pp. 1–2).

## Data and period
Daily log returns, S&P 500, BTC-USD, gold, Nov 2017–May 2025; features: 5 lagged returns, 20-day rolling volatility, squared and sign of last return (p. 7).

## Method
Gradient-boosted quantile forecaster fitted on a 192-day training slice, split-conformal threshold from a 60-day calibration slice, rolled daily (252-day window); TCP-RM adds a Robbins–Monro offset to the threshold (pp. 4, 8, 11).

## Baselines and validation
Rolling QR (same model, no calibration), linear QR, ACI, fixed-parameter GARCH(1,1) with normal intervals (ω, α, β fixed at 10⁻⁶, 0.05, 0.9; no re-estimation), 252-day historical simulation (p. 8). Metrics: coverage, width, Kupiec, Christoffersen on the 5% lower tail (pp. 8–9).

## Results (with page or section references)
- Full-sample coverage (target 95%): S&P 500 TCP 95.2%, Hist 93.1%, ACI 87.4%, QR 83.2%, GARCH 82.7%; widths 5.21 vs Hist 5.06 (p. 10, Table 1).
- Robbins–Monro adds negligible change (coverage deltas ≤ 0.0007) (pp. 9–10).
- COVID window (55 days), S&P 500: TCP 80.0%, GARCH 80.0%, QR 65.45%, Hist 65.45%, ACI 56.36% (pp. 10–11, Table 2). Gold: TCP 87.3%, Hist 69.1%, ACI 58.2%; BTC: TCP 89.1%, Hist 90.9% (p. 18).
- On all three assets only TCP and TCP-RM pass all three backtests (p. 11; Appendix D, p. 18).
- Authors: TCP "can temporarily under-cover during abrupt regime shifts" (p. 13).

## Limits and risks to validity
_My assessment:_ the GARCH baseline uses fixed, untuned parameters and normal innovations, so it is a weak comparator; no GARCH-t, EVT or filtered HS. Three assets; 55-day crisis window gives very noisy coverage. Two-sided 95% intervals, not the 99% level that matters for capital.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Daily rolling walk-forward |
| Baselines | 1 | HS, QR, ACI; GARCH fixed-parameter and normal |
| Point-in-time and leakage controls | 1 | Fit on training slice only; not otherwise discussed |
| Costs and realism | N/A | Risk calibration |
| Sample breadth | 1 | 3 assets, 2017–2025 incl. COVID |
| Statistical testing | 1 | Kupiec, Christoffersen |
| Reproducibility | 2 | Code and processed data on GitHub |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "during the sharpest part of the COVID shock, all methods under-cover" (p. 10)
