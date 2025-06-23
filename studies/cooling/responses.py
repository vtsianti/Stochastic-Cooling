def respH( Dt ):
   # if Dt < 1.*wlH or Dt > 1.*wrH:
    #    print( f' ===> function respH called with Dt ={1e6*Dt:8.4f}' )
      return (1 - 27e18*Dt**2)*(1 - 3.e18*Dt**2)*(1 - 1.15e18*Dt**2)*(1 - (.625e9*Dt)**2)**7
#   return (1 - 23e16*Dt**2)*(1 - 3.e16*Dt**2)*(1 - 1.15e16*Dt**2)*(1 - (.625e8*Dt)**2)**7
#   return (1 - 25e-12*Dt^2)*(1 - 3e-12*Dt^2)*(1 - 1.15e-12*Dt^2)*(1 - (Dt/1.5)^2)^6


def respL( Dt ):
   # if Dt < 1.*wlL or Dt > 1.*wrL:
    #    print( f' ===> function respL called with Dt ={1e6*Dt:8.4f}' )
      return  (63e9*Dt)*(1 - 6.5e18*Dt**2)*(1 - 1.55e18*Dt**2)*(1 - (.625e9*Dt)**2)**8
