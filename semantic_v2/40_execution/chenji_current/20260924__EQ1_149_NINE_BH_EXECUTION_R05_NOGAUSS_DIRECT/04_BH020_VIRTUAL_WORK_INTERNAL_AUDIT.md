# R05 internal virtual-work audit — BH020 predictor at dbar=0.0018

Date: 2026-09-24

## State used

BH020, b=a_h=1000 mm, Delta=3.6 mm.
q=1.9119884635e-4
Aplus=0.2102997054 mm
Aminus=0.1926430184 mm
epsx_bar=4.3819290784e-4
epsy_bar=-1.7987754890e-3
ex_alpha=1.9129663899e-7
ey_beta=1.7420035445e-7
Fx=65881.445204
Fy=58089.100681
P=3.272539852 MN
q0=0.0025
A0=0.140625 mm

The resulting ten raw residuals are:
R1=-113.2810653
R2=-4.97444298e-4
R3=+3.18297638e-3
R4=-86.8969602
R5=+0.252966938
R6=-0.0409388123
RAplus=-41580.965852
RAminus=-34456.909889
Rq=-248481.804397
Rdelta≈0.

## Rq decomposition

Rq1=20470649.888598
Rq2=-21714289.100496
Rq3=-1524195.485410
Rq4=2519352.892906
sum=-248481.804397.

Rq1 material/moment decomposition:
UHPC Mx: +138683.846317
TOP steel Mx: -2716058.463682
BOTTOM steel Mx: +8730765.357535
UHPC My: +153271.273554
TOP steel My: -130804795.993157
BOTTOM steel My: +136713180.627581
web My: +56783.613871
UHPC Mxy: +2056774.332711
TOP steel Mxy: +3052706.867357
BOTTOM steel Mxy: +3089338.426511

Grouped:
UHPC total Rq1 = +2348729.452581
TOP steel total Rq1 = -130468147.589481
BOTTOM steel total Rq1 = +148533284.411627
web total Rq1 = +56783.613871.

Rq2 exact retained-Airy expression for a_h=b:
Rq2=(q0+q)[(pi^4/2)(Fx+Fy) - (pi^2 b P/4)]
= -21714289.100496.

Rq3 component split:
sigma_x term +161555.351721
sigma_y term -1861679.219741
tau term +175928.382611
sum=-1524195.485410.

Rq4 component split:
sigma_x term +248934.912216
sigma_y term +2158779.920200
tau term +111638.060490
sum=+2519352.892906.

TOP local residual:
+83927.291723 (sigma_x)
-165427.372334 (sigma_y)
+39919.114759 (tau)
sum=-41580.965852.

BOTTOM local residual:
+68296.510021 (sigma_x)
-138248.163405 (sigma_y)
+35494.743495 (tau)
sum=-34456.909889.

## Critical implementation disclosure

The quoted numerical values above were produced by the current zero-spatial-Gauss Fourier-polynomial execution backend, NOT by exact evaluation of the signed-C1 rational law and exact pointwise Eq.(83)-(85) Mises factor.

The backend currently uses:
sigma_U_num(e)=4012.04473 e - 156801.533 e^2 - 1.73978833e7 e^3,
secant_U_num(e)=43400 - 1.42492569e6 e - 1.74513902e8 e^2,
and, when the steel plastic-bound branch is active,
g_num(r)=1 - 0.01731828 r,
instead of the exact g=1/sqrt(r) for r>1.

At this BH020 state both steel faces enter the approximate cap branch (bound indicators about 2.2446 and 2.1255).

Therefore these Rq values are diagnostic outputs of the polynomial backend and must not be called exact Eq.(57)-(85) results. The governing virtual-work formulas remain Eq.(105)-(109), but the material evaluation backend must be replaced before formal numerical results are accepted.
