---
type: lit-note
title: "Towards Neural Scaling Laws for Time Series Foundation Models"
authors: [Qingren Yao, Chao-Han Huck Yang, Renhe Jiang, Yuxuan Liang, Ming Jin, Shirui Pan]
year: 2025
venue: ICLR 2025
source_url: https://arxiv.org/abs/2410.12360
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.13, RQ1.10]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, scaling]
---
# Towards Neural Scaling Laws for Time Series Foundation Models (Yao, 2025)

**Basis:** alphaXiv PDF pages 1–4, 6–8, 10–11, 20, 27 (v3).

**Takeaway:** On 17B general time points, encoder-only and decoder-only TSFMs follow similar power laws in parameters, compute and data, in- and out-of-distribution; the token-based Chronos-T5 design shows very small NLL scaling exponents and its gains do not carry over to OOD data.

## Problem
Do TSFM scaling laws hold out of distribution, and how does architecture affect scalability? (pp. 1–2)

## Data and period
Pretraining corpus from LOTSA: ~16.8B time points, 39 datasets, 7 domains (no finance), SNR > 20 dB filter; subsets of 10M, 100M, 1B points (§2.1, Table 1, pp. 2–3). OOD tests: long-sequence benchmark (ETT, electricity, weather) and a Monash subset including M4 hourly/daily/weekly finance series (Table 3, p. 20).

## Method
Patch-embedded encoder-only and decoder-only transformers with RoPE and Student-t mixture heads, ~10^3 to ~10^8 parameters; Moirai and Chronos-T5 retrained on the same corpus as case studies (§2.2, pp. 3–4; §3.2, pp. 7–8).

## Baselines and validation
Architectures compared with each other; 95/5 ID split; OOD on unseen datasets with non-overlapping rolling windows (App. C.2, p. 20). No classical baselines.

## Results (with page or section references)
- NLL follows power laws in parameters, compute and data, both ID and OOD; MAPE improves more OOD than ID with scale (§3.1, p. 6).
- Encoder-only shows "a slight advantage" in parameter scaling ID; compute and data scaling nearly identical across the two architectures (Fig. 5, p. 7).
- Chronos-T5 "exhibits power laws with very small exponents" in NLL, attributed to discrete probability prediction not being distance-sensitive; on OOD data the decoder-only transformer performs better (p. 8).
- Design rule: doubling pretraining data reduces OOD MAPE to ~90% and ID MAPE to ~97% (p. 8). Larger models are more sample-efficient; some OOD tasks show emergent jumps (p. 10).

## Limits and risks to validity
_Authors:_ univariate only; context length and horizon not studied (§2.3, p. 4; §6.2, p. 10).
_My assessment:_ the corpus is filtered for high SNR, the opposite of returns; finance appears only as M4 series. Transfer of these exponents to low-SNR market data is untested.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | ID hold-out plus unseen OOD datasets |
| Baselines | 1 | Architecture comparisons; no classical models |
| Point-in-time and leakage controls | N/A | Not a market study |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Many domains, little finance |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code released (GitHub) |
| **Total** | **4/10 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the design improvements in Chronos-T5 enhance ID time series forecasting" but not OOD (p. 8)
