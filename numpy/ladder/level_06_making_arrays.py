r"""LEVEL 6 · Making arrays without typing them          (what comes next)
Run:  python ladder\level_06_making_arrays.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · counting ──────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → ready-made arrays

#   1a. The whole numbers 0 to 9.
# your code here

#   1b. The odd numbers from 1 to 19.
# your code here

#   1c. 5 evenly spaced numbers from 0 to 1, with 1 included.
# your code here

#   1d. 10, 7, 4, 1 (counting down in 3s).
# your code here


# ─── 2 · DO · filled arrays ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → ready-made arrays

#   2a. Five 0s.
# your code here

#   2b. A 2 × 3 array of 1s, as whole numbers.
# your code here

#   2c. A 3 × 3 array where every value is 7.
# your code here

#   2d. A 4 × 4 array with 1s on the diagonal and 0s everywhere else.
# your code here


# ─── 3 · DO · random numbers ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers;  03_maths_and_aggregations.txt → one number from many;  04_masks_sorting_joining.txt → counting and checking

#   3a. Roll 1000 dice (whole numbers 1 to 6) with a random generator seeded 7. Give back a tuple:
#       (the smallest roll, the biggest roll).
# your code here

#   3b. Make two generators, both seeded 5. Give back whether their first 3 random decimals are all the same.
# your code here


# ─── 4 · WRITE · times_table ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → ready-made arrays;  03_maths_and_aggregations.txt → maths on every value
#   Gives back the first 10 multiples of n:  n, 2n, ..., 10n.
#   n: a whole number

def times_table(n):
    pass  # your code here


# ─── 5 · WRITE · board ──────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → ready-made arrays;  02_indexing_copies_dtypes.txt → picking and changing
#   Gives back a whole-number board of 0s, with a 1 in the top-left corner.
#   rows, cols: the size of the board

def board(rows, cols):
    pass  # your code here


# ─── 6 · WRITE · dice_rolls ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers
#   Gives back how_many rolls of a 6-sided die (1 to 6). The same seed always gives the same rolls.
#   how_many: how many rolls    seed: the random seed

def dice_rolls(how_many, seed):
    pass  # your code here


# ─── 7 · FIX · percentages ──────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → ready-made arrays
#   Should give back 0, 10, 20, ..., 100. The 100 is missing: fix it.

def percentages():
    return np.arange(0, 100, 10)


if __name__ == "__main__":
    import check
    check.level(globals())
