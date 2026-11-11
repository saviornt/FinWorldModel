---
type: lit-note
title: "Multivariate Financial Forecasting using the Chronos Time Series Foundation Models"
authors: [Sanjiv R. Das, Tarang Goyal, Mohini Yadav]
year: 2026
venue: "arXiv q-fin.ST"
source_url: https://arxiv.org/abs/2605.21504
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15, RQ1.1]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, world-model]
---
# Multivariate Financial Forecasting using the Chronos Time Series Foundation Models (Das et al., 2026)

**Basis:** arXiv v1 (8 May 2026), pp. 1–6 (Tables 1–3, Fig. 3), via the alphaXiv PDF reader.

**Takeaway:** In zero-shot Chronos-2 forecasts of price and yield levels (monthly rolling, 2000–2025, 21- and 63-day horizons), feeding related series of the same asset class as a multivariate group cut error for every series (Treasury MAPE 0.050 vs 0.123; Magnificent-7 MAPE 0.071 vs 0.084), but adding the other asset class (stocks with rates) did not help and slightly hurt.

## Problem
Do multivariate inputs improve a covariate-aware foundation model's financial forecasts over univariate inputs (pp. 1–2)?

## Data and period
Seven mega-cap stocks (AAPL, AMZN, GOOGL, MSFT, NFLX, NVDA, TSLA) and ten Treasury maturities (3M–30Y); 2000–2025 (combined panel Jul 2010–Dec 2025); input windows 126–756 days (p. 3).

## Method
Chronos-2 zero-shot with group attention; univariate vs within-class multivariate vs combined stock+rate groups; RMSE and MAPE on levels (pp. 2–3).

## Baselines and validation
Only the univariate Chronos-2 run; no random walk, ARIMA or econometric baseline. Monthly rolling forecasts; pre- vs post-2023 split as a contamination check (pp. 3–5).

## Results (with page or section references)
- Rates MAPE MV 0.0497 vs UV 0.1233; stocks 0.0706 vs 0.0844 (p. 4, Table 1); MV better for every series (p. 5, Table 2).
- Combined stocks+rates: e.g. DGS3MO MAPE 0.2392 vs 0.2304 within rates; AAPL 0.0519 vs 0.0500 within stocks; slightly worse overall (p. 6, Table 3).
- Post-2023 forecasts not less accurate than pre-2023 (p. 5, Fig. 3).

## Limits and risks to validity
_My assessment:_ level forecasts of prices and yields; a univariate foundation model is a weak baseline (no random walk shown, which a level MAPE would favour); table averages mix "in-sample and out-sample combinations" (p. 4); seven hand-picked survivors; no significance tests. The "within-class helps, cross-class hurts" pattern is the useful hypothesis. Paper largely AI-drafted (Appendix A). Code public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling zero-shot forecasts; aggregation unclear |
| Baselines | 0 | Univariate Chronos-2 only |
| Point-in-time and leakage controls | 1 | Pre/post-2023 contamination check |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 17 series, two asset classes |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code on GitHub |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "adding a different class of time series does not improve forecasting" (p. 2)
