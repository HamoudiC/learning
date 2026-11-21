r"""LEVEL 10 · Differential equations
Run:  python ladder\level_10_differential_equations.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, t = symbols("x t")
y = Function("y")
C1, C2 = symbols("C1 C2")


# ─── 1 · DO · solving ───────────────────────────────────────────────────────────────────────────────
#   Bags: 10_differential_equations.txt → writing one, solving

growth = Eq(y(x).diff(x), 2*y(x))
ramp = Eq(y(x).diff(x), x)
spring = Eq(y(x).diff(x, 2) + y(x), 0)
guess = Eq(y(x), C1*exp(2*x))

#   1a. growth solved for y(x).
# your code here

#   1b. Just the right side of growth's solution.
# your code here

#   1c. growth solved with y(0) = 3.
# your code here

#   1d. ramp solved for y(x).
# your code here

#   1e. spring solved for y(x).
# your code here

#   1f. Whether guess really solves growth (the check's result).
# your code here


# ─── 2 · WRITE · general_solution ───────────────────────────────────────────────────────────────────
#   Bags: 10_differential_equations.txt → writing one, solving
#   Gives back the right side of the general solution of  y' = right.
#   right: an expression in x and y(x)

def general_solution(right):
    pass  # your code here


# ─── 3 · WRITE · with_start ─────────────────────────────────────────────────────────────────────────
#   Bags: 10_differential_equations.txt → solving
#   Gives back the right side of the solution of  y' = right  with y(0) = start.
#   right: an expression in x and y(x)    start: the value of y(0)

def with_start(right, start):
    pass  # your code here


# ─── 4 · WRITE · cooling ────────────────────────────────────────────────────────────────────────────
#   Bags: 10_differential_equations.txt → writing one, solving;  01_basics.txt → values and decimals
#   Gives back the temperature at time `when`, from  T' = -k·(T - room)  with T(0) = start_temp. Exact.
#   start_temp, room: temperatures    k: how fast it cools    when: the time

def cooling(start_temp, room, k, when):
    pass  # your code here


# ─── 5 · FIX · solve_growth ─────────────────────────────────────────────────────────────────────────
#   Bags: 10_differential_equations.txt → writing one, solving
#   Should give back the right side of the solution of  y' = rate · y. It crashes: fix it.

def solve_growth(rate):
    return dsolve(Eq(diff(y, x), rate * y), y)


if __name__ == "__main__":
    import check
    check.level(globals())
