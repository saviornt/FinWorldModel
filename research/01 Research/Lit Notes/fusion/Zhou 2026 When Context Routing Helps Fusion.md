---
type: lit-note
title: "When Does Context Routing Help? A Systematic Study of Multi-Modal Fusion in Time Series Forecasting"
authors: [Ruizhe Zhou, Gaoyuan Du, Xiaoyang Liu, Haoqi Yao, Deepayan Chakrabarti, Jiating Lin, Yixuan Shen]
year: 2026
venue: "arXiv (cs.LG); MILETS 2026 workshop"
source_url: https://arxiv.org/abs/2608.25128
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.7, RQ4.4]
family: [fusion]
evidence: Moderate
score: 6
tags: [lit-note, family/fusion]
---
# When Does Context Routing Help? A Systematic Study of Multi-Modal Fusion in Time Series Forecasting (Zhou et al., 2026)

**Basis:** arXiv v1 (25 Aug 2026), pp. 1–2, 4, 6, 8, 11–12, via the alphaXiv PDF reader.

**Takeaway:** Context can only help when the target is not dominated by a last-value shortcut and the context carries information beyond history (a mutual-information permutation test); on financial news (FinMultiTime, 50 S&P 500 tickers) neither holds, a repeat-last-value baseline beats a 14.3B-parameter MoE model, and no fusion mechanism (cross-attention, gating, text-as-variable, output fusion) shows context-attributable gains.

## Problem
Whether reported multimodal fusion gains reflect use of context or incidental architecture effects (extra parameters, regularisation, residual paths) (p. 1).

## Data and period
Time-MMD domains (health, environment, social good, energy, transport, climate, web), FinMultiTime (financial news with S&P 500 prices), 27 Monash datasets for the autocorrelation check (pp. 1–2, 4, 11).

## Method
Two dataset conditions: low h-step autocorrelation and non-zero conditional mutual information I(C; X_{t+h} | X_t), tested by a 200-permutation MI test on residuals. Interventions: toggling text modulation in MoME (Qwen1.5-MoE, 14.3B), adding a shortcut, corrupting context at 0–100% mask rates; four fusion mechanisms in one PatchTransformer testbed with real vs zeroed context (pp. 2, 4, 6).

## Baselines and validation
Repeat-last-value, DLinear, PatchTST, Chronos-T5-Small (zero-shot). MoME 10 seeds with 95% CIs; testbed 3 seeds (10 for some cells) (pp. 4, 11–12).

## Results (with page or section references)
- FinMultiTime (ρ = 0.999): naive repeat-last-value MSE 8.8e-5 beats MoME with modulation 9.1e-5; routing contribution +6.7%, i.e. capacity floor, not context (p. 4, Table 1).
- 50 S&P 500 tickers: MI tests on daily returns non-significant for all 50; routing benefit within ±3% noise (p. 11, B.6).
- Where both conditions hold (HealthUS ρ = 0.77), text modulation cut MSE 51%; corrupting 50–75% of the text made it worse than constant text ("low-quality context is worse than no context") (p. 4, Table 5).
- Adding a last-value shortcut suppressed routing contribution by 77–93% on three datasets (pp. 1–2).
- Testbed: on MI-significant data, small gains (cross-attention +3.2%, output fusion +9.5% on transport); on MI-non-significant data, cross-attention and text-as-variable were slightly harmful (−5.9%, −6.9%, not significant) (p. 6; p. 11, Table 6).
- Pre-training diagnostic (TRY / SKIP / INCONCLUSIVE) gave no false SKIPs in well-powered settings on the datasets tested (p. 6).

## Limits and risks to validity
Large positive magnitudes come from one model family; testbed confirms only direction (p. 8). Single-lag MI conditioning; point forecasts only; finance results are on price levels (near unit root), which makes the "shortcut dominates" finding partly mechanical. _My assessment:_ for returns rather than prices the shortcut argument is weaker, but the null MI result on returns for 50 tickers still stands. No transaction-level or point-in-time text checks.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard benchmark splits |
| Baselines | 2 | Repeat-last-value, DLinear, Chronos, unimodal |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | 6 + 27 datasets; 50 tickers |
| Statistical testing | 1 | Seeds, CIs, permutation tests; no multiple-testing correction |
| Reproducibility | 0 | Code not stated in pages read |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "low-quality context is worse than no context." (p. 4)
