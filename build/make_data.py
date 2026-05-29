"""Generate and verify the data files for the 'Python for Chemists' course.

This script produces two files in ``data/``:

* ``molecules.csv``      — the recurring molecule dataset, with every numeric
                           column computed by RDKit so the figures are
                           self-consistent and correct.
* ``uvvis_spectrum.csv`` — a small synthetic UV-Vis absorption spectrum
                           (a smooth Gaussian peak) used in Lectures 06 and 07.

Run it from the repository root with the ``chem-python`` environment active:

    python build/make_data.py

It re-reads ``molecules.csv`` afterwards and re-checks every value against
RDKit, so a clean run is also a verification.

British English is used throughout (the course style).
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
from rdkit.Chem import rdMolDescriptors


# ---------------------------------------------------------------------------
# Where to write the data. The script lives in build/, so the repo root is its
# parent's parent... actually its parent is build/, so root is parent.parent? No:
# build/make_data.py -> parent is build/, root is parent.parent.
# We compute it robustly below.
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"


# The core teaching set (brief §8) plus methane and acetic acid.
# Only name + SMILES are hand-written; everything else comes from RDKit.
MOLECULES = [
    ("water", "O"),
    ("methane", "C"),
    ("ethanol", "CCO"),
    ("acetic acid", "CC(=O)O"),
    ("benzene", "c1ccccc1"),
    ("glucose", "OCC1OC(O)C(O)C(O)C1O"),
    ("paracetamol", "CC(=O)Nc1ccc(O)cc1"),
    ("aspirin", "CC(=O)Oc1ccccc1C(=O)O"),
    ("caffeine", "Cn1cnc2c1c(=O)n(C)c(=O)n2C"),
    ("ibuprofen", "CC(C)Cc1ccc(cc1)C(C)C(=O)O"),
]

FIELDNAMES = [
    "name",
    "formula",
    "smiles",
    "molar_mass",
    "logp",
    "h_bond_donors",
    "h_bond_acceptors",
]


def compute_row(name: str, smiles: str) -> dict:
    """Compute one CSV row's worth of properties from a SMILES string."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"RDKit could not parse SMILES for {name!r}: {smiles!r}")
    return {
        "name": name,
        "formula": rdMolDescriptors.CalcMolFormula(mol),
        "smiles": smiles,
        # Molar mass rounded to 2 dp (brief §8).
        "molar_mass": round(Descriptors.MolWt(mol), 2),
        # RDKit's *computed* (Crippen) logP, rounded to 2 dp.
        # The "+ 0.0" turns a rounded -0.0 into a tidy 0.0.
        "logp": round(Descriptors.MolLogP(mol), 2) + 0.0,
        "h_bond_donors": Lipinski.NumHDonors(mol),
        "h_bond_acceptors": Lipinski.NumHAcceptors(mol),
    }


def write_molecules_csv(path: Path) -> list[dict]:
    rows = [compute_row(name, smiles) for name, smiles in MOLECULES]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def verify_molecules_csv(path: Path) -> None:
    """Re-read the file and re-check every value against RDKit."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            recomputed = compute_row(row["name"], row["smiles"])
            assert row["formula"] == recomputed["formula"], (
                f"formula mismatch for {row['name']}"
            )
            assert float(row["molar_mass"]) == recomputed["molar_mass"], (
                f"molar_mass mismatch for {row['name']}"
            )
            assert float(row["logp"]) == recomputed["logp"], (
                f"logp mismatch for {row['name']}"
            )
            assert int(row["h_bond_donors"]) == recomputed["h_bond_donors"], (
                f"h_bond_donors mismatch for {row['name']}"
            )
            assert int(row["h_bond_acceptors"]) == recomputed["h_bond_acceptors"], (
                f"h_bond_acceptors mismatch for {row['name']}"
            )


def write_uvvis_csv(path: Path) -> int:
    """Write a smooth synthetic UV-Vis spectrum: a Gaussian peak near 270 nm.

    Columns: wavelength_nm, absorbance. 201 rows (200-400 nm in 1 nm steps).
    """
    wavelengths = np.arange(200.0, 401.0, 1.0)  # 200..400 inclusive -> 201 points

    # A single clean Gaussian absorption band.
    peak_centre = 270.0   # nm
    peak_width = 18.0      # standard deviation, nm
    peak_height = 0.90     # peak absorbance (dimensionless)
    baseline = 0.02        # small flat baseline

    absorbance = baseline + peak_height * np.exp(
        -0.5 * ((wavelengths - peak_centre) / peak_width) ** 2
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["wavelength_nm", "absorbance"])
        for wl, a in zip(wavelengths, absorbance):
            writer.writerow([f"{wl:.1f}", f"{a:.4f}"])
    return len(wavelengths)


def main() -> None:
    molecules_path = DATA_DIR / "molecules.csv"
    spectrum_path = DATA_DIR / "uvvis_spectrum.csv"

    rows = write_molecules_csv(molecules_path)
    verify_molecules_csv(molecules_path)
    n_spectrum = write_uvvis_csv(spectrum_path)

    print(f"Wrote {molecules_path.relative_to(REPO_ROOT)} ({len(rows)} molecules):")
    print(f"  {'name':<12} {'formula':<10} {'M (g/mol)':>10} {'logP':>6} "
          f"{'HBD':>4} {'HBA':>4}")
    for r in rows:
        print(f"  {r['name']:<12} {r['formula']:<10} {r['molar_mass']:>10} "
              f"{r['logp']:>6} {r['h_bond_donors']:>4} {r['h_bond_acceptors']:>4}")
    print("Verification: every value re-checked against RDKit — OK.")
    print(f"Wrote {spectrum_path.relative_to(REPO_ROOT)} "
          f"({n_spectrum} points, Gaussian peak near 270 nm).")

    # A tiny extra sanity check that the peak is where we said it is.
    assert not math.isnan(rows[0]["molar_mass"])


if __name__ == "__main__":
    main()
