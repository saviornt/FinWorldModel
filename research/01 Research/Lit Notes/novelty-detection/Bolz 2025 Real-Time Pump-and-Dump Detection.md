---
type: lit-note
title: "Real-Time Machine Learning Detection of Telegram-Based Pump-and-Dump Schemes"
authors: [Manuel Bolz, Kevin Bründler, Liam Kane, Panagiotis Patsias, Liam Tessendorf, Krzysztof M. Gogol, Taehoon Kim, Claudio J. Tessone]
year: 2025
venue: ACM CCS DeFi Workshop (arXiv 2412.18848)
source_url: https://arxiv.org/abs/2412.18848
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11, RQ1.5]
family: [novelty-detection]
evidence: Weak
score: 3
tags: [lit-note, family/novelty-detection, manipulation]
---
# Real-Time ML Detection of Telegram-Based Pump-and-Dump Schemes (Bolz, 2025)

**Basis:** arXiv v2 (29 Sep 2025), pp. 1, 3–5, 7, 9–10, 13 via alphaXiv.

**Takeaway:** Coordinated crypto pumps announced on Telegram can be classified from the messages almost perfectly (F1 0.98), but predicting the target coin from order-book and trade anomalies works only seconds ahead: the pumped coin was in the top 5 of 51 candidates in 56% of 43 events at 20 s before the pump, falling to 19% at 1 minute.

## Problem
Can coordinated manipulation campaigns be flagged before the target is revealed?

## Data and period
91,295 messages from 43 Telegram pump channels (Dec 2017–Oct 2024), 2,079 pump events; OHLCV for 4,643 coins and order-book/trade data Jul–Oct 2024 on five exchanges (Table 1, pp. 3–4).

## Method
GPT-4o labels 21,092 messages into six classes, manually checked; BERTweet fine-tuned (duplicates removed from test set) (p. 4). Target prediction: market-cap filter plus z-scores of order-book and trade metrics over a 3-day window (pp. 4–5).

## Baselines and validation
80/20 random split for the message classifier (not by time); target-coin backtest on 43 Poloniex events vs 50 random coins each; no baseline model beyond random ranking (chance top-5 ≈ 10%).

## Results (with page or section references)
- Message classifier weighted F1 0.982 (Table 3).
- Target in top 5: 55.8% (20 s), 41.5% (40 s), 19.1% (1 min); trade-only 46.5% → 9.5% (Table 4, p. 5).
- 95.7% of 1,431 pumped coins had market cap ≤ $60M; median $2.7M (p. 7).

## Limits and risks to validity
_My assessment:_ tiny target-prediction sample; random split for the text classifier with repeated templates inflates F1; z-score thresholds unvalidated across time. Lead time of seconds means coordinated-campaign detection is mainly a filter (ignore these assets/periods) rather than a forecast.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out events; classifier split not temporal |
| Baselines | 0 | Random ranking only |
| Point-in-time and leakage controls | 1 | Data cut 20 s–1 min before pump |
| Costs and realism | N/A | Detection, not trading |
| Sample breadth | 1 | Many coins, 43 test events |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Not stated |
| **Total** | **3/12 → 3/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "its predictive power diminishes as the time offset increases" (p. 5)
