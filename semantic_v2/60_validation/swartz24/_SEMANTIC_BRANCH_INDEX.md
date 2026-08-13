# Swartz24 validation semantic branch

Current stored validation entry:

- the 24-row C1/MM + general-D15 first-load-maximum comparison is located in `semantic_v2/50_results/swartz24/`.

## Governing-capacity boundary

The 24 stored loads are equilibrium first-load-maximum candidates. Governing physical capacity additionally requires the same-branch full current-tangent ordering:

```text
first KZ=0 vs first L=0, g:+->- maximum
```

Case21 has the formal zero-spatial ordering completed. The other 23 formal KZ orderings remain pending.

## 2026-08-13 18:34 governing correction — LOCKED

Highest-priority governance is now:

- `semantic_v2/10_governance/20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

The following interpretation is now locked:

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
FORMAL_HALFWAVE = THEORETICAL ENERGY/MINIMUM ADMISSIBLE HALFWAVE FROM DESIGN DATA
OBSERVED EXPERIMENTAL BULGE LENGTH/LOCATION = VALIDATION / INTERFERENCE EVIDENCE ONLY
NGUYEN SECOND-ORDER MEMBRANE STRAIN = ALREADY INCLUDED
ADD u,v RITZ TO REPAIR A GENERIC MISSING MEMBRANE EFFECT = REJECTED
R10 = FROZEN
COMPILER = CURRENT N48-C1/MM
GENERAL-D15 = FROZEN
DIRECT LIMIT = Rq=0 + L=0, FIRST +->- MAXIMUM
```

Accordingly, the earlier 17:56 diagnostic that redefined Cases1-16 production halfwave length from the observed/FE long-wave pattern is **SUPERSEDED AS A PRODUCTION INPUT RULE**. Its numerical direction checks remain historical diagnostic evidence only.

The 18:16 ideal-mode/imperfection/postbuckling narrative is also **PARTIALLY SUPERSEDED** wherever it asserted a missing generic membrane-redistribution mechanism. Nguyen second-order kinematics already contains the nonlinear membrane strain terms through `chi_q=q0*q+q^2/2` and the corresponding `Cmx,Cmy,Cmxy` field.

The valid retained lesson is narrower: noncanonical experimental bulges, eccentricity, thickness variation, support imperfections and other specimen nonidealities can explain departures of an experiment from the theoretical minimum halfwave; they do not redefine the formal halfwave or the locked theory.

## Current interpretation of Swartz accuracy

The current successful Swartz results are treated as evidence that the locked theory has predictive capability. Experimental departures from the formal minimum-halfwave response are external validation effects to be discussed after the blind theoretical solution, not terms to be inserted into the governing equations.

No specimen-specific imperfection, halfwave length, material coefficient or root may be inferred from `Pf`.

## Case1 reconstruction evidence retained with qualification

The square-halfwave Case1 audit reconstructed

```text
D ~ 0.98833818
q ~ 0.00083313173
P ~ 608.92642 kN
KZ_audit at maximum ~ +3066.68 N/mm
```

and isolated a compiler value/tangent effect. Its high-order Gauss evaluator is audit-only; formal zero-spatial Case1 KZ remains pending.

The later long-halfwave `~647.5 kN` result is also audit-only and is **not** promoted as the formal Case1 production geometry merely because Nguyen/experiment showed a long-wave pattern.

## Source-level specimen nonidealities retained as validation evidence

The original Swartz papers and Nguyen's review support real specimen/test nonidealities such as:

```text
within-panel thickness variation ~ +/-3%
unavoidable load eccentricity
discrete support/load bedding
noncanonical/localized bulging
project q0=b/400 not being a measured Case1 imperfection
only limited cylinder-based material sampling
```

These remain legitimate post-solution physical discussion only. They may not be used to calibrate the locked theory.
