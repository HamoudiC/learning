r"""LEVEL 11 · Matrices and saving / loading arrays          (what comes next)
Run:  python ladder\level_11_linear_algebra_and_files.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"
OUT = Path(__file__).parent.parent / "out"


# ─── 1 · DO · multiplying matrices ──────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → matrices;  03_maths_and_aggregations.txt → maths on every value

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
v = np.array([1, 1])
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])

#   1a. A times B, position by position.
# your code here

#   1b. A matrix-multiplied by B.
# your code here

#   1c. A matrix-multiplied by v.
# your code here

#   1d. The dot product of p and q.
# your code here


# ─── 2 · DO · solving ───────────────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → matrices

M = np.array([[2, 0], [0, 4]])
rhs = np.array([6, 8])
arrow = np.array([6, 8])

#   2a. The determinant of M, rounded to 6 decimals.
# your code here

#   2b. The inverse of M.
# your code here

#   2c. The x that solves  M · x = rhs.
# your code here

#   2d. The length of the vector arrow.
# your code here


# ─── 3 · DO · comparing decimals ────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → comparing decimals

measured = np.array([0.1 + 0.2, 1.0])
expected = np.array([0.3, 1.0])

#   3a. Whether measured and expected are equal using ==, for every position (True only if all are).
# your code here

#   3b. Whether they're equal, allowing tiny decimal errors.
# your code here


# ─── 4 · DO · reading a file ────────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → files;  03_maths_and_aggregations.txt → per row or per column
#   Open data/scores.csv in VS Code and look at it first.

scores_file = DATA / "scores.csv"

#   4a. The numbers in scores_file as whole numbers, skipping the header line.
# your code here

#   4b. The first line of scores_file, as text.
# your code here

#   4c. The average of each column of the numbers in scores_file.
# your code here


# ─── 5 · WRITE · solve_two ──────────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → matrices
#   Gives back an array [x, y] for the two equations   a1·x + b1·y = c1   and   a2·x + b2·y = c2.
#   a1, b1, c1, a2, b2, c2: the numbers of the two equations

def solve_two(a1, b1, c1, a2, b2, c2):
    pass  # your code here


# ─── 6 · WRITE · rotate_points ──────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → matrices;  03_maths_and_aggregations.txt → maths functions
#   Gives back the points turned anticlockwise by degrees, rounded to 6 decimals.
#   Each point turns as  R @ point,  where R = [[cos a, -sin a], [sin a, cos a]] and a is in radians.
#   points: shape (n, 2), one (x, y) per row    degrees: how far to turn

def rotate_points(points, degrees):
    pass  # your code here


# ─── 7 · WRITE · save_and_reload ────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → files
#   Saves table in OUT as a CSV of whole numbers (make OUT if it isn't there), then gives back the table read
#   back from that file, as whole numbers.
#   table: a 2D int array    name: a file name like "small.csv"

def save_and_reload(table, name):
    pass  # your code here


# ─── 8 · FIX · same_floats ──────────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → comparing decimals
#   Should give back True if two decimal arrays are equal, allowing tiny decimal errors. It's too strict: fix it.

def same_floats(a, b):
    return (a == b).all()


if __name__ == "__main__":
    import check
    check.level(globals())
