---
type: lit-note
title: "Estimation of tail-related risk measures for heteroscedastic financial time series: an extreme value approach"
authors: [Alexander J. McNeil, Rüdiger Frey]
year: 2000
venue: Journal of Empirical Finance 7(3–4), 271–300
source_url: https://www.wu.ac.at/fileadmin/wu/d/i/statmath/Publications/Publications_Frey/Journal_Papers/evt-garch.pdf
doi: 10.1016/S0927-5398(00)00012-8
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6]
family: [tail-risk]
evidence: Moderate
score: 9
tags: [lit-note, family/tail-risk]
---
# Estimation of tail-related risk measures for heteroscedastic financial time series (McNeil, 2000)

**Basis:** authors' manuscript dated 19 June 1999 (WU Vienna copy), pp. 1–4, 6, 9, 12, 16, 18–19, 21–29, via the alphaXiv PDF reader. Journal details from the EconPapers record; the DOI was not shown in the pages read and is left blank.

**Takeaway:** The standard reference for conditional EVT: filter returns with AR(1)-GARCH(1,1), fit a generalised Pareto tail to the residuals, and the resulting VaR passes violation tests at 95%, 99% and 99.5% on five series (incl. the 1987 crash), where GARCH-normal fails at 99% and above and unconditional EVT is violated in runs during stress.

## Problem
Estimate conditional VaR and expected shortfall that reflect both current volatility and heavy-tailed innovations (pp. 1–3).

## Data and period
Daily negative log returns: S&P 500 (7,414 test days), DAX, BMW (5,146 each), USD/GBP (3,274), gold (3,413) (p. 12, Table 2).

## Method
Pseudo-maximum-likelihood AR(1)-GARCH(1,1) on a rolling 1,000-day window; GPD fitted to the k = 100 largest residuals; refit every day (pp. 6, 12).

## Baselines and validation
Conditional normal (GARCH-normal), conditional t, unconditional EVT; binomial tests on violation counts; one-sided bootstrap test on ES exceedance residuals (pp. 12, 16).

## Results (with page or section references)
- 99% VaR violations, S&P 500: expected 74; conditional EVT 73, conditional normal 104 (p = 0.00), conditional t 78, unconditional EVT 86 (p. 12, Table 2).
- 99.5%: conditional normal rejected on all five series (p = 0.00); conditional EVT not rejected on any (p. 12).
- Unconditional EVT "tends to be violated several times in a row in stress periods" (p. 27, Fig. 7).
- ES: conditional normality fails the test in all cases; GPD residuals rejected for S&P at 99% and 99.5%, DAX at 99.5%, gold at 99% (p. 16, Table 4).
- Conditional t works for symmetric tails but fails when tails are asymmetric (p. 18).

## Limits and risks to validity
_My assessment:_ pre-2000 data, so no GFC or COVID; univariate; violation-count tests only (no independence test in pages read). Its value is as the strong classical baseline that ML tail models must beat.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Daily rolling refit backtest |
| Baselines | 1 | GARCH-normal, GARCH-t, unconditional EVT |
| Point-in-time and leakage controls | 2 | Past-only rolling window |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 2 | 5 series across asset classes, incl. 1987 crash |
| Statistical testing | 1 | Binomial and bootstrap tests |
| Reproducibility | 0 | No code or data |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "an assumption of conditional normality is useless for the purposes of calculating expected shortfall" (p. 16)

**Citation check (2026-11-08):** DOI 10.1016/S0927-5398(00)00012-8 confirmed through OpenAlex by the reference-lookup tool.
