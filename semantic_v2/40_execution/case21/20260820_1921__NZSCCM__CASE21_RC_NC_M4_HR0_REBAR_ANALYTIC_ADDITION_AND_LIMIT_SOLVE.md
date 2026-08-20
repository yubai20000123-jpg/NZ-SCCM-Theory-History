# NZ-SCCM — Case21 NC-M4 + 中置双向钢筋(hr=0)解析叠加与极限重求

时间：2026-08-20 19:21 +08:00

状态：`FORMAL_REBAR_ANALYTIC_ADDITION = PASS`; `RC_LIMIT_DIRECT_CONTINUOUS_AUDIT = PASS_NONPRODUCTION`

## 1. Case21 source inputs used

From Nguyen Table 5.1 transcription:

- b = ell = 1220 mm for the representative square half-wave used by the current NZ-SCCM branch;
- h = 19.30 mm;
- fc = 21.23 MPa;
- E0 = 20321 MPa;
- eps_c0 = 0.00209;
- nominal total reinforcement ratio p = 0.75%;
- source reinforcement layer count = 1;
- source reinforcement offset = hr = 0;
- steel Es = 200000 MPa;
- steel yield strain = 0.00265, hence fy = 530 MPa.

Project rule for missing concrete tensile strength: ft = 0.1 fc. NC-M4 initial-tangent consistency: eps_t0 = 0.0967635 ft/E0.

The nominal total reinforcement ratio is split equally between orthogonal directions, so

rho_x = rho_y = p/2 = 0.00375.

The general bookkeeping remains two layers; for Case21 hr=0 so the two bookkeeping layers coincide and their areas sum to the original single physical layer. No area doubling is permitted.

Define the equivalent reinforcement thickness in each direction

\[
t_s=\rho_d h=(p/2)h.
\]

For Case21

\[
t_s=0.00375\times19.30=0.072375\ \mathrm{mm}.
\]

## 2. hr=0 reinforcement strains

Let

\[
S=A_0A+\frac12A^2,\qquad H=A_0+A.
\]

For the x bars

\[
\varepsilon_{sx}=\varepsilon_m+S\frac{\pi^2}{b^2}\cos^2X\sin^2Y,
\]

and for the loading-direction y bars

\[
\varepsilon_{sy}=-\frac{\Delta}{\ell}+S\frac{\pi^2}{\ell^2}\sin^2X\cos^2Y.
\]

Their A-derivative kernels are

\[
G_{sx}=H\frac{\pi^2}{b^2}\cos^2X\sin^2Y,
\qquad
G_{sy}=H\frac{\pi^2}{\ell^2}\sin^2X\cos^2Y.
\]

Steel is elastic-perfectly-plastic:

\[
\sigma_s=E_s\varepsilon_s\quad (|\varepsilon_s|\le\varepsilon_y),
\]

with saturation at +/-fy beyond yield.

At the final RC audit root all steel strains satisfy |eps_s| < 0.000884 << 0.00265, so the entire reinforcement field is elastic. Therefore the reinforcement additions below are exact elementary integrals with no state-front subdivision.

## 3. Exact reinforcement integrals for general rectangular b x ell, hr=0

Using

\[
\int_0^b\!\int_0^\ell \cos^2X\sin^2Y\,dy\,dx=\frac{b\ell}{4},
\]

\[
\int_0^b\!\int_0^\ell \cos^4X\sin^4Y\,dy\,dx=\frac{9b\ell}{64},
\]

and the corresponding x/y-swapped identities, the exact reinforcement terms are

\[
\boxed{R_{m,s}=t_sE_sb\ell\left(\varepsilon_m+\frac{\pi^2S}{4b^2}\right).}
\]

\[
\boxed{P_s=t_sE_sb\left(\frac{\Delta}{\ell}-\frac{\pi^2S}{4\ell^2}\right).}
\]

\[
\boxed{
R_{A,s}=t_sE_sHb\ell\left[
\frac{\pi^2\varepsilon_m}{4b^2}
-\frac{\pi^2\Delta}{4\ell^3}
+\frac{9\pi^4S}{64}\left(\frac1{b^4}+\frac1{\ell^4}\right)
\right].}
\]

For Case21 b=ell=B these reduce to

\[
\boxed{R_{m,s}=t_sE_s\left(B^2\varepsilon_m+\frac{\pi^2S}{4}\right),}
\]

\[
\boxed{P_s=t_sE_s\left(\Delta-\frac{\pi^2S}{4B}\right),}
\]

\[
\boxed{R_{A,s}=t_sE_sH\left[
\frac{\pi^2}{4}\left(\varepsilon_m-\frac{\Delta}{B}\right)
+\frac{9\pi^4S}{32B^2}
\right].}
\]

No spatial integration remains in the reinforcement terms.

## 4. Exact same-source derivatives of the reinforcement terms, Case21

With dS/dA = H and dH/dA = 1:

\[
R_{m,s,\Delta}=0,
\qquad
R_{m,s,m}=t_sE_sB^2,
\qquad
R_{m,s,A}=t_sE_s\frac{\pi^2H}{4}.
\]

\[
P_{s,\Delta}=t_sE_s,
\qquad
P_{s,m}=0,
\qquad
P_{s,A}=-t_sE_s\frac{\pi^2H}{4B}.
\]

Define

\[
F_s=\frac{\pi^2}{4}\left(\varepsilon_m-\frac{\Delta}{B}\right)+\frac{9\pi^4S}{32B^2}.
\]

Then

\[
R_{A,s,\Delta}=-t_sE_sH\frac{\pi^2}{4B},
\]

\[
R_{A,s,m}=t_sE_sH\frac{\pi^2}{4},
\]

\[
R_{A,s,A}=t_sE_s\left[F_s+\frac{9\pi^4H^2}{32B^2}\right].
\]

## 5. Combined concrete + reinforcement system

The formal concrete functions remain the exact no-spatial-integral NC-M4 shared-GKZ functions `R_m,c`, `P_c`, `R_A,c`.

The reinforced system is simply

\[
\boxed{R_m=R_{m,c}+R_{m,s},}
\]

\[
\boxed{P=P_c+P_s,}
\]

\[
\boxed{R_A=R_{A,c}+R_{A,s}.}
\]

The unknowns remain only

\[
(\Delta,A,\varepsilon_m).
\]

The final three equations remain

\[
R_A=0,\qquad R_m=0,\qquad \det J_{lim}=0,
\]

with the total same-source derivatives obtained by direct addition of the concrete GKZ derivatives and the exact elementary reinforcement derivatives above.

## 6. Independent direct-continuous RC audit

For numerical audit only, the continuous NC-M4 concrete field was evaluated by converging tensor-product Gauss quadrature, while the reinforcement contribution was inserted using the exact closed forms above. Finite-difference derivatives were used only to audit the fold; neither device has production identity.

Convergence of the RC load maximum:

| concrete audit order X x Y x zeta | Delta_u (mm) | A_u (mm) | eps_m | Pu (kN) |
|---|---:|---:|---:|---:|
|28 x 28 x 18|1.0785758|2.8743342|-3.27015e-5|286.09765|
|32 x 32 x 20|1.0780479|2.8706229|-3.26416e-5|286.07829|
|36 x 36 x 24|1.0780673|2.8657105|-3.25314e-5|286.11119|
|40 x 40 x 28|1.0784048|2.8680529|-3.25694e-5|286.12467|
|44 x 44 x 30|1.0782630|2.8681011|-3.25890e-5|286.12632|
|48 x 48 x 34|1.0784140|2.8692766|-3.25941e-5|286.11711|

Use 44x44x30 as the detailed audit checkpoint:

\[
\boxed{\Delta_u^{audit}=1.07826297\ \mathrm{mm}},
\]

\[
\boxed{A_u^{audit}=2.86810110\ \mathrm{mm}},
\]

\[
\boxed{\varepsilon_{m,u}^{audit}=-3.25889600\times10^{-5}},
\]

\[
\boxed{P_u^{RC,audit}=286.1263169\ \mathrm{kN}}.
\]

At this root:

- concrete load contribution `P_c = 270.8949590 kN`;
- reinforcement loading-direction contribution `P_s = 15.2313578 kN`;
- total `P = 286.1263169 kN`;
- concrete and reinforcement transverse generalized resultants cancel: `R_m,c = +242787.39885`, `R_m,s = -242787.39885`;
- concrete and reinforcement A-residuals cancel: `R_A,c = +173.4220155`, `R_A,s = -173.4220155`.

Steel strain/stress audit:

\[
\varepsilon_{sx}\in[-3.25890\times10^{-5},\ 5.26906\times10^{-5}],
\]

\[
\varepsilon_{sy}\in[-8.83822\times10^{-4},\ -7.98543\times10^{-4}],
\]

hence

\[
\sigma_{sx}\in[-6.518,10.538]\ \mathrm{MPa},
\]

\[
\sigma_{sy}\in[-176.764,-159.709]\ \mathrm{MPa},
\]

well below `fy = 530 MPa`, proving the elastic closed forms are self-consistent at the root.

Audit limit Jacobian (rows P, R_A, R_m; columns Delta,A,eps_m):

\[
J_{lim}^{audit}\approx
\begin{bmatrix}
1.98213\times10^5&-4.28879\times10^4&-1.64967\times10^9\\
-1.90703\times10^3&4.25794\times10^2&2.31411\times10^7\\
-1.17100\times10^6&1.34512\times10^6&6.12619\times10^{11}
\end{bmatrix}.
\]

Row-normalized determinant:

\[
\det_{norm}J_{lim}\approx-2.36\times10^{-16}.
\]

The constraint block determinant is nonzero, so the root is an ordinary fold. The implied path derivative from `det J_lim/det J_c` is approximately `-0.024 N/mm`, numerically zero on the load scale.

Local equilibrium-branch check:

\[
P(\Delta_u-0.005)=286.1111582\ \mathrm{kN},
\]

\[
P(\Delta_u)=286.1263169\ \mathrm{kN},
\]

\[
P(\Delta_u+0.005)=286.1107181\ \mathrm{kN}.
\]

Central curvature:

\[
\boxed{d^2P/d\Delta^2\approx-1230.30\ \mathrm{kN/mm^2}<0,}
\]

so the audited root is a local maximum.

## 7. Interpretation

The previous pure-concrete diagnostic maximum was about `288.7205 kN`; adding the source-consistent mid-plane reinforcement changes the audited peak to about `286.12 kN`, a change of about `-0.90%`. Although the y-bars directly contribute about `+15.23 kN` at the RC root, the transverse bars alter the `R_m=0` compatibility/equilibrium state, shifting `(Delta,A,eps_m)` and reducing the concrete contribution. This small net effect is qualitatively consistent with Nguyen Chapter 5's statement that reinforcement had no considerable effect on the buckling loads.

For reference only, Swartz Case21 experimental load is 336 kN and Nguyen FE value is 298 kN; the present RC audit value is about -14.84% vs experiment and -3.98% vs Nguyen FE. Experimental loads are not used in solving or selecting the root.

## 8. Formal status

- `CASE21_REBAR_HR0_ANALYTIC_INTEGRATION = PASS`.
- `STEEL_ELASTIC_AT_LIMIT = VERIFIED`.
- `TOTAL_3VAR_SYSTEM_WITH_REBAR = CLOSED`.
- Numerical `286.12 kN` is still labeled `DIRECT_CONTINUOUS_AUDIT`, because the current session has not yet executed the numerical evaluator for the exact concrete shared-GKZ derivatives. The formal theory itself contains no spatial steel quadrature and no new structural unknowns.
