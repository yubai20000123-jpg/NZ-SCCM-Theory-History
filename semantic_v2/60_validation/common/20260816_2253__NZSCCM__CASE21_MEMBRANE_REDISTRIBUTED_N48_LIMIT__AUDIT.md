# Audit — Case21 membrane-redistributed N48 limit

**Timestamp:** 2026-08-16 22:53 +08:00

## Gate checklist

```text
01 existing Case21-local N48 coefficient identity = PASS
02 18:02 r=0 fingerprint reproduction = PASS
03 five membrane residuals Rm = PASS
04 total Rq = PASS
05 connected-branch first load maximum bracket = PASS
06 N28 final corrector = PASS
07 continuous compiler-domain Bernstein certificate = PASS
08 rebar elastic branch certificate = PASS
09 old-state KZ regression = PASS
10 same-state new KZ = PASS / positive
11 formal spatial quadrature = 0
12 formal spatial sampling = 0
13 formal thickness quadrature = 0
14 experiment excluded until after theory result = PASS
```

## Final state audited

```text
D = 0.4597278541813354
q = 0.0018330938013757293
A = 2.2363744376783896 mm
r0  = -0.012475802483156403
r20 = -0.007141864103343101
r22 = +0.04699488414266459
s02 = +0.041946118067216
s22 = -0.09983629747628982
Pc = 304.05427812103903 kN
Ps =  16.694907204543117 kN
P  = 320.7491853255822 kN
Rq = +2.3335610177355193e-4 kN mm
||Rm||2 = 3.489005279868966e-6
```

## Limit bracket

Neighboring N28-equilibrated states are lower in load:

```text
local s=-0.001 -> P=320.7448725628 kN
local s=-0.002 -> P=320.7488729415 kN
local s=-0.004 -> P=320.7455659492 kN
```

Quadratic stationary locator gives `P≈320.74947 kN`; the re-equilibrated final state gives `320.74919 kN`. The difference is `0.00028 kN`, negligible relative to the engineering precision of the material/structural model.

## Compiler-domain audit

Final Bernstein lower bounds:

```text
min B[0.12-X11]              = 0.0198184192764
min B[det(0.12I-X)]          = 0.0125848299978
min B[X11+1.15]              = 1.0807409482495
min B[det(X+1.15I)]          = 0.5069185061517
```

All positive. Hence the entire complete halfwave lies inside the Case21-local compiler interval `[-1.15,+0.12]` without spatial sampling.

## Rebar audit

```text
max |epsilon_s| ~= 0.00125716
steel yield epsilon_y = 0.00265
```

PASS elastic.

## KZ audit

Old-state regression:

```text
computed KZ old = +0.3807488044 N/mm
frozen 18:02 KZ old = +0.3795268508 N/mm
absolute difference = 0.0012219536 N/mm
```

New same-state result:

```text
KZc_mat = +871.8683854054
KZc_geo = -587.3952216885
KZs_mat = 0
KZs_geo = -24.3022580441
KZtotal = +260.1709056728 N/mm
```

The new limit point is well inside the positive tangent-stability side. Therefore the capacity control is the first connected load maximum, not a pre-limit KZ zero.

## N48 scope audit

This audit explicitly does **not** promote N48 to the NC family compiler. The 12:29 family-source gate on `[-2.60,+2.15]` recorded `N48: E_sigma=0.817103, E_tan=0.954681 -> FAIL` and first family-source pass at `N=3584`. The present N48 result is valid only under the already-reproduced Case21-local interval and the new continuous domain certificate.

## Verdict

```text
CASE21_MEMBRANE_REDISTRIBUTED_LIMIT = PASS
Pu = 320.75 kN
CONTROL = FIRST_CONNECTED_LOAD_MAXIMUM
KZ_AT_Pu = +260.17 N/mm
N48_SCOPE = CASE21_LOCAL_ONLY
Z6_CASE21_N48_REUSE = PROHIBITED
```
