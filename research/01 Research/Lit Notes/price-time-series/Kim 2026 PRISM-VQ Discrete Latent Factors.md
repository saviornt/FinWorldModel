---
type: lit-note
title: "Vector-Quantized Discrete Latent Factors Meet Financial Priors: Dynamic Cross-Sectional Stock Ranking Prediction for Portfolio Construction"
authors: [Namhyoung Kim, Jae Wook Song]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2605.13407
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series, tokenization]
---
# Vector-Quantized Discrete Latent Factors Meet Financial Priors (Kim, 2026)

**Basis:** PDF pages 1–8, 10–11, 17 (v1).

**Takeaway:** A learned 512-code vector-quantisation bottleneck over cross-sectional stock embeddings, plus prior factors and a code-routed mixture of experts, beats XGBoost and nine deep baselines in 2022–2024; removing the codebook is the largest single loss in the ablation, but absolute S&P 500 RankIC is only 0.014.

## Problem
Continuous latent factors over-fit noise in low signal-to-noise return data; does a discrete codebook regularise them? (§1, p. 1)

## Data and period
CSI 300 and S&P 500 via Qlib, contemporaneous constituents; Alpha158 features, 20-day lookback; target 5-day forward return. Train 2009–2019, validation 2020–2021, test 2022–2024 (§5.1, p. 5).

## Method
GRU + cross-asset Transformer embeddings quantised to nearest of K = 512 codewords (straight-through estimator, contrastive and reconstruction losses); frozen codebook then routes a Transformer mixture of experts that outputs dynamic loadings on 13 JKP prior factors and the learned code factors (§4, pp. 3–5).

## Baselines and validation
XGBoost, GRU, TCN, Transformer, CAE, VAE, FactorVQVAE, DTML, MASTER, MATCC, all on identical splits, tuned on validation; 5 seeds; TopK-DropN portfolios with 5 bp open / 15 bp close costs; block bootstrap on daily RankIC (§5.1, p. 5; Table 1 note, p. 6).

## Results (with page or section references)
- CSI 300: RankIC 0.0646 vs XGB 0.0496; Sharpe 1.57 vs 1.15 (Table 1, p. 6).
- S&P 500: RankIC 0.0141 vs XGB 0.0077; Sharpe 0.67 vs 0.43 (Table 1, p. 6). Significant vs 17 of 20 baselines at p < 0.05 (§5.2, p. 6).
- Ablation: without codebook RankIC 0.0472 (CSI) and −0.0024 (S&P) vs full 0.0646 / 0.0141 (Table 2, p. 6). The ablation removes the codebook; whether the replacement is a matched continuous latent is not stated in the part I read.
- Codebook size: K = 512 best in both markets (§5.4, p. 6).

## Limits and risks to validity
_My assessment:_ one test window; many components tuned jointly; large relative gains on very small absolute ICs; seed-averaged RankIC but portfolios from an ensemble. Shows VQ as a regulariser of learned latent states, not as a tokenizer for an autoregressive model.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 2 | XGBoost plus factor-model and deep baselines |
| Point-in-time and leakage controls | 1 | Contemporaneous constituents; priors to t−1 |
| Costs and realism | 1 | Flat costs |
| Sample breadth | 1 | Two markets, one 3-year window |
| Statistical testing | 1 | Block bootstrap; no multiple-testing correction |
| Reproducibility | 1 | Code public; data via Qlib |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Removing the codebook causes the largest degradation" (§5.3, p. 6)
