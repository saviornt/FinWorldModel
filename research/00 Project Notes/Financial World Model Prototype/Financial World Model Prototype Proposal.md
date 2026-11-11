# Financial World Model

## FW-0.1 — Research Prototype Development Proposal & Coding Guide

**Project type:** Experimental research and engineering framework  
**Primary objective:** Test the feasibility of a heterogeneous, multimodal, autoregressive financial world model.  
**Secondary objective:** Establish a reproducible infrastructure capable of scaling into a larger financial intelligence system.

---

# 1. Executive Summary

FW-0.1 is a research prototype designed to test whether combining specialized neural networks for financial time-series, corporate relationships, natural-language information, and macroeconomic conditions produces better representations and forecasts of financial market behavior than conventional approaches.

The proposed architecture consists of:

1. A time-series neural network.
2. A graph neural network (GNN).
3. A language transformer for textual information.
4. A macroeconomic encoder.
5. A multimodal fusion layer.
6. A central autoregressive world model.
7. Multiple downstream prediction heads.

The experimental framework will compare the proposed architecture against:

- HAR-RV (Heterogeneous Autoregressive Realized Volatility).
- Extra Trees / Random Forest.
- A simple persistence baseline.
- A conventional gradient-boosted tree baseline.

The project will use:

| Technology             | Responsibility                                        |
| ---------------------- | ----------------------------------------------------- |
| Python                 | Primary development language                          |
| PyTorch                | Neural network implementation                         |
| ArcticDB               | Historical numerical and temporal storage             |
| SurrealDB              | Graph, document, entity, vector, and model-ready data |
| Alpaca / Alpha Vantage | Market and financial data acquisition                 |
| yfinance               | Optional exploratory data acquisition                 |
| Pandas / Polars        | Data processing                                       |
| NumPy                  | Numerical transformations                             |
| Pydantic v2            | Data contracts and validation                         |
| scikit-learn           | Conventional machine-learning baselines               |
| DuckDB                 | Optional local analytical queries                     |
| pytest                 | Testing and validation                                |
| MLflow                 | Experiment tracking                                   |

The initial prototype should prioritize daily observations, a small instrument universe, and a manageable number of historical information sources.

The goal is not to build a trading application. It is to establish whether the underlying hypothesis is scientifically and computationally viable.

# 2. Research Hypothesis

## 2.1 Primary hypothesis

A heterogeneous neural architecture combining temporal, graph-based, linguistic, and macroeconomic representations can learn financial state transitions more effectively than models trained exclusively on numerical historical observations.

The central hypothesis is that financial markets are better represented as evolving systems of interconnected information than as isolated numerical time-series.

## 2.2 Secondary hypotheses

**H1 — Multimodal representation**

Combining financial time-series, corporate relationships, news, and macroeconomic information improves out-of-sample forecasting relative to individual modalities.

**H2 — Relational learning**

Graph-based representations of corporate relationships provide useful information beyond conventional financial features.

**H3 — Semantic information**

Natural-language representations of financial events contribute information that cannot be adequately captured by simple numerical sentiment scores.

**H4 — Autoregressive state learning**

A central autoregressive model can learn useful representations of evolving financial states.

**H5 — Scalability**

The proposed data and model architecture can accommodate a substantially larger instrument universe and additional information sources without requiring fundamental architectural changes.

## 2.3 What constitutes success?

The project should not require the world model to outperform every conventional model on every metric.

Instead, we want to establish whether it provides statistically meaningful improvements in one or more of the following:

- Forecasting accuracy.
    
- Volatility forecasting.
    
- Market-regime recognition.
    
- Event-impact estimation.
    
- Cross-instrument generalization.
    
- Probabilistic calibration.
    
- Robustness during unusual market conditions.
    

We should also measure computational cost. A marginal accuracy improvement that requires dramatically more resources may not justify the architecture.

---

# 3. Proposed System Architecture

## 3.1 Overall architecture

```
                DATA ACQUISITION
                       |
          +------------+------------+
          |            |            |
       Alpaca     Alpha Vantage   yfinance
          |            |            |
          +------------+------------+
                       |
         RAW DATA LAYER (APPEND-ONLY)          
                       |
                INGESTION LAYER
                       |
	            DATAFRAME ADAPTER (Pandas | Polars)
			           |
              NORMALIZATION LAYER
                       |
           +-----------+-----------+
           |                       |
       ArcticDB                 SurrealDB
           |                       |
     Temporal Data          Documents / Graphs
     OHLCV / Features       Entities / Relationships
     Macro Observations     News / Events / Embeddings
           |                       |
           +-----------+-----------+
                       |
               FEATURE ASSEMBLY
                       |
          +------------+------------+
          |            |            |
      Time-series     GNN        Language
       Encoder      Encoder      Encoder
          |            |            |
          +------------+------------+
                       |
	                Tokenizer
		               |
                 Macro Encoder
                       |
              MULTIMODAL FUSION
                       |
             CROSS-MODAL ATTENTION
                       |
              AUTOREGRESSIVE FWM
                       |
             +---------+---------+
             |         |         |
          Volatility  Regime   Event/State
          Prediction  Model   Prediction
             |         |         |
             +---------+---------+
                       |
                EVALUATION ENGINE
                       |
          HAR-RV / EXTRA TREES / OTHER
                 BASELINES
```

The diagram represents logical components, not necessarily separate services or processes.

For the prototype, these components should run in one Python application with clearly separated interfaces.

The raw data layer should:
- Store every provider response as received, with request metadata, in an append-only raw zone.
- Keep a request ledger keyed by endpoint and normalised parameters, so interrupted ingestion can resume without duplicates.
- Rebuild both databases from the raw zone. Neither is then authoritative.

## 3.2 Architectural responsibilities

### A. Time-series encoder

Input:

- OHLCV observations.
    
- Returns.
    
- Realized volatility.
    
- Volume anomalies.
    
- Technical features.
    
- Company financial observations where available.
    

Suggested architecture:

- Temporal Transformer initially.
    
- TCN as an alternative experimental encoder.
    

Output:

- A sequence of learned financial representations.
    

### B. Graph encoder

Input:

- Companies.
    
- Securities.
    
- Sectors.
    
- Industries.
    
- Executives.
    
- Board members.
    
- Ownership relationships.
    
- Suppliers and customers.
    

Suggested architecture:

- Two-layer GraphSAGE or GAT.
    
- Configurable hidden dimensions.
    
- Temporal edge attributes.
    

Output:

- Entity embeddings.
    
- Relationship-aware contextual embeddings.
    

The graph must support relationships that change over time. A company should not be represented using a relationship that did not exist at the historical observation date.

### C. Language encoder

Input:

- News articles.
    
- Earnings announcements.
    
- Regulatory filings.
    
- Earnings-call transcripts.
    
- Corporate announcements.
    

Suggested architecture:

- Small transformer encoder.
    
- Trainable from scratch for the experimental pipeline.
    
- Masked language modeling or another self-supervised objective as appropriate.
    

Output:

- Semantic event representations.
    
- Contextual sentiment.
    
- Event classification representations.
    

Sentiment should be treated as a separate prediction or auxiliary objective, not as a substitute for semantic understanding.

### D. Macroeconomic encoder

Input:

- Interest rates.
    
- Inflation.
    
- Employment.
    
- GDP.
    
- Monetary policy observations.
    
- Other economic indicators.
    

Suggested architecture:

- Small temporal Transformer or TCN.
    

Output:

- Economic state representations.
    

Macroeconomic observations must be aligned to their actual publication timestamps, not simply their reference periods.

### E. Multimodal fusion

This component receives the outputs of the specialized encoders.

Suggested implementation:

- Projection layers to a shared embedding dimension.
    
- Temporal alignment.
    
- Cross-attention.
    
- Modality-specific masking.
    
- Missing-modality indicators.
    

The fusion layer must accommodate missing or delayed information without fabricating observations.

### F. Autoregressive world model

This is the central predictive component.

Suggested architecture:

- Causal Transformer.
    
- Configurable number of layers.
    
- Configurable hidden dimensions.
    
- Positional or temporal encoding.
    
- Autoregressive latent-state prediction.
    

Its responsibility is to model transitions between financial states.

It should not be permanently coupled to a single stock-price prediction task.

### G. Prediction heads

Initially implement:

1. Realized volatility forecasting.
    
2. Market-regime classification.
    
3. Forward return distribution estimation.
    
4. Latent-state prediction.
    

Additional heads can be introduced as the research develops.

---

# 4. Data Acquisition Strategy

## 4.1 Provider selection

The ingestion system must use provider adapters so the project is not dependent on one data vendor.

### Recommended initial configuration

**Primary market-data provider: Alpaca**

Use Alpaca for historical OHLCV ingestion.

Advantages:

- Dedicated market-data API.
    
- Multi-symbol historical bar requests.
    
- Multiple timeframes.
    
- Python SDK.
    
- Pagination support.
    

The historical bars endpoint uses a page token, and the ingestion implementation must continue fetching until all pages have been retrieved.

**Supplementary provider: Alpha Vantage**

Use Alpha Vantage for selected additional datasets:

- Fundamental information.
    
- Corporate financial observations.
    
- News and sentiment.
    
- Economic indicators.
    
- Additional market-data coverage.
    

Its documentation describes a broad range of financial and economic endpoints.

**Optional exploratory provider: yfinance**

Use yfinance for:

- Initial data exploration.
    
- Prototyping.
    
- Cross-checking selected observations.
    

Do not make yfinance the foundation of a commercial data pipeline. It is an unofficial interface to Yahoo Finance's publicly available APIs, and its documentation identifies personal-use restrictions on the underlying Yahoo data.

### Provider abstraction

Create a common interface:

```
from datetime import datetime
from typing import Protocol

import pandas as pd


class MarketDataProvider(Protocol):

    async def fetch_bars(
        self,
        symbols: list[str],
        start: datetime,
        end: datetime,
        timeframe: str,
    ) -> dict[str, pd.DataFrame]:
        ...
```

Implement separate adapters:

```
acquisition/
├── base.py
├── alpaca.py
├── alpha_vantage.py
├── yfinance.py
└── registry.py
```

Provider-specific response handling must remain inside the corresponding adapter.

The rest of the application should consume normalized domain objects.

## 4.2 Initial instrument universe

Start with ten instruments (ETFs):

| Ticker Symbol | Role                           |
| ------------- | ------------------------------ |
| SPY           | Broad equity market            |
| QQQ           | Technology-heavy equity market |
| IWM           | Small-cap equities             |
| DIA           | Large-cap equities             |
| TLT           | Treasury bonds                 |
| GLD           | Gold                           |
| USO           | Oil exposure                   |
| XLF           | Financial sector               |
| XLK           | Technology sector              |
| XLE           | Energy sector                  |

These instruments provide multiple market exposures and relationships.

## 4.2.1 Initial corporation universe

Start with twenty-five individual corporate entities that are publicly traded:


| Ticker Symbol | Sector                 | Industry                            |
| ------------- | ---------------------- | ----------------------------------- |
| MSFT          | Technology             | Software - Infrastructure           |
| AAPL          | Technology             | Consumer Electronics                |
| NVDA          | Technology             | Semiconductors                      |
| ASML          | Technology             | Semiconductor Equipment & Materials |
| GOOGL         | Communication Services | Internet Content & Information      |
| VZ            | Communication Services | Telecom Services                    |
| AMZN          | Consumer Cyclical      | Internet Retail                     |
| TSLA          | Consumer Cyclical      | Auto Manufacturers                  |
| MCD           | Consumer Cyclical      | Resturants                          |
| PG            | Consumer Defensive     | Household & Personal Products       |
| WMT           | Consumer Defensive     | Discount Stores                     |
| XOM           | Energy                 | Oil & Gas Integrated                |
| SLB           | Energy                 | Oil & Gas Equipment & Services      |
| JPM           | Financial Services     | Banks - Diversified                 |
| V             | Financial Services     | Credit Services                     |
| CB            | Financial Services     | Insurance - Property & Casualty     |
| JNJ           | Healthcare             | Drug Manufacturers - General        |
| LLY           | Healthcare             | Drug Manufacturers - General        |
| ISRG          | Healthcare             | Medical Instruments & Supplies      |
| CAT           | Industrials            | Farm & Heavy Construction Machinery |
| UPS           | Industrials            | Integrated Freight & Logistics      |
| RTX           | Industrials            | Aerospace & Defense                 |
| LIN           | Basic Materials        | Specialty Chemicals                 |
| FCX           | Basic Materials        | Copper                              |
| PLD           | Real Estate            | REIT - Industrial                   |
| NEE           | Utilities              | Utilities - Regulated Electric      |
These corporate entities provide a wide-range of contrasts, sectors and industries. The suggested data layers include:
1. Market Observations: Daily OHLCV, Intraday bars, returns, realized volatility, corporate actions.
2. Corporate Fundamentals: Revenue, earnings, margins, cash flow, debt, balance sheets, valuation metrics.
3. Entity Relationships: Parent/subsidiary relationships, competitors, suppliers, customers, industry membership, executives, board members.
4. Events & External Signals: Earnings announcements, corporate actions, regulatory events, economic indicators, news and sentiment.
5. Temporal Graph Snapshots: Reconstruct relationships using only information available at the prediction timestamp.

For the first experiment, use daily observations.

## 4.2.2 Expanded Universe

Once the 35 instrument and entity universe is constructed and the first market data and baselines has had ingestion being validated, point-in-time storage tested, and our graph reconstruction pipeline has been established, expand the universe to 100-250 entities across suppliers, customers, competitors and international companies so that we can validate the generalization capabilities of the GNN.
## 4.3 Historical coverage

Recommended initial historical window:

- Training: 2016–2022.
    
- Validation: 2023.
    
- Final test: 2024–2025.
    

These dates are initial experimental boundaries. Before finalizing the dataset, verify actual provider coverage and licensing.

The 2026 observations should be retained for later prospective evaluation rather than silently incorporated into the original test set.

## 4.4 Data acquisition requirements

Every ingestion adapter must implement:

- Authentication.
    
- Rate-limit handling.
    
- Retry with exponential backoff.
    
- Pagination.
    
- Date-range partitioning.
    
- Response validation.
    
- Duplicate detection.
    
- Missing-data detection.
    
- Structured error reporting.
    
- Raw-response provenance where permitted.
    

Do not silently discard malformed observations.

Every ingestion operation should generate a report containing:

```
provider
request_id
instrument
requested_start
requested_end
received_records
rejected_records
missing_intervals
ingested_at
source_version
status
```

---

# 5. Data Storage Architecture

## 5.1 ArcticDB: temporal and numerical source of truth

ArcticDB should hold the historical numerical observations.

Suggested libraries:

```
fwm_market
fwm_features
fwm_macro
fwm_derived
```

Suggested symbols:

```
bars_SPY_1d
bars_QQQ_1d
bars_IWM_1d

returns_SPY_1d
volatility_SPY_1d

macro_cpi
macro_fed_funds
macro_unemployment
```

Use a DatetimeIndex for temporal observations.

Recommended bar schema:

| Field            | Type                | Note         |
| ---------------- | ------------------- | ------------ |
| timestamp        | datetime64[ns, UTC] | retrieved_at |
| timestamp        | datetime64[ns, UTC] | observation  |
| timestamp        | datetime64[ns, UTC] | available_at |
| open             | float64             |              |
| high             | float64             |              |
| low              | float64             |              |
| close            | float64             |              |
| adjusted_close   | float64, nullable   |              |
| volume           | int64               |              |
| provider         | string              |              |
| adjustment_basis | string              |              |

Store observations using ArcticDB's versioned write and append mechanisms.

Use:

- `write()` for initial datasets.
    
- `append()` for new chronological observations.
    
- `update()` for controlled corrections.
    
- Versioned reads for historical reconstruction.
    

Do not treat ArcticDB as an ordinary transactional relational database.

### Critical requirement: data versioning

We need to preserve what was known at a particular point in time.

For example, a macroeconomic value originally published as 3.2% might subsequently be revised to 3.0%.

A model evaluated against the revised figure when the original figure was 3.2% would have access to information that wasn't historically available.

Preserve:

- Observation timestamp (observation).
    
- Publication timestamp (available_at).
    
- Ingestion timestamp (retrieved_at).
    
- Provider revision/version.
    
- Adjustment methodology.
    

This is essential for point-in-time backtesting.

## 5.2 SurrealDB: structured and relational information

SurrealDB will hold information needed by the GNN, language encoder, and multimodal assembly pipeline.

Suggested tables:

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
relationship
embedding
dataset_snapshot
```

Suggested graph relationships:

```
company -> operates_in -> industry
company -> belongs_to -> sector
company -> employs -> executive
company -> has_board_member -> board_member
company -> supplies -> company
company -> depends_on -> company
security -> represents -> company
news_article -> concerns -> company
corporate_event -> affects -> company
```

Relationships should carry temporal properties:

```
valid_from
valid_to
observed_at
published_at
source
confidence
```

This allows the GNN to reconstruct historical corporate relationships.

### Document storage

News articles and other textual information should be stored with:

```
document_id
source
url
published_at
retrieved_at
entity_ids
event_type
raw_content_reference
content_hash
language
```

Where licensing prevents storing full text, store permitted metadata, derived features, and references instead.

### Embeddings

Store model-generated embeddings with:

```
embedding_id
entity_id
encoder_version
embedding_dimension
observation_time
source_document_id
vector
```

Do not mix embeddings from different encoder versions without explicitly identifying them.

### Database responsibility

ArcticDB owns numerical temporal observations.

SurrealDB owns structured relationships, documents, entity metadata, and graph-oriented representations.

A dataset assembly service joins these systems using stable identifiers and timestamps.

Avoid maintaining two independently editable copies of the same underlying observation.

---

# 6. Data Normalization and Feature Engineering

Create a dedicated normalization pipeline.

Suggested modules:

```
normalization/
├── prices.py
├── returns.py
├── volatility.py
├── volume.py
├── macro.py
├── sentiment.py
├── corporate.py
└── temporal.py
```

## 6.1 Numerical transformations

Initial features:

- Log returns.
    
- Percentage returns.
    
- High-low range.
    
- Rolling volatility.
    
- Volume relative to rolling averages.
    
- Moving-average distances.
    
- Drawdown.
    
- Cross-instrument relative returns.
    

Example:

[  
r_t = \ln(P_t/P_{t-1})  
]

Realized volatility using daily returns:

[  
RV_{t,n} = \sqrt{\sum_{i=0}^{n-1}r_{t-i}^{2}}  
]

Use clearly documented rolling windows.

Do not normalize using statistics calculated from the complete historical dataset.

Normalization parameters must be fitted on training observations and applied unchanged to validation and test observations.

## 6.2 Event normalization

Normalize events into common structures.

For example:

```
event_type: regulatory_change
entity: company_123
published_at: timestamp
observed_at: timestamp
direction: unknown
severity: unknown
source: provider
```

Do not force every event into positive/negative sentiment.

Event semantics and economic consequences are different concepts.

## 6.3 Temporal alignment

Every observation must distinguish:

- Event time.
    
- Publication time.
    
- Availability time.
    
- Ingestion time.
    

The model may only consume information available by its prediction cutoff.

For example, an earnings report published after market close must not be available to a model making a prediction at that day's market close.

Use a consistent market calendar and explicitly define the forecasting cutoff.

---

# 7. Experimental Model Design

## 7.1 Initial model configuration

Start with deliberately small encoders.

|Component|Initial configuration|
|---|---|
|Time-series encoder|2 Transformer layers|
|GNN|2 GraphSAGE layers|
|Language encoder|2 Transformer layers|
|Macro encoder|2 temporal layers|
|Fusion|Cross-attention|
|World model|2–4 causal Transformer layers|
|Shared dimension|128|
|Attention heads|4|
|Context window|128 trading sessions|

These are starting values, not assumed optimal configurations.

For the language model, use a small vocabulary and embedding dimension appropriate to the dataset.

The prototype should not attempt to reproduce a general-purpose LLM.

## 7.2 Training objectives

Use multiple objectives.

**Objective A — Latent-state autoregression**

Predict the next latent financial state.

$$
L_{latent} =  
\left| \hat{Z}_{t+1} - Z_{t+1} \right|_2^2  
$$

This is a conceptual starting objective. The target representation must be well-defined and stable during training.

Consider a target encoder or stop-gradient strategy to prevent representation collapse.

**Objective B — Volatility forecasting**

Predict future realized volatility.

$$
L_{vol} = MAE(\hat{RV}_{t+h}, RV_{t+h})  
$$

**Objective C — Market-regime classification**

Predict a defined future market regime.

$$
L_{regime} = CrossEntropy(\hat{y}, y)  
$$

**Combined objective**

$$
L =  
\lambda_1 L_{latent}  
+\lambda_2 L_{vol}  
+\lambda_3 L_{regime}  
$$

All coefficients must be configurable.

Do not assume a particular loss weighting is optimal.

## 7.3 Autoregressive state prediction

The model should receive sequences of temporally aligned representations.

Conceptually:

```
Z_001 -> Z_002 -> Z_003 -> ... -> Z_t

                         |
                  Autoregressive model
                         |
                      Z_t+1
```

For the first prototype, predict one-step-ahead latent states and evaluate multiple downstream forecasting horizons.

Later versions can investigate multi-step autoregressive rollout as well as emitting each horizon directly.

The model must never receive future embeddings when predicting earlier states.

---

# 8. Baseline Models and Comparative Evaluation

This is one of the most important parts of the project.

We must not compare a sophisticated multimodal model against an inadequately configured baseline.

All models must receive equivalent information wherever their architectures support it.

## 8.1 Baseline A: HAR-RV

The Heterogeneous Autoregressive Realized Volatility model is a dedicated volatility-forecasting benchmark.

It uses volatility components across different time horizons.

A simplified specification is:

$$  
RV_{t+1} =  
\beta_0 +  
\beta_d RV_t +  
\beta_w RV_{t}^{(w)} +  
\beta_m RV_{t}^{(m)} +  
\epsilon_{t+1}  
$$

Where:

- (RV_t): daily realized volatility.
    
- (RV_t^{(w)}): weekly average realized volatility.
    
- (RV_t^{(m)}): monthly average realized volatility.
    

Use the original HAR-RV formulation as the benchmark and document any extensions.

HAR-RV is not a general-purpose financial world model. It is primarily a benchmark for realized-volatility forecasting.

Consequently, it should be compared with the FWM volatility head, not treated as a complete competitor for every prediction task.

## 8.2 Baseline B: Randomized tree models

Use two related implementations:

- RandomForestRegressor.
    
- ExtraTreesRegressor.
    

Extra Trees is especially useful because it introduces randomized split thresholds.

For a more complete comparison, add HistGradientBoostingRegressor.

These models should receive the same historical numerical feature set available to the corresponding experiment.

They will provide a strong test of whether the neural architecture learns something beyond conventional nonlinear feature interactions.

## 8.3 Baseline C: Persistence

For volatility:

$$
\hat{RV}_{t+1}=RV_t  
$$

For return:

$$
\hat{r}_{t+1}=0  
$$

These simple baselines are essential. A sophisticated model should demonstrate improvement over them.

## 8.4 Evaluation metrics

| Metric               | Application                  |
| -------------------- | ---------------------------- |
| MAE                  | Numerical forecasting        |
| RMSE                 | Numerical forecasting        |
| QLIKE                | Volatility forecasting       |
| Directional accuracy | Return direction             |
| Brier score          | Probabilistic classification |
| F1                   | Regime classification        |
| Cross-entropy        | Latent/token prediction      |
| Calibration error    | Prediction confidence        |

Do not use directional accuracy alone to evaluate a probabilistic forecasting model.

## 8.5 Statistical evaluation

Use:

- Walk-forward validation.
    
- Paired forecast-error comparisons.
    
- Confidence intervals.
    
- Block bootstrap where appropriate.
    
- Diebold-Mariano tests where their assumptions and implementation are appropriate.
    

Correct for multiple comparisons when evaluating many model variants.

Report performance by:

- Instrument.
    
- Market regime.
    
- Forecast horizon.
    
- Volatility environment.
    

---

# 9. Experimental Matrix

The initial experiment should isolate the contribution of each information modality.

| Experiment | Time-series | GNN | Language | Macro |
| ---------- | ----------- | --- | -------- | ----- |
| T0         | Yes         | No  | No       | No    |
| E0         | Yes         | No  | No       | No    |
| E1         | Yes         | Yes | No       | No    |
| E2         | Yes         | No  | Yes      | No    |
| E3         | Yes         | No  | No       | Yes   |
| E4         | Yes         | Yes | Yes      | Yes   |
In experiment T0, use the same causal backbone in three variants: (a) continuous input with a categorical output over volatility-normalised return buckets; (b) tokenized input with the same output; (c) continuous input with a direct regression head. Score all three variants against random walk, GBT and HAR.

Add the complete architecture as E5 if the full configuration differs from the combined modality experiment.

Each experiment should be evaluated against the same baseline suite.

This allows us to determine whether the GNN, language encoder, and macro encoder provide incremental value.

Also run an encoder-ablation experiment after the complete model has been trained.

The experiment tracker must record:

- Model configuration.
    
- Dataset snapshot.
    
- Feature schema version.
    
- Training seed.
    
- Training period.
    
- Validation period.
    
- Test period.
    
- Model checkpoint.
    
- Metrics.
    
- Hardware configuration.
    
- Training duration.
    
- Inference duration.
    

---

# 10. Repository Structure

Recommended initial repository:

```
financial-world-model/
│
├── configs/
│   ├── acquisition/
│   ├── storage/
│   ├── datasets/
│   ├── encoders/
│   ├── fusion/
│   ├── world_model/
│   ├── baselines/
│   └── experiments/
│
├── infrastructure/
│   ├── arcticdb/
│   ├── surrealdb/
│   └── docker/
│
├── src/
│   └── fwm/
│       │
│       ├── acquisition/
│       │   ├── base.py
│       │   ├── alpaca.py
│       │   ├── alpha_vantage.py
│       │   └── yfinance.py
│       │
│       ├── ingestion/
│       │   ├── orchestrator.py
│       │   ├── validation.py
│       │   └── provenance.py
│       │
│       ├── storage/
│       │   ├── arctic.py
│       │   ├── surreal.py
│       │   └── snapshots.py
│       │
│       ├── normalization/
│       │
│       ├── entities/
│       │
│       ├── graphs/
│       │
│       ├── language/
│       │
│       ├── tokenizer/
│       │
│       ├── datasets/
│       │
│       ├── encoders/
│       │   ├── timeseries/
│       │   ├── graph/
│       │   ├── language/
│       │   ├── tokenizer/
│       │   └── macro/
│       │
│       ├── fusion/
│       │
│       ├── world_model/
│       │
│       ├── objectives/
│       │
│       ├── prediction/
│       │
│       ├── baselines/
│       │   ├── har.py
│       │   ├── random_forest.py
│       │   ├── extra_trees.py
│       │   └── persistence.py
│       │
│       ├── evaluation/
│       │
│       └── experiments/
│
├── scripts/
│   ├── ingest.py
│   ├── validate_data.py
│   ├── build_dataset.py
│   ├── train.py
│   ├── evaluate.py
│   └── benchmark.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── data_quality/
│   ├── temporal_leakage/
│   └── reproducibility/
│
├── research/
│   ├── hypothesis.md
│   ├── methodology.md
│   ├── experiments.md
│   └── results/
│
├── artifacts/
├── pyproject.toml
└── README.md
```

The repository should keep research configuration separate from implementation.

A researcher should be able to change the model dimensions, enabled modalities, or training objective without modifying the underlying application code.

---

# 11. Coding Standards and Implementation Guide

## 11.1 Python requirements

Use:

- Python >=3.14,<3.15.
    
- Pydantic v2.
    
- Type annotations throughout.
    
- Async interfaces for external API and database operations.
    
- Explicit dependency injection.
    
- Structured logging.
    
- Configuration-driven behavior.
    

Avoid:

- Global mutable application state.
    
- Provider-specific code in model modules.
    
- Hardcoded API credentials.
    
- Silent exception handling.
    
- Hidden data transformations.
    
- Unversioned feature definitions.
    

Pin and test actual dependency versions rather than assuming all libraries support the same Python release.

ArcticDB currently advertises Python 3.14 support through its package distribution. Verify the installed SurrealDB SDK and all ML dependencies against the chosen interpreter before committing the environment.

## 11.2 Data contracts

Use Pydantic for ingestion and application boundaries.

Example:

```
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MarketBar(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    symbol: str
    timestamp: datetime

    open: float
    high: float
    low: float
    close: float
    volume: int

    provider: str
    adjustment_basis: str
```

Add field-level validation for:

- Positive prices.
    
- Nonnegative volume.
    
- Valid OHLC relationships.
    
- Timezone-aware timestamps.
    
- Valid adjustment basis.
    

Do not rely exclusively on Pydantic to validate entire historical datasets. Dataset-level checks must also detect gaps, duplicates, outliers, and inconsistent corporate-action adjustments.

## 11.3 Storage interfaces

Define storage abstractions independently of the implementation.

Example:

```
from datetime import datetime
from typing import Protocol

import pandas as pd


class TemporalRepository(Protocol):

    async def write(
        self,
        symbol: str,
        data: pd.DataFrame,
    ) -> None:
        ...

    async def read(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
    ) -> pd.DataFrame:
        ...
```

The concrete ArcticDB adapter should implement the interface.

Important: ArcticDB's primary interface is synchronous. Do not pretend its operations are natively asynchronous. If database operations block the event loop, use a bounded worker-thread strategy or a dedicated ingestion worker.

The same principle applies to SurrealDB: use its actual asynchronous SDK methods where appropriate.

## 11.4 Dataset construction

Create a unified dataset assembly interface.

Conceptually:

```
class DatasetBuilder:

    async def build(
        self,
        symbols: list[str],
        start: datetime,
        end: datetime,
        modalities: set[str],
    ):
        ...
```

The builder should:

1. Read temporal data from ArcticDB.
    
2. Retrieve applicable documents and graph records from SurrealDB.
    
3. Apply publication-time and availability-time restrictions.
    
4. Align observations.
    
5. Construct model inputs.
    
6. Generate forecasting targets.
    
7. Record dataset provenance.
    
8. Save an immutable dataset snapshot.
    

Do not make the neural network responsible for retrieving or joining database records.

## 11.5 Dataset snapshots

Every training run must reference a reproducible dataset snapshot.

A snapshot manifest should contain:

```
dataset_id
created_at
arctic_library_versions
surreal_snapshot_id
instrument_universe
date_range
feature_schema_version
encoder_input_schema_version
normalization_version
source_provenance
```

Use ArcticDB versions and named snapshots only to make the store reproducible

A model checkpoint without its corresponding dataset manifest is not a reproducible research artifact.

## 11.6 Model interfaces

Keep specialized encoders interchangeable.

For example:

```
from typing import Protocol
import torch
from torch import Tensor, nn


class FinancialEncoder(Protocol):

    def forward(
        self,
        inputs: Tensor,
        mask: Tensor | None = None,
    ) -> Tensor:
        ...
```

In production implementation, use appropriately typed `nn.Module` classes and a shared encoder output contract.

Each encoder should return:

- Embeddings.
    
- Temporal positions.
    
- Validity masks.
    
- Modality identifiers.
    

The fusion layer must not assume that every modality has an observation at every timestep.

---

# 12. Testing Requirements

Testing must cover both software correctness and scientific validity.

## 12.1 Unit tests

Test:

- Data validation.
    
- Feature calculations.
    
- Temporal alignment.
    
- Normalization.
    
- Tokenization.
    
- Graph construction.
    
- Model input shapes.
    
- Prediction outputs.
    

## 12.2 Integration tests

Test:

- Provider adapters.
    
- ArcticDB writes and reads.
    
- SurrealDB graph creation and traversal.
    
- Dataset assembly.
    
- Model checkpoint persistence.
    
- Full training and evaluation execution.
    

Use synthetic data for automated tests.

Never make the ordinary unit-test suite depend on live external APIs.

## 12.3 Temporal leakage tests

These are mandatory.

Construct synthetic observations with known publication timestamps and verify that the dataset builder cannot expose information before it becomes available.

Test:

- Future bars.
    
- Future corporate events.
    
- Revised macroeconomic values.
    
- Late-published earnings.
    
- Future graph relationships.
    
- Rolling normalization leakage.
    
- Cross-instrument temporal misalignment.
    

A passing temporal-leakage test suite should be a prerequisite for accepting experimental results.

## 12.4 Reproducibility tests

Run identical experiments with fixed seeds and identical dataset snapshots.

Verify that:

- Data ordering is deterministic.
    
- Dataset hashes match.
    
- Configuration hashes match.
    
- Training and evaluation metadata are preserved.
    
- Results are within documented numerical tolerances.
    

---

# 13. Scaling and Performance Evaluation

FW-0.1 must establish whether the architecture can scale.

Do not assume that because ArcticDB or SurrealDB can scale, the complete application can scale automatically.

Benchmark the entire pipeline.

## 13.1 Storage benchmarks

Measure:

- Initial ingestion throughput.
    
- Incremental ingestion throughput.
    
- ArcticDB read latency.
    
- SurrealDB graph traversal latency.
    
- Document retrieval latency.
    
- Dataset assembly throughput.
    
- Snapshot creation time.
    
- Storage consumption.
    

## 13.2 Model benchmarks

Measure:

- Training time per epoch.
    
- GPU utilization.
    
- VRAM consumption.
    
- RAM consumption.
    
- Inference latency.
    
- Batch throughput.
    
- Encoder-specific compute cost.
    
- Fusion-layer overhead.
    
- Autoregressive rollout cost.
    

## 13.3 Scale scenarios

|Scenario|Instruments|Frequency|Purpose|
|---|---|---|---|
|S0|10|Daily|Functional baseline|
|S1|50|Daily|Initial scaling|
|S2|250|Daily|Moderate expansion|
|S3|1,000|Daily|Large-universe simulation|
|S4|10–50|Intraday|Higher-frequency stress test|

The later scenarios can use synthetic data initially.

The goal is to distinguish model scaling limitations from data-ingestion and storage limitations.

## 13.4 Resource reporting

Record:

- CPU utilization.
    
- GPU utilization.
    
- RAM peak.
    
- VRAM peak.
    
- Storage throughput.
    
- Network throughput.
    
- Training duration.
    
- Inference latency.
    

The benchmark should be runnable on different hardware without changing the experimental definitions.

---

# 14. Project Milestones

## Phase 0 — Infrastructure verification

Deliverables:

- Repository.
    
- Dependency environment.
    
- ArcticDB local storage.
    
- SurrealDB instance.
    
- Provider interface.
    
- Configuration system.
    
- Automated test infrastructure.
    

Acceptance criteria:

- Both databases can be initialized and queried.
    
- The ingestion interface can be exercised with synthetic data.
    
- All dependency versions are verified against Python 3.14.
    

## Phase 1 — Data acquisition and storage

Deliverables:

- Alpaca adapter.
    
- Alpha Vantage adapter.
    
- Optional yfinance adapter.
    
- OHLCV ingestion.
    
- Initial macroeconomic dataset.
    
- ArcticDB persistence.
    
- SurrealDB entity and document schemas.
    

Acceptance criteria:

- Historical observations are reproducibly ingested.
    
- Pagination and retries work.
    
- Data validation reports are generated.
    
- Provenance is retained.
    

## Phase 2 — Dataset and baseline implementation

Deliverables:

- Normalization pipeline.
    
- Dataset builder.
    
- Snapshot manifests.
    
- Persistence baseline.
    
- HAR-RV.
    
- RandomForest.
    
- ExtraTrees.
    

Acceptance criteria:

- All baselines can train and evaluate using the same dataset definitions.
    
- Results are reproducible.
    
- Temporal leakage tests pass.
    

## Phase 3 — Specialized encoders

Deliverables:

- Time-series encoder.
    
- GNN.
    
- Language encoder.
    
- Macroeconomic encoder.
    

Acceptance criteria:

- Each encoder trains independently.
    
- Each produces a documented embedding output.
    
- Each has an independent validation objective.
    

## Phase 4 — Multimodal world model

Deliverables:

- Fusion layer.
    
- Cross-attention.
    
- Autoregressive transformer.
    
- Multi-task prediction heads.
    
- Joint training pipeline.
    

Acceptance criteria:

- End-to-end training completes.
    
- All modality ablations can be executed.
    
- Model checkpoints and dataset snapshots are linked.
    

## Phase 5 — Comparative research

Deliverables:

- Experimental matrix.
    
- Baseline comparisons.
    
- Walk-forward evaluation.
    
- Statistical testing.
    
- Resource benchmarks.
    
- Research report.
    

Acceptance criteria:

- Results are available for every experiment.
    
- Improvements and regressions are quantified.
    
- Computational costs are documented.
    
- Conclusions distinguish actual improvements from inconclusive results.
    

## Phase 6 — Scale feasibility

Deliverables:

- Larger synthetic and historical workloads.
    
- Storage benchmarks.
    
- Training benchmarks.
    
- Resource utilization report.
    
- Scaling recommendations.
    

Acceptance criteria:

- Identified bottlenecks.
    
- Documented scaling limits.
    
- Infrastructure migration recommendations.
    
- Decision on whether to proceed to FW-0.2.
    

---

# 15. Risk Register

|Risk|Mitigation|
|---|---|
|Historical data revisions|Point-in-time snapshots|
|Provider rate limits|Backoff, pagination, caching|
|Licensing restrictions|Source-specific provenance and usage policies|
|Survivorship bias|Historical universe membership|
|Temporal leakage|Availability-time enforcement|
|Model overfitting|Walk-forward evaluation|
|Modality imbalance|Auxiliary losses and ablation|
|Graph incompleteness|Confidence and missing-edge metadata|
|Expensive training|Small encoders and resource profiling|
|Weak generalization|Unseen instruments and regimes|
|Database bottlenecks|Independent storage benchmarks|
|Unstable latent learning|Target encoders and representation-collapse tests|

## Important licensing gate

ArcticDB's licensing must be reviewed before using it in a commercial deployment or economically beneficial business activity.

Its published FAQ identifies the Business Source License and states that commercial business use requires a commercial license agreement.

This matters because our research could eventually become a commercial data or model product.

We should not assume that an open-source repository automatically means unrestricted commercial use.

The prototype should document this as an explicit architecture and licensing decision, rather than postponing it until deployment.

---

# 16. Final Deliverables

FW-0.1 should produce the following artifacts:

1. A working ingestion framework.
    
2. A versioned ArcticDB temporal-data repository.
    
3. A SurrealDB entity and graph repository.
    
4. A reproducible dataset builder.
    
5. A temporal-leakage test suite.
    
6. Four independently testable encoders.
    
7. A multimodal fusion architecture.
    
8. An autoregressive financial world model.
    
9. HAR-RV and randomized-tree baselines.
    
10. An experiment tracking system.
    
11. A reproducible evaluation pipeline.
    
12. A performance and scaling report.
    
13. A formal research findings document.
    

# 17. Decision Criteria for FW-0.2

At the end of FW-0.1, we should be able to answer:

- Does multimodal information improve predictive performance?
    
- Does the GNN contribute measurable information?
    
- Does semantic event understanding outperform simple sentiment features?
    
- Does autoregressive latent-state learning provide value beyond direct forecasting?
    
- Does the model generalize to instruments it was not trained on?
    
- How much computational overhead does each modality introduce?
    
- Can the database and dataset architecture support expansion?
    
- What needs to change before introducing MAML-inspired adaptation?
    

The project should proceed to FW-0.2 only when we have sufficient evidence that the architecture provides value beyond conventional approaches, or when we have identified a compelling research result that warrants further investigation.

---

# Conclusion

FW-0.1 is not intended to prove that a financial world model can predict markets with certainty.

It is intended to determine whether a heterogeneous neural architecture can learn useful representations of financial environments, their relationships, and their temporal evolution.

The most important outcome is a reproducible experimental framework.

If the world model outperforms conventional approaches, we have a foundation for further research.

If it does not, the ablation studies and benchmark results should tell us whether the problem lies in the architecture, representations, training objectives, or information sources.

Either way, FW-0.1 should produce useful scientific and engineering knowledge rather than simply another forecasting model.

**Research principle:** Every claimed improvement must be reproducible, evaluated out of sample, and compared against an appropriate conventional baseline.

## Project Notes

1. Don't artificially constrain the GNN to ten market instruments.

The ten instruments are useful for the initial market benchmark, but a corporate relationship graph needs actual company nodes, suppliers, customers, executives, and sector relationships.

I'd add approximately 20–50 companies to the initial graph experiment. Otherwise, we're not really testing relational learning.

2. Treat HAR-RV as a specialized benchmark.

HAR-RV is specifically a realized-volatility model, not a general market-prediction model. Its original formulation uses volatility measurements across different temporal horizons. We should compare it against our volatility head, while using Extra Trees and Random Forest for broader forecasting comparisons. [Original HAR-RV research](https://doi.org/10.1093/JJFINEC/NBP001).

3. Make the data-provider layer interchangeable.

My preference would be:

- [Alpaca](https://docs.alpaca.markets/us/reference/stockbars) for initial historical market ingestion.
    
- [Alpha Vantage](https://www.alphavantage.co/documentation/) for supplementary financial, news, and economic information.
    
- [yfinance](https://ranaroussi.github.io/yfinance/) for exploratory work only.
    

4. Resolve ArcticDB licensing before commercial scaling.

This is particularly important given the possibility of turning the research into a commercial data product. ArcticDB's [published licensing FAQ](https://arcticdb.io/faqs/) explicitly identifies commercial licensing requirements. SurrealDB's native graph relationships are a good fit for our entity model.

## Implementation

Implement this in three engineering increments:

1. Infrastructure and ingestion: ArcticDB, SurrealDB, Alpaca, Alpha Vantage, schemas, and dataset snapshots.
    
2. Benchmark framework: HAR-RV, Extra Trees, Random Forest, walk-forward evaluation, and leakage tests.
    
3. Neural architecture: Specialized encoders, multimodal fusion, and the autoregressive model.
    

Do not begin neural-network development until the first two increments produce reproducible datasets and baseline results.

That gives us an important reference point: we'll know exactly what the neural architecture needs to beat, and we'll know whether any improvement comes from the architecture rather than differences in data preparation.