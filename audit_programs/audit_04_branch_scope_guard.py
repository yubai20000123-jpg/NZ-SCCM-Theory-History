#!/usr/bin/env python3
import pathlib,subprocess,sys
root=pathlib.Path(__file__).resolve().parents[1]
branch=subprocess.check_output(['git','branch','--show-current'],cwd=root,text=True).strip()
expected='archive/ma-origin-recovery-20260823'
if branch!=expected:
    print(f'BRANCH_SCOPE_FAIL current={branch} expected={expected}'); sys.exit(1)
print('BRANCH_SCOPE_PASS '+branch)