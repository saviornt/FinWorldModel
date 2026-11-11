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
title: Heavy Tails and Predictive Ability Testing
authors:
- Jonas F. Frederiksen
- Muneya Matsui
- Rasmus S. Pedersen
year: 2026
venue: arXiv (stat.ME) 2605.16866
source_url: https://arxiv.org/abs/2605.16866
doi: ''
research_questions:
- RQ4.2
evidence: Moderate
score: 7
---
# Heavy Tails and Predictive Ability Testing (Frederiksen, Matsui & Pedersen, 2026)

**Basis:** Full text via alphaXiv (v2), read 2026-11-08: abstract, §1, §4.2 (SPA extension) and §7. Proofs not read.

**Takeaway:** When loss differentials have infinite variance, as heavy-tailed returns and volatility make plausible, the DM statistic has a non-Gaussian stable limit and a nominal 5% test can reject a true null up to 70% of the time; subsampling gives valid inference without estimating tail indices, and in an FX risk application it overturns a DM verdict that a GARCH model dominates simple rolling-window forecasts.

## Problem
DM and Hansen SPA rely on a finite-variance CLT, at odds with power-law tails (κ < 2) in returns and volatility (§1).

## Data and period
Theory and simulations; application to risk forecasts for emerging-market exchange rates (§1, §7).

## Method
New stable limit theorem for strongly mixing infinite-variance series; subsampling-based DM and a heavy-tail SPA statistic (§1, §4.2).

## Baselines and validation
Standard DM with normal critical values versus subsampling test (§1).

## Results (with page or section references)
- Nominal 5% DM can reject a true null as often as 70% of the time, irrespective of sample size, under plausible heavy-tailed DGPs (§1, §7).
- FX application: standard DM says a GARCH-based model dominates each of nine competitors; the heavy-tail-robust test cannot reject that simple rolling-window forecasts are as good (§1, §7).
- Multivariate extension covers SPA-type tests over many competitors (§4.2).

## Limits and risks to validity
_My assessment:_ one empirical application, not equity; code availability not stated in the part read. Subsampling needs a block-size choice.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Test methodology |
| Baselines | 1 | Standard DM as comparator |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Simulations plus one FX panel |
| Statistical testing | 2 | Valid inference under heavy tails is the subject |
| Reproducibility | 0 | Not stated |
| **Total** | 4/8 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a nominal 5% test may reject a true null as often as 70%" (abstract)
