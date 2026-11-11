---
type: lit-note
title: "DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting"
authors: [Wentao Zhao, Hongqiang Wu, Shanghang Liu, Zhaochen Zan, Yu Zhang, Biqing Huang]
year: 2026
venue: arXiv 2609.38197
source_url: https://arxiv.org/abs/2609.38197
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14, RQ1.10]
family: [fusion]
evidence: Weak
score: 3
tags: [lit-note, family/fusion]
---
# DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting (Zhao, 2026)

**Basis:** v1 (18 Sep 2026), page excerpts via alphaXiv (pp. 1–5, 7, 10). The news-ablation table (Table 5) was not in the pages returned.

**Takeaway:** Price tokens (one learned scale "summary" token plus three residual-VQ shape tokens per log-return patch) were added to a frozen Qwen3-8B; a toggleable LoRA "slow path" that reads causally timestamped news and revises the fast price-only forecast cut daily SP500 MAPE at H = 64 from 15.26% to 9.80%, but that gain mixes news with SFT and RL revision, and the slow path costs ~16× the fast path's latency.

## Problem
How can price tokens and news tokens share one autoregressive sequence without losing either numeric accuracy or text reading?

## Data and period
Zero-shot evaluation on MTBench (5-minute US equities, price-only), SP500 and HS300 (daily), energy (weekly); periods not in the pages read (p. 7).

## Method
Log returns, RevIN per patch; shape tokens via residual VQ with a frequency-equalising rebalance (AFE-RVQ); scale token from a learned codebook over (μ, log σ); frozen Qwen3-8B with only new token embeddings and heads trained (fast path); LoRA reviser conditioned on prices, news with timestamps ≤ forecast origin and the fast forecast, trained by SFT then GRPO with a return-space reward; 48.9M trainable parameters (0.60%) (pp. 2–5).

## Baselines and validation
Chronos-2, TimesFM-2.5, Timer, Time-MoE, Moirai-2.0, ChatTime, Aurora, Qwen3 prompted with text (Table 3, p. 7). No random walk, no significance tests, no costs.

## Results (with page or section references)
- Slow path lowest MAPE in 8 of 12 settings; e.g. SP500 H = 64: 9.80% vs Chronos-2 11.12% (Table 3, p. 7).
- Fast → SFT → Slow on identical windows: SP500 H = 64 15.26 → 14.03 → 9.80; HS300 18.06 → 12.43 → 9.19 (Table 4, p. 7). The fast price-token path alone is worse than Chronos-2 on daily equities.
- Prompting Qwen3-8B with prices and news as text: SP500 MAPE 25.7–31.2% (p. 7).
- Latency: fast 0.37 s per window, slow 5.85 s (p. 7).
- Authors say news gains vary by market and are clearest for energy (abstract; p. 10).

## Limits and risks to validity
_My assessment:_ an actual LLM backbone (out of the project's no-LLM scope; kept as the clearest example of the interleaved-token design); evaluation dates vs Qwen3's training cutoff are not given, so memorisation of news–outcome pairs cannot be ruled out; MAPE on price levels without a random walk; RL reward uses realised returns, which is fine for training but makes test-period hygiene critical.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out zero-shot sets; split dates not given |
| Baselines | 1 | TSFMs; no RW or GBT |
| Point-in-time and leakage controls | 0 | News timestamps ≤ origin, but LLM cutoff not addressed |
| Costs and realism | 0 | None |
| Sample breadth | 1 | Several markets and frequencies |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Not stated |
| **Total** | **3/14 → Weak** | LLM cutoff not controlled (rubric cap would apply) |

## Quotes worth keeping (each under 15 words, with page)
- "text helps where it carries information beyond the price path" (Fig. 5, p. 10)
