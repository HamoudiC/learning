r"""LEVEL 1 · Symbols, exact numbers, swapping in values
Run it after every task, from the sympy folder:   python ladder\level_01_symbols.py

  DO     Under each task, delete  # your code here  and write your code on that line.
         Use the data above the tasks. Look things up in the bags named at the top of each section.
         The FORM counts: (x + 1)**2 and x**2 + 2*x + 1 are different answers.
  WRITE  Write the function: delete  pass  and write your code. Here any equal form counts.
  FIX    The function is broken. Fix it.
  ✅ done   ❌ not right yet   ⬜ not started
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · expressions ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → symbols and expressions

#   1a. x added to itself.
# your code here

#   1b. x multiplied by itself.
# your code here

#   1c. x**2 multiplied by x**3.
# your code here

#   1d. x + 1, squared (SymPy keeps the brackets).
# your code here


# ─── 2 · DO · what an expression is built from ──────────────────────────────────────────────────────
#   Bags: 01_basics.txt → symbols and expressions

total = x + 1
product = 3*x
power = x**2

#   2a. The type of total.
# your code here

#   2b. The type of product.
# your code here

#   2c. The type of power.
# your code here

#   2d. The parts total is built from.
# your code here


# ─── 3 · DO · exact numbers ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → exact numbers

#   3a. The exact square root of 8.
# your code here

#   3b. One third plus one sixth, kept exact.
# your code here

#   3c. The square root of -4.
# your code here

#   3d. Half of pi, plus half of pi.
# your code here


# ─── 4 · DO · swapping in values ────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → values and decimals, exact numbers

expr = x**2 + 3*x
pair = x*y + 1

#   4a. expr with x = 2.
# your code here

#   4b. expr with x = one half, kept exact.
# your code here

#   4c. expr with every x replaced by y.
# your code here

#   4d. pair with x = 2 and y = 3.
# your code here


# ─── 5 · DO · decimals on purpose ───────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → values and decimals

root2 = sqrt(2)
third = Rational(1, 3)

#   5a. root2 as a decimal with 4 significant digits.
# your code here

#   5b. third as a decimal with 3 significant digits.
# your code here


# ─── 6 · DO · comparing ─────────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → comparing, symbols and expressions

squared = (x + 1)**2
multiplied = x**2 + 2*x + 1
mixed = x**2 + y

#   6a. Whether squared and multiplied are written the same way (True / False).
# your code here

#   6b. Whether squared and multiplied are equal as maths.
# your code here

#   6c. The letters used in mixed.
# your code here


# ─── 7 · DO · a circle ──────────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → symbols and expressions, exact numbers, values and decimals

r = symbols("r")
area = pi*r**2

#   7a. The area when r is 3, exact.
# your code here

#   7b. The area when r is 3, as a decimal with 4 significant digits.
# your code here


# ─── 8 · WRITE · value_at ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → values and decimals
#   Gives back expr with every x swapped for number.
#   expr: an expression in x    number: what to put in place of x

def value_at(expr, number):
    pass  # your code here


# ─── 9 · FIX · half_of ──────────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → exact numbers
#   Should give back half of expr, exact. It gives decimals: fix it.

def half_of(expr):
    return expr * (1/2)


# ─── 10 · FIX · root_of ─────────────────────────────────────────────────────────────────────────────
#   Bags: 01_basics.txt → exact numbers
#   Should give back the exact square root of expr. It gives decimals or crashes: fix it.

import math

def root_of(expr):
    return math.sqrt(expr)


if __name__ == "__main__":
    import check
    check.level(globals())
