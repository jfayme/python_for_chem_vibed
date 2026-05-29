"""Build the seven 'Python for Chemists' lecture notebooks with nbformat.

Run from the repository root with the ``chem-python`` environment active:

    python build/build_notebooks.py

Each ``build_NN_*`` function returns a list of notebook cells; ``write_notebook``
assembles them into a ``.ipynb`` under ``notebooks/``. The notebooks are written
with **no outputs** — students get the satisfaction of running the cells
themselves. (Execution is verified separately during the build.)

Cell sources are written as raw triple-quoted strings so that what you read here
is exactly what lands in the notebook (no escaping surprises). Cells that
contain a Python docstring use raw triple-SINGLE-quoted wrappers instead.

British English is used throughout (the course style).
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent
NB_DIR = REPO_ROOT / "notebooks"

KERNELSPEC = {
    "display_name": "Python 3 (ipykernel)",
    "language": "python",
    "name": "python3",
}
LANGUAGE_INFO = {
    "name": "python",
    "mimetype": "text/x-python",
    "file_extension": ".py",
    "pygments_lexer": "ipython3",
}


def md(src: str):
    return new_markdown_cell(src.strip("\n"))


def code(src: str):
    return new_code_cell(src.strip("\n"))


def write_notebook(filename: str, cells: list) -> None:
    nb = new_notebook(cells=cells)
    nb.metadata["kernelspec"] = KERNELSPEC
    nb.metadata["language_info"] = LANGUAGE_INFO
    NB_DIR.mkdir(parents=True, exist_ok=True)
    path = NB_DIR / filename
    nbformat.write(nb, path)
    print(f"Wrote {path.relative_to(REPO_ROOT)} ({len(cells)} cells)")


# ===========================================================================
# Notebook 01 — Notebooks
# ===========================================================================
def build_01():
    C = []

    C.append(md(r"""
# Lecture 01 — Notebooks

*Getting comfortable with the tool you will use for everything else: the Jupyter notebook.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- explain what a Jupyter notebook is, and how a **code cell** differs from a **text (markdown) cell**;
- **run a cell** and explain why the **order** you run cells in matters;
- use Python as a **calculator** (`+ - * / ** %`) and show results with `print()`;
- write **comments** to leave notes for your future self;
- find **help** on anything with `help()` and `?`;
- run a real cheminformatics demo (drawing a molecule from its formula) — a taste of what is coming.
"""))

    C.append(md(r"""
## Why should a chemist learn to code?

You already do calculations every day: molar masses, dilutions, fitting a calibration line. Doing them by hand (or in a spreadsheet) is fine for one or two values. It becomes slow and error-prone the moment you have a hundred.

Three reasons coding is worth your time as a chemist:

- **Reproducibility.** A script records *exactly* what you did. Anyone (including future-you) can re-run it and get the same answer — no "which cells did I click?" mystery.
- **Automating the tedious.** Convert 200 absorbance readings to concentrations, or compute the molar mass of every molecule in a list, in one go.
- **Handling real data.** Spectra, large datasets and chemical structures are awkward by hand but natural in code.

The goal of this course is **generic Python**, but every example is wrapped in chemistry so it feels relevant. The Python is the real lesson; the chemistry is the motivation.
"""))

    C.append(md(r"""
## A one-paragraph reminder about conda

You have already created your working environment with **conda** (see `SETUP.md`). The one-line reason it exists: conda gave you an isolated **toolbox** called `chem-python` containing Python and all the scientific packages this course needs (NumPy, matplotlib, pandas and the chemistry toolkit **RDKit**), kept separate from anything else on your computer. As long as you launched these notebooks with that environment active, everything below will just work.
"""))

    C.append(md(r"""
## Meet the notebook: text cells and code cells

This document is a **Jupyter notebook**. It is built from **cells**, stacked top to bottom. There are two kinds:

- **Markdown (text) cells** — like this one. They hold formatted prose: headings, **bold**, lists, the lot. They are for *reading*.
- **Code cells** — they hold Python. When you **run** one, Python executes it and shows the result just underneath.

To run the cell below, click on it and press **Shift + Enter**. (Plain Enter just adds a new line inside the cell.)
"""))

    C.append(code(r"""
print("Hello! This is a code cell. You just ran some Python.")
"""))

    C.append(md(r"""
Notice the `[1]` that appeared to the left of the cell after you ran it. That number is the **execution count** — it tells you the order in which cells were run. The first cell you run shows `[1]`, the next `[2]`, and so on. Keep an eye on it; it matters more than you might think (see below).
"""))

    C.append(md(r"""
## Python as a calculator

The simplest use of a code cell is arithmetic. Run this:
"""))

    C.append(code(r"""
2 + 3
"""))

    C.append(md(r"""
A code cell automatically displays the value of its **last line**, so you did not even need `print()` there. The arithmetic operators are mostly what you would expect:

| Symbol | Meaning |
| --- | --- |
| `+` | add |
| `-` | subtract |
| `*` | multiply |
| `/` | divide |
| `**` | raise to a power (e.g. `2 ** 3` is 2 cubed) |
| `%` | remainder after division (the "modulo") |

Run the next cell to see them in action:
"""))

    C.append(code(r"""
print(10 - 4)      # subtraction
print(6 * 7)       # multiplication
print(2 ** 10)     # 2 to the power 10
print(20 / 8)      # division (note the decimal point in the answer)
"""))

    C.append(md(r"""
> **🧪 Chemistry aside — molar mass**
>
> The **molar mass** of a molecule is the sum of the atomic masses of all its atoms, in grams per mole (g/mol). For water, H₂O, that is two hydrogen atoms (about 1.008 each) plus one oxygen atom (about 15.999). We can work it out by just *typing the arithmetic*.
"""))

    C.append(code(r"""
# Molar mass of water (H2O), in g/mol, typed out directly.
2 * 1.008 + 15.999
"""))

    C.append(md(r"""
That single number, 18.015 g/mol, is the molar mass of water. You have just done your first piece of computational chemistry — it was only arithmetic, but everything we build later starts here.
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Carbon dioxide, CO₂, has one carbon atom (atomic mass ≈ 12.011) and two oxygen atoms (≈ 15.999 each). Work out its molar mass by typing the arithmetic into the cell below.
"""))

    C.append(code(r"""
# Your code here: compute the molar mass of CO2.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
# One carbon plus two oxygens.
12.011 + 2 * 15.999
"""))

    C.append(md(r"""
## A feel for division

Python has two kinds of division, and the difference trips everyone up at first. There is no theory to learn here — just run the cell and *notice* what happens.
"""))

    C.append(code(r"""
print(7 / 2)      # "normal" division -> a decimal answer
print(7 // 2)     # floor division -> throws away the bit after the point
print(7 % 2)      # remainder -> what is left over
"""))

    C.append(md(r"""
So `7 / 2` is `3.5`, `7 // 2` is `3` (how many whole 2s fit into 7), and `7 % 2` is `1` (the leftover). You will mostly want plain `/`. The other two are handy now and then — for example, `%` quickly tells you whether a number is even (`n % 2` is `0`) or odd.
"""))

    C.append(md(r"""
## Comments: notes to your future self

Anything after a `#` on a line is a **comment**. Python ignores it completely — it is purely for humans reading the code. Good comments explain *why* you did something, not *what* the code obviously does.
"""))

    C.append(code(r"""
# Avogadro's number (particles per mole) — useful constant to keep nearby.
6.022e23 * 2     # the e23 means "times 10 to the 23"; this is 2 moles' worth
"""))

    C.append(md(r"""
## `print()`: seeing what happened

A code cell only displays its **last** value automatically. If you want to see several results from one cell, wrap each in `print()`. Beginners should `print()` generously — it is how you *see* what your code is doing.
"""))

    C.append(code(r"""
print("Molar mass of water:", 2 * 1.008 + 15.999, "g/mol")
print("Molar mass of CO2:  ", 12.011 + 2 * 15.999, "g/mol")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

In the cell below, (1) add a comment describing what you are doing, then (2) use `print()` to display a short sentence of your choice and the molar mass of molecular oxygen, O₂ (two oxygen atoms).
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
# Report the molar mass of an oxygen molecule, O2.
print("Oxygen gas is O2.")
print("Its molar mass is", 2 * 15.999, "g/mol")
"""))

    C.append(md(r"""
## Execution order matters

This is the single most common source of confusion for beginners, so read carefully.

A notebook remembers everything you have run, in the order you ran it — **not** the order the cells appear on the page. If you run a cell at the bottom, then one at the top, the bottom one happened *first* as far as Python is concerned.

We will meet **variables** properly next lecture. For now, just copy the next cell: it gives the name `reading` to the number `0.84` (think of it as storing an absorbance measurement under a label).
"""))

    C.append(code(r"""
reading = 0.84          # store a value under the name "reading" (just copy this for now)
print("Stored reading =", reading)
"""))

    C.append(code(r"""
# This cell uses the name we just created.
print("Double the reading is", reading * 2)
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Try to break it on purpose — this teaches the lesson better than any explanation:

1. Click the **last** cell above (the one printing `reading * 2`) and use the menu **Kernel → Restart Kernel** to wipe Python's memory.
2. Now run **only** that last cell, *without* running the `reading = 0.84` cell first.

You will get a `NameError` saying `reading` is not defined — because, in the order you ran things, Python had never heard of it yet. Then run the two cells top-to-bottom and watch it work. **Lesson:** if a cell suddenly errors, the usual fix is *Kernel → Restart Kernel and Run All*, which runs everything cleanly from the top.
"""))

    C.append(md(r"""
## Getting help

You will never remember everything, and you do not need to. Two ways to ask Python for help:

- `help(thing)` prints a description of `thing`.
- Putting a `?` after a name does the same in a notebook, in a pop-up panel.

Run these:
"""))

    C.append(code(r"""
help(round)     # round() rounds a number to a given number of decimal places
"""))

    C.append(code(r"""
# The ? form opens a help panel at the bottom of the screen. Run it and have a look.
abs?
"""))

    C.append(md(r"""
For example, `round` is handy for tidying up a molar mass to two decimal places:
"""))

    C.append(code(r"""
round(2 * 1.008 + 15.999, 2)      # round water's molar mass to 2 decimal places
"""))

    C.append(md(r"""
## ⚗️ With RDKit — your first molecule

Here is a glimpse of where this course is going. **RDKit** is a professional chemistry toolkit (it is one of the packages conda installed for you). The code below turns a **SMILES string** — a compact text recipe for a molecule — into a picture of caffeine.

You are **not** expected to understand this yet. Just run it: by the end of the course you will know exactly what every line does. It also doubles as a check that conda and RDKit installed correctly — if a caffeine molecule appears, you are good to go.
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Draw

# "Cn1cnc2c1c(=O)n(C)c(=O)n2C" is the SMILES recipe for caffeine.
caffeine = Chem.MolFromSmiles("Cn1cnc2c1c(=O)n(C)c(=O)n2C")
Draw.MolToImage(caffeine, size=(320, 280))
"""))

    C.append(md(r"""
> **A note on saving your work.** These `.ipynb` notebooks live as files on your disk, so when you save (Ctrl+S) your work is safely stored. You may also meet a browser-based version of this workshop built with **marimo**, which runs entirely in the web page — convenient, but it can *lose your work if the browser cache is cleared*. With the local notebooks you are using here, that cannot happen.
"""))

    C.append(md(r"""
## Key takeaways

- A notebook is made of **markdown cells** (text) and **code cells** (Python); run a cell with **Shift + Enter**.
- A code cell shows the value of its **last line**; use `print()` to show more than one thing.
- Python is a capable calculator: `+ - * / ** %`, with `/` giving decimals and `//` / `%` giving whole quotient / remainder.
- **Execution order matters** — the notebook remembers what you ran, in the order you ran it. *Restart Kernel and Run All* fixes a muddled state.
- `#` starts a **comment**; `help()` and `?` get you help on anything.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **Variables** — we stop typing raw numbers and start giving them names, and meet the building blocks (strings, lists and dictionaries) that let us store a molecule's data properly.
"""))

    return C


# ===========================================================================
# Notebook 02 — Variables
# ===========================================================================
def build_02():
    C = []

    C.append(md(r"""
# Lecture 02 — Variables

*Giving names to things: numbers, text, lists and look-up tables — using molecules as our data.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- create **variables** and explain what assignment (`=`) does;
- recognise the core **types**: `int`, `float`, `str`, `bool`, and check them with `type()`;
- work with **strings**: quotes, joining, f-strings, `.upper()`, `.replace()`, `len()`;
- build and use **lists**: indexing, slicing, `.append()`;
- build and use **dictionaries** as look-up tables (e.g. element → atomic mass);
- store a molecule's data tidily in variables and a small dictionary.
"""))

    C.append(md(r"""
## Recap of Lecture 01

- A notebook is **markdown** + **code** cells; run a cell with **Shift + Enter**.
- Python is a calculator (`+ - * / ** %`) and `print()` shows results.
- **Execution order matters**; *Restart Kernel and Run All* fixes a muddled notebook.
"""))

    C.append(md(r"""
## Variables: names for values

A **variable** is a name that points at a value. You create one with `=` (read it as "is set to", *not* "equals" in the maths sense). Once named, you can use it as many times as you like — and change it.
"""))

    C.append(code(r"""
molar_mass_water = 18.015      # store the value under a clear name
print(molar_mass_water)
print(molar_mass_water * 3)    # three moles' worth
"""))

    C.append(md(r"""
Two habits worth forming now:

- **Choose clear names.** `molar_mass` tells the reader what it is; `mm` or `x` does not.
- Names use **`snake_case`**: lower-case words joined by underscores. They cannot start with a number or contain spaces.
"""))

    C.append(md(r"""
## Types: what kind of value is it?

Every value has a **type**. The four you will meet constantly:

- **`int`** — a whole number, e.g. `6`.
- **`float`** — a number with a decimal point, e.g. `18.015`.
- **`str`** — a *string*, which is just **text**, written in quotes, e.g. `"ethanol"`.
- **`bool`** — a truth value, either `True` or `False`.

`type()` tells you which is which.
"""))

    C.append(code(r"""
print(type(6))
print(type(18.015))
print(type("ethanol"))
print(type(True))
"""))

    C.append(md(r"""
## Strings: text is data too

A **string** is just text. You write it inside quotes — single `'...'` or double `"..."`, your choice (be consistent). Strings are everywhere in chemistry data: molecule names, formulae, and SMILES are all text.

> **🧪 Chemistry aside — SMILES**
>
> A **SMILES** string is a text recipe for a molecule: a short line of characters that encodes which atoms are bonded to which. For example, ethanol is `"CCO"` (two carbons and an oxygen). For now, treat a SMILES simply as *a string* — text that happens to describe a molecule.
"""))

    C.append(code(r"""
name = "ethanol"
formula = "C2H6O"
smiles = "CCO"
print(name, "has formula", formula, "and SMILES", smiles)
"""))

    C.append(md(r"""
You can **join** (concatenate) strings with `+`, and find a string's length with `len()`:
"""))

    C.append(code(r"""
greeting = "Molecule: " + name
print(greeting)
print("The name has", len(name), "characters")
"""))

    C.append(md(r"""
Strings come with built-in **methods** — actions you call by writing a dot after the string. Two useful ones: `.upper()` (capitalise everything) and `.replace(old, new)`.
"""))

    C.append(code(r"""
print(name.upper())                 # ETHANOL
print(formula.replace("6", "5"))    # swap a character (just to see .replace at work)
"""))

    C.append(md(r"""
### f-strings: the tidy way to build text

An **f-string** lets you drop a value straight into a string. Put an `f` before the opening quote and wrap any value in `{curly braces}`. You can even format numbers — `{value:.2f}` means "show 2 decimal places".
"""))

    C.append(code(r"""
molar_mass = 46.07     # ethanol, g/mol
print(f"The molar mass of {name} is {molar_mass:.2f} g/mol")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Make three variables for **water**: its name (`"water"`), its formula (`"H2O"`) and its molar mass (`18.015`). Then print a sentence using an **f-string** that reports the molar mass to **2 decimal places**.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
water_name = "water"
water_formula = "H2O"
water_mass = 18.015
print(f"{water_name.upper()} ({water_formula}) has a molar mass of {water_mass:.2f} g/mol")
"""))

    C.append(md(r"""
## Lists: an ordered collection

A **list** holds several values in order, inside square brackets `[...]`. The values can be anything — here, a list of molecule names.
"""))

    C.append(code(r"""
molecules = ["water", "ethanol", "caffeine", "aspirin", "glucose"]
print(molecules)
print("There are", len(molecules), "molecules in the list")
"""))

    C.append(md(r"""
### Indexing: counting from zero

You reach an item by its **position (index)** in square brackets. The crucial, everyone-trips-on-it rule: **counting starts at 0**. So the first item is index `0`, the second is `1`, and so on. Negative indices count from the end (`-1` is the last).
"""))

    C.append(code(r"""
print(molecules[0])     # the FIRST item
print(molecules[1])     # the second item
print(molecules[-1])    # the last item
"""))

    C.append(md(r"""
### Slicing: taking a range

A **slice** `list[start:stop]` gives you several items at once. It includes `start` but **stops just before** `stop` (another off-by-one habit to absorb).
"""))

    C.append(code(r"""
print(molecules[0:3])   # items 0, 1, 2 (NOT 3)
print(molecules[2:])    # from item 2 to the end
"""))

    C.append(md(r"""
### Growing a list

Lists can change. `.append()` adds an item to the end.
"""))

    C.append(code(r"""
molecules.append("benzene")
print(molecules)
print("Now there are", len(molecules), "molecules")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Using the `molecules` list above: (1) print the **third** molecule (mind the zero-based counting!); (2) print a slice of the **last two** molecules; (3) `.append()` a new molecule of your choice and print the updated list.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
print(molecules[2])         # third item is at index 2
print(molecules[-2:])       # last two items
molecules.append("methane")
print(molecules)
"""))

    C.append(md(r"""
> **A quick word on tuples.** You will occasionally see round brackets, e.g. `(1.008, 15.999)`. That is a **tuple** — think of it as a *fixed list* that cannot be changed after it is made. We will not dwell on them; just recognise the shape if you meet one.
"""))

    C.append(md(r"""
## Dictionaries: look-up tables

A **list** is great when order matters. But often you want to look something up *by name* — like finding an element's atomic mass from its symbol. That is a **dictionary**: a set of **key → value** pairs, written with curly braces `{key: value, ...}`.

This is the single most useful data structure for a chemist, so meet the headline example: a dictionary mapping each **element symbol to its atomic mass**.
"""))

    C.append(code(r"""
atomic_mass = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
}
print(atomic_mass)
"""))

    C.append(md(r"""
You **look up** a value by its key, in square brackets — just like a list, but with the key instead of a number:
"""))

    C.append(code(r"""
print("Atomic mass of carbon:", atomic_mass["C"])
print("Atomic mass of oxygen:", atomic_mass["O"])

# Build water's molar mass from the dictionary: 2 H + 1 O
water_molar_mass = 2 * atomic_mass["H"] + atomic_mass["O"]
print(f"Molar mass of water = {water_molar_mass:.3f} g/mol")
"""))

    C.append(md(r"""
You can **add** a new entry by assigning to a new key:
"""))

    C.append(code(r"""
atomic_mass["S"] = 32.06     # add sulphur
print(atomic_mass)
"""))

    C.append(md(r"""
### Storing one molecule's data in a dictionary

Dictionaries are also a tidy way to keep all of one molecule's facts together:
"""))

    C.append(code(r"""
ethanol = {
    "name": "ethanol",
    "formula": "C2H6O",
    "smiles": "CCO",
    "molar_mass": 46.07,
}
print(f"{ethanol['name']} has SMILES {ethanol['smiles']}")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

(1) Look up the atomic mass of **nitrogen** in `atomic_mass`. (2) Add **phosphorus** (`"P"`, mass `30.974`) to the dictionary. (3) Using the dictionary, compute the molar mass of **methane**, CH₄ (one carbon, four hydrogens), and print it to 3 decimal places.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
print("Nitrogen:", atomic_mass["N"])
atomic_mass["P"] = 30.974
methane_mass = atomic_mass["C"] + 4 * atomic_mass["H"]
print(f"Molar mass of methane = {methane_mass:.3f} g/mol")
"""))

    C.append(md(r"""
## ⚗️ With RDKit — a string becomes a molecule

You now understand the *input* to the demo from Lecture 01: a SMILES is just a **string**. RDKit's job is to read that string and build a **molecule object** you can compute with and draw. Watch the type change from a humble `str` to an RDKit molecule:
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole   # makes molecules draw themselves in the notebook

smiles = "CCO"               # this is a string (str) — exactly what we learnt above
print("Type of the SMILES:", type(smiles))

mol = Chem.MolFromSmiles(smiles)   # RDKit turns the string into a molecule object
print("Type after RDKit:   ", type(mol))
mol                          # display the molecule
"""))

    C.append(md(r"""
The molecule **object** itself is a job for later notebooks — for now, the point is simply that the thing you feed RDKit is a string, the most ordinary data type there is.
"""))

    C.append(md(r"""
## Key takeaways

- A **variable** names a value; assign with `=` and use clear `snake_case` names.
- Core types: **`int`**, **`float`**, **`str`** (text), **`bool`** (`True`/`False`); check with `type()`.
- **Strings** are text: join with `+`, measure with `len()`, transform with `.upper()`/`.replace()`, and build neatly with **f-strings** (`{value:.2f}`).
- **Lists** hold ordered items; indexing starts at **0**; slice with `[start:stop]`; grow with `.append()`.
- **Dictionaries** map **keys → values** — perfect for look-ups like element → atomic mass.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **Functions** — we package the molar-mass calculation into a reusable tool you can call by name, instead of retyping the arithmetic every time.
"""))

    return C


# ===========================================================================
# Notebook 03 — Functions
# ===========================================================================
def build_03():
    C = []

    C.append(md(r"""
# Lecture 03 — Functions

*Packaging a calculation once, then reusing it: building a `molar_mass()` tool by hand.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- define a **function** with `def`, give it **parameters**, and `return` a result;
- explain *why* functions are worth the effort;
- give a parameter a **default value**;
- write a **docstring** to document what a function does;
- understand, at a beginner level, that variables inside a function are **private** (scope);
- **import** modules and libraries (`import math`, `from rdkit import Chem`).
"""))

    C.append(md(r"""
## Recap of Lecture 02

- **Variables** name values; core types are `int`, `float`, `str`, `bool`.
- **Lists** hold ordered items (indexing from 0); **dictionaries** map keys → values.
- We built an `atomic_mass` dictionary and used it to compute molar masses by hand.
"""))

    C.append(md(r"""
## The problem functions solve

Last lecture we computed a molar mass like this:

```python
water = 2 * atomic_mass["H"] + atomic_mass["O"]
```

That is fine once. But for ethanol, then caffeine, then fifty more, you would copy-paste-and-edit that line over and over — tedious, and every copy is a fresh chance to make a mistake. A **function** lets you write the recipe **once**, give it a name, and run it as often as you like with different inputs.
"""))

    C.append(md(r"""
## Defining your first function

The shape of a function definition:

```python
def function_name(parameters):
    body, indented
    return result
```

- `def` starts the definition; the name follows the same `snake_case` rules as variables.
- The **parameters** in brackets are the inputs.
- The indented lines are the **body** — what the function does.
- `return` hands a value back to whoever called the function.

Here is a tiny one that doubles a number:
"""))

    C.append(code(r"""
def double(x):
    return x * 2

# "Calling" the function: give it an input, get a result back.
print(double(21))
print(double(18.015))     # works on any number
"""))

    C.append(md(r"""
**Indentation is part of the syntax in Python.** The body of the function is the indented block. Jupyter adds the four spaces for you after the colon; just do not remove them.
"""))

    C.append(md(r"""
## A real one: `molar_mass()`

Let us turn the molar-mass arithmetic into a proper tool. First we need the atomic-mass dictionary from last lecture, then a function that takes a molecule described as a dictionary of `{element: count}`.
"""))

    C.append(code(r"""
atomic_mass = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
}

def molar_mass(composition):
    total = 0.0
    for element, count in composition.items():     # go through each element and its count
        total = total + count * atomic_mass[element]
    return total
"""))

    C.append(md(r"""
> The `for ... in ...` line is a **loop** — it walks through each entry in the dictionary. We will study loops properly next lecture; for now, read it as "for each element and its count, add that element's contribution to the total." Just copy it.

Now call it with a few molecules, each described as a `{element: count}` dictionary:
"""))

    C.append(code(r"""
print("Water:  ", molar_mass({"H": 2, "O": 1}), "g/mol")
print("Ethanol:", molar_mass({"C": 2, "H": 6, "O": 1}), "g/mol")
print("Methane:", molar_mass({"C": 1, "H": 4}), "g/mol")
"""))

    C.append(md(r"""
Write the recipe once, reuse it everywhere — that is the whole point of a function.
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Use `molar_mass()` to compute the molar mass of **carbon dioxide**, CO₂ (`{"C": 1, "O": 2}`), and of **glucose**, C₆H₁₂O₆. Print both with a sensible f-string.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
print(f"CO2 molar mass:     {molar_mass({'C': 1, 'O': 2}):.3f} g/mol")
print(f"Glucose molar mass: {molar_mass({'C': 6, 'H': 12, 'O': 6}):.3f} g/mol")
"""))

    C.append(md(r"""
## Parameters, return values and a second function

A function can take **several** parameters. Here is one that converts a mass in grams to an amount in moles, using the familiar `n = m / M`.
"""))

    C.append(code(r"""
def moles_from_mass(mass_g, molar_mass_g_per_mol):
    "Return the amount in moles for a given mass (g) and molar mass (g/mol)."
    return mass_g / molar_mass_g_per_mol

# How many moles in 9.0 g of water?
amount = moles_from_mass(9.0, 18.015)
print(f"{amount:.3f} mol")
"""))

    C.append(md(r"""
## Default arguments

You can give a parameter a **default value**, used when the caller does not supply one. Suppose we usually weigh things in grams but occasionally in milligrams:
"""))

    C.append(code(r"""
def moles(mass, molar_mass_g_per_mol, mass_in_mg=False):
    if mass_in_mg:
        mass = mass / 1000        # convert mg to g first
    return mass / molar_mass_g_per_mol

print(moles(9.0, 18.015))                 # grams (the default)
print(moles(9000, 18.015, mass_in_mg=True))   # milligrams — same physical amount
"""))

    C.append(md(r"""
## Docstrings: documenting a function

A **docstring** is a string written as the very first line of a function body, in triple quotes. It explains what the function does. It is what `help()` shows, so it is worth writing.
"""))

    C.append(code(r'''
def molar_mass(composition):
    """Return the molar mass (g/mol) of a molecule.

    composition: a dictionary mapping element symbol -> number of atoms,
                 e.g. {"C": 2, "H": 6, "O": 1} for ethanol.
    """
    total = 0.0
    for element, count in composition.items():
        total += count * atomic_mass[element]   # += means "add to the running total"
    return total

help(molar_mass)
'''))

    C.append(md(r"""
## Scope: what happens in a function stays in a function

The variable `total` inside `molar_mass` is **private** to the function. It is created fresh each call and vanishes when the function returns — you cannot see it from outside. This is a feature, not a bug: it means a function cannot accidentally clobber your other variables.
"""))

    C.append(code(r"""
result = molar_mass({"H": 2, "O": 1})
print("The function returned:", result)

# Trying to use the function's private variable from outside fails — uncomment to see:
# print(total)     # -> NameError: name 'total' is not defined
"""))

    C.append(md(r"""
## Importing modules and libraries

You do not have to write everything yourself. Python ships with **modules** of ready-made tools, and the scientific world adds **libraries** like NumPy and RDKit. You bring them in with `import`.

- `import math` — gives you the whole `math` module; use it as `math.sqrt(...)`.
- `from math import pi` — pulls out just one name so you can write `pi` directly.

> **🧪 Chemistry aside — pH**
>
> **pH** measures how acidic a solution is: `pH = -log10([H+])`, where `[H+]` is the hydrogen-ion concentration in mol/L. The `log10` lives in the `math` module.
"""))

    C.append(code(r"""
import math
from math import pi

def ph(h_concentration):
    "Return the pH for a given [H+] in mol/L."
    return -math.log10(h_concentration)

print("pH of 1e-3 mol/L acid:", round(ph(1e-3), 2))
print("pi is", pi)     # imported directly with 'from math import pi'
"""))

    C.append(md(r"""
## ⚗️ With RDKit — the same job in one line

Importing RDKit is *exactly* the same `import` idea you just learnt, applied to a professional library. And here is the pay-off for building `molar_mass()` by hand: RDKit will compute the very same number straight from a SMILES string, with `Descriptors.MolWt`.

Let us compute ethanol's molar mass **both ways** and compare.
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Descriptors

# Our hand-built version (ethanol is C2H6O):
by_hand = molar_mass({"C": 2, "H": 6, "O": 1})

# RDKit's version, straight from the SMILES string:
mol = Chem.MolFromSmiles("CCO")
by_rdkit = Descriptors.MolWt(mol)

print(f"By hand: {by_hand:.2f} g/mol")
print(f"RDKit:   {by_rdkit:.2f} g/mol")
"""))

    C.append(md(r"""
They agree (to rounding). You did not *need* RDKit to get the answer — but now you understand exactly what `Descriptors.MolWt` is doing under the bonnet: adding up atomic masses, just as you did. That is the theme of the whole course: **build it by hand to understand it, then let the professional tool do it quickly.**

Let us try a harder one, aspirin, where counting atoms by hand would be a pain:
"""))

    C.append(code(r"""
aspirin = Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")
print(f"Aspirin molar mass (RDKit): {Descriptors.MolWt(aspirin):.2f} g/mol")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Write a function `grams_from_moles(amount_mol, molar_mass_g_per_mol)` that returns a mass in grams (the reverse of `moles_from_mass`). Give it a **docstring**. Then use it to find the mass of `0.25 mol` of ethanol (molar mass `46.07 g/mol`).
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r'''
def grams_from_moles(amount_mol, molar_mass_g_per_mol):
    """Return the mass in grams for a given amount (mol) and molar mass (g/mol)."""
    return amount_mol * molar_mass_g_per_mol

mass = grams_from_moles(0.25, 46.07)
print(f"0.25 mol of ethanol weighs {mass:.2f} g")
'''))

    C.append(md(r"""
## Key takeaways

- A **function** packages a calculation: `def name(parameters):` ... `return result`.
- Functions are reusable, readable, and keep their working variables **private** (scope).
- Parameters can have **default values**; a **docstring** documents what the function does and feeds `help()`.
- `import` brings in modules (`math`) and libraries (`rdkit`) full of ready-made tools.
- RDKit's `Descriptors.MolWt(Chem.MolFromSmiles(...))` reproduces our hand-built `molar_mass()` — same idea, one line.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **Flow** — we teach the computer to make decisions (`if`/`else`) and to repeat work (`for` loops), and use them to screen molecules with Lipinski's famous rule of five.
"""))

    return C


# ===========================================================================
# Notebook 04 — Flow (control flow)
# ===========================================================================
def build_04():
    C = []

    C.append(md(r"""
# Lecture 04 — Flow

*Making decisions and repeating work: screening molecules with Lipinski's rule of five.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- write **boolean** expressions with comparisons and `and` / `or` / `not`;
- branch with **`if` / `elif` / `else`**;
- repeat work with **`for`** loops (over lists and over dictionary items);
- use a **`while`** loop, and avoid the infinite-loop trap;
- skip or stop early with **`continue`** / **`break`**;
- write a simple **list comprehension** once the explicit loop is clear.
"""))

    C.append(md(r"""
## Recap of Lecture 03

- A **function** packages a calculation (`def` ... `return`); we built `molar_mass()`.
- Functions take **parameters** (with optional **defaults**) and have **docstrings**.
- `import` brings in libraries; RDKit's `Descriptors.MolWt` matched our hand-built molar mass.
"""))

    C.append(md(r"""
## Booleans and comparisons

A **boolean** is a value that is either `True` or `False`. You get one whenever you **compare** two things:

| Operator | Meaning |
| --- | --- |
| `==` | equal to (note: **two** equals signs) |
| `!=` | not equal to |
| `<`  `>` | less than / greater than |
| `<=`  `>=` | less than or equal / greater than or equal |
"""))

    C.append(code(r"""
molar_mass = 180.16     # aspirin, g/mol
print(molar_mass < 500)      # is it below 500?
print(molar_mass == 180.16)
print(molar_mass != 500)
"""))

    C.append(md(r"""
Combine conditions with **`and`** (both must be true), **`or`** (at least one), and **`not`** (flip it):
"""))

    C.append(code(r"""
logp = 1.31     # aspirin's (computed) logP
print(molar_mass < 500 and logp < 5)     # both conditions true?
print(molar_mass > 500 or logp < 5)      # at least one true?
print(not (molar_mass > 500))            # flip a condition
"""))

    C.append(md(r"""
## Making decisions: `if` / `elif` / `else`

An **`if`** statement runs a block of code only when its condition is `True`. Add **`elif`** ("else if") for more cases, and **`else`** for "none of the above". Mind the colons and the indentation — the indented block is what runs.
"""))

    C.append(code(r"""
mass = 180.16

if mass < 100:
    print("small molecule")
elif mass < 500:
    print("medium-sized molecule")
else:
    print("large molecule")
"""))

    C.append(md(r"""
> **🧪 Chemistry aside — logP and the rule of five**
>
> **logP** is a number describing how *fat-loving* versus *water-loving* a molecule is: higher logP means more fat-loving (it prefers oil to water). **Lipinski's rule of five** is a rule of thumb for whether a molecule is likely to make a good oral drug. It flags a molecule as potentially problematic if it breaks more than one of: molar mass ≤ 500, logP ≤ 5, hydrogen-bond **donors** ≤ 5, hydrogen-bond **acceptors** ≤ 10. We will use it as our worked example for decisions and loops.
"""))

    C.append(md(r"""
## The rule of five, by hand

Let us implement the rule for one molecule using numbers we have looked up. Aspirin: molar mass 180.16, logP 1.31, 1 H-bond donor, 3 H-bond acceptors.
"""))

    C.append(code(r"""
mass = 180.16
logp = 1.31
donors = 1
acceptors = 3

# Count how many of the four limits are broken.
violations = 0
if mass > 500:
    violations += 1
if logp > 5:
    violations += 1
if donors > 5:
    violations += 1
if acceptors > 10:
    violations += 1

if violations <= 1:
    print(f"Aspirin looks drug-like (violations: {violations})")
else:
    print(f"Aspirin breaks the rule of five (violations: {violations})")
"""))

    C.append(md(r"""
## `for` loops: doing something to every item

A **`for`** loop repeats a block once for each item in a collection. Here we loop over a list of molecule names and print each.
"""))

    C.append(code(r"""
molecules = ["water", "ethanol", "caffeine", "aspirin", "glucose"]
for name in molecules:
    print("Processing", name)
"""))

    C.append(md(r"""
The loop variable (`name` here) takes each value in turn. We can do real work inside — for example, reuse our `molar_mass()` function from Lecture 03 across a list of molecules described as `{element: count}` dictionaries.
"""))

    C.append(code(r"""
atomic_mass = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999}

def molar_mass(composition):
    total = 0.0
    for element, count in composition.items():
        total += count * atomic_mass[element]
    return total

# A small list of (name, composition) pairs.
data = [
    ("water",   {"H": 2, "O": 1}),
    ("ethanol", {"C": 2, "H": 6, "O": 1}),
    ("methane", {"C": 1, "H": 4}),
    ("benzene", {"C": 6, "H": 6}),
]

for name, composition in data:
    print(f"{name:<8} {molar_mass(composition):6.2f} g/mol")
"""))

    C.append(md(r"""
### Looping over a dictionary

Looping over a dictionary's `.items()` gives you each **key and value** together — exactly how `molar_mass()` works inside.
"""))

    C.append(code(r"""
for element, mass in atomic_mass.items():
    print(f"{element}: {mass} g/mol")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Loop over the `data` list above and find the **heaviest** molecule. (Hint: keep a variable for the biggest mass seen so far, start it at 0, and update it inside the loop when you find something heavier.)
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
heaviest_name = ""
heaviest_mass = 0.0
for name, composition in data:
    m = molar_mass(composition)
    if m > heaviest_mass:
        heaviest_mass = m
        heaviest_name = name
print(f"The heaviest is {heaviest_name} at {heaviest_mass:.2f} g/mol")
"""))

    C.append(md(r"""
## Filtering with a loop and an `if`

A very common pattern: loop over items and **keep** only those that pass a test. Here we collect molecules below a molar-mass cut-off.
"""))

    C.append(code(r"""
cutoff = 50.0     # g/mol
light_molecules = []
for name, composition in data:
    if molar_mass(composition) < cutoff:
        light_molecules.append(name)
print(f"Below {cutoff} g/mol:", light_molecules)
"""))

    C.append(md(r"""
## `while` loops (and the infinite-loop trap)

A **`while`** loop keeps going *as long as* a condition stays `True`. Use it when you do not know in advance how many repeats you need. Here we simulate a simple radioactive-style halving until very little remains.
"""))

    C.append(code(r"""
amount = 100.0      # arbitrary units
half_lives = 0
while amount > 1.0:
    amount = amount / 2     # halve it
    half_lives += 1
print(f"After {half_lives} halvings, {amount:.3f} units remain")
"""))

    C.append(md(r"""
> **⚠️ The infinite-loop trap.** A `while` loop only stops when its condition becomes `False`. If you forget to change anything inside the loop, it runs forever and the notebook hangs. The fix if it happens: **interrupt the kernel** (the stop ◼ button, or *Kernel → Interrupt*). Always make sure something inside the loop moves you towards the stopping condition.
"""))

    C.append(md(r"""
## `break` and `continue`

Inside any loop: **`break`** stops the loop completely; **`continue`** skips to the next item.
"""))

    C.append(code(r"""
for name, composition in data:
    m = molar_mass(composition)
    if m < 20:
        continue           # skip the very light ones
    print(name, round(m, 2))
    if name == "ethanol":
        print("  (found ethanol — stopping early)")
        break              # stop the whole loop here
"""))

    C.append(md(r"""
## ⚗️ With RDKit — the rule of five on real descriptors

We screened aspirin by hand using looked-up numbers. Now let RDKit compute the four descriptors **live** from SMILES, and run the very same `if` logic on its values. The decision-making is identical — only the source of the numbers changes.

> **🧪 Chemistry aside — an honesty note about logP.** The logP that RDKit gives you (`Descriptors.MolLogP`) is a **computed** value — specifically Crippen's estimate, worked out from the molecule's structure. It is close to, but **not identical to**, the logP you would *measure* experimentally in the lab. That is fine for screening and teaching, but worth remembering: when you see RDKit's logP (here and in the data file), read it as "a good computed estimate", not "the measured truth".
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

def rule_of_five(smiles):
    "Return (n_violations, is_drug_like) for a molecule given by SMILES."
    mol = Chem.MolFromSmiles(smiles)
    mass = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    donors = Lipinski.NumHDonors(mol)
    acceptors = Lipinski.NumHAcceptors(mol)

    violations = 0
    if mass > 500:
        violations += 1
    if logp > 5:
        violations += 1
    if donors > 5:
        violations += 1
    if acceptors > 10:
        violations += 1
    return violations, violations <= 1

v, drug_like = rule_of_five("CC(=O)Oc1ccccc1C(=O)O")   # aspirin
print(f"Aspirin: {v} violation(s); drug-like? {drug_like}")
"""))

    C.append(md(r"""
Now loop over several molecules (as SMILES) and print each one's verdict — decisions and loops working together:
"""))

    C.append(code(r"""
smiles_set = {
    "water":      "O",
    "ethanol":    "CCO",
    "caffeine":   "Cn1cnc2c1c(=O)n(C)c(=O)n2C",
    "aspirin":    "CC(=O)Oc1ccccc1C(=O)O",
    "glucose":    "OCC1OC(O)C(O)C(O)C1O",
    "ibuprofen":  "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
}

for name, smiles in smiles_set.items():
    violations, drug_like = rule_of_five(smiles)
    verdict = "PASS" if drug_like else "FAIL"
    print(f"{name:<10} {violations} violation(s)  ->  {verdict}")
"""))

    C.append(md(r"""
## A gentle first look at list comprehensions

Once you are comfortable writing a `for` loop that builds a list, Python offers a shorthand for that exact pattern: a **list comprehension**. Compare the two — they do the same thing.
"""))

    C.append(code(r"""
# The explicit loop you already understand:
names_upper = []
for name in smiles_set:
    names_upper.append(name.upper())
print(names_upper)

# The same thing as a list comprehension:
names_upper2 = [name.upper() for name in smiles_set]
print(names_upper2)
"""))

    C.append(md(r"""
Read it as "**give me `name.upper()` for each `name` in `smiles_set`**". You can add a condition too: `[n for n in names if ...]`. Use comprehensions when they make code *clearer*; reach for an ordinary loop whenever you are unsure.
"""))

    C.append(md(r"""
### 🔬 Try it yourself

1. Write a function `is_drug_like(smiles)` that returns just `True` or `False` (reuse `rule_of_five`).
2. Use a **list comprehension** to build a list of the names in `smiles_set` that are drug-like.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
def is_drug_like(smiles):
    _, drug_like = rule_of_five(smiles)
    return drug_like

drug_like_names = [name for name, smi in smiles_set.items() if is_drug_like(smi)]
print("Drug-like:", drug_like_names)
"""))

    C.append(md(r"""
## Key takeaways

- **Booleans** come from comparisons (`==`, `<`, `>=`, ...) and combine with `and` / `or` / `not`.
- **`if` / `elif` / `else`** chooses what to do; indentation marks each block.
- **`for`** loops repeat over the items of a list or the `.items()` of a dictionary.
- **`while`** loops repeat until a condition fails — always move towards stopping, or you loop forever.
- **`break`** stops a loop; **`continue`** skips an item; a **list comprehension** is shorthand for a list-building loop.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **Files** — we read a real molecule dataset from disk, run this rule-of-five screen across it, and save the drug-like subset to a new file.
"""))

    return C


# ===========================================================================
# Notebook 05 — Files
# ===========================================================================
def build_05():
    C = []

    C.append(md(r"""
# Lecture 05 — Files

*The everyday chemist's task: open a data file, process it, and save the result.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- explain what a **file path** is, including what `..` means;
- open a file safely with a **`with`** block, and read it (`.read()`, `.readlines()`, line by line);
- **write** text to a new file;
- understand **CSV** as comma-separated text, and read it with both the `csv` module and `pandas`;
- handle a missing file gracefully with **`try` / `except`**.
"""))

    C.append(md(r"""
## Recap of Lecture 04

- **`if` / `elif` / `else`** make decisions; **`for`** and **`while`** loops repeat work.
- We built a `rule_of_five()` screen and looped it over several molecules.
- A **list comprehension** is shorthand for a list-building loop.
"""))

    C.append(md(r"""
## What is a file path?

A **file path** is the address of a file on your computer. Our data lives in the project's `data/` folder, while this notebook lives in `notebooks/`. To reach the data from here we go *up one level* and then into `data/`:

```
../data/molecules.csv
```

The `..` means "the folder above this one" (here, the project root). The `/` separates folder names. We will use this path throughout the lecture.
"""))

    C.append(md(r"""
## Reading a text file with `with`

The safe way to open a file is a **`with`** block:

```python
with open(path) as f:
    ... use f ...
```

The reason to use `with`: it **automatically closes** the file for you when the block ends, even if something goes wrong. Leaving files open is a classic source of subtle bugs, so always use `with`.

Let us read the molecules file as raw text first, just to see what is in it. `.read()` slurps the whole file into one string; here we print only the first 200 characters.
"""))

    C.append(code(r"""
path = "../data/molecules.csv"

with open(path) as f:
    contents = f.read()

print(contents[:200])      # the first 200 characters
"""))

    C.append(md(r"""
That is a **CSV** file — *comma-separated values*. The first line is a **header** naming the columns; each line after is one molecule, with fields separated by commas.

Often you want the file **line by line** instead of as one blob. `.readlines()` gives you a list of lines; or you can loop straight over the file object.
"""))

    C.append(code(r"""
with open(path) as f:
    lines = f.readlines()

print("Number of lines (including header):", len(lines))
print("Header:", lines[0].strip())          # .strip() removes the trailing newline
print("First molecule row:", lines[1].strip())
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Open `../data/molecules.csv`, loop over the lines **after** the header (remember slicing — `lines[1:]`), and print just the **first field** (the name) of each row. Hint: `line.split(",")` splits a line into a list of fields.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
with open(path) as f:
    lines = f.readlines()

for line in lines[1:]:            # skip the header
    fields = line.strip().split(",")
    print(fields[0])              # the name is the first field
"""))

    C.append(md(r"""
## Reading a CSV properly: the `csv` module

Splitting on commas by hand is fragile. Python's built-in **`csv`** module does it correctly. `csv.DictReader` is especially friendly: it reads each row into a **dictionary** keyed by the column names — exactly the data structure from Lecture 02.
"""))

    C.append(code(r"""
import csv

with open(path, newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)          # turn it into a list of dictionaries

print("Read", len(rows), "molecules")
print(rows[0])                   # the first row, as a dictionary
print("First molecule's name:", rows[0]["name"])
"""))

    C.append(md(r"""
Note that everything read from a text file arrives as a **string** — even the numbers. To do arithmetic we must convert with `float(...)`. Let us report each molecule's molar mass:
"""))

    C.append(code(r"""
for row in rows:
    mass = float(row["molar_mass"])      # convert the text "18.02" to the number 18.02
    print(f"{row['name']:<12} {mass:7.2f} g/mol")
"""))

    C.append(md(r"""
## Applying the rule-of-five filter and writing a new file

Now the real task. We will reuse the rule-of-five idea from Lecture 04 — but this time the descriptors are already in the file, so we just read them. We collect the drug-like molecules and **write them to a new CSV**.
"""))

    C.append(code(r"""
def passes_rule_of_five(row):
    "Decide drug-likeness from a CSV row (values are strings, so convert them)."
    violations = 0
    if float(row["molar_mass"]) > 500:
        violations += 1
    if float(row["logp"]) > 5:
        violations += 1
    if int(row["h_bond_donors"]) > 5:
        violations += 1
    if int(row["h_bond_acceptors"]) > 10:
        violations += 1
    return violations <= 1

drug_like = [row for row in rows if passes_rule_of_five(row)]
print(f"{len(drug_like)} of {len(rows)} molecules pass the rule of five")
"""))

    C.append(code(r"""
out_path = "../data/drug_like_subset.csv"

with open(out_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(drug_like)

print("Wrote", out_path)
"""))

    C.append(md(r"""
Open the `"w"` argument up for a moment: it means **write** mode (it creates the file, or overwrites it if it exists). Reading mode is the default. Be careful — `"w"` will happily wipe an existing file.
"""))

    C.append(md(r"""
## The easier way: pandas

Reading CSVs is so common that the **pandas** library makes it a one-liner. Think of a pandas **DataFrame** as *a smart table* — like a spreadsheet you can compute with. We will not turn this into a pandas course; just meet it as a convenient tool for tabular data.
"""))

    C.append(code(r"""
import pandas as pd

df = pd.read_csv("../data/molecules.csv")
df          # a DataFrame displays as a tidy table
"""))

    C.append(md(r"""
pandas already knows the numeric columns are numbers, so you can compute directly — no `float(...)` needed:
"""))

    C.append(code(r"""
print("Mean molar mass:", round(df["molar_mass"].mean(), 2), "g/mol")
print("Heaviest molecule:", df.loc[df["molar_mass"].idxmax(), "name"])

# The same drug-like filter, the pandas way:
mask = (df["molar_mass"] <= 500) & (df["logp"] <= 5) & \
       (df["h_bond_donors"] <= 5) & (df["h_bond_acceptors"] <= 10)
print(df[mask]["name"].tolist())
"""))

    C.append(md(r"""
## Handling a missing file: `try` / `except`

If you ask to open a file that is not there, Python raises an error and stops. Often you would rather **catch** that and carry on. A **`try` / `except`** block does this: Python *tries* the risky code, and if the named error happens, it runs the *except* block instead of crashing.
"""))

    C.append(code(r"""
try:
    with open("../data/does_not_exist.csv") as f:
        f.read()
except FileNotFoundError:
    print("That file is not there — check the path and try again.")
"""))

    C.append(md(r"""
## ⚗️ With RDKit — confirm the file's numbers from the SMILES

The file *claims* certain molar masses. We can verify them: take the `smiles` column, rebuild each molecule with RDKit, recompute the molar mass, and compare. This is exactly how `data/molecules.csv` was generated in the first place.
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Descriptors

for row in rows[:5]:                      # just the first five, to keep it short
    mol = Chem.MolFromSmiles(row["smiles"])
    from_rdkit = Descriptors.MolWt(mol)
    from_file = float(row["molar_mass"])
    agree = abs(from_rdkit - from_file) < 0.1
    print(f"{row['name']:<12} file={from_file:7.2f}  rdkit={from_rdkit:7.2f}  match={agree}")
"""))

    C.append(md(r"""
> **🧪 Chemistry aside — other file formats.** CSV is fine for tables of properties, but chemists also use dedicated structure formats such as **SDF** and **MOL**, which store full 2D/3D atom-and-bond information. RDKit can read these too (e.g. `Chem.SDMolSupplier`) — worth knowing they exist; no need to dive in now.
"""))

    C.append(md(r"""
### 🔬 Try it yourself

1. Count how many molecules in `rows` pass the rule of five (you have `passes_rule_of_five`).
2. Write a short **summary text file** to `../data/summary.txt` containing one line: how many of how many molecules are drug-like. Read it back and print it to check.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
n_pass = sum(1 for row in rows if passes_rule_of_five(row))

with open("../data/summary.txt", "w") as f:
    f.write(f"{n_pass} of {len(rows)} molecules are drug-like by Lipinski's rule of five.\n")

with open("../data/summary.txt") as f:
    print(f.read())
"""))

    C.append(md(r"""
## Key takeaways

- A **file path** locates a file; `..` means the folder above.
- Always open files in a **`with`** block — it closes them for you automatically.
- Read text with `.read()` / `.readlines()`; write with mode `"w"` (which overwrites!).
- **CSV** is comma-separated text; read it cleanly with the `csv` module or, even more easily, `pandas.read_csv` (a DataFrame is "a smart table").
- Catch errors like a missing file with **`try` / `except`**.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **NumPy** — we move from rows-and-loops to fast **arrays**, doing maths on whole columns of numbers at once (and meeting the Beer–Lambert law).
"""))

    return C


# ===========================================================================
# Notebook 06 — NumPy
# ===========================================================================
def build_06():
    C = []

    C.append(md(r"""
# Lecture 06 — NumPy

*Doing maths on whole columns of numbers at once: concentrations, descriptors and a UV–Vis spectrum.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- explain why **NumPy arrays** beat plain lists for numerical work;
- create arrays with `np.array`, `np.arange`, `np.linspace`, `np.zeros` / `np.ones`;
- do **element-wise** arithmetic and understand **broadcasting**;
- **index**, **slice** and apply **boolean masks** to arrays;
- compute **aggregations**: `mean`, `std`, `min`, `max`, `sum`, `argmax`.
"""))

    C.append(md(r"""
## Recap of Lecture 05

- Files are opened safely with **`with`**; CSVs read cleanly via the `csv` module or `pandas`.
- We screened `data/molecules.csv` with the rule of five and wrote out a subset.
- Numbers read from text files arrive as **strings** and need converting.
"""))

    C.append(md(r"""
## Why NumPy?

A Python **list** can hold numbers, but doing maths on it is clumsy — to double every value you need a loop. **NumPy** gives you the **array**: a list-like container built for numbers, where maths applies to *every element at once* and runs fast. Watch the difference:
"""))

    C.append(code(r"""
import numpy as np

# A plain list: multiplying by 2 does NOT do what a chemist wants...
concs_list = [0.1, 0.2, 0.3]
print("list * 2:", concs_list * 2)        # it repeats the list!

# A NumPy array: maths applies element by element.
concs = np.array([0.1, 0.2, 0.3])
print("array * 2:", concs * 2)            # every value doubled
"""))

    C.append(md(r"""
That element-wise behaviour is the whole point. No loop, no fuss — and for big datasets it is dramatically faster.
"""))

    C.append(md(r"""
## Creating arrays

A few standard ways to make arrays:

- `np.array([...])` — from a list you already have.
- `np.arange(start, stop, step)` — evenly spaced, like `range` (stops *before* `stop`).
- `np.linspace(start, stop, n)` — `n` points evenly spaced, **including** both ends.
- `np.zeros(n)` / `np.ones(n)` — arrays filled with 0.0 or 1.0.
"""))

    C.append(code(r"""
print(np.arange(0, 1, 0.25))         # 0, 0.25, 0.5, 0.75
print(np.linspace(0, 1, 5))          # 5 points from 0 to 1 inclusive
print(np.zeros(3))
print(np.ones(3))
"""))

    C.append(md(r"""
## Element-wise arithmetic and broadcasting

> **🧪 Chemistry aside — the Beer–Lambert law**
>
> The **Beer–Lambert law** relates the absorbance of a solution to its concentration: `A = ε · c · l`, where `ε` is the molar absorptivity (how strongly the substance absorbs), `c` is the concentration, and `l` is the path length of the cuvette. Given a list of concentrations, we can get all their absorbances in one line.

Here a single number (`epsilon * path_length`) multiplies a whole array — NumPy "broadcasts" the scalar across every element.
"""))

    C.append(code(r"""
concentrations = np.linspace(0.0, 1.0e-4, 6)   # mol/L (0 to 100 micromolar)
epsilon = 12000      # molar absorptivity, L/(mol*cm)
path_length = 1.0    # cm

absorbances = epsilon * concentrations * path_length   # Beer-Lambert, all at once
print("Concentrations:", concentrations)
print("Absorbances:   ", absorbances)
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Make an array of concentrations from `0` to `5e-5 mol/L` (that is 50 µM) with **11** points (`np.linspace`). Using `ε = 8000` and a `1 cm` path length, compute the absorbances in one line and print them.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
c = np.linspace(0, 5e-5, 11)
a = 8000 * c * 1.0
print(a)
"""))

    C.append(md(r"""
## Indexing, slicing and boolean masks

Arrays index and slice just like lists (still zero-based). The new superpower is the **boolean mask**: compare an array to a value and you get an array of `True`/`False`, which you can use to *select* elements.
"""))

    C.append(code(r"""
print(absorbances[0])        # first element
print(absorbances[1:4])      # a slice

# A boolean mask: which absorbances exceed 0.5?
mask = absorbances > 0.5
print(mask)                  # array of True/False
print(absorbances[mask])     # keep only the elements where the mask is True
"""))

    C.append(md(r"""
## Aggregations: summarising an array

NumPy arrays have handy methods to summarise them: `.mean()`, `.std()` (standard deviation), `.min()`, `.max()`, `.sum()`. Let us use the molecule dataset. We will load it with pandas (from Lecture 05) and pull the molar-mass column out as a NumPy array.
"""))

    C.append(code(r"""
import pandas as pd

df = pd.read_csv("../data/molecules.csv")
masses = df["molar_mass"].to_numpy()      # a column -> a NumPy array
print("Molar masses:", masses)
print(f"mean  = {masses.mean():.2f} g/mol")
print(f"std   = {masses.std():.2f} g/mol")
print(f"min   = {masses.min():.2f} g/mol")
print(f"max   = {masses.max():.2f} g/mol")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Pull the `logp` column out as a NumPy array. (1) Print its **mean** and **standard deviation**. (2) Use a **boolean mask** to print only the logP values **above 1.0**.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
logp = df["logp"].to_numpy()
print(f"mean logP = {logp.mean():.2f}")
print(f"std  logP = {logp.std():.2f}")
print("logP above 1.0:", logp[logp > 1.0])
"""))

    C.append(md(r"""
## Processing a spectrum

Now a classic array job: a **UV–Vis spectrum**. The file `data/uvvis_spectrum.csv` has two columns, `wavelength_nm` and `absorbance`. We load them into arrays and do real analysis.
"""))

    C.append(code(r"""
spectrum = pd.read_csv("../data/uvvis_spectrum.csv")
wavelength = spectrum["wavelength_nm"].to_numpy()
absorbance = spectrum["absorbance"].to_numpy()
print("Number of points:", len(wavelength))
print("Wavelength range:", wavelength.min(), "to", wavelength.max(), "nm")
"""))

    C.append(md(r"""
**Where is the peak?** `argmax` gives the *index* of the largest value; use it to look up the wavelength there.
"""))

    C.append(code(r"""
peak_index = absorbance.argmax()
print(f"Peak absorbance {absorbance[peak_index]:.3f} at {wavelength[peak_index]:.0f} nm")
"""))

    C.append(md(r"""
**Normalising** is just element-wise division — rescale so the maximum becomes 1:
"""))

    C.append(code(r"""
normalised = absorbance / absorbance.max()
print("New maximum:", normalised.max())
print("First few normalised values:", normalised[:5])
"""))

    C.append(md(r"""
**Slicing a window** with a boolean mask — keep only the 250–290 nm region:
"""))

    C.append(code(r"""
window = (wavelength >= 250) & (wavelength <= 290)
print("Points in the 250-290 nm window:", window.sum())
print("Mean absorbance there:", absorbance[window].mean().round(3))
"""))

    C.append(md(r"""
## ⚗️ With RDKit — build a descriptor array, then do statistics

Here RDKit (which makes molecule **objects**) and NumPy (which crunches **numbers**) team up. We loop the SMILES through RDKit to compute three descriptors per molecule — molar mass, logP and **TPSA** — and stack them into a NumPy array to analyse.

> **🧪 Chemistry aside — TPSA.** The **topological polar surface area** (TPSA) estimates the surface area of a molecule taken up by polar (nitrogen- and oxygen-containing) parts. It correlates with how easily a drug crosses membranes — another quick descriptor RDKit gives for free.
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Descriptors

rows = []
for smiles in df["smiles"]:
    mol = Chem.MolFromSmiles(smiles)
    rows.append([Descriptors.MolWt(mol), Descriptors.MolLogP(mol), Descriptors.TPSA(mol)])

descriptors = np.array(rows)        # a 2D array: one row per molecule, three columns
print("Shape (rows, columns):", descriptors.shape)
print(descriptors.round(2))
"""))

    C.append(md(r"""
With a 2D array, `axis=0` means "down each column". So we can summarise all three descriptors at once:
"""))

    C.append(code(r"""
column_names = ["MolWt", "MolLogP", "TPSA"]
means = descriptors.mean(axis=0)        # mean of each column
for name, value in zip(column_names, means):
    print(f"mean {name:<8} = {value:.2f}")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Using the `descriptors` array: (1) find the **maximum TPSA** (the third column, index `2`); (2) find which molecule it belongs to. Hint: `descriptors[:, 2]` is the whole TPSA column, and `argmax` gives its index; look that index up in `df["name"]`.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
tpsa = descriptors[:, 2]
i = tpsa.argmax()
print(f"Highest TPSA is {tpsa[i]:.2f} for {df['name'].iloc[i]}")
"""))

    C.append(md(r"""
## Key takeaways

- A **NumPy array** does maths **element-wise** and fast — no loops needed.
- Create arrays with `np.array`, `np.arange`, `np.linspace`, `np.zeros`/`np.ones`.
- A scalar applied to an array **broadcasts** across every element (e.g. Beer–Lambert in one line).
- **Boolean masks** (`arr[arr > x]`) select elements that pass a test.
- Summarise with `mean`, `std`, `min`, `max`, `sum`; find the peak position with `argmax`.
"""))

    C.append(md(r"""
## Looking ahead

Next lecture — **Plotting** — we turn all these numbers into figures: the UV–Vis spectrum, a calibration curve, and a property scatter — with properly labelled, unit-bearing axes.
"""))

    return C


# ===========================================================================
# Notebook 07 — Plotting
# ===========================================================================
def build_07():
    C = []

    C.append(md(r"""
# Lecture 07 — Plotting

*Turning numbers into clear figures: spectra, calibration curves and property plots.*
"""))

    C.append(md(r"""
## Learning objectives

By the end of this lecture you will be able to:

- make **line**, **scatter**, **bar** and **histogram** plots with `matplotlib.pyplot`;
- label axes (**with units**), add a **title**, a **legend** and set axis **limits**;
- put **multiple series** on one set of axes and control the **figure size**;
- **save** a figure to a file with `plt.savefig`;
- explain what makes a tidy, publication-style scientific figure.
"""))

    C.append(md(r"""
## Recap of Lecture 06

- **NumPy arrays** do fast, element-wise maths; we used them for Beer–Lambert and descriptors.
- We loaded a **UV–Vis spectrum** and found its peak with `argmax`.
- **Boolean masks** select array elements that pass a test.
"""))

    C.append(md(r"""
## The golden rule of scientific figures

A figure is only useful if a reader can tell what it shows. So, every single time:

- **label both axes**, and **include the units** (e.g. "wavelength / nm");
- give it a **title**;
- add a **legend** if there is more than one series.

We will hold to this throughout. Let us load our data first (the spectrum and the molecule table from earlier lectures).
"""))

    C.append(code(r"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

spectrum = pd.read_csv("../data/uvvis_spectrum.csv")
wavelength = spectrum["wavelength_nm"].to_numpy()
absorbance = spectrum["absorbance"].to_numpy()

molecules = pd.read_csv("../data/molecules.csv")
print("Loaded", len(wavelength), "spectrum points and", len(molecules), "molecules")
"""))

    C.append(md(r"""
## A line plot: the UV–Vis spectrum

The basic recipe: create a figure, call `plt.plot(x, y)`, then label everything and `plt.show()`.
"""))

    C.append(code(r"""
plt.figure(figsize=(7, 4))            # width, height in inches
plt.plot(wavelength, absorbance)
plt.xlabel("Wavelength / nm")
plt.ylabel("Absorbance")
plt.title("Synthetic UV-Vis spectrum")
plt.show()
"""))

    C.append(md(r"""
### Annotating the peak

We can mark the peak using `argmax` from Lecture 06, and `plt.annotate` to add a label with an arrow.
"""))

    C.append(code(r"""
peak_i = absorbance.argmax()
peak_x = wavelength[peak_i]
peak_y = absorbance[peak_i]

plt.figure(figsize=(7, 4))
plt.plot(wavelength, absorbance, color="darkblue")
plt.annotate(f"peak at {peak_x:.0f} nm",
             xy=(peak_x, peak_y),
             xytext=(peak_x + 30, peak_y * 0.9),
             arrowprops={"arrowstyle": "->"})
plt.xlabel("Wavelength / nm")
plt.ylabel("Absorbance")
plt.title("UV-Vis spectrum with peak annotated")
plt.show()
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Plot the same spectrum but (1) change the line **colour**, (2) restrict the x-axis to **240–300 nm** with `plt.xlim(240, 300)`, and (3) give it your own title.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
plt.figure(figsize=(7, 4))
plt.plot(wavelength, absorbance, color="crimson")
plt.xlim(240, 300)
plt.xlabel("Wavelength / nm")
plt.ylabel("Absorbance")
plt.title("Zoom on the absorption band")
plt.show()
"""))

    C.append(md(r"""
## A scatter plot with a best-fit line: Beer–Lambert calibration

> **🧪 Chemistry aside — calibration curve.** To measure an unknown concentration, you first build a **calibration curve**: prepare standards of known concentration, measure each one's absorbance, and fit a straight line (Beer–Lambert predicts `A = ε·l·c`, a line through the origin). You then read unknowns off that line.

We make some standards, add a touch of realistic scatter, plot them as points, and overlay a best-fit line found with `np.polyfit`.
"""))

    C.append(code(r"""
rng = np.random.default_rng(0)        # fixed seed -> reproducible "measurements"
conc = np.linspace(0.0, 1.0e-4, 8)    # mol/L (0 to 100 micromolar)
true_slope = 12000                    # epsilon * path length, L/(mol*cm)
measured_A = true_slope * conc + rng.normal(0, 0.03, size=conc.size)

# Fit a straight line: returns [slope, intercept]
slope, intercept = np.polyfit(conc, measured_A, 1)
fit_line = slope * conc + intercept

plt.figure(figsize=(6, 4))
plt.scatter(conc, measured_A, label="measured standards")
plt.plot(conc, fit_line, color="black", label=f"best fit (slope {slope:.0f})")
plt.xlabel("Concentration / mol L$^{-1}$")
plt.ylabel("Absorbance")
plt.title("Beer-Lambert calibration curve")
plt.legend()
plt.show()
"""))

    C.append(md(r"""
## A scatter coloured by a category: molar mass vs logP

We can colour points by a property. Here we colour molecules by whether they are drug-like (rule of five), tying together the chemistry from the whole course. We compute a simple drug-like flag from the table's columns.
"""))

    C.append(code(r"""
mw = molecules["molar_mass"].to_numpy()
logp = molecules["logp"].to_numpy()

drug_like = ((molecules["molar_mass"] <= 500) & (molecules["logp"] <= 5) &
             (molecules["h_bond_donors"] <= 5) & (molecules["h_bond_acceptors"] <= 10)).to_numpy()

plt.figure(figsize=(6, 4))
plt.scatter(mw[drug_like], logp[drug_like], color="green", label="drug-like")
plt.scatter(mw[~drug_like], logp[~drug_like], color="red", label="not drug-like")
plt.xlabel("Molar mass / g mol$^{-1}$")
plt.ylabel("logP (computed)")
plt.title("Molecular properties, coloured by drug-likeness")
plt.legend()
plt.show()
"""))

    C.append(md(r"""
## A histogram and a bar chart

A **histogram** shows the distribution of one set of values (how many fall in each range). A **bar chart** compares a value across labelled categories.
"""))

    C.append(code(r"""
plt.figure(figsize=(6, 4))
plt.hist(mw, bins=6, color="slateblue", edgecolor="white")
plt.xlabel("Molar mass / g mol$^{-1}$")
plt.ylabel("Number of molecules")
plt.title("Distribution of molar masses")
plt.show()
"""))

    C.append(code(r"""
plt.figure(figsize=(8, 4))
plt.bar(molecules["name"], molecules["molar_mass"], color="teal")
plt.xlabel("Molecule")
plt.ylabel("Molar mass / g mol$^{-1}$")
plt.title("Molar mass of each molecule")
plt.xticks(rotation=45, ha="right")     # rotate labels so they do not overlap
plt.tight_layout()
plt.show()
"""))

    C.append(md(r"""
## Saving a figure

To keep a figure, call `plt.savefig(...)` **before** `plt.show()`. The file extension chooses the format (`.png`, `.pdf`, ...). `dpi` controls the resolution.
"""))

    C.append(code(r"""
plt.figure(figsize=(7, 4))
plt.plot(wavelength, absorbance, color="darkblue")
plt.xlabel("Wavelength / nm")
plt.ylabel("Absorbance")
plt.title("UV-Vis spectrum")
plt.savefig("uvvis_spectrum.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved uvvis_spectrum.png")
"""))

    C.append(md(r"""
### 🔬 Try it yourself

Make **one** figure with **two series on the same axes**: the raw spectrum and its **normalised** version (`absorbance / absorbance.max()`). Add a **legend** so the two lines are distinguishable, label the axes, and save it as a PNG.
"""))

    C.append(code(r"""
# Your code here.
"""))

    C.append(md(r"""
**Solution**
"""))

    C.append(code(r"""
normalised = absorbance / absorbance.max()

plt.figure(figsize=(7, 4))
plt.plot(wavelength, absorbance, label="raw")
plt.plot(wavelength, normalised, label="normalised")
plt.xlabel("Wavelength / nm")
plt.ylabel("Absorbance (raw or normalised)")
plt.title("Raw vs normalised spectrum")
plt.legend()
plt.savefig("spectrum_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
"""))

    C.append(md(r"""
## ⚗️ With RDKit — show the molecules behind the numbers

Finally, let us put faces to the data. `Draw.MolsToGridImage` renders our molecule set as a labelled grid — the structures whose properties we have been plotting all along.
"""))

    C.append(code(r"""
from rdkit import Chem
from rdkit.Chem import Draw

names = molecules["name"].tolist()
mols = [Chem.MolFromSmiles(smi) for smi in molecules["smiles"]]

Draw.MolsToGridImage(mols, molsPerRow=4, subImgSize=(180, 160), legends=names)
"""))

    C.append(md(r"""
## Key takeaways

- `matplotlib.pyplot` makes **line**, **scatter**, **bar** and **histogram** plots.
- **Always** label both axes with units, add a title, and use a legend for multiple series.
- Put several series on one axes by calling `plot`/`scatter` more than once before `show`.
- `plt.figure(figsize=...)` sets the size; `plt.savefig(...)` (before `show`) saves the figure.
- RDKit's `Draw.MolsToGridImage` displays the molecules behind the numbers.
"""))

    C.append(md(r"""
## Where to go next

Congratulations — you have covered the Python fundamentals a working chemist needs, all the way from a bare notebook to publication-style figures, with RDKit woven throughout. To keep going:

- **Real datasets.** Try your skills on actual data — for example public sets from PubChem or ChEMBL — instead of our small teaching table.
- **Deeper RDKit.** There is a great deal more: molecular **fingerprints**, **substructure search** (does my molecule contain this group?), and **reaction** handling.
- **The browser version.** This workshop also exists as **marimo** notebooks that run entirely in the browser via WebAssembly — handy for experimenting with the Python without installing anything (note that RDKit is not available in that in-browser version, which is exactly why we used local Jupyter here).

Most of all: keep using it. The fastest way to get comfortable is to automate a small, real task from your own work.
"""))

    return C


def main() -> None:
    write_notebook("01-notebooks.ipynb", build_01())
    write_notebook("02-variables.ipynb", build_02())
    write_notebook("03-functions.ipynb", build_03())
    write_notebook("04-flow.ipynb", build_04())
    write_notebook("05-files.ipynb", build_05())
    write_notebook("06-numpy.ipynb", build_06())
    write_notebook("07-plotting.ipynb", build_07())
    print("All notebooks built.")


if __name__ == "__main__":
    main()
