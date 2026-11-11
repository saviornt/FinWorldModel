---
type: lit-note
title: "Measuring Deep Learning Performance - An Empirical Study of Performance Distributions Across Architectures and Tasks"
authors: [Kevin L Coakley, Odd Erik Gundersen]
year: 2026
venue: arXiv (cs.LG) 2610.38037
source_url: https://arxiv.org/abs/2610.38037
doi: 10.1038/s41598-026-49656-z
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.4, RQ4.7]
family: [evaluation]
evidence: Moderate
score: 8
tags: [lit-note, family/evaluation, training, reproducibility, seeds]
---
# Measuring Deep Learning Performance Distributions (Coakley & Gundersen, 2026)

**Basis:** Full text (pp. 1, 3, 7–10, 12–13, 24, 28–29, 35, 45–46) via the alphaXiv PDF reader, read 2026-11-08. Not financial data; time-series forecasting results are taken as transferable.

**Takeaway:** Over 18,600 runs (100 seeds per configuration), time-series forecasting performance across seeds is often non-Gaussian and has about three times more underperforming outliers than image classification; early stopping gives the best balance of mean and robustness, and a few seeds cannot characterise the distribution.

## Problem
How robust deep learning performance is to seed-level non-determinism, and whether this differs by architecture, size, training length and task (§3.1).

## Data and period
Time series: ETTh1, ETTh2, ETTm1, ETTm2, Traffic, Weather; horizons 96–720. Images: CIFAR-10/100, Oxford Flowers, UC Merced (§3.2).

## Method
186 experiments × 100 seed replicates with deterministic training (PyTorch deterministic algorithms, fixed cuBLAS workspace, containers); NLinear, TSMixer, Autoformer, iTransformer; ResNet and ViT. Robustness = spread (range, s.d.), skewness, Tukey-fence outliers (§3.2–3.3, App. A.3).

## Baselines and validation
Original authors' splits and hyperparameters; NLinear as linear model; Shapiro–Wilk with W effect size; binomial tests with Holm–Bonferroni (§4.1).

## Results (with page or section references)
- 59 of 94 time-series MAE distributions non-Gaussian; 37 of the 39 substantively non-Gaussian (W < 0.95) cases are time series (p. 13).
- Underperforming outliers per replicate: 2.83 for time series vs 1.0 for images (Holm-adjusted p = 4.7×10⁻⁵) (p. 24).
- Time-series models often reach peak robustness early and degrade with more training; early stopping balances mean performance and robustness (§5.1, p. 24; p. 29).
- Typical practice of 3–10 seeds gives an incomplete picture of the distribution, especially its tails (p. 8).

## Limits and risks to validity
_My assessment:_ benchmarks are not financial and are higher-signal than returns; only seed variation is studied (hyperparameter and preprocessing variation excluded, p. 29). Transfers as a measurement rule: report a distribution over many seeds, with tail statistics, and use early stopping.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard benchmark splits |
| Baselines | 1 | NLinear linear model |
| Point-in-time and leakage controls | N/A | Methods study |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Six time-series datasets, non-financial |
| Statistical testing | 2 | Tests with Holm–Bonferroni |
| Reproducibility | 1 | Deterministic setup documented; code release not stated in pages read |
| **Total** | 6/10 → **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "model performance is best understood as a distribution rather than a fixed value" (p. 29)

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
