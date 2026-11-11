---
type: lit-note
title: "Regime-Adaptive Continual Learning for Portfolio Management"
authors: [Chaofan Pan, Lingfei Ren, Linbo Xiong, Yonghao Li, Wei Wei, Xin Yang]
year: 2026
venue: KDD 2026
source_url: https://arxiv.org/abs/2606.00143
doi: 10.1145/3770855.3817620
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ4.9]
family: [rl-planning]
evidence: Moderate
score: 8
tags: [lit-note, family/rl-planning, adaptation]
---
# ReCAP: Regime-Adaptive Continual Learning for Portfolios (Pan, 2026)

**Basis:** KDD 2026 version (arXiv v1) read through alphaXiv excerpts (pp. 1, 7–8, 10–12). Main results Table 2–3 seen only via text and Fig. 3; Table 4 and appendix tables read.

**Takeaway:** For PPO portfolio agents on US, Japanese and commodity-ETF universes (test ~2020-05 to 2025), standard continual-learning fixes — fine-tuning, replay (ER), EWC, constrained activations — performed the same as plain rolling retraining (NAS100 average performance 24.5–24.6% vs 24.5%), forgetting was near zero, while a regime library of policy vectors switched by a CUSUM change detector added about 15 points and held up at +10 bps costs.

## Problem
Can continual learning keep RL portfolio policies useful across regime shifts without full retraining (p. 1)?

## Data and period
Five datasets: DOW30, NAS100, SP500, NIKKEI30, commodity ETFs; 12-year training window; test period from about May 2020 to early 2025 (Figs. 3, 5) (pp. 7–8, 11–12).

## Method
Adaptive regime detection (CUSUM; HMM alternative tested) segments data; each regime learns a policy vector added to a library; a regime gate mixes vectors; only the gate and current vector update online; PPO base; 10 seeds; 10 bps costs (p. 7).

## Baselines and validation
Buy-and-hold, constant rebalanced portfolio, universal portfolio, EG, OLMAR, WMAMR; PPO, SAC, A2C, EIIE, SARL, AlphaGAT, Cross-Insight; Static, Retrain, Finetune, ER, EWC, CoR; matched rolling-window retraining for the PM baselines (pp. 7–8, 11–12).

## Results (with page or section references)
- Average performance (DOW30 / NAS100 / SP500): Static 13.1 / 17.5 / 16.2; Retrain 18.3 / 24.5 / 22.9; Finetune, ER, EWC, CoR within ±0.2 of Retrain; ReCAP 24.9 / 39.0 / 47.2 (Table 4, p. 8).
- With fixed quarterly or yearly task boundaries, the best CL baseline still only reaches 19.5 (DOW30) and 28.5 (NAS100) (Table 7, p. 12).
- NAS100 matched rolling retraining: best baseline Sharpe 0.92 vs ReCAP 1.14 (Table 8, p. 12).
- At +10 bps: ReCAP Sharpe 1.02 vs A2C 0.82 (Table 9, p. 12).
- DOW30: ReCAP underperformed from late 2020 to end 2021 before catching up (p. 11).

## Limits and risks to validity
Authors: change-point detection may miss gradual shifts; daily only (pp. 11–12). _My assessment:_ current index constituents imply survivorship; one test period; buy-and-hold numbers not reported in the parts read; no significance tests; gains accumulate late in the sample, which is also when more tuning choices could have been informed by results. The CL-baseline null result (everything ≈ retrain) is the more transferable finding.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One train/test split with online adaptation |
| Baselines | 2 | Buy-and-hold, CRP, rolling retraining, many RL agents |
| Point-in-time and leakage controls | 1 | Online updates causal; survivorship not addressed |
| Costs and realism | 1 | 10 bps with +5/+10 bps sensitivity |
| Sample breadth | 2 | Five universes, 2020–2025 incl. 2022 bear market |
| Statistical testing | 0 | Seed spreads only |
| Reproducibility | 1 | Code on GitHub |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "their overall performance is not superior to native Finetune" (p. 8)
