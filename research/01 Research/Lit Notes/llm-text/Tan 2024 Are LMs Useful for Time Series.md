---
type: lit-note
title: "Are Language Models Actually Useful for Time Series Forecasting?"
authors: [Mingtian Tan, Mike A. Merrill, Vinayak Gupta, Tim Althoff, Thomas Hartvigsen]
year: 2024
venue: NeurIPS 2024 (arXiv 2406.16964)
source_url: https://arxiv.org/abs/2406.16964
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.2, RQ1.7]
family: [llm-text]
evidence: Moderate
score: 8
tags: [lit-note, family/llm-text]
---
# Are Language Models Actually Useful for Time Series Forecasting? (Tan, 2024)

**Basis:** v2, page excerpts via alphaXiv (pp. 1–2, 4–6, 9, 19–21, 23).

**Takeaway:** Removing the LLM from three popular LLM-based forecasters (Time-LLM, CALF, OneFitsAll), or replacing it with one attention layer, gives the same or better accuracy at up to three orders of magnitude less compute; pretraining, sequence order and few-shot settings show no LLM benefit.

## Problem
Does the language model inside LLM-based time-series forecasters contribute anything?

## Data and period
13 benchmarks, including daily exchange rates of eight currencies (1990–2016) and FRED-MD macro series (p. 4).

## Method
Three ablations per method: no LLM, LLM→attention, LLM→transformer block; shuffled inputs; random initialisation; 10% few-shot (pp. 4, 9).

## Baselines and validation
Reproduced original results; DLinear, PatchTST, iTransformer and others (Table 19, p. 23). Standard fixed splits; bootstrapped 95% CIs.

## Results (with page or section references)
- Ablations beat Time-LLM in 26/26, CALF 22/26, OneFitsAll 19/26 dataset–metric cases (p. 5).
- Exchange rate: "w/o LLM" has lower MAE than Time-LLM at every horizon (Table 15, p. 19).
- Time-LLM: 6,652M parameters vs 0.55M for its ablation; 3,003 vs ~2 minutes training on Weather (p. 6).
- No few-shot benefit (Tables 7–8, p. 9).

## Limits and risks to validity
_My assessment:_ mostly non-financial data; point forecasting of numeric series only, so it says nothing about LLMs reading text. Transfers to the "price tokens" question because exchange rates and FRED-MD are included.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Fixed split |
| Baselines | 1 | Strong deep baselines; no RW |
| Point-in-time and leakage controls | N/A | General benchmarks |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 13 datasets; 2 financial |
| Statistical testing | 1 | Bootstrap CIs |
| Reproducibility | 2 | Code and data public |
| **Total** | **6/10 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "pretrained LLMs do no better than models trained from scratch" (abstract, p. 1)
