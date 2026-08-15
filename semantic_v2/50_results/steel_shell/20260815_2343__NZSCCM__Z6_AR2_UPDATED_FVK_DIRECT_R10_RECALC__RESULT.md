# Z6 AR2 updated-FvK direct-R10 continuum audit result

**Result identity:** `Z6_AR2_UPDATED_FVK_R10_DIRECT_CONTINUUM_AUDIT_RECALC`

## Geometry

```text
a/b=2.0
a=24000 mm
b=12000 mm
m=2
ell=12000 mm
A0=a/500=48 mm
```

## Updated equilibrium

```text
unknown internal coordinates at each D: q,c,p20,p02
balance: Rq=Rc=R20=R02=0
```

## Peak

High-order audit peak:

```text
D_peak ≈ 0.8308
q_peak ≈ 0.01712
c_peak ≈ -0.538
p20_peak ≈ -0.700
p02_peak ≈ +0.697
Pu_audit ≈ 40.97 MN
```

At D=.8308, 160x160x60 independent audit:

```text
P=40.9733400613 MN
Pc≈20.69203 MN
Ps≈20.28131 MN
Ainc≈205.41984 mm
Atotal≈253.41984 mm
Atotal/h≈1.94938
slope estimate≈0.06635 rad≈3.80 deg
R10 normalized principal lambda≈[-1.13695,+0.47949]
steel trial rmax≈1.30146
```

Local steel radial yielding is active near the peak.

## Comparison

```text
old AR2 R10 direct-continuum audit without complete membrane redistribution: 44.5529191054 MN
updated membrane equilibrium audit:                                40.9733400613 MN
difference:                                                       -3.5795790441 MN
relative:                                                         -8.0344 %

Zhou comparator:                                                   49.4867667519 MN
updated-vs-Zhou:                                                  -17.2034 %

Winter comparator:                                                 50.1858541295 MN
updated-vs-Winter:                                                -18.3568 %
```

## Interpretation lock

The missing FvK membrane coordinates are mechanically active, but releasing them does **not** automatically increase postbuckling capacity. In the current reduced two-face steel object they lower the connected peak and drive strong membrane redistribution/local steel yielding.

This is an audit-only direct-R10 continuum result. It is **not** a formal N48/D15 zero-spatial-quadrature production release.

The current augmented equilibrium also does not yet include the longitudinal PBL/web steel phase; therefore it is not the final full-section Z6 capacity.
