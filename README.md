# Python for Chemists

A beginner Python course for chemistry undergraduates, taught as **seven
60-minute lectures**, each delivered as a Jupyter notebook. It assumes **no
prior programming experience** at all. The Python fundamentals are the real
lesson; every example is wrapped in a chemistry or cheminformatics context so
the material feels relevant rather than abstract.

The chemistry toolkit **RDKit** is woven throughout using one consistent rule:
**build it by hand in plain Python first, then meet the professional library
that does the same job in one line** — so you always understand what the tool is
doing under the bonnet.

> New to all this? Start with **[SETUP.md](SETUP.md)** — it walks you through
> installing conda and RDKit and opening your first notebook, assuming you have
> never installed Python before.

---

## Quick start

1. **Install conda.** Miniforge is recommended — see [SETUP.md](SETUP.md) for the
   gentle, step-by-step version.
2. **Create the environment** (from this folder):
   ```
   conda env create -f environment.yml
   ```
   This builds an isolated environment called **`chem-python`** containing
   Python, JupyterLab, NumPy, matplotlib, pandas and RDKit.
3. **Activate it** (in every new terminal):
   ```
   conda activate chem-python
   ```
4. **Launch the notebooks:**
   ```
   jupyter lab
   ```
   Then open the `notebooks/` folder and begin with `01-notebooks.ipynb`.

Prefer pip? A `requirements.txt` is provided as a fallback, but conda is smoother
for RDKit. See [SETUP.md](SETUP.md).

---

## The seven lectures

| # | Notebook | Python focus | Chemistry framing |
| --- | --- | --- | --- |
| 01 | `01-notebooks.ipynb` | notebooks, cells, Python as a calculator, `print`, help | molar mass by arithmetic; an RDKit "draw a molecule" demo |
| 02 | `02-variables.ipynb` | variables, types, strings, lists, dictionaries | SMILES as strings; an element → atomic-mass dictionary |
| 03 | `03-functions.ipynb` | `def`, parameters, `return`, defaults, docstrings, `import` | a hand-built `molar_mass()`, then RDKit's `Descriptors.MolWt` |
| 04 | `04-flow.ipynb` | booleans, `if`/`elif`/`else`, `for`/`while` loops, comprehensions | Lipinski's rule of five, by hand then with RDKit descriptors |
| 05 | `05-files.ipynb` | file paths, `with`, reading/writing, CSV, `try`/`except` | read `molecules.csv`, filter drug-like molecules, save a subset |
| 06 | `06-numpy.ipynb` | arrays, broadcasting, masks, aggregations | Beer–Lambert law; descriptor statistics; a UV–Vis spectrum |
| 07 | `07-plotting.ipynb` | matplotlib: line/scatter/bar/histogram, labels, saving | spectrum, calibration curve, property plots, a molecule grid |

A small set of molecules (water, ethanol, caffeine, aspirin, glucose, benzene,
ibuprofen, paracetamol, and several more — including sucrose and atorvastatin,
which deliberately *fail* the drug-likeness screen) recurs throughout so
concepts build on familiar data.

---

## Repository layout

```
python_for_chem_vibed/
├── README.md            # this file
├── SETUP.md             # beginner conda + RDKit walkthrough
├── environment.yml      # conda environment (recommended install path)
├── requirements.txt     # pip fallback
├── notebooks/           # the seven lecture notebooks
├── data/
│   ├── molecules.csv         # the recurring dataset (generated/verified by RDKit)
│   └── uvvis_spectrum.csv    # a synthetic UV–Vis spectrum for L06/L07
└── build/
    ├── make_data.py          # generates and verifies the data/ files
    └── build_notebooks.py    # generates the notebooks with nbformat
```

### A note on the notebooks

The notebooks are shipped with their **outputs cleared**, so you get the
satisfaction (and the learning) of running each cell yourself. They have all
been executed end-to-end during the build to confirm they run cleanly from top
to bottom — if a cell ever errors for you, the usual cause is running cells out
of order; use **Kernel → Restart Kernel and Run All**.

### Rebuilding the materials (for maintainers)

The `data/` files and notebooks are generated programmatically. To rebuild them:

```
conda activate chem-python
python build/make_data.py        # regenerate and verify data/
python build/build_notebooks.py  # regenerate the seven notebooks
```

Every numeric value in `data/molecules.csv` (molar mass, logP, hydrogen-bond
donors/acceptors) is computed by RDKit, so the figures are self-consistent.
Note that the `logp` column is RDKit's **computed** (Crippen) logP, which is
close to — but not identical to — experimentally measured logP.

You may also notice **water** is listed with 0 hydrogen-bond donors and 0
acceptors — which looks wrong, since water is the textbook hydrogen bonder. This
is because RDKit's Lipinski counts follow precise structural definitions that do
not always match chemical intuition for very small molecules. It is a useful
reminder (made in Lecture 04 too): a computed descriptor is only as meaningful
as its definition — always check what a number actually counts.

---

## Acknowledgements & where to go next

This course deliberately targets local Jupyter notebooks with conda, where RDKit
works fully. The closing section of Lecture 07 points to natural next steps:
real datasets, going deeper with RDKit (fingerprints, substructure search,
reactions), and a browser-based [marimo](https://marimo.io) version of the
workshop for experimenting without a local install.
