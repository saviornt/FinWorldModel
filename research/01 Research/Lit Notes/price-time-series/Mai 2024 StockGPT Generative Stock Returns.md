---
type: lit-note
title: "StockGPT: A GenAI Model for Stock Prediction and Trading"
authors: [Dat Mai]
year: 2024
venue: arXiv (q-fin.CP)
source_url: https://arxiv.org/abs/2404.05101
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10, RQ1.13]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, tokenization]
---
# StockGPT: A GenAI Model for Stock Prediction and Trading (Mai, 2024)

**Basis:** PDF pages 1, 3–5, 8–12, 14–16, 18–21, 23–24, 26 (v3, Sept 2024).

**Takeaway:** A 0.93M-parameter decoder trained once on daily US returns 1926–2000, with returns cut into 402 fixed 50-bp bins, produces cross-sectional forecasts whose monthly long-short portfolio earns ~13% a year (Sharpe ~1) in 2001–2023 with a 15–16% alpha against 11 factors; daily results are dominated by small caps.

## Problem
Can a GPT architecture trained on return tokens learn price-based patterns (momentum, reversal) without hand-crafted signals? (pp. 2–3)

## Data and period
CRSP common stocks (share codes 10/11) on NYSE, AMEX, NASDAQ. Train 1926–1990, tune 1991–2000, test 2001–2023; the main model is trained on NYSE only (§3, p. 8).

## Method
Returns in basis points cut into 50-bp intervals; bins 0–401; returns beyond ±100% clipped (Table 1, p. 20; §2.3, p. 7). Context 256 days, 4 attention blocks, embedding 128; trained once, never retrained (§2.3, p. 7; p. 2). Forecast = probability-weighted mean of bin midpoints (p. 8).

## Baselines and validation
Fama–MacBeth regressions of realised on predicted returns; decile long-short portfolios; spanning tests against short-term reversal, momentum, long-term reversal, FF5 and q5 factors (§4–5, pp. 9–14). No other ML model and no alternative tokenisation compared.

## Results (with page or section references)
- Daily: slope 0.50 (t = 25.18), cross-sectional R² 1.19% (Table 2, p. 20). Equal-weighted daily long-short 119.1% a year, Sharpe 6.5; value-weighted 27.0%, Sharpe 1.0 (Table 3, p. 20). Skipping one day: EW 26.1%, VW 5.8% (t = 1.2) (Table 3).
- Worst-case cost (400% turnover at 5 bp per trade) leaves 69% a year EW (p. 10).
- Monthly (20-day) model: EW long-short 13.5% a year, Sharpe 0.9–1.0; alpha ~15–16% (t = 4.7) against all factors (Table 6, p. 23; §5.3, p. 13).
- Model trained on all three exchanges is weaker: daily EW 82.5%, VW skip-a-day −0.6% (Table A.1, p. 25).

## Limits and risks to validity
_My assessment:_ the daily headline is a small-cap, equal-weighted, before-realistic-cost result; value-weighted signal mostly disappears after one day. No comparison with a continuous-input model or with simple ML (GBT on past returns), so it says nothing about whether tokenisation helps. Fixed bins of 50 bp put most daily returns in ~40 central bins. No code or data released (CRSP is licensed).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single split, 23-year test, trained once |
| Baselines | 1 | Factor and price-pattern benchmarks; no ML/GBT baseline |
| Point-in-time and leakage controls | 1 | CRSP with delisted names; training ends 2000 |
| Costs and realism | 1 | Flat worst-case cost; small-cap filter only |
| Sample breadth | 2 | All US stocks, 2001–2023 incl. GFC and COVID |
| Statistical testing | 1 | Newey–West t-stats; no multiple-testing correction |
| Reproducibility | 0 | No code or data |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "I treat all daily returns greater than 100% as 100%." (§2.3, p. 7)
