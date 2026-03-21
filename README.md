
# 💻 Fundamentals of Information Technology (Programming)

Welcome to the **Fundamentals of Information Technology** programming repository!
This repo contains a section of practical hands-on Python labs used in the course to help you understand how a computer system works through **Input → Storage → Processing → Output (ISPO)**.

---

## 🎯 Module Purpose

This module of the course introduces students to **core programming and computational thinking**.
By writing simple Python programs, you’ll learn how data flows through systems and how to design programs that make computers solve problems logically and efficiently.

You’ll gain experience with:

* Writing and running Python programs
* Understanding the **ISPO** model of computing
* Using loops, conditionals, and functions
* Handling errors and validating input
* Structuring clean and reusable code

---

## 🧩 Repository Structure

```
FundIT/
│
├── Simple_Calculator_Lab/
│   ├── calculator.py
│   ├── README.md
│   └── .gitignore
│
└── Beyond_Calculator_Projects/
    ├── temperature_converter.py
    ├── advanced_calculator.py
    ├── bill_splitter.py
    ├── age_calculator.py
    ├── guessing_game.py
    ├── palindrome_checker.py
    ├── expense_tracker.py
    ├── password_checker.py
    ├── file_organizer.py
    ├── grade_analyzer.py
    └── README.md
```

---

## 🧮 In-Class Lab: Simple Calculator

The **Simple Calculator Lab** is your first coding exercise, introducing:

* Functions and variables
* Conditionals and loops
* Input/output
* Error handling
* Logical program flow (ISPO model)

### 🔗 Launch in Binder

Run the calculator live in your browser — no installation required!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ntious/FundIT/HEAD?labpath=Simple_Calculator_Lab/)
[![Launch Binder Directly](https://img.shields.io/badge/Launch_on_Binder-Click_to_Run-green?logo=jupyter)](https://mybinder.org/v2/gh/ntious/FundIT/HEAD?labpath=Simple_Calculator_Lab)

> 💡 *Tip:* This lab simulates how computers work:
> **Input** data → **Store** it in memory → **Process** it → **Output** the result.

---

## 🚀 Beyond the Calculator Projects

For students who want to go further — these optional mini-projects expand on your foundational skills.
Each one focuses on a specific new Python concept while reinforcing structured problem solving.

| #  | Project                         | Concepts                     | Binder Link                                                                                                         |
| -- | ------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1  | 🔢 Temperature Converter        | Functions, validation        | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/temperature_converter.py) |
| 2  | 🧮 Advanced Calculator (Memory) | State management             | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/advanced_calculator.py)   |
| 3  | 💰 Bill Splitter                | Arithmetic, formatted output | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/bill_splitter.py)         |
| 4  | 📅 Age Calculator               | Using `datetime`             | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/age_calculator.py)        |
| 5  | 🎲 Number Guessing Game         | Loops and logic              | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/guessing_game.py)         |
| 6  | 🔡 Palindrome Checker           | String manipulation          | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/palindrome_checker.py)    |
| 7  | 🧾 Expense Tracker              | File I/O and CSV             | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/expense_tracker.py)       |
| 8  | 🔐 Password Strength Checker    | Regular expressions          | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/password_checker.py)      |
| 9  | 🗂 File Organizer               | Automation and filesystem    | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/file_organizer.py)        |
| 10 | 📊 Grade Analyzer               | Lists, loops, averages       | [Launch](https://mybinder.org/v2/gh/ntious/FundIT/v1.0?labpath=Beyond_Calculator_Projects/grade_analyzer.py)        |



---

## ⚙️ Getting Started (Run Locally)

### 🔸 Step 1 — Clone the Repository

Open your terminal or VS Code and run:

```bash
git clone https://github.com/ntious/FundIT.git
cd FundIT
```

### 🔸 Step 2 — Run Any Script

Each program can be executed individually using:

```bash
python Simple_Calculator_Lab/calculator.py
```

or for a project in the advanced directory:

```bash
python Beyond_Calculator_Projects/guessing_game.py
```

### 🔸 Step 3 — Try Interactive Mode (Optional)

You can also open these files inside **VS Code**, **Jupyter Notebook**, or run them directly in the **Binder environment** linked above.

---

## 🧠 Learning Outcomes

By completing the labs in this repository, you will:

* Understand how a computer processes information step by step
* Apply programming logic to solve real-world problems
* Develop structured thinking for algorithm design
* Gain confidence using Python syntax, libraries, and debugging tools

---

## 🧰 Tools and Resources

* 🐍 [Python 3.8+](https://www.python.org/downloads/)
* ☁️ [MyBinder.org](https://mybinder.org) — run code in your browser
* 🧑‍💻 [GitHub Codespaces](https://github.com/features/codespaces) — online development
* 🧠 [W3Schools Python Reference](https://www.w3schools.com/python/)
* 🎓 [Real Python Tutorials](https://realpython.com/)

---

## 🤝 Contribution Guide

Students and contributors are welcome to **improve, expand, or fix** any of the labs in this repository.

### 🔧 How to Contribute

1. **Fork this repository** to your GitHub account.
2. Create a new branch with a descriptive name:

   ```bash
   git checkout -b feature-add-new-lab
   ```
3. Make your changes (add comments, fix bugs, or create new labs).
4. Commit and push your changes:

   ```bash
   git add .
   git commit -m "Added a new mini-project: BMI calculator"
   git push origin feature-add-new-lab
   ```
5. Open a **Pull Request (PR)** from your forked branch to this main repo.

### 🧩 Guidelines

* Keep code **clear and readable** — follow the **Inputs → Storage → Processing → Output** model.
* Include a short docstring at the top of each file with your name and the date.
* Test your program locally or via Binder before submitting.
* Use meaningful variable names and include at least 2–3 inline comments explaining key logic.

---

## 👩‍🏫 Designed By

**Dr. I. K Nti**
Assistant Professor, School of Information Technology
University of Cincinnati

📧 [ntiik@ucmail.us.edu](ntiik@ucmail.us.edu)
🌐 [Google Scholar]([https://researchdirectory.uc.edu/p/ntious](https://scholar.google.com/citations?user=eMCHVxcAAAAJ&hl=en))

---

## 📝 License

This repository is intended for **educational use**.
All materials © 2025 — provided for student learning, practice, and open collaboration.

---

