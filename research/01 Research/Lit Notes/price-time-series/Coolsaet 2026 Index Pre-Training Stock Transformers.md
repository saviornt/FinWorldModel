---
type: lit-note
title: "From Index to Equity: Pre-Training Transformers for Stock Return Prediction"
authors: [Marie Soehl Coolsaet, Roberto Gallardo, Zhen Gao]
year: 2026
venue: arXiv 2605.23962
source_url: https://arxiv.org/abs/2605.23962
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.4, RQ4.8]
family: [price-time-series]
evidence: Weak
score: 3
tags: [lit-note, family/price-time-series, training, staged-training]
---
# From Index to Equity: Pre-Training Transformers (Coolsaet et al., 2026)

**Basis:** Full text (10 pages) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** A transformer trained from scratch on individual TSX stocks never learned past epoch one (BCE 0.6942, predicting one class), while pre-training on the TSX index first and then fine-tuning reached BCE 0.6404; but XGBoost had the best F1, and XGBoost and the ensemble earned far higher test portfolio returns than the pre-trained transformer.

## Problem
Whether pre-training on smoother index data helps a transformer predict noisy individual stock returns (§2).

## Data and period
1,853 TSX tickers from Yahoo Finance, 1980–2023 (current listings, so survivorship-biased); 10 days × 15 technical features; train 2010–2022, validation 2022, test 2023 to 1 Dec 2023 (§2).

## Method
Encoder transformer (4 blocks) pre-trained on the TSX index for intra-day direction, fine-tuned on stocks (all weights; no freezing stated), then fine-tuned again for regression by swapping the output layer; LSTM pre-trained the same way; XGBoost; averaging ensemble (§2–3).

## Baselines and validation
LSTM and XGBoost; single chronological split; min–max scaling from training data; top-5/bottom-5 daily long–short with no costs (§2–3).

## Results (with page or section references)
- Classification: baseline transformer BCE 0.6942, test F1 0.0000; pre-trained transformer BCE 0.6404, F1 0.0523; XGBoost F1 0.5675 (§4, Table 2).
- Regression test MSE: transformer 5.682e-9, LSTM 5.683e-9, XGBoost 9.923e-9 (Table 3).
- Average daily long–short return: transformer 0.0003, LSTM 0.0002, XGBoost 0.0059, ensemble 0.0069 (Table 4).

## Limits and risks to validity
_My assessment:_ one test year, survivorship-biased universe, no costs, no significance tests, unusual MSE scale; the "pre-training helps" result is relative to a from-scratch transformer that failed to train, not to a strong baseline. Supports only the narrow point that staged training can rescue optimisation of a deep model on very noisy targets; the economically better model was XGBoost.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | XGBoost, LSTM |
| Point-in-time and leakage controls | 0 | Survivorship bias not addressed |
| Costs and realism | 0 | No costs |
| Sample breadth | 1 | Many stocks, one market, one test year |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code |
| **Total** | **3/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "performance failed to improve beyond the first training epoch" (§4)
