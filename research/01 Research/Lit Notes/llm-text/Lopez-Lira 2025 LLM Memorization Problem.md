---
type: lit-note
title: 'The Memorization Problem: Can We Trust LLMs'' Economic Forecasts?'
authors:
- Alejandro Lopez-Lira
- Yuehua Tang
- Mingyin Zhu
year: 2025
venue: arXiv 2504.14765v2 (SSRN 5217505)
source_url: https://arxiv.org/abs/2504.14765
doi: ''
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.2, RQ3.1, RQ4.5, RQ1.14]
family:
- llm-text
evidence: Moderate
score: 7
tags:
- lit-note
- family/llm-text
---
# The Memorization Problem (Lopez-Lira, 2025)

**Basis:** v2 (15 Dec 2025), page excerpts via alphaXiv (pp. 1, 3, 16, 23, 25–26, 34–35, 37–38, 47, 57–58, 76, 81, 83) plus the alphaXiv summary report.

**Takeaway:** GPT-4o (and Llama-3.1-70B) recall pre-cutoff index levels, macro data and stock prices close to exactly; accuracy collapses after the cutoff; instructions to respect a fake cutoff and entity masking do not stop the recall, so pre-cutoff forecasting skill is not identified.

## Problem
Can LLM forecasts inside the training window be read as forecasts at all?

## Data and period
GPT-4o (cutoff Oct 2023) and Llama-3.1-70B (cutoff Dec 2023); S&P 500, DJIA, Nasdaq daily 1990–Feb 2025; macro series; CRSP stocks by size quintile; 90,123 WSJ front-page headlines; masked earnings calls (pp. 16, 23, 26, 57).

## Method
Recall prompts with and without context, compared across pre-cutoff, recent pre-cutoff and post-cutoff zones; fake-cutoff prompts; masking tests; a formal non-identification result (pp. 3, 16, 37, 58).

## Baselines and validation
The post-cutoff period is the control. No forecasting baselines (not the aim).

## Results (with page or section references)
- S&P 500 daily level recall: MAPE 0.61%, directional accuracy 80.6% pre-cutoff; 16.9% and 45.7% post-cutoff (Table 2, p. 25).
- Headline dating: 98.5% correct year pre-cutoff vs 28.8% post-cutoff (p. 26).
- Recall is strongest for large and recent stocks: no-context MAPE 3.2% (largest quintile, 2014–2023) vs 15.2% (smallest) (Table 5, p. 34).
- Fake 2010 cutoff in the system prompt: 98.0% GDP-direction accuracy after the fake cutoff vs 40% on truly unseen data (pp. 3, 37–38).
- Llama-3.1-70B also memorises, more weakly (index MAPE 2–4.5% pre vs 14–18% post) (pp. 57–58).
- Memorisation extends to embeddings (abstract, p. 1).

## Limits and risks to validity
_My assessment:_ mostly GPT-4o; recall tests show memorisation exists but do not measure how much it inflates a specific trading backtest. Post-cutoff samples are short (e.g. 12 monthly observations).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Pre vs post cutoff split |
| Baselines | N/A | Not a forecasting comparison |
| Point-in-time and leakage controls | 2 | The subject of the paper; explicit and checked |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 2 | Indices, macro, stocks, text; 1990–2025 |
| Statistical testing | 0 | Descriptive metrics (none in the part I read) |
| Reproducibility | 0 | No code or data mentioned in the part I read |
| **Total** | **5/10 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Instructions to respect historical boundaries fail to prevent recall-level accuracy" (abstract, p. 1)
