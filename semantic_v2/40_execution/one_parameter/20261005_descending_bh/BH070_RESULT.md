# BH070 current-path calculation result

## Inputs
[
b=3500 {m mm},quad a_h=7000 {m mm},quad w_0=8.75 {m mm},
]
[
t_c=42 {m mm},quad t_s=4 {m mm},quad
A_0^pm=0.4921875 {m mm},quad N_pm=m_pm=4.
]

The material/state-update route is the same ABS/raw current path frozen in `CURRENT_PATH_SPEC.md`.

## Search
The complete coarse curve was evaluated over (w=0,5,ldots,90) mm. Peak neighborhood was then evaluated at 1 mm intervals. BOTTOM predictor Mises rises from 351.878 MPa at (w=49) mm to 359.945 MPa at (w=50) mm.

Solving
[
maxsigma_{m VM,BOT}^{trial}(w)-355=0
]
gives
[
oxed{w_u=49.38881691 {m mm}}.
]

Direct checks:
- (w=49.36): (P=9.5176967) MN, BOTTOM elastic;
- (w=w_u): (P=9.51795) MN;
- (w=49.42): (P=9.5148145) MN, BOTTOM local/global-yield.

Therefore the current theoretical peak again occurs at the real BOTTOM first-yield transition.

## Frozen peak state
[
oxed{P_u^{BH070}=9.51798 {m MN}},
qquad
oxed{w_u=49.38881691 {m mm}}.
]

Components:
[
P_U=3.496676 {m MN},qquad
P_s^+=1.793752 {m MN},qquad
P_s^-=4.227550 {m MN}.
]

UHPC:
[
ho_A=0.72601482,qquad
ho_D=0.66225533,qquad
w_P=26.30766 {m mm}.
]

TOP:
[
A^+=3.0143558 {m mm},quad
e^+=1.0235071 {m mm},quad
A_P^+=1.9908487 {m mm},
]
[
sigma_{m VM,max}^+=355.0000 {m MPa},
]
while its full-recovery predictor reaches 477.076 MPa.

BOTTOM:
[
A^-=3.2350308 {m mm},
quad e^-approx A^-,
quad sigma_{m VM,max}^-=355.0000 {m MPa}.
]

## UHPC integration convergence at (w_u)
- nq=80: 9.51797834 MN
- nq=100: 9.51794735 MN
- nq=120: 9.51794969 MN
- nq=160: 9.51797808 MN

The small non-monotone last digits come from the piecewise material-table breakpoints crossing quadrature abscissae; the spread is (3.1	imes10^{-5}) MN (about (3.3	imes10^{-4}%)). Frozen reporting precision is 9.51798 MN.

## Post-peak
The same path decreases after the BOTTOM yield event:
- (w=50): (Papprox9.4559) MN;
- (w=55): (Papprox8.8777) MN;
- (w=60): (Papprox8.0836) MN.

No FEM/test value entered the solve.
