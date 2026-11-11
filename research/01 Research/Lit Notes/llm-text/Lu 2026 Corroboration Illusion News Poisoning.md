---
type: lit-note
title: "The Corroboration Illusion: When More News Makes LLM Forecasts Less True"
authors: [Yuan Lu, Yukuan Zhang]
year: 2026
venue: arXiv 2609.22246
source_url: https://arxiv.org/abs/2609.22246
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.11]
family: [llm-text]
evidence: Moderate
score: 9
tags: [lit-note, family/llm-text, corroboration, misinformation]
---
# The Corroboration Illusion: When More News Makes LLM Forecasts Less True (Lu, 2026)

**Basis:** v1 (5 Sep 2026), full text via alphaXiv (pp. 1–8). Kept as a comparison case under the scope update: the failure is about a text pipeline counting repeated, unverified reports as corroboration, which applies to any news-reading model.

**Takeaway:** In retrieval-based forecasters, a handful of fabricated, mutually consistent articles look like corroboration: five articles per question moved probabilities by +0.13 to +0.23 net of a placebo and flipped 69–77% of forecasts; publisher labels were ignored, and allow-lists, isolate-then-aggregate and perplexity filters each had a cheap bypass.

## Problem
Can someone who can only publish articles move a news-reading probabilistic forecaster?

## Data and period
500 resolved ForecastBench questions (Jul 2024–Aug 2025; Polymarket, Manifold, Metaculus, INFER; some crypto/finance); 17.4M Common Crawl News articles from 10.6k publishers; availability = crawl date, 60-day window, 0 of 10,000 retrieved articles after cutoff (pp. 3–4).

## Method
Halawi-style RAG forecasters on Qwen2.5-7B (vanilla, calibrated) and Hermes-3-8B; injected LLM-written articles (k = 1–10); neutral placebo; seed noise floor; three defenses (pp. 3–6).

## Baselines and validation
Clean forecasters, no-retrieval, market prices (Brier 0.074), base rate; bootstrap CIs; placebo-net effects (Tables II–III).

## Results (with page or section references)
- k = 1 flips 56%; k = 5 70–74%; k = 10 89% (Δp +0.27) (p. 4, Fig. 3); Brier 0.18 → 0.37 for the calibrated forecaster (abstract, Table III).
- Same articles labelled Reuters vs obscure domain: Δp +0.215 vs +0.212 (p. 4).
- Stricter relevance filtering raised vulnerability (poison share of kept documents rises) (pp. 4–5).
- Allow-list neutralised unknown domains but spoofed labels restored the full effect; isolate-then-aggregate halved the effect but fails once poison is the majority; perplexity filter beaten by sampling at T = 1.2 (Table IV, pp. 5–6).
- Even clean retrieval added an optimism bias that grows with the number of retrieved documents (p. 3).

## Limits and risks to validity
_My assessment:_ small open LLMs; in-memory injection; prediction-market questions, not returns. Post-cutoff questions and crawl-date control are a model for leak-free text evaluation. Lesson for a non-LLM model: count independent, provenance-verified sources, not article volume.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Post-cutoff questions, single evaluation set |
| Baselines | 2 | Placebo, noise floor, market prices, no-retrieval |
| Point-in-time and leakage controls | 2 | Crawl-date cutoff checked; post-cutoff questions |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 500 questions, one year |
| Statistical testing | 1 | Bootstrap CIs |
| Reproducibility | 1 | Code and harness released; no poisoned corpus |
| **Total** | **8/12 → 9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "is the system forecasting the world, or merely forecasting the news it retrieves?" (p. 1)
