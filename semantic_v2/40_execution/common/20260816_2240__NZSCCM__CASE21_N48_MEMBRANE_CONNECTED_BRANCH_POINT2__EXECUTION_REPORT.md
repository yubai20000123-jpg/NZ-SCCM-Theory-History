# Case21 membrane connected branch — accepted point 2

**2026-08-16 22:40 +08:00**

Starting state is the locked point 1 at `q=1e-4`. The next continuation parameter is

`q2=2e-4`.

## Predictor

First secant-style predictor doubled the first state:

```text
D=0.032092612
r=2*r(point1)
```

N=20 predictor evaluation:

```text
||Rm||2=0.0356441062091
Rq=-3.07048911485 kN mm
P=31.8183777149 kN
```

The exact zero-state five-membrane tangent `Krr0` from the previous gate was used only as a local corrector preconditioner. Its first correction was

```text
Delta r=[-3.4033024253e-5,
         +1.8538228852e-5,
         +4.6927280512e-5,
         +1.3644315672e-4,
         -7.5043075574e-5]
```

At the same D this gave

```text
||Rm||2=0.00230955197529
Rq=-2.89872881757 kN mm
```

## Rq bracketing/correction

With corrected `r`:

```text
D=0.031690000 -> Rq=+0.426721413201 kN mm
D=0.032092612 -> Rq=-2.898728817568 kN mm
```

Interpolation/correction:

```text
D=0.031741670 -> Rq=+0.001015778388 kN mm
```

At that state `||Rm||2=0.00333888573`. A second internal correction was

```text
Delta r=[+2.0611101845e-6,
         +5.0099649717e-8,
         -2.5590584631e-6,
         -1.3880132506e-5,
         +5.9767122834e-6]
```

followed by one small residual correction and one D correction.

## Accepted N=28 corrector state

```text
q=0.000200000000000
D=0.031737797000000
r0 =-0.0009851269073948984
r20=-0.0004459452528374698
r22=+0.0006055135286393538
s02=-0.0003630828054164307
s22=+0.0005376886688340636
```

N=28 corrector gives

```text
Rm=[-3.1233995587e-7,
    +5.2660701095e-7,
    -3.3182002435e-7,
    +1.3448198007e-5,
    +1.4630120726e-6]
||Rm||2=1.3545457160e-5
Rq=+3.9798686409e-6 kN mm
Pc=30.2812892446083 kN
Ps=1.1487318823342 kN
P =31.4300211269425 kN
```

N=20 predictor and N=28 corrector agree at this accepted state to displayed precision.

## Continuous compiler-domain certificate

```text
Cm=0.002455595353381085
Cb=0.007470521803318873
ex in [-0.00379430403219,+0.0157052524908]
ey in [-0.0401090902776,-0.0209109083690]
X11 in [-0.0113827410936,+0.0123411419847]
X22 in [-0.0421579836744,-0.0186895028118]
|X12|<=0.00647433284894
lambda in [-0.0486323165234,+0.0188154748336]
```

Compiler interval is `[-1.15,+0.12]`; both margins remain positive.

## Gate status

```text
POINT1_ACCEPTED=YES
POINT2_ACCEPTED=YES
CONNECTED_DIRECTION=P_INCREASING
P1=15.2626325741 kN
P2=31.4300211269 kN
FULL_BRANCH=OPEN
SCHUR=OPEN
NEW_Pu=NOT_RELEASED
```

Next execution continues to point 3 from point 1–2 secant predictor. No root-cloud search and no old-limit initialization.