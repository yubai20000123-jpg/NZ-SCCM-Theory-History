# NZ-SCCM — Z1/Z4 direct Yun-Lu event-ordering execution after Z6 zero-spatial lock

**Timestamp:** 2026-08-18 14:01 +08:00  
**Identity:** DIRECT EXECUTION / SOURCE-BASED MECHANISM CHECK / NO NEW Pu FABRICATION  
**Formal structural integration:** zero spatial quadrature retained

## 0. Purpose

The immediate question is whether the already-established Yun-Lu large-deflection steel-wall theory can be used directly to replace the unresolved steel-shell post-yield tangent treatment for the current Z1/Z4 recalculation.

This execution does not introduce another material theory. It evaluates the existing Yun-Lu local branch on the actual Zhou Table-5.1 local steel-panel dimensions already used by Z1/Z4.

Formal counters retained:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 1. Z1/Z4 current source geometry used for the local Yun check

From the persisted Zhou Table-5.1 representative source table:

```text
Z1:
  ns = 30
  local steel-panel spacing ls = 200 mm
  a = 6000 mm
  b = 6000 mm
  h = 100 mm
  tc = 92 mm
  ts = 4 mm
  fy = 235 MPa

Z4:
  ns = 40
  local steel-panel spacing ls = 200 mm
  a = 6000 mm
  b = 8000 mm
  h = 200 mm
  tc = 192 mm
  ts = 4 mm
  fy = 355 MPa
```

Common steel constants retained from the current Z-series execution:

```text
Es = 206000 MPa
nu_s = 0.30
```

For both cases, the local steel subpanel width entering the direct Yun-Lu wall-panel check is

\[
B_s=l_s=200\ \mathrm{mm}.
\]

The longitudinal theoretical wave count for the source geometry is selected by the Yun energy-minimum condition. With \(a/B_s=30\), take

\[
m=30,
\qquad
\ell=a/m=200\ \mathrm{mm},
\qquad
r=\ell/B_s=1.
\]

No observed bulge count or comparator load is used.

## 2. Direct Yun-Lu coefficients

For the direct Yun-Lu Chapter-2 constrained-wall formula,

\[
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2}.
\]

At \(r=1\),

\[
\boxed{k_{crx}=\frac{32}{3}=10.6666666667}.
\]

The membrane coefficient is

\[
\boxed{k_p(1)=\frac{1066}{25}=42.64}.
\]

The elastic local-buckling stress is

\[
\sigma_{cr,Yun}^{E}
=
 k_{crx}
\frac{\pi^2E_s}{12(1-\nu_s^2)}
\left(\frac{t_s}{B_s}\right)^2.
\]

Substitution gives

\[
\boxed{\sigma_{cr,Yun}^{E}=794.388671697\ \mathrm{MPa}}.
\]

This value is common to Z1 and Z4 because their local \(B_s/t_s\), \(E_s\), \(\nu_s\) and minimum local halfwave ratio are the same.

## 3. Z1 event ordering

For Z1,

\[
f_y=235\ \mathrm{MPa},
\qquad
\varepsilon_y=\frac{f_y}{E_s}=0.001140776699.
\]

The direct ratio is

\[
\frac{\sigma_{cr,Yun}^{E}}{f_y}
=
\frac{794.388671697}{235}
=
\boxed{3.38037732637}.
\]

Therefore

\[
\boxed{f_y<\sigma_{cr,Yun}^{E}}.
\]

Hence the physically admissible local sequence is

\[
\boxed{Y_s\ \text{first}},
\]

not

\[
B_s\rightarrow S1_{Yun}\rightarrow Y_s.
\]

Result:

```text
Z1_DIRECT_YUN_LOCAL_ORDERING = YIELD_FIRST
Z1_YUN_ELASTIC_POSTBUCKLING_S1_BEFORE_YIELD = INACTIVE
```

The direct Yun elastic postbuckling strength-growth branch must not be forced before yield.

## 4. Z4 event ordering

For Z4,

\[
f_y=355\ \mathrm{MPa},
\qquad
\varepsilon_y=\frac{f_y}{E_s}=0.001723300971.
\]

The direct ratio is

\[
\frac{\sigma_{cr,Yun}^{E}}{f_y}
=
\frac{794.388671697}{355}
=
\boxed{2.23771456816}.
\]

Therefore

\[
\boxed{f_y<\sigma_{cr,Yun}^{E}}.
\]

Again the physically admissible local sequence is

\[
\boxed{Y_s\ \text{first}}.
\]

Result:

```text
Z4_DIRECT_YUN_LOCAL_ORDERING = YIELD_FIRST
Z4_YUN_ELASTIC_POSTBUCKLING_S1_BEFORE_YIELD = INACTIVE
```

## 5. What Yun-Lu does and does not supply for these two cases

Yun-Lu Chapter 2 supplies an elastic large-deflection postbuckling branch. In the project-derived Y-1/Y-2/Y-3/Y-4 interface, that branch is active only when the local elastic plate-buckling event precedes material yield.

For Z1/Z4 this prerequisite is not satisfied.

Therefore the Yun quantities

\[
\sigma_Y(A,A_0),
\qquad
E_{post}^{Yun}=\frac{d\sigma_Y/dA}{d\varepsilon_Y/dA}
\]

are not the active pre-yield continuation for either Z1 or Z4.

The user-approved ideal elastic-perfectly-plastic supplement still implies, at the scalar effective-stress level,

\[
\sigma_{s,eff}=E_s\varepsilon_s\quad(|\sigma|<f_y),
\]

and under continued plastic loading after first yield,

\[
\sigma_{s,eff}=f_y,
\qquad
E_{s,eff}^{tan}=0
\]

(up to a purely numerical platform regularization if a specific solver requires it).

However, Yun-Lu Chapter 2 does **not** provide the two-dimensional post-yield plane-stress redistribution/yield-front evolution required to obtain a source-consistent field

\[
\boldsymbol\sigma_s(\varepsilon_x,\varepsilon_y,\gamma_{xy}),
\qquad
\mathbf C_t^s=\partial\boldsymbol\sigma_s/\partial\boldsymbol\varepsilon_s
\]

after the yield-first event.

This limitation is source-consistent with Yun-Lu's own stated research boundary: material plasticity is not included in the analytical theory.

## 6. Consequence for the requested Z1/Z4 recalculation

The direct Yun execution therefore resolves the question as follows:

```text
DIRECT_YUN_FORMULA_RECOVERED = YES
Z1_LOCAL_YUN_COEFFICIENTS = CALCULATED
Z4_LOCAL_YUN_COEFFICIENTS = CALCULATED
Z1_EVENT_ORDERING = YIELD_FIRST
Z4_EVENT_ORDERING = YIELD_FIRST
YUN_S1_ACTIVE_FOR_Z1 = NO
YUN_S1_ACTIVE_FOR_Z4 = NO
```

Consequently, a new Z1/Z4 Pu cannot honestly be generated by simply replacing the radial-cap tangent with the Yun elastic postbuckling tangent. Doing so would activate a branch that both panels do not reach before yield.

The existing radial-cap Z1/Z4 values remain historical/current diagnostic checkpoints only; they are not relabeled as Yun results.

```text
NEW_Pu_Z1_FROM_DIRECT_YUN = NOT RELEASED
NEW_Pu_Z4_FROM_DIRECT_YUN = NOT RELEASED
REASON = YIELD-FIRST; YUN ELASTIC POSTBUCKLING BRANCH INACTIVE BEFORE THE REQUIRED PLASTIC PLANE-STRESS CONTINUATION
```

## 7. Relation to the zero-spatial Z6 framework

Nothing in this result reopens the Z6 integration machinery.

The formal structural path remains

```text
continuous current field
-> analytic representation
-> Cayley-Hamilton / exact analytic reduction as applicable
-> General-D15 exact moments
-> P, Rq, RA, KZ, L
-> connected limit solve
```

with zero formal spatial quadrature.

The only conclusion is mechanistic: for the current Zhou-family Z1/Z4 local steel panels, Yun-Lu is an event-ordering/elastic-postbuckling module, but it is not the missing yield-first plane-stress plastic current operator.

## 8. Supersession clarification

This execution corrects the overly broad statement that the previously constructed Yun Y-1 to Y-4 branch could itself be frozen as the complete steel current operator for Z1/Z4.

Correct statement:

```text
Yun Y-1..Y-4 = valid local elastic-postbuckling structural branch when B_s precedes Y_s.
Z1/Z4 Zhou Table-5.1 local panels = Y_s precedes B_s under the direct Yun formula.
Therefore Yun Y-1..Y-4 does not replace the required post-yield plane-stress continuation for Z1/Z4.
```

This is an execution result, not a new model assumption.
