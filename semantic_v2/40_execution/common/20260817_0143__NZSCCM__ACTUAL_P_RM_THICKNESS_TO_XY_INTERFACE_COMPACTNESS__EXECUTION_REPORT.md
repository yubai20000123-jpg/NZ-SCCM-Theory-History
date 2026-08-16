# NZ-SCCM — actual P/Rm thickness-to-XY interface compactness execution

**Timestamp:** 2026-08-17 01:43 +08:00  
**Status:** EXECUTED / INTERFACE CLOSED / PRODUCTION REPRESENTATION SELECTED / NO Pu RUN

## 1. Objective

Continue from the 01:15 full-R10 branch-aware `Syy` reduction and decide which exact representation should be carried into the actual structural `P` and five current membrane residuals `Rm`.

The comparison is end-to-end at the thickness-to-`(X,Y)` interface:

```text
A. global positive-part / factorised period form
B. event-resolved branchwise <=8-state form
```

The decision is made by the compactness of the **combined thickness + in-plane target**, not by through-thickness state size alone.

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

`Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS`.

---

## 2. Actual P/Rm interface collapses to only three common thickness resultants

Define the normalized complete-thickness stress moments

\[
N_x^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_x(X,Y,\zeta)\,d\zeta,
\]

\[
N_y^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_y(X,Y,\zeta)\,d\zeta,
\]

\[
N_{xy}^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\tau_{xy}(X,Y,\zeta)\,d\zeta.
\]

For `P` and the five membrane residuals, all five membrane basis functions are independent of thickness. Therefore only

\[
\boxed{N_x^{(0)},\;N_y^{(0)},\;N_{xy}^{(0)}}
\]

are required.

Concrete axial load:

\[
\boxed{
P_c=-\frac{bt}{2\pi^2}\int_0^\pi\!\int_0^\pi N_y^{(0)}\,dY\,dX.
}
\]

Let

\[
C_m^{vol}=\frac{\varepsilon_0 b\ell t}{2\pi^2}.
\]

For the five basis functions

\[
B_0=(1,0,0),
\]

\[
B_{20}=(\cos2X,0,0),
\]

\[
B_{u22}=(\cos2X\cos2Y,0,-\sin2X\sin2Y),
\]

\[
B_{02}=(0,\cos2Y,0),
\]

\[
B_{v22}=(0,\cos2X\cos2Y,-\sin2X\sin2Y),
\]

the concrete current membrane residuals reduce exactly to

\[
\boxed{
R_{m,0}^{c}=C_m^{vol}\int\!\int N_x^{(0)}\,dX\,dY,
}
\]

\[
\boxed{
R_{m,20}^{c}=C_m^{vol}\int\!\int \cos2X\,N_x^{(0)}\,dX\,dY,
}
\]

\[
\boxed{
R_{m,u22}^{c}=C_m^{vol}\int\!\int
\left[\cos2X\cos2Y\,N_x^{(0)}-\sin2X\sin2Y\,N_{xy}^{(0)}\right]dX\,dY,
}
\]

\[
\boxed{
R_{m,02}^{c}=C_m^{vol}\int\!\int \cos2Y\,N_y^{(0)}\,dX\,dY,
}
\]

\[
\boxed{
R_{m,v22}^{c}=C_m^{vol}\int\!\int
\left[\cos2X\cos2Y\,N_y^{(0)}-\sin2X\sin2Y\,N_{xy}^{(0)}\right]dX\,dY.
}
\]

Hence the actual `P + 5 Rm` package does **not** require six unrelated material integrals. One common three-resultant thickness operator feeds all six structural targets.

This is the first actual structural interface closure of the compact exact branch.

---

## 3. Downstream feedback from Rq / tangent before freezing the thickness API

Although the present gate is `P/Rm`, the later solver requirements were checked now so the API is not under-designed.

Nguyen `q`-derivative strains contain a membrane part plus a bending part proportional to `zeta`. Therefore:

```text
P and Rm values        -> stress moments k=0
Rq value               -> stress moments k=0,1
P/Rm derivatives wrt D,r -> tangent moments k=0
P/Rm derivatives wrt q   -> tangent moments k=0,1
Rq,q and bending-stability quadratic tangent kernels -> tangent moments up to k=2
```

Thus the complete later runtime needs only a low finite family

\[
\boxed{k=0,1\text{ for stress},\qquad k=0,1,2\text{ for tangent kernels}.}
\]

There is no downstream reason to generate an unbounded sequence of thickness moments.

---

## 4. Representation A — global positive-part / factorised period

Historical branch-free algebraic closure bound:

```text
full pointwise R10 field degree/state bound <=64
```

The current source-regular implementation no longer uses the singular old `c0,c1` differential basis; square-root derivatives are evaluated at source/matrix level by Fréchet/Sylvester rules.

For the three actual zero-order thickness resultants, a common fixed-endpoint descriptor may be viewed conservatively as

```text
64 common algebraic states
+ 3 accumulated target functionals Nx0, Ny0, Nxy0
<= 67 descriptor states
```

or equivalently each scalar stress component has holonomic order `<=64` and its antiderivative has order `<=65`.

The important property is not the exact implementation count `67`; it is that the bound is **fixed and independent of any Chebyshev/Taylor truncation order**.

The output presented to the `(X,Y)` layer is simply

```text
Nx0(X,Y), Ny0(X,Y), Nxy0(X,Y)
```

evaluated between the fixed physical endpoints

\[
\boxed{\zeta=-1,\qquad\zeta=+1.}
\]

No source-knot root is exposed to the in-plane integration layer.

---

## 5. Representation B — event-resolved branchwise <=8-state

On any fixed material-event topology interval, the complete R10 stress lies in the 8-state field

\[
[1,q,s,qs,g,qg,sg,qsg].
\]

Therefore a fixed-topology common three-resultant antiderivative package would need only roughly

```text
8 branch field states + 3 accumulated resultants <= 11 states
```

and each scalar branch antiderivative has order at most `9`.

This local reduction is real and remains retained.

However, the material-event endpoints are roots of

\[
\det(E_m(X,Y)+\zeta E_b(X,Y)-\lambda_mI)=0.
\]

For the full five-coordinate Nguyen strain field, writing

\[
a_2(X,Y)\zeta^2+a_1(X,Y)\zeta+a_0(X,Y)=0,
\]

the exact symbolic trigonometric-polynomial degrees are

```text
deg a2 = 4

deg a1 = 6

deg a0 = 8

deg(a1^2-4 a2 a0) = 12
```

and the event roots therefore contain

\[
\sqrt{\Delta_{event}(X,Y)},\qquad \deg\Delta_{event}=12.
\]

An event enters/leaves the physical thickness interval when

\[
F_{m,\pm}(X,Y)=\det(E(X,Y,\pm1)-\lambda_mI)=0.
\]

For generic five-coordinate kinematics:

```text
trigonometric-polynomial total degree of F_m,+/- = 8
```

with 45 monomial terms in the un-reduced `(sinX,cosX,sinY,cosY)` representation used by the reproducer.

Thus explicit event resolution sends nontrivial moving algebraic endpoints and event-front selectors into the `(X,Y)` layer.

---

## 6. Actual Case21 topology audit confirms that the event pattern changes over X,Y

This audit uses the historical Case21 state only as an independent topology probe; it is **not** a production spatial integration and does not select any coefficient or capacity.

Input:

```text
D  = 0.8359179831666168
q  = 0.0017897894751107222
q0 = 0.0025
Cm = 0.02869338081034484
Cb = 0.06685330648582646
nu = 0.18
kappa = 2.0005129533678754
lambda1  = 0.05008051764913755
lambda10 = 0.49988116674539307
```

A deterministic `61 x 61` `(X,Y)` audit grid was used only to classify whether exact thickness knot roots lie in `[-1,1]`.

With `r=0`:

```text
no knot root in thickness   : 2260 / 3721 = 60.7364%
one lambda1 root, no lambda10: 1461 / 3721 = 39.2636%
```

With the elastic Airy leading membrane coordinate

```text
r=[-0.008464547339051727,
   -0.0058821430661206925,
   +0.007173345202586210,
   -0.0058821430661206925,
   +0.007173345202586210]
```

the topology is still nonuniform:

```text
no knot root in thickness   : 2646 / 3721 = 71.1099%
one lambda1 root, no lambda10: 1075 / 3721 = 28.8901%
```

Representative exact-root locations from the same audit:

```text
r=0, X=Y=pi/2             : zeta_lambda1 = 0.6142706566203897
r=0, X~0,Y=pi/2           : no root
elastic Airy, X=Y=pi/2    : zeta_lambda1 = 0.5262848354947325
elastic Airy, X~0,Y=pi/2  : no root
```

At `r=0`, the endpoint event-front determinant for `lambda1` changes sign between these locations; the front is therefore not a vacuous algebraic artifact.

---

## 7. Independent thickness-value audit

For audit only, direct adaptive numerical integration of the frozen R10 principal-value law was compared with integration explicitly split at the exact event roots.

Representative normalized zero-order resultants:

```text
r=0, X=Y=pi/2:
Nx0  = -0.008123709089485608
Ny0  = -1.2564804933299716
Nxy0 = 0
root = 0.6142706566203897
max(global - event-split) = 2.22e-16

r=0, X=pi/4,Y=pi/3:
Nx0  = +0.05308843805915956
Ny0  = -1.1700505691347807
Nxy0 = +0.016744936289816503
root = 0.7645958247563336
max(global - event-split) = 6.94e-18

elastic Airy, X=Y=pi/2:
Nx0  = +0.014344421825753101
Ny0  = -1.167862053500704
Nxy0 = 0
root = 0.5262848354947325
max(global - event-split) = 6.94e-18
```

This confirms that representations A and B are evaluations of the same frozen source law; the choice is computational representation only.

The numerical integration above is an independent oracle and is not a formal structural operator.

---

## 8. End-to-end representation decision

The locally smaller 8-state form is **not** promoted to the global structural production interface because its event topology varies over the complete halfwave.

To use it globally one must do one of two things:

1. partition the `(X,Y)` domain by the algebraic fronts `F_m,+/-=0`; or
2. reassemble moving-root inclusion/order with clipped-root / positive-part selectors.

Option 1 conflicts with the locked one-complete-domain formal architecture.

Option 2 recreates the same branch-free algebraic structure that representation A already keeps directly, while adding explicit moving-root bookkeeping.

Therefore:

```text
PRODUCTION_THICKNESS_TO_XY_REPRESENTATION
    = GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD

EVENT_RESOLVED_8_STATE
    = RETAIN_AS_LOCAL_EXACT/AUDIT_REPRESENTATION
    = NOT THE GLOBAL XY PRODUCTION INTERFACE
```

This is a structural-complexity decision, not a material approximation and not a calibration.

---

## 9. What is now closed

```text
ACTUAL_P_RM_COMMON_THICKNESS_INTERFACE = PASS_EXACT_FORM
P_PLUS_FIVE_RM_REQUIRE_ONLY_3_ZERO_ORDER_STRESS_RESULTANTS = PASS
EVENT_ROOT_XY_TOPOLOGY_NONUNIFORM = CONFIRMED
EVENT_RESOLVED_8_STATE_GLOBAL_PRODUCTION = REJECTED_FOR_INTERFACE_COMPLEXITY
GLOBAL_FIXED_ENDPOINT_BRANCH_FREE_PERIOD = SELECTED_FOR_PRODUCTION
HIGH_ORDER_MATERIAL_COEFFICIENT_ENUMERATION = NOT REQUIRED
```

The 8-state result remains valuable for:

- source identity audits;
- branchwise endpoint checks;
- exact local oracle construction;
- diagnosing source-knot events.

It is not discarded.

---

## 10. Next execution

The next unique implementation task is

```text
GLOBAL_FIXED_ENDPOINT_THREE_STRESS_MOMENT_DESCRIPTOR_GATE
```

Construct the actual common fixed-endpoint operator

\[
(D,q,r;X,Y)\mapsto
[N_x^{(0)},N_y^{(0)},N_{xy}^{(0)}]
\]

without explicit 64-coefficient canonicalization and without numerical thickness quadrature.

The implementation should use the source-regular factorized R10 DAG, exact matrix Fréchet/Sylvester rules, CH reduction and target-side contraction.

It must return all three resultants from one common material state and expose their same-source parameter derivatives needed by `P/Rm`.

Only after this operator passes should the three fixed-endpoint period outputs be contracted over `(X,Y)` to produce actual `P_c` and all five `Rm,c` values.

`NEW_Pu = NOT_RUN`.
