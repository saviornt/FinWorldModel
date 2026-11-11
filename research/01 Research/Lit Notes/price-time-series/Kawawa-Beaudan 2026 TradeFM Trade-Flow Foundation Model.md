---
type: lit-note
title: "TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure"
authors: [Maxime Kawawa-Beaudan, Srijan Sood, Kassiani Papasotiriou, Daniel Borrajo, Manuela Veloso]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2602.23784
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.13, RQ1.10]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, autoregressive, scaling, microstructure]
---
# TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure (Kawawa-Beaudan, 2026)

**Basis:** alphaXiv PDF pages 1–2, 4, 8–10, 12–14, 18–19, 23–24, 27 (v1). J.P. Morgan AI Research.

**Takeaway:** A 524M decoder-only model on tokenized trade events from >9K US equities reproduces stylized facts in closed-loop rollouts and has 2–3× lower return-distribution distance than a Compound Hawkes baseline; test loss follows power laws in compute (α≈0.18) and data (α≈0.19). It is evaluated on realism, not on forecasting returns.

## Problem
Can one generative model learn transferable market mechanics from partially observed, multi-asset order flow, without asset-specific calibration? (pp. 1–2)

## Data and period
Proprietary tick-level US equity transactions, 368 trading days, Feb 2024–Sep 2025, >19B tokens; temporal hold-out from Jan 2025 (10.7B train, 8.7B test tokens); tokenizer calibrated on Feb 2024 only; Jan 2025 Japan and China held out for OOD (§5.1, p. 4; Table 6, p. 24).

## Method
Events (Δt, price depth in bps, volume, action, side) mapped by scale-invariant features into one discrete token; Llama-style decoder (32 layers, 1,024 dim, GQA, RoPE), 524.4M parameters, 4 epochs (pp. 18–19). Closed-loop rollouts with a deterministic price-time-priority simulator; multinomial sampling with repetition penalty 1.2 (§8.2, p. 8). Models at 125M, 250M and 500M for scaling (Table 5, p. 18; App. C, p. 23).

## Baselines and validation
Calibrated zero-intelligence agent and Compound Hawkes process, both through the same simulator (p. 8; App. B.6–B.7, p. 23). 10 rollouts of 1,024 events for 9 assets × 3 liquidity tiers × 9 held-out months (§9.1, p. 8).

## Results (with page or section references)
- Log-return K-S distance at 10–120 s: TradeFM 0.013–0.043 vs Hawkes 0.039–0.101 vs ZI 0.376–0.439 (Table 2, p. 9).
- Order-flow fidelity: lowest distance on most quantities; Hawkes better on bid-ask spread K-S (0.218 vs 0.238) (Table 3, p. 10).
- Rollouts show near-zero return autocorrelation, slowly decaying absolute-return autocorrelation, heavy tails and aggregational Gaussianity (Fig. 4, p. 9).
- Distance metrics stable over the 9 held-out months; moderate perplexity degradation on Japan/China (pp. 10, 24).
- Scaling: L(C) ∝ C^−0.18, L(D) ∝ D^−0.19 on the minimum-loss frontier, three sizes, repeated data included (App. C, p. 23).

## Limits and risks to validity
_Authors:_ closed-loop evaluation couples model and simulator quality; full disentanglement is future work (p. 10).
_My assessment:_ no forecasting target (returns, volatility) and no comparison against a continuous-input generator; scaling fit uses only three sizes and multi-epoch data; proprietary data; no significance tests. Rollouts are only 1,024 events (minutes for liquid names), so long-horizon error compounding is untested.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Temporal hold-out (2025) plus APAC OOD |
| Baselines | 1 | ZI and Compound Hawkes; no neural or continuous baseline |
| Point-in-time and leakage controls | 1 | Tokenizer calibrated on first training month; temporal split |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | >9K equities, 9 held-out months, three geographies |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Proprietary data; code not released |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Rather than relying on next-token perplexity, we evaluate TradeFM by its ability to reproduce" stylized facts (p. 8)
