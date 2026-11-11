---
type: lit-note
title: 'When Alpha Disappears: A One-Switch Benchmark for Decision-Time Leakage in Financial Backtests'
authors:
- Fan Zhang
- Zhen Li
- Sijia Peng
- Yu Chen
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2605.23959
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ3.1
- RQ3.6
- RQ3.3
- RQ3.7
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- leakage
---
# When Alpha Disappears: A One-Switch Benchmark for Decision-Time Leakage in Financial Backtests (Zhang et al., 2026)

**Basis:** full text via alphaXiv, opened 2026-11-08 (abstract, setup §4.1, protocol definitions, Tables 1–2).

**Takeaway:** Holding data, split, model and costs fixed and toggling one convention at a time, centered (non-causal) rolling features and same-day-open execution with the day's full bar inflate Sharpe by roughly 15–26 points for Ridge, LightGBM and graph models, while global normalisation, future-informed graph structure and close-to-close execution add almost nothing.

## Problem
How much does each common decision-time violation inflate backtest metrics when the train/test split is already chronological?

## Data and period
Daily OHLCV for S&P 500 constituents (439 tickers, 2010–2024) and CSI 300 constituents (186 tickers); yearly walk-forward tests 2016–2024; horizons 5 and 20 days.

## Method
Clean reference: features from data up to day-t close, entry at t+1 open, open-to-open labels. Five variants each change one rule: TEMP_CENTER (centered rolling windows), EXEC_OPEN (same-day-open entry with the full day-t bar), NORM_GLOBAL (normalisation fit on the full sample), STRUCT_GRAPH (graph built with future data), EXEC_CLOSE (close-based entry). Leakage Gain = variant minus clean, paired.

## Baselines and validation
Six model families (momentum, Ridge, LightGBM, graph MLP, LSTM, Transformer); yearly walk-forward; Wilcoxon tests and confidence intervals in an appendix; 5 bps cost.

## Results (with page or section references)
- US, h=5: clean Sharpe@5bps 0.25–0.68 across models; TEMP_CENTER and EXEC_OPEN gains about 19–23 for Ridge, LightGBM and graph, about 4–9 for LSTM/Transformer; momentum gains 5.4 under EXEC_OPEN only (Table 1).
- NORM_GLOBAL gains about 0.00–0.04; STRUCT_GRAPH up to 0.32; EXEC_CLOSE within ±0.4 (Table 1).
- Effects are positive in 9 of 9 test years for the dominant violations (Table 2).
- Tree and graph models are the most sensitive; sequence models inflate less on the US panel (§4.5).

## Limits and risks to validity
Panels are built from index constituents with "retained tickers", so survivorship is not addressed (it affects clean and variant alike). Only price features; no text, fundamentals or intraday data. Sharpe gains of 20 are mechanical artefacts, so the ranking of violations matters more than the magnitudes. Diagnostic benchmark, not a forecasting claim.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Yearly walk-forward |
| Baselines | 1 | Momentum, Ridge, LightGBM; no random walk |
| Point-in-time and leakage controls | 1 | Decision-time leakage explicit; survivorship not addressed |
| Costs and realism | 1 | Flat 5 bps |
| Sample breadth | 2 | Two markets, 2016–2024 incl. 2020 |
| Statistical testing | 1 | Wilcoxon, CIs; no multiple-testing correction |
| Reproducibility | 1 | Feature schema and configs released |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "The same split can still be wrong." (§1)
