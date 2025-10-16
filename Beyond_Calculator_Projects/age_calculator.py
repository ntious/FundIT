"""
Age / Days-to-Birthday Calculator
Author: (Your Name)    Date: 2025-10-16

Uses datetime for age and days-till-next-birthday.
Inputs → Storage → Processing → Output
"""

from datetime import date

# ---------- INPUTS ----------
def get_date():
    while True:
        raw = input("Enter your birth date (YYYY-MM-DD): ").strip()
        try:
            y, m, d = map(int, raw.split("-"))
            return date(y, m, d)
        except Exception:
            print("Invalid format. Use YYYY-MM-DD.")

# ---------- PROCESSING ----------
def compute_age(bday: date, today: date) -> int:
    years = today.year - bday.year
    if (today.month, today.day) < (bday.month, bday.day):
        years -= 1
    return years

def days_until_next_birthday(bday: date, today: date) -> int:
    next_bd = date(today.year, bday.month, bday.day)
    if next_bd < today:
        next_bd = date(today.year + 1, bday.month, bday.day)
    return (next_bd - today).days

# ---------- OUTPUT ----------
def main():
    print("=== Age / Days-to-Birthday ===")
    b = get_date()
    t = date.today()
    age = compute_age(b, t)
    days = days_until_next_birthday(b, t)
    print(f"Current age: {age} years")
    print(f"Days until next birthday: {days}")

if __name__ == "__main__":
    main()
