r"""LEVEL 9 · Matrices and linear systems
Run:  python ladder\level_09_matrices.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
from sympy import *

x, y, z, t = symbols("x y z t")


# ─── 1 · DO · making and reading ────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → making and reading

A = Matrix([[1, 2], [3, 4]])
v = Matrix([5, 6])

#   1a. The shape of A.
# your code here

#   1b. The value of A in row 0, column 1.
# your code here

#   1c. The second row of A.
# your code here

#   1d. A with its rows and columns swapped.
# your code here

#   1e. A as plain lists.
# your code here


# ─── 2 · DO · maths ─────────────────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → maths

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[0, 1], [1, 0]])
v = Matrix([5, 6])

#   2a. A plus B.
# your code here

#   2b. A times B (matrix multiplication).
# your code here

#   2c. B times A.
# your code here

#   2d. A times v.
# your code here


# ─── 3 · DO · determinant, inverse, rank ────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → maths

A = Matrix([[1, 2], [3, 4]])
flat = Matrix([[1, 2], [2, 4]])

#   3a. The determinant of A.
# your code here

#   3b. The inverse of A.
# your code here

#   3c. The determinant of flat.
# your code here

#   3d. The rank of flat.
# your code here


# ─── 4 · DO · solving and eigenvalues ───────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → solving and eigenvalues

A = Matrix([[1, 2], [3, 4]])
v = Matrix([5, 6])
mirror = Matrix([[2, 1], [1, 2]])

#   4a. The solution of  A · (x, y) = v.
# your code here

#   4b. The eigenvalues of mirror.
# your code here


# ─── 5 · WRITE · solve_system ───────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → making and reading, maths, solving and eigenvalues;  00_python_basics.txt → lists, tuples, dicts, checks
#   Gives back the solution as a plain list, or None if the determinant is 0.
#   rows: the left-hand numbers as a list of rows    right_side: a list of the right-hand numbers

def solve_system(rows, right_side):
    pass  # your code here


# ─── 6 · WRITE · rotate ─────────────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → making and reading, maths
#   Gives back the point turned anticlockwise by angle, as a tuple, exact.
#   The rotation matrix is  Matrix([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]).
#   point: a tuple (x, y)    angle: in radians

def rotate(point, angle):
    pass  # your code here


# ─── 7 · WRITE · power_of ───────────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → maths, making and reading
#   Gives back the matrix to the power k, as a list of rows.
#   rows: a square matrix as a list of rows    k: 0 or more

def power_of(rows, k):
    pass  # your code here


# ─── 8 · WRITE · eigenvalue_list ────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → solving and eigenvalues;  00_python_basics.txt → loops, lists, tuples, dicts
#   Gives back the eigenvalues, smallest first, each one written as many times as it repeats.
#   rows: a square matrix as a list of rows

def eigenvalue_list(rows):
    pass  # your code here


# ─── 9 · FIX · multiply ─────────────────────────────────────────────────────────────────────────────
#   Bags: 09_matrices.txt → making and reading, maths
#   Should give back the matrix product of two matrices given as lists of rows, as a list of rows. It crashes: fix it.

def multiply(rows_a, rows_b):
    return rows_a * rows_b


if __name__ == "__main__":
    import check
    check.level(globals())
