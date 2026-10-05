# BH100 restored peak-rebased UHPC + continuous local-Mises steel result

Status: PROVISIONAL / MECHANISM AUDIT ONLY

This run restores the locked peak-rebased UHPC damage/plastic-reference path exactly and combines it with the candidate continuous local Mises-cap steel operator.

No FEM/test value entered the solve.

## 1. UHPC regression gate — PASSED

At w = 82.2 mm:

rho_A = 0.97921043
rho_D = 0.96641992
w_P = 10.330668 mm
P_UHPC = 10.569428 MN

This reproduces the previously locked BH100 peak-rebased UHPC state (about rho_A=0.97921, rho_D=0.96642, w_P=10.33 mm, P_U≈10.57 MN).

Therefore the accidental ABS/raw damage-plastic reversion is removed.

## 2. Steel state at the same w = 82.2 mm

Predictor amplitudes:
A_TOP = 4.434799 mm
A_BOTTOM = 4.660565 mm

Yun predictor means:
TOP = 251.401 MPa
BOTTOM = 271.665 MPa

Global elastic face means:
TOP = 223.961 MPa
BOTTOM = 299.286 MPa

After the continuous local Mises-cap integral:
TOP mean = 246.978 MPa
BOTTOM mean = 271.665 MPa

Steel forces:
P_TOP = 4.93956 MN
P_BOTTOM = 5.43330 MN

UHPC:
P_U = 10.56943 MN

Total:
P(82.2) = 20.94229 MN

Local-cap active area fractions:
TOP ≈ 19.6 percent
BOTTOM = 0

Global-only yield fractions in the numerical evaluator:
TOP ≈ 7.2 percent
BOTTOM = 0

Steel resultant eccentricity about the UHPC mid-plane is only about 1.09 mm, so the previous artificial TOP/BOTTOM whole-face split is removed.

## 3. Recomputed branch

Representative points:
w=20 mm: P=5.89372 MN
w=40 mm: P=9.99991 MN
w=60 mm: P=15.00110 MN
w=80 mm: P=20.37053 MN
w=82.2 mm: P=20.94229 MN
w=90 mm: P=22.83888 MN
w=100 mm: P=24.70349 MN
w=110 mm: P=25.77260 MN
w=120 mm: P=26.36593 MN
w=130 mm: P=26.70165 MN
w=140 mm: P=26.85969 MN
w≈142.3 mm: P≈26.873 MN
w=150 mm: P≈26.660 MN
w=160 mm: P≈25.582 MN
w=180 mm: P≈22.672 MN

## 4. First external maximum of this candidate branch

Refined numerical evaluation places the maximum near

w_u ≈ 142.3 mm
P_u ≈ 26.873 MN

A representative high-order state at w=142.30 mm gives approximately:

P_UHPC = 14.0698 MN
P_TOP = 6.1472 MN
P_BOTTOM = 6.6557 MN

rho_A = 0.86181
rho_D = 0.82880
w_P = 79.02 mm

A_TOP ≈ 7.326 mm
A_BOTTOM ≈ 7.536 mm

mean TOP steel stress ≈ 307.4 MPa
mean BOTTOM steel stress ≈ 332.8 MPa

steel resultant eccentricity ≈ 0.91 mm

local-cap active fractions are roughly:
TOP ≈ 78 percent
BOTTOM ≈ 36 percent

At this point the global elastic trial is over the Mises surface essentially everywhere on both faces, so the global current-state cap is active over the full face.

## 5. Numerical evaluator convergence

The theory definition remains continuous surface/thickness integrals and algebraic yield boundaries. Fixed quadrature points are not constitutive states.

At w=142.30 mm, independent evaluator orders gave total loads approximately:

UHPC 80 / steel 56: 26.87270 MN
100 / 64: 26.87290 MN
120 / 80: 26.87279 MN
140 / 88: 26.87220 MN
160 / 96: 26.87269 MN
180 / 144: 26.87399 MN
220 / 160: 26.87193 MN
240 / 192: 26.87343 MN

Thus a practical numerical uncertainty of about ±0.002 MN is assigned to the present audit value.

## 6. Interpretation

The UHPC module is now back on the intended peak-rebased route. The very high total load therefore cannot be blamed on the previous ABS/raw UHPC reversion.

The continuous local Mises-cap repair still removes the artificial whole-face TOP collapse, but once that collapse is removed the steel/global branch carries too much total force. The remaining dominant inconsistency is the steel predictor / mean-stress identity: the Yun whole-face predictor is still being used as a total face mean while the global base already carries the overall axial demand.

Therefore this 26.87-MN branch is NOT accepted as final UCFT theory.

BH085 and smaller cases remain paused.

Next audit target:
retain the restored peak-rebased UHPC and continuous local Mises cap, but re-derive the steel global-base / Yun-local mean compatibility so that Yun contributes only the true local increment and does not duplicate the global axial demand.
