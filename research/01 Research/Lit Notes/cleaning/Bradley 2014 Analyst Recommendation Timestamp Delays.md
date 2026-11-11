---
type: lit-note
title: Are Analysts' Recommendations Informative? Intraday Evidence on the Impact of Time Stamp Delays
authors:
- Daniel Bradley
- Jonathan Clarke
- Suzanne Lee
- Chayawat Ornthanalai
year: 2014
venue: Journal of Finance 69(2), 645–673
source_url: https://www.scheller.gatech.edu/directory/research/finance/lee/pdf/jump2-1-12.pdf
doi: 10.1111/jofi.12107
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.2
- RQ3.1
family:
- cleaning
evidence: Moderate
score: 7
tags:
- lit-note
- family/cleaning
- timestamps
---
# Are Analysts' Recommendations Informative? Intraday Evidence on the Impact of Time Stamp Delays (Bradley et al., 2014)

**Basis:** authors' working-paper PDF (Georgia Tech) read through a summarising page fetch on 2026-11-08; page numbers are from that version. Journal version not opened.

**Takeaway:** Vendor timestamps for daytime analyst recommendations (I/B/E/S) and guidance (First Call) are often late: of those matched to newswires, about 56% (recommendations) and 58% (guidance) were moved earlier, by about 2.4 hours on average, and the 30-minute reaction to upgrades flips from −0.07% with vendor times to +1.83% with newswire times.

## Problem
Do analyst recommendations move prices, once the event time is right?

## Data and period
NYSE stocks, January 2002 – December 2007, 537 firms; I/B/E/S recommendations and First Call guidance hand-checked against Dow Jones, Reuters and Lexis-Nexis (p. 5).

## Method
Manual timestamp verification against three newswires, then intraday (15-minute) jump and return analysis around corrected times.

## Baselines and validation
Same events with vendor vs corrected timestamps; significance tests.

## Results (with page or section references)
- About 56% of matched daytime recommendations had an earlier newswire time; 61% of those moved to the overnight period (p. 3, Table 3).
- Average delay about 2.4 hours (median 1.3); 3.7 hours average without truncation (p. 12).
- 30-minute returns: upgrades −0.07% (I/B/E/S) vs 1.83% (newswire); downgrades −0.09% vs −2.10%, significant at 1% (Table 4).
- Guidance: about 58% adjusted earlier; an estimated 15% daytime error rate remains (pp. 3, 25).
- Only 13.6% of 3,993 hand-checked recommendations could be matched to a newswire (p. 12, n. 7).

## Limits and risks to validity
Small matched subsample; 2002–2007 only; vendor practices may have changed since. Read through a summarising tool.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Event study |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Subject of the paper |
| Costs and realism | N/A | |
| Sample breadth | 1 | NYSE, six years |
| Statistical testing | 1 | Significance tests |
| Reproducibility | 0 | Licensed data, manual matching |
| **Total** | 4/8 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "critical that time stamps be verified against newswires" (p. 3)
