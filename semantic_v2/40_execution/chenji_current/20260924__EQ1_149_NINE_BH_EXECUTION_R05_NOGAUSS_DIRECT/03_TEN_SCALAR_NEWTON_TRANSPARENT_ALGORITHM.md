# R05 transparent ten-scalar Newton / continuation algorithm

Date: 2026-09-24

## Governing scalar state at prescribed Delta

X = [q, Aplus, Aminus, epsx_bar, epsy_bar, ex_alpha, ey_beta, Fx, Fy, P]^T.

The Chen-Ji §8.8/H1 retained compatible field satisfies Eq.(28) identically. Eq.(89)–(91) are reduced to six current-resultant/Airy consistency residuals R1–R6. Eq.(114), Eq.(119), Eq.(109), Eq.(123) give R7–R10.

The fixed-Delta problem is R(X;Delta)=0.

## Physical zero-load state

At Delta=0 the incremental unknowns are exactly:
q=Aplus=Aminus=epsx_bar=epsy_bar=ex_alpha=ey_beta=Fx=Fy=P=0.
Initial imperfections q0 and A0plus/A0minus remain geometric parameters and are not zeroed.

## Predictor

For the first nonzero step the clean theoretical predictor is obtained from the tangent equation
J0 * (dX/dDelta) = -R_,Delta,
which is the finite ten-scalar counterpart of Eq.(128)–(143).

For a continuation step, the current execution may use the previous converged root and either:
(1) one-step axial predictor: inherit all components and advance epsy_bar by the normalized shortening increment; or
(2) two-point secant predictor:
Xpred = Xn + (Xn-Xn-1)*(Delta_n+1-Delta_n)/(Delta_n-Delta_n-1).

Neither predictor changes the governing equations.

## Residuals

R1=<Nx>
R2=2<Nx cos(2pi x/b)>
R3=2<Nx cos(2pi y/a_h)> + 4pi^2 Fy/a_h^2
R4=<Ny> + P/b
R5=2<Ny cos(2pi x/b)> + 4pi^2 Fx/b^2
R6=2<Ny cos(2pi y/a_h)>
R7=Eq.(114)
R8=Eq.(119)
R9=Eq.(109)
R10=-2 a_h epsy_bar + pi^2 b^2/(4 a_h)*(q^2+2 q0 q)-Delta.

## Numerical residual scaling used in the current trace

Residual zeroes are unchanged by scaling.

S1..S6 = 1.0e4
S7=S8=max(1.0e4, Es*ts*b*1.0e-3)
S9=max(1.0e5, Ec*tc*b*1.0e-3)
S10=max(1.0, b*1.0e-3)

r_i=R_i/S_i
error = ||r||_infinity = max_i |r_i|.

Current convergence test in the explicit trace: error < 1.0e-9.

## Variable scaling

Y=X/Xscale, with
Xscale=[0.01, max(0.1,0.002b), max(0.1,0.002b), 0.005,0.005,0.005,0.005, max(1e6,1000b^2), max(1e6,1000b^2), max(1e6,1000b^2)].

For BH020 (b=1000 mm):
Xscale=[0.01,2,2,0.005,0.005,0.005,0.005,1e9,1e9,1e9].

## Newton corrector

At iteration k:
J_ij ≈ [r_i(Y+h_j e_j)-r_i(Y-h_j e_j)]/(2 h_j)
with h_j=2e-5 max(1,|Y_j|).

Solve:
J dY = -r.

Line-search trial factors:
1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128.
Accept the first factor that reduces ||r||_infinity; if none reduces it, retain the best trial among those evaluated.

Update:
Y_{k+1}=Y_k + lambda dY,
X_{k+1}=Xscale .* Y_{k+1}.

## Explicit BH020 example: dbar 0.0016 -> 0.0018

Previous converged state at dbar=0.0016:
q=1.9119884635e-4,
Aplus=0.2102997054 mm,
Aminus=0.1926430184 mm,
epsx_bar=4.3819290784e-4,
epsy_bar=-1.5987754890e-3,
ex_alpha=1.9129663899e-7,
ey_beta=1.7420035445e-7,
Fx=65881.445204,
Fy=58089.100681,
P=3.272539852 MN.

Predictor to dbar=0.0018:
inherit every component and set
epsy_bar(pred)=epsy_bar(old)-0.0002=-0.001798775489.

Raw residual:
[-113.2810653, -4.97444e-4, 3.18298e-3, -86.8969602, 0.25296694, -0.04093881, -41580.96585, -34456.90989, -248481.80440, 0].

Scaled residual:
[-1.13281065e-2, -4.97444e-8, 3.18298e-7, -8.68969602e-3, 2.52966938e-5, -4.09388123e-6, -5.04623372e-2, -4.18166382e-2, -1.36318743e-1, 0].

Therefore error=0.1363187428, governed by Rq.

The first Newton solve returns the scaled correction:
dY=[-7.60647574e-5, 3.19670832e-2, 3.40803976e-2, 9.08962127e-3, -1.01018060e-6, 8.85026734e-6, 1.08761173e-5, -7.06412505e-6, -1.31458185e-6, 3.53959575e-5].

In physical units:
dq=-7.60647574e-7,
dAplus=+0.0639341663 mm,
dAminus=+0.0681607951 mm,
depsx_bar=+4.54481063e-5,
depsy_bar=-5.05090298e-9,
dex_alpha=+4.42513367e-8,
dey_beta=+5.43805866e-8,
dFx=-7064.12505,
dFy=-1314.58185,
dP=+0.0353959575 MN.

lambda=1 is accepted because the residual error drops from 0.1363187428 to 0.01743672854.

Further full Newton updates reduce the error:
0.1363187428
-> 0.01743672854
-> 4.46294540e-4
-> 3.80491324e-7
-> 1.231340e-13.

## Locked scope correction

The previous text below this heading introduced 21-scalar and 11-scalar direct-stationary systems. Those were not authorized by the user and are withdrawn. They are not part of R05.

R05 is locked to exactly ten scalar unknowns at prescribed Delta:
q, Aplus, Aminus, epsx_bar, epsy_bar, ex_alpha, ey_beta, Fx, Fy, P.

Peak search is performed only by continuation in prescribed Delta and locating the maximum P on that connected ten-scalar branch. No additional sensitivity unknowns, no 11-scalar direct-peak system, and no 21-scalar augmented system are allowed in R05.
