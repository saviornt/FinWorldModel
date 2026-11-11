---
type: lit-note
title: "Re(Visiting) Time Series Foundation Models in Finance"
authors: [Eghbal Rahimikia, Hao Ni, Weiguan Wang]
year: 2025
venue: arXiv (q-fin.CP); SSRN 5770562
source_url: https://arxiv.org/abs/2511.18578
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.1]
family: [price-time-series]
evidence: Strong
score: 12
tags: [lit-note, family/price-time-series]
---
# Re(Visiting) Time Series Foundation Models in Finance (Rahimikia, 2025)

**Basis:** full text via alphaXiv (sections 1, 3.3, 5.1, 5.2.4, 6; Tables 7, 12, B.6, B.7, B.17).

**Takeaway:** Off-the-shelf TSFMs lose to tree ensembles on daily excess returns; finance-native pretraining narrows but does not close the gap, and every daily long–short strategy (including CatBoost) turns negative after 20 bps costs.

## Problem
First large-scale test of TSFMs for daily excess-return forecasting: zero-shot, fine-tuned and pretrained-from-scratch regimes vs strong benchmarks (§1).

## Data and period
~2 billion daily excess-return observations, 34 years, 94 countries; out-of-sample 2001–2023; tests in the US and seven other markets (§1, §5).

## Method
Chronos and TimesFM families (plus ten more TSFMs in the appendix) in three regimes; pretraining from scratch done year by year on data available up to that year (§5, p. 3–4).

## Baselines and validation
OLS, Lasso, Ridge, Elastic Net, PCR, XGBoost, CatBoost, LightGBM, two NNs; expanding window refit each year from 1990 (walk-forward), window sizes 5/21/252/512 (§5, p. 24). R²_OOS is measured against a zero forecast (§3.3.1). Modified DM tests (fn. 27). Decile long–short, equal-weight, daily rebalance (§3.3.2).

## Results (with page or section references)
- Off-the-shelf TSFMs perform poorly; fine-tuning gives limited gains (Abstract; p. 3).
- Benchmark R²_OOS for 512-day window is −0.03%; best pretrained TSFM (Chronos small) is −0.59% (p. 40).
- CatBoost is the best benchmark and beats all pretrained TSFMs on modified DM tests (fn. 27, p. 40).
- At 512 days: CatBoost long–short Sharpe 6.46 vs pretrained Chronos small 5.42 at zero cost (p. 43).
- With JKP factors or synthetic augmentation, TSFMs improve; Chronos small directional accuracy 51.74% vs CatBoost 51.16% (p. 4).
- TSFMs had higher Sharpe than the benchmark in 2008 and 2020 stress periods (p. 61).
- Net of 20 bps, every long–short Sharpe in Table 12 and Table B.17 is negative (e.g. CatBoost −3.13 at 512 days) (p. 64, p. 116).

## Limits and risks to validity
_My assessment:_ the gross Sharpe ratios (5–7) are a frictionless artefact of daily decile rebalancing; the economic result after costs is negative for all models. Hyperparameters were tuned only in 2000 (fn. 15). Univariate returns only. Multiple-testing correction across the many model/window pairs not seen. Data proprietary; models released on Hugging Face.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Yearly expanding-window refits, 2001–2023 |
| Baselines | 2 | Zero forecast plus GBTs and linear models |
| Point-in-time and leakage controls | 2 | Year-by-year pretraining to avoid look-ahead; flags it for off-the-shelf TSFMs |
| Costs and realism | 2 | 0/20/40 bps and size-dependent costs |
| Sample breadth | 2 | 94 countries, 34 years, includes 2008 and 2020 |
| Statistical testing | 1 | Modified DM; no multiple-testing correction seen |
| Reproducibility | 1 | Models released; data not |
| **Total** | **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "Off-the-shelf TSFMs perform poorly" (Abstract, p. 1)
