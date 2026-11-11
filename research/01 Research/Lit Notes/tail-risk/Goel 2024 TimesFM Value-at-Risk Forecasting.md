---
type: lit-note
title: "Time-Series Foundation AI Model for Value-at-Risk Forecasting"
authors: [Anubha Goel, Puneet Pasricha, Juho Kanniainen]
year: 2024
venue: arXiv (q-fin.RM), v7 May 2025
source_url: https://arxiv.org/abs/2410.11773
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6, RQ1.1]
family: [tail-risk]
evidence: Moderate
score: 9
tags: [lit-note, family/tail-risk]
---
# Time-Series Foundation AI Model for Value-at-Risk Forecasting (Goel, 2024)

**Basis:** arXiv v7 pp. 1–3, 5, 7–8, 11–13, 18, 21, 23 via the alphaXiv PDF reader.

**Takeaway:** Fine-tuned Google TimesFM gives the best actual-over-expected violation ratios for 1-day VaR on 91 S&P 100 stocks (2015–2023 out of sample) and matches the GAS model on quantile loss; zero-shot TimesFM is clearly worse, and at 5% and 10% levels it fails to beat historical simulation.

## Problem
Can a pretrained time-series foundation model forecast left-tail quantiles as well as GARCH and GAS (pp. 1–2)?

## Data and period
Daily returns of the S&P 100 index and 91 constituents, Jan 2005–Sep 2023 (Datastream); 2005–2014 estimation, 2 Jan 2015–19 Sep 2023 test (2,268 forecasts) (pp. 7–8).

## Method
TimesFM zero-shot (only 10% decile available) and fine-tuned daily on a rolling window with linear probing of quantile heads; prediction lengths 1, 21, 63 days (p. 8). TimesFM's quantile heads "have not been calibrated after pretraining" per its GitHub (p. 8, footnote).

## Baselines and validation
GARCH with EDF, normal and t residuals; one-factor GAS; 512-day historical simulation. GARCH/GAS parameters estimated once on 2005–2014 (p. 7). Tests: |1−AE|, quantile score, Diebold–Mariano, Kupiec UC, Christoffersen CC, DQ (pp. 11–12).

## Results (with page or section references)
- VaR(1%) mean |1−AE|: FT1 0.328, FT63 0.282, GAS 0.424, G-t 0.399, G-N 0.892, Historical 0.348 (p. 13, Table 2).
- FT1 outperforms GAS on |1−AE| for VaR 1%, 5% and 10% (t-tests, p. 12).
- Quantile score: GAS 1.005 relative to FT1 at 1%; DM tests show no preference among TimesFM variants (p. 18).
- At 5% and 10% VaR, TimesFM "fails to beat the historical simulation method" (p. 18).
- Zero-shot use is "not optimal" and significantly worse than econometric benchmarks (pp. 1, 3).

## Limits and risks to validity
_My assessment:_ GARCH and GAS are not re-estimated through the test period while TimesFM is fine-tuned daily, which favours TimesFM. No crisis-subperiod breakdown in the pages read (test includes COVID). Possible overlap of TimesFM pretraining data with the test period is not discussed.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One split; benchmarks fixed, TimesFM rolling |
| Baselines | 2 | GARCH (3 variants), GAS, historical simulation |
| Point-in-time and leakage controls | 1 | Pretraining-data overlap not addressed |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 2 | 91 stocks + index, 2015–2023 incl. COVID |
| Statistical testing | 1 | DM, t-tests, UC/CC/DQ; no multiple-testing correction |
| Reproducibility | 1 | Code on GitHub; Datastream data licensed |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "fine-tuning is practically necessary for the foundation model" (p. 3)
