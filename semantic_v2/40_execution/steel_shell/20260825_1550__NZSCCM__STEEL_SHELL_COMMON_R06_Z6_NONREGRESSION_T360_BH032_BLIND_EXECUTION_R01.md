# NZ-SCCM — STEEL-SHELL COMMON R06: Z6 strict non-regression + T360/BH032 blind execution R01

**Time:** 2026-08-25 15:50 +08:00  
**Parent:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**R06 theory:** `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`  
**Comparator in root solve:** `0`  
**Formal spatial sampling:** `0`  
**Formal spatial quadrature:** `0`  
**Material points:** `0`  
**Effective width/area:** `0`

---

# 0. Execution order

The execution was deliberately separated into two phases.

**Phase A — blind theory only**

```text
1. freeze R06 operator
2. Z6 strict non-regression
3. T360 blind root
4. BH032 blind root
5. finite-algebraic local-max certificate
6. freeze roots
```

Only after all of Phase A was fixed was the already-existing Abaqus comparator table reopened.

---

# 1. Common R06 operator used

R02 is unchanged. The only new steel-face rule is:

\[
\sigma_{cr,s}^E\ge f_y
\Rightarrow R06\equiv R04,
\]

while

\[
\sigma_{cr,s}^E<f_y
\Rightarrow
\text{R02 local-buckling-first branch}.
\]

For the local-buckling-first branch, with the current face strain ray

\[
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,
\]

R02 is re-condensed at every `eta`. The first local-Mises boundary satisfies

\[
\max_{[-1,1]^2}\Phi(u,v;\eta_y)=f_y^2.
\]

The full-area face stress returned to the terminal section is

\[
\bar{\boldsymbol\sigma}_{R06}
=
\bar{\boldsymbol\sigma}_{R02}(\eta_y\boldsymbol\varepsilon_f).
\]

No effective width or reduced area is used.

For the present `gamma_xy=0` cases, `Phi` is a degree-6-or-lower polynomial. During Newton continuation the active finite algebraic branch was the edge `v=-1`; after the blind roots were fixed, the complete finite candidate set — interior resultant roots, all four edges and four corners — was enumerated at every final face state. The `v=-1` candidate remained the global maximum where local yield was active.

---

# 2. G1 — Z6 strict non-regression

Frozen Z6 local steel cell:

```text
Lx = 200 mm
Ly = 200 mm
ts = 4 mm
A0 = 0.125 mm
Es = 206000 MPa
nu = 0.30
fy = 355 MPa
```

R02/Yun elastic local critical stress:

\[
\boxed{\sigma_{cr,s}^{E}=794.388671697\ \mathrm{MPa}>355\ \mathrm{MPa}.}
\]

Therefore R06 selects

```text
R04_YIELD_FIRST
```

**before** any comparator is read. Hence the R06 operator is exactly R04 for Z6.

At the already-fixed Z6 R05 common endpoint:

\[
\varepsilon_x=+0.00182595997641601,
\qquad
\varepsilon_y=-0.00187124903945807,
\]

R06 reproduces identically:

\[
U=0.127098680687955\ \mathrm{mm},
\]

\[
\boldsymbol\sigma^{tr}
=(+286.326378023,-299.539050646,0)\ \mathrm{MPa},
\]

\[
\sigma_{VM}^{tr}=507.417351952\ \mathrm{MPa},
\]

\[
\lambda=0.699621324801838,
\]

\[
\boxed{
\boldsymbol\sigma_s
=(+200.320039918,-209.563907443,0)\ \mathrm{MPa}.
}
\]

Each face therefore remains

\[
N_x=+801.280159673\ \mathrm{N/mm},
\qquad
N_y=-838.255629772\ \mathrm{N/mm}.
\]

Consequently the full Z6 R05 root remains exactly

\[
\boxed{P_u^{Z6,R06}=49.45439833719624\ \mathrm{MN}.}
\]

No new nonlinear solve is required because the branch operator is mathematically identical.

```text
G1_Z6_STRICT_NONREGRESSION = PASS
```

---

# 3. G2 — T360 blind R06 solve

## 3.1 Frozen structural input

```text
b = 1600 mm
a_phys = 3000 mm
tc = 42 mm
ts = 4 mm
web net height = 37 mm
rho_w = 0.0198214285714286
q0 = 0.0025
m* = 2
ell = 1500 mm
```

Unchanged initial-Airy coefficients:

\[
P_{cr}=30.7519466756596\ \mathrm{MN},
\]

\[
C=7056.00486840761\ \mathrm{MN},
\quad
G=5.07477413681440\times10^6\ \mathrm{N/mm},
\]

\[
K_x=4.26124168384866\times10^6\ \mathrm{N/mm},
\]

\[
J_x=1.00182230495780\times10^7\ \mathrm N,
\quad
J_y=1.09525417988951\times10^7\ \mathrm N.
\]

Local steel cell:

```text
Lx = 360 mm
Ly = 375 mm
A0 = 0.225 mm
```

with

\[
\boxed{\sigma_{cr,s}^{E}=245.794898415\ \mathrm{MPa}<355\ \mathrm{MPa}.}
\]

Thus T360 enters the R06 local-buckling-first branch.

## 3.2 Blind root

Solving the unchanged four section-resultant balances plus the unchanged UHPC first-compression-peak active equation gives

\[
\boxed{q_u=0.00134518627955957},
\]

\[
\boxed{\varepsilon_x^0=+1.55496505369409\times10^{-4}},
\]

\[
\boxed{\kappa_x=2.10866374135730\times10^{-5}\ \mathrm{mm}^{-1}},
\]

\[
\boxed{\varepsilon_y^0=-0.00246762598056689},
\]

\[
\boxed{\kappa_y=4.91606675920531\times10^{-5}\ \mathrm{mm}^{-1}}.
\]

The controlling UHPC condition remains

\[
\varepsilon_y(-t_c/2)=-0.0035.
\]

The added global amplitude is

\[
bq_u=2.15229804730\ \mathrm{mm}.
\]

The blind load is

\[
\boxed{P_u^{T360,R06}=10.8183777809815\ \mathrm{MN}.}
\]

Relative to the previous R01 steel-face operator, but without opening Abaqus,

\[
\frac{10.818377781}{12.182556843}-1
=
\boxed{-11.1978\%}.
\]

## 3.3 T360 demand and exact section closure

At the fixed root:

\[
N_x^d=+36.3716473942\ \mathrm{N/mm},
\]

\[
N_y^d=-6718.17059402\ \mathrm{N/mm},
\]

\[
M_x^d=13476.3761919\ \mathrm N,
\qquad
M_y^d=14733.2089542\ \mathrm N.
\]

UHPC:

\[
N_x^U=+2.59552337762,
\quad
M_x^U=2187.29735545,
\]

\[
N_y^U=-4321.32836356,
\quad
M_y^U=11937.8842483.
\]

Web:

\[
N_y^w=-292.091722922,
\qquad
M_y^w=+65.631326802.
\]

Upper steel face (`z=+23 mm`):

\[
(\varepsilon_x,\varepsilon_y)
=(+0.000640489166,-0.001336930626),
\]

\[
U_+=0.628786543424\ \mathrm{mm}.
\]

Its complete finite-algebraic local maximum is

\[
\max\sigma_{VM,loc}=303.562024486\ \mathrm{MPa}<355\ \mathrm{MPa},
\]

so it remains uncapped R02:

\[
\bar{\boldsymbol\sigma}_+
=(+65.57570483,-248.25852334,0)\ \mathrm{MPa}.
\]

Hence

\[
\mathbf N_+=(+262.30281932,-993.03409336)\ \mathrm{N/mm}.
\]

Lower steel face (`z=-23 mm`):

\[
(\varepsilon_x,\varepsilon_y)
=(-0.000329496155,-0.003598321335),
\]

R06 finds the radial first-local-yield factor

\[
\boxed{\eta_{y,-}=0.419889652186}.
\]

At that admissible boundary:

\[
U_-=1.541807734687\ \mathrm{mm},
\]

\[
\bar{\boldsymbol\sigma}_-
=(-57.13167383,-277.92910355,0)\ \mathrm{MPa},
\]

\[
\mathbf N_-=(-228.52669530,-1111.71641418)\ \mathrm{N/mm}.
\]

The complete finite algebraic candidate enumeration gives

\[
\boxed{\max\sigma_{VM,loc}=355.000000004\ \mathrm{MPa}},
\]

with the active candidate on `v=-1`; no interior/other-edge/corner candidate exceeds it.

Steel-face sums:

\[
N_x^f=+33.776124017,
\qquad
N_y^f=-2104.750507541,
\]

\[
M_x^f=11289.078836408,
\qquad
M_y^f=2729.693379053.
\]

Therefore

\[
N_x^{sec}=36.3716473942=N_x^d,
\]

\[
N_y^{sec}=-6718.17059402=N_y^d,
\]

\[
M_x^{sec}=13476.37619186=M_x^d,
\]

\[
M_y^{sec}=14733.20895418=M_y^d,
\]

with retained numerical residuals of order `1e-10` or smaller.

```text
G2_T360_BLIND_R06 = PASS
```

---

# 4. G3 — BH032 blind R06 solve

## 4.1 Frozen structural input

Current corrected BH032 geometry:

```text
b = 1600 mm
a_phys = 3200 mm
tc = 42 mm
ts = 4 mm
9 longitudinal webs, net height = 37 mm
rho_w = 0.0198214285714286
q0 = 0.0025
m* = 2
ell = 1600 mm
```

The use of 37 mm net web height is independently confirmed by the current

\[
P_{cr}=30.6035224490574\ \mathrm{MN},
\]

whereas the superseded 32 mm web contract would give about `30.600955 MN`.

Current Airy coefficients:

\[
C=6977.19391202655\ \mathrm{MN},
\]

\[
G=4.46025070618453\times10^6\ \mathrm{N/mm},
\]

\[
K_x=4.26124168384866\times10^6\ \mathrm{N/mm},
\]

\[
J_x=9.72684495985725\times10^6\ \mathrm N,
\quad
J_y=9.88235146460377\times10^6\ \mathrm N.
\]

The controlling local steel cell is

```text
Lx = 360 mm
local halfwave count = 9
Ly = 3200/9 = 355.555555556 mm
A0 = 0.225 mm
```

which gives

\[
\boxed{\sigma_{cr,s}^{E}=245.238446006\ \mathrm{MPa}<355\ \mathrm{MPa}.}
\]

Thus BH032 independently enters the same common R06 local-buckling-first branch.

## 4.2 Blind root

The blind R06 solution is

\[
\boxed{q_u=0.00137889961633743},
\]

\[
\boxed{\varepsilon_x^0=+1.60605822952534\times10^{-4}},
\]

\[
\boxed{\kappa_x=2.07125070401497\times10^{-5}\ \mathrm{mm}^{-1}},
\]

\[
\boxed{\varepsilon_y^0=-0.00249442810080108},
\]

\[
\boxed{\kappa_y=4.78843761523297\times10^{-5}\ \mathrm{mm}^{-1}}.
\]

Again

\[
\varepsilon_y(-t_c/2)=-0.0035
\]

is the unchanged core active condition.

Added global amplitude:

\[
bq_u=2.20623938614\ \mathrm{mm}.
\]

Blind R06 load:

\[
\boxed{P_u^{BH032,R06}=10.9405345132294\ \mathrm{MN}.}
\]

Relative to the previous blind R01 value alone:

\[
\boxed{-11.4333\%}.
\]

## 4.3 BH032 demand and closure

Demand:

\[
N_x^d=+37.4812947953\ \mathrm{N/mm},
\]

\[
N_y^d=-6798.60232003\ \mathrm{N/mm},
\]

\[
M_x^d=13412.3427833\ \mathrm N,
\qquad
M_y^d=13626.7706431\ \mathrm N.
\]

UHPC:

\[
N_x^U=+9.56201202007,
\quad
M_x^U=2095.33545853,
\]

\[
N_y^U=-4367.14036120,
\quad
M_y^U=11594.81057147.
\]

Web:

\[
N_y^w=-293.194029786,
\qquad
M_y^w=+45.388284391.
\]

Upper face:

\[
(\varepsilon_x,\varepsilon_y)
=(+0.000636993485,-0.001393087449),
\]

\[
U_+=0.711487681071\ \mathrm{mm},
\]

\[
\max\sigma_{VM,loc}=317.237163177\ \mathrm{MPa}<355\ \mathrm{MPa}.
\]

Thus it remains uncapped, with

\[
\bar{\boldsymbol\sigma}_+
=(+64.99538494,-256.48690533,0)\ \mathrm{MPa}.
\]

Lower face:

\[
(\varepsilon_x,\varepsilon_y)
=(-0.000315781839,-0.003595768752),
\]

\[
\boxed{\eta_{y,-}=0.425379325768},
\]

\[
U_-=1.518650391337\ \mathrm{mm},
\]

\[
\bar{\boldsymbol\sigma}_-
=(-58.01556424,-278.08007693,0)\ \mathrm{MPa}.
\]

The full finite-algebraic certificate gives

\[
\boxed{\max\sigma_{VM,loc}=355.000000002\ \mathrm{MPa}},
\]

again with the global candidate on `v=-1`.

Face-resultant sums:

\[
N_x^f=+27.9192827752,
\qquad
N_y^f=-2138.26792904,
\]

\[
M_x^f=11317.00732480,
\qquad
M_y^f=1986.57178719.
\]

All four section resultants close to the Airy demand to about `1e-9` or better.

```text
G3_BH032_BLIND_R06 = PASS
G4_FINITE_ALGEBRAIC_LOCAL_MAX_CERTIFICATE = PASS
```

---

# 5. Blind-root freeze ledger

Before comparator reopening, the frozen common-R06 values are:

| case | branch | old R01 Pu / MN | R06 blind Pu / MN | change |
|---|---|---:|---:|---:|
| Z6 | `R04_YIELD_FIRST` | 49.45439834 | **49.45439834** | **0.0000%** |
| T360 | `LOCAL_BUCKLING_FIRST` | 12.18255684 | **10.81837778** | **-11.1978%** |
| BH032 | `LOCAL_BUCKLING_FIRST` | 12.35286995 | **10.94053451** | **-11.4333%** |

At this point the roots were declared frozen.

```text
COMPARATOR_IN_ROOT_SELECTION = 0
```

---

# 6. Phase B — comparator reopened only after freeze

Only now reopen the existing Abaqus R02 peak loads:

```text
T360  = 10.9688 MN
BH032 = 10.9905 MN
```

Post-check:

| case | R01 theory error | R06 blind Pu / MN | Abaqus / MN | R06 error |
|---|---:|---:|---:|---:|
| T360 | +11.0655% | **10.81837778** | 10.9688 | **-1.3714%** |
| BH032 | +12.3959% | **10.94053451** | 10.9905 | **-0.4546%** |

No parameter or branch was modified after opening these comparator values.

The signs also matter: R06 does not merely fit the old positive bias to zero; it slightly crosses to the conservative side in both independent local-buckling-first cases.

---

# 7. Mechanical interpretation

The common-module hypothesis is now supported by three deliberately different cases:

```text
Z6:
  sigma_cr/fy = 2.238
  yield-first
  R06 -> R04 exactly
  Pu unchanged

T360:
  sigma_cr/fy = 0.692
  local-buckling-first
  lower face local yield active
  full-area face resultant reduced
  Pu 12.1826 -> 10.8184 MN

BH032:
  sigma_cr/fy = 0.691
  local-buckling-first
  lower face local yield active
  Pu 12.3529 -> 10.9405 MN
```

Therefore the correction is not tied to NC or UHPC. It is controlled by the local steel-face event order.

R06 does not alter UHPC parameters, does not use an effective width, and does not change the Airy front.

---

# 8. Gate decision

```text
STEEL_SHELL_COMMON_R06_THEORY = PASS
Z6_STRICT_NONREGRESSION = PASS
T360_BLIND_R06 = PASS
BH032_BLIND_R06 = PASS
FINITE_ALGEBRAIC_LOCAL_MAX = PASS
RESULTANT_CLOSURE = PASS
COMPARATOR_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH = 0
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
R03_REOPENED = NO
UHPC_RETUNED = NO
```

For the present axial terminal scope (`gamma_xy=0`), R06 is promoted to the **common steel-shell production face gate**:

```text
YIELD-FIRST CELL        -> existing R04 branch
LOCAL-BUCKLING-FIRST    -> R06 local-yield resultant branch
```

R04 is therefore not deleted; it survives as the exact yield-first degeneration inside R06.

The next validation task, if continued, is a common non-regression batch over the remaining stocky steel-shell cases and then the more severe BH050 case. That is validation of the already-frozen R06 operator, not permission to refit it.
