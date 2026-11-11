---
type: lit-note
title: "Classification Modeling with RNN-Based, Random Forest, and XGBoost for Imbalanced Data: A Case of Early Crash Detection in ASEAN-5 Stock Markets"
authors: [Deri Siswara, Agus M. Soleh, Aji Hamim Wigena]
year: 2024
venue: Scientific Journal of Informatics 11(3), 569–582; arXiv 2406.07888
source_url: https://arxiv.org/abs/2406.07888
doi: 10.15294/sji.v11i3.4067
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.5]
family: [novelty-detection]
evidence: Moderate
score: 6
tags: [lit-note, family/novelty-detection, labels, crash-definition, class-imbalance]
---
# Early Crash Detection in ASEAN-5 Stock Markets (Siswara, 2024)

**Basis:** arXiv 2406.07888v2 (journal version) read via alphaXiv PDF query on 2026-11-08 (pp. 569–581).

**Takeaway:** Defining a "crash" as a next-day index return below the 5%, 2.5% or 1% historical VaR quantile, models without imbalance handling never flag a crash (RNN hit rate 0); with SMOTE-ENN the best models catch about 21% of crash days on average (range 0–64%) with PR-AUC about 0.07 at a 1% base rate, i.e. barely above chance.

## Problem
One-day-ahead crash classification with rare positives.

## Data and period
Daily indices of Indonesia, Malaysia, Philippines, Singapore, Thailand, 2010–2023 (Yahoo Finance); 213 technical predictors × 7 lags = 1,491 inputs (pp. 570–571).

## Method
Crash = return below the VaR quantile "based on the historical distribution" (one threshold per market, Table 4, e.g. Indonesia 1%: −3.13%); KNN imputation for cross-market time gaps; SMOTE-ENN; Simple RNN, LSTM, GRU, RF, XGBoost (pp. 571–574).

## Baselines and validation
Expanding time-series CV with folds ending 2013, 2015, 2019; test 2020–2023 (Table 3, p. 574).

## Results (with page or section references)
- Without resampling, RNNs had hit rate 0 (p. 576).
- 1% scenario: RNN hit rate 0.278, PR score 0.072; XGBoost hit rate 0.038 (Table 5, p. 577).
- Average hit rate across all 21% (p. 578); cites Chatzis 2018 (38–59%) and Dichtl 2023 (9–50%) for comparison.

## Limits and risks to validity
The VaR thresholds appear to be computed on the full 2010–2023 sample (one value per market), so labels use future data; whether SMOTE-ENN was applied only to training folds is not stated; 1,491 features for a few hundred positives.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding TSCV with 2020–2023 test |
| Baselines | 1 | RF/XGBoost; no naive-rule baseline |
| Point-in-time and leakage controls | 0 | Full-sample thresholds; KNN imputation |
| Costs and realism | N/A | Classification only |
| Sample breadth | 1 | Five markets incl. 2020 |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Public data; no code |
| **Total** | 5/12 → 6/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the lowest 5% are considered a market crash" (p. 571)
