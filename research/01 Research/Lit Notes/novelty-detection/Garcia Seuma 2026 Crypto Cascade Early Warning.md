---
type: lit-note
title: "Where does the criticality live? Early-warning signals are event-heterogeneous across seven crypto-perpetual liquidation cascades"
authors: [Ramon Marc Garcia Seuma]
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2607.27070
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.5, RQ1.8, RQ4.5]
family: [novelty-detection]
evidence: Strong
score: 11
tags: [lit-note, family/novelty-detection]
---
# Where does the criticality live? Early-warning signals across seven crypto liquidation cascades (Garcia Seuma, 2026)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1–13, full paper).

**Takeaway:** Classic critical-slowing-down warnings (rising variance and autocorrelation) do not generalise across seven BTC perpetual-futures crashes: an in-sample pattern inverted out of sample, rising variance was non-specific, and the two sudden-news (tariff) shocks showed no price precursor at all; only a fall in order-flow variance survived a 300-onset placebo test, and only as a population-level, not per-event, signal.

## Problem
Do crashes carry a reproducible early-warning signature, and in which state variable (price, leverage, order flow)?

## Data and period
Binance BTCUSDT perpetuals around seven cascades, May 2022–Oct 2025 (LUNA, FTX, yen-carry unwind, Dec 2024, Feb 2025 tariff scare, Apr 2025, Oct 2025 $19bn event); 1-minute prices, 5-minute open interest, long/short ratios and taker flow; all public (p. 3).

## Method
Causal detrending (trailing mean); rolling variance and lag-1 autocorrelation; Kendall-τ trend test into the onset; 39-configuration sweep of detrend, rolling and pre-window choices; hypothesis formed on Oct 2025 tested on Aug 2024, then all seven; placebo null of 300 ordinary-market onsets (pp. 2–4, 8).

## Baselines and validation
Event-level out-of-sample test plus placebo null; consistent onset definition (p. 4). Not a forecasting model; no false-alarm rate per unit time.

## Results (with page or section references)
- Oct 2025: price autocorrelation rises in only 4/39 configurations; variance rises for nearly all variables, so it does not discriminate (pp. 5–6, Table 1).
- The Oct 2025 pattern (signal in leverage/flow, not price) inverts in Aug 2024 (price 28/39; open interest 3/39) (Table 2, p. 8).
- Across seven events no variable is invariant; price signature present in five, absent in the two sudden-news tariff shocks (Feb 2025 silent in every variable) (Table 3, pp. 7–8).
- Taker-flow variance falls before all six events with data; placebo sign test p ≈ 0.014, Fisher p ≈ 5×10⁻⁶; two of six events individually overlap the null (p. 8).
- Interpretation: shock-driven discontinuous transitions, not critical ones; consistent with Guttal et al. (2016) for equity meltdowns (pp. 2, 10–11).

## Limits and risks to validity
_My assessment:_ seven events on one venue; liquidations themselves not observable; the two-type typology (endogenous build-up vs exogenous news shock) is a hypothesis at n = 2 in one class (p. 10). The design (multi-configuration sweep, out-of-sample event, placebo null, public code) is a model for evaluating any shock detector. Score is high for design quality, not for breadth.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Hypothesis from one event tested on others |
| Baselines | 1 | 300-onset placebo null; no competing detector |
| Point-in-time and leakage controls | 2 | Causal detrending; fixed onset rule |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Seven cascades, one asset and venue |
| Statistical testing | 2 | Kendall tests across 39 configs, placebo, combined p-values |
| Reproducibility | 2 | Public data and scripted pipeline |
| **Total** | **9/12 → 11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "Single-event critical-slowing-down claims in crypto derivatives are therefore fragile by construction." (p. 1)
- "Out-of-sample testing is not a robustness appendix in this literature" (p. 10)
