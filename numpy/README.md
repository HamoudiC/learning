# numpy/: numpy from start to full

Levels 1-5 are what your Colab notebook covered. Levels 6-11 are what comes next. Then 9 projects: the first 2
use only what your notebook covered, the other 7 need basic Python + all of numpy.

**Start with `ladder/level_01_arrays.py`.**

| Folder / file | What it is |
|---|---|
| `ladder/level_01..11_*.py` | **Where you type.** Each section says what to do and which bag to read. |
| `bags/NN_*.txt` | **Your documentation.** Every function: its syntax, then an example and what it does. |
| `projects/project_NN_*.py` | Bigger tasks. You write the import line yourself. |
| `ladder/check.py`, `answers.json` | The checker and the hidden answers it compares with. You don't edit them. |
| `data/`, `out/` | Files the tasks read / where your code saves files. |

## How it works

| Kind | What you do |
|---|---|
| **DO** | Under each task, delete `# your code here` and write your code on that line. Use the data above the tasks. |
| **WRITE** | Write the function: delete `pass` and write your code. |
| **FIX** | The function is broken. Fix it. |

Each section starts with a **Bags:** line: the bag file and the sections in it to read. Run the file after every
task: ✅ done, ❌ not right yet (it says what kind of answer it expected), ⬜ not started.

## The levels

| Level | File | What it covers | Bags |
|---|---|---|---|
| 1 | `level_01_arrays.py` | making arrays, ndim, shape, size, list vs array | `01` |
| 2 | `level_02_indexing_and_slicing.py` | positions, slices, rows, columns, 3D | `02` |
| 3 | `level_03_dtypes.py` | dtypes and converting | `02` |
| 4 | `level_04_copy_and_view.py` | same array, view or copy | `02` |
| 5 | `level_05_shape_and_reshape.py` | reshape, flatten, transpose | `01` |
| 6 | `level_06_making_arrays.py` | ready-made arrays, random numbers | `01` |
| 7 | `level_07_maths_and_broadcasting.py` | maths on whole arrays, shapes that fit together | `03` |
| 8 | `level_08_aggregations.py` | sum, mean, max, running totals, axis | `03` |
| 9 | `level_09_masks_and_where.py` | picking values that match, np.where, unique, missing values | `04` |
| 10 | `level_10_join_split_sort.py` | joining, splitting, sorting | `04` |
| 11 | `level_11_linear_algebra_and_files.py` | matrices, comparing decimals, files | `05` |

## The projects

| Project | What you build | Needs |
|---|---|---|
| 1 `cinema_seats` | a seat map: make the hall, find "B3", book a seat, count free seats | levels 1-5 |
| 2 `pixel_art` | an image editor: crop, mirror, flip, rotate, shrink, draw as text | levels 1-5 |
| 3 `gradebook` | averages, who failed, curving marks, report cards, a ranking | levels 1-9 |
| 4 `game_of_life` | Conway's Game of Life | levels 1-9 |
| 5 `weather` | missing readings, moving averages, hottest week, reading a CSV | levels 1-11 |
| 6 `monte_carlo` | estimate pi, dice odds, the birthday paradox, random walks | levels 1-9 |
| 7 `linear_regression` | fit a line two ways, measure it, gradient descent | levels 1-11 |
| 8 `knn_classifier` | k-nearest neighbours from scratch, accuracy | levels 1-10 |
| 9 `gold_backtest` | returns, moving-average crossover, no look-ahead, drawdown | levels 1-10 |

`bags/00_python_basics.txt` has the plain-Python pieces the projects use (text, lists, loops, numbers).

## Commands (PowerShell)

```powershell
cd C:\Users\hamou\Downloads\allMyLearning\numpy
```

```powershell
python ladder\level_01_arrays.py
```

```powershell
python projects\project_01_cinema_seats.py
```
