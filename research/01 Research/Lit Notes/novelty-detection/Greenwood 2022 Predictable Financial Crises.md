---
type: lit-note
title: "Predictable Financial Crises"
authors: [Robin Greenwood, Samuel G. Hanson, Andrei Shleifer, Jakob Ahm Sørensen]
year: 2022
venue: Journal of Finance 77(2), 863–921 (read as NBER Working Paper 27396, June 2020)
source_url: https://www.nber.org/system/files/working_papers/w27396/w27396.pdf
doi: 10.1111/jofi.13105
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.8, RQ3.5, RQ4.5]
family: [novelty-detection]
evidence: Moderate
score: 8
tags: [lit-note, family/novelty-detection]
---
# Predictable Financial Crises (Greenwood, 2022)

**Basis:** NBER WP 27396 (June 2020) read through alphaXiv page excerpts (pp. 1, 4, 12, 15, 17–18, 20, 23–25, 28, 34, 49). The JF 2022 version (vol. 77(2), 863–921, per EconPapers) was not opened; its DOI was not shown and is left blank; numbers may differ.

**Takeaway:** Crises are predictable in probability but not in timing: when 3-year credit growth is in the top quintile and asset-price growth in the top tercile (the "R-zone"), the chance of a crisis within three years is about 40–45% vs a ~12% base rate, with the signal arriving 2.9 years early on average — but the R-zone misses 36–60% of crises, more than half its alarms are false, and out-of-sample R² is only 0.9–4.5%.

## Problem
Are financial crises unpredictable "bolts from the sky", or the predictable result of credit booms?

## Data and period
42 countries, 1950–2016; Baron–Verner–Xiong (BVX) crisis chronology (from bank-equity crashes plus narrative); business and household credit-to-GDP, equity and home prices (p. 4). 50 crises in the business sample (p. 49).

## Method
Panel linear probability regressions of crisis onset within h years on indicators of high credit growth, high price growth and their interaction (R-zone) (p. 12). Robustness: backward-looking thresholds from 1973, leave-one-out thresholds, pre-2000 sample, other chronologies (JST, Reinhart–Rogoff), developed vs developing (pp. 15, 18). Recursive out-of-sample R² from 1973 to 2012 (pp. 17–18). Contingency tables (precision, TPR, TNR) and a policy-possibility frontier (pp. 23–25).

## Baselines and validation
Unconditional crisis probability; credit growth alone (Schularick & Taylor style: +1 s.d. credit growth adds 2.8 pp over five years) (p. 4). In-sample headline; recursive OOS R² reported as a check (p. 18).

## Results (with page or section references)
- Business R-zone: 13% 1-year and 45.3% 3-year crisis probability vs 4% unconditional 1-year (p. 4, p. 12); household R-zone 14.0% and 36.8% (p. 12).
- Both R-zones together: probability rises by 68.6%, but only 19 such episodes (p. 20).
- Within-country 3-year R² only 7.8% (multivariate) / 6.1% (univariate), because R-zones (6% of country-years) are rarer than crisis windows (12.0%) (p. 15).
- Recursive OOS R²: 4.2% (business R-zone, in-sample 6.7%), 0.9% (household, in-sample 6.8%), 4.5% (both, in-sample 11.1%) (p. 18).
- Backward-looking thresholds: R-zone effect 34.1% vs 38.2% baseline (business), 23.8% vs 30.1% (household) (p. 15).
- Classification: business R-zone precision 45.3%, TPR 40.0%, TNR 89.2%, signal 2.9 years before onset; "either" R-zone TPR 64.0%, precision 35.9%; looser Y-zone TPR 82% but precision ~20–35% (Table 10, p. 49; pp. 25, 28).
- Missed crises are mostly "double-dip" crises that follow an earlier crisis (p. 28).
- Adding global R-zone share raises 3-year R² to 19.2% (p. 20).

## Limits and risks to validity
_My assessment:_ crisis chronology built partly from bank-stock crashes, so a crash-based label is predicted by asset-price booms (some circularity). Annual data and multi-year horizons: this is a slow vulnerability gauge, not a market-timing signal. Headline probabilities are in-sample; OOS R² drops sharply for households. The key lesson for RQ1.8: boom-bust (endogenous) crises leave a measurable build-up; timing within a three-year window is not forecast.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Headline in-sample; recursive OOS R² as a check |
| Baselines | 1 | Unconditional rate, credit growth alone |
| Point-in-time and leakage controls | 2 | Backward-looking and leave-one-out thresholds tested |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | 42 countries, 1950–2016, many crises |
| Statistical testing | 1 | Standard errors and p-values; no multiple-testing correction |
| Reproducibility | 0 | No code noted in pages read; BVX data shared privately |
| **Total** | **7/12 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "crises are slow to develop" (p. 12)

**Citation check (2026-11-08):** DOI 10.1111/jofi.13105 confirmed through OpenAlex by the reference-lookup tool.
