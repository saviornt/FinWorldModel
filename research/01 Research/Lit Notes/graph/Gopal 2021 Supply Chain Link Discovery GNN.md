---
type: lit-note
title: "Discovering Supply Chain Links with Augmented Intelligence"
authors: [Achintya Gopal, Chunho Chang]
year: 2021
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2111.01878
doi: 10.48550/arXiv.2111.01878
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.7]
family: [graph]
evidence: Moderate
score: 6
tags: [lit-note, family/graph, supply-chain, link-prediction]
---
# Discovering Supply Chain Links with Augmented Intelligence (Gopal, 2021)

**Basis:** arXiv 2111.01878v1 pages 1, 3–7, 10, 13–17 read via alphaXiv on 2026-11-08.

**Takeaway:** A GAT trained on Bloomberg's supply-chain graph plus firm features ranks likely unseen customers; known-graph structure is the biggest input (Hit@20 22% → 40%), and analysts found public evidence for 21% of sampled predictions (39% for US suppliers), showing commercial supply-chain graphs are far from complete.

## Problem
Predict supplier–customer links not yet recorded in a curated database.

## Data and period
Bloomberg supply-chain dataset (historical years) plus industry, revenue segments, facilities, financials, raw materials, descriptions, competitors (p. 3).

## Method
Inductive GAT per edge type, multi-hop, dot-product scoring, two-step hard-negative training (pp. 3–4). Validation edges removed from training "across all years" to avoid leakage (p. 5).

## Baselines and validation
Feature-only baseline; Mean rank, Recall@100, Hit@20; human analyst check of 180 predictions (p. 5–6).

## Results (with page or section references)
- Hit@20: baseline 16%, + graph 40%, final 45% (Table 2, p. 5).
- Analysts confirmed 37 of 180 (21%); US suppliers 39% (Table 3, p. 6).
- Weakest for Financials and Real Estate (Tables 4–5, p. 14).

## Limits and risks to validity
Proprietary data; edge split random not time-based; no return test; recall metrics are lower bounds because true links are unknown.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out edges |
| Baselines | 1 | Feature-only model |
| Point-in-time and leakage controls | 1 | Edges removed across years; not time-split |
| Costs and realism | N/A | |
| Sample breadth | 2 | Global multi-industry graph |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Proprietary |
| **Total** | 5/12 → 6/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
