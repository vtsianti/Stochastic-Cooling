#addding new apertures the old way
#doesnt really work

import numpy as np
import xtrack as xt

env = xt.get_environment()

env.vars.default_to_zero = True

'''
LimitEllipse
a (float) Horizontal semi-axis in meters.
b (float) Vertical semi-axis in meters.

MADX: horizontal and vertical semi-axes of ellipse
---------

LimitRect
min_x (float) Lower x limit in meters.
max_x (float) Upper x limit in meters.
min_y (float) Lower y limit in meters.
max_y (float) Upper y limit in meters.

MADX: half width and half height of rectangle, radius of circle
(i suppose it is in meters)

=> transform values to fit xsuite definition
'''

#define main apertures

line = env['AD']
tab = line.get_table()
env = xt.get_environment()


def insert_aper_2(element, ap_type, name, l_type):
    
    env = xt.get_environment()
    line = env['AD']
    tab = line.get_table()

    #name = f'{ap_type=}'.split('=')[0]

    s_array = tab.rows[element + '.*'].s

    line.insert_element('a'+ element[2:] + '...' + name[3:], ap_type, at_s= s_array[0] + l_type)



#index='dr.qsk4308')
#at_s=tab['s', 'dr.qsk4308'] + env['l_qsk'])

#magnet from decomposition file
#change all to meters from mm

#AD_VCTUB0081: 123-1.5*2 circle
#qds01? * 7 - 
env['rad_vctub0081'] = ((123 - (1.5*2)) /2)* 1e-3
ap_vctub0081= xt.LimitEllipse(a=env['rad_vctub0081'],b=env['rad_vctub0081'])

name = f'{ap_vctub0081=}'.split('=')[0]
insert_aper_2('dr.qds01.h1',ap_vctub0081, 'ap_vctub0081', env['l_qds']/2)

#AD_VCTUB0083: 123-1.5*2 circle
#qds01? * 3 - 
env['rad_vctub0083'] = ((123 - (1.5*2)) /2)* 1e-3
ap_vctub0083= xt.LimitEllipse(a=env['rad_vctub0083'],b=env['rad_vctub0083'])

insert_aper_2('dr.qds01.h1',ap_vctub0083, 'ap_vctub0083',env['l_qds']/2)


#AD_BPM__0001: 202-1.5*2 circle orange
#qds01?*4 
env['rad_bpm0001'] = ((202 - (1.5*2)) /2)* 1e-3
ap_bpm0001 = xt.LimitEllipse(a=env['rad_bpm0001'],b=env['rad_bpm0001'])

insert_aper_2('dr.qds01.h1', ap_bpm0001, 'ap_bpm0001', env['l_qds']/2)


#AD_MQFNA0002: 143-1.5*2 circle orange
#qfn02 * 5
env['rad_mqfna0002'] = ((143 - (1.5*2))/2) * 1e-3
ap_mqfna0002= xt.LimitEllipse(a=env['rad_mqfna0002'],b=env['rad_mqfna0002'])

insert_aper_2('dr.qfn02',ap_mqfna0002, 'ap_mqfna0002',env['l_qfn'])


#PS.C.488.43.1: 238 circle
#qdw07*1 | qdw19*1 | qfw22 *1 | qfw38 *1
#qfn16*2 | qfn44*2 | qfw50 * 2 | qfc54*2 | qds55*2 | qfn56
env['rad_psc0488_43'] = ((238)/2) * 1e-3
ap_psc0488_43 = xt.LimitEllipse(a=env['rad_psc0488_43'],b=env['rad_psc0488_43'])

all_elem = ['dr.qdw07', 'dr.qdw19']
for element in all_elem:
    insert_aper_2(element, ap_psc0488_43, 'ap_psc0488_43',env['l_qdw7'])


all_elem = ['dr.qfw22', 'dr.qfw38', 'dr.qfw50']
for element in all_elem:
    insert_aper_2(element, ap_psc0488_43, 'ap_psc0488_43', env['l_qfw8'])

all_elem = ['dr.qfn16','dr.qfn44']
for element in all_elem:
    insert_aper_2(element, ap_psc0488_43,'ap_psc0488_43', env['l_qfn'])


insert_aper_2('dr.qfc54', ap_psc0488_43, 'ap_psc0488_43', env['l_qfc'])
insert_aper_2('dr.qds55', ap_psc0488_43, 'ap_psc0488_43', env['l_qds'])
insert_aper_2('dr.qfn56', ap_psc0488_43, 'ap_psc0488_43', env['l_qfns'])


#AD_VCTUB0001: 300 circle orange
#qdw07*1 | qdw19*1 | qfw22*1 | qfw38*1 
env['rad_vctub0001'] = ((300)/2) * 1e-3
ap_vctub0001 = xt.LimitEllipse(a=env['rad_vctub0001'], b=env['rad_vctub0001'])

all_elem = ['dr.qdw07', 'dr.qdw19']
for element in all_elem:
    insert_aper_2(element, ap_vctub0001,'ap_vctub0001', env['l_qdw7'])


all_elem = ['dr.qfw22', 'dr.qfw38']
for element in all_elem:
    insert_aper_2(element, ap_vctub0001, 'ap_vctub0001', env['l_qfw8'])


counter = 0
#AD_MQFWI0001: rectangle 80, 340 |-| 
#qfw08*5 | qfw10*5 | qfw18*5 | qfw20 *5| qfw22*5| qfw24*5| qfw48*5 |qfw50*5| qfw52*5
env['x_mqfwi0001'] = (340) * 1e-3
env['y_mqfwi0001'] = (80) * 1e-3
ap_mqfwi0001= xt.LimitRect(max_x=env['x_mqfwi0001'],max_y=env['y_mqfwi0001'])

all_elem = ['dr.qfw08', 'dr.qfw10', 'dr.qfw20', 'dr.qfw22', 'dr.qfw48','dr.qfw50']
for element in all_elem:
    insert_aper_2(element, ap_mqfwi0001, 'ap_mqfwi0001', env['l_qfw8'])


all_elem = ['dr.qfw18', 'dr.qfw24', 'dr.qfw52']
for element in all_elem:
    insert_aper_2(element, ap_mqfwi0001,'ap_mqfwi0001', env['l_qfw6'])



#AD_VCTUB0008: 332-? cricle orange
# qfw10 *8
env['rad_vctub0008'] = ((332)/2) * 1e-3
ap_vctub0008= xt.LimitEllipse(a=env['rad_vctub0008'],b=env['rad_vctub0008'])

insert_aper_2('dr.qfw10', ap_vctub0008, 'ap_vctub0008', env['l_qfw8'])


#AD_VCTUB0005: circle ??
# qfw10*7
#env['rad_vctub0005'] = #((332)/2) * 1e-3
#ap_vctub0005 = xt.LimitEllipse(a=env['rad_vctub0005'],b=env['rad_vctub0005'])

#PS.C.0467.43 : 140 circle orange
# qdn13*5 | qfn16*5 | qdn25*5 |
env['rad_psc0467_43'] = ((140)/2) * 1e-3
ap_psc0467_43 = xt.LimitEllipse(a=env['rad_psc0467_43'],b=env['rad_psc0467_43'])

all_elem = ['dr.qdn13', 'dr.qdn25']
for element in all_elem:
    insert_aper_2(element, ap_psc0467_43, 'ap_psc0467_43', env['l_qdn'])

    #line.insert_element('a'+ element[2:]+'.psc0467_43', ap_psc0467_43, at_s=tab['s', element] + env['l_qdn'])

insert_aper_2('dr.qfn16', ap_psc0467_43, 'ap_psc0467_43', env['l_qfn'])
#line.insert_element('a.qfn16.vctub0008', ap_psc0467_43, at_s=tab['s', 'dr.qfn16'] + env['l_qfn'])


#AD_MCB_A0019: 156/159 – 1.5*2 circle orange
#qdn13*4 | 
env['rad_mcba0019'] = ((156-(1.5*2))/2) * 1e-3
ap_mcba0019= xt.LimitEllipse(a=env['rad_mcba0019'],b=env['rad_mcba0019'])

insert_aper_2('dr.qdn13', ap_mcba0019,'ap_mcba0019', env['l_qdn'])
#line.insert_element('a.qdn13.mcba0019', ap_mcba0019, at_s=tab['s', 'dr.qdn13'] + env['l_qdn'])


#AD_MQSK_0001: 156/159 circle
#qdn13*8 | 
env['rad_mqsk0001'] = ((156)/2) * 1e-3
ap_mqsk0001 = xt.LimitEllipse(a=env['rad_mqsk0001'],b=env['rad_mqsk0001'])

insert_aper_2('dr.qdn13', ap_mqsk0001, 'ap_mqsk0001', env['l_qdn'])
#line.insert_element('a.qdn13.mqsk0001', ap_mqsk0001, at_s=tab['s', 'dr.qdn13'] + env['l_qdn'])


#AD_MQFNA0028: 55*2 | 75*2 diams |---| ellipse
# qfn14*5 | 
env['a_mqfna0028'] = ((75*2)/2) * 1e-3
env['b_mqfna0028'] = ((55*2)/2) * 1e-3
ap_mqfna0028 = xt.LimitEllipse(a=env['a_mqfna0028'],b=env['b_mqfna0028'])

insert_aper_2('dr.qfn14', ap_mqfna0028,'ap_mqfna0028', env['l_qfn'])
#line.insert_element('a.qfn14.mqfna0028', ap_mqfna0028, at_s=tab['s', 'dr.qfn14'] + env['l_qfn'])


#AD_MQSK_0011: 156/159 circle
# qfn14*4
env['rad_mqsk0011'] = ((156)/2) * 1e-3
ap_mqsk0011 = xt.LimitEllipse(a=env['rad_mqsk0011'],b=env['rad_mqsk0011'])

insert_aper_2('dr.qfn14', ap_mqsk0011, 'ap_mqsk0011', env['l_qfn'])
#line.insert_element('a.qfn14.mqsk0011', ap_mqsk0011, at_s=tab['s', 'dr.qfn14'] + env['l_qfn'])

#AD_MQDSE0008: 143 cricle
# qds15*5 | qds43*5
env['rad_mqdse0008'] = ((143)/2) * 1e-3
ap_mqdse0008 = xt.LimitEllipse(a=env['rad_mqdse0008'],b=env['rad_mqdse0008'])

insert_aper_2('dr.qds15', ap_mqdse0008,'ap_mqdse0008', env['l_qds'])
#line.insert_element('a.qds15.mqdse0008', ap_mqdse0008, at_s=tab['s', 'dr.qds15'] + env['l_qds'])


#AD_VCTUB0072: 159 circle RED
#qds15*4
env['rad_vctub0072'] = ((159)/2) * 1e-3
ap_vctub0072= xt.LimitEllipse(a=env['rad_vctub0072'],b=env['rad_vctub0072'])

insert_aper_2('dr.qds15', ap_vctub0072,'ap_vctub0072', env['l_qds'])
#line.insert_element('a.qds15.vctub0072', ap_vctub0072, at_s=tab['s', 'dr.qds15'] + env['l_qds'])


#AD_VCTUB0068: 100 circle
#qds15*3 | 
env['rad_vctub0068'] = ((100)/2) * 1e-3
ap_vctub0068= xt.LimitEllipse(a=env['rad_vctub0068'],b=env['rad_vctub0068'])

insert_aper_2('dr.qds15', ap_vctub0068, 'ap_vctub0068', env['l_qds'])
#line.insert_element('a.qds15.vctub0068', ap_vctub0068, at_s=tab['s', 'dr.qds15'] + env['l_qds'])


#AD_VCTUB0071: 159-1.5*2 circle
#qds15*4
env['rad_vctub0071'] = ((159 - (1.5*2))/2) * 1e-3
ap_vctub0071= xt.LimitEllipse(a=env['rad_vctub0071'],b=env['rad_vctub0071'])

insert_aper_2('dr.qds15', ap_vctub0071,'ap_vctub0071', env['l_qds'])
#line.insert_element('a.qds15.vctub0071', ap_vctub0071, at_s=tab['s', 'dr.qds15'] + env['l_qds'])


#AD_MQFNA0024: 55*2 | 75*2 diams |---| ellipse
#qds15*5 |qfn44*5
env['a_mqfna0024'] = ((75*2)/2) * 1e-3
env['b_mqfna0024'] = ((55*2)/2) * 1e-3
ap_mqfna0024 = xt.LimitEllipse(a=env['a_mqfna0024'],b=env['b_mqfna0024'])

insert_aper_2('dr.qds15', ap_mqfna0024, 'ap_mqfna0024', env['l_qds'])
insert_aper_2('dr.qfn44', ap_mqfna0024, 'ap_mqfna0024', env['l_qfn'])
'ap_mqfna0024', 
#line.insert_element('a.qds15.mqfna0024', ap_mqfna0024, at_s=tab['s', 'dr.qds15'] + env['l_qds'])
#line.insert_element('a.qfn44.mqfna0024', ap_mqfna0024, at_s=tab['s', 'dr.qfn44'] + env['l_qfn'])


#AD_BEECN0080: 163-10*2 circle orange
#SOL26*4
env['rad_beecn0080'] = ((163-(10*2))/2) * 1e-3
ap_beecn0080 = xt.LimitEllipse(a=env['rad_beecn0080'],b=env['rad_beecn0080'])

insert_aper_2('dr.scomp2607', ap_beecn0080,'ap_beecn0080', env['l_sec'])
#line.insert_element('a.scomp2607.beecn0080', ap_beecn0080, at_s=tab['s', 'dr.scomp2607'] + env['l_sec'])


#AD_MQDNA0003: 145/148 circle
#qdn27*7
env['rad_mqdna0003'] = ((145)/2) * 1e-3
ap_mqdna0003 = xt.LimitEllipse(a=env['rad_mqdna0003'],b=env['rad_mqdna0003'])

insert_aper_2('dr.qdn27', ap_mqdna0003, 'ap_mqdna0003', env['l_qdnec'])
#line.insert_element('a.qdn27.mqdna0003', ap_mqdna0003, at_s=tab['s', 'dr.qdn27'] + env['l_qdnec'])


#AD_MQDNA0001: 156 circle
#qdn28*6 | 
env['rad_mqdna0001'] = ((156)/2) * 1e-3
ap_mqdna0001 = xt.LimitEllipse(a=env['rad_mqdna0001'],b=env['rad_mqdna0001'])

insert_aper_2('dr.qdn28', ap_mqdna0001,'ap_mqdna0001', env['l_qdnec'])
#line.insert_element('a.qdn28.mqdna0001', ap_mqdna0001, at_s=tab['s', 'dr.qdn28'] + env['l_qdnec'])


#AD_MQFNA0001: 172 circle
#qfn29*4
env['rad_mqfna0001'] = ((172)/2) * 1e-3
ap_mqfna0024 = xt.LimitEllipse(a=env['rad_mqfna0001'],b=env['rad_mqfna0001'])

insert_aper_2('dr.qfn29b', ap_mqfna0024,'ap_mqfna0024', env['l_qfnec'])
#line.insert_element('a.qdn29b.mqfna0024', ap_mqfna0024, at_s=tab['s', 'dr.qdn29b'] + env['l_qfnec'])


#dont know in which ecooler solenoid to install
'''
#AD_BEECN0058: 145 circle
#ecooler*8
env['rad_beecn0058'] = ((145)/2) * 1e-3
ap_beecn0058 = xt.LimitEllipse(a=env['rad_beecn0058'],b=env['rad_beecn0058'])

#AD_BEECN0044: 72|112: |---| rectangle
#ecooler*3
env['x_beecn0044'] = ((112)/2) * 1e-3
env['y_beecn0044'] = ((72)/2) * 1e-3
ap_beecn0044 = xt.LimitRect(max_x=env['x_beecn0044'],max_y=env['y_beecn0044'])

#LEABEECN0002: ?? red
#ecooler*7
#env['rad_leabeecn0002'] = #((145)/2) * 1e-3
#ap_leabeecn0002 = xt.LimitEllipse(a=env['rad_leabeecn0002'],b=env['rad_leabeecn0002'])

#AD_BEECN0070: 160 circle
#ecooler*3
env['rad_beecn0070'] = ((160)/2) * 1e-3
ap_beecn0070 = xt.LimitEllipse(a=env['rad_beecn0070'],b=env['rad_beecn0070'])

#LEABEECN0018: L: 154 R:140
#ecooler*6
env['rad_leabeecn0018'] = ((140)/2) * 1e-3
ap_leabeecn0018 = xt.LimitEllipse(a=env['rad_leabeecn0018'],b=env['rad_leabeecn0018'])
'''

#AD_BEECN0073: 145 circle
# sol31*5
env['rad_beecn0073'] = ((145)/2) * 1e-3
ap_beecn0073 = xt.LimitEllipse(a=env['rad_beecn0073'],b=env['rad_beecn0073'])

insert_aper_2('dr.scomp3106', ap_beecn0073, 'ap_beecn0073', env['l_sol'])
#line.insert_element('a.scomp3106.beecn0073', ap_beecn0073, at_s=tab['s', 'dr.scomp3106'] + env['l_sol'])


#AD_LM___0022: L:X M: 300 R: 238 circle orange
# no-where-> breaks to PS.C0488.43 (installed) && AD_VCTUB0001(installed) && PS.C.0400.44(dont exist in decomp)
#env['rad_lm0022'] = ((238)/2) * 1e-3
#ap_lm0022 = xt.LimitEllipse(a=env['rad_lm0022'],b=env['rad_lm0022'])

#AD_VCTUB0014: 156 circle
#qdn41*4
env['rad_vctub0014'] = ((156)/2) * 1e-3
ap_vctub0014= xt.LimitEllipse(a=env['rad_vctub0014'],b=env['rad_vctub0014'])

insert_aper_2('dr.qdn41', ap_vctub0014, 'ap_vctub0014', env['l_qdn'])
#line.insert_element('a.qdn41.vctub0014', ap_vctub0014, at_s=tab['s', 'dr.qdn41'] + env['l_qdn'])


#AD_VCTUB0012: 156 circle
#qdn41*4
env['rad_vctub0012'] = ((156)/2) * 1e-3
ap_vctub0012 = xt.LimitEllipse(a=env['rad_vctub0012'],b=env['rad_vctub0012'])

insert_aper_2('dr.qdn41', ap_vctub0012, 'ap_vctub0012', env['l_qdn'])
#line.insert_element('a.qdn41.vctub0012', ap_vctub0012, at_s=tab['s', 'dr.qdn41'] + env['l_qdn'])


#AD_VCTUB0020: 160/163 circle
#qfn42*5
env['rad_vctub0020'] = ((160)/2) * 1e-3
ap_vctub0020= xt.LimitEllipse(a=env['rad_vctub0020'],b=env['rad_vctub0020'])

insert_aper_2('dr.qfn42', ap_vctub0020, 'ap_vctub0020', env['l_qfn'])
#line.insert_element('a.qfn42.vctub0020', ap_vctub0020, at_s=tab['s', 'dr.qfn42'] + env['l_qfn'])


#AD_VCTUB0034: 156/159 circle
#qds43*4
env['rad_vctub0034'] = ((156)/2) * 1e-3
ap_vctub0034= xt.LimitEllipse(a=env['rad_vctub0034'],b=env['rad_vctub0034'])

insert_aper_2('dr.qds43', ap_vctub0034, 'ap_vctub0034', env['l_qds'])


#AD_MQSK_0007: 156 circle
# dont exist in decomp
#env['rad_mqsk0007'] = ((156)/2) * 1e-3
#ap_mqsk0007 = xt.LimitEllipse(a=env['rad_mqsk0007'],b=env['rad_mqsk0007'])

#AD_VCTUB0003: circle 245 orange
#qdw47*5
env['rad_vctub0003'] = ((245)/2) * 1e-3
ap_vctub0003= xt.LimitEllipse(a=env['rad_vctub0003'],b=env['rad_vctub0003'])

insert_aper_2('dr.qdw47', ap_vctub0003, 'ap_vctub0003', env['l_qdw7'])


#AD_VCTUB0040: L:332-? R: 544 -? circle
#qdw47*8
env['rad_vctub0040'] = ((332)/2) * 1e-3
ap_vctub0040= xt.LimitEllipse(a=env['rad_vctub0040'],b=env['rad_vctub0040'])

insert_aper_2('dr.qdw47', ap_vctub0040, 'ap_vctub0040', env['l_qdw7'])
#line.insert_element('a.qdw47.vctub0040', ap_vctub0040, at_s=tab['s', 'dr.qdw47'] + env['l_qdw7'])


#AD_MCB_A0002: 269 circle
#qfc54*4
env['rad_mcba0002'] = ((269)/2) * 1e-3
ap_mcba0002 = xt.LimitEllipse(a=env['rad_mcba0002'],b=env['rad_mcba0002'])

insert_aper_2('dr.qfc54', ap_mcba0002, 'ap_mcba0002', env['l_qfc'])
#line.insert_element('a.qfc54.mcba0002', ap_mcba0002, at_s=tab['s', 'dr.qfc54'] + env['l_qfc'])


#AD_MCB_A0003: 205/200 circle orange
#qfc54*3
env['rad_mcba0003'] = ((200)/2) * 1e-3
ap_mcba0003 = xt.LimitEllipse(a=env['rad_mcba0003'],b=env['rad_mcba0003'])

insert_aper_2('dr.qfc54', ap_mcba0003, 'ap_mcba0003', env['l_qfc'])
#line.insert_element('a.qfc54.mcba0003', ap_mcba0003, at_s=tab['s', 'dr.qfc54'] + env['l_qfc'])


#AD_MQDSE0005: 140 circle
#qfn56*5
env['rad_mqdse0005'] = ((140)/2) * 1e-3
ap_mqdse0005 = xt.LimitEllipse(a=env['rad_mqdse0005'],b=env['rad_mqdse0005'])

#AD_VCTUB0028: 95 circle
#qfn56*3
env['rad_vctub0028'] = ((95)/2) * 1e-3
ap_vctub0028 = xt.LimitEllipse(a=env['rad_vctub0028'],b=env['rad_vctub0028'])

#AD_VCTUB0029: 95 circle
#qfn56*3
env['rad_vctub0029'] = ((95)/2) * 1e-3
ap_vctub0029 = xt.LimitEllipse(a=env['rad_vctub0029'],b=env['rad_vctub0029'])

#AD_VCDBG0001: 81 circle
# qfn56*4
env['rad_vcdbg0001'] = ((80)/2) * 1e-3
ap_vcdbg0001 = xt.LimitEllipse(a=env['rad_vcdbg0001'],b=env['rad_vcdbg0001'])

#AD_VCQAK0001: 54-(1.5*2) circle
# qfn56*4
env['rad_vcqak0001'] = ((54-(1.5*2))/2) * 1e-3
ap_vcqak0001 = xt.LimitEllipse(a=env['rad_vcqak0001'],b=env['rad_vcqak0001'])

#AD_VCQAL0001: L:51 M: 54-(1.5*2) R:52 circle
#qfn56*3
env['rad_vcqal0001'] = ((54-(1.5*2))/2) * 1e-3
ap_vcqal0001 = xt.LimitEllipse(a=env['rad_vcqal0001'],b=env['rad_vcqal0001'])

#AD_VBCB_0001: 60 circle orange
#qfn56*3
env['rad_vbcb0001'] = ((60)/2) * 1e-3
ap_vbcb0001 = xt.LimitEllipse(a=env['rad_vbcb0001'],b=env['rad_vbcb0001'])

#AD_VCDBH0001: L:66 M:70-(4*2) R:66 orange circle
# not found in decomp0
env['rad_vcdbh0001'] = ((70-(4*2))/2) * 1e-3
ap_vcdbh0001 = xt.LimitEllipse(a=env['rad_vcdbh0001'],b=env['rad_vcdbh0001'])

#AD_VCTCM0001: L:100 M:103-(1.5*2) R:100 orange circle
#qfn56 * 4
env['rad_vctcm0001'] = ((103-(1.5*2))/2) * 1e-3
ap_vctcm0001 = xt.LimitEllipse(a=env['rad_vctcm0001'],b=env['rad_vctcm0001'])

#AD_VCDCD0001: 160 circle orange
#qfn56 * 3
env['rad_vcdcd0001'] = ((160)/2) * 1e-3
ap_vcdcd0001 = xt.LimitEllipse(a=env['rad_vcdcd0001'],b=env['rad_vcdcd0001'])

#AD_VCTCN0001: 156 cicrle
#qfn56*4
env['rad_vctcn0001'] = ((156)/2) * 1e-3
ap_vctcn0001 = xt.LimitEllipse(a=env['rad_vctcn0001'],b=env['rad_vctcn0001'])

#AD_VCTUB0048: 109.1 circle
#qfn56*2
env['rad_vctub0048'] = ((109.1)/2) * 1e-3
ap_vctub0048 = xt.LimitEllipse(a=env['rad_vctub0048'],b=env['rad_vctub0048'])

#PSZMQ___0052: 120 cicrle
#qfn56*8
env['rad_pszmq0052'] = ((120)/2) * 1e-3
ap_pszmq0052 = xt.LimitEllipse(a=env['rad_pszmq0052'],b=env['rad_pszmq0052'])

#PSZVCTUB0022: 135 circle
#qfn56*2
env['rad_pszvctub0022'] = ((135)/2) * 1e-3
ap_pszvctub0022 = xt.LimitEllipse(a=env['rad_pszvctub0022'],b=env['rad_pszvctub0022'])

#PSZMB___0082: 0081: 163.1 & 0078:120/123 RED && don’t understand shape connects to PSZMB___0081 &&  PSZMB___0078   
# ||| https://edms.cern.ch/ui/file/221232/0/pszmb___0078-v0_plt_cpdf.pdf |||| https://edms.cern.ch/ui/file/221229/0/pszmb___0081-v0_plt_cpdf.pdf
#qfn56*5

#PSZMCB_A0021: 130 circle
#qfn56*4
env['rad_pszmcba0021'] = ((130)/2) * 1e-3
ap_pszmcba0021 = xt.LimitEllipse(a=env['rad_pszmcba0021'],b=env['rad_pszmcba0021'])

#PS.C.3841.43: 240 circel orange
#qfn56*5
env['rad_psc3841_43'] = ((240)/2) * 1e-3
ap_psc3841_43 = xt.LimitEllipse(a=env['rad_psc3841_43'],b=env['rad_psc3841_43'])

#PS.C.3861.43: L:204 M: 220/224 circle
#qfn56*5
env['rad_psc3861_43'] = ((204)/2) * 1e-3
ap_psc3861_43 = xt.LimitEllipse(a=env['rad_psc3861_43'],b=env['rad_psc3861_43'])

#PS.C.3869.43: 200/204 circle
#qfn56*2
env['rad_psc3869_43'] = ((200)/2) * 1e-3
ap_psc3869_43 = xt.LimitEllipse(a=env['rad_psc3869_43'],b=env['rad_psc3869_43'])

#PS.C.4502.43.3 L:204 R:200
#qfn56*5
env['rad_psc4502_43'] = ((200)/2) * 1e-3
ap_psc4502_43 = xt.LimitEllipse(a=env['rad_psc4502_43'],b=env['rad_psc4502_43'])

#PS.C.4504.43: 245/240  circle
#qfn56*2
env['rad_psc4504_43'] = ((240)/2) * 1e-3
ap_psc4504_43 = xt.LimitEllipse(a=env['rad_psc4504_43'],b=env['rad_psc4504_43'])

#AD_VCTUB0075: 148-1.5*2 circle
#qfn56*3
env['rad_vctub0075'] = ((148-(1.5*2))/2) * 1e-3
ap_vctub0075 = xt.LimitEllipse(a=env['rad_vctub0075'],b=env['rad_vctub0075'])

#AD_VCTUB0077: 159-2 orange circle
#qfn56
env['rad_vctub0077'] = ((159-2)/2) * 1e-3
ap_vctub0077 = xt.LimitEllipse(a=env['rad_vctub0077'],b=env['rad_vctub0077'])

############
# adding all types of qdn56 apertype together -> makes no sense since they will be at the same point 
i =0
all_types = [ap_mqdse0005, ap_vctub0028, ap_vctub0029,ap_vcdbg0001, ap_vcqak0001, 
             ap_vcqal0001, ap_vbcb0001, ap_vcdbh0001, ap_vctcm0001, ap_vcdcd0001, 
             ap_vctcn0001, ap_vctub0048,ap_pszmq0052, ap_pszvctub0022, ap_pszmcba0021,
             ap_psc3841_43, ap_psc3861_43, ap_psc3869_43, ap_psc4502_43, ap_psc4504_43,
              ap_vctub0075, ap_vctub0077]
all_names = ['ap_mqdse0005', 'ap_vctub0028', 'ap_vctub0029','ap_vcdbg0001', 'ap_vcqak0001', 
             'ap_vcqal0001', 'ap_vbcb0001', 'ap_vcdbh0001', 'ap_vctcm0001', 'ap_vcdcd0001', 
             'ap_vctcn0001',' ap_vctub0048','ap_pszmq0052',' ap_pszvctub0022',' ap_pszmcba0021',
             'ap_psc3841_43',' ap_psc3861_43',' ap_psc3869_43',' ap_psc4502_43',' ap_psc4504_43',
              'ap_vctub0075',' ap_vctub0077']
for aptype in all_types:

    name = all_names[i]
    insert_aper_2('dr.qfn56', aptype, name, env['l_qfc'])
    i+=1
    #name = f'{type=}'.split('=')[0]
    #line.insert_element('a.qfn56'+'..'+name[3:], type , at_s=tab['s', 'dr.qfn56'] + env['l_qfns'])

