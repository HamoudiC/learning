r"""LEVEL 6 · Max, min, shape, optimisation   (MTH 112: weeks 7, 9)
Run:  python ladder\level_06_using_derivatives.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · critical points and shape ─────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points, shape of the graph;  05_derivatives.txt → differentiating

f = x**3 - 3*x

#   1a. f'(x).
# your code here

#   1b. The x where f'(x) = 0, as a list.
# your code here

#   1c. f''(x).
# your code here

#   1d. f'' at x = 1.
# your code here

#   1e. The real x where f is increasing.
# your code here

#   1f. The real x where f is concave up.
# your code here


# ─── 2 · DO · biggest and smallest ──────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → biggest and smallest;  01_basics.txt → values and decimals

f = x**3 - 3*x

#   2a. f at x = -2, -1, 1 and 3, as a list.
# your code here

#   2b. The biggest value of f on [-2, 3].
# your code here

#   2c. The smallest value of f on [-2, 3].
# your code here


# ─── 3 · DO · positive letters ──────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → biggest and smallest

w = symbols("w", positive=True)
side_area = w**2 - 4

#   3a. The answers of side_area = 0 for w.
# your code here


# ─── 4 · WRITE · critical_points ────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points;  03_solving.txt → sets of answers
#   Gives back a sorted list of the real x where f'(x) = 0 ([] if none).
#   f: an expression in x

def critical_points(f):
    pass  # your code here


# ─── 5 · WRITE · classify ───────────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → shape of the graph
#   Gives back "max", "min" or "unknown", from the second derivative test.
#   f: an expression in x    c: a critical point of f

def classify(f, c):
    pass  # your code here


# ─── 6 · WRITE · absolute_extremes ──────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points, biggest and smallest
#   Gives back (smallest value, biggest value) of f on [a, b]: try the critical points inside AND both ends.
#   f: an expression in x    a, b: the ends of the interval

def absolute_extremes(f, a, b):
    pass  # your code here


# ─── 7 · WRITE · best_rectangle ─────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points, biggest and smallest;  01_basics.txt → exact numbers
#   Gives back (width, height, area) of the rectangle with this perimeter and the BIGGEST area, exact.
#   perimeter: a whole number

def best_rectangle(perimeter):
    pass  # your code here


# ─── 8 · WRITE · open_box ───────────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points
#   Gives back the corner cut c that gives the biggest box: volume = c·(side - 2c)², with 0 < c < side/2.
#   side: the side of a square sheet of card

def open_box(side):
    pass  # your code here


# ─── 9 · FIX · increasing_on ────────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → shape of the graph
#   Should give back the set of real x where f is increasing. It doesn't solve it: fix it.

def increasing_on(f):
    return solveset(diff(f, x) > 0, x)


if __name__ == "__main__":
    import check
    check.level(globals())
