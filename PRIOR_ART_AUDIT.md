# Scoped Prior-Art Audit

Date: September 6, 2026  
Status: targeted literature screening; **not a certification of novelty**.

## Direct predecessor

Ryutaro Yonezu, *Two-Orbit Packing for Exact State Complexity of Explicit Binary Consensus in Anonymous Dynamic Networks with Periodic Time*, Zenodo preprint v1.0.0, September 6, 2026. DOI: `10.5281/zenodo.22538052`.

That paper proves the exact known-diameter formula and the known-size lower bound
`2 + ceil(floor(n/2)/P)`. The present work addresses the residual known-size gap.

## Nearby work checked

- G. Parzych and J. J. Daymude, *Memory Lower Bounds and Impossibility Results for Anonymous Dynamic Broadcast*, Distributed Computing 39(3), Art. 18 (2026), DOI `10.1007/s00446-026-00511-4`. Nearby termination-memory lower bounds; different broadcast task/start semantics and no free periodic-phase state threshold.
- T. Blanc, G. A. Di Luna, and G. Viglietta, *Computing in Anonymous Dynamic Networks with One-Bit Communications*, arXiv:2607.08358 (2026). Same severe one-bit aggregate interface; different general-computation / round-complexity objective.
- G. A. Di Luna and G. Viglietta, *Universal Finite-State and Self-Stabilizing Computation in Anonymous Dynamic Networks*, OPODIS 2024 / later journal version. Finite-state and self-stabilizing general computation; different exact persistent-state / periodic-phase termination question.
- V. Turau, *Broadcasts in Anonymous, Dynamic Networks: A New Algorithm and Impossibility Results*, SAND 2026, DOI `10.4230/LIPIcs.SAND.2026.6`. Randomized broadcast and stabilizing termination; different task, randomization, and objective.
- L. Penet de Monterno, B. Charron-Bost, and S. Merz, *Synchronization modulo P in Dynamic Networks*, Theoretical Computer Science 942 (2023). Computes/synchronizes a modulo clock rather than treating a common phase as a free resource.
- B. Charron-Bost and L. Penet de Monterno, *Self-Stabilizing Clock Synchronization in Dynamic Networks*, OPODIS 2022, DOI `10.4230/LIPIcs.OPODIS.2022.28`.

A final targeted search on September 6, 2026 using combinations of the exact model terms, `state complexity`, `periodic phase/time`, `three-state threshold`, `regular dynamic graphs`, and the numerical forms `n-13` / `P>=n-1` did not identify a prior theorem giving either the paper's `n-O(1)` known-size lower numerator or its exact three-state threshold in the stated model.

## Narrow claim boundary

The paper does **not** claim novelty for:

- finite-state pumping;
- deterministic trajectory packing in general;
- causal-cone locality;
- regular graph constructions;
- monotone flooding;
- periodic clocks;
- generic clock-memory or time-space tradeoffs.

The scoped residual contribution is the task-specific use of regular dynamic witnesses to force a near-linear waiting sum for known-size explicitly terminating binary consensus under the stated one-bit periodic-phase model, plus the exact three-state phase threshold.
