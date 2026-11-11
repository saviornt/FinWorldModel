---
type: lit-note
title: "Forecasting Equity Correlations with Hybrid Transformer Graph Neural Network"
authors: [Jack Fanshawe, Rumi Masih, Alexander Cameron]
year: 2026
venue: arXiv (q-fin.CP)
source_url: https://arxiv.org/abs/2601.04602
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.4, RQ1.6]
family: [graph]
evidence: Weak
score: 5
tags: [lit-note, family/graph]
---
# Forecasting Equity Correlations with a Transformer–GNN (Fanshawe, 2026)

**Basis:** pp. 1–3, 6, 13–16, 22–23 read through alphaXiv page excerpts.

**Takeaway:** A Transformer + graph-attention model predicting 10-day S&P 500 pairwise correlations as residuals over a rolling baseline cuts MAE from 0.307 to 0.230 (2019–2024), but it is compared only with persistence, the graph is not ablated, and the authors could not reproduce the ML gains of the trading study they build on.

## Problem
Can forward-looking correlation forecasts improve graph-based clustering for basket statistical arbitrage?

## Data and period
S&P 500 stocks (CRSP/Compustat, FRED macro), 37 features incl. VIX, oil, rates, sector codes; train 2006–2018, out-of-sample from March 2019 to 2024 (p. 6).

## Method
Transformer temporal encoder, edge-aware GAT, predicting Fisher-z residual over a rolling correlation; forecasts fed to SPONGEsym clustering and an ML filter trading the top 10% of signals (pp. 6, 13).

## Baselines and validation
Persistence (past 20-day correlation) for forecasting; S&P 500 buy-and-hold for trading; stationary-bootstrap Sharpe test (pp. 13–16). Authors note no LSTM, CNN or other GNN comparison (p. 23).

## Results (with page or section references)
- 269 million edge forecasts: MAE 0.307 → 0.230, RMSE 0.385 → 0.294, Pearson 0.31 → 0.78 (Table 1, p. 14).
- Errors spike for both in COVID 2020 and Feb–Jul 2022; model about 0.05 lower in those periods (p. 14–15).
- Strategy Sharpe 1.84 vs S&P 500 0.65, max drawdown −9.4% (Table 3, p. 16), without slippage (p. 23).
- Replication of Korniejczuk & Ślepaczuk (2024): non-ML baseline matched, ML gains not reproduced (p. 15).

## Limits and risks to validity
Authors state: no slippage, no alternative ML models, one hyperparameter set (p. 23). _My assessment:_ persistence is a weak correlation baseline (no DCC-GARCH, shrinkage or EWMA); the graph's own contribution is not isolated; benchmark is the index, not a market-neutral peer.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One split |
| Baselines | 0 | Persistence only |
| Point-in-time and leakage controls | 1 | Rolling features, 60-day gap |
| Costs and realism | 0 | No slippage |
| Sample breadth | 2 | S&P 500, includes 2020 and 2022 stress |
| Statistical testing | 1 | Bootstrap Sharpe test |
| Reproducibility | 0 | Not stated |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "highlights the fragility of backtests" (p. 23)
