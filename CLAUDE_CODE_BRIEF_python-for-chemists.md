# Build Brief — "Python for Chemists" (7-Lecture Introductory Course)

**Audience for this document:** Claude Code.
**What you are building:** a self-contained set of teaching materials. Follow this brief exactly. Where it leaves a choice open, choose the option that is simplest for an absolute beginner.

**Repository & working location**
- GitHub repo: `https://github.com/jfayme/python_for_chem_vibed`
- Local folder (Windows): `C:\Users\44793\Documents\GitHub\python_for_chem_vibed`
- Build everything **at the repository root** (the local folder above). Do not nest the project inside an extra sub-folder.
- Do **not** push or commit to git unless explicitly asked — the human will review first.

---

## 1. Goal

Build a beginner Python course for chemistry undergraduates, delivered as **7 Jupyter notebooks** (`.ipynb`). Each notebook is the support material for **one 60-minute lecture**. The notebooks must be readable as standalone learning resources (a student who missed the lecture should be able to follow them alone) and also work as live teaching material.

The seven lectures, in order, are fixed:

1. `01-notebooks.ipynb` — Notebooks
2. `02-variables.ipynb` — Variables
3. `03-functions.ipynb` — Functions
4. `04-flow.ipynb` — Flow (control flow)
5. `05-files.ipynb` — Files
6. `06-numpy.ipynb` — NumPy
7. `07-plotting.ipynb` — Plotting

---

## 2. Who the students are (read this carefully — it drives every decision)

- Bachelor-level chemistry students.
- **Zero prior programming experience.** Assume they have never opened a terminal, never written a line of code, and do not know what a "variable" or "function" is.
- **Beginners in cheminformatics too.** Do not assume they know what SMILES, logP, or a molecular descriptor is. Every chemistry-flavoured concept must be introduced in one or two plain sentences before it is used.
- They *are* competent chemists: molar mass, concentration, the Beer–Lambert law, atomic masses, and basic spectroscopy are fair game and should be used as the *motivating context* for the coding.

The pedagogical strategy is: **teach generic Python fundamentals, but frame every example in a chemistry/cheminformatics context** so the material feels relevant rather than abstract. The Python concept is always the real lesson; the chemistry is the wrapper.

---

## 3. Deliverables (exact file tree, at the repo root)

```
python_for_chem_vibed/            (= the local folder above)
├── README.md                     # course overview + quick-start (points to SETUP.md)
├── SETUP.md                      # beginner-friendly conda + RDKit setup walkthrough (see §4a)
├── environment.yml               # conda environment incl. RDKit (the RECOMMENDED install path)
├── requirements.txt              # pip fallback (see §4) — RDKit + the rest
├── .gitignore                    # ignore .ipynb_checkpoints/, __pycache__/, env folders, etc.
├── notebooks/
│   ├── 01-notebooks.ipynb
│   ├── 02-variables.ipynb
│   ├── 03-functions.ipynb
│   ├── 04-flow.ipynb
│   ├── 05-files.ipynb
│   ├── 06-numpy.ipynb
│   └── 07-plotting.ipynb
├── data/
│   ├── molecules.csv             # the recurring dataset (see §8) — used from L05 onwards
│   └── uvvis_spectrum.csv        # a small synthetic UV–Vis spectrum for L06/L07
└── build/
    ├── make_data.py              # generates/verifies the data/ files (uses RDKit)
    └── build_notebooks.py        # generates the .ipynb files via nbformat
```

---

## 4. Environment & dependencies

- Target a **local Jupyter / JupyterLab** environment running CPython 3.10+, managed with **conda** (see §4a). RDKit is included.
- **conda is the recommended install path** because RDKit installs cleanly from the `conda-forge` channel. Provide `environment.yml` with:
  - channel: `conda-forge`
  - packages: `python>=3.10`, `jupyterlab`, `notebook`, `numpy`, `matplotlib`, `pandas`, `rdkit`
- Also provide a `requirements.txt` as a **pip fallback** (`jupyterlab`, `numpy`, `matplotlib`, `pandas`, `rdkit`) and note in SETUP.md that `pip install rdkit` works too, but conda is smoother for beginners.
- `pandas` is used mainly from Notebook 05 onwards (reading a CSV) and lightly in 06/07. Introduce it gently as "a tool for tabular data" — do not turn the course into a pandas course.
- **RDKit is now a required, taught part of the course** (the human asked for it explicitly, and locally-run Jupyter supports it). See the RDKit teaching principle in §5 and the per-notebook plan in §9. Key APIs you will use (use these, do not invent others):
  - `from rdkit import Chem` — `mol = Chem.MolFromSmiles("CCO")`
  - `from rdkit.Chem import Draw` — `Draw.MolToImage(mol)`, `Draw.MolsToGridImage([...], legends=[...])`
  - `from rdkit.Chem.Draw import IPythonConsole` — makes mol objects render inline automatically in Jupyter
  - `from rdkit.Chem import Descriptors` — `Descriptors.MolWt(mol)`, `Descriptors.MolLogP(mol)` (this is Crippen's *computed* logP), `Descriptors.TPSA(mol)`
  - `from rdkit.Chem import Lipinski` — `Lipinski.NumHDonors(mol)`, `Lipinski.NumHAcceptors(mol)`
- Every notebook must run **top to bottom with no errors** in this environment, using only the packages above and the files in `data/`.

### 4a. Brief intro to conda (required content — write this into SETUP.md, short version into README)

The students have never installed Python. SETUP.md must hold their hand. Write it in plain British English with copy-pasteable commands. It must cover, briefly:

1. **What conda is** — one short paragraph: conda is a tool that installs Python *and* scientific packages (like RDKit) for you, and lets you keep each project in its own isolated **environment** so projects don't interfere with one another. Use an analogy ("a separate, clean toolbox per project").
2. **What to install** — recommend **Miniforge** (a small conda installer that uses the `conda-forge` channel by default; good for RDKit and avoids licensing concerns of full Anaconda). Give the download location (`https://conda-forge.org/download/` / the Miniforge GitHub releases) and note Miniconda or Anaconda also work.
3. **Create the environment from the file** — from inside the project folder:
   ```
   conda env create -f environment.yml
   ```
   Explain this reads `environment.yml` and builds an environment (suggest naming it `chem-python` via the `name:` field in the yml).
4. **Activate it every time** — `conda activate chem-python` (explain they must do this in each new terminal before working).
5. **Launch the notebooks** — `jupyter lab` (or `jupyter notebook`), explaining a browser tab opens and they navigate into `notebooks/`.
6. **A 3-line "what is a notebook" teaser** pointing them to Lecture 01.
7. Keep it friendly and reassuring: setup is the most intimidating bit and everyone finds it fiddly the first time. Be honest, not breezy.

Also add a **3–4 sentence conda recap** near the top of Notebook 01 ("you've already created your environment with conda — here's the one-paragraph reminder of why"), so the lecture is self-contained but doesn't repeat the whole of SETUP.md.

---

## 5. Pedagogical principles (apply to all notebooks)

1. **One new idea at a time.** Introduce a concept in a short markdown cell, immediately show a tiny runnable code cell that demonstrates it, then let the student try a variation.
2. **Show, then explain, then practise.** Never present a wall of code. Maximum ~8–12 lines per code cell; split longer examples across cells with explanation between them.
3. **Everything runs.** No pseudo-code, no "imagine this returns…". Every code cell executes and produces visible output. Use `print()` generously so beginners can *see* what happened.
4. **Plain language.** Explain jargon the first time it appears (e.g. "a *string* is just text", "*iterating* means going through items one by one"). Define a chemistry term the same way ("*logP* is a number describing how fat-loving vs water-loving a molecule is — higher means more fat-loving").
5. **Spaced exercises, not a final exam.** Sprinkle 3–5 small "Try it yourself" exercises through each notebook, each immediately after the relevant concept. Provide worked solutions (see §6 for how to present them).
6. **No magic.** If you use something not yet taught, either teach it first or flag it explicitly as "we'll cover this properly later — for now just copy it".
7. **Honesty about difficulty.** It is fine to say "this bit is fiddly and everyone finds it confusing at first." Do not over-promise ("super easy!").
8. **RDKit: build it by hand first, then meet the library.** This is the central rule for weaving RDKit in without it swallowing the Python lesson. For each cheminformatics task, FIRST have students implement it in plain Python (so they learn the dictionary/loop/function concept), THEN reveal the RDKit one-liner that does the same thing, and compare the two results. Frame RDKit explicitly as "the professional tool — and now you understand what it's doing under the bonnet." RDKit must never replace the fundamental Python lesson; it rewards and reinforces it. In the very early material (Notebook 01–02) RDKit appears only as short "look what's coming" demos, not as something the student must understand yet.

---

## 6. Standard notebook template (use this exact skeleton for all 7)

Each notebook must contain, in order:

1. **Title cell (markdown):** `# Lecture N — <Topic>` plus a one-line subtitle of the chemistry framing.
2. **Learning objectives (markdown):** a short bulleted list, "By the end of this lecture you will be able to…", 4–6 items, phrased as concrete skills.
3. **Recap (markdown)** — *from Notebook 02 onward only*: 2–3 bullets reminding the student what the previous lecture covered.
4. **Main content:** alternating markdown → code → (optional) "Try it yourself" exercise, following §5. Group into clearly headed sections (`## Section title`).
5. **Chemistry asides:** where a chemistry concept is used, include a short blockquote-style markdown note titled **"🧪 Chemistry aside"** explaining it in 1–3 sentences.
6. **RDKit asides:** when RDKit is introduced in a notebook, mark the moment with a short note titled **"⚗️ With RDKit"** so students can see clearly where the hand-built version ends and the professional tool begins.
7. **Exercises with solutions:** present each "Try it yourself" as a markdown prompt followed by an *empty or partially-filled* code cell for the student. Then provide the solution in a clearly marked **"Solution"** markdown cell + code cell immediately after, so the standalone reader can check themselves. (Do not hide solutions behind tooling that may not render — keep them as ordinary cells.)
8. **Summary (markdown):** "Key takeaways" — 4–6 bullets recapping the concepts (not the chemistry).
9. **Looking ahead (markdown):** one sentence on what the next lecture covers. (In Notebook 07, instead point to where to go next: real datasets, more of RDKit, and the browser-based marimo version of the workshop.)

Keep the *visual rhythm* consistent across all seven notebooks so students always know where they are.

---

## 7. Style & conventions

- **British English throughout** — in all prose, comments, and identifiers where a spelling choice arises (e.g. "colour", "normalise", "analyse", "centre", "behaviour", "litre", "metre"). Be consistent.
- Use **`g/mol`**, SI-ish units, and chemistry conventions students recognise.
- Code style: clear, beginner-friendly variable names (`molar_mass`, not `mm`), comments that explain *why* not *what*, `snake_case` for names, f-strings for output. Do not introduce advanced idioms ahead of schedule.
- Markdown: use headings, short paragraphs, and bold for the *first* appearance of a key term. Avoid huge text blocks.
- Tone: warm, encouraging, plain. No hype.

---

## 8. The recurring cheminformatics thread (continuity device)

To make the course feel coherent, reuse a small, consistent set of molecules across the notebooks so concepts build on familiar data.

**Core molecule set** (use these throughout): water, ethanol, caffeine, aspirin, glucose, benzene, ibuprofen, paracetamol. For each, you will progressively use: name, molecular formula, SMILES, molar mass (g/mol), and logP.

Build `data/molecules.csv` with columns:
`name, formula, smiles, molar_mass, logp, h_bond_donors, h_bond_acceptors`
(8–12 rows; include the core set plus a couple more such as methane and acetic acid).

**Generate and verify the CSV with RDKit** (in `build/make_data.py`): for each SMILES, compute `molar_mass` from `Descriptors.MolWt`, `logp` from `Descriptors.MolLogP`, donors/acceptors from `Lipinski.NumHDonors`/`NumHAcceptors`. This guarantees the numbers are self-consistent and correct. **Important honesty note to put in a chemistry aside:** the `logp` column is RDKit's *computed* (Crippen) logP, which is close to but not identical to experimentally measured logP — say so plainly. Round molar masses sensibly (2 dp).

Build `data/uvvis_spectrum.csv` with columns `wavelength_nm, absorbance` (a smooth synthetic peak, e.g. a Gaussian centred ~270 nm, ~100–200 rows), for use in Notebooks 06 and 07.

**Use the thread like this (hand-built first, RDKit second — see §5.8):**
- L01: a single RDKit "wow" demo at the end (draw a molecule from a SMILES) — pure motivation, also confirms the environment works.
- L02: SMILES/formulae as strings; a dictionary of atomic masses; brief RDKit teaser turning a SMILES string into a drawable molecule object.
- L03: build a `molar_mass()` function by hand from the atomic-mass dictionary → then reveal `Descriptors.MolWt` and compare.
- L04: implement Lipinski's rule of five with `if/elif/else` by hand → then use RDKit-computed descriptors to drive the same logic; loop over several molecules.
- L05: read `molecules.csv` from disk; convert the `smiles` column to RDKit molecules; recompute/verify properties; write a filtered subset back out.
- L06: build a NumPy array of RDKit descriptors across the molecule set; do statistics; process the spectrum.
- L07: plot the spectrum and the molecular properties; use `Draw.MolsToGridImage` to display the molecules.

---

## 9. Detailed content specification per notebook

For each notebook, cover **at least** the listed concepts, in roughly the given order, each with a runnable chemistry-framed example and a small exercise. You may add small connective material but **do not introduce concepts from later lectures early**. Apply the RDKit rule from §5.8 everywhere.

### Notebook 01 — Notebooks
*Python concepts:* what a notebook is; code vs markdown cells; running a cell; **execution order matters**; `print()`; Python as a calculator (`+ - * / ** %`); integer vs decimal division feel (observationally, no theory); comments with `#`; how to get help (`help()`, `?`).
*Chemistry framing:* "Why should a chemist learn to code?" (reproducibility, automating tedious calculations, handling spectra/large datasets). First real calculation: molar mass of water *by typing the arithmetic directly* (`2*1.008 + 15.999`). A dilution or unit-conversion calculator exercise.
*RDKit:* end the notebook with a short **"⚗️ With RDKit"** wow-demo — `Chem.MolFromSmiles` + `Draw.MolToImage` to draw caffeine or aspirin from its SMILES — framed as "by the end of this course, you'll understand exactly how this works." Students just run it; no explanation required yet. This doubles as a check that conda + RDKit installed correctly.
*Also include:* the short conda recap from §4a; and one friendly line that the browser-based marimo version of this workshop loses work if the cache is cleared, whereas these local `.ipynb` files save to disk.
*Exercises:* run cells out of order to see what breaks; compute the molar mass of CO₂ as raw arithmetic; add a comment; `print()` a sentence.

### Notebook 02 — Variables
*Python concepts:* variables & assignment; core types `int`, `float`, `str`, `bool`; `type()`; **strings** (quotes, concatenation, f-strings, `.upper()`, `.replace()`, `len()`); **lists** (creating, 0-based indexing, slicing, `.append()`, `len()`); **dictionaries** (key→value, lookup, adding keys); brief mention of tuples as "fixed lists".
*Chemistry framing:* SMILES and molecular formulae are just **strings** (introduce SMILES in one sentence as "a text recipe for a molecule"). A list of element symbols / molecule names. Headline example: a **dictionary mapping element symbol → atomic mass**, then storing one molecule's data in variables / a small dict.
*RDKit:* a light **"⚗️ With RDKit"** teaser — `mol = Chem.MolFromSmiles("CCO")` turns the *string* "CCO" into a molecule object you can draw. Point out the input is just a string they now understand; the object itself is for later notebooks.
*Exercises:* store and print ethanol's details; index/slice a list of molecule names; look up an atomic mass in the dictionary; build an f-string reporting a molar mass to 2 dp.

### Notebook 03 — Functions
*Python concepts:* defining functions (`def`), parameters, `return`; calling functions; why functions exist; default arguments; **docstrings**; beginner-level scope ("variables inside a function are private"); **importing modules** (`import math`, `from math import pi`) and the idea of libraries.
*Chemistry framing:* turn the L01/L02 molar-mass arithmetic into a **reusable `molar_mass()` function** taking a dict of `{element: count}` and using the atomic-mass dictionary. Add `moles_from_mass(mass_g, molar_mass)`. Use `math` via e.g. `math.log10` for a quick pH-from-concentration example.
*RDKit:* the key **"⚗️ With RDKit"** reveal — after building `molar_mass()` by hand, show `Descriptors.MolWt(Chem.MolFromSmiles(smiles))` does the same job in one line; compute it for ethanol/aspirin and compare to the hand-built result. Frame importing RDKit as exactly the same `import` idea just taught, applied to a professional library.
*Exercises:* write grams↔moles conversion functions; add a docstring; give a function a default argument; write a function that builds a report string for a molecule.

### Notebook 04 — Flow (control flow)
*Python concepts:* booleans & comparison operators; `and / or / not`; `if / elif / else`; `for` loops (over lists and over dict items); `while` loops (one clear example + infinite-loop warning); `break` / `continue`; a **gentle** first look at list comprehensions *after* the explicit loop is understood.
*Chemistry framing:* loop over the core molecule list and print each molar mass (reusing L03). **Lipinski's rule of five** as the flagship `if/elif/else` example (MW ≤ 500, logP ≤ 5, H-bond donors ≤ 5, H-bond acceptors ≤ 10 → "drug-like?"); introduce logP and the rule in a chemistry aside. Filter a list to molecules below a molar-mass cut-off.
*RDKit:* implement the rule-of-five check first with hand-held numbers, then **"⚗️ With RDKit"** compute the four descriptors live with `Descriptors.MolWt`, `Descriptors.MolLogP`, `Lipinski.NumHDonors`, `Lipinski.NumHAcceptors`, and run the same `if` logic on RDKit's values. Loop over all SMILES and print each molecule's pass/fail.
*Exercises:* loop to find the heaviest molecule; `if` that labels "small / medium / large"; implement the Lipinski check as a function returning `True/False`; rewrite a simple loop as a comprehension.

### Notebook 05 — Files
*Python concepts:* what a file path is; `open()` with the `with` block (and *why*); reading text (`.read()`, `.readlines()`, line-by-line); writing a file; CSV as comma-separated text; reading CSV first with the built-in `csv` module **then** the easier `pandas.read_csv`; basic `try / except` for a missing file.
*Chemistry framing:* read `data/molecules.csv`, loop over rows, report molar masses, apply the L04 Lipinski filter, and **write the drug-like subset to a new CSV**. Frame as "the everyday chemist's task: take a data file, process it, save the result." Introduce a pandas DataFrame minimally as "a smart table".
*RDKit:* **"⚗️ With RDKit"** — take the `smiles` column from the CSV, convert each with `Chem.MolFromSmiles`, and recompute properties to confirm they match the file. Mention in an aside that SDF/MOL are other common chemistry file formats RDKit can read (one line, no deep dive).
*Exercises:* read the CSV and print all names; count how many pass the rule of five; write a small summary text file; wrap a file read in `try/except` and trigger the error.

### Notebook 06 — NumPy
*Python concepts:* why NumPy (arrays vs lists, vectorised maths, speed — one quick before/after); creating arrays (`np.array`, `np.arange`, `np.linspace`, `zeros/ones`); element-wise arithmetic & **broadcasting**; indexing & slicing; boolean masks (`arr[arr > x]`); aggregations (`mean`, `std`, `min`, `max`, `sum`).
*Chemistry framing:* (1) **Beer–Lambert law** `A = ε·c·l` across an array of concentrations in one line (broadcasting) — introduce Beer–Lambert in an aside. (2) summary statistics over the molecule properties. (3) load `uvvis_spectrum.csv` and do array work: peak via `argmax`, normalise absorbance, slice a wavelength window.
*RDKit:* **"⚗️ With RDKit"** — build a NumPy array of descriptors by looping the SMILES through RDKit (e.g. columns MolWt, MolLogP, TPSA), then do NumPy statistics on that array. This shows RDKit (objects) and NumPy (numbers) working together.
*Exercises:* concentration array → absorbances; mean & standard deviation of molar masses; boolean mask to select logP above a threshold; locate the wavelength of maximum absorbance.

### Notebook 07 — Plotting
*Python concepts:* `matplotlib.pyplot` basics; line, scatter, bar, histogram; axis labels, title, legend, limits; multiple series on one axes; figure size; saving a figure (`plt.savefig`); brief note on tidy, publication-style plots (units on axes).
*Chemistry framing:* (1) plot the **UV–Vis spectrum** as a line plot with proper labels (wavelength / nm, absorbance), annotate the peak. (2) **Beer–Lambert calibration curve** (absorbance vs concentration) as a scatter with a best-fit line from the L06 numbers. (3) **scatter of molar mass vs logP**, coloured by drug-likeness. (4) **histogram** of molar masses. Stress that a good scientific figure always has labelled, unit-bearing axes.
*RDKit:* **"⚗️ With RDKit"** — use `Draw.MolsToGridImage(mols, legends=names)` to display the molecule set as a labelled grid alongside the property plots, tying the visual molecules back to the numbers being plotted.
*Exercises:* relabel/restyle a plot; add a legend; plot two spectra on one axes; save a figure as PNG.
*Closing "Where to go next" section:* point to real datasets, going deeper with RDKit (fingerprints, substructure search, reactions), and the browser-based marimo version of the workshop for experimenting without a local install.

---

## 10. How to build the notebooks (technical)

1. **Set up the environment first.** Create `environment.yml` (and `requirements.txt`), then create and use the conda environment so you can actually execute notebooks during the build. If conda is unavailable on the machine, say so clearly and fall back to a venv + `pip install rdkit numpy matplotlib pandas jupyterlab nbformat nbclient`.
2. **Generate the data first.** Write `build/make_data.py` to produce and verify `data/molecules.csv` (via RDKit) and `data/uvvis_spectrum.csv`. Run it and sanity-check the output.
3. **Generate the notebooks programmatically with `nbformat`** (`build/build_notebooks.py`), one clearly-named function per notebook constructing cells from markdown/code lists. Do not hand-write raw notebook JSON.
4. **Execute every notebook end-to-end** to verify it runs with no errors and produces sensible output. Use `jupyter nbconvert --to notebook --execute` (or `nbclient`). Fix anything that errors. RDKit drawing cells must actually render.
5. **Ship notebooks with outputs cleared** (so students get the satisfaction of running cells), but confirm during the build that they execute cleanly. State this choice in the README.
6. Write a sensible `.gitignore`. Do **not** run any git commands (commit/push) unless the human asks.

---

## 11. Definition of done (quality checklist)

Before declaring finished, verify every item:

- [ ] All 7 notebooks exist with the correct names and the standard template from §6.
- [ ] Each notebook is sized for ~60 minutes of teaching (roughly 8–14 content sections with interleaved exercises).
- [ ] Every code cell runs top-to-bottom with **no errors**, using only `rdkit`, `numpy`, `matplotlib`, `pandas`, and the standard library.
- [ ] RDKit follows the "build by hand first, then reveal the library" rule (§5.8); it never short-circuits the underlying Python lesson.
- [ ] No concept is used before it is taught; later-lecture material does not leak earlier.
- [ ] Every chemistry term (SMILES, logP, molar mass, Beer–Lambert, Lipinski, etc.) is explained in plain language before use, including the honesty note that RDKit logP is *computed*, not measured.
- [ ] `data/molecules.csv` is generated/verified with RDKit and the values are correct.
- [ ] Exercises each have a clearly-marked worked solution.
- [ ] **British English** spelling is consistent everywhere.
- [ ] The recurring molecule dataset is used consistently from L02 → L07.
- [ ] `environment.yml` (conda + RDKit) and `requirements.txt` (pip fallback) both exist and are correct.
- [ ] `SETUP.md` contains the beginner conda + RDKit walkthrough from §4a; `README.md` gives a short overview and quick-start and points to SETUP.md.
- [ ] Notebook 01 contains the short conda recap and an RDKit wow-demo that also verifies the install.
- [ ] Tone is encouraging, plain, and honest — appropriate for someone who has never coded.
- [ ] No git commit/push was performed.

---

### Note on the source image / marimo
The original workshop screenshot shows these seven topics delivered as **marimo** notebooks running in the browser via WebAssembly (which is why RDKit was unavailable *there*). This brief deliberately targets **`.ipynb` (Jupyter) notebooks run locally with conda**, where RDKit works fully — as requested. The teaching content is platform-independent, so it could later be ported to marimo `.py` notebooks (minus RDKit in the browser) if desired.
