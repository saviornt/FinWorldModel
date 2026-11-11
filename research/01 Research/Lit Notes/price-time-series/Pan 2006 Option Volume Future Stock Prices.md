---
type: lit-note
title: "The Information in Option Volume for Future Stock Prices"
authors: [Jun Pan, Allen M. Poteshman]
year: 2006
venue: Review of Financial Studies
source_url: https://nber.org/system/files/working_papers/w10925/w10925.pdf
doi: 10.1093/rfs/hhj024
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, information-diffusion]
---
# The Information in Option Volume for Future Stock Prices (Pan, 2006)

**Basis:** NBER Working Paper 10925 (November 2004), read through a page-fetch summary of the PDF (first ~100k of 105k characters). Published as RFS 19(3), 871–908, 2006 (DOI from EconPapers). Numbers are from the working paper; check against the journal version.

**Takeaway:** Put-call ratios built from buyer-initiated *opening* option volume predict next-day and next-week stock returns (low-minus-high quintile ≈42 bp/day, >1% over a week), the effect decays over about three weeks without reversal, and it comes from non-public order flow rather than from publicly observable volume.

## Problem
Does option trading volume carry information about future stock prices, and is it private information or cross-market inefficiency?

## Data and period
CBOE daily option volume split by trade type (open/close, buy/sell) and investor class, January 1990–December 2001; stocks with ≥50 open-buy contracts a day, ≈242 stocks per day on average (pp. 10–11, 17).

## Method
Daily put-call ratio = open-buy puts / (open-buy puts + calls). Cross-sectional regressions of next-day and next-week four-factor-adjusted returns on the ratio; quintile hedge portfolios; split into a public signal (Lee-Ready signed total volume) and the non-public open-buy signal; interactions with PIN and size; investor classes; moneyness and maturity (pp. 8, 19–31).

## Baselines and validation
Risk adjustment (four-factor), raw returns, public volume signal, liquidity and short-term reversal controls, pre/post 1997 closing-time change, exclusion of earnings dates. Full-sample predictive regressions; no fitted forecasting model, no costs.

## Results (with page or section references)
- Next-day risk-adjusted slope −53 bp (t = −32.9); quintile hedge ≈42 bp/day (t = 28.6), daily Sharpe 0.52 (p. 19); raw-return hedge 38 bp (p. 22).
- Coefficients decay roughly exponentially; first five days sum to >1%; near zero after three weeks; no reversal at longer horizons (pp. 19–20).
- Bivariate regression: open-buy signal stays (−44 bp) while the public signal falls to −5 bp (t = −1.7); the public signal's effect dies faster and partly reverses (pp. 23–24).
- Stronger in small stocks and high-PIN stocks; strongest for full-service customers (incl. hedge funds); none for firm proprietary traders (pp. 26–28).
- Strongest for >10% OTM and short-dated options (leverage) (pp. 29–30). No informed trading found in index options (pp. 32–33).

## Limits and risks to validity
_My assessment:_ relies on proprietary CBOE open/close classification not available in standard feeds; no transaction costs (daily rebalanced hedge would be costly); 1990–2001 only; later work suggests the effect weakened once similar data were sold publicly (not checked here).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Ex-ante signal, no fitted model, but full-sample regressions |
| Baselines | 1 | Factor adjustment, public-volume signal |
| Point-in-time and leakage controls | 2 | Signal from day t volume, returns from t+1; closing-time change checked |
| Costs and realism | 0 | Ignored |
| Sample breadth | 2 | ~242 stocks/day over 12 years incl. 1998 and 2000–01 |
| Statistical testing | 1 | Fama-MacBeth, Newey-West |
| Reproducibility | 0 | Proprietary CBOE data |
| **Total** | **7/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "the economic source of our main result is valuable private information" (p. 3)
- "there is no reversal (i.e., positive coefficients) over longer horizons" (p. 19)
