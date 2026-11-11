---
type: lit-note
title: "Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting"
authors: [Hengyi Yang, Sida Lin, Yiyan Qi, Yankai Chen, Haohan Zhang, Xianhua Peng, Jian Guo]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2609.25617
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, pretraining-objective]
---
# Yang 2026 LiMT Liquidity-Aware Multi-Task Stocks (Yang et al., 2026)

**Takeaway:** Adding volume-shock and volatility prediction as auxiliary tasks to next-day return prediction raised CSI300 IC only modestly (0.0543 to 0.0575), the auxiliary losses were given small hand-tuned weights, and simply adding auxiliary heads without the gated transfer module helped less, so auxiliary objectives help only when their influence on the main task is controlled.

## Problem
Whether jointly learning return, volume and volatility improves return forecasts and executable portfolios.

## Data and period
CSI300 and CSI500 constituents, Qlib Alpha158 features; train 2008–2014, validation 2015–2016, test 2017–2020-08 (§IV.1).

## Method
Cross-stock then temporal attention encoder; multi-gate mixture-of-experts with sigmoid gates that pass volume and volatility representations into the return head; loss Σ λ_i·MSE on daily cross-sectional z-scored targets (Eq. 21). λ_r, λ_v, λ_σ chosen from small grids (0.63–0.7, 0.3–0.35, 0.03–0.08) by validation IC (App. A).

## Baselines and validation
Ten deep models plus XGBoost, CatBoost, LightGBM and DoubleEnsemble (Qlib implementations); three seeds; IC, ICIR, excess return and IR vs the CSI index; top-50 long strategy (§IV.2–3). Separate long-short backtest with 10 bp cost and a 2% participation cap (§IV.C).

## Results (with page or section references)
- LiMT IC 0.0575 vs XGBoost 0.0538 and LightGBM 0.0455 on CSI300; 0.0496 vs 0.0410/0.0348 on CSI500 (Table I).
- Ablation on CSI300: without auxiliary tasks IC 0.0543, ICIR 0.4035; without gated transfer 0.0568; without both 0.0528 (Table II).
- Auxiliary heads are predictive on their own: volume-shock IC 0.34, volatility IC 0.52 (§IV.B).
- Long-short with 10 bp costs: Sharpe 1.86 vs 1.22 for equal weighting of the same signal; FF5 daily alpha 0.35% (p < 0.01) (Table III).

## Limits and risks to validity
_My assessment:_ one Chinese market, one split, three seeds; loss weights and other settings tuned on validation IC without a trial-count correction; survivorship of constituent lists not discussed; the portfolio gain mixes the forecast with a new weighting rule. The auxiliary-task effect on IC is small relative to seed variation reported elsewhere.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 2 | Four tuned gradient-boosted tree models plus deep models (cross-sectional setting, no random-walk analogue) |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | 1 | Flat 10 bp plus participation cap |
| Sample breadth | 1 | Two Chinese universes, 2017–2020 incl. March 2020 |
| Statistical testing | 1 | Factor-model alpha t-test; no correction |
| Reproducibility | 1 | Anonymous code repository |
| **Total** | 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "simply adding auxiliary heads is not sufficient" (§IV.B)
