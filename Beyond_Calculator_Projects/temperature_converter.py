"""
Temperature Converter
Author: (I. K. NTI)    Date: 2025-10-16

Converts between Celsius, Fahrenheit, and Kelvin.
Structured as: Inputs → Storage → Processing → Output
"""

# ---------- STORAGE ----------
SCALES = {"C", "F", "K"}

def to_celsius(value: float, scale: str) -> float:
    scale = scale.upper()
    if scale == "C":
        return value
    if scale == "F":
        return (value - 32) * 5/9
    if scale == "K":
        return value - 273.15
    raise ValueError("Unsupported scale. Use C, F, or K.")

def from_celsius(value_c: float, target: str) -> float:
    target = target.upper()
    if target == "C":
        return value_c
    if target == "F":
        return value_c * 9/5 + 32
    if target == "K":
        return value_c + 273.15
    raise ValueError("Unsupported target scale. Use C, F, or K.")

# ---------- INPUTS ----------
def get_value(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Error: please enter a numeric value.")

def get_scale(prompt: str) -> str:
    while True:
        s = input(prompt).strip().upper()
        if s in SCALES:
            return s
        print("Error: scale must be one of C, F, or K.")

# ---------- PROCESSING ----------
def convert(value: float, from_scale: str, to_scale: str) -> float:
    c = to_celsius(value, from_scale)
    return from_celsius(c, to_scale)

# ---------- OUTPUT ----------
def main():
    print("=== Temperature Converter (C/F/K) ===")
    v = get_value("Enter value: ")
    src = get_scale("Enter source scale (C/F/K): ")
    dst = get_scale("Enter target scale (C/F/K): ")
    try:
        result = convert(v, src, dst)
        print(f"Result: {v}°{src} → {result:.2f}°{dst}")
    except Exception as e:
        print(f"Conversion error: {e}")

if __name__ == "__main__":
    main()
