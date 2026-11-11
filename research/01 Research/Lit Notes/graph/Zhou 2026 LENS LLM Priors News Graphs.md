---
type: lit-note
title: "LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs"
authors: [Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb]
year: 2026
venue: CIKM 2026 (arXiv)
source_url: https://arxiv.org/abs/2611.04217
doi: 10.1145/3799682.3840912
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ1.4, RQ1.2, RQ1.11, RQ3.7]
family: [graph]
evidence: Weak
score: 5
tags: [lit-note, family/graph]
---
# LENS: LLM-Extracted Priors and News-Driven Graphs (Zhou, 2026)

**Basis:** pp. 1–3, 6, 9–10 read through alphaXiv page excerpts (main results Table 1 not returned).

**Takeaway:** A company graph extracted by o3-mini (five runs, reliability-weighted) beats GICS, WikiData and news co-occurrence graphs inside the same GNN (top-5 Sharpe 1.87 vs 1.37–1.42), and a news-similarity graph adds more; but the test is five bullish quarters (Oct 2023–Dec 2024) with no costs.

## Problem
Can treating relation reliability as a signal improve static (LLM-extracted) and dynamic (news) graphs for stock ranking?

## Data and period
S&P 500 (450 stocks) and NASDAQ 100 (87), constituents fixed 2023-09-30 and filtered to full data over the horizon; Thomson Reuters News Archive headlines embedded with Voyage-3-large; 5 rolling folds, ~7 years train, 3-month validation, 3-month test (p. 6).

## Method
Static graph: o3-mini (knowledge cutoff 2023-10-01) prompted for 14 relation types, 5 runs, edge weight = frequency × confidence; dynamic graph: decayed daily headline embeddings, mutual top-k; gated fusion; RankNet loss (pp. 2–3, 6).

## Baselines and validation
o3-mini direct, FinGPT, MLP, ALSTM, Transformer, StockMixer, RSR-I, RTGCN, GERU, MASTER, COGRASP (p. 6). Human check of 120 extracted triples: 91.1% relaxed precision, Fleiss κ 0.58 (p. 2).

## Results (with page or section references)
- Static graph source (AR@5 / SR@5): LLM Highrecall 0.523 / 1.87; GICS 0.372 / 1.39; WikiData 0.365 / 1.42; news co-occurrence 0.358 / 1.37 (p. 9).
- Removing reliability weights: 0.465 / 1.71; single extraction run: 0.334 / 1.28 (p. 9).
- No dynamic graph: SR@5 1.09; price-correlation dynamic graph 1.46 (Table 5, p. 9).
- Gated fusion narrows the low- vs high-news-coverage MAE gap from 5.39% to 3.18% (Table 7, p. 10).

## Limits and risks to validity
Authors state: one LLM extractor, US large caps, bullish regime, backtest only (p. 10). _My assessment:_ the universe is filtered on complete data through the test period (survivorship); an LLM may still encode post-cutoff knowledge despite the prompt; no costs or significance tests; MRR differences are tiny (0.031–0.037).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling quarterly folds |
| Baselines | 1 | Many deep/graph baselines; no GBT |
| Point-in-time and leakage controls | 1 | LLM cutoff before test; survivorship filter |
| Costs and realism | 0 | None |
| Sample breadth | 1 | Two US universes, one regime |
| Statistical testing | 0 | Seed averages only |
| Reproducibility | 0 | Not stated; licensed news |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "treat every extracted edge as a trustworthy binary fact" (p. 1)
