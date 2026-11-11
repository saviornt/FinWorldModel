---
type: lit-note
title: "Regime-Aware Financial Volatility Forecasting via In-Context Learning"
authors: [Saba Asaad, Shayan Mohajer Hamidi, Ali Bereyhi]
year: 2026
venue: ICLR 2026 workshop (arXiv cs.LG)
source_url: https://arxiv.org/abs/2603.10299
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.9, RQ1.2]
family: [rl-planning]
evidence: Weak
score: 5
tags: [lit-note, family/rl-planning, in-context-learning]
---
# Regime-Aware In-Context Learning for Volatility (Asaad, 2026)

**Basis:** Full PDF read through alphaXiv, pp. 1–9, 11.

**Takeaway:** Prompting gpt-4o-mini with five demonstrations drawn by an estimated volatility regime (no fine-tuning) cut next-day high-volatility MAE about 27% versus GJR-GARCH on the S&P 500 and gave the lowest overall MAE on three series, but HAR stayed best in calm periods, overall gains over HAR were small (S&P 500 MAE 1.14 vs 1.17), and the LLM's memory of these well-known series was not controlled.

## Problem
Can a frozen LLM adapt to volatility regimes purely through which in-context examples it is shown (pp. 1–2)?

## Data and period
Daily S&P 500, NASDAQ Composite (Stooq) and EUR/USD; target = squared daily log return; 70/30 chronological split; exact dates not stated (p. 6).

## Method
Oracle-guided refinement on training data builds a pool of 500 regime-labelled demonstrations; at test time the regime is estimated from the last three squared returns and five demonstrations sampled with a regime-dependent prior; 7-day input window (pp. 3–7).

## Baselines and validation
Rolling mean, HAR, GARCH(1,1), GJR-GARCH, one-shot LLM, random demonstrations; MAE and RMSE overall and by regime (80th-percentile split) (pp. 6–7).

## Results (with page or section references)
- S&P 500 MAE: HAR 1.17, GJR-GARCH 1.33, one-shot LLM 1.72, random demos 1.22, regime-aware 1.14; MAE in high regime 4.85 / 3.76 / 5.09 / 3.12 / 2.73 (Table 1, p. 8).
- HAR has the lowest low-regime MAE on all three series (0.25, 0.44, 0.07) (Table 1).
- One-shot prompting under-reacts to spikes and is worst of the LLM variants (pp. 7–8).

## Limits and risks to validity
_My assessment:_ gpt-4o-mini's training data covers much of these index histories and the test dates are not given, so memorisation is uncontrolled (rubric cap: Weak); squared daily returns are a very noisy target; no significance tests; one split. In-context selection is a cheap adaptation mechanism worth testing, but this paper does not prove it.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One 70/30 split |
| Baselines | 2 | HAR, GARCH, GJR-GARCH, rolling mean |
| Point-in-time and leakage controls | 0 | LLM memorisation not addressed |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Three series |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code link seen |
| **Total** | **4/12 → 5/14** | Weak (also capped by the memorisation rule) |

## Quotes worth keeping (each under 15 words, with page)
- "naive in-context learning faces similar limitations as those in conventional volatility forecasting" (p. 2)
