# NC POSTPEAK C2 SCALAR TARGET RULE — 2026-08-10

## Identity

This rule belongs to the existing G18/G20/G27 unified current-map route. It is a material-target rule, not a runtime TT/TC/CC state machine and not a structural calibration rule.

## Source anchor

Nguyen Eqs. 3.69–3.73 use a post-crushing bilinear compression law: stress falls linearly from the peak `sigma_p` at `eps_p` to `0.1 sigma_p` at `gamma2 eps_p`, then remains at the 10% residual level with zero tangent. Current source baseline: `gamma2=10`.

The source bilinear handoff contains tangent jumps at the compression peak and at residual onset. G20/G21 already permit C1/C2 regularization for the memoryless analytic production current surface.

## R06 C2 target

Let

```text
s = (-lambda-1)/9,     0 <= s <= 1
sigma/fc = -1 + 0.9 q(s)
```

The exact source line is `q=s`.

R06 keeps the source line exactly except for two endpoint C2 bridges. The normalized start bridge is

```text
g(tau) = 3 tau^5 - 8 tau^4 + 6 tau^3
```

with

```text
g(0)=g'(0)=g''(0)=0
g(1)=1
g'(1)=1
g''(1)=0
```

The end bridge is symmetric.

Frozen R06 bridge width:

```text
delta_s = 0.05
Delta_lambda = 9 delta_s = 0.45 per endpoint
```

Selection rule: local increase of compression magnitude relative to the exact source bilinear line must not exceed 1% fc. Executed R06 value:

```text
max extra compression = 0.888889% fc
max conservative reduction = 0.888889% fc
```

Endpoint conditions:

```text
U(-1)=-1
U'(-1)=0
U(-10)=-0.1
U'(-10)=0
```

## Status

```text
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
```

This target may be used as the NC material-level postpeak target in later compact scalar compilation.

## Prohibitions

- no Case21/Swartz Pu calibration of `delta_s`;
- no runtime spatial/material-state split is implied;
- no inference that the same numerical postpeak target applies to UHPC;
- UHPC must define its own postpeak/hardening/softening target from UHPC sources.
