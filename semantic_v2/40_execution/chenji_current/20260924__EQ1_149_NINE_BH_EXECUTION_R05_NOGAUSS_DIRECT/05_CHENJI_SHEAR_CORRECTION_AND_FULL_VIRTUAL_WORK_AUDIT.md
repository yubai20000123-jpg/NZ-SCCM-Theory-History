# Chen Ji shear correction and fully expanded virtual-work structure

Date: 2026-09-25

## Mandatory correction

General Chen Ji 8.7 does NOT assume gamma_xy=0. It retains the engineering shear strain and the Airy shear resultant Nxy=-Phi_xy.

Chen Ji 8.8 uses Nxy=0 only as part of the special straight-edge postbuckling analytical problem. For the homogeneous linear-elastic membrane law gamma_xy=2(1+nu)Nxy/(Et), gamma_xy=0 then follows as a consequence of Nxy=0; it is not an independent general assumption.

For the present nonlinear composite current section, Nxy=0 must not be replaced silently by gamma_xy=0. If the 8.8 special static assumption Nxy=0 is retained, gamma_xy must be determined from the current composite shear relation Nxy_current(...,gamma_xy,...)=0. The previous ten-scalar closure that directly set gamma_xy=0 is therefore not a faithful Chen-Ji-current closure and its numerical results are diagnostic only pending repair.

## Global q virtual work, fully expanded geometry

W=b(q0+q) sin(pi x/b) sin(pi y/a)
W0=b q0 sin(pi x/b) sin(pi y/a)

dW_x/dq=pi cos(pi x/b) sin(pi y/a)
dW_y/dq=(pi b/a) sin(pi x/b) cos(pi y/a)
dkappa_x/dq=(pi^2/b) sin(pi x/b) sin(pi y/a)
dkappa_y/dq=(pi^2 b/a^2) sin(pi x/b) sin(pi y/a)
dkappa_xy/dq=-(2 pi^2/a) cos(pi x/b) cos(pi y/a)

Rq1 is the sum of UHPC, TOP steel, BOTTOM steel, and web triple integrals with the exact thickness bounds:
UHPC z in [-tc/2,tc/2], TOP/BOTTOM zeta in [-ts+/2,ts+/2] / [-ts-/2,ts-/2], x in [0,b], y in [0,a].

Rq2 before the 8.8 Nxy=0 specialization is
int_0^b int_0^a [
pi^2(q0+q) Nx cos^2(pi x/b) sin^2(pi y/a)
+ pi^2 b^2/a^2 (q0+q) Ny sin^2(pi x/b) cos^2(pi y/a)
+ 2 pi^2 b/a (q0+q) Nxy sin(pi x/b)cos(pi x/b)sin(pi y/a)cos(pi y/a)
] dy dx.
Only the last term disappears when Nxy=0.

## Local shapes

psi+=(1-cos(2 pi N+ x/b))(1-cos(2 pi m+ y/a))
psi+_x=(2 pi N+/b) sin(2 pi N+ x/b)(1-cos(2 pi m+ y/a))
psi+_y=(2 pi m+/a)(1-cos(2 pi N+ x/b))sin(2 pi m+ y/a)
psi+_xx=(2 pi N+/b)^2 cos(2 pi N+ x/b)(1-cos(2 pi m+ y/a))
psi+_yy=(2 pi m+/a)^2(1-cos(2 pi N+ x/b))cos(2 pi m+ y/a)
psi+_xy=(2 pi N+/b)(2 pi m+/a)sin(2 pi N+ x/b)sin(2 pi m+ y/a).

TOP:
Ws+=W+(A0+ + A+)psi+
Ws0+=W0+A0+ psi+.

BOTTOM uses the same derivatives with minus local sign.

## Local amplitude virtual strains

TOP:
d epsx_s+/dA+ =
pi(q0+q) cos(pi x/b)sin(pi y/a) psi+_x
+(A0+ +A+) psi+_x^2
-zeta psi+_xx.

d epsy_s+/dA+ =
(pi b/a)(q0+q) sin(pi x/b)cos(pi y/a) psi+_y
+(A0+ +A+) psi+_y^2
-zeta psi+_yy.

d gammaxy_s+/dA+ =
pi(q0+q)cos(pi x/b)sin(pi y/a)psi+_y
+(pi b/a)(q0+q)sin(pi x/b)cos(pi y/a)psi+_x
+2(A0+ +A+)psi+_x psi+_y
-2 zeta psi+_xy.

BOTTOM:
d epsx_s-/dA- =
-pi(q0+q)cos(pi x/b)sin(pi y/a)psi-_x
+(A0-+A-)psi-_x^2
+zeta psi-_xx.

d epsy_s-/dA- =
-(pi b/a)(q0+q)sin(pi x/b)cos(pi y/a)psi-_y
+(A0-+A-)psi-_y^2
+zeta psi-_yy.

d gammaxy_s-/dA- =
-pi(q0+q)cos(pi x/b)sin(pi y/a)psi-_y
-(pi b/a)(q0+q)sin(pi x/b)cos(pi y/a)psi-_x
+2(A0-+A-)psi-_x psi-_y
+2 zeta psi-_xy.

The local residuals are the exact triple integrals of sigma_x * d epsx/dA + sigma_y * d epsy/dA + tau_xy * d gamma/dA over the above bounds.

## Direct integrability audit

1. Geometry alone is not the obstruction. All W, psi, derivatives and virtual-strain factors are finite trigonometric polynomials and z/zeta polynomials.
2. If UHPC and steel are linear elastic, every virtual-work integral is exactly reducible by trigonometric orthogonality and elementary thickness power integrals.
3. Exact signed-C1 UHPC makes the normal stress rational in a thickness-affine strain A(x,y)+z B(x,y). For fixed x,y the z integral can be reduced by rational partial fractions; after evaluation at z=+/-tc/2, logarithm/arctangent terms whose arguments are trigonometric functions of x,y appear. The remaining two-dimensional area integral generally has no finite elementary antiderivative. Tension/compression switching also introduces a moving z-boundary z=-A/B.
4. Exact current Mises steel gives trial VM^2=a(x,y)zeta^2+b(x,y)zeta+c(x,y). In the plastic branch stresses contain 1/sqrt(VM^2). For fixed x,y the zeta integrals are elementary (sqrt/log/asinh form), but their coefficients are trigonometric functions and the elastic/plastic transition roots move with x,y. The remaining area integral therefore requires exact regional partition/symbolic algebraic integration or a non-elementary special-function representation.
5. The web clip law is easier: for fixed x,y the yield-crossing z values are explicit and the thickness integrals are piecewise polynomial. The difficulty is again the x,y-dependent moving active region.
6. Rq2 is the clean exception: under the Chen-Ji 8.8 special Nxy=0 assumption and a retained finite Airy form, it reduces to exact trigonometric moments and is directly algebraic.
