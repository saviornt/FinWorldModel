---
type: lit-note
title: "Foundation vs. Specialized Models: Evaluating Catastrophic Forgetting in Continual Time Series Forecasting"
authors: [Nouha Karaouli, Denis Coquenet, Elisa Fromont, Martial Mermillod, Marina Reyboz]
year: 2025
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2510.00809
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.9]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, adaptation, continual-learning, forgetting, non-finance]
---
# Catastrophic Forgetting in Continual TSFM Fine-Tuning (Karaouli et al., 2025)

**Basis:** alphaXiv PDF pages 1–15 (v3, 26 Jun 2026). Univ. Rennes / Grenoble / CEA. Energy and synthetic data; cited for method points.

**Takeaway:** Sequentially fine-tuning TimesFM-2.0, Chronos-2, Chronos-small or a 100k-parameter SAMformer on four tasks always causes forgetting (larger models forget less); replaying stored past inputs and predictions (Dark Experience Replay) removes most of it and lets the small model match the foundation models on real energy data.

## Problem
How much do time-series foundation models forget earlier tasks when fine-tuned in sequence, compared with a small specialised model, and does replay fix it? (§1)

## Data and period
Synthetic sequence of four spectrally different series; real sequence of four daily French energy series 2021–2025 (residential load, photovoltaic, wind; plus one private household so at least one task cannot be in TSFM pretraining) (§3.1).

## Method
Task-incremental continual learning: independent, offline (all at once), cumulative, sequential and DER training; RMSE and backward transfer (BWT); a model-aware cross-series transferability (CST) ratio to anticipate forgetting (§3).

## Baselines and validation
Zero-shot TSFMs and SAMformer from scratch; chronological windows per task; results averaged (seeds not reported in the pages read) (§3.2, §4).

## Results (with page or section references)
- All models forget under sequential fine-tuning; synthetic average BWT: SAMformer 2.04, Chronos-base 1.54, Chronos-small 0.93, TimesFM 0.77 (Table 1).
- Real energy sequence BWT: SAMformer 0.45, Chronos-small 0.52, Chronos-base 0.33, TimesFM 0.25 (Table 2).
- DER cuts forgetting everywhere: SAMformer synthetic BWT 2.04 → 0.15; TimesFM energy 0.25 → −0.03; Chronos-base energy average RMSE 1.44 with DER vs 1.48 cumulative and 1.56 offline (Tables 1–2, §4.3).
- Cumulative training (all data so far) beats sequential for all models (§4.2).
- CST predicts which task switches cause forgetting; DTW similarity does not (§4.1).

## Limits and risks to validity
_Authors:_ the scenario is designed to induce forgetting; a related study found the opposite on milder shifts (§2.3).
_My assessment:_ not financial; four tasks per scenario; no significance tests or seed spread reported in pages read; forgetting of earlier *tasks* is a proxy for forgetting earlier *regimes*.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Chronological per-task splits, sequential protocol |
| Baselines | 1 | Zero-shot, small model, cumulative/offline training |
| Point-in-time and leakage controls | 1 | Private series to avoid pretraining contamination |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Synthetic + one energy domain |
| Statistical testing | 0 | None reported |
| Reproducibility | 1 | Public data (Enedis, Zenodo); code not confirmed |
| **Total** | 5/12 → **6/14** | Moderate (non-finance) |

## Quotes worth keeping (each under 15 words, with page)
- "fine-tuning improves new task accuracy, it consistently triggers forgetting" (abstract, p. 1)
