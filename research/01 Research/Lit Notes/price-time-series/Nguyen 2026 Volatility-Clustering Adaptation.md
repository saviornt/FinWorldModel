---
type: lit-note
title: "Volatility-Clustering Adaptation for Financial Time Series"
authors: [Manh Nguyen, Minh Hoang Nguyen, Huu Hiep Nguyen, Van Dai Do, Hung Le]
year: 2026
venue: arXiv preprint
source_url: https://arxiv.org/abs/2609.37715
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.1, RQ1.9, RQ4.4, RQ4.9]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series]
---
# Volatility-Clustering Adaptation for Financial Time Series (Nguyen, 2026)

**Basis:** full extracted text via alphaXiv, searched by keyword (Abstract, §1, method, Table 1, data description). Appendix D (limitations) not read in full.

**Takeaway:** Plain next-token fine-tuning of a financial foundation model (Kronos) on target-market data can make forecasts worse than the frozen model; adding a penalty that matches the autocorrelation of squared returns helps, mostly by cutting variance error.

## Problem
Whether more target-domain fine-tuning data improves TSFM forecasts in finance (Abstract).

## Data and period
Three asset sets including CSI300 (Qlib) and 20 Binance USDT pairs at 15-minute bars (data section; App. Table 3). Exact periods not in the part I read.

## Method
VCA: cross-entropy plus a differentiable loss on the gap between rolled-out and realised ACF of squared returns, L = L_CE + λ·L_ACF² (method section). Also tested on Chronos-T5-small.

## Baselines and validation
Frozen Kronos, CE fine-tuning, MSE fine-tuning, GARCH(1,1) and HAR-RV for variance (Table 1). Evaluation conventions "FORE" and one other. No random-walk return baseline or significance tests found in the part I read.

## Results (with page or section references)
- On CSI300 under FORE, CE fine-tuning averages −5.7 Score vs frozen; MSE fine-tuning −6.7 (Table 1).
- On CSI300, HAR-RV improves variance MAE relative to frozen Kronos at the longer horizons (+7.9%, +15.8%), while GARCH is worse than frozen at all horizons (Table 1).
- VCA improves over the pretrained model across the three asset sets, mainly through lower variance error (Abstract).

## Limits and risks to validity
_My assessment:_ single test split, deltas reported relative to frozen model rather than to naive baselines, no significance tests seen; useful mainly as a warning that naive fine-tuning can hurt and that HAR-RV is a strong variance baseline for Kronos.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single split |
| Baselines | 1 | GARCH and HAR-RV for variance; no random walk for returns |
| Point-in-time and leakage controls | 0 | Not in the part read |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | Three asset sets |
| Statistical testing | 0 | None seen |
| Reproducibility | 1 | Code public |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "We show that this assumption can fail in financial forecast-ing" (Abstract)
