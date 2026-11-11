---
type: lit-note
title: "Dynamic Multi-Step Decoding for Time-Series Foundation Models"
authors: [Birmjune Kim, Hyungju Lee, Hyun Oh Song]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2610.34409
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.13, RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, autoregressive, rollout]
---
# Dynamic Multi-Step Decoding for Time-Series Foundation Models (Kim, 2026)

**Basis:** alphaXiv PDF pages 1–4, 9–10, 12–13, 17, 23 (v1). Seoul National University.

**Takeaway:** On fev-bench with a frozen Chronos-2, fully autoregressive patch-by-patch rollout is significantly worse than one-shot decoding (skill −3.1% overall, −10.7% and 0/19 wins on the longest horizons); finer chunks compound error more, and a learned per-window schedule selector gains only +0.2% to +0.7%.

## Problem
Should multi-step forecasts be decoded in one shot or by autoregressive rollout, and can the schedule be chosen per instance? (pp. 1–3)

## Data and period
fev-bench: 100 tasks across seven domains, official windows and MASE; 34 tasks have one horizon patch (structural ties) (§5, pp. 9–10).

## Method
Rollouts as ordered partitions of the horizon into patch chunks; dynamic program over prefixes; selector network on backbone hidden states; five-seed agreement gate falling back to one-shot (§3.2, §4, pp. 4, 9). Rollouts feed back point forecasts; claims are confined to point accuracy (p. 10).

## Baselines and validation
One-shot decoding; fixed chunks of 1 (fully autoregressive), 2 and 4 patches; per-task and per-horizon schedule choice; median/mean ensembles (App. C.1, p. 17). Selectors trained only on windows before the official evaluation windows; task-level bootstrap CIs, 20,000 resamples (p. 10).

## Results (with page or section references)
- Fixed schedules vs one-shot (Chronos-2): fully autoregressive skill −3.11% [−4.43, −1.95], 11/34/55 W/T/L; on H≥9, −10.73% [−16.04, −6.28], 0/0/19. Chunk 2: −1.18%; chunk 4: −0.16% (n.s.) (Table 6, p. 17).
- Selector: +0.20% [+0.06, +0.37] overall; +0.68% on H≥9; recovers ~6–8% of the oracle gain; Moirai backbone +0.23% (Table 2, p. 10).
- Cost: slowdown 13.7× to 103.6× over one-shot (Table 3, p. 12).
- Background: increasing TimesFM's output patch length (fewer AR steps) improved long-horizon accuracy (p. 3).

## Limits and risks to validity
_Authors:_ point accuracy only; propagating a distribution through rollouts not studied; gains concentrated in energy tasks (pp. 10, 12).
_My assessment:_ no finance tasks; backbones trained for direct decoding, so autoregressive use is off their training distribution. Still, the clearest quantitative test found of rollout error compounding in modern TSFMs.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Selector trained on pre-evaluation windows |
| Baselines | 1 | One-shot and fixed schedules; no classical models |
| Point-in-time and leakage controls | N/A | Not a market study |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 100 tasks, no finance |
| Statistical testing | 1 | Bootstrap CIs; no multiple-testing correction |
| Reproducibility | 0 | Code not stated in pages read |
| **Total** | **4/10 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "full autoregression loses all 19 tasks with H ≥ 9 (skill −10.7%)." (p. 17)
