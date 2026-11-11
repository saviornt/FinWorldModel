---
type: lit-note
title: "Cashtag piggybacking: uncovering spam and bot activity in stock microblogs on Twitter"
authors: [Stefano Cresci, Fabrizio Lillo, Daniele Regoli, Serena Tardelli, Maurizio Tesconi]
year: 2018
venue: ACM Transactions on the Web (arXiv 1804.04406)
source_url: https://arxiv.org/abs/1804.04406
doi: 10.48550/arxiv.1804.04406
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11]
family: [sentiment]
evidence: Weak
score: 2
tags: [lit-note, family/sentiment, bots]
---
# Cashtag piggybacking: spam and bot activity in stock microblogs on Twitter (Cresci, 2018)

**Basis:** arXiv v2 (17 Jul 2018), pages 1, 3, 5–6, 9–11, 19–21, 25 via alphaXiv. Journal DOI not confirmed; arXiv DOI used. Dataset on Zenodo (10.5281/zenodo.2686861).

**Takeaway:** Bursts in cashtag tweet volume are largely mass retweets by coordinated bots that pair a few popular large-cap tickers with many unrelated OTC tickers; 71% of accounts behind the 100 largest bursts were classified as bots, so raw tweet counts and spikes are contaminated.

## Problem
How much stock-microblog activity is spam or bot-driven?

## Data and period
~9M tweets with cashtags, May–Sep 2017, ~2.5M users, 30,032 companies on five US markets; financial data from Google Finance (pp. 3, 6, Table 1).

## Method
Hourly tweet-count series per stock; peaks > mean + 10 SD (1,926 peaks); analysis of retweet share and cashtag co-occurrence in peak tweets; group bot detection with "digital DNA" (reported F1 0.97 on evolved bots) on 25,957 users from the top 100 peaks; Twitter suspension check (pp. 10, 19–20).

## Baselines and validation
Descriptive; no price-prediction test.

## Results (with page or section references)
- Peak tweets were 60% retweets vs 23% in the whole dataset, with many more cashtags per tweet (p. 10).
- 71% (18,509) of users behind top-100 peaks classified as bots; 37% (9,490) suspended by Twitter within months; 94% of suspended accounts were also flagged by the detector (p. 20).
- OTC tweets were 76% retweets (Table 1).

## Limits and risks to validity
_My assessment:_ five months of 2017 data; Twitter's API and bot ecosystem have since changed; no link to returns tested; bot labels from one detector. Valuable as a measurement of contamination, not as evidence that filtering improves a signal.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Descriptive |
| Baselines | 0 | None |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Many stocks, 5 months |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Dataset released |
| **Total** | **2/12 → 2/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "as much as 71% of the authors of suspicious financial tweets are classified as bots" (p. 1)
