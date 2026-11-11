---
type: lit-note
title: Empirical Asset Pricing via Machine Learning
authors:
- Shihao Gu
- Bryan Kelly
- Dacheng Xiu
year: 2020
venue: Review of Financial Studies 33(5)
source_url: https://www.nber.org/papers/w25398
doi: 10.1093/rfs/hhaa009
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ1.1
- RQ3.6
- RQ4.2
- RQ4.3
- RQ4.6
family:
- price-time-series
evidence: Moderate
score: 8
tags:
- lit-note
- family/price-time-series
---
# Empirical Asset Pricing via Machine Learning (Gu, 2020)

**Basis:** NBER Working Paper 25398 (revised Sept 2019), PDF via alphaXiv: §3.1–3.4 and Tables 1–3, 5–7, A.7–A.11. The RFS published version (DOI from the RePEc record) was not opened.

**Takeaway:** For monthly US stock returns, trees and shallow neural nets beat linear models out of sample (R²_oos ≈ 0.3–0.4% vs ~0.1–0.2%); NNs beat linear models significantly but are not significantly better than trees, and depth beyond three layers does not help.

## Problem
Comparative test of ML methods for measuring risk premia in the cross-section and time series of US equities (Abstract).

## Data and period
60 years of US stocks; 94 characteristics × 8 macro predictors + 74 industry dummies = 920 covariates (§3.1). Training 1957–1974, validation 1975–1986, test 1987–2016 (p. 25).

## Method
OLS, OLS-3, PLS, PCR, elastic net, group-lasso GLM, random forest, GBRT, NN1–NN5 (§3.2).

## Baselines and validation
Refit yearly with expanding training window and rolling 12-year validation; no cross-validation, to keep time order (p. 25, fn. 32). R²_oos against a zero forecast (fn. 34). Pairwise DM with Bonferroni adjustment (Table 3).

## Results (with page or section references)
- Monthly stock-level R²_oos: OLS −3.46%, OLS-3 0.16%, ENet 0.11%, RF 0.33%, GBRT 0.34%, NN3 0.40% (Table 1, p. 26).
- Benefits of depth are limited: NN4 and NN5 do not improve over NN3 (p. 28).
- Trees improve on linear models but at best marginally significantly; NNs are the only models with large significant gains over linear models, and are not significantly better than trees (p. 29).
- Benchmarking against the historical mean inflates R²_oos by about 3% (fn. 34).
- Value-weighted NN4 long–short decile Sharpe 1.35; equal-weighted 2.45; equal-weighted excluding microcaps 1.69 (p. 41). No transaction costs.

## Preprocessing (added for RP3 RQ3.6, 2026-11-08)
- Characteristics are ranked cross-sectionally each month and mapped to [−1, 1]; missing values set to the monthly cross-sectional median (rev1 PDF p. 24, fn. 29–30). Publication lags assumed: monthly 1 month, quarterly 4 months, annual 6 months (same footnote). Read from NBER w25398 rev1 (June 2019) via alphaXiv.

## Limits and risks to validity
_My assessment:_ no trading costs; characteristic-timing lags not in the part I read (check for RP3); CRSP/Compustat data are licensed; sample ends 2016. Widely replicated benchmark; later work (e.g. [[Rahimikia 2025 ReVisiting TSFMs in Finance]]) uses it as the standard set-up.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Yearly refits, expanding window, 30-year test |
| Baselines | 2 | Zero forecast, OLS-3, RF, GBRT |
| Point-in-time and leakage controls | 0 | Not in the part read |
| Costs and realism | 0 | No costs |
| Sample breadth | 2 | All US stocks, 1987–2016, several recessions |
| Statistical testing | 2 | DM with Bonferroni |
| Reproducibility | 0 | Licensed data; no code seen |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the benefits of “deep” learning are limited" (p. 28)
