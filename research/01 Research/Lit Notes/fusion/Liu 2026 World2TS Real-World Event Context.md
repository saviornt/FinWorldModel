---
type: lit-note
title: "World2TS: Real-World Event Context for Time-Series Forecasting"
authors: [Zhiding Liu, Jiqian Yang, Mingyue Cheng, Zhi Li, Enhong Chen]
year: 2026
venue: "arXiv cs.LG (under review, Sci China Inf Sci)"
source_url: https://arxiv.org/abs/2610.14861
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15, RQ1.14]
family: [fusion]
evidence: Weak
score: 5
tags: [lit-note, family/fusion, world-model]
---
# World2TS: Real-World Event Context for Time-Series Forecasting (Liu et al., 2026)

**Basis:** arXiv v1 (10 Oct 2026), pp. 1–2, 9–13 (Tables 2–3, Figs. 3–6), via the alphaXiv PDF reader.

**Takeaway:** An agent-plus-human pipeline linked 1,159 verified real-world events to 4,179 series in six domains; giving the linked pre-origin events to LLM forecasters reduced error in 49 of 54 paired comparisons (finance: GPT-5.6 MAE 0.189 → 0.176 on Apple closes, vs Chronos-2 0.218), but event context also hurt (an energy case +93% MAE when the model assumed a storm's effect would persist), and PatchTST without context stayed best on transport and energy.

## Problem
Build a large dataset aligning real-world events with the series they affect, and test whether that context improves forecasts (pp. 1–2).

## Data and period
31 datasets, 97.1M observations, 56,846 event–series links; evaluation uses one series per domain (finance: Apple close; crypto: Bitcoin), look-back 96, horizon 6 (finance, health) or 24; only test windows whose look-back contains a linked event (pp. 2, 9–10).

## Method
Events discovered by web search and agent reasoning, verified by humans, linked with temporal and semantic scope. Forecasters: Seasonal Naive, PatchTST, Chronos-2 (numbers only); GPT-5.6, DeepSeek-V4-Flash, CastFSR-Zero agent, each with and without context, closed-book (p. 10).

## Baselines and validation
Chronological 70/10/20 split, train-only scaling, non-overlapping test windows; MAE, RMSE, sMAPE; no significance tests (p. 10).

## Results (with page or section references)
- Context lowered error in 49 of 54 model–domain–metric pairs; GPT in 18 of 18 (p. 11).
- Finance MAE: Seasonal 0.295, PatchTST 0.384, Chronos-2 0.218; GPT 0.189 → 0.176 with context; DeepSeek 0.186 → 0.187 (no gain); CastFSR 0.208 → 0.201 (p. 12, Table 3).
- Energy case: context-driven persistence assumption raised MAE by 93% (p. 12, Fig. 6).

## Limits and risks to validity
_My assessment:_ events were found after the fact by searching for what explains each series, and test windows were selected to contain such events: this is hindsight selection, so the context is not what a forecaster would have had. The LLM forecasters (GPT-5.6, DeepSeek-V4) are run on 2013–2024 data inside their training windows, so memorisation is not controlled (rubric cap). One target series per domain; finance is a single stock. Useful as a general "world context" benchmark and for the failure case, not as evidence for finance.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 1 | Seasonal naive, PatchTST, Chronos-2 |
| Point-in-time and leakage controls | 0 | Hindsight event selection; pre-cutoff LLMs |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Six domains, one series each |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Dataset and homepage released |
| **Total** | **4/12 → 5/14, capped** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "no individual contextual record is guaranteed to improve a forecast" (p. 12)
