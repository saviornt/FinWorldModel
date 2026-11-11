---
type: lit-note
title: "Bridging the Gap Between Natural Language and Market Dynamics via High-Dimensional Representation Learning"
authors: [Yujin Jeong, Noelle Jung, Brian Y. C. Leung]
year: 2026
venue: arXiv 2605.30652
source_url: https://arxiv.org/abs/2605.30652
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.14]
family: [sentiment]
evidence: Weak
score: 5
tags: [lit-note, family/sentiment]
---
# Bridging the Gap Between Natural Language and Market Dynamics via High-Dimensional Representation Learning (Jeong, 2026)

**Basis:** v1 (28 May 2026), full text via alphaXiv (pp. 1–8).

**Takeaway:** On five mega-cap stocks (FNSPID), feeding a price Transformer daily mean-pooled frozen FinBERT embeddings cut price-level MSE by 17% against a scalar FinBERT sentiment score, and a small contrastive (Siamese) projection cut it further, but none of the variants had directional skill (~50%) or beat buy-and-hold.

## Problem
Does replacing a scalar sentiment score with a dense text embedding improve a sequence model's forecasts?

## Data and period
FNSPID news summaries and daily prices for GOOG, MSFT, NVDA, AAPL, AMZN; 37,707 records, chronological 80/20 split; news coverage only 7.3% of days (pp. 1–2). Exact dates of the split not given.

## Method
50-day window of Open, Close, Volume plus text input, 4-layer Transformer predicting the close 3 days ahead (p. 2). Text variants: FinBERT probabilities mapped to a 1–5 score with exponential decay imputation; daily mean of frozen 768-d FinBERT embeddings (forward-filled); unfreezing FinBERT; a Siamese MLP (768→256→64) trained with contrastive loss on tercile bins of next-open return, on news from other stocks; attention pooling with a learnable stock query (pp. 2–4).

## Baselines and validation
Same Transformer and an LSTM without text (Table 4–5, p. 3). One chronological split. Min-max scaling per stock and partition after the authors found global scaling leaked (p. 4). No random-walk, GBT or significance tests.

## Results (with page or section references)
- Transformer: no text MSE 0.244; scalar sentiment 0.199 (−18%); frozen FinBERT embedding 0.165 (−17% vs scalar); Siamese 64-d embedding 0.078; attention pooling 0.199 (worse than mean pooling); unfrozen FinBERT abandoned after one epoch (7.7M trainable parameters, ~50 min per epoch on a T4) (Tables 5–9, pp. 3–5).
- LSTM: adding the scalar score made MSE worse (0.172 → 0.223) (Table 7, p. 4).
- Siamese pair classifier ROC AUC ~0.505–0.509, i.e. near chance (p. 4).
- Directional accuracy ~50%; no variant beat buy-and-hold in a long/cash backtest (p. 5, Fig. 3).

## Limits and risks to validity
_My assessment:_ the target is the min-max-scaled price level, so MSE and R² mainly reward persistence; a random walk is not reported and could match these numbers. Single split, five survivors, no tests, no costs. The Siamese gain sits alongside near-chance pair AUC and near-chance direction, so it is not evidence of usable signal. Positive for one design point: dense embeddings were cheaper to use frozen and better than a scalar; end-to-end fine-tuning was costly.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Price-only Transformer/LSTM; no RW or GBT |
| Point-in-time and leakage controls | 1 | Per-partition scaling; FinBERT period not discussed |
| Costs and realism | 0 | None |
| Sample breadth | 1 | Five stocks |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code (GitHub) |
| **Total** | **5/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "none were able to outperform a passive buy-and-hold benchmark" (p. 5)
