---
type: lit-note
title: "Machine Learning-Based Bitcoin Trading Under Transaction Costs: Evidence From Walk-Forward Forecasting"
authors: [Andrei Bysik, Robert Ślepaczuk]
year: 2026
venue: arXiv (q-fin.TR) 2606.00060
source_url: https://arxiv.org/abs/2606.00060
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.6]
family: [evaluation]
evidence: Moderate
score: 8
tags: [lit-note, family/evaluation, economic-value, transaction-costs, crypto]
---
# ML Bitcoin Trading Under Transaction Costs (Bysik & Ślepaczuk, 2026)

**Basis:** Full text (pp. 1–7, 16, 31) via the alphaXiv PDF reader, read 2026-11-09.

**Takeaway:** Hourly BTC/USDT forecasts from XGBoost, LSTM and iTransformer are profitable gross, but every naive sign strategy is wiped out at 10 bps; a filter that trades only when the forecast exceeds a multiple of the cost restores profit in some configurations, yet the best strategy does not significantly beat buy-and-hold.

## Problem
Whether ML forecasts of hourly returns can be turned into net-of-cost trading performance, and whether the execution rule matters more than the model (pp. 1–2).

## Data and period
Binance BTC/USDT USD-M futures hourly OHLCV, Dec 2017–Jan 2026, 70,872 observations; 122 missing hours forward-filled (pp. 5, 31).

## Method
27-fold rolling walk-forward (12-month train, 3-month validation, 3-month test). Sign rule long-only or long-short; cost-aware filter trades only if |forecast| > λ·c·turnover, with c = 10 bps and λ = 2 (pp. 6–7).

## Baselines and validation
Buy-and-hold and 24-hour momentum; scaling and features rebuilt inside each fold (p. 7). Paired circular block bootstrap on return differentials with Holm correction (pp. 4, 16).

## Results (with page or section references)
- No costs: long-only XGBoost Sharpe 1.27, LSTM 1.45, iTransformer 2.59 vs buy-and-hold 0.82 (Table 4, p. 16).
- At 10 bps all naive ML strategies have annual returns of −50.7% to −98.6%; iTransformer made 17,942 trades (Table 4, p. 16). Cost drag 1.43–6.06 bps per hour, significant after Holm (Table 5, p. 16).
- The cost-aware filter cut turnover by more than an order of magnitude; best long-only XGBoost: annual return above 65%, Sharpe above 1 (p. 2).
- Best cost-aware strategies do not significantly beat buy-and-hold in Sharpe after bootstrap; profitable in 16 of 27 folds, positive Sharpe in 14 (p. 31).
- Architecture, loss and model-selection effects are secondary and statistically fragile (p. 2).

## Limits and risks to validity
_My assessment:_ one asset, one venue; flat proportional cost, no order book or funding; λ fixed at 2 with no reported search penalty; the >65% figure comes from a selected configuration. Good evidence that the execution rule, not the forecaster, decides net value at short horizons.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | 27-fold rolling walk-forward |
| Baselines | 1 | Buy-and-hold, momentum; XGBoost included as a model |
| Point-in-time and leakage controls | 1 | Fold-internal preprocessing; not separately checked |
| Costs and realism | 1 | Flat 10 bps with sensitivity |
| Sample breadth | 1 | One asset, several regimes |
| Statistical testing | 2 | Block bootstrap with Holm |
| Reproducibility | 0 | Code or data release not stated in pages read |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a predictable return is not the same as a profitable trade." (p. 1)
