---
type: lit-note
title: "Dynamics of market correlations: Taxonomy and portfolio analysis"
authors: [J.-P. Onnela, A. Chakraborti, K. Kaski, J. Kertész, A. Kanto]
year: 2003
venue: Physical Review E 68 (arXiv cond-mat/0302546)
source_url: https://arxiv.org/abs/cond-mat/0302546
doi: 10.1103/PhysRevE.68.056110
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.7]
family: [graph]
evidence: Weak
score: 5
tags: [lit-note, family/graph, correlation-network, time-valid-graph]
---
# Dynamic Asset Trees (Onnela, 2003)

**Basis:** arXiv cond-mat/0302546v1 pages 1–4, 7–9, 11 read via alphaXiv on 2026-11-08. Journal (Phys. Rev. E) not opened; DOI not looked up.

**Takeaway:** Minimum spanning trees of rolling four-year return correlations (477 NYSE stocks, 1980–1999, monthly steps) are mostly stable from one window to the next but reorganise sharply around crashes (shorter trees, higher mean correlation), and half of the edges decay within about 0.12 × the window length; window length is a direct trade-off between noise and staleness.

## Problem
How do correlation-based stock networks change over time?

## Data and period
CRSP split-adjusted daily closes, 477 NYSE stocks, 1980-01-02 to 1999-12-31 (p. 2).

## Method
Correlation distance d = √(2(1−ρ)); MST per window; T = 1000 days, step ≈ 21 days (195 windows); tree length, central vertex, survival ratios, half-life (pp. 2–9).

## Baselines and validation
Descriptive; no forecasting test.

## Results (with page or section references)
- Mean correlation and tree length correlate at −0.98 (p. 3).
- Single-step edge survival high except two dips around Black Monday (Fig. 7, p. 8).
- Edge half-life t½ ≈ 0.12 T for 1–5-year windows (p. 9).
- The Black Monday effect appears over 1986–1990, centred on the crash (p. 2), which implies windows are not dated at their last day; a point-in-time feature must be stamped at the window's end.

## Limits and risks to validity
Survivor universe (stocks traded over the whole 20 years); descriptive only; window dating not point-in-time (my reading of p. 2).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Descriptive |
| Baselines | N/A | |
| Point-in-time and leakage controls | 0 | Survivors; centred dating |
| Costs and realism | N/A | |
| Sample breadth | 2 | 477 stocks, 20 years incl. 1987 crash |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Standard data, no code |
| **Total** | 3/8 → 5/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
