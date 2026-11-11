---
type: lit-note
title: "Small Vocabularies, Big Gains: Pretraining and Tokenization in Time Series Models"
authors: [Alexis Roger, Gwen Legate, Kashif Rasul, Yuriy Nevmyvaka, Irina Rish]
year: 2025
venue: arXiv (AAAI-format preprint)
source_url: https://arxiv.org/abs/2511.11622
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.10]
family: [price-time-series]
evidence: Weak
score: 2
tags: [lit-note, family/price-time-series, tokenization]
---
# Small Vocabularies, Big Gains: Pretraining and Tokenization in Time Series Models (Roger, 2025)

**Basis:** full text via alphaXiv (v1, 6 Nov 2025; page numbers not shown, sections cited).

**Takeaway:** Chronos-style mean scaling with uniform bins wastes vocabulary; standard scaling with uniform bins keeps error low even at 512 tokens, while the Chronos default degrades sharply (MASE 4.868 vs 2.342 at 512 tokens), and the three schemes converge at 4,096 tokens.

## Problem
How do scaling and quantisation choices, vocabulary size and LLM-weight initialisation interact in tokenized time-series models? (Introduction)

## Data and period
GIFT-Eval pretraining data; MASE on GIFT-Eval (Training Results). Non-financial; authors include Morgan Stanley researchers.

## Method
Three scalings (mean, min–max, standard) × three binnings (uniform, normal-CDF, exponential-decay); theoretical error with a perfect bin predictor; Qwen3 600M trained with vocabularies 512/1024/4096 from pretrained or random weights (Theoretical Foundation; Training Results).

## Baselines and validation
Chronos-T5 Large shown as a reference point only (Fig. 2). No statistical tests; correlation analysis on three points per cell (Table 1).

## Results (with page or section references)
- Theoretical error follows a power law in vocabulary size with the same slope for all tokenizers (Fig. 1).
- Pretrained, 512 tokens: mean+uniform MASE 4.868; normal+uniform 2.342; mean+normal 2.813. At 4,096: 2.473 / 2.594 / 2.554 (Table 2).
- Pretrained LLM weights help most with small vocabularies; misaligned tokenisation can cancel or invert the benefit (Abstract; Table 2).
- Authors recommend standard scaling with uniform bins, especially when a vocabulary is shared across modalities (Discussion).

## Limits and risks to validity
_My assessment:_ one dataset family, one backbone, one run per cell; the authors call the evaluation a "synthetic task setting" (Limitations). Useful for tokenizer design, not as proof.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | GIFT-Eval held-out evaluation |
| Baselines | 0 | Only a Chronos reference point |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Multi-domain benchmark |
| Statistical testing | 0 | None meaningful |
| Reproducibility | 0 | Code "will be released" |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "misaligned tokenization can diminish or even invert the benefits of pre-training" (Abstract)
