---
type: lit-note
title: "Imputation for prediction: beware of diminishing returns"
authors: [Marine Le Morvan, Gaël Varoquaux]
year: 2024
venue: arXiv (cs.LG); later ICLR 2025
source_url: https://arxiv.org/abs/2407.19804
doi: 10.48550/arXiv.2407.19804
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Moderate
score: 8
tags: [lit-note, family/cleaning, imputation]
---
# Imputation for prediction: beware of diminishing returns (Le Morvan, 2024)

**Basis:** arXiv 2407.19804 read via the alphaXiv report on 2026-11-08 (section-level, no page numbers). The ICLR 2025 venue is noted from memory and was not checked.

**Takeaway:** Across 20 tabular datasets, better imputation buys little better prediction (gains in prediction R² are about a tenth of the gain in imputation R² or less), less still with expressive models such as XGBoost and with nonlinear targets; adding missingness indicators helps even when values are missing completely at random.

## Problem
Does more accurate imputation translate into more accurate downstream prediction?

## Data and period
20 regression datasets (not financial), capped at 50,000 rows; MCAR missingness induced; semi-synthetic linear outcomes for a control (Experimental design).

## Method
Mean, iterative Bayesian ridge, MissForest and conditional-expectation imputation, each with and without missingness indicators, feeding MLP, SAINT and XGBoost; 3-fold CV × 10 repeats; about 2.5 CPU-years.

## Baselines and validation
Mean imputation as the simple baseline; random (not time-ordered) cross-validation.

## Results (with page or section references)
- ΔR²(prediction) ≈ 0.1 × ΔR²(imputation) or less (Key findings).
- XGBoost depends least on imputation quality; nonlinear targets weaken the link further.
- Missingness indicators improve prediction even under MCAR and reduce dependence on imputation quality (The role of missingness indicators).

## Limits and risks to validity
Not financial and not time series; MCAR only, the most favourable case for imputation. Financial data are not MAR (see [[Bryzgalova 2025 Missing Financial Data]]), where indicators should matter more, not less, but that was not tested here.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Repeated random CV (not temporal) |
| Baselines | 1 | Mean imputation; several models |
| Point-in-time and leakage controls | N/A | Cross-sectional data |
| Costs and realism | N/A | |
| Sample breadth | 1 | 20 non-financial datasets, MCAR only |
| Statistical testing | 1 | Repeated runs; no correction |
| Reproducibility | 2 | Public datasets and code |
| **Total** | 6/10 → 8/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read via report only).
