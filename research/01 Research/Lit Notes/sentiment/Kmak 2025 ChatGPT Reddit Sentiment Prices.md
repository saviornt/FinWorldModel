---
type: lit-note
title: "Predicting stock prices with ChatGPT-annotated Reddit sentiment: Hype or reality?"
authors: [Mateusz Kmak, Kamil Chmurzyński, Kamil Matejuk, Paweł Kotzbach, Jan Kocoń]
year: 2025
venue: arXiv 2507.22922
source_url: https://arxiv.org/abs/2507.22922
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.3]
family: [sentiment]
evidence: Weak
score: 2
tags: [lit-note, family/sentiment]
---
# ChatGPT-Annotated Reddit Sentiment (Kmak, 2025)

**Basis:** v1, full text via alphaXiv, pp. 1–15.

**Takeaway:** For GME and AMC in Q1 2021, sentiment from TextBlob, Financial-RoBERTa and a RoBERTa fine-tuned on ChatGPT labels barely relates to prices, while comment volume and Google Trends are correlated and Granger-related in both directions.

## Problem
Does WSB sentiment predict meme-stock prices, and does a Reddit-tuned model help?

## Data and period
~7 million r/wallstreetbets posts, 4 Jan–31 Mar 2021; GME and AMC daily prices; Google Trends (p. 3).

## Method
TextBlob, Financial-RoBERTa, and Financial-RoBERTa fine-tuned on 10,525 ChatGPT-labelled (partly ChatGPT-generated negative) posts; emoji counter. Pearson and Kendall correlations and Granger tests on levels and daily changes (pp. 4–7).

## Baselines and validation
Comment volume and Google Trends as baselines. No holdout; no forecasting test.

## Results (with page or section references)
- GME: comment volume vs price r = 0.52; sentiment correlations −0.06 to 0.23 (Tables 1, 3, pp. 8, 10).
- Comment volume Granger-predicts GME price changes (p = 0.018 stationary) and price changes predict comments (p = 0.041) (Table 2, p. 8).
- Fine-tuned sentiment not significant for AMC; only emoji count Granger-predicts AMC (p = 0.007) (Table 8, p. 13).
- Authors: sentiment "neither strongly correlated nor causally related" to price (p. 14).

## Limits and risks to validity
_My assessment:_ two stocks, one quarter, price levels, many uncorrected tests, synthetic training negatives. Useful only as a negative datapoint for WSB sentiment versus attention.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | Volume, Google Trends |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 0 | Two stocks, one quarter |
| Statistical testing | 1 | Granger tests, no correction |
| Reproducibility | 0 | No code or data |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "social media sentiment has only a weak correlation with stock prices" (abstract, p. 1)
