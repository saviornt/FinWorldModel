---
type: lit-note
title: "WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting"
authors: [Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng, Wongmeng Shen, Chenjuan Guo, Bin Yang, Jilin Hu, Christian S. Jensen]
year: 2026
venue: "arXiv cs.LG (preprint)"
source_url: https://arxiv.org/abs/2609.31162
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15]
family: [fusion]
evidence: Weak
score: 4
tags: [lit-note, family/fusion, world-model]
---
# WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting (Zhu et al., 2026)

**Basis:** arXiv v1 (25 Sep 2026), pp. 1–4, 7–9, 15, 18 (Tables 1–4), via the alphaXiv PDF reader.

**Takeaway:** A JEPA-style latent world model (predict the encoded future state from encoded history plus covariates, then train a decoder) beat published covariate-aware baselines on 21 non-financial datasets, incl. five electricity-price markets with load and wind forecasts (e.g. Nord Pool MSE 0.297 vs 0.325 for KITE); removing covariates raised error (Colbun MSE 0.052 → 0.073, MMSP 0.061 → 0.101), and one-stage observation-space training was worse than latent supervision.

## Problem
Let covariates shape latent-state formation and evolution rather than only the observation-space forecast (pp. 1–3).

## Data and period
12 numerical-covariate sets (NP, PJM, BE, FR, DE electricity prices; Chilean energy and hydro; wind turbines), 8 Time-MMD text sets, one satellite-image solar set (pp. 7, 15).

## Method
Two stages: (1) shared TS encoder, modality encoders (frozen GPT-2 input embeddings for text, CNN for images), predictor trained with L1 + cosine + VICReg on encoded future states; (2) frozen encoder and predictor, decoder trained to observations (pp. 4, 7, 18).

## Baselines and validation
Baseline numbers copied from DAG, KITE, VoT and UniCA papers under their protocols (pp. 7–8). No significance tests; no random walk.

## Results (with page or section references)
- Best MSE and MAE on all 12 numerical-covariate sets (p. 8, Table 1); 14 of 16 text-set cells (Table 2); MMSP MSE 0.061 vs TFT 0.067 (Table 3).
- Ablation (MSE): Colbun full 0.052, no covariates 0.073, one-stage 0.059; Climate 1.072 vs 1.134 and 1.149; MMSP 0.061 vs 0.101 and 0.085 (p. 9, Table 4).

## Limits and risks to validity
_My assessment:_ no financial-asset data (electricity prices are a market, with future-known load and wind forecasts as covariates, a structure equities lack). Baselines taken from other papers' tables, so tuning effort is not matched. The covariate-free ablation covers only three datasets. Relevant only as evidence that latent-state prediction is a workable world-model training recipe.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Benchmark chronological splits |
| Baselines | 1 | Strong covariate-aware models; no naive |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 21 datasets, none equities |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Code not stated in pages read |
| **Total** | **3/12 → 4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "sequences of observations generally provide only a partial view of the dynamics" (p. 1)
