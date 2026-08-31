# NZ-SCCM — Fully parameter-driven zero-iteration Excel R03 checkpoint

**Date:** 2026-08-31  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Role:** implementation checkpoint / no new material law / no comparator calibration

## 1. Decision

Formal Excel execution is no longer based on Newton, Goal Seek, Solver, loading increments, or path iteration. The implementation identity is:

```text
raw specimen parameters
-> explicit stiffness compiler
-> finite integer mode enumeration
-> explicit Airy coefficient compiler
-> explicit R02 polynomial compiler
-> all-root algebraic enumeration + active-set selection
-> finite-resultant gates where applicable
```

Low-degree polynomial roots are evaluated in closed form. For degree > 4, the formal object is a finite polynomial/root set (RootOf/resultant identity), not an iterative load path.

## 2. R03 Excel artifact

Local artifact name:

`NZSCCM_钢壳UHPC_全参数驱动_零迭代显式Excel_R03_20260831.xlsx`

The workbook contains:

- `00_CONTROL` — formal zero-iteration rules and claim boundary;
- `01_INPUT` — single raw-input page;
- `02_STIFFNESS` — raw geometry/material -> A/D formulas;
- `03_MODE_AIRY` — finite integer mode enumeration and automatic `Pcr,Kx,G,C,Jx,Jy` compiler;
- `04_AIRY_STATE` — arbitrary-q direct structural state calculator;
- `05_CAPACITY_STATE` — historical BH050 capacity coordinates, guarded so they cannot survive a raw-input change;
- `06_R02_LL` — qU-off production-baseline R02 local polynomial compiler and explicit cubic all-root active set;
- `07_R06_GATE` — parameter-driven elastic local-buckling classification and explicit resultant boundary for eta_y;
- `08_UHPC_EXACT` — exact Zhang UHPC mathematical-class ledger;
- `09_TERMINAL_COMPILER` — terminal elimination status;
- `10_OUTPUT` — automatic outputs with anti-mixing guards;
- `11_BH_SCENARIOS` — BH005/BH010/BH020/BH032/BH050 upstream parameter-propagation check;
- `12_SOURCES` — theory/source identities.

## 3. Fully parameter-driven blocks achieved

For the current qU-off common-R06 production baseline, the workbook now recomputes from raw inputs:

```text
rho_w
A11,A22,A12,A66
Dx,Dy,Dmu,D66,H
m*, ell, alpha, beta, Pcr
Kx,G,C,Jx,Jy
R02 kx,ky,cx,cy,Ds,Kb,KA,Qs,Gs
R02 depressed cubic coefficients B3,B1,B0
all real cubic roots + U=0 KKT boundary candidate
R06 sigma_cr^E and branch classification
```

No BH050 frozen `A/D` or Airy coefficients are needed for these blocks.

BH050 regression checks from formulas reproduce:

```text
m*   = 2
Pcr  = 19.581877236731064 MN
Kx   = 4.2729259661361715e6 N/mm
G    = 4.400171479082514e6 N/mm
C    = 1.0841371806523357e10 N
Jx   = 6.234616244717026e6 N
Jy   = 6.298311709061200e6 N
R06 branch = LOCAL_BUCKLING_FIRST
```

The A/D terms reproduce the source-audited BH050 values to floating precision.

## 4. R02 execution sign convention

To reproduce the frozen 20260825 common-R06 qU-off BH050 cubics, the workbook uses the execution convention

\[
d=U^2-A_0^2,
\qquad m_x=e_x+c_xd,
\qquad m_y=e_y+c_yd.
\]

Then

\[
B_3=4t_sE_sK_A+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2),
\]

\[
B_1=K_b-A_0^2B_3+2t_sQ_s(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y),
\]

\[
B_0=-A_0K_b.
\]

This is explicitly versioned because later ledgers use a different compression/strain bookkeeping sign. Do not mix sign conventions without transformation.

Using the historical BH050 capacity state only as a regression input, the explicit cubic compiler reproduces approximately:

```text
upper U = 0.169266886 mm
lower projected U = 2.939845915 mm
```

The small sub-nanometre differences from the archived roots are caused by rounded historical state coordinates stored in the workbook, not an iterative solve.

## 5. Mandatory anti-mixing guard

The historical BH050 capacity-contact state

```text
q = 0.004772819645833164
eps_x0 = 2.820431413e-5
kappa_x_cap = 4.402758337803803e-5 1/mm
eps_y0 = -0.00213545799
kappa_y_cap = 6.497819104663830e-5 1/mm
```

is not a raw-input function and is not the geometric curvature from q. The R03 workbook fingerprints the BH050 raw input. If geometry/material/local-cell inputs are changed, historical `q_terminal` and candidate `Pu` are invalidated and the workbook returns:

```text
RECOMPILE_TERMINAL_ROOT
```

rather than silently mixing a new specimen with the old BH050 terminal root.

## 6. Exact mathematical boundary discovered

The remaining obstacle to arbitrary-input -> automatic `Pu` is not Excel formula propagation.

The exact current UHPC operator uses the Zhang backbone

\[
r_U=\frac{E_c}{E_c-f_c/\varepsilon_{c0}},
\qquad
g_a(x)=\frac{r_Ux}{r_U-1+x^{r_U}},
\]

where `r_U` is generally non-integer. Exact thickness primitives contain hypergeometric `2F1`; the descending source branch contains `atan/log`. Hence the exact section terminal equations are generally algebraic-transcendental, not a finite polynomial system in q.

Therefore under the unchanged exact UHPC source operator it is mathematically incorrect to claim a universal finite polynomial

\[
R_q(q)=0
\]

for arbitrary raw material parameters.

This is separate from the R06 local gate. R06 finite Fourier/local-Mises conditions are finite polynomial/resultant objects; their general interior resultant can be high degree and should be retained as a finite all-root/RootOf object, not solved by path iteration.

## 7. Current output identity

R03 therefore has two different readiness levels:

```text
RAW -> A/D -> MODE -> AIRY -> R02 POLYNOMIAL -> R06 BRANCH
= FULLY PARAMETER DRIVEN / ZERO ITERATION

RAW -> UNIQUE PHYSICAL Pu
= NOT YET FROZEN
```

The second line is blocked by both:

1. exact non-polynomial UHPC section primitives under the current source law; and
2. the still-open `DEFORMATION_COMPATIBLE_STRUCTURAL_TERMINAL` rule.

Neither block may be hidden by Solver/Newton, empirical fitting, old BH050 roots, or FEM/test calibration.

## 8. Next theory task if universal zero-iteration Pu remains mandatory

The next legitimate task is not an Excel Solver implementation. It is to choose and source-freeze an algebraic UHPC compiler that preserves the accepted current material operator to the required accuracy/identity, then derive the full section/terminal resultant and finite admissible q-root set under the finally frozen deformation-compatible terminal rule.

Until then, R03 is the correct guarded parameter-driven explicit workbook: every frozen algebraic upstream block changes automatically with specimen parameters, while unresolved terminal physics cannot silently return a false Pu.
