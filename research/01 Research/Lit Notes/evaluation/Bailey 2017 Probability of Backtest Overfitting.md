---
type: lit-note
title: The Probability of Backtest Overfitting
authors:
- David H. Bailey
- Jonathan Borwein
- Marcos López de Prado
- Qiji Jim Zhu
year: 2017
venue: Journal of Computational Finance 20(4), 39–69
source_url: https://escholarship.org/uc/item/4w1110bb
doi: 10.21314/jcf.2016.322
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
score: 7
tags:
- lit-note
- family/evaluation
- backtest-overfitting
---
# The Probability of Backtest Overfitting (Bailey, Borwein, López de Prado & Zhu, 2017)

**Basis:** eScholarship record and full PDF read through a summarising page fetch on 2026-11-08 (pages cited from that PDF); SSRN abstract page 2326253 also opened.

**Takeaway:** PBO is the probability that the configuration that looks best in-sample ranks below the median out of sample; combinatorially symmetric cross-validation (CSCV) estimates it from the full matrix of trial returns, and hold-out is unreliable for backtests because it ignores how many trials were run.

## Problem
How likely is it that a strategy chosen from many backtested variants is overfit?

## Data and period
Simulated and example strategy return matrices (T × N trials); Monte Carlo checks referenced to a companion SSRN study (p. 8).

## Method
Split the T × N matrix into S blocks (S = 16 suggested: 12,870 half/half combinations), take each half as in-sample, find the best in-sample trial, record the logit of its out-of-sample relative rank; PBO = share of logits below zero (pp. 10–13). Also performance degradation (IS vs OOS Sharpe) and probability of loss (pp. 14–16).

## Baselines and validation
Hold-out discussed as the standard alternative (pp. 6–8).

## Results (with page or section references)
- Hold-out problems: the out-of-sample period may already be known or reused, small samples, dependence on which section is held out, and no account of the number of trials (pp. 7–8).
- Example: all in-sample Sharpe ratios positive, about 78% of out-of-sample Sharpe ratios negative (p. 15).
- CSCV on one dataset approximates PBO computed over many independent samples with small error (Monte Carlo, p. 8; figures not read).
- Limitations stated: all trials must be reported; a high PBO can occur among many skilful strategies; structural breaks outside the sample are not captured; large S can hide autocorrelation; do not use CSCV as an optimisation target (pp. 23–25).

## Limits and risks to validity
_My assessment:_ CSCV swaps halves of the sample, so later blocks train models tested on earlier ones; the authors say it respects time dependence (p. 21), but this is not causal in the walk-forward sense (see Li 2026). Read through a summary, so the S = 16 combination count (12,870) is computed here, the summary gave 12,780. Assumes Sharpe-type statistics are IID normal on subsamples (p. 11).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | CSCV half splits |
| Baselines | N/A | Method paper |
| Point-in-time and leakage controls | 1 | Multiplicity, not time leakage |
| Costs and realism | N/A |  |
| Sample breadth | 0 | Illustrative examples |
| Statistical testing | 2 | Corrects for the number of trials |
| Reproducibility | 0 | No code by the authors (third-party R package exists) |
| **Total** | 4/8 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- hold-out "is clearly inadequate for small samples" (p. 7)
