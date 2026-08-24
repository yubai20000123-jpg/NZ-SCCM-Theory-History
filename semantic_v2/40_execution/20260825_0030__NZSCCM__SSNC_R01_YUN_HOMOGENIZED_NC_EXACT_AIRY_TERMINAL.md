# NZ-SCCM — SSNC-R01 Yun homogenized steel-shell + ordinary-concrete exact-section Airy terminal

**Time:** 2026-08-25 00:30 +08:00  
**Status:** `EXECUTED / USER-AUTHORIZED OPTION-H REOPEN / Y-NORMAL SOURCE CLOSURE PASS / Z0-Z6 DIAGNOSTIC COMPLETE / NOT USER-LOCKED`

## 0. Decision first

The 2026-08-24 R20-1 blocker is **closed for the current axial y-normal steel-shell-concrete terminal** without reopening the global material virtual-work route.

The missing bridge is supplied directly by Yun Chapter 5's effective-width definition, not by an arbitrary point-cut or area-average rule:

\[
\boxed{\eta_Y=\frac{b_e}{b}=\frac{\sigma_u}{f_y}}.
\]

Yun Chapter 2 determines the first positive local amplitude `Au` at which the maximum plate stress reaches `fy`; Chapter 5 then defines the corresponding average ultimate stress `sigma_u` and effective width. Therefore the terminal steel plate can be homogenized per gross strip width as

\[
\boxed{f_{yc,Y}=\sigma_u=\eta_Y f_y}
\]

on a compression-active face. This quantity is already a source-defined local-to-resultant homogenization and depends only on local plate geometry/material/imperfection. It does **not** require the historical `(D,alpha)` variables.

```text
STRUCTURAL_BACKBONE = MARGUERRE_AIRY_EXPLICIT
GLOBAL_VIRTUAL_WORK_CLOSURE = NOT_USED
D15 = NOT_USED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
R20_1_OPTION_H_SOURCE_CLOSURE = PASS_FOR_Y_NORMAL_TERMINAL
FULL_BIAXIAL_STEEL_TERMINAL = NOT_CLAIMED
```

The phase label is `SSNC-R01`; no inference is tied to the historical number R20.

---

## 1. Frozen Airy demand retained exactly

No structural equation is altered. For the Z family,

\[
Q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ,
\]

\[
n_d(s,q)=\frac{P(q)}{b}+GQ(1-2s^2),
\qquad
m_d(s,q)=J_yqs.
\]

The script regenerates the R07 coefficients from raw geometry/material data. The regenerated values are identical to the previous forward-generated R07 values to printed precision.

---

## 2. Yun source chain used for the new terminal

Source: `考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`.

Relevant source equations are:

- Eq. (2-32), repeated as Eq. (5-19): average postbuckling load/stress as a function of local amplitude `A`;
- Eq. (2-37), repeated as Eq. (5-18): maximum axial compression in the local steel plate;
- Eq. (2-38), repeated as Eq. (5-20): first positive `A=Au` when maximum compression reaches `fy`;
- Eq. (2-40)/(5-21): average ultimate stress at `Au`;
- Eqs. (5-22)–(5-23): effective-width definition.

For local half-wave aspect ratio

\[
r=\frac{a/m}{b_s},
\]

Yun gives

\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

and the source `kp` rational polynomial. For the current 200-mm strips, `r=1`, hence

\[
\boxed{k_{cr}=32/3=10.6666666667},
\qquad
\boxed{k_p=42.64}.
\]

The code also verifies the source coefficient symmetry

\[
k_{cr}(r)=k_{cr}(1/r),\qquad k_p(r)=k_p(1/r),
\]

with maximum numerical discrepancy

\[
\boxed{5.684\times10^{-14}}.
\]

This is the appropriate x/y coefficient-swap gate. The maximum-stress coefficient itself is loading-directional and is not incorrectly asserted to be a scalar invariant under axis swap.

---

## 3. Finite cubic elimination of the Yun local amplitude

Write the Yun average compression as

\[
\bar\sigma(A)=c_1\frac{A}{A+A_0}+c_2(A^2+2A_0A),
\]

where

\[
c_1=C_\sigma k_{cr},
\qquad
C_\sigma=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)b_s^2},
\]

\[
c_2=C_\sigma\frac{k_p(1-\nu_s^2)}{t_s^2}.
\]

From Yun Eq. (2-37)/(5-18), the difference between maximum local compression and average compression is

\[
\Delta\sigma(A)=c_3(A^2+2A_0A),
\]

with

\[
c_3=\frac{E_s\pi^2}{b_s^2}K_{max}(r),
\]

\[
K_{max}(r)=
\frac{3}{2r^2}
+\frac{4r^2}{(r^2+1)^2}
-\frac{8r^2}{(4r^2+1)^2}
+\frac{2r^2}{(r^2+4)^2}.
\]

The first-yield condition

\[
\bar\sigma(A_u)+\Delta\sigma(A_u)=f_y
\]

is exactly reduced to the cubic

\[
\boxed{
(c_2+c_3)A^3
+3A_0(c_2+c_3)A^2
+\left[2A_0^2(c_2+c_3)-f_y+c_1\right]A
-f_yA_0=0.
}
\]

The formal model therefore requires only the finite real roots of one cubic; the first positive root is `Au`. There is no spatial integration and no local load stepping.

For the current `bs=200 mm`, `ts=4 mm`, `A0=bs/1600=0.125 mm`:

| fy MPa | Au mm | sigma_u MPa | eta=sigma_u/fy | local reduction |
|---:|---:|---:|---:|---:|
|235|0.051082181150|233.233271154|0.992482004910|0.75180%|
|355|0.096051511208|351.181785119|0.989244465125|1.07555%|
|460|0.156191431294|452.712083706|0.984156703708|1.58433%|

This modest reduction is a source consequence; no fitting factor is introduced.

---

## 4. Why this closes the two R20-1 blockers

### Blocker A: local 2D Yun field -> terminal resultant

R20-1 correctly found that the older ideal-EP Yun current field admits several non-equivalent reductions: point cut, subpanel average, phase average, effective width, etc.

Chapter 5 now supplies a source-backed choice explicitly:

\[
\boxed{b_e/b=\sigma_u/f_y}.
\]

Therefore the current route deliberately selects **source-defined effective-width homogenization**. It does not claim the older pointwise 2026-08-18 current field itself is uniquely projected.

### Blocker B: missing `(D,alpha)`

The Chapter-5 terminal depends on `Au`, and `Au` is the first positive root of the cubic above. Hence

\[
\boxed{(E_s,\nu_s,t_s,b_s,A_0,f_y,r)\mapsto A_u\mapsto\sigma_u}
\]

is closed independently of `(D,alpha)`.

Thus the accepted Airy demand remains a function of `q`, and the terminal material capacity is separately source-closed.

---

## 5. No-double-counting rule

The new Yun quantity is used **only on the terminal steel-capacity side**:

```text
Pcr, C, G, Jy = unchanged Airy structural-demand coefficients
Yun local postbuckling = not fed back into Airy stiffness
Yun effective width = terminal compression-face steel resultant only
```

Thus the global Airy postbuckling field and the local 200-mm Yun subpanel field do not both contribute energy/stiffness to the same structural equation.

For the generalized plastic terminal used only as an isolation test, set

\[
f_{yc}=\sigma_u,\qquad f_{yt}=f_y,\qquad f_{yw}=f_y.
\]

With

\[
a_c=(1-\rho_w)f_c,
\quad h_c=t_c/2,
\quad z_f=h_c+t_s/2,
\]

the exact asymmetric face-strength envelope becomes

\[
D=a_c+2\rho_wf_y,
\]

\[
N_0=(a_c+\rho_wf_y)t_c+(f_{yc}-f_y)t_s,
\]

\[
N_p=(a_c+\rho_wf_y)t_c+2f_{yc}t_s.
\]

For `n<=N0`,

\[
z_n=\frac{a_ch_c+(f_{yc}-f_y)t_s-n}{D},
\]

\[
M_A(n)=\frac{D}{2}(h_c^2-z_n^2)+(f_{yc}+f_y)t_sz_f.
\]

For `N0<=n<=Np`,

\[
x=\frac{n-N_0}{f_{yc}+f_y},
\]

\[
M_B(n)=\frac{f_{yc}+f_y}{2}(t_s-x)(2h_c+t_s+x).
\]

Setting `fyc=fy` reduces identically to R07.

---

## 6. Mandatory R07 regression

Before using the modification, the code sets `fyc=fy` and regenerates all seven R07 roots without comparator information.

```text
R07_MAX_Q_ABS_ERR = 4.179e-13
R07_MAX_PU_ABS_ERR_MN = 4.445e-10
R07_BASELINE_REGRESSION = PASS
```

This establishes that any subsequent change comes from the new terminal material law rather than an accidental change to Airy demand or root selection.

If only the Yun homogenized face cap is inserted into the old plastic concrete terminal, the shifts are small:

|Case|R07 Pu MN|Yun-only Pu MN|shift|
|---|---:|---:|---:|
|Z0|37.825707|37.680647|-0.3835%|
|Z1|24.714129|24.653508|-0.2453%|
|Z2|42.959011|42.690438|-0.6252%|
|Z3|46.495652|46.355728|-0.3009%|
|Z4|70.265719|70.060586|-0.2919%|
|Z5|14.118194|14.059585|-0.4151%|
|Z6|56.379421|56.189447|-0.3370%|

So Yun by itself is not being used as an artificial large correction.

---

## 7. Ordinary-concrete exact-section insertion

The ordinary concrete terminal is then changed from the R07 rectangular plastic block to the already-developed exact affine-section material kernel:

- Saenz compression branch;
- postpeak compression and residual branch;
- elastic/Foster tension and residual branch;
- exact branch primitives;
- exact finite branch-front cuts in thickness.

No thickness quadrature is used.

For the y-normal terminal define

\[
\lambda(z)=-1+\kappa(z-h_c),
\]

so the compression-side concrete face satisfies the existing peak-compression terminal condition

\[
\lambda(h_c)=-1.
\]

Concrete, equivalent web steel, and the two external steel faces are integrated into the same per-unit-width section resultants

\[
n_c(\kappa),\qquad m_c(\kappa),
\]

with exact derivatives

\[
n_c'(\kappa),\qquad m_c'(\kappa).
\]

The external steel compression cap is `sigma_u` from Yun; tensile steel retains `fy`. The 2% equivalent longitudinal web retains the existing ideal-EP law.

---

## 8. New finite scalar terminal reduction

This step also removes the need to scan the Airy control coordinate `s`.

Define

\[
F(\kappa,q)=n_c(\kappa)-\frac{P(q)}b
-GQ\left[1-2\left(\frac{m_c(\kappa)}{Jq}\right)^2\right].
\]

The control coordinate is recovered only after the section state:

\[
\boxed{s=\frac{m_c(\kappa)}{Jq}}.
\]

The complete finite candidate set is:

### Endpoint `s=0`

`kappa=0`, `m_c=0`; solve one scalar axial equation in `q`.

### Endpoint `s=1`

\[
\boxed{q=\frac{m_c(\kappa)}J}
\]

is substituted directly into `F=0`, leaving one scalar equation in `kappa`.

### Interior stationary controller

At a minimum admissible `q`, `dq/dkappa=0`. Since

\[
F_\kappa
=n_c'
+4GQ\frac{m_c}{Jq}\frac{m_c'}{Jq}=0,
\]

let

\[
K(\kappa)=-\frac{n_c'J^2}{4Gm_cm_c'}.
\]

Because

\[
\frac{Q}{q^2}=1+\frac{2q_0}{q}=K,
\]

we obtain the explicit elimination

\[
\boxed{q(\kappa)=\frac{2q_0}{K(\kappa)-1}}.
\]

Substitution into `F=0` again leaves **one scalar equation in the section slope `kappa`**.

Therefore the primary SSNC-R01 terminal is a finite set of scalar closed equations; it does not use a spatial control-point grid.

---

## 9. Primary Z0-Z6 diagnostic — NC exact section + Yun terminal

The new prediction was fixed before opening the Zhou comparator.

|Case|control|s|q|Pu MN|shift vs R07|error vs Zhou|
|---|---|---:|---:|---:|---:|---:|
|Z0|s=1|1.000000|0.003132300908|35.890695|-5.116%|-2.855%|
|Z1|s=1|1.000000|0.004418628214|23.125147|-6.429%|-2.514%|
|Z2|s=1|1.000000|0.003378267974|37.508331|-12.688%|-8.990%|
|Z3|s=1|1.000000|0.004093708661|43.656035|-6.107%|-1.499%|
|Z4|s=1|1.000000|0.002252704576|66.629404|-5.175%|-3.909%|
|Z5|s=1|1.000000|0.000255597302|13.951816|-1.178%|-4.971%|
|Z6|interior|0.431421|0.013281405459|54.522183|-3.294%|+10.175%|

Against Zhou:

\[
\boxed{\text{mean signed}=-2.0803\%,\qquad MAE=4.9875\%.}
\]

This is essentially the same overall MAE as R07 (`4.973%`) but with materially different error distribution. In particular:

- Z6 drops from `+13.93%` to `+10.18%`;
- Z2 becomes the clearest new low-side outlier at `-8.99%`;
- Z0/Z1/Z3/Z4 cluster within about `1.5–3.9%` low;
- the Yun face correction itself is only about `0–0.46%` on top of the NC exact-section result, so the larger shifts arise from replacing the old plastic concrete block by the ordinary-concrete current section law.

No parameter was fitted to Zhou.

---

## 10. External literature candidates tried in parallel

Two additional explicit/closed-form families were re-checked as candidate future extensions:

1. Ueda–Rashed–Paik, *Buckling and Ultimate Strength Interactions of Plates and Stiffened Plates under Combined Loads (1st Report): In-plane Biaxial and Shearing Forces*, and the later Marine Structures development. Their explicit interaction family remains a candidate for biaxial/shear steel terminal closure.
2. Ishibashi–Shiomitsu–Tatsumi–Fujikubo, *Simplified ultimate strength estimation method of rectangular plates under combined loads*, Marine Structures 95 (2024) 103592, together with its earlier open precursor. This family remains a candidate for combined biaxial/shear extension.

Their exact equation sets have not yet been frozen into the repository in this execution, so they are not silently substituted into SSNC-R01.

The current y-normal steel-shell-concrete path no longer depends on them for closure because Yun Chapter 5 already gives the needed source-backed homogenized axial terminal.

---

## 11. Status and next technical question

```text
SSNC_R01 = EXECUTED
YUN_CH2_CH5_SOURCE_EXTRACTION = PASS
YUN_LOCAL_AMPLITUDE_FINITE_CUBIC = PASS
YUN_HOMOGENIZED_TERMINAL = PASS
KCR_KP_AXIS_SWAP_GATE = PASS
R07_BASELINE_REPRODUCTION = PASS
NC_EXACT_SECTION_RECOVERY = PASS
AIRY_NY_MY_DIRECT_TERMINAL = PASS
FINITE_SCALAR_CONTROL_ELIMINATION = PASS
Z0_Z6_DIAGNOSTIC = COMPLETE
COMPARATOR_IN_ROOT_SELECTION = 0
NEW_FITTED_FACTOR = 0
FULL_BIAXIAL_STEEL_TERMINAL = OPEN / NOT REQUIRED FOR THIS Y-NORMAL GATE
USER_ACCEPTANCE = PENDING
```

The main new diagnostic is no longer a source-closure failure. The remaining scientific question is whether the ordinary-concrete peak-compression terminal used here should be retained for steel-shell concrete, or whether the source-consistent steel-shell terminal should continue farther on the concrete postpeak branch before declaring `Pu`. That question can now be studied **inside the closed Airy + Yun + exact-section framework** without rebuilding the structural theory.
