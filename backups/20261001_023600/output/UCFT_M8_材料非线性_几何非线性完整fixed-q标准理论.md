# UCFT M8 — 材料非线性 + 几何非线性完整 fixed-q 标准理论

时间：2026-10-01 02:36 +08:00

## 0. 范围
本标准对应：single-q global field + C1 membrane + upper/lower whole-face steel-local A+/A- + final-INP UHPC current law + Q355 consistent secant-Mises deformation theory。

正式 fixed-q 未知量仅：
Ex,Ey,Bx,By,Hx,Hy,P,A+,A-。
M3 candidate harmonics 不默认实例化。

## 1. 整体几何
0<=x<=b, 0<=y<=a_h.

W0=b q0 sin(pi x/b) sin(pi y/a_h)
Wg=b(q0+q) sin(pi x/b) sin(pi y/a_h)
wg=b q sin(pi x/b) sin(pi y/a_h)

C1:
eps_x^0 =
Ex + Bx cos(2pi x/b)
- pi^2/8 (q^2+2q0 q) cos(2pi y/a_h)
+ Hx cos(2pi x/b) cos(2pi y/a_h)

eps_y^0 =
Ey
- pi^2 b^2/(8 a_h^2)(q^2+2q0 q) cos(2pi x/b)
+ By cos(2pi y/a_h)
+ Hy cos(2pi x/b) cos(2pi y/a_h)

gamma_xy^0 =
-[b/a_h Hx + a_h/b Hy]
sin(2pi x/b) sin(2pi y/a_h)

kappa_x^g = pi^2 q/b sin(pi x/b) sin(pi y/a_h)
kappa_y^g = pi^2 q b/a_h^2 sin(pi x/b) sin(pi y/a_h)
kappa_xy^g = -2 pi^2 q/a_h cos(pi x/b) cos(pi y/a_h)

## 2. steel-local
psi+=[1-cos(2pi N+ x/b)][1-cos(2pi m+ y/a_h)]
psi-=[1-cos(2pi N- x/b)][1-cos(2pi m- y/a_h)]

TOP:
Delta eps_x^{l,+} =
pi(q0 A+ + q A0+ + q A+) cos(pi x/b) sin(pi y/a_h) psi+_,x
+ 1/2[(A+)^2+2A0+A+] (psi+_,x)^2

Delta eps_y^{l,+} =
pi b/a_h(q0 A+ + q A0+ + q A+) sin(pi x/b) cos(pi y/a_h) psi+_,y
+ 1/2[(A+)^2+2A0+A+] (psi+_,y)^2

Delta gamma^{l,+} =
pi(q0 A+ + q A0+ + q A+)
[cos(pi x/b)sin(pi y/a_h)psi+_,y
+b/a_h sin(pi x/b)cos(pi y/a_h)psi+_,x]
+[(A+)^2+2A0+A+]psi+_,x psi+_,y

kappa_x^{l,+}=-A+ psi+_,xx
kappa_y^{l,+}=-A+ psi+_,yy
kappa_xy^{l,+}=-2A+ psi+_,xy

BOTTOM is identical except the qA cross terms change sign and:
kappa_x^{l,-}=+A- psi-_,xx
kappa_y^{l,-}=+A- psi-_,yy
kappa_xy^{l,-}=+2A- psi-_,xy.

Thus all three exact geometric channels are retained:
q^2+2q0q;
q0A+qA0+qA;
A^2+2A0A.

## 3. thickness strains
UHPC:
eps_x^U=eps_x^0+z kappa_x^g
eps_y^U=eps_y^0+z kappa_y^g
gamma^U=gamma_xy^0+z kappa_xy^g

TOP steel:
eps_x^{s,+}=eps_x^0+Delta eps_x^{l,+}+[(tc+ts)/2+zeta]kappa_x^g+zeta kappa_x^{l,+}
eps_y^{s,+}=eps_y^0+Delta eps_y^{l,+}+[(tc+ts)/2+zeta]kappa_y^g+zeta kappa_y^{l,+}
gamma^{s,+}=gamma_xy^0+Delta gamma^{l,+}+[(tc+ts)/2+zeta]kappa_xy^g+zeta kappa_xy^{l,+}

BOTTOM steel:
eps_x^{s,-}=eps_x^0+Delta eps_x^{l,-}+[-(tc+ts)/2+zeta]kappa_x^g+zeta kappa_x^{l,-}
eps_y^{s,-}=eps_y^0+Delta eps_y^{l,-}+[-(tc+ts)/2+zeta]kappa_y^g+zeta kappa_y^{l,-}
gamma^{s,-}=gamma_xy^0+Delta gamma^{l,-}+[-(tc+ts)/2+zeta]kappa_xy^g+zeta kappa_xy^{l,-}

## 4. UHPC material nonlinearity
e_x^U=(eps_x^U+nu_c eps_y^U)/(1-nu_c^2)
e_y^U=(eps_y^U+nu_c eps_x^U)/(1-nu_c^2)
tau_xy^U=Ec/[2(1+nu_c)] gamma_xy^U

normal stress uses the final-INP piecewise-linear total-strain backbone.
For every adjacent pair (e_j,sigma_j),(e_{j+1},sigma_{j+1}):
sigma(e)=sigma_j+(sigma_{j+1}-sigma_j)/(e_{j+1}-e_j)(e-e_j).

At fixed x,y, e_x^U(z),e_y^U(z) are affine in z, so every material threshold gives one explicit z-root; sort all valid roots and integrate each linear branch exactly.

## 5. Q355 material nonlinearity
For nu_s=0.30:
bar eps_s^2 =
7900/8281[(eps_x^s)^2+(eps_y^s)^2]
+1100/8281 eps_x^s eps_y^s
+75/169 (gamma_xy^s)^2.

yield:
bar eps_s = 355/206000.

Elastic:
sigma_x=206000[100/91 eps_x+30/91 eps_y]
sigma_y=206000[30/91 eps_x+100/91 eps_y]
tau=206000(5/13)gamma.

Plastic EPP deformation theory:
sigma_x=355/bar eps_s [100/91 eps_x+30/91 eps_y]
sigma_y=355/bar eps_s [30/91 eps_x+100/91 eps_y]
tau=355/bar eps_s (5/13)gamma.

Because all three steel strains are affine in zeta, the yield equation is exactly quadratic in zeta and gives at most two internal roots. Thickness elastic/plastic intervals are therefore exact and finite.

## 6. six C1 membrane residuals
G_Ex =
int_0^b int_0^ah [Nx^U+Nx^{s,+}+Nx^{s,-}] dy dx =0

G_Ey =
int_0^b int_0^ah [Ny^U+Ny^{s,+}+Ny^{s,-}] dy dx + P ah =0

G_Bx =
int int [Nx^U+Nx^{s,+}+Nx^{s,-}] cos(2pi x/b) dy dx=0

G_By =
int int [Ny^U+Ny^{s,+}+Ny^{s,-}] cos(2pi y/ah) dy dx=0

G_Hx =
int int { [Nx^U+Nx^{s,+}+Nx^{s,-}] cos(2pi x/b)cos(2pi y/ah)
- b/ah [Nxy^U+Nxy^{s,+}+Nxy^{s,-}] sin(2pi x/b)sin(2pi y/ah)}dy dx=0

G_Hy =
int int { [Ny^U+Ny^{s,+}+Ny^{s,-}] cos(2pi x/b)cos(2pi y/ah)
- ah/b [Nxy^U+Nxy^{s,+}+Nxy^{s,-}] sin(2pi x/b)sin(2pi y/ah)}dy dx=0

## 7. q residual
For every layer, Rq is current stress contracted with the exact strain derivative with respect to q. External work is:
-P pi^2 b^2/(4 ah)(q+q0).

UHPC q-derivatives:
d eps_x^U/dq =
-pi^2/4(q+q0)cos(2pi y/ah)
+z pi^2/b sin(pi x/b)sin(pi y/ah)

d eps_y^U/dq =
-pi^2 b^2/(4ah^2)(q+q0)cos(2pi x/b)
+z pi^2 b/ah^2 sin(pi x/b)sin(pi y/ah)

d gamma^U/dq =
-z 2pi^2/ah cos(pi x/b)cos(pi y/ah).

TOP/BOTTOM add the exact derivatives of the qA local cross terms.

## 8. A+ and A- residuals
RA+ = triple integral through TOP steel of
sigma_x^{s,+} d eps_x^{s,+}/dA+
+sigma_y^{s,+} d eps_y^{s,+}/dA+
+tau^{s,+} d gamma^{s,+}/dA+
=0.

RA- analogously equals zero in the bottom steel.

TOP derivatives:
d eps_x^{s,+}/dA+ =
pi(q0+q)cos(pi x/b)sin(pi y/ah)psi+_,x
+(A0++A+)(psi+_,x)^2
-zeta psi+_,xx

d eps_y^{s,+}/dA+ =
pi b/ah(q0+q)sin(pi x/b)cos(pi y/ah)psi+_,y
+(A0++A+)(psi+_,y)^2
-zeta psi+_,yy

d gamma^{s,+}/dA+ =
pi(q0+q)[cos(pi x/b)sin(pi y/ah)psi+_,y
+b/ah sin(pi x/b)cos(pi y/ah)psi+_,x]
+2(A0++A+)psi+_,x psi+_,y
-2zeta psi+_,xy.

BOTTOM uses the opposite sign on the qA terms and the opposite local-curvature signs.

## 9. Newton standard
At fixed q solve:
F=[G_Ex,G_Ey,G_Bx,G_By,G_Hx,G_Hy,Rq,RA+,RA-]^T=0
for:
y=[Ex,Ey,Bx,By,Hx,Hy,P,A+,A-]^T.

At iteration n:
J^(n) Delta y^(n) = -F^(n),
y^(n+1)=y^(n)+alpha Delta y^(n).

Every Jacobian entry follows the exact current virtual-work linearization:
material tangent term
(d epsilon / d residual-direction)^T Ct (d epsilon / d unknown)
plus current-stress geometric term
sigma^T d^2 epsilon/(d residual-direction d unknown),
plus exact derivative of external work.

The only non-zero second-kinematic families introduced by steel-local geometry are qA, AA, plus the global qq term used for q-sensitivity.

## 10. interpretation
This system already contains:
- global geometric nonlinearity q^2+2q0q;
- global-local qA coupling;
- local-local A^2 coupling;
- UHPC material branch switching/softening;
- steel elastic-plastic current stress;
- steel current tangent;
- local amplitude equilibrium;
- full current virtual-work coupling.

What is not yet reduced is only the most efficient production evaluation of the nonlinear steel x-y surface integrals after exact zeta integration. That is an integration-operator problem, not a missing structural equation.
