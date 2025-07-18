#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:21:43 2024

simple program to check a possible mechanism leading to growing amplitudes

=> Indeed, first cooling followed by emittance growth seen with simple model

=> think of the problem in terms of eigenvalues of a 6x6 transfer matrix of all
   three particles!!
"""

import numpy as np
import matplotlib.pyplot as plt

nturns       = 200
muPUK, muKPU = 1.51, 2*np.pi*1.28 - 1.51
gainK        = 0.05
gainPU       = 0.

matPUK11, matPUK12, matPUK21, matPUK22 = np.cos(muPUK), np.sin(muPUK), -np.sin(muPUK), np.cos(muPUK)
matKPU11, matKPU12, matKPU21, matKPU22 = np.cos(muKPU), np.sin(muKPU), -np.sin(muKPU), np.cos(muKPU)

#rng = np.random.default_rng(18022002)
#rng = np.random.default_rng(22072005)
rng = np.random.default_rng()
fct = 0.0  # to be able to switch between two cases (fct = 0 the interesting one)!!

# now do simulation - generation of three particles followed by tracking over nturns turns
xb, xpb = [rng.normal(0, 1)], [rng.normal(0, 1)]
xg, xpg = [rng.normal(0, 1)], [rng.normal(0, 1)]
xo, xpo = [rng.normal(0, 1)], [rng.normal(0, 1)]
print('in loop over cases')
for turn in range(1, nturns + 1):
    # first get phase space coordinates out pf kicker
    xbK  = matPUK11*xb[turn-1] + matPUK12*xpb[turn-1]
    xpbK = matPUK21*xb[turn-1] + matPUK22*xpb[turn-1] + gainK*(xb[turn-1] + xg[turn-1] + fct*xo[turn-1])
    xgK  = matPUK11*xg[turn-1] + matPUK12*xpg[turn-1]
    xpgK = matPUK21*xg[turn-1] + matPUK22*xpg[turn-1] + gainK*(xb[turn-1] + xg[turn-1] + xo[turn-1])
    xoK  = matPUK11*xo[turn-1] + matPUK12*xpo[turn-1]
    xpoK = matPUK21*xo[turn-1] + matPUK22*xpo[turn-1] + gainK*(fct*xb[turn-1] + xg[turn-1] + xo[turn-1])
    # then track further to PU and coordinates to arrays
    xb.append(matKPU11*xbK + matKPU12*xpbK)
    xpb.append(matKPU21*xbK + matKPU22*xpbK)
    xg.append(matKPU11*xgK + matKPU12*xpgK)
    xpg.append(matKPU21*xgK + matKPU22*xpgK)
    xo.append(matKPU11*xoK + matKPU12*xpoK)
    xpo.append(matKPU21*xoK + matKPU22*xpoK)

# Some plotting of results
fig1 = plt.figure( figsize=(5., 8.) )
fig1.suptitle('Testing a hypothesis to\n explain unexpected emittance increase\n' +
              'seen in simulations')
ax = fig1.subplots(2, 1) 
ax[0].scatter( xb, xpb, s=1, color = 'blue' )
ax[0].scatter( xg, xpg, s=1, color = 'green' )
ax[0].scatter( xo, xpo, s=1, color = 'orange' )
ax[1].plot( [ xb[ind]**2 + xpb[ind]**2 for ind in range(nturns) ], color='blue' )
ax[1].plot( [ xg[ind]**2 + xpg[ind]**2 for ind in range(nturns) ], color='green' )
ax[1].plot( [ xo[ind]**2 + xpo[ind]**2 for ind in range(nturns) ], color='orange' )
ax[1].plot( [(xb[ind]**2 + xpb[ind]**2 + xo[ind]**2 + xpo[ind]**2 + 
              xg[ind]**2 + xpg[ind]**2)/3 for ind in range(nturns) ], color='black' )
    