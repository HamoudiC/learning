r"""The checker. Every level file runs it at the bottom. You don't edit this file.

It reads the level file itself, one question at a time. A question starts with a line like
    # ─── 4 · WRITE · slope_at ───────
and goes on until the next one.

  READ   runs the question's code on its own, works out the line written in the comment after each
         q4a = ..., q4b = ... answer, and compares it with your answer. READ asks what SymPy GIVES BACK,
         so the FORM counts: (x + 1)**2 and x**2 + 2*x + 1 are the same value but not the same answer.
  WRITE  runs every example written as   something  ->  result   in the question. The examples ARE the tests:
         nothing is hidden. Here any form that is mathematically equal counts.
  FIX    the same, on a function that's broken until you fix it.

Then it prints one line per question and explains what isn't done yet:
  ✅ done   ❌ not right yet   📝 plan missing   ⬜ not started (or, for a FIX, still broken)

Add  show  to the command to see SymPy's answer for READ questions you got wrong:
    python ladder\level_01_symbols.py show
"""
import ast
import base64
import copy
import json
import io
import re
import sys
import threading
import tokenize
import traceback
from pathlib import Path

import sympy
from sympy import Basic, Float, FiniteSet, MatrixBase, Set, simplify, symbols, sympify
from sympy.core.relational import Relational
from sympy.logic.boolalg import BooleanAtom
from sympy.printing.str import StrPrinter

HEADER = re.compile(r"^# ─+ (\d+) · (READ|WRITE|FIX|DO) · (.+?) ─*\s*$")
ANSWER_NAME = re.compile(r"q\d+[a-z]")
NUMBERED = re.compile(r"^\s*#\s*\d+\.(.*)$")
ARROW = "  ->  "
TIMEOUT = 15  # seconds before an example counts as "never finishes" (SymPy can be slow the first time)

ICON = {"done": "✅", "wrong": "❌", "plan": "📝", "todo": "⬜"}

# Every name  from sympy import *  gives, plus the usual symbols, so examples can always be worked out.
SYMPY_NAMES = {name: getattr(sympy, name) for name in sympy.__all__}
SYMPY_NAMES.update(zip("x y z t n k a b".split(), symbols("x y z t n k a b")))
PRELOADED = SYMPY_NAMES

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ── reading the level file ─────────────────────────────────────────────────────────────────────

class Question:
    def __init__(self, number, kind, title, lines, first_line):
        self.number = int(number)
        self.kind = kind
        self.title = title.strip()
        self.lines = lines              # the question's source lines, without its header
        self.first_line = first_line    # the file's line number of lines[0]


def split_questions(source):
    lines = source.splitlines()
    heads = [(i, m) for i, line in enumerate(lines) if (m := HEADER.match(line))]
    end = next((i for i, line in enumerate(lines) if line.startswith("if __name__")), len(lines))
    questions = []
    for n, (i, m) in enumerate(heads):
        stop = heads[n + 1][0] if n + 1 < len(heads) else end
        questions.append(Question(m[1], m[2], m[3], lines[i + 1:stop], i + 2))
    return questions


def comments_by_line(text):
    found = {}
    for tok in tokenize.generate_tokens(io.StringIO(text).readline):
        if tok.type == tokenize.COMMENT:
            found[tok.start[0]] = tok.string.lstrip("#").strip()
    return found


def expression_in(comment):
    """The Python in a READ comment. Your own notes after it (2 spaces or a # later) are ignored."""
    for candidate in (comment, re.split(r"\s{2,}|\s#", comment)[0].strip()):
        try:
            ast.parse(candidate, mode="eval")
            return candidate
        except SyntaxError:
            continue
    return None


def examples_in(question):
    """Every comment line written as  something  ->  result  where both sides are Python."""
    found = []
    for line in question.lines:
        text = line.strip()
        if not text.startswith("#") or ARROW not in text:
            continue
        left, right = (part.strip() for part in text.lstrip("#").split(ARROW, 1))
        try:
            ast.parse(left, mode="eval")
            ast.parse(right, mode="eval")
        except SyntaxError:
            continue
        found.append((left, right))
    return found


def find_def(tree, name):
    found = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            found = node
    return found


def is_placeholder(func):
    body = func.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
            and isinstance(body[0].value.value, str):
        body = body[1:]
    return all(isinstance(s, ast.Pass) or (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant)
                                           and s.value.value is Ellipsis) for s in body)


# ── showing values the way you would TYPE them ─────────────────────────────────────────────────

class Typeable(StrPrinter):
    """Like print(), except a fraction on its own shows as Rational(1, 2): typing 1/2 would give 0.5."""

    def _print_Rational(self, expr):
        return str(expr.p) if expr.q == 1 else f"Rational({expr.p}, {expr.q})"

    def _print_Half(self, expr):
        return "Rational(1, 2)"

    def _print_MatrixBase(self, expr):
        return "Matrix(" + show_value(expr.tolist()) + ")"

    _print_MutableDenseMatrix = _print_ImmutableDenseMatrix = _print_MatrixBase


def show_value(v):
    if isinstance(v, type):
        return v.__name__
    if isinstance(v, list):
        return "[" + ", ".join(show_value(a) for a in v) + "]"
    if isinstance(v, tuple):
        inner = ", ".join(show_value(a) for a in v)
        return f"({inner},)" if len(v) == 1 else f"({inner})"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{show_value(k)}: {show_value(w)}" for k, w in v.items()) + "}"
    if isinstance(v, (set, frozenset)):
        return "{" + ", ".join(sorted(show_value(a) for a in v)) + "}" if v else "set()"
    if isinstance(v, FiniteSet):
        return "{" + ", ".join(show_value(a) for a in v.args) + "}"
    if isinstance(v, Float):
        from mpmath.libmp import prec_to_dps
        digits = prec_to_dps(v._prec)
        if digits < 15:                          # N(x, 4) keeps 4 digits: say so, so it reads back the same
            return f"Float('{v}', {digits})"
    if isinstance(v, (Basic, MatrixBase)):
        printed = str(v)             # what print() shows: use it when typing it back gives the same thing
        try:
            if "\n" not in printed and same(eval(printed, dict(SYMPY_NAMES)), v, EXACT):
                return printed
        except Exception:
            pass
        return Typeable().doprint(v)
    return repr(v)


# ── comparing ──────────────────────────────────────────────────────────────────────────────────

EXACT, MATH = "exact", "math"   # READ: the form counts.  WRITE: any equal form counts.
LOOSE = MATH                    # the name the shared tools use
_MISSING = object()


def as_sympy(v):
    if isinstance(v, (bool, str)) or v is None:
        return None
    try:
        s = sympify(v, strict=True)
    except Exception:
        return None
    return s if isinstance(s, Basic) else None


def kind_of(v):
    if isinstance(v, type):
        return "a type (like Symbol or Integer, written without quotes)"
    if v is None:
        return "None"
    if isinstance(v, (bool, BooleanAtom)):
        return "True or False"
    if isinstance(v, str):
        return "a str (text in quotes)"
    if isinstance(v, MatrixBase):
        return "a Matrix"
    if isinstance(v, list):
        return "a list [ ]"
    if isinstance(v, tuple):
        return "a tuple ( )"
    if isinstance(v, dict):
        return "a dict {key: value}"
    if isinstance(v, (set, frozenset, FiniteSet)):
        return "a set { }"
    s = as_sympy(v)
    if s is None:
        return f"a {type(v).__name__}"
    if isinstance(s, Set):
        return f"a SymPy set ({type(s).__name__})"
    if isinstance(s, Relational):
        return "an equation or inequality (Eq, <, >)"
    if s.has(Float) or isinstance(v, float):
        return "a decimal (Float)" if s.is_number else "an expression with decimals in it"
    if s.is_number:
        return "an exact number"
    return "a SymPy expression"


def retype(real):
    """real printed, then typed back in: some printed forms (like 1/(2*(x + 1))) come back a little different."""
    env = dict(SYMPY_NAMES)
    env.update({s.name: s for s in real.free_symbols if isinstance(s, sympy.Symbol)})
    try:
        return eval(str(real), env)
    except Exception:
        return None


def float_tolerance(real, mode):
    if mode == MATH:
        return 1e-6 * max(1.0, abs(complex(real)))
    text = str(real)
    if "." in text and "e" not in text.lower():
        return 0.5 * 10 ** -len(text.split(".")[1]) * 1.001 + 1e-15
    return 1e-6 * max(1.0, abs(complex(real)))


def same(mine, real, mode):
    if isinstance(real, sympy.Tuple):        # SymPy's own (3, 2) inside sets: compare it as a normal tuple
        real = tuple(real.args)
    if isinstance(mine, sympy.Tuple):
        mine = tuple(mine.args)
    if isinstance(real, type):
        return isinstance(mine, type) and (mine is real or issubclass(real, mine))
    if isinstance(mine, type):
        return False
    if real is None or mine is None:
        return mine is real
    if isinstance(real, (bool, BooleanAtom)):
        return isinstance(mine, (bool, BooleanAtom)) and bool(mine) == bool(real)
    if isinstance(mine, (bool, BooleanAtom)):
        return False
    if isinstance(real, str) or isinstance(mine, str):
        return mine == real
    if isinstance(real, (list, tuple)):
        return type(mine) is type(real) and len(mine) == len(real) and \
            all(same(a, b, mode) for a, b in zip(mine, real))
    if isinstance(real, dict):
        if not isinstance(mine, dict) or len(mine) != len(real):
            return False
        for key, value in real.items():
            match = next((k for k in mine if same(k, key, EXACT)), _MISSING)
            if match is _MISSING or not same(mine[match], value, mode):
                return False
        return True
    if isinstance(real, (set, frozenset, FiniteSet)):
        if not isinstance(mine, (set, frozenset, FiniteSet)):
            return False
        mine_items, real_items = list(mine), list(real)
        return len(mine_items) == len(real_items) and \
            all(any(same(m, r, mode) for m in mine_items) for r in real_items)
    if isinstance(real, MatrixBase):
        return isinstance(mine, MatrixBase) and mine.shape == real.shape and \
            all(same(a, b, mode) for a, b in zip(mine, real))
    if isinstance(mine, (list, tuple, dict, set, frozenset, FiniteSet, MatrixBase)):
        return False

    m, r = as_sympy(mine), as_sympy(real)
    if m is None or r is None:
        return mine == real
    if isinstance(r, (Set, Relational)) or isinstance(m, (Set, Relational)):
        if m == r:
            return True
        if mode == MATH and isinstance(m, Relational) and type(m) is type(r):
            try:
                return simplify((m.lhs - m.rhs) - (r.lhs - r.rhs)) == 0
            except Exception:
                return False
        return False
    real_float, mine_float = r.has(Float), m.has(Float) or isinstance(mine, float)
    if real_float:
        if m == r:
            return True
        if not (m.is_number and r.is_number):
            return False
        try:
            tolerance = float_tolerance(r, mode)
            if mode == MATH and isinstance(m, Float):    # N(thing, 4) only keeps 4 digits: compare to those
                tolerance = max(tolerance, float_tolerance(m, EXACT))
            return abs(complex(m) - complex(r)) <= tolerance
        except Exception:
            return False
    if mine_float:
        return False
    if m == r:
        return True
    if mode == EXACT:
        retyped = retype(r)          # what you get by typing exactly what print() showed
        return retyped is not None and m == retyped
    try:
        return simplify(m - r) == 0
    except Exception:
        return False


def why_wrong(mine, real, mode):
    """One plain-English line on the difference, for the most common slips."""
    m, r = as_sympy(mine), as_sympy(real)
    said = "you wrote" if mode == EXACT else "yours is"
    if isinstance(real, type) and isinstance(mine, str) and mine.strip() == real.__name__:
        return f"you wrote the text {mine!r}. Write the type itself, without quotes:  {real.__name__}"
    if isinstance(mine, str) and r is not None:
        return f"{said} the text {mine!r} (in quotes). SymPy objects aren't text: no quotes."
    if m is not None and r is not None and not isinstance(m, (Set, Relational)):
        if (m.has(Float) or isinstance(mine, float)) and not r.has(Float):
            return (f"{said} a decimal. SymPy keeps numbers EXACT here (fractions, sqrt(2), pi...). "
                    "Careful: 1/2 in Python is the decimal 0.5: write Rational(1, 2).")
        if r.has(Float) and not m.has(Float):
            return f"{said} an exact value, but the answer is a DECIMAL (Float) here."
        if mode == EXACT and not r.has(Float):
            try:
                if simplify(m - r) == 0:
                    return ("right value, but not the FORM SymPy gives back (multiplied out? factored? in another "
                            "order of steps?). READ asks for exactly what SymPy hands back.")
            except Exception:
                pass
    if kind_of(mine) != kind_of(real):
        return f"{said} {show_value(mine)}, which is {kind_of(mine)}. The answer is {kind_of(real)}."
    return f"{said} {show_value(mine)}: the right kind ({kind_of(real)}), but not the right value."


# ── running code safely ────────────────────────────────────────────────────────────────────────

def run(expr, env):
    """eval(expr) with what it prints captured, and a time limit."""
    box = {}

    def target():
        try:
            box["value"] = eval(expr, env)
        except BaseException as err:  # noqa: BLE001 - any error in the learner's code is a result
            box["error"] = err

    printed, old = io.StringIO(), sys.stdout
    sys.stdout = printed
    worker = threading.Thread(target=target, daemon=True)
    try:
        worker.start()
        worker.join(TIMEOUT)
    finally:
        sys.stdout = old
    box["printed"] = printed.getvalue()
    box["timeout"] = worker.is_alive()
    return box


def where(err, level_file):
    for frame in reversed(traceback.extract_tb(err.__traceback__)):
        if Path(frame.filename).resolve() == level_file:
            return f"   (your line {frame.lineno}:  {(frame.line or '').strip()})"
    return ""


def crash_hint(err):
    if isinstance(err, NameError):
        return ("   A name Python doesn't know. Is the import line at the top of the file? Are the symbols made "
                "(x = symbols(\"x\"))?\n   Look up: bags/01_basics.txt → import, symbols")
    if isinstance(err, TypeError) and "Symbol" in str(err) and "math" in str(err).lower():
        return "   math.sqrt / math.sin only take numbers. On a Symbol use SymPy's own: sqrt(x), sin(x)."
    if isinstance(err, TypeError) and "not subscriptable" in str(err):
        return "   [0] on something that isn't a list. Probe it first: what is its type()?"
    if isinstance(err, TypeError) and "is not callable" in str(err):
        return "   An expression isn't a Python function: f(3) doesn't work on it. Swap the value in: f.subs(x, 3)"
    if isinstance(err, TypeError) and "UndefinedFunction" in str(err):
        return "   y = Function(\"y\") is only the function's NAME. Inside an equation write y(x), with the (x)."
    if isinstance(err, TypeError) and "can't multiply sequence" in str(err):
        return "   Plain Python lists: * on lists doesn't do maths. Make them Matrix(...) first."
    if isinstance(err, KeyError):
        return "   That key isn't in the dict. Probe what came back: print it, or its .keys(). What SHAPE is it?"
    if isinstance(err, IndexError):
        return "   [n] past the end of a list. How many items does it really have? Probe it: len(...)"
    return ""


def snapshot(ns):
    """Copies of the file's UPPER-CASE data, to check no function changed it."""
    kept = {}
    for name, value in ns.items():
        if name.isupper() and not callable(value) and not isinstance(value, type(sys)) and name not in SYMPY_NAMES:
            try:
                kept[name] = copy.deepcopy(value)
            except Exception:
                pass
    return kept


# ── the three kinds of question ────────────────────────────────────────────────────────────────

def check_read(q, ns, show):
    block = "\n".join(q.lines)
    tree = ast.parse(block)
    comments = comments_by_line(block)
    setup, answers = [], []
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
                and ANSWER_NAME.fullmatch(node.targets[0].id)):
            answers.append((node.targets[0].id, comments.get(node.lineno) or comments.get(node.end_lineno)))
        else:
            setup.append(node)

    env = {**SYMPY_NAMES, **ns}
    printed, old = io.StringIO(), sys.stdout
    sys.stdout = printed
    try:
        exec(compile(ast.Module(body=setup, type_ignores=[]), "<question>", "exec"), env)
    except Exception as err:
        return "wrong", [f"The code in this question crashed ({type(err).__name__}: {err}).",
                         "Did something above the answers get changed? Undo it (Ctrl+Z)."]
    finally:
        sys.stdout = old

    notes, right, answered = [], 0, 0
    for name, comment in answers:
        expr = expression_in(comment) if comment else None
        if not expr:
            notes.append(f"{name}: the comment after it is gone or changed, so there's nothing to check. Undo (Ctrl+Z).")
            continue
        mine = ns.get(name, ...)
        if mine is ...:
            continue
        answered += 1
        result = run(expr, env)
        if "error" in result:
            notes.append(f"{name}   {expr}\n   SymPy gives an error: {type(result['error']).__name__}. "
                         "(Tell Claude: this question has a bug.)")
            continue
        real = result["value"]
        if same(mine, real, EXACT):
            right += 1
            continue
        why = why_wrong(mine, real, EXACT)
        if show:
            why += f"\n   SymPy gives:  {show_value(real)}"
        notes.append(f"{name}   {expr}\n   {why}")

    total = len(answers)
    if right == total:
        return "done", []
    if notes:
        notes.append("Work it out again. Stuck? Try that line in the >>> prompt, or add  show  to the command.")
        return "wrong", notes
    return "todo", [f"Replace each  ...  with your answer. ({answered} of {total} answered so far)"]


TASK = re.compile(r"^#\s+(\d+[a-z])\.\s")


def hidden_answers(level_file):
    """The answers, kept out of sight in answers.json next to the file (so the levels don't give them away)."""
    path = level_file.parent / "answers.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get(level_file.stem, {})


def decode(text, names=None):
    """A hidden answer, worked out with the level's own names (its symbols, its data)."""
    return eval(base64.b64decode(text).decode("utf-8"), {**PRELOADED, **(names or {})})


def task_slots(source):
    """{task id: (first line, last line)} of the lines under each task of the DO questions."""
    slots = {}
    for q in split_questions(source):
        if q.kind != "DO":
            continue
        starts = [(q.first_line + i, m[1]) for i, line in enumerate(q.lines) if (m := TASK.match(line))]
        block_end = q.first_line + len(q.lines) - 1
        for n, (line_no, tid) in enumerate(starts):
            end = starts[n + 1][0] - 1 if n + 1 < len(starts) else block_end
            slots[tid] = (line_no + 1, end)
    return slots


def assigned_name(node):
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    if isinstance(node, (ast.AugAssign, ast.AnnAssign)) and isinstance(node.target, ast.Name):
        return node.target.id
    return None


def run_tasks(source, level_file, slots):
    """Runs the file again, top to bottom, and keeps what each task's code gives at the moment it runs."""
    body = []
    for node in ast.parse(source).body:
        if isinstance(node, ast.If) and "__name__" in ast.unparse(node.test):
            break
        body.append(node)
    owner, last, nodes = {}, {}, {tid: [] for tid in slots}
    for i, node in enumerate(body):
        for tid, (a, b) in slots.items():
            if a <= node.lineno <= b:
                owner[i] = tid
                last[tid] = i
                nodes[tid].append(node)
    results = {tid: ("todo", None) for tid in slots}
    g = {"__file__": str(level_file), "__name__": "__tasks__"}
    printed, old = io.StringIO(), sys.stdout
    sys.stdout = printed
    try:
        for i, node in enumerate(body):
            tid = owner.get(i)
            try:
                if tid and last[tid] == i and isinstance(node, ast.Expr):
                    results[tid] = ("value", eval(compile(ast.Expression(node.value), str(level_file), "eval"), g))
                    continue
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(level_file), "exec"), g)
                if tid and last[tid] == i:
                    name = assigned_name(node)
                    results[tid] = ("value", g[name]) if name else ("noanswer", None)
            except Exception as err:  # noqa: BLE001
                if tid:
                    results[tid] = ("error", err)
    finally:
        sys.stdout = old
    return results, nodes, g


def check_do(q, tasks, hidden):
    """DO: each task says in English what to make from the data. The learner writes the code under it."""
    results, nodes, names = tasks
    ids = [m[1] for line in q.lines if (m := TASK.match(line))]
    block = ast.parse("\n".join(q.lines))
    slot_lines = set()
    for tid in ids:
        for node in nodes.get(tid, []):
            slot_lines.add(node.lineno)
    data_names = [n.id for node in block.body if isinstance(node, ast.Assign)
                  and node.lineno + q.first_line - 1 not in slot_lines
                  for t in node.targets for n in ast.walk(t) if isinstance(n, ast.Name)]
    notes, right, started = [], 0, 0
    for tid in ids:
        state = results.get(tid, ("todo", None))
        if state[0] == "todo":
            continue
        started += 1
        if state[0] == "error":
            err = state[1]
            notes.append(f"{tid}: your code crashed:  {type(err).__name__}: {err}\n{crash_hint(err)}".rstrip())
            continue
        if state[0] == "noanswer":
            notes.append(f"{tid}: end your code with the answer: an expression, or a  name = ...  line.")
            continue
        if tid not in hidden.get("tasks", {}):
            notes.append(f"{tid}: there's no hidden answer for this task. (Tell Claude: this task has a bug.)")
            continue
        mine, expected = state[1], decode(hidden["tasks"][tid], names)
        if not same(mine, expected, EXACT):
            if kind_of(mine) != kind_of(expected):
                notes.append(f"{tid}: not right yet. Yours gives {kind_of(mine)}; the answer is {kind_of(expected)}.")
            else:
                notes.append(f"{tid}: not right yet. Yours gives the right kind of thing ({kind_of(mine)}), "
                             "but not the right values.")
            continue
        used = {n.id for node in nodes[tid] for n in ast.walk(node)
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
        if data_names and not used & set(data_names):
            notes.append(f"{tid}: right, but it's typed in. Work it out from the data ({', '.join(data_names)}).")
            continue
        right += 1
    if ids and right == len(ids):
        return "done", []
    if notes:
        return "wrong", notes
    return "todo", [f"Write your code under each task, in place of  # your code here.  ({started} of {len(ids)} started)"]


def check_write(q, ns, tree, source_lines, level_file, hidden=None):
    fix = q.kind == "FIX"
    name = q.title if q.title.isidentifier() else None
    func = find_def(tree, name) if name else None
    if name and func is None:
        return "wrong", [f"There's no  def {name}(  in the file any more. Did it get renamed or deleted?"]
    if func is not None and not fix and is_placeholder(func):
        return "todo", ["Not started. Write your code in the function, in place of  pass."]
    if func is not None:
        body = source_lines[func.lineno - 1:func.end_lineno]
        if any("# PLAN" in line for line in body):
            filled = [m[1] for line in body if (m := NUMBERED.match(line)) and m[1].strip()]
            if len(filled) < 2:
                return "plan", ["Write the PLAN first: fill in the  # 1.  # 2.  ...  lines in plain English, one",
                                "step per line. Then run again and the code gets checked."]

    env = {**SYMPY_NAMES, **ns}
    tests = (hidden or {}).get("tests", {}).get(name) if name else None
    if tests is not None:                       # hidden tests: the calls are known, the answers aren't shown
        examples = [(call, answer, False) for call, answer in tests]
    else:
        examples = [(left, right, True) for left, right in examples_in(q)]
    if not examples:
        return "wrong", ["There are no tests for this function. (Tell Claude: this question has a bug.)"]
    before = snapshot(ns)
    passed, first_fail = 0, None
    for left, right, visible in examples:
        expected = eval(right, env) if visible else decode(right, env)
        result = run(left, env)
        if result["timeout"]:
            first_fail = first_fail or [
                f"{left}",
                f"   didn't finish in {TIMEOUT} seconds: a loop that never ends, or SymPy stuck on something it",
                "   can't do (simplify or integrate on a huge expression)?"]
            break
        if "error" in result:
            err = result["error"]
            first_fail = first_fail or [f"{left}", f"   crashed:  {type(err).__name__}: {err}",
                                        where(err, level_file), crash_hint(err)]
            continue
        got = result["value"]
        if got is ... and not fix:
            return "todo", ["Not finished. Replace every  ...  with your code."]
        if same(got, expected, MATH):
            passed += 1
            continue
        if first_fail is None and not visible:
            first_fail = [f"{left}", f"   yours gave    {show_value(got)}",
                          "   not right yet" + (f": the answer is {kind_of(expected)}" if kind_of(got) != kind_of(expected)
                                               else "")]
        if first_fail is None:
            first_fail = [f"{left}",
                          f"   should give   {show_value(expected)}",
                          f"   yours gave    {show_value(got)}"]
            if got is None and expected is not None:
                first_fail.append("   None means nothing was handed back: it PRINTS instead of RETURNING, the return "
                                  "line is missing,\n   or the function never reaches it.")
            else:
                first_fail.append("   (" + why_wrong(got, expected, MATH) + ")")
            if result["printed"].strip():
                shown = "\n      ".join(result["printed"].strip().splitlines()[:4])
                first_fail.append(f"   it also printed:\n      {shown}")

    changed = [k for k in before if ns.get(k) != before[k]]
    for k in changed:
        ns[k] = before[k]
    if changed and first_fail is None:
        first_fail = [f"It gives the right results, but it CHANGED {', '.join(changed)}: the data it was given.",
                      "A function should leave its input alone: build a new list or dict instead."]

    if first_fail is None and passed == len(examples):
        return "done", []
    lines = [line for line in first_fail if line]
    lines.append(f"{passed} of {len(examples)} tests right.")
    if fix:
        lines.insert(0, "Still broken.")
    return ("todo" if fix else "wrong"), lines


# ── the report ─────────────────────────────────────────────────────────────────────────────────

def level(ns):
    """Called at the bottom of each level file with its globals()."""
    level_file = Path(ns["__file__"]).resolve()
    source = level_file.read_text(encoding="utf-8")
    source_lines = source.splitlines()
    tree = ast.parse(source)
    show = "show" in sys.argv[1:]

    questions = split_questions(source)
    hidden = hidden_answers(level_file)
    tasks = run_tasks(source, level_file, task_slots(source)) if any(q.kind == "DO" for q in questions) else ({}, {}, {})
    results = []
    for q in questions:
        if q.kind == "DO":
            status, notes = check_do(q, tasks, hidden)
        elif q.kind == "READ":
            status, notes = check_read(q, ns, show)
        else:
            status, notes = check_write(q, ns, tree, source_lines, level_file, hidden)
        results.append((q, status, notes))

    title = (ns.get("__doc__") or level_file.stem).strip().splitlines()[0]
    print(f"\n{title}\n")
    for q, status, _ in results:
        print(f"  {ICON[status]}  {q.number:>2}  {q.kind:<5}  {q.title}")

    done = sum(status == "done" for _, status, _ in results)
    print(f"\n  {done} of {len(results)} done.")
    print("  " + "─" * 100)

    to_explain = [r for r in results if r[1] in ("wrong", "plan")]
    first_open = next((r for r in results if r[1] != "done"), None)
    if first_open and first_open not in to_explain:
        to_explain.insert(0, first_open)
    to_explain.sort(key=lambda r: r[0].number)
    for q, status, notes in to_explain:
        print(f"\n  {ICON[status]} {q.number} · {q.kind} · {q.title}")
        for note in notes:
            for line in note.splitlines():
                print(f"     {line}")

    if done == len(results):
        number = re.match(r"level_(\d+)", level_file.stem)
        nxt = sorted(level_file.parent.glob(f"level_{int(number[1]) + 1:02d}_*.py")) if number else []
        print("\n  Level done!" + (f"  Next:  python ladder\\{nxt[0].name}" if nxt else
                                   "  That's the whole ladder: you can use SymPy from start to full."))
    print()
