#!/usr/bin/env python3
"""R18 exact linear assembler from six R17 spectral states to nine masks.

This is a finite algebraic re-expression of the already verified R17 state
partition.  It introduces no new material law and no spatial partition.

If F_ss denotes any smooth branch quantity (stress component, generalized-force
integrand, or same-source derivative) evaluated in ordered spectral state ss,
then the global piecewise quantity is sum_ss I_ss F_ss.  R17 expresses every
state indicator I_ss as an idempotent polynomial in nine reusable Heaviside
products.  This script collects those terms once, yielding nine smooth
coefficient combinations G_mask.
"""
from __future__ import annotations
import json
import sympy as sp

states=['00','10','11','20','21','22']
masks=['0000','0001','0011','0100','0101','0111','1100','1101','1111']
F={s:sp.Symbol('F_'+s) for s in states}
state_masks={
 '00':{'1100':-1,'0100':1},
 '10':{'0111':1,'0101':-1,'0011':-1,'0001':1},
 '11':{'1111':-1,'1101':1},
 '20':{'1111':-1,'1101':1,'1100':-1,'0011':1,'0001':-1,'0000':1},
 '21':{'1101':-1,'1100':1},
 '22':{'0011':1},
}
G={m:sp.expand(sum(sp.Integer(state_masks[s].get(m,0))*F[s] for s in states)) for m in masks}
reconstructed=sp.expand(sum(G[m]*sp.Symbol('H_'+m) for m in masks))
direct=sp.expand(sum(F[s]*sum(sp.Integer(c)*sp.Symbol('H_'+m) for m,c in state_masks[s].items()) for s in states))
assert sp.expand(reconstructed-direct)==0
report={
 'identity':'NZSCCM_Z1_R18_GLOBAL_MASK_COEFFICIENT_ASSEMBLY',
 'parent':'R17 six-state / nine-mask spectral-Heaviside constructor',
 'state_order':states,
 'mask_order':masks,
 'mask_coefficients':{m:sp.sstr(G[m]) for m in masks},
 'identity_reconstruction_pass':True,
 'application':'For every smooth branch quantity F (Sxx,Syy,Sxy and same-source derivatives), compute the six branch values once and combine them with these nine global mask coefficients before exact semialgebraic integration.',
 'governance':{
   'spatial_sampling':0,
   'spatial_quadrature':0,
   'spatial_subdomains':1,
   'material_points':0,
   'finite_prefix':0
 }
}
print(json.dumps(report,ensure_ascii=False,indent=2))
