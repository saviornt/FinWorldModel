---
type: lit-note
title: "A machine learning approach to volatility forecasting"
authors: [Kim Christensen, Mathias Siggaard, Bezirgen Veliyev]
year: 2023
venue: Journal of Financial Econometrics 21(5)
source_url: https://arxiv.org/abs/2601.13014
doi: 10.1093/jjfinec/nbac020
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.1, RQ1.6]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series]
---
# A machine learning approach to volatility forecasting (Christensen, 2023)

**Basis:** arXiv version (2601.13014, dated May 2022) via alphaXiv: abstract, §1–3 (part), §5, §7, Tables 7, 9, 11, 13. Published version (DOI from the reference list of [[Brini 2026 TSFMs vs Econometric Realized Volatility]]) not opened.

**Takeaway:** With minimal tuning, random forests and neural networks beat the HAR family for realised-variance forecasts of DJIA stocks, with larger gains at weekly and monthly horizons and when extra predictors are added.

## Problem
Whether ML can beat HAR models for realised variance and extract information from extra predictors (§1).

## Data and period
High-frequency data for 29 of 30 DJIA constituents (§3). The out-of-sample window plotted in Fig. 9 runs 2015–2018; the full sample period is not in the part I read.

## Method
Ridge, lasso, elastic net, adaptive and post-lasso, bagging, random forest, gradient boosting, feed-forward NNs; two predictor sets: HAR lags only (M_HAR) and an extended set incl. implied volatility and macro (M_ALL) (§2–4).

## Baselines and validation
HAR, HAR-X, LogHAR, LevHAR, SHAR, HARQ. One-sided DM tests and Model Confidence Set (§2). Exact window scheme not in the part I read.

## Results (with page or section references)
- ML beats the HAR lineage even with only HAR lags as inputs (Abstract).
- Gains grow with horizon; for M_ALL at one month, regression trees and NNs give large improvements (§5, p. 26). Example: RF MSE relative to HAR is 0.604 at one month (Table 7, p. 30).
- Implied volatility ranks higher in RF and NN than in HAR-X (p. 26).
- VaR application: ML lowers loss but with weaker significance (§7, Table 9).

## Limits and risks to validity
_My assessment:_ 29 large-cap stocks only; minimal hyperparameter tuning (authors' framing); no code release seen.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Out-of-sample window; scheme not verified |
| Baselines | 2 | Six HAR variants |
| Point-in-time and leakage controls | 0 | Not addressed in the part read |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | 29 stocks |
| Statistical testing | 2 | DM plus MCS |
| Reproducibility | 0 | Not stated |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "The forecast gains are more pronounced at longer horizons." (Abstract, p. 1)
