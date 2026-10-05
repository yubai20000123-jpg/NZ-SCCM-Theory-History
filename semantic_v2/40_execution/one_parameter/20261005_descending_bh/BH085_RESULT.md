# BH085 current-path calculation result

## Inputs
[
b=4250 {m mm},quad a_h=8500 {m mm},quad t_c=42 {m mm},quad t_s=4 {m mm},
]
[
w_0=10.625 {m mm},quad A_0^pm=0.59765625 {m mm},
quad N_pm=m_pm=4.
]

Material and state-update route are exactly those frozen in `CURRENT_PATH_SPEC.md` (ABS/raw UC141 current-state path).

## Search
A coarse full curve was evaluated over (w=0,5,ldots,105) mm. The load rises through (w=65) mm, and the BOTTOM elastic predictor reaches the Mises surface between 66 and 67 mm. The event equation
[
maxsigma_{m VM,BOT}^{trial}(w)-355=0
]
has the positive root
[
oxed{w_u=66.36008521 {m mm}}.
]
Direct evaluations immediately to both sides give:
- (w=66.34): (P=11.4103400) MN, BOTTOM elastic;
- (w=w_u): (P=11.41091) MN;
- (w=66.38): (P=11.4091467) MN, BOTTOM local/global-yield.

Thus the current path has a cusp-type maximum at the BOTTOM first-yield transition, not at a fitted FEM point.

## Frozen peak state
Using the high-order current evaluator:
[
oxed{P_u^{BH085}=11.41091 {m MN}}
]
at
[
oxed{w_u=66.36008521 {m mm}}.
]

Components:
[
P_U=4.303014 {m MN},qquad
P_s^+=2.281940 {m MN},qquad
P_s^-=4.825954 {m MN}.
]

UHPC condensation:
[
ho_A=0.74883493,qquad
ho_D=0.67679524,qquad
w_P=35.97821 {m mm}.
]

TOP:
[
A^+=3.7275310 {m mm},quad
e^+=1.3831052 {m mm},quad
A_P^+=2.3444259 {m mm},
]
[
sigma_{m VM,max}^+=355.0000 {m MPa},
]
with full-recovery predictor (sigma_{m VM,max}^{trial,+}=462.394) MPa.

BOTTOM at the peak:
[
A^-=3.9587195 {m mm},quad e^-=A^-,
quad A_P^-=0,
]
[
sigma_{m VM,max}^-=355.0000 {m MPa}.
]

Predictor root residuals are below (10^{-18}) in magnitude.

## UHPC quadrature convergence at the peak
Keeping the same (w_u) and steel continuous maximization:
- nq=80: 11.4107759 MN
- nq=100: 11.4109145 MN
- nq=120: 11.4109088 MN
- nq=160: 11.4109072 MN

The nq=120→160 change is about (1.5	imes10^{-6}) MN. Peak value is therefore frozen to 11.41091 MN for the present execution path.

## Post-peak check
The same equations give a descending branch after the event:
- (w=70) mm: (Papprox11.0718) MN;
- (w=80) mm: (Papprox9.8136) MN;
- (w=90) mm: (Papprox9.2355) MN;
- (w=105) mm: (Papprox9.0204) MN.

No FEM/test value was used in any root or maximization.
