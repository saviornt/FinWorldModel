---
type: lit-note
title: "Sequential Structure in Intraday Futures Data: LSTM vs Gradient Boosting on MNQ"
authors: [Mathias Mesfin]
year: 2026
venue: arXiv preprint (independent researcher)
source_url: https://arxiv.org/abs/2605.17724
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.1]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, negative-result]
---
# LSTM vs Gradient Boosting on MNQ Intraday Futures (Mesfin, 2026)

**Basis:** full text via alphaXiv.

**Takeaway:** Negative result: on 944 days of 5-minute Micro Nasdaq futures data, neither gradient boosting nor an LSTM beats the base rate out of sample (accuracies 50.00–50.89%; permutation p = 0.135–0.515).

## Problem
Whether Kronos-style sequential bar structure is learnable from four years of single-instrument intraday data (§1).

## Data and period
72,604 five-minute RTH bars, MNQ, Dec 2021–Sept 2025; 944 usable days (§2.1, Table 1).

## Method
HistGradientBoosting on 29–30 decile-tokenised features (three configurations) vs a 16-unit LSTM on the 12-bar return sequence; target: session close > 10:30 open + 10 points (§3–4).

## Baselines and validation
Base rate 51.80%; expanding walk-forward with test years 2023, 2024, 2025; hyperparameters fixed before testing; 200-shuffle permutation tests (§4.3). Expanding-window quantiles for tokenisation to avoid look-ahead (§2.2).

## Results (with page or section references)
- Combined OOS accuracy: GB-Daily 50.00%, GB-Intraday 50.45%, GB-VolAdj 50.89%, LSTM 50.59% (Table 12).
- Best single fold 54.76% has permutation p = 0.135; some shuffled models reach 61.31% on the same fold (Tables 7, 11).
- Top features change across folds, consistent with noise fitting (Table 8).
- LSTM converges to predicting the base rate (§5.4).

## Limits and risks to validity
Minimal LSTM by design; coarse target; price-only sequences (§7.1). _My assessment:_ single instrument, small sample, not peer reviewed; valuable as a documented null and as a warning that small test sets produce high accuracies by chance.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward, 3 folds |
| Baselines | 1 | Base rate; GBT vs LSTM |
| Point-in-time and leakage controls | 2 | Explicit no-look-ahead feature and tokenisation construction |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 0 | One instrument, ~4 years |
| Statistical testing | 1 | Permutation tests, no multiple-testing correction |
| Reproducibility | 0 | No code or data stated |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "No configuration produces out-of-sample accuracy materially above base rate." (Abstract)
