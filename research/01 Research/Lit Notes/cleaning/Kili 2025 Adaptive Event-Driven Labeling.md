---
type: lit-note
title: "Adaptive Event-Driven Labeling: Multi-Scale Causal Framework with Meta-Learning for Financial Time Series"
authors: [Amine Kili, Brahim Raouyane, Mohamed Rachdi, Mostafa Bellafkih]
year: 2025
venue: Applied Sciences 15(24), 13204
source_url: https://www.mdpi.com/2076-3417/15/24/13204
doi: 10.3390/app152413204
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.5]
family: [cleaning]
evidence: Weak
score: 4
tags: [lit-note, family/cleaning, labels, triple-barrier, trend-scanning]
---
# Adaptive Event-Driven Labeling (Kili, 2025)

**Basis:** MDPI HTML page read via page fetch on 2026-11-08 (first 100,000 of 104,256 characters, summarised by the fetch tool; no page numbers).

**Takeaway:** In the only source found that runs fixed-horizon, triple-barrier and trend-scanning labels side by side (16 assets, 2000–2025), all three standard labels gave average Sharpe ratios near or below zero (−0.29, −0.03, 0.00); the authors' adaptive labeling reached 0.48, but parameters, costs and the out-of-sample scheme are not described on the page.

## Problem
Can label horizons adapt to regime instead of being fixed?

## Data and period
16 assets incl. SPY, QQQ, IWM, VTI, 2000–2025 (others not listed on the page).

## Method
Multi-scale horizons, Granger-style causal filtering, meta-learning; baselines FH (horizon h, threshold τ), TB, trend scanning.

## Baselines and validation
The three standard label methods; Wilcoxon test vs FH p = 0.0024.

## Results (with page or section references)
- Average Sharpe: FH −0.29, TB −0.03, TS 0.00, AEDL 0.48 (abstract).
- Ablation on 12 assets: minimal baseline −0.404; adding attention cut asset coverage to 2/12.

## Limits and risks to validity
Baseline parameters unstated; costs not mentioned; walk-forward not confirmed; complex method with many components tuned on the same assets.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | "Out-of-sample" stated, scheme not confirmed |
| Baselines | 1 | Three standard label methods |
| Point-in-time and leakage controls | 0 | Not described |
| Costs and realism | 0 | Not mentioned |
| Sample breadth | 2 | 16 assets, 25 years |
| Statistical testing | 1 | Wilcoxon; correction mentioned, not named |
| Reproducibility | 0 | Not stated |
| **Total** | 5/14 → capped Weak 4 (page read partly, via summary) | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept (summary read).
