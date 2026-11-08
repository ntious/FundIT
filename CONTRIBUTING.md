# Contributing to FundIT

Thank you for your interest in contributing!
FundIT contains adaptable programming and database activities for a broader
Fundamentals of Information Technology context. Contributions that improve
correctness, learning clarity, accessibility, or instructor reuse are welcome.

## Contribution principles

- Keep activities beginner-friendly and aligned with the Input → Storage →
  Processing → Output (ISPO) model where applicable.
- State prerequisites, platform requirements, expected results, and what
  learners should submit or save.
- Prefer standard-library code for small Python exercises. Include automated
  tests for reusable logic and use temporary files/directories for tests that
  read or write data.
- Keep examples safe: use synthetic data, never ask learners to enter real
  passwords, and tell learners when a script changes files.
- Preserve existing paths and Binder/Codespaces links unless a change includes
  a migration plan.

## Pull request workflow

1. Fork and clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/FundIT.git
   cd FundIT
   ```

2. Create a focused branch:

   ```bash
   git checkout -b fix-sqlite-lab-instructions
   ```

3. Make the change and run the relevant checks:

   ```bash
   python -m unittest discover -s tests -v
   python -m compileall -q Simple_Calculator_Lab Beyond_Calculator_Projects
   ```

   For documentation or launch changes, also verify affected links and test
   the launch path when possible. Do not claim a clean Binder or Codespaces
   launch unless it was tested.

4. Commit, push your branch, and open a pull request. Include a short summary,
   tests performed, and any platform or migration notes.

## Python exercise conventions

- Use clear names and small functions for logic that can be tested independently.
- Use a `main()` function and the `if __name__ == "__main__":` guard for
  interactive command-line programs.
- Comment only where the reason for an action or a non-obvious step needs
  explanation; do not require a fixed number of comments per file.
- Use `snake_case` for new Python filenames. Existing directory names are
  retained to avoid breaking links.

## License

The repository's [MIT License](LICENSE) is the applicable license. The
educational setting describes the intended use of these materials; it is not an
additional non-commercial restriction. By submitting a contribution, you agree
that it may be distributed under the same MIT License.
