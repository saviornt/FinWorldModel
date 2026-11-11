---
type: lit-note
title: "Proactive Model Adaptation Against Concept Drift for Online Time Series Forecasting"
authors: [Lifan Zhao, Yanyan Shen]
year: 2025
venue: KDD 2025
source_url: https://arxiv.org/abs/2412.08435
doi: 10.1145/3690624.3709210
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.9]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series, adaptation, concept-drift, leakage, non-finance]
---
# PROCEED: Proactive Adaptation Against Concept Drift (Zhao & Shen, KDD 2025)

**Basis:** alphaXiv PDF pages 1, 3–4, 7, 11–13 (v5). Shanghai Jiao Tong University. Code: github.com/SJTU-DMTai/OnlineTSF.

**Takeaway:** Earlier online forecasters (FSNet, OneNet) trained on labels that did not yet exist; with the correct H-step feedback delay their errors rise by 107% on average, and a model that estimates drift between the last usable training sample and the current input, then shifts parameters accordingly, beats plain online gradient descent and earlier methods.

## Problem
An H-step forecast's label is known only H steps later, so online updates always use data at least H steps old; drift over that gap is not handled (§1).

## Data and period
ETTh2, ETTm1, Weather, ECL, Traffic; chronological 20:5:75 train/validation/test split (§3.1).

## Method
Online fine-tuning on (X_{t−H}, Y_{t−H}); concept encoders estimate drift between that sample and X_t; an adaptation generator maps drift to parameter shifts; trained on synthetic drifts (§4).

## Baselines and validation
Frozen model, online GD, FSNet, OneNet, SOLID++; backbones TCN, PatchTST, iTransformer; three seeds averaged (§5, App. C.3).

## Results (with page or section references)
- "Practical" (delayed) updating is worse than the infeasible "Optimal" (next-step) updating by 107% MSE on average; the gap grows with horizon; OneNet goes from best under leakage to worst on ETTm1 and Traffic (Table 1, §3.4).
- FSNet and OneNet's official code used the leaky (X_{t−1}, Y_{t−1}) sample (Table 2 note).
- Proceed lowest MSE in most cells, e.g. PatchTST ETTh2 H=24: frozen 2.880, GD 2.092, Proceed 1.735 (Table 3).
- Online GD on PatchTST often helps only a little over frozen (ETTm1 H=96: 0.769 → 0.674; Traffic H=96: 0.403 → 0.398) (Table 3).
- Using partial ground truth adds little but costs up to H× memory (App. E.2).
- Authors suggest monthly rolling retraining plus daily online updates as complementary (App. B.1).

## Limits and risks to validity
_My assessment:_ non-financial; no persistence or seasonal-naive baseline; no significance tests; gains on ECL/Traffic small; synthetic-drift training may not cover market regime shifts.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Online streaming over 75% test span |
| Baselines | 1 | Frozen, online GD and published methods; no naive forecast |
| Point-in-time and leakage controls | 2 | Feedback delay enforced and leakage effect measured |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Five non-finance datasets |
| Statistical testing | 0 | Means of three seeds only |
| Reproducibility | 1 | Code released |
| **Total** | 7/12 → **8/14** | Moderate (non-finance) |

## Quotes worth keeping (each under 15 words, with page)
- "obtaining ground-truth future values of each sample should be delayed until after the forecast horizon" (abstract, p. 1)
