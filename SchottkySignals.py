#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Test scheme with macroparticle distribution divided into two groups 
(red and blue ones)
 => First try to generate time traces, which later can be used to determine 
    kicks due to the stochastic cooling system.
 => No electronic noise so far!! To be discussed how to add it.

"""

import numpy as np
import math
import matplotlib.pyplot as plt
import time

datin  = time.time()  # record start time - to estimate run duration at end

#Nparts, Nturns =  1000, 5000
Nparts, Nturns =  5000,   100

betPU, alfPU       =  1.3, -0.9
betK, alfK         =  0.8,  0.6
gamPU, gamK        =  (1 + alfPU**2)/betPU, (1 + alfK**2)/betK
muPUK, muKPU       =  1.51, 2*np.pi*1.34 - 1.51
etaPUK, etaKPU     =  0.000, 0.500
sigdelt            = .001            # rms momentum spread in unit
Th, Trev           =  .1e-6, 5.0e-6, # half width of simulation window and revolution period in s
Tovlap, NSamp, add = 4*sigdelt*(etaPUK + etaKPU)*Trev, 2000, '2000'
gain               =  .002

# definition of the transverse "response function", which is given by the 
#    routine resp for the interval -wlH < Dt < wrH and 0 outside
wlH, wrH = -1.6e-9, 1.6e-9
def respH( Dt ):
    if Dt < 1.*wlH or Dt > 1.*wrH:
        print( f' ===> function respH called with Dt ={1e6*Dt:8.4f}' )
    return (1 - 27e18*Dt**2)*(1 - 3.e18*Dt**2)*(1 - 1.15e18*Dt**2)*(1 - (.625e9*Dt)**2)**7
#   return (1 - 23e16*Dt**2)*(1 - 3.e16*Dt**2)*(1 - 1.15e16*Dt**2)*(1 - (.625e8*Dt)**2)**7
#   return (1 - 25e-12*Dt^2)*(1 - 3e-12*Dt^2)*(1 - 1.15e-12*Dt^2)*(1 - (Dt/1.5)^2)^6

wlL, wrL = -1.6e-9, 1.6e-9
def respL( Dt ):
    if Dt < 1.*wlL or Dt > 1.*wrL:
        print( f' ===> function respL called with Dt ={1e6*Dt:8.4f}' )
    return (63e9*Dt)*(1 - 6.5e18*Dt**2)*(1 - 1.55e18*Dt**2)*(1 - (.625e9*Dt)**2)**8

#rng = np.random.default_rng(18022005)
rng = np.random.default_rng(22072002 + 3)

# Total width (particles of both colors) of beam time window is 2*Th ('h' for half)
#  for sampling each sub-window (red or blue) divided into NSamp intervals. This
#  means samp,ing rate DTsamp and NSamp + 1 points. On both ends to be added 
#  ceiling( Tovlap/DTSamp ) points   
DTSamp   = Th/NSamp
NSampext = math.ceil( Tovlap/DTSamp )

print('========>', NSamp, NSampext, DTSamp, Th, (wrH - wlH)/DTSamp)

# Routine to do do the exchange of .. ended up by regrouping from scratch
def PartsExchange( ptsEarly, ptsLate ):
    ptsEarlyNew, ptsLateNew = [], []
    for x, xp, delt, Tau in ptsEarly:
        if Tau < Th/2:  # should remain in "early group
            ptsEarlyNew += [ [x, xp, delt, Tau] ]
        else:
            ptsLateNew += [ [x, xp, delt, Tau - Th] ]
    for x, xp, delt, Tau in ptsLate:
        if Tau > -Th/2:
            ptsLateNew += [ [x, xp, delt, Tau] ]
        else:
            ptsEarlyNew += [ [x, xp, delt, Tau + Th] ]
    return ptsEarlyNew, ptsLateNew

# Routine to generate time traces
def TimeTraces( ptsEarly, ptsMain, ptsLate ):
    TraceH = [ 0. for _ in range(NSamp + 1 + 2*NSampext) ]
    TraceL = [ 0. for _ in range(NSamp + 1 + 2*NSampext) ]
#   first generate transverse trace
    for x, xp, delt, Tau in ptsEarly:
        for ind in range( max(-NSampext, math.ceil((wlH+Tau-Th)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrH+Tau-Th)/DTSamp)) ):
            TraceH[ind] += x*respH(ind*DTSamp - (Tau-Th) )
    for x, xp, delt, Tau in ptsMain:
        for ind in range( max(-NSampext, math.ceil((wlH+Tau)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrH+Tau)/DTSamp)) ):
            TraceH[ind] += x*respH(ind*DTSamp - Tau )
    for x, xp, delt, Tau in ptsLate:
        for ind in range( max(-NSampext, math.ceil((wlH+Tau+Th)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrH+Tau+Th)/DTSamp)) ):
            TraceH[ind] += x*respH(ind*DTSamp - (Tau+Th) )
#   then some time generate longitudinal trace
    for x, xp, delt, Tau in ptsEarly:
        for ind in range( max(-NSampext, math.ceil((wlL+Tau-Th)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrL+Tau-Th)/DTSamp)) ):
            TraceL[ind] += respL(ind*DTSamp - (Tau-Th) )
    for x, xp, delt, Tau in ptsMain:
        for ind in range( max(-NSampext, math.ceil((wlL+Tau)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrL+Tau)/DTSamp)) ):
            TraceL[ind] += respL(ind*DTSamp - Tau )
    for x, xp, delt, Tau in ptsLate:
        for ind in range( max(-NSampext, math.ceil((wlL+Tau+Th)/DTSamp)), 
                          min(NSamp+1+NSampext, math.ceil((wrL+Tau+Th)/DTSamp)) ):
            TraceL[ind] += respL(ind*DTSamp - (Tau+Th) )
    return TraceH, TraceL

# Computation of transverse transfer matrix elements
projPU11 =  betPU**(1/2)
projPU21 = -alfPU/betPU**(1/2)
projPU22 =  1/betPU**(1/2)

matPUK11 = ((betK/betPU)**(1/2))*(np.cos(muPUK) + alfPU*np.sin(muPUK))
matPUK12 = ((betPU*betK)**(1/2))*np.sin(muPUK)
matPUK21 = ((alfPU-alfK)*np.cos(muPUK) - (1+alfPU*alfK)*np.sin(muPUK))/((betPU*betK)**(1/2))
matPUK22 = ((betPU/betK)**(1/2))*(np.cos(muPUK) - alfK*np.sin(muPUK))

matKPU11 = ((betPU/betK)**(1/2))*(np.cos(muKPU) + alfK*np.sin(muKPU))
matKPU12 = ((betPU*betK)**(1/2))*np.sin(muKPU)
matKPU21 = ((alfK-alfPU)*np.cos(muKPU) - (1+alfPU*alfK)*np.sin(muKPU))/((betPU*betK)**(1/2))
matKPU22 = ((betK/betPU)**(1/2))*(np.cos(muKPU) - alfPU*np.sin(muKPU))

# Generate macroparticles in two groups with red ones and blue ones
#    .. say we start with red particles the early ones
ptsRed  = []
ptsBlue = []
for _ in range(Nparts):
    Tau = rng.uniform(-Th, Th)
    xn, xpn, deltn = rng.normal(0., 1.), rng.normal(0., 1.), rng.normal(0., 1.)
    if Tau < 0:
        ptsRed += [ [projPU11*xn, projPU21*xn + projPU22*xpn, 
                     deltn*sigdelt, Tau + Th/2] ]
    else:
        ptsBlue += [ [projPU11*xn, projPU21*xn + projPU22*xpn, 
                      deltn*sigdelt, Tau - Th/2] ]
        
# Track red (now early) particles ones once around
ptsRedprev = ptsRed
ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
            Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]  # no action at kicker
ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
            Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed]

# Prepare for tracking of blue particles and track them once around
ptsBlue, ptsRed = PartsExchange( ptsBlue, ptsRed )
ptsBlueprev = ptsBlue
TrHBlue, TrLBlue = TimeTraces( ptsRedprev, ptsBlue, ptsRed )
ptsBlue = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
            Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsBlue ]  # no action at kicker
ptsBlue = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
            Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsBlue]

# Prepare for 2nd tracking of red particles and track them once around
ptsRed, ptsBlue = PartsExchange( ptsRed, ptsBlue )
ptsRedprev = ptsRed
TrHRed, TrLRed = TimeTraces( ptsBlueprev, ptsRed, ptsBlue )
ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
            Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]  # no action at kicker
ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
            Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed]

# Now the blue ones are early - now just enter loop over number of turns
#   later - for longitudinal filter cooling - some more tracking will be needed

fHBlue = open('TrHBlue' + add + '.dat', 'w', encoding="utf-8")
fHBlue.write( f'{NSamp:6d} {NSampext:5d} {DTSamp:12.4e}\n' )
fLBlue = open('TrLBlue' + add + '.dat', 'w', encoding="utf-8")
fLBlue.write( f'{NSamp:6d} {NSampext:5d} {DTSamp:12.4e}\n' )
fHRed  = open('TrHRed' + add + '.dat',  'w', encoding="utf-8")
fHRed.write( f'{NSamp:6d} {NSampext:5d} {DTSamp:12.4e}\n' )
fLRed  = open('TrLRed' + add + '.dat',  'w', encoding="utf-8")
fLRed.write( f'{NSamp:6d} {NSampext:5d} {DTSamp:12.4e}\n' )

# Now we can go in loop and even implement transverse cooling or longitudinal time delay cooling (but not filter)
for turn in range(Nturns):
    print(f' turn {turn:5d} after {(time.time() - datin):8.2f} s <===')
#   Get ready for the blue particles to be tracked and track them to kicker
    ptsBlue, ptsRed = PartsExchange( ptsBlue, ptsRed )
    ptsBlueprev, TrLBlueprev = ptsBlue, TrLBlue  # Keep longitudinal trace to add filter cooling later
    TrHBlue, TrLBlue = TimeTraces( ptsRedprev, ptsBlue, ptsRed )
    #print(len(TrHBlue))
    ptsBlue = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
                 Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsBlue ]
#   One day cooling to be applied -  now just dump time traces instead
    for item in TrHBlue:
        fHBlue.write( f' {item:7.4e} ')
    fHBlue.write( '\n' )
    for item in TrLBlue:
        fLBlue.write( f' {item:7.4e} ')
    fLBlue.write( '\n' )
#   track the blue one further to the PU
    ptsBlue = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
                 Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsBlue ]
#   Get ready for the red particles to be tracked and track them to kicker
    ptsRed, ptsBlue = PartsExchange( ptsRed, ptsBlue )
    ptsRedprev, TrLRedprev = ptsRed, TrLRed  # Keep longitudinal trace to add filter cooling later
    TrHRed, TrLRed = TimeTraces( ptsBlueprev, ptsRed, ptsBlue )
    ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
                Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]
#   One day cooling(s) to be applied - now just dump time traces instead
    for item in TrHRed:
        fHRed.write( f' {item:7.4e} ' )
    fHRed.write( '\n' )
    for item in TrLRed:
        fLRed.write( f' {item:7.4e} ' )
    fLRed.write( '\n' )
#   track the red ones further to the PU, where they will be the late ones
    ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
                Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed ] 

fHBlue.close()
fLBlue.close()
fHRed.close()
fLRed.close()

print(f'\n\n =======> duration of run{(time.time() - datin):8.2f} s <===\n')
