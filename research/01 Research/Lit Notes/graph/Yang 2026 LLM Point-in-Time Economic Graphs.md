---
type: lit-note
title: "LLM Latent Edge Measurement: Point-in-Time Economic Graphs for Quantitative Investing from Corporate Disclosures"
authors: [Fan Yang, Lin Zhang]
year: 2026
venue: arXiv (stat.AP)
source_url: https://arxiv.org/abs/2607.15640
doi: 10.48550/arXiv.2607.15640
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.7]
family: [graph]
evidence: Moderate
score: 7
tags: [lit-note, family/graph, time-valid-graph, filings]
---
# LLM Point-in-Time Economic Graphs from Disclosures (Yang, 2026)

**Basis:** arXiv 2607.15640v1 full PDF (pp. 1–9) read via alphaXiv on 2026-11-08.

**Takeaway:** An LLM pipeline reading each firm's latest 10-K/20-F builds a directed, weighted firm graph stamped with each filing date; 88% of audited edges with weight ≥ 0.1 were confirmed, errors sat in the low-weight tail, and 28% of disclosed exposures named only a category ("third-party foundries") and could not become edges; edges from the model's own background knowledge are not point-in-time and must be dropped for backtests (cutting edges 149 → 109).

## Problem
Can unstructured disclosures be turned into a calibrated, point-in-time adjacency matrix?

## Data and period
42 Nasdaq-100 firms; most recent annual filings (filed 2025-07 to 2026-05) (p. 4).

## Method
Filing agents quote verbatim evidence; knowledge agents give priors; latent counterparties ("one customer, 17% of revenue") resolved but flagged; logit-pooled fusion; IDF down-weighting of ubiquitous counterparties (TSMC, Samsung); double-sided relative threshold (pp. 3–4).

## Baselines and validation
Adversarial audit of 30 stratified edges; comparison with GICS; component ablations (pp. 5–7).

## Results (with page or section references)
- 149 edges; audit 23 confirmed, 4 plausible, 3 refuted, all refuted below weight 0.1 (Table 2, p. 5).
- 70.5% of edges within GICS sector vs 37.3% random (lift 1.9); 44 cross-sector edges such as power-purchase agreements (p. 5–6).
- Filing-only and knowledge-only graphs overlap at Jaccard 0.435; without IDF, spurious hub edges appear; an absolute threshold isolates peripheral firms (p. 6–7, Table 4).
- Knowledge-channel edges inherit the LLM's training cutoff, so cannot be rebuilt for past dates (p. 7).

## Limits and risks to validity
One snapshot, 42 firms; no return test; the auditor is also an LLM; reading truncation lost some disclosures (p. 7).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Measurement study |
| Baselines | 1 | GICS comparison, ablations |
| Point-in-time and leakage controls | 2 | Filing-date stamps; non-PIT channel identified |
| Costs and realism | N/A | |
| Sample breadth | 0 | 42 firms, one date |
| Statistical testing | 0 | Small audit only |
| Reproducibility | 2 | Code, records and matrices released |
| **Total** | 5/10 → 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a 2021 backtest cannot use a 2026 model's priors without look-ahead" (p. 7)
