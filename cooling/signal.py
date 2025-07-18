import numpy as np
from utils import running_average
from responses import respH, respL
from config import *

def TimeTraces(ptsEarly, ptsMain, ptsLate, bins,Th,respH_new_once, respL_new_once):
     """
    Generate time traces without applying the `Th / 2` offset internally.
     """
    
     ptsEarly = np.array(ptsEarly)
     ptsMain = np.array(ptsMain)
     ptsLate = np.array(ptsLate)
     # Compute histograms of beam distribution
     bin_centers_early, averages_early, count_early, sum_early = running_average(
        ptsEarly[:, 3]-Th, ptsEarly[:, 0], bins
      )
     bin_centers_main, averages_main, count_main, sum_main = running_average(
        ptsMain[:, 3], ptsMain[:, 0], bins
      )
     bin_centers_late, averages_late, count_late, sum_late = running_average(
        ptsLate[:, 3]+Th, ptsLate[:, 0], bins
      )

    # Compute time traces
     TraceH_early = np.convolve(respH_new_once, sum_early, 'same')
     TraceH_main = np.convolve(respH_new_once, sum_main, 'same')
     TraceH_late = np.convolve(respH_new_once, sum_late, 'same')
    
     TraceL_early = np.convolve(respL_new_once, count_early, 'same')
     TraceL_main = np.convolve(respL_new_once, count_main, 'same')
     TraceL_late = np.convolve(respL_new_once, count_late, 'same')

     TraceH = TraceH_early + TraceH_main + TraceH_late
     TraceL = TraceL_early + TraceL_main + TraceL_late #i am multiplying with this factor in order to amplify the signal!!!!!
    
    
    
     return bin_centers_main, TraceH, TraceL

def kickH(pts, signalH,gain):
      corrected_pts = []
      for x, xp, delt, Tau in pts:
        # Interpolate signalH at the particle's Tau
        signal_value = signalH(Tau)
        # Correct xp using the signal value (define your correction logic)
        corrected_xp = xp +gain * signal_value  # I add the signal!!!!!
        # Append the updated particle to the new list
        corrected_pts.append([x, corrected_xp, delt, Tau])
      return corrected_pts

def kickL(pts, signalL,gainL):
     corrected_pts = []
     for x, xp, delt, Tau in pts:
        # Interpolate signalL at the particle's Tau
        signal_value = signalL(Tau)
        # Correct xp using the signal value (define your correction logic)
        corrected_delt = delt + gainL * signal_value  # Example: subtracting scaled signal
        # Append the upd1.0pend([x, xp, corrected_delt, Tau])
        corrected_pts.append([x, xp, corrected_delt, Tau])
     return corrected_pts