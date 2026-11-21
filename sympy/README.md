# sympy/: SymPy from start to full

Maths with letters: algebra, solving, limits, derivatives, integrals, series, matrices and differential
equations, with exact answers. Levels 4-7 follow MTH 112 (Calculus 1).

**Start with `ladder/level_01_symbols.py`.**

| Folder / file | What it is |
|---|---|
| `ladder/level_01..11_*.py` | **Where you type.** Each section says what to do and which bag to read. |
| `bags/NN_*.txt` | **Your documentation.** Every function: its syntax, then an example and what it does. |
| `ladder/check.py`, `answers.json` | The checker and the hidden answers it compares with. You don't edit them. |

## How it works

| Kind | What you do |
|---|---|
| **DO** | Under each task, delete `# your code here` and write your code on that line. Use the data above the tasks. The **form** counts: `(x + 1)**2` and `x**2 + 2*x + 1` are different answers. |
| **WRITE** | Write the function: delete `pass` and write your code. Any equal form counts. |
| **FIX** | The function is broken. Fix it. |

Each section starts with a **Bags:** line: the bag file and the sections in it to read. Run the file after every
task: ✅ done, ❌ not right yet (it says what kind of answer it expected), ⬜ not started.

## The levels

| Level | File | What it covers | MTH 112 | Bags |
|---|---|---|---|---|
| 1 | `level_01_symbols.py` | symbols, exact numbers, swapping in values, decimals | | `01` |
| 2 | `level_02_algebra.py` | expand, factor, tidying, trig, logs | week 1 | `02` |
| 3 | `level_03_solving.py` | solve, sets of answers, inequalities, decimal answers | | `03` |
| 4 | `level_04_functions_and_limits.py` | functions, limits, one side or both | weeks 1-3 | `04` |
| 5 | `level_05_derivatives.py` | derivatives, the rules, slopes, implicit | weeks 4-6 | `05` |
| 6 | `level_06_using_derivatives.py` | critical points, shape, max and min, optimisation | weeks 7, 9 | `06` |
| 7 | `level_07_integrals.py` | integrals, substitution, Riemann sums, area | weeks 10-12 | `07` |
| 8 | `level_08_sums_and_series.py` | sums, infinite series, Taylor polynomials | | `08` |
| 9 | `level_09_matrices.py` | matrices, solving systems, eigenvalues | | `09` |
| 10 | `level_10_differential_equations.py` | differential equations | | `10` |
| 11 | `level_11_whole_tasks.py` | 5 whole tasks; you write the import and setup lines too | all | all |

`bags/11_output_and_numbers.txt` (printing, LaTeX, typed maths, graphs) and `bags/00_python_basics.txt` (plain
Python) have no level of their own.

## Commands (PowerShell)

```powershell
cd C:\Users\hamou\Downloads\allMyLearning\sympy
```

```powershell
python ladder\level_01_symbols.py
```
