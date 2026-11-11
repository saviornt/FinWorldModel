---
type: lit-note
title: "Beyond Sentiment: Structured Information Extraction from Financial News"
authors: [Daohan Zhu, Sitong Ge, Ruofei Wang, Honggu Chen, Yubo Hou, Tao Wan, Zengchang Qin]
year: 2026
venue: arXiv 2607.28496
source_url: https://arxiv.org/abs/2607.28496
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14, RQ1.3]
family: [sentiment]
evidence: Weak
score: 5
tags: [lit-note, family/sentiment]
---
# Beyond Sentiment: Structured Information Extraction from Financial News (Zhu, 2026)

**Basis:** v1 (30 Jul 2026), full text via alphaXiv (pp. 1–18).

**Takeaway:** On 41,618 news–stock pairs (100 NASDAQ stocks, 2019–2023), adding six LLM-extracted fields (event type, impact subject, horizon, confidence, sentiment) to FinBERT's three probabilities raised next-day direction F1 from 0.576 to 0.600 under XGBoost, but AUROC was only 0.526–0.528, splits were random, and the extractor (LLaMA-3.1-70B) post-dates the test period.

## Problem
Does a small, structured event schema add information beyond sentiment polarity?

## Data and period
FNSPID NASDAQ news, Jan 2019–Dec 2023; up to 500 articles for each of the 100 most-covered stocks; next-day close-to-close direction label; positive rate 48.7% (p. 5).

## Method
FinBERT (ProsusAI) probabilities (3-d) vs LLaMA-3.1-70B zero-shot JSON extraction of six fields (sentiment, score, event type in 7 classes, impact subject, short/long horizon, confidence) vs both (9-d); logistic regression and XGBoost (pp. 5–6, App. A.5).

## Baselines and validation
Random classifier; each feature set alone. 1,000 bootstrap resamples, each with a random 80/20 split; paired t-tests with Bonferroni correction (p. 6). No temporal split, no price features, no costs.

## Results (with page or section references)
- XGBoost F1 / AUROC: FinBERT 0.576 / 0.526; LLM fields 0.450 / 0.507; combined 0.600 / 0.528 (Table 1, p. 7).
- Removing the LLM's own sentiment fields still gave +0.019 F1 over FinBERT; gains on every event type (+0.010 to +0.023) (pp. 8–9, Table 3).
- FinBERT and LLaMA disagreed on polarity in 53.5% of articles (Table 4, p. 11).
- Logistic regression on FinBERT alone: F1 0.230, below random — the sentiment–return mapping is nonlinear (p. 7).

## Limits and risks to validity
The authors list random (non-temporal) splits, bootstrap duplicates leaking across train/test, LLaMA's training data overlapping 2019–2023, and no extraction ground truth (pp. 13–14). _My assessment:_ AUROC barely above 0.5 means the F1 gains reflect threshold behaviour more than ranking skill; treat as weak evidence that event-type fields are complementary to polarity, not as evidence of forecasting value. Cost: one 70B-model pass per article.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Random splits, no time order |
| Baselines | 1 | Random and single-source feature sets; no price baseline |
| Point-in-time and leakage controls | 0 | LLM pre-cutoff; random splits |
| Costs and realism | 0 | None |
| Sample breadth | 2 | 100 stocks, 2019–2023 incl. 2020 |
| Statistical testing | 2 | Paired tests, Bonferroni |
| Reproducibility | 0 | Prompt only |
| **Total** | **5/14 → capped Weak** | Rubric cap: LLM used on events before its cutoff without memorisation control |

## Quotes worth keeping (each under 15 words, with page)
- "the text reads positively, but the event implies negative consequences" (p. 2)
