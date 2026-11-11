---
type: lit-note
title: 'Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal'
authors:
- Chenhao Xue
- Raslen Guesmi
- Siwei Feng
- Yucheng Gong
- Jacob Xavier Sundram
- Jordan Pang
- Lan Wang
- Julian Kaljuvee
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2608.17223
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ3.2
- RQ3.1
- RQ3.6
family:
- cleaning
evidence: Strong
score: 10
tags:
- lit-note
- family/cleaning
- leakage
- text
---
# Temporal Leakage in Financial News NLP (Xue et al., 2026)

**Basis:** arXiv v2 read via alphaXiv on 2026-11-08 (pp. 1–5, 19–20, 26, 28).

**Takeaway:** On 49,799 news articles, random train/test splits inflate next-day direction MCC by 1.1× to 6.5× over chronological splits, growing with model capacity and feature richness; under a chronological split general news prediction is near random (best MCC 0.06), and masking firm names improves several event types, exposing firm-name memorisation.

## Problem
How much of the reported predictability of returns from news is temporal leakage?

## Data and period
56,409 articles (49,799 after removing near-zero returns) from a proprietary provider, 2020-05 – 2025-08 (81% from 2025), 64 exchanges, 203 event types; chronological train < 2025-04, validation 2025-04/05, test ≥ 2025-06 (Table 1). After-hours releases labelled close-to-next-open (§3.3).

## Method
Sixteen feature–model combinations (TF-IDF, MiniLM, FinBERT, fine-tuned RoBERTa/DeBERTa) plus LLM probes, each on paired random (10 seeds, size-matched) and chronological splits; leakage ratio = random MCC / temporal MCC.

## Baselines and validation
Locked test used once; permutation tests (10,000), weekly block bootstrap, Benjamini–Hochberg across 12 events; cross-corpus checks on EDT and FNSPID.

## Results (with page or section references)
- Random/temporal MCC ratio 1.1×–6.5×; trees on rich features worst (§4.1, Fig. 1).
- Frozen FinBERT + LR: ratio 1.1×, best temporal MCC 0.060; fine-tuning raises the gap (size-matched 1.75×) (Table 16).
- Leakage sources named: near-duplicates, overlapping return windows, regime memorisation (§4).
- Clinical-study headlines: random MCC 0.15 vs chronological 0.04 (4.2×); earnings: no leakage and no signal (App. I.2).
- Masking organisation names improves locked-test MCC by 0.04–0.13 on non-M&A events (App. I.3).

## Limits and risks to validity
Mostly 2025 data; near-temporal test only; proprietary corpus (released by the authors). Direction labels only, no trading.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological locked test |
| Baselines | 1 | Several models; majority baseline implicit in MCC |
| Point-in-time and leakage controls | 2 | Subject of the paper |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 64 exchanges but mostly 2025 |
| Statistical testing | 2 | Permutation, bootstrap, BH correction |
| Reproducibility | 2 | Code and data released |
| **Total** | 9/12 → **10/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "it is not a robustness check, it is the primary evaluation" (p. 2)
