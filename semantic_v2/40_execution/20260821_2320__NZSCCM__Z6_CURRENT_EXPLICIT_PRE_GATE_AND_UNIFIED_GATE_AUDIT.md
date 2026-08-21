# NZ-SCCM — Z6 当前显式理论 PRE-GATE 与 Unified Multiaxial Capacity Gate 审计

**Time:** 2026-08-21 23:20 +08:00  
**Status:** EXECUTED / PRE-GATE ROOT SOLVED / FINAL UMCG ROOT OPEN

## 0. Boundary

This execution uses the current Marguerre–Airy explicit theory plus the newly frozen Unified Multiaxial Capacity Gate (UMCG). No experimental or historical comparator enters mode choice, coefficient generation, candidate selection, or root solution.

The structural layer is not modified:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

The first calculation deliberately solves the existing explicit uniaxial Z-section capacity exactly as a PRE-GATE baseline. Only after that root is fixed are historical Zhou/Winter comparators opened.

## 1. Source-closed Z6 input

Physical whole wall:

\[
a_{phys}=24000\rm\ mm,\qquad b=12000\rm\ mm.
\]

Section/material:

\[
t_c=122\rm\ mm,\qquad t_s=4\rm\ mm/face,\qquad h=130\rm\ mm,
\]

\[
\rho_w=0.02,
\]

\[
f_c=30.4\rm\ MPa,\qquad \varepsilon_0=0.0018712490394580678,
\]

\[
E_c^0=32500\rm\ MPa,
\]

\[
E_s=206000\rm\ MPa,\qquad f_y=355\rm\ MPa,
\]

\[
\nu_c^A=0.18,\quad\nu_s^A=0.30,\quad\mu_c^Z=0.20,\quad\mu_s^Z=0.30.
\]

Initial imperfection:

\[
A_0=48\rm\ mm,\qquad q_0=A_0/b=0.004.
\]

## 2. Extensional and bending constants

\[
A_{11}=5.826801330128901\times10^6\rm\ N/mm,
\]

\[
A_{22}=6.329441330128901\times10^6\rm\ N/mm,
\]

\[
A_{12}=1.266142920741884\times10^6\rm\ N/mm,
\]

\[
A_{66}=2.280329204693509\times10^6\rm\ N/mm,
\]

\[
\Delta_A=3.5277279265623125\times10^{13}.
\]

Bending constants:

\[
D_x=1.14610310\times10^{10}\rm\ N\,mm,
\]

\[
D_y=1.198611371333303\times10^{10}\rm\ N\,mm,
\]

\[
H=1.2160676566638245\times10^{10}\rm\ N\,mm.
\]

## 3. Integer halfwave search

The current explicit elastic mode candidates are:

| j | Pcr / MN |
|---:|---:|
|1|60.17333767|
|2|39.28801472|
|3|46.37389941|
|4|61.79282475|

Therefore

\[
\boxed{m_*=2},\qquad \ell=12000\rm\ mm,
\]

and

\[
\alpha=\beta=\pi/12000.
\]

No comparator was used in this selection.

## 4. Current explicit coefficients

\[
\boxed{P_{cr}=39.2880147150\rm\ MN},
\]

\[
\boxed{C=86071.5974582\rm\ MN},
\]

where C is the coefficient of the dimensionless quantity \(q(q+2q_0)\).

\[
\boxed{G=7.4692093263\times10^6\rm\ N/mm},
\]

\[
\boxed{J=1.2419245217\times10^7\rm\ N}.
\]

## 5. Existing explicit Z-section capacity

For the current uniaxial section model:

\[
N_0=[(1-\rho_w)f_c+\rho_wf_y]t_c=4500.824\rm\ N/mm,
\]

\[
N_p=N_0+2f_yt_s=7340.824\rm\ N/mm.
\]

The finite algebraic candidate set includes endpoints, interior stationary roots, the Regime-A/B boundary \(n=N_0\), and the squash boundary \(n=N_p\).

## 6. PRE-GATE finite algebraic ultimate root

The smallest positive admissible root of the existing uniaxial Z capacity is an interior stationary point in Regime B:

\[
\boxed{q_u^{pre}=0.0138074129378},
\]

\[
\boxed{s_u^{pre}=0.298387166},
\]

\[
\boxed{n_u^{pre}=6546.81307\rm\ N/mm},
\]

\[
\boxed{m_u^{pre}=51166.7292\rm\ N}.
\]

The Regime-B tensile-face strip thickness is

\[
\delta=\frac{N_p-n_u}{2f_y}=1.11832525\rm\ mm.
\]

The resulting load is

\[
\boxed{P_u^{pre}=56.37942109\rm\ MN}.
\]

Postbuckling decomposition:

\[
P_{cr}\frac{q}{q+q_0}=30.46292264\rm\ MN,
\]

\[
Cq(q+2q_0)=25.91649845\rm\ MN.
\]

Incremental amplitude:

\[
bq_u=165.688955\rm\ mm,
\]

with total geometric amplitude including the initial imperfection

\[
A_0+bq_u=213.688955\rm\ mm.
\]

## 7. Comparison opened only after root solution

Historical/source comparators retained for post-solution assessment are:

\[
P_{Zhou}=49.48676675\rm\ MN,
\]

\[
P_{Winter}=50.18585413\rm\ MN.
\]

Thus the current PRE-GATE explicit result is

\[
\frac{56.37942109}{49.48676675}-1=\boxed{+13.9283\%},
\]

relative to Zhou, and

\[
\frac{56.37942109}{50.18585413}-1=\boxed{+12.3413\%},
\]

relative to Winter.

These differences are assessment outputs only; no parameter is changed from them.

## 8. Unified multiaxial demand at the PRE-GATE root

The Airy field gives a transverse tensile membrane demand

\[
\boxed{N_x^d=+2070.407936\rm\ N/mm}.
\]

This is large enough that the uniaxial fully-plastic Regime-B stress pattern cannot automatically be accepted.

### 8.1 Steel necessary-condition check under the unchanged PRE-GATE stress pattern

The current Regime-B pattern leaves only a \(\delta=1.11832525\) mm strip of one external face in longitudinal tension at \(+f_y\). Under plane-stress von Mises, that strip can carry at most \(+f_y\) transverse tension without changing its longitudinal stress. Its maximum transverse contribution under the unchanged baseline pattern is therefore

\[
N_{x,s}^{max,baseline}=\delta f_y
=397.005465\rm\ N/mm.
\]

Steel regions already at longitudinal \(-f_y\) cannot take positive transverse stress without reducing their longitudinal compression; doing so must lower/rebalance the axial section capacity.

### 8.2 Ordinary-concrete tension diagnostic

For the project ordinary-concrete family only as a diagnostic screening value,

\[
f_t=0.10f_c=3.04\rm\ MPa.
\]

The maximum core transverse-tension contribution under the same simplified baseline pattern is

\[
N_{x,c}^{max,diag}=(1-\rho_w)t_cf_t
=363.4624\rm\ N/mm.
\]

Therefore the unchanged baseline pattern can supply at most approximately

\[
N_{x}^{max,baseline,diag}
=397.0055+363.4624
=760.4679\rm\ N/mm,
\]

against demand

\[
2070.4079\rm\ N/mm.
\]

The diagnostic demand/capacity ratio is

\[
\boxed{\eta_x\approx2.723}.
\]

The 0.10fc concrete tension value is not used to fit Z6 and is not the final section solution. The important result is the necessary-condition failure of the **unchanged uniaxial plastic stress pattern**.

## 9. Gate decision

```text
CURRENT_EXPLICIT_Z6_PRE_GATE = SOLVED
PRE_GATE_PU = 56.37942109 MN
PRE_GATE_VS_ZHOU = +13.9283 percent
UMCG_BASELINE_STRESS_PATTERN = FAIL
FINAL_UNIFIED_Z6_PU = OPEN
STRUCTURAL_LAYER_MODIFIED = NO
EXPERIMENT_OR_COMPARATOR_IN_ROOT_SELECTION = 0
```

The UMCG does not imply that the complete Z6 section is incapable of carrying the required transverse membrane force. It implies that the current uniaxial plastic allocation cannot do so while preserving its longitudinal stresses. The phase stress field must be re-solved with steel von-Mises and concrete TC/CC admissibility simultaneously active; that redistribution is expected to reduce the 56.38 MN axial capacity, but its magnitude must be computed rather than imposed.

## 10. Applicability interpretation

Z6 is the first current explicit SC case that clearly exposes the boundary of the simple uniaxial N-M capacity layer:

\[
\boxed{
\text{Marguerre--Airy structural backbone remains usable, but uniaxial section capacity is not universally admissible.}
}
\]

This is precisely the intended role of UMCG. The observed +13.9% PRE-GATE overprediction is in the same direction as the capacity reduction required by the multiaxial admissibility check, without using the comparator to tune the theory.
