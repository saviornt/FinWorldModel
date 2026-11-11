---
type: lit-note
title: "Comparative analysis of financial data differentiation techniques using LSTM neural network"
authors: [Dominik Stempień, Janusz Gajda]
year: 2025
venue: arXiv (q-fin)
source_url: https://arxiv.org/abs/2505.19243
doi: 10.48550/arXiv.2505.19243
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6]
family: [cleaning]
evidence: Moderate
score: 6
tags: [lit-note, family/cleaning, normalisation, fractional-differencing]
---
# Fractional Differencing vs Log Returns for LSTM (Stempień, 2025)

**Basis:** arXiv 2505.19243v1 pages 1, 3, 12, 35–37, 41–56 read via alphaXiv on 2026-11-08.

**Takeaway:** On four equity indices (2014–2023, 2021–2023 test), LSTMs fed fractionally differenced log prices (d estimated on training data only) had lower price-level RMSE than those fed log returns for all four indices, and an ARFIMA-estimated d did best in trading tests; but errors are measured on price levels after inverting the transform, with no random-walk baseline, so the gain may reflect persistence rather than skill.

## Problem
Do memory-preserving (fractional) differences beat log returns as inputs?

## Data and period
S&P 500, WIG20, DAX, Nikkei 225 daily, 2014–2023; train 2014–2020 (validation 2019–2020), test 2021–2023 (pp. 3, 35–37).

## Method
Log returns; López de Prado minimum-d fractional differencing (ADF on training data); ARFIMA(0,d,0) d; tempered ARTFIMA; plus technical indicators; one LSTM per series and asset (pp. 36–45).

## Baselines and validation
Log-return LSTM; buy-and-hold for trading. One chronological split; transaction costs included (p. 45).

## Results (with page or section references)
- S&P 500 RMSE: log returns 65.3, fractional (López de Prado d) 49.8, ARFIMA d 49.9 (Table 4, p. 46).
- WIG20: López de Prado d worst (39.4), ARFIMA d best (30.5) (p. 46).
- Tempered differencing behaved like log returns (d ≈ 1) and did worst (pp. 43, 53).
- Long-short strategies rarely beat buy-and-hold; ARFIMA-d long-only beat it on information ratio for all four (p. 48).

## Limits and risks to validity
Price-level error metrics; no random-walk or naive baseline; four indices, one split; no significance tests; extensive hyperparameter tuning per series.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One split |
| Baselines | 0 | No random walk; buy-and-hold only for trading |
| Point-in-time and leakage controls | 2 | d estimated on training data only |
| Costs and realism | 1 | Flat costs |
| Sample breadth | 1 | Four indices, one test regime |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Public data; code not stated |
| **Total** | 6/14 | Moderate (low end) |

Note: the headline comparison is on price levels with no naive baseline, so it cannot by itself show predictive skill; cited for the direction of the effect only.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
