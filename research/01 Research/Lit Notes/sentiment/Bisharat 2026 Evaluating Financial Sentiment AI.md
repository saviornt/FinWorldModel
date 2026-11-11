---
type: lit-note
title: "Evaluating Financial Sentiment in the Age of AI"
authors: [Arslan Bisharat, Oudom Hean]
year: 2026
venue: arXiv 2609.20198
source_url: https://arxiv.org/abs/2609.20198
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3, RQ4.3]
family: [sentiment]
evidence: Weak
score: 6
tags: [lit-note, family/sentiment]
---
# Evaluating Financial Sentiment in the Age of AI (Bisharat, 2026)

**Basis:** v1 (draft 17 Jul 2026), full text via alphaXiv, pp. 1–20.

**Takeaway:** Twelve sentiment tools (VADER, TextBlob, LM, five finance transformers, four open LLMs, plus Claude Opus 4.5) differ hugely on Financial PhraseBank accuracy but none is significantly related to next-day returns after 221 earnings releases; several track the earnings surprise.

## Problem
Does better agreement with human sentiment labels ("linguistic validity") mean more economically useful sentiment ("economic validity")?

## Data and period
Financial PhraseBank all-agree subset (2,264 sentences). 221 quarterly earnings press releases (8-K Exhibit 99.1) for 15 large US firms, 2022–mid-2026 (pp. 5–6).

## Method
Zero-shot common prompt for Llama 3.2, Gemma 3, Qwen 2.5, Mistral; off-the-shelf FinBERT, FinBERT-Tone, FinancialBERT, DistilRoBERTa-Financial, RoBERTa-Large-Financial; dictionaries. McNemar tests for accuracy; Spearman correlations with EPS surprise and next-day return, 2,000-draw bootstrap CIs (pp. 6–8).

## Baselines and validation
No training on the economic sample; all tools are compared with each other. No price-only or market baseline.

## Results (with page or section references)
- PhraseBank accuracy: dictionaries 54–65%; finance transformers > 90% (two were fine-tuned on PhraseBank); Qwen 2.5 92.1% vs FinBERT-Tone 91.7%, not significantly different (pp. 9–10).
- Claude Opus 4.5: 93.6% accuracy, not significantly better than Qwen 2.5 (p. 13).
- No model, including Claude, is significantly correlated with next-day returns; several are significantly correlated with EPS surprise, FinancialBERT the strongest (pp. 10, 14).
- Signal is strongest in the extreme surprise quartiles and weak in the middle (p. 11).

## Limits and risks to validity
_Authors:_ 15 hand-picked mega-caps; results may not generalise (p. 6). _My assessment:_ 221 events gives low power, so "no significant correlation" is weak evidence of no effect. Next-day close-to-close may miss the announcement reaction. Most events precede the LLMs' training cutoffs; memorisation would bias towards finding a signal, so the null is if anything conservative, but the rubric cap applies.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | No fitting; single evaluation sample |
| Baselines | 1 | Dictionaries and FinBERT family; no price baseline |
| Point-in-time and leakage controls | 0 | LLM cutoffs not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 15 firms, one regime |
| Statistical testing | 1 | Bootstrap CIs, McNemar; no correction |
| Reproducibility | 1 | Replication files mentioned (p. 10) |
| **Total** | **5/12 → 6/14** | Moderate → capped Weak (pre-cutoff LLMs) |

## Quotes worth keeping (each under 15 words, with page)
- "higher classification accuracy does not translate into stronger economic relationships" (abstract, p. 1)
