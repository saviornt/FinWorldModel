---
type: lit-note
title: "Stock Price Prediction Using Triple Barrier Labeling and Raw OHLCV Data: Evidence from Korean Markets"
authors: [Sungwoo Kang, Jong-Kook Kim]
year: 2025
venue: arXiv (cs.CE), v2
source_url: https://arxiv.org/abs/2504.02249
doi: 10.48550/arXiv.2504.02249
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.5]
family: [cleaning]
evidence: Weak
score: 5
tags: [lit-note, family/cleaning, labels, triple-barrier]
---
# Triple Barrier Labels on Korean Stocks (Kang, 2025)

**Basis:** arXiv 2504.02249v2 read via alphaXiv PDF query on 2026-11-08 (pp. 1–7).

**Takeaway:** On all KOSPI/KOSDAQ stocks (2006–2024), triple-barrier parameters were chosen to balance the three classes (29 days, ±9%), and an LSTM on raw OHLCV matched a tuned XGBoost on indicators (macro-F1 0.431 vs 0.432, AUC 0.625 vs 0.625); no fixed-horizon comparison and no trading test, so it shows how TB labels are tuned, not that they help.

## Problem
Can raw OHLCV with TB labels match indicator-based models?

## Data and period
Daily OHLCV for all KOSPI and KOSDAQ tickers, January 2006 – December 2024, scraped from Naver Finance (survivorship unclear); train to March 2020, validation to September 2022, test to December 2024 (p. 3).

## Method
TB labels using daily high/low; grid over 5–29 days and 7–15% barriers to balance classes; same-day double hits labelled "time limit" (p. 3).

## Baselines and validation
Dummy classifier (F1 0.185), 15 PyCaret models, tuned XGBoost (Table III, p. 5).

## Results (with page or section references)
- Label shares: time limit 36.2%, take profit 34.9%, stop loss 29.0% (Table I, p. 3).
- LSTM F1 0.4312 vs XGBoost 0.4316 (Table III).

## Limits and risks to validity
Barrier parameters selected for class balance, not out of sample on value; no costs or trading; reference list contains entries that look fabricated (e.g. generic author names for [4], [9], [11]), lowering trust.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Dummy, XGBoost |
| Point-in-time and leakage controls | 1 | Chronological; label-parameter selection data unclear |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | Whole Korean market, incl. 2008 and 2020 |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code |
| **Total** | 5/12 → 6/14; capped to Weak 5 for suspect references | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "a prediction horizon of 29 days and take-profit/stop-loss percentage of 9%" (p. 3)
