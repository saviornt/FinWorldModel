---
type: lit-note
title: "Limits To (Machine) Learning"
authors: [Zhimin Chen, Bryan Kelly, Semyon Malamud]
year: 2025
venue: arXiv (stat.ML) working paper
source_url: https://arxiv.org/abs/2512.12735
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.8, RQ1.1]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation]
---
# Limits To (Machine) Learning (Chen, 2025)

**Basis:** arXiv v1 (14 Dec 2025) read through alphaXiv page excerpts (pp. 1–3, 8, 12, 14, 17, 23, 25–27, 29–30 and figures pp. 32–37). The proofs in the appendix were not read.

**Takeaway:** For any linear (incl. kernel / random-feature) estimator, finite samples impose a computable lower bound on estimation error (the Limits-to-Learning Gap, LLG), so a weak or negative out-of-sample R² does not show that a target is unpredictable; on Welch–Goyal data (train 1933–1989, test 1990–2024) the implied population R² for monthly US market excess returns is at least about 20% even though realised R²_OOS is negative.

## Problem
When ML forecasts fail out of sample, is the target unpredictable, or is the signal there but too hard to learn from the sample available?

## Data and period
Welch and Goyal (2008) monthly series, 1930-01 to 2020-11 (p. 23), with figures showing train 1933-01 to 1989-12 and test 1990-01 to 2024-12 (pp. 32–37): CRSP value-weighted excess returns, valuation ratios, stock variance, yields, spreads, inflation. Semi-synthetic simulations on the same predictors (p. 25).

## Method
Decompose OOS MSE into estimation error plus irreducible noise (p. 2). Derive a lower bound on estimation error for linear estimators, E[(f − f̂)²] ≥ σ²ε·L̂, where L̂ depends only on the signals, not on the target (pp. 3, 12). This gives R²* ≥ (R²_OOS + L̂)/(1 + L̂), with a CLT-based one-sided confidence band (pp. 3, 14). Applied with up to 20,000 random features (ReLU, tanh) and ridge; then ridge and a "recursive ridge" model test whether the implied predictability can be recovered (pp. 26–29).

## Baselines and validation
Single split at January 1990 (p. 25). Semi-synthetic simulations with known R²* (0, 0.25, 0.5, 0.75) and pure-noise / GARCH(1,1) benchmarks check that the confidence bound stays below the truth (pp. 25–26). No transaction-cost or trading test.

## Results (with page or section references)
- The confidence lower bound "is always below R²*" in simulations, while R²_OOS decays quickly as model complexity rises (p. 26).
- Market excess returns: ReLU-based LLG implies a lower bound of about 20% for population R², "around 10–20 times higher" than typical realised monthly R²_OOS (p. 27).
- dp, ep, de lower bounds about 50% (up to 70% for de); svar and bm 20–25%; T-bills and long-term rate at least 10%; default spread and long-term yield at least 25% (pp. 26–27).
- In every target except de, the high bound coexists with negative realised R²_OOS (p. 27).
- Recursive ridge recovers part of it for some targets (dfy, ep ≈ 15% R²_OOS vs ~25% bound; tbl ≈ 10% vs 10%; de ≈ 42% vs 67%) but falls far short for retx, dp, bm, svar, lty (p. 29). Bound correlates 80% with best nonlinear R²_OOS (p. 29).
- Authors note this also explains sharply diminishing returns to scaling when the gap closes slowly (p. 30).

## Limits and risks to validity
_My assessment:_ the bound is proven for linear estimators; extension to deep networks is argued (p. 14) but I did not read the proof. The headline "≥20% for market returns" is a bound on what could exist, not a forecast anyone achieved; it rests on stationarity of f² (p. 12) and a single structural split. For RQ1.8 the relevance is indirect: with very few crisis observations, the estimation-error floor is large, so failing to forecast crises out of sample does not prove they are unforecastable — but it also means no realistic sample will reveal the mapping. The paper does not study rare events.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One train/test split (1990) |
| Baselines | 1 | Ridge, recursive ridge; R²_OOS vs historical mean implied |
| Point-in-time and leakage controls | 1 | Lagged public predictors; AR(1) residual targets; not discussed further |
| Costs and realism | N/A | Predictability bound, no trading claim |
| Sample breadth | 2 | 14 series, 1933–2024, multiple stress periods |
| Statistical testing | 1 | CLT confidence band; no multiple-testing correction |
| Reproducibility | 2 | Public data; code at github.com/czm319319/CKM_LLG (p. 1) |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the apparent weakness of predictability in financial data is often a statistical illusion" (p. 30)
