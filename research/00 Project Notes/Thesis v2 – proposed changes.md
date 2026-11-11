---
type: project-note
title: Thesis v2 – proposed changes
status: proposed
created: 2026-11-09
updated: 2026-11-09
related:
  - "[[Project Thesis - A Framework for Real-Time Time-Series Forecasting, Portfolio Optimization, and Automated Trading]]"
  - "[[Multimodal Financial Forecasting and Shock Detection (Final)]]"
  - "[[RP5 Vault Review]]"
  - "[[Financial Foundation Model Research Direction]]"
tags:
  - project-note
  - thesis
---
# Thesis v2 – proposed changes

What the research supports changing in [[Project Thesis - A Framework for Real-Time Time-Series Forecasting, Portfolio Optimization, and Automated Trading]] (v1), for review at the methodology stage. v1 is left untouched. These are proposals drawn from the evidence, not decisions; the methodology plan decides. The verdicts behind each line are in [[RP5 Vault Review#RP5.1 – Project Thesis claims|RP5.1]] and the [[Multimodal Financial Forecasting and Shock Detection (Final)]].

## Changes the evidence supports

| # | v1 says | Proposed v2 | Evidence |
| --- | --- | --- | --- |
| 1 | The aim is "consistent profitability in volatile markets" | State a forecasting target, horizon and success test instead, for example: beat a random walk on returns (Clark–West), HAR on volatility (QLIKE), a GARCH-t or conditional EVT model on VaR/ES, a plain logit on crisis warning; net Sharpe against 1/N only if a trading layer is built | Not supported: gross gains turn negative at realistic costs in the best tests (RP4 RQ4.6; RP5.1). Synthesis section 2, Q1 |
| 2 | Real-time, multi-horizon forecasting with horizons and parameters adjusted by portfolio returns | Multi-horizon forecasting of risk first (volatility, tails), returns second; horizons and parameters chosen inside nested validation with every trial counted | Risk is forecastable, direction barely is (RP1 cross-cutting 2); choosing settings by realised returns is a search needing a trial correction (RP4 RQ4.1, RQ4.2) |
| 3 | "Real time" as an edge | Drop real-time speed as a source of edge on public scheduled news; focus on slower channels: linked firms, small and thinly covered stocks, repeated news, monthly cross-market lead-lag | Liquid scheduled news is priced in milliseconds to seconds (RP1 RQ1.12) |
| 4 | Core model family not tied to a baseline | Name the mandatory baselines per target (random walk, GBT, HAR, GARCH-t/EVT, logit, 1/N, frozen model, periodic retraining) and require the main model to beat them under the RP4 protocol | RP1 cross-cutting 1; RP4 protocol table |
| 5 | TD3 agent with A\* planning and MAML adaptation | Replace with forecast-then-decide: a forecaster feeding a transparent allocation rule; adaptation by periodic retraining unless another method beats it leak-free | RP1 RQ1.9 (High, negative for RL); RP4 RQ4.9; RP5.5 (prototype Not supported, with target leakage) |
| 6 | Model scope | Adopt the [[Financial Foundation Model Research Direction]] as the model hypothesis (autoregressive, LLM-inspired, no LLM inside), framed as experiments: continuous vs token inputs, categorical bucket output, gated world-state inputs, each against price-only | RP5.7 (Partly supported); Synthesis section 8 |
| 7 | Data sources implied but not named | Name sources whose terms allow storage and training (EDGAR, BLS, GDELT, USGS, GLEIF), a price API pending written training terms, and a survivorship-free daily reference | RP2 RQ2.6, RQ2.7; Synthesis section 3 |
| 8 | No data-integrity section | Add the integrity rules: knowledge time stamped in-house, dated permanent IDs, earliest-public text time, encoder cutoffs before the test window, past-only imputation, no shuffled splits | RP3 cross-cutting; RP4 rules a–g; Synthesis section 4 |
| 9 | Shock handling implied as prediction | State the shock aim as fast detection after onset, spread along supply chains, and a slow fragility gauge over months to years, not prediction of timing | RP1 RQ1.5, RQ1.8 (High) |
| 10 | Sentiment module as an input | Keep FinBERT-style scoring; fit any mixing weights against returns or volatility on training data; test VADER's share; record encoder cutoffs; add a return-based test | RP5.2, RP5.3 |

## Left open (Untested; needs its own test before v2 relies on it)

- Black-Litterman and robust Bayesian allocation fed by ML views; test against 1/N net of costs (RP5.1).
- Captum attributions; would need placebo checks (RP5.1; RP1 RQ1.7).
- Stop-loss, buying-power and cash-threshold execution rules; staged paper trading suggested by the backtest-to-live gap (RP5.1).
- CuPy, Celery and the async stack: engineering choices outside the research.

## Next step

Review at the methodology stage together with the [[Multimodal Financial Forecasting and Shock Detection (Final)]] section 7 questions.
