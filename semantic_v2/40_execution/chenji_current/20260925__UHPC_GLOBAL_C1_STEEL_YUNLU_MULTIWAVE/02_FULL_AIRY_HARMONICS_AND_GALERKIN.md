# 02 Full Airy harmonics and Galerkin algebra

Date: 2026-09-25

## Geometry

alpha=pi/b, beta=pi/a_h,
g=sin(alpha x)sin(beta y),
phi=[1-cos(2N alpha x)][1-cos(2m beta y)].

TOP:
Ws0=b q0 g + A0 phi,
Ws=b(q0+q)g+(A0+A)phi.

Let H(W)=W_xy^2-W_xx W_yy. Then
DeltaH=b^2(q^2+2q0q)H_GG+b(q0A+qA0+qA)H_GL+(2A0A+A^2)H_LL.

## Fully expanded compatibility harmonics

H_GG=
(alpha^2 beta^2/2)[cos(2 alpha x)+cos(2 beta y)].

H_GL=
alpha^2 beta^2[
-(N-m)^2 sin((2N+1)alpha x)sin((2m+1)beta y)
+(N+m)^2 sin((2N+1)alpha x)sin((2m-1)beta y)
+(N+m)^2 sin((2N-1)alpha x)sin((2m+1)beta y)
-(N-m)^2 sin((2N-1)alpha x)sin((2m-1)beta y)
+2N^2 sin((2N+1)alpha x)sin(beta y)
-2N^2 sin((2N-1)alpha x)sin(beta y)
+2m^2 sin(alpha x)sin((2m+1)beta y)
-2m^2 sin(alpha x)sin((2m-1)beta y)
].

H_LL=
8N^2m^2 alpha^2 beta^2[
-cos(4N alpha x)
-cos(4m beta y)
-2cos(2N alpha x)cos(2m beta y)
+cos(2m beta y)
+cos(4N alpha x)cos(2m beta y)
+cos(2N alpha x)
+cos(2N alpha x)cos(4m beta y)
].

## Fully expanded Airy particular

F_GG=
Es b^2(q^2+2q0q)[
(beta^2/(32 alpha^2)) cos(2 alpha x)
+(alpha^2/(32 beta^2)) cos(2 beta y)
].

F_GL=Es b(q0A+qA0+qA) alpha^2 beta^2 times the following eight explicit terms:
-(N-m)^2 sin((2N+1)alpha x)sin((2m+1)beta y) /
 [((2N+1)^2 alpha^2+(2m+1)^2 beta^2)^2]
+(N+m)^2 sin((2N+1)alpha x)sin((2m-1)beta y) /
 [((2N+1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+(N+m)^2 sin((2N-1)alpha x)sin((2m+1)beta y) /
 [((2N-1)^2 alpha^2+(2m+1)^2 beta^2)^2]
-(N-m)^2 sin((2N-1)alpha x)sin((2m-1)beta y) /
 [((2N-1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+2N^2 sin((2N+1)alpha x)sin(beta y) /
 [((2N+1)^2 alpha^2+beta^2)^2]
-2N^2 sin((2N-1)alpha x)sin(beta y) /
 [((2N-1)^2 alpha^2+beta^2)^2]
+2m^2 sin(alpha x)sin((2m+1)beta y) /
 [(alpha^2+(2m+1)^2 beta^2)^2]
-2m^2 sin(alpha x)sin((2m-1)beta y) /
 [(alpha^2+(2m-1)^2 beta^2)^2].

F_LL=8Es N^2m^2 alpha^2 beta^2(2A0A+A^2) times:
-cos(4N alpha x)/(4N alpha)^4
-cos(4m beta y)/(4m beta)^4
-2cos(2N alpha x)cos(2m beta y)/
 [(4N^2 alpha^2+4m^2 beta^2)^2]
+cos(2m beta y)/(2m beta)^4
+cos(4N alpha x)cos(2m beta y)/
 [(16N^2 alpha^2+4m^2 beta^2)^2]
+cos(2N alpha x)/(2N alpha)^4
+cos(2N alpha x)cos(4m beta y)/
 [(4N^2 alpha^2+16m^2 beta^2)^2].

## Exact Galerkin bending and homogeneous-load projections

For the local weight phi on x in [0,b], y in [0,a_h]:

B_bend =
64 b q N^2m^2 (alpha^2+beta^2)^2 /
[(4N^2-1)(4m^2-1) alpha beta]
+
pi^2 A[12N^4 alpha^4+8N^2m^2 alpha^2beta^2+12m^4 beta^4]/
(alpha beta).

J_x =
-alpha/beta[
64N^2m^2 b(q0+q)/((4N^2-1)(4m^2-1))
+3pi^2N^2(A0+A)
].

With Yun-Lu's homogeneous Airy field F_h=-p_s y^2/(2 t_s), the Galerkin equation is
D_s B_bend = t_s P_mem - p_s J_x,
hence
p_s=(D_s B_bend-t_s P_mem)/(-J_x).

P_mem is not a numerical integral. It is the exact finite harmonic contraction
P_mem=<phi,[F_p,W]>. Its evaluation can be reduced entirely to algebraic overlap coefficients because all F_p and W harmonics above are finite. The next formal expansion must enumerate every pairwise harmonic overlap, including exceptional resonances N=1 or m=1 separately; no integral is required.

## UHPC raw-data audit

The exact raw 30-row UC141 compression-hardening table is not present in the currently retrievable Project/Library material. The available records prove only that UC141 has 30 compression-hardening rows and 23 tension-stiffening rows; they do not expose the 30 compression values.

Therefore a defensible "minimum-order fit to original tension+compression data" cannot yet be completed. The previously reported epsilon-only rational candidate was fitted against the current signed-C1 reference and must remain provisional. It cannot be relabeled as a raw-data fit.

The corrected 23-row tension data available in conversation can be used, but the exact 30 compression rows are required before the joint minimum-order screening is formally closed.
