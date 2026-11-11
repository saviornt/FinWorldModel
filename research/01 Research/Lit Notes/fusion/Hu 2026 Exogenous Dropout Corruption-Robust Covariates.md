---
type: lit-note
title: "Exogenous Dropout: A Simple, Strong Baseline for Corruption-Robust Time Series Forecasting with Covariates"
authors: [Hao Hu, Xue-shan Ai]
year: 2026
venue: "arXiv cs.LG"
source_url: https://arxiv.org/abs/2607.05452
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.15, RQ4.4]
family: [fusion]
evidence: Moderate
score: 7
tags: [lit-note, family/fusion, world-model]
---
# Exogenous Dropout: Corruption-Robust Forecasting with Covariates (Hu & Ai, 2026)

**Basis:** arXiv v1 (5 Jul 2026), pp. 1–2, 4, 7–8, 10–17 (Tables 2, 3, 5, 6), via the alphaXiv PDF reader.

**Takeaway:** On five electricity-price markets, covariate-using forecasters that beat the price-only floor when covariates were clean (DAG −27.5% MSE) became 24–62% worse than the floor when the covariates were noised, shifted by 3–24 hours or missing; randomly zeroing whole covariate channels in training (p = 0.3) brought DAG back to −8% to +3% of the floor at almost no clean-accuracy cost, and a purpose-built gated "fallback" architecture did worse.

## Problem
Exogenous covariates help in clean data but can actively harm forecasts when they are corrupted in deployment; is an architectural bound needed (pp. 1–2)?

## Data and period
EPF (Nord Pool, PJM, Belgium, France, Germany; hourly prices with day-ahead load and generation forecasts), Rapel reservoir, Jena weather; 70/10/20 chronological split, look-back 168, horizon 24 (pp. 7–8).

## Method
Five forecasters (PatchTST floor, TimeXer, DAG, iTransformer, CrossLinear) plus a bounded FiLM-gated foil (BoundEx), each with and without whole-channel exogenous dropout; test-time corruption by Gaussian noise (SNR ≈ 1), misalignment, or all channels missing (pp. 4, 7–8).

## Baselines and validation
Endogenous-only PatchTST as the floor; five seeds; paired t-test, Wilcoxon and bootstrap CIs for the DAG vs BoundEx comparison (pp. 8, 11).

## Results (with page or section references)
- EPF vs floor (clean / Gaussian / misalign / missing): DAG −27.5 / +32.2 / +24.8 / +23.7%; DAG + dropout −26.1 / +3.4 / −7.9 / −4.3%; TimeXer −17.9 / +34.3 / +19.0 / +27.5%; iTransformer +15.5 / +61.9 / +60.8 / +51.9% (p. 10, Table 2).
- iTransformer and CrossLinear were worse than the floor even with clean covariates in all three domains (p. 10, Table 2).
- Learned gate never closed under corruption (EPF mean gate 0.73 clean, 0.60 missing) (p. 17, Table 6).
- Higher dropout (p = 0.5–0.7) made DAG still more robust with small clean cost (p. 15, Table 5).

## Limits and risks to validity
_My assessment:_ electricity prices, not securities; corruption is synthetic; single chronological split. The transferable finding is that a model trained only on clean covariates can be much worse than ignoring them when the feed degrades, and that channel dropout is a cheap guard. Benchmark released.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 1 | Price-only floor and four covariate models |
| Point-in-time and leakage controls | N/A | Covariates are day-ahead forecasts by design |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Five power markets plus two domains |
| Statistical testing | 1 | Paired tests and bootstrap CIs, no multiple-test correction |
| Reproducibility | 1 | Benchmark released |
| **Total** | **5/10 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the exogenous pathway, rather than helping, can actively harm prediction" (p. 2)
