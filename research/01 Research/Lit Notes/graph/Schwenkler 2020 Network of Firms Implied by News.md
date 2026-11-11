---
type: lit-note
title: "The network of firms implied by the news"
authors: [Gustavo Schwenkler, Hannan Zheng]
year: 2020
venue: ESRB Working Paper Series No 108
source_url: https://www.esrb.europa.eu/pub/pdf/wp/esrb.wp108~40756dc3b5.en.pdf
doi: 10.2139/ssrn.3723464
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.7]
family: [graph]
evidence: Moderate
score: 9
tags: [lit-note, family/graph, news-network, time-valid-graph]
---
# The Network of Firms Implied by the News (Schwenkler, 2020)

**Basis:** ESRB WP 108 (January 2020) PDF read through a summarising page fetch on 2026-11-08 (first ~100k characters; Table 15 cut off). Page numbers as reported by the fetch.

**Takeaway:** Linking two firms whenever they are named in the same sentence of a Reuters article (106,521 articles, 2006–2013) gives a network of 2,961 firms and 20,504 links, each dated by its article's publication date, that contains all overlapping Compustat customer–supplier links and most 10-K similarity and co-search links; its connectivity predicts one-month-ahead market volatility and credit spreads out of sample.

## Problem
Can news text give a dated, wide-coverage firm network?

## Data and period
Reuters financial news (Ding et al. 2015 corpus), 20 Oct 2006 – 20 Nov 2013 (p. 7).

## Method
Named-entity recognition (Stanford CoreNLP) per sentence, rule-based cleaning, matching to CRSP/Compustat; same-sentence co-mention = link; yearly and monthly networks (pp. 7–15).

## Baselines and validation
Alternative networks (Compustat segments, Hoberg–Phillips TNIC, EDGAR co-search, return variance decomposition) as controls; one-month-ahead out-of-sample regressions (p. 24).

## Results (with page or section references)
- Overlap: all Compustat customer–supplier links, 83.9% of TNIC links, 77.5% of co-search links, 55.9% of return-decomposition links (p. 23).
- Connectivity predicts S&P 500 returns, VIX, AAA/BAA spreads and GDP growth one month ahead; higher OOS R² with news measures; F-tests reject no predictability (p. 24; R² values not verified).

## Limits and risks to validity
Co-mention does not give direction or type; read via summary; working-paper version; table values not verified.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One-month-ahead OOS regressions |
| Baselines | 1 | Alternative network controls |
| Point-in-time and leakage controls | 2 | Links dated by publication date |
| Costs and realism | N/A | |
| Sample breadth | 2 | ~3,000 firms, 2006–2013 incl. crisis |
| Statistical testing | 1 | F-tests |
| Reproducibility | 1 | Monthly networks downloadable |
| **Total** | 8/12 → 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
