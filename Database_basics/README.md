# Freshman Databases & SQL Lab (PostgreSQL, GitHub Codespaces)

**No installs required.** Students click one button and get a live PostgreSQL + a simple web UI (Adminer) in the browser.

## One‑click start
1. On GitHub, click **Code → Create codespace on main**.
2. Wait until you see “Setup complete.”
3. The port forwarder will open **Adminer** automatically (port 8080). If not, open the forwarded port manually.

### Adminer (web UI) login
- System: **PostgreSQL**
- Server: **postgres**
- Username: `labuser`
- Password: `labpass`
- Database: `labdb`

### psql (terminal client)
```bash
psql "postgresql://labuser:labpass@localhost:5432/labdb"
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
- To reset the database, stop the Codespace and delete the `pgdata` volume in the Docker tab, or create a fresh Codespace.

---
**Copyright:** MIT
