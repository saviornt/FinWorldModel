---
type: lit-note
title: "When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting"
authors: [Taizhen Cheung]
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2607.12248
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.13, RQ1.1, RQ4.9]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation, foundation-models, negative-result]
---
# When Directional Accuracy Lies: LoRA-Adapted TimesFM on Equities (Cheung, 2026)

**Basis:** alphaXiv PDF pages 1–11 (v2). Hunter College (student project; single author).

**Takeaway:** With walk-forward folds, held-out tickers and an always-up base rate, LoRA-adapted and zero-shot TimesFM (a decoder-only TSFM) show no directional skill on S&P 500 or NASDAQ-100 at any horizon; an earlier "~80% accuracy" was the bull-market base rate; the 5% quantile covers ~44% of outcomes.

## Problem
Does a fine-tuned decoder-only TSFM have directional skill on equities once the up-trend base rate is accounted for? (pp. 1–2)

## Data and period
Daily adjusted closes 2005–2026; NASDAQ-100 (100 stocks) and S&P 500 (501 stocks + 11 SPDR ETFs); ~80/20 seen/held-out tickers per sector; current-membership snapshot (survivorship acknowledged) (Table 1, p. 3).

## Method
google/timesfm-2.5-200m with LoRA (rank 32), context 512, horizon 128, MSE + 0.3·directional loss; pooled vs per-sector adapters (Table 3, §5.5, p. 4). Normalisation fit only on pre-target history (§5.3, p. 4).

## Baselines and validation
Zero-shot TimesFM, always-up, random walk, persistence, AR(1); three expanding walk-forward folds with test windows 2020–2022, 2022–2024, 2024–2026; McNemar, Diebold–Mariano, block bootstrap, Benjamini–Hochberg FDR (§5.1, §5.7, pp. 3–5). Pre-registered per-sector test.

## Results (with page or section references)
- Excess accuracy over always-up on held-out stocks spans zero at all horizons; at h=128, −0.081 (NASDAQ pooled) and −0.017 (S&P pooled); zero-shot −0.151 and −0.125 (Table 5, p. 6).
- Legacy condition: base rate 0.704 vs model 0.626 at h=128 (Table 4, p. 5).
- Per-sector adapters significantly worse than pooled (DM +5.12, p<.001, fold 0, h=128) (Table 6, p. 7).
- LoRA lowers MAE vs zero-shot (S&P 15.15 vs 16.31) but not vs always-up (15.56) (Table 7, p. 8).
- Tail calibration: nominal 0.05 quantile has ~0.44 empirical coverage (pooled 0.440, zero-shot 0.408 on S&P) (§6.5, p. 8).

## Limits and risks to validity
_Author (p. 10):_ low power at h=128; survivorship; single seed; non-overlapping windows; equities only.
_My assessment:_ single-author student work, but the protocol is the most careful equity test of a decoder-only TSFM read so far. No GBT or GARCH baseline; costs not modelled.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward plus held-out tickers |
| Baselines | 1 | RW, persistence, AR(1), always-up; no GBT/GARCH |
| Point-in-time and leakage controls | 1 | Pre-target normalisation; survivorship not fixed |
| Costs and realism | 0 | No costs |
| Sample breadth | 2 | ~600 stocks, three test periods incl. 2022 |
| Statistical testing | 2 | DM, McNemar, BH FDR |
| Reproducibility | 1 | Seeded, versioned pipeline; release not confirmed |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "High raw accuracy is not skill." (Fig. 2 caption, p. 7)
