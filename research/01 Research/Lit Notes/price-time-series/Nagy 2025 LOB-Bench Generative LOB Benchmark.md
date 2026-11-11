---
type: lit-note
title: "LOB-Bench: Benchmarking Generative AI for Finance – an Application to Limit Order Book Data"
authors: [Peer Nagy, Sascha Frey, Kang Li, Bidipta Sarkar, Svitlana Vyetrenko, Stefan Zohren, Anisoara Calinescu, Jakob Foerster]
year: 2025
venue: ICML 2025
source_url: https://arxiv.org/abs/2502.09172
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.13, RQ1.10]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, autoregressive, rollout, microstructure]
---
# LOB-Bench: Benchmarking Generative AI for Finance (Nagy, 2025)

**Basis:** alphaXiv PDF pages 1–3, 6–8, 10–11, 21 (v2). Oxford-Man Institute, University of Oxford, J.P. Morgan AI Research.

**Takeaway:** In a distributional benchmark of generated order-book message streams, the token-level autoregressive state-space model (LOBS5, 35M) beats a parametric model, a CGAN and BPE-tokenized RWKV models, but all models show "derailment": distribution errors grow with rollout length, fastest for the RWKV models, whose impact curves diverge.

## Problem
Next-token cross-entropy on held-out data does not measure behaviour under autoregressive sampling, where errors accumulate; a quantitative realism benchmark is needed (p. 2).

## Data and period
LOBSTER message data for Alphabet (GOOG) and Intel (INTC); LOBS5 trained on all of 2022 and tested on a January 2023 sub-sample; Coletta CGAN trained on three days of Jan 2019 (p. 7).

## Method
Aggregator functions map LOB sequences to 1-D statistics (spread, imbalance, inter-arrival, volumes, OFI, etc.); L1 and Wasserstein distances between real and generated histograms; conditional scores, including conditioning on the rollout step to measure divergence; discriminator score; price-response (impact) curves; downstream mid-price-trend MLP trained with and without generated data (§4–5, pp. 2, 6–7).

## Baselines and validation
Cont et al. (2010) parametric model, Coletta CGAN, RWKV-4/6 (170M, off-the-shelf BPE tokenizer), LOBS5 (token-level S5) (p. 7). 99% bootstrapped CIs (Fig. 4, p. 7).

## Results (with page or section references)
- LOBS5 has the lowest overall L1/Wasserstein scores (Fig. 4, p. 7).
- Error divergence: "increasing errors across all models", fastest for RWKV (p. 8); L1 divergence vs horizon attributed to "snowballing errors caused by teacher forcing" (Fig. 18, p. 21).
- Impact curves: mean L1 distance ΔR = 2.45 (LOBS5) vs 126 (RWKV-6); Coletta and RWKV curves "quickly diverge due to error accumulation" (p. 8).
- Discriminator ROC 0.83 for LOBS5 on GOOG; ~1 for the baseline (p. 6).
- Adding generated data to the downstream classifier does not help; for Coletta it reduces precision and recall; no significant effect at longer horizons for baseline or LOBS5 (p. 8).

## Limits and risks to validity
_My assessment:_ two stocks, one test month; realism metrics, not forecasting; the token-level model wins on generation fidelity, but generic BPE tokenization of the same data (RWKV) does worst, so tokenizer design matters as much as the AR objective. Synthetic data did not improve a downstream predictor.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Train 2022, test Jan 2023 |
| Baselines | 1 | Parametric, CGAN, RWKV |
| Point-in-time and leakage controls | N/A | Generation benchmark |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 0 | Two stocks, one month |
| Statistical testing | 1 | Bootstrapped CIs |
| Reproducibility | 2 | Code and generated data released |
| **Total** | **5/10 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "error accumulation can cause distribution shifts." (p. 2)
