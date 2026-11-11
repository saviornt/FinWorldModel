---
type: lit-note
title: "Deep Hedging Under Non-Convexity: Limitations and a Case for AlphaZero"
authors: [Matteo Maggiolo, Giuseppe Nuti, Miroslav Štrupl, Oleg Szehr]
year: 2025
venue: arXiv (stat.ML)
source_url: https://arxiv.org/abs/2510.01874
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9]
family: [rl-planning]
evidence: Weak
score: 4
tags: [lit-note, family/rl-planning, planning]
---
# Deep Hedging Under Non-Convexity: A Case for AlphaZero (Maggiolo, 2025)

**Basis:** v2 PDF read through alphaXiv excerpts (pp. 1–6, 11–12, appendices pp. 25–32). Theory sections (pp. 7–10) not read in full.

**Takeaway:** In simulated hedging problems with non-convex costs or constraints, gradient-trained deep hedging finds the optimal action in only 0–26% of runs while AlphaZero-style tree search finds it in 85–100% and needs fewer samples; the only search-based planning evidence found for finance, but entirely on toy simulated markets.

## Problem
When does deep hedging (gradient descent through a policy stack) fail, and can Monte Carlo tree search do better for replication portfolios (pp. 1–3)?

## Data and period
Simulated markets only: bi-modal reward toy tasks, trinomial markets with non-convex costs (DP-solvable), trading constraints; no historical data, following the original deep hedging study (p. 3).

## Method
Theory linking deep hedging to convex optimisation; AlphaZero (UCT + policy/value networks) and MuZero (learned dynamics) on discretised states and actions; 100 independent training runs per method; deep hedging tuned with Optuna, AlphaZero untuned (pp. 6, 11, App. D).

## Baselines and validation
Deep hedging; exact dynamic programming where feasible; evaluation on separate simulated paths.

## Results (with page or section references)
- Deterministic sequence task: deep hedging optimal in ~10% of runs, AlphaZero ~85% (p. 11).
- State-dependent composition: deep hedging 0%, AlphaZero 100% (pp. 11–12).
- Trinomial market with non-convex costs: deep hedging picks the right mode in ~26% of runs (its initialisation), AlphaZero 100% (p. 12).
- With concave utility and convex costs the problem is convex, so deep hedging works there (p. 2).
- MuZero reaches deep hedging's test loss with fewer training samples (p. 3; Sec. 4.3).

## Limits and risks to validity
No historical data; no comparison with RL methods other than deep hedging (p. 3); small discretised spaces. _My assessment:_ supports search/planning where the objective is non-convex and a model of the dynamics exists; says nothing about forecasting or alpha.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Separate simulated evaluation paths |
| Baselines | 1 | Deep hedging and exact DP |
| Point-in-time and leakage controls | N/A | Simulation |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 0 | Toy simulated markets |
| Statistical testing | 1 | Distributions over 100 runs; no formal tests |
| Reproducibility | 0 | No code link seen |
| **Total** | **3/10 → 4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "its effectiveness is contingent on convexity assumptions" (p. 1)
