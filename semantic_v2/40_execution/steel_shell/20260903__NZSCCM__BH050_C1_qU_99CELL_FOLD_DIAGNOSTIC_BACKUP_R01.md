# NZ-SCCM BH050 C1-qU 99-cell fold diagnostic backup R01

Date: 2026-09-03
Branch: `diagnostic/bh032-bh050-mode-projection-20260827`
Status: **REGISTRATION DIAGNOSTIC / NOT PRODUCTION Pu**

This file preserves the completed numerical execution state before further fold dissection. It is intentionally additive and does not supersede R14 production or earlier C1/PBL ledgers.

## 1. C1-PBL kinematic contract actually executed

At each PBL line:

\[
w_s=W_c,\qquad w_{s,n}=W_{c,n},
\]

while **not** imposing

\[
w_{s,nn}=W_{c,nn}.
\]

The original R02 local mode is retained unchanged:

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta).
\]

It satisfies \(\phi=0\) and \(\phi_{,n}=0\) at the cell boundary but permits \(\phi_{,nn}\neq0\). Therefore C1-PBL does not require the historical C2 \(r^3(1-r)^3\) mode. Existing R02 \(c_x,c_y,K_b,K_A\), LL seven-harmonic terms, and GL `qU` finite-harmonic machinery remain usable. `K_A` was independently recompiled for BH050 and matched the frozen closed form to machine precision.

## 2. Registration diagnostic geometry

Exact face-specific \((x_0,y_0,s_f)\) registration was not preserved in the old frozen BH050 report. The executed diagnostic therefore used the previously declared deterministic 5/4 staggered layout.

Top face: 4 PBL lines giving 5 bays

```text
[406.25, 562.5, 562.5, 562.5, 406.25] mm
```

Bottom face: 5 PBL lines giving 6 bays

```text
[125, 562.5, 562.5, 562.5, 562.5, 125] mm
```

Axial registration cell length:

\[
L_y=555.5556=5000/9\ \mathrm{mm}.
\]

Nine deterministic axial cells were used. Local imperfection:

\[
A_{0b}=b_b/1600.
\]

Total independent local cells:

\[
5\times9+6\times9=99.
\]

Each cell therefore has its own solved local amplitude \(U_b\); no single-face common \(U\) is imposed.

## 3. qU terms actually used

For every cell:

\[
d_b=U_b^2-A_{0b}^2,
\]

\[
\Delta_b=s_fB[(q_0+q)U_b-q_0A_{0b}],
\]

with

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=-h_\gamma\Delta.
\]

The coefficients \(h_x,h_y,h_\gamma\) were calculated separately for each real cell registration \((x_0,y_0,L_x,L_y)\) from finite trigonometric integrals; they were not tuned.

The GL Airy compatibility term was explicitly expanded as

\[
\mathcal C_{GL}=\psi_{xx}\phi_{yy}+\phi_{xx}\psi_{yy}-2\psi_{xy}\phi_{xy},
\]

and the finite harmonic coefficients were used to obtain \(K_{d\Delta}\) and \(K_{\Delta\Delta}\). No formal spatial integration grid was introduced.

## 4. Rebalanced section state at the old R14 q

At

\[
q=0.00493091069216,
\]

all four R4 equilibrium equations were re-solved rather than freezing the old section strains. The resulting state was

\[
\varepsilon_x^0=3.52910\times10^{-4},
\]

\[
\kappa_x=2.57553\times10^{-5}/\mathrm{mm},
\]

\[
\varepsilon_y^0=-1.544995\times10^{-3},
\]

\[
\kappa_y=2.63515\times10^{-5}/\mathrm{mm}.
\]

Old R14 had

\[
\kappa_y^{R14}=6.56100\times10^{-5}/\mathrm{mm}.
\]

Thus the rebalanced C1-qU state reduces \(\kappa_y\) by about 60% without an imposed curvature reduction.

At the same old R14 q,

\[
P=13.52478\ \mathrm{MN}.
\]

Area-weighted longitudinal membrane stresses were approximately

\[
\bar\sigma_y^{top}=-149.30\ \mathrm{MPa},
\]

\[
\bar\sigma_y^{bottom}=-404.38\ \mathrm{MPa}.
\]

Longitudinal resultants:

\[
N_y^{steel}=-2214.73\ \mathrm{N/mm},
\]

\[
N_y^{UHPC}=-2817.12\ \mathrm{N/mm},
\]

\[
N_y^{web}=-162.60\ \mathrm{N/mm},
\]

with required total

\[
N_y^A=-5194.4433\ \mathrm{N/mm}.
\]

Corresponding shares are approximately

\[
UHPC=54.2\%,\qquad steel=42.6\%,\qquad web=3.1\%.
\]

This is a first-order redistribution relative to the old R14 state of roughly 73% UHPC / 24% steel. No effective area, effective width, FEM load-share fitting, or force-share parameter was used.

The remaining strong top/bottom asymmetry is important: top about \(-149\) MPa versus bottom about \(-404\) MPa. The next audit must explain this asymmetry rather than tune it away.

## 5. Continuation toward the structural fold

At

\[
q=0.00650,
\]

a stable equilibrium state was found:

\[
\varepsilon_x^0\approx4.058\times10^{-4},
\]

\[
\kappa_x\approx3.984\times10^{-5}/\mathrm{mm},
\]

\[
\varepsilon_y^0\approx-1.8653\times10^{-3},
\]

\[
\kappa_y\approx4.7840\times10^{-5}/\mathrm{mm}.
\]

The most compressed UHPC longitudinal strain was only about

\[
\varepsilon_y^-\approx-0.002870,
\]

well short of \(-0.0035\).

Numerical consistent R4-Jacobian smallest singular values along the connected branch:

| q | s_min |
|---:|---:|
| 0.00675 | 0.547 |
| 0.00680 | 0.0598 |
| 0.00685 | 0.0443 |
| 0.00690 | 0.0308 |
| 0.00695 | 0.0188 |
| 0.00700 | 0.00776 |

This sequence indicates an approaching R4/J4 singular fold.

## 6. Turning-parameter continuation and located diagnostic fold

Near the fold, \(\varepsilon_x^0\) was used as the local continuation parameter and \((\kappa_x,\varepsilon_y^0,\kappa_y,q)\) were solved.

| eps_x0 | q |
|---:|---:|
| 0.0028 | 0.00702516878 |
| 0.0029 | 0.00702558852 |
| 0.0030 | 0.00702569192 |
| 0.0031 | 0.00702547988 |

Therefore

\[
q_{fold}^{C1,diag}\approx0.00702570,
\]

near

\[
\varepsilon_x^0\approx2.983\times10^{-3}.
\]

Using the frozen Airy \(P(q)\) mapping,

\[
P_{fold}^{C1,diag}\approx15.36\ \mathrm{MN}.
\]

Diagnostic ordering for comparison:

```text
R14                    13.5248 MN
multi-bay only          13.7905 MN
C2 trial              ~ 14.424  MN
C1-qU registration    ~ 15.36   MN
```

## 7. Event ordering at the fold

Approximate section state near the fold:

\[
\varepsilon_x^0\approx2.98\times10^{-3},
\]

\[
\kappa_x\approx1.69\times10^{-4}/\mathrm{mm},
\]

\[
\varepsilon_y^0\approx-2.09\times10^{-3},
\]

\[
\kappa_y\approx3.5\times10^{-5}/\mathrm{mm}.
\]

The most compressed UHPC longitudinal strain remained approximately

\[
\varepsilon_y^-\approx-2.8\times10^{-3},
\]

rather than reaching \(-0.0035\). Thus the diagnostic event ordering changed from the old R14 `UHPC material boundary first` to `R4/J4 structural fold first`.

## 8. Two gates deliberately left open

### Gate A — exact registration

The executed \((x_0,y_0,s_f)\) set is deterministic but not the exact source-locked BH050 face registration. Therefore this result is a registration diagnostic.

### Gate B — formal R06 global-maximum certificate

The executed diagnostic used the exact finite-harmonic stress field plus deterministic spatial seeds and continuous local extremum optimization to locate maximum Mises stress. This is not formal spatial quadrature, not a material-point grid, and not effective-width theory. However, it has not yet supplied the complete finite-algebraic enumeration of every interior/edge/corner stationary root required by the frozen R06 theorem-level global-maximum certificate.

Accordingly, the correct current identity is

\[
\boxed{P_{fold}^{C1-PBL/qU,\ registration\ diagnostic}\approx15.36\ \mathrm{MN}}
\]

and **not** a new production \(P_u\).

## 9. Locked interpretation from this execution

1. C1-PBL plus independent cell amplitudes materially changes steel-shell longitudinal membrane-force participation.
2. The first-order change does not come merely from partitioning a face into bays; it comes from the global-local `qU` kinematic coupling.
3. PBL must remain a displacement/rotation-compatible C1 line, not a full-curvature lock.
4. The current model has largely addressed the old low-total-steel-force symptom, but a strong top/bottom steel-face asymmetry remains.
5. The next required diagnostic is therefore not another local shape-function invention. It is a fold dissection by face/bay/cell and by J4 singular direction.

## 10. Immediate continuation target

At/near \(q\approx0.00702570\), extract per-cell and aggregate quantities at minimum:

- face;
- bay index;
- axial cell index;
- \(L_x,L_y,x_0,y_0,s_f\);
- \(A_{0b}\);
- solved \(U_b\);
- localization/amplitude measure \(\lambda_b\) if defined by the frozen kernel;
- cell mean longitudinal membrane stress \(\bar\sigma_y^b\);
- relevant local tangent contribution.

Then compute the smallest left/right singular vectors of the R4 Jacobian and identify which generalized balance direction collapses. Where the existing finite-algebraic assembly permits exact component removal/reassembly, decompose the directional tangent by top face, bottom face, web and UHPC, and then by bay. This is diagnostic decomposition only; do not modify the frozen equilibrium equations during attribution.
