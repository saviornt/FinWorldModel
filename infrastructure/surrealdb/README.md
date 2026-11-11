# SurrealDB Infrastructure

SurrealDB provides the relational and graph-oriented database layer for FinWorldModel.

It stores financial entity relationships, corporate structures, ownership information, economic classifications, and other structured information that connects the financial world model.

SurrealDB is deployed as a Docker container and managed independently of the Python application.

## 1. Architecture

**Database:** SurrealDB

**Deployment:** Docker Compose

**Storage engine:** SurrealKV

**Network binding:** `127.0.0.1:8000`

**Persistent storage:** Docker named volume

**Schema management:** SurrealQL

### Responsibilities

SurrealDB is responsible for:

- Publicly traded corporate entities
- Corporate ownership and subsidiaries
- Board members and executive relationships
- Sector and industry classifications
- Corporate events and organizational changes
- Relationships between financial entities
- Structured metadata and references to external datasets

Historical market observations and high-volume time-series data belong in ArcticDB rather than SurrealDB.

## 2. Directory Structure

```text
infrastructure/surrealdb/
├── compose.yaml
├── .env
├── README.md
└── schema/
    └── schema.surql
```

The actual database files are persisted in the Docker volume `surrealdb-data`.

## 3. Configuration

### Environment Variables

The `.env` file contains database authentication credentials.

```dotenv
SURREAL_USER=root
SURREAL_PASS=replace-with-a-long-random-password
```

Do not commit `.env` files or database credentials to version control.

### Database Endpoint

Local endpoint:

```text
http://127.0.0.1:8000
```

WebSocket endpoint:

```text
ws://127.0.0.1:8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

## 4. Deployment

Deployment is managed by the project initialization script.

From the project root:

```fish
uv run python scripts/deploy_surrealdb.py
```

The script performs the following operations:

1. Checks Docker availability.
2. Validates the Docker Compose configuration.
3. Creates or updates the SurrealDB container.
4. Waits for the container to become available.
5. Checks Docker container health.
6. Checks the SurrealDB HTTP health endpoint.
7. Reports deployment status and diagnostics.

### Manual Deployment

The container can also be managed directly:

```fish
docker compose -f infrastructure/surrealdb/compose.yaml up -d
```

Check status:

```fish
docker compose -f infrastructure/surrealdb/compose.yaml ps
```

View logs:

```fish
docker compose -f infrastructure/surrealdb/compose.yaml logs -f surrealdb
```

Stop the service:

```fish
docker compose -f infrastructure/surrealdb/compose.yaml stop
```

Restart the service:

```fish
docker compose -f infrastructure/surrealdb/compose.yaml restart surrealdb
```

## 5. Schema Management

Schema definitions are maintained as SurrealQL files under:

```text
infrastructure/surrealdb/schema/
```

Initial schema:

```text
schema/schema.surql
```

The schema is intended to define the namespaces, databases, tables, indexes, fields, and relationships used by FinWorldModel.

Schema changes should be version-controlled and reviewed before deployment.

Avoid relying on destructive schema changes or automatic database recreation to apply updates.

## 6. Persistence and Backups

SurrealDB data is stored in the persistent Docker volume:

```text
surrealdb-data
```

The database volume must survive container recreation and application updates.

Do not use:

```fish
docker compose down -v
```

unless intentionally deleting the database and all its persistent data.

Backups should be performed using a supported SurrealDB backup/export procedure and verified before being considered recoverable.

## 7. Security

- Database ports are bound to localhost by default.
- Credentials must not be committed to Git.
- Production deployments must use strong credentials.
- Remote access should use an authenticated and encrypted network path.
- Database access should be restricted to authorized application components.
- Backups should be protected against unauthorized access.

## 8. Operational Responsibilities

| Operation | Mechanism |
|---|---|
| Initial deployment | `deploy_surrealdb.py` |
| Health verification | Deployment script |
| Database queries | SurrealDB Python SDK |
| Schema management | SurrealQL |
| Persistence | Docker named volume |
| Logs | Docker Compose |
| Backups | Dedicated backup procedure |

## 9. Integration with FinWorldModel

SurrealDB is accessed through the application's database integration layer.

Application modules should not independently create database connections or embed credentials.

Connection configuration and lifecycle management should eventually be centralized in the application infrastructure layer.

SurrealDB is one component of the broader FinWorldModel storage architecture, alongside ArcticDB for time-series data and MLflow for experiment tracking.

---

**Status:** Initial infrastructure configuration

**Project:** FinWorldModel
