# BH100 corrected multiaxial UHPC damage-activation trial — result

## Scope
This run changes **only** the UHPC multiaxial driver used to feed the existing ABS/raw UC141 damage/plastic functions. Steel predictor/corrector, geometry, whole-face N=m=4 topology, material constants and P=PU+Ps+ + Ps- are kept as in the BH100 13.40-MN A/B path.

Rejected driver:
[
eta_t^{old}=langlearepsilon_1angle_+,qquad
eta_c^{old}=langle-arepsilon_2angle_+.
]

Corrected plane-stress equivalent-uniaxial driver:
[
oxed{eta_t^{eq}=rac{langlearepsilon_1+
u_carepsilon_2angle_+}{1-
u_c^2}},
qquad
oxed{eta_c^{eq}=rac{langle-arepsilon_2-
u_carepsilon_1angle_+}{1-
u_c^2}}.
]
For pure uniaxial compression this gives (eta_t^{eq}=0), so Poisson lateral expansion no longer creates tensile damage. For uniaxial tension/compression the original UC141 uniaxial total-strain calibration is recovered exactly.

## Peak
BOTTOM trial whole-face Mises first reaches 355 MPa at
[
oxed{w_u=82.15506222 {m mm}}.
]
Immediately before the event the total load is still increasing; immediately after the BOTTOM corrector activates and the total load decreases. Thus the first external maximum is the cusp at this real yield root:
[
oxed{P_u=15.61115 {m MN}}.
]

At the peak:
[
P_U=7.21811 {m MN},quad
P_s^+=2.96108 {m MN},quad
P_s^-=5.43196 {m MN}.
]

UHPC state:
[
ho_A=0.8533161,quad
ho_D=0.7715349,quad
w_P=31.59680 {m mm}.
]
Equivalent-strain extrema:
[
eta_{t,max}^{eq}=0.00123863,qquad
eta_{c,max}^{eq}=0.00157270.
]

TOP steel:
[
A^+=4.4312342 {m mm},quad
e^+=1.8956005 {m mm},quad
A_P^+=2.5356337 {m mm},
]
[
arsigma_y^+=148.05383 {m MPa},qquad
maxsigma_{VM}^+=355.0000 {m MPa}.
]
The unreduced TOP predictor would reach about 446.08 MPa.

BOTTOM steel:
[
A^-=4.6598346 {m mm},quad e^-=A^-,
]
[
arsigma_y^-=271.59798 {m MPa},qquad
maxsigma_{VM}^-=355.0000 {m MPa}.
]

## Direct A/B against the rejected old strain driver at the same w
Old principal-total-strain driver at (w=82.1551) mm:
[
ho_A=0.7540082,quad
ho_D=0.6822918,quad
w_P=45.35476 {m mm},quad
P_U=5.00809 {m MN}.
]

Corrected driver:
[
ho_A=0.8533161,quad
ho_D=0.7715349,quad
w_P=31.59680 {m mm},quad
P_U=7.21811 {m MN}.
]

Therefore the correction:
- recovers about 9.93 percentage points of membrane-stiffness retention;
- recovers about 8.92 percentage points of bending-stiffness retention;
- reduces the projected plastic reference imperfection by about 30.33%;
- raises the UHPC axial contribution at this state by about 44.13%.

## Peak-neighborhood monotonicity
[
P(82.1051)=15.60666 {m MN},
]
[
P(82.1451)=15.61025 {m MN},
]
[
P(82.1551)=15.61115 {m MN},
]
[
P(82.1651)=15.61084 {m MN},
]
[
P(82.2051)=15.60960 {m MN}.
]
So the maximum is not produced by a coarse w-grid.

## Numerical-evaluator convergence
At the same peak root, the continuous-integral evaluator was checked with increasing quadrature order only as an independent numerical evaluator:
- order 80: 15.611354 MN
- order 100: 15.611207 MN
- order 120: 15.611129 MN
- order 160: 15.611147 MN
- order 200: 15.611181 MN

The theory definition remains the continuous area integrals for (ho_A,ho_D,w_P); fixed spatial integration points are not part of the constitutive/model definition. Production implementation still has to be replaced by the previously derived level-set + one-dimensional deterministic integral backend.

## Post-freeze comparison only
The already-extracted BH100 DIRECT peak is 13.486 MN. After freezing the theoretical result, the corrected trial is therefore about +15.76% high. This comparison was not used in any root or material-state calculation.

## Interpretation
The Poisson false-cracking diagnosis was real: correcting it materially restores UHPC stiffness and plastic-reference state. However, it also proves that the former 13.40-MN agreement with DIRECT was not a robust validation; it contained compensating errors. The next audit must therefore target load partition and the steel/global-local branch rather than re-introducing false tensile damage.
