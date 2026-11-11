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
- metrics
title: 'Elicitability and backtesting: Perspectives for banking regulation'
authors:
- Natalia Nolde
- Johanna F. Ziegel
year: 2017
venue: Annals of Applied Statistics 11(4); arXiv 1608.05498
source_url: https://arxiv.org/abs/1608.05498
doi: 10.1214/17-aoas1041
research_questions:
- RQ4.3
evidence: Moderate
score: 8
---
# Elicitability and backtesting: Perspectives for banking regulation (Nolde & Ziegel, 2017)

**Basis:** arXiv v2 via the alphaXiv PDF reader, read 2026-11-08: pp. 1–3, 14, 18, 25, 28, 31–32, 46. Not every simulation table read.

**Takeaway:** Traditional backtests (is this VaR/ES calibrated?) cannot rank forecasting methods and many misspecified models pass them; comparative backtests with strictly consistent scores (tick loss for VaR, Fissler–Ziegel scores for joint VaR–ES) rank methods, and a two-stage scheme (calibration test, then comparative traffic-light test against a standard model) is recommended.

## Problem
How to backtest VaR, expectiles and ES so that accuracy, not just calibration, is rewarded (pp. 1–2).

## Data and period
Simulation from AR(1)-GARCH(1,1) with skewed-t innovations; NASDAQ Composite negated log-returns 8 Feb 1971 – 18 May 2016, 500-day moving window, 10,920 out-of-sample days (pp. 18, 25).

## Method
Conditional calibration tests as a unifying framework for traditional backtests; comparative backtests with DM-type tests on consistent scoring functions and a three-zone (red/yellow/green) traffic light (pp. 2, 14).

## Baselines and validation
Six methods: normal/t/skewed-t likelihood × fully parametric, filtered historical simulation, EVT (pp. 18, 25).

## Results (with page or section references)
- ES is not elicitable alone but is jointly elicitable with VaR, so comparative backtests of ES must score the (VaR, ES) pair (p. 2).
- Many methods based on misspecified models pass traditional backtests, giving an incentive to minimise capital subject to passing (p. 28).
- 0-homogeneous scores need weaker moment conditions and suit heavy-tailed data; Patton and Sheppard found b = 0 has best DM power for volatility (p. 14, p. 31).
- NASDAQ: fully parametric methods fall in the red zone against flexible alternatives for VaR₀.₉₉ and (VaR, ES)₀.₉₇₅ (pp. 25, 28).
- With 250 verifying days the optimal forecaster beats others in only about 70% (VaR) or 70–85% (VaR–ES) of samples; a calm evaluation window can rank optimal forecasts lowest (p. 46).
- Recommendation: stage I calibration test, stage II comparative backtest against a flexible standard model such as GARCH-filtered historical simulation with skewed-t (p. 31).

## Limits and risks to validity
_My assessment:_ one index for the data analysis; no code. The 250-day result matches [[Coelho 2026 Tail Forecast Comparison Exceedances]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling 500-day estimation, one long evaluation run |
| Baselines | 2 | Fully parametric, FHS and EVT methods compared |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | One index over 45 years incl. crises, plus simulations |
| Statistical testing | 2 | Calibration and comparative tests with traffic lights |
| Reproducibility | 0 | No code |
| **Total** | 6/10 → **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "many methods based on misspecified models may pass traditional backtests" (p. 28)
