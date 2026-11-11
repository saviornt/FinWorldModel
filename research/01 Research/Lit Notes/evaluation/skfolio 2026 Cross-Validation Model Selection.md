---
type: lit-note
title: 'skfolio model selection: WalkForward and MultipleRandomizedCV example'
authors:
- skfolio developers
year: 2026
venue: skfolio documentation
source_url: https://skfolio.org/auto_examples/model_selection/plot_1_multiple_randomized_cv.html
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Primary documentation
tags:
- lit-note
- family/evaluation
- cross-validation
- guide-seed
---
# skfolio cross-validation example (2026)

**Basis:** Documentation page read through a summarising page fetch on 2026-11-08. The guide's seed named a CPCV example; the page opened covers WalkForward and MultipleRandomizedCV only (CombinatorialPurgedCV not described there).

**Takeaway:** Resampling many walk-forward paths over random asset subsets and windows turns one backtest into a distribution of out-of-sample Sharpe ratios (benchmark 0.36 ± 0.38, tuned model 0.50 ± 0.32 on FTSE 100 2000–2023), showing how much a single path can hide.

## Problem
Show the spread of out-of-sample performance that a single walk-forward path hides.

## Data and period
FTSE 100, 64 assets, 2000–2023.

## Method
WalkForward(test_size = 20 days, train_size = 252); MultipleRandomizedCV with 200 subsamples of 50 assets and 3-year windows, walk-forward inside each.

## Baselines and validation
Top-10-by-Sharpe HERC benchmark vs a randomised-search tuned model.

## Results (with page or section references)
- Annualised OOS Sharpe: benchmark mean 0.36 (s.d. 0.38), tuned 0.50 (s.d. 0.32).
- The standard deviation across paths is as large as the mean.

## Limits and risks to validity
Library documentation; example chosen by the developers; no significance test of the difference.

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
