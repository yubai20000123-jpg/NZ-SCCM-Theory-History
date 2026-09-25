# 03 — Closed Galerkin coefficients for full q-A steel path

Date: 2026-09-25

This ledger removes the last unevaluated Galerkin integrals from the elastic whole-face q-A steel law.

Let alpha=pi/b, beta=pi/a_h. N,m are positive integers.

## 1. GG coefficients

J_GG_g =
-8 N^2 m^2 {
 alpha^4[16N^2m^2-52N^2-36m^2+117]
+beta^4 [16N^2m^2-36N^2-52m^2+117]
}
/
{
3 alpha beta
(2N-3)(2N-1)(2N+1)(2N+3)
(2m-3)(2m-1)(2m+1)(2m+3)
}.

J_GG_phi =
-(pi^2/4)[
 delta_{N1} m^2 beta^3/alpha
+delta_{m1} N^2 alpha^3/beta
].

Thus J_GG_phi=0 for N>1 and m>1.

## 2. Exact odd-harmonic algebra for GL

For positive integer n and odd positive r define, purely algebraically,

U_n(r)=
(pi/2) delta_{r1}
-(pi/4) delta_{2n,|r-1|}
+(pi/4) delta_{2n,r+1},

V_n(r)=
(pi/2) delta_{r1}
-(pi/4) delta_{2n,|r-1|}
-(pi/4) delta_{2n,r+1}.

Then
K_g(r,s)=alpha beta[
(r^2+s^2)U_N(r)U_m(s)-2rs V_N(r)V_m(s)
].

Also define

X_n(r)=1/(r+2n)+1/(r-2n)-1/r
       -1/[2(r+4n)]-1/[2(r-4n)],

Y_n(r)=3/r-2/(r+2n)-2/(r-2n)
       +1/[2(r+4n)]+1/[2(r-4n)],

Z_n(r)=1/(2n+r)+1/(2n-r)
       -1/[2(4n+r)]-1/[2(4n-r)].

Then
K_phi(r,s)=
-alpha beta[
s^2(2N)^2 X_N(r)Y_m(s)
+r^2(2m)^2 Y_N(r)X_m(s)
+2rs(2N)(2m) Z_N(r)Z_m(s)
].

These are exact rational/Kronecker expressions, not numerical integration rules.

The eight GL Airy harmonic coefficients (with the common alpha^2 beta^2 included) are:

c1=-alpha^2beta^2(N-m)^2 /
 [((2N+1)^2alpha^2+(2m+1)^2beta^2)^2],
 at (r,s)=(2N+1,2m+1);

c2=+alpha^2beta^2(N+m)^2 /
 [((2N+1)^2alpha^2+(2m-1)^2beta^2)^2],
 at (2N+1,2m-1);

c3=+alpha^2beta^2(N+m)^2 /
 [((2N-1)^2alpha^2+(2m+1)^2beta^2)^2],
 at (2N-1,2m+1);

c4=-alpha^2beta^2(N-m)^2 /
 [((2N-1)^2alpha^2+(2m-1)^2beta^2)^2],
 at (2N-1,2m-1);

c5=+2alpha^2beta^2m^2 /
 [(alpha^2+(2m+1)^2beta^2)^2],
 at (1,2m+1);

c6=-2alpha^2beta^2m^2 /
 [(alpha^2+(2m-1)^2beta^2)^2],
 at (1,2m-1);

c7=+2alpha^2beta^2N^2 /
 [((2N+1)^2alpha^2+beta^2)^2],
 at (2N+1,1);

c8=-2alpha^2beta^2N^2 /
 [((2N-1)^2alpha^2+beta^2)^2],
 at (2N-1,1).

Hence, explicitly,
J_GL_g =
c1 K_g(2N+1,2m+1)+c2 K_g(2N+1,2m-1)
+c3 K_g(2N-1,2m+1)+c4 K_g(2N-1,2m-1)
+c5 K_g(1,2m+1)+c6 K_g(1,2m-1)
+c7 K_g(2N+1,1)+c8 K_g(2N-1,1).

J_GL_phi is the same eight-term expression with K_phi replacing K_g.

For N>1,m>1, J_GL_g further collapses to

J_GL_g =
-pi^2 alpha^3 beta^3 {
 (N-m)^4/[4((2N+1)^2alpha^2+(2m+1)^2beta^2)^2]
+(N+m)^4/[4((2N+1)^2alpha^2+(2m-1)^2beta^2)^2]
+(N+m)^4/[4((2N-1)^2alpha^2+(2m+1)^2beta^2)^2]
+(N-m)^4/[4((2N-1)^2alpha^2+(2m-1)^2beta^2)^2]
+m^4/[alpha^2+(2m+1)^2beta^2]^2
+m^4/[alpha^2+(2m-1)^2beta^2]^2
+N^4/[(2N+1)^2alpha^2+beta^2]^2
+N^4/[(2N-1)^2alpha^2+beta^2]^2
}.

The Kronecker form above is retained for N=1 or m=1 so harmonic resonance is handled exactly rather than silently lost.

## 3. LL-to-global coefficient, seven harmonics individually

J_LL_g=T1+T2+T3+T4+T5+T6+T7,

T1=
-128 N^2 beta^3 m^4(8N^2+1)/
[alpha(2N-1)(2N+1)(4N-1)(4N+1)(2m-1)(2m+1)],

T2=
-128 N^4 alpha^3 m^2(8m^2+1)/
[beta(2N-1)(2N+1)(2m-1)(2m+1)(4m-1)(4m+1)],

T3=
-256 N^4 alpha^3 beta^3 m^4
[64N^4m^2+8N^4+64N^2m^4-56N^2m^2+N^2+8m^4+m^2]
/
[(2N-1)(2N+1)(4N-1)(4N+1)
 (2m-1)(2m+1)(4m-1)(4m+1)
 (N^2alpha^2+m^2beta^2)^2],

T4=
-32 N^2 beta^3 m^4(44N^2+1)/
[alpha(2N-1)(2N+1)(4N-1)(4N+1)(6N-1)(6N+1)(2m-1)(2m+1)],

T5=
-32 N^4 alpha^3 m^2(44m^2+1)/
[beta(2N-1)(2N+1)(2m-1)(2m+1)(4m-1)(4m+1)(6m-1)(6m+1)],

T6=
-128 N^4 alpha^3 beta^3 m^4
[256N^4m^2+176N^4+352N^2m^4-212N^2m^2+4N^2+8m^4+m^2]
/
[(2N-1)(2N+1)(4N-1)(4N+1)(6N-1)(6N+1)
 (2m-1)(2m+1)(4m-1)(4m+1)
 (4N^2alpha^2+m^2beta^2)^2],

T7=
-128 N^4 alpha^3 beta^3 m^4
[352N^4m^2+8N^4+256N^2m^4-212N^2m^2+N^2+176m^4+4m^2]
/
[(2N-1)(2N+1)(4N-1)(4N+1)
 (2m-1)(2m+1)(4m-1)(4m+1)(6m-1)(6m+1)
 (N^2alpha^2+4m^2beta^2)^2].

## 4. LL-to-local coefficient

J_LL_phi =
-pi^4 m^2/(4 a_h b) * kp(N,m,a_h,b),

where kp is not a fitted symbol but the explicit polynomial ratio

kp =
[
272 N^16 a_h^16
+2856 N^14 a_h^14 b^2 m^2
+11273 N^12 a_h^12 b^4 m^4
+23146 N^10 a_h^10 b^6 m^6
+31506 N^8 a_h^8 b^8 m^8
+23146 N^6 a_h^6 b^10 m^10
+11273 N^4 a_h^4 b^12 m^12
+2856 N^2 a_h^2 b^14 m^14
+272 b^16 m^16
]
/
[
a_h^2 b^2 m^2
(N^2 a_h^2+b^2m^2)^2
(N^2 a_h^2+4b^2m^2)^2
(4N^2 a_h^2+b^2m^2)^2
].

## 5. Full explicit elastic q-A plate path

Let Ds=Es t_s^3/[12(1-nu_s^2)].

BG =
64 N^2m^2(alpha^2+beta^2)^2/
[alpha beta(4N^2-1)(4m^2-1)].

BL =
4 pi^2[3beta^4m^4+2alpha^2beta^2N^2m^2+3alpha^4N^4]/(alpha beta).

CG =
64 beta N^2m^2/[alpha(4N^2-1)(4m^2-1)].

CL=3pi^2 beta m^2/alpha.

Then, without any unevaluated area integral,

p_s(q,A)=
{
Ds[bq BG+A BL]
-t_s Es [
b^2(q^2+2q0q){b(q0+q)J_GG_g+(A0+A)J_GG_phi}
+b(q0A+qA0+qA){b(q0+q)J_GL_g+(A0+A)J_GL_phi}
+(2A0A+A^2){b(q0+q)J_LL_g+(A0+A)J_LL_phi}
]
}
/
{
b(q0+q)CG+(A0+A)CL
}.

Every J on the right is explicitly evaluated above. No Airy field, no spatial integral, no Gauss point, and no fitted width-thickness parameter remains in this elastic steel-face equation.
