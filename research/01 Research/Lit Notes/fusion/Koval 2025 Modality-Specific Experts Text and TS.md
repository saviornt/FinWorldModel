---
type: lit-note
title: "Multimodal Language Models with Modality-Specific Experts for Financial Forecasting from Interleaved Sequences of Text and Time Series"
authors: [Ross Koval, Nicholas Andrews, Xifeng Yan]
year: 2025
venue: "arXiv (cs.CE)"
source_url: https://arxiv.org/abs/2509.19628
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.7, RQ1.2, RQ1.10, RQ1.14, RQ4.4]
family: [fusion]
evidence: Weak
score: 8
tags: [lit-note, family/fusion]
---
# Multimodal Language Models with Modality-Specific Experts for Financial Forecasting (Koval, Andrews & Yan, 2025)

**Basis:** arXiv v1 (23 Sep 2025), pp. 1–3, 7–10, 13, via the alphaXiv PDF reader.

**Takeaway:** On 3,500+ US stocks (test 2020–2024), a Llama3-8B with separate time-series expert parameters and cross-modal attention only in later layers reached 57.1–58.5% AUC for 30-day direction versus 54.1% text-only, and a monthly long-short net Sharpe of 1.51 versus 0.46 (price-only PatchTST) and 0.82 (text-only); sharing parameters across modalities or fusing in early layers did worse, and GPT-4o did worse with prices added than with text alone.

## Problem
How to model interleaved news and daily returns in one LLM so each modality keeps its structure while allowing joint reasoning (pp. 1–2).

## Data and period
FNSPID English news (Nasdaq, Reuters, CNBC, Benzinga) filtered per Chen, Kelly & Xiu (2022); last 252 daily returns and 10 most recent articles per company. Train 2010–2017 (2,591 firms), validation 2018–2019, test 2020–2024 (3,564 firms, 115,611 samples) (p. 3, Table 1; p. 13).

## Method
MSE-ITT: modality-specific (TS) parameters in each layer of Llama3-8B (separate QKV and MLP for TS tokens), selective cross-modal attention in the second half of layers, discretised return tokens; SALMON cross-modal alignment pretraining with salient-token weighting (pp. 1, 3, 7).

## Baselines and validation
General multimodal TS (TaTs, Time-MMD, Time-LLM, Hybrid-MMF, TTSR), finance multimodal (FinMA, MTFE-MICM, FININ, StockTime, MAT, MM-iTransformer), unimodal PatchTST and text-only, zero-shot GPT-4o; AUC for 7- and 30-day direction; quintile long-short portfolios on liquid stocks (≥$250M cap, ≥$1M daily value) with turnover-based costs (pp. 7–9, 13).

## Results (with page or section references)
- 30D AUC ablation: text-only 54.13, shared parameters 55.80, separate QKV 56.78, cross-modal attention in layers 1–16 56.00 / 1–32 56.51, MSE-ITT 57.14; with SALMON+STW 58.48 (p. 7, Table 3; p. 8, Table 4).
- Methods that encode the series with separate parameters beat those relying on the LLM's native reading of numbers; treating text as extra channels in a TS model underperformed (p. 7).
- GPT-4o performed better with text-only inputs than multimodal inputs (p. 7).
- Net Sharpe (2020–2024): TS-only 0.46, text-only 0.82, StockTime 1.10, Hybrid-MMF 1.13, MSE-ITT 1.51 (p. 9, Table 6).

## Limits and risks to validity
_My assessment:_ Llama3-8B (pretraining cutoff around end-2023) reads 2020–2024 test news without a memorisation control, so look-ahead may inflate the text and fusion gains (rubric cap). Price-only baseline is PatchTST, not GBT or a factor model; costs are a flat proportional estimate. Single split. Authors include a practitioner (AJO Vista). Code released.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split, 5-year test |
| Baselines | 1 | Many deep baselines; no GBT/linear factor model |
| Point-in-time and leakage controls | 0 | LLM pre-cutoff test text, not controlled |
| Costs and realism | 1 | Turnover-based cost estimate; liquidity filter |
| Sample breadth | 2 | 3,564 stocks, 2020–2024 incl. COVID and 2022 |
| Statistical testing | 1 | Significance stated for portfolio comparison; no multiple-testing correction |
| Reproducibility | 2 | Code released; public FNSPID data |
| **Total** | **8/14, capped** | Weak (LLM on pre-cutoff events) |

## Quotes worth keeping (each under 15 words, with page)
- "GPT-4o performs better with text-only inputs than multimodal inputs" (p. 7)
