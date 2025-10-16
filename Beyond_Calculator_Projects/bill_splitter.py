"""
Bill Splitter
Author: (Your Name)    Date: 2025-10-16

Compute per-person cost including tip and rounding.
Inputs → Storage → Processing → Output
"""

# ---------- INPUTS ----------
def get_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def get_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val > 0:
                return val
            print("Enter a positive integer.")
        except ValueError:
            print("Please enter a whole number.")

# ---------- PROCESSING ----------
def compute_split(total: float, tip_percent: float, people: int) -> float:
    tip = total * (tip_percent / 100.0)
    grand = total + tip
    return grand / people

# ---------- OUTPUT ----------
def main():
    print("=== Bill Splitter ===")
    total = get_float("Total bill amount: $")
    tip = get_float("Tip percentage (e.g., 15 for 15%): ")
    people = get_int("Number of people: ")
    per = compute_split(total, tip, people)
    print(f"Each person pays: ${per:.2f}")

if __name__ == "__main__":
    main()
