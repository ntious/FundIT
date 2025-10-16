"""
Number Guessing Game
Author: (I. K. NTI)    Date: 2025-10-16

Random number guessing with difficulty levels.
Inputs → Storage → Processing → Output
"""

import random

# ---------- STORAGE ----------
LEVELS = {"E": 10, "M": 50, "H": 100}

# ---------- INPUTS ----------
def get_level():
    while True:
        lvl = input("Choose difficulty (E=Easy, M=Medium, H=Hard): ").strip().upper()
        if lvl in LEVELS:
            return lvl
        print("Invalid level. Choose E, M, or H.")

# ---------- PROCESSING ----------
def play(level: str):
    max_n = LEVELS[level]
    secret = random.randint(1, max_n)
    print(f"I'm thinking of a number between 1 and {max_n}.")
    attempts = 0
    while True:
        raw = input("Your guess: ").strip()
        if not raw.isdigit():
            print("Enter a whole number.")
            continue
        guess = int(raw)
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You guessed in {attempts} tries.")
            break

# ---------- OUTPUT ----------
def main():
    print("=== Number Guessing Game ===")
    lvl = get_level()
    play(lvl)

if __name__ == "__main__":
    main()
