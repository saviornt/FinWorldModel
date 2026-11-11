---
type: lit-note
title: "Better Retrieval, Limited Clustering Gains: A Controlled Study of Multilingual Company Entity Resolution"
authors: [Yijiashun Qi, Yuxuan Li, Hanzhe Guo]
year: 2026
venue: arXiv (cs.AI)
source_url: https://arxiv.org/abs/2610.05573
doi: 10.48550/arXiv.2610.05573
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.8, RQ3.2]
family: [cleaning]
evidence: Moderate
score: 7
tags: [lit-note, family/cleaning, entity-resolution]
---
# Multilingual Company Entity Resolution (Qi, 2026)

**Basis:** arXiv 2610.05573v2 full PDF (pp. 1–9) read via alphaXiv on 2026-11-08.

**Takeaway:** On 3,633 company names from a later GLEIF snapshot (10 countries), fine-tuning the name encoder raised candidate recall from 53.7% to 77.0%, but final cluster recall only from 32.5% to 33.3% because most new candidates failed the fixed pair classifier; entities with successors (renamed or merged) were excluded, so identity change over time was not tested.

## Problem
Do better name retrievers give better company entity clusters?

## Data and period
ROR and GLEIF training names; held-out GLEIF pages timestamped 2026-09-20 (DE, FR, ES, GB, JP, CN, NO, HK, TH, TW) (p. 4).

## Method
Contrastive multilingual-E5 adaptation; equal candidate budgets; frozen gradient-boosted pair classifier; guarded Union-Find clustering (pp. 2–4).

## Baselines and validation
Lexical TF-IDF, frozen encoder, RRF and union; paired bootstrap; assisted single-reviewer audit of 137 pairs (pp. 5–7).

## Results (with page or section references)
- Retrieval recall 53.74% → 76.98%; cluster recall 32.54% → 33.33%, precision 95.99% → 95.45% (Table 1, p. 5).
- 97% of newly retrieved positives scored below the 0.4 threshold (p. 6).
- Only active entities "with no successors" kept (p. 4).

## Limits and risks to validity
Silver labels from the registry; one seed; no temporal identity test; code not public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Later held-out snapshot |
| Baselines | 1 | Lexical, frozen encoders |
| Point-in-time and leakage controls | 2 | Exposure exclusions, snapshot timestamp |
| Costs and realism | N/A | |
| Sample breadth | 1 | 10 countries, 3,633 names |
| Statistical testing | 1 | Bootstrap intervals |
| Reproducibility | 0 | Not public |
| **Total** | 6/12 → 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
