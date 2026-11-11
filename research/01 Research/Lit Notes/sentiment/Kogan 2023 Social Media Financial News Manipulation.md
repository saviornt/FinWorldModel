---
type: lit-note
title: "Social Media and Financial News Manipulation"
authors: [Shimon Kogan, Tobias J. Moskowitz, Marina Niessner]
year: 2023
venue: Review of Finance
source_url: https://conference.nber.org/conf_papers/f121760/f121760.pdf
doi: 10.1093/rof/rfac058
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.11]
family: [sentiment]
evidence: Moderate
score: 7
tags: [lit-note, family/sentiment, misinformation]
---
# Social Media and Financial News Manipulation (Kogan, 2023)

**Basis:** April 2019 NBER conference version ("Fake News: Evidence from Financial Markets"), read through a page-fetch summary (first 100k of 114k characters). Published in Review of Finance 27(4), 2023. Check numbers against the journal version.

**Takeaway:** Paid-for fake articles on Seeking Alpha raised volume and volatility and temporarily lifted small-firm prices (which later reversed); once the SEC case became public, investors reacted less to all articles, legitimate ones included, especially for small, retail-held firms; a linguistic fake detector caught only ~10% of fakes.

## Problem
Does false information on crowd-sourced financial platforms move prices, and what happens to trust in real news once fraud is revealed?

## Data and period
171 SEC-identified fake articles (20 authors, 47 firms) plus 334 non-fake articles by the same authors (pp. 11, 14); 203,545 Seeking Alpha (2005–2015) and 147,916 Motley Fool (2009–2014) articles, ~7,700 firms (p. 12); SEC announcement Feb–Mar 2014 as an awareness shock (pp. 29–31).

## Method
Event studies of volume, volatility and returns around fake vs non-fake articles; LIWC "authenticity" score turned into a fake probability by Bayes' rule calibrated on the SEC sample (pp. 15–18); difference-in-differences around the SEC revelation with placebo outlets.

## Baselines and validation
Same-author non-fake articles as controls; placebo tests on filings, press releases, WSJ/NYT (pp. 32–33); held-out staff-writer check of the classifier (p. 20). No trading strategy.

## Results (with page or section references)
- Abnormal volume >50% higher over 3 days for fake vs non-fake, concentrated in the smallest decile; idiosyncratic volatility ≈40% higher (pp. 5, 7, 26).
- Small firms: prices up to ≈13% after ~60 days, then fully reversed (cumulative −5% after a year) (p. 40).
- After revelation, volume response to all articles fell ≈4–5%; −35% for small firms vs −11.7% for large; −30.3% high-retail vs −9.5% low-retail; Motley Fool also fell; placebo outlets did not (pp. 5, 32–36).
- Classifier: of 171 fakes it flagged 18 (17 correct), missed ~90%, and left ~64% of articles ambiguous (pp. 18–19); estimated fake prevalence ≈2.8% (p. 4).

## Limits and risks to validity
_My assessment:_ small clean fake sample; probabilistic labels in the broad sample are noisy; event-study design without a forecasting test. Strong identification of the trust spillover.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Classifier validated on a held-out author; otherwise event study |
| Baselines | 1 | Same-author non-fake; placebo outlets |
| Point-in-time and leakage controls | 1 | Article timestamps; SEC labels known only ex post |
| Costs and realism | N/A | Not a trading claim |
| Sample breadth | 2 | ~7,700 firms, 10 years |
| Statistical testing | 1 | Clustered significance, placebos |
| Reproducibility | 0 | SEC labels public, platform data not |
| **Total** | **6/12 → 7/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
