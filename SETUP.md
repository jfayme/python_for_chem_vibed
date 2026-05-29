# Setup — getting Python, conda and RDKit ready

This is the most intimidating part of the whole course, and that is completely
normal. Everyone finds the first install a bit fiddly. Take it slowly, copy and
paste the commands exactly, and you will get there. Once it is done, you never
have to do it again.

By the end of this page you will have:

- a working Python, installed through **conda**;
- an isolated **environment** called `chem-python` containing everything the
  course needs (including **RDKit**, the chemistry toolkit);
- **JupyterLab** open in your browser, showing the seven lecture notebooks.

---

## 1. What is conda (and why bother)?

**conda** is a tool that installs Python *and* scientific packages — things like
NumPy, matplotlib and RDKit — for you, without you having to fight with each one
separately. Crucially, it lets you keep every project in its own isolated
**environment**.

> Think of an environment as **a separate, clean toolbox for each project**.
> The tools you put in one toolbox can't knock over or clash with the tools in
> another. If a project ever gets into a mess, you just throw that one toolbox
> away and build a fresh one — your other projects are untouched.

For this course we will create one toolbox called `chem-python`.

---

## 2. Install conda (Miniforge recommended)

If you have never installed Python before, install **Miniforge**. It is a small
conda installer that already points at the **conda-forge** channel — the
community package collection that RDKit installs from cleanly. It also avoids
the licensing questions that come with the full Anaconda distribution.

1. Go to **<https://conda-forge.org/download/>** (this is the Miniforge
   download page; it links to the Miniforge GitHub releases).
2. Download the installer for your operating system (on Windows, the `.exe`).
3. Run it and accept the **default settings**.
4. **Close and reopen your terminal** afterwards, so it picks up conda.

> Already have **Miniconda** or **Anaconda**? Those work too — you can skip this
> step. If you use Anaconda, the commands below are identical.

To check conda is installed, open a terminal (on Windows, **PowerShell**) and
run:

```
conda --version
```

You should see something like `conda 24.5.0`. If instead you get
"command not found", close the terminal, open a fresh one, and try again — the
installer's changes only apply to new terminals.

---

## 3. Get the course files

Download or clone this repository so you have a folder called
`python_for_chem_vibed` on your computer, then move into it in the terminal:

```
cd path/to/python_for_chem_vibed
```

On Windows that might look like:

```
cd C:\Users\you\Documents\GitHub\python_for_chem_vibed
```

You should now be **inside** the project folder. (If you list the contents you
will see `environment.yml`, a `notebooks` folder, and so on.)

---

## 4. Create the environment from the file

The repository ships with `environment.yml`, a short recipe that lists
everything the course needs. From inside the project folder, run:

```
conda env create -f environment.yml
```

This reads `environment.yml`, downloads Python plus all the packages
(JupyterLab, NumPy, matplotlib, pandas and RDKit), and builds them into a brand
new environment named **`chem-python`**. The first time it runs it has a lot to
download, so **expect it to take several minutes** — this is normal, let it
finish.

> **pip alternative.** If you'd rather not use conda, there is a
> `requirements.txt` for pip, and `pip install rdkit` does now work. But conda
> is genuinely smoother for beginners here — it sorts out RDKit's tricky
> non-Python parts for you — so we recommend it.

---

## 5. Activate the environment (every time)

Before you do any work, you must **activate** the toolbox so the terminal uses
its tools and not the system's:

```
conda activate chem-python
```

Your prompt will usually change to show `(chem-python)` at the start. You have
to do this **once in every new terminal window** before working — if a command
later complains a package is missing, the most common reason is that you forgot
this step.

---

## 6. Launch the notebooks

Still inside the project folder and with the environment active, start
JupyterLab:

```
jupyter lab
```

A tab opens in your web browser showing a file list. (If it doesn't open
automatically, copy the `http://localhost:...` link the terminal prints into
your browser.) In the file browser on the left, open the **`notebooks`** folder
and double-click **`01-notebooks.ipynb`** to begin.

> Prefer the classic interface? `jupyter notebook` works too.

When you're finished, save your work (Ctrl+S), close the browser tab, and press
**Ctrl+C** in the terminal to stop the server.

---

## 7. What is a notebook? (the 10-second version)

A Jupyter notebook is a document that mixes **text** you can read with **code**
you can run, one block ("cell") at a time. You run a cell by clicking it and
pressing **Shift+Enter**; the result appears just underneath. Because these
`.ipynb` files live on your disk, your work is saved when you save the file.

That's all you need to start. **Lecture 01** explains notebooks properly — head
there next.

---

### Quick reference

| What you want to do | Command |
| --- | --- |
| Check conda is installed | `conda --version` |
| Create the environment (once) | `conda env create -f environment.yml` |
| Activate it (every new terminal) | `conda activate chem-python` |
| Start the notebooks | `jupyter lab` |
| Stop the notebook server | Ctrl+C in the terminal |
| Rebuild a broken environment | `conda env remove -n chem-python` then create again |
