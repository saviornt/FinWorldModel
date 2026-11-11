---
type: lit-note
title: "Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting"
authors: [Junyi Ye, Gargi Vijay Borde]
year: 2026
venue: "arXiv (q-fin.ST)"
source_url: https://arxiv.org/abs/2608.12251
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.7, RQ1.1, RQ1.6, RQ1.15, RQ4.4]
family: [fusion]
evidence: Strong
score: 11
tags: [lit-note, family/fusion]
---
# Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting (Ye & Borde, 2026)

**Basis:** arXiv v1 (12 Aug 2026), pp. 1–6, 8, via the alphaXiv PDF reader.

**Takeaway:** For 5-day realised volatility of 1,027 US stocks (30 walk-forward quarters, 2018–2025), regime variables helped only when they routed small residual experts on top of a frozen base network; appending the same variables to the inputs lowered IC and made MLPs collapse (30 of 30 seeds), a standard MoE collapsed in 24 of 30 seeds, and soft routing beat every hard regime split — though the total gain over a capacity-matched MLP is small (IC 0.547 vs 0.542; HAR 0.532).

## Problem
Where regime information should enter a neural cross-sectional volatility model, holding information, capacity, tuning and seeds fixed (p. 1).

## Data and period
1,027 US common stocks (Yahoo Finance, Dec 2015–Nov 2025; stocks listed through sample end), replication on 1,552 Japanese TSE Prime stocks. 16 stock features (trailing RV 5/20/60, returns, RSI, last 10 returns); regime variables = 20-day market and idiosyncratic volatility (p. 2).

## Method
RG-ResMoE: frozen base MLP forecast + four zero-initialised residual experts mixed by a soft gate that sees stock features and regime variables; shrinkage and load-balancing penalties (pp. 2–3).

## Baselines and validation
Persistence, per-stock GARCH(1,1), pooled HAR, Ridge, MLP-S, MLP-L (capacity-matched), standard MoE, input-concatenation variants (+z), hard routing (top-1, volatility quantiles, GICS, vol split). Rolling walk-forward: 2-year development (85/15 train/validation), 1-quarter test, 30 windows Apr 2018–Oct 2025 (~1.9M forecasts); 30 seeds; DM-style tests with Newey–West errors; IC, RMSE, R², QLIKE, Kupiec VaR (pp. 2, 4).

## Results (with page or section references)
- IC / QLIKE: persistence 0.502 / 0.799; GARCH 0.520 / 1.120; HAR 0.532 / 0.749; Ridge 0.527 / 0.760; MLP-L 0.542 / 2.23 (3/30 collapses); standard MoE 0.541 / 8,775 (24/30); RG-ResMoE 0.547 / 0.735 (0/30) (p. 5, Table 3).
- Regime variables as inputs: ΔIC −0.0023 (Ridge), −0.0043 with 30/30 collapses (MLP-L); via the gate: +0.0004, 0 collapses (p. 5, Table 4).
- Around the COVID shock the input pathway briefly improved IC then reversed in the recovery; the gate pathway was stable (p. 6, Fig. 2).
- Soft routing beat hard routing by 0.0021–0.0034 IC (all p < 1e-4) (p. 6, Table 5).
- Japan: same ordering; MLP-L(+z) collapsed 28/30 (p. 8, Table 9).

## Limits and risks to validity
Volatility only, compact MLP backbone, two markets (p. 8). _My assessment:_ the panel keeps only stocks listed to the end (survivorship), which mainly flatters level accuracy; effect sizes are small, so the main lesson is about stability and where auxiliary signals enter, not large accuracy gains. Not a text–price fusion study; it informs the mixture-of-experts arm of RQ1.7.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | 30-window rolling walk-forward |
| Baselines | 2 | Persistence, GARCH, HAR, Ridge, capacity-matched MLP |
| Point-in-time and leakage controls | 1 | Train-only normalisation; survivor universe |
| Costs and realism | N/A | Forecast accuracy and VaR, no trading |
| Sample breadth | 2 | 2,579 stocks, two markets, COVID and 2022 |
| Statistical testing | 1 | DM with Newey–West; 30 seeds; no multiple-testing correction |
| Reproducibility | 1 | Public Yahoo data; code not stated |
| **Total** | **9/12 → 11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "the primary value of mixture-of-experts models lies less in increasing model capacity" (p. 1)
