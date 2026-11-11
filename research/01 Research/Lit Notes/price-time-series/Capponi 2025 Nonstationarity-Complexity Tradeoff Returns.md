---
type: lit-note
title: "The nonstationarity-complexity tradeoff in return prediction"
authors: [Agostino Capponi, Chengpiao Huang, J. Antonio Sidaoui, Kaizheng Wang, Jiacheng Zou]
year: 2025
venue: arXiv (stat.ML)
source_url: https://arxiv.org/abs/2512.23596
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.9]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, adaptation, training-window, regimes]
---
# The Nonstationarity–Complexity Tradeoff in Return Prediction (Capponi et al., 2025)

**Basis:** alphaXiv PDF pages 1–5, 7, 9–13, 27, 40, 61 (v1, 29 Dec 2025). Columbia University. Pages with Table 2 and the code statement were not among those returned.

**Takeaway:** In predicting 17 US industry-portfolio returns (out of sample 1990–2016), complex models need long training windows that mix in old regimes, so in recessions a ridge model on the last 64 months beat a random forest on all history; choosing model class and training window jointly, by comparing candidates on adaptively chosen recent validation data, raised out-of-sample R² by 14–23% over fixed-window selection and stayed positive in the 1990 recession.

## Problem
How to choose model complexity and training-window length together when the return-generating process drifts (§1).

## Data and period
Daily excess returns of 17 Kenneth French industry portfolios with covariates; data from Sept 1987, OOS 1990–2016 including the 1990–91, 2001 and 2007–09 NBER recessions (§3.1, §5).

## Method
Bound: error ≲ misspecification + estimation uncertainty + non-stationarity over the window (Theorem 3.1). ATOMS: a tournament that compares candidate (model, window) pairs on validation data whose length is chosen adaptively to the local drift (§4).

## Baselines and validation
Fixed-window validation (32, 128, 512) and cross-validation selectors over the same candidates (ridge, random forest, etc.); zero-forecast R² (standard R² in App. G) (§2, §5).

## Results (with page or section references)
- Average OOS R² 0.049; 14% above long-window validation and more than double short-window validation (§1).
- 1990 recession: R² 0.027 vs negative for all benchmarks (Fixed-val(512) −0.031); 2001: 0.125 vs 0.117 (long window) and 0.071 (CV) (§1, §6).
- Recessions: ridge on 64 months beats RF on 64 months and RF on all history (Fig. 2).
- Trading rule: 31% more terminal wealth than the best benchmark selector, 3.54× vs CV (Table 3), no costs.
- Optimal window shrinks as drift grows; with strong drift the simpler class wins (Example 3.4).

## Limits and risks to validity
_My assessment:_ portfolios not single stocks; cost-free trading claim; no DM or multiple-testing results seen in pages read; benchmarks are other selectors, not a GBT on expanding window or the historical mean (zero forecast used); code not confirmed.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Recursive monthly re-selection 1990–2016 |
| Baselines | 1 | Fixed-window and CV selectors; zero forecast |
| Point-in-time and leakage controls | 1 | Portfolio returns (no survivorship); covariate timing not checked |
| Costs and realism | 0 | Trading rule without costs |
| Sample breadth | 2 | 17 industries, three recessions |
| Statistical testing | 0 | None seen in pages read |
| Reproducibility | 0 | Code not confirmed |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a complex model trained on a long window of past data may be outperformed" (§1, p. 2)
