---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- metrics
title: Volatility forecast comparison using imperfect volatility proxies
authors:
- Andrew J. Patton
year: 2011
venue: Journal of Econometrics 160(1), 246–256; QFRC Research Paper 175 (2006)
source_url: https://www.uts.edu.au/sites/default/files/qfr-archive-02/QFR-rp175.pdf
doi: 10.1016/j.jeconom.2010.03.034
research_questions:
- RQ4.3
evidence: Moderate
score: 6
---
# Volatility forecast comparison using imperfect volatility proxies (Patton, 2011)

**Basis:** UTS Quantitative Finance Research Centre Research Paper 175 (2006 version) PDF, read 2026-11-08 through a summarising page fetch; journal version not opened.

**Takeaway:** When the volatility target is measured with noise (squared returns, range, realised variance), only losses in a specific family — including MSE and QLIKE — rank forecasts as they would with the true variance; MAE, MSE on log or standard deviation and proportional losses can prefer badly biased forecasts, especially with daily squared returns.

## Problem
Forecast comparison with a conditionally unbiased but noisy volatility proxy (pp. 1–4).

## Data and period
Analytical results; IBM returns 1993–2003 (captions say 1994), 60-day rolling window vs RiskMetrics, 2,500 comparison days (p. 16, Tables 3–4).

## Method
Necessary and sufficient conditions for robust losses (Proposition 2); QLIKE the only robust loss depending only on σ̂²/h (Proposition 3); a robust homogeneous family nesting MSE (b = 0) and QLIKE (b = −2) (Proposition 4) (pp. 13–15).

## Baselines and validation
Two volatility models compared with DM-type tests across proxies (Table 4).

## Results (with page or section references)
- With daily squared returns, the optimal forecast under MAE is about 0.45σ², under MSE-log about 0.28σ², under MSE-prop about 3σ² (Table 1, pp. 6–8, 30).
- With 5-minute realised variance the distortions nearly vanish (MSE-log 0.98σ², MAE 0.99σ²) (Table 2, p. 31).
- IBM: QLIKE DM statistics 1.94 (daily), 2.21–2.73 with intraday proxies, favouring RiskMetrics; MSE differences insignificant (Table 4, p. 32).
- Recommends robust losses (MSE, QLIKE, or b ≤ −2 when moments are a concern) and the least noisy proxy (pp. 15–18).

## Limits and risks to validity
_My assessment:_ theory with a one-stock illustration; read via summarising fetch of the working paper. Standard reference behind QLIKE use in RP1 volatility studies.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling forecasts in the illustration |
| Baselines | 1 | Two simple volatility models |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 0 | One stock |
| Statistical testing | 1 | DM-type tests |
| Reproducibility | 1 | Matlab code offered by the author |
| **Total** | 4/10 → **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- (none kept; read via summary)
