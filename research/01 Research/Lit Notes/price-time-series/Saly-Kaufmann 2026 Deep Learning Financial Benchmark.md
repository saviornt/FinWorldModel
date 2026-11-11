---
type: lit-note
title: "How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjusted performance"
authors: [Adir Saly-Kaufmann, Kieran Wood, Jan Peter-Calliess, Stefan Zohren]
year: 2026
venue: "arXiv preprint (read); published in Journal of Forecasting"
source_url: https://arxiv.org/abs/2603.01820
doi: 10.1002/for.70233
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.1, RQ4.6]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series]
---
# How Do Standard Time Series Forecasting Benchmarks Translate to Finance? (Saly-Kaufmann, 2026)

**Basis:** first read through alphaXiv's structured report (2026-11-07). **Checked against the PDF (v2, 22 Oct 2026) on 2026-11-08** (pp. 1, 8–10, 13–14, 17, 19, 31, 40, 46–47). Corrections: data span and test period, LPatchTST Sharpe (2.29, not 2.31), code is available (Git repository linked, p. 1), and portfolio-level net-of-cost curves exist (not only break-even).

**Takeaway:** In a Sharpe-optimised, volatility-targeted multi-asset futures setting (out of sample 2010–2024), gated recurrent and hybrid models (VSN+LSTM Sharpe 2.40, LSTM+PatchTST 2.29, TFT 2.27) beat linear baselines, while generic Transformers and state-space models (iTransformer 0.38, Mamba 0.36, PatchTST 0.75) do no better than an AR(1) benchmark (0.77).

## Problem
Whether architectures that win generic forecasting benchmarks also win on noisy financial data when judged by risk-adjusted returns (report §2–3).

## Data and period
Daily back-adjusted continuous futures and FX across bonds, commodities, energy, FX and equity indices, 1990–2024; initial training 1990–2010, out of sample 2010–2024 (the paper also labels it 2010–2025) (p. 8). Vendor named as Pinnacle Data Corp. in the alphaXiv report; not confirmed on the pages read.

## Method
16 architectures (AR1x, DLinear, NLinear, iTransformer, PatchTST, Mamba, Mamba2, LSTM, xLSTM variants, VSN hybrids, TFT) map features (multi-horizon returns, MACD) to positions in [−1, 1]; loss is negative Sharpe; 10% volatility target (report §4).

## Baselines and validation
AR(1), ARn, DLinear, NLinear; passive long-only for relative metrics. Walk-forward, retrained every five years on a rolling window; same evaluation days for every model; validation = last 10% of training; grid search on validation Sharpe (pp. 8, 31). HAC t-statistics, pairwise t-tests, sub-periods, break-even and portfolio-level costs, seed and parameter-count robustness.

## Results (with page or section references)
- Sharpe 2010–2024: VLSTM 2.40, LPatchTST 2.29, TFT 2.27, xLSTM 1.79, LSTM 1.48; AR1x 0.77, PatchTST 0.75, Mamba2 0.80, iTransformer 0.38, Mamba 0.36 (Table 1, p. 9).
- VLSTM: 24.0% annual return at 10% vol target, HAC t = 8.81, hit 58.8%, information ratio vs passive 0.85 (t = 3.31) (Table 2, pp. 10, 14).
- Linear models do well in some high-volatility years (2014, 2020) but are unstable (Table 12, p. 47).
- Net of 0–5 bp per trade the ranking of the leading models is unchanged; Mamba2 and iTransformer lose virtually all gross advantage (p. 14). xLSTM has the largest portfolio break-even cost buffer (p. 17); liquid bond futures have break-evens near 0–1 bp (Table 10, p. 40).
- Rankings hold with fewer seeds (Table 4, p. 17) and with every model constrained to 1–2M parameters (p. 31).

## Limits and risks to validity
Authors: results conditional on this dataset and period (p. 8). _My assessment:_ headline Sharpe ratios are gross; costs as a flat per-trade bp range; trend-style features on futures, so the result is about position-sizing models, not single-stock return forecasts; no GBT or plain time-series-momentum baseline; one five-year retraining cadence.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling windows, out-of-sample 2010–2025 |
| Baselines | 1 | AR(1) and linear models, passive; no GBT or plain momentum |
| Point-in-time and leakage controls | 0 | Walk-forward, but no explicit leakage checks on the pages read |
| Costs and realism | 1 | Flat 0–5 bp per trade plus break-even analysis |
| Sample breadth | 2 | Multi-asset, 15 years incl. 2020 |
| Statistical testing | 1 | HAC t-stats; no multiple-testing correction stated |
| Reproducibility | 1 | Code repository linked (p. 1); data licensed |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "underperformed a simple AR(1) benchmark in a realistic financial forecasting task" (abstract, p. 1)

**Citation check (2026-11-08):** DOI 10.1002/for.70233 confirmed through OpenAlex by the reference-lookup tool.
