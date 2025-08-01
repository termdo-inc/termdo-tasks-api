# >-----< CONFIG STAGE >-----< #

ARG POETRY_VERSION=2.1.3

# >-----< BASE STAGE >-----< #

FROM python:3.13-alpine AS base

# >-----< INSTALL STAGE >-----< #
FROM base AS installer

WORKDIR /app/

COPY poetry.lock .
COPY poetry.toml .
COPY pyproject.toml .
