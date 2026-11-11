---
type: lit-note
title: "XForecast: The KDD 2026 Finance Day Challenge on News-Grounded Financial Forecasting"
authors: [Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, Yongjae Lee, Wonbin Ahn]
year: 2026
venue: "arXiv (cs.LG)"
source_url: https://arxiv.org/abs/2610.16131
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.7, RQ4.3]
family: [fusion]
evidence: Weak
score: 5
tags: [lit-note, family/fusion]
---
# XForecast: The KDD 2026 Finance Day Challenge on News-Grounded Financial Forecasting (Lee et al., 2026)

**Basis:** arXiv v1 (12 Oct 2026), pp. 1–6, via the alphaXiv PDF reader.

**Takeaway:** A Kaggle competition (100 US large caps, train 2019–2022, test 2023, four-week direction) that required text embeddings; inspected top solutions were ensembles that pooled cross-sectional signals and compressed text into small auxiliary features (projected embeddings, embedding novelty), with tree models as competitive as deep ones — but the paper reports no text-off ablation, and its metric weights test cases by news agreement with the realised move.

## Problem
Provide a standard benchmark for news-grounded stock forecasting (p. 1).

## Data and period
Top-100 US stocks by market cap continuously tradable 2019–2023; text generated with FinTexTS (macro, sector, related-company, company levels); text only as precomputed embeddings from six allowed models (pp. 1, 3).

## Method
Predict close four weeks ahead using data up to t − 4 weeks; weighted hit rate where each instance's weight is the share of GPT-tagged atomic news statements whose direction matches the realised move (pp. 3–4).

## Baselines and validation
No baseline table in the pages read; submissions using price only were excluded from ranking (p. 4). 341 submissions, 51 teams (p. 4).

## Results (with page or section references)
- Five inspected high-ranking solutions: mostly ensembles; separated market direction from stock-specific parts; pooled same-date cross-sectional information; text turned into compact auxiliary signals before fusion with momentum and volatility features; deep and tree models both competitive (p. 4).
- Organisers stress precise temporal constraints, clear text-use policies and reproducible runtimes (p. 5).

## Limits and risks to validity
_My assessment:_ the weight construction uses the realised future direction, so the metric rewards models on cases where news "turned out right" — a hindsight-weighted score that inflates apparent text value. No price-only reference score. Universe selected as survivors (continuously tradable 2019–2023). One test year.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One temporal split |
| Baselines | 0 | None reported |
| Point-in-time and leakage controls | 1 | t − 4 weeks rule; survivor universe; hindsight-weighted metric |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 100 stocks, one test year |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Reproducible Kaggle notebooks required; data on Kaggle |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "both deep architectures and tree-based models remained competitive" (p. 4)
