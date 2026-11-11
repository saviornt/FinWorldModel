---
type: lit-note
title: "Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions"
authors: [Kemal Kirtac]
year: 2026
venue: arXiv 2609.23703 (revise and resubmit, Engineering Applications of Artificial Intelligence)
source_url: https://arxiv.org/abs/2609.23703
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.14, RQ1.3]
family: [sentiment]
evidence: Strong
score: 10
tags: [lit-note, family/sentiment]
---
# Financial Language Models as Applied AI Systems for News-Based Trading under Market Frictions (Kirtac, 2026)

**Basis:** v1 (20 Sep 2026), page excerpts via alphaXiv (pp. 1–5, 8, 10, 13, 15–16, 19, 25–26, 29–30, 32, 35–37).

**Takeaway:** On 973,481 single-firm Refinitiv news items linked to CRSP (2010–Jan 2026), with the test restricted to June 2024–Jan 2026 (after the LLaMA-3 data cutoff), net long–short Sharpe after 5 bp costs and a 10% ADV cap ranked LLaMA-3-8B 2.85 > OPT-1.3B 2.45 > RoBERTa 2.25 > BERT 1.95 > FinBERT 1.75 > Loughran–McDonald 0.68, while FinBERT ran ~13× faster per article than LLaMA-3 on ~1/12 the GPU memory.

## Problem
Do text-model sentiment signals survive point-in-time observability, calibration, costs, capacity and multiple testing, and how do small encoders compare with decoders on signal and compute?

## Data and period
Refinitiv News Analytics, 3,129,924 US items Jan 2010–Jan 2026; single-firm stories; five-day cosine-similarity novelty screen to remove repeated wire coverage; liquidity screens (spread < 20%, Amihud, Kyle lambda); 973,481 items, 3,452 firms (pp. 4–5). Validation buffer Jan–May 2024; primary test Jun 2024–Jan 2026 (p. 19).

## Method
Six scorers fine-tuned on execution-aligned labels (sign of 3-day excess return): LLaMA-3-8B and OPT-1.3B with LoRA; RoBERTa, BERT, FinBERT fully fine-tuned; LM dictionary (Table 5, p. 25). Validation-set calibration, daily ranks, value-weighted quintile long–short, positions update only after news is observable (pp. 15–16, 26).

## Baselines and validation
Dictionary, encoder models, Nasdaq/Dow benchmarks. Chronological split with no cross-split labels; post-cutoff test window; McNemar, block-bootstrap CIs, Diebold–Mariano, White reality check, Hansen SPA, deflated Sharpe (pp. 26, 32). No price-only or momentum model.

## Results (with page or section references)
- Accuracy / AUC: LLaMA-3 0.787 / 0.846; FinBERT 0.713 / 0.764; dictionary 0.503 / 0.512; ECE 0.032 vs 0.068 vs 0.143 (Table 7, p. 29).
- Fixed-effects regression coefficients on next-day return: LLaMA-3 0.312 (t 6.44) … FinBERT 0.158 (t 3.98); dictionary 0.049 (t 1.31) (Table 8, p. 30).
- Net L–S Sharpe (5 bp): see takeaway; FinBERT cumulative 64% vs LLaMA-3 180% (Table 9, p. 30). LLaMA-3 Sharpe CI [2.31, 3.34]; SPA p = 0.026; DSR p = 0.014 (Table 12, p. 32).
- Compute: LLaMA-3 54.2 GB, 112 ms/article; FinBERT 4.4 GB, 8.5 ms/article (Table 11, p. 32).
- Gains of large models concentrate in articles where negation, contrast, guidance or numeric context make word polarity misleading (p. 35).

## Limits and risks to validity
The author notes that public model cards cannot prove no document-level pretraining exposure; no order-book execution model; US English only (p. 36). _My assessment:_ 71–79% direction accuracy on 3-day excess returns is far above other news studies in this vault (typically 51–56%; see [[Zhu 2026 Beyond Sentiment Structured News Extraction]]), so the absolute numbers need replication; the 20-month test is one regime; single author. The ranking (encoder < decoder ≪ dictionary) and the compute table are the most transferable results.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Dictionary, encoders, index; no price model |
| Point-in-time and leakage controls | 2 | Post-cutoff test, observability rule, novelty screen |
| Costs and realism | 2 | 5 bp, ADV cap, liquidity screens |
| Sample breadth | 1 | 3,452 firms, 20-month test |
| Statistical testing | 2 | SPA, reality check, DSR |
| Reproducibility | 1 | Code and public replication arm; core data licensed |
| **Total** | **10/14 → Strong** | Absolute performance flagged as an outlier |

## Quotes worth keeping (each under 15 words, with page)
- "RoBERTa and FinBERT remain relevant when throughput and cost dominate" (p. 35)
