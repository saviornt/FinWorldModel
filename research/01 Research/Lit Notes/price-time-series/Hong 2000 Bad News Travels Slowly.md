---
type: lit-note
title: "Bad News Travels Slowly: Size, Analyst Coverage, and the Profitability of Momentum Strategies"
authors: [Harrison Hong, Terence Lim, Jeremy C. Stein]
year: 2000
venue: Journal of Finance
source_url: https://www.nber.org/digest/nov98/bad-news-travels-slowly
doi: 10.1111/0022-1082.00206
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, information-diffusion]
---
# Bad News Travels Slowly (Hong, 2000)

**Basis:** summary only. The NBER Working Paper 6553 PDF has no machine-readable text, and the JF article is paywalled. Read: the NBER Digest summary (Nov 1998) and the JF abstract on EconPapers (DOI from there). Score reflects what those pages show; table and page references are not available.

**Takeaway:** Momentum profits are largest where information should diffuse slowly: in small (but not the smallest) stocks and, holding size fixed, in stocks with low residual analyst coverage (1.13% vs 0.72% a month), and the coverage effect is much stronger for past losers, so bad news diffuses more slowly than good news.

## Problem
Test the gradual-information-diffusion explanation of medium-term momentum (Hong & Stein 1999).

## Data and period
NYSE, AMEX and NASDAQ stocks with analyst-coverage data, 1980–1996 (NBER Digest).

## Method
Winner-minus-loser (top 30% minus bottom 30% by past return) momentum strategies sorted into 10 size classes; residual analyst coverage (coverage orthogonalised to size) as a proxy for information flow; winners vs losers separately (Digest; abstract). Formation and holding periods not stated on the pages read.

## Baselines and validation
Full-sample momentum (0.53%/month) as the reference; in-sample portfolio sorts.

## Results (with page or section references)
- Full-sample momentum 0.53%/month; negative in the smallest size class (thin trading); peaks at 1.43%/month in the third-smallest class (mean cap $45M); falls to about zero for the largest firms (Digest).
- Low residual coverage 1.13%/month vs high 0.72%/month (Digest).
- Coverage effect far stronger for past losers than past winners (abstract; Digest).

## Limits and risks to validity
_My assessment:_ in-sample sorts; no transaction costs (small, low-coverage stocks are expensive to trade, especially short); results end in 1996. Read only through summaries; magnitudes to be checked against the JF tables.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample sorts |
| Baselines | 1 | Unconditional momentum, size classes |
| Point-in-time and leakage controls | 1 | Lagged coverage implied; not verifiable from summaries |
| Costs and realism | 0 | Ignored |
| Sample breadth | 2 | All US listed stocks, 1980–96, incl. 1987 |
| Statistical testing | 1 | Significance tests reported in summary |
| Reproducibility | 0 | No code; CRSP/I-B-E-S licensed |
| **Total** | **5/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
