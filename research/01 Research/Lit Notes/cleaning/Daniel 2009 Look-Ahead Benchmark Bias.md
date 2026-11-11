---
type: lit-note
title: Look-Ahead Benchmark Bias in Portfolio Performance Evaluation
authors:
- Gilles Daniel
- Didier Sornette
- Peter Wohrmann
year: 2009
venue: Journal of Portfolio Management 36(1), 121–130
source_url: https://arxiv.org/abs/0810.1922
doi: 10.3905/jpm.2009.36.1.121
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.1
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- survivorship
- index-membership
---
# Look-Ahead Benchmark Bias in Portfolio Performance Evaluation (Daniel, Sornette & Wohrmann, 2009)

**Basis:** arXiv preprint 0810.1922 read in full via alphaXiv on 2026-11-08 (pp. 1–16); journal version not opened.

**Takeaway:** Picking the stock universe from an index's end-of-period members inflates buy-and-hold returns by up to about 8% a year on CRSP 1926–2006: in 2001–2006 an equal-weight portfolio of end-2006 S&P 500 members earned 6.4% a year (Sharpe 0.4) against 2.3% (0.1) for start-2001 members.

## Problem
How large is the bias from using today's index constituents to backtest the past?

## Data and period
CRSP daily prices, splits and shares for 26,892 US stocks, January 1926 – December 2006; eight ten-year periods; top 500 by market cap at start vs end of each period (§3).

## Method
Ex-post (end-of-period top 500) vs ex-ante (start-of-period top 500) equal-weight buy-and-hold portfolios; analytic bias of the estimated bias for mean-variance rules (§4); constrained random strategies as a test (§5).

## Baselines and validation
The ex-ante portfolio is the unbiased reference; two-sample t-tests per decade (Table 1).

## Results (with page or section references)
- 2001–2006: 6.4% vs 2.3% a year; Sharpe 0.4 vs 0.1 (pp. 4–5, Fig. 1).
- Ex-post minus ex-ante: 1.5–7.2% a year by decade (Fig. 3); means differ at 5% in each decade 1967–1996 but not in 1927–1966 or 1997–2006 (Table 1, p. 12).
- Random long-only strategies on the biased universe earn 9.1% ± 4% a year with Sharpe 2 ± 0.8 (p. 9).
- Using biased data, the estimated bias itself understates the true bias (§4).
- 25% of CRSP names disappear within 3.3 years, 75% within 14 years (p. 2).

## Limits and risks to validity
Buy-and-hold and random strategies only; top-500-by-size is a proxy for the S&P 500. Standard t-tests on overlapping data; no correction for multiple periods. Old sample, ends 2006.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Bias measurement |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Subject of the paper |
| Costs and realism | N/A | |
| Sample breadth | 2 | 80 years, all regimes incl. 1929–1940s |
| Statistical testing | 1 | t-tests per decade |
| Reproducibility | 0 | CRSP licensed; no code |
| **Total** | 5/8 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "This apparently innocuous look-ahead bias leads to a huge difference in performance" (p. 4)
