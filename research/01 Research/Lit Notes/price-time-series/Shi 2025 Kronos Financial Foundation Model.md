---
type: lit-note
title: "Kronos: A Foundation Model for the Language of Financial Markets"
authors: [Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, Jian Li]
year: 2025
venue: AAAI 2026 (arXiv 2508.02739)
source_url: https://arxiv.org/abs/2508.02739
doi: 10.1609/aaai.v40i30.39730
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.1, RQ1.10, RQ1.13, RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series]
---
# Kronos: A Foundation Model for the Language of Financial Markets (Shi, 2025)

**Basis:** full text via alphaXiv (§1–4, Appendices A–F). AAAI proceedings page in the guide not opened; the arXiv version was read.

**Takeaway:** A finance-only K-line foundation model (tokenised OHLCVA, 12 billion records) beats generic TSFMs and deep baselines on IC/RankIC and beats GARCH on realised-volatility MAE, in a single post-June-2024 test window without significance tests.

## Problem
Generic TSFMs contain under ~1% financial data and often lose to non-pretrained models on finance tasks (§1; App. A Table 3).

## Data and period
Pretraining: >12 billion K-line records, 45 exchanges, 7 frequencies, up to June 2024. Test from July 2024 on stocks from nine exchanges, Binance crypto and >1,000 forex pairs (App. B, D).

## Method
Transformer tokenizer quantises each OHLCVA bar into coarse and fine subtokens; decoder-only Transformer (up to ~0.5B parameters) trained by next-token prediction (§3).

## Baselines and validation
25 baselines: 8 deep full-shot models, 5 zero-shot TSFMs, ARCH/GARCH (BIC-selected) for volatility, 3 generative models (App. D). Single temporal split. No random-walk or GBT baseline for price/return tasks. No significance tests (not in the part I read).

## Results (with page or section references)
- Price forecasting RankIC +93% vs best TSFM, +87% vs best non-pretrained model (Abstract).
- Realised-volatility MAE 9% lower than the best baseline (Abstract; Fig. 4c).
- Investment simulation on CSI 300/800 with 0.15% per-trade cost: Kronos-large average AER 0.2084, IR 1.6491; Chronos-large −0.0302 (Table 10, App. E–F).
- Absolute IC levels are small (Kronos-small price IC 0.0431, return IC 0.0665; Table 2).

## Limits and risks to validity
_My assessment:_ one test window starting July 2024 with no statistical tests; IC is the headline metric, not error against a random walk; backtest only in Chinese A-shares; author-run baselines with two hyperparameter sets each. Weights and code are public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single split after pretraining cutoff |
| Baselines | 1 | GARCH for volatility; no random walk or GBT for returns |
| Point-in-time and leakage controls | 1 | Explicit temporal separation; not otherwise checked |
| Costs and realism | 1 | Flat 0.15% per trade, turnover limits |
| Sample breadth | 1 | Many assets but one short regime |
| Statistical testing | 0 | None reported |
| Reproducibility | 1 | Code and weights; data not |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "general-purpose TSFMs often under-perform specialized, non-pre-trained models" (§1, p. 2)

## Update 2026-11-07 – tokenizer evidence for RQ1.10 (PDF pp. 3–4, 6–7, 16, 18–19 read via alphaXiv)
- Tokenizer: Transformer autoencoder with Binary Spherical Quantization; k = 20 bits split into coarse and fine 10-bit subtokens, predicted sequentially (§3, pp. 3–4; Table 1, p. 4).
- Paradigm ablation at comparable size (Table 2, p. 6): continuous Direct-AR (MSE) price IC 0.0212, return IC 0.0416, volatility MAE 0.0565; continuous Prob-AR (Student-t mixture NLL) 0.0179 / 0.0356 / 0.0464; Kronos-Parallel (discrete, subtokens predicted together) 0.0345 / 0.0529 / 0.0461; Kronos-small (discrete, sequential) 0.0431 / 0.0665 / 0.0384. Variant details in App. D (p. 16).
- Larger vocabularies (2^14 → 2^20) improve both reconstruction and forecasting (Fig. 6, p. 7). Averaging more sampled paths raises IC (Fig. 7, p. 7).
- Codebook use 97.66% (coarse) and 85.25% (fine); rare tokens decode to extreme K-bars (Table 11, p. 19).
- Tokenizer ablation: Transformer vs CNN tokenizer reconstruction MAE 0.0785 vs 0.0916 (Table 9, p. 18).
- _My assessment:_ the continuous variants are author-built baselines, untuned as far as stated, on one post-2024 window with no tests; the ablation favours discrete prediction but does not test continuous input with a categorical output (the VAIOM design).

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
