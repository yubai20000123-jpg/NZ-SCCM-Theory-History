# NZ-SCCM — step-5 blocker resolution audit R01

**Time:** 2026-08-27 11:55 +08:00  
**Parent:** unified q–U explicit kinematic ledger R01  
**Status:** `BLOCKERS RESOLVED AS FAR AS AVAILABLE SOURCES ALLOW / NO ROOT INVENTED`

## 1. Geometry/phase blocker

The accepted BH family ODB extraction contract explicitly requires the actual steel-face subpanels to be discovered from shell connectivity, with PBL/web attachment edges acting as subpanel boundaries. It prohibits hard-coding a theoretical sinusoidal cell. The later family extraction reports 5 TOP and 6 BOTTOM actual face subpanels per model, but the currently archived summary does not contain their absolute boundary coordinates.

The qU term depends on the physical registration through exact moments such as

\[
\langle\psi_x\phi_x\rangle,
\qquad
\langle\psi_y\phi_y\rangle,
\]

and therefore absolute subpanel origin/registration cannot be replaced by an antinode-centered assumption.

A read-only Abaqus 2019-compatible extractor is added with this audit:

`20260827_1155__NZSCCM__BH_PBL_SUBPANEL_GEOMETRY_EXTRACTOR_R01.py`

It:

1. opens the canonical ODB read-only;
2. classifies steel-face shell elements from undeformed normals;
3. finds PBL/web attachment boundaries by shell-edge adjacency;
4. constructs actual TOP/BOTTOM connected subpanels;
5. emits exact node labels and global x/y/z coordinate bounds.

It does not infer a favorable local sign from the loaded FEM response. The sign/orientation must come from the stress-free initial imperfection geometry/model definition.

This closes the **method** for geometry recovery, but not the missing numerical coordinates in the present remote runtime because the local multi-GB ODBs are not mounted here.

## 2. UHPC shear blocker

The source audit was extended beyond the current SSUHPC directional N-M contract.

Current source evidence distinguishes three different objects:

### A. Initial isotropic elastic UHPC subregion

A complete plane-stress operator exists:

\[
\boldsymbol\sigma=2G\mathbf E+\lambda_{ps}I_1\mathbf I.
\]

This includes a legitimate elastic shear response, but only while the material remains in the initial elastic subregion.

### B. Historical UCFT layer-0 spectral operator

Historical files contain a mathematically complete spectral plane-stress completion with

\[
h_{12}=\frac{\sigma_1-\sigma_2}{\varepsilon_1-\varepsilon_2}
\]

and a repeated-eigenvalue limit. It produces global shear stress/tangent.

However, that operator belongs to the historical UHPC layer-0/equivalent-uniaxial material identity. The current NZ-SCCM material governance explicitly does not permit silently restoring that layer-0 model as the production UHPC material. Therefore it is **not imported** into the new SSUHPC q-U theory.

### C. Current SSUHPC UHPC material

The current terminal SSUHPC source freezes exact directional x/y UHPC N-M primitives from the Hu-type compression/tension backbones, but it does not freeze a nonlinear current in-plane shear law for the continuous half-wave.

The UHPC source ledgers independently state that post-cracking/general multiaxial shear remains incomplete and that ordinary-concrete shear-retention beta values must not be copied to UHPC because fiber bridging changes shear transfer.

Therefore neither

```text
tau_UHPC = 0
```

nor

```text
tau_UHPC = Gc * gamma for all states
```

nor a historical NC/UHPC-layer0 beta law is inserted.

## 3. Consequence

The rebuilt kinematics and exact integration engine are closed, but a unique nonlinear BH032/BH050 blind branch still requires:

1. actual PBL-cell registration from the canonical geometry;
2. a current UHPC shear/tensor completion explicitly accepted as part of the rebuilt material contract.

This is not a new mathematical obstruction created by qU. It is an existing source incompleteness that was hidden by the later pointwise directional N-M terminal formulation, because that formulation only sampled an antinode where the shear demand was not part of the terminal closure.

## 4. No silent fallback

```text
ANTINODE_CENTER_PHASE_ASSUMPTION = NO
FEM_FAVORABLE_PHASE_SELECTION = NO
UHPC_TAU_ZERO_ASSUMPTION = NO
UHPC_ELASTIC_SHEAR_ALL_STATES_ASSUMPTION = NO
HISTORICAL_LAYER0_RESTORATION = NO
NC_SHEAR_BETA_TRANSFER = NO
NEW_BLIND_PU = NOT_INVENTED
```

The next blind solve is executable immediately after those two source inputs are frozen; no further change to the qU/common-curvature architecture is required first.
