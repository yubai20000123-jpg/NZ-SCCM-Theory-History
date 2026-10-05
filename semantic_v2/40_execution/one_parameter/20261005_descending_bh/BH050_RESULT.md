# BH050 current-path calculation result

## Inputs
[
b=2500 {m mm},quad a_h=5000 {m mm},quad w_0=6.25 {m mm},
]
[
A_0^pm=0.3515625 {m mm},quad N_pm=m_pm=4.
]

## Search and peak mechanism
The current curve was scanned over (w=0,5,ldots,70) mm. TOP has already entered the Mises corrector before the total maximum. BOTTOM trial Mises:
[
sigma_{m VM,BOT}^{trial}(20)=349.441 {m MPa},
quad
sigma_{m VM,BOT}^{trial}(21)=359.867 {m MPa}.
]
The real transition root is
[
oxed{w_u=20.53287143 {m mm}}.
]
Immediately beyond it the BOTTOM corrector activates and the total load drops.

## Frozen peak
[
oxed{P_u^{BH050}=7.59054 {m MN}},
qquad
oxed{w_u=20.53287143 {m mm}}.
]

Components:
[
P_U=2.205998 {m MN},quad
P_s^+=2.158473 {m MN},quad
P_s^-=3.226069 {m MN}.
]

UHPC:
[
ho_A=0.66088856,quad
ho_D=0.65061864,quad
w_P=11.03064 {m mm}.
]

TOP:
[
A^+=1.9257085 {m mm},quad
e^+=1.2047807 {m mm},quad
A_P^+=0.7209278 {m mm},
]
[
sigma_{m VM,max}^+=355 {m MPa},quad
sigma_{m VM,max}^{trial,+}=429.436 {m MPa}.
]

BOTTOM:
[
A^-=2.0714096 {m mm},quad e^-=A^-,
quad sigma_{m VM,max}^-=355.0000 {m MPa}.
]

## Integration convergence at (w_u)
- nq=80: 7.59056022 MN
- nq=100: 7.59055275 MN
- nq=120: 7.59054429 MN
- nq=160: 7.59053993 MN

nq=120→160 change is (4.35	imes10^{-6}) MN. No FEM/test data entered the calculation.
