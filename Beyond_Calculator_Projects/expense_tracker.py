"""
Expense Tracker (CSV)
Author: (Your Name)    Date: 2025-10-16

Track expenses by category and save to CSV.
Inputs → Storage → Processing → Output
"""

import csv, os
from collections import defaultdict

FILE = "expenses.csv"

# ---------- STORAGE ----------
def load_totals():
    totals = defaultdict(float)
    if os.path.exists(FILE):
        with open(FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    cat, amt = row
                    try:
                        totals[cat] += float(amt)
                    except ValueError:
                        pass
    return totals

def save_totals(totals):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for cat, amt in totals.items():
            writer.writerow([cat, f"{amt:.2f}"])

# ---------- INPUTS ----------
def get_amount(prompt="Amount: $"):
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if val >= 0:
                return val
            print("Enter a non-negative amount.")
        except ValueError:
            print("Please enter a number.")

# ---------- PROCESSING / OUTPUT ----------
def main():
    print("=== Expense Tracker (saves to expenses.csv) ===")
    totals = load_totals()
    while True:
        print("A=Add expense  L=List totals  R=Reset  E=Exit")
        choice = input("Choice: ").strip().upper()
        if choice == "E":
            save_totals(totals)
            print("Saved. Goodbye!")
            break
        elif choice == "A":
            cat = input("Category (e.g., food, travel): ").strip().lower() or "misc"
            amt = get_amount()
            totals[cat] += amt
            print(f"Added ${amt:.2f} to '{cat}'.")
        elif choice == "L":
            if not totals:
                print("No expenses yet.")
            else:
                for c, a in sorted(totals.items()):
                    print(f"{c}: ${a:.2f}")
        elif choice == "R":
            confirm = input("Type 'YES' to clear all totals: ").strip()
            if confirm == "YES":
                totals.clear()
                print("All totals cleared.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
