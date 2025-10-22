"""
Advanced Calculator (with Memory)
Author: (I. K. NTI)    Date: 2025-10-16

Extends the simple calculator with a memory feature (M) to reuse the last result.
Inputs → Storage → Processing → Output
"""

# ---------- STORAGE ----------
last_result = None

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

OPS = {
    "A": ("Add", add),
    "S": ("Subtract", sub),
    "MUL": ("Multiply", mul),
    "D": ("Divide", div),
}

# ---------- INPUTS ----------
def get_number(prompt: str):
    global last_result
    while True:
        raw = input(prompt).strip()
        if raw.upper() == "M":
            if last_result is None:
                print("Memory empty. Enter a number.")
                continue
            return last_result
        try:
            return float(raw)
        except ValueError:
            print("Error: enter a number or 'M' to use memory.")

# ---------- PROCESSING & OUTPUT ----------
def main():
    global last_result
    print("=== Advanced Calculator (M = use last result) ===")
    while True:
        print("A=Add  S=Subtract  MUL=Multiply  D=Divide  E=Exit")
        choice = input("Choose operation: ").strip().upper()
        if choice == "E":
            print("Goodbye!")
            break
        if choice not in OPS:
            print("Invalid choice.")
            continue
        a = get_number("Enter first number (or M for memory): ")
        b = get_number("Enter second number (or M for memory): ")
        label, fn = OPS[choice]
        try:
            last_result = fn(a, b)
            print(f"Result: {last_result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
