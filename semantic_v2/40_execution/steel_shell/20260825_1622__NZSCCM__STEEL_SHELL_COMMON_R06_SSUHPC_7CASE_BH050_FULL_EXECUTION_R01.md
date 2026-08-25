# NZ-SCCM — STEEL-SHELL COMMON R06: SSUHPC seven-case validation + BH050 full blind execution R01

**Time:** 2026-08-25 16:22 +08:00  
**Parent:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Common R06:** `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`  
**Comparator in BH050 root solve:** `0`  
**Formal spatial sampling:** `0`  
**Formal spatial quadrature:** `0`  
**Material points:** `0`  
**Effective width/area:** `0`

---

## 0. Execution discipline

BH050 was solved with the **same frozen common R06 operator** used for T360 and BH032. No new BH050-specific method, coefficient, fit, or comparator-dependent root selection was introduced.

Blind order:

```text
1. freeze common R06
2. recover BH050 geometry/material input from the already-fixed SSUHPC model contract
3. compute initial full-composite ABD and integer elastic mode
4. classify the local steel cell from sigma_cr^E versus fy
5. solve the same 5-equation terminal section system as T360/BH032
6. certify the final R02/R06 local extrema by the complete finite algebraic candidate set
7. freeze BH050 root
8. only then reopen the already-existing Abaqus comparator 12.2198 MN
9. assemble the seven-case R06 table
```

---

# 1. Common R06 identity

For every steel face:

\[
\sigma_{cr,s}^{E}\ge f_y
\Rightarrow
R06\equiv R04,
\]

while

\[
\sigma_{cr,s}^{E}<f_y
\Rightarrow
\text{R02 local-buckling-first branch}.
\]

For the local-buckling-first branch, along the current physical face-strain ray

\[
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,
\]

R02 is re-condensed and the first local yield boundary satisfies

\[
\max_{[-1,1]^2}\Phi(u,v;\eta_y)=f_y^2,
\]

with

\[
\Phi=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2.
\]

The face returned to the section is the **whole-width R02 mean resultant at that local-yield state**. No effective width or effective area is used.

---

# 2. BH050 frozen input

Global member geometry:

```text
b = 2500 mm
a_phys = 5000 mm
tc = 42 mm
ts = 4 mm
zf = tc/2 + ts/2 = 23 mm
9 longitudinal webs
net web height = 37 mm
Aw = 9*4*37 = 1332 mm^2
rho_w = Aw/(b*tc) = 0.0126857142857143
q0 = 0.0025
s = 1
```

Material parameters:

```text
steel: Es = 206000 MPa, nu_s = 0.30, fy = 355 MPa
UHPC: Ec = 43400 MPa, nu_c = 0.20, fc = 141.1 MPa, eps_c0 = 0.0035
UHPC tension: fct = 4.513133983249735 MPa, eps_t0 = 0.001, mt = 0.4418
```

BH-family local steel cell:

```text
Lx = 0.225*b = 562.5 mm
local longitudinal halfwave count = 9
Ly = a_phys/9 = 555.555555555556 mm
A0 = Lx/1600 = 0.3515625 mm
```

---

# 3. Initial full-composite ABD

Using

\[
Q^{11}=E/(1-\nu^2),\qquad
Q^{12}=\nu Q^{11},\qquad
Q^{66}=E/[2(1+\nu)],
\]

and the frozen two-skin + distributed-UHPC + longitudinal-web formulas gives

\[
A_{11}=3.685652010989011\times10^6\ \mathrm{N/mm},
\]
\[
A_{22}=3.795408810989011\times10^6\ \mathrm{N/mm},
\]
\[
A_{12}=9.182293032967034\times10^5\ \mathrm{N/mm},
\]
\[
A_{66}=1.383711353846154\times10^6\ \mathrm{N/mm}.
\]

With the steel-face parallel-axis term included exactly once:

\[
D_x=1.236003299827839\times10^9\ \mathrm{N\,mm},
\]
\[
D_y=1.252137549427839\times10^9\ \mathrm{N\,mm},
\]
\[
D_\mu=3.432434438483517\times10^8\ \mathrm{N\,mm},
\]
\[
D_{66}=4.463799279897436\times10^8\ \mathrm{N\,mm},
\]
\[
H=D_\mu+2D_{66}=1.236003299827839\times10^9\ \mathrm{N\,mm}.
\]

---

# 4. Elastic mode and Marguerre–Airy coefficients

The integer mode scan gives

| m | Pcr,m / MN |
|---:|---:|
| 1 | 30.5130828854 |
| 2 | **19.5818772367** |
| 3 | 23.0500697915 |
| 4 | 30.7519408767 |
| 5 | 41.4350738286 |
| 6 | 54.7904307691 |

Thus

\[
\boxed{m_*=2},\qquad \ell=a/m_*=2500\ \mathrm{mm},
\]

\[
\boxed{P_{cr}=19.5818772367311\ \mathrm{MN}}.
\]

The unchanged Airy coefficients are

\[
K_x=4.272925966136171\times10^6\ \mathrm{N/mm},
\]
\[
G=4.400171479082513\times10^6\ \mathrm{N/mm},
\]
\[
C=1.0841371806523354\times10^{10}\ \mathrm{N}
=10841.3718065234\ \mathrm{MN},
\]
\[
J_x=6.234616244717026\times10^6\ \mathrm N,
\qquad
J_y=6.298311709061200\times10^6\ \mathrm N.
\]

---

# 5. BH050 local steel classification

For the R02/Yun local elastic criterion:

\[
r=L_y/L_x=0.987654320987654,
\]

\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2}=10.6691358977290,
\]

\[
\sigma_0=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}
=9.41497684974175\ \mathrm{MPa},
\]

hence

\[
\boxed{\sigma_{cr,s}^{E}=100.449667483867\ \mathrm{MPa}<f_y=355\ \mathrm{MPa}}.
\]

Therefore BH050 enters exactly the same

```text
R06_LOCAL_BUCKLING_FIRST
```

branch as T360/BH032.

---

# 6. Blind BH050 terminal root

At `s=1`, solve the same five equations

\[
N_x^{sec}=N_x^d,
\quad
N_y^{sec}=N_y^d,
\quad
M_x^{sec}=M_x^d,
\quad
M_y^{sec}=M_y^d,
\]

plus the already-frozen first UHPC compression-peak contact

\[
\varepsilon_y(-t_c/2)=-0.0035.
\]

The blind solution, before reopening any comparator, is

\[
\boxed{q_u=0.004772819645833164},
\]

\[
\boxed{\varepsilon_x^0=+2.820431413\times10^{-5}},
\]

\[
\boxed{\kappa_x=4.402758337803803\times10^{-5}\ \mathrm{mm}^{-1}},
\]

\[
\boxed{\varepsilon_y^0=-0.00213545799},
\]

\[
\boxed{\kappa_y=6.497819104663830\times10^{-5}\ \mathrm{mm}^{-1}}.
\]

The added global amplitude is

\[
bq_u=11.9320491146\ \mathrm{mm}.
\]

The active UHPC face checks are

\[
\varepsilon_y(+21)=-0.000770915976,
\qquad
\boxed{\varepsilon_y(-21)=-0.0035},
\]

\[
\varepsilon_x(+21)=+0.000952783565,
\qquad
\varepsilon_x(-21)=-0.000896374937,
\]

so no other UHPC face has crossed the frozen compression peak.

---

# 7. Explicit load evaluation

\[
Q_q=q(q+2q_0)=4.664390560081682\times10^{-5}.
\]

The linear/postbuckling asymptote contribution is

\[
P_{cr}\frac{q}{q+q_0}=12.8506924314162\ \mathrm{MN},
\]

and the nonlinear Airy contribution is

\[
CQ_q=0.505683923126832\ \mathrm{MN}.
\]

Therefore

\[
\boxed{P_u^{BH050,R06}=13.3563763545430\ \mathrm{MN}}.
\]

Demand resultants are

\[
N_x^d=+199.305955403735\ \mathrm{N/mm},
\]
\[
N_y^d=-5137.30935871948\ \mathrm{N/mm},
\]
\[
M_x^d=29756.6988970160\ \mathrm N,
\qquad
M_y^d=30060.7058605883\ \mathrm N.
\]

At `s=1`, the terms entering the y-demand are

\[
P/b=5342.55054181721\ \mathrm{N/mm},
\qquad
GQ_q=205.241183097731\ \mathrm{N/mm}.
\]

---

# 8. Exact UHPC and longitudinal-web resultants

The frozen zero-thickness-quadrature UHPC primitives give

\[
N_x^U=-313.907222827064\ \mathrm{N/mm},
\qquad
M_x^U=6458.07382899297\ \mathrm N,
\]

\[
N_y^U=-3775.20864050157\ \mathrm{N/mm},
\qquad
M_y^U=16306.0755102416\ \mathrm N.
\]

The exact ideal-EP longitudinal-web integration gives

\[
N_y^w=-170.904638861559\ \mathrm{N/mm},
\qquad
M_y^w=293.915178045378\ \mathrm N,
\]

with

\[
N_x^w=M_x^w=0.
\]

No thickness quadrature is used for either constituent.

---

# 9. Upper steel face

At `z=+23 mm`, the physical face strain is

\[
(\varepsilon_x,\varepsilon_y)_+
=(+0.001040838732,-0.000640959594).
\]

R02 uses

\[
B_3U^3+B_1U+B_0=0
\]

with the numerical coefficients

\[
B_3=0.0193334947724247,
\quad
B_1=+0.0795041275744123,
\quad
B_0=-0.0135511779774194.
\]

The only admissible nonnegative real amplitude root is

\[
\boxed{U_+=0.169266885792264\ \mathrm{mm}}.
\]

The R02 mean physical stress is

\[
\bar{\boldsymbol\sigma}_+
=(+190.77460961,-75.74344920,0)\ \mathrm{MPa}.
\]

Complete finite-algebraic enumeration of the degree-6-or-lower local Mises polynomial gives

\[
\boxed{\max\sigma_{VM,loc,+}=239.872701525\ \mathrm{MPa}<355\ \mathrm{MPa}},
\]

at an `edge-u` stationary candidate approximately

\[
(u,v)=(-1,0.69204902235).
\]

Therefore the upper face remains uncapped R02. Its whole-width resultant is

\[
\mathbf N_+
=(+763.09843842,-302.97379680)\ \mathrm{N/mm}.
\]

---

# 10. Lower steel face and R06 local-yield projection

At `z=-23 mm`, the full physical face strain is

\[
(\varepsilon_x,\varepsilon_y)_-
=(-0.000984430104,-0.003629956382).
\]

If R02 were evaluated at the full unprojected strain, it would give

\[
U_{-,full}=4.99939554164\ \mathrm{mm},
\]

\[
\bar{\boldsymbol\sigma}_{-,full}
=(-124.92888832,-539.50433643,0)\ \mathrm{MPa},
\]

\[
\sigma_{VM,mean}=489.154862154\ \mathrm{MPa},
\]

and the complete local field reaches

\[
\max\sigma_{VM,loc}=960.317703343\ \mathrm{MPa}.
\]

Thus the mean-R04 cap is far too late for this local-buckling-first face.

R06 solves the first radial local-yield condition and obtains

\[
\boxed{\eta_{y,-}=0.384465068379632}.
\]

The projected strain is therefore

\[
(\varepsilon_x,\varepsilon_y)_{-,y}
=(-0.000378478987,-0.001395591429).
\]

At this state the R02 amplitude cubic becomes

\[
0.0193334947724247U^3
-0.162483993492182U
-0.0135511779774194=0.
\]

Its three real roots are approximately

\[
U=2.93984591448,\quad -2.85637664,\quad -0.08346928\ \mathrm{mm},
\]

so the unique admissible nonnegative root is

\[
\boxed{U_{-,y}=2.93984591447788\ \mathrm{mm}}.
\]

The corresponding **whole-width mean** stress is

\[
\boxed{
\bar{\boldsymbol\sigma}_{-,R06}
=(-62.47131505,-222.05557064,0)\ \mathrm{MPa}.
}
\]

Its mean Mises stress is only

\[
\sigma_{VM,mean}=198.341216453\ \mathrm{MPa},
\]

showing directly why a mean-Mises cap would miss the local event.

## 10.1 Finite-algebraic local maximum certificate

For this active projected state, the explicit polynomial

\[
\Phi(u,v)=\sum c_{ij}u^iv^j
\]

has 22 nonzero coefficients:

| (i,j) | c_ij |
|---|---:|
| (4,2) | +1995.409352574 |
| (4,1) | -3479.417112874 |
| (4,0) | +2177.194325217 |
| (3,3) | +1808.824170635 |
| (3,2) | -7389.238825412 |
| (3,1) | +8105.147499532 |
| (3,0) | -7120.373139931 |
| (2,4) | +1936.798112410 |
| (2,3) | -7355.052703979 |
| (2,2) | +1350.171884613 |
| (2,1) | +22902.204480117 |
| (2,0) | -17401.896128513 |
| (1,4) | -3401.278440968 |
| (1,3) | +8101.510189645 |
| (1,2) | +9795.665158028 |
| (1,1) | -35811.036406037 |
| (1,0) | +39550.822517839 |
| (0,4) | +2080.798219372 |
| (0,3) | -6651.334271016 |
| (0,2) | +8749.174217812 |
| (0,1) | -20495.636469773 |
| (0,0) | +57371.334514278 |

The finite candidate set from interior stationarity, all four edges, and all four corners gives the governing candidate

\[
(u,v)=(0.757308975358,-1),
\]

\[
\Phi_{max}=126025.000000001\ \mathrm{MPa}^2,
\]

hence

\[
\boxed{\max\sigma_{VM,loc}=355.000000000001\ \mathrm{MPa}}.
\]

The next-highest candidate is the corner `(1,-1)` with

\[
\Phi=122569.37239106\ \mathrm{MPa}^2,
\]

so the active `v=-1` stationary root is the actual global maximum, not a sampled approximation.

The returned full-width lower-face resultant is

\[
\mathbf N_-
=(-249.88526019,-888.22228255)\ \mathrm{N/mm}.
\]

---

# 11. Steel-face sums and exact section closure

Upper and lower face resultants give

\[
N_x^f=+513.213178230797\ \mathrm{N/mm},
\]
\[
N_y^f=-1191.19607935637\ \mathrm{N/mm},
\]
\[
M_x^f=23298.6250680230\ \mathrm N,
\]
\[
M_y^f=13460.7151723014\ \mathrm N.
\]

Adding UHPC + web + two full-width steel faces:

\[
N_x^{sec}=+199.305955403733\ \mathrm{N/mm},
\]
\[
N_y^{sec}=-5137.30935871949\ \mathrm{N/mm},
\]
\[
M_x^{sec}=29756.6988970160\ \mathrm N,
\]
\[
M_y^{sec}=30060.7058605884\ \mathrm N.
\]

Against the structural demands, the retained raw residuals are

```text
Rx_N = -1.42e-12 N/mm
Ry_N = -1.27e-11 N/mm
Rx_M = -1.82e-11 N
Ry_M = +1.82e-11 N
R_peak = 0
```

Therefore

```text
BH050_R06_BLIND_ROOT = PASS
SECTION_NM_CLOSURE = PASS
FINITE_ALGEBRAIC_LOCAL_MAX = PASS
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_AREA = 0
```

The physical first-contact branch was also continued away from the endpoint; its load increased as `s` decreased (`13.3564 MN` at `s=1`, `13.4380 MN` at `s=0.95`, `13.5239 MN` at `s=0.90`, `13.7096 MN` at `s=0.80`), confirming that the already-frozen endpoint `s=1` remains controlling for BH050 under R06. This continuation is a root-path check, not spatial quadrature.

---

# 12. Root freeze and comparator post-check

Only after the blind root above was fixed was the existing BH050 comparator reopened:

\[
P_{Abaqus}=12.2198\ \mathrm{MN}.
\]

Thus

\[
\boxed{
\frac{P_u^{R06}}{P_{Abaqus}}-1
=+9.3011\%.
}
\]

The previous R01/R04 result was

\[
P_u^{R04}=15.69757377\ \mathrm{MN},
\]

so R06 changes the theory prediction by

\[
\boxed{-14.9144\%}
\]

and reduces the comparator error from

\[
+28.4602\%\rightarrow\boxed{+9.3011\%}.
\]

BH050 remains the largest positive error in the seven-case set and its comparator remains the lower-confidence/different-model-family case already identified in the parent audit. No further repair is made here.

---

# 13. Seven-case common-R06 result table

Because R06 is mathematically identical to R04 whenever \(\sigma_{cr,s}^{E}\ge f_y\), T120/BH005/BH010/BH020 are strict non-regressions, not fitted carry-overs.

| Case | sigma_cr,s / MPa | R06 branch | previous R04 Pu / MN | current R06 Pu / MN | Abaqus / MN | error |
|---|---:|---|---:|---:|---:|---:|
| T120 | 2206.635 | yield-first = R04 | 12.76914369 | **12.76914369** | 12.6378 | **+1.0393%** |
| T360 | 245.795 | local-buckling-first | 12.18255684 | **10.81837778** | 10.9688 | **-1.3714%** |
| BH005 | 10044.967 | yield-first = R04 | 2.46233215 | **2.46233215** | 2.3558 | **+4.5221%** |
| BH010 | 2511.242 | yield-first = R04 | 4.58337285 | **4.58337285** | 4.3043 | **+6.4836%** |
| BH020 | 627.810 | yield-first = R04 | 8.55797773 | **8.55797773** | 8.0076 | **+6.8732%** |
| BH032 | 245.238 | local-buckling-first | 12.35286995 | **10.94053451** | 10.9905 | **-0.4546%** |
| BH050 | 100.450 | local-buckling-first | 15.69757377 | **13.35637635** | 12.2198 | **+9.3011%** |

All seven:

\[
\boxed{\text{mean signed error}=+3.7705\%},
\]

\[
\boxed{\text{MAE}=4.2922\%},
\]

\[
\boxed{\text{RMSE}=5.3373\%}.
\]

For comparison, before R06 the same seven had

```text
mean signed = +10.1200%
MAE         = 10.1200%
RMSE        = 13.0761%
```

For the historical primary six excluding the lower-confidence BH050 comparator, current R06 gives

```text
mean signed = +2.8487%
MAE         = 3.4574%
RMSE        = 4.3377%
```

---

# 14. Decision

```text
COMMON_R06_SEVEN_CASE_BATCH = PASS
T120_NONREGRESSION = PASS
BH005_NONREGRESSION = PASS
BH010_NONREGRESSION = PASS
BH020_NONREGRESSION = PASS
T360_LOCAL_BUCKLING_BRANCH = PASS
BH032_LOCAL_BUCKLING_BRANCH = PASS
BH050_LOCAL_BUCKLING_BRANCH = PASS
BH050_BLIND_Pu = 13.3563763545430 MN
BH050_ABAQUS_POSTCHECK_ERROR = +9.3011%
```

The common R06 mechanism is therefore internally consistent across the full current seven-case SSUHPC set. It does **not** eliminate all model error, and BH050 remains a lower-confidence outlier, but it removes the earlier systematic large overprediction for the three local-buckling-first steel-shell cases without perturbing the four yield-first cases.