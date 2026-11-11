---
type: lit-note
title: "International Stock Return Predictability: On the Role of the United States in Bad and Good Times"
authors: [Boriss Siliverstovs]
year: 2015
venue: "KOF Swiss Economic Institute working paper (read); published in Applied Economics Letters, 2016"
source_url: https://ecomod.net/system/files/StockReturnPredictabilityGoodBad_V01.pdf
doi: 10.1080/13504851.2016.1226485
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12, RQ1.15]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series, information-diffusion, world-model]
---
# On the Role of the United States in Bad and Good Times (Siliverstovs, 2015)

**Basis:** full working paper (Nov 2015) read through a page-fetch summary. No DOI found.

**Takeaway:** An exact replication of [[Rapach 2013 International Return Predictability US Role]] shows that the out-of-sample gain from lagged US returns is concentrated in NBER-dated US recessions (R²OS 4–13%) and is mostly absent or negative in expansions, so the cross-market lead-lag is fragile and regime-dependent.

## Problem
Is the predictive power of lagged US returns for other countries stable across the business cycle?

## Data and period
Monthly excess returns, US plus 10 industrialised countries, 1980M2–2010M12, from Rapach et al.'s website.

## Method
Country return on lagged US return vs historical mean; OLS on a recursive expanding window (initial 1980–84; forecasts 1985M1–2010M12); R²OS (Campbell-Thompson) and Clark-West tests, whole sample and split by NBER recessions/expansions (pp. 3–5).

## Baselines and validation
Historical-mean benchmark; walk-forward recursive evaluation.

## Results (with page or section references)
- Whole sample reproduces Rapach et al. exactly: R²OS −0.7% to 3.8%, 9 of 10 significant (Table 1, p. 8).
- Recessions: R²OS 4.3% (Japan) to 13.2% (Netherlands), 9 of 10 significant (Table 1, p. 8).
- Expansions: R²OS −3.1% to 0.7%; only Sweden and Switzerland significant at 10% (Table 1, p. 8).
- Concludes the original evidence is fragile with respect to the evaluation period (p. 6).

## Limits and risks to validity
_My assessment:_ sub-samples split ex post by NBER dates (not known in real time); no formal test of recession vs expansion difference; sub-sample sizes not reported; unpublished.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Recursive expanding window |
| Baselines | 1 | Historical mean |
| Point-in-time and leakage controls | 1 | Forecasts real-time, but regime split uses ex-post NBER dates |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | 10 countries, 26 forecast years incl. three recessions |
| Statistical testing | 1 | Clark-West |
| Reproducibility | 1 | Uses public data and code |
| **Total** | **8/12 → 9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "the gains to be concentrated in NBER-dated U.S. business cycle recessions" (p. 2)
- "the evidence reported in Rapach et al. (2013) is fragile" (p. 6)

**Citation check (2026-11-08):** DOI 10.1080/13504851.2016.1226485 confirmed through OpenAlex by the reference-lookup tool.
