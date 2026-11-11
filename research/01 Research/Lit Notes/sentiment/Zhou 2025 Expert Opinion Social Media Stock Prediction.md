---
type: lit-note
title: "Unleashing Expert Opinion from Social Media for Stock Prediction"
authors: [Wanyun Zhou, Saizhuo Wang, Xiang Li, Yiyan Qi, Jian Guo, Xiaowen Chu]
year: 2025
venue: arXiv 2504.10078
source_url: https://arxiv.org/abs/2504.10078
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11, RQ1.3]
family: [sentiment]
evidence: Moderate
score: 6
tags: [lit-note, family/sentiment, source-reliability]
---
# Unleashing Expert Opinion from Social Media for Stock Prediction (Zhou, 2025)

**Basis:** v2 (10 Nov 2025), pp. 1–6 and 9–12 via alphaXiv. Code: github.com/wanyunzh/DualGAT.

**Takeaway:** Crowd StockTwits sentiment predicted next-day direction worse than a coin flip (47.6%), but users selected by a track record across market regimes (after de-spamming) were right 72.8% of the time; the catch is that these signals cover only ~4% of stock-days and, once fed into a strong price model, added little (S&P 500 IC 7.15% → 8.26%; Nasdaq 100 7.83% → 7.98%).

## Problem
Can source reliability (user track record) turn noisy social sentiment into a usable signal?

## Data and period
All StockTwits posts 2010–2023 with self-labelled bullish/bearish tags; prices from Polygon.io, fundamentals from EODHD; temporal model pre-trained 2010–18, DualGAT trained/validated 2019–21, tested 2022–23 on Nasdaq 100, S&P 500 and StockNet (pp. 9–10).

## Method
De-spam (keep each user's last post per stock-day); expert if ≥80% accuracy on last 20 posts spanning ≥5 days and ≥65% over two years; inverse experts symmetrically (Algorithm 1, pp. 5–6). Dual graph attention (industry + correlation) propagates sparse expert signals to related stocks (Sec. V).

## Baselines and validation
Four published expert-identification methods; 12 deep time-series and graph models; single chronological split; long-short decile portfolio with 4 bp costs (pp. 10–11).

## Results (with page or section references)
- Crowd dominant-sentiment direction accuracy 47.6% (T+1), 47.0% (T+3, T+7) (p. 1, Fig. 1).
- Earlier expert methods failed out of sample: users >80% accurate on 20 posts were 54.0% accurate later (p. 5).
- Expert tracing 72.8% at T+1, 13–15 points above prior methods (p. 10).
- With vs without expert signals: Nasdaq 100 IC 7.98 vs 7.83, AR 32.9% vs 32.6%; S&P 500 IC 8.26 vs 7.15, SR 2.92 vs 2.61 (Table II).
- Baselines such as PatchTST and LSTM had IC ≈ 1–4% (Table II).

## Limits and risks to validity
_My assessment:_ most of the gain over baselines comes from the pre-trained model plus graph, not from the expert filter; one test window; universe chosen from current index members (survivorship); AR > 20% at 4 bp for daily long-short deciles looks optimistic; no significance tests. The track-record filter is a cheap, point-in-time reliability weight worth testing.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 1 | Deep and graph models; no RW/GBT |
| Point-in-time and leakage controls | 1 | Posts cut 5 min before close; prices to t−1; current index lists |
| Costs and realism | 1 | Flat 4 bp |
| Sample breadth | 1 | ~500 stocks, 2-year test incl. 2022 |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code released |
| **Total** | **6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "Users identified as experts in the training phase did not perform reliably" (p. 5)
