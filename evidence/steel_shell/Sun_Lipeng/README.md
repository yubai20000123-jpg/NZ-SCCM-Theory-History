# 孙立鹏 — PBL加劲型薄壁钢管混凝土桥塔：有效理论证据包

Authoritative source: `PBL加劲型薄壁钢管混凝土...塔的计算理论与设计方法研究_孙立鹏.pdf`

- PDF SHA-256: `e441312bd0585536bbb7244e6cc2aaa37235fbe7a75f2c1e934f1a4e78981a6e`
- frozen `pdftotext -layout` extraction SHA-256: `2c7eda7fb72c7702eed78d18fca5d5cbdd51f2956a1a88c6124cee099a160e92`

Following `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`, the 187-page thesis is not mirrored in full. The following Chapter-3 regions are archived because they directly constrain the Y/steel-shell theory discussion.

## Archived excerpts

1. `01_flat_plate_elastic_inelastic_buckling.txt`
   - frozen extraction lines `2825–3055`
   - local excerpt SHA-256: `95347009fb873c2f355c1bec9fc359ad74506e8b80ace55dc46256bfcd0af883`
   - includes: unilateral-constrained plate model; four-edge fixed approximation; elastic `k=10.67`; Bleich tangent-modulus inelastic plate equation; single-term double-cosine mode; Ramberg–Osgood relation; normalized slenderness limits.

2. `02_PBL_stiffened_elastic_buckling_boundary.txt`
   - lines `4515–4735`
   - SHA-256: `8f9018c55a3e02245ebe9fb185c3a086a21bf1442b22414b8567f8d440a64f5f`
   - includes: PBL-stiffened unilateral plate model; global-stiffener mode vs local subpanel mode; equivalent continuous elastic support; energy expressions; `ko`, `ks`, minimum buckling coefficients; limiting relative PBL stiffness.

3. `03_PBL_postbuckling_strength_conclusion.txt`
   - lines `4726–4795`
   - SHA-256: `5d38155d99219406ff0a5f3ac8a812a15127c7d22c3bd8dfdd61d92b543fa2dc`
   - includes: effective-area postbuckling method and Chapter-3 conclusions.

## Current-project interpretation boundary

Retained as source evidence:

- concrete unilateral restraint motivates outward-only wall buckling;
- four-edge strong/fixed boundary is a defensible idealization for selected local shell subpanels;
- Bleich tangent-modulus/Ramberg–Osgood route is useful historical elastoplastic buckling theory;
- the distinction between stiffener-global mode and inter-stiffener local mode is mechanically meaningful;
- limiting relative PBL stiffness is useful evidence for when a PBL line can behave as a strong local boundary.

Not automatically adopted into the current formal NZ-SCCM/Y operator:

- the explicit continuous PBL spring energy term;
- the thesis effective-width/effective-area design closure;
- preclassification of the current formal solution into historical mode classes before solving;
- any empirical design equation as a replacement for a future shell material/stability operator.

This distinction preserves the original mechanics without undoing later project decisions that PBL is presently treated as a strong local boundary rather than an explicit independent spring/load-bearing term in the formal UCFT/NZ-SCCM mother theory.
