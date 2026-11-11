---
type: lit-note
title: "Pre-training Time Series Models with Stock Data Customization"
authors: [Mengyu Wang, Tiejun Ma, Shay B. Cohen]
year: 2025
venue: KDD 2025
source_url: https://arxiv.org/abs/2506.16746
doi: 10.1145/3711896.3737005
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, pretraining-objective]
---
# Wang 2025 SSPT Stock-Customised Pretraining Tasks (Wang, Ma & Cohen, 2025)

**Takeaway:** Three stock-specific pretext tasks (identify the stock, identify its sector, predict masked moving averages) improved top-5 stock selection over training from scratch; predicting masked moving averages beat predicting masked raw values (Sharpe 1.97 vs 1.54), but the tasks conflicted when trained together and the result was sensitive to loss weights.

## Problem
Whether pretraining objectives tailored to stock data help stock selection more than masked-value prediction borrowed from other domains.

## Data and period
NASDAQ, NYSE, FTSE-100 (2013–2017), TOPIX-100 (2016–2020), NASDAQ-recent (2018–2022, includes COVID). Daily OHLCV plus 5/10/20/30-day moving averages; min-max normalisation on training statistics only (§5.1).

## Method
Two-layer transformer (SSPT). Pretext tasks: stock code classification (SCC), sector classification (SSC), and moving-average prediction after masking (MAP). Combined loss α·SCC + β·SSC + γ·MAP (Eq. 4). Fine-tuning freezes early layers and trains a return head with regression plus pairwise ranking loss (Eq. 5).

## Baselines and validation
Chronological 3-year train, 1-year validation, 1-year test per dataset (§5.1). Classification, regression, RL and ranking baselines on the three benchmark datasets; market (buy-all) baseline on all five (§6.3). Top-5 daily strategy; IRR and Sharpe, no costs.

## Results (with page or section references)
- Each task trained alone reaches a better pretext score than when combined; equal-weight combination degrades every task, "indicating conflicts between different training objectives" (Table 1, §6.2).
- Increasing the MAP weight γ "significantly harms the classification tasks"; two of three combinations including MAP are worse than no pretraining; γ = 10 works but γ = 5 does not, so the authors call MAP's inclusion not robust (§6.2, Fig. 6).
- Recommended robust recipe: SCC + SSC with equal weights (§6.2).
- MAP vs masked value prediction on NASDAQ: IRR 0.59 vs 0.53, Sharpe 1.97 vs 1.54 (Table 4, App. C).
- Mask rate 0.05 underperforms no pretraining; benefits start at 0.15, best near 0.3 (Fig. 9).
- SSPT beats market and baselines on Sharpe across datasets (Tables 2–3).

## Limits and risks to validity
_My assessment:_ one-year test windows; no transaction costs; fixed constituent lists (survivorship not discussed); hyperparameters and loss weights chosen on validation from a wide grid with no trial-count correction; no GBT baseline; no significance tests. Results for task combinations come from NASDAQ only.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split per dataset |
| Baselines | 1 | Many deep baselines and market; no random walk or GBT |
| Point-in-time and leakage controls | 1 | Train-only normalisation; universe survivorship not addressed |
| Costs and realism | 0 | Ignored |
| Sample breadth | 2 | Four markets, two periods incl. COVID |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code released |
| **Total** | 6/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "MAP is not an optimal component for combined pre-training" (§6.2)
