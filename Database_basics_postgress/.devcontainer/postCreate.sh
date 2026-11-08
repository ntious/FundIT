#!/usr/bin/env bash
set -euo pipefail

: "${PGUSER:?Missing generated database user}"
: "${PGPASSWORD:?Missing generated database password}"
: "${PGDATABASE:?Missing generated database name}"
: "${PGHOST:?Missing database host}"
: "${PGPORT:?Missing database port}"

# Install Postgres client & basic tooling
apt-get update -y
apt-get install -y postgresql-client curl

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h "$PGHOST" -p "$PGPORT" >/dev/null 2>&1; do sleep 1; done

echo "Applying idempotent schema and sample data..."
PSQL=(psql -v ON_ERROR_STOP=1 -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d "$PGDATABASE")
"${PSQL[@]}" -f sql/00_init.sql
"${PSQL[@]}" -f sql/01_schema.sql
"${PSQL[@]}" -f sql/02_seed.sql

echo "Setup complete. Open the private Adminer forward (port 8080) or use psql."
