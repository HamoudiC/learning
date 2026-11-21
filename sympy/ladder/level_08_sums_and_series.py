r"""LEVEL 8 · Sums and series
Run:  python ladder\level_08_sums_and_series.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")
n = symbols("n", positive=True, integer=True)
k = symbols("k", integer=True)


# ─── 1 · DO · sums ──────────────────────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → sums;  02_algebra.txt → multiplying out and factoring

term = k
odd = 2*k + 1
halving = Rational(1, 2)**k
harmonic = 1/k
basel = 1/k**2

#   1a. term added up for k = 1 to 10.
# your code here

#   1b. odd added up for k = 0 to 4.
# your code here

#   1c. term added up for k = 1 to n, as a factored formula.
# your code here

#   1d. halving added up for k = 0 to infinity.
# your code here

#   1e. harmonic added up for k = 1 to infinity.
# your code here

#   1f. basel added up for k = 1 to infinity.
# your code here


# ─── 2 · DO · series ────────────────────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → series

grow = exp(x)
wave = sin(x)
geometric = 1/(1 - x)

#   2a. The series of grow around 0, up to but not including x**4.
# your code here

#   2b. The same, without the O(...) part.
# your code here

#   2c. The Taylor polynomial of wave around 0, up to and including x**5, without the O(...) part.
# your code here

#   2d. The series of geometric around 0, up to but not including x**4.
# your code here


# ─── 3 · WRITE · sum_of ─────────────────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → sums
#   Gives back the total of expr for k = start up to end (end included).
#   expr: an expression in k    start: a whole number    end: a whole number, n, or oo

def sum_of(expr, start, end):
    pass  # your code here


# ─── 4 · WRITE · partial_sums ───────────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → sums;  00_python_basics.txt → loops, lists, tuples, dicts
#   Gives back a list [S1, S2, ..., S_count]: the totals from k = 1 up to 1, 2, ..., count.
#   expr: an expression in k    count: how many

def partial_sums(expr, count):
    pass  # your code here


# ─── 5 · WRITE · taylor_polynomial ──────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → series
#   Gives back the Taylor polynomial of f around a, up to AND including (x - a)**degree, without O(...).
#   f: an expression in x    a: the centre    degree: the highest power

def taylor_polynomial(f, a, degree):
    pass  # your code here


# ─── 6 · WRITE · approximate ────────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → formulas, differentiating;  01_basics.txt → values and decimals
#   Gives back the linear approximation of f(value): the tangent line at a, at x = value. Exact.
#   f: an expression in x    a: an easy point    value: a number near a

def approximate(f, a, value):
    pass  # your code here


# ─── 7 · FIX · geometric_total ──────────────────────────────────────────────────────────────────────
#   Bags: 08_sums_and_series.txt → sums
#   Should give back 1 + ratio + ratio**2 + ... added up FOREVER. It stops too early: fix it.

def geometric_total(ratio):
    return summation(ratio**k, (k, 0, 100))


if __name__ == "__main__":
    import check
    check.level(globals())
