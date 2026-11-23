r"""PROJECT 4 · Conway's Game of Life          (levels 1-9)
1 = alive, 0 = dead. Each step: a live cell with 2 or 3 live neighbours stays alive, otherwise it dies;
a dead cell with exactly 3 live neighbours comes alive. Outside the grid counts as dead.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_04_game_of_life.py
"""
# ── your import line goes here ──



BLINKER = [[0, 0, 0],
           [1, 1, 1],
           [0, 0, 0]]


# ─── 1 · WRITE · count_neighbours ───────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → joining and splitting;  02_indexing_copies_dtypes.txt → 2D and 3D;  01_arrays_and_shape.txt → ready-made arrays, size and shape;  03_maths_and_aggregations.txt → maths on every value;  00_python_basics.txt → loops
#   Gives back, for every cell, how many of its 8 neighbours are alive (same shape as grid).
#   grid: 2D array of 0s and 1s

def count_neighbours(grid):
    pass  # your code here


# ─── 2 · WRITE · next_generation ────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks);  02_indexing_copies_dtypes.txt → dtypes
#   Gives back the grid one step later.
#   grid: 2D array of 0s and 1s

def next_generation(grid):
    pass  # your code here


# ─── 3 · WRITE · run ────────────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops
#   Gives back the grid after that many steps.
#   grid: the start    steps: how many steps

def run(grid, steps):
    pass  # your code here


# ─── 4 · WRITE · history ────────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → one number from many;  00_python_basics.txt → lists, tuples, dicts, loops, numbers
#   Gives back a list: how many cells are alive at the start and after each step.
#   grid: the start    steps: how many steps

def history(grid, steps):
    pass  # your code here


# ─── 5 · WRITE · show ───────────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops, text, checks
#   Gives back the grid as text: "█" alive, "·" dead, one line per row, joined with "\n".
#   grid: 2D array of 0s and 1s

def show(grid):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
