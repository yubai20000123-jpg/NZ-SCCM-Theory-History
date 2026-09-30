#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UCFT M8 frozen production UHPC normal-direction law."""
from pathlib import Path
import numpy as np
import pandas as pd
from numpy.polynomial import Polynomial

class GeneralPiecewiseUHPC:
    def __init__(self, thresholds, stress_polynomials):
        self.thresholds=[float(x) for x in thresholds]
        self.P_branch=list(stress_polynomials)
        if len(self.P_branch)!=len(self.thresholds)+1:
            raise ValueError('need one more branch than thresholds')
        E=Polynomial([0.0,1.0])
        self.F_branch=[]; self.H_branch=[]
        Fprev=Polynomial([0.0]); Hprev=Polynomial([0.0])
        self.F_branch.append(Fprev); self.H_branch.append(Hprev)
        for j in range(1,len(self.P_branch)):
            P=self.P_branch[j]
            rawF=P.integ(); rawH=(E*P).integ()
            x0=self.thresholds[j-1]
            F=rawF + Polynomial([Fprev(x0)-rawF(x0)])
            H=rawH + Polynomial([Hprev(x0)-rawH(x0)])
            self.F_branch.append(F); self.H_branch.append(H)
            Fprev,Hprev=F,H
    def branch_index(self,e):
        return int(np.searchsorted(self.thresholds,float(e),side='right'))
    def stress(self,e):
        i=self.branch_index(e); return float(self.P_branch[i](float(e)))
    def tangent(self,e):
        i=self.branch_index(e); return float(self.P_branch[i].deriv()(float(e)))
    def FH(self,e):
        i=self.branch_index(e); x=float(e)
        return float(self.F_branch[i](x)),float(self.H_branch[i](x))

def _local_cubic_to_global(e_left,c0,c1,c2,c3):
    s=Polynomial([-float(e_left),1.0])
    return float(c0)+float(c1)*s+float(c2)*s**2+float(c3)*s**3

def build_production_law(csv_path=None,Ec=43400.0,fc=141.1,eps_c0=0.0035,
                         ft=7.2,e_cr=0.00042,e_tp=0.0038,e_loc=0.0069,e_tu=0.00759):
    E=Polynomial([0.0,1.0])
    Ac=Ec*eps_c0/fc; Bc=6.0-5.0*Ac; Cc=4.0*Ac-5.0
    Pc=Ec*E + fc*Bc/eps_c0**5*E**5 - fc*Cc/eps_c0**6*E**6
    roots=[z.real for z in Pc.roots() if abs(z.imag)<1e-12 and z.real<0]
    e_z=min(roots)
    fcr=ft*(10.1/11.1)
    e_el=fcr/Ec
    Pel=Ec*E
    Pplateau=Polynomial([fcr])
    if csv_path is None:
        csv_path=Path(__file__).with_name('UCFT_M8_UHPC拉伸分段三次多项式系数.csv')
    df=pd.read_csv(csv_path)
    cubics=[]
    for _,r in df.iloc[1:].iterrows():
        cubics.append(_local_cubic_to_global(r.e_left,r.c0,r.c1,r.c2,r.c3))
    zero=Polynomial([0.0])
    thresholds=[e_z,0.0,e_el,e_cr,e_tp,e_loc,e_tu]
    branches=[zero,Pc,Pel,Pplateau,*cubics,zero]
    law=GeneralPiecewiseUHPC(thresholds,branches)
    law.Ec=Ec;law.fc=fc;law.eps_c0=eps_c0;law.ft=ft
    law.e_z=e_z;law.e_el=e_el;law.e_cr=e_cr;law.e_tp=e_tp;law.e_loc=e_loc;law.e_tu=e_tu;law.fcr=fcr
    return law

def self_check(law=None):
    law=build_production_law() if law is None else law
    pts=[law.e_z,0.0,law.e_el,law.e_cr,law.e_tp,law.e_loc,law.e_tu]
    jumps=[]
    for x in pts:
        dx=1e-12*max(1.0,abs(x))
        jumps.append(abs(law.stress(x-dx)-law.stress(x+dx)))
    grid=np.linspace(0,law.e_tu,4001)
    vals=np.array([law.stress(x) for x in grid])
    return {
      'max_interface_stress_jump_MPa':float(max(jumps)),
      'sigma0':law.stress(0.0),
      'initial_tangent_MPa':law.tangent(0.5*law.e_el),
      'sigma_peak':law.stress(law.e_tp),
      'sigma_terminal':law.stress(law.e_tu+1e-10),
      'tension_min':float(vals.min()),'tension_max':float(vals.max()),
      'thresholds':law.thresholds,
    }

if __name__=='__main__':
    print(self_check())
