---
type: lit-note
title: "Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data"
authors: [Xinyue Fang, Robert Ślepaczuk]
year: 2026
venue: arXiv preprint
source_url: https://arxiv.org/abs/2606.09478
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.1, RQ1.6]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series]
---
# Volatility Forecasting and Return Prediction under Market Regimes (Fang, 2026)

**Basis:** first read through alphaXiv's structured report (2026-11-07). **Numbers checked against the PDF (v1, 8 Jun 2026) on 2026-11-08:** Tables 2, 4, 5, 8, 12, 17 and the Reality Check/SPA paragraph (p. 37) confirm the figures below, with one correction (max drawdown) and two items not found on the pages returned (buy-and-hold full-sample drawdown, bootstrap p-value).

**Takeaway:** Adding a Markov-switching volatility-regime probability improves HARQ volatility forecasts, especially in stress; XGBoost return predictability on the CSI 300 is weak, exists only in low-volatility regimes, and the best strategy is not significant after data-snooping correction.

## Problem
Whether regime-aware volatility forecasts and ML return prediction can be combined to improve statistics and economic value (report §3).

## Data and period
5-minute CSI 300 index data, 2005-04-08 to 2023-05-31 (Wind). Out-of-sample: volatility 2013-08-21 to 2023-05-29; returns 2014-12-17 to 2023-05-26 (report §4.1–4.2).

## Method
Stage 1: HARQ, then two-state MS-GJR-GARCH on residuals, filtered high-vol probability p_t added to HARQ. Stage 2: XGBoost on volatility, regime and lagged-return features; conservative hyperparameter grid (report §4.3–4.4).

## Baselines and validation
Expanding-window walk-forward with quarterly re-estimation; filtered (not smoothed) probabilities to avoid look-ahead. Baseline HARQ; strategy vs buy-and-hold and weekly momentum. DM (incl. conditional), MZ, HAC hit-ratio tests, block bootstrap Sharpe, White Reality Check and Hansen SPA (report §4.2, 4.6).

## Results (with page or section references)
- QLIKE: HARQ + p_t 0.162259 vs HARQ 0.171013 (Table 2, p. 20); conditional DM in the high-volatility half p = 0.0049, low-volatility half p = 0.082; gains significant at every re-estimation frequency (Tables 4, 11, pp. 21, 29).
- Returns: full-sample correlation 0.0449, hit ratio 53.49% (HAC p = 0.0009); low-vol regime correlation 0.0638 (p = 0.0013), high-vol regime −0.0617 (p = 0.19) (Table 5, p. 22). Only quarterly re-estimation gives significant direction accuracy; monthly and semi-annual do not (Table 12, p. 30).
- Strategy net of 5 bp: Sharpe 0.255, max drawdown −14.52%, break-even cost ≈20 bp (Table 17, p. 33). In the 2015–16 crash window the strategy returned +10.2% vs −39.4% for buy-and-hold (drawdown −14.5% vs −50.3%) (Table 8, p. 27). The report's full-sample buy-and-hold drawdown (−50.60%) and bootstrap p = 0.182 were not on the pages returned (unverified).
- Ablation: removing the volatility forecast cuts Sharpe to 0.09; removing regime features to 0.18; removing both to −0.01 (Table 17, p. 33).
- Best parameter set not significant after Reality Check / SPA (p ≈ 0.50 both) (p. 37). Long-only version near zero after costs (report §5.3; not re-checked).
- An expanded XGBoost grid did not improve out-of-sample results (p. 14).

## Limits and risks to validity
Single index; simplified cost assumptions; generated regressors (report §6). _My assessment:_ an honest negative-leaning result; the value is risk control, not alpha.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward, quarterly refits |
| Baselines | 1 | HARQ for vol; no random-walk/GBT comparison for returns beyond naive strategies |
| Point-in-time and leakage controls | 2 | Filtered probabilities, walk-forward calibration |
| Costs and realism | 1 | Flat 5 bp with turnover band |
| Sample breadth | 1 | One index, includes 2015 crash and 2020 |
| Statistical testing | 2 | HAC, bootstrap, Reality Check and SPA |
| Reproducibility | 0 | Licensed data; code not stated in report |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "return predictability remains weak, state-dependent" (abstract, p. 1)
