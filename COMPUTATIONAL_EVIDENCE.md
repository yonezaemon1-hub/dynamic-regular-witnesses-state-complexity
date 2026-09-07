# Computational evidence backfill

Status: candidate for a future manuscript version; the current published PDF is unchanged.

This paper already carried a substantial implementation audit: 3,653 quartic-witness schedules plus 2,600 cubic-witness schedules, for 6,253 complete schedules and zero failures. The backfill makes that evidence easier to reproduce and supplements it with a finite boundary table for the theorem bounds.

## Existing evidence

See `PREPUBLICATION_AUDIT.md` and the repository audit materials for the 6,253-schedule construction audit. That computation is implementation verification, not proof.

## Added finite table

Run:

```bash
python audit/computational_evidence.py
```

The script records representative lower/upper state bounds across `n` and `P`, including the stronger even-`n` cubic lower bound where applicable. It checks that the stated lower bounds never exceed the constructive upper bound over the audited grid and highlights the exact three-state threshold separately.

## Interpretation

The table is intended to show how close the witness bounds are to the upper construction at finite sizes and where the cubic even-size improvement matters. It does not turn the near-exact theorem into an exact formula outside the regimes proved in the manuscript.
