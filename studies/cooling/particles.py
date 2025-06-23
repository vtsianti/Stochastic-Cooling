# Routine to do do the exchange of .. ended up by regrouping from scratch 
import numpy as np

def PartsExchange( ptsEarly, ptsLate,Th ):
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



