r"""PROJECT 6 · Monte Carlo: answers from random numbers          (levels 1-9)
Simulate thousands of times and count. Answers are never exact, so the tests check yours lands close.
Make the generator inside each function:  np.random.default_rng(seed).
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_06_monte_carlo.py
"""
# ── your import line goes here ──



# ─── 1 · WRITE · estimate_pi ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers;  03_maths_and_aggregations.txt → maths on every value, per row or per column
#   Gives back an estimate of pi: 4 × the fraction of random points in the 1 × 1 square with x² + y² ≤ 1.
#   points: how many random points    seed: the random seed

def estimate_pi(points, seed):
    pass  # your code here


# ─── 2 · WRITE · two_dice_counts ────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers;  03_maths_and_aggregations.txt → per row or per column (axis)
#   Gives back 11 counts: how many times two dice added up to 2, 3, ..., 12.
#   rolls: how many times to roll both dice    seed: the random seed

def two_dice_counts(rolls, seed):
    pass  # your code here


# ─── 3 · WRITE · shared_birthday_chance ─────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers;  04_masks_sorting_joining.txt → sorting, counting and checking
#   Gives back the fraction of rooms where at least two people share a birthday (365 days).
#   people: people per room    trials: how many rooms    seed: the random seed

def shared_birthday_chance(people, trials, seed):
    pass  # your code here


# ─── 4 · WRITE · random_walk ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → random numbers;  03_maths_and_aggregations.txt → running totals
#   Gives back the position after each step, starting at 0. Each step is +1 or -1.
#   steps: how many steps    seed: the random seed

def random_walk(steps, seed):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
