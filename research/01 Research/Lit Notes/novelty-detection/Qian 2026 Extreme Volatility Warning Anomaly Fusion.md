---
type: lit-note
title: "Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion"
authors: [Jin Qian, Zhangzhi Xiong, Mingrui Li, Zhen Liu]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2607.23682
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.5, RQ1.7, RQ1.11, RQ4.4]
family: [novelty-detection, fusion]
evidence: Moderate
score: 6
tags: [lit-note, family/novelty-detection, family/fusion]
---
# Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion (Qian, 2026)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1–14, full paper).

**Takeaway:** For 3-day-ahead extreme-volatility warnings on the CSI 300, unsupervised Isolation Forest anomaly scores on GDELT events and Chinese news, added to market features, gave the best test AUC (0.680 vs 0.608 market-only); a 100K-parameter attention fusion model did worse than chance, English news hurt, and learned source weights were unreliable.

## Problem
Can news and event anomalies warn of extreme index volatility when there are only about 80 positive training days?

## Data and period
CSI 300 daily, 2018–2023. Sources: 16 market features; GDELT China-filtered events (tone, Goldstein scale, conflict ratios, counts); 17,619 Chinese financial news articles; 153,851 English articles (Reuters, NYT, Guardian, Twitter, Hacker News) filtered by LaBSE similarity (pp. 4–5).

## Method
Label EV3: max absolute-return z-score over the next 3 days above the 96.5th percentile of training z-scores (about 10% positives in train, 14% in test) (pp. 3–4). AAMSF: per-source Isolation Forest scores (equal weights) fused 85/15 with a 16-parameter Ridge on market features; T-AAMSF adds exponential decay over 3 days (pp. 6–7). News after 15:00 CST mapped to next trading day; news features converted to rolling z-scores, including embedding novelty and crisis-similarity (pp. 4–5).

## Baselines and validation
Strict temporal split: train to 2021-06 (791 days, 80 positives), validation 2021-07–2022-06 (242 days), test from 2022-07 (366 days, 50 positives) (p. 4). Baselines: GARCH(1,1), Isolation Forest, logistic regression, LightGBM, TF-IDF+LR, MLP, LSTM, Transformer, a simplified TFT (Table 3, p. 8).

## Results (with page or section references)
- Test AUC / PR-AUC: AAMSF-Opt 0.680 / 0.276; IF alone 0.630; GARCH 0.507; LightGBM 0.305; HTSF (100K params) 0.443 (Table 3, p. 8).
- Source ablation: market only 0.608; GDELT only 0.624; market+GDELT 0.658; +Chinese news 0.680; +English news falls to 0.605–0.613 (Table 7, p. 10).
- Finance-tagged GDELT only is worse than all China-related events (0.583 vs 0.658), i.e. non-financial geopolitical events carry risk signal (Table 9, p. 10).
- Validation vs test AUC for GDELT 0.423 vs 0.625; learned weighting prunes GDELT and loses (Tables 6, 10, pp. 9, 11).
- Temporal accumulation over 2–3 days raises PR-AUC to 0.291 (Table 2, p. 7).
- Case windows: fires on 5 of 11 positive days in Oct–Nov 2022 (Table 4, p. 9).
- Test AUC falls as parameters per positive label rise (Table 12, p. 12).

## Limits and risks to validity
_My assessment:_ one market, one test year, 50 positive days; no confidence intervals or significance tests, so a 0.05–0.07 AUC gain may be noise. Several model choices (85/15 weights, 3-source set, mixed preprocessing) were made after looking at test results, which is a form of test-set selection. LightGBM's AUC of 0.305 (well below 0.5) suggests an inverted signal or a setup issue. Lead time is fixed at 1–3 days by the label; no false-alarm rate per year is reported. AUC 0.68 is modest for a warning system.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One temporal train/val/test split |
| Baselines | 2 | GARCH plus LightGBM and others |
| Point-in-time and leakage controls | 1 | After-close mapping, training-only thresholds; test-informed design choices |
| Costs and realism | N/A | Warning task, no trading |
| Sample breadth | 1 | One index, 2018–2023 incl. stress |
| Statistical testing | 0 | No tests or intervals |
| Reproducibility | 0 | No code link found |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "English news consistently reduces performance" (p. 1)
- "when detector quality cannot be reliably estimated, equal weighting dominates" (p. 11)
