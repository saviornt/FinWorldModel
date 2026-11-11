---
type: lit-note
title: Pretrained Time-Series Foundation Models for Financial Return Forecasting
authors:
- Miquel Noguer i Alonso
- Rodolfo Pereira Franklin
year: 2026
venue: arXiv (q-fin.MF)
source_url: https://arxiv.org/abs/2606.27100
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ1.1
- RQ4.2
family:
- price-time-series
evidence: Moderate
score: 6
tags:
- lit-note
- family/price-time-series
---
# Pretrained Time-Series Foundation Models for Financial Return Forecasting (Noguer i Alonso, 2026)

**Basis:** full text via alphaXiv (sections 1–7, Appendix B).

**Takeaway:** Zero-shot TSFMs win most rankings against train-from-scratch deep nets on five US stocks, but beat a zero-return random walk significantly in only 2 of 10 cases.

## Problem
Whether off-the-shelf pretrained TSFMs are preferable to per-ticker deep models for 20-business-day return forecasts when only one series per asset is available (§1).

## Data and period
Yahoo Finance daily adjusted close for AAPL, AMZN, GOOG, JPM, META; training 2014-09-15 to 2024-08-21, evaluation 2024-08-22 to Feb 2026; linear and log returns (§4.1, App. B Table 10).

## Method
Six TSFMs zero-shot (TimeGPT, TimeGPT-LH, TimesFM-2.5, Moirai-2.0, Chronos, Chronos-2) vs five per-ticker baselines (NBEATS, NHITS, PatchTST, iTransformer, KAN), all with context L = 512, horizon H = 20 (§4.2–4.3).

## Baselines and validation
Zero-return random walk and 5-day seasonal naive; 10 rolling-origin windows over a fixed test period (Table 1). No GARCH or gradient-boosted trees. One-sided Diebold–Mariano with Harvey–Leybourne–Newbold correction (§4.4). Pretraining-corpus overlap with the test period is not discussed (not in the part I read).

## Results (with page or section references)
- TSFMs take 8 of 10 task-level wins; Moirai-2.0 and TimesFM-2.5 have the best average ranks (Abstract, §6).
- iTransformer wins both META tasks (Abstract, §5.3).
- Only 16 TSFM model–asset cases show positive skill vs random walk (§5.3).
- One-sided DM rejects only for Chronos on AMZN (p = 0.0421, skill 0.0863) and Moirai-2.0 on GOOG (p = 0.0421, skill 0.2289); TimesFM-2.5 on AAPL and JPM has negative skill (−0.0319, −0.0466) (Table 7, p. 30).
- Forecast error only; no trading, cost or calibration evaluation (§6, fourth limitation).

## Limits and risks to validity
_My assessment:_ five large-cap assets and ~18 months of test data; DM across many model–asset pairs with no multiple-testing correction, so the two "significant" cases at p = 0.0421 may be chance; no strong simple baselines (GBT, linear) beyond naive; zero-shot TSFMs may have seen test-period data during pretraining (not addressed); companion code not part of the paper (§4.3, App. B).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One train/test split with rolling origins, no refits |
| Baselines | 1 | Random walk and seasonal naive plus deep nets; no GARCH/GBT |
| Point-in-time and leakage controls | 0 | Pretraining overlap not addressed |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | Five assets, one period |
| Statistical testing | 1 | DM, no multiple-testing correction |
| Reproducibility | 1 | Public data source; code not in paper |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "gains over the random-walk benchmark are small and sparse" (Abstract, p. 1)
