# full basic sequence: quadrupoles, bends, sextupololar windings, some drifts & markers 

# cntrl F -> PROB TODO 

import xtrack as xt
import numpy as np

env = xt.get_environment()

env.vars.default_to_zero = True

#general element types - name conventions
# connecting: xsuite native - database official name - used name

env.new('sbend', 'Bend')
env.new('quadrupole', 'Quadrupole')
env.new('qsk', 'quadrupole') #skew 
env.new('quadrupole_sw', 'quadrupole') # Quadrupoles with sextupolar windings
env.new('tkick', 'Multipole',knl=[-0.], ksl=[0.])
env.new('rfcavity', 'Cavity')
env.new('sextupole', 'Sextupole')
env.new('solenoid', 'Solenoid')
env.new('drift', 'Drift')
env.new('marker', xt.Marker)
env.new('instrument', 'drift') 
env.new('vvs', 'drift') 

########################################



#### Bending magnets 

#parameters
env['phi'] = .2457993878
env['phi2'] = 'phi/2'

#### bending magnets
#full gap of BHN, BHW, BHS
env['fgap_bhn'] = 0.114
env['fgap_bhw'] = 0.114
env['fgap_bhs'] = 0.116

#fringe gield integral
env['ffi'] = 0.5
#length
env['l_bhn'] = 1.9513
env['l_bhw'] = 1.9513
env['l_bhs'] = 1.9513

# k0_from_h: assigns value through angle

#BHN
# DBname: PXMBHHGWWP
env.new('bhn', 'sbend', length='l_bhn', angle='phi', k0_from_h=True,
         edge_entry_angle='phi2', edge_exit_angle ='phi2',
         edge_entry_fint = 'ffi', edge_exit_fint = 'ffi',
         edge_entry_hgap='fgap_bhn/2', edge_exit_hgap = 'fgap_bhn/2') 

#BHW
# DBname: PXMBHHFHWP
env.new('bhw', 'sbend', length='l_bhw', angle='phi', k0_from_h=True,
         edge_entry_angle='phi2', edge_exit_angle ='phi2',
         edge_entry_fint = 'ffi', edge_exit_fint = 'ffi',
         edge_entry_hgap='fgap_bhw/2', edge_exit_hgap = 'fgap_bhw/2') 

#BHS
# DBname: PXMBHHHWWP
env.new('bhs', 'sbend', length='l_bhs', angle='phi', k0_from_h=True,
         edge_entry_angle='phi2', edge_exit_angle ='phi2',
         edge_entry_fint = 'ffi', edge_exit_fint = 'ffi',
         edge_entry_hgap='fgap_bhs/2', edge_exit_hgap = 'fgap_bhs/2') 


#define all names - can skip: parents defined also when installed
env.new('dr.bhn05','bhn')
env.new('dr.bhn06','bhn')
env.new('dr.bhw08','bhw')
env.new('dr.bhw09','bhw')
env.new('dr.bhn11','bhn')
env.new('dr.bhn12','bhn')
env.new('dr.bhn17','bhn')
env.new('dr.bhn18','bhn')
env.new('dr.bhw20','bhw')
env.new('dr.bhw21','bhw')
env.new('dr.bhn23','bhn')
env.new('dr.bhn24','bhn')
env.new('dr.bhn33','bhn')
env.new('dr.bhn34','bhn')
env.new('dr.bhw36','bhw')
env.new('dr.bhw37','bhw')
env.new('dr.bhn39','bhn')
env.new('dr.bhn40','bhn')
env.new('dr.bhn45','bhn')
env.new('dr.bhn46','bhn')
env.new('dr.bhw48','bhw')
env.new('dr.bhw49','bhw')
env.new('dr.bhn51','bhn')
env.new('dr.bhs52','bhs')


#### More Sbends: work as Quadrupoles

#QFN
# DBname: PXMQNENNWP
env['phi_qfn'] = 0.030
env['l_qfn'] = 0.7321
#env['BendingQFN'] =  'kQFN * 0.0816* l_QFN*enable_qkick'

env.new('qfn', 'sbend', length='l_qfn', angle='phi_qfn', k1 = 'kqfn', k0_from_h=True,
        edge_entry_angle='phi_qfn/2', edge_exit_angle ='phi_qfn/2')

#QDN
# DBname: PXMQNEONWP
env['phi_qdn'] = 0.018
env['l_qdn'] = 0.7396
#env['BendingQDN'] = '-kQDN*0.0496*l_QDN*enable_qkick' 

env.new('qdn', 'sbend', length='l_qdn', angle='phi_qdn', k1 = 'kqdn', k0_from_h=True,
        edge_entry_angle='phi_qdn/2', edge_exit_angle ='phi_qdn/2')

#QDC
# DBname: PXMQNERNWP
env['phi_qdc'] = 0.018
env['l_qdc'] = 0.7396
#env['BendingQDC'] = '-kQDC53*0.0496*l_QDC*enable_qkick' 

env.new('qdc', 'sbend', length='l_qdc', angle='phi_qdc', k1 = 'kqdc53', k0_from_h=True,
        edge_entry_angle='phi_qdc/2', edge_exit_angle ='phi_qdc/2')

#QFC
# DBname: PXMQNEPCWP
env['phi_qfc'] = 0.030
env['l_qfc'] = 0.7321
#env['BendingQFC'] = 'kQFC54*0.0816*l_QFC*enable_qkick' 

env.new('qfc', 'sbend', length='l_qfc', angle='phi_qfc', k1 = 'kqfc54', k0_from_h=True,
        edge_entry_angle='phi_qfc/2', edge_exit_angle ='phi_qfc/2')

#define names 
env.new('dr.qfn04','qfn')
env.new('dr.qdn05','qdn')
env.new('dr.qdn13','qdn')
env.new('dr.qfn14','qfn')
env.new('dr.qfn16','qfn')
env.new('dr.qdn17','qdn')
env.new('dr.qdn25','qdn')
env.new('dr.qfn26','qfn')
env.new('dr.qfn32','qfn')
env.new('dr.qdn33','qdn')
env.new('dr.qdn41','qdn')
env.new('dr.qfn42','qfn')
env.new('dr.qfn44','qfn')
env.new('dr.qdn45','qdn')
env.new('dr.qdc53','qdc')
env.new('dr.qfc54','qfc')


#### Quadrupoles

#define main qupole types with parameters and sextupolar k constants (=windings)
#QDS
# DBname: PXMM4EANWP
env['l_qds'] = 0.7106
#env.new('qds','quadrupole', length='l_qds', k1 = 'kqds')
env.new('qds','quadrupole_sw', length='l_qds', k1 = 'kqds', knl=[0,0, 'ksd.qd3*l_qds'])

#env.new('qds.h','quadrupole', length='l_qds/2', k1= 'kqds') #half for start & end
env.new('qds.h','quadrupole_sw', length='l_qds/2', k1= 'kqds', knl=[0,0, 'ksd.qd3*l_qds/2']) #half for start & end

#QFNS
# DBname: PXMQNEMNWP
env['l_qfns'] = 0.7106
env.new('qfns','quadrupole', length='l_qfns', k1='kqfns')

#QFNEC
# DBname: PXMQNEMNWP
env['l_qfnec'] = 0.7090
env.new('qfnec','quadrupole', length='l_qfnec', k1='kqfnecool')

#QDNEC
# DBname: PXMQNEMNWP
env['l_qdnec'] = 0.7196
env.new('qdnec','quadrupole', length='l_qdnec', k1='kqdnecool')

#QFW6
# DBname: PXMQNFCAWP
env['l_qfw6'] = 0.7568
#env.new('qfw6','quadrupole', length='l_qfw6', k1 ='kqfw6')
env.new('qfw6','quadrupole_sw', length='l_qfw6', k1 ='kqfw6', knl=[0,0, 'ksf.qfw6*l_qfw6'])

#QFW8
# DBname: PXMQNFEAWP
env['l_qfw8'] = 0.7494
#env.new('qfw8','quadrupole', length='l_qfw8', k1='kqfw8')
env.new('qfw8','quadrupole_sw', length='l_qfw8', k1='kqfw8', knl=[0,0,'ksf.qfw8*l_qfw8'])

#QDW7
# DBname: PXMQNFDAWP
env['l_qdw7'] = 0.7499
#env.new('qdw7','quadrupole', length='l_qdw7', k1='kqdw7')
env.new('qdw7','quadrupole_sw', length='l_qdw7', k1='kqdw7', knl=[0,0,'ksf.qdw7*l_qdw7'])

#QDW9
# DBname: PXMQNFFAWP
env['l_qdw9'] = 0.7641
#env.new('qdw9','quadrupole', length='l_qdw9', k1='kqdw9')
env.new('qdw9','quadrupole_sw', length='l_qdw9', k1='kqdw9', knl=[0,0,'ksf.qdw9*l_qdw9'])


#### Skew quadrupoles
# DBname: PXMQSCANWP
env['l_qsk'] = 0.510  

# tilt = -pi/4 # from madxsuite survey:  _sin_rot_s = -0.7071, _cos_rot_s = 0.7071
env.new('qsk14','qsk', length = 'l_qsk', k1 = 'ksk1404', rot_s_rad= -np.pi/4) 
env.new('qsk43','qsk', length = 'l_qsk', k1 = 'ksk4308', rot_s_rad= -np.pi/4)

#define all names
env.new('dr.qsk1404','qsk14') 
env.new('dr.qsk4308','qsk43')


##### RF cavities

#deceleration cavity
env['l_decelcav'] = 0.670
env['f_decelcav'] = 1.
#, length='l_decelcav'
env.new('drift_decelcav', 'drift', length ='l_decelcav')
env.new('decelcav','rfcavity', voltage = 'cbr.v', frequency = 'f_decelcav', lag =0.) #HARMON=1 
# was DR_CRB0106 - defined later

#cavities for bunch rotation 
#f_rf = h * f_rev || f_rev = f_rf = 1 (prev cavity with h=1)
env['l_rotcav'] = 2.028
env['h_rotcav'] = 6. #HARMON=6; 
#length='l_rotcav',
env.new('drift_rotcav', 'drift', length ='l_rotcav')
env.new('rotcav','rfcavity',  voltage = 'cbr.v', frequency = 'f_decelcav * h_rotcav', lag =0.)  

##### Rotatable Sextupole
# DBname: PXMX_BANWP
env['l_xrc'] = 0.270
env.new('xrc', 'sextupole', length='l_xrc', k2 = 'kxrc16.41') 

#define all names
env.new('dr.xrc1604', 'xrc') 
env.new('dr.xrc4108', 'xrc')


##### Solenoids Electron Cooler Solenoids

#type 1
env['l_sec'] = 2.83
env['kecsol'] = 'on_ecsol * ( 0.062173 * dr.sec2910_i / (400 * 3.3356 * momentum))'
env.new('solsec', 'solenoid', length='l_sec', ks='kecsol') 

# type 2
env['l_sol'] = 0.343
env['kscomp26'] = 'on_ecsol * ((-0.4600 * dr.scomp2607_i) / (700 * 3.3356 * momentum))'
env.new('solscomp2607', 'solenoid', length='l_sol', ks='kscomp26') 

env['kscomp31'] = 'on_ecsol * ((-0.4600 * dr.scomp3106_i) / (700 * 3.3356 * momentum))'
env.new('solscomp3106', 'solenoid', length='l_sol', ks='kscomp31') 

#### Instruments

# Xsuite sees them as drifts
#simple l=0
env.new('instrument', 'drift', length=0.) 

# for instruments with length
env['l_shv'] = 0.4
env['l_ccc'] = 1.032
env['l_uhm'] = 2.2
env['l_uvm'] = 2.2


#### Vacum Valves

# considered instruments so i set them as drifts
env.new('vvs', 'drift', length=0.) 


#### Drifts

env['l_smi'] = 1.680
env.new('dr.smi5306','drift', length='l_smi') #, at = 170.931600)  # installed later


#### T Kicks
env['l_kick_kfe'] = 1.3285
env.new('kick.kfe', 'tkick', knl=[-0.], ksl=[0.], length='l_kick_kfe') 
#is dr.KFE3505 and dr.KFE5005 - defined later

env['l_kick_kfi'] = 2.0425
env.new('kick.kfi', 'tkick', knl=[-0.], ksl=[0.], length='l_kick_kfi') 
#is dr.KFI5506 and dr.KFI5606 - defined later

# after splits
#dr.kfe.e, dr.kfe.e
env['l_kick_ed'] = 0.600
env.new('kick.ed', 'tkick', knl=[-0.], ksl=[0.], length='l_kick_ed') 
env.new('drift_kick.ed', 'drift', length='l_kick_ed') 

env['l_kick_a'] = 0.672
env.new('kick.a', 'tkick', knl=[-0.], ksl=[0.], length='l_kick_a') 
env.new('drift_kick.a', 'drift', length='l_kick_a') 

env['l_kick_bc'] = 0.504
env.new('kick.bc', 'tkick', knl=[-0.], ksl=[0.], length='l_kick_bc') 
env.new('drift_kick.bc', 'drift', length='l_kick_bc') 

#define position & names
# main sequence
env.new_line(name='AD', components=[
        #main sequence -  quaadrupoles, bending magnets, sextupoles, 
        env.new('dr.qds01.h1','qds.h', at = 0.3553/2),
        env.new('dr.qfn02','qfns', at = 3.300000),
        env.new('dr.qds03','qds', at = 6.600000),
        env.new('dr.qfn04','qfn', at = 9.800000),
        env.new('dr.qdn05','qdn', at = 13.000000),
        env.new('dr.bhn05','bhn', at = 14.750650),
        env.new('dr.qfw06','qfw6', at = 16.501300),
        env.new('dr.bhn06','bhn', at = 18.251950),
        env.new('dr.qdw07','qdw7', at = 20.002600),
        env.new('dr.qfw08','qfw8', at = 22.602800),
        env.new('dr.bhw08','bhw', at = 24.353450),
        env.new('dr.qdw09','qdw9', at = 26.104100),
        env.new('dr.bhw09','bhw', at = 27.854750),
        env.new('dr.qfw10','qfw8', at = 29.605400),
        env.new('dr.qdw11','qdw7', at = 32.205600),
        env.new('dr.bhn11','bhn', at = 33.956250),
        env.new('dr.qfw12','qfw6', at = 35.706900),
        env.new('dr.bhn12','bhn', at = 37.457550),
        env.new('dr.qdn13','qdn', at = 39.208200),
        env.new('dr.qfn14','qfn', at = 42.408200),
        env.new('dr.qsk1404','qsk14', at = 43.301700),
        env.new('dr.qds15','qds', at = 45.608200),
        env.new('dr.qfn16','qfn', at = 48.808200),
        env.new('dr.xrc1604','xrc', at = 49.698200),
        env.new('dr.qdn17','qdn', at = 52.008200),
        env.new('dr.bhn17','bhn', at = 53.758850),
        env.new('dr.qfw18','qfw6', at = 55.509500),
        env.new('dr.bhn18','bhn', at = 57.260150),
        env.new('dr.qdw19','qdw7', at = 59.010800),
        env.new('dr.qfw20','qfw8', at = 61.611000),
        env.new('dr.bhw20','bhw', at = 63.361650),
        env.new('dr.qdw21','qdw9', at = 65.112300),
        env.new('dr.bhw21','bhw', at = 66.862950),
        env.new('dr.qfw22','qfw8', at = 68.613600),
        env.new('dr.qdw23','qdw7', at = 71.213800),
        env.new('dr.bhn23','bhn', at = 72.964450),
        env.new('dr.qfw24','qfw6', at = 74.715100),
        env.new('dr.bhn24','bhn', at = 76.465750),
        env.new('dr.qdn25','qdn', at = 78.216400),
        env.new('dr.qfn26','qfn', at = 81.416400),
        env.new('dr.qdn27','qdnec', at = 85.776800),
        env.new('dr.qdn28','qdnec', at = 86.729540),
        env.new('dr.qfn29a','qfnec', at = 87.785840),

        #mid AD 
        env.new('dr.qfn29b','qfnec', at = 94.646960),
        env.new('dr.qdn30','qdnec', at = 95.703260),
        env.new('dr.qdn31','qdnec', at = 96.656000),
        env.new('dr.qfn32','qfn', at = 101.016400),
        env.new('dr.qdn33','qdn', at = 104.216400),
        env.new('dr.bhn33','bhn', at = 105.967050),
        env.new('dr.qfw34','qfw6', at = 107.717700),
        env.new('dr.bhn34','bhn', at = 109.468350),
        env.new('dr.qdw35','qdw7', at = 111.219000),
        env.new('dr.qfw36','qfw8', at = 113.819200),
        env.new('dr.bhw36','bhw', at = 115.569850),
        env.new('dr.qdw37','qdw9', at = 117.320500),
        env.new('dr.bhw37','bhw', at = 119.071150),
        env.new('dr.qfw38','qfw8', at = 120.821800),
        env.new('dr.qdw39','qdw7', at = 123.422000),
        env.new('dr.bhn39','bhn', at = 125.172650),
        env.new('dr.qfw40','qfw6', at = 126.923300),
        env.new('dr.bhn40','bhn', at = 128.673950),
        env.new('dr.qdn41','qdn', at = 130.424600),
        env.new('dr.xrc4108','xrc', at = 133.004600),
        env.new('dr.qfn42','qfn', at = 133.624600),
        env.new('dr.qds43','qds', at = 136.824600),
        env.new('dr.qsk4308','qsk43', at = 139.131100),
        env.new('dr.qfn44','qfn', at = 140.024600),
        env.new('dr.qdn45','qdn', at = 143.224600),
        env.new('dr.bhn45','bhn', at = 144.975250),
        env.new('dr.qfw46','qfw6', at = 146.725900),
        env.new('dr.bhn46','bhn', at = 148.476550),
        env.new('dr.qdw47','qdw7', at = 150.227200),
        env.new('dr.qfw48','qfw8', at = 152.827400),
        env.new('dr.bhw48','bhw', at = 154.578050),
        env.new('dr.qdw49','qdw9', at = 156.328700),
        env.new('dr.bhw49','bhw', at = 158.079350),
        env.new('dr.qfw50','qfw8', at = 159.830000),
        env.new('dr.qdw51','qdw7', at = 162.430200),
        env.new('dr.bhn51','bhn', at = 164.180850),
        env.new('dr.qfw52','qfw6', at = 165.931500),
        env.new('dr.bhs52','bhs', at = 167.682150),
        env.new('dr.qdc53','qdc', at = 169.432800),
        env.new('dr.qfc54','qfc', at = 172.632800),
        env.new('dr.qds55','qds', at = 175.832800),
        env.new('dr.qfn56','qfns', at = 179.132800),
        env.new('dr.qds01.h2','qds.h', at = 182.255150),
        
        # Solenoids
        env.new('dr.sec2910', 'solsec', at = 91.216400), 
        env.new('dr.scomp2607', 'solscomp2607', at = 84.345400), 
        env.new('dr.scomp3106', 'solscomp3106', at = 98.087400), 

#############
        # kickers with no overlap

        #multipoles are thin elements => no actual length
        #installing a kicker drift with their length
        # | |_______| : kicker ref left (at=prev-l/2) - drift after(at=prev)
        #they are removed and replaced by smaller kickers

        #env.new('dr.kfe3505','kick.kfe', at = 112.568950),
        env.new('dr.kfe3505.d','kick.ed', at = 111.9247), 
        env.new('dr.drift_kfe3505.d','drift_kick.ed', at = 112.2247), #112.568950 - 1.3285/2+ 0.320000

        env.new('dr.kfe3505.e','kick.ed', at = 112.5557), 
        env.new('dr.drift_kfe3505.e','drift_kick.ed', at = 112.8557), #112.568950 - 1.3285/2+ 0.951000

        #env.new('dr.kfe5005','kick.kfe', at = 161.080250),
        env.new('dr.kfe5005.e','kick.ed', at = 160.4935), 
        env.new('dr.drift_kfe5005.e','drift_kick.ed', at = 160.7935), #161.080250- 1.3285/2+ 0.377500

        env.new('dr.kfe5005.d','kick.ed', at = 161.1245), 
        env.new('dr.drift_kfe5005.d','drift_kick.ed', at = 161.4245), #161.080250- 1.3285/2+ 1.008500
        
        #env.new('dr.kfi5506','kick.kfi', at = 177.512550), 
        env.new('dr.kfi5506.a','kick.a',  at = 176.7288), 
        env.new('dr.drift_kfi5506.a','drift_kick.a',  at = 177.0648), #177.512550 - 2.0425/2 + 0.573500

        env.new('dr.kfi5506.b','kick.bc', at = 177.4258), 
        env.new('dr.drift_kfi5506.b','drift_kick.bc', at = 177.6778), #177.512550 - 2.0425/2 + 1.186500

        env.new('dr.kfi5506.c','kick.bc', at = 177.9548), 
        env.new('dr.drift_kfi5506.c','drift_kick.bc', at = 178.2068), #177.512550 - 2.0425/2 + 1.715500

        #env.new('dr.kfi5606','kick.kfi', at = 180.753050),
        env.new('dr.kfe5606.c','kick.bc', at = 179.8068), 
        env.new('dr.drift_kfe5606.c','drift_kick.bc', at = 180.0588), #180.753050 - 2.0425/2 + 0.327000

        env.new('dr.kfe5606.b','kick.bc', at = 180.3358), 
        env.new('dr.drift_kfe5606.b','drift_kick.bc', at = 180.5878), #180.753050 - 2.0425/2 + 0.856000

        env.new('dr.kfi5606.a','kick.a',  at = 180.8648), 
        env.new('dr.drift_kfi5606.a','drift_kick.a',  at = 181.2008), #180.753050 - 2.0425/2 + 1.469000

        
#############

        # RF cavities
        #rf dont have length -> installing a rf drift with their length after them
        env.new('dr.crb0106','decelcav', at = 1.1724), 
        env.new('dr.drift_crb0106','drift_decelcav', at = 1.507400), #=1.549 - 0.0416

        env.new('dr.cbr2506', 'rotcav', at = 78.8049), 
        env.new('dr.drift_crb02506','drift_rotcav', at = 79.818900),

        env.new('dr.cbr2606', 'rotcav', at = 82.0599),
        env.new('dr.drift_crb02606','drift_rotcav', at = 83.073900), 

        # instruments
        env.new('dr.shv1305','instrument', length='l_shv', at = 40.6542), # =39.2082 + 1.446
        env.new('dr.ccc1501','instrument', length='l_ccc', at = 47.2465), # = 45.6082 + 1.6383
        env.new('dr.uhm3107','instrument', length='l_uhm', at = 99.41640), #98.316400 + 1.1
        env.new('dr.uvm3207','instrument', length='l_uvm', at = 102.6139), #101.513900 + 1.1
        env.new('dr.smi5306','instrument', length='l_smi', at = 170.931600),
        
        env.new('dr.usv0205','instrument', at = 4.3325), #(5.240000+5.825000)/2 - 1.2
        env.new('dr.ush0207','instrument', at = 5.5325), #(5.240000+5.825000)/2
        env.new('dr.bipm4207','instrument', at = 134.8106), #133.624600 + 0.732/2 + 1*0.82
        env.new('dr.bipm4208','instrument', at = 135.6306), #133.624600 + 0.732/2 + 2*0.82
        #env.new('dr.tfa4106','instrument', at = ), # PROB not installed
        env.new('dr.ush4405','instrument', at = 140.8246), #140.024600 + (143.224600 - 140.024600)*(1/4)
        env.new('dr.usv4407','instrument', at = 142.4246), #140.024600 + (143.224600 - 140.024600)*(3/4)
 
        #markers
        env.new('dr.start.ad', 'marker', at = 0.000),
        env.new('dr.s.khm0307', 'marker', at = 7.097500), 
        env.new('dr.e.khm0307', 'marker', at = 9.297500), #7.097500 + 2.2
        env.new('dr.s.kvm0407', 'marker', at = 10.297500), 
        env.new('dr.e.kvm0407', 'marker', at = 12.4975), # 10.297500 + 2.2
        env.new('dr.s.cbr2506', 'marker', at = 78.804900), 
        env.new('dr.s.cbr2606', 'marker', at = 82.059900), 
        env.new('dr.s.scomp2607', 'marker', at = 84.173900), 
        env.new('dr.s.sec2910', 'marker', at = 89.801400), 
        #env.new('dr.mid.ad', 'marker', at = 91.216400), #mid AD # it crashes-overlaps -> moved to extras
        env.new('dr.s.scomp3106', 'marker', at = 97.915900), 
        env.new('dr.s.uhm3107', 'marker', at = 98.316400), 
        env.new('dr.e.uhm3107', 'marker', at = 100.516400), # 98.316400 + 2.2
        env.new('dr.s.uvm3207', 'marker', at = 101.513900), 
        env.new('dr.e.uvm3207', 'marker', at = 103.713900), #101.513900 + 2.2
        env.new('dr.s.kfe3505', 'marker', at = 111.90470), # 112.568950-1.3285/2
        env.new('dr.s.kfe5005', 'marker', at = 160.41600), # 161.080250-1.3285/2
        env.new('dr.s.smi5306', 'marker', at = 170.091600), 
        env.new('dr.e.smi5306', 'marker', at = 171.771600), 
        env.new('dr.s.kfi5506', 'marker', at = 176.49130), # 177.512550-2.0425/2
        env.new('dr.s.kfi5606', 'marker', at = 179.73180), # 180.753050-2.0425/2
        env.new('dr.end.ad', 'marker', at = 182.43280),

        #vacum valves - PROB all not installed
        #env.new('dr.vvs0103', 'vvs', at = ) #right after qdn01
        #env.new('dr.vvs1008', 'vvs', at = )
        #env.new('dr.vvs1508', 'vvs', at = )
        #env.new('dr.vvs2607', 'vvs', at = )
        #env.new('dr.vvs3105', 'vvs', at = )
        #env.new('dr.vvs4704', 'vvs', at = )
        ]) 


'''
injection exctraction stuff

!!! apertures
#/* ******************* */
#! Injection/Extraction kickers
DR.KFI.A, APERTYPE=RECTANGLE, APERTURE={ 0.07000, 0.04750 };
DR.KFI.B, APERTYPE=RECTANGLE, APERTURE={ 0.07000, 0.04100 };
DR.KFI.C, APERTYPE=RECTANGLE, APERTURE={ 0.07000, 0.03600 };
!
DR.KFE.D, APERTYPE=ELLIPSE, APERTURE={ 0.99999, 0.99999 };
DR.KFE.E, APERTYPE=ELLIPSE, APERTURE={ 0.99999, 0.99999 };

/* ******************* */
! Extraction Septum
! PROB Aperture type is not defined for a "DRIFT" object... Need to define it as collimator maybe... 
!DR.SMI5306,       APERTYPE=RECTANGLE,   APERTURE={ 0.99999, 0.99999 };


!!!!additional split.MADX:

#### Injection & exctraction septa

# PROB not installed 
env['l_sme'] = 1.
env.new('dr.sme5305','drift', length='l_sme')
env.new('dr.sme5307','drift', length='l_sme')



/* ********************************************************** */
!           Injection/Extraction kickers


AUX.ELM.AT = 112.568950;
AUX.ELM.L  = DR.KFE3505->l;
SEQEDIT,SEQUENCE=AD;
REMOVE,  ELEMENT=DR.KFE3505;
INSTALL, ELEMENT=DR.KFE.D        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.320000;
INSTALL, ELEMENT=DR.KFE.E        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.951000;
ENDEDIT;


AUX.ELM.AT = 161.080250;
AUX.ELM.L  = DR.KFE5005->l;
SEQEDIT,SEQUENCE=AD;
REMOVE,  ELEMENT=DR.KFE5005;
INSTALL, ELEMENT=DR.KFE.E        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.377500;
INSTALL, ELEMENT=DR.KFE.D        , at = AUX.ELM.AT - AUX.ELM.L/2 + 1.008500;
ENDEDIT;


AUX.ELM.AT = 177.512550;
AUX.ELM.L  = DR.KFI5506->l;
SEQEDIT,SEQUENCE=AD;
REMOVE,  ELEMENT=DR.KFI5506;
INSTALL, ELEMENT=DR.KFI.A        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.573500;
INSTALL, ELEMENT=DR.KFI.B        , at = AUX.ELM.AT - AUX.ELM.L/2 + 1.186500;
INSTALL, ELEMENT=DR.KFI.C        , at = AUX.ELM.AT - AUX.ELM.L/2 + 1.715500;
ENDEDIT;


AUX.ELM.AT = 180.753050;
AUX.ELM.L  = DR.KFI5606->l;
SEQEDIT,SEQUENCE=AD;
REMOVE,  ELEMENT=DR.KFI5606;
INSTALL, ELEMENT=DR.KFI.C        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.327000;
INSTALL, ELEMENT=DR.KFI.B        , at = AUX.ELM.AT - AUX.ELM.L/2 + 0.856000;
INSTALL, ELEMENT=DR.KFI.A        , at = AUX.ELM.AT - AUX.ELM.L/2 + 1.469000;
ENDEDIT;

!!! main seq

kickers:
DR.KFE.D:   TKICKER,  L=0.600, HKICK=0.; ! Here L is magnetic length
DR.KFE.E:   TKICKER,  L=0.600, HKICK=0.; ! Here L is magnetic length

DR.KFI.A:   TKICKER,  L=0.672, HKICK=0.; ! Here L is magnetic length
DR.KFI.B:   TKICKER,  L=0.504, HKICK=0.; ! Here L is magnetic length
DR.KFI.C:   TKICKER,  L=0.504, HKICK=0.; ! Here L is magnetic length
!



'''
