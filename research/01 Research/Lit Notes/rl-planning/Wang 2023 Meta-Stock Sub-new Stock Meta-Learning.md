---
type: lit-note
title: "Meta-Stock: Task-Difficulty-Adaptive Meta-learning for Sub-new Stock Price Prediction"
authors: [Linghao Wang, Zhen Liu, Peitian Ma, Qianli Ma]
year: 2023
venue: AAAI 2024 (arXiv cs.CE)
source_url: https://arxiv.org/abs/2308.11117
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ4.9]
family: [rl-planning]
evidence: Weak
score: 5
tags: [lit-note, family/rl-planning, meta-learning]
---
# Meta-Stock: Meta-Learning for Newly Listed Stocks (Wang, 2023)

**Basis:** Full PDF read through alphaXiv, pp. 1–2, 5–9. Appendix not read.

**Takeaway:** For stocks listed less than a year (US, China, Hong Kong; test Dec 2021–Feb 2022), Reptile-style first-order meta-learning trained on older stocks beats training only on the new stocks and usually beats plain transfer learning on MCC (e.g. China 8.4–10.3 vs 6.7–8.3), but accuracies stay at 51–57%, the plain Reptile trading strategy lost 79% a year, and the test window is under three months.

## Problem
Can meta-learning on old stocks give fast adaptation to newly listed ("sub-new") stocks with little history (pp. 1–2)?

## Data and period
AKShare daily data for US, CN and HK markets, 2000-01-01 to 2022-02-22; old stocks up to 2021-02-22; sub-new stock data 2021-02-23 to 2022-02-22 split 6:2:2, so test = 2021-12-03 to 2022-02-22; samples with small moves (between −0.5% and +0.55%) filtered out (p. 5).

## Method
Reptile-style outer update (φ ← φ + β(φ_k − φ)) with inner-loop gradients weighted by task difficulty measured from wavelet high-frequency coefficients; then fine-tune on sub-new stocks (pp. 5). Four time-series CNN/LSTM backbones; grid search on validation; 5 repeats.

## Baselines and validation
Train on sub-new stocks only; transfer learning (pre-train + fine-tune); plain Reptile; Wilcoxon signed-rank tests (pp. 5–6).

## Results (with page or section references)
- CN MCC: train-only 0.5–4.9; transfer 6.7–8.3; Reptile 8.4–10.3; Meta-Stock 10.4–11.5 (Table 1, p. 6).
- Accuracy 51–57% everywhere; US accuracy of Meta-Stock is not best for any backbone (Table 1).
- Trading (ResNet, all markets): Reptile annual return −79%, Sharpe −2.08; Meta-Stock +141%, Sharpe 2.05 (Table 2, p. 6).
- Reptile helped easy and medium tasks but hurt hard (volatile) tasks early in training (Table 3, p. 7).

## Limits and risks to validity
_My assessment:_ filtering out small-move days at test time inflates accuracy and is not tradable as stated; the trading test has no costs, a ~2.5-month window and one backbone, so a swing from −79% to +141% between two variants signals noise, not skill. Useful as evidence that first-order meta-learning transfers some structure to new listings (the cold-start use case), not as evidence of profit.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Train-only, transfer learning, Reptile; no simple model |
| Point-in-time and leakage controls | 1 | Time split; test-sample filtering on realised moves |
| Costs and realism | 0 | None |
| Sample breadth | 1 | Three markets, one short window |
| Statistical testing | 1 | Wilcoxon; no multiple-testing correction |
| Reproducibility | 0 | No code link seen |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "Reptile takes riskier trading decisions and often experiences enormous losses" (p. 6)
