---
type: lit-note
title: "Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction"
authors: [Kasun Dewage, Suranadi De Silva, Shankhadeep Mondal]
year: 2026
venue: arXiv (cs.LG); IEEE (copyright notice)
source_url: https://arxiv.org/abs/2608.08825
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.1, RQ4.4]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series]
---
# Hybrid Neural-Classical Correction for Frozen TSFMs (Dewage, 2026)

**Basis:** full text via alphaXiv.

**Takeaway:** Frozen TimesFM is no better than a historical-mean forecast for opening-hour returns of 10 tech stocks; most of the gain from a correction model comes from a random-forest residual stage, in a 40-day test.

## Problem
How to adapt a frozen TSFM to 1-minute return prediction for 9:30–10:30 using pre-market data (§I).

## Data and period
1-minute bars for NVDA, MSFT, AAPL, GOOG, GOOGL, AMZN, META, AVGO, TSLA, NFLX, Dec 2024–Jan 2026; 186/40/40 train/val/test days per stock (§IV.A, Table II).

## Method
Frozen TimesFM (200M) + neural corrector (AttnCorrect ~471K or GatedLinear ~49K parameters) + random forest on residuals (§III).

## Baselines and validation
Historical mean, MLP, LSTM, BiLSTM, frozen TimesFM; chronological split; training-only normalisation (§IV.B). No significance tests; no costs.

## Results (with page or section references)
- Frozen TimesFM RMSE 0.1946%, equal to HistMean 0.1946%; per-day correlation 0.0586 vs 0.0442 (Table III).
- GatedLinear+RF: RMSE 0.1535%, per-day correlation 0.3730, pooled 0.5972 (Table III).
- RF adds +0.158 per-day correlation to GatedLinear; largest single component (Table V).
- Authors warn that pooled correlation can be inflated by cross-day variance structure (§VI.A).

## Limits and risks to validity
Authors list: 10 large-cap tech stocks, 40-day test, no costs, TimesFM only (§VI.E). _My assessment:_ correlations this high for minute returns over 40 days need independent replication; treat as a design hint (trees on summary features), not proof.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 1 | Historical mean and deep nets; no standalone GBT |
| Point-in-time and leakage controls | 2 | Explicit input/label separation, training-only normalisation |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 0 | 10 stocks, 40 test days |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code promised on publication |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "we observe near-zero mean per-day correlation (0.059) with actual returns" (§I)
