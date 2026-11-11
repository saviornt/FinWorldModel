---
type: lit-note
title: "Forecasting Probability Distributions of Financial Returns with Deep Neural Networks"
authors: [Jakub Michańków]
year: 2025
venue: arXiv (q-fin.RM), v2
source_url: https://arxiv.org/abs/2508.18921
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6]
family: [tail-risk]
evidence: Moderate
score: 9
tags: [lit-note, family/tail-risk]
---
# Forecasting Probability Distributions of Financial Returns with Deep Neural Networks (Michańków, 2025)

**Basis:** full text of arXiv v2 (pp. 1–12) via the alphaXiv PDF reader.

**Takeaway:** CNN and LSTM networks that output the parameters of a normal, Student-t or skewed-t distribution give VaR exceedance rates close to nominal on six equity indices (2000–2021), comparable to the best GARCH variants; the skewed-t LSTM has the best LPS and CRPS, and normal outputs fail the 1% tests.

## Problem
Do deep networks give accurate, usable return-distribution forecasts compared with GARCH (p. 1)?

## Data and period
Daily log returns of S&P 500, BOVESPA, DAX, WIG, Nikkei 225, KOSPI, 3 Jan 2000–31 Dec 2021; 2,487 forecasts per index (p. 5).

## Method
1D CNN (256 filters) and 3-layer LSTM (128/64/32) trained by negative log-likelihood to output distribution parameters; 10-day input sequences; expanding-window walk-forward with 33% validation and checkpointing (pp. 4–6).

## Baselines and validation
GARCH, APARCH, EGARCH, GJR with N, t, skew-t (p. 10). Metrics: LPS, CRPS, PIT; Kupiec, Christoffersen; McNeil–Frey ES tests (p. 5).

## Results (with page or section references)
- S&P 500 LSTM-SSTD: LPS 1.1933, CRPS 0.5094, best (p. 6, Table 2).
- S&P 500 LSTM: 1% VaR exceedances 1.97% (normal, Kupiec rejected), 1.005% (t), 0.84% (skew-t) (p. 10, Table 4).
- Best NN vs best GARCH exceedances, 1%: S&P 1.01 vs 0.97; DAX 1.12 vs 0.84 (p. 10, Table 5).
- Exceedances cluster in 2008, the European debt crisis and COVID-19 (p. 10).
- PIT p-values for many configurations are below 0.05 (e.g. Nikkei LSTM-SSTD 2.41e-07) (p. 6).

## Limits and risks to validity
_My assessment:_ the NN-vs-GARCH comparison picks the best model per index after the fact and uses exceedance counts only, without loss-based tests (DM, MCS); PIT tests still reject calibration in many cases. No crisis-subperiod statistics.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding-window walk-forward |
| Baselines | 1 | GARCH family only |
| Point-in-time and leakage controls | 1 | Validation inside training window; not otherwise discussed |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 2 | 6 indices, 2000–2021 incl. GFC and COVID |
| Statistical testing | 1 | Kupiec, Christoffersen, ES tests |
| Reproducibility | 1 | Code on GitHub |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "deep neural networks are viable alternatives to traditional econometric models" (p. 11)
