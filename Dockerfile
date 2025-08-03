# >-----< BASE IMAGE >-----< #

FROM python:3.13-alpine AS base

ENV \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  \
  PIP_NO_INPUT=1 \
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  \
  PATH="/app/.venv/bin:$PATH"

RUN \
  addgroup --system appgroup && \
  adduser --system --no-create-home --ingroup appgroup appuser

# >-----< POETRY IMAGE >-----< #

FROM base AS poetry

ENV \
  POETRY_VERSION=2.1.3 \
  POETRY_HOME="/opt/poetry" \
  \
  PATH="/opt/poetry/bin:$PATH"

RUN \
  wget -qO- https://install.python-poetry.org | python3 && \
  poetry self add poetry-plugin-export

# >-----< BUILD STAGE >-----< #
FROM poetry AS builder

WORKDIR /app/

COPY source/ source/
COPY \
  poetry.lock \
  poetry.toml \
  pyproject.toml ./

RUN \
  poetry export --no-interaction --no-cache --without-hashes --only=main --output=requirements.txt && \
  pip wheel --no-deps --requirement=requirements.txt --wheel-dir=out/ && \
  poetry build --no-interaction --no-cache --format=wheel --output=out/ && \
  rm requirements.txt

# >-----< RUN STAGE >-----< #
FROM base AS runner

USER appuser

WORKDIR /app/

COPY --from=builder --chown=appuser:appgroup /app/out/ out/

RUN \
  python -m venv .venv && \
  pip install out/*.whl && \
  rm -rf out/

ENTRYPOINT ["python", "-m", "termdo_tasks_api.main"]
