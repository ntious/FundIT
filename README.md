# FundIT: Applied Programming and Database Activities

FundIT contains hands-on programming and database activities used in a broader
Fundamentals of Information Technology context. Learners use the
**Input → Storage → Processing → Output (ISPO)** model to build small Python
programs, practice SQL, and connect technical work to an IT project.

FundIT is an activity collection, not a sequenced Python course. For guided
beginner Python instruction, see
[python_foundation](https://github.com/ntious/python_foundation). The two
repositories are complementary and do not need to be combined.

## Choose an activity

Times are planning estimates; instructors should adjust them for their class.
Evidence examples are suggestions to adapt to the course's submission policy.

| Activity | Concepts | Prerequisites | Approx. time | Learning outcome | Platform | Suggested evidence |
|---|---|---|---:|---|---|---|
| [Simple Calculator](Simple_Calculator_Lab/README.md) | Input, variables, functions, decisions, loops, ISPO | None | 45–60 min | Build and explain a small interactive Python program | Local Python terminal or Binder terminal | Source file and a sample run |
| [Temperature Converter](Beyond_Calculator_Projects/temperature_converter.py) | Functions, validation, numeric conversion | Basic input and variables | 20–30 min | Convert values between temperature scales | Local Python terminal or Binder terminal | Source file and test conversions |
| [Advanced Calculator](Beyond_Calculator_Projects/advanced_calculator.py) | Functions, operations, state | Simple Calculator or equivalent | 20–30 min | Reuse a previous result in later calculations | Local Python terminal or Binder terminal | Source file and a sample run using memory |
| [Bill Splitter](Beyond_Calculator_Projects/bill_splitter.py) | Arithmetic, input, formatted output | Basic arithmetic | 15–25 min | Calculate a per-person bill including a tip | Local Python terminal or Binder terminal | Source file and one checked calculation |
| [Age Calculator](Beyond_Calculator_Projects/age_calculator.py) | Dates and `datetime` concepts | Basic variables and input | 20–30 min | Calculate age and days until a birthday | Local Python terminal or Binder terminal | Source file and sample dates |
| [Number Guessing Game](Beyond_Calculator_Projects/guessing_game.py) | Loops, decisions, random values | Basic input and conditionals | 20–30 min | Use repeated input and feedback to control a game | Local Python terminal or Binder terminal | Source file and a completed game |
| [Palindrome Checker](Beyond_Calculator_Projects/palindrome_checker.py) | Strings, normalization, functions | Basic strings | 15–25 min | Normalize text and test whether it reads the same backward | Local Python terminal or Binder terminal | Source file and sample inputs |
| [Expense Tracker](Beyond_Calculator_Projects/expense_tracker.py) | CSV, files, dictionaries, persistence | Basic loops and collections | 30–45 min | Save and summarize categorized expenses | Local Python terminal or Binder terminal | Source file and sample CSV (use synthetic data) |
| [Password Checker](Beyond_Calculator_Projects/password_checker.py) | Strings, rules, regular expressions | Basic strings and conditionals | 15–25 min | Evaluate a few password-pattern rules | Local Python terminal or Binder terminal | Source file and sample results using fake values only |
| [File Organizer](Beyond_Calculator_Projects/file_organizer.py) | Filesystem, paths, extensions | Basic Python; disposable test folder | 20–30 min | Group files by extension using a script | Local Python terminal or Binder terminal | Source file and before/after listing of a disposable folder |
| [Grade Analyzer](Beyond_Calculator_Projects/grade_analyzer.py) | Lists, loops, averages, functions | Basic numbers and lists | 20–30 min | Summarize scores and assign an average letter grade | Local Python terminal or Binder terminal | Source file and sample scores |
| [SQLite SQL Lab](Database_basic_SQL_lite/README.md) | Tables, keys, inserts, queries, updates | None; prior database concepts helpful | 45–60 min | Create and query a small relational database | Binder notebook or local Jupyter | Completed notebook or query results |
| [PostgreSQL SQL Lab](Database_basics_postgress/README.md) | SELECT, joins, aggregates, subqueries, updates | Basic SQL recommended | 60–90 min | Query a multi-table PostgreSQL database | GitHub Codespaces with the lab dev container | SQL answers and query results |
| [Final Project Prototype](final_project/README.md) | Requirements, use cases, prototyping, testing | Course project milestones | Instructor-set | Demonstrate an interactive prototype and draft test plan | Browser; no installation for the sample | Prototype walkthrough and testing plan |

## Start here

### Learners

1. Begin with the [Simple Calculator Lab](Simple_Calculator_Lab/README.md), or
   use [python_foundation](https://github.com/ntious/python_foundation) if you
   want a guided Python sequence first.
2. Try any of the optional [mini-projects](Beyond_Calculator_Projects/README.md).
3. Choose the [SQLite](Database_basic_SQL_lite/README.md) or
   [PostgreSQL](Database_basics_postgress/README.md) activity as assigned.
4. Review the [final project prototype](final_project/README.md) as a sample;
   follow your instructor's requirements for your own work.

### Instructors

- Select activities from the matrix to fit your course; the sequence is
  adaptable rather than a required full Python curriculum.
- Adjust the time estimates and evidence examples to your class and assessment
  policy.
- Read each activity's prerequisites and platform notes before assigning it.
- Provide alternatives for learners who cannot use Binder or Codespaces.
- Keep project examples separate from graded student submissions and explain
  any local academic-integrity requirements.

## Running the activities

### Run a Python project locally

Install Python 3, clone or download this repository, then run a script from the
repository root. For example:

```console
python Simple_Calculator_Lab/calculator.py
python Beyond_Calculator_Projects/temperature_converter.py
```

On Windows, use `py` in place of `python` if that is how Python is installed.
These command-line programs are intended to run in a terminal; opening a
`.py` file in a notebook editor does not run its interactive prompts.

### Run the SQLite notebook

Open [SQL_Lab.ipynb](Database_basic_SQL_lite/SQL_Lab.ipynb) using the
[Binder launch](https://mybinder.org/v2/gh/ntious/FundIT/HEAD?labpath=Database_basic_SQL_lite/SQL_Lab.ipynb)
or a local Jupyter environment. Run cells from top to bottom. Binder sessions
are temporary: download your notebook or other work before closing the session.

### Run the PostgreSQL lab

Follow the setup instructions in the
[PostgreSQL lab guide](Database_basics_postgress/README.md). The activity uses
GitHub Codespaces, Docker Compose, PostgreSQL, and Adminer; it is separate from
the Binder-based SQLite notebook.

## Accessibility and beginner support

- Use the Markdown instructions and code in each activity; no prior Python
  experience is assumed for the Simple Calculator.
- In notebooks, run cells in order and read the output directly below each
  cell. Save a copy before ending a temporary cloud session.
- Instructors can provide an equivalent local or institution-approved
  environment when cloud platforms are unavailable or unsuitable.
- The password checker is a rule demonstration, **not** a secure password
  strength estimator. Never enter a real password.
- The file organizer moves files. Run it only on a disposable folder containing
  sample files, not on personal or important data.

## Repository map

| Path | Purpose |
|---|---|
| `Simple_Calculator_Lab/` | Introductory in-class Python activity |
| `Beyond_Calculator_Projects/` | Optional standalone Python practice |
| `Database_basic_SQL_lite/` | SQLite notebook and Binder environment |
| `Database_basics_postgress/` | PostgreSQL, Adminer, and Codespaces activity |
| `final_project/` | Prototype example and project guidance |
| `FundIT-pages-site/` | Source and build scripts for the course website |
| `tests/` | Automated tests for Python project logic |

The database folder names are retained to avoid breaking existing links; the
activities use the correct product names, **SQLite** and **PostgreSQL**.

## Contributing

Bug fixes, clearer instructions, accessibility improvements, and additional
beginner activities are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before
opening a pull request. Python changes can be checked locally with:

```console
python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs the same tests and checks Python syntax.

## License and citation

The repository is licensed under the [MIT License](LICENSE). Educational use is
the intended context, not an additional non-commercial restriction. The sample
final-project academic-integrity guidance describes course submission
expectations and does not change the repository license.

For this archived release, cite FundIT v1.0.0:
[10.5281/zenodo.24046742](https://doi.org/10.5281/zenodo.24046742). The project
DOI, which points to the latest version, is
[10.5281/zenodo.24046741](https://doi.org/10.5281/zenodo.24046741).

[GitHub release v1.0.0](https://github.com/ntious/FundIT/releases/tag/v1.0.0).
