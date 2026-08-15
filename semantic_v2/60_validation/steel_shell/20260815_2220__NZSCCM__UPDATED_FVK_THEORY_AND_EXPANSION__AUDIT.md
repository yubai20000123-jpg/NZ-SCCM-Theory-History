# NZ-SCCM — 更新理论全过程与“膨胀”现象审计

**Timestamp:** 2026-08-15 22:20 +08:00  
**Identity:** no-Pu theory/implementation audit

## 1. Theory evolution audited

The current chain is:

```text
single complete (1,1) out-of-plane halfwave
-> Nguyen imperfect second-order membrane source
-> boundary-admissible c direction
-> FvK source-rank audit
-> minimum p20 + p02 in-plane completion
-> generalized residuals Rc,R20,R02
-> flat 3x3 membrane condensation into scalar Rq
-> same R10/N48/Cayley-Hamilton/General-D15 current operator
```

The physical model did not introduce any new out-of-plane mode, spatial cell or formal quadrature point.

## 2. Is there theoretical dimensional inflation?

Only controlled minimum growth:

```text
D+q                      : 2 total generalized coordinates
D+q+c                    : 3 total
D+q+c+p20+p02            : 5 total
```

At fixed D the nonlinear unknown count is `2 -> 4`. The intended membrane block is only

```text
m=[c,p20,p02]^T
Jmm = 3x3
```

plus one scalar q equation. This is not uncontrolled model-order growth.

## 3. Is there kinematic polynomial inflation?

No.

Exact support counting from the committed strain algebra gives:

```text
quantity      D+q+c     augmented
ex terms         4          4
ey terms         6          7
gamma^2 terms   12         12
Exx terms        7          7
Eyy terms        7          7
I1 terms         7          7
I2 terms        25         25
K1 terms         7          7
K2 terms        25         25
```

Maximum polynomial degree boxes are unchanged:

```text
ex,ey,I1      : (2,2,1)
gamma^2,I2    : (4,4,2)
```

The low-order Chebyshev boxes are also unchanged:

```text
K1 shape = 3x3x2, nnz = 7
K2 shape = 5x5x3, nnz = 27
```

So p20/p02 do **not** create a new polynomial order family.

## 4. What actually grows?

The numerical magnitudes of some low-order K1/K2 coefficients increase. At the audited parent and augmented states:

```text
min |nonzero K1 Cheb coefficient|:
0.0188973 -> 0.0949024  (~5.02x)

min |nonzero K2 Cheb coefficient|:
0.000371642 -> 0.00334348 (~9.00x)
```

This matters because the inherited `trim(A,tol)` routine is not element-wise sparse pruning. It scans each coordinate axis, finds the last index plane whose maximum coefficient exceeds `tol`, and then retains the **entire dense rectangular box** up to those last indices.

Therefore the 21:53 phrase “dense coefficient support grows” must be interpreted precisely as:

```text
high-order numerical tails remain above the axis-tail trim tolerance
-> retained degree extents become longer
-> the whole dense 3D bounding box is retained
-> FFT/Laurent intermediates grow rapidly
```

It is **not** evidence that the exact low-order kinematic support or formal D15 basis exploded.

## 5. Why the dense implementation can become very expensive

With base K1 degree vector `(2,2,1)`, an N48 matrix function has a worst-case spatial degree envelope

```text
(96,96,48).
```

Products such as `det(F)*F` can reach a rough envelope

```text
(288,288,144),
```

and after an additional low-order strain factor a rough stress box is

```text
(290,290,145).
```

A real float64 dense field of that full bounding-box size contains about

```text
12.36 million entries ≈ 94.3 MiB.
```

The current `ctl()` Laurent conversion doubles each axis approximately, giving a possible box

```text
581 x 581 x 291
≈ 98.23 million entries
≈ 0.73 GiB as real float64.
```

A same-size full convolution output envelope can reach roughly

```text
1161 x 1161 x 581
≈ 783 million real-equivalent entries
≈ 5.83 GiB before FFT workspace overhead.
```

These are **worst-case representation envelopes**, not claims that every current array reaches them. They explain why retaining only a few additional high-order tail planes can trigger severe runtime/memory growth in the dense algorithm.

## 6. Jacobian “ill-conditioning” audit

The stored 4x4 finite-difference Jacobian has raw condition number

```text
1.7401e4.
```

However simple scaling changes it strongly:

```text
row-normalized                    ~406.82
column-normalized                 ~358.80
row+column normalized              ~83.33
coordinate-scale + row normalized ~66.58
```

with coordinate scales approximately

```text
q=.008, c=.08, p20=.06, p02=.16.
```

Thus the raw 1.74e4 value is dominated in part by different residual/coordinate scales. It is not evidence of a nearly singular physical equilibrium system by itself.

## 7. Important intermediate parameters at D=.50

Frozen geometry/material:

```text
a=9000 mm
b=12000 mm
k=b/a=1.3333333333
h=130 mm
tc=122 mm
ts=4 mm
eps0=0.0018712490394580678
fc=30.4 MPa
Es=206000 MPa
fy=355 MPa
nu_c=.18
nu_s=.30
q0=.0015
A0=18 mm
```

Parent D+q+c state:

```text
q=.007244278905
c=-.0154563484942
Ainc=86.93135 mm
Atotal=104.93135 mm
M=.1957107654
B=.1942280304
P=37.34514010 MN
R20=-19.48685822 MN mm
R02=-23.47348406 MN mm
```

Best released augmented near-equilibrium:

```text
q=.008002
c=-.077622
p20=-.060657
p02=.165133
Ainc=96.024 mm
Atotal=114.024 mm
Atotal/h=.87711
M=.2321712005
B=.2145434653
Mq=50.11678245
Bq=26.81123035
P=37.69591555 MN
Rq=-3.06330915 MN mm
Rc=+.01005384 MN mm
R20=-.05300744 MN mm
R02=-.02373140 MN mm
```

Generalized membrane strain amplitudes are not intrinsically huge despite the numerical coordinate values:

```text
eps0*c   = -1.4525e-4
eps0*p20 = -1.1350e-4
eps0*p02 = +3.0900e-4
```

The larger magnitude of `c,p20,p02` therefore does not by itself imply physical-strain blow-up.

## 8. Final diagnosis

```text
PHYSICAL THEORY EXPLOSION                  = NO
OUT-OF-PLANE MODAL EXPLOSION               = NO
LOW-ORDER POLYNOMIAL DEGREE EXPLOSION      = NO
LOW-ORDER INVARIANT SUPPORT EXPLOSION      = NO
FORMAL INTEGRATION COMPLEXITY CHANGE        = NO
DENSE HIGH-ORDER BOUNDING-BOX FILL-IN       = YES
RAW JACOBIAN SCALING PROBLEM                = YES
PHYSICAL JACOBIAN SINGULARITY               = NOT ESTABLISHED
```

The current runtime gate is therefore an implementation representation problem, not evidence that the FvK membrane completion itself violates the desired compact theory structure.

## 9. Current next step

Remain at D=.50 and implement

```text
DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050
```

The required change is computational ordering only: contract the current material operator directly against the five needed generalized quantities `P,Rq,Rc,R20,R02` and their directional Jacobian entries, instead of building avoidable full high-order dense stress tensors.

No Pu or D continuation is authorized before that evaluator reproduces/certifies the fixed-D state.
