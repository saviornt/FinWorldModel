---
type: lit-note
title: "Chronos-2: A foundation model for multivariate time series forecasting"
authors: [Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, Pedro Mercado, Syama Sundar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan Zhang, Michael Bohlke-Schneider]
year: 2026
venue: arXiv 2610.41956
source_url: https://arxiv.org/abs/2610.41956
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10, RQ1.13, RQ1.15]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series, tokenization]
---
# Chronos-2: A foundation model for multivariate time series forecasting (Ansari, 2026)

**Basis:** PDF pages 1–3, 14–15, 21–22, 24, 31 (v1). Author list shortened here (11 of 25 listed). Macroeconomic case study and ablations not in the pages I read.

**Takeaway:** The Chronos family itself moved from per-value bins with cross-entropy and autoregressive sampling (Chronos) to continuous patches with a direct multi-step quantile head (Chronos-Bolt, Chronos-2); Chronos-2 leads fev-bench (skill 35.5% vs Chronos-Bolt 26.5%), but this is a design trajectory, not a controlled tokenisation ablation.

## Problem
Zero-shot forecasting with multivariate targets and covariates (§1, pp. 1–2).

## Data and period
Real and synthetic univariate series plus synthetic multivariate systems for pretraining; evaluated on fev-bench (100 tasks), Chronos-Bench-II (27) and GIFT-Eval (97) (App. A.6, p. 24).

## Method
120M encoder-only T5; inputs standardised then arcsinh-transformed, split into length-16 patches with time-index and mask features, embedded by a residual network; time attention plus group attention; 21-quantile head trained with quantile loss; multi-step patches decoded in one pass (§2, pp. 2–3; App. A.2–A.3, pp. 21–22).

## Baselines and validation
Naive, Seasonal Naive, AutoETS/ARIMA/Theta and ensemble, LightGBM, CatBoost, DeepAR, TFT, PatchTST, and nine pretrained models (App. A.6, p. 24). Skill scores and win rates with 95% CIs (Table S4, p. 31).

## Results (with page or section references)
- Family comparison: Chronos = individual observations, autoregressive sampling, cross-entropy, max context 512; Chronos-Bolt and Chronos-2 = patches, multi-step quantile forecast, quantile loss (Table S3, p. 31).
- fev-bench point skill (MASE): Chronos-2 35.5 (CI 31.6–39.5); Chronos-Bolt 26.5; TimesFM-2.5 30.3; CatBoost 23.7; LightGBM 21.7; Seasonal Naive 0.0; Naive −16.7 (Table S4, p. 31).
- Speed: 100 series in under one second on one mid-range GPU (Abstract, p. 1).

## Limits and risks to validity
_My assessment:_ general benchmarks, not finance; the original token-based Chronos is not in Table S4, so the gain cannot be attributed to dropping tokens. Still evidence that the leading general TSFM builders now prefer continuous patches plus quantile heads.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Benchmark held-out windows |
| Baselines | 2 | Naive, seasonal naive, stats, GBTs, deep and pretrained |
| Point-in-time and leakage controls | 1 | Benchmark protocols followed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | ~200 tasks, finance marginal |
| Statistical testing | 1 | Bootstrap CIs; no multiple-testing correction |
| Reproducibility | 2 | Code, weights and benchmarks public |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "decodes multiple forecast patches in a single forward pass" (§2, p. 3)
