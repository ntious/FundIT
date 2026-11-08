import csv
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

from Beyond_Calculator_Projects import (
    advanced_calculator,
    age_calculator,
    bill_splitter,
    expense_tracker,
    file_organizer,
    grade_analyzer,
    guessing_game,
    palindrome_checker,
    password_checker,
    temperature_converter,
)
from Simple_Calculator_Lab import calculator


class CalculatorTests(unittest.TestCase):
    def test_arithmetic_operations(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.divide(6, 3), 2)

    def test_divide_by_zero_is_rejected(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1, 0)

    def test_advanced_calculator_operations(self):
        self.assertEqual(advanced_calculator.OPS["A"][1](2, 3), 5)
        with self.assertRaises(ZeroDivisionError):
            advanced_calculator.OPS["D"][1](1, 0)


class MiniProjectTests(unittest.TestCase):
    def test_temperature_conversion(self):
        self.assertAlmostEqual(temperature_converter.convert(32, "F", "C"), 0)
        self.assertAlmostEqual(temperature_converter.convert(0, "C", "F"), 32)
        self.assertAlmostEqual(temperature_converter.convert(0, "C", "K"), 273.15)

    def test_temperature_rejects_unknown_scale(self):
        with self.assertRaises(ValueError):
            temperature_converter.convert(10, "X", "C")

    def test_bill_split(self):
        self.assertAlmostEqual(bill_splitter.compute_split(100, 10, 4), 27.5)

    def test_age_and_days_to_birthday(self):
        self.assertEqual(
            age_calculator.compute_age(date(2000, 6, 10), date(2025, 6, 9)),
            24,
        )
        self.assertEqual(
            age_calculator.days_until_next_birthday(
                date(2000, 6, 10), date(2025, 6, 9)
            ),
            1,
        )

    def test_guessing_game_reports_attempt_count(self):
        output = io.StringIO()
        with (
            patch.object(guessing_game.random, "randint", return_value=2),
            patch("builtins.input", side_effect=["1", "3", "2"]),
            redirect_stdout(output),
        ):
            guessing_game.play("E")
        self.assertIn("Correct! You guessed in 3 tries.", output.getvalue())

    def test_palindrome_normalizes_case_and_punctuation(self):
        self.assertTrue(palindrome_checker.is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(palindrome_checker.is_palindrome("FundIT"))

    def test_password_rule_results(self):
        score, results = password_checker.evaluate("Abcdef1!")
        self.assertEqual(score, len(password_checker.RULES))
        self.assertTrue(all(result for _, result in results))

    def test_grade_analysis(self):
        self.assertEqual(grade_analyzer.analyze([80, 90]), (85.0, 90, 80, "B"))
        self.assertEqual(grade_analyzer.analyze([]), (0.0, 0.0, 0.0, "N/A"))

    def test_expense_tracker_round_trips_csv_in_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            data_file = Path(directory) / "expenses.csv"
            totals = {"food": 12.5, "travel": 7.25}
            with patch.object(expense_tracker, "FILE", data_file):
                expense_tracker.save_totals(totals)
                loaded = expense_tracker.load_totals()
            self.assertEqual(dict(loaded), totals)
            with data_file.open(newline="", encoding="utf-8") as file:
                self.assertEqual(len(list(csv.reader(file))), 2)

    def test_file_organizer_moves_only_files_from_temporary_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / "notes.txt").write_text("sample", encoding="utf-8")
            (base / "archive.zip").write_text("sample", encoding="utf-8")
            (base / "existing").mkdir()

            file_organizer.organize(str(base))

            self.assertTrue((base / "Text" / "notes.txt").is_file())
            self.assertTrue((base / "Other" / "archive.zip").is_file())
            self.assertTrue((base / "existing").is_dir())

    def test_file_organizer_defaults_to_sample_folder_and_requires_confirmation(self):
        output = io.StringIO()
        with patch("builtins.input", return_value=""):
            self.assertEqual(file_organizer.get_folder(), "sample_files")
        with (
            patch("builtins.input", side_effect=["", "no"]),
            redirect_stdout(output),
        ):
            file_organizer.main()
        self.assertIn("Cancelled. No files were moved.", output.getvalue())


class RepositorySetupTests(unittest.TestCase):
    def test_sqlite_binder_target_exists(self):
        repository_root = Path(__file__).resolve().parents[1]
        notebook_path = repository_root / "Database_basic_SQL_lite" / "SQL_Lab.ipynb"
        self.assertTrue(notebook_path.is_file())
        self.assertTrue((repository_root / ".binder" / "requirements.txt").is_file())

    def test_notebook_cell_magics_start_their_code_cell(self):
        repository_root = Path(__file__).resolve().parents[1]
        notebook_path = repository_root / "Database_basic_SQL_lite" / "SQL_Lab.ipynb"
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        for cell_number, cell in enumerate(notebook["cells"]):
            if cell["cell_type"] != "code":
                continue
            lines = "".join(cell["source"]).splitlines()
            nonempty_lines = [line for line in lines if line.strip()]
            for line in nonempty_lines:
                if line.lstrip().startswith("%%"):
                    self.assertEqual(
                        line,
                        nonempty_lines[0],
                        f"Cell magic must start code cell {cell_number}",
                    )

    def test_postgresql_codespaces_configuration_resolves_its_files(self):
        repository_root = Path(__file__).resolve().parents[1]
        config_path = (
            repository_root / ".devcontainer" / "postgresql" / "devcontainer.json"
        )
        config = json.loads(config_path.read_text(encoding="utf-8"))
        compose_path = (config_path.parent / config["dockerComposeFile"][0]).resolve()
        database_root = repository_root / "Database_basics_postgress"

        self.assertTrue(compose_path.is_file())
        self.assertTrue(
            (repository_root / config["initializeCommand"].split(maxsplit=1)[1]).is_file()
        )
        self.assertTrue(
            (database_root / config["postCreateCommand"].split()[-1]).is_file()
        )


if __name__ == "__main__":
    unittest.main()
