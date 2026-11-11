---
type: lit-note
title: "Decision by Supervised Learning with Deep Ensembles: A Practical Framework for Robust Portfolio Optimization"
authors: [Juhyeong Kim, Sungyoon Choi, Youngbin Lee, Yejin Kim, Yongmin Choi, Yongjae Lee]
year: 2025
venue: CIKM 2025; arXiv 2503.13544 (v7)
source_url: https://arxiv.org/abs/2503.13544
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.4]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation, training, ensembling]
---
# Decision by Supervised Learning with Deep Ensembles (Kim et al., 2025)

**Basis:** Full text (pp. 1–5, 7) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** Averaging portfolio weights over many independently seeded networks steadily raises median return and Sharpe and narrows their spread as ensemble size grows from 1 to 64; but in the survivorship-safer rolling NASDAQ 100 and S&P 500 universes the ensembled models only roughly match equal- and value-weighted benchmarks.

## Problem
End-to-end portfolio learning with non-convex objectives is unstable; can a convex surrogate (cross-entropy to a pre-computed max-Sharpe/Sortino portfolio) plus deep ensembles stabilise it (§1)?

## Data and period
US stocks; six static universes (e.g. Large Cap 24 stocks, High Dividend 84, NASDAQ/S&P Top 30 by current membership) and two rolling universes (NASDAQ 100, S&P 500, membership updated monthly); data Jan 2010–May 2025; backtest from Nov 2019 (§4.1–4.2).

## Method
Mamba, LSTM, Transformer predict portfolio weights from 21 days of OHLCV transforms; monthly retraining, 100 epochs, best validation epoch; DSL averages weights over 100 independent runs; ensemble-size study bootstraps from 1,000 trained models (§3.3, §4.1, §4.4).

## Baselines and validation
Equal-weighted, value-weighted, mSSRM, prediction-focused and end-to-end learning (reported as averages over 100 runs). Two-day trading lag, 0.4% cost per trade; no significance tests (§4.2).

## Results (with page or section references)
- Rolling S&P 500: VW Sharpe 0.45, EW 0.39; best DSL 0.47 (MSO, Mamba) and 0.45 (MSH, Transformer); rolling NASDAQ 100: VW 0.58, mSSRM 0.82, best DSL 0.49 (Table 3).
- Static Top-30 universes show large DSL gains (e.g. S&P Top 30 cumulative return 10.14 vs VW 4.83) (Table 2) — these universes use current constituents.
- Ensemble size 1 → 64: median cumulative return, Sharpe and Sortino rise and interquartile ranges narrow (Fig. 3, §4.4).
- DSL can act like a high-beta strategy and lose its edge in range-bound or falling universes (§5).

## Limits and risks to validity
_My assessment:_ the headline gains sit in static universes picked with hindsight; in rolling universes the method roughly ties simple weights. The ensemble-size result is the transferable part: seed averaging cuts decision variance, which matters more for weights and trades than for loss.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Monthly rolling retraining |
| Baselines | 2 | EW, VW, mSSRM |
| Point-in-time and leakage controls | 1 | Trading lag; rolling universes; static ones survivorship-biased |
| Costs and realism | 1 | Flat 0.4% per trade |
| Sample breadth | 2 | Up to S&P 500 rolling, 2019–2025 incl. COVID |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code public; data not shared |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "DSL can behave as a high-beta strategy" (§5)
