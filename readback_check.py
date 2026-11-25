"""Tiny read-back checker: compares the numbers in an ATC instruction with the pilot's read-back.

Usage: python readback_check.py "DLH4AB, descend flight level 110, squawk 2741" "Descend FL100, squawk 2741, DLH4AB"
"""
import re
import sys

WORDS = {"zero": "0", "one": "1", "two": "2", "three": "3", "tree": "3", "four": "4", "fower": "4",
         "five": "5", "fife": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "niner": "9",
         "decimal": ".", "point": ".", "hundred": "00", "thousand": "000"}

PATTERNS = {
    "squawk": r"squawk\s+(\d{4})",
    "level": r"(?:flight level|fl)\s*(\d{2,3})|(?:altitude|climb|descend)\D{0,12}?(\d{3,5})\s*(?:ft|feet)",
    "heading": r"heading\s+(\d{3})",
    "speed": r"(?:speed|reduce|increase)\D{0,10}?(\d{3})\s*(?:knots|kt)",
    "frequency": r"(1[1-3]\d\.\d{1,3})",
    "altimeter": r"(?:qnh|qfe|altimeter)\s+(\d{3,4})",
    "runway": r"runway\s+(\d{1,2}[lrc]?)",
}


def normalize(text):
    t = text.lower().replace(",", " ")
    # "one two one decimal five" -> "121.5"; spoken digits are joined
    tokens = [WORDS.get(w, w) for w in t.split()]
    out = []
    for tok in tokens:
        if out and re.fullmatch(r"[\d.]+", tok) and re.fullmatch(r"[\d.]+", out[-1]):
            out[-1] += tok
        else:
            out.append(tok)
    return " ".join(out)


def extract(text):
    t = normalize(text)
    found = {}
    for key, pat in PATTERNS.items():
        vals = [next(g for g in m.groups() if g) for m in re.finditer(pat, t)]
        if vals:
            found[key] = vals
    return found


def check(instruction, readback):
    """Returns a list of problems; empty list = numbers read back correctly."""
    want, got = extract(instruction), extract(readback)
    problems = []
    for key, vals in want.items():
        for v in vals:
            if v not in got.get(key, []):
                problems.append(f"{key}: expected {v}, got {', '.join(got.get(key, [])) or 'nothing'}")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    issues = check(sys.argv[1], sys.argv[2])
    print("\n".join(issues) if issues else "Read-back OK")
