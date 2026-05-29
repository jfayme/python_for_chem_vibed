# Improvement Brief — "Python for Chemists" (revision pass)

**Audience:** Claude Code. **Working location:** the existing repo at
`C:\Users\44793\Documents\GitHub\python_for_chem_vibed`.

This is a revision pass over a course you already built. The course is good: the
template is consistent, the "build by hand, then RDKit" arc works well, the
chemistry framing is natural, British English is consistent, and the data file is
RDKit-verified. The fixes below address specific issues found by **running the
code**, checked against the original build brief.

**How to work:** make the edits in `build/build_notebooks.py` and
`build/make_data.py` (the notebooks are generated, so edit the generators, not the
`.ipynb` directly), then re-run `python build/make_data.py` and
`python build/build_notebooks.py`, then **execute every notebook end-to-end**
(`jupyter nbconvert --to notebook --execute`) to confirm no errors, and clear
outputs before shipping. **Do not commit or push** — the human will review.

Work top-down: Priority 0 first (correctness/consistency), then 1, then 2.

---

## Priority 0 — correctness and consistency (must fix)

### 0.1 The rule of five is defined three different ways, and they disagree
This is the course's flagship cheminformatics concept, and it is implemented
inconsistently:

- **NB04** (`rule_of_five`) and **NB05** (`passes_rule_of_five`): count violations,
  drug-like if **≤ 1 violation**. ✅ This is the correct Lipinski interpretation.
- **NB05 "the pandas way"** and **NB07** (`drug_like`): require **all four** limits
  to hold simultaneously, i.e. **0 violations**. ❌ This is stricter and is **not**
  the same rule — yet NB05 introduces it with the words "the same drug-like filter,
  the pandas way", which is incorrect.

Right now every molecule has 0 violations (see 0.2), so the discrepancy is hidden.
Once failing molecules are added it will produce contradictory labels for the same
molecule across notebooks.

**Fix:** use the **≤ 1 violation** definition *everywhere*. Replace the NB05 pandas
mask and the NB07 flag with a violation-count version. For NB07 (NumPy arrays):

```python
violations = ((mw > 500).astype(int) + (logp > 5).astype(int)
              + (donors > 5).astype(int) + (acceptors > 10).astype(int))
drug_like = violations <= 1
```
(pull `donors`/`acceptors` from the dataframe as arrays). Do the analogous thing in
the NB05 pandas section and make the surrounding prose state honestly that it
reproduces the ≤ 1-violation rule from Lecture 04.

### 0.2 The molecule set contains zero failing molecules — the screen demonstrates nothing
I ran the rule-of-five over the whole dataset: **all 10 molecules pass with 0
violations.** Consequences: NB05's "drug-like subset" filter keeps *everything*
(prints "10 of 10"), and NB07's "scatter coloured by drug-likeness" has **no red
points at all**. The flagship example screens nothing out.

**Fix:** add familiar molecules that genuinely fail, so PASS/FAIL variety is real.
These SMILES are verified to parse and to give the stated verdict under RDKit:

| name | SMILES | result |
| --- | --- | --- |
| sucrose | `OC1C(O)C(O)C(OC1CO)OC1(CO)OC(CO)C(O)C1O` | **FAIL** — 2 violations (8 donors, 11 acceptors) |
| atorvastatin | `CC(C)c1c(C(=O)Nc2ccccc2)c(-c2ccccc2)c(-c2ccc(F)cc2)n1CCC(O)CC(O)CC(=O)O` | **FAIL** — 2 violations (MW 559, logP 6.3) |
| cholesterol *(optional)* | `CC(C)CCCC(C)C1CCC2C1(CCC3C2CC=C4C3(CCC(C4)O)C)C` | PASS — but with **1 violation** (logP 7.4) |

- Add **sucrose** and **atorvastatin** to `MOLECULES` in `make_data.py` (sucrose is
  relatable "table sugar"; atorvastatin/Lipitor is a famous large drug — they fail
  for *different* reasons, which is good teaching). Cholesterol is optional but a
  nice borderline case (it has 1 violation yet still passes — illustrating that the
  rule allows *one* violation). Re-running `make_data.py` regenerates and verifies
  the CSV, so NB05/06/07 pick the new molecules up automatically.
- Also add **sucrose** (and ideally atorvastatin) to the hard-coded `smiles_set`
  dictionary inside **NB04**, so the in-notebook RDKit screen visibly prints at
  least one `FAIL` next to the passes.
- The brief asked for 8–12 rows; 12 (or 13 with cholesterol) is fine.

### 0.3 Two cases of "concept used before it is taught" (violates the brief)
Running the cells confirmed both:

- **NB03 default-argument example uses `if`**, but `if` is not taught until NB04.
  Replace the `moles(..., mass_in_mg=False)` example (which branches on a boolean)
  with a default that needs no control flow. A clean, on-theme choice that also
  foreshadows Beer–Lambert in NB06:
  ```python
  def absorbance(concentration, epsilon, path_length=1.0):
      "Beer-Lambert absorbance; path_length defaults to a standard 1 cm cuvette."
      return epsilon * concentration * path_length
  ```
  Show it called with and without the default `path_length`.
- **f-string width/alignment specs (`{name:<8}`, `{mass:6.2f}`) appear from NB04
  onward**, but NB02 only teaches the `.2f` form. Teach the wider syntax where
  f-strings are introduced: add a short paragraph + example in **NB02** right after
  the `.2f` example, explaining that a number before the dot sets a minimum width
  and `<`/`>` left/right-aligns (e.g. `f"{name:<8}{mass:6.2f}"` lines values up in
  columns). Then the later notebooks are using something already taught.

### 0.4 NB01 calls SMILES a "formula" (chemistry inaccuracy)
The learning objectives and intro say the RDKit demo draws "a molecule from its
formula". A SMILES string is **not** a molecular formula (formula = `C8H10N4O2`;
SMILES = the structural recipe). Change wording to "from its **structure** (a SMILES
string)" in the objective and anywhere else NB01 conflates the two.

---

## Priority 1 — clarity and trust

### 1.1 Water shows 0 H-bond donors and 0 acceptors — looks like broken data
Confirmed by running RDKit: water (and methane) come out as 0 donors / 0 acceptors,
because RDKit's Lipinski counts use strict structural SMARTS (a donor atom must
carry exactly one H, etc.) that don't match a chemist's intuition for tiny
molecules. A student or lecturer scanning the table will reasonably think the data
is wrong, which undermines trust in the whole course.

**Fix (do not hide it — explain it):** add a short **🧪 Chemistry aside** where
donors/acceptors first appear (NB04), and a one-line note in the README's data
section, along the lines of:

> You may notice water is listed with 0 hydrogen-bond donors and acceptors — which
> looks wrong, since water is the textbook hydrogen bonder. This is because RDKit's
> Lipinski counts follow precise structural definitions that don't always match
> chemical intuition for very small molecules. It's a useful reminder: a computed
> descriptor is only as meaningful as its definition — always check what a number
> actually counts.

### 1.2 NB04 reuses the name `molar_mass` as a float and then as a function
In the booleans section `molar_mass = 180.16` (a float); later `def molar_mass(...)`
redefines the same name as a function. This works top-to-bottom but contradicts the
brief's "clear names" principle and breaks if cells run out of order. Rename the
float to `aspirin_mass` (and similarly the stray `logp` float to `aspirin_logp`).

### 1.3 NB04 is overloaded for a single 60-minute beginner session
NB04 covers booleans, `if/elif/else`, rule-of-five-by-hand, `for` over lists and
dicts, filtering, `while`, `break`/`continue`, the RDKit rule-of-five, looping a
set, *and* list comprehensions. For absolute beginners that is too much for one
hour. Don't delete content, but help a lecturer flex:
- Mark the **`while` loop** and **list-comprehension** sections with a clear
  heading prefix like "Optional / stretch:" and a one-line note that they can be
  skipped on a first pass.
- Add a short note at the top of NB04 that it is the densest lecture and the
  optional sections can move to self-study if time is short.
(Consider the same "optional" tag for `break`/`continue`.)

### 1.4 Several notebooks have only 2 exercises; the brief asked for 3–5
Counts: NB01 ≈2–3, NB03 = 2, NB04 = 2, NB05 = 2, NB07 = 2. Add one or two more
"🔬 Try it yourself" exercises (each with a worked **Solution** cell) to **NB03,
NB04, NB05, NB07**. Concrete suggestions:
- **NB03:** write a `percent_by_mass(element_mass, molar_mass)` helper; or a
  function returning moles from grams *and* its reverse, tested on CO₂.
- **NB04:** the brief's "label a molecule small / medium / large with `if/elif/else`"
  as an exercise (currently only shown as a demo); and "count how many molecules in
  `smiles_set` fail the rule of five" (now meaningful once 0.2 is done).
- **NB05:** read the CSV with `csv.DictReader` and print each name + formula; and
  write only the *failing* molecules to a `non_drug_like.csv`.
- **NB07:** a bar chart of logP per molecule; and add axis labels/title/legend to a
  deliberately unlabelled starter plot.

---

## Priority 2 — polish

### 2.1 NB01 "two kinds of division" wording
The section says "Python has two kinds of division" then shows `/`, `//` **and**
`%`. `%` is the remainder, not a division. Reword to "two kinds of division (`/`
and `//`), plus the remainder operator `%`".

### 2.2 NB06 is missing the brief's quick speed before/after
The brief asked NB06 to show *why* NumPy with a quick speed comparison. NB06 shows
the behaviour difference (`list*2` vs `array*2`) but no timing. Add a tiny,
beginner-safe timing demo, e.g. summing a large array vs a Python loop using
`%timeit` or `time.perf_counter`, with one sentence of takeaway. Keep it short.

### 2.3 NB07 scatter uses red/green (colour-blindness)
The drug-like/not-drug-like scatter relies on green vs red, the hardest pair for
colour-blind readers. Use a colour-blind-safe pairing *and* distinct marker shapes
(e.g. blue circles for drug-like, orange crosses for not), and mention briefly why
(good-figure habit). This reinforces the "tidy scientific figure" message.

### 2.4 Keep code cells within ~8–12 lines
NB04's `rule_of_five` cell (~22 lines incl. the test call) exceeds the brief's
guideline. Split the function definition and the test call into two cells with a
sentence between them.

### 2.5 Clean up `make_data.py`
There is a confused, self-contradicting comment block around the `REPO_ROOT`
computation ("parent.parent? No: ... actually..."). Replace it with a single clear
line. Harmless but unprofessional.

### 2.6 Low-risk: `abs?` in NB01
The `?` help form is IPython-only. It should execute under `nbconvert --execute`,
but verify it doesn't error during the build; if it does, replace with `help(abs)`
and keep a one-line note that `abs?` works the same way interactively.

---

## After editing — re-verify against the original Definition of Done
Re-run `make_data.py` and `build_notebooks.py`, execute all seven notebooks, clear
outputs, then confirm:

- [ ] Every notebook runs top-to-bottom with no errors (re-run after the edits).
- [ ] Rule of five uses the **≤ 1 violation** definition in NB04, NB05 (both the
      `csv` and pandas paths) and NB07, and the prose says so honestly.
- [ ] The dataset contains clear FAIL molecules; NB05's filter removes some, NB07's
      scatter shows both colours/markers, and NB04 prints at least one `FAIL`.
- [ ] No concept is used before it is taught (NB03 default-arg, f-string width/align).
- [ ] NB01 describes the demo as drawing from a SMILES **structure**, not a formula.
- [ ] The water donor/acceptor surprise is explained, not left to look like a bug.
- [ ] NB03/04/05/07 each have at least 3 exercises, all with worked solutions.
- [ ] NB04's optional sections are clearly flagged; the `molar_mass` name is no
      longer reused as both a float and a function.
- [ ] British English and the standard template are still intact throughout.
- [ ] No git commit/push was performed.
