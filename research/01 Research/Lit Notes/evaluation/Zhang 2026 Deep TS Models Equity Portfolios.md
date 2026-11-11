---
type: lit-note
title: "Benchmarking Deep Time Series Models for Equity Portfolios"
authors: [Aoxin Zhang, Yuhan Cheng, Kwanting Leung]
year: 2026
venue: arXiv (math.OC) 2606.09420
source_url: https://arxiv.org/abs/2606.09420
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.6, RQ4.7]
family: [evaluation]
evidence: Strong
score: 12
tags: [lit-note, family/evaluation, economic-value, transaction-costs]
---
# Benchmarking Deep Time Series Models for Equity Portfolios (Zhang, Cheng & Leung, 2026)

**Basis:** Full text (pp. 1, 8–10, 17, 19–20, 28, 37, 40, 44–45) via the alphaXiv PDF reader, read 2026-11-09.

**Takeaway:** On a CRSP daily panel (2020–2024 test), 15 deep and statistical models give strong gross long–short decile Sharpe ratios for a few (ridge 3.88), but turnover decides what survives 20 bps costs, and once capacity, beta, industry and turnover constraints are imposed every promoted model has negative net Sharpe; ridge, the gross winner, ranks fourth after the decision layer.

## Problem
Whether forecast-architecture benchmarks for daily equity portfolios still rank models the same way once costs, preferences and portfolio constraints are imposed (p. 1).

## Data and period
Daily CRSP common stocks 2018–2024, filters on share code, exchange, price ≥ $5 and dollar volume; delisting returns included; 5,451 assets; shared evaluation window 2020-03-30 to 2024-12-30 (1,197 days); confirmatory window 2021–2024 (Table 1, p. 8; Table 44, p. 45).

## Method
15 architectures (TS-RIDGE, TS-OLS, AR1-GARCH, LSTM, GRU, RNN, transformer encoders, PatchTST, N-BEATS, TSMixer, MoE-MLP, graph-LSTM) predict next-day returns in a walk-forward protocol (refit every 21 days). Equal-weight daily decile long–short portfolios; SMAA multi-criteria ranking; a constrained quadratic portfolio layer with capacity, beta, industry, leverage and turnover controls (pp. 8–9, 17).

## Baselines and validation
Walk-forward; ridge, OLS and AR-GARCH baselines (no gradient-boosted trees); moving-block bootstrap (20-day blocks, 10,000 resamples), BH-FDR and Bonferroni, SPA screen, Model Confidence Set; FF5 alphas with Newey–West (Table 1, p. 8).

## Results (with page or section references)
- Gross Sharpe: TS-RIDGE 3.88, TS-OLS 2.48, LSTM 0.98, TransEnc-8 0.71; net Sharpe at 20 bps: 0.60, −2.32, 0.60, 0.48; turnover 0.72, 1.18, 0.17, 0.10 (Table 3, p. 9).
- After 20 bps the 90% MCS narrows from seven models to TransEnc-8, LSTM, TransEnc-10 (p. 10).
- Constrained portfolio at 20 bps: net Sharpe −0.76 (TransEnc-8) to −3.99 (TS-OLS) for all five promoted models; at 50 bps −2.23 to −8.75 (Table 12, p. 17); "does not by itself establish a profitable trading rule" (p. 19).
- Break-even costs ~10 bps (TS-OLS) to 24–61 bps in the decile layer, but at or below a few bps in the constrained layer (p. 28). Restricting to the Top 500 turned the best combinations negative (Table 23, p. 28); Top 1000 at 0.8–2 bps: only the two transformers slightly positive (Table 35, p. 40).
- Weekly rebalancing raised TS-RIDGE net Sharpe from 0.60 to 1.02 (p. 40).
- Strong stock sorting did not give positive aggregate market-timing R²oos (p. 28).
- General forecasting benchmark ranks (GIFT-Eval MASE/CRPS proxies) were not significantly related to CRSP Sharpe (r −0.24 to −0.63, all p > 0.13) (Table 36, p. 40).

## Limits and risks to validity
_My assessment:_ test window starts in the high-dispersion 2020 recovery; costs are flat bps, not spread- or impact-based; deep models trained for eight epochs per refit, so they may be under-tuned; no gradient-boosted tree baseline. Strong evidence that gross ranking ≠ net ranking and that liquid-universe constraints remove most of the edge.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Walk-forward, refit every 21 days |
| Baselines | 1 | Ridge, OLS, AR-GARCH; no GBT |
| Point-in-time and leakage controls | 2 | CRSP with delisting returns; next-date alignment |
| Costs and realism | 2 | Reconstructed turnover, 10/20/50 bps, capacity, constrained QP |
| Sample breadth | 2 | ~4,400–5,450 stocks, 2020–2024 incl. COVID recovery and 2022 |
| Statistical testing | 2 | Block bootstrap, BH-FDR, Bonferroni, MCS |
| Reproducibility | 1 | Scripts and fixed environment; licensed data excluded |
| **Total** | **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "Gross Sharpe is a selection input." (p. 10)
