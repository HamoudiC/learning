r"""LEVEL 7 · Integrals   (MTH 112: weeks 10-12)
Run:  python ladder\level_07_integrals.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")
u = symbols("u")


# ─── 1 · DO · integrating ───────────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → integrating;  01_basics.txt → exact numbers

square = x**2
recip = 1/x
grow = exp(2*x)
wave = sin(x)

#   1a. An antiderivative of square.
# your code here

#   1b. The integral of square from 0 to 3.
# your code here

#   1c. An antiderivative of recip.
# your code here

#   1d. An antiderivative of grow.
# your code here

#   1e. The integral of wave from 0 to π.
# your code here


# ─── 2 · DO · to infinity, and decimals ─────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → integrating

tail = 1/x**2
harmonic = 1/x
bell = exp(-x**2)

#   2a. The integral of tail from 1 to infinity.
# your code here

#   2b. The integral of harmonic from 1 to infinity.
# your code here

#   2c. The integral of bell from 0 to 1, as a decimal with 4 significant digits.
# your code here


# ─── 3 · DO · substitution, step by step ────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → integrating;  05_derivatives.txt → differentiating;  01_basics.txt → values and decimals

inner = x**2
expr = 2*x*cos(x**2)

#   3a. expr divided by the derivative of inner, then with inner replaced by u.
# your code here

#   3b. An antiderivative of expr, worked out straight away.
# your code here


# ─── 4 · DO · Riemann sums ──────────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → adding up strips, integrating;  00_python_basics.txt → loops

f = x**2
a, b, strips = 0, 2, 4

#   4a. The width of each strip, exact.
# your code here

#   4b. The left Riemann sum (each strip as tall as f at its left end).
# your code here

#   4c. The right Riemann sum.
# your code here

#   4d. The exact integral of f from a to b.
# your code here


# ─── 5 · WRITE · is_antiderivative ──────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating;  02_algebra.txt → tidying;  01_basics.txt → comparing
#   Gives back True if F' = f (any + C is fine), else False.
#   F, f: two expressions in x

def is_antiderivative(F, f):
    pass  # your code here


# ─── 6 · WRITE · average_value ──────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → integrating;  01_basics.txt → exact numbers
#   Gives back the average value of f on [a, b]: 1/(b - a) × the integral from a to b, exact.
#   f: an expression in x    a, b: the interval

def average_value(f, a, b):
    pass  # your code here


# ─── 7 · WRITE · riemann_sum ────────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → adding up strips;  00_python_basics.txt → loops, checks
#   Gives back the Riemann sum, exact, with each strip as tall as f at its "left", "right" or "mid" point.
#   f: an expression in x    a, b: the interval    strips: how many strips    kind: "left", "right" or "mid"

def riemann_sum(f, a, b, strips, kind):
    pass  # your code here


# ─── 8 · WRITE · area_between ───────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → sets of answers, equations;  07_integrals.txt → integrating;  04_functions_and_limits.txt → functions;  00_python_basics.txt → loops, lists, tuples, dicts, numbers
#   Gives back the total area enclosed between y = f and y = g, from their first crossing to their last.
#   f, g: two curves that cross at least twice

def area_between(f, g):
    pass  # your code here


# ─── 9 · FIX · definite ─────────────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → integrating
#   Should give back the integral of f from a to b, as F(b) - F(a). It comes out negative: fix it.

def definite(f, a, b):
    F = integrate(f, x)
    return F.subs(x, a) - F.subs(x, b)


if __name__ == "__main__":
    import check
    check.level(globals())
