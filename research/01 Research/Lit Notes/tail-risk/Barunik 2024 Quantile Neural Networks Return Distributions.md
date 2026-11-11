---
type: lit-note
title: "Forecasting stock return distributions around the globe with quantile neural networks"
authors: [Jozef Baruník, Martin Hronec, Ondřej Tobek]
year: 2024
venue: arXiv (q-fin.GN), v2 Aug 2025
source_url: https://arxiv.org/abs/2408.07497
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6, RQ1.1]
family: [tail-risk]
evidence: Moderate
score: 8
tags: [lit-note, family/tail-risk]
---
# Forecasting stock return distributions around the globe with quantile neural networks (Baruník, 2024)

**Basis:** arXiv v2 pp. 1–2, 4, 6, 11, 17–19, 21, 28, 63–64, 68, 77–78 via the alphaXiv PDF reader. The acknowledgements thank an editor and reviewers, but the journal is not named in the pages read.

**Takeaway:** A two-stage quantile neural network on 176 firm and market features beats GARCH, linear, shallow NN, random forest and gradient-boosted trees on out-of-sample quantile loss for monthly stock returns in the US, Europe, Japan and Asia-Pacific (1995–2018), including the extreme tails; the edge narrows and loses significance in 2019–2023, and no VaR backtest is run.

## Problem
Forecast the full distribution of next-month stock returns without parametric assumptions (pp. 1–2).

## Data and period
US and international stocks, monthly, out of sample 1995–2018 plus a US extension 2019–2023; trained annually on an expanding window on US data only (pp. 17, 19, 63).

## Method
Multi-output network for 37 quantiles (τ from 0.00005 to 0.99995) of volatility-standardised returns, times a market-volatility sub-network; cubic B-spline interpolation to a CDF and moments (pp. 4, 6, 11).

## Baselines and validation
GARCH, linear, 1-layer and 2-layer NNs; RF and GBRT in Appendix I; Newey–West-adjusted DM tests (pp. 17–19, 77).

## Results (with page or section references)
- Average quantile loss (×100), US full sample: two-stage 2.550 vs GARCH 2.659, 2hNN 2.564 (p. 19, Table 4).
- Tail quantiles, US full sample: τ = 0.01 loss 0.409 vs GARCH 0.469; τ = 0.001 0.059 vs 0.074 (p. 68, Table G1).
- vs trees (7 quantiles): US 2.907 vs RF 2.984 and GBRT 2.994 (p. 78, Table I1).
- 22-day volatility RMSE US full: 7.46 vs GARCH 13.14 (p. 21, Table 6).
- 2019–2023: quantile-loss gains over other NNs are no longer significant at 5% (p. 64).
- "A formal backtesting exercise in this context is beyond the scope" (VaR) (p. 21).

## Limits and risks to validity
_My assessment:_ calibration of tail quantiles (exceedance rates) is not tested, only quantile loss; monthly horizon; crisis periods not split out. Long-short Sharpe of 4.34 (p. 78) is reported without costs in the pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding window, annual retraining |
| Baselines | 2 | GARCH, linear, NNs, RF, GBRT |
| Point-in-time and leakage controls | 1 | Train on US, test abroad; feature timing not in pages read |
| Costs and realism | 0 | Portfolio results without costs in pages read |
| Sample breadth | 2 | Four regions, 1995–2023 incl. GFC |
| Statistical testing | 1 | Newey–West DM tests |
| Reproducibility | 0 | Not stated in pages read |
| **Total** | **8/14 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the model's ability to predict volatility remains robust and statistically meaningful" (p. 64)
