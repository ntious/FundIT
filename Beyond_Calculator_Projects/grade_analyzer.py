"""
Grade Analyzer
Author: (Your Name)    Date: 2025-10-16

Computes averages and letter grades. Can be extended to read/write files.
Inputs → Storage → Processing → Output
"""

# ---------- STORAGE ----------
def letter_grade(avg: float) -> str:
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

# ---------- INPUTS ----------
def get_scores():
    scores = []
    print("Enter scores (0-100). Blank line to finish.")
    while True:
        raw = input("Score: ").strip()
        if raw == "":
            break
        try:
            val = float(raw)
            if 0 <= val <= 100:
                scores.append(val)
            else:
                print("Enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a numeric score.")
    return scores

# ---------- PROCESSING ----------
def analyze(scores):
    if not scores:
        return 0.0, 0.0, 0.0, "N/A"
    avg = sum(scores) / len(scores)
    high = max(scores)
    low = min(scores)
    grade = letter_grade(avg)
    return avg, high, low, grade

# ---------- OUTPUT ----------
def main():
    print("=== Grade Analyzer ===")
    scores = get_scores()
    avg, high, low, grade = analyze(scores)
    print(f"Count: {len(scores)}")
    print(f"Average: {avg:.2f}  High: {high:.2f}  Low: {low:.2f}")
    print(f"Letter Grade (avg): {grade}")

if __name__ == "__main__":
    main()
