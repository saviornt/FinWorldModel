---
type: lit-note
title: "Deep Adaptive Input Normalization for Time Series Forecasting"
authors: [Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis]
year: 2020
venue: IEEE Transactions on Neural Networks and Learning Systems 31(9) (arXiv 1902.07892)
source_url: https://arxiv.org/abs/1902.07892
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6]
family: [cleaning]
evidence: Moderate
score: 7
tags: [lit-note, family/cleaning, normalisation, limit-order-book]
---
# Deep Adaptive Input Normalization (Passalis, 2020)

**Basis:** arXiv 1902.07892v2 full PDF (pp. 1–7) read via alphaXiv on 2026-11-08. Journal details (TNNLS 31(9), 3760–3765, 2020) are from the citation in [[Chen 2026 Centering Drives Normalization Gains]] ref. 13; DOI not looked up, left empty.

**Takeaway:** On FI-2010 limit-order-book data (5 Finnish stocks, 10 days), a learned per-window shift-scale-gate layer raised mid-price-direction Cohen's κ from about 0.31 (global z-score) and 0.37 (instance normalisation) to about 0.49 for an MLP; with no normalisation the models learned nothing (κ ≈ 0); most of the gain came from the learned shift and scale steps.

## Problem
Can a network learn how to normalise non-stationary, multimodal financial inputs?

## Data and period
FI-2010: 4.5M limit orders, 5 Nasdaq Nordic stocks, 1–14 June 2010, 144 features (p. 3); household power data as a second set.

## Method
DAIN: adaptive shift (linear map of window mean), adaptive scale (of window s.d.), sigmoid gate; trained end to end; parameters fixed at inference (pp. 2–3).

## Baselines and validation
No normalisation, global z-score, sample-mean subtraction, batch and instance normalisation; anchored day-by-day walk-forward (9 splits) (pp. 3–4).

## Results (with page or section references)
- MLP κ: none 0.001, z-score 0.306, instance 0.372, DAIN 0.493 (Table I, p. 4).
- Shift and scale sublayers carry the gain; the gate adds ~2.5% for MLP/CNN, nothing for GRU (p. 5).
- Shifting test inputs by 3× their mean cut z-score MLP accuracy 75.4% → 56.6% on power data; DAIN fell <0.5% (p. 5).

## Limits and risks to validity
Ten trading days, five stocks; no trading or cost test; FI-2010's labels and preprocessing are fixed by the benchmark; no significance tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Anchored walk-forward, 9 folds |
| Baselines | 1 | Normalisation variants only |
| Point-in-time and leakage controls | 1 | Walk-forward; global z-score stats source not stated |
| Costs and realism | N/A | |
| Sample breadth | 0 | 5 stocks, 10 days |
| Statistical testing | 0 | Mean ± s.d. only |
| Reproducibility | 2 | Code and public data |
| **Total** | 6/12 → 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
