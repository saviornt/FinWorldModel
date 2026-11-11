---
type: lit-note
title: "How Should Transformers Encode Numeric Values in Electronic Health Records?"
authors: [Maria Elkjær Montgomery, Christian Igel, Mikkel Odgaard, Martin Sillesen, Mads Nielsen]
year: 2026
venue: ICML 2026 (PMLR 306); arXiv 2607.01391
source_url: https://arxiv.org/abs/2607.01391
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10, RQ1.14]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, tokenization]
---
# How Should Transformers Encode Numeric Values in Electronic Health Records? (Montgomery, 2026)

**Basis:** PDF pages 1–5, 7–9, 14 (v2). Transfer evidence: mixed event-and-number sequences, not markets.

**Takeaway:** In a controlled comparison inside one transformer, continuous values conditioned on their event type (FiLM) are most precise, while "combined binning" (bin the value, then project it as a continuous token) is the robust default for token sequences; the best bin count follows an approximate power law in data size, and real-task gains from numbers are modest.

## Problem
Discrete, continuous or hybrid encoding of numeric values inside event sequences (§1, pp. 1–2).

## Data and period
Danish regional EHR data 2016–2024 (2.2M people) with synthetic lab signals inserted; real tasks: breast cancer, lung cancer, stroke (§3.1, §4.4).

## Method
ModernBERT-based CORE-BEHRT; five encodings: discretisation, combination, combined binning, concatenation, FiLM; masked-LM pretraining then fine-tuning; "information efficiency" against a theoretical optimum AUC (§3.3–3.4, pp. 3–5).

## Baselines and validation
Encodings compared with each other and with a lab-name-only model on clinical tasks; repeated runs with SD; significance tests on multiplication tasks and clinical AUROC (§4.3–4.4, pp. 7–9).

## Results (with page or section references)
- FiLM best on precision-sensitive arithmetic; combination intermediate; binning-based weakest there (§4.3, p. 7; App. G, p. 14).
- Optimal bin count vs number of unique values fits a power law (R² 0.74 and 0.53), presented as approximate (p. 7).
- Clinical gains from adding values are modest and task-dependent; no method dominates (§4.4, p. 7; Fig. 6f, p. 9).
- Token-budget-matched FiLM performs the same as full FiLM (p > 0.05) (§4.4, p. 8).

## Limits and risks to validity
_My assessment:_ not financial; the encodings also differ in architecture (authors' limitation, p. 9). Its value here is the controlled design and the hybrid-binning recommendation for event streams with attached numbers, which resembles events + market values.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Held-out patients, right-censored |
| Baselines | 1 | Lab-name-only and alternative encodings |
| Point-in-time and leakage controls | 1 | Censoring before label |
| Costs and realism | N/A | Not trading |
| Sample breadth | 1 | Large cohort, one health system |
| Statistical testing | 1 | Tests on key comparisons; no correction stated |
| Reproducibility | 1 | Evaluation framework public; data private |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "motivating hybrid token-based approaches as a practical default" (Abstract, p. 1)
