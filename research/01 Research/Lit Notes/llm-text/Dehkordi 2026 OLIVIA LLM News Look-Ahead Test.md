---
type: lit-note
title: 'Thinking Fast, Trading Late: System One Decision Models vs the Market'
authors:
- Amir Dehkordi
- Alireza Kargarzadeh
- Nariman Khaledian
- Navid Parvini
- Sid Ghatak
- Arman Khaledian
year: 2026
venue: arXiv 2611.03985
source_url: https://arxiv.org/abs/2611.03985
doi: ''
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.2, RQ3.1, RQ4.5]
family:
- llm-text
evidence: Strong
score: 10
tags:
- lit-note
- family/llm-text
---
# Thinking Fast, Trading Late (Dehkordi, 2026)

**Basis:** v1 (2 Nov 2026), page excerpts via alphaXiv (pp. 1–5, 9–11, 23, 27, 32).

**Takeaway:** Under a pre-registered, blinded, identity-masked test on the point-in-time S&P 500, LLM-style news readings predict the overnight move to the open but not the move after it; a validated fine-tuned signal fell from IC 0.065 to 0.020 on the test, and no pre-registered strategy survives costs and a deflated Sharpe ratio.

## Problem
How much LLM news predictability survives a test that rules out look-ahead, memorisation and selection?

## Data and period
Point-in-time S&P 500 members; news state at 09:15 ET with names, tickers, people, dates and price-move mentions masked; train Jul 2024–Jun 2025, validation Jul–Dec 2025 (two quarters), blinded test 2 Jan–31 Jul 2026 (pp. 2, 5).

## Method
"OLIVIA" protocol: one-time unblinding, look-ahead-free states, masking, validation-only selection, hash-frozen analysis plan, audit log (p. 3). Decision models (non-generative, return probabilities): fine-tuned open model Laya-Fin, three commercial models, untuned Laya, a Dec-2024 ModernBERT anchor (p. 9).

## Baselines and validation
Price-only gradient-boosted model, ridge on sentence embeddings, a generative LLM whose stated cutoff (Apr 2024) precedes the sample, and vendor-label baselines flagged as possibly look-ahead (p. 9). Daily Spearman IC with Newey–West t; block bootstrap; Holm and Benjamini–Hochberg corrections; deflated Sharpe (pp. 9–10).

## Results (with page or section references)
- Laya-Fin IC 0.065 (t = 3.6) on validation, 0.020 (t = 1.7) on test; every clearly positive validation IC fell (p. 10; Table A2, p. 32).
- Commercial models: IC 0.074–0.077 with the overnight move, about zero after the open (p. 10).
- None of five primary hypotheses supported (Holm p 0.27–0.85) (Table 2, p. 11).
- Generative LLM baseline (pre-sample cutoff): IC 0.052 validation → 0.001 test (p. 10).
- Price-only and embedding baselines near zero in both periods (p. 10).
- Masked companies identified in 62–74% of cases vs a 28% baseline (p. 1).
- Eight conditions selected on validation (in-sample Sharpe up to 6.8): 5 changed sign on test, all lose net of 10 bps (p. 23).

## Limits and risks to validity
Authors: S&P 500 only, seven-month test (140 sessions), one seed and one epoch, commercial models released after the sample, flat costs, overlap with the authors' earlier study (p. 23). _My assessment:_ low power means small true ICs could be missed; the forward test on post-release news is pre-registered but not yet reported.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split, blinded |
| Baselines | 2 | Price-only GBT, embeddings, clean LLM |
| Point-in-time and leakage controls | 2 | PIT universe, masking, identification test |
| Costs and realism | 1 | Flat costs; no borrow or impact |
| Sample breadth | 1 | S&P 500, ~2 years |
| Statistical testing | 2 | Holm, BH, deflated Sharpe |
| Reproducibility | 1 | Code public; data private |
| **Total** | **10/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "masking hides names, not companies. The market reads the news first." (abstract, p. 1)
