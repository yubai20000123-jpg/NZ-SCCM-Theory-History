# UCFT M8a — final-INP UHPC material reintegration into analytic/rational-Y operator

Timestamp: 2026-09-30 22:35 +08:00

## 1. Scope
This is not a new theory gate. The user supplied the actual final Abaqus INP material definition `UHPC_UC141`; M8 therefore rebinds the already-passed M4/M8 analytic active-set operator to this material input before the fixed-q path solver is assembled.

No FEM/experimental Pu target is used.

## 2. Frozen material provenance
- density = 2.5e-09 tonne/mm3
- E = 43400 MPa
- nu = 0.30
- CDP: psi=36 deg, eccentricity=0.1, fb0/fc0=1.16, Kc=0.6667, viscosity=1e-5
- compression hardening: user-provided final-INP table
- tension stiffening STRAIN: user-provided final-INP table
- compression/tension damage tables: retained as FEM provenance only; not silently converted into the current low-dimensional history-free material operator.

Abaqus total strains used by the low-dimensional stress law are reconstructed as
[
\varepsilon_{tot}^{c}=\varepsilon_{inel}+\sigma_c/E,
\qquad
\varepsilon_{tot}^{t}=\varepsilon_{cr}+\sigma_t/E.
]
With UCFT sign convention tension positive / compression negative:
- compression peak = 141.1 MPa at total compressive strain 0.003500000073732719;
- tension peak = 7.3 MPa at total tensile strain 0.0009722027649769585.
The quoted 0.000804 is the Abaqus cracking strain at the tensile peak, not total strain.

The exact tabular monotonic backbone is represented as a piecewise-linear law in total strain. Each branch is a degree-1 polynomial; its stress primitive F and first strain moment primitive H are exact polynomials. Therefore the existing M4/M8 active-set architecture remains valid and actually becomes algebraically simpler than the previous source-scaled cubic tensile surrogate.

## 3. Rational-Y regression with the actual INP backbone
Three fixed-X tests were run:
1. baseline C1-like field;
2. high-harmonic C/S/B-like field with k=7,9,16;
3. mixed field with k=8,16 plus odd S harmonics.

For each state:
- face threshold roots are obtained algebraically by t=tan(Y/2);
- thickness integration uses exact branch primitives;
- Y integration uses the recovered Fourier/rational primitive operator;
- an independent diagnostic nested integration was used only as verification, not as the production definition.

Results:

| test | active Y cuts | max relative difference |
|---|---:|---:|
| baseline | 22 | 4.3564168e-09 |
| highharm | 60 | 1.9992804e-09 |
| mixed | 64 | 6.4278613e-10 |

Global maximum relative difference:
[
4.3564168\times 10^{-9}.
]

Thus:
[
\boxed{\mathrm{UHPC\_UC141\ actual\ INP\ rational-Y\ integration}=PASS}
]

No 2D/3D Gauss material integration has been introduced into the production definition.

## 4. Steel M5 regression
Using the already-frozen Q355 ideal elastic-perfectly plastic equivalent law:
[
P_s(\bar\varepsilon)=
\begin{cases}
E_s\bar\varepsilon,&\bar\varepsilon\le f_y/E_s,\\
f_y,&\bar\varepsilon>f_y/E_s,
\end{cases}
]
with E_s=206000 MPa, nu_s=0.30, f_y=355 MPa:

- exact thickness resultants vs independent numerical diagnostic:
  - elastic state: N relative error 0; M ~5.55e-17;
  - plastic state 1: N ~1.42e-16; M ~4.19e-14;
  - plastic state 2: N ~1.41e-16; M ~1.11e-14.
- consistent tangent finite-difference checks:
  - elastic: 2.47e-11;
  - plastic: 1.42e-10.

So the current M5 kernel remains compatible with the new UHPC input.

## 5. Important solver-interface correction now frozen
Any older prototype that still hard-codes nu_c=0.20 or the former ~7.2 MPa surrogate tensile law is NOT an M8 production solver.

M8 production must use:
[
E_c=43400\;\mathrm{MPa},\qquad \nu_c=0.30,
]
and the final-INP tabular backbone above.

The damage tables and CDP flow-potential constants are retained for FEM provenance and later constitutive audit, but are not inserted as additional history variables into the current directional low-dimensional operator without an explicit material-theory upgrade.

## 6. Status
- M0–M7: PASS
- M8_INPUT_FREEZE: PASS, updated to final-INP UHPC_UC141
- M8_RATIONAL_Y_OPERATOR: PASS with final-INP tabular backbone
- M8_M5_STEEL_OPERATOR: PASS
- M8_PATH_SOLVER: PARTIAL
- M9: NOT STARTED

## 7. Unique NEXT_ACTION
Assemble the full fixed-q evaluator:
[
(\boldsymbol\xi,P,A^+,A^-;q)\mapsto
(\mathbf G,R_q,R_{A^+},R_{A^-},J),
]
using the now-frozen actual-INP UHPC operator, M3 compatible enrichment, M5 steel operator and exact M6 Schur interface.

Immediately after that evaluator passes zero-state/linear regression already covered by M7, execute BH005:
perfect-local A0=0 N,m identification -> restore A0=0.225b/1600 coefficient -> imperfect connected q-path.

No new theory gate is introduced.
