# Z6 higher-harmonic release diagnostic — governance lock

**Timestamp:** 2026-08-15 16:47 +08:00

This lock changes no production material or kinematic law. It only authorizes a zero-spatial diagnostic extension of the current single-harmonic displacement subspace.

Frozen:

```text
R10 = UNCHANGED
N48-C1/MM = UNCHANGED
CAYLEY_HAMILTON = UNCHANGED
GENERAL_D15 = UNCHANGED
NGUYEN_SECOND_ORDER = UNCHANGED
A0 = a/500
OUTER_SHELL_CURRENT_MAP = current local progressive radial-cap diagnostic
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
ZHOU/WINTER_LOAD_USED_FOR_ROOT_SELECTION = NO
```

Diagnostic modal extension on the same complete continuous domain:

\[
w/b=q_{11}\sin X\sin Y+q_{31}\sin X\sin 3Y+q_{13}\sin 3X\sin Y.
\]

Here `q31` means the third longitudinal harmonic (`m=3,n=1`), and `q13` the third transverse harmonic (`m=1,n=3`). Initial imperfection remains only in the source first mode, `q0=a/(500b)`.

The first gate is the exact first variation at the already accepted single-mode state:

```text
Rq11 ~= 0 must reproduce the current branch equilibrium;
Rq31 and Rq13 are then evaluated with no change to the current material state.
```

A nonzero `Rq31` or `Rq13` proves that the current single-q state is not stationary in the enlarged modal subspace. It does **not** by itself provide a two-mode ultimate load.

Production multimode theory is not created by this diagnostic. A finite-q31 capacity may be released only after coefficient-space evaluation is stable and the coupled equations are solved without comparator calibration.
