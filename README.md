# Dynamic Regular Witnesses for Near-Exact State Complexity

Source and audit package for:

**Dynamic Regular Witnesses for Near-Exact State Complexity of Explicit Binary Consensus with Periodic Time**

Ryutaro Yonezu — Independent Researcher  
Version v1.0.0  
Date: September 6, 2026  
Status: preprint / not peer reviewed

## Main results

For deterministic binary consensus with explicit termination in anonymous synchronous 1-interval-connected dynamic networks under one-bit broadcast-counting communication and a free globally aligned phase `phi_t = t mod P`:

For every `n >= 15`,

```text
2 + ceil((n - 13)/P) <= S_n(n,P) <= 2 + ceil((n - 1)/P).
```

For even `n >= 12`,

```text
S_n(n,P) >= 2 + ceil((n - 10)/P).
```

At the minimum persistent-state budget,

```text
S_n(n,P) = 3  iff  P >= n - 1,   for n >= 4.
```

The paper does **not** claim the full exact formula
`S_n(n,P) = 2 + ceil((n-1)/P)` for arbitrary state budgets.

## Direct predecessor

Ryutaro Yonezu, *Two-Orbit Packing for Exact State Complexity of Explicit Binary Consensus in Anonymous Dynamic Networks with Periodic Time*, Zenodo preprint v1.0.0, 2026.  
Paper DOI: `10.5281/zenodo.22538052`  
Software DOI: `10.5281/zenodo.22538011`

## Files

- `paper.tex` — final v1.0.0 LaTeX source.
- `Yonezu_2026_Dynamic_Regular_Witnesses_Near_Exact_State_Complexity.pdf` — authoritative final manuscript PDF.
- `audit/construction_audit_6253.py` — finite implementation audit of the 6,253 regular slow-cone schedule cases reported in the paper.
- `audit/construction_audit_6253_output.txt` — output of that audit.
- `audit/boundary_round_audit.py` — finite theorem-boundary and three-state round-index sanity checks.
- `audit/boundary_round_audit_output.txt` — output of those checks.
- `PREPUBLICATION_AUDIT.md` — final internal prepublication audit status.
- `PRIOR_ART_AUDIT.md` — scoped literature-screening and claim-boundary note.
- `ZENODO_PREPRINT_FIELDS.md` — ordered metadata card for manual Zenodo preprint entry.
- `CITATION.cff` — citation metadata.
- `.zenodo.json` — Zenodo metadata for the software/source package.
- `paper.publish.json` — preprint-deposit metadata.
- `LICENSE` — MIT license for audit scripts/package utilities.
- `LICENSE_PAPER.txt` — CC BY 4.0 notice for manuscript text/PDF.
- `SHA256SUMS.txt` — integrity manifest.

## Reproduction

Compile the paper with a standard LaTeX installation:

```bash
pdflatex paper.tex
pdflatex paper.tex
```

Run the finite audits with Python 3 using only the standard library:

```bash
python audit/construction_audit_6253.py
python audit/boundary_round_audit.py
```

These computations are implementation/sanity audits, not mathematical proofs. The proof is in the manuscript.

## DOI

Paper DOI: **pending**  
Software/source-package DOI: `10.5281/zenodo.22541098`
