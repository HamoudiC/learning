r"""PROJECT 7 · Linear regression from scratch          (levels 1-11)
Find the line y = slope·x + intercept that fits some points best, two ways, and measure how good it is.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_07_linear_regression.py
"""
# ── your import line goes here ──



X = [1, 2, 3, 4, 5]
Y = [2.0, 4.1, 5.9, 8.2, 9.8]


# ─── 1 · WRITE · fit_line ───────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many
#   Gives back (slope, intercept):  slope = sum((x - mean_x)(y - mean_y)) / sum((x - mean_x)²),
#   intercept = mean_y - slope · mean_x.
#   x, y: 1D arrays, same length

def fit_line(x, y):
    pass  # your code here


# ─── 2 · WRITE · predict ────────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value
#   Gives back slope · x + intercept for every x.
#   x: a 1D array    slope, intercept: numbers

def predict(x, slope, intercept):
    pass  # your code here


# ─── 3 · WRITE · mean_squared_error ─────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many
#   Gives back the average of (y - predicted)². 0 is perfect.
#   y, predicted: 1D arrays, same length

def mean_squared_error(y, predicted):
    pass  # your code here


# ─── 4 · WRITE · r_squared ──────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many
#   Gives back 1 - sum((y - predicted)²) / sum((y - mean_y)²). 1.0 is perfect.
#   y, predicted: 1D arrays, same length

def r_squared(y, predicted):
    pass  # your code here


# ─── 5 · WRITE · gradient_descent ───────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many;  00_python_basics.txt → loops
#   Gives back (slope, intercept) after training from (0.0, 0.0). Each step, with error = slope·x + intercept - y:
#   slope -= rate · 2 · mean(error · x)   and   intercept -= rate · 2 · mean(error)   (both from the OLD values).
#   x, y: float arrays    rate: the learning rate    steps: how many steps

def gradient_descent(x, y, rate, steps):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
