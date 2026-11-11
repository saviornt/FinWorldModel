---
type: lit-note
title: "ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall"
authors: [Yichi Zhang, Ke Zhu, Zhoufan Zhu]
year: 2026
venue: arXiv (stat.ML)
source_url: https://arxiv.org/abs/2606.04576
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6, RQ1.1]
family: [tail-risk]
evidence: Strong
score: 11
tags: [lit-note, family/tail-risk]
---
# ReSGA: A Large Tail Risk Model for Learning VaR and ES (Zhang, 2026)

**Basis:** arXiv v1 pp. 1, 3–4, 6–7, 9, 12–14, 16–17, 25, 34, 38–39, 42 via the alphaXiv PDF reader. Tables 2–4 (numeric loss and pass rates) not in the pages returned.

**Takeaway:** A single pooled model (GRU encoder, learned asset groups, retrieval of similar histories) trained on 153 firm characteristics for 40,000+ US stocks gives the lowest joint 5% VaR–ES loss in 2014–2023, beats per-asset GARCH and GAS significantly, and transfers to five other markets without retraining; scaling tests credit more data, not more parameters.

## Problem
Can a high-capacity "universal" model trained on massive cross-sectional data forecast VaR and ES better than per-asset econometric models (p. 3)?

## Data and period
Jensen–Kelly–Pedersen dataset, monthly, Jan 1926–Dec 2023, 153 characteristics rank-normalised, missing values set to cross-sectional medians (pp. 13–14). Expanding window: train from 1926, 18-year validation, test one year at a time, 2014–2023 (p. 14).

## Method
FZ-loss joint VaR–ES learning framework; ReSGA = GRU encoder + self-grouping + retriever + decoder (pp. 7, 9, 42).

## Baselines and validation
Linear, NN, LANN, DLinear, LSTM, GRU, Informer variants, SGA, plus per-asset GARCH and GAS (pp. 12–13). Tests: DM, model confidence set (90%), Christoffersen CC, Bayer–Dimitriadis ES regression test (p. 17).

## Results (with page or section references)
- ReSGA has the lowest out-of-sample loss in the full sample and all five size groups (p. 16).
- All eleven pooled models "substantially outperform" GARCH and GAS (p. 16); only SGA and ReSGA remain in the MCS (p. 17).
- Scaling: gains "primarily driven by data complexity rather than model complexity" (p. 1); increasing model size alone "does not guarantee better tail-risk forecasts" (p. 25).
- Transfer without retraining: lowest loss in Japan, UK, Australia; 4th in China, 2nd in Canada (p. 34).

## Limits and risks to validity
_My assessment:_ monthly 5% level, so not the daily 99% regulatory setting; crisis subperiods (COVID) not split out in pages read. Median imputation of characteristics uses contemporaneous cross-sections, acceptable point-in-time but worth checking. Portfolio results reported without costs in pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding window with separate validation |
| Baselines | 2 | GARCH, GAS and ten ML models |
| Point-in-time and leakage controls | 1 | Lagged characteristics; leakage not discussed explicitly |
| Costs and realism | 0 | Portfolio claims without costs in pages read |
| Sample breadth | 2 | 40,000+ stocks, 2014–2023 incl. COVID, five other markets |
| Statistical testing | 2 | DM plus model confidence set |
| Reproducibility | 2 | Code, data links and forecasts on companion site |
| **Total** | **11/14 → 11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "simply increasing model size alone does not guarantee better tail-risk forecasts" (p. 25)
