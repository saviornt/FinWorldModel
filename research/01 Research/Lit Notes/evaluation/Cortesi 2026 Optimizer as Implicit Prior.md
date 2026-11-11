---
type: lit-note
title: "Same Error, Different Function: The Optimizer as an Implicit Prior in Financial Time Series"
authors: [Federico Vittorio Cortesi, Giuseppe Iannone, Giulia Crippa, Tomaso Poggio, Pierfrancesco Beneventano]
year: 2026
venue: arXiv (cs.LG) 2603.02620 (v2, Oct 2026)
source_url: https://arxiv.org/abs/2603.02620
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.4, RQ4.6, RQ4.7]
family: [evaluation]
evidence: Strong
score: 12
tags: [lit-note, family/evaluation, training, underspecification]
---
# Same Error, Different Function (Cortesi et al., 2026)

**Basis:** Full text (selected pages 1–4, 6, 10, 23–24, 47–48, 55, 57) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** In daily S&P 500 volatility forecasting, 12 architecture–optimizer pairs (13 seeds each) are statistically tied on test error and none beats HAR, yet the optimizer changes the learned function and the portfolio it drives (up to 58% turnover dispersion at near-equal gross Sharpe), so model choice under a tie must use decision-level criteria.

## Problem
Whether models with comparable out-of-sample loss are interchangeable in low-signal financial forecasting, and whether the optimizer only affects efficiency or also the learned function (§1).

## Data and period
Survivorship-bias-free S&P 500 constituents from CRSP, 2000–2024; target next-day Garman–Klass log-variance; 100-lag input (§2.1, App. C). Chronological train/validation/test 3:1:1; 564,795 held-out observations from 21 May 2020 (App. C, G.1).

## Method
4 architectures (MLP, CNN, LSTM, Transformer) × 3 optimizers (SGD, Adam, Muon); learning rate and weight decay tuned on validation, then refit on train+validation; 13 repeated fits per configuration. Prediction distances, impulse-response surfaces, SHAP lag attribution, matched-initialization refits (§2.2–2.3, §4).

## Baselines and validation
OLS, LASSO and HAR baselines; clipping and standardisation fitted on training data only (App. C). Holm–Bonferroni across 66 pairwise comparisons; TOST equivalence tests (§3.1).

## Results (with page or section references)
- Test NMSE: HAR 0.5671 (lowest); OLS 0.5751; best neural 0.5747 ± 0.0015 (CNN–Adam); SGD runs vary most (e.g. LSTM–SGD 0.5899 ± 0.0203) (Table 1, p. 4).
- After Holm–Bonferroni, only 7 of 66 comparisons reject equal NMSE; 59 (89%) are indistinguishable (§3.1, p. 4).
- With identical initialization and data order, models diverge 1.3–7.8× more across optimizers than across repeated runs in 11 of 12 comparisons; predictions differ by 5–17% of typical forecast error while error magnitudes differ by under 0.7% (abstract, p. 1).
- Volatility-quintile portfolios: gross Sharpe 0.883–0.959 (Q1) but turnover max/min ratio 1.41 (Q1) and 1.58 (Q5); no costs deducted, full-history diagnostic (App. G.3).

## Limits and risks to validity
_My assessment:_ one target (volatility), one market, one chronological split; portfolio diagnostic is gross and partly in-sample (App. G.1 says so). Strong for the claim that ties are common and seeds/optimizers change the function; it does not show which training choice is better. Relevance: seed and optimizer variation must be measured and reported, and selection under a tie should use the downstream objective (turnover, decision stability), not tiny loss gaps.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 2 | HAR, OLS, LASSO |
| Point-in-time and leakage controls | 2 | Survivorship-free CRSP; train-only preprocessing |
| Costs and realism | N/A | Forecasting study; portfolio is a gross diagnostic |
| Sample breadth | 2 | ~500 stocks, 2000–2024, test includes 2020 and 2022 stress |
| Statistical testing | 2 | Holm–Bonferroni, TOST |
| Reproducibility | 1 | Recorded artifacts and exact CRSP query; code release not stated |
| **Total** | 10/12 → **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "In finance, the optimizer is part of the model." (p. 10)
