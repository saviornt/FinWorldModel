---
type: lit-note
title: "Risk forecasting using Long Short-Term Memory Mixture Density Networks"
authors: [Nico Herrig]
year: 2025
venue: arXiv (q-fin.CP); MSc thesis, University of St Andrews (2023)
source_url: https://arxiv.org/abs/2501.01278
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6]
family: [tail-risk]
evidence: Moderate
score: 6
tags: [lit-note, family/tail-risk]
---
# Risk forecasting using LSTM Mixture Density Networks (Herrig, 2025)

**Basis:** arXiv v1 pp. 1, 3, 5, 14–15, 34, 47, 51–52, 60–63 via the alphaXiv PDF reader. Results tables (pp. 28–33) not in the pages returned.

**Takeaway:** Negative result: LSTM mixture density networks for 99% VaR on FTSE 100, S&P 500 and EURO STOXX 50 do poorly in a calm period (2017–18), somewhat better in a turbulent one (2021–22), but show no superiority over GARCH(1,1), and results depend on the random weight initialisation.

## Problem
Do LSTM-MDNs give better VaR than historical simulation, a constant-mean model and GARCH, and are they practical (p. 15)?

## Data and period
Three indices; evaluation periods 2017–2018 (calm) and 2021–2022 (turbulent); training sets 2,189–4,565 days (pp. 3, 47).

## Method
LSTM layers feeding a 2- or 3-component Gaussian mixture output (one regularised variant), 10 lagged returns as input, VaR by Monte Carlo sampling; best of three seeds (pp. 3, 34, 51).

## Baselines and validation
HS and constant mean on 250-day windows; GARCH(1,1) with GED innovations; Kupiec, Christoffersen independence and joint tests (pp. 3, 34).

## Results (with page or section references)
- "The results do not indicate a superiority of the neural network approach compared to the GARCH(1,1) model" (p. 51).
- Networks outperformed in the calm EURO STOXX 50 evaluation; comparatively well in the turbulent period (p. 51).
- Correlation of VaR with 5-day rolling volatility lower than GARCH's (e.g. S&P 500 turbulent: NNet1 −0.240 vs GARCH 0.820) (p. 47, Table 5.2).
- Different seeds gave significantly different results (p. 51).

## Limits and risks to validity
_My assessment:_ a master's thesis; two short evaluation windows per index; single train/test split. Useful as a negative result consistent with other studies of deep VaR models.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One train/validation/test split per period |
| Baselines | 1 | HS, CMM, GARCH-GED |
| Point-in-time and leakage controls | 1 | Chronological split; not otherwise discussed |
| Costs and realism | N/A | Risk forecasting |
| Sample breadth | 1 | 3 indices, two 2-year windows |
| Statistical testing | 1 | Kupiec, Christoffersen |
| Reproducibility | 0 | No code or data statement in pages read |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a successful implementation of an LSTM-MDN would just perform well 'on the off chance'" (p. 52)
