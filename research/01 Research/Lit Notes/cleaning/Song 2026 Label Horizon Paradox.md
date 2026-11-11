---
type: lit-note
title: "The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting"
authors: [Chen-Hui Song, Shuoling Liu, Liyuan Chen]
year: 2026
venue: arXiv (preprint, E Fund Management)
source_url: https://arxiv.org/abs/2602.03395
doi: 10.48550/arXiv.2602.03395
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ3.5, RQ4.8]
family: [cleaning]
evidence: Moderate
score: 6
tags: [lit-note, family/cleaning, labels]
---
# The Label Horizon Paradox (Song, 2026)

**Basis:** arXiv 2602.03395 read via the alphaXiv report on 2026-11-08 (section-level; no page or table numbers).

**Takeaway:** Training on the same horizon you predict is not always best: for next-day returns on CSI 500, an LSTM trained on a much shorter intraday-horizon label predicts the next-day return better; for 30-minute targets the best label is the target itself; for 90-minute targets an intermediate horizon wins. A learned mixture of label horizons improved IC and Sharpe across ten architectures, A-share indices and the S&P 500.

## Problem
Is the label horizon that matches the inference target the best supervision signal?

## Data and period
CSI 300, 500 and 1000 constituents (minute and daily data), S&P 500; stress test on the 2024 A-share crash (report §§4–5). Exact periods not given in the report.

## Method
Candidate labels r(δ) for δ ≤ Δ; theory from a linear factor model (signal saturates while noise grows linearly with δ); bi-level optimisation learns softmax weights over horizons on an inner/outer data split.

## Baselines and validation
Standard training on r(Δ); equal-weight multi-horizon averaging; brute-force horizon search.

## Results (with page or section references)
- Interday: performance falls monotonically with label horizon (δ* ≪ Δ); 30-minute: rises (δ* ≈ Δ); 90-minute: hump-shaped (§4.3 of report).
- Bi-level method beats standard training across 10 backbones and three CSI indices on IC, RankIC, ICIR and Sharpe; gains also on S&P 500 and during the 2024 crash; portfolio backtest with costs, slippage and TWAP execution (§5).

## Limits and risks to validity
Read via summary only; split design and test periods not verified; no significance tests reported in the summary. The label-horizon choice is itself a tuned hyperparameter and needs out-of-sample selection.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Chronological split (assumed from summary) |
| Baselines | 1 | Standard training, averaging |
| Point-in-time and leakage controls | 1 | Not detailed |
| Costs and realism | 1 | Costs, slippage, TWAP in backtest |
| Sample breadth | 2 | Three A-share universes, S&P 500, crash period |
| Statistical testing | 0 | None reported |
| Reproducibility | 0 | Not stated |
| **Total** | 6/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read via report).
