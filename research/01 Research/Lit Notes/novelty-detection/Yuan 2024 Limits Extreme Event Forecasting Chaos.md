---
type: lit-note
title: "Limits to extreme event forecasting in chaotic systems"
authors: [Yuan Yuan, Adrián Lozano-Durán]
year: 2024
venue: arXiv (physics.data-an)
source_url: https://arxiv.org/abs/2401.16512
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.8, RQ4.3]
family: [novelty-detection]
evidence: Weak
score: 0
tags: [lit-note, family/novelty-detection]
---
# Limits to extreme event forecasting in chaotic systems (Yuan, 2024)

**Basis:** arXiv v3 (13 Jun 2024) read through alphaXiv page excerpts (pp. 1–3, 5–6, 8–18, 24, 26–27). Not a finance paper; kept because the bound is model-independent and transfers (guide step 4).

**Takeaway:** There is a model-independent minimum probability of error for forecasting a binary extreme event from a given set of observables, with information-theoretic upper and lower bounds; error decomposes into initial-condition uncertainty, unobserved variables and model error, and in the test systems missing variables dominate as the horizon grows, while rarer (higher-threshold) events are harder to predict.

## Problem
What is the minimum possible error in predicting extreme events in chaotic systems, regardless of the model used (p. 1)?

## Data and period
Two simulated systems: the Rössler system (10,000 time units; event = θ₃ > mean + 3σ, also + 6σ) (pp. 10, 12, 26) and 2-D Kolmogorov turbulent flow at Re = 100 (event = dissipation > mean + 1.5σ, also + 3σ) (pp. 14–15).

## Method
Minimum cost-sensitive probability of error over all models, Eq. (7) (p. 5); lower/upper bounds via cost-sensitive Fano and Hellman inequalities with Rényi entropy (p. 6); "information can't hurt" link to Takens embedding: adding lags can lower but never raise the minimum error (p. 8). Error split P_I (initial conditions) + P_O (unobserved variables) + P_M (suboptimal model) (pp. 8–9). Decision trees used as an example model (p. 11).

## Baselines and validation
Not a model comparison. The decision tree is compared with the theoretical minimum to show whether it is near-optimal (pp. 11–12).

## Results (with page or section references)
- Minimum normalised error rises towards 1 with forecast horizon in all cases (p. 11).
- With one observable, a decision tree operates near the theoretical minimum; with lagged inputs it is suboptimal for short horizons (δt < 0.4), so better models are possible (p. 12).
- As horizon grows, error from unobserved variables "rapidly becomes the predominant source of error"; initial-condition error is minor (p. 12).
- In Kolmogorov flow the minimum error is non-zero even at zero lead time (the event variable is not observed) and is lowest at a lag matching the physical energy-transfer time (pp. 15–16).
- Higher thresholds make prediction harder "due to the higher scarcity of events" (p. 26).

## Limits and risks to validity
_My assessment:_ the bound requires knowing the joint distribution of observables and the event, which for markets must itself be estimated from very few crises, so the bound is a concept, not a number one can compute for crashes. Simulated stationary systems; markets are non-stationary and reflexive. Useful as a framework: improvements must come from new observables (e.g. text, order flow) rather than better models once a model is near the bound.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Theoretical bound |
| Baselines | N/A | Not a model comparison |
| Point-in-time and leakage controls | N/A | Simulated systems |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 0 | Two simulated systems, no financial data |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Data on request (p. 18) |
| **Total** | **0/6 → 0/14** | Weak as empirical evidence; the bound itself is a mathematical result |

## Quotes worth keeping (each under 15 words, with page)
- "missing variables have a greater impact on the accuracy of the forecast" (p. 12)
