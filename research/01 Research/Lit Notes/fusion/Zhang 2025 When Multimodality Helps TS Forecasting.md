---
type: lit-note
title: "When Does Multimodality Lead to Better Time Series Forecasting?"
authors: [Xiyuan Zhang, Boran Han, Haoyang Fang, Abdul Fatir Ansari, Shuai Zhang, Danielle C. Maddix, Cuixiong Hu, Andrew Gordon Wilson, Michael W. Mahoney, Hao Wang, Yan Liu, Huzefa Rangwala, George Karypis, Bernie Wang]
year: 2025
venue: "arXiv (cs.CL), v2"
source_url: https://arxiv.org/abs/2506.21611
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.7, RQ1.2, RQ1.15]
family: [fusion]
evidence: Moderate
score: 6
tags: [lit-note, family/fusion]
---
# When Does Multimodality Lead to Better Time Series Forecasting? (Zhang et al., 2025)

**Basis:** arXiv v2 (29 Sep 2025), pp. 1–7, 18, 31, via the alphaXiv PDF reader. Found by snowballing from [[Zhou 2026 When Context Routing Helps Fusion]] and [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]].

**Takeaway:** Across 16 text-paired forecasting tasks (7 domains, incl. MTFinance), text–time-series models did not beat the strongest unimodal models on average (paired t-test p = 0.79 for MSE); gains appear mainly when the time-series model is weak (correlation 0.90 between unimodal error and multimodal gain), the text model is large, training data are ample and text is complementary; prompting LLMs with series plus text lost to aligned models and to unimodal Chronos.

## Problem
Whether and under which modelling and data conditions adding text improves time-series forecasting (p. 1).

## Data and period
16 datasets: Time-MMD domains (agriculture, climate, economy, energy, environment, health, social good, traffic), fashion, weather, medical, PTF, MSPG, LEU, MTFinance, MTWeather (p. 4; Table 1).

## Method
Aligning-based (time-series encoder + text encoder + fusion: add/concat, avg/CLS pooling, MLP/residual projector, early/middle/late fusion, fine-tuning strategies) and prompting-based (LLaMA-405B, Qwen-32B/72B, Mixtral, GPT-4o-mini, Claude 3.5) methods (pp. 3–4, 7).

## Baselines and validation
Unimodal PatchTST, DLinear, Chronos, plus Time-LLM, TimeCMA, LeRet; MSE, MAE, WQL, CRPS; paired t-tests (p. 4).

## Results (with page or section references)
- Unimodal models best on 6/16 datasets (MSE) and 7/16 (MAE); unimodal vs aligned Chronos p = 0.789 (MSE), 0.247 (MAE) (p. 4).
- MTFinance MSE: unimodal DLinear and Chronos 0.002 vs aligned PatchTST 0.060; prompting GPT-4o-mini and Claude 0.002 (p. 5, Table 1) — no multimodal gain on finance.
- Prompting is worse than aligning; larger LLMs help but do not reach unimodal Chronos; distilled reasoning models were worse than non-reasoning ones (pp. 4–6).
- Multimodal gain rises with unimodal weakness (corr 0.90) (p. 7, Fig. 6).
- Fusion design is dataset-dependent: addition beat concatenation on average; location and fine-tuning choices varied (p. 7, Table 2).

## Limits and risks to validity
_My assessment:_ mostly non-financial data; the single finance dataset is a short benchmark. LLM prompting on public datasets that predate model cutoffs risks contamination (not discussed in pages read). No code statement seen. Transfers as a design rule: test text against a strong unimodal baseline, not a weak one.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Benchmark splits |
| Baselines | 2 | PatchTST, DLinear, Chronos (strong simple and FM baselines) |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | 16 datasets, 7 domains; one finance set |
| Statistical testing | 1 | Paired t-tests; no multiple-testing correction |
| Reproducibility | 0 | Not stated in pages read |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "MMTS models do not consistently outperform the strongest unimodal baselines." (p. 4)
