---
type: lit-note
title: Synchronizing Multivariate Financial Time Series
authors:
- Francesco Audrino
- Peter Bühlmann
year: 2002
venue: Working paper (revised May 2002), ETH Zürich / University of Southern Switzerland
source_url: https://doc.rero.ch/record/5232/files/1_fin0206.pdf?version=1
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.3
family:
- cleaning
evidence: Weak
score: 5
tags:
- lit-note
- family/cleaning
- asynchronous-trading
---
# Synchronizing Multivariate Financial Time Series (Audrino & Bühlmann, 2002)

**Basis:** working-paper PDF (RERO), read through a summarising page fetch on 2026-11-08; journal publication not checked.

**Takeaway:** Daily closes from markets with different hours understate cross-market correlation; estimating each index's value at the New York close (following Burns, Engle & Mezrich 1998) raised DJIA–Nikkei correlation from 0.19 to 0.33 and DJIA–DAX from 0.24 to 0.38, and slightly improved out-of-sample portfolio volatility loss, though not every pair rose.

## Problem
How to model daily data from markets that close at different times.

## Data and period
Seven equity indices (DJIA, CAC40, DAX, BCI, CBS, FTAS, Nikkei 225); estimation 1990-01 to 1994-06 (~1,000 days), test 1994-06 to 1996-09 (500 days); synchronised to 4 p.m. New York.

## Method
Synchronise prices to a common time, then fit a CCC-GARCH(1,1) on synchronised data.

## Baselines and validation
Asynchronous CCC-GARCH and univariate models; out-of-sample loss and VaR violation counts.

## Results (with page or section references)
- Correlations rise for most US–foreign pairs (Table 3.1); some fall (DAX–Nikkei 0.32 → 0.28).
- Portfolio out-of-sample loss 240.8 → 227.4 with synchronisation.
- VaR violations similar across models (95%: 27, 23, 24 vs 25 expected); no formal test (Fig. 4.2).

## Limits and risks to validity
Seven indices, 1990s; VaR comparison informal. Read through a summarising tool.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One later test window |
| Baselines | 1 | Asynchronous and univariate models |
| Point-in-time and leakage controls | 1 | Timing alignment is the subject |
| Costs and realism | N/A | |
| Sample breadth | 1 | Seven markets, one period |
| Statistical testing | 0 | Informal |
| Reproducibility | 0 | No code |
| **Total** | 4/12 → **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
