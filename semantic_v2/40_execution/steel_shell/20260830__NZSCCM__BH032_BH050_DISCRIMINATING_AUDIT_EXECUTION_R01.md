# NZ-SCCM — BH032/BH050 受力重分配判别审计执行 R01

**Date:** 2026-08-30  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `EXECUTED DIAGNOSTIC AUDIT / NO CALIBRATION / NO PRODUCTION THEORY CHANGE / MAIN UNCHANGED`

## 0. Purpose and governance

本文件执行 2026-08-30 先前冻结的 D1–D4 判别方案，用现有 frozen theory states 和已归档 FEM post-check evidence 区分 BH050 受力分配误差究竟主要来自：

1. frozen initial-stiffness Airy demand；
2. force-first R4 section strain–curvature path；
3. R02 local operator；
4. exact GL(qU) omission；
5. R06 first-local-yield gate。

No FEM/test value is used to modify a root, choose a theory branch, fit a parameter, or calibrate a material rule. Historical five-equation R06 endpoints are used only because they carry the archived BH032/BH050 component-resultant evidence. Current production diagnostic terminal remains the R4/J4 architecture; this audit does not reinstate the old UHPC `-0.0035` contact as a global terminal.

Primary frozen theory evidence:

- BH032: `20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`
- BH050: `20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md`
- common R06 code: `20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`
- equal-contract load-share evidence: `20260826_1401__NZSCCM__BH032_BH050_LOAD_SHARE_AND_BH075_BH100_BLIND_PREFLIGHT_R01.md`

---

# 1. D1 — component force-share residual

Frozen equal-contract shares at the comparison section are:

| Case/source | UHPC | steel faces | web |
|---|---:|---:|---:|
| BH032 FEM | 66.49% | 28.95% | 4.56% |
| BH032 theory | 64.24% | 31.45% | 4.31% |
| BH050 FEM | 55.80% | 40.61% | 3.58% |
| BH050 theory | 73.49% | 23.19% | 3.33% |

Theory minus FEM, percentage points:

\[
BH032=(-2.25,+2.50,-0.25),
\]

\[
\boxed{BH050=(+17.69,-17.42,-0.25).}
\]

Therefore the new BH050 error is almost a one-for-one transfer:

\[
\boxed{\text{steel faces}\longrightarrow\text{UHPC}},
\]

while web error remains essentially unchanged at `-0.25 percentage point` in both cases.

The more detailed archived BH050 split is:

```text
FEM upper steel  = 19.84%
FEM lower steel  = 20.85%
theory upper     =  5.90%
theory lower     = 17.29%
```

so

\[
\Delta share_{upper}=-13.94\ \text{points},
\qquad
\Delta share_{lower}=-3.56\ \text{points}.
\]

About 80% of the steel-share deficit is therefore associated with the **upper face**, not the lower R06 face.

Frozen terminal face-mean longitudinal stresses provide the same diagnosis:

```text
BH050 theory upper/lower = -75.74 / -222.06 MPa
BH050 FEM    upper/lower = -256.87 / -226.94 MPa
```

Errors in compression magnitude are approximately:

```text
upper = 181.13 MPa under-compressed by theory
lower =   4.88 MPa under-compressed by theory
```

At the same FEM peak load, the archived same-load theory solve gives approximately:

```text
theory upper/lower = -94.8 / -222.4 MPa
FEM    upper/lower = -256.9 / -226.9 MPa
```

so the upper error remains about `162.1 MPa`, whereas the lower error is only about `4.5 MPa`.

**D1 decision:**

```text
WEB_PRIMARY_CAUSE = REJECTED
LOWER_R06_ALONE_PRIMARY_CAUSE = REJECTED
UPPER_FACE / UHPC REDISTRIBUTION = CONFIRMED
```

---

# 2. D2 — uncapped upper-R02 consistent tangent audit

The frozen common R02 operator uses, for the local-buckling branch,

\[
F(U,e_x,e_y)=B_3U^3+B_1(e_x,e_y)U+B_0=0.
\]

For an admissible interior amplitude root,

\[
\boxed{
U_{,e_i}=-\frac{F_{,e_i}}{F_{,U}},
\qquad
F_{,U}=3B_3U^2+B_1.
}
\]

The whole-width physical mean stress is

\[
\bar\sigma_x=-Q_s[m_x+\nu_s m_y],
\qquad
\bar\sigma_y=-Q_s[m_y+\nu_s m_x],
\]

with compression-positive internal R02 strains and tension-positive physical stresses. Applying the implicit derivative above to the exact frozen upper-face states gives the condensed physical tangent

\[
\mathbf C^{R02}_{upper}
=\frac{\partial(\sigma_x,\sigma_y)}{\partial(\varepsilon_x,\varepsilon_y)}.
\]

### BH032 upper face

Frozen state:

\[
(\varepsilon_x,\varepsilon_y)_+
=(+0.000636993485,-0.001393087449),
\]

\[
U_+=0.711487681071\ \mathrm{mm}.
\]

Computed tangent:

\[
\boxed{
\mathbf C^{R02}_{upper,BH032}
\approx
\begin{bmatrix}
177.465&18.345\\
18.345&176.139
\end{bmatrix}\ \mathrm{GPa}.
}
\]

### BH050 upper face

Frozen state:

\[
(\varepsilon_x,\varepsilon_y)_+
=(+0.001040838732,-0.000640959594),
\]

\[
U_+=0.169266885792\ \mathrm{mm}.
\]

Computed tangent:

\[
\boxed{
\mathbf C^{R02}_{upper,BH050}
\approx
\begin{bmatrix}
225.290&66.814\\
66.814&225.261
\end{bmatrix}\ \mathrm{GPa}.
}
\]

For reference, the uncondensed plane-stress elastic steel matrix is approximately

\[
\begin{bmatrix}
226.374&67.912\\
67.912&226.374
\end{bmatrix}\ \mathrm{GPa}.
\]

Hence the BH050 upper R02 state is positive, regular, and almost elastic in its condensed mean tangent. In particular,

\[
\boxed{\partial\sigma_y/\partial\varepsilon_y>0.}
\]

Therefore, if the upper-face longitudinal strain becomes more compressive, this R02 operator itself predicts a more compressive mean longitudinal stress. It does **not** intrinsically produce the upper-face unloading seen in the theory path.

The archived FEM path also shows upper strain and upper stress both becoming more compressive toward peak. Thus the direction of the R02 constitutive response is compatible with FEM; the discrepancy enters because the coupled section solve supplies the upper face with a different strain/curvature path.

**D2 decision:**

```text
UPPER_R02_OPERATOR_PRIMARY_CAUSE = REJECTED
UPPER_UNLOADING_IS_IMPOSED_BY_COUPLED_SECTION_PATH = SUPPORTED
```

---

# 3. D3 — q-implied common-curvature versus independent R4/R06 section curvature

For the retained global added mode

\[
w_m=bq\sin(\alpha x)\sin(\beta y),
\]

at the transverse/longitudinal antinode the added global curvature is

\[
\kappa_g=bq\beta^2.
\]

For both frozen BH032 and BH050 families,

\[
\ell=b,\qquad \beta=\pi/b,
\]

therefore

\[
\boxed{\kappa_g=\frac{\pi^2q}{b}.}
\]

This is a pure kinematic audit quantity. It is **not** imposed as a new equation.

## 3.1 BH032 frozen endpoint

\[
q=0.00137889961633743,\qquad b=1600\ \mathrm{mm}.
\]

Thus

\[
\boxed{\kappa_g=8.50574608\times10^{-6}/\mathrm{mm}.}
\]

Frozen force-first section solution:

\[
\kappa_x=2.07125070\times10^{-5}=2.435\kappa_g,
\]

\[
\boxed{\kappa_y=4.78843762\times10^{-5}=5.630\kappa_g.}
\]

Archived UHPC thickness-fit diagnostic at FEM peak:

\[
\kappa_{UHPC,FE}=1.93135\times10^{-5}/\mathrm{mm}
=2.271\kappa_g.
\]

So the frozen section \(\kappa_y\) is approximately

\[
2.479\times\kappa_{UHPC,FE}.
\]

BH032 therefore already contains a nontrivial q-to-section-curvature mismatch even though total Pu happens to be nearly exact.

## 3.2 BH050 frozen endpoint

\[
q=0.004772819645833164,\qquad b=2500\ \mathrm{mm}.
\]

Therefore

\[
\boxed{\kappa_g=1.88423367\times10^{-5}/\mathrm{mm}.}
\]

Frozen section solution:

\[
\kappa_x=4.40275834\times10^{-5}=2.337\kappa_g,
\]

\[
\boxed{\kappa_y=6.49781910\times10^{-5}=3.449\kappa_g.}
\]

Archived UHPC thickness-fit diagnostic:

\[
\kappa_{UHPC,FE}=1.83974\times10^{-5}/\mathrm{mm}.
\]

Remarkably,

\[
\boxed{\kappa_{UHPC,FE}/\kappa_g=0.9764.}
\]

Thus the **Airy q-implied geometric curvature differs from the FEM UHPC fit by only about 2.4% at this endpoint**, whereas the force-first section \(\kappa_y\) is

\[
\boxed{3.532\times\kappa_{UHPC,FE}.}
\]

This is the strongest new discriminator from the present audit.

It means the BH050 problem cannot be summarized as “the Airy amplitude q is incapable of representing the observed curvature.” The q-derived geometric curvature is actually close to the observed UHPC thickness gradient; the very large asymmetry is introduced when the four-resultant section solve chooses an **independent** \(\kappa_y\).

## 3.3 Same-load audit at the FEM peak load

Without using FEM to change the root, invert only the already-frozen explicit Airy relation

\[
P^A(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)
\]

at the independently observed FEM peak loads.

BH032, at `10.990480 MN`:

\[
q=0.001388642235,
\quad bq=2.22183\ \mathrm{mm},
\]

\[
\kappa_g=8.56584\times10^{-6}/\mathrm{mm}.
\]

BH050, at `12.591227 MN`:

\[
q=0.004117589557,
\quad bq=10.29397\ \mathrm{mm},
\]

\[
\boxed{\kappa_g=1.62555920\times10^{-5}/\mathrm{mm}.}
\]

The BH050 FEM UHPC fit is only about `13.2%` larger than this same-load q-implied curvature. This is still far closer than the frozen independent section curvature.

**D3 decision:**

```text
GENERIC_AIRY_Q_CURVATURE_FAILURE = NOT_SUPPORTED
R4 / SECTION INDEPENDENT-CURVATURE PATH MISMATCH = STRONGLY SUPPORTED
BH032_NEAR-EXACT_Pu_DOES_NOT_VALIDATE_INTERNAL_KINEMATICS = CONFIRMED
```

---

# 4. Additional direct evidence: theoretical upper/local amplitude asymmetry

The R02 mode

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta)
\]

has maximum shape value `4`, so a rough theory-side peak local deflection scale is `4U`.

Frozen theory values:

| case | upper U mm | lower U mm | 4U upper mm | 4U lower mm |
|---|---:|---:|---:|---:|
| BH032 | 0.7115 | 1.5187 | 2.846 | 6.075 |
| BH050 | 0.1693 | 2.9398 | 0.677 | 11.759 |

Archived FEM local-wave diagnostic at peak is approximately:

```text
BH032 TOP/BOTTOM = 8.565 / 11.322 mm
BH050 TOP/BOTTOM = 14.672 / 15.945 mm
```

The definitions are not identical enough to promote `4U / FE-wave` to a formal equality, because the FEM quantity is a Coons-baseline shell-wave observable. Nevertheless the **directional** result is decisive: BH050 theory chooses an almost flat/low-amplitude upper local state while FEM exhibits a strong upper local wave of the same order as the lower face. This is consistent with the upper-unloading / excessive section-curvature diagnosis.

---

# 5. D4 — exact GL(qU) geometric significance audit

The exact two-scale geometry uses

\[
\boxed{d=U^2-A_0^2}
\]

and

\[
\boxed{\Delta=b[(q_0+q)U-q_0A_0].}
\]

Both have unit `mm^2`. Before applying registration-dependent coefficients \(h_x,h_y,h_\gamma,K_{d\Delta},K_{\Delta\Delta}\), the ratio

\[
|\Delta/d|
\]

is a useful **raw geometric significance indicator only**.

Computed frozen-state values:

| Case/face | d mm² | Delta mm² | |Delta/d| |
|---|---:|---:|---:|
| BH032 upper | 0.45559 | 3.51566 | 7.717 |
| BH032 lower R06 | 2.25567 | 8.52511 | 3.779 |
| BH050 upper | -0.094945 | 0.880353 | 9.272 |
| BH050 lower R06 | 8.51910 | 51.25516 | 6.017 |
| BH050 lower full trial | 24.87036 | 88.70199 | 3.567 |

Therefore GL is not parametrically negligible. In particular the BH050 lower projected state has a raw \(|\Delta/d|\) around `6.0`, versus `3.8` for BH032 lower.

However the actual sign and resultant correction require the real PBL-cell registration

\[
(x_0,y_0,s_f)
\]

because

\[
h_x,h_y,h_\gamma,K_{d\Delta},K_{\Delta\Delta}
\]

are phase dependent. Those registration values are not carried in the frozen R06 terminal reports used here. Therefore this audit does **not** invent them and does not claim a corrected steel resultant.

**D4 decision:**

```text
GL_qU_PARAMETRICALLY_SMALL = REJECTED
GL_qU_GEOMETRIC_SIGNIFICANCE = PASS
GL_qU_RESULTANT_CORRECTION = BLOCKED_BY_MISSING_EXACT_CELL_REGISTRATION
GL_qU_PRIMARY_CAUSE = NOT_YET_PROVEN
```

---

# 6. Lower R06 is a trigger, but not the sole error

Archived same-load path evidence places BH050 lower-face R06 activation around

\[
P_{LY,-}\approx8.833\ \mathrm{MN}\approx0.70P_u^{FE}.
\]

After that event, the theoretical lower mean longitudinal stress remains close to `-223 MPa`, which is also close to FEM. To continue satisfying

\[
N_L^{sec}=N_L^d,
\qquad
M_L^{sec}=M_L^d,
\]

theory then changes \(\varepsilon_L^0,\kappa_L\) so that the upper face unloads from roughly `-129 MPa` toward `-95 MPa` at the same FE peak load. FEM instead keeps the lower face near `-207` to `-227 MPa` **and continues compressing the upper face** from roughly `-211` to `-257 MPa`.

Since D2 shows the uncapped upper R02 operator has a positive regular tangent, this upper unloading is not a constitutive necessity. It is selected by the coupled N–M equilibrium path after the lower active-set change.

Therefore:

\[
\boxed{
\text{lower R06 event}
\;\text{acts as a trigger}
\quad+
\quad
\text{R4/section N--M redistribution chooses the wrong high-asymmetry branch}.
}
\]

This is more precise than either extreme statement:

- `R06 is wrong` — too broad;
- `Airy is wrong` — also too broad.

---

# 7. Revised causal ranking after execution

The earlier 2026-08-30 diagnosis ranked frozen Airy stiffness feedback first and R4 compatibility second. The actual discriminating calculations require that ranking to be refined.

## Rank 1 — PRIMARY, strongest direct evidence

\[
\boxed{
\textbf{force-first R4 / section strain--curvature path and N--M redistribution branch}
}
\]

Evidence:

1. BH050 error is almost entirely UHPC ↔ steel-face transfer;
2. lower R06 face is already close to FEM;
3. upper face carries most of the missing steel compression;
4. upper uncapped R02 tangent is healthy and predicts continued compression under continued compressive strain;
5. Airy q-implied curvature is close to the FEM UHPC thickness gradient;
6. independent section \(\kappa_y\) is about 3.45 times q-implied curvature and 3.53 times the FEM fit;
7. after lower R06 activation, theory satisfies N–M by upper unloading whereas FEM continues upper compression.

## Rank 2 — IMPORTANT architecture contributor, but not isolated as primary by current evidence

\[
\boxed{
\textbf{frozen initial-stiffness Airy demand lacks current tangent feedback}
}
\]

This remains a real theoretical limitation: current steel/UHPC/web tangent changes do not re-enter \(K_x,G,J_x,J_y,C\) to regenerate the global demand field. It can amplify redistribution error in deep local buckling.

However D3 demonstrates that the Airy q coordinate itself is not grossly wrong for BH050 curvature. Therefore current evidence does not support blaming the 17.7-point phase-share error primarily on “Airy cannot use nonlinear stiffness”. A full constituent tangent-to-demand sensitivity audit would be required to isolate this effect.

## Rank 3 — IMPORTANT, presently unquantified correction

\[
\boxed{\textbf{exact registered GL(qU) coupling}}
\]

The raw geometric ratios prove GL is not negligible, particularly in BH050. But without exact cell registration the sign/magnitude of the resultant correction cannot honestly be stated.

## Rank 4 — active-set trigger / secondary continuation issue

\[
\boxed{\textbf{R06 first-local-yield projection and post-event tangent/work consistency}}
\]

R06 lower-face capping cannot be the sole cause because the lower face is already reproduced well. Nevertheless its activation changes the coupled equilibrium branch and is the point after which the upper-unloading discrepancy grows. Post-local-yield continuation may still require improvement.

## Not leading suspects at this stage

- geometric wave numbers \(k_x,k_y\);
- frozen LL coefficient \(K_A\);
- local wavelength \(L_y\);
- global integer mode \(m_*\);
- web;
- lower R06 face alone;
- the uncapped upper R02 constitutive operator alone;
- the old UHPC `-0.0035` contact as a universal physical failure criterion.

---

# 8. Current best causal statement

\[
\boxed{
\begin{aligned}
\text{BH050 discrepancy is primarily a }&
\text{force-first section-kinematics / N--M redistribution branch problem},\\
&\text{triggered and amplified by deep local buckling},\\
&\text{rather than simply an Airy nonlinear-stiffness deficiency.}
\end{aligned}
}
\]

A more physical description is:

```text
BH050 enters deep local buckling early
    -> lower face reaches the R06 active set
    -> actual structure keeps both faces substantially engaged in compression
    -> frozen theory holds the lower face near its R06 resultant
    -> R4 closes the prescribed N_L / M_L demand by increasing section curvature
       and unloading the upper face
    -> UHPC is forced to take too much axial compression
    -> total P can remain moderately close while constituent load sharing becomes wrong
```

This diagnosis also explains why BH032 can have an excellent total-load error while still failing strict internal kinematic correspondence: BH032 lies closer to the transition regime and its internal errors can compensate in total P.

---

# 9. Next discriminating execution

The next operation should **not** immediately rewrite Airy or R06. The highest-information next tests are:

1. recover exact BH032/BH050 PBL-cell registrations `(x0,y0,s_f)` and execute the full GL(qU) resultant correction at frozen same-load states;
2. compute constituent-by-constituent longitudinal tangent block

\[
\frac{\partial(N_L,M_L)}{\partial(\varepsilon_L^0,\kappa_L)}
\]

before and after lower R06 activation to identify which term drives the high-curvature branch;
3. compare this block with the q-implied common-curvature diagnostic without imposing a fifth compatibility equation;
4. only if these fail should a current-tangent-updated Airy front be opened as a new theory candidate.

This preserves the current explicit zero-spatial architecture and avoids changing several layers simultaneously.

---

# 10. Gate ledger

```text
D1_FORCE_SHARE_EXECUTED = PASS
D2_UPPER_R02_TANGENT_EXECUTED = PASS
D3_Q_COMMON_CURVATURE_EXECUTED = PASS
D4_GL_GEOMETRIC_MAGNITUDE_EXECUTED = PASS
D4_FULL_RESULTANT = BLOCKED_BY_MISSING_CELL_REGISTRATION
AIRY_MATHEMATICS_PRIMARY_CAUSE = NO
FROZEN_AIRY_FEEDBACK_LIMITATION = REAL_BUT_NOT_ISOLATED_PRIMARY
R4_SECTION_PATH_PRIMARY_CAUSE = STRONGLY_SUPPORTED
LOWER_R06_ALONE_PRIMARY_CAUSE = NO
UPPER_R02_OPERATOR_PRIMARY_CAUSE = NO
GL_qU_IMPORTANCE = PLAUSIBLE_AND_NONSMALL / NOT_YET_CAUSALLY_QUANTIFIED
CALIBRATION_USED = NO
THEORY_ROOT_CHANGED = NO
PRODUCTION_MAIN_CHANGED = NO
```
