r"""PROJECT 2 · Pixel art editor          (only needs levels 1-5: your notebook)
A picture is a 2D array of pixels: 0 = black, 9 = white. Crop, flip, rotate and shrink it.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_02_pixel_art.py
"""
# ── your import line goes here ──



ARROW = [[0, 0, 9, 0, 0, 0],
         [0, 9, 9, 9, 0, 0],
         [9, 0, 9, 0, 9, 0],
         [0, 0, 9, 0, 0, 0]]          # an arrow pointing up: 4 rows of 6 pixels


# ─── 1 · WRITE · load ───────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays, size and shape;  00_python_basics.txt → lists, tuples, dicts
#   Gives back (picture as a 2D array, height, width).
#   rows: a list of lists of pixels

def load(rows):
    pass  # your code here


# ─── 2 · WRITE · crop ───────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D
#   Gives back the part of the picture that starts at (top, left) and is height × width.
#   picture: 2D array    top, left: where the cut-out starts    height, width: its size

def crop(picture, top, left, height, width):
    pass  # your code here


# ─── 3 · WRITE · mirror ─────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices, 2D and 3D
#   Gives back the picture with left and right swapped.
#   picture: 2D array

def mirror(picture):
    pass  # your code here


# ─── 4 · WRITE · flip ───────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back the picture upside down (the rows in reverse order).
#   picture: 2D array

def flip(picture):
    pass  # your code here


# ─── 5 · WRITE · rotate_right ───────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices;  01_arrays_and_shape.txt → changing the shape
#   Gives back the picture turned 90° clockwise.
#   picture: 2D array

def rotate_right(picture):
    pass  # your code here


# ─── 6 · WRITE · shrink ─────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices, 2D and 3D
#   Gives back a half-size picture: every 2nd row and every 2nd column, starting from the first.
#   picture: 2D array

def shrink(picture):
    pass  # your code here


# ─── 7 · WRITE · as_text ────────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops, text, lists, tuples, dicts, checks
#   Gives back the picture as text: "#" for 9, "." for 0, one line per row, joined with "\n".
#   picture: 2D array of 0s and 9s

def as_text(picture):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
