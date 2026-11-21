r"""LEVEL 2 · Indexing and slicing          (your notebook)
Run:  python ladder\level_02_indexing_and_slicing.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · one value ─────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices

scores = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

#   1a. The first score.
# your code here

#   1b. The fourth score.
# your code here

#   1c. The last score.
# your code here

#   1d. The third score from the end.
# your code here


# ─── 2 · DO · slices ────────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices

scores = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

#   2a. The first three scores.
# your code here

#   2b. Every score from position 7 to the end.
# your code here

#   2c. Every second score, starting with the first.
# your code here

#   2d. All the scores in reverse order.
# your code here


# ─── 3 · DO · rows and columns ──────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D

marks = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

#   3a. The value in row 1, column 3.
# your code here

#   3b. The whole second row.
# your code here

#   3c. The whole third column.
# your code here

#   3d. The first two columns of both rows, as a 2D block.
# your code here


# ─── 4 · DO · 3D ────────────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D

cube = np.array([[[1, 2, 3], [4, 5, 6]],
                 [[7, 8, 9], [10, 11, 12]]])

#   4a. The value in block 1, row 0, column 2.
# your code here

#   4b. The second row of the first block.
# your code here

#   4c. The whole second block.
# your code here


# ─── 5 · WRITE · first_and_last ─────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back a tuple: (the first n values, the last n values).
#   arr: a 1D array    n: how many from each end

def first_and_last(arr, n):
    pass  # your code here


# ─── 6 · WRITE · column ─────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D
#   Gives back column j of the table, as a 1D array.
#   table: a 2D array    j: a column number (0 is the first)

def column(table, j):
    pass  # your code here


# ─── 7 · WRITE · corners ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D;  01_arrays_and_shape.txt → making arrays
#   Gives back a 1D array of the 4 corners: top-left, top-right, bottom-left, bottom-right.
#   table: a 2D array

def corners(table):
    pass  # your code here


# ─── 8 · WRITE · inner_block ────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D
#   Gives back the table without its outside edge (no first or last row, no first or last column).
#   table: a 2D array, at least 3 × 3

def inner_block(table):
    pass  # your code here


# ─── 9 · FIX · second_row ───────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D
#   Should give back the second ROW of the table. It doesn't: fix it.

def second_row(table):
    return table[:, 2]


if __name__ == "__main__":
    import check
    check.level(globals())
