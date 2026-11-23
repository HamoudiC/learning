r"""LEVEL 3 · Solving equations and inequalities
Run:  python ladder\level_03_solving.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · solve ─────────────────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations

line = Eq(3*x, 12)
square = x**2 - 9
no_real = x**2 + 4
irrational = x**2 - 2

#   1a. The answers of line, as a list.
# your code here

#   1b. The one answer of line on its own (not in a list).
# your code here

#   1c. The answers of square = 0.
# your code here

#   1d. The answers of no_real = 0 (they're complex).
# your code here

#   1e. The answers of irrational = 0.
# your code here


# ─── 2 · DO · two letters ───────────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations

pair = [x + y - 5, x - y - 1]
rectangle = x*y - 6

#   2a. pair solved for x and y.
# your code here

#   2b. Just the x of the answer to pair.
# your code here

#   2c. rectangle = 0 solved for y.
# your code here

#   2d. pair solved as straight-line equations (a set of tuples).
# your code here


# ─── 3 · DO · sets of answers ───────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → sets of answers

square = x**2 - 9
no_real = x**2 + 4
wave = sin(x)

#   3a. Every answer of square = 0, as a set.
# your code here

#   3b. The REAL answers of no_real = 0.
# your code here

#   3c. The answers of wave = 0 between 0 and 2π.
# your code here

#   3d. Whether 3 is an answer of square = 0.
# your code here


# ─── 4 · DO · inequalities ──────────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → inequalities and intervals

small = x**2 < 4
big = x**2 >= 4
rising = 2*x - 6 > 0

#   4a. The real x where small is true.
# your code here

#   4b. The real x where big is true.
# your code here

#   4c. The real x where rising is true.
# your code here


# ─── 5 · DO · decimal answers ───────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations;  01_basics.txt → values and decimals

loop = cos(x) - x
cubic = x**3 - 2*x - 5

#   5a. The answer of loop = 0 near 1, as a decimal with 4 significant digits.
# your code here

#   5b. The answer of cubic = 0 near 2, as a decimal with 4 significant digits.
# your code here


# ─── 6 · WRITE · solve_linear ───────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations
#   Gives back the x that makes  a·x + b = c  true, exact.
#   a, b, c: whole numbers (a is never 0)

def solve_linear(a, b, c):
    pass  # your code here


# ─── 7 · WRITE · real_roots_of ──────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → sets of answers
#   Gives back a sorted list of the real x where expr = 0 ([] if none).
#   expr: an expression in x

def real_roots_of(expr):
    pass  # your code here


# ─── 8 · WRITE · crossing_points ────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → sets of answers, equations;  01_basics.txt → values and decimals;  00_python_basics.txt → loops, lists, tuples, dicts
#   Gives back a list of the (x, y) points where y = f and y = g cross, smallest x first.
#   f, g: two expressions in x

def crossing_points(f, g):
    pass  # your code here


# ─── 9 · WRITE · where_positive ─────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → inequalities and intervals
#   Gives back the set of real x where expr > 0.
#   expr: an expression in x

def where_positive(expr):
    pass  # your code here


# ─── 10 · FIX · x_of_solution ───────────────────────────────────────────────────────────────────────
#   Bags: 03_solving.txt → equations
#   Should give back just the x of the answer to two equations in x and y. It crashes: fix it.

def x_of_solution(first, second):
    answer = solve([first, second], [x, y])
    return answer[0]


if __name__ == "__main__":
    import check
    check.level(globals())
