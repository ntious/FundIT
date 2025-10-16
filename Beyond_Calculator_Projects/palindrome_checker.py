"""
Palindrome Checker
Author: (Your Name)    Date: 2025-10-16

Checks if text is a palindrome (ignores spaces/punctuation/case).
Inputs → Storage → Processing → Output
"""

import string

# ---------- PROCESSING ----------
def clean_text(s: str) -> str:
    allowed = set(string.ascii_letters + string.digits)
    return "".join(ch.lower() for ch in s if ch in allowed)

def is_palindrome(s: str) -> bool:
    c = clean_text(s)
    return c == c[::-1]

# ---------- INPUTS / OUTPUT ----------
def main():
    print("=== Palindrome Checker ===")
    text = input("Enter a word or phrase: ")
    if is_palindrome(text):
        print("Result: It's a palindrome!")
    else:
        print("Result: Not a palindrome.")

if __name__ == "__main__":
    main()
