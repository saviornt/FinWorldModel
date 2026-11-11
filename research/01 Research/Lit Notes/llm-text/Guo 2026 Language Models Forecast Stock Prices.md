---
type: lit-note
title: "Can Language Models Learn to Forecast Stock Prices"
authors: [Jiacheng Guo, Suozhi Huang, Shuzhen Li, Yunlong Gao, Zerui Cheng, Jason Ge, Shushu Liang, Zihao Li, Hao Lu, Ming Yin, Shilong Liu, Jiashuo Liu, Xu Kuang, Mengdi Wang]
year: 2026
venue: arXiv 2609.36914
source_url: https://arxiv.org/abs/2609.36914
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.2, RQ1.9]
family: [llm-text]
evidence: Weak
score: 5
tags: [lit-note, family/llm-text]
---
# Can Language Models Learn to Forecast Stock Prices (Guo, 2026)

**Basis:** v1 (29 Sep 2026), page excerpts via alphaXiv (pp. 1–6, 8, 15–18).

**Takeaway:** On a price-and-volume-only, tool-use forecasting benchmark, simple momentum extrapolation beats seven of nine frontier LLMs, frontier LLM scores collapse in the later test period, and a 4B model post-trained with SFT and PPO matches the frontier mostly by better magnitude, not direction.

## Problem
Can post-training (SFT, then PPO on realised returns) teach an LLM agent to forecast returns from numeric market data?

## Data and period
499 US equities; 3,807 training tasks (Feb 2011–Dec 2023) and 398 test tasks (Feb 2024–Mar 2026), 240 scored; horizons 1–126 days (Table 2, p. 5).

## Method
Agent queries nine point-in-time tools (candles, indicators, rankings, market context) then submits a log-return forecast; score = direction × magnitude agreement (pp. 3–4). Qwen3-4B → SFT on outcome-conditioned GPT-5.4 demonstrations → PPO (p. 6).

## Baselines and validation
Historical median, momentum-20, momentum extrapolation, GBM classifier; nine frontier LLMs (Table 3, p. 5). Chronological split with label realisation before the first test decision (p. 4). No significance tests or trading costs.

## Results (with page or section references)
- Momentum extrapolation scores 42.00, above seven of nine frontier LLMs (p. 5).
- AURA-4B: 20.94 → 43.31; directional accuracy only 62.9 → 65.4 (p. 1).
- GBM has the best direction (85.8%) but low magnitude (p. 6).
- Frontier scores fall sharply from Feb 2024–Jul 2025 to Aug 2025–Mar 2026: glm-5.3 60.94 → 23.43; claude-fable-5 54.76 → 20.02; momentum 41.99 → 42.01 (Table 7, p. 17).

## Limits and risks to validity
_My assessment:_ tasks are selected using realised outcomes (both train and test), so the benchmark is not a random sample of market states (pp. 4, 15). Frontier models were likely trained on much of the early test window; their later-period collapse is consistent with memorisation, though the paper does not test it. Small scored set (240, of which 71 in the later period); no costs or tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Momentum, GBM, median; no plain RW |
| Point-in-time and leakage controls | 1 | Tools point-in-time; frontier-model contamination not controlled |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | 499 stocks, ~2 years |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Not stated in the part I read |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "The resulting benchmark is an outcome-selected collection rather than a random sample" (p. 4)
