# pandas/: pandas from start to full

Tables in Python: load, clean, filter, group, join and save. 10 levels, then 6 projects that use basic Python +
pandas. Uses pandas 3.1 (installed for your `python`).

**Start with `ladder/level_01_series.py`.**

| Folder / file | What it is |
|---|---|
| `ladder/level_01..10_*.py` | **Where you type.** Each section says what to do and which bag to read. |
| `bags/NN_*.txt` | **Your documentation.** Every function: its syntax, then an example and what it does. |
| `projects/project_NN_*.py` | Bigger tasks. You write the setup lines yourself (the imports and `DATA`). |
| `ladder/check.py`, `answers.json` | The checker and the hidden answers it compares with. You don't edit them. |
| `data/`, `out/` | The CSV files the tasks read / where your code saves files. |

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
| 1 | `level_01_series.py` | Series, labels vs positions, lining up by label | `01` |
| 2 | `level_02_dataframes.py` | tables: looking, columns, rows, cells, making them | `01` |
| 3 | `level_03_reading_files.py` | reading and saving CSV and Excel | `02` |
| 4 | `level_04_choosing_rows.py` | choosing rows by position, label, condition | `03` |
| 5 | `level_05_changing_data.py` | new columns, sorting, renaming, types | `03` |
| 6 | `level_06_cleaning.py` | missing values, text, duplicates | `04` |
| 7 | `level_07_grouping.py` | groupby, several answers at once, counting | `05` |
| 8 | `level_08_combining.py` | merge, concat | `05` |
| 9 | `level_09_dates.py` | dates, per month, rolling, shift, % change | `06` |
| 10 | `level_10_reshaping_and_output.py` | wide/long, pivot tables, handing data on | `06` |

## The projects

| Project | What you build | Needs |
|---|---|---|
| 1 `sales_report` | revenue, totals per region/product, monthly totals, a saved report | levels 1-7 |
| 2 `student_records` | students joined with programs: credits left, honours, at-risk, progress | levels 1-8 |
| 3 `contact_cleaner` | clean a messy contact list, then print contact cards | levels 1-6 |
| 4 `inbox_stats` | an inbox: emails per sender, busiest hour, search, domains | levels 1-9 |
| 5 `gold_prices` | returns, weekly closes, monthly ranges, signals, a no-look-ahead backtest | levels 1-9 |
| 6 `expense_tracker` | sort a bank statement into categories, monthly savings, over budget | levels 1-10 |

`bags/00_python_basics.txt` has the plain-Python pieces the projects use.

## Commands (PowerShell)

```powershell
cd C:\Users\hamou\Downloads\allMyLearning\pandas
```

```powershell
python ladder\level_01_series.py
```
