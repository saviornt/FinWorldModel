---
type: lit-note
title: 'JEL: Applying End-to-End Neural Entity Linking in JPMorgan Chase'
authors:
- Wanying Ding
- Vinay K. Chaudhri
- Naren Chittar
- Krishna Konakanchi
year: 2021
venue: AAAI 2021 (IAAI); arXiv:2411.02695
source_url: https://arxiv.org/abs/2411.02695
doi: 10.1609/aaai.v35i17.17796
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.2
- RQ3.8
family:
- cleaning
evidence: Weak
score: 4
tags:
- lit-note
- family/cleaning
- entity-linking
---
# JEL: Applying End-to-End Neural Entity Linking in JPMorgan Chase (Ding et al., 2021)

**Basis:** arXiv 2411.02695v1 read in full via alphaXiv on 2026-11-08 (pp. 1–8).

**Takeaway:** For linking company names in news to an internal knowledge graph, a model that combines character n-grams with short-context semantics beat string matching, classifiers and a Wikipedia-style neural linker (F1 0.999 vs 0.88 for tri-gram cosine), but the test set excluded the hardest, mid-similarity name pairs, so the scores overstate real accuracy.

## Problem
Wikipedia-based entity linkers miss most companies of financial interest and need rich context; how to link news mentions to an enterprise knowledge graph?

## Data and period
586,975 labelled mention–entity pairs from financial news (spaCy ORG mentions) against JPMorgan's knowledge graph; random 80/10/10 split (p. 5).

## Method
Wide (linear Siamese on character n-grams after suffix normalisation) plus deep (two short LSTMs with attention on context) model with contrastive loss (pp. 3–4).

## Baselines and validation
Bi/tri-gram cosine, Jaccard/cosine context, LR, SVM, SVM-Rank, end-to-end neural EL (ENEL) (p. 5, Table 1).

## Results (with page or section references)
- F1: JEL 0.999, SVM-Rank 0.965, tri-gram cosine 0.877, ENEL 0.866; context-only methods 0.55–0.66 (Table 1).
- Name normalisation matters: suffix standardisation and n-grams fix cases like "Salarius Pharm LLC" (p. 6).
- Pure string matching fails when different firms share a name (p. 2).

## Limits and risks to validity
Labels were built partly from string similarity, and pairs with similarity 0.5–0.75 were discarded as too hard (p. 5), so the test set is easy. Internal data; no time dimension (renames and mergers not tested). No effect on any forecasting task.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Random split |
| Baselines | 2 | String, classifier, ranking and neural baselines |
| Point-in-time and leakage controls | N/A | Not a forecasting study |
| Costs and realism | N/A | |
| Sample breadth | 0 | One internal dataset; hard cases removed |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Internal data and code |
| **Total** | 3/10 → **4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
