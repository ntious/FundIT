# Beyond the Calculator: Optional Python Projects

These standalone command-line projects are optional practice after the
[Simple Calculator Lab](../Simple_Calculator_Lab/README.md). Each applies
beginner Python concepts to a small task. They are intended to be run in a
terminal, not opened as executable notebook cells.

## Projects

| Project | Main concepts |
|---|---|
| `temperature_converter.py` | Functions, validation, numeric conversion |
| `advanced_calculator.py` | Functions, operations, state |
| `bill_splitter.py` | Arithmetic, input, formatted output |
| `age_calculator.py` | Dates and `datetime` |
| `guessing_game.py` | Loops, decisions, random values |
| `palindrome_checker.py` | Strings and normalization |
| `expense_tracker.py` | CSV, files, dictionaries |
| `password_checker.py` | Strings and regular expressions |
| `file_organizer.py` | Filesystem paths and file movement |
| `grade_analyzer.py` | Lists, loops, averages |

## Run a project

Install Python 3, then run a script from the repository root:

```console
python Beyond_Calculator_Projects/temperature_converter.py
```

On Windows, use `py` in place of `python` if that is how Python is installed.
Alternatively, open the repository in Binder, start a Jupyter terminal, and
run the same command. Binder sessions are temporary and do not save work when
closed.

## Safety and privacy

- The password checker demonstrates a few pattern rules only; it is not a
  secure password strength estimator. Use fake example strings and never enter
  a real password.
- The file organizer moves files into subfolders. Test it only on a disposable
  folder containing sample files, not on personal or important data. Its
  default folder is `sample_files`, and it asks for confirmation before moving
  anything.
- The expense tracker writes `expenses.csv` beside its script. Use synthetic
  data, not real financial or personal information.

## Practice and evidence

Try a normal case, an edge case, and an invalid input where relevant. Keep the
script and a short sample run or output as evidence if your instructor asks
for it. You can run the automated checks from the repository root:

```console
python -m unittest discover -s tests -v
```
