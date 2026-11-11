---
type: lit-note
title: "FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting"
authors: [Jaehoon Lee, Jun Seo, Seunghan Lee, Junhyeok Kang, Sangjun Han, Stefan Zohren, Lukasz Szpruch, Wonbin Ahn]
year: 2026
venue: arXiv (under review, ICLR 2027)
source_url: https://arxiv.org/abs/2608.03259
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.13, RQ1.1, RQ4.8]
family: [evaluation]
evidence: Moderate
score: 6
tags: [lit-note, family/evaluation, foundation-models, benchmark]
---
# FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting (Lee, 2026)

**Basis:** alphaXiv PDF pages 1, 3–4, 6, 8–10, 14, 25 (v3). LG AI Research with UCL, J.P. Morgan, Oxford, others (author list abridged in properties; first eight of many listed).

**Takeaway:** Across 43 zero-shot TSFMs on 60K US-centred financial series from 2020, rankings agree only moderately with GIFT-Eval (r=0.43) and very weakly on portfolio outcomes (rank correlation with MASE 0.09); model size does not predict rank, and no family wins across categories.

## Problem
Do generic forecasting benchmarks pick the models that work for financial decisions (direction, ranking, portfolios)? (pp. 1, 3)

## Data and period
116,897 series, 171.1M observations, 13 categories (equities, ETFs, FX, commodities, crypto, rates, macro, fundamentals, news sentiment); 60,232 evaluation targets, 13.6M observations from 1 Jan 2020 (§3.1, p. 4; Table, p. 14).

## Method
Zero-shot evaluation of 43 public TSFMs (TimesFM, Chronos, Chronos-Bolt, Chronos-2, Moirai, Timer-S1, Toto, TiRex, TTM, Sundial and others) with point (hit ratio, RelMAE vs naive), cross-sectional (IC) and portfolio metrics; rank aggregation by geometric mean (§3.2, p. 4; §4.1, p. 6). The decoder-only transformer is described as the dominant TSFM paradigm (p. 3).

## Baselines and validation
RelMAE against persistence, plus seasonal naive, seasonal mean, random walk with drift and lookback mean (App. E.3, p. 25). No GBT, GARCH or HAR. Authors cannot rule out evaluation-period data in pretraining (p. 6).

## Results (with page or section references)
- FinVerse vs GIFT-Eval rank agreement r=0.43 (p. 1); rank correlation of MASE with portfolio metrics 0.09, with IC 0.48 (Fig. 6, p. 25).
- Best overall: Reverso Small, then Chronos-2 Synth; leaders differ by category (Table 3, p. 8).
- Many models have RelMAE_ori ≥ 1, i.e. no better than persistence on average; best 0.981 (Reverso Small) (Table 4, p. 9).
- Timer-S1 (8.3B MoE decoder) ranks mid-table; model size and FinVerse rank show no clear relation (Fig. 5, p. 25).

## Limits and risks to validity
_Authors (pp. 9–10):_ no transaction costs or turnover; strict point-in-time consistency not ensured; US-heavy.
_My assessment:_ possible pretraining contamination makes "zero-shot" claims optimistic; no significance tests. Still the broadest finance check of TSFM families, and it shows token-based or decoder-only models have no systematic edge.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Post-2020 evaluation; contamination possible |
| Baselines | 1 | Persistence, drift, seasonal naive; no GBT/GARCH |
| Point-in-time and leakage controls | 1 | Acknowledged, partly addressed |
| Costs and realism | 0 | Ignored |
| Sample breadth | 2 | Many asset classes, 2020–2026 incl. stress |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code in supplement; data on acceptance |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "generic forecasting benchmarks do not fully capture the aspects of forecast quality that matter" (p. 1)
