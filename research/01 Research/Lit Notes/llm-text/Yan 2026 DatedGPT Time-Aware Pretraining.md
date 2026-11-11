---
type: lit-note
title: 'DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining'
authors:
- Yutong Yan
- Raphael Tang
- Zhenyu Gao
- Wenxi Jiang
- Yao Lu
year: 2026
venue: arXiv 2603.11838v2
source_url: https://arxiv.org/abs/2603.11838
doi: ''
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.2, RQ3.1, RQ4.5, RQ1.14]
family:
- llm-text
evidence: Moderate
score: 9
tags:
- lit-note
- family/llm-text
---
# DatedGPT (Yan, 2026)

**Basis:** v2 (23 Jul 2026), page excerpts via alphaXiv (pp. 1–10).

**Takeaway:** Twelve 1.3B models trained from scratch with annual data cutoffs (2013–2024) still predict next-day returns from headlines without look-ahead (gross Sharpe 3.20), and a vintage that has seen the outcome period adds a significant "lookahead premium".

## Problem
Can time-locked pretraining remove look-ahead bias at acceptable cost, and how large is the bias?

## Data and period
~100B FineWeb-Edu tokens per vintage filtered by crawl date; time-locked instruction data (DatedInstruct); 61,290 firm-day headlines, 2014–2024 (pp. 2–4).

## Method
Good/bad/neutral headline classification; panel regression with firm and date fixed effects; daily long–short portfolio; vintage y−1 scores year y (look-ahead free) vs the 2024 vintage scoring all years (pp. 4–6). Perplexity probing of the cutoff (p. 6).

## Baselines and validation
Off-the-shelf Llama-2/3.2 and Gemma-3 (look-ahead biased), ChronoGPT and PIT time-locked families (Table 3, p. 6). Fama–French five-factor alpha. No costs.

## Results (with page or section references)
- DatedGPT-instruct look-ahead-free: 28.3 bp per SD, Sharpe 3.20 (gross) (Table 3, p. 6).
- PIT-4B look-ahead-free: 29.6 bp per SD vs biased Llama-2-7B 35.3 bp (p. 5).
- Biased vintages beat their own look-ahead-free versions: DatedGPT 28.3 → 33.0 bp, Sharpe 3.20 → 3.65 (p. 5).
- Residual signal from the biased vintage adds 26.4 bp per SD (t = 10.65) for DatedGPT-instruct and 40.1 bp (t = 10.98) for PIT-4B (Table 4, p. 6).
- Perplexity reverses at each cutoff, consistent with bounded knowledge (Fig. 2, p. 6).

## Limits and risks to validity
_My assessment:_ crawl date is not creation date, so old pages can still leak little beyond the cutoff but later pages are excluded, as intended; small models; gross returns only; one headline dataset.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling annual vintages (walk-forward) |
| Baselines | 1 | Other LLMs; no price-only baseline |
| Point-in-time and leakage controls | 2 | Time-locked training, perplexity check |
| Costs and realism | 0 | Gross only |
| Sample breadth | 2 | 2014–2024 incl. 2020, 2022 |
| Statistical testing | 1 | t-stats; no multiple-testing correction |
| Reproducibility | 1 | Model checkpoints released; news data not |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "showing that lookahead bias is a real concern in financial forecasting" (p. 2)
