"""
Password Strength Checker
Author: (Your Name)    Date: 2025-10-16

Validates password complexity using simple rules.
Inputs → Storage → Processing → Output
"""

import re

# ---------- STORAGE ----------
RULES = [
    ("Length ≥ 8", lambda s: len(s) >= 8),
    ("Has uppercase", lambda s: any(c.isupper() for c in s)),
    ("Has lowercase", lambda s: any(c.islower() for c in s)),
    ("Has digit", lambda s: any(c.isdigit() for c in s)),
    ("Has symbol", lambda s: re.search(r"[^A-Za-z0-9]", s) is not None),
]

# ---------- PROCESSING ----------
def evaluate(pw: str):
    results = [(desc, check(pw)) for desc, check in RULES]
    score = sum(1 for _, ok in results if ok)
    return score, results

# ---------- INPUTS / OUTPUT ----------
def main():
    print("=== Password Strength Checker ===")
    pw = input("Enter a password to evaluate: ")
    score, results = evaluate(pw)
    print(f"Score: {score} / {len(RULES)}")
    for desc, ok in results:
        print(f" - {desc}: {'OK' if ok else 'Missing'}")

if __name__ == "__main__":
    main()
