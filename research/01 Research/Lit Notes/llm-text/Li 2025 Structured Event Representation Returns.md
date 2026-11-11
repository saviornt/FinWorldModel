---
type: lit-note
title: "Structured Event Representation and Stock Return Predictability"
authors: [Gang Li, Dandan Qiao, Mingxuan Zheng]
year: 2025
venue: arXiv 2512.19484
source_url: https://arxiv.org/abs/2512.19484
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.2, RQ1.14]
family: [llm-text]
evidence: Weak
score: 6
tags: [lit-note, family/llm-text]
---
# Structured Event Representation and Stock Return Predictability (Li, 2025)

**Basis:** v1 (22 Dec 2025), page excerpts via alphaXiv (pp. 1–4, 8–12, 15, 22, 29, 36, 59, 61, Online Appendix pp. 1–8).

**Takeaway:** LLM-extracted subject–action–object event triplets fed to an attention model beat sentiment and embedding baselines for daily and weekly cross-sectional returns, but the extractor (GPT-3.5-turbo-0125) was run on 2003–2023 news that is mostly inside its training window, with no memorisation control.

## Problem
Do structured LLM event features predict returns better than sentiment or embeddings?

## Data and period
ProQuest and Factiva news 2003–2023; 301,409 firm-days, 4,355 stocks, 6.2 million events; evaluation 2008–2022 (pp. 22, 59; OA p. 1).

## Method
GPT-3.5-turbo extracts event triplets with DBpedia links; TransE embeddings; attention aggregation; MLP to returns; rolling six-year windows (pp. 9–15, 22).

## Baselines and validation
Loughran–McDonald, RavenPack, BERT, FinBERT (Table 2, p. 59). Rolling windows. No price-only baseline; no costs.

## Results (with page or section references)
- Daily long–short: annualised return 10.93%, Sharpe 0.78 vs FinBERT 8.59%, 0.61 (Table 2, p. 59).
- Fama–MacBeth coefficient on SER forecast 0.222 (t = 2.90); sentiment and embedding baselines insignificant (Table 4, p. 61).

## Limits and risks to validity
_My assessment:_ the LLM's knowledge cutoff falls inside the evaluation period and no masking or post-cutoff test is reported, so the rubric cap applies. Gross returns only; event extraction quality checked on samples only.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling windows |
| Baselines | 1 | Text baselines only |
| Point-in-time and leakage controls | 0 | Pre-cutoff LLM, no control |
| Costs and realism | 0 | None |
| Sample breadth | 2 | 4,355 stocks, 2008–2022 |
| Statistical testing | 1 | HAC t-stats |
| Reproducibility | 0 | None |
| **Total** | **6/14 → capped Weak** | Rubric cap: LLM used before its cutoff without memorisation control |

## Quotes worth keeping (each under 15 words, with page)
- "highlight the crucial benefit of structured model inputs" (abstract, p. 1)
