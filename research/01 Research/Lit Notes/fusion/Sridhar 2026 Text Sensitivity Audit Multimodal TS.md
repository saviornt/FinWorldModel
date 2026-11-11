---
type: lit-note
title: "Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting"
authors: [Karthik Sridhar, Atharva Gupta, Nishant Pradhan, Murari Mandal, Dhruv Kumar, Saurabh Deshpande]
year: 2026
venue: "arXiv (cs.CL); ICML 2026 Workshop on Foundation Models for Structured Data"
source_url: https://arxiv.org/abs/2608.22321
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.7, RQ4.4, RQ1.14]
family: [fusion]
evidence: Moderate
score: 7
tags: [lit-note, family/fusion]
---
# Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting (Sridhar et al., 2026)

**Basis:** arXiv v1 (23 Aug 2026), pp. 1–5, 11–14, via the alphaXiv PDF reader.

**Takeaway:** On Time-MMD, replacing the text fed to AURORA (cross-attention foundation model), MM-TSFLIB (late fusion) and TATS (early fusion) with empty, constant, shuffled, cross-domain or oracle text moved MSE by under 0.5%; the published "multimodal lift" came from a numeric prior column routed through the same fusion path, so a text-on vs text-off ablation does not show that text content is used.

## Problem
Whether multimodal forecasters respond to what the text says, or to other inputs sharing the text pathway (p. 1).

## Data and period
Time-MMD (nine domains incl. Economy; public reports paired with numeric series), four horizons, three seeds, eight backbones for the two trained paradigms (pp. 2–3).

## Method
Hold each model at its released configuration; swap text through five substitutes; 2×3 factorial crossing text conditions with zeroing a co-shipped numeric column p; gradient, attention-entropy and divergence probes of AURORA's text pathway; paired bootstrap CIs (10,000 resamples) (pp. 2–4, 14).

## Baselines and validation
Each model's own unimodal configuration; standard Time-MMD splits (p. 2).

## Results (with page or section references)
- Text substitutions changed mean MSE by at most +0.16% (MM-TSFLIB, constant text); TATS within ±0.001%, AURORA within ±0.05% (p. 3, Table 2).
- Unimodal lifts are real (+1.87% MM-TSFLIB, +7.54% TATS) but disappear when p is zeroed with text intact; in TATS half the forecast is literally p (pp. 3–4, Table 3).
- Lift varied by an order of magnitude across backbones (TATS +1.2% to +15.0%) (p. 3).
- AURORA's text pathway is trained (non-zero gradients) but content-blind (attention entropy ≈ 0.975 in every condition) (p. 4).

## Limits and risks to validity
One benchmark (not equity returns), frozen-encoder architectures only; numeric oracle limited by sub-word tokenisation of numbers (p. 4). _My assessment:_ transfers directly as an evaluation rule for any text–price model: test with shuffled and placebo text, and isolate numeric side channels.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Benchmark splits |
| Baselines | 1 | Unimodal configurations; perturbation controls |
| Point-in-time and leakage controls | 0 | Not addressed (contamination of AURORA noted, p. 11) |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | 9 domains, 8 backbones, 3 models |
| Statistical testing | 1 | Paired bootstrap CIs and p-values |
| Reproducibility | 2 | Code and harness released; public data |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "what looks like a text gain may be something else entirely." (p. 4)
