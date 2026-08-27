# NZ-SCCM — BH032/BH050 qU + common-curvature exact-coefficient blind recalculation R01

**Time:** 2026-08-27 13:35 +08:00  
**Parent theory:** `20260827_1240__NZSCCM__EXPLICIT_AIRY_Q_U_COMMON_CURVATURE_REPAIR_WITH_UNCHANGED_NM_R02.md`  
**Status:** `GEOMETRY_COEFFICIENTS PASS / BLIND PRE-CERTIFIED ROOTS FIXED / FIRST-REPAIR Pu ARCHITECTURE FAILS MOMENT GATE / NO MATERIAL RETUNING`

---

## 0. Scope

This execution does exactly the requested next step:

1. recover the actual self-similar BH PBL registration relevant to the control station;
2. compute `hx, hy, hgamma, KdDelta, KDeltaDelta` by finite exact harmonic moments;
3. retain the frozen UHPC directional exact N-M, web law and R06 concept;
4. enforce the repaired common curvature `kappa_x=kappa_y=pi^2 q/b` at the BH antinode;
5. solve the first repaired terminal system for BH032 and BH050 blind;
6. freeze the new roots before comparator post-check;
7. audit the old Airy moment demands rather than using them to create independent curvatures.

No experimental/FEM load is used in the coefficient calculation or root solve.

Formal spatial integration remains

```text
N_formal_spatial_quadrature = 0
MATERIAL_POINTS = 0
FITTED_qU_COEFFICIENT = NONE
FITTED_CURVATURE_FACTOR = NONE
UHPC_NM_CHANGED = NO
WEB_CHANGED = NO
```

The new GL+LL local-Mises maximum is evaluated from the continuous analytic harmonic stress field. The final R06 extrema are numerically stationary-point checked in this execution, but the high-degree finite-algebraic resultant certificate has not yet been emitted. Therefore the roots below are `BLIND PRE-CERTIFIED`, not yet final production roots. This distinction does not affect the moment-gate conclusion because the current moment deficits are orders of magnitude larger than the remaining R06 extremum tolerance.

---

# 1. BH actual registration recovered

The accepted 9-rib topology gives normalized transverse rib stations

\[
\frac{x_{rib}}b=\{-0.45,-0.3375,-0.225,-0.1125,0,0.1125,0.225,0.3375,0.45\}.
\]

The current BH family contract is `PBL bottom/top = 5/4`, with

\[
L_x=0.225b.
\]

Hence at the global transverse antinode (`x_model=0`, or theory `x/b=1/2`):

- the TOP/4-rib face has one full central local cell
  \[
  x/b\in[31/80,49/80]=[0.3875,0.6125];
  \]
- the BOTTOM/5-rib face has the antinode on the common boundary of two mirror cells
  \[
  x/b\in[11/40,1/2]
  \]
  and
  \[
  x/b\in[1/2,29/40].
  \]

The frozen local longitudinal wavelength is

\[
L_y=a/9=2b/9,
\]

so with the local pattern registered from the loaded end, the local cell containing the global longitudinal antinode `y/b=1/2` is

\[
y/b\in[4/9,6/9].
\]

This removes the previous practical registration blocker without using a favorable FEM phase. The bottom left/right cells are exact mirror images; only `hgamma` changes sign, while the normal coefficients and Airy energies are identical.

---

# 2. Exact harmonic method

All frequencies are stored as rational multiples of `pi/b` before evaluation:

\[
\alpha/\pi=1/b,
\qquad
k_x/\pi=\frac{80}{9b},
\qquad
k_y/\pi=\frac9b.
\]

Therefore harmonic collisions are merged algebraically rather than by floating-frequency comparison.

For each cell,

\[
h_x=\langle\psi_x\phi_x\rangle,
\quad
h_y=\langle\psi_y\phi_y\rangle,
\quad
h_\gamma=\langle\psi_x\phi_y+\psi_y\phi_x\rangle.
\]

The LL and GL Airy sources are

\[
S_{LL}=-(\phi_{,xx}\phi_{,yy}-\phi_{,xy}^2),
\]

\[
S_{GL}=-(\psi_{,xx}\phi_{,yy}+\phi_{,xx}\psi_{,yy}-2\psi_{,xy}\phi_{,xy}).
\]

Each finite Fourier source term is inverted exactly through the biharmonic multiplier

\[
(a^2+b^2)^{-2}.
\]

The complementary-energy bilinear form then yields

\[
U_A^{aug}=t_sE_s[K_A d^2+2K_{d\Delta}d\Delta+K_{\Delta\Delta}\Delta^2].
\]

No Gauss/Simpson/collocation/material-point rule is used.

---

# 3. Scale-free BH coefficients

Because all BH geometry is self-similar, the coefficients scale as

\[
h\sim b^{-2},\qquad K\sim b^{-4}.
\]

The exact dimensionless constants are:

| face/cell | `b^2 hx` | `b^2 hy` | `b^2 hgamma` | `b^4 KA` | `b^4 KdDelta` | `b^4 KDeltaDelta` |
|---|---:|---:|---:|---:|---:|---:|
| TOP, 4-rib central | 9.564070824136 | 9.564070824136 | 0 | 103860.659999837 | 2354.894386211 | 57.0765244960 |
| BOTTOM, 5-rib left | 8.972928383353 | 8.972928383353 | +1.167386193322 | 103860.659999837 | 2209.341510155 | 50.6709272133 |
| BOTTOM, 5-rib right | 8.972928383353 | 8.972928383353 | -1.167386193322 | 103860.659999837 | 2209.341510155 | 50.6709272133 |

`KA` exactly reproduces the frozen R02 LL coefficient. Thus

```text
R02_LL_REGRESSION = PASS
Q_U_GL_COEFFICIENTS = NONZERO
BOTTOM_MIRROR_INVARIANCE = PASS
```

---

# 4. Dimensional coefficients

## BH032 (`b=1600 mm`)

TOP:

\[
h_x=h_y=3.735965165678\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
h_\gamma\simeq0,
\]

\[
K_A=1.584787902830\times10^{-8}\;\mathrm{mm^{-4}},
\]

\[
K_{d\Delta}=3.593283670365\times10^{-10}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=8.709186477058\times10^{-12}\;\mathrm{mm^{-4}}.
\]

BOTTOM:

\[
h_x=h_y=3.505050149747\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
|h_\gamma|=4.560102317665\times10^{-7}\;\mathrm{mm^{-2}},
\]

\[
K_{d\Delta}=3.371187607048\times10^{-10}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=7.731769899488\times10^{-12}\;\mathrm{mm^{-4}}.
\]

## BH050 (`b=2500 mm`)

TOP:

\[
h_x=h_y=1.530251331862\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
h_\gamma\simeq0,
\]

\[
K_A=2.658832895996\times10^{-9}\;\mathrm{mm^{-4}},
\]

\[
K_{d\Delta}=6.028529628699\times10^{-11}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=1.461159027099\times10^{-12}\;\mathrm{mm^{-4}}.
\]

BOTTOM:

\[
h_x=h_y=1.435668541336\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
|h_\gamma|=1.867817909316\times10^{-7}\;\mathrm{mm^{-2}},
\]

\[
K_{d\Delta}=5.655914265997\times10^{-11}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=1.297175736660\times10^{-12}\;\mathrm{mm^{-4}}.
\]

---

# 5. Repaired local operator used in the blind solve

For each face

\[
d=U^2-A_0^2,
\qquad
\Delta=b[(q_0+q)U-q_0A_0].
\]

The mean R02 strains are

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

The local amplitude is the minimum-energy admissible real root of the exact augmented cubic.

For the R06 local-buckling-first radial projection, the repaired generalized radial state is

\[
q(\eta)=\eta q,
\qquad
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,
\]

with `q0,A0` retained as stress-free imperfections. This is required so that `eta=0` returns the undeformed imperfect reference with `Delta=0`; holding q fixed while scaling only face strain would not satisfy the repaired total kinematics.

The R06 return resultant remains the whole-width augmented R02 mean stress at first local Mises yield. No effective width is introduced.

---

# 6. Blind first-repair terminal equations

At the previously controlling BH station `s=1`:

\[
\kappa_x^g=\kappa_y^g=\pi^2q/b.
\]

The first-repair unknowns are

\[
(q,\varepsilon_x^0,\varepsilon_y^0).
\]

The equations solved are

\[
N_x^{sec}=N_x^d,
\]

\[
N_y^{sec}=N_y^d,
\]

and the first compressed UHPC face contact

\[
\varepsilon_y^0-\frac{t_c}{2}\kappa_y^g=-0.0035.
\]

At the resulting roots, the other x/y core endpoints remain strictly inside the compression-peak domain, so this is the active UHPC endpoint among the four finite core-face candidates.

The old independent terminal `kappa_x,kappa_y` and the two pointwise moment equalities are not used to select these roots.

---

# 7. Blind roots fixed before comparator reopening

| quantity | BH032 | BH050 |
|---|---:|---:|
| `q_u` | **0.001835902565** | **0.011215527128** |
| `P_g(q_u)` / MN | **13.04567021** | **17.98426079** |
| `kappa_x=kappa_y` / mm^-1 | 1.132477003e-5 | 4.427712636e-5 |
| `eps_x0` | +2.911229525e-4 | +5.468045298e-4 |
| `eps_y0` | -0.003262179830 | -0.002570180346 |
| UHPC `eps_y(top)` | -0.003024359659 | -0.001640360693 |
| UHPC `eps_y(bottom)` | **-0.003500000000** | **-0.003500000000** |
| TOP R06 `eta_y` | 0.513872737 | 0.823987466 |
| BOTTOM R06 `eta_y` | 0.434548109 | 0.390928947 |
| TOP condensed `U` / mm | 1.18593113 | 0.29111473 |
| BOTTOM condensed `U` / mm | 1.38791771 | 2.59513836 |

The membrane residuals at both fixed roots are below approximately `2e-8 N/mm` in the final numerical solve.

Both faces are on the R06 first-local-yield return by the eventual UHPC endpoint root. This is a consequence of the much larger q required once the gross section curvature is constrained to the actual global q-mode.

---

# 8. Blind section redistribution at the fixed roots

## BH032

\[
N_y^{UHPC}=-5594.0452\;\mathrm{N/mm},
\]

\[
N_y^{faces}=-2207.9848\;\mathrm{N/mm},
\]

\[
N_y^{web}=-295.5375\;\mathrm{N/mm}.
\]

Shares:

\[
\boxed{UHPC/steel/web=69.0830\%/27.2673\%/3.6497\%.}
\]

Mean longitudinal face stresses:

\[
\boxed{\sigma_{y,+}=-277.2772\;\mathrm{MPa}},
\]

\[
\boxed{\sigma_{y,-}=-274.7190\;\mathrm{MPa}}.
\]

## BH050

\[
N_y^{UHPC}=-4528.8643\;\mathrm{N/mm},
\]

\[
N_y^{faces}=-1675.6588\;\mathrm{N/mm},
\]

\[
N_y^{web}=-188.9410\;\mathrm{N/mm}.
\]

Shares:

\[
\boxed{UHPC/steel/web=70.8358\%/26.2089\%/2.9552\%.}
\]

Mean longitudinal face stresses:

\[
\boxed{\sigma_{y,+}=-199.5582\;\mathrm{MPa}},
\]

\[
\boxed{\sigma_{y,-}=-219.3566\;\mathrm{MPa}}.
\]

The old BH050 artificial upper-face unloading direction is therefore substantially reduced, but it is not eliminated at the eventual material endpoint.

---

# 9. Isolation of qU versus common-curvature effects

The same repaired terminal calculation was repeated with all GL coefficients set to zero while retaining the hard common curvature.

| case | common-curvature only / MN | + exact qU GL / MN | qU change |
|---|---:|---:|---:|
| BH032 | 13.12750540 | **13.04567021** | **-0.6234%** |
| BH050 | 18.02939520 | **17.98426079** | **-0.2503%** |

Thus, for this material-endpoint calculation:

\[
\boxed{qU\text{ is real and nonzero, but it is not the dominant Pu shift.}}
\]

The dominant change comes from removing the independent section-curvature freedom. This does not justify deleting qU; it identifies its quantitative role after the exact omitted term is restored.

---

# 10. Mandatory moment audit — decisive FAIL

The old initial-ABD Airy demand moments were not used as closure equations, but were evaluated after the roots were fixed.

## BH032

\[
M_x^{sec}=4277.96\;\mathrm N,
\qquad
M_x^d=17857.54\;\mathrm N,
\]

\[
\boxed{M_x^{sec}/M_x^d=0.23956.}
\]

\[
M_y^{sec}=1724.10\;\mathrm N,
\qquad
M_y^d=18143.03\;\mathrm N,
\]

\[
\boxed{M_y^{sec}/M_y^d=0.09503.}
\]

## BH050

\[
M_x^{sec}=23688.65\;\mathrm N,
\qquad
M_x^d=69924.51\;\mathrm N,
\]

\[
\boxed{M_x^{sec}/M_x^d=0.33877.}
\]

\[
M_y^{sec}=12528.23\;\mathrm N,
\qquad
M_y^d=70638.89\;\mathrm N,
\]

\[
\boxed{M_y^{sec}/M_y^d=0.17736.}
\]

The one-q projected antinode audit is also very large:

\[
r_{M_q}=\frac{\pi^2}{b}(r_{Mx}+r_{My}),
\]

with

\[
\boxed{r_{M_q}^{BH032}=-185.05\;\mathrm{N/mm}},
\]

\[
\boxed{r_{M_q}^{BH050}=-411.94\;\mathrm{N/mm}}.
\]

Therefore:

```text
COMMON_CURVATURE_KINEMATICS = PASS
EXACT_qU_LOCAL_AIRY = PASS
MEMBRANE_SECTION_CLOSURE = PASS
OLD_POINTWISE_MOMENT_CLOSURE_REMOVAL = PASS
FIRST_REPAIR_CURRENT_MOMENT_GATE = FAIL_HARD
```

This is the key result of the recalculation. Once the physically required q-curvature is enforced, the old initial-ABD Galerkin bending demand cannot remain disconnected from the current section bending resistance all the way to the UHPC endpoint. The calculation simply keeps increasing q/P until the material endpoint, even though the current section supplies only a small fraction of the bending work demanded by the frozen elastic front.

---

# 11. Comparator post-check — only after blind root freeze

Accepted comparators:

- BH032 FEM peak: `10.990480 MN`;
- BH050 equal-contract FEM peak: `12.591227 MN`.

Therefore the pre-certified first-repair endpoint roots give:

\[
\boxed{BH032:\ +18.70\%},
\]

\[
\boxed{BH050:\ +42.83\%}.
\]

This is a deterioration in Pu prediction and is **not** repaired by adjusting qU coefficients, R06, UHPC strength, or web geometry.

Mechanism comparison remains informative:

- BH032 new share = `69.08/27.27/3.65%`; accepted FEM = approximately `66.49/28.95/4.56%`;
- BH050 new share = `70.84/26.21/2.96%`; accepted equal-contract FEM = approximately `55.80/40.61/3.58%`.

For BH050 the upper face is no longer driven to the extreme old theory unloading state (`-75.7 MPa`); the repaired endpoint gives about `-199.6 MPa`, but the branch continues far past the accepted FE peak because the current bending resistance is not fed back into global q equilibrium.

Thus a closer local stress direction does not validate the endpoint Pu architecture.

---

# 12. Decision

The requested coefficient calculation and direct BH032/BH050 recalculation are complete.

The result is not a new production Pu formula. It is a **hard fail of the minimal endpoint closure** and a clean localization of the next missing relation.

The next theory step must be:

\[
\boxed{\text{current section bending resultants}\rightarrow\text{the same global }q\text{ Galerkin equilibrium}.}
\]

This must be derived over one complete representative halfwave, including the common twisting-curvature term away from the antinode. It must replace the frozen elastic bending part of the global q equation by its work-conjugate current resultant contribution while retaining the already repaired:

```text
q -> common curvature
qU GL local Airy
R02 LL terms once only
UHPC directional N-M unchanged
web unchanged
R06 concept unchanged pending finite-algebraic GL+LL max certificate
zero formal spatial quadrature
```

Do **not** restore independent `kappa_x,kappa_y`; do **not** tune qU; do **not** repair the result by changing UHPC material parameters.

The antinode scalar `r_Mq` above is only an audit indicator. It is not promoted as the production global residual because the exact full-halfwave Galerkin work also contains spatial variation and twisting curvature.
