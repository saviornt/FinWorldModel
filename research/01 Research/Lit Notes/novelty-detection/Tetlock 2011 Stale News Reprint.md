---
type: lit-note
title: 'All the News That''s Fit to Reprint: Do Investors React to Stale Information?'
authors:
- Paul C. Tetlock
year: 2011
venue: Review of Financial Studies
source_url: https://scispace.com/pdf/all-the-news-that-s-fit-to-reprint-do-investors-react-to-2iivnc026r.pdf
doi: 10.1093/rfs/hhq141
accessed: 2026-11-08
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ1.11
- RQ1.12
- RQ3.2
family:
- novelty-detection
evidence: Moderate
score: 6
tags:
- lit-note
- family/novelty-detection
- corroboration
---
# All the News That's Fit to Reprint: Do Investors React to Stale Information? (Tetlock, 2011)

**Basis:** October 2010 working-paper version (scispace PDF), read through a page-fetch summary; journal version paywalled. Numbers to check against the RFS version before RP1 is final.

**Takeaway:** News that repeats earlier stories about a firm (high textual overlap) moves prices much less than fresh news, but the move it does cause partly reverses the next week, driven by individual investors who trade on the repetition.

## Problem
Do investors tell repeated (stale) news from new information, and does reacting to repetition move prices temporarily?

## Data and period
All Dow Jones newswire stories on US public firms, Nov 1996–Oct 2008, about 850,000 firm-days across 10,187 firms (pp. 4, 7–8). Individual vs institutional order flow from one Nasdaq market centre, Feb 2003–Dec 2007 (p. 26).

## Method
Staleness = average Jaccard similarity of a story to the previous ten stories on the same firm, on single words (Stale1) and bigrams (Stale2) (p. 9, eq. 2). Fama–MacBeth regressions of post-news returns on day-t abnormal return × staleness; calendar-time portfolios sorted on staleness.

## Baselines and validation
In-sample regressions and portfolios with standard controls; no out-of-sample test; the author notes the order-flow predictability is not an implementable strategy (p. 30).

## Results (with page or section references)
- Initial reaction, bottom vs top staleness decile: 413 bp equal-weighted, 75 bp value-weighted (p. 4).
- Following-week reversal (days 1–5) after stale news: −26.2 bp equal-weighted (≈6.3% of the initial gap; Newey–West t ≈ −4.8), −14.8 bp value-weighted (≈19.8%) (p. 24, Table 6).
- Fama–MacBeth AbRet × Stale1: −0.059 (SE 0.016) (Table 3).
- Individuals trade more in the direction of stale news (+0.90% per SD of staleness); institutions do not; reversal concentrated in stocks with above-median individual trading (pp. 28–30, Table 8).

## Limits and risks to validity
_My assessment:_ in-sample; one newswire; similarity is lexical, so paraphrased repetition is missed; reversal is small relative to the initial move and before costs. The measure is cheap and point-in-time (only past stories), which makes it directly usable as a feature.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | Standard return controls |
| Point-in-time and leakage controls | 1 | Staleness uses only prior stories; timestamps from newswire |
| Costs and realism | N/A | Not a trading claim |
| Sample breadth | 2 | ~10,000 firms, 12 years incl. 2000–02 and 2008 |
| Statistical testing | 1 | Newey–West, Fama–MacBeth |
| Reproducibility | 0 | Licensed data |
| **Total** | **5/12 → 5.8 ≈ 6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "firms' stock returns respond less to stale news" (abstract)
