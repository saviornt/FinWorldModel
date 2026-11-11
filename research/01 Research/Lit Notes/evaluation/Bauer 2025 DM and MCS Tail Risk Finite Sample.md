---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- forecast-comparison
title: 'Evaluating financial tail risk forecasts: Testing Equal Predictive Ability'
authors:
- Lukas Bauer
year: 2025
venue: arXiv (econ.EM) 2505.23333
source_url: https://arxiv.org/abs/2505.23333
doi: ''
research_questions:
- RQ4.2
- RQ4.3
evidence: Weak
score: 5
---
# Evaluating financial tail risk forecasts: Testing Equal Predictive Ability (Bauer, 2025)

**Basis:** Full text via alphaXiv (v1), read 2026-11-08: abstract, §1, §3.2 (MCS results, Table 3.9, Figure 3.4) and §4. Not every simulation table read.

**Takeaway:** For 1%–2.5% VaR and joint VaR–ES forecasts, Diebold–Mariano and model confidence set tests have little power against models that understate tail risk, give skewed statistics and non-negligible wrong-sign (type III) errors for evaluation windows up to two years; several years of daily data are needed.

## Problem
Finite-sample behaviour of the DM test and Hansen et al.'s MCS when the loss is a strictly consistent tail loss (tick loss for VaR, Fissler–Ziegel loss for VaR and ES) (§1).

## Data and period
Monte Carlo: location-scale models with time-varying variance, t innovations with ν = 3, 7, 12; 1-day VaR/ES at 1%, 2.5%, 5%, 10%; out-of-sample sizes 63 to 2,500 days; m = 5 and m = 10 candidate models incl. constant variance, GARCH-n, GARCH-t, TGARCH-n (§3).

## Method
Pairwise DM tests and the MCS (α = 0.25) on simulated forecasts; reports potency (best model kept), power (MCS size) and type III errors (§3).

## Baselines and validation
Candidate models include the true DGP and a naive constant-variance model (§3.2).

## Results (with page or section references)
- Little power against tail-underestimating models at p = 0.01 and 0.025; power rises with p and out-of-sample size (abstract, §4).
- At p ≤ 0.025 and up to two years out of sample, statistics are heavily skewed with non-negligible type III errors, so standard normal or bootstrap critical values need caution (§4).
- Only a tiny fraction of observations reveals the true ranking at extreme p, which drives sampling variability (§1).
- For up to 10 years of daily data the MCS does not single out the best model; up to about 1,000 days it eliminates the true model and GARCH-t more often than worse models at p = 0.01 (§3.2, Table 3.9).
- Joint VaR–ES evaluation gives more power than VaR alone from two years of data; MCS potency is usually well above 1 − α from four years, so large α is safe in applied work (§4).
- Enlarging the model set from 5 to 10 lowers power against inferior models (§3.2).
- Author argues against using the MCS for model averaging with very short out-of-sample periods (§3.2).

## Limits and risks to validity
_My assessment:_ simulation only for one-day horizons and GARCH-family DGPs; no code; single author. Results concern consistent tail losses, not point forecasts.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Simulation study of tests |
| Baselines | 1 | True model and naive model in the set |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Several DGPs, one return process family |
| Statistical testing | 1 | Rejection frequencies over replications |
| Reproducibility | 0 | No code |
| **Total** | 3/8 → **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "the tests need long evaluation windows of several years" (§4)
