---
type: lit-note
title: "Does Normalization Choice Matter for Causal Large Time-Series Models?"
authors: [Samy-Melwan Vilhes, Gilles Gasso, Mokhtar Z. Alaya]
year: 2026
venue: ICLR 2026 Workshop TSALM (arXiv)
source_url: https://arxiv.org/abs/2606.09954
doi: 10.48550/arXiv.2606.09954
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6, RQ1.13]
family: [cleaning]
evidence: Moderate
score: 8
tags: [lit-note, family/cleaning, normalisation, autoregressive]
---
# Does Normalization Choice Matter for Causal Large Time-Series Models? (Vilhes, 2026)

**Basis:** arXiv 2606.09954v1 PDF pages 1–4, 13–19 read via alphaXiv on 2026-11-08.

**Takeaway:** In a 300M-parameter patch-based causal Transformer, normalising every patch with statistics of the whole window (vanilla RevIN) leaks future values during parallel training; causal (running) statistics with an arcsinh transform gave the best forecasts at contexts of 256–1024, prefix-based statistics were best at short contexts, and no normalisation was worst of all.

## Problem
Which normalisation fits an efficiently trained causal (next-patch) time-series model without look-ahead?

## Data and period
Pretraining on GIFT and UTSD corpora plus synthetic data (~715M patches); evaluation on ~115,000 signals from UTSD, synthetic and GIFT-Eval; contexts 64–1024, horizons 32–512 (p. 3). Not financial.

## Method
Six strategies: vanilla RevIN (global window statistics, non-causal in training), prefix@k (first k=8 patches), causal (running statistics up to each patch), each with and without arcsinh; plus no normalisation (pp. 2–3, A.10). Pinball loss; median used as point forecast.

## Baselines and validation
Strategies compared against each other and no normalisation; Friedman/Nemenyi critical-difference ranks; pairwise skill scores (Table 1, p. 4; Fig. 5, p. 13).

## Results (with page or section references)
- Causal+arcsinh best overall for contexts >128; prefix@k best at 128 and 64 (Table 1, p. 4; Table 4, p. 14).
- RMSE skill score of causal+arcsinh vs vanilla RevIN ≈ 0.50 (Fig. 5, p. 13).
- RevIN reaches the lowest training loss but not the best forecasts, consistent with leaked statistics (p. 4).
- No normalisation worst on every metric (Fig. 14, p. 19).
- GIFT-Eval more mixed: RevIN variants best on MAE/RMSE up to 1024 context (p. 14).

## Limits and risks to validity
Workshop paper; univariate only; Transformer only; non-financial data; results vary by benchmark; code not stated.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out evaluation sets |
| Baselines | 1 | Normalisation variants and no-norm |
| Point-in-time and leakage controls | 2 | Causal leakage is the subject; explicit |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | Large, but not financial |
| Statistical testing | 2 | Nemenyi critical-difference test |
| Reproducibility | 0 | Code not stated |
| **Total** | 7/12 → 8/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "computing global statistics introduces look-ahead leakage that violates causal constraints" (p. 1)
