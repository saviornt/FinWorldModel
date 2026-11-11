---
type: lit-note
title: "Random Initialization as a Baseline for Time Series Foundation Models"
authors: [Pinar Sungu Isiacik, Georgiana Ifrim]
year: 2026
venue: NeurIPS 2026 Workshop (TS-LIMITS)
source_url: https://arxiv.org/abs/2610.30950
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.8]
family: [evaluation]
evidence: Strong
score: 11
tags: [lit-note, family/evaluation, pretraining-objective]
---
# Sungu Isiacik 2026 Random Initialization TSFM Baseline (Sungu Isiacik & Ifrim, 2026)

**Takeaway:** Against the same architectures with random weights, the pretrained weights of seven released time-series foundation models (masked-reconstruction, contrastive, self-distillation and multi-task objectives) added only 1.4–5.2 accuracy points on frozen-feature classification; only one model's gain survived a Holm correction, and non-pretrained ROCKET, Hydra and Quant scored higher on average.

## Problem
How much of a TSFM's downstream performance comes from pretraining rather than from its architecture and aggregation pipeline.

## Data and period
UEA multivariate time-series classification archive (30 datasets; 24–27 usable per model), standard train/test splits (§3.3). No financial data.

## Method
Seven released instances from four families: MOMENT (masked reconstruction; S/B/L), Mantis and MantisV2 (contrastive), NuTime (BYOL self-distillation), UniTS (multi-task). Each compared with five architecture-matched random initialisations, frozen encoders, four downstream classifiers (ridge, logistic, RBF SVM, random forest) tuned by training-split CV (§3.2–3.3).

## Baselines and validation
Architecture-matched random weights; ROCKET, Hydra, Quant (§3.4). Wilcoxon signed-rank per model with Holm correction; bootstrap CIs (§3.5).

## Results (with page or section references)
- Mean gain from pretraining 1.43–5.19 points per instance, 2.58 overall; 127 wins, 3 ties, 53 losses over 183 pairs (Table 1).
- After Holm correction only NuTime is significant (p = 0.002); MOMENT gains do not rise with scale (2.29, 1.43, 1.76 points for S/B/L) (Table 1, §4.1).
- ROCKET 0.754, Hydra 0.752, Quant 0.752 mean accuracy vs best TSFM (Mantis) 0.731 (Table 3).
- Recommends architecture-matched random initialisation and strong non-pretrained methods as standard controls (§5).

## Limits and risks to validity
_My assessment:_ classification with frozen encoders, not forecasting or fine-tuning (authors' own limitation, §4.4). Not finance. Transfers as a method point: measure a pretraining objective against a random-init twin and a strong non-pretrained baseline.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard train/test splits |
| Baselines | 2 | Architecture-matched random init plus strong specialised methods |
| Point-in-time and leakage controls | N/A | Not financial |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 24–27 datasets, seven models, no finance |
| Statistical testing | 2 | Wilcoxon with Holm correction, bootstrap CIs |
| Reproducibility | 2 | Code, configs and full results released; public data |
| **Total** | 8/10 → 11/14 | Strong (non-finance; method point only) |

## Quotes worth keeping (each under 15 words, with page)
- "the mean advantage is modest" (abstract)
