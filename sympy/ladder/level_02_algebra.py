r"""LEVEL 2 · Algebra: choosing the form
Run:  python ladder\level_02_algebra.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")
a, b = symbols("a b")
p, q = symbols("p q", positive=True)


# ─── 1 · DO · multiplying out and factoring ─────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → multiplying out and factoring

product = (x + 2)*(x - 3)
quadratic = x**2 - x - 6
cubic = x**3 - x
squares = x**2 - 9

#   1a. product multiplied out.
# your code here

#   1b. quadratic in brackets.
# your code here

#   1c. cubic in brackets.
# your code here

#   1d. squares in brackets.
# your code here


# ─── 2 · DO · tidying ───────────────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → tidying

fraction_one = (x**2 - 1)/(x - 1)
messy = a*x + b*x + a
two_fractions = 1/x + 1/(x + 1)

#   2a. fraction_one with the common factor crossed out.
# your code here

#   2b. messy grouped by x.
# your code here

#   2c. two_fractions as one fraction.
# your code here


# ─── 3 · DO · trig ──────────────────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → trig, tidying

identity = sin(x)**2 + cos(x)**2
double = sin(2*x)
ratio = sin(x)/cos(x)

#   3a. identity shortened with the trig rules.
# your code here

#   3b. double opened up.
# your code here

#   3c. ratio simplified.
# your code here


# ─── 4 · DO · logs ──────────────────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → logs and powers
#   (p and q are positive; x and y could be anything.)

product_log = log(p*q)
power_log = log(p**3)
plain_log = log(x*y)

#   4a. product_log split into two logs.
# your code here

#   4b. power_log written without the power inside.
# your code here

#   4c. plain_log split into two logs, even though x and y could be anything.
# your code here


# ─── 5 · DO · taking it apart ───────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → taking it apart, multiplying out and factoring

poly = 3*x**2 + 2*x + 1
square = (x + 1)**2

#   5a. The highest power of x in poly.
# your code here

#   5b. The number in front of x**2 in poly.
# your code here

#   5c. The number in front of x**2 in square.
# your code here


# ─── 6 · WRITE · expanded_and_factored ──────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → multiplying out and factoring
#   Gives back a tuple: (the multiplied-out form, the factored form). The tests check the FORM.
#   expr: a polynomial in x

def expanded_and_factored(expr):
    pass  # your code here


# ─── 7 · WRITE · quadratic_coefficients ─────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → taking it apart, multiplying out and factoring
#   Gives back a list [a, b, c]: the numbers in front of x**2 and x, and the number on its own.
#   expr: a polynomial in x of degree 2 or less, in any form

def quadratic_coefficients(expr):
    pass  # your code here


# ─── 8 · WRITE · is_identity ────────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → tidying;  01_basics.txt → comparing
#   Gives back True if left and right are equal for every x, False if not.
#   left, right: two expressions in x

def is_identity(left, right):
    pass  # your code here


# ─── 9 · FIX · split_log ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_algebra.txt → logs and powers
#   Should give back log(inside) split into simple logs, for plain x and y. Nothing gets split: fix it.

def split_log(inside):
    return expand_log(log(inside))


if __name__ == "__main__":
    import check
    check.level(globals())
