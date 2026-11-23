r"""LEVEL 8 · Adding up: sum, mean, max, and axis          (what comes next)
Run:  python ladder\level_08_aggregations.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · one number from many ──────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → one number from many

x = np.array([4, 8, 15, 16, 23, 42])

#   1a. All of x added up.
# your code here

#   1b. The average of x.
# your code here

#   1c. The biggest value minus the smallest.
# your code here

#   1d. The position of the biggest value.
# your code here


# ─── 2 · DO · running totals ────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals

changes = np.array([100, -30, 50, -20])
prices = np.array([10, 12, 11, 18])

#   2a. The account balance after each change, starting from 0.
# your code here

#   2b. How much the price changed from each day to the next.
# your code here


# ─── 3 · DO · per student, per test ─────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis), one number from many

scores = np.array([[70, 80, 90],
                   [60, 65, 100],
                   [85, 85, 85]])      # one row per student, one column per test

#   3a. Each test's total.
# your code here

#   3b. Each student's average.
# your code here

#   3c. Each student's best mark.
# your code here

#   3d. The row number of the student with the highest average.
# your code here


# ─── 4 · WRITE · student_averages ───────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis)
#   Gives back each student's average.
#   scores: one row per student, one column per test

def student_averages(scores):
    pass  # your code here


# ─── 5 · WRITE · hardest_test ───────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis), one number from many
#   Gives back the column number of the test with the LOWEST average.
#   scores: one row per student, one column per test

def hardest_test(scores):
    pass  # your code here


# ─── 6 · WRITE · balance_history ────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value
#   Gives back the balance after each change.
#   start: the money at the beginning    changes: deposits (+) and withdrawals (-), in order

def balance_history(start, changes):
    pass  # your code here


# ─── 7 · WRITE · biggest_jump ───────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, one number from many;  00_python_basics.txt → lists, tuples, dicts
#   Gives back a tuple (day, jump): the biggest rise from one day to the next, and the day it rose TO.
#   prices: one price per day

def biggest_jump(prices):
    pass  # your code here


# ─── 8 · FIX · total_per_row ────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis)
#   Should give back the total of each ROW. It gives the wrong totals: fix it.

def total_per_row(table):
    return table.sum(axis=0)


if __name__ == "__main__":
    import check
    check.level(globals())
