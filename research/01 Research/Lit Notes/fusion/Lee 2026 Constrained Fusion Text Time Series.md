---
type: lit-note
title: "Rethinking Multimodal Fusion for Time Series Forecasting: Text Modalities Need Constrained Fusion"
authors: [Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, SoonYoung Lee, Wonbin Ahn]
year: 2026
venue: "arXiv (cs.LG) v3; KDD 2026 MILETS Workshop"
source_url: https://arxiv.org/abs/2603.22372
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.7, RQ4.4]
family: [fusion]
evidence: Moderate
score: 7
tags: [lit-note, family/fusion]
---
# Rethinking Multimodal Fusion for Time Series Forecasting: Text Modalities Need Constrained Fusion (Lee et al., 2026)

**Basis:** arXiv v3 (15 Jul 2026), pp. 1–2, 4–5, 8, 21, 27, 39, via the alphaXiv PDF reader.

**Takeaway:** Across ~20K runs (9 Time-MMD datasets, 14 TS backbones, 4 text encoders), naive addition or concatenation of text embeddings often underperformed the text-free model and sometimes diverged, while constrained fusion (gating, FiLM, orthogonal injection, a low-rank residual adapter "CFA") beat both, with CFA beating the unimodal model on 13 of 14 backbones; normalised MSE: concat 0.36–0.62, add 0.33–0.42, no text 0.35, gating 0.26, CFA 0.26.

## Problem
Why naive text–time-series fusion often fails, and whether constraining how text enters fixes it (p. 1).

## Data and period
Time-MMD (agriculture, climate, economy, energy, environment, public health, security, social good, traffic); 7:1:2 split; four horizons (p. 4).

## Method
Fusion at first/middle/last layer by addition or concatenation (naive) vs gating, FiLM, orthogonal-component injection, and CFA (text injected through a low-rank residual adapter); text encoder frozen (BERT, GPT-2, Llama3, Doc2Vec) (pp. 2, 4).

## Baselines and validation
Each backbone without text (incl. DLinear, PatchTST, TiDE, Koopa, iTransformer); MSE/MAE; 10 learning rates per setting with the best reported (p. 4).

## Results (with page or section references)
- Naive fusion frequently below the unimodal baseline and sometimes divergent (MSE >10× unimodal) (p. 4, Table 4).
- CFA win rate vs unimodal 88.9–100% per backbone with BERT; gating 66.7–100%; naive concat-middle 11.1% on several backbones (p. 4, Table 4).
- Average normalised MSE: concat first/middle/last 0.484/0.364/0.621; additive 0.421/0.333/0.334; no fusion 0.349; orthogonal/FiLM/gating 0.317/0.275/0.261; CFA 0.256 (p. 5, Fig. 3d).
- CFA adds 0.61% parameters (p. 8, Table 5).

## Limits and risks to validity
_My assessment:_ Time-MMD is the benchmark whose "multimodal lift" was traced to a co-shipped numeric column rather than text in [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]]; this paper does not run shuffled- or placebo-text controls, so it shows constrained fusion is safer, not that text content helps. "Best of 10 learning rates" may be selected on test results (not clear in pages read). No financial data. Code released.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Fixed benchmark split |
| Baselines | 2 | Unimodal versions of 14 backbones incl. DLinear |
| Point-in-time and leakage controls | 0 | Not addressed; selection rule unclear |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | 9 domains, no finance |
| Statistical testing | 0 | None |
| Reproducibility | 2 | Code; public data |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "naive fusion often underperforms unimodal baselines" (p. 8)
