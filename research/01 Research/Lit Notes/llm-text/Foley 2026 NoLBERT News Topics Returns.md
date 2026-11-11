---
type: lit-note
title: "Reading the News Without Hindsight: NoLBERT Topics and the Cross-Section of Stock Returns"
authors: [Kevin Foley, Jonathan Hartadi, Shivesh Prakash, Charishma Takkallapalli, Swapnil Vatsal]
year: 2026
venue: arXiv 2610.22745
source_url: https://arxiv.org/abs/2610.22745
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.2, RQ1.3, RQ3.1, RQ1.14]
family: [llm-text]
evidence: Strong
score: 10
tags: [lit-note, family/llm-text]
---
# Reading the News Without Hindsight (Foley, 2026)

**Basis:** v1 (15 Oct 2026), page excerpts via alphaXiv (pp. 1–3, 6–9, 14, 18, 20, 24).

**Takeaway:** A point-in-time encoder (NoLBERT, pretrained on 1976–1995 text) gives news topics that forecast returns about as well as LDA and better on average than MiniLM; the best single validated experiment loses money on the test, and the best combination (net monthly Sharpe 1.12) does not beat a price-only benchmark.

## Problem
Does removing hindsight from the text encoder cost forecasting power in narrative asset pricing?

## Data and period
1.26 million articles, 2012–2024; 1,000 largest US stocks; fit 2013–2019, choose 2020–2021, hold out 2022–2024 (p. 1).

## Method
Six topic readers (LDA, LDA-all, MiniLM, FinBERT classifier, NoLBERT-60/20 after contrastive adaptation on pre-2020 articles); attention shocks (5- or 63-day windows) and stock exposures (Bybee et al. framework); eight forecasting models from OLS to XGBoost/EBM; nine portfolio rules at 10 bp per dollar traded (pp. 6–9).

## Baselines and validation
Price-only ensemble, placebo exposures, LM and FinBERT tone, headline embeddings (Table 1, p. 9). Ledoit–Wolf, SPA, false-discovery and deflated-Sharpe checks (pp. 6, 18).

## Results (with page or section references)
- Best-validation experiment loses money at every frequency (p. 1).
- 63-day attention window raises test rank IC for every reader (pp. 1, 24).
- Equal-weight combination (price + text, 63-day): monthly net Sharpe 1.12 decile, 1.19 buffered; not significant vs the price-only ensemble (Sharpe 0.66) (p. 14).
- Cap-weighting the legs cuts the monthly combination Sharpe from 1.12 to 0.03 (p. 14).
- No single experiment survives a false-discovery correction (p. 18).
- Data traps found: bodies attached to wrong headlines, a source collected after the fact, missing returns that depend on the future (p. 2).

## Limits and risks to validity
Authors: 36 test months gives power only for Sharpe ≈ 1.7+; ~600 experiments per frequency; MiniLM and FinBERT readers trained on in-sample text; firm news imputed for 40–50% of stocks; flat costs (p. 18).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Train/validation/test split |
| Baselines | 2 | Price-only ensemble with trees, placebo |
| Point-in-time and leakage controls | 2 | PIT encoder, PIT universe, missingness handled |
| Costs and realism | 1 | Flat 10 bp; turnover reported |
| Sample breadth | 2 | 1,000 stocks, 2013–2024 incl. 2020, 2022 |
| Statistical testing | 2 | SPA, FDR, deflated Sharpe |
| Reproducibility | 0 | Not stated in the part I read |
| **Total** | **10/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "The experiment with the best validation score loses money at every frequency." (abstract, p. 1)
