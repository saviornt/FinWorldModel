---
type: lit-note
title: "Multimodal Stock Price Prediction: A Case Study of the Russian Securities Market"
authors: [Kasymkhan Khubiyev, Mikhail Semenov]
year: 2025
venue: "arXiv (q-fin.ST); preprint for Program Systems: Theory and Applications"
source_url: https://arxiv.org/abs/2503.08696
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7]
family: [fusion]
evidence: Weak
score: 6
tags: [lit-note, family/fusion]
---
# Multimodal Stock Price Prediction: A Case Study of the Russian Securities Market (Khubiyev & Semenov, 2025)

**Basis:** arXiv v1 (5 Mar 2025), pp. 1–15, via the alphaXiv PDF reader. Guide seed source.

**Takeaway:** Adding mean-pooled Qwen2.5-0.5B news embeddings to an LSTM cut next-day price MAPE by 55% (0.397% → 0.256%) on 18 MOEX stocks, but every text variant lowered direction accuracy versus price-only LSTM (52.0% → 46.97–49.80%), so the headline gain is on a metric that a near-random-walk forecast already makes tiny.

## Problem
Whether combining candlestick series with Russian-language news embeddings improves price forecasts over price-only models (pp. 1–2).

## Data and period
176 MOEX stocks (07/2022–08/2024) and 79,555 Russian news articles from six sources; experiments reported for 18 stocks across nine sectors. Train 07/2022–03/2024, test 28/03/2024–30/08/2024 (a falling market) (pp. 2–3, 10). Dataset public on Kaggle (p. 10).

## Method
Five-day window of OHLC returns (20 features) concatenated with an aggregated (sum or mean) news embedding from RuBERT (768-d) or Vikhr-Qwen2.5-0.5B (896-d), zero vector if no news; LSTM predicts next-day return. Keyword matching for ticker linkage; Siamese network to filter rewritten (duplicate) news; only previous-day news used (pp. 7–9).

## Baselines and validation
Price-only LinReg, KNN, DT, RF, XGBoost, LSTM. Accuracy (direction) and MAPE of implied price. Single chronological split (pp. 4, 10).

## Results (with page or section references)
- Price only: LSTM accuracy 52.02%, MAPE 0.397%; XGB 45.0%, LinReg 50.15% (p. 10, Table 9).
- With news: LSTM-Qwen-Mean accuracy 48.55%, MAPE 0.256%; LSTM-Qwen-Sum 46.97%; LSTM-RuBERT-Mean 49.80%; LSTM-RuBERT-Sum 48.15% (p. 10, Table 10).
- Mean pooling beat sum pooling; the larger-context LLM beat RuBERT on MAPE (p. 11).
- Authors note the test window's clear downtrend "simplifies the prediction task" (p. 11).

## Limits and risks to validity
_My assessment:_ MAPE on next-day price is dominated by the previous price; direction accuracy (the economically relevant metric) got worse with text. One 5-month test window, 18 stocks, no significance tests, no costs. Qwen2.5 (2024) embeds 2022–2024 news that predates its training cutoff, with no memorisation control (rubric cap). Practical value: news de-duplication and previous-day-only alignment are documented.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | XGB, RF, LSTM; no explicit random walk |
| Point-in-time and leakage controls | 1 | Previous-day news only; LLM pre-cutoff not controlled |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 18 stocks, one regime |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Dataset public; code not stated |
| **Total** | **5/12 → 6/14, capped** | Weak (LLM on pre-cutoff text) |

## Quotes worth keeping (each under 15 words, with page)
- "The presence of a clear trend is a significant factor that simplifies the prediction task." (p. 11)
