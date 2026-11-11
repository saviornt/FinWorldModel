---
type: lit-note
title: "Do Better Volatility Forecasts Lead to Better Portfolios? Evidence from Graph Neural Networks"
authors: [Rylan Wade]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2605.19278
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ1.4, RQ1.1, RQ1.15, RQ3.7]
family: [graph]
evidence: Moderate
score: 7
tags: [lit-note, family/graph]
---
# Do Better Volatility Forecasts Lead to Better Portfolios? (Wade, 2026)

**Basis:** full text (pp. 1–10, v2) read through alphaXiv page excerpts.

**Takeaway:** On 465 S&P 500 stocks, a GraphSAGE model on a rolling correlation graph beats HAR and LSTM for weekly realised volatility only slightly (MSE 0.0322 vs 0.0329), sector and Granger graphs do worse than HAR, and macro features, not the graph, give most of the gain; portfolio value depends on the construction.

## Problem
Do GNNs improve weekly realised-volatility forecasts over HAR and LSTM, and do better forecasts give better portfolios?

## Data and period
465 current S&P 500 constituents, daily OHLCV from yfinance, 2015–2025; target is weekly realised volatility. Train 2015–2022, validate 2023, test 2024–2025 (103 weeks) (p. 2).

## Method
Shared GraphSAGE backbone on three graphs: weekly-updated rolling return correlation (|ρ| ≥ 0.3), GICS sector (updated annually), and a static Bonferroni-corrected Granger graph from the training period; each with and without macro features (VIX, credit spread, term spread, average correlation); inverse-MSE ensemble (pp. 3–4).

## Baselines and validation
Per-stock and pooled HAR (Corsi 2009), a 2-layer LSTM without cross-stock information. One chronological split; GNN hyperparameters tuned on 2023 (p. 2, Table 1). Four portfolios at 10 bps per unit turnover vs equal weight (p. 5).

## Results (with page or section references)
- Test MSE: HAR per-stock 0.0329, LSTM 0.0324, GNN-Correlation 0.0322, GNN-Sector 0.0336, GNN-Granger 0.0337; best is GNN-Correlation + macro (63-day window) 0.0298 (Table 3, p. 6).
- Rank IC: LSTM 0.429 with the highest ICIR (4.36); GNN-Sector and GNN-Granger without macro are the weakest (0.383, 0.375); best GNN ensemble + macro 0.438 (Table 4, p. 6).
- Macro features improve every graph model; sector graph MSE goes from 0.0336 to 0.0315 with macro (p. 5).
- Minimum-variance Sharpe: GNN-Sector + macro 0.984 vs HAR pooled 0.729; no model beats equal weight in inverse-volatility weighting (0.513); volatility targeting and long–short are negative for every model (Tables 5–8, pp. 7–8).
- Correlation graph density goes from 0.09 in a calm 2018 week to 0.93 in March 2020; dense crisis graphs risk oversmoothing (Table 2, p. 4; p. 9).

## Limits and risks to validity
Author states: survivorship (current constituents), short 2024–2025 test regime, static Granger graph, specific cost and weight settings (p. 10). _My assessment:_ no significance tests (Diebold–Mariano or MCS) on MSE gaps of about 2%; no GBT baseline; the graph model and the macro set are tuned on validation while HAR and LSTM are fixed, which favours the GNN.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | HAR and LSTM; no GBT |
| Point-in-time and leakage controls | 1 | Lagged features, annual GICS; survivorship |
| Costs and realism | 1 | Flat 10 bps with turnover |
| Sample breadth | 1 | 465 stocks; test has no stress period |
| Statistical testing | 0 | None |
| Reproducibility | 2 | Code released; public data source |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "graph connectivity is not generically useful" (p. 5)
