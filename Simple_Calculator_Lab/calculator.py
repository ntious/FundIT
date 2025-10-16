"""
In-Class Lab: Simple Calculator
Author: (Your Name)
Date: (YYYY-MM-DD)

This program demonstrates core programming concepts by implementing
a robust, menu-driven calculator. The code is intentionally organized
to mimic a computer system's four main stages:
    (1) INPUTS   – get user choices and numbers
    (2) STORAGE  – keep values/state and map choices to operations
    (3) PROCESSING – compute results using validated operations
    (4) OUTPUT   – display results or helpful error messages

Requirements covered:
- Functions: add, subtract, multiply, divide
- Looping: continuous while-loop until user exits
- Error Handling: invalid choices, non-numeric input, division by zero
"""

from typing import Callable, Dict, Tuple


# -----------------------------
# (2) STORAGE: Functions/State
# -----------------------------

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Return the quotient of a and b.
    Raises ZeroDivisionError if b == 0; caller is expected to handle gracefully.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# A mapping from menu choice to (label, function).
# This is part of STORAGE because it encodes the program's "knowledge."
OPERATIONS: Dict[str, Tuple[str, Callable[[float, float], float]]] = {
    "A": ("Add", add),
    "S": ("Subtract", subtract),
    "M": ("Multiply", multiply),
    "D": ("Divide", divide),
}


def print_menu() -> None:
    """Display the available operations. Part of OUTPUT stage (UI)."""
    print("===== Simple Python Calculator =====")
    print("A - Add")
    print("S - Subtract")
    print("M - Multiply")
    print("D - Divide")
    print("E - Exit")
    print("Q - Quit")


def get_number(prompt: str) -> float:
    """
    (1) INPUTS: Safely collect a numeric value from the user.
    Uses try/except to handle non-numeric entries and re-prompts as needed.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Error: Please enter a valid number (e.g., 10, 3.14, -2).")


def main() -> None:
    """
    Main control flow:
      - Loop until user exits (while True)
      - (1) INPUTS: get menu choice and numbers
      - (2) STORAGE: use the OPERATIONS map to resolve functions
      - (3) PROCESSING: compute result with validation
      - (4) OUTPUT: show result or clear error messages
    """
    while True:
        # (4) OUTPUT: UI - show the menu each iteration
        print_menu()

        # (1) INPUTS: read the user's menu choice
        choice = input("Choose an operation: ").strip().upper()

        # Exit path
        if choice in {"E", "Q"}:
            print("Exiting program. Goodbye!")
            break

        # Validate the choice using STORAGE (OPERATIONS map)
        if choice not in OPERATIONS:
            # (4) OUTPUT: invalid choice message
            print("Invalid choice! Please select a valid operation (A, S, M, D, E, Q).")
            continue

        # (1) INPUTS: gather operands with validation
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        # (2) STORAGE: unpack chosen operation
        op_label, op_func = OPERATIONS[choice]

        # (3) PROCESSING: perform computation with robust error handling
        try:
            result = op_func(a, b)
        except ZeroDivisionError as zde:
            # (4) OUTPUT: explain division-by-zero gracefully
            print(f"Error: {zde} Please try again.")
            continue
        except Exception as exc:
            # (4) OUTPUT: catch-all for unexpected issues (defensive programming)
            print(f"Unexpected error while computing {op_label.lower()}: {exc}")
            continue

        # (4) OUTPUT: show the successful result in a consistent format
        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
