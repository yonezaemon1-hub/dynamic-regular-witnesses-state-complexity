# Witness audit tables

- `construction_audit_summary.csv` — 3,653 quartic + 2,600 cubic complete schedules; 6,253 total; zero failures.
- `dynamic_regular_finite_selected.csv` — representative formal lower/upper state bounds over `n` and `P`.
- `../audit/construction_audit_6253.py` — original complete schedule audit.
- `../audit/boundary_round_audit.py` — original theorem-boundary audit.
- `../audit/computational_evidence.py` — wider finite-grid table generator.

The finite table reports the interval honestly; it does not turn the near-exact theorem into an exact formula outside the proven threshold regime.
