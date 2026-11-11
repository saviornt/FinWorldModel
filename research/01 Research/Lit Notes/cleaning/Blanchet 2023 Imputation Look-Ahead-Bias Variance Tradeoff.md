---
type: lit-note
title: "Bayesian Imputation with Optimal Look-Ahead-Bias and Variance Tradeoff"
authors: [Jose Blanchet, Fernando Hernandez, Viet Anh Nguyen, Markus Pelger, Xuhui Zhang]
year: 2023
venue: arXiv (stat.ME), v2
source_url: https://arxiv.org/abs/2202.00871
doi: 10.48550/arXiv.2202.00871
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.4, RQ3.6]
family: [cleaning]
evidence: Moderate
score: 7
tags: [lit-note, family/cleaning, imputation, leakage]
---
# Bayesian Imputation with Optimal Look-Ahead-Bias and Variance Tradeoff (Blanchet, 2023)

**Basis:** arXiv 2202.00871v2 (April 2023) read via alphaXiv PDF query on 2026-11-08.

**Takeaway:** Imputing a panel with the full data set (including the test period) plants a spurious signal that a downstream portfolio model exploits, so even a "properly out-of-sample" test on globally imputed data can be invalid; training-only imputation avoids the bias but is noisier, and a weighted consensus of the two is usually best.

## Problem
Imputation is usually run on the whole panel before a train/test split; how much look-ahead does that add, and how should it be traded off against variance?

## Data and period
Simulated factor-model returns (10 assets); empirical: 10 large-cap US stocks 2015–2017 and 10 Fama–French industry portfolios 2017–2019, daily (§8.2, p. 28).

## Method
Bayesian posteriors of the mean from data truncated at successive dates, fused by KL or Wasserstein consensus with a tolerance δ on look-ahead bias; downstream task: max-mean portfolio; regret = test minus later out-of-sample return (§8).

## Baselines and validation
Training-only imputation (δ = 0) and full-panel imputation (δ max); masking MCAR, MAR, blocks and missing-by-value.

## Results (with page or section references)
- Global imputation "is likely to create a spurious signal" through temporal correlation between training and test portions (p. 1); Giglio, Liao & Xiu (2021) is cited as a case with an implicit in-sample component (p. 2).
- In most cases a non-trivial δ minimises error; under MAR a small δ is optimal because bias grows faster than variance falls; for block or value-dependent missingness more future information pays (pp. 30–31).

## Limits and risks to validity
Small samples (10 assets, 400 days); Gaussian conjugate model for the mean only; effect sizes are shown in figures, not tabulated.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Fixed train/test/OOS split |
| Baselines | 1 | The two extreme imputations |
| Point-in-time and leakage controls | 2 | The paper's subject |
| Costs and realism | N/A | |
| Sample breadth | 0 | 10 assets, two years each |
| Statistical testing | 0 | None |
| Reproducibility | 2 | Code and data on GitHub |
| **Total** | 6/12 → 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the look-ahead-bias from the imputation can render the results invalid" (p. 1)
