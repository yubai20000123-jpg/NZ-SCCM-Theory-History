# 03 Explicit reduced steel path without Airy placeholders or unevaluated integrals

Date: 2026-09-25

This note closes the elastic whole-face Yun-Lu/Chen-Ji steel path to a finite algebraic formula. No Airy placeholder field and no unevaluated area integral remains. The formula is written for integer N,m. The generic multiwave branch N,m>=2 is shown directly; N=1 and/or m=1 add the explicitly stated GG-LL resonance term.

Let alpha=pi/b and beta=pi/a_h.

Define the purely algebraic parity overlap
chi(r,k)=2k/(k^2-r^2),
where r is a nonnegative even integer and k is a positive odd integer. Because even and odd integers cannot coincide, this expression has no singularity.

The exact finite harmonic contractions are:

K_GG_GL =
-(N-m)^2 Omega(2N+1,2m+1)
+(N+m)^2 Omega(2N+1,2m-1)
+(N+m)^2 Omega(2N-1,2m+1)
-(N-m)^2 Omega(2N-1,2m-1)
+2N^2 Omega(2N+1,1)
-2N^2 Omega(2N-1,1)
+2m^2 Omega(1,2m+1)
-2m^2 Omega(1,2m-1),

where the above Omega is not an unevaluated integral but the following explicit rational expression:
Omega(k,l)=
[beta^3/(32 alpha)] chi(2,k)chi(0,l)
+[alpha^3/(32 beta)] chi(0,k)chi(2,l).

K_GL_GL =
(pi^2 alpha^3 beta^3/4){
 (N-m)^4/[((2N+1)^2 alpha^2+(2m+1)^2 beta^2)^2]
+(N+m)^4/[((2N+1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+(N+m)^4/[((2N-1)^2 alpha^2+(2m+1)^2 beta^2)^2]
+(N-m)^4/[((2N-1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+4N^4/[((2N+1)^2 alpha^2+beta^2)^2]
+4N^4/[((2N-1)^2 alpha^2+beta^2)^2]
+4m^4/[ (alpha^2+(2m+1)^2 beta^2)^2]
+4m^4/[ (alpha^2+(2m-1)^2 beta^2)^2]
}.

For the GL-LL cross contraction define the following explicit seven-term rational expression:
Xi(k,l)=8N^2m^2 alpha^2 beta^2[
-chi(4N,k)chi(0,l)
-chi(0,k)chi(4m,l)
-2chi(2N,k)chi(2m,l)
+chi(0,k)chi(2m,l)
+chi(4N,k)chi(2m,l)
+chi(2N,k)chi(0,l)
+chi(2N,k)chi(4m,l)
].

Then
K_GL_LL =
alpha beta[
-(N-m)^2 Xi(2N+1,2m+1)/
 ((2N+1)^2 alpha^2+(2m+1)^2 beta^2)^2
+(N+m)^2 Xi(2N+1,2m-1)/
 ((2N+1)^2 alpha^2+(2m-1)^2 beta^2)^2
+(N+m)^2 Xi(2N-1,2m+1)/
 ((2N-1)^2 alpha^2+(2m+1)^2 beta^2)^2
-(N-m)^2 Xi(2N-1,2m-1)/
 ((2N-1)^2 alpha^2+(2m-1)^2 beta^2)^2
+2N^2 Xi(2N+1,1)/
 ((2N+1)^2 alpha^2+beta^2)^2
-2N^2 Xi(2N-1,1)/
 ((2N-1)^2 alpha^2+beta^2)^2
+2m^2 Xi(1,2m+1)/
 (alpha^2+(2m+1)^2 beta^2)^2
-2m^2 Xi(1,2m-1)/
 (alpha^2+(2m-1)^2 beta^2)^2
].

K_LL_LL =
(17 pi^2/8)[m^4 beta^3/alpha+N^4 alpha^3/beta]
+4pi^2 N^4m^4 alpha^3beta^3/(N^2alpha^2+m^2beta^2)^2
+pi^2 N^4m^4 alpha^3beta^3/(4N^2alpha^2+m^2beta^2)^2
+pi^2 N^4m^4 alpha^3beta^3/(N^2alpha^2+4m^2beta^2)^2.

K_GG_LL=0 for N,m>=2.
For N=1 and/or m=1, the exact resonance correction is
K_GG_LL =
(pi^2/8)[N^2m^2 beta^3/alpha delta_{N1}
        +N^2m^2 alpha^3/beta delta_{m1}].

With
Q=q^2+2q0q,
L=q0 A+q A0+q A,
R=2A0 A+A^2,

the exact current particular-Airy membrane contribution to the local Galerkin equation is

P_mem = -Es[
 b^3 Q(q0+q) K_GG_GL
+b^2 L(q0+q) K_GL_GL
+b R(q0+q) K_GL_LL
+2b^2 Q(A0+A) K_GG_LL
+2b L(A0+A) K_GL_LL
+2R(A0+A) K_LL_LL
].

No integral appears in this formula.

The exact bending projection is

B_bend =
64 b q N^2m^2(alpha^2+beta^2)^2/
[(4N^2-1)(4m^2-1)alpha beta]
+
pi^2 A[12N^4alpha^4+8N^2m^2alpha^2beta^2+12m^4beta^4]/(alpha beta).

The homogeneous-load projection is

-J_x =
(alpha/beta)[
64N^2m^2 b(q0+q)/((4N^2-1)(4m^2-1))
+3pi^2N^2(A0+A)
].

Therefore the explicit elastic whole-face steel load path is

p_s(q,A)=
{D_s B_bend - t_s P_mem}/(-J_x),

with D_s=Es t_s^3/[12(1-nu_s^2)].

All objects on the right are explicit rational/algebraic functions of
b,a_h,t_s,Es,nu_s,N,m,q0,q,A0,A
(and Kronecker resonance indicators only for N=1 or m=1).

No normalized width-thickness ratio has been introduced.

Checks required:
1. q=q0=0 must reduce algebraically to Yun-Lu Eq.(2-32).
2. A=A0=0 must reduce to the pure-global Chen-Ji/Marguerre branch after changing the Galerkin test to the global sine; the local phi projection itself is then not the global equilibrium equation.
3. The post-yield branch is not contained here. It begins when the elastic stress reconstruction first reaches fy, consistent with Chen Ji Fig.8.19 and Yun-Lu Eq.(2-38).

## UHPC data status

Formal raw-data minimum-order screening remains blocked only by one missing input: the exact 30-row UC141 compression-hardening values. The currently retrievable audit proves the block exists and has 30 rows but does not expose those values. The 23-row tension dataset is known. Therefore no final "minimum order from original tension+compression data" is asserted here; the earlier signed-C1-fitted rational law remains provisional only.
