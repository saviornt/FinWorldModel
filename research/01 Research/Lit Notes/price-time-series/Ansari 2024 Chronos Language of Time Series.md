---
type: lit-note
title: "Chronos: Learning the Language of Time Series"
authors: [Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix, Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael Bohlke-Schneider, Yuyang Wang]
year: 2024
venue: Transactions on Machine Learning Research (arXiv 2403.07815)
source_url: https://arxiv.org/abs/2403.07815
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10, RQ1.13]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series, tokenization]
---
# Chronos: Learning the Language of Time Series (Ansari, 2024)

**Basis:** PDF pages read via alphaXiv: pp. 1–2, 4–5, 9, 18–19, 37, 43 (v3). Benchmark tables other than Table 10 and the vocabulary-size ablation (§5.6) were not in the pages I read.

**Takeaway:** Mean scaling plus 4,094 uniform bins turns any series into tokens that an unmodified T5 can model with cross-entropy; it is competitive zero-shot on 27 unseen datasets, but the bins cap the representable range and lose precision.

## Problem
Can a language model with no time-series-specific design forecast real values if they are turned into tokens? (§1, p. 2)

## Data and period
Training: 28 datasets (~890K series, ~84B observations) plus TSMixup augmentation and KernelSynth synthetic Gaussian-process series. Evaluation: Benchmark I (15 in-domain datasets) and Benchmark II (27 zero-shot datasets); test set = last H observations of each series (§5.1, p. 9). Finance content limited to datasets such as Exchange Rate and FRED-MD (Table 10, p. 37).

## Method
Mean scaling by the context's mean absolute value, then uniform quantisation into bins on [−15, +15] with vocabulary 4,096 (incl. PAD and EOS); T5 models 20M–710M and a GPT-2 decoder trained by cross-entropy; forecasts by sampling token paths autoregressively (§3.1, p. 5; §5.2, p. 9; Fig. 1, p. 2).

## Baselines and validation
Naive, Seasonal Naive, AutoETS, AutoARIMA, AutoTheta, SCUM ensemble; task-specific deep models (PatchTST, DeepAR, TFT, N-BEATS, N-HiTS, DLinear, WaveNet, GPT4TS); other pretrained models (LLMTime, Lag-Llama, Moirai, ForecastPFN) (§5.3, p. 9; Table 10, p. 37). One held-out final window per series; 3 seeds for Chronos and task-specific models (Table 10 caption).

## Results (with page or section references)
- Benchmark II (zero-shot) aggregate relative MASE: Chronos-T5 Large 0.823; PatchTST 0.810; N-BEATS 0.835; AutoETS 0.838; Seasonal Naive 1.000 (Table 10, p. 37). Token model is in the top group, not clearly ahead of continuous-input deep models.
- Exchange Rate (only FX set): Chronos-T5 Large MASE 2.375 vs Naive 1.874, AutoARIMA 1.740, Moirai-Base 1.507 (Table 10, p. 37) — worse than a random walk on the one finance-like dataset.
- Limits of tokenisation: values outside [−15s, 15s] cannot be represented (sparse spikes); if scale is large relative to variance, nearby values share a token, losing precision (§5.7, pp. 18–19; Fig. 16).
- Cross-entropy is not distance-aware but the model learns distributions over neighbouring tokens, including multimodal ones (Fig. 15, p. 18).
- v3 fixed an off-by-one decoding error that had made Chronos look worse and changed the vocabulary-size conclusion (App. F, p. 43).

## Limits and risks to validity
_My assessment:_ not a finance study; one final-window split; no significance tests; the one FX dataset favours a random walk. The tokenizer limits (range cap, precision loss) are directly relevant to heavy-tailed returns. Training corpus overlap with Benchmark I is by design; Benchmark II is the fair test.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Last-window holdout; zero-shot datasets |
| Baselines | 2 | Naive (random walk), seasonal naive, ETS/ARIMA/SCUM, deep models |
| Point-in-time and leakage controls | 1 | Zero-shot datasets excluded from training |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | 42 datasets, little finance, no stress test |
| Statistical testing | 0 | Aggregated scores, 3 seeds, no tests |
| Reproducibility | 2 | Code, weights and datasets public |
| **Total** | **7/12 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "making it theoretically infeasible to model time series with a strong trend" (§3.1, p. 5)
