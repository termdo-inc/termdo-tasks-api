# Termdo Tasks API

Internal microservice for task management (CRUD) scoped to user accounts. Exposes REST endpoints via FastAPI and persists data in PostgreSQL.

This service is part of the Termdo system alongside:

- termdo-gateway-api: Edge/API gateway and routing
- termdo-auth-api: Authentication and JWT issuance
- termdo-web: Frontend web application
- termdo-db: Database assets (schemas, migrations, seed data)
- termdo-infra: Infrastructure and deployment assets

## Features

- CRUD for tasks per account (`accountId` path parameter)
- Pydantic models with field aliases for clean API payloads
- PostgreSQL async connection pool via `asyncpg`
- Consistent response envelope with `data` field
- Custom `X-Hostname` response header for observability

## Tech Stack

- Runtime: Python 3.12+
- Web: FastAPI + Uvicorn
- DB: asyncpg (PostgreSQL)
- Config: python-dotenv (used in dev mode)
- Dev tooling: Black, isort, Flake8, Pytest
- Packaging: Poetry (PEP 621) and wheels
- Container: Multi-stage Docker

## Getting Started

### Prerequisites

- Python 3.12+
- A reachable PostgreSQL instance
- An `.env` file (see `.env.example`)

### Environment Variables

- `APP_PORT`: Port number to listen on
- `DB_HOST`: PostgreSQL host
- `DB_PORT`: PostgreSQL port
- `DB_USER`: PostgreSQL user
- `DB_PASSWORD`: PostgreSQL password
- `DB_NAME`: PostgreSQL database name

Create a `.env` file by copying `.env.example` and filling values accordingly.

### Install, Build, Run (Local)

Using Poetry (recommended):

```bash
poetry install
poetry run python -m termdo_tasks_api.main --dev
```

Using Makefile (expects `.venv` with deps installed):

```bash
python -m venv .venv && . .venv/bin/activate
pip install -U pip
pip install -e .
make run  # runs: python -m termdo_tasks_api.main --dev
```

Server adds `X-Hostname` header and initializes the DB pool on startup.

### Docker

Builds a wheel and installs into a slim runtime image.

```bash
docker build -t termdo-tasks-api:local .
docker run --rm --env-file .env -p 8081:8081 termdo-tasks-api:local
```

Alternatively, use the provided compose file (expects external DB on the same network):

```bash
docker compose up --build
```

## Database

The service expects a `task` table with fields referenced by the code:

- `task_id` (integer, primary key)
- `account_id` (integer, owner account)
- `title` (text)
- `description` (text)
- `is_completed` (boolean)
- `created_at` (timestamp with time zone)
- `updated_at` (timestamp with time zone)

Example schema:

```sql
CREATE TABLE IF NOT EXISTS task (
  task_id     SERIAL PRIMARY KEY,
  account_id  INTEGER NOT NULL,
  title       TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  is_completed BOOLEAN NOT NULL DEFAULT FALSE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
  -- , FOREIGN KEY (account_id) REFERENCES account(account_id)
);

CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_set_updated_at ON task;
CREATE TRIGGER trg_set_updated_at
BEFORE UPDATE ON task
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
```

## API

All responses share a simple envelope:

- Header: `X-Hostname: <server-hostname>`
- Body: `{ data: <payload> }`

Base router is the root; all routes are under `/{account_id}`. Validation is enforced by FastAPI/Pydantic.

### GET /{accountId}

- Success: `200 OK`
  - `data`: `Array<{ taskId, title, description, isCompleted, createdAt, updatedAt }>`

Example:

```bash
curl -sS http://localhost:$APP_PORT/123
```

### POST /{accountId}

- Body:
  - `title`: string (1–64)
  - `description`: string (0–1024)
  - `isCompleted`: boolean
- Success: `201 Created`
  - `data`: `{ taskId, title, description, isCompleted, createdAt, updatedAt }`

Example:

```bash
curl -sS -X POST http://localhost:$APP_PORT/123 \
  -H 'Content-Type: application/json' \
  -d '{"title":"Study Python","description":"Finish FastAPI course","isCompleted":false}'
```

### GET /{accountId}/{taskId}

- Success: `200 OK`
  - `data`: `{ taskId, title, description, isCompleted, createdAt, updatedAt }`
- Errors: `404 Not Found` when task does not exist

Example:

```bash
curl -sS http://localhost:$APP_PORT/123/456
```

### PUT /{accountId}/{taskId}

- Body:
  - `title`: string (1–64)
  - `description`: string (0–1024)
  - `isCompleted`: boolean
- Success: `200 OK`
  - `data`: `{ taskId, title, description, isCompleted, createdAt, updatedAt }`
- Errors: `404 Not Found` when task does not exist

Example:

```bash
curl -sS -X PUT http://localhost:$APP_PORT/123/456 \
  -H 'Content-Type: application/json' \
  -d '{"title":"Study Python","description":"Practice pydantic","isCompleted":true}'
```

### DELETE /{accountId}/{taskId}

- Success: `200 OK`
  - `data`: `null`
- Errors: `404 Not Found` when task does not exist

Example:

```bash
curl -sS -X DELETE http://localhost:$APP_PORT/123/456
```

## Validation Rules

- `title`: length 1–64, required
- `description`: length 0–1024, required (may be empty string)
- `isCompleted`: boolean, required

If validation fails, FastAPI returns a 422 response with details.

## Middleware & Behavior

- Header Middleware: Adds `X-Hostname` with server hostname to responses.
- Lifespan: Opens DB connection pool on startup; closes on shutdown.

## Development

- Format: `poetry run black source/` or `make format`
- Lint: `poetry run flake8` or `make lint`
- Clean: `make clean`

## Integration Notes

- Typically called via `termdo-gateway-api`.
- Authorization is expected upstream; routes are scoped by `accountId` path segment.
- Compose uses the `termdo-net` network; ensure the DB is reachable on that network (see `termdo-db` or your infrastructure setup in `termdo-infra`).

## License

MIT — see `LICENSE.md`.
