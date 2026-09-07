#!/usr/bin/env python3
"""Finite boundary table for Dynamic Regular Witnesses.

This is implementation evidence only. It does not replace the proofs.
"""

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent


def cdiv(a: int, b: int) -> int:
    return (a + b - 1) // b


def upper(n: int, P: int) -> int:
    return 2 + cdiv(n - 1, P)


def quartic_lower(n: int, P: int):
    if n < 15:
        return None
    return 2 + cdiv(n - 13, P)


def cubic_lower(n: int, P: int):
    if n < 12 or n % 2:
        return None
    return 2 + cdiv(n - 10, P)


def main() -> None:
    path = OUT / "dynamic_regular_finite_table.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "P", "quartic_lower", "cubic_lower", "best_lower", "upper", "gap", "three_state_exact"])
        for n in range(12, 61):
            for P in range(1, 61):
                q = quartic_lower(n, P)
                c = cubic_lower(n, P)
                available = [x for x in (q, c) if x is not None]
                lo = max(available) if available else ""
                hi = upper(n, P)
                if available:
                    assert lo <= hi
                    gap = hi - lo
                else:
                    gap = ""
                exact_three = int(n >= 4 and P >= n - 1)
                assert (hi == 3) == bool(exact_three)
                w.writerow([n, P, q if q is not None else "", c if c is not None else "", lo, hi, gap, exact_three])
    print("PASS_DYNAMIC_REGULAR_FINITE_AUDIT")
    print(path.name)


if __name__ == "__main__":
    main()
