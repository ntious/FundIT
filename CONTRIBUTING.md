# 🤝 Contributing to *Fundamentals of Information Technology (Programming Module)*

Thank you for your interest in contributing!
This repository is used for **educational and collaborative programming practice** in the *School of Information Technology, University of Cincinnati*.
Students are encouraged to submit improvements, fixes, and new exercises following the guidelines below.

---

## 🧠 Contribution Philosophy

All code in this repository should:

* Be **educational** — designed to teach or demonstrate a programming concept.
* Follow the **ISPO model** — Inputs → Storage → Processing → Output.
* Be **readable, modular, and well-documented**.

---

## 🧩 How to Contribute

### 1️⃣ Fork and Clone

Fork this repository to your GitHub account and clone it locally:

```bash
git clone https://github.com/YOUR-USERNAME/FundIT.git
cd FundIT
```

### 2️⃣ Create a New Branch

Give your branch a clear name:

```bash
git checkout -b feature-add-new-lab
```

### 3️⃣ Make Your Changes

You can:

* Add a new lab or mini-project (e.g., `bmi_calculator.py`)
* Improve code comments or fix bugs
* Add examples or new Binder links to the README

> 💡 Each Python file should include a top-level docstring:

```python
"""
Project Title: BMI Calculator
Author: Your Name
Date: YYYY-MM-DD
Description: Calculates BMI and provides weight category.
Structure: Inputs → Storage → Processing → Output
"""
```

### 4️⃣ Test Your Code

Make sure your program runs without errors:

```bash
python Beyond_Calculator_Projects/your_script.py
```

or use **Binder** to test it online.

### 5️⃣ Commit and Push

```bash
git add .
git commit -m "Added new BMI calculator mini-project"
git push origin feature-add-new-lab
```

### 6️⃣ Submit a Pull Request

Go to your fork on GitHub and open a **Pull Request (PR)** to the main repository.
Include a short summary of your contribution (what you added, improved, or fixed).

---

## 🧰 Code Style Guidelines

* Use **clear variable names** (`total_amount` instead of `x`).
* Keep lines under **80 characters** where possible.
* Include at least **2–3 inline comments** explaining major logic steps.
* Use **functions** where appropriate to structure your code.
* Follow the **Inputs → Storage → Processing → Output** comment format for all scripts.

---

## ⚙️ Example Project Layout

Here’s how your Python file should generally be structured:

```python
# ---------- INPUTS ----------
# Get input data from the user
# ---------- STORAGE ----------
# Store constants, configuration, or global variables
# ---------- PROCESSING ----------
# Perform the main logic or computations
# ---------- OUTPUT ----------
# Display the result clearly
```

---

## ✅ Before Submitting

✔ Test your code locally or via Binder
✔ Confirm your script runs without syntax errors
✔ Ensure you didn’t overwrite existing files unintentionally
✔ Follow naming conventions (e.g., `snake_case` for file names)

---

## 👩‍🏫 Maintainer

**Dr. Isaac Kofi Nti**
Assistant Professor, School of Information Technology
University of Cincinnati

📧 [ntious@ucmail.uc.edu](mailto:ntious1@gmail.com)
🌐 [Google Scholar]([https://researchdirectory.uc.edu/p/ntious](https://scholar.google.com/citations?user=eMCHVxcAAAAJ&hl=en))

---

## 📝 License

All contributions are licensed for **educational and non-commercial use**.
By submitting a pull request, you agree that your contribution may be used for instructional or student learning purposes.

---

