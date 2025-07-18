import numpy as np
import math
import matplotlib.pyplot as plt
import time
import scipy as sp
import seaborn as sns
import pandas as pd

from particles import PartsExchange
from cooling import TimeTraces,kickH, kickL
from responses import respH,respL 



def Cooling(Nparts,Nturns,gain, gainL, sigdelt,NSamp, over_sample_factor, random_seed ):


    betPU, alfPU       =  1.3, -0.9
    betK, alfK         =  0.8,  0.6
    gamPU, gamK        =  (1 + alfPU**2)/betPU, (1 + alfK**2)/betK
    muPUK, muKPU       =  1.51, 2*np.pi*1.34 - 1.51
    total_angle        =  2*np.pi*1.34
    etaPUK, etaKPU     =  -0.01, -0.01     #eta PUK must be reletevely small, so they dont change slices so fast... 0.02 breaks the system ... It is the limit case!!!! very sensitive on etaPUK --> 2 much unwanted mixing, also etaKPU cant go very low(limit case 0.3) because then the mixing is bad
          # rms momentum spread in unit
    Th, Trev           =  .1e-6, 5.0e-6, # half width of simulation window and revolution period in s

    wlL, wrL = -1.6e-9, 1.6e-9
    wlH, wrH = -1.6e-9, 1.6e-9
    Tovlap,  add = 4*sigdelt*abs(etaPUK + etaKPU)*Trev,  '2000'
    #gain               =  0.00018  #as long as I reduce the eta, i have to reduce gains as well... see book
    #gainL              =  3e-8
 
    DTSamp   = Th/NSamp
    NSampext = math.ceil( Tovlap/DTSamp )
    inds = np.arange( (-NSampext)*over_sample_factor , (NSamp+1+NSampext + 1)*over_sample_factor )
    t_bins = inds*DTSamp/over_sample_factor -Th/2
 

    respH_new_once = respH(np.arange(wlH, wrH, DTSamp/over_sample_factor ))
    respL_new_once = respL(np.arange(wlL, wrL, DTSamp/over_sample_factor ))

    rng = np.random.default_rng(random_seed )
    
# Routine to generate time traces

   

   

    
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


    emittance=np.zeros(Nturns+2)
    geo_emittance=np.zeros(Nturns+2)
    rms_momentum_spread=np.zeros(Nturns+2)
    beam=[]
    xp_beam=[]
    x_beam=[]
    beam=ptsRed+ptsBlue
    beam = np.array(beam)
    x_beam=beam[:,0]
    xp_beam=beam[:,1]
    x_initial=x_beam
    xp_initial=xp_beam
    tau_initial=beam[:,3]
    delt_initial=beam[:,2]
    counts_initial, bins_initial = np.histogram(delt_initial, bins=30)
    emittance[0]=np.sqrt(np.mean(x_initial**2)*np.mean(xp_initial**2)-np.mean(x_initial*xp_initial)**2)   
    geo_emittance[0]=((gamPU*np.mean(x_initial**2)+2*alfPU*np.mean(x_initial*xp_initial)+betPU*np.mean(xp_initial**2)))/2
#emittance_individual_particles[0][:]=(gamPU*x_beam[:10]**2+2*alfPU*(x_beam[:10]*xp_beam[:10])+betPU*(xp_beam[:10]**2))/2
    rms_momentum_spread[0]=np.sqrt(np.mean(delt_initial**2)-np.mean(delt_initial)**2)



    ptsRedprev = ptsRed
    ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
               Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]  # no action at kicker
    ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
               Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed]

# Prepare for tracking of blue particles and track them once around
    ptsBlue, ptsRed = PartsExchange( ptsBlue, ptsRed,Th )
    ptsBlueprev = ptsBlue
    time2,TrHBlue, TrLBlue = TimeTraces( ptsRedprev, ptsBlue, ptsRed,t_bins,Th,respH_new_once,respL_new_once )

    ptsBlue = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
            Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsBlue ]  # no action at kicker
#ptsBlue=kickH(ptsBlue,cs)
    ptsBlue = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
            Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsBlue]
    TrHBlue_prev, TrLBlue_prev = TrHBlue, TrLBlue
# Prepare for 2nd tracking of red particles and track them once around
    ptsRed, ptsBlue = PartsExchange( ptsRed, ptsBlue,Th )
    ptsRedprev = ptsRed
    time2,TrHRed, TrLRed = TimeTraces( ptsBlueprev, ptsRed, ptsBlue,t_bins,Th,respH_new_once,respL_new_once )
#cs = sp.interpolate.CubicSpline( DTSamp*np.arange(-NSampext, NSamp + 1 + NSampext)-Th/2, 
 #                 TrHRed[-NSampext:] + TrHRed[:NSamp + 1 + NSampext] )
    ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
            Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]  # no action at kicker
#ptsRed=kickH(ptsRed,cs)
    ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
            Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed]
    TrHRed_prev, TrLRed_prev = TrHRed, TrLRed
# Now the blue ones are early - now just enter loop over number of turns
#   later - for longitudinal filter cooling - some more tracking will be needed

    beam=[]
    xp_beam=[]
    x_beam=[]
    beam=ptsRed+ptsBlue
    beam = np.array(beam)
    x_beam=beam[:,0]
    xp_beam=beam[:,1]
    dtl_beam=beam[:,2]
    emittance[1]=np.sqrt(np.mean(x_beam**2)*np.mean(xp_beam**2)-np.mean(x_beam*xp_beam)**2) 
#emittance_individual_particles[1][:]=(gamPU*x_beam[:10]**2+2*alfPU*(x_beam[:10]*xp_beam[:10])+betPU*(xp_beam[:10]**2))/2
    rms_momentum_spread[1]=np.sqrt(np.mean(dtl_beam**2)-np.mean(dtl_beam)**2)

# Now we can go in loop and even implement transverse cooling or longitudinal time delay cooling (but not filter)
    for turn in range(Nturns):
    #print(f' turn {turn:5d} after {(time.time() - datin):8.2f} s <===')
#   Get ready for the blue particles to be tracked and track them to kicker
     ptsBlue, ptsRed = PartsExchange( ptsBlue, ptsRed,Th )
     ptsBlueprev, TrLBlueprev = ptsBlue, TrLBlue  # Keep longitudinal trace to add filter cooling later
     time2,TrHBlue, TrLBlue = TimeTraces( ptsRedprev, ptsBlue, ptsRed,t_bins,Th ,respH_new_once,respL_new_once)
     TrLDiffBlue = [h - l for h, l in zip(TrLBlue_prev, TrLBlue)]
     cs = sp.interpolate.CubicSpline( time2, 
                  TrHBlue )
     csL=sp.interpolate.CubicSpline( time2, 
                  np.array(TrLDiffBlue) )
    #cs = sp.interpolate.interp1d( DTSamp*np.arange(-NSampext, NSamp + 1 + NSampext)-Th/2, 
     #             TrHBlue[-NSampext:] + TrHBlue[:NSamp + 1 + NSampext] )
    #csL=sp.interpolate.interp1d( DTSamp*np.arange(-NSampext, NSamp + 1 + NSampext)-Th/2, 
     #             TrLBlue[-NSampext:] + TrLBlue[:NSamp + 1 + NSampext] )

    #print(len(TrHBlue))
     ptsBlue = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
                 Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsBlue ]
#   One day cooling to be applied -  now just dump time traces instead
     ptsBlue=kickH(ptsBlue,cs,gain)
     ptsBlue=kickL(ptsBlue,csL,gainL)
#   track the blue one further to the PU
     ptsBlue = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
                 Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsBlue ]
     TrHBlue_prev, TrLBlue_prev = TrHBlue, TrLBlue
#   Get ready for the red particles to be tracked and track them to kicker
     ptsRed, ptsBlue = PartsExchange( ptsRed, ptsBlue,Th )
     ptsRedprev, TrLRedprev = ptsRed, TrLRed  # Keep longitudinal trace to add filter cooling later
     time2,TrHRed, TrLRed = TimeTraces( ptsBlueprev, ptsRed, ptsBlue,t_bins,Th ,respH_new_once,respL_new_once)
     TrLDiffRed = [h - l for h, l in zip(TrLRed_prev, TrLRed)]
     cs = sp.interpolate.CubicSpline( time2, 
                  TrHRed )
     csL=sp.interpolate.CubicSpline( time2, 
                  np.array(TrLDiffRed) )
    
     y_cs = cs(time2)
     y_csL = csL(time2)
    #print("Spline Knots:", cs.x)  # Knots where the spline pieces join
    #print("Spline Coefficients:", cs.c)  # Coefficients of the spline pieces
   
     tauPU=[]
     xPU=[]
     beam=ptsRed
     beam = np.array(beam)
     tauPU=beam[:,3]
     xPU=beam[:,0]
    
    
# Plot the spline
     '''
     if turn==Nturns-1:
      plt.figure(figsize=(8, 5))
      plt.plot(time2, y_cs, label="TrHRed Interpolated", linestyle="-")
     #plt.plot(t_smooth, y_csL, label="TrLDiffRed Interpolated", linestyle="--")
      plt.scatter(time2, TrHRed, marker="o", color="blue", label="horizontal signal")
      plt.scatter(tauPU, xPU, zorder=5, color="red", label="position of particles")
     '''
     
     ptsRed = [ [matPUK11*x + matPUK12*xp, matPUK21*x + matPUK22*xp, delt, 
                Tau + etaPUK*delt*Trev] for x, xp, delt, Tau in ptsRed ]
#   One day cooling(s) to be applied - now just dump time traces instead
     ptsRed=kickH(ptsRed,cs,gain)
     ptsRed=kickL(ptsRed,csL, gainL)   #time of flight method longitudinal cooling
#   track the red ones further to the PU, where they will be the late ones
     ptsRed = [ [matKPU11*x + matKPU12*xp, matKPU21*x + matKPU22*xp, delt, 
                Tau + etaKPU*delt*Trev] for x, xp, delt, Tau in ptsRed ] 
     TrHRed_prev, TrLRed_prev = TrHRed, TrLRed
     beam=[]
     xp_beam=[]
     x_beam=[]
     delta_beam=[]
     dlt_final=[]
     tau_final=[]
     beam=ptsRed+ptsBlue
     beam = np.array(beam)
     x_beam=beam[:,0]
     xp_beam=beam[:,1]
     delta_beam=beam[:,2]
     tau_final=beam[:,3]
     dlt_final=beam[:,2]
     counts_final, bins_final = np.histogram(dlt_final, bins=30)
     emittance[turn+2]=np.sqrt(np.mean(x_beam**2)*np.mean(xp_beam**2)-np.mean(x_beam*xp_beam)**2)
     geo_emittance[turn+2]=(gamPU*np.mean(x_beam**2)+2*alfPU*np.mean(x_beam*xp_beam)+betPU*np.mean(xp_beam**2))/2
     rms_momentum_spread[turn+2]=np.sqrt(np.mean(delta_beam**2)-np.mean(delta_beam)**2)
    #emittance_individual_particles[turn+2][:]=(gamPU*x_beam[:10]**2+2*alfPU*(x_beam[:10]*xp_beam[:10])+betPU*(xp_beam[:10]**2))/2

    print(f'The initial emittance is {emittance[0]}{chr(0x03C0)} mm*mrad')
    print(f'The final emittance after cooling is {emittance[-1]}{chr(0x03C0)} mm*mrad')
    print(f'Is emittance reduced? -->  {emittance[-1] < emittance[0]}')
    if emittance[-1] < emittance[0]:
      print(f"Emittance is reduced by {(emittance[0] - emittance[-1]) * 100 / emittance[0]}%")
    print(f'The initial rms_momentum_spread is {rms_momentum_spread[0]} ')
    print(f'The final rms_momentum_spread after cooling is {rms_momentum_spread[-1]} ')
    print(f'Is rms_momentum_spread reduced? -->  {rms_momentum_spread[-1] < rms_momentum_spread[0]}')
    if rms_momentum_spread[-1] < rms_momentum_spread[0]:
      print(f"rms_momentum_spread is reduced by {(rms_momentum_spread[0] - rms_momentum_spread[-1]) * 100 / rms_momentum_spread[0]}%")

    return emittance[-1], rms_momentum_spread[-1]

