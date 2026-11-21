r"""LEVEL 4 · Functions and limits   (MTH 112: weeks 1-3)
Run:  python ladder\level_04_functions_and_limits.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · functions ─────────────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → functions;  02_algebra.txt → multiplying out and factoring
#   Bags: 03_solving.txt → equations

f = x**2 + 1
g = 2*x - 3

#   1a. f at x = 3.
# your code here

#   1b. f(g(x)).
# your code here

#   1c. g(f(x)).
# your code here

#   1d. f(g(x)) multiplied out.
# your code here

#   1e. The answers for x when y = g (a list, in terms of y).
# your code here


# ─── 2 · DO · limits ────────────────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → limits;  01_basics.txt → values and decimals

sinc = sin(x)/x
hole = (x**2 - 4)/(x - 2)
ratio = (3*x**2 + 1)/(x**2 - 5)
decay = exp(-x)

#   2a. The limit of sinc as x goes to 0.
# your code here

#   2b. The limit of hole as x goes to 2.
# your code here

#   2c. The VALUE of hole at x = 2 (swap it in).
# your code here

#   2d. The limit of ratio as x goes to infinity.
# your code here

#   2e. The limit of decay as x goes to infinity.
# your code here


# ─── 3 · DO · one side or both ──────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → limits

recip = 1/x
sign = abs(x)/x
step = floor(x)

#   3a. The limit of recip as x goes to 0 from the right.
# your code here

#   3b. The limit of recip as x goes to 0 from the left.
# your code here

#   3c. The limit of recip as x goes to 0 from both sides.
# your code here

#   3d. The limit of sign as x goes to 0 from the right.
# your code here

#   3e. The limit of sign as x goes to 0 from the left.
# your code here

#   3f. The limit of step as x goes to 1 from the left.
# your code here


# ─── 4 · WRITE · compose ────────────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → functions
#   Gives back f(g(x)).
#   f, g: two expressions in x

def compose(f, g):
    pass  # your code here


# ─── 5 · WRITE · inverse_of ─────────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations;  04_functions_and_limits.txt → functions
#   Gives back the inverse function as an expression in x (the first answer if there are several).
#   f: a one-to-one function of x

def inverse_of(f):
    pass  # your code here


# ─── 6 · WRITE · two_sided_limit ────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → limits
#   Gives back the limit as x → a if the left and right limits are the same, otherwise None.
#   expr: an expression in x    a: the number x goes to

def two_sided_limit(expr, a):
    pass  # your code here


# ─── 7 · WRITE · is_continuous_at ───────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → limits, functions
#   Gives back True if the left limit, the right limit and the value at a are all the same.
#   expr: an expression in x    a: a number

def is_continuous_at(expr, a):
    pass  # your code here


# ─── 8 · FIX · value_at_3 ───────────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → functions
#   Should give back f(3) for an expression f in x. It crashes: fix it.

def value_at_3(f):
    return f(3)


# ─── 9 · FIX · limit_both_sides ─────────────────────────────────────────────────────────────────────
#   Bags: 04_functions_and_limits.txt → limits
#   Should give back the limit of expr as x → a from BOTH sides. It only looks from one: fix it.

def limit_both_sides(expr, a):
    return limit(expr, x, a)


if __name__ == "__main__":
    import check
    check.level(globals())
