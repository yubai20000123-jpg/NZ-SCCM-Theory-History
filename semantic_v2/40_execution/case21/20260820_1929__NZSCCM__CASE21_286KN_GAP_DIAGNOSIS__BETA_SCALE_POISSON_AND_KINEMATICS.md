# NZ-SCCM — Case21 286 kN gap diagnosis: beta-scale, Poisson coupling, and kinematic mismatch

Time: 2026-08-20 19:29 +08:00

Status: `286KN_CASE21_BENCHMARK = WITHDRAWN`; `INTEGRATION_ERROR = NOT_PRIMARY`; `NC_M4_MATERIAL_AND_KINEMATICS_REPAIR_REQUIRED`

## 1. Comparator correction

For Case21 the experimental buckling onset and ultimate/failure load are different quantities:

- experimental buckling onset: about 336.286 kN;
- experimental failure/ultimate: 82.8 kip = 368.312750 kN.

The current three-variable fold result is an ultimate-load candidate, therefore it must be compared with 368.312750 kN, not 336 kN.

Current NC-M4 + hr=0 rebar audit:

\[
P_u^{current}=286.1263\ \mathrm{kN},
\]

so the gap to the ultimate experiment is

\[
\Delta P=-82.1864\ \mathrm{kN},\qquad -22.314\%.
\]

The 336-kN comparison in the immediately preceding execution report was a load-type labeling error and is superseded.

## 2. Decisive material-scale error in TC/CT beta

NC-M2 originally defined the tensile coordinate for both tension and TC compression reduction as

\[
t=\varepsilon_t/\varepsilon_{cr}.
\]

NC-M4 changed the tensile shape coordinate to

\[
t_T=\varepsilon_t/\varepsilon_{t0}
\]

for the new T4 law, but retained

\[
\beta(t)=\frac1{1+0.15t^2}
\]

using that same newly scaled t. For Case21, under the current initial-tangent rule,

\[
\varepsilon_{t0}=0.0967635\frac{f_t}{E_0}
=1.0109193\times10^{-5},
\]

whereas

\[
\varepsilon_{cr}=f_t/E_0=1.0447321\times10^{-4}.
\]

Thus the beta coordinate was compressed by a factor about 10.334 without recalibrating beta.

### Pointwise same-state proof

Use the previously successful full-coupled Case21 R10 limit field at the plate center/midsurface. It has normalized principal strains

\[
e_1=+0.142383751750872,\qquad e_2=-0.787651836809646,
\]

with physical strain scale eps0=0.00209. Therefore

\[
\varepsilon_1=2.97582041\times10^{-4},
\qquad
c_2=0.7876518368.
\]

With current NC-M4:

\[
t_T=\varepsilon_1/\varepsilon_{t0}=29.4367752,
\]

\[
\beta_{M4}=\frac1{1+0.15t_T^2}=0.00763484,
\]

and

\[
C(c_2)=\frac{2c_2}{1+c_2^2}=0.97217238.
\]

Hence the current TC axial compression is only

\[
\boxed{\sigma_{2,M4}=-21.23(0.00763484)(0.97217238)=-0.15758\ \mathrm{MPa}}.
\]

At the identical state, the previously source-consistent R10 operator gives approximately

\[
\boxed{\sigma_{2,R10}=-20.60002\ \mathrm{MPa}}.
\]

The discrepancy is a factor about 130.73.

Crucially, the NC-M4 compression skeleton itself is not the problem. With beta removed at this state,

\[
-f_cC(c_2)=-20.63922\ \mathrm{MPa},
\]

which is within about 0.2% of the old R10 value. Therefore the catastrophic loss of axial compression is specifically caused by the TC beta treatment, not by C(c).

If one merely restores the old M2 coordinate `t_beta=eps_t/eps_cr`, then at this same state

\[
t_\beta=2.8484054,\qquad \beta=0.4510576,
\]

and

\[
\sigma_2\approx-9.3095\ \mathrm{MPa},
\]

which is still far below -20.600 MPa. Therefore there are two nested issues:

1. a definite scale-wiring error from reusing the new T4 coordinate inside beta;
2. even the simplified beta function itself is too punitive relative to the previously accepted source-consistent TC response on the Case21 reachable strain range.

## 3. Initial Poisson coupling was lost in NC-M4

The current NC-M4 principal laws are essentially independent scalar normal-stress functions plus the beta/eta modifiers. The parameter nu does not appear in the material operator.

Consequently, in the infinitesimal uniaxial-compression limit with zero transverse stress, the new operator tends toward transverse strain approximately zero, not the source-consistent plane-stress dilation

\[
\varepsilon_x\approx-\nu\varepsilon_y.
\]

This is visible directly in the roots:

- current low RC root: `epsilon_m = -3.2589e-5` (transverse compression);
- old successful coupled field at center/midsurface: `epsilon_x = +2.9758e-4` (transverse dilation) while transverse stress is near zero.

Nguyen's source TC implementation contains cross-principal coupling and shear-retention/tangent terms; it is not equivalent to two independent scalar principal laws. Hence the current Rm=0 equation is solving against a materially different biaxial tangent structure.

This explains why the current solver moves epsilon_m negative: it is trying to avoid the severe TC beta penalty and satisfy zero transverse resultant in an operator that no longer has the correct Poisson/biaxial coupling.

## 4. Structural kinematics are also not identical to the previously successful compatible field

The earlier successful Case21 formulation used a third in-plane/Airy redistribution variable alpha in addition to axial shortening D and out-of-plane amplitude q. The current formulation replaced that nonuniform in-plane compatibility field by one uniform transverse membrane strain epsilon_m.

For a square halfwave, writing u=sin X, v=sin Y, the current midsurface x-strain can only have the form

\[
\varepsilon_x^0/\varepsilon_0=e_m+M(v^2-u^2v^2),
\]

so its polynomial coefficients must satisfy

- standalone u^2 coefficient = 0;
- coefficient(v^2) = -coefficient(u^2 v^2).

The old successful limit field instead had

\[
e_x=0.1413559193
-0.00022562175u^2
+0.02781688062v^2
-0.02656342645u^2v^2
+0.06754686156uv\zeta.
\]

No choice of a single e_m and M can reproduce these coefficients exactly. The y-strain and shear have the same incompatibility. Therefore the new `(Delta,A,epsilon_m)` structural subspace is not an exact condensation of the old `(D,q,alpha)` compatible field; it is a genuine kinematic reduction.

Previous formal Airy-restored zero-spatial calculations gave Case21 ultimate loads about 365.257-366.768 kN without experiment-based root selection, showing that the full compatible in-plane redistribution materially affects the correct branch.

## 5. Reinforcement is secondary, not the source of the 82-kN gap

Current RC audit decomposition:

\[
P_c\approx270.895\ \mathrm{kN},\qquad P_s\approx15.231\ \mathrm{kN}.
\]

Previously successful coupled result:

\[
P_c\approx337.923\ \mathrm{kN},\qquad P_s\approx28.845\ \mathrm{kN}.
\]

Differences:

\[
\Delta P_c\approx-67.03\ \mathrm{kN},
\qquad
\Delta P_s\approx-13.61\ \mathrm{kN}.
\]

Thus most of the load deficit is concrete/branch physics. The exact hr=0 steel integration itself is not the dominant error source.

## 6. Integration error is not the primary cause

The current direct-continuous audit converged tightly around 286.12 kN as the audit quadrature order was increased. Therefore the 82-kN discrepancy is not plausibly a numerical integration truncation of the current equations. The current equations themselves produce the low branch.

## 7. Governance decision

The value `Pu = 286.12 kN` is retained only as the numerical solution of the current NC-M4 + reduced-kinematics equations. It is withdrawn as a valid Case21 benchmark prediction.

The next work must not tune ft, the reinforcement, or choose a different root using experiment. It must repair/audit the two model layers in controlled order:

1. **Material gate:** separate the tensile-shape coordinate `t_T=eps_t/eps_t0` from the TC compression-interaction coordinate. Restore a source-constrained TC relation and the small-strain Poisson/biaxial coupling; verify pointwise against the previously accepted R10/Nguyen operator over the reachable Case21 strain domain. The minimal correction cannot simply reuse `eps_t0` inside beta.
2. **Kinematics gate:** determine whether the uniform `epsilon_m` field can be derived as an exact condensation of the Airy-compatible in-plane field. The coefficient comparison above shows the present form cannot. Therefore either restore the compatible Airy in-plane variable/field or derive an exact equivalent condensed representation before recomputing Pu.

Only after both gates pass should Case21 be recomputed, with the experimental 368.312750 kN read only after the root is fixed.
