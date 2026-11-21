r"""The checker. Every level and project file runs it at the bottom. You don't edit this file.

It reads the file itself, one question at a time. A question starts with a line like
    # ─── 4 · WRITE · column_means ───────
and goes on until the next one.

  READ   runs the question's code on its own, works out the line written in the comment after each
         q4a = ..., q4b = ... answer, and compares it with your answer. The TYPE counts: a list is not an
         array, 3 is not 3.0, a DataFrame is not a Series.
  WRITE  runs every example written as   something  ->  result   in the question. The examples ARE the tests:
         nothing is hidden.
  FIX    the same, on a function that's broken until you fix it.

Then it prints one line per question and explains what isn't done yet:
  ✅ done   ❌ not right yet   📝 plan missing   ⬜ not started (or, for a FIX, still broken)

Add  show  to the command to see Python's answer for READ questions you got wrong:
    python ladder\level_01_arrays.py show
"""
import ast
import base64
import copy
import io
import json
import math
import re
import sys
import threading
import tokenize
import traceback
from pathlib import Path, PurePath

try:
    import numpy as np
except ImportError:          # a course without numpy still works
    np = None
try:
    import pandas as pd
except ImportError:
    pd = None

HEADER = re.compile(r"^# ─+ (\d+) · (READ|WRITE|FIX|DO) · (.+?) ─*\s*$")
TARGET = re.compile(r"^\s*#\s*→\s*(.+?)\s*$")          # a DO task's  →  result  line
ANSWER_LINE = re.compile(r"^\s*q\d+[a-z]\s*=")
TOOLS = {"np", "pd", "math", "Path", "json"}            # names that don't count as "using the data"
ANSWER_NAME = re.compile(r"q\d+[a-z]")
NUMBERED = re.compile(r"^\s*#\s*\d+\.(.*)$")
ARROW = "  ->  "
TIMEOUT = 10  # seconds before an example counts as "never finishes"

ICON = {"done": "✅", "wrong": "❌", "plan": "📝", "todo": "⬜"}
EXACT, LOOSE = "exact", "loose"      # READ: the type counts exactly.  WRITE: equal numbers are equal.

# Names every example and READ comment can use, even before your own import line.
PRELOADED = {"Path": Path, "json": json, "math": math}
if np is not None:
    PRELOADED["np"] = np
if pd is not None:
    PRELOADED["pd"] = pd

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ── reading the file ───────────────────────────────────────────────────────────────────────────

class Question:
    def __init__(self, number, kind, title, lines, first_line):
        self.number = int(number)
        self.kind = kind
        self.title = title.strip()
        self.lines = lines
        self.first_line = first_line


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
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name == name:
            found = node
    return found


def is_placeholder(func):
    if isinstance(func, ast.ClassDef):           # a class is "not started" while every method is still a placeholder
        methods = [n for n in func.body if isinstance(n, ast.FunctionDef)]
        return bool(methods) and all(is_placeholder(m) for m in methods)
    body = func.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
            and isinstance(body[0].value.value, str):
        body = body[1:]
    return all(isinstance(s, ast.Pass) or (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant)
                                           and s.value.value is Ellipsis) for s in body)


# ── what kind of thing is it? ──────────────────────────────────────────────────────────────────

def is_array(v):
    return np is not None and isinstance(v, np.ndarray)


def is_frame(v):
    return pd is not None and isinstance(v, pd.DataFrame)


def is_series(v):
    return pd is not None and isinstance(v, pd.Series)


def is_index(v):
    return pd is not None and isinstance(v, pd.Index)


def is_dtype(v):
    return np is not None and isinstance(v, np.dtype)


def is_number(v):
    if isinstance(v, bool) or (np is not None and isinstance(v, np.bool_)):
        return False
    return isinstance(v, (int, float)) or (np is not None and isinstance(v, (np.integer, np.floating)))


def is_whole(v):
    return isinstance(v, int) or (np is not None and isinstance(v, np.integer))


def is_bool(v):
    return isinstance(v, bool) or (np is not None and isinstance(v, np.bool_))


def is_missing(v):
    try:
        return v is None or (pd is not None and v is pd.NA) or (isinstance(v, float) and math.isnan(v)) \
            or (np is not None and isinstance(v, np.floating) and np.isnan(v)) or (pd is not None and v is pd.NaT)
    except Exception:
        return False


ARRAY_KIND = {"b": "True/False values", "i": "whole numbers (int)", "u": "whole numbers (int)",
              "f": "decimals (float)", "c": "complex numbers", "U": "text (str)", "S": "bytes (b'...')",
              "O": "Python objects", "M": "dates", "m": "time spans"}


def kind_of(v):
    if isinstance(v, type):
        return "a type (written without quotes)"
    if is_dtype(v):
        return "a dtype"
    if v is None:
        return "None"
    if is_bool(v):
        return "a bool (True or False)"
    if is_whole(v):
        return "an int (a whole number)"
    if is_number(v):
        return "a float (a number with a point)"
    if isinstance(v, str):
        return "a str (text, in quotes)"
    if is_array(v):
        return f"an ndarray of {ARRAY_KIND.get(v.dtype.kind, v.dtype.name)} with shape {v.shape}"
    if is_frame(v):
        return f"a DataFrame with shape {v.shape}"
    if is_series(v):
        return f"a Series with {len(v)} values"
    if is_index(v):
        return "an Index (pandas' row/column labels)"
    if isinstance(v, PurePath):
        return "a Path"
    names = {list: "a list", dict: "a dict", tuple: "a tuple", set: "a set"}
    return names.get(type(v), f"a {type(v).__name__}")


# ── showing values the way you would TYPE them ─────────────────────────────────────────────────

DEFAULT_DTYPES = {"int64", "float64", "bool", "complex128"}


def show_value(v):
    if isinstance(v, type):
        if np is not None and v is np.ndarray:
            return "np.ndarray"
        if pd is not None and v in (pd.DataFrame, pd.Series, pd.Index):
            return f"pd.{v.__name__}"
        return "Path" if issubclass(v, PurePath) else v.__name__
    if is_dtype(v):
        return f"np.dtype({v.str!r})" if v.kind in "USV" else f"np.dtype({v.name!r})"
    if is_missing(v):
        return "None" if v is None else "np.nan"
    if is_bool(v):
        return repr(bool(v))
    if is_whole(v):
        return repr(int(v))
    if is_number(v):
        return repr(float(v))
    if np is not None and isinstance(v, np.str_):
        return repr(str(v))
    if is_array(v):
        inside = show_value(v.tolist())
        if v.size == 0 and v.dtype.kind not in "US":
            return f"np.array({inside}, dtype={v.dtype.name!r})"
        if v.dtype.kind == "U" or v.dtype.name in DEFAULT_DTYPES:
            return f"np.array({inside})"
        if v.dtype.kind == "S":
            return f"np.array({inside}, dtype={v.dtype.str!r})"
        return f"np.array({inside}, dtype={v.dtype.name!r})"
    if is_series(v):
        index = "" if isinstance(v.index, pd.RangeIndex) and v.index.start == 0 and v.index.step == 1 \
            else f", index={show_value(list(v.index))}"
        name = "" if v.name is None else f", name={show_value(v.name)}"
        return f"pd.Series({show_value(v.tolist())}{index}{name})"
    if is_frame(v):
        columns = "{" + ", ".join(f"{show_value(c)}: {show_value(v[c].tolist())}" for c in v.columns) + "}"
        index = "" if isinstance(v.index, pd.RangeIndex) and v.index.start == 0 and v.index.step == 1 \
            else f", index={show_value(list(v.index))}"
        return f"pd.DataFrame({columns}{index})"
    if is_index(v):
        return f"pd.Index({show_value(list(v))})"
    if pd is not None and isinstance(v, pd.Timestamp):
        return f"pd.Timestamp({str(v)!r})"
    if pd is not None and isinstance(v, pd.api.extensions.ExtensionDtype):
        return repr(str(v))
    if isinstance(v, PurePath):
        return f'Path("{v.as_posix()}")'
    if isinstance(v, list):
        return "[" + ", ".join(show_value(a) for a in v) + "]"
    if isinstance(v, tuple):
        inner = ", ".join(show_value(a) for a in v)
        return f"({inner},)" if len(v) == 1 else f"({inner})"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{show_value(k)}: {show_value(w)}" for k, w in v.items()) + "}"
    if isinstance(v, (set, frozenset)):
        return "{" + ", ".join(sorted(show_value(a) for a in v)) + "}" if v else "set()"
    if is_missing(v):
        return "None" if v is None else "np.nan"
    return repr(v)


# ── comparing ──────────────────────────────────────────────────────────────────────────────────

def numbers_equal(a, b):
    a, b = float(a), float(b)
    if math.isnan(a) and math.isnan(b):
        return True
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)


def arrays_equal(mine, real, mode):
    if mine.shape != real.shape:
        return False
    mk, rk = mine.dtype.kind, real.dtype.kind
    if mode == EXACT and ({mk, rk} - {"i", "u"}) and mk != rk:
        return False
    if (mk == "b") != (rk == "b") or (mk in "US") != (rk in "US"):
        return False
    if rk in "fc" or mk in "fc":
        return bool(np.allclose(mine, real, rtol=1e-9, atol=1e-12, equal_nan=True))
    return bool(np.array_equal(mine, real))


def same(mine, real, mode):
    if isinstance(real, type):
        return isinstance(mine, type) and (mine is real or issubclass(real, mine)
                                           or (mine in (Path, PurePath) and issubclass(real, PurePath)))
    if pd is not None and isinstance(real, pd.api.extensions.ExtensionDtype):   # pandas' own dtypes, like str
        try:
            return str(mine) == str(real) or bool(mine == real)
        except Exception:
            return False
    if is_dtype(real):
        if isinstance(mine, (list, dict, tuple, set)) or mine is None or is_bool(mine) or is_number(mine):
            return False
        try:
            return np.dtype(mine) == real
        except Exception:
            return False
    if isinstance(mine, type) or is_dtype(mine):
        return False
    if is_missing(real) or is_missing(mine):
        return is_missing(real) and is_missing(mine) and (real is None) == (mine is None)
    if is_bool(real) or is_bool(mine):
        return is_bool(real) and is_bool(mine) and bool(mine) == bool(real)
    if is_number(real) or is_number(mine):
        if not (is_number(real) and is_number(mine)):
            return False
        if mode == EXACT and is_whole(real) != is_whole(mine):
            return False
        return numbers_equal(mine, real)
    if isinstance(real, str) or isinstance(mine, str):
        return isinstance(mine, str) and isinstance(real, str) and str(mine) == str(real)
    if is_array(real) or is_array(mine):
        return is_array(real) and is_array(mine) and arrays_equal(mine, real, mode)
    if is_frame(real) or is_series(real) or is_index(real):
        return type(mine) is type(real) and frame_difference(mine, real, mode) is None
    if isinstance(real, PurePath):
        return isinstance(mine, PurePath) and Path(mine) == Path(real)
    if isinstance(real, (list, tuple)):
        return type(mine) is type(real) and len(mine) == len(real) and \
            all(same(a, b, mode) for a, b in zip(mine, real))
    if isinstance(real, dict):
        if not isinstance(mine, dict) or len(mine) != len(real):
            return False
        return all(k in mine and same(mine[k], w, mode) for k, w in real.items())
    if isinstance(real, (set, frozenset)):
        return isinstance(mine, (set, frozenset)) and mine == real
    try:
        return bool(mine == real) and type(mine) is type(real)
    except Exception:
        return False


def frame_difference(mine, real, mode):
    """None when the pandas things match, otherwise one plain-English line about the first difference."""
    if is_index(real):
        return None if list(mine) == list(real) else "the labels differ"
    if mine.shape != real.shape:
        return f"the shape differs: yours is {mine.shape}, it should be {real.shape}"
    if is_frame(real) and list(mine.columns) != list(real.columns):
        return f"the columns differ: yours are {list(mine.columns)}, they should be {list(real.columns)}"
    if is_series(real) and mine.name != real.name:
        return f"the Series' name differs: yours is {mine.name!r}, it should be {real.name!r}"
    if list(mine.index) != list(real.index):
        hint = ""
        if list(real.index) == list(range(len(real))):
            hint = ("\n   (after filtering or sorting, rows keep their old labels: .reset_index(drop=True) "
                    "numbers them 0, 1, 2 again)")
        return f"the index (row labels) differs: yours is {list(mine.index)[:8]}, it should be " \
               f"{list(real.index)[:8]}{hint}"
    columns = list(real.columns) if is_frame(real) else [None]
    for c in columns:
        a = mine[c] if c is not None else mine
        b = real[c] if c is not None else real
        for i, (x, y) in enumerate(zip(a.tolist(), b.tolist())):
            if not same(x, y, LOOSE):
                where_ = f"column {c!r}, " if c is not None else ""
                return f"{where_}row {real.index[i]!r}: yours is {show_value(x)}, it should be {show_value(y)}"
        if mode == EXACT and a.dtype.kind != b.dtype.kind and not ({a.dtype.kind, b.dtype.kind} <= {"i", "u"}):
            where_ = f"column {c!r}: " if c is not None else ""
            return f"{where_}the values look the same but the dtype differs ({a.dtype} vs {b.dtype})"
    return None


def why_wrong(mine, real, mode, said=None):
    said = said or ("you wrote" if mode == EXACT else "yours is")
    if isinstance(real, type) and isinstance(mine, str) and mine.strip() in (real.__name__, show_value(real)):
        return f"you wrote the text {mine!r}. Write the type itself, without quotes:  {show_value(real)}"
    if is_array(real) and isinstance(mine, (list, tuple)):
        return f"{said} a {type(mine).__name__}, but numpy gives an ndarray: write np.array({show_value(list(mine))})"
    if is_array(real) and is_array(mine):
        if mine.shape != real.shape:
            return f"{said} an array with shape {mine.shape}; the answer has shape {real.shape}"
        if mine.dtype.kind != real.dtype.kind:
            return (f"the right shape, but {said} {ARRAY_KIND.get(mine.dtype.kind, mine.dtype.name)}; "
                    f"the answer holds {ARRAY_KIND.get(real.dtype.kind, real.dtype.name)}")
        return f"the right shape and kind, but some values differ: {said} {show_value(mine)}"
    if (is_frame(real) and is_frame(mine)) or (is_series(real) and is_series(mine)) or \
            (is_index(real) and is_index(mine)):
        return frame_difference(mine, real, mode) or "the values differ"
    if is_number(real) and is_number(mine) and numbers_equal(mine, real) and is_whole(real) != is_whole(mine):
        return (f"the right number, but {said} {kind_of(mine)}. The answer is {kind_of(real)}"
                + (": numpy gives back a float here (it prints with a point)." if not is_whole(real) else "."))
    if kind_of(mine) != kind_of(real):
        return f"{said} {show_value(mine)}, which is {kind_of(mine)}. The answer is {kind_of(real)}."
    return f"{said} {show_value(mine)}: the right kind ({kind_of(real)}), but not the right value."


# ── running code safely ────────────────────────────────────────────────────────────────────────

def run(expr, env):
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
    text = str(err)
    if isinstance(err, NameError):
        return ("   A name Python doesn't know. Is the import line at the top of the file (import numpy as np,\n"
                "   import pandas as pd ...)? Are your setup lines there (like DATA = ...)?")
    if isinstance(err, KeyError):
        return "   That key / column isn't there. Probe it first: print(.keys()) or print(df.columns). Spelling? Case?"
    if isinstance(err, IndexError):
        return "   A position past the end. Probe it: len(...) or .shape. Positions start at 0."
    if isinstance(err, ValueError) and "truth value" in text:
        return ("   if / and / or on a WHOLE array or Series: Python can't turn many True/False values into one.\n"
                "   Use .any() / .all(), or & | ~ with brackets: (a > 1) & (a < 5)")
    if isinstance(err, ValueError) and ("reshape" in text or "broadcast" in text):
        return "   The shapes don't fit. Print .shape of each array: the sizes must match (or be 1)."
    if isinstance(err, FileNotFoundError):
        return "   No file there. Print the path you built: is the folder right? (Path(__file__).parent ...)"
    if isinstance(err, AttributeError):
        return "   That object has no such method/attribute. Probe it: type(thing), then dir(thing) or help(thing)."
    if isinstance(err, TypeError) and "not callable" in text:
        return "   Brackets after something that isn't a function: .shape and .dtype have no ( ); .sum() does."
    return ""


def snapshot(ns):
    kept = {}
    for name, value in ns.items():
        if name.isupper() and not callable(value) and not isinstance(value, type(sys)) \
                and not isinstance(value, PurePath):
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

    env = {**PRELOADED, **ns}
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
            notes.append(f"{name}   {expr}\n   Python gives an error: {type(result['error']).__name__}. "
                         "(Tell Claude: this question has a bug.)")
            continue
        real = result["value"]
        if same(mine, real, EXACT):
            right += 1
            continue
        why = why_wrong(mine, real, EXACT)
        if show:
            why += f"\n   Python gives:  {show_value(real)}"
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
        return "wrong", [f"There's no  def {name}(  or  class {name}  in the file any more. Renamed or deleted?"]
    if func is not None and not fix and is_placeholder(func):
        return "todo", ["Not started. Write your code in the function, in place of  pass."]
    if name is None and not fix:                      # a question with several functions in it
        defs = [find_def(tree, m[1]) for line in q.lines if (m := re.match(r"def (\w+)\(", line))]
        defs = [d for d in defs if d is not None]
        if defs and all(is_placeholder(d) for d in defs):
            return "todo", ["Not started. Replace the  ...  in the functions with your code."]
    if func is not None:
        body = source_lines[func.lineno - 1:func.end_lineno]
        if any("# PLAN" in line for line in body):
            filled = [m[1] for line in body if (m := NUMBERED.match(line)) and m[1].strip()]
            if len(filled) < 2:
                return "plan", ["Write the PLAN first: fill in the  # 1.  # 2.  ...  lines in plain English, one",
                                "step per line. Then run again and the code gets checked."]

    env = {**PRELOADED, **ns}
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
                f"   didn't finish in {TIMEOUT} seconds: a loop that never ends? (a while whose condition never",
                "   becomes False, or a list that grows while you loop over it)"]
            break
        if "error" in result:
            err = result["error"]
            first_fail = first_fail or [f"{left}", f"   crashed:  {type(err).__name__}: {err}",
                                        where(err, level_file), crash_hint(err)]
            continue
        got = result["value"]
        if got is ... and not fix:
            return "todo", ["Not finished. Replace every  ...  with your code."]
        if same(got, expected, LOOSE):
            passed += 1
            continue
        if first_fail is None and not visible:
            first_fail = [f"{left}", f"   yours gave    {show_value(got)}",
                          "   not right yet" + (f": the answer is {kind_of(expected)}" if kind_of(got) != kind_of(expected)
                                               else "")]
            if got is None and expected is not None:
                first_fail.append("   None means nothing was handed back: it PRINTS instead of RETURNING, or the "
                                  "return line is missing.")
        if first_fail is None:
            first_fail = [f"{left}",
                          f"   should give   {show_value(expected)}",
                          f"   yours gave    {show_value(got)}"]
            if got is None and expected is not None:
                first_fail.append("   None means nothing was handed back: it PRINTS instead of RETURNING, the return "
                                  "line is missing,\n   or the function never reaches it.")
            else:
                first_fail.append("   (" + why_wrong(got, expected, LOOSE) + ")")
            if result["printed"].strip():
                shown = "\n      ".join(result["printed"].strip().splitlines()[:4])
                first_fail.append(f"   it also printed:\n      {shown}")

    changed = [k for k in before if not same(ns.get(k), before[k], EXACT)]
    for k in changed:
        ns[k] = before[k]
    if changed and first_fail is None:
        first_fail = [f"It gives the right results, but it CHANGED {', '.join(changed)}: the data it was given.",
                      "A function should leave its input alone: work on a copy (.copy()) or build a new one."]

    if first_fail is None and passed == len(examples):
        return "done", []
    lines = [line for line in first_fail if line]
    lines.append(f"{passed} of {len(examples)} tests right.")
    if fix:
        lines.insert(0, "Still broken.")
    return ("todo" if fix else "wrong"), lines


# ── the report ─────────────────────────────────────────────────────────────────────────────────

def level(ns):
    """Called at the bottom of each level / project file with its globals()."""
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
        m = re.match(r"(level|project)_(\d+)", level_file.stem)
        nxt = sorted(level_file.parent.glob(f"{m[1]}_{int(m[2]) + 1:02d}_*.py")) if m else []
        if nxt:
            print(f"\n  Done!  Next:  python {level_file.parent.name}\\{nxt[0].name}")
        elif m and m[1] == "level":
            print("\n  That's the whole ladder! Next: the projects (projects\\README.md).")
        else:
            print("\n  Done! That's every project in this folder.")
    print()
