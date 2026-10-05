# BH060 current-path calculation result

## Inputs
[
b=3000 {m mm},quad a_h=6000 {m mm},quad w_0=7.50 {m mm},
]
[
A_0^pm=0.421875 {m mm},quad N_pm=m_pm=4.
]

## Search and peak mechanism
The coarse current curve was evaluated over (w=0,5,ldots,80) mm. TOP enters the Mises corrector before the total peak. The BOTTOM elastic predictor gives
[
sigma_{m VM,BOT}^{trial}(35)=353.328 {m MPa},
quad
sigma_{m VM,BOT}^{trial}(36)=361.393 {m MPa}.
]
The exact event equation
[
maxsigma_{m VM,BOT}^{trial}(w)=355 {m MPa}
]
has the real root
[
oxed{w_u=35.20802328 {m mm}}.
]
After this event BOTTOM corrector activates and the load falls; e.g. (P(36)=8.35193) MN.

## Frozen peak
[
oxed{P_u^{BH060}=8.43835 {m MN}},
qquad
oxed{w_u=35.20802328 {m mm}}.
]

Components:
[
P_U=2.843770 {m MN},quad
P_s^+=1.896483 {m MN},quad
P_s^-=3.698097 {m MN}.
]

UHPC:
[
ho_A=0.70205318,quad
ho_D=0.65605463,quad
w_P=18.45981 {m mm}.
]

TOP:
[
A^+=2.4601595 {m mm},quad
e^+=1.0815584 {m mm},quad
A_P^+=1.3786011 {m mm},
]
[
sigma_{m VM,max}^+=355 {m MPa},quad
sigma_{m VM,max}^{trial,+}=459.198 {m MPa}.
]

BOTTOM at the transition:
[
A^-=2.6557751 {m mm},quad e^-simeq A^-,
quad sigma_{m VM,max}^-=355 {m MPa}.
]

## Integration convergence
At the frozen (w_u):
- nq=80: 8.43836199 MN
- nq=100: 8.43833247 MN
- nq=120: 8.43835707 MN
- nq=160: 8.43834959 MN

Spread is (2.95	imes10^{-5}) MN. No FEM/test quantity entered the solve.
