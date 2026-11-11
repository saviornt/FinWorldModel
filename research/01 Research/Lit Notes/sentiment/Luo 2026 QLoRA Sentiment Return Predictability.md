---
type: lit-note
title: "From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models"
authors: [Fusheng Luo]
year: 2026
venue: arXiv 2608.04200
source_url: https://arxiv.org/abs/2608.04200
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3]
family: [sentiment]
evidence: Weak
score: 6
tags: [lit-note, family/sentiment]
---
# QLoRA Sentiment vs Return Predictability (Luo, 2026)

**Basis:** v1, page excerpts via alphaXiv (pp. 1, 7, 9, 11, 13–15).

**Takeaway:** QLoRA-tuned 7–8B LLMs classify financial sentiment far better (macro-F1 0.86–0.88) than FinBERT (0.68), but on 2019 Benzinga headlines FinBERT has the best one-day rank IC (0.0143), the signal turns negative from day 2, and none of 28 model–horizon tests survives Newey–West plus FDR.

## Problem
Does a more accurate sentiment classifier give a more useful cross-sectional return signal?

## Data and period
Exp. 1: unified 3-class benchmark from five labelled datasets (test n = 5,033). Exp. 2: 10,637 unique Benzinga headlines, 13,115 headline–stock observations, fixed S&P 100 (72 firms with news), calendar 2019 (pp. 1, 9).

## Method
TF-IDF Naive Bayes; FinBERT and Financial-RoBERTa checkpoints; zero-shot Qwen2.5-7B; QLoRA Qwen2.5-7B, LLaMA3-8B, Mistral-7B (4-bit, r = 16). Score = p(pos) − p(neg), averaged per stock-day; returns from next session open, horizons 1, 2, 3, 5 days; daily rank IC; equal-weight top/bottom 15% portfolios (pp. 7, 9).

## Baselines and validation
Fixed train/val/test for Exp. 1; Exp. 2 is a temporally separate year. Newey–West and Benjamini–Hochberg FDR over 28 tests. Gross returns only.

## Results (with page or section references)
- Macro-F1: Mistral QLoRA 0.877, LLaMA3 QLoRA 0.875, Qwen QLoRA 0.862, zero-shot Qwen 0.727, FinBERT 0.675, NB 0.633 (Table 6, p. 9).
- One-day rank IC: FinBERT 0.0143, Financial-RoBERTa 0.0141, NB 0.0141, Qwen QLoRA 0.0083, LLaMA3 QLoRA 0.0013; all negative at 2 and 5 days (Fig. 5a, p. 14).
- Minimum FDR-adjusted q = 0.96; nothing significant (p. 11).
- One-day gross L-S: FinBERT 12.96% (Sharpe 1.11), Qwen QLoRA −2.35% (Table 11, p. 13).

## Limits and risks to validity
_Authors:_ one year, one large-cap universe, uneven coverage; models released after 2019 may have seen the headlines; daily aggregation may miss intraday reaction (p. 15). _My assessment:_ low power; next-open entry is the right timing for a tradable test.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Separate year, one split |
| Baselines | 1 | NB, FinBERT; no price-only model |
| Point-in-time and leakage controls | 1 | Next-open alignment; contamination acknowledged, not tested |
| Costs and realism | 0 | Gross only |
| Sample breadth | 1 | S&P 100, one year |
| Statistical testing | 2 | Newey–West + FDR |
| Reproducibility | 0 | No code or data stated |
| **Total** | **6/14** | Moderate → capped Weak (LLMs used on pre-cutoff 2019 news) |

## Quotes worth keeping (each under 15 words, with page)
- "None of the 28 model–horizon tests remains significant" (abstract, p. 1)
