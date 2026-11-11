---
type: lit-note
title: "Cross-Modal Temporal Fusion for Financial Market Forecasting"
authors: [Yunhua Pei, John Cartlidge, Anandadeep Mandal, Daniel Gold, Enrique Marcilio, Riccardo Mazzon]
year: 2025
venue: "arXiv (cs.LG) v2; PAIS at ECAI 2025"
source_url: https://arxiv.org/abs/2504.13522
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7]
family: [fusion]
evidence: Weak
score: 4
tags: [lit-note, family/fusion]
---
# Cross-Modal Temporal Fusion for Financial Market Forecasting (Pei et al., 2025)

**Basis:** arXiv v2 (12 Aug 2025, accepted ECAI-PAIS manuscript), pp. 1–2, 5–8, via the alphaXiv PDF reader. Guide seed source.

**Takeaway:** A transformer fusing prices, macro series, LLM-scored news and reports for five FTSE 100 stocks reached F1 0.64 on next-day direction versus 0.61 for linear regression and SVR, but its precision (51.0%) was below random forest (51.5%) and near chance; removing both text sources cost only 0.02 F1, and the authors note simpler models' strength suggests text matters little for next-day prices.

## Problem
Align multi-frequency structured and unstructured data (prices, macro, news, reports) for next-day direction forecasting with interpretability (pp. 1–2).

## Data and period
Five FTSE 100 firms (Shell, Unilever, BAT, BP, Diageo), 02/2019–05/2024 (1,360 days); OHLCV, US/UK bond yields, GDP, CPI; company news and reports scored on five dimensions by Llama-3.1-8B. Chronological split 804/268/268 days; test 10/2023–05/2024 (pp. 5–6, Tables 1–2).

## Method
Tensor encoding of all modalities, Lasso-based tensor interpretation for feature selection, encoder-only transformer; Optuna TPE hyperparameter search (pp. 5).

## Baselines and validation
Zero change, linear regression, ARIMA, random forest, SVR, LSTM, transformer. Precision, recall, F1 only (p. 6).

## Results (with page or section references)
- Precision: CMTF 51.04%, RF 51.54%, SVR 50.10%, linear 49.33%; F1: CMTF 0.64, linear 0.61, SVR 0.61, RF 0.60, LSTM 0.13 (p. 6, Table 3). The F1 edge comes mostly from recall (predicting "up" more often).
- Ablation without interpretation module: +news +reports F1 0.61; no text 0.59 (p. 7, Table 4).
- Authors: SVR's strength "suggests that unstructured data may be less relevant for next-day price level prediction" (p. 7).

## Limits and risks to validity
_My assessment:_ five stocks, one 8-month test window, no significance tests, recall-driven F1 in a mostly rising market can reward always predicting "up". Llama-3.1-8B (training cutoff end-2023) scored text that partly predates its cutoff, with no memorisation control (rubric cap at Weak). Extensive Optuna search with a single validation window risks overfitting. Code public, data on request.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Zero-change, RF, SVR, LSTM; no GBT |
| Point-in-time and leakage controls | 0 | LLM pre-cutoff text, no control |
| Costs and realism | N/A | Classification only, no trading claim |
| Sample breadth | 0 | Five stocks, short period |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code public; data on request |
| **Total** | **3/12 → 4/14** | Weak (also capped: LLM pre-cutoff) |

## Quotes worth keeping (each under 15 words, with page)
- "increased complexity is justified only when it adds meaningful predictive value." (p. 7)
