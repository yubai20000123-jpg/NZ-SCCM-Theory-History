# NZ-SCCM — BH032/BH050 Airy-demand vs terminal-allocation causal decomposition R01

**Date:** 2026-08-28  
**Identity:** DIAGNOSTIC / THEORY FIRST / NO FORMULA CHANGE / NOT PRODUCTION  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Parent:** `20260828__NZSCCM__AIRY_SSUHPC_FORCE_FIRST_TERMINAL_CAPACITY_SYSTEM_R01.md`

---

## 0. Objective and discipline

Do not modify Airy, R02, R06, UHPC, web, material parameters, control station, or root selection.

The task is only to split the already-frozen BH032/BH050 result into two causal layers:

\[
\boxed{
\text{Airy structural demand}
\quad\text{vs}\quad
\text{terminal constituent allocation / outer endpoint}
}
\]

and determine which layer best explains why BH050 is high while BH032 is essentially correct.

The canonical comparator is the **equal-contract** BH050 Abaqus result

\[
P_{FE}^{050}=12.591227\ \mathrm{MN},
\]

not the excluded legacy `12.2198 MN` model.

No comparator enters any theory root. FEM is opened only after the theory ledgers are frozen, as a mechanism discriminator.

---

# G0 — frozen theory roots and comparator contract

Frozen R06 roots:

\[
P_u^{032}=10.9405345132294\ \mathrm{MN},
\qquad
q_u^{032}=0.00137889961633743,
\]

\[
P_u^{050}=13.3563763545430\ \mathrm{MN},
\qquad
q_u^{050}=0.004772819645833164.
\]

Canonical equal-contract comparison:

\[
P_{FE}^{032}=10.990480\ \mathrm{MN},
\]

\[
P_{FE}^{050}=12.591227\ \mathrm{MN}.
\]

Hence

\[
\Delta P_{032}=-0.04994549\ \mathrm{MN}\approx-0.45\%,
\]

\[
\boxed{
\Delta P_{050}=+0.76514935\ \mathrm{MN}=+6.07685\%.
}
\]

```text
G0_FROZEN_ROOTS = PASS
G0_CANONICAL_EQUAL_CONTRACT_COMPARATOR = PASS
THEORY_RECALIBRATION = NO
```

---

# G1 — Airy demand ledger

For both cases

\[
Q_q=q(q+2q_0),
\]

\[
P^A(q)=P_{cr}\frac{q}{q+q_0}+CQ_q.
\]

At the governing `s=1` section,

\[
N_y^A=-\left(\frac{P}{b}-GQ_q\right),
\]

therefore the frozen root admits the exact accounting identity

\[
\boxed{
P=b(-N_y^{sec})+bGQ_q.
}
\]

This identity is used only as a decomposition of the existing root; no term is removed in the theory.

## G1.1 BH032

Using the frozen coefficients/root:

\[
Q_q=8.79586223362\times10^{-6},
\]

\[
P_E:=P_{cr}\frac{q}{q+q_0}=10.8791640768\ \mathrm{MN},
\]

\[
P_G:=CQ_q=0.0613704364\ \mathrm{MN}.
\]

Thus

\[
P_G/P_u=0.56095\%.
\]

The section/global accounting is

\[
b(-N_y^{sec})=10.8777637120\ \mathrm{MN},
\]

\[
bGQ_q=0.0627708012\ \mathrm{MN},
\]

\[
10.8777637120+0.0627708012=10.9405345132\ \mathrm{MN}.
\]

The Airy redistribution uplift is only

\[
0.57375\%\text{ of }P_u.
\]

## G1.2 BH050

Using the frozen coefficients/root:

\[
Q_q=4.66439056008\times10^{-5},
\]

\[
P_E=12.8506924314\ \mathrm{MN},
\]

\[
P_G=0.5056839231\ \mathrm{MN},
\]

so

\[
P_G/P_u=3.78609\%.
\]

The section/global accounting is

\[
\boxed{b(-N_y^{sec})=12.8432733968\ \mathrm{MN}},
\]

\[
\boxed{bGQ_q=0.5131029577\ \mathrm{MN}},
\]

\[
12.8432733968+0.5131029577=13.3563763545\ \mathrm{MN}.
\]

Hence the Airy `s=1` redistribution uplift is

\[
\boxed{0.513103\ \mathrm{MN}=3.841\%\text{ of }P_u}.
\]

Relative to the equal-contract total theory error `0.765149 MN`, this additive uplift is

\[
\boxed{0.513103/0.765149=67.06\%}.
\]

This does **not** mean that 67.06% is a rigorously separable model-error percentage, because `q` itself is selected by the terminal contact system. It means only that once the terminal system has allowed the root to reach `q=0.00477282`, the Airy redistribution converts that late root into an additional `0.513 MN` of global load.

A second useful accounting check is the nonlinear Airy term itself:

\[
CQ_q=0.505684\ \mathrm{MN}.
\]

Even if that term were omitted only as a counterfactual diagnostic, not as a theory change,

\[
P_E=12.850692\ \mathrm{MN}>12.591227\ \mathrm{MN}.
\]

Therefore the BH050 error cannot be caused solely by the `CQ_q` postbuckling term.

```text
G1_AIRY_DEMAND_LEDGER = PASS
AIRY_AMPLIFICATION_BH050 = MATERIAL
AIRY_CQ_TERM_ALONE_EXPLAINS_FULL_BIAS = NO
```

---

# G2 — terminal total-resultant and constituent-allocation ledger

The governing terminal section resultants are frozen before any FE comparison.

## G2.1 BH032

Theory:

\[
N_y^U=-4367.140,
\quad
N_y^{faces}=-2138.268,
\quad
N_y^w=-293.194,
\]

\[
N_y^{sec}=-6798.602\ \mathrm{N/mm}.
\]

Canonical equal-contract section integration gives approximately

\[
N_{y,FE}^U=-4531.590,
\quad
N_{y,FE}^{steel}=-1972.752,
\quad
N_{y,FE}^{web}=-311.039,
\]

\[
N_{y,FE}^{total}=-6815.381\ \mathrm{N/mm}.
\]

Theory shares:

```text
UHPC  64.24%
steel 31.45%
web    4.31%
```

FE shares:

```text
UHPC  66.49%
steel 28.95%
web    4.56%
```

The total longitudinal resultant differs by only

\[
\frac{|N_y^{th}|}{|N_y^{FE}|}-1=-0.246\%.
\]

This is the control case: the force-first terminal allocation is broadly consistent when the load prediction is also accurate.

## G2.2 BH050

Theory:

\[
N_y^U=-3775.209,
\quad
N_y^{faces}=-1191.196,
\quad
N_y^w=-170.905,
\]

\[
N_y^{sec}=-5137.309\ \mathrm{N/mm}.
\]

Canonical equal-contract section integration gives

\[
N_{y,FE}^U=-2947.266,
\quad
N_{y,FE}^{steel}=-2144.846,
\quad
N_{y,FE}^{web}=-189.296,
\]

\[
N_{y,FE}^{total}=-5281.408\ \mathrm{N/mm}.
\]

Theory shares:

```text
UHPC  73.49%
steel 23.19%
web    3.33%
```

FE shares:

```text
UHPC  55.80%
steel 40.61%
web    3.58%
```

Therefore BH050 develops a new internal allocation error absent in BH032:

\[
\boxed{\Delta\eta_U=+17.68\text{ percentage points}},
\]

\[
\boxed{\Delta\eta_s=-17.42\text{ percentage points}}.
\]

In absolute phase forces,

\[
\frac{|N_y^U|_{th}}{|N_y^U|_{FE}}-1=+28.09\%,
\]

\[
\frac{|N_y^{steel}|_{th}}{|N_y^{steel}|_{FE}}-1=-44.46\%.
\]

Yet the **total** terminal longitudinal resultant differs by only

\[
\boxed{
\frac{|N_y^{sec}|_{th}}{|N_y^{total}|_{FE}}-1=-2.73\%.
}
\]

Thus the principal new BH050 discrepancy is not an excessive total local `Ny`; it is a large UHPC↔steel load-transfer error hidden by cancellation in the total resultant.

```text
G2_TOTAL_NY_BH032 = CLOSE
G2_TOTAL_NY_BH050 = CLOSE_TO_FIRST_ORDER
G2_PHASE_ALLOCATION_BH032 = CLOSE
G2_PHASE_ALLOCATION_BH050 = LARGE_MISMATCH
```

---

# G3 — terminal outer-endpoint audit

The frozen BH032/BH050 theory uses

\[
\boxed{\varepsilon_y(-21\ \mathrm{mm})=-0.0035}
\]

as the outer terminal contact.

The extracted equal-contract FE UHPC fields show a decisive change:

- BH032 crosses `min(LE33)=-0.0035` before its peak (approximately `0.843 Pu` in the available ascending-branch checkpoint ledger) and then continues to peak.
- BH050 reaches its FE global peak while the extracted minimum is only

\[
\boxed{\min LE33_{FE}(P_u)\approx-0.002813},
\]

so the BH050 FE peak occurs **before** the frozen theory's UHPC `-0.0035` terminal contact is reached.

This statement does not equate a fitted FE curvature with the terminal generalized coordinate. It only tests whether the physical UHPC field has reached the material threshold used as the theory outer endpoint.

Therefore the current terminal active set is late for BH050.

Under the **unchanged** BH050 Airy law, the `q` that corresponds to the equal-contract FE peak load is

\[
\boxed{q(P=12.591227)=0.00411758956}.
\]

Compared with the frozen terminal root

\[
q_u=0.00477281965,
\]

this is

\[
\boxed{13.73\%\text{ earlier in the Airy demand coordinate}}.
\]

This is not a calibrated replacement root. It is a causal sufficiency test: an earlier terminal stop of order 14% in `q` would remove the observed global load bias **without changing the Airy formula at all**.

```text
G3_BH032_FROZEN_UHPC_CONTACT_RELEVANT = YES
G3_BH050_FE_PEAK_REACHES_UHPC_-0p0035 = NO
G3_BH050_FROZEN_TERMINAL_ACTIVE_SET_IS_LATE = YES
```

---

# G4 — steel-face asymmetry and R06-only exclusion

At BH050 peak the frozen theory mean longitudinal steel-face stresses are approximately

\[
\sigma_{y,+}^{th}=-75.74\ \mathrm{MPa},
\qquad
\sigma_{y,-}^{th}=-222.06\ \mathrm{MPa}.
\]

The equal-contract FE section-point means are approximately

\[
\sigma_{y,+}^{FE}=-256.87\ \mathrm{MPa},
\qquad
\sigma_{y,-}^{FE}=-226.94\ \mathrm{MPa}.
\]

The bottom face, where R06 local-yield projection is active, is already close in mean longitudinal stress. The largest discrepancy is the **top face**, which remains uncapped R02 in the theory.

Hence

\[
\boxed{\text{R06 first-local-yield projection alone cannot be the BH050 root cause}.}
\]

The evidence points upstream inside the coupled terminal section state / active set: too much UHPC compression, too little top-face longitudinal compression, and too much section asymmetry before the chosen UHPC endpoint is reached.

```text
G4_R06_ONLY_CAUSE = REJECTED
G4_COUPLED_TERMINAL_STATE_MISMATCH = SUPPORTED
```

---

# G5 — causal attribution

The evidence must distinguish **root cause** from **load amplification**.

## Root cause

The strongest case-specific change from BH032 to BH050 is in the terminal layer:

1. BH032 phase allocation is close to FE; BH050 UHPC/steel allocation reverses badly.
2. BH050 FE peaks before the theory's frozen UHPC `-0.0035` outer contact.
3. The largest steel-face discrepancy is on the uncapped top face, so the lower-face R06 cap is not sufficient as an explanation.
4. The theory total local `Ny` at BH050 is not excessively high; it is actually about 2.7% less compressive than the equal-contract FE section total.

Therefore

\[
\boxed{
\text{PRIMARY ROOT CAUSE}
=
\text{BH050 terminal coupled allocation / outer active-set closure}.
}
\]

## Amplifier

Once that terminal closure permits the Airy coordinate to advance to `q=0.00477282`, the Airy demand front amplifies the delay:

\[
bGQ_q=0.513103\ \mathrm{MN},
\]

and

\[
CQ_q=0.505684\ \mathrm{MN}.
\]

Thus

\[
\boxed{
\text{AIRY ROLE}
=
\text{significant positive amplifier at the late BH050 root, not presently the best-supported primary cause}.
}
\]

This audit does **not** prove the Airy backbone exact. It only establishes that the presently observed BH050 error can be generated by a terminal root that occurs too late, while preserving the same Airy law; and that the terminal phase state itself is independently inconsistent with the equal-contract FE mechanism.

---

# Final status

```text
THEORY_FORMULAS_CHANGED = NO
PRODUCTION_CHANGED = NO
FEM_USED_IN_THEORY_ROOT = NO
BH032_AIRY_DEMAND_LEDGER = PASS
BH050_AIRY_DEMAND_LEDGER = PASS
BH032_TERMINAL_ALLOCATION = CLOSE
BH050_TERMINAL_ALLOCATION = LARGE_MISMATCH
BH050_FROZEN_UHPC_OUTER_CONTACT = TOO_LATE_RELATIVE_TO_FE_PEAK
R06_ONLY_CAUSE = REJECTED
PRIMARY_BH050_BIAS_LAYER = TERMINAL_COUPLED_ALLOCATION_AND_OUTER_ACTIVE_SET
SECONDARY_AMPLIFIER = AIRY_REDISTRIBUTION / POSTBUCKLING_DEMAND_AT_LATE_q
AIRY_BACKBONE_REJECTION = NOT_JUSTIFIED
NEXT_THEORY_TARGET = PATH_FREE_TERMINAL_ENDPOINT/ACTIVE_SET THAT TERMINATES BH050 EARLIER WHILE LEAVING BH032 ESSENTIALLY UNCHANGED
```
