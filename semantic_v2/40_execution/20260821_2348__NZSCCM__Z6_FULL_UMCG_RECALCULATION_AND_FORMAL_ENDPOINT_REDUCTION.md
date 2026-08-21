# NZ-SCCM — Z6 Full UMCG Recalculation and Formal Endpoint Reduction

**Time:** 2026-08-21 23:48 +08:00  
**Status:** `EXECUTED / FINAL_Z6_UMCG_ROOT_RESOLVED / STRUCTURAL_BACKBONE_UNCHANGED`

## 0. Boundary

This execution continues directly from:

- `semantic_v2/20_theory/20260821_2315__NZSCCM__UNIFIED_MULTIAXIAL_CAPACITY_GATE_V1.md`;
- `semantic_v2/40_execution/20260821_2320__NZSCCM__Z6_CURRENT_EXPLICIT_PRE_GATE_AND_UNIFIED_GATE_AUDIT.md`.

No Zhou/Winter comparator is used in mode selection, coefficient generation, gate activation, control-location selection, or root solution. The Marguerre–Airy structural backbone remains frozen:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n_y(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m_y(s;q)=Jqs.
\]

## 1. Frozen Z6 data

\[
a_{phys}=24000\,\mathrm{mm},\qquad b=12000\,\mathrm{mm},
\]

\[
t_c=122\,\mathrm{mm},\qquad t_s=4\,\mathrm{mm/face},\qquad \rho_w=0.02,
\]

\[
f_c=30.4\,\mathrm{MPa},\quad E_c^0=32500\,\mathrm{MPa},\quad \varepsilon_0=0.0018712490394580678,\quad \nu_c=0.18,
\]

\[
E_s=206000\,\mathrm{MPa},\qquad f_y=355\,\mathrm{MPa},\qquad \nu_s=0.30,
\]

\[
q_0=0.004,\qquad m_*=2,\qquad \ell=12000\,\mathrm{mm}.
\]

Current structural coefficients:

\[
P_{cr}=39.2880147150\,\mathrm{MN},
\]

\[
C=86071.5974582\,\mathrm{MN},
\]

\[
G=7.4692093263\times10^6\,\mathrm{N/mm},
\qquad
J=1.2419245217\times10^7\,\mathrm{N}.
\]

The Airy transverse membrane resultant at the longitudinal halfwave centre is

\[
N_x^d(q)=K_xq(q+2q_0),
\]

with

\[
\boxed{K_x=6.876056916767441\times10^6\,\mathrm{N/mm}}.
\]

## 2. Phase-compatible UMCG section recovery

At each finite structural candidate \((q,s)\), use the compatible section strain family

\[
\varepsilon_x(z)=\varepsilon_0 X,
\]

\[
\varepsilon_y(z)=\varepsilon_0\left(Y+K\frac{z}{65}\right),
\]

\[
\gamma_{xy}=0.
\]

The section phases are:

1. effective ordinary-concrete core: \((1-\rho_w)\times[-61,61]\) mm;
2. longitudinal equivalent web steel: \(\rho_w\times[-61,61]\) mm, y-only source clip law;
3. lower external steel face: \([-65,-61]\) mm;
4. upper external steel face: \([61,65]\) mm.

Concrete uses the frozen NC-M6 plane-stress current operator. External steel faces use the frozen plane-stress elastic-trial + von-Mises radial-cap current law. The web uses

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y,-f_y,+f_y).
\]

The recovered phase stresses satisfy simultaneously

\[
N_x^{sec}=N_x^d(q),
\]

\[
N_y^{sec}=-n_y(s;q),
\]

\[
M_y^{sec}=m_y(s;q).
\]

Capacity is reached when the compatible section equilibrium map loses local rank / reaches an active material boundary. No scalar correction factor is applied to the PRE-GATE root.

## 3. Finite control-location audit

For each prescribed finite control coordinate s, the augmented UMCG section system was solved independently. The capacity boundary is monotone upward away from s=0 in the resolved interval:

| s | q_UMCG | P_UMCG / MN |
|---:|---:|---:|
|0.00|0.012360880154|51.345022|
|0.05|0.012362225640|51.349600|
|0.10|0.012367107350|51.366220|
|0.15|0.012377749610|51.402450|
|0.20|0.012397080340|51.468300|
|0.25|0.012428137880|51.574160|
|0.30|0.012473758750|51.729850|
|0.35|0.012534787410|51.938450|
|0.40|0.012613167720|52.206910|
|0.45|0.012711982270|52.546280|
|0.50|0.012833518790|52.965090|
|0.55|0.012979607980|53.470580|
|0.60|0.013151345850|54.067770|
|0.65|0.013349356980|54.760340|
|0.70|0.013573002850|55.547860|
|0.75|0.013820092700|56.424580|
|0.80|0.014086991430|57.379590|
|0.85|0.014365795690|58.386250|
|0.90|0.014641232360|59.390020|
|0.95|0.014891587660|60.310510|
|1.00|0.015092779620|61.055940|

Therefore the first positive UMCG capacity root is the endpoint

\[
\boxed{s_u=0}.
\]

The resolved root is

\[
\boxed{q_u^{UMCG}=0.01236088015386989},
\]

\[
\boxed{P_u^{UMCG}=51.34502178921372\,\mathrm{MN}}.
\]

The gate therefore changes the current explicit Z6 prediction from

\[
P_u^{pre}=56.37942109\,\mathrm{MN}
\]

to

\[
P_u^{UMCG}=51.3450217892\,\mathrm{MN},
\]

a reduction of

\[
\boxed{-8.92950\%}.
\]

## 4. Formal endpoint reduction — no thickness quadrature required

At the governing endpoint s=0,

\[
m_y=Jqs=0.
\]

By section symmetry the compatible solution has

\[
K=0,
\]

so each phase is uniform through its thickness. The final root therefore admits a direct finite algebraic/material reduction and does not require formal thickness quadrature.

Recovered normalized physical strains:

\[
\boxed{X=\varepsilon_x/\varepsilon_0=1.6614491883152634},
\]

\[
\boxed{Y=\varepsilon_y/\varepsilon_0=-1.6813465681824617}.
\]

The NC equivalent-uniaxial principal coordinates are

\[
\boxed{\lambda_x=1.4043063311724063},
\]

\[
\boxed{\lambda_y=-1.4285714285714286=-10/7}.
\]

For Z6,

\[
x_{cr}=0.049987179453974\ldots,
\]

thus

\[
\lambda_x/x_{cr}\approx28.0933>11,
\]

so the frozen NC-M6 tensile branch is T5:

\[
\tau=0.3.
\]

The active TC compression argument is

\[
(-\lambda_y)(1-\tau)
=\frac{10}{7}\times0.7
=1.
\]

Therefore the governing concrete compression direction is exactly at the Saenz peak:

\[
\boxed{\sigma_y^c=-f_c=-30.4\,\mathrm{MPa}}.
\]

The transverse concrete tensile stress is

\[
\boxed{\sigma_x^c=\rho\tau f_c=0.1\times0.3\times30.4=0.912\,\mathrm{MPa}}.
\]

## 5. Steel-face and web state at the final root

The external steel-face elastic trial von-Mises stress is

\[
\sigma_{VM}^{tr}=858.4297833644\,\mathrm{MPa}>355\,\mathrm{MPa},
\]

so both faces are on the plane-stress radial cap.

The physical steel-face stresses are

\[
\boxed{\sigma_x^s=+202.6895348824\,\mathrm{MPa}},
\]

\[
\boxed{\sigma_y^s=-207.2208079830\,\mathrm{MPa}}.
\]

The longitudinal equivalent web is at y-compression yield:

\[
\boxed{\sigma_y^w=-355\,\mathrm{MPa}}.
\]

Because s=0 gives uniform-through-thickness states, section resultants are direct phase sums:

\[
N_x^{sec}
=(1-\rho_w)t_c\sigma_x^c+2t_s\sigma_x^s,
\]

\[
N_y^{sec}
=(1-\rho_w)t_c\sigma_y^c+2t_s\sigma_y^s+\rho_wt_c\sigma_y^w.
\]

Numerically:

\[
\boxed{N_x^{sec}=1730.5549990592\,\mathrm{N/mm}},
\]

\[
\boxed{N_y^{sec}=-6158.5904638640\,\mathrm{N/mm}},
\]

\[
\boxed{M_y^{sec}=0}.
\]

These equal the Marguerre–Airy demands at the same q.

The same endpoint can therefore be solved without a thickness discretization from the two coupled equations in \((\lambda_x,q)\):

\[
N_x^{sec}(\lambda_x)=K_xq(q+2q_0),
\]

\[
N_y^{sec}(\lambda_x)
=-\left[\frac{P_{pb}(q)}b+Gq(q+2q_0)\right],
\]

with

\[
\lambda_y=-10/7,
\]

\[
\varepsilon_x/\varepsilon_0=\lambda_x-\nu_c\lambda_y,
\qquad
\varepsilon_y/\varepsilon_0=\lambda_y-\nu_c\lambda_x,
\]

and the frozen steel radial-cap map. High-precision evaluation reproduces

\[
\lambda_x=1.4043063311724062858,
\]

\[
q=0.012360880153869890853,
\]

\[
P=51.345021789213721916\,\mathrm{MN}.
\]

Hence the governing Z6 UMCG root has a formal finite no-thickness-quadrature representation under the current current-map assumptions.

## 6. Comparator opened only after final root

Historical/source comparators:

\[
P_{Zhou}=49.48676675\,\mathrm{MN},
\]

\[
P_{Winter}=50.18585413\,\mathrm{MN}.
\]

The final UMCG errors are

\[
\boxed{+3.75505\%\quad\text{vs Zhou}},
\]

\[
\boxed{+2.30975\%\quad\text{vs Winter}}.
\]

No parameter is changed to remove this residual.

## 7. Mechanism interpretation

The controlling mechanism changes materially after UMCG:

- PRE-GATE: Regime-B uniaxial N-M interior control at \(s\approx0.2984\), \(P\approx56.38\) MN;
- UMCG: transverse endpoint \(s=0\), zero bending demand, multiaxial membrane material-capacity control at \(P\approx51.35\) MN.

At the governing UMCG state:

1. ordinary concrete is in TC and its compressed principal direction reaches the NC-M6 softened Saenz peak;
2. the two external steel faces spend substantial yield capacity on simultaneous transverse tension and longitudinal compression;
3. the longitudinal web reaches y-compression yield;
4. the section simultaneously satisfies the Airy transverse and longitudinal membrane demands.

Thus the earlier uniaxial N-M layer over-predicted Z6 because it allowed longitudinal plastic utilization without paying the transverse Airy membrane-force demand. UMCG removes this inconsistency without changing the structural backbone or fitting to Zhou/Winter.

## 8. Decision

```text
Z6_FINAL_UMCG_ROOT = RESOLVED
Z6_CONTROL_LOCATION = s=0
Z6_FINAL_UMCG_q = 0.01236088015386989
Z6_FINAL_UMCG_Pu = 51.34502178921372 MN
Z6_GATE_EFFECT_FROM_PRE_GATE = -8.92950 percent
Z6_FINAL_VS_ZHOU = +3.75505 percent
Z6_FINAL_VS_WINTER = +2.30975 percent
Z6_FORMAL_ENDPOINT_THICKNESS_QUADRATURE = 0
STRUCTURAL_BACKBONE_MODIFIED = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

This is the first resolved final SC result under the common NC--SC--SUHPC UMCG architecture.