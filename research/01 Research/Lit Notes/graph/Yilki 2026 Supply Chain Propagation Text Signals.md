---
type: lit-note
title: "Supply Chain Propagation of Textual Signals: LLM Embeddings and Cross-Sectional Return Predictability"
authors: [Asef Yılkı]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2606.29290
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.4, RQ1.2]
family: [graph]
evidence: Weak
score: 5
tags: [lit-note, family/graph]
---
# Supply Chain Propagation of Textual Signals (Yılkı, 2026)

**Basis:** pp. 1–3, 6–8, 10–15, 19–21, 26–28 read through alphaXiv page excerpts (pp. 22–25 tables not returned).

**Takeaway:** Averaging FinBERT 10-K embeddings over supply-chain neighbours makes one embedding component a stronger monthly return predictor (Newey–West t −2.64; long–short Sharpe 0.86 gross, 0.67 net), but the hand-built graph has only 48 firms and 51 edges and is static, so the result is fragile.

## Problem
Do supply-chain links carry textual (10-K MD&A) information into partner firms' prices, beyond each firm's own text?

## Data and period
255 S&P 500 firms, 2,365 10-K MD&A filings, monthly returns from Yahoo Finance, 2011–2025 (24,723 firm-months, 155 cross-sections). Supply-chain knowledge graph: 48 nodes, 51 directed edges, manually curated from filings and reports, weighted by estimated revenue dependence and input specificity (pp. 3, 8, 11).

## Method
FinBERT mean-pooled 768-d embeddings, PCA to 10 components; network-augmented embedding = (1−α)·own + α·weighted mean of upstream suppliers (α = 0.4), then PCA; Fama–MacBeth regressions with Newey–West errors; quintile long–short (pp. 12–15, 19–21).

## Baselines and validation
Direct embedding factors; controls for momentum, reversal, volatility and log price (no book-to-market, profitability or investment; no customer-momentum control) (p. 10). Out-of-sample tests split at 2018 and 2020; 100-run edge-shuffle placebo (pp. 8, 26).

## Results (with page or section references)
- net_pc_5 NW t −2.60 alone, −2.64 with controls; direct pc_5 t −2.12, insignificant once net_pc_5 is added (Table 2, pp. 20–21).
- Long–short on net_pc_5: 10.9% a year, Sharpe 0.86 gross, 0.67 after 20 bps round trip; FF5 alpha 7.27% (t 2.30); direct factor Sharpe 0.56 gross, 0.34 net (pp. 1, 21).
- Out-of-sample t −2.54 (2018 split) and −1.96 (2020 split); placebo p = 0.000; strongest in mid-size firms and 2017–2021 (p. 26).

## Limits and risks to validity
Author states: small manual graph, price-only controls, static graph, FinBERT not chronologically consistent (pp. 27–28). _My assessment:_ the predictor is the 5th of 10 PCs, picked from the same sample, and its t-stat is below the Harvey–Liu–Zhu 3.0 hurdle the paper itself cites (p. 6); a graph built today from current documents can encode relationships that were not known at each date; current constituents give survivorship bias; the reported firm-month return range (−6.2% to +8.35%, Table 1, p. 12) is implausibly narrow for 2011–2025 and suggests a data-processing problem. No code or data release was found in the pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Two split-date holdouts |
| Baselines | 1 | Own-text factors and price controls |
| Point-in-time and leakage controls | 0 | Static hand-built graph, current constituents |
| Costs and realism | 1 | Flat 20 bps |
| Sample breadth | 1 | 255 firms, but graph covers 48 |
| Statistical testing | 1 | NW t-stats, placebo; no multiple-testing correction |
| Reproducibility | 0 | Not stated |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "The baseline KG contains 48 nodes and 51 directed edges" (p. 11)
