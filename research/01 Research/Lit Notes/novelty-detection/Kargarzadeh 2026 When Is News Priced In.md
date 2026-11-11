---
type: lit-note
title: 'Buy the Rumor, Sell the News: When Is News Priced In?'
authors:
- Alireza Kargarzadeh
- Nariman Khaledian
- Navid Parvini
- Sid Ghatak
- Arman Khaledian
year: 2026
venue: ACM AI4F 2026 (arXiv 2608.14014)
source_url: https://arxiv.org/abs/2608.14014
doi: ''
accessed: 2026-11-08
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ1.12
- RQ1.11
- RQ1.14
- RQ3.2
family:
- novelty-detection
evidence: Weak
score: 5
tags:
- lit-note
- family/novelty-detection
- information-diffusion
---
# Buy the Rumor, Sell the News: When Is News Priced In? (Kargarzadeh, 2026)

**Basis:** v2 (18 Oct 2026), pp. 1–2, 4–5, 7–8 via alphaXiv.

**Takeaway:** Across 1.68M tagged stock-day news events (≈3,000 US stocks, 2023–2026), most of the news-direction move happens before and on publication day (pooled running total +0.58% by day-0 close vs +0.20% at day +20); net of a neutral-news placebo, quantified fundamental news keeps drifting (earnings +0.22% over days 6–20) while soft stories reverse, and an apparent sentiment-fade strategy is just the background drift of covered small caps.

## Problem
Where in event time does the news-aligned price move sit, by kind of news?

## Data and period
4.57M deduplicated articles from a commercial crawl of >500k sources, ~3,000 US stocks, 2023–2026 (2023 backfilled); daily adjusted closes for 2,591 symbols (p. 2).

## Method
GPT-5-mini teacher distilled into a small classifier (95% agreement): 17 event tags, five attributes (scheduled, forward-looking, primary source, quantified, rumor); articles clustered into stories to separate first reports from follow-ups; beta-adjusted abnormal returns; 364,405 neutral events and quiet days as placebo; date-bootstrap p-values (pp. 1–2, 4).

## Baselines and validation
Placebo (neutral coverage, quiet days) by size bucket; teacher-only and first-report-only reruns; descriptive, in-sample; calendar-time portfolios with flat costs (Table 6).

## Results (with page or section references)
- Pre-window −5..0 and day 0: earnings +1.41% and +0.42%, analyst actions +1.12% and +0.22%; afterwards ≈ −0.05% to −0.13% raw (p. 4, Table 2).
- Restricting to first reports shrinks the earnings pre-window from +1.41% to +1.02%: follow-up coverage inflates measured anticipation by about a third (p. 4).
- Rumor events: +0.36% on rumor day, nothing to confirmation (−0.09%), +0.01% on confirmation day (p. 4, Table 3).
- Net of placebo: capital returns +0.35%, earnings +0.22%, guidance +0.13%, analyst +0.10% continuation; macro read-throughs −0.34%, launches −0.18% reversal (Table 2).
- Press wires show no pre-publication drift (−0.06%); retail-analysis sites, portals, mainstream media and aggregators +0.8% to +1.1% (Table 5).
- Neutral news widens publication-day moves (guidance 1.29× normal); ≥10 articles 1.36× vs 1.05× (p. 7).
- Fading small-cap launch news (Sharpe 1.35) equals shorting every covered small cap (Sharpe 1.35) (Table 6, Fig. 5).

## Limits and risks to validity
_My assessment:_ one regime (2023–26); in-sample; vendor LLM sentiment may encode realised returns (authors note articles describe moves already made); single-beta benchmark; commercial data, authors linked to the vendor. Strong design features: placebo, first-report split, source groups.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Descriptive, in-sample |
| Baselines | 1 | Neutral-news and quiet-day placebo |
| Point-in-time and leakage controls | 1 | Live daily sentiment; tags retrospective |
| Costs and realism | 1 | Flat per-side costs |
| Sample breadth | 1 | ~3,000 stocks, one regime |
| Statistical testing | 1 | Date bootstrap |
| Reproducibility | 0 | Commercial data |
| **Total** | **5/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "markets underreact to numbers and overreact to stories" (p. 8)
