---
type: lit-note
title: "Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction"
authors: [Tian Guo, Emmanuel Hauptmann]
year: 2025
venue: "arXiv (q-fin.CP), v3"
source_url: https://arxiv.org/abs/2510.15691
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7, RQ1.14, RQ1.15]
family: [fusion]
evidence: Weak
score: 4
tags: [lit-note, family/fusion]
---
# Exploring the Synergy of Quantitative Factors and Newsflow Representations from LLMs for Stock Return Prediction (Guo & Hauptmann, 2025)

**Basis:** arXiv v3 (25 Nov 2025), pp. 1–3, 8–9, 22–29, via the alphaXiv PDF reader.

**Takeaway:** On ~1,000-stock universes (NA, EM, EU, test 2023–2024), simple concatenation of ~200 factors with a bottlenecked DeBERTa news embedding beat summation and attention fusion; news alone was useless or negative, fusion helped only where news was complementary (NA, EU) and hurt in EM, while a decoupled mixture over factor-only and fusion predictions was the most robust across universes.

## Problem
How to combine structured quantitative factors with LLM newsflow representations for monthly return prediction and stock selection; which fusion design works (pp. 1–2).

## Data and period
Three investment universes from a commercial vendor: North America (830 stocks), Emerging Markets (1,090), Europe (370); ~200 factors (quality, size, momentum, revision, valuation…); company news headlines (one-week window NA/EU, one-month EM). Train/validation 2003–2022, test 2023–2024 (pp. 8, 22, Table 5).

## Method
Fusion learning: (a) representation combination (concatenate factors with a half-dimension bottleneck of the news embedding, dense layer), (b) summation in a shared space, (c) attention-weighted representations. Mixture model: gate adaptively weights factor-only and fusion predictions per instance; "decoupled" training to fix instability. Optional LoRA fine-tuning of DeBERTa (pp. 3, 23).

## Baselines and validation
Equal-weight universe; factors-alone dense NN; news-alone (linear head on DeBERTa); FININ (factor-weighted news attention). Single chronological split, no retraining in the test period. Monthly-rebalanced decile long-only and long-short portfolios; annualised return, Sharpe, MAPE, IC (p. 8).

## Results (with page or section references)
- NA long-short Sharpe: factors alone 1.26, news alone 0.18, fusion combination 1.64, fusion attention 0.87, mixture decoupled 1.78; IC 0.018 / −0.000 / 0.031 / −0.005 / 0.027 (p. 8, Table 1a).
- EM long-short Sharpe: factors alone 2.96, news alone −1.57, fusion combination 2.21, attention 1.07, mixture decoupled 2.93 — fusion lost to factors alone (p. 8, Table 1b; p. 9).
- EU long-short Sharpe: factors 1.46, news 0.21, combination 1.70, attention 1.35, mixture decoupled 1.70 (p. 29, Table 10).
- Attention fusion was worst of the three fusion designs in every universe (Tables 1, 10); authors suggest shared-space compression destroys complementary information (p. 9).
- News helped when it carried information beyond the factors (partnerships, trial results) and hurt when it repeated earnings and ratings already in the factors (p. 26, Fig. 10).
- LoRA fine-tuning of the LLM did not consistently help (p. 1; Table 7).
- Low MAPE did not imply better portfolios (p. 9).

## Limits and risks to validity
_My assessment:_ single 2-year test window (one regime), no significance tests, no transaction costs on monthly decile portfolios, proprietary data and no code. DeBERTa (2022) with a 2023–2024 test window controls the LLM-memorisation risk reasonably (p. 22). Factors-alone baseline is a dense NN, not GBT. Authors work at an asset manager.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split; no retraining in test |
| Baselines | 1 | Factor NN, news-only, FININ; no GBT or linear factor model |
| Point-in-time and leakage controls | 1 | Post-cutoff test for the LLM; factor timing not discussed |
| Costs and realism | 0 | No costs on decile portfolios |
| Sample breadth | 1 | ~2,300 stocks in 3 universes, but one 2-year regime |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Vendor data, no code |
| **Total** | **4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "preserving the structure of each modality … can yield predictive representations" (p. 9)
