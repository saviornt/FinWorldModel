---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- tail-risk
tags:
- lit-note
- family/tail-risk
- metrics
title: E-backtesting
authors:
- Qiuqi Wang
- Ruodu Wang
- Johanna F. Ziegel
year: 2025
venue: Management Science; arXiv 2209.00991 (v6, 2026)
source_url: https://arxiv.org/abs/2209.00991
doi: 10.1287/mnsc.2023.01659
research_questions:
- RQ4.3
- RQ4.5
evidence: Moderate
score: 7
---
# E-backtesting (Wang, Wang & Ziegel, 2025)

**Basis:** arXiv v6 (15 Apr 2026) via the alphaXiv PDF reader, read 2026-11-08: pp. 1–5, 12, 14, 16, 27, 31–32, 36–37, EC-18, EC-23. Management Science version not opened; DOI from OpenAlex lookup.

**Takeaway:** E-values give the first model-free, anytime-valid backtest of ES (with VaR): a regulator can monitor forecasts daily and stop when evidence accumulates, with type I error controlled at any stopping time, at some cost in power versus model-based tests.

## Problem
Backtests of ES need parametric assumptions and fixed sample sizes, so they are invalid under optional stopping (pp. 1–3, Table 1).

## Data and period
Simulations (AR-GARCH, structural-break GARCH); a stock portfolio 3 Jan 2005 – 31 Dec 2021 with normal, t, skewed-t forecasts (pp. 31–36).

## Method
Backtest e-statistics for VaR and (ES, VaR) built from identification functions; betting processes (GREE, GREL, GREM) form e-processes; reject when the e-process exceeds 1/α; thresholds 2, 5, 10 read as minor, substantial, strong evidence (pp. 12–14).

## Baselines and validation
Compared with McNeil–Frey, Nolde–Ziegel and Hoga–Demetrescu sequential monitoring (pp. 31–32, EC-18).

## Results (with page or section references)
- Valid under arbitrary stopping; traditional backtests checked at every sample size have type I error that "explodes" at 10⁵ observations (Remark 3, p. 14; EC-18).
- Portfolio data: detections for thresholds 2 and 5 mostly come before the large 2008 losses (p. 36, Table 7).
- Structural-break simulation: the parametric sequential monitor detects faster; e-backtests detect about 0–30 days later (p. 32).
- One-sided: tests ES underestimation only; ES overestimation cannot be tested this way (Remark 5, p. 16).
- Main limitation: less power than model-based or p-value tests when a fixed sample and a correct model are available (p. 37).

## Limits and risks to validity
_My assessment:_ designed for regulators monitoring one forecaster; useful for this project as an anytime-valid monitor of a live tail model. Code availability not stated in the part read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Sequential evaluation of forecasts |
| Baselines | 1 | Existing ES backtests |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | One portfolio 2005–2021 incl. 2008, simulations |
| Statistical testing | 2 | Anytime-valid error control |
| Reproducibility | 0 | Not stated |
| **Total** | 5/10 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the first model-free and non-asymptotic backtest for ES" (p. 36)
