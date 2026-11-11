---
type: lit-note
title: "News implied volatility and disaster concerns"
authors: [Asaf Manela, Alan Moreira]
year: 2017
venue: Journal of Financial Economics 123(1), 137–162
source_url: https://amoreira2.github.io/alan-moreira.github.io/NVIX_published.pdf
doi: 10.1016/j.jfineco.2016.01.032
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.5, RQ1.8]
family: [novelty-detection]
evidence: Moderate
score: 7
tags: [lit-note, family/novelty-detection]
---
# News implied volatility and disaster concerns (Manela, 2017)

**Basis:** published JFE version (author copy) read through alphaXiv page excerpts (pp. 137–144).

**Takeaway:** A support-vector regression from Wall Street Journal front-page word frequencies to VIX (NVIX) extends implied volatility back to 1890; it fits VIX out of sample only modestly (R² 0.19), predicts higher returns at 6–24 months and a higher one-year disaster probability (+2.5 pp per s.d.), and missed the March 2000 tech crash.

## Problem
Can newspaper coverage measure investors' disaster concerns over a century, and do those concerns predict returns and disasters?

## Data and period
Titles and abstracts of all WSJ front-page articles, Jul 1889–Dec 2009; 468,091 one- and two-word n-grams, monthly frequencies (p. 140). VXO/VIX from 1986; CRSP and Dow Jones returns (p. 143).

## Method
SVR of VIX on n-gram frequencies; train 1996–2009, test 1986–1995, predict pre-1986 (p. 140). Return-predictability regressions on NVIX², skipping a month; Newey–West and generated-regressor (Murphy–Topel) standard errors (p. 144). Bayesian disaster-timing model for 1896–1944; topic decomposition into war, government, financial intermediation, stock markets, natural disasters (p. 138).

## Baselines and validation
Out-of-sample VIX fit on 1986–1995 (one split). Controls for contemporaneous and forward-looking volatility measures; other text measures (EPU, Loughran–McDonald) compared (p. 138).

## Results (with page or section references)
- Out-of-sample VIX fit: R² 18.5%, RMSE 7.48 vol points; slope 0.82 (t 4.01 vs zero) (Table 1, p. 141).
- +1 s.d. NVIX² → +3.3 pp annualised excess return over the next year; significant at 6–24 months, R² 2–5% (Table 3, p. 144).
- +1 s.d. NVIX → +2.5 pp probability of a disaster over the next year (p. 138).
- Priced variation comes mostly from war (53%) and government (27%) words; stock-market words drive much of NVIX but are not priced (p. 138).
- NVIX peaks in the 1929 crash, wars and financial crises, but is absent for the March 2000 tech crash (p. 141).

## Limits and risks to validity
_My assessment:_ monthly, slow-moving risk-premium measure, not an early alarm; small R²; the SVR is trained on a later period than it is applied to (authors argue the bias works against them, p. 140). Few disasters, so disaster-prediction evidence rests on a handful of episodes. Data are public on the authors' site.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One train/test split for the text model |
| Baselines | 1 | VIX, realised-volatility and text-index controls |
| Point-in-time and leakage controls | 1 | One-month skip; train period after predict period |
| Costs and realism | N/A | No strategy |
| Sample breadth | 1 | One market, 1890–2009, many crises |
| Statistical testing | 1 | NW and generated-regressor errors |
| Reproducibility | 1 | NVIX data published |
| **Total** | **6/12 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Absent, however, is the burst of the tech bubble in March 2000." (p. 141)
