---
type: synthesis
title: "Synthesis: Multimodal Financial Forecasting and Shock Detection"
status: final
papers: ["[[RP1 ML Methods]]", "[[RP2 Data Sources and Storage]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
sources_count: 357
evidence_strong: 27
evidence_moderate: 157
evidence_weak: 100
evidence_primary_documentation: 73
created: 2026-11-09
updated: 2026-11-09
related: ["[[Research Questions]]", "[[Evidence Register]]", "[[Decisions Log]]", "[[Financial Foundation Model Research Direction]]"]
tags: [synthesis]
---
# Synthesis: Multimodal Financial Forecasting and Shock Detection

This note pulls together [[RP1 ML Methods]], [[RP2 Data Sources and Storage]], [[RP3 Cleaning and Labelling]], [[RP4 Training and Evaluation]] and [[RP5 Vault Review]] for the methodology plan. It records findings and open questions only. Decisions belong to the methodology plan.

**Evidence base.** 357 unique lit notes across the five papers (counted from lit-note properties on 2026-11-09): 27 Strong, 157 Moderate, 100 Weak, 73 primary documentation. Per paper: RP1 163, RP2 80, RP3 92, RP4 106, RP5 72 (RP5 reused existing notes only). Many notes feed more than one paper.

**How this was written.** From the five final papers' Abstracts, Findings, Cross-cutting observations, Contradictions and Open questions, with no new search, as the guide requires. Every claim below points to the RP section that holds its evidence; lit notes are named where one or two sources carry the claim.

## 1. The answer to the overall question

The methods with real out-of-sample evidence are simple and narrow: a random walk and gradient-boosted trees for returns, HAR for volatility, volatility-filtered fat-tailed models for tail risk, and slow fragility gauges (credit and price booms, news novelty) for shock risk over months to years ([[RP1 ML Methods#Cross-cutting observations|RP1 cross-cutting]] 1, 2, 7). Complex models, including deep RL, generic foundation models and token models, rarely beat these baselines in the best-designed tests, and positive results cluster in studies with weak baselines, one test window or no costs (RP1 cross-cutting 1, 9). Risk is forecastable; return direction barely is. Text, macro, cross-asset and graph inputs help only when compressed and fed through a gated or bounded pathway on top of a strong price model; naive concatenation and corrupted feeds make forecasts worse than price-only (RP1 RQ1.7, RQ1.15). The timing of exogenous shocks is not predictable; fast detection after onset and spread along supply-chain links are (RP1 RQ1.4, RQ1.5, RQ1.8). The project's central bet, an LLM-inspired autoregressive token model conditioned on a world state, is untested where it matters: no matched finance study compares token and continuous inputs with the same backbone against GARCH/HAR and GBT under walk-forward tests and costs (RP1 RQ1.10, RQ1.13). Data licences limit the design more than price does (RP2 RQ2.6), and protocol choices (shuffled splits, label leakage, uncounted search) move results more than method choices do (RP3 RQ3.1, [[RP4 Training and Evaluation#Observations across the questions|RP4 observations]]). The research therefore supports building the token/world model as a set of controlled experiments against strong baselines, not as an assumed improvement. Overall confidence: Medium.

## 2. Methods ranked by strength of evidence, per target

Ranks follow the evidence, not the expected upside. The Evidence column gives the rubric level of the sources named and, in brackets, the confidence the RP gave its answer.

### 2.1 Returns (point, sign, cross-sectional rank)

| Rank | Method | Evidence | Where |
| --- | --- | --- | --- |
| 1 | Random walk / historical mean as the benchmark; gradient-boosted trees and random forests on factor and price features | Strong and Moderate (High). Generic TSFMs rarely beat them ([[Rahimikia 2025 ReVisiting TSFMs in Finance]], Strong); monthly R²oos is small (about 0.3–0.4%) even for the best ML ([[Gu 2020 Empirical Asset Pricing Machine Learning]], Moderate) | RP1 RQ1.1 |
| 2 | Neighbour-average features over customer, analyst and correlation links, inside a GBT | Moderate, no Strong source (High that linked-firm returns predict; Medium that GNNs add nothing) ([[Cohen 2008 Economic Links Predictable Returns]], [[Xu 2021 HIST Concept Graph Stock Forecasting]]) | RP1 RQ1.4 |
| 3 | Return-supervised small text encoders, cross-sectional, 1–2 day horizon | Strong for both the positive and the null: return-supervised encoders give cross-sectional signal net of frictions, with outlier-sized accuracy ([[Kirtac 2026 MFAST News Trading Under Frictions]]); point-in-time topics do not beat price-only ([[Foley 2026 NoLBERT News Topics Returns]]) | RP1 RQ1.3, RQ1.14 |
| 4 | Shallow MLPs, gated LSTM hybrids | Moderate; depth adds nothing; seed sensitivity | RP1 RQ1.1 |
| 5 | Finance-pretrained token models with categorical bucket outputs (Kronos, StockGPT, VAIOM) | Moderate studies, Low confidence; no matched comparison; per-series TSFM targets negative ([[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]]) | RP1 RQ1.10, RQ1.13 |
| 6 | Generic time-series foundation models, zero-shot | Strong that they mostly fail to beat the random walk ([[Rahimikia 2025 ReVisiting TSFMs in Finance]]) | RP1 RQ1.1 |
| 7 | LLM backbones for numeric series; pre-cutoff LLM text backtests | Moderate (High): memorisation inflates pre-cutoff results ([[Lopez-Lira 2025 LLM Memorization Problem]]); no study shows an LLM backbone helping | RP1 RQ1.2 |
| 8 | Deep RL trading agents (TD3 and others) | Strong negative (High): no edge over 1/N or buy-and-hold after costs ([[Pollok 2026 End-to-End Policies vs Simple Rules]], Strong; [[Go 2026 FinPILOT Inference-Time Planning RL]]) | RP1 RQ1.9 |

Economic value is a separate test: gross gains often turn negative at realistic costs on liquid universes; turnover, tradable universe and investor size decide it (RP4 RQ4.6, High; [[Jensen 2026 ML Implementable Efficient Frontier]], [[Zhang 2026 Deep TS Models Equity Portfolios]]).

### 2.2 Volatility

| Rank | Method | Evidence | Where |
| --- | --- | --- | --- |
| 1 | HAR / Log-HAR on realised variance (benchmark); GARCH-type | Strong (High) | RP1 RQ1.1 |
| 2 | Random forests and neural nets on HAR inputs, larger gains at weekly and monthly horizons | Moderate (High) ([[Christensen 2023 Machine Learning Volatility Forecasting]]) | RP1 RQ1.1 |
| 3 | Regime-gated or bounded corrections to HAR using macro or cross-asset state | Strong source, small gains (Medium) ([[Ye 2026 Regime-Gated Residual MoE Volatility]]) | RP1 RQ1.7, RQ1.15 |
| 4 | Monthly news novelty / uncertainty as a slow volatility input | Moderate ([[Glasserman 2023 New News is Bad News]], [[Manela 2017 News Implied Volatility Disasters]]) | RP1 RQ1.5 |
| 5 | Fine-tuned TSFMs (TTM, TimesFM) | Strong source: zero-shot mostly loses to Log-HAR; fine-tuning narrows the gap ([[Brini 2026 TSFMs vs Econometric Realized Volatility]]) | RP1 RQ1.1 |
| 6 | Scalar sentiment aggregates added to HAR | Negative against HAR ([[Lis 2026 ModernFinBERT News Volatility HAR]]) | RP1 RQ1.14 |

### 2.3 Tail risk (VaR, ES, intervals)

| Rank | Method | Evidence | Where |
| --- | --- | --- | --- |
| 1 | Volatility-filtered fat-tailed models: conditional EVT, GARCH-t / skew-t | Strong (3 Strong sources) | RP1 RQ1.6 |
| 2 | Forecast combinations of VaR/ES; pooled cross-sectional quantile nets (monthly) | Moderate ([[Taylor 2025 Combining VaR and ES Forecasts]]) | RP1 RQ1.6 |
| 3 | Conformal layer on top: recency-weighted (better in stress) or ACI (better on average) | Moderate; contradictory on under-coverage | RP1 RQ1.6 |
| 4 | Deep / foundation tail models | Parity at best after fine-tuning; sampled tails off by more than ten times nominal at 1% ([[Decker 2026 Calibration of Probabilistic TSFMs]]) | RP1 RQ1.6, RQ1.13 |
| — | Any method at shock onset | None stays calibrated (High) | RP1 RQ1.6 |

### 2.4 Shock detection and early warning

| Rank | Method | Evidence | Where |
| --- | --- | --- | --- |
| 1 | Slow fragility gauges: credit and price booms raising crisis probability over 1–3 years; plain logit | Moderate (High) ([[Greenwood 2022 Predictable Financial Crises]]); ML adds little over logit ([[Beutel 2019 ML vs Logit Banking Crisis Warning]]) | RP1 RQ1.8 |
| 2 | Text novelty / unusualness, monthly, for volatility and returns | Moderate; unusual negative news forecasts volatility up to six months ahead, in-sample ([[Glasserman 2019 Unusual News Forecast Market Stress]]) | RP1 RQ1.5 |
| 3 | Fast detection after onset plus spread along supply-chain links | Moderate (High for spread along supply chains) ([[Barrot 2016 Input Specificity Shock Propagation]]); detection itself Moderate | RP1 RQ1.4, RQ1.5 |
| 4 | Option-implied signals and pre-announcement drift as "already priced" measures | Moderate; often move before public news ([[Pan 2006 Option Volume Future Stock Prices]]) | RP1 RQ1.12 |
| 5 | Event-level bursts in news or social posts | Moderate–Weak; short leads, many false alarms, synthetic or single-crisis tests; the Strong crypto study found warnings non-specific ([[Garcia Seuma 2026 Crypto Cascade Early Warning]]) | RP1 RQ1.5 |
| — | Predicting the timing of exogenous shocks | No source does (High); models cannot extrapolate beyond the largest events seen ([[Sun 2024 AI Weather Gray Swan Cyclones]]) | RP1 RQ1.8, RP3 RQ3.4 |
| — | Science papers or preprints as shock signals | No study found (evidence thin) | RP1 RQ1.5 |

## 3. Data-source shortlist, with costs and licence limits

Prices and terms are as read on 2026-11-08 and are not quotes; licence readings are not legal advice (RP2 Assumptions).

| Need | Shortlist | Cost (list) | Licence limit that matters | Where |
| --- | --- | --- | --- | --- |
| US stock/ETF price API | (1) Alpaca, (2) Databento, (3) EODHD; scores 112, 109, 106 of 170, Low confidence | Alpaca free (IEX) or $99/month; Databento per GB plus $199+/month; EODHD $19.99–$99.99/month | None documents delisted names; none mentions model training (silence is not permission); Alpaca and EODHD personal, non-commercial | RP2 RQ2.1, RQ2.7 |
| Survivorship-free daily reference | Norgate (or CRSP if licensed) | Norgate $630 / $787.50 a year; CRSP institutional | Training terms not read for Norgate | RP2 RQ2.1 |
| Excluded price API | Massive (only API with documented delisted coverage) | $29–$199/month | Bans AI/ML training (s. 5(g)) without written permission | RP2 RQ2.6, RQ2.7 |
| Filings, insiders, holdings | SEC EDGAR, SEC 13F and insider data sets | Free; 10 requests/s | Public records; next-business-day rule after 5:30 p.m. (10 p.m. Forms 3/4/5) | RP2 RQ2.2, RQ2.8 |
| News events | GDELT 2.0 | Free | Any use with citation; opaque coding; about 2.5% of archives missing | RP2 RQ2.2, RQ2.9 |
| Licensed news | Benzinga, RavenPack | On request / institutional | Training rights not stated | RP2 RQ2.2 |
| Social posts | X (paid), Reddit (terms blocked), StockTwits (scraping banned) | X $0.005 per post read | X bans use for foundation or frontier models and has a 24-hour deletion duty | RP2 RQ2.2, RQ2.6 |
| Macro vintages | BLS original releases (archived by the project); Philadelphia Fed RTDSM | Free | FRED/ALFRED ban AI training and API caching; RTDSM licence not stated | RP2 RQ2.3 |
| Identifiers and entities | GLEIF LEI (CC0), OpenFIGI (free), CRSP PERMNO/PERMCO (licensed) | Free / institutional | Current mappings only for OpenFIGI | RP2 RQ2.8 |
| Supply-chain and boards | FactSet Revere, Compustat Segments, BoardEx | Subscription / academic | Valid time only; academic copies non-commercial | RP2 RQ2.8 |
| Hazard and shipping events | USGS feeds (public domain, minute updates); MarineCadastre AIS (CC0, months behind) | Free | ACLED bans training; NOAA Storm Events lags about 5–6 months | RP2 RQ2.9 |
| Storage | Append-only raw zone + request ledger; a version-per-write or bitemporal layer (ArcticDB, LanceDB, XTDB-style tables, dated Parquet with DuckDB) | Mostly free | ArcticDB BSL "production use" clause unresolved; no engine covers knowledge and valid time out of the box | RP2 RQ2.4, RQ2.5 |

The open vendor questions (delisted coverage, storage after cancellation, training rights) are listed in [[RP2 Data Sources and Storage#Facts that need a vendor quote or a trial account|RP2 vendor-quote list]].

## 4. Practices every later stage must follow

From RP3 and RP4, with the RP sections that hold the evidence.

1. **Every value used at time t must have been knowable at t.** This one rule covers leakage, timestamps, normalisation, graphs and identity (RP3 cross-cutting). The largest measured leaks come from inside the pipeline: future-reaching feature windows and same-bar execution (Sharpe +15 to +26 in one benchmark; [[Zhang 2026 When Alpha Disappears Decision-Time Leakage]]), then survivorship and index membership, missing delisting returns and restatements (RP3 RQ3.1).
2. **Stamp knowledge time and keep vintages in-house.** Vendors give valid time but rarely knowledge time; CRSP rewrites history and FactSet links carry no first-seen date. Store retrieval time on every record and keep every version (RP2 RQ2.5, RP3 RQ3.8).
3. **Key every join on dated permanent IDs**, never tickers or current names (RP3 RQ3.8).
4. **Text time is the earliest public time**, not vendor or acceptance time; after-close items belong to the next session (RP3 RQ3.2). Every pretrained component, including small encoders and zero-shot classifiers, must have a training cutoff before the test window, or a dated checkpoint (RP4 rule e; RP1 RQ1.14).
5. **Impute from the past only, flag imputed values, and model at the frequency the data has.** Do not reconstruct intraday history from daily bars (RP3 RQ3.4).
6. **Normalise with backward windows or same-date cross-sectional ranks**, scalers fitted per walk-forward step (RP3 RQ3.6). Crash thresholds use past data only (RP3 RQ3.5).
7. **Never shuffle.** Select inside purged CV or CPCV, purge and embargo to at least the label horizon, and quote results only from an untouched walk-forward segment (RP4 RQ4.1).
8. **Count every trial and correct for it**: deflated Sharpe, PBO, SPA or an FDR hurdle on the stated count (RP4 RQ4.1, RQ4.2).
9. **Beat the mandatory baselines with the right test**: random walk and GBT (Clark–West for nested), HAR (QLIKE, DM/MCS), conditional EVT or GARCH-t (Kupiec/Christoffersen then comparative backtests), plain logit (shock), 1/N or buy-and-hold (portfolios), frozen model and periodic retraining (adaptation) (RP4 protocol table).
10. **Report costs, turnover and capacity** for any trading claim, with costs inside selection and a second backtest engine (RP4 RQ4.6, RQ4.7).
11. **Run tens of seeds and report distributions**, and run the whole pipeline on synthetic nulls once to catch leaks (RP4 rules c, d).
12. **Test every multimodal or world-state gain with placebos**: shuffled, constant and empty text; corrupted, delayed and missing feeds; whole-source dropout in training (RP1 RQ1.7, RQ1.14, RQ1.15; [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]], [[Hu 2026 Exogenous Dropout Corruption-Robust Covariates]]).
13. **Compare pretrained models with an architecture-matched random-init twin** as well as the strong baselines ([[Sungu Isiacik 2026 Random Initialization TSFM Baseline]]; RP4 rule g).
14. **Evaluate adaptation leak-free**: labels enter an update only after their horizon plus data latency, and every forecast is scored before its target can enter an update (RP4 RQ4.9; [[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]]).
15. **Shock studies use a mechanical event rule, first-public dating, placebo onsets and a preset false-alarm budget** (RP4 RQ4.5).
16. **Pin code, environment and a data snapshot** pointing at the immutable raw store (RP4 RQ4.7).

## 5. Places where sources contradict each other

Each is reconciled in its RP section; the reading given is the RP's, not a new judgement.

| Topic | One side | Other side | Reading | Where |
| --- | --- | --- | --- | --- |
| Finance token models | Kronos, StockGPT positive (cross-sectional targets) | TimesFM, FinVerse negative (per-series targets) | Not comparable: target, pretraining data and tests differ | RP1 RQ1.13 |
| Discrete vs continuous input | Kronos and TOTEM favour tokens | VAIOM favours continuous input with bucketed output; Chronos moved to patches | Contrasts differ (input only vs input and output) | RP1 RQ1.10 |
| GNN vs neighbour average | GAT Sharpe 4, neighbour average useless ([[Gorduza 2024 Alpha from Analyst Networks]]) | Neighbour average alpha 1.68%/month ([[Ali 2020 Shared Analyst Coverage Momentum Spillover]]) | No same-feature, point-in-time, net-of-cost comparison | RP1 RQ1.4 |
| LLM sentiment | Pro-LLM results (Kirtac; Lopez-Lira & Tang) | Null or FinBERT-favouring results | Split follows memorisation control | RP1 RQ1.3 |
| Text fusion | Large gain with a pre-cutoff 8B LLM ([[Koval 2025 Modality-Specific Experts Text and TS]]) | No text information about daily returns ([[Zhou 2026 When Context Routing Helps Fusion]]) | Split follows point-in-time control and baseline strength | RP1 RQ1.7 |
| Macro conditioning | Large trading-Sharpe gain ([[Oliveira 2026 HANET Macro-Aware Mixed-Frequency Attention]]) | Tiny forecast gains against strong baselines (Ye 2026, Zhao 2026) | All agree naive concatenation hurts | RP1 RQ1.15 |
| Crisis predictability | Crises are predictable (Greenwood 2022) | An unpredictable component remains (Beutel 2019) | Probability over years yes; timing no | RP1 RQ1.8 |
| Sign of pretrained look-ahead | Seeing the future inflates text results ([[Yan 2026 DatedGPT Time-Aware Pretraining]]) | Post-origin exposure usually worsens numeric TSFM forecasts ([[Chen 2026 Look-Ahead Bias Pretrained Forecasting Models]]) | Exclude contamination by design; do not correct for it | RP3 RQ3.1, RP4 RQ4.5 |
| CPCV vs walk-forward | CPCV lowest PBO (Arian 2024, abstract) | Time-ordered hold-out most accurate on non-stationary series (Cerqueira 2020) | CPCV inside, walk-forward outside | RP4 RQ4.1 |
| AUROC for warnings | Policy-neutral standard (Drehmann 2014) | Saturates at low prevalence (Nikolopoulos 2025) | AUROC for slow gauges; preset false-alarm budget for daily detectors | RP4 RQ4.3 |
| Net value of ML portfolios | Largely gone in liquid, constrained settings (Avramov 2023, Zhang 2026) | Large net Sharpe above the NYSE median (Jensen 2026) | Jensen needs costs in the objective | RP4 RQ4.6 |
| Pre-training vs fine-tuning | Pre-training rescues optimisation (Coolsaet 2026) | Fine-tuning can hurt (Nguyen 2026) | Both lose to the frozen model or a simple baseline on their own data | RP4 RQ4.4 |
| Inside the sentiment module | Stated aim: domain vocabulary | VADER, a generic lexicon, keeps 25–50% of the score | Lexicon evidence argues against that share | RP5.2 |

## 6. Evidence gaps

The gaps that bear most on the project's own design come first.

1. **Token vs continuous input** with the same backbone and output, against GARCH/HAR and GBT, walk-forward, with costs (RP1 RQ1.10, RQ1.13). No rollout-error measurement for daily or hourly price-token models; no VaR/ES backtest of sampled token paths.
2. **A full world-state model vs price-only** (cross-asset, macro, graph, events; singly and combined; equal tuning; corrupted feeds) (RP1 RQ1.15: thin).
3. **Pretraining objectives** (masked, contrastive, multi-step, next-token) compared under walk-forward with a random-init twin and a GBT baseline (RP4 RQ4.8).
4. **Adaptation on market data under delayed labels**, forgetting and rollback; MAML-inspired meta-learning has two Weak finance studies (RP4 RQ4.9; RP1 RQ1.9).
5. **Text forms compared on the same data** (scores, descriptors, event codes, embeddings, interleaved tokens) in a non-LLM sequence model; no point-in-time GDELT/CAMEO study against price-only (RP1 RQ1.14).
6. **Text-based warnings** for equity drawdowns, out of sample, with false alarms per year and lead times against a VIX baseline; no controlled gray-swan test of a financial model (RP1 RQ1.5, RQ1.8).
7. **Independent corroboration** as a point-in-time feature; out-of-sample bot-filtering ablations (RP1 RQ1.11).
8. **Strictly as-known vs back-filled graphs** and identity errors: their effect on forecasts is unmeasured (RP3 RQ3.7, RQ3.8).
9. **Net-of-cost results for tokenised or multimodal models** on a liquid US universe; no prospective results for daily equity ML (RP4 RQ4.6).
10. **Data quality of the shortlisted APIs** against CRSP, their outage histories and delisted coverage (RP2 RQ2.7); Reddit, X Developer Policy, Tiingo and Databento terms; infrastructure-event sources (RP2 RQ2.2, RQ2.6, RQ2.9).
11. **Untested vault items**: Black-Litterman and robust Bayesian allocation fed by ML views, Captum attributions, long-text chunking, the nlptown model on financial text (RP5).
12. **Unchecked numbers**: 21 RP1 journal papers and 18 RP4 classics were read as working papers, summaries or abstracts; their figures are not checked against published versions (RP1 and RP4 Assumptions). Each RQ section also lists top-up sources seen but not opened.

## 7. Questions the methodology plan must settle

Grouped and de-duplicated from the five papers' Open questions; each names where its evidence sits.

**Targets and success tests**
1. What is the stated forecasting target, horizon and success test that replaces "consistent profitability" (e.g. Clark–West against a random walk, QLIKE against HAR, net Sharpe against 1/N)? (RP5 Q1; RP4 protocol)
2. Which shock definition: mechanical event rule, candidate pool, warning window and false-alarm budget, fixed before any detector is run? Aim at fast detection plus a slow fragility gauge, rather than timing prediction? (RP1 RQ1.8; RP4 Q5)
3. Which forecast horizon and rebalancing frequency keep turnover low enough for signals to survive costs, and which cost model, investor size and universe? (RP1 RQ1.1; RP4 Q6)

**Model design**
4. Predict a categorical distribution over volatility-normalised return buckets while feeding inputs as continuous or hybrid vectors? Which tail handling beyond the bin range? Emit the horizon directly rather than roll out? (RP1 RQ1.10, RQ1.13)
5. Should added state (text, macro, cross-asset, graph, events) enter only through gated, residual or bounded pathways on a price model that works alone, with plain concatenation as a negative control and whole-source dropout in training? (RP1 RQ1.7, RQ1.15)
6. Should graph information enter first as neighbour-average features in a GBT, with a GNN only if it beats that on the same graph? Which graph sources are built point-in-time? (RP1 RQ1.4; RP3 RQ3.7)
7. Which compact text form first: a return-supervised small-encoder score per firm-day plus a few descriptors, with embeddings and event codes as ablations? Which encoders with documented cutoffs, or dated encoders? (RP1 RQ1.14; RP5 Q2–Q3)
8. Should every tail output sit on a volatility-filtered fat-tailed base with any ML model judged against it, and which conformal scheme on top? (RP1 RQ1.6)
9. Is finance-native pretraining worth its compute, and which ablation set (next-token vs derived-target reconstruction vs direct multi-horizon), each with a random-init twin and GBT? (RP1 RQ1.1; RP4 Q8)
10. Does any adaptation beyond periodic retraining enter the build, and with what label-delay protocol, held-out tickers and fallback-to-frozen rule? (RP1 RQ1.9; RP4 Q9)
11. Forecast-then-decide (forecaster plus transparent allocation) rather than end-to-end RL? Is any portfolio layer needed in the first build? Does anything in the A\*/TD3/MAML prototype survive? (RP1 RQ1.9; RP5 Q5–Q6)

**Data and storage**
12. Which price vendor goes first in a trial, with which survivorship-free reference, and what happens if its terms ban or stay silent on training? (RP2 RQ2.6, RQ2.7)
13. Where do macro vintages come from, given FRED's training ban? (RP2 RQ2.3)
14. Which layer gives as-known reads (version-per-write store, bitemporal tables, dated Parquet), which permanent identifier set, and how is knowledge time assigned to valid-time-only sources? (RP2 RQ2.5, RQ2.8; RP3 RQ3.8)
15. Should the text pipeline store, per item, a repetition score, first-report flag, source type and time since first trace? (RP1 RQ1.11, RQ1.12)

**Evaluation**
16. How long is the untouched final segment, how wide the purge and embargo, what counts as a trial, and which correction applies? (RP4 Q1–Q2)
17. Which baselines are mandatory per target, the seed budget per configuration, and which labels (fixed horizon, triple barrier, trend scanning) chosen on validation only? (RP4 Q3, Q7; RP3)
18. Which of the direction note's §9.2 ablations come first? (RP5 Q7; section 8 below)

## 8. The direction note's open decisions and ablations

For [[Financial Foundation Model Research Direction]] §13 (ten open architectural decisions) and §9.2 (required ablations): the evidence found for and against each option. Verdicts on the note as a whole are in [[RP5 Vault Review#RP5.7 – Financial Foundation Model Research Direction (2026-11-07)|RP5.7]].

### 8.1 Section 13: open architectural decisions

| # | Decision | Evidence for | Evidence against / caution | State of evidence | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Balance of autoregressive token prediction vs continuous numerical modelling | A categorical output over normalised return buckets is a sound target ([[Shi 2025 Kronos Financial Foundation Model]], [[Ma 2026 VAIOM Continuous-Input Discrete-Output]]); Kronos's own tokenizer ablation favours discrete | Continuous input with bucketed output beat tokenized input (VAIOM); rollout error compounds; sampled tails poorly calibrated (Decker 2026); per-series token/TSFM forecasts no better than base rate (Cheung 2026) | Low; the matched ablation is missing. Leans to continuous or hybrid inputs with a categorical, direct multi-horizon output | RP1 RQ1.10, RQ1.13 |
| 2 | One shared model with specialised pathways vs coordinated encoders plus shared layers | Gated, residual and mixture-of-experts pathways with regime routing help modestly (Ye 2026; Koval 2025 modality experts) | No study compares the two layouts; unconstrained attention over all inputs hurts | Low; the evidence is on how inputs enter (gated, compressed), not on layout | RP1 RQ1.7, RQ1.15; RP4 RQ4.4 |
| 3 | Graph operations outside vs relationships learned inside the transformer | Neighbour averages outside the model match GNNs (Xu 2021; Huang 2023 TGB heuristics); shocks spread along supply chains (Barrot 2016) | A GAT reported large Sharpe (Gorduza 2024), not replicated; correlation graphs go near-complete in crises | Medium for "compute simple graph features outside first"; Low for learned relations | RP1 RQ1.4; RP3 RQ3.7 |
| 4 | Interaction of text representations and structured event tokens | Return-supervised encoder scores carry cross-sectional signal (Kirtac 2026); event triplets beat sentiment and embedding baselines in one Weak study whose LLM extractor had no memorisation control ([[Li 2025 Structured Event Representation Returns]]) | Scalar sentiment adds little to strong price models; no point-in-time GDELT/CAMEO study against price-only; text placebos often show no use of content (Sridhar 2026) | Low; no study compares the forms on the same data | RP1 RQ1.14 |
| 5 | Pretraining objectives beyond next-token | Derived-target (indicator) reconstruction is the most promising lead ([[Chen 2026 DIVINE Indicator Reconstruction Pretraining]]); index pre-training eased optimisation (Coolsaet 2026) | No objective beats next-token or direct training under a strong financial test; random-init twins often match pretrained models (Sungu Isiacik 2026) | Low | RP4 RQ4.8 |
| 6 | What counts as a MAML adaptation task | Tasks by stock, regime or new listing used in two Weak studies ([[Liu 2025 Robust Meta-Learning Zero-Shot Financial]], [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]]) | Light adaptation matched meta-learning (Wu 2026, Pan 2026); the archived prototype's shuffled support/query split leaks (RP5.5) | Low; if tried, tasks must be time-ordered with support strictly before query | RP1 RQ1.9; RP4 RQ4.9 |
| 7 | Company/sector adaptation vs global market adaptation | Adaptive window choice helps risk forecasts ([[Li 2026 Adaptive Window Selection Risk]]); periodic retraining is the baseline to beat ([[Dasari 2026 When to Retrain Drift Policies]], non-finance) | Under delayed labels, published test-time adapters gain at most 0.5% (Fentazi 2026, non-finance); label leakage inflated adaptation gains by up to 110% (RP4 RQ4.9) | Low; no finance study of hierarchical adaptation | RP4 RQ4.9 |
| 8 | Genuine early-warning signals without overfitting to past black swans | Slow gauges generalise across eras (Greenwood 2022); novelty works monthly (Glasserman 2019, 2023); mechanical event screens shrink curated effects (3.49× to about 0.5–1.6×) | Timing not predictable; models fail beyond the largest events seen (Sun 2024); tens of events only | Medium for the approach: plain logit or small regularised models, held-out larger extremes (gray-swan test), preset false-alarm budget | RP1 RQ1.5, RQ1.8; RP4 RQ4.5 |
| 9 | Representing market awareness and what is already priced in | Scheduled news in liquid stocks is priced in milliseconds to seconds (Chordia 2018); options and pre-announcement drift carry anticipation (Pan 2006, [[Lucca 2015 Pre-FOMC Announcement Drift]]); slower diffusion across linked, small and foreign markets ([[Kargarzadeh 2026 When Is News Priced In]]) | Pre-FOMC drift faded after 2015 ([[Kurov 2021 Disappearing Pre-FOMC Drift]]); no walk-forward test of pre-publication measures as features | Medium that option-implied and first-report/follow-up features are the candidates; Low on their forecast value | RP1 RQ1.11, RQ1.12 |
| 10 | Evidence required before promoting an adapted state into a new release | The leak-free adaptation protocol (labels after horizon plus latency; score before update; frozen and retraining baselines; held-out tickers) and the trial-count rules | No finance study of rollback or forgetting | Medium for the protocol (RP4); Low for any specific threshold | RP4 RQ4.9, protocol table |

### 8.2 Section 9.2: required baselines and ablations

| Ablation | Evidence so far | What it adds to RP4's protocol | Priority suggested by the gaps | Where |
| --- | --- | --- | --- | --- |
| Continuous-feature vs discrete-token model | Contradictory, no matched test (section 8.1 #1) | Same backbone and output; GARCH/HAR and GBT beside it | First: it tests the project's central premise | RP1 RQ1.10, RQ1.13 |
| Fixed vs learned vs hybrid tokenizer | Kronos ablation and TOTEM favour learned codebooks; no finance test of motif (BPE) tokens | Tail-bucket calibration in a stress period | After the first ablation, only if tokens win | RP1 RQ1.10 |
| Foundation model alone vs plus contextual memory | Context and retrieval adaptation weakly supported; regime retrieval cited but not opened | Leak-free context: memory holds only items knowable at t | Medium | RP1 RQ1.9; RP4 RQ4.9 |
| Foundation plus context vs plus parameter adaptation | Light adaptation matches heavy; fine-tuning can hurt (Nguyen 2026) | Frozen model and periodic retraining as baselines | Medium | RP4 RQ4.4, RQ4.9 |
| MAML-inspired vs simpler adaptation | Two Weak finance studies for MAML; simpler methods match | Time-ordered tasks; delayed labels | Low, unless simpler adaptation is shown to help first | RP1 RQ1.9; RP4 RQ4.9 |
| With vs without temporal knowledge graph | Linked-firm effects real; GNNs no better than neighbour features | As-known graph vs back-filled graph; neighbour-average GBT baseline | Second: cheap as neighbour features, and the as-known vs back-filled gap is unmeasured | RP1 RQ1.4; RP3 RQ3.7 |
| With vs without global event intelligence | Novelty works monthly; event alarms unreliable; scalar sentiment adds little | Shuffled, constant and empty text placebos; first-report flags | Second, at monthly or slower horizons | RP1 RQ1.5, RQ1.14 |
| Individual domains vs combined multidomain training | Added state helps only when gated; corrupted feeds fall below price-only | Corrupted, delayed and missing-feed tests; whole-source dropout | Third, after single-domain gains exist | RP1 RQ1.15 |

RP5.7 notes that RP4's protocol also adds what §9.2 does not list: trial-count corrections, nested baselines (random walk, GBT, HAR, 1/N), random-init twins and placebo controls (RP4 rules a–g).

## Assumptions made during the synthesis

1. No new search was run. No gap was narrow enough to be settled by one or two sources; the gaps in section 6 are experiments, not missing reading.
2. Ranks in section 2 are this session's ordering of the RP findings by evidence strength and RP confidence; where two methods have similar evidence, the simpler one is ranked first, following RP1 cross-cutting 1.
3. "Priority suggested by the gaps" in section 8.2 is an ordering of what the evidence leaves open, offered for the methodology plan. It is not a decision.
4. The vault-wide source counts come from lit-note `evidence` properties (357 notes); paper counts come from each paper's properties and overlap.
5. Numbers quoted here are copied from the RP sections, which hold the page references; the working-paper caveats in RP1 and RP4 Assumptions apply to them.

## References

The five papers, whose References sections hold full citations and link every lit note: [[RP1 ML Methods]], [[RP2 Data Sources and Storage]], [[RP3 Cleaning and Labelling]], [[RP4 Training and Evaluation]], [[RP5 Vault Review]]. Lit notes named directly in this synthesis (each verified in RP1–RP4's citation checks):

[[Ali 2020 Shared Analyst Coverage Momentum Spillover]] · [[Barrot 2016 Input Specificity Shock Propagation]] · [[Beutel 2019 ML vs Logit Banking Crisis Warning]] · [[Brini 2026 TSFMs vs Econometric Realized Volatility]] · [[Chen 2026 DIVINE Indicator Reconstruction Pretraining]] · [[Chen 2026 Look-Ahead Bias Pretrained Forecasting Models]] · [[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]] · [[Christensen 2023 Machine Learning Volatility Forecasting]] · [[Cohen 2008 Economic Links Predictable Returns]] · [[Dasari 2026 When to Retrain Drift Policies]] · [[Decker 2026 Calibration of Probabilistic TSFMs]] · [[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]] · [[Foley 2026 NoLBERT News Topics Returns]] · [[Garcia Seuma 2026 Crypto Cascade Early Warning]] · [[Glasserman 2019 Unusual News Forecast Market Stress]] · [[Glasserman 2023 New News is Bad News]] · [[Go 2026 FinPILOT Inference-Time Planning RL]] · [[Gorduza 2024 Alpha from Analyst Networks]] · [[Greenwood 2022 Predictable Financial Crises]] · [[Gu 2020 Empirical Asset Pricing Machine Learning]] · [[Hu 2026 Exogenous Dropout Corruption-Robust Covariates]] · [[Jensen 2026 ML Implementable Efficient Frontier]] · [[Kargarzadeh 2026 When Is News Priced In]] · [[Kirtac 2026 MFAST News Trading Under Frictions]] · [[Koval 2025 Modality-Specific Experts Text and TS]] · [[Kurov 2021 Disappearing Pre-FOMC Drift]] · [[Li 2025 Structured Event Representation Returns]] · [[Li 2026 Adaptive Window Selection Risk]] · [[Lis 2026 ModernFinBERT News Volatility HAR]] · [[Liu 2025 Robust Meta-Learning Zero-Shot Financial]] · [[Lopez-Lira 2025 LLM Memorization Problem]] · [[Lucca 2015 Pre-FOMC Announcement Drift]] · [[Ma 2026 VAIOM Continuous-Input Discrete-Output]] · [[Manela 2017 News Implied Volatility Disasters]] · [[Oliveira 2026 HANET Macro-Aware Mixed-Frequency Attention]] · [[Pan 2006 Option Volume Future Stock Prices]] · [[Pollok 2026 End-to-End Policies vs Simple Rules]] · [[Rahimikia 2025 ReVisiting TSFMs in Finance]] · [[Shi 2025 Kronos Financial Foundation Model]] · [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]] · [[Sun 2024 AI Weather Gray Swan Cyclones]] · [[Sungu Isiacik 2026 Random Initialization TSFM Baseline]] · [[Taylor 2025 Combining VaR and ES Forecasts]] · [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]] · [[Xu 2021 HIST Concept Graph Stock Forecasting]] · [[Yan 2026 DatedGPT Time-Aware Pretraining]] · [[Ye 2026 Regime-Gated Residual MoE Volatility]] · [[Zhang 2026 Deep TS Models Equity Portfolios]] · [[Zhang 2026 When Alpha Disappears Decision-Time Leakage]] · [[Zhou 2026 When Context Routing Helps Fusion]]
