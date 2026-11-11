---
type: lit-note
title: "Human Agreement and Return Association Are Not Interchangeable Criteria"
authors: [AS Aravinthakshan, Laven Srivastava, Harsh Nandwani]
year: 2026
venue: arXiv 2609.11144
source_url: https://arxiv.org/abs/2609.11144
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3]
family: [sentiment]
evidence: Moderate
score: 9
tags: [lit-note, family/sentiment]
---
# Human Agreement vs Return Association (Aravinthakshan, 2026)

**Basis:** v2, page excerpts via alphaXiv (pp. 1–7, 10–11).

**Takeaway:** On 70,500 X posts around securities class actions, the best human-agreeing tool (Claude Haiku, κ = 0.74) is not the best one-day predictor (FinBERT, κ = 0.08, has the largest lead), instrument rankings flip with the sampling rule, and post volume carries no signal.

## Problem
Does agreement with human sentiment labels predict which tool best tracks abnormal returns, and at which horizon?

## Data and period
845 securities class actions, 2002–2025; 70,500 X messages (17.6% spam), 179 cases and 103,542 case-days with prices; 400-message single-annotator gold set (pp. 1, 3–5).

## Method
VADER, LM, FinBERT, Twitter-RoBERTa and Claude Haiku scored through one pipeline; coarse and graded negativity averaged per case-day. Market-model abnormal returns fitted on pre-event data. Spearman lead–lag, Granger, distributed lag with case FE, local projections with negative-horizon placebo; BH-FDR (pp. 3–5).

## Baselines and validation
Message volume and impressions as count baselines; instruments compared with each other on conventional and fixed-n (common-day) samples (Sec. 7.1).

## Results (with page or section references)
- Gold-set κ: Claude 0.741, Twitter-RoBERTa 0.449, LM 0.210, VADER 0.171, FinBERT 0.079 (Table 2, p. 4).
- Same day: every sentiment family beats volume (ρ = −0.031) by 2–3×; strongest Twitter-RoBERTa coarse ρ = −0.097 (Table 3, p. 5).
- One-day lead: FinBERT coarse largest (ρ1 = −0.047, q = 0.003); VADER and LM do not survive FDR (Table 4, p. 5). Lag-2 effects mostly near zero.
- On common days the same-day leader flips to FinBERT (−0.126) and VADER drops to zero (Table 6, p. 7).
- Posts from news accounts carry the strongest attributed signal (ρ = −0.261) (p. 2). Volume predicts neither price damage nor settlement size (p. 5).

## Limits and risks to validity
_Authors:_ single annotator; between-instrument differences not tested; case-level comparison underpowered (pp. 5, 7). _My assessment:_ a niche, adverse corpus (litigation, spam); effects are associations, not trading tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Lead–lag on held event windows; no fitted model |
| Baselines | 1 | Volume and five instruments; no price-only model |
| Point-in-time and leakage controls | 1 | Pre-event market model; LLM contamination analysed (Sec. 9, not read) |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Many firms 2002–2025 but one event type |
| Statistical testing | 2 | BH-FDR, placebo horizons |
| Reproducibility | 2 | Corpus and code released |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "message volume predicts neither market damage nor settlement size" (abstract, p. 1)
