---
type: lit-note
title: "Adaptive Window Selection for Financial Risk Forecasting"
authors: [Yinhuan Li, Chenxin Lyu, Ruodu Wang]
year: 2026
venue: arXiv (q-fin.RM), v2
source_url: https://arxiv.org/abs/2603.01157
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.6, RQ4.9]
family: [tail-risk]
evidence: Moderate
score: 8
tags: [lit-note, family/tail-risk]
---
# Adaptive Window Selection for Financial Risk Forecasting (Li, 2026)

**Basis:** arXiv v2 (29 May 2026) pp. 1–4, 12, 15, 18–22, 24–27, 39 via the alphaXiv PDF reader.

**Takeaway:** Choosing the look-back window adaptively (keep the longest window whose score is not significantly worse than shorter ones, with a bootstrap threshold) lowers joint VaR–ES loss on the S&P 500 in 2006–2025 and especially in the GFC, where fixed 250–750-day and full windows react with long delays.

## Problem
Fixed rolling windows trade bias against variance and lag after structural breaks such as the GFC and COVID (p. 2).

## Data and period
Daily S&P 500 losses, 4 Jan 2005–30 Oct 2025 (Yahoo Finance); forecasts from 28 Dec 2006; stress episodes GFC, COVID, 2025 tariffs (pp. 20–21, 24). Plus simulations with breaks, smooth drift and GARCH volatility shifts (pp. 15–19).

## Method
Bootstrap-based adaptive window selection (BAWS) using elicitable scores (VaR check loss, joint VaR–ES score); moving block bootstrap; max window 1,000 (pp. 1, 3, 20–21).

## Baselines and validation
SAWS (Huang & Wang 2025), fixed windows 250/500/750, full window (p. 21).

## Results (with page or section references)
- Average joint VaR–ES loss (%), 2006–2025: BAWS 2.2642, SAWS 2.3145, 250-day 2.3565, full 2.4447 (p. 22, Table 4).
- GFC: BAWS 3.2513, SAWS 3.1852, 250-day 3.6631, full 4.1779; COVID: BAWS 4.0501, SAWS 3.8752, 250-day 4.1750 (p. 22).
- Tariff 2025: 750-day window best (2.3021) (p. 22).
- SAWS "exhibits sharper spikes", suggesting overreaction to transient shocks (p. 21).
- Gains "not uniformly in every scenario" (p. 4).

## Limits and risks to validity
_My assessment:_ one index; window selection is applied to a non-parametric (historical) estimator, not to GARCH or ML models; no significance tests on the empirical loss differences in pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Sequential rolling forecasts, 2006–2025 |
| Baselines | 1 | Fixed/full windows and SAWS; no GARCH or EVT |
| Point-in-time and leakage controls | 2 | Past-only windows |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 1 | One index with three stress episodes |
| Statistical testing | 0 | No tests on empirical differences in pages read |
| Reproducibility | 1 | Public data; code not stated |
| **Total** | **7/12 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "fixed and full windows react with substantial delays" (p. 4)
