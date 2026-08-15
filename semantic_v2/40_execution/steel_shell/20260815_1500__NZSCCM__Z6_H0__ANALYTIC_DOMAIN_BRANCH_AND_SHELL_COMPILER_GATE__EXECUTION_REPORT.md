# NZ-SCCM Z6 H0 — analytic-domain branch continuation and shell-compiler gate

**Timestamp:** 2026-08-15 15:00 +08:00  
**Status:** CONCRETE DOMAIN PREFLIGHT PASS / H0 BRANCH PARTIALLY RECOVERED / NEW SHELL COEFFICIENT GATE / FULL KZ NOT RELEASED

## 0. Objective

The previous Stage-A audit showed that H0 already reproduces Zhou's longitudinal elastic rigidity exactly and that the old Z6 state has not suffered a wholesale steel tangent collapse. The next required task was therefore:

```text
1. determine the larger-q concrete material-coordinate domain analytically;
2. recompile the same frozen R10/N48 degree over the justified domain;
3. recover the connected H0 Rq=0 branch;
4. proceed toward full directional KZ and L only while every analytic compiler remains admissible.
```

No structural spatial grid, numerical quadrature, load calibration, R10 refit, observed-mode fitting or experiment-driven root selection is used.

## 1. Analytic domain preflight — PASS

For Z6, `k=b/ell=4/3`, `nu=0.18`, `q0=0.0015`, and

\[
M=\frac{\pi^2}{\varepsilon_0}(q_0q+q^2/2),
\qquad
B=\frac{\pi^2t_c}{2\varepsilon_0b}q.
\]

The branch material-coordinate envelope is reduced analytically to

\[
\lambda_{min}=-D-\frac{\nu+k^2}{1-\nu^2}B,
\]

and, for the active larger-q branch where

\[
x_*=\frac{(1+\nu k^2)B}{2M}\le1,
\]

\[
\lambda_{max}=
\frac{M+(1+\nu k^2)^2B^2/(4M)}{1-\nu^2}.
\]

At `D=0.705`:

```text
q=0.006 -> lambda=[-1.03049,+0.22898]
q=0.008 -> lambda=[-1.13898,+0.32909]
```

Thus the old interval `[-1.15,0.23]` fails on the positive side as H0 drives q upward. This explains why the prior q=0.008 polynomial extrapolation was invalid without implying that the R10 material law itself is wrong.

The minimal interval `[-1.15,0.30]` covers the recovered same-D equilibrium. A unified diagnostic interval `[-1.30,0.40]` covers approximately `D<=0.80,q<=0.009`.

```text
CONCRETE_ANALYTIC_DOMAIN_PREFLIGHT = PASS
OLD_INTERVAL_EXTRAPOLATION = REJECTED
R10 = UNCHANGED
N48 DEGREE = 48 UNCHANGED
```

## 2. Scalar N48 compiler consequence

The wider domain increases the finite-degree scalar approximation error. Representative checks are persisted in the companion JSON.

For `[-1.15,0.30]`:

```text
U max error  ~= 0.00944
C max error  ~= 0.02250
T max error  ~= 0.18210
T7 max error ~= 0.26652
T minimax    ~= 0.18052
```

For the wider exploratory `[-1.30,0.40]`:

```text
U max error  ~= 0.01949
C max error  ~= 0.02784
T max error  ~= 0.25442
T7 max error ~= 0.25447
T minimax    ~= 0.25153
```

This is sufficient for the present engineering branch-location audit under the project's relaxed strict-remainder priority, but it is not promoted as a new high-precision material theorem certificate.

## 3. Old H0 state independently reproduced

Before continuing, the q0-parameterized concrete kernel and H0 web/shell resultants reproduced the persisted Z6 old state:

```text
D = 0.705
q = 0.0058975999
Pc(full concrete) = 13.32145962 MN
Pc,eq = 0.98 Pc = 13.05503043 MN
Pw = 7.26267911 MN
Psh = 24.18847467 MN
P = 44.50618420 MN
Rq = -1.65814501e9 N mm
```

This confirms that the continuation uses the same H0 object rather than a new load model.

## 4. Same-D H0 equilibrium is recovered after justified domain coverage

### 4.1 Minimal interval `[-1.15,0.30]`

At `D=0.705`:

```text
q=0.0073400:
  P = 40.24905651 MN
  Rq = -1.0313981e7 N mm

q=0.0073573:
  P = 40.20446690 MN
  Rq = +1.2728846e7 N mm
```

The connected root is therefore near

\[
\boxed{q\approx0.007348},
\qquad
\boxed{P\approx40.23\ \mathrm{MN}}.
\]

At the root neighborhood the analytic material coordinate is approximately

```text
lambda_min = -1.10360
lambda_max = +0.29436
x* = 0.64845
```

so the minimal interval covers it without extrapolation.

### 4.2 Unified interval `[-1.30,0.40]`

At the same `D=0.705`:

```text
q=0.0073500:
  P = 40.40091624 MN
  Rq = -8.0327118e6 N mm

q=0.0073595:
  P = 40.37085952 MN
  Rq = +4.4360984e6 N mm
```

giving the branch locator

```text
q ~= 0.0073561
P ~= 40.38 MN
```

The approximately `0.15 MN` difference between the minimal and unified interval locations is small relative to the remaining Z6 discrepancy. Thus domain widening removes the extrapolation block but does not recover the missing several MN.

## 5. Connected branch continuation

Using the unified interval only as an engineering continuation compiler, the same H0 `Rq=0` branch was followed to larger D. Representative root neighborhoods are persisted in the CSV.

Approximate connected states are:

|D|q on Rq=0|P (MN)|
|---:|---:|---:|
|0.650|0.00645|39.56|
|0.705|0.007356|40.38|
|0.720|0.007616|40.45|
|0.730|~0.00779|~40.53|
|0.740|0.007904|40.84|
|0.760|0.007995|41.72|
|0.780|0.008153|42.26|

The important physical observation is that the H0 branch remains deeply finite-amplitude and is still rising through approximately `D=0.78`, yet its load remains far below the Zhou lower-envelope value `49.6724 MN`.

These are branch-locator states, not final `Pu`, not strict `Rq,L` roots, and not a KZ event.

## 6. A new fail-fast gate appears before full KZ

The concrete material coordinate is still admissible when the branch approaches `D≈0.80`. For example:

```text
D=0.80, q=0.009:
  lambda_min=-1.28823
  lambda_max=+0.38639
```

which remains inside `[-1.30,0.40]`.

The outer-shell radial-cap material coordinate also remains physically inside its existing `[0,4]` interval; trial `sigma_VM/fy` is only about `1.30–1.34` near the problematic region.

Nevertheless, the coefficient-space composition of the shell radial-cap current map becomes ill-conditioned. At `D=0.80,q=0.0081`:

```text
degree 10: Psh=25.4701 MN, Rq_sh=+0.7582e9 N mm
degree 16: Psh=25.2803 MN, Rq_sh=+0.6130e9 N mm
degree 20: Psh=25.1672 MN, Rq_sh=+0.5372e9 N mm
degree 24: Psh=25.2695 MN, Rq_sh=-1.0490e9 N mm
```

At `q=0.009` the breakdown becomes unmistakable:

```text
deg 16: Psh=24.0507 MN, Rq_sh=+1.8560e9
deg 18: Psh=23.9975 MN, Rq_sh=+1.8221e9
deg 20: Psh=23.8492 MN, Rq_sh=+0.2588e9
deg 22: Psh=20.6016 MN, Rq_sh=+73.113e9
deg 24: Psh=-159.807 MN, Rq_sh=+205.024e9
```

The degree-24 value is physically impossible and is rejected. The detailed degree table is persisted separately.

This failure is not evidence of physical shell softening. It is a coefficient-space analytic-composition conditioning failure.

## 7. Why no full KZ number is released

The requested next theoretical quantity is

\[
K_Z=K_{Z,c}^{mat}+K_{Z,w}^{mat}+K_{Z,sh}^{mat}+K_Z^{geo},
\]

together with `L` and the ordering of first yield, `KZ=0`, and the load maximum/fold.

That calculation requires a valid current stress and full directional tangent at every connected branch state. Once the shell current-map coefficient composition becomes ill-conditioned, continuing the branch or evaluating `b_phi^T C_t b_phi` would turn a numerical representation error into a fake physical stability result.

Therefore:

```text
CONNECTED_H0_Rq_BRANCH = PARTIALLY RECOVERED THROUGH D≈0.78
CONCRETE_DOMAIN_GATE = PASS
SHELL_RADIAL_CAP_SCALAR_R_DOMAIN = PASS
SHELL_RADIAL_CAP_COEFFICIENT_COMPOSITION = FAIL AT DEEP q
FULL_KZ = NOT RELEASED
L_EVENT = NOT RELEASED
FINAL_H0_Pu = NOT RELEASED
```

No silent switch to degree 16/18 is authorized. Those values are useful only because they diagnose where degree-24 coefficient composition stops being trustworthy.

## 8. Updated causal meaning

The earlier N48 interval exhaustion was a real computational blocker, but resolving it does **not** restore Z6 to the Zhou lower band. The connected H0 branch stays around `40–42 MN` through the recovered range.

This reinforces the Stage-A conclusion that Z6 is governed by a deep nonlinear equilibrium/stability path rather than a missing small-amplitude elastic rigidity. However the new shell compiler failure occurs before the full directional KZ decomposition can separate concrete tangent degradation, current-stress geometric stiffness, and shell/web contributions quantitatively.

The coefficient failure itself is not a physical cause of Z6; it is the next representation gate.

## 9. Next task

```text
CURRENT_NEXT_TASK = Z6_H0_SHELL_RADIAL_CAP_ANALYTIC_COMPILER_STABILIZATION_THEN_FULL_KZ
```

Required sequence:

1. preserve the exact same scalar `alpha_loc(r)` target;
2. stabilize its finite analytic coefficient composition without structural sampling/quadrature;
3. prove shell force and q-work convergence across the required H0 branch domain;
4. continue the connected `Rq=0` branch;
5. form the full directional concrete/web/shell current tangents;
6. evaluate exact-D15 `KZ` components and `L`;
7. establish event ordering and only then judge the remaining Z6 physical mechanism.

No empirical Z6 correction, Zhou/Winter calibration, observed-mode fit or R10 change is authorized.
