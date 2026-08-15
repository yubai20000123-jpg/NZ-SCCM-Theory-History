# NZ-SCCM Z0-Z6 — homogenized web-steel phase H0 execution

**Timestamp:** 2026-08-15 13:36 +08:00  
**Identity:** USER-DIRECTED H0 ACTIVATION AUDIT / ZERO FORMAL SPATIAL DISCRETIZATION / FAIL-FAST  
**Theory contract:** `semantic_v2/20_theory/nc_steel_shell_panel/20260815_1336__NZSCCM__HOMOGENIZED_WEB_STEEL_PHASE__THEORY_AND_ZERO_DISCRETIZATION_CONTRACT.md`

---

## 0. Purpose and boundary

The user requested execution of the continuous internal-web-as-reinforcement idea while preserving zero structural discretization and synchronizing the process/intermediate parameters to GitHub.

This H0 run answers three questions before any new `Pu` is accepted:

1. does the geometry-derived web phase recover the original web-steel material amount exactly?
2. what happens when the web phase is inserted into the already persisted current Z0-Z6 states?
3. can the new `Rq=0` equilibrium branch still be reached inside the currently validated material-compiler domain?

The run does **not** use Zhou load to choose roots or tune coefficients.

---

## 1. Frozen parent identity

```text
A0 = a/500
OUTER_STEEL = current local progressive radial-cap diagnostic
R10 = unchanged
N48-C1/MM = unchanged
CAYLEY_HAMILTON = unchanged
GENERAL_D15 = unchanged
NGUYEN_SECOND_ORDER = unchanged
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

The only H0 addition is the continuous homogenized longitudinal web-steel phase.

---

## 2. Geometry and exact material bookkeeping

All Z0-Z6 cases have

```text
ts = 4 mm
ls = 200 mm
rho_w = ts/ls = 0.020000
```

The equivalent web-steel area is

\[
A_{w,eq}=\rho_wbt_c=n_st_st_c.
\]

|case|Aw,eq mm2|remaining concrete mm2|outer-face steel mm2|old reduced Pyth MN|web-phase Pyth MN|
|---|---:|---:|---:|---:|---:|
|Z0|14640|717360|48000|39.292800|44.044944|
|Z1|11040|540960|48000|28.060800|30.319584|
|Z2|14640|717360|48000|44.332800|50.622144|
|Z3|14640|717360|48000|50.419200|54.948816|
|Z4|30720|1505280|64000|69.414400|79.386112|
|Z5|4880|239120|16000|13.097600|14.681648|
|Z6|29280|1434720|96000|78.585600|88.089888|

The web-phase `Pyth` values exactly reproduce the original full-section Zhou bookkeeping for every case. This gate is therefore **PASS**.

```text
H0_SECTION_MATERIAL_CONSERVATION = PASS
H0_WEB_STEEL_AREA_IDENTITY = PASS
```

---

## 3. Web material current map used in H0

The web phase is uniaxial in the loading direction but occupies the complete core thickness continuously:

\[
\varepsilon_y^w=\varepsilon_y(D,q;X,Y,z),
\qquad z\in[-t_c/2,t_c/2].
\]

With

\[
u=E_s\varepsilon_y^w/f_y,\qquad r=u^2,
\]

H0 uses

\[
\sigma_y^w=f_yu\alpha(r),
\quad
\alpha=1\;(r\le1),
\quad
\alpha=r^{-1/2}\;(r>1).
\]

The material function is compiled in material coordinate `r`; after composition with the continuous Nguyen field, all structural integrals are exact coefficient-space D15 moments.

Primary fixed-state H0 checkpoint:

```text
web/local-cap material r interval = [0,4]
fixed-state compiler degree = 24
material-coordinate nodes = 4001
pre-yield weight = 100
structural x/y/z points = 0
```

The later same-D equilibrium search uses a cheaper degree-10 compiler only as a branch-location diagnostic; it is not a final capacity result. Degree-16 spot checks were added for Z0 and Z4 to verify the sign and scale of the degree-10 conclusion.

---

## 4. Insertion into the previously accepted current states

At each already persisted `A0=a/500 + outer local-cap` peak state `(D_old,q_old)`, H0 replaces

\[
P_c+P_{sh}
\]

by

\[
(1-\rho_w)P_c+P_w+P_{sh}.
\]

These are **fixed-state activation values, not new equilibrated Pu values**, because the added web phase changes `Rq`.

|case|D_old|q_old|Pc,eq MN|Pw MN|Psh MN|Pfixed MN|Zhou original MN|Pfixed-Zhou|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.9821872|0.0009526833|17.69817|5.41552|18.57044|41.68413|36.94554|+12.826%|
|Z1|0.6330140|0.0014823123|11.04310|2.64711|11.92660|25.61681|23.72143|+7.990%|
|Z2|1.2428525|0.0012468869|16.21833|6.92666|23.66333|46.80831|41.21338|+13.576%|
|Z3|0.7382990|0.0011725595|25.83420|5.43799|18.68109|49.95327|44.32027|+12.710%|
|Z4|0.9952684|0.0004703293|41.10652|11.41416|24.96395|77.48464|70.18727|+10.397%|
|Z5|1.0049145|0.0001462738|6.76890|1.81700|6.27775|14.86366|14.68165|+1.240%|
|Z6|0.7050000|0.0058975999|13.05503|7.26268|24.18847|44.50618|49.67244|-10.401%|

The corresponding `Rq` residuals are large and nonzero; therefore none of these `Pfixed` values is admissible as the new ultimate load.

The important mechanism result is immediate: the web phase recovers a large part of Z6's raw load deficit at the old state, but it simultaneously drives Z0-Z4 to clear overprediction at those same states. Therefore the web phase cannot be accepted on section-strength reasoning alone; the new equilibrium path must be solved.

---

## 5. Same-D `Rq=0` branch relocation diagnostic

To determine the direction and magnitude of branch movement before a full two-variable limit search, `q` was re-equilibrated at each old peak `D` using exact generalized-coordinate residual evaluations. No spatial grid is introduced.

The degree-10 values below are **branch-locator diagnostics**, not new Pu values:

|case|D fixed|old q|new q at Rq≈0|q shift|P at same-D equilibrium MN|Zhou original MN|same-D error|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.9821872|0.0009526833|0.0011468507|+20.38%|40.95234|36.94554|+10.845%|
|Z1|0.6330140|0.0014823123|0.0017721507|+19.55%|24.87771|23.72143|+4.874%|
|Z2|1.2428525|0.0012468869|0.0017724895|+42.15%|44.93681|41.21338|+9.035%|
|Z3|0.7382990|0.0011725595|0.0013209693|+12.66%|49.49642|44.32027|+11.679%|
|Z4|0.9952684|0.0004703293|0.0005139217|+9.27%|77.29708|70.18727|+10.130%|
|Z5|1.0049145|0.0001462738|0.0001494408|+2.17%|14.96329|14.68165|+1.918%|

Residual magnitudes at these located roots are small relative to structural residual scales (from single digits to about `2.5e3 N mm` in this deliberately low-degree locator).

Degree-16 spot checks confirm that the conclusion is not a degree-10 sign artifact:

```text
Z0, D=0.9821872:
  degree10 P = 40.95234 MN
  degree16 P = 40.80059 MN
  both remain > Zhou by about 10%

Z4, D=0.9952684:
  degree10 P = 77.29708 MN
  degree16 P = 77.02945 MN
  both remain > Zhou by about 9.7-10.1%
```

Thus the web phase materially shifts the equilibrium branch rather than merely adding an axial-force offset.

---

## 6. Z6 fail gate

Z6 behaves differently and prevents promotion of H0 into a full Z0-Z6 Pu recalculation under the currently frozen compiler domain.

At `D=0.705`, the old current state has `q≈0.00590`. With the web phase activated, the residual remains strongly negative through the last evaluated admissible neighborhood:

```text
q = 0.005 : Rq ≈ -2.5164e9 N mm
q = 0.006 : Rq ≈ -1.5459e9 N mm
```

The next attempted continuation toward `q=0.008` drives the current concrete N48 representation outside its validated Z6 compiler interval `[-1.15,0.23]`; direct polynomial extrapolation becomes catastrophic and is rejected as invalid.

No extrapolated load is retained.

Therefore H0 stops here under the project's fail-fast rule:

```text
Z6_WEB_PHASE_RQ_ROOT_INSIDE_CURRENT_COMPILER_DOMAIN = NOT FOUND
N48_EXTRAPOLATION = REJECTED
SILENT_COMPILER_WIDENING = NOT PERFORMED
FULL_Z0_Z6_WEB_PHASE_Pu_RECALCULATION = NOT COMPLETE
```

This is a genuine new cause introduced by the web-phase extension, not a reuse of the old strict-certificate issue.

---

## 7. Current engineering interpretation

The H0 result is mixed:

1. **Material accounting is excellent.** The continuous web phase restores the original web-steel area and exact section-strength bookkeeping without any physical discretization.
2. **It is not a harmless correction.** The web phase changes `Rq` strongly and pushes the equilibrium `q` upward by about 2%-42% in Z0-Z5 at the old `D` values.
3. **Z0-Z4 tend to become too strong**, already by roughly 5%-12% at the same-D equilibrium diagnostic.
4. **Z5 remains close**, consistent with the earlier finding that its raw gap was mostly section representation.
5. **Z6 improves in raw load at the old state**, but its new equilibrium branch moves toward larger finite amplitude and leaves the currently validated concrete compiler domain before an accepted same-D root is recovered.

Therefore it would be incorrect to simply declare `internal webs -> full homogenized reinforcement` as the new production model.

---

## 8. Gate decision and next task

```text
HOMOGENIZED_WEB_STEEL_CONCEPT = MECHANICALLY FEASIBLE / ANALYTICALLY COMPATIBLE
ZERO_STRUCTURAL_DISCRETIZATION = PASS
SECTION_MATERIAL_CONSERVATION = PASS
DIRECT_PRODUCTION_PROMOTION = NO
Z0_Z5_BRANCH_RELOCATION = CONFIRMED
Z6_CURRENT_COMPILER_DOMAIN = BLOCKING GATE
```

The next executable task is narrowly defined:

```text
CURRENT_NEXT_TASK = WEB_PHASE_Z6_MATERIAL_DOMAIN_PREFLIGHT
```

It must determine, from analytic strain/invariant bounds rather than spatial sampling, the material-coordinate interval required by the connected Z6 web-phase branch. Only if a source-consistent N48-C1/MM compilation covers that interval with acceptable material-function error may the full `Rq=0 -> L=0 -> KZ` Z0-Z6 recalculation continue.

No R10 parameter, web fraction, steel strength, imperfection, or Zhou value may be fitted in that step.
