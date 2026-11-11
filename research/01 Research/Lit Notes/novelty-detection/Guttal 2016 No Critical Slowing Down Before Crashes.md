---
type: lit-note
title: "Lack of Critical Slowing Down Suggests that Financial Meltdowns Are Not Critical Transitions, yet Rising Variability Could Signal Systemic Risk"
authors: [Vishwesha Guttal, Srinivas Raghavendra, Nikunj Goel, Quentin Hoarau]
year: 2016
venue: PLoS ONE 11(1), e0144198
source_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144198
doi: 10.1371/journal.pone.0144198
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.8, RQ1.5]
family: [novelty-detection]
evidence: Moderate
score: 8
tags: [lit-note, family/novelty-detection]
---
# Lack of Critical Slowing Down Before Financial Meltdowns (Guttal, 2016)

**Basis:** Published PDF read through alphaXiv page excerpts (pp. 1–8, 11, 16–17). Supplementary figures not read.

**Takeaway:** Before the 1929, 1987, 2000 and 2008 crashes (Dow Jones, S&P 500, NASDAQ, DAX, FTSE) there was no critical slowing down (no rising lag-1 autocorrelation), so crashes do not look like tipping-point transitions; detrended variance did rise before every major Dow crash, but the same signal fired seven times with no crash in 115 years and gave no reliable timing (3 months to 5 years).

## Problem
Are financial crashes critical transitions near a tipping point, and if so do generic early warning signals (rising autocorrelation, variance, spectral reddening) precede them (p. 2)?

## Data and period
Daily closes of DJI (115 years incl. 1929, 1987, 2000, 2008), S&P 500 and NASDAQ (1987, 2000, 2008), DAX and FTSE (2000, 2008); 1-minute data for some crashes (pp. 5–7).

## Method
Gaussian-kernel detrending in a 4-year window; rolling-window (500-day) lag-1 autocorrelation, variance and low-frequency power spectrum; Kendall-τ trend over 250 days before the crash (pp. 3, 16). Scan of the whole DJI history for strong trends (τ > 0.9) (pp. 4, 6). Three surrogate nulls (Fourier-matched, AR(1), bootstrap) for significance; sensitivity scan over >1.25 million parameter combinations (pp. 16–17). Simple bistable and agent-based models to explain the pattern (pp. 5, 8).

## Baselines and validation
Surrogate-data null models; historical-window comparison (p_hist); comparison of detrended variance with standard return volatility (pp. 7–8, 11). No forecasting test with a decision rule set in advance.

## Results (with page or section references)
- Autocorrelation showed no or weak trends before any crash, in all five markets (pp. 6–7).
- Variance and low-frequency power rose strongly before all four major DJI crashes; no spectral reddening (p. 6).
- Over 115 years of DJI, 16 strong-trend events: 9 preceded crises (incl. minor ones) and 7 were false alarms; no known crash was missed (Table 1, pp. 6–7).
- Lead time ranged from 3 months to 5 years, so "occurrence of an EWS is not a predictive measure of when the crash will occur" (Table 1 note, p. 6).
- Return volatility did not always rise (e.g. NASDAQ 1987; DJI and S&P 500 2000) (pp. 8, 11).
- Model: crashes fit "stochastic transitions" driven by rising noise; a single large shock gives no warning at all (p. 8).
- False alarms may be increasing over time (p. 11).

## Limits and risks to validity
_My assessment:_ the crash list and the τ > 0.9 threshold are chosen with hindsight; the huge parameter scan without a multiple-testing correction makes the "no false negatives" claim fragile. Index-level only. Still strong negative evidence against tipping-point (critical slowing down) warnings for markets, and consistent with [[Garcia Seuma 2026 Crypto Cascade Early Warning]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Retrospective analysis of known crashes |
| Baselines | 1 | Surrogate nulls; volatility comparison |
| Point-in-time and leakage controls | 1 | Backward rolling windows, but crash dates and thresholds known ex post |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | Five indices, a century, many crashes |
| Statistical testing | 1 | Surrogate p-values; no correction for the parameter scan |
| Reproducibility | 2 | Code and data on GitHub (p. 1) |
| **Total** | **7/12 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "inevitably prone to both false and failed alarms" (p. 11)
