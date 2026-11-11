---
type: lit-note
title: "The Effectiveness of Discretization in Forecasting: An Empirical Study on Neural Time Series Models"
authors: [Stephan Rabanser, Tim Januschowski, Valentin Flunkert, David Salinas, Jan Gasthaus]
year: 2020
venue: arXiv
source_url: https://arxiv.org/abs/2005.10111
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, tokenization]
---
# The Effectiveness of Discretization in Forecasting (Rabanser, 2020)

**Basis:** PDF pages 1–2, 5, 7, 10–11 (v1).

**Takeaway:** Binning inputs and outputs usually improves neural forecasters, and output binning matters more than input binning, but the effect depends on the model: it helps WaveNet, does nothing for a feed-forward net, and hurts DeepAR.

## Problem
Systematic test of input and output transformations (scaling, binning) across neural forecasting architectures (§1, p. 2).

## Data and period
M4 (hourly, daily, weekly, monthly, quarterly, yearly), electricity, traffic, Wikipedia (Tables 1–3, pp. 10–11). No financial returns.

## Method
Mean scaling; global relative (quantile) binning, local absolute binning, probability-integral transform, and multi-resolution hybrid binning (16/128/1024 bins), with WaveNet, DeepAR and feed-forward models; outputs either binned (categorical) or real-valued (Student-t, spline quantiles) (§3; §5, pp. 5–7).

## Baselines and validation
Comparison is between representations within each architecture; mean ± sd over runs; no classical baseline (Tables 1–3).

## Results (with page or section references)
- WaveNet with 1,024 quantile bins on input and output "almost always" beats all other combinations (m4_y the exception) (§5, p. 5).
- DeepAR is much worse with binned outputs than with mean-scaled real outputs (§5, p. 5; Table 1, e.g. m4_d wQL 0.2134 binned vs 0.0282 Student-t, p. 10).
- Input binning matters less than output binning; few input bins suffice, while more output bins steadily help (§5, p. 7).
- Multi-scale hybrid binning on the input is often best for WaveNet (§5, p. 7).

## Limits and risks to validity
_My assessment:_ non-financial data; one holdout per dataset; no statistical tests. Useful as the earliest controlled evidence that the value of discretisation depends on the architecture and loss.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard holdout |
| Baselines | 1 | Real-valued variants of each model; no naive |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 9 datasets, no finance |
| Statistical testing | 0 | Mean ± sd only |
| Reproducibility | 1 | Public datasets |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "binning almost always improves performance" (Abstract, p. 1)
