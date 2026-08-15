"""NZ-SCCM D=.55 connected continuation gate reproducer.

Imports the certified 22:35 directional moment-first evaluator.  It does not
change the physical theory or formal General-D15 integration.  The default run
reproduces only the completed D=.55-at-D050-coordinate evaluation and computes
stored predictor coordinates.  Expensive predictor evaluation is deliberately
not launched automatically because the audited same-expression call exceeded
180 s in the execution window.
"""
from pathlib import Path
import importlib.util, numpy as np, time
HERE=Path(__file__).resolve().parent

PARENT=HERE/'20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__REPRO.py'
spec=importlib.util.spec_from_file_location('mf',PARENT)
mf=importlib.util.module_from_spec(spec); spec.loader.exec_module(mf)

X050=np.array([0.008003063422252722,-0.07766034129851779,-0.06065823792663306,0.16525678113314005])
J050=np.array([
 [2787333.552306, 96636.847993, -7730.455557, 19480.240744],
 [67271.966759, 7906.237458, -914.530413, 2343.313840],
 [-20821.855030, -785.947042, 155.898351, 46.725646],
 [-4168.426027, 2094.413911, -426.456221, 882.897056]
])

def eval_state(D,x,ctol=5e-4):
    state=dict(D=float(D),q=float(x[0]),cw=float(x[1]),p20=float(x[2]),p02=float(x[3]))
    t0=time.time(); tot,cc,ss=mf.total(state,ctol=ctol)
    return state,time.time()-t0,np.array(tot),np.array(cc),np.array(ss)

def predictor(x,residual_MNmm):
    dx=np.linalg.solve(J050,-np.asarray(residual_MNmm,float))
    return dx,x+dx

if __name__=='__main__':
    mf.base.set_compiler(-1.75,.45,601)
    state,dt,tot,cc,ss=eval_state(.55,X050,5e-4)
    print('D055 reused D050 coordinates',state)
    print('runtime_s=',dt)
    print('total [P,Rq,Rc,R20,R02] MN or MNmm=',tot/1e6)
    print('concrete=',cc/1e6)
    print('steel=',ss/1e6)
    dx55,x55=predictor(X050,tot[1:]/1e6)
    print('D055 predictor delta=',dx55)
    print('D055 predictor coordinates=',x55)
    # Stored execution: evaluating x55 through inherited dense buildS exceeded
    # 180 s.  Do not silently replace it with another integral/constitutive path.
    print('formal spatial sampling/quadrature=0; Pu not solved')
