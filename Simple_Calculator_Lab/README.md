# Fundamentals of Information Technology
# 🧮 In‑Class Lab: Build a Simple Calculator in Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ntious/FundIT/HEAD)

Binder opens a temporary Jupyter environment for this repository. To run this
interactive command-line program there, open a Jupyter terminal and run
`python Simple_Calculator_Lab/calculator.py`. You can also run it locally.
Binder does not save your work after the session ends.


## 🎯 Objective
In this lab, you’ll apply core programming concepts to build a **simple but fault‑tolerant calculator** that can handle user input gracefully.  
You’ll demonstrate your understanding of **variables, input/output, conditional statements, functions, loops, and robust error handling**.

---

## 🧠 Task Requirements
Write a Python program that acts as a **continuous, basic calculator**.  
Your program **must** meet the following structural and functional requirements:

### 1️⃣ Structural Design (Functions)
- Define **four separate functions**: `add`, `subtract`, `multiply`, and `divide`.
- Each function must accept two numeric arguments and return the computed result.
- Use a **`main()` function** (or similar structure) to organize the overall flow — handling the menu display and user interaction.

### 2️⃣ Application Flow (Looping)
- Wrap the calculator logic in a **`while` loop** so the user can perform multiple calculations without restarting the program.
- Include an option (`E` or `Q`) in the menu to **gracefully exit** the program.
- The calculator should keep running until the user explicitly chooses to exit.

### 3️⃣ Menu and Input
Present a clear menu of available operations:
```
A = Addition
S = Subtraction
M = Multiplication
D = Division
E = Exit (or Q = Quit)
```
Prompt the user to choose an operation and enter **two numbers**.

### 4️⃣ Error Handling and Validation
- **Invalid Choice:** If the user enters an invalid option (e.g., `Z`), display an error message and prompt again.
- **Division by Zero:** Gracefully handle division by zero by displaying an informative message instead of crashing.
- **Non‑Numeric Input:** Use `try...except` to catch a `ValueError` if the user enters text or a symbol instead of a number (e.g., typing `"hello"` instead of `10`). Display a clear error and re‑prompt for input.

### 5️⃣ Output
- Display the **final result** clearly, such as:
  ```
  Result: 15.0
  ```
- After showing the result, redisplay the main menu for the next operation.

---

## 💻 Example Interaction
```
===== Simple Python Calculator =====
A - Add
S - Subtract
M - Multiply
D - Divide
E - Exit
Choose an operation: A
Enter first number: 10
Enter second number: 5
Result: 15.0

Choose an operation: D
Enter first number: 12
Enter second number: 0
Error: Cannot divide by zero. Please try again.

Choose an operation: Q
Exiting program. Goodbye!
```

---

## 🏗️ Program Architecture (Mimicking a Computer System)

To reinforce systems thinking, the program is structured into the classic four stages:

1. **Inputs** — Collect user choices and numbers.
2. **Storage** — Hold values and state (variables, constants, and a mapping of menu choices to operation functions).
3. **Processing** — Run the selected operation using functions with validation and error handling.
4. **Output** — Display results or helpful error messages and show the menu again.

> The provided `calculator.py` includes clear section headers and comments for these four stages.

---

## ▶️ How to Run
1. Ensure you have **Python 3.8+** installed.
2. Download or clone this repository.
3. From the repository root, open a terminal and run:
   ```bash
   python Simple_Calculator_Lab/calculator.py
   ```
   If you are already in this folder, run `python calculator.py`.

### ✅ Testing Checklist
Before submitting, verify all of the following cases:
- Valid operations (**A, S, M, D**)
- Invalid choice (**e.g., `Z`**)
- Division by zero
- Non‑numeric input for numbers
- Exit command (**E or Q**)

---

## Submission evidence

Follow your instructor's requirements. A useful evidence set is the source file
and a short transcript showing a valid calculation, invalid choice,
division-by-zero handling, and exit.

---

## 🧩 File Structure
```
simple-calculator-lab/
├── README.md
├── calculator.py
└── .gitignore
```

---

## Designed by I. K. NTI
