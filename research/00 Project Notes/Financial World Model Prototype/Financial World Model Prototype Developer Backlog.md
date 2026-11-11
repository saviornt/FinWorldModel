# Financial World Model

## FW-0.1 — Developer Implementation Backlog & Coding Specification

**Document type:** Engineering execution plan  
**Project phase:** Research prototype  
**Priority:** Establish reproducible infrastructure and comparative benchmarks before developing the complete neural architecture.

---

# 1. Development Strategy

The project will be implemented as a modular Python monorepo.

The backlog is organized into eight epics:

| Epic    | Name                                  | Priority |
| ------- | ------------------------------------- | -------- |
| FWM-001 | Project foundation                    | Critical |
| FWM-002 | Data contracts and provider ingestion | Critical |
| FWM-003 | ArcticDB and SurrealDB infrastructure | Critical |
| FWM-004 | Dataset construction and validation   | Critical |
| FWM-005 | Conventional benchmark models         | Critical |
| FWM-006 | Specialized neural encoders           | High     |
| FWM-007 | Multimodal fusion and world model     | High     |
| FWM-008 | Evaluation and scalability            | High     |

The critical path is:

```
FWM-001
   |
   v
FWM-002
   |
   v
FWM-003
   |
   v
FWM-004
   |
   v
FWM-005
   |
   v
FWM-006
   |
   v
FWM-007
   |
   v
FWM-008
```

Some tasks can be developed in parallel once their interfaces are defined.

For example, the graph schema, time-series feature pipeline, and baseline implementations can be developed independently against shared data contracts.

# 2. Repository and Development Foundation

## FWM-001 — Project Foundation

**Objective:** Establish a reproducible development environment, repository structure, dependency management, and application configuration.

### FWM-001.1 — Initialize repository

Priority: Critical

Create the initial repository structure.

```
financial-world-model/
├── configs/
├── infrastructure/
├── src/
│   ├── baseline/
│   └── fwm/
├── scripts/
├── tests/
├── research/
├── artifacts/
├── logs/
├── pyproject.toml
├── README.md
└── .gitignore
```

Implementation requirements:

-  [x] Python >=3.14,<3.15.
-  [x] `src` package layout.
-  [x] Strict type checking.
-  [x] Pyright
-  [x] uv
-  [x] Ruff linting and formatting.
-  [x] pytest.
-  [x] Pydantic v2.
-  [ ] Centralized configuration.
-  [ ] Structured logging.

Acceptance tests:

- Package installs in editable mode.
- Application imports successfully.
- Test suite executes.
- Linting and type-checking execute.
- No credentials or generated artifacts are committed.

### FWM-001.2 — Dependency verification

Priority: Critical

Verify actual Python 3.14 compatibility for:

-  [x] PyTorch (CPU + CUDA).
-  [x] ArcticDB.
-  [x] SurrealDB Python SDK.
-  [x] NumPy.
-  [ ] CuPy (optional - maybe)
-  [x] Pandas or Polars.
-  [x] scipy.
-  [x] scikit-learn.
-  [x] PyTorch Geometric.
-  [x] MLflow.

Do not assume the latest versions of all these libraries support the same Python interpreter.

Produce a dependency compatibility report before locking versions.

Acceptance tests:

- [x] Clean environment installation.
- [x] Import tests for all direct dependencies.
- [x] Minimal CPU tensor operation.
- [x] Minimal GPU tensor operation where supported.
- [x] ArcticDB connectivity tests
- [x] SurrealDB connectivity tests.

### FWM-001.3 — Configuration framework

Priority: Critical

Create:

```
src/fwm/config/
├── settings.py
├── acquisition.py
├── storage.py
├── model.py
├── training.py
└── experiments.py
```

Use Pydantic Settings for application configuration.

Configuration must support:

- Provider credentials through environment variables.
- Database connection settings.
- Storage paths.
- Model dimensions.
- Enabled modalities.
- Training parameters.
- Dataset date ranges.
- Experiment identifiers.

Credentials must never be included in serialized experiment configurations.

Acceptance tests:

- Invalid configurations fail validation.
- Missing optional provider credentials do not prevent unrelated components from running.
- Experiment configurations can be serialized and hashed.

### FWM-001.4 — Experiment identification

Priority: High

Every experiment receives a stable identifier.

Record:

```
experiment_id
created_at
git_commit
configuration_hash
dataset_id
random_seed
software_versions
hardware_information
```

Acceptance tests:

- Experiment IDs are unique.
- Configuration changes produce different hashes.
- Dataset identifiers remain linked to completed experiments.

---

# 3. Data Acquisition and Contracts

## FWM-002 — Data Contracts and Provider Ingestion

**Objective:** Establish a provider-independent data acquisition layer.

### FWM-002.1 — Define domain schemas

Priority: Critical

Create:

```
src/fwm/schemas/
├── market.py
├── macro.py
├── corporate.py
├── events.py
├── documents.py
├── entities.py
└── provenance.py
```

Initial schemas:

**MarketBar**

```
symbol
timestamp
open
high
low
close
volume
provider
adjustment_basis
```

**MacroObservation**

```
series_id
observation_period
published_at
available_at
retrieved_at
value
unit
provider
revision_id
```

**FinancialEvent**

```
event_id
event_type
entity_id
published_at
available_at
retrieved_at
source
confidence
```

**NewsDocument**

```
document_id
source
url
published_at
retrieved_at
language
content_hash
entity_ids
event_type
content_reference
```

All timestamps must be timezone-aware.

Use UTC for canonical storage while retaining original source timezone information when relevant.

Acceptance tests:

- Valid records pass.
- Invalid OHLC relationships fail.
- Negative volume fails.
- Missing publication timestamps are handled explicitly.
- Duplicate identities are detected.

### FWM-002.2 — Provider interface

Priority: Critical

Create:

```
src/fwm/acquisition/
├── base.py
├── registry.py
├── models.py
└── providers/
    ├── alpaca.py
    ├── alpha_vantage.py
    └── yfinance.py
```

Define interfaces for:

- Historical market bars.
- Corporate financial observations.
- Economic indicators.
- News and sentiment.

Not every provider must implement every capability.

The registry must expose supported capabilities so the ingestion orchestrator can select the appropriate provider.

Acceptance tests:

- Provider adapters satisfy their declared interfaces.
- Unsupported operations raise explicit errors.
- Provider responses are converted into common schemas.
- Provider-specific fields are retained where needed for provenance.

### FWM-002.3 — Alpaca adapter

Priority: Critical

Request SIP feed explicitly and store `feed` on every bar.

Initial responsibilities:

- Historical daily bars.
- Historical intraday bars.
- Multi-symbol retrieval.
- Pagination.
- Rate-limit handling.
- Date-range partitioning.
- Adjustment settings.
- Provider metadata.

Implement an explicit distinction between:

- Raw OHLCV.
- Split-adjusted OHLCV.
- Dividend-adjusted data.

Do not mix adjustment methodologies in the same dataset.

Acceptance tests:

- Pagination retrieves all requested pages.
- Duplicate records are detected.
- Interrupted ingestion can resume.
- Date boundaries are respected.
- Adjustment metadata is preserved.
- Where two sources overlap, they are reconciled before joining.

### FWM-002.4 — Alpha Vantage adapter

Priority: High

Initial responsibilities:

- Economic indicators.
- Selected company fundamentals.
- News and sentiment.
- Supplemental market data.

Implement endpoint-specific response validation.

Rate limits must be configuration-driven rather than hardcoded.

Acceptance tests:

- Invalid API responses fail validation.
- Rate-limit responses trigger backoff.
- Missing observations are represented explicitly.
- Publication timestamps are retained.

### FWM-002.5 — yfinance adapter

Priority: Low

Provide an optional exploratory adapter.

Requirements:

- Clearly identify source data.
- Retain acquisition timestamps.
- Do not treat it as a guaranteed commercial data source.
- Do not use it as the authoritative source when data licensing or reproducibility is uncertain.

### FWM-002.6 — Ingestion orchestrator

Priority: Critical

Create:

```
src/fwm/ingestion/
├── orchestrator.py
├── scheduler.py
├── retry.py
├── validation.py
├── checkpoints.py
└── reports.py
```

Responsibilities:

1. Resolve requested instruments and date ranges.
2. Select providers.
3. Request data.
4. Handle pagination.
5. Validate responses.
6. Detect duplicates and missing intervals.
7. Persist accepted records.
8. Record ingestion provenance.
9. Generate ingestion reports.

Acceptance tests:

- Interrupted operations resume without duplication.
- Failed provider requests are recorded.
- Partial ingestion is distinguishable from complete ingestion.
- Every ingestion run has a report.

---

# 4. Storage Infrastructure

## FWM-003 — ArcticDB and SurrealDB

**Objective:** Establish independent temporal and relational storage systems.

### FWM-003.1 — ArcticDB initialization

Priority: Critical

Create:

```
src/fwm/storage/arctic/
├── client.py
├── libraries.py
├── market_repository.py
├── macro_repository.py
└── versioning.py
```

Initial libraries:

```
fwm_market
fwm_features
fwm_macro
fwm_derived
```

Responsibilities:

- Initialize local ArcticDB storage.
- Create and validate libraries.
- Read and write historical observations.
- Append incremental observations.
- Update controlled corrections.
- Retrieve historical versions.
- Expose storage metadata.

Important implementation detail:

ArcticDB operations are synchronous. The application should expose an asynchronous repository boundary where necessary, but blocking database calls must execute through an appropriate worker strategy rather than directly on the event loop.

Acceptance tests:

- Initial dataset write.
- Incremental append.
- Date-range retrieval.
- Version retrieval.
- Controlled update.
- Restart persistence.

### FWM-003.2 — ArcticDB symbol conventions

Priority: High

Use predictable naming:

```
bars_SPY_1d
bars_SPY_5m
bars_QQQ_1d

returns_SPY_1d
realized_vol_SPY_5m
realized_vol_SPY_1d

macro_cpi
macro_fed_funds
macro_unemployment
```

Maintain a metadata registry describing:

- Symbol.
- Instrument.
- Frequency.
- Provider.
- Adjustment methodology.
- Feature schema version.

Do not rely exclusively on parsing symbol names to determine their meaning.

### FWM-003.3 — SurrealDB initialization

Priority: Critical

Create:

```
src/fwm/storage/surreal/
├── client.py
├── schema.py
├── repositories/
│   ├── entities.py
│   ├── relationships.py
│   ├── documents.py
│   ├── events.py
│   └── embeddings.py
└── migrations/
```

Initial record types:

```
company
security
sector
industry
executive
board_member
news_article
corporate_event
economic_event
```

Create graph relationships:

```
company -> operates_in -> industry
company -> belongs_to -> sector
company -> employs -> executive
company -> supplies -> company
company -> depends_on -> company
security -> represents -> company
news_article -> concerns -> company
```

Relationships must support historical validity and source provenance.

Acceptance tests:

- Schema initialization.
- Record creation and retrieval.
- Relationship traversal.
- Temporal edge filtering.
- Duplicate entity detection.
- Transaction or batch-write behavior appropriate to the selected SDK.

### FWM-003.4 — Temporal graph support

Priority: Critical

Implement historical relationship properties:

```
valid_from
valid_to
observed_at
published_at
source
confidence
```

The graph builder must support queries such as:

"Return the corporate relationships that were valid and known as of a particular historical date."

This is essential to prevent graph leakage.

Acceptance tests:

- Historical graph reconstruction.
    
- Relationship expiration.
    
- New relationship activation.
    
- Exclusion of future-known edges.
    

### FWM-003.5 — Storage reconciliation

Priority: High

Create a reconciliation process between ArcticDB and SurrealDB.

It must detect:

- Missing temporal observations.
    
- Orphaned entity references.
    
- Invalid instrument identifiers.
    
- Missing document references.
    
- Inconsistent observation timestamps.
    

Do not allow either database to silently overwrite the authoritative copy held by the other.

### FWM-003.6 — Snapshot manifest

Priority: Critical

Create:

```
src/fwm/storage/snapshots.py
```

Each dataset snapshot must record:

- ArcticDB library versions.
    
- SurrealDB snapshot or export identifier.
    
- Source provider versions.
    
- Date boundaries.
    
- Feature schema versions.
    
- Instrument universe.
    
- Dataset generation time.
    

A dataset snapshot must be immutable from the experiment's perspective.

---

# 5. Dataset Construction

## FWM-004 — Dataset Assembly and Validation

**Objective:** Convert independently stored observations into reproducible model inputs.

### FWM-004.1 — Feature engineering

Priority: Critical

Create:

```
src/fwm/features/
├── returns.py
├── volatility.py
├── volume.py
├── technical.py
├── macro.py
└── cross_asset.py
```

Initial numerical features:

- Log returns.
    
- Rolling volatility.
    
- High-low range.
    
- Volume anomalies.
    
- Moving-average distance.
    
- Drawdown.
    
- Cross-instrument returns.
    

All transformations must have explicit configuration and versioning.

Acceptance tests:

- Numerical calculations match reference implementations.
    
- Rolling windows do not include future observations.
    
- Missing values are handled consistently.
    
- Feature calculations are reproducible.
    

### FWM-004.2 — HAR realized-volatility dataset

Priority: Critical

Create a dedicated intraday dataset builder.

Use intraday observations to calculate realized variance:

[  
RV_t = \sum_{i=1}^{M}r_{t,i}^{2}  
]

Where (r_{t,i}) represents intraday returns.

Aggregate realized variance over daily, weekly, and monthly horizons.

The benchmark must use consistent sampling, market sessions, and treatment of overnight returns.

Keep this dataset separate from the ordinary daily OHLCV dataset.

Acceptance tests:

- Known synthetic returns produce expected realized variance.
- Missing intraday intervals are detected.
- Market-session boundaries are respected.
- HAR-RV features do not include the prediction target period.

### FWM-004.3 — Temporal alignment

Priority: Critical

Create:

```
src/fwm/datasets/
├── alignment.py
├── availability.py
├── calendars.py
└── point_in_time.py
```

Responsibilities:

- Market-calendar alignment.
- Publication-time filtering.
- Availability-time filtering.
- Historical entity-state reconstruction.
- Cross-modal synchronization.
- BLS release archiver (sets `available_at` from release calendar).
- RTDSM vintage adapter (sets `available_at` from release calendar).

The system must distinguish an observation's economic reference date from the date it became available.

Acceptance tests:

- Future information cannot enter historical samples.
- Late-published news is excluded from earlier cutoffs.
- Macro revisions are reconstructed correctly.
- Historical corporate relationships are respected.

### FWM-004.4 — Dataset builder

Priority: Critical

Create:

```
src/fwm/datasets/builder.py
```

Interface:

```
class DatasetBuilder:

    async def build(
        self,
        symbols: list[str],
        start: datetime,
        end: datetime,
        modalities: set[str],
    ) -> DatasetManifest:
        ...
```

Responsibilities:

1. Retrieve temporal observations.
    
2. Retrieve relevant entities and relationships.
    
3. Retrieve applicable documents and events.
    
4. Apply temporal restrictions.
    
5. Construct feature sequences.
    
6. Generate targets.
    
7. Validate output.
    
8. Create dataset manifest.
    

The builder must support individual modalities being disabled.

### FWM-004.5 — Data splitting

Priority: Critical

Implement chronological splitting.

Initial periods:

```
Training:   2016–2022
Validation: 2023
Testing:    2024–2025
```

Use a configurable embargo or purge interval where overlapping target horizons could cause leakage.

Do not randomly split time-series observations.

### FWM-004.6 — Dataset quality report

Priority: High

Generate:

- Coverage statistics.
    
- Missing observation percentages.
    
- Instrument distribution.
    
- Feature distributions.
    
- Temporal consistency checks.
    
- Source distribution.
    
- Duplicate counts.
    
- Dataset hashes.
    

Acceptance criterion: No training run may begin without a valid dataset manifest and a successful quality report.

---

# 6. Conventional Benchmark Framework

## FWM-005 — Baseline Models

**Objective:** Establish the performance that the heterogeneous architecture must improve upon.

### FWM-005.1 — Baseline interface

Priority: Critical

Create:

```
src/fwm/baselines/
├── base.py
├── persistence.py
├── har.py
├── random_forest.py
└── extra_trees.py
```

Define a common interface for:

- Training.
    
- Prediction.
    
- Serialization.
    
- Configuration.
    
- Evaluation.
    

All models must receive identical training, validation, and test boundaries.

### FWM-005.2 — Persistence baseline

Priority: Critical

Implement:

- Zero-return prediction.
    
- Last-observation volatility prediction.
    
- Last-known-regime prediction.
    

Acceptance tests:

- Predictions reproduce expected persistence behavior.
    
- Evaluation uses correct forecast horizons.
    

### FWM-005.3 — HAR-RV

Priority: Critical

Implement standard HAR-RV.

Use:

- Daily realized volatility.
    
- Weekly realized volatility.
    
- Monthly realized volatility.
    

Compare one-day and additional configured forecast horizons.

Report MAE, RMSE, and QLIKE.

### FWM-005.4 — Random Forest

Priority: Critical

Implement:

- Configurable estimator count.
    
- Maximum depth.
    
- Minimum leaf size.
    
- Feature selection.
    
- Reproducible random seed.
    

### FWM-005.5 — Extra Trees

Priority: Critical

Implement equivalent configuration and evaluation interfaces.

The purpose is to compare the neural architecture against randomized tree-based nonlinear models, not simply a linear statistical baseline.

### FWM-005.6 — Gradient-boosted baseline

Priority: High

Implement HistGradientBoostingRegressor as an additional baseline.

This gives us another useful comparison against the neural architecture.

### FWM-005.7 — Benchmark reporting

Priority: Critical

Create a unified results schema:

```
experiment_id
model_name
instrument
forecast_target
forecast_horizon
metric_name
metric_value
training_duration
inference_duration
dataset_id
```

Acceptance tests:

- All baselines execute against the same dataset snapshot.
    
- Results are comparable.
    
- Model configurations are preserved.
    
- Results can be exported to CSV and Parquet.
    

---

# 7. Specialized Neural Networks

## FWM-006 — Individual Encoders

**Objective:** Build and evaluate each specialized representation network independently.

### FWM-006.1 — Time-series encoder

Priority: High

Create:

```
src/fwm/encoders/timeseries/
├── model.py
├── embeddings.py
├── masks.py
└── objectives.py
```

Initial implementation:

- Two Transformer layers.
    
- 128-dimensional hidden representation.
    
- Four attention heads.
    
- Configurable context length.
    
- Causal temporal masking.
    

Initial training objectives:

- Masked observation reconstruction.
    
- Next-state prediction.
    
- Volatility prediction.
    

Acceptance tests:

- Correct tensor dimensions.
    
- No future attention.
    
- Stable training.
    
- Embeddings can be serialized and retrieved.
    

### FWM-006.2 — Graph neural network

Priority: High

Create:

```
src/fwm/encoders/graph/
├── model.py
├── graph_builder.py
├── features.py
└── objectives.py
```

Initial implementation:

- GraphSAGE or GAT.
    
- Two message-passing layers.
    
- 128-dimensional embeddings.
    
- Temporal edge filtering.
    

Start with approximately 20–50 companies and a small number of verified relationships.

Initial objectives:

- Link prediction.
    
- Entity representation learning.
    
- Relationship classification.
    

Acceptance tests:

- Historical graph reconstruction.
    
- Edge validity filtering.
    
- Node embedding generation.
    
- Missing relationship handling.
    
- No future graph leakage.
    

### FWM-006.3 — Language encoder

Priority: High

Create:

```
src/fwm/encoders/language/
├── model.py
├── preprocessing.py
├── event_extraction.py
├── embeddings.py
└── objectives.py
```

Initial implementation:

- Locally executable pretrained transformer encoder.
    
- Frozen parameters initially.
    
- Optional adapter-based fine-tuning.
    
- Event classification.
    
- Semantic representation extraction.
    

Keep the encoder independent from the central world model.

Store encoder version, source document ID, publication timestamp, and embedding provenance.

Acceptance tests:

- Repeatable embedding generation.
    
- Correct document-to-entity association.
    
- Temporal availability enforcement.
    
- Missing-document handling.
    

A separately trained-from-scratch language encoder is a later experiment, not a prerequisite for FW-0.1.

### FWM-006.4 — Macroeconomic encoder

Priority: High

Create:

```
src/fwm/encoders/macro/
├── model.py
├── preprocessing.py
└── objectives.py
```

Initial implementation:

- Temporal Transformer or TCN.
    
- 128-dimensional output.
    
- Publication-aware temporal inputs.
    

Acceptance tests:

- Correct historical macroeconomic reconstruction.
    
- No future revisions.
    
- Missing observations are represented correctly.
    

### FWM-006.5 — Tokenization

Initial implementation:

Acceptance tests:
- Vocabulary version is recorded in the snapshot manifest.
- Bin edges are fitted on training data only.
- Tail buckets beyond the bin range are handled.
### FWM-006.6 — Encoder benchmark suite

Priority: High

Train and evaluate each encoder independently.

Record:

- Training loss.
    
- Validation loss.
    
- Embedding dimensions.
    
- Training time.
    
- Inference time.
    
- Memory utilization.
    
- Model checkpoint.
    

---

# 8. Multimodal Fusion and World Model

## FWM-007 — Central Autoregressive Architecture

**Objective:** Combine independently learned representations and model evolving financial states.

### FWM-007.1 — Embedding projection

Priority: High

Create:

```
src/fwm/fusion/
├── projection.py
├── alignment.py
├── modality_masks.py
└── cross_attention.py
```

Project all modality embeddings into a common latent dimension.

Initial target: 128 dimensions.

Retain:

- Modality identity.
    
- Temporal position.
    
- Observation availability.
    
- Missing-modality indicators.
    

### FWM-007.2 — Cross-modal fusion

Priority: High

Implement cross-attention.

Test:

- Time-series attending to language.
    
- Graph context attending to financial observations.
    
- Language attending to relevant entities.
    
- Macro context influencing other representations.
    

Start with a relatively simple fusion architecture before experimenting with multiple cross-attention blocks.

Acceptance tests:

- Variable modality availability.
    
- Stable tensor dimensions.
    
- Correct attention masks.
    
- No future information leakage.
    

### FWM-007.3 — Autoregressive world model

Priority: High

Create:

```
src/fwm/world_model/
├── transformer.py
├── state.py
├── positional.py
├── rollout.py
└── objectives.py
```

Initial configuration:

- Two to four causal Transformer layers.
    
- 128-dimensional hidden representation.
    
- Four attention heads.
    
- 128 trading-session context window.
    

Responsibilities:

- Learn financial state transitions.
    
- Predict subsequent latent states.
    
- Support multiple forecast horizons.
    
- Support probabilistic downstream outputs.
    

Acceptance tests:

- Causal attention verified.
    
- (Optional) One-step prediction works.
    
- Multi-step rollout works.
    
- Checkpoint restoration works.
    

### FWM-007.4 — Prediction heads

Priority: High

Create:

```
src/fwm/prediction/
├── volatility.py
├── returns.py
├── regime.py
└── latent_state.py
```

Initial heads:

1. Volatility distribution.
    
2. Forward return distribution.
    
3. Market-regime probabilities.
    
4. Latent-state prediction.
    

Use separate configurable losses.

### FWM-007.5 — Joint training

Priority: High

Create:

```
src/fwm/training/
├── trainer.py
├── optimizer.py
├── scheduler.py
├── checkpoints.py
└── callbacks.py
```

Implement:

- Independent encoder training.
    
- Fusion training.
    
- Autoregressive training.
    
- Joint fine-tuning.
    
- Modality ablation.
    
- Reproducible checkpoints.
    

Do not make end-to-end joint training mandatory for the first successful prototype.

### FWM-007.6 — Modality ablation

Priority: High

Execute:

| Experiment | Enabled modalities                                                            |
| ---------- | ----------------------------------------------------------------------------- |
| T0         | Time-series (price only, continous versus tokenized input vs regression head) |
| E0         | Time-series                                                                   |
| E1         | Time-series + GNN                                                             |
| E2         | Time-series + Language                                                        |
| E3         | Time-series + Macro                                                           |
| E4         | Time-series + GNN + Language + Macro                                          |

Compare all configurations against the same numerical baselines.

---

# 9. Evaluation and Scaling

## FWM-008 — Research Evaluation and Performance

**Objective:** Determine whether the system is scientifically useful and technically scalable.

### FWM-008.1 — Evaluation engine

Priority: Critical

Create:

```
src/fwm/evaluation/
├── metrics.py
├── walk_forward.py
├── calibration.py
├── statistical_tests.py
└── reports.py
```

Support:

- MAE.
    
- RMSE.
    
- QLIKE.
    
- Directional accuracy.
    
- Brier score.
    
- F1.
    
- Cross-entropy.
    
- Calibration error.
    

### FWM-008.2 — Walk-forward evaluation

Priority: Critical

Implement rolling or expanding training windows.

The final test period must remain untouched during model selection.

Record all forecast timestamps and actual target timestamps.

### FWM-008.3 — Statistical comparisons

Priority: High

Implement:

- Paired forecast-error comparisons.
    
- Block-bootstrap confidence intervals.
    
- Diebold-Mariano comparisons where appropriate.
    
- Multiple-comparison correction.
    

Acceptance tests:

- Tests operate on aligned forecasts.
    
- Invalid sample comparisons are rejected.
    
- Statistical assumptions are documented.
    

### FWM-008.4 — Storage benchmarks

Priority: High

Measure:

- ArcticDB write throughput.
    
- ArcticDB read latency.
    
- SurrealDB graph traversal latency.
    
- Document retrieval.
    
- Snapshot generation.
    
- Dataset assembly throughput.
    

### FWM-008.5 — Model benchmarks

Priority: High

Measure:

- Training time.
    
- Epoch duration.
    
- GPU memory.
    
- System memory.
    
- Inference latency.
    
- Batch throughput.
    
- Autoregressive rollout performance.
    

### FWM-008.6 — Scale simulation

Priority: High

Run progressively larger synthetic workloads:

|Scenario|Instruments|Frequency|
|---|---|---|
|S0|10|Daily|
|S1|50|Daily|
|S2|250|Daily|
|S3|1,000|Daily|
|S4|10–50|Intraday|

Measure where each component becomes a bottleneck.

Do not assume model parameter scaling and data-volume scaling are equivalent.

### FWM-008.7 — Final research report

Priority: Critical

Generate a report containing:

- Research hypotheses.
    
- Dataset descriptions.
    
- Model configurations.
    
- Baseline results.
    
- Ablation results.
    
- Statistical comparisons.
    
- Resource utilization.
    
- Limitations.
    
- Reproducibility instructions.
    
- FW-0.2 recommendations.
    

---

# 10. Development Order and Dependency Gates

The following gates determine when development can advance.

|Gate|Required completion|
|---|---|
|G0|Project installs and tests|
|G1|Provider adapters ingest valid data|
|G2|Both databases persist and retrieve data|
|G3|Dataset builder creates valid snapshots|
|G4|Baselines produce reproducible results|
|G5|Specialized encoders train independently|
|G6|Fusion and world model train end-to-end|
|G7|Comparative evaluation is complete|
|G8|Scale feasibility report is complete|

A gate cannot be considered complete merely because the relevant Python modules exist.

It requires passing acceptance tests and documented results.

# 11. Initial Experiment Configuration

Suggested initial configuration:

```
project:
  name: financial-world-model
  version: "0.1.0"

runtime:
  python: ">=3.14,<3.15"
  device: auto
  seed: 42

data:
  symbols:
    - SPY
    - QQQ
    - IWM
    - DIA
    - TLT
    - GLD
    - USO
    - XLF
    - XLK
    - XLE

  start_date: "2016-01-01"
  end_date: "2025-12-31"

  frequencies:
    - 1d
    - 5m

storage:
  temporal:
    backend: arcticdb

  relational:
    backend: surrealdb

models:
  timeseries:
    enabled: true
    hidden_dim: 128
    layers: 2
    heads: 4

  graph:
    enabled: true
    architecture: graphsage
    hidden_dim: 128
    layers: 2

  language:
    enabled: true
    training_mode: frozen

  macro:
    enabled: true
    hidden_dim: 128

  fusion:
    enabled: true
    architecture: cross_attention
    hidden_dim: 128

  world_model:
    enabled: true
    architecture: causal_transformer
    hidden_dim: 128
    layers: 2
    heads: 4
    context_length: 128

experiments:
  walk_forward: true
  modality_ablation: true
  baselines:
    - persistence
    - har_rv
    - random_forest
    - extra_trees
    - hist_gradient_boosting
```

This is a starting configuration, not a claim that every component should be enabled in every experiment.

The configuration system must support independent experiment overrides.

# 12. Definition of Done

FW-0.1 is complete when all of the following are true:

- Project environment is reproducible.
    
- Alpaca ingestion works.
    
- Alpha Vantage ingestion works.
    
- ArcticDB stores versioned historical observations.
    
- SurrealDB stores entities and temporal relationships.
    
- Data provenance is preserved.
    
- Dataset snapshots can be reproduced.
    
- Temporal leakage tests pass.
    
- HAR-RV is implemented correctly.
    
- Random Forest and Extra Trees benchmarks work.
    
- Each specialized encoder trains independently.
    
- Multimodal fusion operates with missing modalities.
    
- Autoregressive prediction works.
    
- Walk-forward evaluation works.
    
- Modality ablations are complete.
    
- Performance benchmarks are documented.
    
- Scaling limitations are identified.
    
- Research findings are reproducible.
    

---

# 13. Recommended Implementation Priorities

Do not attempt to implement every epic simultaneously.

The first development sprint should contain only:

1. FWM-001.1 — Repository initialization.
    
2. FWM-001.2 — Dependency compatibility.
    
3. FWM-001.3 — Configuration framework.
    
4. FWM-002.1 — Data contracts.
    
5. FWM-002.2 — Provider interfaces.
    
6. FWM-003.1 — ArcticDB initialization.
    
7. FWM-003.3 — SurrealDB initialization.
    

The second sprint should focus on actual ingestion and storage.

The third should produce the first reproducible dataset and baseline results.

Only after the baseline framework works should neural-network development become the primary focus.

**The engineering objective is to make each component independently replaceable. The research objective is to determine whether combining them produces something better than the sum of their individual contributions.**