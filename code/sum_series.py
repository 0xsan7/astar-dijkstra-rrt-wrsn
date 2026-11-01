"""Sum the series S = 1 + x + x^2 + ... + x^n using three methods.

Methods:
1) Two nested for loops (`sum_nested_loops`)
2) Single for loop (`sum_single_loop`)
3) Closed-form geometric formula (`sum_closed_form`)

Run as a script to see example outputs or provide `x` and `n` as command-line args.
"""
from __future__ import annotations
import argparse
import math
from typing import Union

Number = Union[int, float]


def sum_nested_loops(x: Number, n: int) -> float:
    """Compute S using two nested loops.

    Outer loop iterates over k=0..n. Inner loop computes x^k by repeated
    multiplication.
    """
    total = 0.0
    for k in range(n + 1):
        term = 1.0
        for _ in range(k):
            term *= x
        total += term
    return float(total)


def sum_single_loop(x: Number, n: int) -> float:
    """Compute S using a single loop and iterative term update.

    Start with term=1 and multiply by x each iteration.
    """
    total = 0.0
    term = 1.0
    for _ in range(n + 1):
        total += term
        term *= x
    return float(total)


def sum_closed_form(x: Number, n: int) -> float:
    """Closed-form geometric series sum.

    Handles the special case x == 1 where the denominator would be zero.
    """
    if x == 1:
        return float(n + 1)
    # Use math.pow for numeric stability with floats when needed
    return float((x ** (n + 1) - 1) / (x - 1))


def close_enough(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main() -> None:
    parser = argparse.ArgumentParser(description="Sum geometric series by three methods")
    parser.add_argument("x", type=float, nargs="?", help="base x (default examples used)")
    parser.add_argument("n", type=int, nargs="?", help="maximum exponent n (default examples used)")
    args = parser.parse_args()

    examples = [(2, 5), (1, 10), (1.5, 3), (0.5, 4), (-2, 3)]
    if args.x is not None and args.n is not None:
        examples = [(args.x, args.n)]

    for x, n in examples:
        a = sum_nested_loops(x, n)
        b = sum_single_loop(x, n)
        c = sum_closed_form(x, n)

        ok_ab = close_enough(a, b)
        ok_ac = close_enough(a, c)

        print(f"x={x!r}, n={n}")
        print(f"  nested loops : {a}")
        print(f"  single loop  : {b}  (matches nested: {ok_ab})")
        print(f"  closed form  : {c}  (matches nested: {ok_ac})")
        if not (ok_ab and ok_ac):
            print("  WARNING: results differ beyond tolerance")
        print()


if __name__ == "__main__":
    main()
