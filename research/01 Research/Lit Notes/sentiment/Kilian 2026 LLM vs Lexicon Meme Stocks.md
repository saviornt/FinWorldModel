---
type: lit-note
title: "LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks"
authors: [Paul Kilian, Markus Kleffmann]
year: 2026
venue: arXiv 2607.24072
source_url: https://arxiv.org/abs/2607.24072
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3, RQ1.5]
family: [sentiment]
evidence: Weak
score: 2
tags: [lit-note, family/sentiment]
---
# LLM vs Lexicon Sentiment for Meme Stocks (Kilian, 2026)

**Basis:** v1, full text via alphaXiv, pp. 1–10.

**Takeaway:** On r/WallStreetBets posts about GME, AMC and NOK, VADER carries no next-day signal (AUC ≈ 0.48–0.57); a multi-dimensional Gemini indicator does slightly better but is asset-specific, partly contemporaneous, and its tail-event warnings are weak.

## Problem
Does LLM-extracted, multi-dimensional sentiment from Reddit beat a lexicon for next-day returns and extreme up-moves?

## Data and period
623,360 WSB posts and comments (Kaggle and Figshare), Nov 2020–May 2022; yfinance daily closes (pp. 2–3, Table 1).

## Method
VADER compound (plain and Reddit-score weighted) vs Gemini 2.5 Flash-Lite outputs (sentiment, bullishness, sarcasm, relevance) combined into an index (LMI). OLS on next-day returns, ROC-AUC, ±5-day lead/lag, quantile-threshold tail warnings (pp. 3–7).

## Baselines and validation
VADER only; all in-sample; calendar-day aggregation without an exchange-time cutoff (p. 8).

## Results (with page or section references)
- VADER: p > 0.58 and R² ≤ 0.003 for all six specs; AUC 0.48–0.57 (Table 2, p. 6).
- LMI: significant only for AMC (negative sign, R² = 0.083); AUC 0.51–0.53 (Table 3, p. 6).
- Tail warnings: AMC precision 20% vs 8.3% base rate, recall 24%; GME 9.4% vs 7.6%; NOK recall 52% but precision 8.8% vs 6.3% (Table 4, p. 7).

## Limits and risks to validity
_Authors:_ three stocks, no human labels, no multiple-testing or serial-correlation correction, posts after the close may leak into "next-day" (p. 8). _My assessment:_ Gemini used on pre-cutoff 2020–22 posts. Treat as an idea, not evidence.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | VADER |
| Point-in-time and leakage controls | 0 | No time cutoff; pre-cutoff LLM |
| Costs and realism | N/A | No trading |
| Sample breadth | 0 | Three stocks, one episode |
| Statistical testing | 1 | Basic tests, no correction |
| Reproducibility | 0 | Prompt given; no code |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "increased linguistic expressiveness does not necessarily translate into stable forecasting performance" (abstract, p. 1)
