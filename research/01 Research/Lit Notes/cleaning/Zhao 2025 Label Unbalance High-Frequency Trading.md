---
type: lit-note
title: "Label Unbalance in High-frequency Trading"
authors: [Zijian Zhao, Xuming Zhang, Jiayu Wen, Mingwen Liu, Xiaoteng Ma]
year: 2025
venue: arXiv (preprint, Likelihood Lab)
source_url: https://arxiv.org/abs/2503.09988
doi: 10.48550/arXiv.2503.09988
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.5]
family: [cleaning]
evidence: Weak
score: 5
tags: [lit-note, family/cleaning, labels, class-imbalance]
---
# Label Unbalance in High-frequency Trading (Zhao, 2025)

**Basis:** arXiv 2503.09988 read via the alphaXiv report on 2026-11-08 (section-level).

**Takeaway:** When labels are set by whether a 29.5-second return clears the trading fee, about 80% of samples are "no trade"; plain class-weighted losses worked best, while under-sampling and focal loss were sometimes worse than doing nothing, on only 20 days of Chinese futures data.

## Problem
Which imbalance treatment works for fee-aware three-class HFT labels?

## Data and period
0.5-second data, six Chinese futures (rebar, silver, fuel oil, nickel, tin, gold), 4–29 May 2023 (20 trading days); chronological 80/10/10 split.

## Method
Label +1 / −1 / 0 by return vs fee; MLP, LSTM, Mamba backbones; under-sampling, fixed class weights (8/1/8), class-size weighting, focal loss, accuracy-weighted loss.

## Baselines and validation
No-adjustment benchmark.

## Results (with page or section references)
- Class 0 ≈ 80%, ±1 ≈ 10% each.
- Fixed and class-size loss weighting best; under-sampling and focal loss sometimes below benchmark; training on all six contracts cut overfitting.

## Limits and risks to validity
20 days; no trading test; read via summary only.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | No-adjustment benchmark |
| Point-in-time and leakage controls | 1 | Chronological split |
| Costs and realism | N/A | Fee used in label only |
| Sample breadth | 0 | 20 days |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code public (per report) |
| **Total** | 4/12 → 5/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept (summary read).
