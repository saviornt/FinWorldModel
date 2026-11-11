---
type: lit-note
title: "Sentiment trading with large language models"
authors: [Kemal Kirtac, Guido Germano]
year: 2024
venue: Finance Research Letters 62, 105227 (arXiv 2412.19245)
source_url: https://arxiv.org/abs/2412.19245
doi: 10.1016/j.frl.2024.105227
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.3, RQ1.14]
family: [sentiment]
evidence: Weak
score: 6
tags: [lit-note, family/sentiment]
---
# Sentiment Trading with LLMs (Kirtac, 2024)

**Basis:** journal version via alphaXiv, pp. 1–7.

**Takeaway:** Fine-tuned OPT (2.7B) beats BERT, FinBERT and the Loughran–McDonald dictionary on Refinitiv news (L-S Sharpe 3.05 vs 2.07 FinBERT vs 1.23 LM after 10 bps), but the random split and pre-cutoff LLM make the size of the edge unreliable.

## Problem
Do LLM sentiment scores predict next-day US stock returns better than FinBERT and a finance dictionary?

## Data and period
965,375 unique Refinitiv articles on 6,214 US firms, Jan 2010–Jun 2023; CRSP daily returns; near-duplicates (cosine ≥ 0.8) removed (pp. 3, Table 1).

## Method
BERT (345M) and OPT (2.7B) fine-tuned with labels = sign of 3-day excess return from publication; FinBERT and LM used off the shelf. Panel regressions of next-day return on scores with firm and date fixed effects; value-weighted top/bottom 20% long–short portfolios, rebalanced daily, trades timed to news release (pp. 4–5).

## Baselines and validation
Random 20% test and 20% validation split of articles (p. 4). Baselines: LM dictionary, BERT, FinBERT, equal- and value-weighted market. 10 bps cost per trade (p. 5).

## Results (with page or section references)
- Direction accuracy over 3 days: OPT 74.4%, BERT 72.5%, FinBERT 72.2%, LM 50.1% (Table 3, p. 5).
- Next-day regression: OPT 0.274 (t = 5.37), FinBERT 0.257 (t = 5.12), BERT 0.142 (t = 2.63), LM 0.083 (t = 1.87, n.s.) (Table 4, p. 6).
- L-S Sharpe after 10 bps: OPT 3.05, BERT 2.11, FinBERT 2.07, LM 1.23; VW market 1.45 (Table 5, p. 6).
- Aug 2021–Jul 2023 cumulative: OPT L-S 355%, BERT 235%, FinBERT 165%, LM 0.91% (Fig. 1, p. 7).

## Limits and risks to validity
_My assessment:_ the labels are future 3-day returns, and the test set is a random draw from the same 2010–2023 period, so the model trains on news from days after test articles; the 74% "accuracy" is partly a same-period fit. OPT and BERT were pre-trained on web text overlapping the sample, with no memorisation control (rubric cap). Flat 10 bps on daily-rebalanced portfolios is light. Descriptive stats look odd (mean daily return 0.37% with SD 0.18%, Table 2), which suggests reporting errors. No code.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One random split, not time-ordered |
| Baselines | 1 | Dictionary, BERT/FinBERT, market; no price-only model |
| Point-in-time and leakage controls | 0 | Random split; pre-cutoff LLM |
| Costs and realism | 1 | Flat 10 bps |
| Sample breadth | 2 | All US stocks with news, 2010–2023 incl. 2020 |
| Statistical testing | 1 | Clustered t-stats, no correction |
| Reproducibility | 0 | No code or data |
| **Total** | **6/14** | Moderate → capped Weak (pre-cutoff LLM, no memorisation control) |

## Quotes worth keeping (each under 15 words, with page)
- "a transaction cost of 10 basis points for each trade" (p. 5)
