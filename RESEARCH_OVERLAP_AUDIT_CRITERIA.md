# RESEARCH OVERLAP AUDIT CRITERIA

Status: `BINDING_GOVERNANCE / NOT_HISTORICAL_PAYLOAD`

This file defines how future literature reviews judge whether an earlier method truly overlaps with the intended NZ-SCCM Marguerre–Airy architecture.

## 1. Six questions for every candidate paper or method

For each work, record explicitly:

1. **Out-of-plane field** — Is `w(x,y)` obtained from a mechanics-based mode/solution, or from an empirical shape/amplification rule?
2. **Membrane resultants** — Are `N_x,N_y,N_xy` obtained through Airy equilibrium/compatibility or an equivalent theoretical equilibrium solution, or by empirical redistribution/effective width?
3. **Postbuckling relation** — Is the `P-q` relation derived from Marguerre/von-Karman or another mechanics equation, or fitted/calibrated from tests/FE?
4. **Section demand** — Are `N-M` demands derived from the structural solution, or altered by empirical structural reduction/amplification factors?
5. **Ultimate condition** — Is `Pu` obtained from an explicit material/section capacity condition, or directly from a structural empirical strength curve?
6. **Location of empirical content** — Is empirical input confined to material/strength relations, or does empirical content enter the structural response/strength operator itself?

## 2. Overlap classes

### Class A — theoretical postbuckling only
Mechanics-based postbuckling solution, but no ultimate-capacity closure.

Relation to current project: front-end theoretical source, not a duplicate of the complete architecture.

### Class B — theoretical structural demand + material/section capacity
Mechanics-based structural postbuckling demand; empirical content confined to material/section capacity; Pu obtained by demand-capacity closure.

Relation to current project: **highest potential overlap**. This class requires line-by-line novelty comparison.

### Class C — semi-analytical ultimate strength with structural empirical simplification
A theoretical backbone exists, but effective-width, fitted slenderness reduction, empirical postbuckling coefficient, structural amplification/reduction factor, or similar specimen/structural empirical simplification enters before Pu.

Relation to current project: conceptually related but not methodologically identical. Swartz-type methods belong here if structural-level empirical simplifications are present.

### Class D — nonlinear/incremental structural analysis to ULS
Material nonlinearity/plasticity is embedded in the structural solve and the load path is incrementally followed to collapse/peak.

Relation to current project: physically related, but a different computational architecture.

### Class E — direct empirical/design strength formula
Ultimate load is obtained mainly from fitted/effective-width/design reduction equations.

Relation to current project: engineering comparator, not a theoretical-architecture duplicate.

## 3. High-overlap gate

A work may be labelled `HIGH_OVERLAP` only if all of the following are substantially satisfied:

- structural postbuckling demand is mechanics-derived;
- no specimen-level structural strength fit/reduction is needed;
- material empirical input is separable from the structural operator;
- the capacity condition is material-/section-specific;
- Pu is obtained from direct or finite demand-capacity closure;
- the structural class and boundary/section idealization are sufficiently close to the target composite panel.

Finding the words "postbuckling", "ultimate strength", "Airy", or "N-M interaction" is not sufficient.

## 4. Novelty wording discipline

Do not claim novelty as "first to combine postbuckling and strength" unless a comprehensive literature audit proves it.

A safer potential contribution, subject to literature verification, is:

> a common analytical mechanics architecture in which structural postbuckling demand is theoretically derived and the empirical content is confined to material-/section-specific capacity modules, extended to the target steel-concrete/UHPC composite-panel classes without a structural empirical strength reduction.
