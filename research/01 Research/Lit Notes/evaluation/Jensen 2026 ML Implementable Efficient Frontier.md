---
type: lit-note
title: "Machine Learning and the Implementable Efficient Frontier"
authors: [Theis Ingerslev Jensen, Bryan T. Kelly, Semyon Malamud, Lasse Heje Pedersen]
year: 2026
venue: Review of Financial Studies (in press, 2026); SFI Research Paper 22-63 (SSRN 4187217)
source_url: https://afajof.org/management/viewp.php?n=32368
doi: 10.1093/rfs/hhag022
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.6]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation, economic-value, transaction-costs, capacity]
---
# Machine Learning and the Implementable Efficient Frontier (Jensen, Kelly, Malamud & Pedersen)

**Basis:** Working-paper version of 12 Feb 2023 (AFA copy), read 2026-11-09 through a summarising page fetch; page numbers as reported by the fetch and may be off by one. Journal status (RFS, in press) from the Swiss Finance Institute publication page seen in search. Numbers should be checked against the published version.

**Takeaway:** Judged net of realistic, size-dependent trading costs, standard "forecast returns, then optimise" ML portfolios are not implementable (Markowitz-ML has the best gross Sharpe, 2.00, but deeply negative net results; a decile sort goes from gross 1.10 to net −11.87), while learning portfolio weights directly with costs in the objective gives net Sharpe 1.38 for a $10B investor; value and quality, not fleeting reversal signals, carry the net value.

## Problem
Evaluate strategies by net-of-cost return per unit of risk (the "implementable efficient frontier") and build ML portfolios that are good on that frontier (abstract, pp. 1–6).

## Data and period
US common stocks above the NYSE median market cap (~1,204 stocks at end-2020), 115 rank-standardised characteristics, 1952–2020; monthly out-of-sample backtests 1981–2020 (pp. 22–23).

## Method
Portfolio-ML learns portfolio weights directly with an economic (utility, net of costs) objective, generalising Gârleanu–Pedersen; costs calibrated to Frazzini et al. (2018): a trade of 1% of daily volume moves price 0.1%; investor wealth $10B baseline, also $0, $1B, $100B (pp. 23–24, 37).

## Baselines and validation
Markowitz-ML, portfolio sort, Static-ML and Multiperiod-ML with a second tuning layer; hyperparameters re-chosen each year by validation backtests starting 1971 (pp. 27–28). Bayesian probabilities of higher utility (Table 3, p. 32).

## Results (with page or section references)
- Net Sharpe / utility / monthly turnover: Portfolio-ML 1.38 / 0.095 / 0.32; Multiperiod-ML* 1.16 / 0.060 / 0.40; Static-ML* 1.11 / 0.060 / 0.61; portfolio sort −11.87 / −1.921 / 2.60 (Table 2, p. 30).
- Portfolio sort: costs about 1.97 a year against gross excess return 0.17 (p. 30).
- Without the second tuning layer, Multiperiod-ML and Static-ML have negative realised utility (p. 30).
- Probability Portfolio-ML has higher utility: 95–96% vs the tuned benchmarks, 100% vs sort and Markowitz-ML (Table 3, p. 32).
- Net Sharpe falls as risk rises along the frontier, and larger investors face lower frontiers (at 14% volatility: ~19% net excess return for $10B vs ~22% for $1B) (p. 37).
- Value and quality have the highest economic feature importance; short-term reversal barely matters net of costs (pp. 5–6, 38).

## Limits and risks to validity
_My assessment:_ read through a summarising fetch, not the PDF; large-cap universe only; cost model is a calibrated linear-impact assumption, not executed trades; no 1/N or market benchmark reported in the part read. Strong design overall, held at Moderate for the unscored statistical and reproducibility checks.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Annual re-tuning on validation backtests, 1981–2020 |
| Baselines | 1 | ML and sort benchmarks; no 1/N or market reported |
| Point-in-time and leakage controls | 1 | Monthly characteristics; PIT handling not seen |
| Costs and realism | 2 | Volume-based impact, wealth levels, turnover |
| Sample breadth | 2 | ~1,200 stocks, 40 years incl. several crises |
| Statistical testing | 1 | Bayesian comparison probabilities |
| Reproducibility | 0 | Code/data release not seen |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept (summarised read).

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
