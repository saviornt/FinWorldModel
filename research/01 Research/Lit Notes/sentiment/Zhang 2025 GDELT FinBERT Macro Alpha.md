---
type: lit-note
title: "Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study"
authors: [Yuke Zhang]
year: 2025
venue: arXiv 2505.16136
source_url: https://arxiv.org/abs/2505.16136
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14]
family: [sentiment]
evidence: Moderate
score: 8
tags: [lit-note, family/sentiment]
---
# Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study (Zhang, 2025)

**Basis:** v1 (22 May 2025), full text via alphaXiv (pp. 1–12).

**Takeaway:** Daily aggregates of FinBERT headline sentiment and GDELT Goldstein scores (mean, dispersion, volume, lags) fed to XGBoost reportedly gave out-of-sample Sharpe ratios of 4.65–5.87 on EUR/USD, USD/JPY and 10-year Treasury futures (2017–2025, after flat costs); the numbers are implausibly large and unconfirmed, so this is useful as a feature recipe, not as evidence of size.

## Problem
Can global news, scored by a small finance encoder and summarised with GDELT event metadata, predict next-day macro asset direction?

## Data and period
GDELT v2 events Jan 2015–Apr 2025, EventCode 100–199, top 100 events per day by article count; headlines re-fetched from the stored URLs; Yahoo Finance prices (pp. 3, 5).

## Method
FinBERT (ProsusAI) polarity p+ − p− per headline; daily mean, standard deviation, volume, "article impact" (mean × log volume), Goldstein mean and dispersion, lags, moving averages; plus lagged return and 20-day volatility; logistic regression and XGBoost; long/short on p > 0.5 (pp. 4–6).

## Baselines and validation
Logistic regression only; no buy-and-hold, random-walk or price-only model reported. 5-fold expanding-window TimeSeriesSplit, tuning inside each training fold, first test from 2017 (pp. 5–6). Flat costs 0.02% (FX) and 0.05% (ZN) per round trip. Block-bootstrap CIs mentioned but not shown (p. 6).

## Results (with page or section references)
- XGBoost Sharpe 5.87 (EUR/USD), 4.65 (USD/JPY), 4.65 (ZN); CAGR 55%, 53%, 22%; win rate 66–73% of days. Logistic Sharpe 0.83, 0.66, −0.15 (Table 1, p. 7).
- SHAP: sentiment dispersion and article impact rank highest (p. 7).

## Limits and risks to validity
_My assessment:_ a 72% daily win rate on EUR/USD from public news is far outside any other result in this vault and points to an error or leak; the Table 1 caption still contains a drafting note about verifying the numbers (p. 7). Headlines were fetched in 2025 from GDELT URLs, so headline text and availability are not point-in-time; GDELT event dates do not equal first-publication times; the day-t close cut-off is asserted, not checked. No price-only ablation, so the text contribution is not isolated. Single author, no peer review.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding-window folds |
| Baselines | 1 | Logistic only |
| Point-in-time and leakage controls | 1 | Day-t alignment stated; headlines fetched later |
| Costs and realism | 1 | Flat costs |
| Sample breadth | 1 | Three instruments, 2017–2025 |
| Statistical testing | 0 | CIs not reported |
| Reproducibility | 2 | Code on GitHub; GDELT public |
| **Total** | **8/14 → Moderate** | Rubric score Moderate; results flagged as implausible |

## Quotes worth keeping (each under 15 words, with page)
- "sentiment dispersion and article impact are key predictive features" (abstract, p. 1)
