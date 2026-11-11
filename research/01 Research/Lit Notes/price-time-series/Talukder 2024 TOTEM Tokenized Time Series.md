---
type: lit-note
title: "TOTEM: TOkenized Time Series EMbeddings for General Time Series Analysis"
authors: [Sabera Talukder, Yisong Yue, Georgia Gkioxari]
year: 2024
venue: Transactions on Machine Learning Research (arXiv 2402.16412)
source_url: https://arxiv.org/abs/2402.16412
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, tokenization]
---
# TOTEM: TOkenized Time Series EMbeddings (Talukder, 2024)

**Basis:** PDF pages 1–2, 4–5, 10–12, 25–26, 28, 32–33 (v2).

**Takeaway:** A VQ-VAE codebook (256 codes, 4× compression) learned on many domains, with the forecaster held fixed, beats the same model fed continuous patches in every regime (e.g. 78.6% vs 23.2% win share in-domain generalist), with the biggest margins zero-shot.

## Problem
Can one discrete, self-supervised tokenizer serve many domains and tasks (imputation, anomaly detection, forecasting)? (§1, pp. 1–2)

## Data and period
Weather, Electricity, Traffic, ETT (4 sets) for training; zero-shot on five further datasets (§5.3; Table 21, p. 25). No finance.

## Method
1D strided CNN encoder, K-codeword codebook, CNN decoder, RevIN normalisation; univariate temporal tokens only; Transformer forecaster over tokens (§3.2–3.4, pp. 4–5).

## Baselines and validation
14 forecasting baselines from prior work; key ablation fixes the architecture and swaps tokens for patches ("PatchTOTEM") with Transformer and MLP forecasters (§6, pp. 10–11). Seeded runs, mean ± sd; win-share metric, no tests.

## Results (with page or section references)
- Tokens vs patches, same architecture: 67.9% vs 39.3% (specialist), 78.6% vs 23.2% (generalist in-domain), 67.5% vs 35.0% (zero-shot) average wins (§6, p. 11; Table 21, p. 25).
- With an MLP forecaster: 66.1% vs 37.5% (p. 11).
- Codebook 32 → 256 → 512 lowers reconstruction MSE 0.0451 → 0.0192 → 0.0184 (Table 21D, p. 25).
- Generalist training on diverse data beats larger single-domain training zero-shot (§6, p. 12).

## Limits and risks to validity
_My assessment:_ per-dataset differences are small (often third decimal of MSE); win-share counts ties loosely; no naive baseline; no finance. Contradicts VAIOM's finance result in direction (see RP1 §RQ1.10).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard splits and zero-shot sets |
| Baselines | 1 | Many deep baselines; no naive |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 12 datasets, no finance |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code public |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "discrete tokens outperform patches" (§1, p. 2)
