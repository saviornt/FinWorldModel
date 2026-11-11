---
type: lit-note
title: Twitter Sentiment around the Earnings Announcement Events
authors:
- Peter Gabrovšek
- Darko Aleksovski
- Igor Mozetič
- Miha Grčar
year: 2017
venue: PLOS ONE 12(2)
source_url: https://arxiv.org/abs/1611.02090
doi: 10.1371/journal.pone.0173151
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.2
family:
- cleaning
evidence: Moderate
score: 8
tags:
- lit-note
- family/cleaning
- timestamps
- social
---
# Twitter Sentiment around the Earnings Announcement Events (Gabrovšek et al., 2017)

**Basis:** arXiv version 1611.02090v2 read via alphaXiv on 2026-11-08 (pp. 1–14).

**Takeaway:** Tweets about after-close earnings peak before midnight, but the market reacts the next day; aggregating posts by calendar day instead of by market close makes day −1 sentiment look predictive when it is not, so posts after 4 p.m. must be assigned to the next trading day.

## Problem
Does Twitter sentiment reflect or anticipate earnings-announcement returns, and how does alignment change the answer?

## Data and period
30 DJIA stocks, June 2013 – June 2016; 4.5 million sentiment-labelled tweets; 359 announcements (253 before open, 106 after close) (Table 2, p. 6).

## Method
Days delimited at the 4 p.m. close; event study with polarity from same-day (day 0) or prior-day (day −1) sentiment; a simple short strategy tested on a further six months.

## Baselines and validation
DJIA buy-and-hold; a 0.05 USD per-share spread; out-of-sample half-year.

## Results (with page or section references)
- Day-0 sentiment matches CAR direction: about 4% (after close) and 2% (before open), significant at 1% (p. 9, Fig. 4).
- Day −1 sentiment has almost no predictive power; only negative after-close events show about −1% (p. 10, Fig. 5).
- Calendar-day aggregation would produce spurious prediction for after-close events (p. 11).
- The strategy's 42% over 3.5 years came mostly from six trades in one half-year; out of sample it made two trades with negligible profit (p. 12).

## Limits and risks to validity
30 large stocks, three years; sentiment from one classifier. The alignment lesson is general; the trading result is not.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One later half-year |
| Baselines | 1 | DJIA buy-and-hold |
| Point-in-time and leakage controls | 2 | Market-close alignment explicit |
| Costs and realism | 1 | Flat spread |
| Sample breadth | 1 | 30 stocks, 2013–2016 |
| Statistical testing | 1 | CAR significance |
| Reproducibility | 1 | Data on figshare |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "important to take into account the exact timing of the events" (p. 3)
