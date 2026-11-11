---
type: lit-note
title: "Understanding the Implicit Biases of Design Choices for Time Series Foundation Models"
authors: [Annan Yu, Danielle C. Maddix, Boran Han, Xiyuan Zhang, Abdul Fatir Ansari, Oleksandr Shchur, Christos Faloutsos, Andrew Gordon Wilson, Michael W. Mahoney, Yuyang Wang]
year: 2025
venue: arXiv
source_url: https://arxiv.org/abs/2510.19236
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10, RQ1.13]
family: [price-time-series]
evidence: Weak
score: 2
tags: [lit-note, family/price-time-series, tokenization]
---
# Understanding the Implicit Biases of Design Choices for Time Series Foundation Models (Yu, 2025)

**Basis:** PDF pages 1–4, 7–10, 12, 22 (v1). Section 4 details and appendices beyond p. 22 not read.

**Takeaway:** Controlled Chronos (quantised input, cross-entropy) vs Chronos-Bolt (continuous input, quantile loss) comparisons show tokenisation is a trade-off, not a free gain: quantised embeddings favour local detail, small scales and dampen outliers; continuous embeddings preserve geometry but let large values dominate; cross-entropy regresses less to the mean than L1/L2 losses.

## Problem
Explain how patch size, embedding type (discrete vs continuous) and loss shape the behaviour of time-series foundation models (§1, pp. 1–3).

## Data and period
Mostly synthetic signals (multi-scale, multi-offset, sinusoids with outliers, chaotic systems) plus Chronos training data for some diagnostics (§§2–5).

## Method
Theory plus controlled runs; a Chronos-Bolt with patch size 1 was pretrained to compare embeddings without the patching effect (§3, p. 7).

## Baselines and validation
Chronos vs Chronos-Bolt, with TimesFM and Moirai in some panels; 30 repeats in the outlier study (Fig. 8, p. 12). No statistical tests.

## Results (with page or section references)
- Quantised embeddings make nearby values look more distinct and learn fine-scale patterns better: at scale ratio 40, relative error on the small-scale component 1.556 for Chronos vs 2.679 Chronos-Bolt and 3.201 TimesFM (Fig. 5c, p. 9).
- Continuous ReLU embeddings weight large-magnitude values more (norm bias); near-zero patterns are harder to learn (Fig. 6, pp. 9–10).
- L2/L1 losses regress to the mean/median under uncertainty; cross-entropy can commit to a mode (§4, p. 10).
- Outliers: quantisation damps limited outliers; large outliers dominate continuous embeddings; but cross-entropy sometimes forecasts an outlier, so Chronos has higher variance (§5, p. 12).
- Motivation: Chronos-Bolt replaced quantisation and cross-entropy to improve benchmarks, yet Chronos does better on chaotic systems (p. 4).

## Limits and risks to validity
_My assessment:_ mechanism study on synthetic data; no financial series. Relevant because returns are heavy-tailed, multi-scale and noisy, which is where these biases bite.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out synthetic forecasts |
| Baselines | 0 | Model-vs-model only |
| Point-in-time and leakage controls | 0 | Not applicable/not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Synthetic + some real data |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Not stated in the pages read |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "Quantization dampens outliers." (Fig. 1, p. 2)
- "Cross-entropy favors outlier forecasts." (Fig. 1, p. 2)
