---
type: lit-note
title: "Predicting Stock Price Direction on Earnings Announcement Days using Multi-modal Deep Learning"
authors: [Manuel Noseda, Nathan Soldati, Marco Paina]
year: 2026
venue: "arXiv (cs.LG); ETH Zürich course project"
source_url: https://arxiv.org/abs/2605.25894
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7, RQ1.3]
family: [fusion]
evidence: Weak
score: 5
tags: [lit-note, family/fusion]
---
# Predicting Stock Price Direction on Earnings Announcement Days using Multi-modal Deep Learning (Noseda, Soldati & Paina, 2026)

**Basis:** arXiv v1 (25 May 2026), pp. 1–6, via the alphaXiv PDF reader.

**Takeaway:** On S&P 500-scale firms' earnings days (±3% three-class target), adding daily FinBERT sentiment to fundamentals and price features raised macro-F1 modestly (Transformer 0.359 → 0.390; LSTM 0.292 → 0.325), but with accuracy near 39–44% on a test set of about 150 events and no significance tests, the evidence is anecdotal.

## Problem
Whether pre-announcement news sentiment adds to fundamentals and recent prices for earnings-day direction (p. 1).

## Data and period
Top-500 US firms by market cap; a ten-month window; news from a Markets API feed; 15 FactSet fundamentals, adjusted close and two moving averages, 3 FinBERT probabilities; 30-day window before each announcement (p. 2).

## Method
Logistic regression, 2-layer LSTM, 2-layer Transformer encoder; weighted cross-entropy for class imbalance; with and without sentiment (pp. 2–3).

## Baselines and validation
Logistic regression; accuracy, macro-F1, precision for UP/DOWN, custom asymmetric cost (p. 3).

## Results (with page or section references)
- With / without sentiment, macro-F1: logistic 0.367 / 0.370; LSTM 0.325 / 0.292; Transformer 0.390 / 0.359; custom cost lower with sentiment for all three (p. 4, Table 1).

## Limits and risks to validity
_My assessment:_ split design not described in the pages read; ten months is one regime; mean imputation and z-scoring may use full-sample statistics; accuracies such as 38.816% imply a test set near 150 events. Code public. Cited only as a small consistent sign that sentiment adds a little to price and fundamentals at earnings events.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Hold-out (details not stated) |
| Baselines | 1 | Logistic regression only |
| Point-in-time and leakage controls | 0 | Scaling and imputation scope unclear |
| Costs and realism | N/A | Classification only |
| Sample breadth | 1 | ~500 firms, 10 months |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code on GitHub; licensed data |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "Removing sentiment features degrades performance for all models" (p. 4)
