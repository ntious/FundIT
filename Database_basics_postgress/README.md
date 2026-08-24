# Freshman Databases & SQL Lab (PostgreSQL, GitHub Codespaces)

**No installs required.** Students click one button and get a live PostgreSQL + a simple web UI (Adminer) in the browser.

## One‑click start
1. On GitHub, click **Code → Create codespace on main**.
2. Wait until you see “Setup complete.”
3. The port forwarder will open **Adminer** automatically (port 8080). If not, open the forwarded port manually.

The environment generates a unique database password in the untracked `.env`
file before the containers start. Both database-related host ports bind to
loopback, and Codespaces forwards them privately.

### Adminer (web UI) login
- System: **PostgreSQL**
- Server: **postgres**
- Username: `labuser`
- Password: run `printf '%s\n' "$PGPASSWORD"` in the Codespace terminal
- Database: `labdb`

### psql (terminal client)
```bash
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d "$PGDATABASE"
```

## What’s included
- Pre-created tables: `students`, `courses`, `enrollments` (with sample data).
- Beginner labs in `sql/labs/`:
  - `lab1_select.sql` (basic SELECTs, ORDER BY)
  - `lab2_filter_join.sql` (WHERE, AND/OR, INNER JOIN)
  - `lab3_groupby.sql` (GROUP BY, aggregates, HAVING)
  - `lab4_subqueries.sql` (subqueries, IN/EXISTS)
  - `lab5_updates_indexes.sql` (INSERT, UPDATE, DELETE, simple indexes)

## How to run a lab
1. Open a lab file under `sql/labs/`.
2. Copy a task query and run it in Adminer (SQL tab) or in `psql`.
3. Optional: save your solutions to a new file like `lab1_answers_<yourname>.sql` and commit.

## Instructor notes
- This repo is **Codespaces-ready** using devcontainers and Docker Compose.
- Adminer is lighter and simpler than pgAdmin—ideal for freshmen.
- Never commit `.env` or publish the generated password.
- To reset the database, stop the Codespace and delete the `pgdata` volume in the Docker tab, or create a fresh Codespace.

---
**Copyright:** MIT
