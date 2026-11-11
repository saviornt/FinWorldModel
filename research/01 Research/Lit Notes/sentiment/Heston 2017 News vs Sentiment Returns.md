---
type: lit-note
title: "News vs. Sentiment: Predicting Stock Returns from News Stories"
authors: [Steven L. Heston, Nitish Ranjan Sinha]
year: 2017
venue: Financial Analysts Journal 73(3), 67–83 (FEDS working paper 2016-048)
source_url: https://www.federalreserve.gov/econresdata/feds/2016/files/2016048pap.pdf
doi: 10.2469/faj.v73.n3.3
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3]
family: [sentiment]
evidence: Moderate
score: 6
tags: [lit-note, family/sentiment]
---
# News vs Sentiment: Predicting Returns from News (Heston, 2017)

**Basis:** FEDS 2016-048 working-paper PDF (federalreserve.gov), read through page fetch; FAJ version not opened.

**Takeaway:** Neural-network news tone predicts returns for only 1–2 days when measured daily, but tone aggregated over a week predicts returns for up to 13 weeks; the slow part comes from negative news and clusters at the next earnings announcement.

## Problem
Is news tone transient "sentiment" (reverses) or "information" (persists), and does the answer depend on aggregation horizon?

## Data and period
900,754 Thomson Reuters articles on US firms, 2003–2010; relevance ≥ 35%; CRSP returns (pp. 6–7).

## Method
Thomson Reuters NewsScope 3-layer neural network trained on 3,000 triple-annotated articles (< 1% of sample) (p. 8). Daily quintile and weekly decile long–short portfolios; Fama–MacBeth regressions with lags 0–13, separate positive and negative tone, and a news-existence dummy that separates tone from the effect of having news at all (pp. 10–17).

## Baselines and validation
Momentum- and size-adjusted returns; earnings-announcement decomposition. No holdout sample: "out-of-sample" means returns after the news week (p. 11). No transaction costs.

## Results (with page or section references)
- Daily: day 1 spread 0.17%, day 2 0.04%, flat afterwards (Table 3, pp. 10–11).
- Weekly: announcement-week spread 3.75%; positive, mostly significant spreads to week 13 (0.21% in week 13) (Table 4, pp. 11–12).
- Spreads survive momentum and size adjustment (week 0: 3.61%, 3.62%) (p. 12).
- Positive tone fades after a day; negative tone coefficients are negative at all 13 lags, significant at lags 1–6 and 10 (Table 5, pp. 16–17).
- Delayed response sits mainly in the next earnings week: 5.57% (t = 2.66) vs 0.25% pre-earnings (Table 6, pp. 18–19).
- Stocks with no news underperform stocks with neutral news (pp. 15–17).

## Limits and risks to validity
_My assessment:_ 2003–2010 only, proprietary classifier, no costs; small-firm effects may be untradable (authors, p. 9). Old sample, so decay speeds today may be faster.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Predictive regressions; classifier fit on < 1% of data |
| Baselines | 1 | Momentum and size adjustments |
| Point-in-time and leakage controls | 1 | Tone scored from text at publication; partial |
| Costs and realism | 0 | None |
| Sample breadth | 2 | All US stocks with news, 2003–2010 incl. 2008 |
| Statistical testing | 1 | Fama–MacBeth t-stats |
| Reproducibility | 0 | Proprietary data |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "daily news predicts stock returns for only 1 to 2 days" (abstract, p. 1)
