---
type: lit-note
title: "Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models"
authors: [Alejandro Lopez-Lira, Yuehua Tang]
year: 2026
venue: Journal of Financial Economics 184 (arXiv 2304.07619v6)
source_url: https://arxiv.org/abs/2304.07619
doi: 10.1016/j.jfineco.2026.104335
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.2, RQ1.3]
family: [llm-text]
evidence: Moderate
score: 7
tags: [lit-note, family/llm-text]
---
# Can ChatGPT Forecast Stock Price Movements? (Lopez-Lira, 2026)

**Basis:** arXiv v6 (28 Oct 2025) read as page excerpts via alphaXiv (pp. 1, 3–4, 18–20, 31, 35, 46, 50–51, 56–59, 89, 92, 140–141). The JFE 2026 version (DOI from the reference list of [[Dehkordi 2026 OLIVIA LLM News Look-Ahead Test]]) was not opened.

**Takeaway:** GPT-4 reading post-cutoff headlines identifies the direction of the (non-tradable) initial reaction ~90% of days and predicts a 1–2 day drift worth a gross Sharpe of ~3, but the drift is concentrated in small caps, turns negative at 20 bps round trip, and decays from 2021 to 2024.

## Problem
Can an off-the-shelf LLM read the economic content of firm news and predict the market reaction and the drift after it?

## Data and period
159,137 firm-headline-date observations for 4,123 US common stocks, Oct 2021–May 2024 (after GPT-4-0314's Sep 2021 cutoff); headlines matched to RavenPack for timestamps; 82% overnight news (pp. 3–4).

## Method
Zero-shot prompt: is the headline good, bad or unknown for the stock; mapped to +1/−1/0; daily long–short portfolios; predictive regressions with firm and date fixed effects; 12 LLMs compared; supervised embedding baselines retrained monthly (pp. 18–20, 31).

## Baselines and validation
RavenPack sentiment, FinBERT, BERT, BART, Llama-2 7–70B, GPT-1/2/3.5; OpenAI and MiniLM embeddings with rolling 6-month logistic regression (Tables 5, 8). Single post-cutoff evaluation period; no random-walk or price-only GBT baseline.

## Results (with page or section references)
- Initial reaction hit rate 93.3% (overnight) and 88.8% (intraday); not tradable (Table 1, p. 51).
- Drift long–short: 0.34%/day, gross Sharpe 2.97 overnight; 2.63 intraday (Table 1).
- Costs: Sharpe 2.13 at 5 bps, 1.29 at 10 bps, −0.39 at 20 bps; turnover ~190%/day (Table OA7, p. 89).
- Value-weighted Sharpe only 0.56; large-cap drift Sharpe 0.06 (Tables OA7, OA10, pp. 89, 92).
- Sharpe by year: 6.54 (2021Q4), 3.68, 2.33, 1.22 (Jan–May 2024) (p. 35).
- Model size matters: GPT-3.5 Sharpe 1.66, Llama-2-70b 0.97, FinBERT −0.33, BERT −0.47 (Table 5, p. 56).
- GPT-4 beats supervised embeddings: OpenAI embeddings drift Sharpe 2.53, MiniLM 1.42 (Table 8, p. 59).

## Limits and risks to validity
_My assessment:_ the only out-of-sample window is 2.5 years; costs are flat round-trip figures with no price impact or borrow costs; the tradable edge sits in small, costly-to-short stocks. The study relies on the vendor cutoff date; it has no masking or contamination test of its own. Proprietary data (RavenPack, scraped headlines), so it cannot be reproduced.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One post-cutoff period |
| Baselines | 1 | Sentiment and embedding baselines; no RW or price-only GBT |
| Point-in-time and leakage controls | 2 | Post-cutoff sample, RavenPack timestamps |
| Costs and realism | 1 | Flat 0–20 bps; turnover reported |
| Sample breadth | 1 | Many stocks, one short period |
| Statistical testing | 1 | t-stats, Lo (2002) CIs; no multiple-testing correction |
| Reproducibility | 0 | No code or data |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "A transaction cost of 20 bps round-trip makes the strategy unprofitable." (p. 20)
