# FW-0.1 Prototype Review: Corrections and Suggestions

Nov 10, 2026 · @Dave

This reviews the *Financial World Model Prototype Proposal* and *Developer Backlog* (FW-0.1) against the final Synthesis and RP1–RP5 in the research vault. I checked the dependency facts on the web on 2026-11-10. Section references such as "Synthesis §4" or "RP2 RQ2.6" point to the vault notes that hold the evidence.

## Summary

Both documents are in good shape. They already follow many of the research's rules: point-in-time data, chronological splits with an embargo, HAR used only as a volatility benchmark, staged rather than mandatory end-to-end training, modality ablations, snapshot manifests, and baselines before neural work.

The review is split by document. **Part A** covers the Proposal: the hypothesis, data, storage and evaluation design, with the evidence behind each change. **Part B** covers the Backlog: the ticket, gate and sprint changes. Several problems appear in both documents. For those, the reasoning is in Part A, and Part B gives the ticket change with a pointer back (for example "see A1.1").

| Main problem                                                                 | Proposal | Backlog |
| ---------------------------------------------------------------------------- | -------- | ------- |
| The token-versus-continuous experiment is missing                            | A1.1     | B1.1    |
| Alpaca history starts in 2016; training starts in 2015                       | A1.2     | B1.2    |
| Alpha Vantage macro data falls under FRED's training ban and has no vintages | A1.3     | B1.3    |
| The licensing gate covers ArcticDB only                                      | A1.4     | B1.4    |
| ArcticDB versions are not point-in-time history                              | A1.5     | B1.5    |
| No append-only raw zone                                                      | A1.6     | B1.6    |
| The 10-ETF universe can't test the graph and is small for neural training    | A1.7     | B1.7    |
| RP4's evaluation rules are missing                                           | A1.8     | B1.8    |
| The test and validation periods are short                                    | A1.9     | B1.9    |

# Part A — Proposal

Corrections and suggestions for *FW-0.1 — Research Prototype Development Proposal & Coding Guide*. Section numbers refer to the proposal.

## A1. Must fix before coding starts

### A1.1 Test the central premise: token versus continuous input (§3.2F, §7.2–7.3, §8.4, §9)

**Problem.** The world model is a causal Transformer that predicts continuous latent states with an L2 loss. There is no tokenizer, no categorical output, and the experimental matrix (§9) varies only modalities. The project's scope, as logged in the Decisions Log (session 9), is an autoregressive, LLM-inspired next-token model. Synthesis §8.2 puts "continuous versus discrete-token input, same backbone and output" first in the experiment order, because no matched finance study exists (RP1 RQ1.10, RQ1.13).

**Fix.**

-  [x] Add experiment **T0** to §9, before E0–E4. It is price-only and uses the same causal backbone in three variants: (a) continuous input with a categorical output over volatility-normalised return buckets; (b) tokenized input with the same output; (c) continuous input with a direct regression head. Score all three against the random walk, GBT and HAR.
-  [x] In §7.3, emit each horizon directly rather than rolling out. Rollout error compounds, and sampled tails were off by more than ten times nominal at 1% (Decker 2026; Synthesis Q4).
-  [x] Add a tokenization component to §3.1 and the repository layout (fixed bins first, with a versioned vocabulary). Learned codebooks are a later ablation, run only if tokens win T0.
-  [ ] ~~In §7.2, demote Objective A (latent-state autoregression) to an ablation objective. No pretraining objective has beaten next-token or direct training under a strong financial test (RP4 RQ4.8).~~
-  [ ] ~~§8.4 lists cross-entropy for "latent/token prediction". That only means something once tokens exist.~~

### A1.2 Price data: Alpaca's history starts in 2016 (§4.1, §4.3)

**Problem.** RP2 RQ2.1 found that Alpaca's SIP bars start in 2016, but the training window starts in 2015.

**Fix.**

- Either start the data in 2016 and shift the splits, or take 2015 from a second source. Candidates are Alpha Vantage intraday (back to 2000, but one informal CRSP check found adjusted-close errors), Databento or FirstRate. Don't join two vendors inside one series without a reconciliation check on the overlap.
- State in §4.1 that ingestion requests the SIP feed explicitly. IEX-only bars cover a fraction of consolidated volume, so mixing feeds would corrupt volume features and 5-minute realised variance.
- Add to the limitations that all ten ETFs survived to 2025 (a selection effect). If the universe grows to single stocks (A1.7), a survivorship-free reference such as Norgate or CRSP becomes mandatory (RP2 RQ2.1, RQ2.7).

### A1.3 Macro data: Alpha Vantage can't be the source (§4.1, §5.1)

**Problem.** RP2 RQ2.6 found that Alpha Vantage's macro and commodity APIs fall under FRED terms. FRED and ALFRED ban ML/AI development and training, and caching through the API. A current-value endpoint also can't give the original-versus-revised values that §5.1's "critical requirement: data versioning" depends on.

**Fix.**

- Archive BLS original releases yourself (public domain) for CPI and unemployment.
- Use the Philadelphia Fed Real-Time Data Set (RTDSM) for vintages. Its licence isn't stated, so confirm it first.
- The fed funds rate comes from the Federal Reserve Board. Its terms were not covered by RP2, so check them.
- Remove economic indicators from Alpha Vantage's responsibilities in §4.1.
- Take availability times from the release calendar (for example, BLS releases at 8:30 a.m. ET).

### A1.4 Licences: widen the licensing gate beyond ArcticDB (§15, Project Note 4)

**Problem.** §15 treats ArcticDB as the licensing gate. RP2 RQ2.6 found that data contracts bind harder than software licences:

- Alpaca and Alpha Vantage license data for personal, non-commercial use, and neither mentions model training. Silence is not permission.
- Nasdaq's pass-through agreement covers data "as used or processed".
- yfinance sits on Yahoo terms with personal-use limits.

The proposal anticipates a possible commercial product, so this matters as much as ArcticDB.

**Fix.**

- Extend §15's licensing gate to every data source, with written vendor answers on the RP2 vendor-quote list (delisted coverage, storage after cancellation, training rights) required before any paid subscription.
- Keep a licence register per source, and tag every dataset snapshot with the licences of its inputs.
- ArcticDB: its PyPI page now says production use, "including business or commercial environments", needs a paid licence. Whether solo research counts is still open; it is on the vendor-quote list.

### A1.5 ArcticDB versions are not point-in-time history (§5.1)

**Problem.** §5.1 relies on "versioned reads for historical reconstruction". ArcticDB creates a version each time you write, so the version time is the time *your store* learned the data, not the time the source published it. If 2015–2025 is backfilled in 2026, every version is dated 2026, and a CPI value as first published in 2016 can't be recovered. RP2 RQ2.5 found no engine that covers both valid time and knowledge time. RP3 RQ3.8 found that vendors give valid time only, so vintages have to be kept in-house. The same limit applies to SurrealDB's `VERSION` time travel (§5.2), which also works only on SurrealKV.

**Fix.** Rewrite §5.1's versioning paragraph:

- Store each vintage as its own row with three times: valid time (the observation period), `available_at` (first public time) and `retrieved_at`. A point-in-time read filters to `available_at ≤ cutoff` and takes the latest row per key.
- Use ArcticDB versions and named snapshots only to make the store reproducible (the §11.5 snapshot manifest).

### A1.6 Make an append-only raw zone the source of truth (§4.4, §5.2 "Database responsibility")

**Problem.** §5.2 makes ArcticDB and SurrealDB each the owner of their data and warns against two editable copies, but there is no raw layer to rebuild from. §4.4 mentions raw-response provenance only "where permitted".

**Fix.** Add a raw layer to the §3.1 architecture (RP2 RQ2.4):

- Store every provider response as received, with request metadata, in an append-only raw zone.
- Keep a request ledger keyed by endpoint and normalised parameters, so interrupted ingestion can resume without duplicates.
- Rebuild both databases from the raw zone. Neither is then authoritative.
- Point snapshots at the immutable raw store (Synthesis practice 16). Check each licence for limits on how long raw data can be kept.

### A1.7 Fix the universe: the graph needs a path to the targets, and the neural models need more data (§3.2B, §4.2, Project Note 1)

**Graph.** Project Note 1 adds 20–50 companies to the graph, but the forecast targets are ETFs. A company graph has no route to an ETF forecast unless (a) ETF holdings are joined point-in-time (no holdings source is in the plan), or (b) the targets include those companies' stocks, which then needs survivorship-free stock prices. State which in §4.2. Also:

- Free relationship data is thin: 10-K customer disclosures above 10% of sales, and EDGAR. FactSet Revere and Compustat Segments are paid and give valid time only (RP2 RQ2.8, RP3 RQ3.7).
- In §3.2B, test neighbour-average features inside a GBT before the GNN. Bring in the GNN only if it beats that on the same graph (Synthesis Q6; RP1 RQ1.4).

**Sample size.** 10 ETFs × about 2,500 sessions is about 25,000 instrument-days, and the series are highly correlated. One RP4 study found 1.33–2.35 effective assets out of six. A 2–4 layer Transformer with a 128-session context (§7.1) will overfit that.

**Fix.** Train the neural models on a broader survivorship-free stock panel (for example several hundred names) and keep the 10 ETFs as a fixed evaluation set. Otherwise, state that the S0 runs of E0–E4 are pipeline tests, not tests of the hypothesis.

### A1.8 Add RP4's mandatory evaluation rules (§2.3, §8, §9, §12)

These are missing (RP4 protocol table, rules a–g; Synthesis §4):

- **One primary metric per target, fixed in advance (§2.3; Synthesis Q1).** The proposal lists seven possible areas of success. Across several horizons and ten instruments, that invites picking whichever comparison happens to win. Fix the primary metrics:
  - Returns: MSE and R²oos against zero or the historical mean, with sign accuracy secondary
  - Volatility: QLIKE and MSE on 5-minute realised variance
  - Tails: Kupiec and Christoffersen tests first, then tick loss and the Fissler–Ziegel score
  - Distributions: log score, CRPS or pinball loss, with PIT histograms
- **Trial counting (§8.5).** Every configuration, loss weight, seed and hyperparameter counts as a trial. Apply deflated Sharpe, PBO, SPA or an FDR hurdle on the stated count.
- **The right tests (§8.5).** Clark–West for nested comparisons (random walk versus model; HAR versus HAR+X). DM on QLIKE for non-nested volatility models. MCS or SPA across the model set.
- **Missing baselines (§8):**
  - GARCH-t or conditional EVT for the return-distribution and tail heads
  - A plain logit for regime and shock targets
  - The historical mean for returns
  - Log-HAR beside HAR
  - An architecture-matched random-init twin for any pretrained encoder (Synthesis 13)
- **Placebos for every gain from an added modality (§9):** shuffled, constant and empty text; corrupted, delayed and missing feeds; plain concatenation as a negative control; whole-source dropout in training (Synthesis 12).
- **Seeds (§12.4).** Run tens of seeds per configuration and report the distribution, not the best run.
- **Synthetic null (§12.3).** Run the whole pipeline once on synthetic nulls to catch leaks.
- **Encoder cutoffs (§12.3).** Every pretrained encoder needs a training cutoff before the test window (2024), or dated checkpoints. Many recent encoders were trained on web text from 2024–2025. Fit encoders and scalers on each walk-forward step's training data only.

### A1.9 The test period is too short for tail claims, and one validation year is thin (§4.3)

- 2024–2025 is about 500 sessions, which gives about five exceedances at 1% VaR. RP4 RQ4.3 says ranking tail models at 1–2.5% needs several years of daily test data. Either drop tail-ranking claims from FW-0.1, or report the exceedance counts and treat the results as descriptive.
- 2023 is a single validation year. Use expanding walk-forward refits (for example yearly, 2019 to 2023) with purged CV inside for selection, and keep 2024–2025 untouched (RP4 RQ4.1).
- Set the purge and embargo to at least the label horizon.

## A2. Should fix (design)

### A2.1 Fusion: start with gated pathways on a price model, not open cross-attention (§3.2E)

§3.2E leads with cross-attention. RP1 RQ1.7 and RQ1.15 found that added state helps only when it is compressed and fed through a gated, residual or bounded pathway on top of a price model that already works alone. Naive concatenation and unconstrained attention hurt, and corrupted feeds fell below price-only. Make fusion v1 a gated residual correction per modality on E0's output (or on HAR), and run cross-attention as a v2 ablation. In §9, order the ablations as Synthesis §8.2 suggests: T0 first; then graph (as neighbour features) and events (at monthly or slower horizons); combined multidomain training last.

### A2.2 Language encoder: settle the contradiction and choose a compact text form (§3.2C, §7.1)

- §3.2C says "trainable from scratch" with masked language modelling, but the Backlog (FWM-006.3) says frozen and pretrained, with from-scratch training as a later experiment. The Backlog is closer to the evidence, so bring §3.2C and §7.1 into line.
- Start with a return-supervised small-encoder score per firm-day plus a few descriptors, and run embeddings and event codes as ablations (RP1 RQ1.14; Synthesis Q7). Scalar sentiment added to HAR was negative (Lis 2026).
- With ETF targets, firm-level text has to be mapped to ETFs through holdings. This is the same gap as the graph (A1.7).
- Text time is the earliest public time, and after-close items belong to the next session (RP3 RQ3.2). §6.3 says this already; keep it.
- News sources in §4.1:
  - Alpha Vantage news and Alpaca news: training rights are not stated, and history depth should be checked.
  - Alpha Vantage's precomputed sentiment comes from an undisclosed model with an unknown training cutoff, so use it as a cross-check, not as a feature.
  - GDELT (any use, with citation) and EDGAR 8-K filings (public, with exact acceptance times) are licence-clean.

### A2.3 Define the regime target mechanically, from past data only (§3.2G, §7.2 Objective C)

"Market-regime classification" has no definition. RP3 RQ3.5 says thresholds must come from past data only; an HMM fitted on the full sample leaks. Define the regime from something like a trailing percentile of realised volatility, and add a plain logit baseline. If shock work enters FW-0.1, aim it at fast detection after onset plus a slow fragility gauge, not at timing (Synthesis §2.4).

### A2.4 HAR-RV details (§6.1, §7.2 Objective B, §8.1)

- §6.1's "realized volatility using daily returns" is fine as a feature, but it must not be HAR's input or target; HAR uses intraday realised variance. Say so in §8.1.
- In §8.1, define the weekly component as the mean of the last 5 daily RVs and the monthly component as the mean of the last 22. Fix one scale (variance or volatility), and add Log-HAR as a second benchmark.
- §7.2 trains volatility with MAE but evaluates with QLIKE (§8.4). Train on QLIKE (or on log RV), or justify the mismatch.
- USO had a 1-for-8 reverse split in April 2020 and changed how it held futures during that year's oil crash. Name it in §4.2 as a known structural break.

### A2.5 Corporate actions: store raw prices and adjust at read time (§5.1 bar schema)

The §5.1 bar schema stores `adjusted_close` beside raw prices. RP3 RQ3.3 recommends storing raw prices with a corporate-actions table, applying factors at read time, and cross-checking against a reference.

- Back-adjusted price levels embed future splits. Use ratio features (returns, distance from a moving average), or adjust as of each cutoff.
- TLT, XLF and the others pay distributions. Use total-return series for return targets, and say so.

### A2.6 Data contracts (§5.2, §11.2)

- **§11.2 MarketBar example:**
  - Add a permanent `instrument_id` rather than the ticker (RP3 RQ3.8)
  - Add the bar interval, and whether the timestamp marks the bar's start or end
  - Add `available_at`, `feed` (SIP or IEX), `retrieved_at` and `request_id`
- **§5.2 document and embedding fields:**
  - Documents: add `first_seen_at`, `source_type` and `licence_id`, plus the repetition and first-report fields (Synthesis Q15)
  - Embeddings: add the encoder's training cutoff and the training window used
- **Validation at scale.** Checking millions of bars one Pydantic object at a time is slow. Use Pydantic at API and configuration boundaries, and a DataFrame schema check (for example pandera) for bulk data. §11.2 already says dataset-level checks are needed.

### A2.7 Storage and async (§5.2, §11.1, §11.3–11.4)

- For 20–50 companies, edge tables in Parquet with DuckDB are simpler than a graph database. In the one benchmark RP2 found (Weak, vendor-authored), edge tables beat native graph engines on scans and joins. Keeping SurrealDB is reasonable, but present it as replaceable behind the repository interface, not as a fixed part of the architecture.
- §11.1 asks for async interfaces for every database operation. ArcticDB is synchronous, and a batch research pipeline gains little from async. Limit async to HTTP provider calls, and make the §11.4 `DatasetBuilder.build` synchronous.

### A2.8 Python version (§11.1)

PyTorch, PyTorch Geometric 2.8 and ArcticDB 6.16 all support Python 3.14 now. The SurrealDB SDK states only Python 3.10 or later. §11.1's ArcticDB statement is confirmed. Allow Python 3.13 as the fallback if a direct dependency fails, rather than hard-pinning `>=3.14,<3.15`.

## A3. Editorial fixes

- [x] Delete the stray "Database+1" line after Project Note 4.
- [x] Strip `?utm_source=chatgpt.com` from the links.
- [x] The formulas use `[ … ]` and `( … )` delimiters, which don't render in Obsidian or GitHub. Use `$$ … $$` and `$ … $`.
- [ ] The §10 repository layout differs from the Backlog: the proposal has `acquisition/alpaca.py`, `storage/arctic.py` and `normalization/`, while the Backlog has `acquisition/providers/`, `storage/arctic/` and `features/`. Make the Backlog authoritative and point §10 to it.
- [ ] The proposal is in effect the methodology plan. Add a table that maps each of the 18 Synthesis §7 questions to the decision taken, and log those decisions in the Decisions Log.

## A4. Keep as they are

- The research framing: not a trading application, success not required on every metric, compute cost measured (§1, §2.3)
- HAR compared only with the volatility head (§8.1)
- Publication-time and availability-time rules (§6.3)
- Train-only normalisation (§6.1)
- 2026 held back for prospective evaluation (§4.3)
- Missing-modality handling without fabricated observations (§3.2E)
- The encoder output contract with validity masks and modality IDs (§11.6)
- yfinance used for exploration only (§4.1)
- The sequencing rule: no neural development before reproducible datasets and baselines

# Part B — Developer Backlog

Corrections and suggestions for *FW-0.1 — Developer Implementation Backlog & Coding Specification*, by ticket. Where the reasoning is already given in Part A, the item points to it.

## B1. Must fix before coding starts

### B1.1 Token-versus-continuous experiment (see A1.1)

- **FWM-006:** add a ticket for `src/fwm/tokenization/` (fixed bins and a versioned vocabulary). Acceptance tests: the vocabulary version is recorded in the snapshot manifest; bin edges are fitted on training data only; tail buckets beyond the bin range are handled.
- **FWM-007.3:** add a categorical output with direct multi-horizon heads. Keep latent-state prediction as an ablation objective.
- **FWM-007.6:** add T0 (price-only; continuous versus tokenized input versus a regression head, same backbone) before E0.

### B1.2 Alpaca adapter (FWM-002.3; see A1.2)

- Request the SIP feed explicitly, and store `feed` on every bar.
- Data starts in 2016. Either change the configuration's `start_date` (§11) to 2016, or add a second-source adapter for 2015.
- New acceptance test: where two sources overlap, they are reconciled before joining.

### B1.3 Macro sources (FWM-002.4, FWM-004.3; see A1.3)

- Add tickets for a BLS release archiver and an RTDSM vintage adapter, each setting `available_at` from the release calendar.
- FWM-004.3's "macro revisions are reconstructed correctly" test can pass only with these sources.

### B1.4 Licence register (FWM-001 or FWM-002; see A1.4)

- Add a ticket for a licence register with these fields: source, terms URL, date read, storage allowed, training allowed, commercial use allowed.
- FWM-003.6 snapshot manifest: add the licences of every input.

### B1.5 ArcticDB repository (FWM-003.1, FWM-003.3; see A1.5)

- **FWM-003.1:** "Retrieve historical versions" supports reproducibility only. Point-in-time reads come from `available_at` rows. Use named snapshots, because unnamed old versions can be pruned. ArcticDB allows one writer per symbol and the last writer wins, so the orchestrator must serialise writes per symbol.
- **FWM-003.3:** SurrealDB `VERSION` time travel has the same limit. Temporal edges keep their `valid_from`, `valid_to` and `observed_at` fields (FWM-003.4 is right).

### B1.6 Raw zone and request ledger (FWM-002.6, FWM-003.5; see A1.6)

- Add a ticket ahead of FWM-002.6: an append-only raw zone and a request ledger keyed by endpoint and normalised parameters. The ledger is what makes "interrupted operations resume without duplication" testable.
- **FWM-003.5:** with a raw zone, reconciliation becomes "rebuild both stores from raw and diff". Remove the language about an authoritative copy.

### B1.7 Universe and graph (FWM-006.2; see A1.7)

- Add a dataset ticket that decides how the graph reaches the targets: a point-in-time ETF holdings source, or company stocks as targets with a survivorship-free price reference.
- **FWM-006.2:** before the GNN, add a baseline of neighbour-average features inside a GBT. Make the forecast target the graph's objective, and drop link prediction as the primary objective; with about 50 nodes and few verified edges it won't train meaningfully.
- If the neural models stay on 10 ETFs, label the S0 runs of FWM-007.6 as pipeline tests.

### B1.8 Evaluation rules (see A1.8)

- **FWM-001.4:** add a trial log. Every configuration, loss weight, seed and hyperparameter gets a trial ID, and the count feeds the multiple-testing correction.
- **FWM-005:** add tickets for GARCH-t or conditional EVT, Log-HAR, a plain logit and the historical mean.
- **FWM-006.x:** train each encoder on the walk-forward training fold only. Record every pretrained encoder's training cutoff, and make the acceptance test fail if the cutoff falls inside the test window. FWM-006.5: add an architecture-matched random-init twin.
- **FWM-007.6:** add placebo runs (shuffled, constant and empty text; corrupted, delayed and missing feeds), plain concatenation as a negative control, whole-source dropout in training, and tens of seeds per configuration.
- **FWM-008.1:** add R²oos, CRPS, log score, pinball loss, tick loss, the Fissler–Ziegel score, Kupiec and Christoffersen tests, and PIT. Make directional accuracy secondary.
- **FWM-008.3:** add Clark–West for nested models, and MCS/SPA across the model set.
- **New test ticket:** run the whole pipeline once on synthetic nulls; no signal should be found.

### B1.9 Splits (FWM-004.5, FWM-008.2; see A1.9)

- Replace the single 2023 validation year with expanding walk-forward folds and purged CV inside for selection. Keep 2024–2025 untouched.
- Set the embargo to at least the label horizon. Drop or warm up the first 22 sessions of each fold for the monthly HAR term.
- Add the exceedance counts to the tail-risk reports.

## B2. Should fix (design)

- **FWM-007.2 (see A2.1):** make v1 a gated residual correction per modality on the price model, and move cross-attention to a v2 ablation. Acceptance test: performance with the added modality corrupted is no worse than price-only.
- **FWM-006.3 (see A2.2):** frozen pretrained is the right start; keep it. Add the first text form (a return-supervised small-encoder score per firm-day), the ETF-to-firm mapping, and GDELT and EDGAR 8-K adapters. Use Alpha Vantage sentiment only as a cross-check.
- **FWM-005.2 and FWM-007.4 (see A2.3):** define "regime" before implementing the "last-known-regime" baseline or the regime head. Use past-data thresholds only.
- **FWM-004.2 (see A2.4):** specify:
  - 5-minute sampling in the regular session (9:30–16:00 ET), with half-days handled
  - The overnight return, either as a separate term or excluded, chosen once and documented
  - A minimum number of intervals per day
  - SIP data only, never mixed with IEX
  - HAR components averaged over 5 and 22 days, with Log-HAR alongside
- **FWM-003.1 and FWM-002.3 (see A2.5):** add a corporate-actions table. Store raw OHLCV and apply split and dividend factors at read time. Check USO's April 2020 split.
- **FWM-002.1 (see A2.6):**
  - MarketBar: add `instrument_id`, the bar interval, the timestamp convention, `available_at`, `feed`, `retrieved_at`, `request_id`, and VWAP and trade count where given
  - FinancialEvent: add a valid time separate from `published_at`, and `first_seen_at`
  - NewsDocument: add `first_seen_at`, `source_type`, `licence_id` and the repetition and first-report fields
  - Use a DataFrame schema check for bulk validation
- **FWM-003.2:** key every join on the permanent `instrument_id`; symbol names stay for display.
- **FWM-003.3 (see A2.7):** move SurrealDB from sprint 1 to sprint 2 or 3, since nothing needs it before FWM-006.2. If kept:
  - Pin SDK 3.0 or later (SDK version 2 can't write datetimes to SurrealDB 4.0).
  - The SDK README I read says client-side transactions work only over WebSocket connections. Write the batch-write test for that.
- **FWM-004.4:** make `DatasetBuilder.build` synchronous. Keep async for provider HTTP calls only.
- **FWM-001.1 and FWM-001.2 (see A2.8):**
  - PyTorch 2.9+, PyTorch Geometric 2.8 and ArcticDB 6.16 have Python 3.14 wheels.
  - The SurrealDB SDK needs testing on 3.14.
  - MLflow and the text libraries were not checked.
  - Allow Python 3.13 as the fallback.
- **FWM-005.7:** add these fields to the results schema: seed, trial ID, fold ID, forecast-origin and target timestamps, test name, statistic and p-value.
- **FWM-008.6:** say that synthetic scale runs test the plumbing only and can't answer H5 (whether the model scales).

## B3. Gates, Definition of Done and sprint plan

- **Gates:**
  - G1: add written licence answers from the vendors.
  - G3: add the synthetic-null run and a passing leakage suite.
  - G4: add seed distributions, and the check that baselines beat persistence where they should.
  - G6 says "train end-to-end", which contradicts FWM-007.5 ("do not make end-to-end joint training mandatory"). Reword it to "staged or joint".
- **Definition of Done:** make "Alpha Vantage ingestion works" conditional on its licence. Add "T0 complete", "placebo tests run" and "trial log complete".
- **Sprint 1:** add the raw zone, the request ledger and the licence register. Move SurrealDB initialisation (FWM-003.3) to sprint 2 or 3.

## B4. Keep as they are

- The linear critical path, with interfaces allowing parallel work
- Gates that need passing acceptance tests and documented results, not just modules that exist
- The explicit adjustment-basis distinction, never mixed in one dataset (FWM-002.3)
- Configuration-driven rate limits (FWM-002.4)
- An ingestion report for every run (FWM-002.6)
- A metadata registry instead of parsing symbol names (FWM-003.2)
- Temporal edge properties and the "valid and known as of" query (FWM-003.4)
- The HAR dataset kept separate from daily OHLCV (FWM-004.2)
- No training without a valid manifest and quality report (FWM-004.6)
- Frozen pretrained language encoder first (FWM-006.3)
- End-to-end training not mandatory (FWM-007.5)

## Sources

Vault: Synthesis; RP1 ML Methods; RP2 Data Sources and Storage; RP3 Cleaning and Labelling; RP4 Training and Evaluation; RP5 Vault Review; Decisions Log; Financial Foundation Model Research Direction.

Web (2026-11-10): [ArcticDB on PyPI](https://pypi.org/project/arcticdb/) · [SurrealDB Python SDK](https://surrealdb.com/docs/reference/python) · [PyG 2.8 release notes](https://newreleases.io/project/github/pyg-team/pytorch_geometric/release/2.8.0) · [vLLM issue on PyTorch 3.14 wheels](https://github.com/vllm-project/vllm/issues/34096)
