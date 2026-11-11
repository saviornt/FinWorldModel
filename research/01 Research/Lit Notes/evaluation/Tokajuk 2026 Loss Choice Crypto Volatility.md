---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- metrics
title: Loss Choice or Model Choice? The Role of Forecast Level in Cryptocurrency Volatility Forecasting
authors:
- Andrzej Tokajuk
- Jarosław A. Chudziak
year: 2026
venue: arXiv (q-fin.CP) 2609.27024
source_url: https://arxiv.org/abs/2609.27024
doi: ''
research_questions:
- RQ4.3
evidence: Moderate
score: 8
---
# Loss Choice or Model Choice? (Tokajuk & Chudziak, 2026)

**Basis:** Full text (8 pages) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** In crypto volatility forecasting, the training loss changes results about 2.9 times more than the model does, but mostly by shifting the forecast level; after a validation-based level alignment the loss effect falls by 77% and model differences dominate, and raw 5% VaR breach rates across losses (1.3%–6.3%) collapse to 3.5%–3.6%.

## Problem
Whether loss-function effects reflect forecast level or forecast dynamics, and how they carry into VaR (§1).

## Data and period
Daily Binance spot OHLCV for BTC, ETH, BNB, XRP, ADA, from 2017 (BTC, ETH) to 31 May 2026; target next-day Garman–Klass variance; Parkinson and Rogers–Satchell for robustness (§4).

## Method
Seven training losses (MSE-log, Huber-log, pinball, QLIKE, Patton b = −1, HMAE, HMSE) × five models (HAR, HAR-X, NeuralHAR, DLinear, LightGBM); one validation constant rescales each forecast; LevelShare measures the constant-offset part of cross-loss differences (§3).

## Baselines and validation
HAR and LightGBM among the models; five expanding walk-forward folds with disjoint 379-day test windows; scalers on training data; three seeds; stationary bootstrap CIs; Kupiec test (§4).

## Results (with page or section references)
- Raw cross-loss vs cross-model score variation ratio 2.91 (95% CI 2.27–3.25); after alignment 0.67 (0.56–0.99) (§5.1–5.2).
- Level share of cross-loss differences: HAR 89%, LightGBM 56%; alignment cuts cross-loss variation by 77% overall (Table 3).
- QLIKE- and Patton-trained models generally lead under QLIKE evaluation; "a score favours its own target" (§5.1).
- Loss rankings under QLIKE and MSE-log have Spearman −0.200 (§5.3).
- 5% Gaussian VaR raw breach rates 1.28%–6.31% across losses; aligned 3.48%–3.61%; Kupiec rejects 128/175 series raw and 109 aligned (Table 4, §5.3).

## Limits and risks to validity
_My assessment:_ crypto only, one-day horizon, Gaussian VaR; short conference-style paper; no code. The lesson transfers: report forecast level (bias) separately from ranking, and evaluate with the loss the decision uses.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward folds |
| Baselines | 2 | HAR plus LightGBM |
| Point-in-time and leakage controls | 1 | Inputs available by day t; train-only scalers |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Five cryptocurrencies, one market |
| Statistical testing | 1 | Bootstrap CIs, Kupiec |
| Reproducibility | 0 | No code |
| **Total** | 7/12 → **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a score favours its own target" (§5.1)
