---
type: lit-note
title: "Analytical Uncertainty-Based Loss Weighting in Multi-Task Learning"
authors: [Lukas Kirchdorfer, Cathrin Elich, Simon Kutsche, Heiner Stuckenschmidt, Lukas Schott, Jan M. Köhler]
year: 2024
venue: arXiv
source_url: https://arxiv.org/abs/2408.07985
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [evaluation]
evidence: Moderate
score: 7
tags: [lit-note, family/evaluation, pretraining-objective, loss-balancing]
---
# Kirchdorfer 2024 Uncertainty-Based Loss Weighting MTL (Kirchdorfer et al., 2024)

**Takeaway:** In a benchmark with per-method learning-rate tuning, a brute-force grid of fixed loss weights (scalarization) and a simple analytic inverse-loss weighting (UW-SO) did best; learned uncertainty weighting overfit, equal weighting was often far worse, differences between methods shrank in larger networks, and tuning the learning rate per method mattered more than the weighting scheme's details.

## Problem
How to weight several task losses in one network, and why published rankings of weighting methods disagree.

## Data and period
Computer-vision MTL benchmarks: Cityscapes, NYUv2 (segmentation, depth, normals), CelebA (40 tasks). Not financial (§4).

## Method
UW-SO: softmax with temperature over inverse task losses (analytic optimum of uncertainty weighting). Compared with equal weighting (EW), random loss weighting, DWA, geometric loss, IMTL-L, uncertainty weighting (UW) and scalarization; learning rate and weight decay tuned per method by line search (§3–4).

## Baselines and validation
Single-task models and all methods above; 5 runs (3 for a fixed protocol); test-set results reported with early stopping on validation (§4).

## Results (with page or section references)
- Scalarization or UW-SO best or second best on every dataset/architecture by the Δm metric; equal weighting much worse on Cityscapes with SegNet (Δm 59.9 vs 1.9 for scalarization) (Tables 1–2).
- UW overfits: on CelebA its best validation epoch was 6 and it had the worst Δm (Table 3, §4.2).
- "larger networks diminish the influence of weighting methods" (abstract).
- Missing method-specific learning-rate tuning is the main cause of inconsistent rankings in prior work (§1); weight decay matters less (App.).
- Scalarization is infeasible for many tasks (40-task CelebA) (§4.2).

## Limits and risks to validity
_My assessment:_ vision tasks with dense labels and strong signal, not low-signal financial targets; code release not stated. Transfers as practice: tune fixed weights (and the learning rate per setting) on validation, count those trials, and check each task's metric, not only the sum.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard splits, validation early stopping |
| Baselines | 2 | Single-task, equal weighting and six methods, all tuned |
| Point-in-time and leakage controls | N/A | Not financial |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Three datasets, four architectures |
| Statistical testing | 1 | Mean ± std over 5 runs |
| Reproducibility | 0 | Code not stated |
| **Total** | 5/10 → 7/14 | Moderate (non-finance) |

## Quotes worth keeping (each under 15 words, with page)
- "LR tuning is more important than WD tuning" (§1)
