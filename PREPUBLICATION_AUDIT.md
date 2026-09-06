# Paper 7 Final Prepublication Audit — v1.0.0

Date: 2026-09-06  
Author: Ryutaro Yonezu (Independent Researcher)  
Peer review: none

## Verdict

`PASS_INTERNAL_PREPUBLICATION_AUDIT_CANDIDATE_NOT_PEER_REVIEWED`

This is an internal proof/implementation/publication audit, not peer review and not a novelty certification.

## Frozen claims

1. For every `n >= 15`, `P >= 1`:
   `S_n(n,P) >= 2 + ceil((n-13)/P)`.
2. For even `n >= 12`, `P >= 1`:
   `S_n(n,P) >= 2 + ceil((n-10)/P)`.
3. For every `n >= 4`, `P >= 1`:
   `S_n(n,P) = 3 iff P >= n-1`.
4. Existing block-counter upper bound retained:
   `S_n(n,P) <= 2 + ceil((n-1)/P)`.

Not claimed: the full exact formula for arbitrary state budgets.

## Line-by-line dependency audit

Regular-witness chain rechecked:

1. dynamic causal-cone locality;
2. regular homogeneous invariance;
3. regular two-orbit phase packing;
4. quartic protected block;
5. cubic protected block;
6. quartic complement completion;
7. cubic complement completion;
8. quartic slow-cone schedule;
9. cubic slow-cone schedule;
10. waiting-sum contradictions;
11. conversion to persistent-state lower bounds.

Three-state chain rechecked:

1. minimum-three-state necessity and three-state normal form;
2. path symmetry before first final-one event;
3. first final-one event occurs by time `P`;
4. endpoint-first exclusion;
5. interior-first exclusion for `T < n-2`;
6. critical boundary `T=P=n-2`;
7. forced maximal-speed zero wave;
8. `F0`/live broadcast separation at every phase;
9. later endpoint termination implies `F1`/live separation at one phase;
10. binary alphabet forces `F0` and `F1` broadcasts to collide at that phase;
11. single-zero placement at distance `psi+1` gives the final contradiction.

## Clarifications introduced during final audit

No theorem statement was changed. The final source explicitly clarifies:

- target selection and the `t_b=0` horizon case in both slow-cone propositions;
- distinct first-expansion connectors chosen outside protected sets;
- an explicit half-pairing construction for the cubic matching steps;
- the universal lower bound of three persistent states used in the exact-threshold theorem.

## Finite construction audit

`audit/construction_audit_6253.py` independently instantiates the finite schedule range reported in the manuscript and recomputes graph and causal-cone invariants.

Result:

```text
VERDICT=PASS_CONSTRUCTION_AUDIT_NOT_A_PROOF
QUARTIC_CASES=3653
CUBIC_CASES=2600
TOTAL_CASES=6253
FAILURES=0
```

For each case it checks simple connected exact regularity, recomputes each backward causal cone, and checks time-zero cone disjointness.

## Boundary and round-index audit

`audit/boundary_round_audit.py` checks representative formula boundaries for `n=4..30` and the critical three-state round-index arithmetic for `n=4..100`.

Result:

```text
VERDICT=PASS_BOUNDARY_ROUND_SANITY_NOT_A_PROOF
BOUNDARY_ROWS=161
ROUND_INDEX_CASES=9603
FAILURES=0
```

## LaTeX / PDF audit

Final v1.0.0 build:

- two-pass `pdflatex -halt-on-error`: PASS;
- pages: 13;
- Warning / Overfull / Underfull / Undefined matches in final second-pass log: 0;
- embedded fonts: PASS;
- PDF opens and renders: PASS;
- visual all-page contact-sheet inspection: PASS;
- v0.6-final to v1.0.0 render diff: only page 1 changed, corresponding to the version-label change; pages 2-13 were pixel-identical at the audit render DPI.

Final SHA256:

- `paper.tex`: `b480ec2ed4b0981b33bd89f09399809fa2dd6c348616e0bd9854da6fd2728189`
- authoritative PDF: `64986616cf206678b908f3ad6f19d927b0a158b2fcc27da5f19cc4af25e0b488`

## Prior-art audit

A final targeted literature search was rerun on September 6, 2026. No direct theorem matching the near-exact `n-O(1)` known-size state lower bound or the exact three-state periodic-phase threshold in the stated model was identified. See `PRIOR_ART_AUDIT.md`.

This remains scoped literature screening, not a novelty certification.
