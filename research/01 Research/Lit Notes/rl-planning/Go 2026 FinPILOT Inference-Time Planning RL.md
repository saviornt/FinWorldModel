---
type: lit-note
title: "Plan Before You Trade: Inference-Time Optimization for RL Trading Agents"
authors: [Eun Go, Rohan Deb, Arindam Banerjee]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2605.12653
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9]
family: [rl-planning]
evidence: Moderate
score: 7
tags: [lit-note, family/rl-planning, planning]
---
# FinPILOT: Inference-Time Planning for RL Trading Agents (Go, 2026)

**Basis:** v2 PDF read through alphaXiv excerpts (pp. 1–2, 4, 6–8, 10, 13, 15–17).

**Takeaway:** Five standard pre-trained RL portfolio agents (PPO, SAC, A2C, TD3, DDPG) on 28 Dow stocks did *worse* than buy-and-hold in 2023–2025 (Sharpe 0.85–1.13 vs 1.18), but adding MPC-style planning at decision time — adapting the actor against forecast price paths from an XGBoost model with out-of-sample R² of only 0.016 — raised Sharpe to 1.22–1.55 and improved 27 of 30 policy–market–year settings.

## Problem
Can a separately trained price forecaster be plugged into a frozen RL policy at inference time, in the spirit of model predictive control (pp. 1–2)?

## Data and period
TradeMaster environment; 28 DJ30 constituents and 22 USD FX pairs; rolling windows: 8 years train, 1 validation, test years 2023, 2024, 2025; 10 bps costs (pp. 6, 16).

## Method
Under the price-taker assumption, imagined rollouts = forecaster path (H = 50 days, 512 perturbed particles from validation error covariance) + exact cost-aware portfolio accounting; two gradient steps on the actor per decision with a downside-risk penalty; execute one step, carry parameters forward (pp. 2, 4, 16). Only the risk weight is tuned per setting on validation.

## Baselines and validation
Frozen base policy; buy-and-hold and daily 1/N; Boyd single- and multi-period convex optimisers fed the same forecasts; 5 seeds per window (pp. 7–8).

## Results (with page or section references)
- DJ30 three-year mean Sharpe: buy-and-hold 1.18, 1/N 1.13; base RL 0.85–1.13; FinPILOT 1.22–1.55; drawdowns rose (Tables 1, 3, pp. 7–8).
- FX: buy-and-hold Sharpe 0.17; base 0.09–0.16 (DDPG −0.11); FinPILOT 0.19–0.53 (Tables 1, 3).
- Return improved in 28/30 and Sharpe in 27/30 settings (Fig. 3, p. 8).
- Convex optimisers with the same forecasts did worse than passive (DJ30 Sharpe 0.52 and 0.37) (Table 3).
- Gains grow with controlled forecast skill (diagnostic only, uses future prices) (Fig. 4, p. 10).

## Limits and risks to validity
Authors: price-taker assumption, long-only, three test years, step size matters (larger updates hurt in DJ30 2024) (p. 10). _My assessment:_ current DJ30 constituents imply survivorship; no significance tests; the convex-optimiser baselines' poor showing may reflect their tuning. Shows the pattern "forecast + planning beats a static RL policy", and also that the static RL policies on their own failed to beat passive.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling train/validation/test over three years |
| Baselines | 2 | Buy-and-hold, 1/N, convex MPC with the same forecasts |
| Point-in-time and leakage controls | 1 | Forecaster fit before test; survivorship not addressed |
| Costs and realism | 1 | Flat 10 bps |
| Sample breadth | 1 | Two markets, three years, no major stress |
| Statistical testing | 0 | Seed spreads only |
| Reproducibility | 0 | No code link seen |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "trained and deployed as static policies" (p. 1)
