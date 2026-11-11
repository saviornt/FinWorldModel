---
type: lit-note
title: "Crowds on Wall Street: Extracting Value from Collaborative Investing Platforms"
authors: [Gang Wang, Tianyi Wang, Bolun Wang, Divya Sambasivan, Zengbin Zhang, Haitao Zheng, Ben Y. Zhao]
year: 2015
venue: ACM CSCW 2015
source_url: https://sites.cs.ucsb.edu/~tianyi/doc/alpha.pdf
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11, RQ1.3]
family: [sentiment]
evidence: Moderate
score: 6
tags: [lit-note, family/sentiment, source-reliability]
---
# Crowds on Wall Street: Extracting Value from Collaborative Investing Platforms (Wang, 2015)

**Basis:** author PDF read through a page-fetch summary (no page markers in the extracted text). DOI not confirmed; left empty.

**Takeaway:** Average sentiment on SeekingAlpha and StockTwits barely predicted returns (best correlation ≈0.05), but authors ranked on the previous year's record kept some skill the next year on edited SeekingAlpha (correlation ≈0.12 out of sample) and not on open StockTwits; ranking by reader comments worked best.

## Problem
Does filtering a crowd platform by contributor reputation recover useful signals?

## Data and period
SeekingAlpha 2004–Apr 2014 (410,290 articles, 8,783 authors); StockTwits 2009–Feb 2014 (12.7M messages, 86,497 users).

## Method
Lexicon sentiment per article/message; author ranking by prior-year hypothetical return per article/stock or by comments per article; yearly re-ranked trading simulations.

## Baselines and validation
All-content sentiment; S&P 500; rank-on-2012/test-on-2013 check and yearly re-ranking (walk-forward by construction).

## Results (with page or section references)
- All-content correlation with future returns ≤ ≈0.05 (≈53% direction accuracy); StockTwits weaker and sometimes negative.
- Top SeekingAlpha authors: ≈0.4 in sample, ≈0.12 out of sample; StockTwits top users did not persist.
- SeekingAlpha comment-ranked strategy ≈108% over 8 years vs 47.8% S&P 500 (no dividends, no costs); StockTwits ≈54.5% vs 64.1%.
- 80% of surveyed users had seen manipulative articles.

## Limits and risks to validity
_My assessment:_ no costs or dividends; lexicon sentiment; returns not risk-adjusted; per-year concentration not reported in text. Supports reliability weighting only where the platform itself curates.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Yearly re-ranking on prior-year data |
| Baselines | 1 | Index, all-content sentiment |
| Point-in-time and leakage controls | 1 | Prior-year rankings only |
| Costs and realism | 0 | Ignored |
| Sample breadth | 2 | Thousands of stocks, 2005–2014 incl. 2008 |
| Statistical testing | 0 | None reported |
| Reproducibility | 0 | No code or data |
| **Total** | **6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "minimal value for investors" (on aggregate sentiment; no page)
