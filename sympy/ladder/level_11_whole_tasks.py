r"""LEVEL 11 · Whole tasks: you write everything, the import too
Write your setup lines at the top (the import, then x = symbols("x")).
Then write each function: delete  pass  and write your code.
Run:  python ladder\level_11_whole_tasks.py
"""
# ── your setup lines go here ──




# ─── 1 · WRITE · newton_method ──────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating;  01_basics.txt → values and decimals;  00_python_basics.txt → loops
#   Gives back the guess after `steps` Newton steps, exact: each step, guess = guess - f(guess) / f'(guess).
#   f: an expression in x    start: the first guess    steps: how many steps

def newton_method(f, start, steps):
    pass  # your code here


# ─── 2 · WRITE · check_answer ───────────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating;  02_algebra.txt → tidying;  03_solving.txt → equations
#   Gives back True if my answer is right: "derivative" = equal to the derivative, "integral" = its
#   derivative equals the problem (any + C), "solve" = the same solutions in any order.
#   kind: "derivative", "integral" or "solve"    problem: an expression in x    answer: an expression (a list for "solve")

def check_answer(kind, problem, answer):
    pass  # your code here


# ─── 3 · WRITE · tangent_and_normal ─────────────────────────────────────────────────────────────────
#   Bags: 05_derivatives.txt → differentiating, formulas;  00_python_basics.txt → lists, tuples, dicts
#   Gives back {"tangent": the tangent line, "normal": the line at right angles (slope -1/slope)},
#   with "normal" None when the tangent's slope is 0.
#   f: an expression in x    a: the x of the point

def tangent_and_normal(f, a):
    pass  # your code here


# ─── 4 · WRITE · function_report ────────────────────────────────────────────────────────────────────
#   Bags: 06_using_derivatives.txt → critical points, shape of the graph;  03_solving.txt → sets of answers
#   Gives back {"derivative", "critical_points", "increasing", "decreasing", "concave_up", "inflection_points"}.
#   An inflection point is where f'' = 0 AND f'' changes sign (check a little left and right).
#   f: an expression in x

def function_report(f):
    pass  # your code here


# ─── 5 · WRITE · riemann_table ──────────────────────────────────────────────────────────────────────
#   Bags: 07_integrals.txt → adding up strips, integrating;  00_python_basics.txt → loops
#   Gives back a list of (strips, right Riemann sum, error) for each strip count; error = sum - exact integral.
#   f: an expression in x    a, b: the interval    strip_counts: a list of ints

def riemann_table(f, a, b, strip_counts):
    pass  # your code here


if __name__ == "__main__":
    import check
    check.level(globals())
