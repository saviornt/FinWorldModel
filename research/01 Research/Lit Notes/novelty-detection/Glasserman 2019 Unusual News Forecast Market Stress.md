---
type: lit-note
title: "Does Unusual News Forecast Market Stress?"
authors: [Paul Glasserman, Harry Mamaysky]
year: 2019
venue: Journal of Financial and Quantitative Analysis 54(5), 1937–1974
source_url: https://www.financialresearch.gov/working-papers/files/OFRwp-2016-04_Does-Unusual-News-Forecast-Stress.pdf
doi: 10.1017/S0022109019000127
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.5, RQ1.6, RQ1.12, RQ1.8]
family: [novelty-detection]
evidence: Moderate
score: 6
tags: [lit-note, family/novelty-detection]
---
# Does Unusual News Forecast Market Stress? (Glasserman, 2019)

**Basis:** OFR Working Paper 16-04 (April 2016) read through alphaXiv page excerpts (pp. 1–5, 7, 9–10, 14–17, 20, 24, 33, 41, 43). The JFQA 2019 version (DOI above) was not opened; numbers may differ.

**Takeaway:** Unusual negative news (4-gram entropy × negative sentiment, on 367,331 Reuters articles about 50 large financial firms, 1996–2014) forecasts higher company and market volatility up to six months ahead, even after controlling for lagged implied and realised volatility, with the aggregate response peaking around four months; the tests are in-sample regressions and VARs.

## Problem
Does the unusualness of news, combined with its sentiment, forecast market stress (volatility) rather than return direction?

## Data and period
Thomson Reuters news, Jan 1996–Dec 2014, articles mentioning the top 50 global banks, insurers and real-estate firms; about 1,611 articles a month (p. 3). One-month at-the-money implied volatilities, VIX, S&P 500 realised volatility; monthly, Apr 1998–Dec 2014 (p. 43).

## Method
Entropy of each month's 4-grams relative to a rolling training corpus from months t−27 to t−4 (the last three months excluded so new phrases still count as unusual) with add-one smoothing (pp. 13–14). Sentiment from word lists; interaction ENTSENT_NEG; aggregate entropy = first principal component of single-name series (pp. 15–16). Company regressions, panel regressions with volatility controls, VARs with impulse responses, long–short sorts (pp. 3–4).

## Baselines and validation
Controls: lagged implied and realised volatility and negative returns (Bekaert–Hoerova style) (p. 3). No out-of-sample forecast evaluation in the pages read; the text measure is built from past data only.

## Results (with page or section references)
- Company level: ENTSENT_NEG raises average R² by 0.22 over the control model (negative sentiment alone about 0.14, negative entropy 0.09); all six monthly lags significant; +1 s.d. raises next month's implied volatility by about 4 vol points (pp. 3, 19).
- Remains significant with lagged volatility controls, though the incremental R² is then much smaller (p. 3).
- Aggregate: a shock to ENTSENT_NEG raises VIX and realised volatility over several months, hump-shaped, peaking around four months (p. 4).
- ENTSENT_NEG has the highest VIX correlation of the news measures (0.60) (p. 23, Table 6).
- Examples: "the collapse of Lehman" (Sep 2008), "the euro zone crisis" and "a failed hedging strategy" (May 2012) are top entropy contributors (pp. 2, 14–15).
- Published abstract adds: articles explicitly about "the market" do not forecast volatility (JFQA abstract page).

## Limits and risks to validity
_My assessment:_ forecasts are in-sample; 50 firms in one sector; monthly frequency, so this is a slow stress-build-up signal, not an alarm with a lead time measured in days. No false-alarm analysis. The rolling corpus with a 3-month gap is a good point-in-time design for novelty.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample regressions and VARs |
| Baselines | 1 | Lagged implied and realised volatility controls |
| Point-in-time and leakage controls | 2 | Rolling past-only corpus with gap |
| Costs and realism | N/A | Main claim is volatility forecasting |
| Sample breadth | 1 | 50 financial firms, 1998–2014 incl. GFC |
| Statistical testing | 1 | Standard significance tests |
| Reproducibility | 0 | Licensed Reuters data, no code |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Brewing concerns often generate public discourse well before they materialize as market stress" (p. 4)
