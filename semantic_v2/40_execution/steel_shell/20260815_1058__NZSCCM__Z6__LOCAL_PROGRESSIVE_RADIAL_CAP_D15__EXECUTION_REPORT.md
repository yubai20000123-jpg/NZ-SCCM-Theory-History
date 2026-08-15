# NZ-SCCM Z6 — local progressive radial-cap / exact-D15 execution

**Timestamp:** 2026-08-15 10:58 +08:00  
**Identity:** CURRENT Z6-C EXECUTION / ZERO FORMAL SPATIAL QUADRATURE / DIAGNOSTIC CURRENT-MAP, NOT FULL INCREMENTAL FLOW PLASTICITY  
**Parent preflight:** `20260815_0126__NZSCCM__Z6__LOCAL_IDEAL_EP_PROGRESSIVE_YIELD__PREFLIGHT_AUDIT.md`

---

## 0. Purpose

The preflight hypothesis was that the reduced whole-shell strength cap might turn first local yield into an artificially global loss of steel-shell resultant/tangent and therefore create the Z6 yield-cusp too early. This execution replaces the single global cap by a **local current-state radial cap field** and recompiles that field into finite analytic coefficient space, while retaining the frozen concrete operator, Nguyen kinematics and exact D15 structural moments.

The question is deliberately narrow:

> If yield is allowed to spread locally instead of scaling the entire shell from the first yielded point, how much of the Z6 `-23.422%` discrepancy is actually recovered?

No Z1/Z3/Z4/Z5 recomputation is performed.

---

## 1. Frozen structural identity

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = FROZEN
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_TUNING = NO
```

Z6 geometry/material remains

```text
a = 9000 mm
b = 12000 mm
ell = 9000 mm
h = 130 mm
tc = 122 mm
ts_each_face = 4 mm
Es = 206000 MPa
fy = 355 MPa
fcu = 40 MPa
fc' = 30.4 MPa
```

The formal batch imperfection remains `q0=1/400=0.0025` for the primary isolation result. A separate `a/500` comparator-identity sensitivity is retained only as a sensitivity, not promoted into the production input.

---

## 2. Local steel current-map diagnostic

The elastic plane-stress shell field is generated continuously from the same Nguyen strain field. Define

\[
r(X,Y,z;D,q)=\frac{[\sigma_{VM}^{E}(X,Y,z;D,q)]^2}{f_y^2}.
\]

Instead of the old whole-shell scalar

\[
\alpha_g=\min\left(1,\frac{f_y}{\max_\Omega \sigma_{VM}^{E}}\right),
\]

the present diagnostic uses the local current scale

\[
\boxed{\alpha_{loc}(r)=\begin{cases}
1,&r\le1,\\
r^{-1/2},&r>1,
\end{cases}}
\]

and

\[
\boxed{\boldsymbol\sigma_s^{loc}(X,Y,z)=\alpha_{loc}(r)\,\boldsymbol\sigma_s^E(X,Y,z).}
\]

Thus first yield starts at the most highly stressed location while the remaining shell remains essentially elastic; the yielded region expands continuously as the elastic trial invariant exceeds `fy` elsewhere.

### Identity boundary

This is a **path-independent local radial-return/current-map diagnostic**. It is deliberately closer to local ideal-EP spreading than the homogeneous whole-shell cap, but it is not relabelled as a fully incremental J2 flow-history solver. Therefore its purpose is root-cause isolation, not immediate production promotion.

---

## 3. Zero-spatial-quadrature analytic compilation

For each outer faceplate, the elastic in-plane strains are finite polynomials in

\[
x=\sin X,\qquad y=\sin Y,\qquad \eta\in[-1,1],
\]

with physical shell coordinate

\[
z=z_c+\frac{t_s}{2}\eta.
\]

Consequently

\[
\sigma_x^E,\sigma_y^E,[\sigma_{VM}^E]^2,
\quad
(\boldsymbol\sigma_s^E)^T\boldsymbol\varepsilon_{,q}
\]

are finite polynomial/trigonometric-thickness fields.

The scalar `alpha_loc(r)` is compiled **only in material coordinate `r`**, then composed with the analytic `r(X,Y,eta)` field. The resulting finite coefficient field is contracted by general-D15 exact moments. No structural point grid, Gauss rule, Simpson rule, adaptive cell or material-point mesh enters the formal operator.

Diagnostic compiler used:

```text
r-domain = [0, 6.25]  # covers elastic-trial sigma_VM/fy up to 2.5
Chebyshev degree checks = 24, 32, 40, 48, 56
pre-yield weighting = 100 in material-coordinate least-squares fit
formal structural quadrature = 0
```

At the original first-yield state, the degree-32 compiler reproduces the elastic shell axial resultant to about `3.2e-4 %` and the shell q-work resultant to about `1.7e-2 %`. Degree escalation changes final reported loads only at the `~0.01–0.03 MN` level, far below the Z6 discrepancy.

---

## 4. Formal q0=1/400 branch: yield cusp disappears, but only slightly

Original reduced whole-shell-cap Z6 state:

```text
D = 0.663425
q = 0.0054394
Pc = 11.9026733 MN
Ps = 22.3585766 MN
Pu = 34.2612499 MN
control = first-yield cusp
error vs Zhou = -23.422 %
```

With the local progressive radial-cap field, the equilibrium branch continues past first yield:

|D|q|P (MN)|interpretation|
|---:|---:|---:|---|
|0.6640|0.00544582|34.26743|post-yield equilibrium retained|
|0.6650|0.00545700|34.27816|still rising|
|0.6670|0.00547944|34.29992|still rising|
|0.6700|0.00551338|34.33322|still rising|
|0.6800|~0.0056288|~34.45|still rising|
|0.6920|0.00578973|34.59460|near terminal fold|
|0.6922|~0.005802|34.59458|Rq approximately zero; Rq(q) near its local maximum|

At `D=0.693`, the maximum of the local-cap `Rq(D,q)` neighborhood is already negative (about `-13.5 MN mm` at `q≈0.00580`), so the connected equilibrium branch no longer has a nearby root. The branch therefore terminates in a **q-equilibrium fold** between approximately `D=0.6922` and `0.6930`, not at first steel yield.

Engineering localization:

\[
\boxed{D_{fold}\approx0.6922},
\qquad
\boxed{q_{fold}\approx0.00580},
\]

\[
\boxed{P_{Z6,loc}\approx34.59\ \mathrm{MN}}.
\]

At the degree-32 checkpoint `D=0.6922, q=0.005802`:

```text
Pc = 11.46087 MN
Ps,loc = 23.13371 MN
P = 34.59458 MN
Rq = +0.066 MN mm
sigma_VM,max^E / fy ~= 1.0506
```

Degree 24–56 at this same state gives `P≈34.5932–34.5949 MN`; hence the load conclusion is insensitive to the local material-compiler degree at engineering scale.

Relative to the old whole-shell-cap value:

\[
\Delta P_{local-global}\approx+0.333\ \mathrm{MN},
\]

which is only about `0.97%` of the old Z6 load and explains only about

\[
\boxed{3.2\%}
\]

of the original `10.479 MN` gap to Zhou.

The remaining error is still approximately

\[
\boxed{-22.68\%}.
\]

Therefore:

```text
FIRST_LOCAL_YIELD_AS_GLOBAL_CUSP = CONFIRMED ARTIFACT
WHOLE_SHELL_CAP_AS_PRIMARY_23P4_PERCENT_ERROR_CAUSE = NOT SUPPORTED
```

---

## 5. a/500 comparator-imperfection sensitivity + local spreading

The earlier comparator-identity sensitivity used

```text
A0 = a/500 = 18 mm
q0 = A0/b = 0.0015
```

without promoting it to the production input. Under the old whole-shell cap this gave approximately

\[
P=37.3777\ \mathrm{MN}.
\]

The same local progressive radial-cap diagnostic gives the connected branch

|D|q|P (MN)|
|---:|---:|---:|
|0.680|0.00557366|37.44887|
|0.700|0.00583137|37.50667|
|0.705|0.00589760|37.50943 (degree 32)|
|0.710|0.00596545|37.50695|
|0.720|0.00611150|37.48171|

A local quadratic localization around `D=0.700–0.710` gives a degree-32 peak near

\[
D\approx0.7051,\qquad P\approx37.5094\ \mathrm{MN}.
\]

Higher material-compiler degree shifts the same neighborhood slightly downward; degree 56 gives about `37.488 MN` after q-equilibrium correction at `D=0.705`. The defensible engineering range is therefore

\[
\boxed{P_{a/500,loc}\approx37.49\text{–}37.51\ \mathrm{MN}}.
\]

This remains approximately `-16.2%` below the Zhou comparator. Relative to the old `a/500 + whole-shell-cap` sensitivity, local progressive spreading adds only about `0.11–0.13 MN`.

Thus the earlier conclusion is strengthened:

1. the imperfection-normalization identity can explain a significant part of the original gap;
2. local progressive steel yielding removes the artificial yield cusp but recovers very little additional capacity;
3. neither item closes Z6.

---

## 6. Root-cause decision after execution

```text
Z6_A_IMPERFECTION_IDENTITY = SIGNIFICANT PARTIAL CAUSE
Z6_B_N48_COMPILER_WIDTH = MINOR / NOT DOMINANT
Z6_C_WHOLE_SHELL_GLOBAL_CAP = CREATES ARTIFICIAL YIELD CUSP
Z6_C_LOCAL_PROGRESSIVE_SPREADING_CAPACITY_RECOVERY = SMALL
Z6_C_AS_PRIMARY_REMAINING_CAUSE = DOWNGRADED
FULL_INCREMENTAL_LOCAL_J2_EP = NOT CLAIMED CLOSED
R10_CHANGE = NOT JUSTIFIED
N48_ORDER_CHANGE = NOT JUSTIFIED
RERUN_Z1_Z3_Z4_Z5 = NOT JUSTIFIED
```

The current data do **not** support a steel-hardening fix, a Z6 load factor, a concrete refit, or further compiler expansion as the next move.

---

## 7. New highest-priority unresolved item

The next diagnostic must move to the Z6 geometry/comparator/stability identity:

```text
NEXT = Z6-D
1. re-audit same-object Zhou comparator construction at the extreme lambda/slenderness end;
2. re-audit design-side minimum-energy halfwave for the reduced object;
3. check whether the reduced removal of internal webs preserves the support/stiffness identity implicit in Zhou's source comparator;
4. establish same-branch KZ ordering for the locally capped Z6 branch;
5. do not use observed FE/test mode shape to tune ell.
```

The specific reason is quantitative: after correcting the first-yield globalization artifact, the formal-q0 branch is still about `22.7%` low, while the source-equivalent imperfection sensitivity remains about `16.2%` low. The dominant unresolved discrepancy therefore lies outside the tested compiler/whole-shell-cap mechanisms.
