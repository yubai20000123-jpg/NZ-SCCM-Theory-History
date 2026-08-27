# NZ-SCCM — restored direct Airy -> N-M path source-consistency audit R01

**Time:** 2026-08-27 15:40 +08:00  
**Parent correction:** `20260827_1525__NZSCCM__RESTORE_DIRECT_AIRY_TO_NM_PATH_AND_DOWNGRADE_CURRENT_BENDING_EXTENSION_R01.md`  
**Status:** `DIRECT PATH SOURCE AUDIT / AIRY FRONT PASS / UHPC ENDPOINT PASS / qU PASS / MEMBRANE-DEFORMATION HANDOFF REQUIRES NEXT CLARIFICATION`

---

## 0. Purpose

After restoring the compact direct architecture, this audit checks whether the large BH032/BH050 candidate loads came from an accidental formula/unit change, an unauthorized UHPC endpoint, or from a still-hybrid deformation handoff.

No FEM/test value is used to alter any equation or root.

---

# 1. Airy front identity — PASS

The frozen milestone source `20260825_1435__NZSCCM__SSUHPC_MILESTONE_CORE_NM_CLOSURE_7CASE_BLIND_ABAQUS_POSTCHECK_R01.md` defines after integer half-wave selection

\[
Q_q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ_q,
\]

\[
N_x^d=K_xQ_q,
\]

\[
N_y^d=-\left[\frac{P(q)}b+GQ_q(1-2s^2)\right],
\]

\[
M_x^d=J_xqs,\qquad M_y^d=J_yqs.
\]

The 2026-08-27 qU/common-curvature repair retained exactly the same `P(q), Nx^d, Ny^d` formulas and definitions.

Therefore

```text
AIRY_PQ_FORMULA_DRIFT = NO
AIRY_NX_NY_FORMULA_DRIFT = NO
AIRY_UNIT_REDEFINITION = NO
```

The rise of the repaired BH candidate loads is not caused by changing the explicit Airy load law.

---

# 2. UHPC compression endpoint identity — PASS

The frozen UHPC material unit is explicitly defined only on the pre-peak compression branch

\[
\sigma_U(\varepsilon)
=-f_c\frac{n_h\xi-\xi^2}{1+(n_h-2)\xi},
\qquad
\xi=-\frac{\varepsilon}{\varepsilon_{c0}},
\qquad
0\le\xi\le1.
\]

The same source explicitly states that the terminal capacity envelope stops at first compressed UHPC face contact with

\[
\boxed{\xi=1}
\]

and that a post-peak branch is not used to extend `Pu`.

Hence the 13:35 repaired calculation's active condition

\[
\varepsilon_y^0-\frac{t_c}{2}\kappa_y^g=-0.0035
\]

is source-faithful.

Therefore

```text
UHPC_ENDPOINT_EPS_C0 = PASS
POSTPEAK_EXTENSION_REQUIRED = NO
```

The large BH050 candidate cannot be explained by an accidental use of an unauthorized UHPC post-peak branch.

---

# 3. qU identity — PASS and quantitatively secondary

The repaired steel-local operator uses

\[
\Delta=b[(q_0+q)U-q_0A_0]
\]

and the exact finite harmonic GL coefficients.

The 13:35 isolation calculation showed, with the common-curvature repair held fixed:

```text
BH032: qU changes candidate Pu by about -0.6234%
BH050: qU changes candidate Pu by about -0.2503%
```

Therefore qU is physically required but is not the cause of the large upward shift in the direct-path BH050 endpoint.

---

# 4. Common-curvature identity — PASS as the intended repair

The repaired gross curvature at the BH control antinode is

\[
\boxed{
\kappa_x^g=\kappa_y^g=\frac{\pi^2q}{b}.
}
\]

This follows directly from

\[
\Delta w_g=bq\sin(\pi x/b)\sin(\pi y/\ell)
\]

and removes the old ability of terminal `kappa_x,kappa_y` to become much larger than the curvature implied by the global deflection amplitude.

The 13:35 result confirms that this is the dominant change. Therefore

```text
RESTORE_INDEPENDENT_KAPPA = PROHIBITED
```

No attempt is made to recover the old predictions by reintroducing the deleted curvature degrees of freedom.

---

# 5. Important remaining distinction: the present direct path is not yet literally "Airy gives every strain"

The milestone terminal architecture before the repair used five terminal unknowns

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)
\]

and solved four resultant equalities plus one UHPC endpoint condition.

After the common-curvature repair, the 13:35 calculation reduced this to

\[
(q,\varepsilon_x^0,\varepsilon_y^0)
\]

with

\[
\kappa_x=\kappa_x^g(q),\qquad
\kappa_y=\kappa_y^g(q),
\]

but it still obtained the two membrane offsets by **current section resultant closure**:

\[
\boxed{N_x^{sec}=N_x^d,}
\]

\[
\boxed{N_y^{sec}=N_y^d.}
\]

Therefore the exact current implementation is best described as

```text
Airy gives: P(q), Nx^d, Ny^d, common curvature kappa(q)
current N-M section solves: eps_x0, eps_y0 from Nx/Ny equilibrium
material endpoint selects: q_u
Pu = P_Airy(q_u)
```

It is **not** yet literally

```text
Airy gives every membrane strain/deformation directly
then N-M is only evaluated with no resultant closure
```

This distinction matters because the user's intended compact wording is "Airy explicitly computes deformation -> substitute deformation into N-M -> reach ultimate load".

The existing 13:35 root solve is compact and contains no new plate-area integral, but the membrane-deformation handoff remains a hybrid `Airy demand -> current-section membrane closure` rather than a fully explicit `Airy deformation -> N-M evaluation` map.

No conclusion is made here that this hybrid handoff is wrong. It is identified as the next exact architecture question that must be resolved from the original Airy derivation rather than from FEM agreement.

---

# 6. Consequence for the existing BH candidates

Under the corrected governance, the 13:35 roots are no longer rejected by a mandatory full-halfwave moment gate:

| quantity | BH032 | BH050 |
|---|---:|---:|
| `q_u` | 0.001835902565 | 0.011215527128 |
| `Pu=P_Airy(q_u)` / MN | 13.04567021 | 17.98426079 |

They remain

```text
DIRECT_AIRY_TO_NM_BLIND_CANDIDATES
NOT PRODUCTION-QUALIFIED
```

because comparator post-checks show large overprediction, especially BH050.

But the next audit must remain inside the direct architecture; the prediction error alone is not permission to reopen full-halfwave nonlinear current-moment integration.

---

# 7. Frozen next step

The next task is narrowly defined:

\[
\boxed{
\text{Recover from the original explicit Airy solution exactly which membrane deformation variables are already explicit functions of }q\text{ (and load/control variables), and which must legitimately be obtained from }N_x,N_y\text{ closure.}
}
\]

Specifically:

1. trace the original Airy stress-function / compatible displacement derivation from `q` to membrane displacement/strain coefficients;
2. distinguish quantities fixed by kinematics from quantities fixed by in-plane equilibrium;
3. determine whether `eps_x0, eps_y0` in the SSUHPC terminal section are independent equilibrium variables or should be explicit Airy functions;
4. derive the resulting no-new-area-integral direct system;
5. only then rerun BH032/BH050 blind.

The following remain prohibited:

```text
full-halfwave nonlinear current M projection as automatic next step
independent terminal curvature
material retuning
FEM-selected root/phase
spatial numerical quadrature
material-point grid
```

---

# 8. Current status

```text
DIRECT AIRY P(q) FRONT             PASS
qU STEEL-LOCAL REPAIR              PASS
q -> COMMON CURVATURE              PASS
UHPC N-M                           UNCHANGED / PASS
UHPC xi=1 TERMINAL ENVELOPE        SOURCE-FAITHFUL / PASS
NEW x-y NONLINEAR AREA INTEGRAL    NOT REQUIRED
MEMBRANE DEFORMATION HANDOFF       NEXT AUDIT TARGET
```
