# PostgreSQL Basics Lab (GitHub Codespaces)

This lab provides a PostgreSQL database, sample tables, and Adminer, a browser
interface for running SQL. It is separate from the SQLite notebook lab.

## Start the lab

1. On GitHub, choose **Code → Codespaces → Create codespace on main**.
2. In the advanced creation options, select the **FundIT PostgreSQL Lab**
   configuration (`.devcontainer/postgresql/devcontainer.json`).
3. Wait for the container setup to finish. Adminer should open automatically
   on the private forwarded port 8080. If it does not, open port 8080 from the
   Ports panel.

Codespaces requires a GitHub account and may have usage or billing limits.
Alternatively, an instructor can run the included Docker Compose environment
locally.

## Connect with Adminer

Use the following values:

- System: **PostgreSQL**
- Server: `postgres`
- Username: `labuser`
- Password: in the Codespace terminal, run `printf '%s\n' "$PGPASSWORD"`
- Database: `labdb`

The setup generates a unique password in an untracked `.env` file. Do not
commit that file, share the password, or use real personal data in the sample
database.

To connect from the Codespace terminal:

```bash
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d "$PGDATABASE"
```

## Activities

The database is initialized with the `students`, `courses`, and `enrollments`
tables and synthetic sample rows. Start with files in `sql/labs/`:

- `lab1_select.sql`: SELECT and ORDER BY
- `lab2_filter_join.sql`: WHERE, AND/OR, and INNER JOIN
- `lab3_groupby.sql`: GROUP BY, aggregates, and HAVING
- `lab4_subqueries.sql`: subqueries, IN, and EXISTS
- `lab5_updates_indexes.sql`: INSERT, UPDATE, DELETE, and simple indexes

Open a lab file, run its task query in Adminer's SQL tab or in `psql`, then
compare the result with the task. Save your answers separately if your
instructor asks for submission evidence.

## Local setup

Install Docker Compose, then run the initialize script from the repository
root to create a unique local password and start the database environment:

```bash
bash Database_basics_postgress/.devcontainer/initialize.sh
docker compose -f Database_basics_postgress/docker-compose.yml up -d
```

The Compose file binds the host database and Adminer ports to loopback. Keep the
generated `.env` private. To stop the environment without removing its data:

```bash
docker compose -f Database_basics_postgress/docker-compose.yml down
```

To remove the database volume as well, use `down -v`; this permanently deletes
the lab database data.
