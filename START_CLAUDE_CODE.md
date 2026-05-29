# How to start Claude Code and build the course

A step-by-step guide for Windows. You only do steps 0–2 once; after that, building is steps 3–7.
Verified against the official Claude Code docs (code.claude.com/docs) as of 29 May 2026.

---

## Step 0 — What you need first

1. **A paid Claude plan.** Claude Code needs a **Pro, Max, Team, Enterprise, or Console (API)** account. The **free Claude.ai plan does not work** with Claude Code.
2. **Git for Windows** — recommended (it lets Claude Code use the Bash tool). You almost certainly already have it since you use GitHub; if not, install from `https://git-scm.com/downloads/win` with default settings.
3. **Miniforge (conda)** — needed so Claude Code can build the conda environment and run the notebooks. Install it from `https://conda-forge.org/download/` (Miniforge). Miniconda or Anaconda also work. Install with default settings, then close and reopen your terminal.

> You do **not** need to install Node.js. The native Claude Code installer below doesn't require it.

---

## Step 1 — Install Claude Code (native, one time)

Open **PowerShell** (Start menu → type "PowerShell" → Enter). Your prompt should start with `PS`.

Run:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then **close and reopen** PowerShell and check it worked:

```powershell
claude --version
```

You should see a version number.

**If you get "claude is not recognized":** the installer put `claude.exe` in `%USERPROFILE%\.local\bin` but didn't add it to your PATH. Fix it by running this in PowerShell, then reopening the terminal:

```powershell
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:USERPROFILE\.local\bin", [EnvironmentVariableTarget]::User)
```

Still stuck? Run `claude doctor` — it diagnoses install problems.

> Prefer not to use the terminal at all? There's also a Claude **Desktop app** that runs Claude Code with a graphical interface (`https://claude.com/download`). The steps below assume the terminal.

---

## Step 2 — Put the brief into your repo (one time)

Save the brief file (`CLAUDE_CODE_BRIEF_python-for-chemists.md`) into your repo folder:

```
C:\Users\44793\Documents\GitHub\python_for_chem_vibed\
```

You can rename it to `BRIEF.md` if you like — just remember whatever you call it for Step 4.

---

## Step 3 — Open a terminal *inside the repo folder*

In PowerShell:

```powershell
cd C:\Users\44793\Documents\GitHub\python_for_chem_vibed
```

(Tip: in File Explorer you can also open the folder, type `powershell` in the address bar, and press Enter — it opens a terminal already in that folder.)

---

## Step 4 — Launch Claude Code

```powershell
claude
```

The **first time**, a browser window opens asking you to log in to your Anthropic account. Do that once; it remembers you afterwards. You'll then land at the Claude Code prompt inside your repo.

---

## Step 5 — Give it the build instruction

Paste this prompt (adjust the filename if you didn't rename it to `BRIEF.md`):

> Read `BRIEF.md` in this repository. It is a complete specification for a course I want you to build — follow it exactly. In order: (1) create `environment.yml` (conda + RDKit from conda-forge), `requirements.txt`, `.gitignore`, and `SETUP.md` with the beginner conda walkthrough; (2) write the build scripts in `build/`, generate the `data/` files (verifying `molecules.csv` with RDKit), and build all 7 Jupyter notebooks programmatically with `nbformat`; (3) create the conda environment and execute every notebook end-to-end to confirm they run with no errors, fixing anything that breaks; (4) write `README.md`. Use British English throughout. Show me a short summary as you finish each notebook. Do **not** run any git commit or push — I'll review first.

Claude Code will work through it, asking permission before running commands or editing files. You can just approve as it goes. Building and executing 7 notebooks plus creating the conda environment will take a while — let it run.

---

## Step 6 — Review what it made

When it's done, check the work yourself before trusting it:

```powershell
conda activate chem-python
jupyter lab
```

A browser tab opens. Open `notebooks/01-notebooks.ipynb` and run the cells (Shift+Enter). Skim a couple of notebooks for: do they run cleanly, is the explanation actually clear for a beginner, are the chemistry facts right, is the molar-mass / Lipinski logic correct? Automated execution proves the code *runs*, not that the *teaching* is good — that part is your call.

If you want changes, just tell Claude Code in plain English, e.g. *"Notebook 04 is too long for an hour — trim the while-loop section"* or *"add more explanation before the first dictionary in Notebook 02"*. Iterating is normal and expected.

---

## Step 7 — Commit and push (when you're happy)

You can ask Claude Code to do it:

> Now commit everything with a sensible message and push to the `python_for_chem_vibed` repo.

…or do it yourself in PowerShell:

```powershell
git add .
git commit -m "Add Python for Chemists course: 7 notebooks, data, setup"
git push
```

---

## Handy Claude Code tips

- Press **Esc** to interrupt it mid-task; **Ctrl+C** twice to quit.
- Type `/clear` to start a fresh context if a long session gets muddled.
- Type `/help` to see all in-session commands.
- If something about the install misbehaves later, `claude doctor` is your first port of call.
- It updates itself in the background, so you don't need to reinstall.
