# NZ-SCCM Case21 V2 second blank-chat reproduction — status snapshot

**Date:** 2026-08-12  
**Evidence identity:** latest user-visible independent reproduction result; supersedes the earlier first blank-chat `BLOCKED_AT_R10` as the current Case21 reproducibility status.

## Current independent layer status

```text
R10 = PASS
N48-C1 = PASS
T-minimax = PASS
Cayley-Hamilton = PASS
KINEMATICS = PASS
D15 = PASS
STEEL = PASS
Rq = PASS as equation / equilibrium-branch balance
SPECTRAL-CERTIFICATE = PASS

OVERALL = BLOCKED
FIRST_SUBSTANTIVE_DIVERGENCE = L
```

The independent run produced a positive-branch limit candidate approximately

\[
D\approx0.834734841190971,
\]

\[
q\approx0.00186261154469431,
\]

\[
P\approx365.101993832409\ \mathrm{kN}.
\]

These values are **not** frozen as unique production \(D_u,q_u,P_u\). Their current identity is

```text
UNRESOLVED_LIMIT_ROOT_CANDIDATE
```

because the V2 contract did not yet uniquely define:

- admissible \((D,q)\) domain;
- primary equilibrium branch;
- unique root-selection rule among multiple real joint roots;
- production tolerances for \(R_q\) and \(L\);
- a unique definition of \(L_{norm}\).

This gap is addressed separately by `current/governance/NZ_SCCM_NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT_V1_20260812.md`.

No experimental load should be used to upgrade this candidate to a production root.
