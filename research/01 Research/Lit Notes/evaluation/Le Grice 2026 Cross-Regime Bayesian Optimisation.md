---
type: lit-note
title: "Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation"
authors: [Josh Le Grice]
year: 2026
venue: arXiv (cs.LG) 2608.27076 (MSc work, University of Exeter)
source_url: https://arxiv.org/abs/2608.27076
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.4, RQ4.6]
family: [evaluation]
evidence: Moderate
score: 6
tags: [lit-note, family/evaluation, training, hyperparameter-search, ensembling]
---
# Cross-Regime Bayesian Optimisation for Equity Signals (Le Grice, 2026)

**Basis:** Full text (pp. 1–2, 5, 7–9, 11, 16, 19) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** Tuning hyperparameters with a fixed composite objective across three distinct validation years (with penalties for any losing year) gave no tabular deep model that beat XGBoost; a rank-averaged XGBoost + TabNet ensemble reported Sharpe 2.44 in a single held-out year (2025), which is a single-path, after-selection result.

## Problem
Whether hyperparameters chosen to perform across several market regimes generalise, and whether tabular deep learning beats gradient-boosted trees for daily cross-sectional signals (§1).

## Data and period
About 300 S&P 500 constituents, daily, 2015–2025; Bloomberg prices, fundamentals and news sentiment, Google Trends, FRED macro; target: next-day cross-sectional return decile (long/hold/short) (§3.1, Fig. 2).

## Method
Five models (logistic regression, XGBoost, MLP, TabNet, FT-Transformer). Optuna TPE, 30 trials per model; expanding-window folds 2022, 2023, 2024 with a one-day purge; objective = weighted return, Sharpe and drawdown across folds minus quadratic penalties for any negative fold; weights fixed before experiments. Ensemble partner chosen by the same composite score after discarding combinations with a losing validation year (§3.2.1–3.3.2).

## Baselines and validation
Logistic regression, XGBoost, MLP, S&P 500 buy-and-hold; final retrain on 2015–2024, test on 2025 only; RobustScaler fitted on training folds; 2.2 bp per trade, market-on-close execution (§3.2.2, §3.4).

## Results (with page or section references)
- 2025 test: XGBoost return 33.61%, Sharpe 1.37; TabNet Sharpe 0.44; FT-Transformer 0.06; Hybrid (XGBoost + TabNet rank average) 51.26%, Sharpe 2.44, max drawdown −7.76% (Table 2, p. 11).
- No individual tabular deep model beats XGBoost; FT-Transformer is best in 2022 validation but near zero after (Table 2; §5, p. 16).
- Ensemble partner TabNet chosen for low error correlation with XGBoost (pairwise CAPM R² 0.028 vs 0.149 for MLP) (p. 16).
- With all inputs replaced by noise, the Hybrid Sharpe falls to −1.44 (p. 16).
- Author notes: one OOS year; no single-regime tuning baseline under the same budget; short-borrow costs not modelled (§5.4, p. 19).

## Limits and risks to validity
_My assessment:_ the Sharpe 2.44 is an outlier from one year after selecting among models and ensembles; no deflation for the 150+ trials and ensemble search; no comparison against ordinary single-fold tuning, so the cross-regime objective's benefit is not isolated. Useful as a design pattern (multi-period objective, worst-fold penalties, fixed objective weights, noise-input null check), not as evidence of size.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Expanding folds for tuning; one held-out year |
| Baselines | 1 | XGBoost, logit, buy-and-hold; no naive ranking baseline across years |
| Point-in-time and leakage controls | 1 | Purge, train-only scaler, pre-close features; not checked |
| Costs and realism | 1 | Flat 2.2 bp; no borrow costs |
| Sample breadth | 1 | ~300 large caps, one market |
| Statistical testing | 1 | CAPM alpha, PSR, non-parametric tests; no multiple-testing correction |
| Reproducibility | 0 | No code or data release stated |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "All weights were fixed before experimentation began" (p. 8)
