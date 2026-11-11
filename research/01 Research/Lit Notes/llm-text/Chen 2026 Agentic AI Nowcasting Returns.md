---
type: lit-note
title: "Autonomous Market Intelligence: Agentic AI Nowcasting Predicts Stock Returns"
authors: [Zefeng Chen, Darcy Pu]
year: 2026
venue: arXiv 2601.11958
source_url: https://arxiv.org/abs/2601.11958
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.2, RQ4.5]
family: [llm-text]
evidence: Moderate
score: 8
tags: [lit-note, family/llm-text]
---
# Autonomous Market Intelligence (Chen, 2026)

**Basis:** v1 (17 Jan 2026), page excerpts via alphaXiv (pp. 1–2, 4, 7–11, 13, 16–17, 29–30, 36).

**Takeaway:** A live, web-searching LLM scoring every Russell 1000 stock each night (Apr 2025–Jan 2026) picks top winners (top-20 value-weighted: daily six-factor alpha 18.4 bp, Sharpe 2.43) but cannot pick losers; the design is free of look-ahead because predictions are logged before outcomes exist.

## Problem
Can an agentic LLM nowcast returns when it chooses its own information in real time?

## Data and period
Russell 1000, daily, April 2025–January 2026 (~155,000 predictions); signals logged after the close, returns open-to-open (pp. 8, 10–13).

## Method
Web interface of a leading US LLM with search enabled; attractiveness score −5 to +5 plus price, EPS and sentiment outputs; value-weighted top-20 and rank-sorted portfolios (pp. 10–11, 17).

## Baselines and validation
Fama–French five factors plus momentum; Russell 1000 benchmark; Newey–West errors (pp. 2, 29). Repeat-query reliability tests (split-half ρ = 0.94) (p. 16). No ML baselines.

## Results (with page or section references)
- Top-20 VW: ~50% vs ~26% for the Russell 1000 over nine months; alpha 0.184%/day (t = 2.46); Sharpe 2.43 (p. 2).
- Bottom-ranked portfolios: alpha not different from zero (pp. 1, 4).
- Costs ~1.6 bp per trade, under 10% of gross alpha (p. 30).

## Limits and risks to validity
_My assessment:_ nine months in one rising market; the model version changes over the sample ("latest version"); many portfolio cuts without multiple-testing correction; cannot be re-run, which also means it cannot be checked. Preliminary draft.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Live, one period |
| Baselines | 1 | Factor models only |
| Point-in-time and leakage controls | 2 | Live logging by construction |
| Costs and realism | 1 | Spread-based estimate; no impact |
| Sample breadth | 1 | Russell 1000, nine months |
| Statistical testing | 1 | Newey–West; no correction |
| Reproducibility | 1 | Data posted on GitHub |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "AI possesses genuine stock selection ability, but only for identifying top winners." (abstract, p. 1)
