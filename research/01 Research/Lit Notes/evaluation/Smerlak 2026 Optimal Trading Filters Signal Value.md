---
type: lit-note
title: "Optimal Trading Filters and the Value of Predictive Signals"
authors: [Matteo Smerlak]
year: 2026
venue: arXiv (q-fin.MF) 2610.24558
source_url: https://arxiv.org/abs/2610.24558
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.6]
family: [evaluation]
evidence: Weak
score: 2
tags: [lit-note, family/evaluation, economic-value, transaction-costs, theory]
---
# Optimal Trading Filters and the Value of Predictive Signals (Smerlak, 2026)

**Basis:** Full text (pp. 1–2, 4, 7–11) via the alphaXiv PDF reader, read 2026-11-09. Theory paper; no empirical test.

**Takeaway:** With trading costs and transient price impact, signals with the same predictive strength (same frictionless value) can have very different net value: what counts is how well the signal forecasts the part of future drift that is cheap to trade, so a forecast's speed and smoothness, not just its accuracy, set its economic value.

## Problem
How to turn return forecasts into positions under costs and decaying price impact, and what a forecast is worth after costs (p. 1).

## Data and period
None; analytical model with Gaussian (OU and Matérn) predictors and exponential or power-law impact kernels (pp. 2, 4).

## Method
Stationary quadratic trading problem solved by Wiener–Hopf factorization: optimal policy = conditional forecast of a friction-adjusted signal followed by a causal linear filter; recovers the Gârleanu–Pedersen aim portfolio (pp. 1, 4).

## Baselines and validation
Not applicable (theory).

## Results (with page or section references)
- At fixed predictor variance, all signals have equal frictionless Markowitz value; with costs, net value is half the mean square of a friction-weighted conditional forecast (p. 1, eq. 30, p. 7).
- A perfectly predictable oscillation at a costly frequency can have arbitrarily small value (p. 7).
- Under power-law impact with exposure bleeding, an intermediate OU decay rate maximises value; slow and fast signals reach 0.30 and 0.17 of the bound vs 0.57 at the preferred rate (p. 9). With ordinary stock holdings and inventory risk, slower signals are favoured (pp. 7, 10).
- "Empirical use requires estimating predictive strength jointly with signal dynamics and trading costs" (p. 1).

## Limits and risks to validity
_My assessment:_ stylised linear-quadratic model, Gaussian signals, no data. Cited as theory for why forecast accuracy metrics cannot rank signals by economic value, never as empirical proof.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | No data |
| Baselines | N/A | Theory |
| Point-in-time and leakage controls | N/A | Theory |
| Costs and realism | 1 | Explicit cost and impact model, not calibrated |
| Sample breadth | 0 | None |
| Statistical testing | N/A | Theory |
| Reproducibility | 0 | No code |
| **Total** | 1/8 → **2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "The value of a forecast depends on its accuracy, but also on its actionability." (p. 1)
