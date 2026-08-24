#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_dir="$(cd "$script_dir/.." && pwd)"
env_file="$project_dir/.env"

if [[ -f "$env_file" ]]; then
  existing_password="$(sed -n 's/^PGPASSWORD=//p' "$env_file" | head -n 1)"
  if [[ ${#existing_password} -lt 24 ]] ||
     [[ "$existing_password" == "labpass" ]] ||
     [[ "$existing_password" == "<GENERATED_UNIQUE_PASSWORD>" ]]; then
      echo "Refusing a missing, weak, or placeholder password in $env_file." >&2
      echo "Delete $env_file and rebuild to generate a unique credential." >&2
      exit 1
  fi
  chmod 600 "$env_file"
  exit 0
fi

umask 077
password="$(od -An -N24 -tx1 /dev/urandom | tr -d ' \n')"
if [[ ${#password} -ne 48 ]]; then
  echo "Could not generate a high-entropy database password." >&2
  exit 1
fi

printf '%s\n' \
  'PGUSER=labuser' \
  "PGPASSWORD=$password" \
  'PGDATABASE=labdb' \
  'PGHOST=postgres' \
  'PGPORT=5432' > "$env_file"

chmod 600 "$env_file"
echo "Created $env_file with a unique database password."
