---
type: lit-note
title: "It Is an Equal Failing to Trust Everybody and to Trust Nobody: Stock Price Prediction Using Trust Filters and Enhanced User Sentiment on Twitter"
authors: [Teng-Chieh Huang, Razieh Nokhbeh Zaeem, K. Suzanne Barber]
year: 2019
venue: ACM Transactions on Internet Technology (UT CID Report 21-08)
source_url: https://identity.utexas.edu/sites/default/files/2021-12/it-is-an-equal-failing-to-trust-everybody-and-to-trust-nobody-stock-price-prediction-using-trust-filters-and-enhanced-user-sentiment-on-twitter.pdf
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11]
family: [sentiment]
evidence: Weak
score: 4
tags: [lit-note, family/sentiment, source-reliability]
---
# Stock Price Prediction Using Trust Filters and Enhanced User Sentiment on Twitter (Huang, 2019)

**Basis:** UT Center for Identity report version (Nov 2021) of the ACM TOIT paper, read through a page-fetch summary. DOI not confirmed.

**Takeaway:** Weighting tweets by user trust scores (topic expertise, experience, retweet-network authority and reputation) raised six-month strategy ROI over unweighted sentiment (e.g., 4.26% vs 2.81%), but the test is one short window on a 1% tweet sample with no costs.

## Problem
Does scoring users' credibility before aggregating sentiment improve stock predictions?

## Data and period
1% Twitter "spritzer" sample, Nov 2015–Apr 2016: 31,308 stock tweets by 9,324 users on 507 stocks (Table 1, pp. 1:7, 1:11).

## Method
Four trust filters (Expertise, Experience, HITS Authority, PageRank Reputation) recomputed monthly from the previous month (pp. 1:5–1:6); sentiment-driven buy/sell simulation with $100 per stock.

## Baselines and validation
Unweighted "Simple Accumulation" and buy-and-hold; single six-month backtest, no separate train/test split (pp. 1:7, 1:13).

## Results (with page or section references)
- Final ROI (buy-zero start): Authority 4.26%, Experience 3.70%, Expertise 3.48%, Reputation 3.52% vs Simple 2.81% and buy-and-hold 1.35% (Table 5).
- With a second sentiment engine, gains shrink (Simple 0.95% vs filters 1.01–1.38%; buy-and-hold 1.35%) (Table 7).

## Limits and risks to validity
_My assessment:_ six months; tiny sample; no costs; no significance tests; results sensitive to the sentiment engine.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Trust from prior month; one window |
| Baselines | 1 | Unweighted sentiment, buy-and-hold |
| Point-in-time and leakage controls | 1 | Prior-month trust scores |
| Costs and realism | 0 | None |
| Sample breadth | 1 | 507 stocks, 6 months |
| Statistical testing | 0 | None |
| Reproducibility | 0 | None |
| **Total** | **4/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
