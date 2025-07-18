# constants for high energy scenario

# cntrl F -> PROB TODO 

import xtrack as xt

env = xt.get_environment()


#define beam

# MADX: Beam, particle=ANTIPROTON, pc:=beam_p_GeV_c,ex=5.0E-6,ey=5.0E-6, sige=1E-3, NPART=3e7;

env['mass_p'] = xt.PROTON_MASS_EV * 10**(-9)
env['q_ap'] = -1

#case 1
env['beam_p_GeV_c'] = 3.575
env['beam_beta'] = 0.9672
env['beam_gamma'] = 3.9368

'''
#case 2
env['beam_p_GeV_c'] = 2.0
env['beam_beta'] = 0.9057
env['beam_gamma'] = 2.3589
'''

#env.particle_ref = xt.Particles(mass0=env['mass_p'], p0c=env['beam_p_GeV_c'], beta0 = env['beam_beta'], gamma0=env['beam_gamma'])
env.particle_ref = xt.Particles(mass0=env['mass_p'], q0=env['q_ap'], p0c=env['beam_p_GeV_c'])#, beta0=env['beam_beta'], gamma0=env['beam_gamma'])


line = env['AD']
env['momentum'] = 'beam_p_GeV_c' #line.particle_ref.p0c[0]

#### Quadrupoles
env['deltak_qmain1'] = 0.
env['deltak_qmain2'] = 0.
env['deltak_qtrim1'] = 0.
env['deltak_qtrim2'] = 0.
env['deltak_qtrim3'] = 0.
env['deltak_qtrim4'] = 0.
env['deltak_qtrim5'] = 0.

env['kqfns'] = '0.558153759866 + deltak_qmain1'                     
env['kqds'] =  '-(kqfns + deltak_qmain1)'                           
env['kqfnecool'] = '0.594999986705 +deltak_qmain1+deltak_qtrim4'          
env['kqdnecool'] = '-(0.36175160802 + deltak_qmain2)'               
env['kqfn'] = '0.5138363513 + deltak_qmain1'                        
env['kqdn'] = '-(0.4632118053 + deltak_qmain1)'                                
env['kqdc53'] = '-(0.4632118053 + deltak_qmain1)'                   
env['kqfc54'] = '0.5138363513 + deltak_qmain1 + deltak_qtrim5'                     
env['kqfw6'] = '0.434013207981 + deltak_qmain1 + deltak_qtrim1'           
env['kqfw8'] = '0.560993621836 + deltak_qmain1 + deltak_qtrim3'       
env['kqdw7'] = '-(0.526485397793 + deltak_qmain1 + deltak_qtrim2)'         
env['kqdw9'] = '-(0.4130277946   + deltak_qmain1 + deltak_qtrim2)'     

# to enable/disable kick from "bad" optics
env['enable_qkick'] = 0.
env['enable_dkick'] = 0.
env['enable_q_sext'] = 0.

env['relativegradient_sextupolarwindings'] = 1.36
env['relativegradient_qfw6'] = 1.43
env['relativegradient_qfw7'] = 'relativegradient_qfw6'
env['relativegradient_qfw8'] = 0.60
env['relativegradient_qfw9'] = 'relativegradient_qfw6'

env['ksd.qd1'] =  'kqfns*relativegradient_sextupolarwindings*enable_q_sext'  
env['ksd.qd3'] =  'kqds*relativegradient_sextupolarwindings*enable_q_sext'   
env['ksd.qdnec'] = 0.
env['ksf.qfw6'] = 'kqfw6*relativegradient_qfw6*enable_q_sext' 
env['ksf.qdw7'] = 'kqdw7*relativegradient_qfw7*enable_q_sext'  
env['ksf.qfw8'] = 'kqfw8*relativegradient_qfw8*enable_q_sext'  
env['ksf.qdw9'] = 'kqdw9*relativegradient_qfw9*enable_q_sext'  

#### Skew quadrupoles
env['ksk1404'] = 0.
env['ksk4308'] = '-ksk1404'

#### EC Solenoids
# PROB they are defined again in main code - what will be the output?
env['kecsol'] = 0.
env['kscomp26'] = 0.
env['kscomp31'] = 'kscomp26'

#### Rotale sextupoles:
# PROB they are defined again in main code - what will be the output?
env['kxrc16.41'] = 0.

# Eddy currents in main dipoles
# PROB not used because of bend def
env['bh_k2eddy'] = 0.

### Voltage of bunch rotation cavities & deceleration cavity
env['cbr.v'] =  0. 

# --- in main code they were not defined
# --- i define them here because on_ecsol = 0 by default

#### turn EC Solenoids on/off
env['on_ecsol'] = 0.

#### EC Solenoid Current:
env['dr.sec2910_i'] = 360.

#### Compensation Solenoids Currents:
env['dr.scomp2607_i'] = 221.256
env['dr.scomp3106_i'] = 221.256

#values for kicks
env['k.bhztrim'] = 0.
env['k.bhztr05.06'] = 0.
env['k.bhztr08.09'] = 0.
env['k.bhztr11.12'] = 0.
env['k.bhztr17.18'] = 0.
env['k.bhztr20.21'] = 0.
env['k.bhztr23.24'] = 0.
env['k.bhztr33.34'] = 0.
env['k.bhztr36.37'] = 0.
env['k.bhztr39.40'] = 0.
env['k.bhztr45.46'] = 0.
env['k.bhztr48.49'] = 0.
env['k.bhztr51.52'] = 0.

env['th.tkick'] = 0.


#were not defined in originals 
# set them here to 0
# kicker values

env['dr.sec2910_i']=   0.
env['dr.dhx2908_i']=   0.
env['dr.dhz2913_i']=   0.
env['dr.dvt2608_i']=   0.
env['dr.dvt3105_i']=   0.
env['dr.dhv2904_hi'] = 0.
env['dr.dhv2904_vi'] = 0.
env['dr.dhv2917_hi'] = 0.
env['dr.dhv2917_vi'] = 0.
env['ipm_on'] = 0.
env['on_eckick'] = 0.

