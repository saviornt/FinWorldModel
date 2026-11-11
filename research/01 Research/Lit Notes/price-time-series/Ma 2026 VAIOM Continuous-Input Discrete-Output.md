---
type: lit-note
title: "VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling"
authors: [Yiming Ma, Xinyu Chen]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2607.13929
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.10, RQ1.13]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, tokenization]
---
# VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling (Ma, 2026)

**Basis:** alphaXiv structured report plus PDF pages 1, 10, 15, 17, 19, 21–22, 25, 28–29, 33–34 (v1). Numbers below are from the PDF pages. Institutional affiliation not stated in the pages read.

**Takeaway:** In a small decoder-only model on 1-hour FX bars, feeding continuous event vectors in and predicting 16 return buckets out beats a fully tokenized input (~0.01 bits/event on validation) and beats Frequency, Markov and single-bar LightGBM baselines on 2025 test data by 0.02–0.04 bits/event.

## Problem
Market observations are continuous and heavy-tailed, while next-token models expect discrete inputs. Does discretising the input lose signal when the output stays categorical? (p. 1; §1)

## Data and period
11 FX and spot-metal assets, 1H bars built from Dukascopy 1-minute data. Train before 2024; 2024H1 buffer; 2024H2 validation; 2025H1 and 2025H2 test (Table 13, p. 29; §4, p. 19).

## Method
Target: next return normalised by EWMA volatility (span 20), mapped to 16 buckets with fixed tail cutoffs (±2, 3, 5, 8σ) and train-fitted interior quantiles (p. 10). Inputs: DiscIn (15 categorical fields), ContIn (25 numeric fields, clipped to [−32, 32]) or HybridContIn (ContIn + asset/class/timeframe embeddings) (§3.5, p. 10). 4-layer causal Transformer, 0.9M parameters; mixture-of-market-states output head; Gap, VolReg and Ordinal auxiliary losses; full-sequence supervision (Table 11, p. 28).

## Baselines and validation
Frequency (Laplace-smoothed), first-order Markov, and LightGBM on the last bar's features with no sequence context, all fitted on train (§3.11, p. 15). Single chronological split; ablations on validation only; test used once (§4, p. 19). Paired block bootstrap by asset-month, 10,000 replicates; three training seeds (§3.13, p. 17).

## Results (with page or section references)
- Input representation: 1H validation NLL DiscIn 3.1633 vs pure ContIn 3.1536 bits/event (−0.0097); 1D 3.1743 vs 3.1649 (Table 5, p. 21). Authors note fields are not matched, so this is not a clean estimate of continuity alone (§4.2, p. 21).
- Adding identity metadata: 3.1488 → 3.1465 (Table 6, p. 22).
- Test vs LightGBM: gains +0.0177 to +0.0426 bits/event across 3 seeds and two halves; all 95% intervals exclude zero; block win-rates 71–92% (Table 4, p. 21; Table 26, p. 34).
- Capacity: 0.9M beats 5M and 15M on validation (3.1542 vs 3.1580 vs 3.1607) (Table 10, p. 25).
- Ordinal auxiliary loss helps (3.1719 → 3.1673 at 5M) (Table 22, p. 33).

## Limits and risks to validity
_My assessment:_ the gains are small in absolute terms (~1% of NLL) and the strongest baseline has no sequence context; no GARCH-type density baseline; one market and one test year; authors state likelihood gains are not trading profits. Code/data release not stated in the pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split; test untouched until the end |
| Baselines | 1 | Frequency, Markov, single-bar LightGBM; no GARCH/sequence GBT |
| Point-in-time and leakage controls | 2 | All preprocessing fitted on train; buffer period; masks |
| Costs and realism | N/A | Likelihood only, no trading claim |
| Sample breadth | 1 | 11 FX/metal assets, one test year |
| Statistical testing | 1 | Block bootstrap CIs, 3 seeds; no multiple-testing correction |
| Reproducibility | 0 | Not stated in the pages read |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "They do not constitute a field-matched causal estimate of continuity alone." (§4.2, p. 21)
