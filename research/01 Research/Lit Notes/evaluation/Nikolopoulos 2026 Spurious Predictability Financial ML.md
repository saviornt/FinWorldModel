---
type: lit-note
title: Spurious Predictability in Financial Machine Learning
authors:
- Sotirios D. Nikolopoulos
year: 2026
venue: arXiv (q-fin.ST) 2604.15531
source_url: https://arxiv.org/abs/2604.15531
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ4.1
- RQ4.2
- RQ4.7
family:
- evaluation
evidence: Moderate
score: 9
tags:
- lit-note
- family/evaluation
- backtest-overfitting
---
# Spurious Predictability in Financial Machine Learning (Nikolopoulos, 2026)

**Basis:** Full text via alphaXiv (v1), pp. 1–10, 20–21, 26–27, 32, read 2026-11-08.

**Takeaway:** Run the whole pipeline on synthetic nulls first (white noise, regime-switching volatility, bid–ask bounce, factor-only, GARCH): a workflow that earns significant walk-forward results there is falsified; for survivors, measure the gap between the best in-sample t-statistic and its walk-forward value, which grows like √(2 ln K_eff) under the null.

## Problem
How to tell genuine predictability from leakage, selection bias and microstructure artefacts in an ML trading workflow.

## Data and period
Monte Carlo on five synthetic environments (Appendix B); empirical case studies on returns and volatility forecasting (§6).

## Method
Two stages: a falsification audit on induced nulls, then a strictly disjoint in-sample/walk-forward evaluation with HAC t-statistics; inflation measured by ΔZ = Z*IS − Z*WF and an effective number of trials K_eff; blind-parameter protocol to stop overfitting to the audit (§§3–4).

## Baselines and validation
HAR benchmark in the volatility case; random vs chronological CV compared (§6).

## Results (with page or section references)
- Under the global null the best of K in-sample statistics grows like √(2 ln 2K); about K = 100 trials already gives apparently significant results; walk-forward statistics of the selected model stay null-like (§2.2, Lemma 1).
- HAC t-tests over-reject in short walk-forward windows (e.g. 252 days), so a test-based admission gate is conservative only in the accepting direction (§3.1).
- Detection power collapses for weak, rare signals: pass rate 4.8% at φ = 0.05, θ = 3σ, about the 5% size (Table 9, p. 20).
- Volatility case: random CV and walk-forward gave almost the same R² (inflation ratio 1.006), and HAR stayed slightly better than the high-dimensional Lasso: validation inflation must be measured case by case, not assumed (Table 14, p. 26).

## Limits and risks to validity
_My assessment:_ single author; thresholds in the appendix are illustrative and must be re-simulated per pipeline; the audit has no formal inference yet (the author says so, p. 27). Code archiving recommended but not stated as done.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Strictly disjoint walk-forward |
| Baselines | 1 | HAR; null environments |
| Point-in-time and leakage controls | 2 | Leakage and timing placebos built in |
| Costs and realism | 1 | Bid–ask placebo; no full cost model |
| Sample breadth | 1 | Several synthetic regimes, limited empirical cases |
| Statistical testing | 2 | HAC tests plus multiplicity (K_eff) adjustment |
| Reproducibility | 0 | Code not linked |
| **Total** | 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Workflows generating significant walk-forward evidence in these environments are falsified." (abstract)
