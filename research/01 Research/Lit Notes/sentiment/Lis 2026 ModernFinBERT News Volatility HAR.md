---
type: lit-note
title: "Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics"
authors: [Szymon Lis, Robert Ślepaczuk, Paweł Sakowski]
year: 2026
venue: arXiv 2610.39636
source_url: https://arxiv.org/abs/2610.39636
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.14, RQ1.3]
family: [sentiment]
evidence: Moderate
score: 9
tags: [lit-note, family/sentiment]
---
# Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics (Lis, 2026)

**Basis:** v1 (29 Oct 2026), page excerpts via alphaXiv (pp. 214, 217, 235–236, 252, 262–277 of the source numbering; abstract and Sections 3.3, conclusions, Appendix C tables).

**Takeaway:** Market-wide ModernFinBERT news variables (sentiment, directionality, entropy, intensity, volume) from the New York Times did not reliably improve HAR volatility forecasts for 11 US stocks, 2000–2022: HAR-Text beat HAR in 2 of 33 expanding cells and neither win survived longer HAC bandwidths; the naive forecast had the lowest mean QLIKE at every horizon.

## Problem
Do small-encoder news sentiment features add information to volatility forecasts beyond persistence, VIX and survey sentiment?

## Data and period
New York Times corpus scored with ModernFinBERT; 11 ex-post selected large US stocks; 2000–2022; horizons h = 1, 5, 22; target the square root of a future average of trailing 252-session Yang–Zhang variance (abstract, p. 214).

## Method
Article probabilities → sentiment (p+ − p−), directionality (1 − p0), entropy, intensity, volume, aggregated market-wide; HAR, matched HAR-X (VIX, AAII, Text, Full), Elastic Net, Random Forest, XGBoost, naive, stacking (pp. 217, 236).

## Baselines and validation
HAR, naive and VIX/AAII-augmented HAR. Purged expanding and rolling walk-forward with a horizon-length gap; hyperparameters chosen once on the first 252 observations; QLIKE primary; Diebold–Mariano and Clark–West tests; 792 Benjamini–Hochberg-adjusted tests in the primary family (pp. 214, 217).

## Results (with page or section references)
- Naive lowest mean QLIKE at each horizon; HAR-VIX most frequent cell winner but higher mean QLIKE than HAR (abstract; p. 252).
- HAR-Text improves on HAR in 2 of 33 expanding cells; neither QLIKE rejection survives longer HAC (abstract, p. 214).
- Tree models with text (RF-Text, XGB-Text) lose to the benchmark in almost every stock and horizon (Appendix C, pp. 262–274).
- Text is "relatively less adverse" in high-volatility states, but median gains are negative in both states (p. 252).

## Limits and risks to validity
The authors flag that ModernFinBERT's training cutoff is unknown (weights released 4 Jul 2025), so this is an ex-post measurement exercise; the stock panel is survivors; the long-window target is very persistent, which favours naive forecasts (pp. 235–236, 252). _My assessment:_ the target choice makes text gains hard to show; a result on next-day realised variance could differ. Still the most carefully tested small-encoder text study in the vault.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Purged expanding and rolling walk-forward |
| Baselines | 2 | HAR, naive, VIX, GBT |
| Point-in-time and leakage controls | 1 | Purging explicit; encoder not point-in-time |
| Costs and realism | N/A | Volatility forecasts, no trading |
| Sample breadth | 1 | 11 surviving stocks, 2000–2022 incl. 2008 and 2020 |
| Statistical testing | 2 | DM/CW with BH correction |
| Reproducibility | 0 | Not stated in pages read |
| **Total** | **8/12 → 9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "Additional information does not reliably improve this particular highly persistent target" (p. 252)
