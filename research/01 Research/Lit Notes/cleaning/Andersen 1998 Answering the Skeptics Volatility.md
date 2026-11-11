---
type: lit-note
title: "Answering the Skeptics: Yes, Standard Volatility Models Do Provide Accurate Forecasts"
authors: [Torben G. Andersen, Tim Bollerslev]
year: 1998
venue: International Economic Review 39(4), 885–905
source_url: https://faculty.washington.edu/ezivot/econ589/AndersenBollerslevIER1998.pdf
doi: 10.2307/2527343
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Weak
score: 4
tags: [lit-note, family/cleaning, realized-volatility]
---
# Answering the Skeptics (Andersen & Bollerslev, 1998)

**Basis:** JSTOR copy of the published article hosted on a University of Washington course page, read via alphaXiv PDF query on 2026-11-08 (pp. 885–900).

**Takeaway:** A daily return is a very noisy reading of that day's volatility; intraday returns carry most of the information about it. Measurement error of daily variance falls from 1.138 (daily return) to 0.381 (8-hour), 0.048 (hourly) and 0.004 (5-minute), and the daily high–low range is about as informative as 2–3-hour returns, so daily OHLC bars fix only a small part of the intraday path.

## Problem
Why do GARCH forecasts explain so little of squared daily returns, and how should volatility be measured ex post?

## Data and period
DM/$ and ¥/$ spot rates, daily estimation; five-minute quotes 1 October 1992 – 29 September 1993 (260 weekdays); continuous-time simulations of 1,000,000 days (§§2–5).

## Method
Population R² under GARCH(1,1); continuous-time stochastic volatility model; realised variance from summed intraday squared returns at m = 1, 3, 24, 288.

## Baselines and validation
One-year out-of-sample GARCH forecasts against ex-post measures at each frequency.

## Results (with page or section references)
- Out-of-sample R² against squared daily returns 0.047 and 0.025 (p. 891); against 5-minute realised variance 0.479 and 0.392 (Table 5, p. 900).
- Measurement error by frequency: 1.138 / 0.381 / 0.048 / 0.004 (DM/$) (Table 3, p. 897).
- High–low range MSE 0.103–0.114, about the accuracy of 2–3-hour returns (fn. 20, p. 898).

## Limits and risks to validity
Two currencies, one year of intraday data; diffusion assumptions. Used here for the information argument (what daily bars do and do not contain), not as a forecasting benchmark.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One-year hold-out |
| Baselines | N/A | |
| Point-in-time and leakage controls | N/A | |
| Costs and realism | N/A | |
| Sample breadth | 1 | Two FX rates plus large simulation |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Proprietary quote data |
| **Total** | 2/8 → 4/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "it is also an extremely noisy estimator" (p. 896)
