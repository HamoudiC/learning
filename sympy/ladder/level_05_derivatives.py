r"""LEVEL 5 · Derivatives   (MTH 112: weeks 4-6)
Run:  python ladder\level_05_derivatives.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · derivatives ───────────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating

cube = x**3
poly = 5*x**2 - 3*x + 7
grow = exp(2*x)
natural_log = log(x)
root = sqrt(x)

#   1a. The derivative of cube.
# your code here

#   1b. The second derivative of cube.
# your code here

#   1c. The derivative of poly.
# your code here

#   1d. The derivative of grow.
# your code here

#   1e. The derivative of natural_log.
# your code here

#   1f. The derivative of root.
# your code here


# ─── 2 · DO · the rules ─────────────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating;  02_algebra.txt → tidying

product = x*sin(x)
chain = sin(x**2)
quotient = (x + 1)/(x - 1)

#   2a. The derivative of product.
# your code here

#   2b. The derivative of chain.
# your code here

#   2c. The derivative of quotient.
# your code here

#   2d. The derivative of quotient, simplified.
# your code here


# ─── 3 · DO · partial, and at a point ───────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating

surface = x**2*y
cube = x**3

#   3a. The derivative of surface with respect to y.
# your code here

#   3b. The derivative of surface with respect to x.
# your code here

#   3c. The slope of cube at x = 2.
# your code here


# ─── 4 · DO · implicit ──────────────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → implicit

circle = x**2 + y**2 - 25
hyperbola = x*y - 1

#   4a. dy/dx for circle = 0.
# your code here

#   4b. dy/dx for circle = 0 at the point (3, 4).
# your code here

#   4c. dy/dx for hyperbola = 0.
# your code here


# ─── 5 · WRITE · slope_at ───────────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating
#   Gives back f'(a), exact.
#   f: an expression in x    a: a number

def slope_at(f, a):
    pass  # your code here


# ─── 6 · WRITE · tangent_line ───────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating, formulas
#   Gives back the tangent line to y = f at x = a, as an expression in x.
#   f: an expression in x    a: where the line touches

def tangent_line(f, a):
    pass  # your code here


# ─── 7 · WRITE · derivative_by_definition ───────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → formulas;  04_functions_and_limits.txt → limits, functions;  01_basics.txt → symbols and expressions
#   Gives back f'(x) worked out with the limit definition (not diff).
#   f: an expression in x

def derivative_by_definition(f):
    pass  # your code here


# ─── 8 · WRITE · implicit_slope ─────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → implicit
#   Gives back dy/dx at the point (a, b).
#   equation: an expression in x and y that equals 0    a, b: a point on the curve

def implicit_slope(equation, a, b):
    pass  # your code here


# ─── 9 · FIX · second_derivative ────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating
#   Should give back f''(x). It gives something else: fix it.

def second_derivative(f):
    return diff(f, x)**2


# ─── 10 · FIX · rate_of_change ──────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating
#   Should give back the derivative with t as the variable. It crashes when there's an x too: fix it.

def rate_of_change(expr):
    return diff(expr)


if __name__ == "__main__":
    import check
    check.level(globals())
