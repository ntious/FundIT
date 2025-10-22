#!/usr/bin/env bash
set -euo pipefail

# Copy env if missing
[ -f .env ] || cp .env.example .env

# Install Postgres client & basic tooling
apt-get update -y
apt-get install -y postgresql-client curl

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h localhost -p 5432 >/dev/null 2>&1; do sleep 1; done

echo "Running idempotent seed (ok to ignore errors if objects exist)..."
# Initial schema/data (runs again to ensure lab is ready even if init scripts were skipped by caching)
PSQL="psql postgresql://$PGUSER:$PGPASSWORD@localhost:$PGPORT/$PGDATABASE"
$PSQL -f sql/00_init.sql || true
$PSQL -f sql/01_schema.sql || true
$PSQL -f sql/02_seed.sql || true

echo "Setup complete. Open Adminer (port 8080) or use psql."
