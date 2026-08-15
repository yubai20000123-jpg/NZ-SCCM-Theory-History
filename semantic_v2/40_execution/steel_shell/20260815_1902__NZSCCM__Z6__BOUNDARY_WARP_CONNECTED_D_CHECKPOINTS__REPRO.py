"""Evaluate persisted Z6 boundary-warp connected-D checkpoints.
This script intentionally does not invent a Pu or select roots from Zhou/Winter.
It imports the same zero-structural-quadrature current-operator extension used at D=0.5.
"""
from pathlib import Path
import importlib.util
HERE=Path(__file__).resolve().parent
P=HERE/'20260815_1844__NZSCCM__Z6__BOUNDARY_WARP_D050_CURRENT_OPERATOR__REPRO.py'
s=importlib.util.spec_from_file_location('bw',P);bw=importlib.util.module_from_spec(s);s.loader.exec_module(bw)
bw.base.set_compiler(-1.75,.45,601)
cas=dict(b=12000.,ell=9000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.0015)
pts=[
 (.50,.007244278905,-.0154563484942,'CERTIFIED'),
 (.55,.0081982051032,-.0200407144410,'NEAR_EQUILIBRIUM'),
 (.60,.0091774724300,-.0265508834600,'NEAR_EQUILIBRIUM'),
 (.625,.0096456265800,-.0300476754200,'NOT_CERTIFIED'),
 (.65,.0099845100000,-.0297538300000,'EXPLORATORY_NOT_EQUILIBRIUM'),
]
for D,q,c,status in pts:
    r=bw.total(D,q,c,cas)
    print(dict(D=D,q=q,c=c,status=status,P_MN=r[0]/1e6,Rq_MNmm=r[1]/1e6,Rc_MNmm=r[2]/1e6,Pc_MN=r[3]/1e6,Ps_MN=r[4]/1e6))
