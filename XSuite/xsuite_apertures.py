#define aperture types
# set aperture-elements  front & back of actual elements
# addition to add apertures between splits and new elements

# cntrl F -> PROB TODO 

import numpy as np
import xtrack as xt
import matplotlib.pyplot as plt


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
=> in rect apertype do *2
'''

#define main apertures

#### Sextupoles

env['radiusinscribedcircle'] = 0.105078
ap_xrc = xt.LimitEllipse(a=env['radiusinscribedcircle'],b=env['radiusinscribedcircle'])

#### Quadrupoles

#QDS types
env['radiusqdschamber'] = 0.140/2
ap_qds = xt.LimitEllipse(a=env['radiusqdschamber'],b=env['radiusqdschamber'])

# dr.QDS15 & dr.QDS43
env['radiusqds15_qds43'] = 0.143/2
ap_qds15 = xt.LimitEllipse(a=env['radiusqds15_qds43'],b=env['radiusqds15_qds43'])
ap_qds43 = xt.LimitEllipse(a=env['radiusqds15_qds43'],b=env['radiusqds15_qds43'])

# DR.QDS55
env['halfwidthqds55'] = 0.113/2   
env['halfheightqds55'] = 0.108/2
ap_qds55 = xt.LimitEllipse(a=env['halfwidthqds55'],b=env['halfheightqds55'])

#QFNS types
env['radiusqfns'] = 0.140/2
ap_qfns = xt.LimitEllipse(a=env['radiusqfns'],b=env['radiusqfns'])

#DR.QFN56
env['radiusqfns56'] = 0.154/2
ap_qfns56 = xt.LimitEllipse(a=env['radiusqfns56'],b=env['radiusqfns56'])

env['radius_28_30'] = 0.154/2
ap_qdnec = xt.LimitEllipse(a=env['radius_28_30'],b=env['radius_28_30'])

#DR.QDN27 DR.QDN31
env['radius_27_31'] = 0.156/2
ap_qdn27 = xt.LimitEllipse(a=env['radius_27_31'],b=env['radius_27_31'])
ap_qdn31 = xt.LimitEllipse(a=env['radius_27_31'],b=env['radius_27_31'])

#dr.qfnec
env['radius29a29b'] = 0.172/2
ap_qfnec = xt.LimitEllipse(a=env['radius29a29b'],b=env['radius29a29b'])

#QFN types
env['halfwidthqfn'] = 0.150/2
env['halfheightqfn'] = 0.110/2
ap_qfn = xt.LimitEllipse(a=env['halfwidthqfn'],b=env['halfheightqfn'])

#QFC types
env['halfwidthqfc'] = 0.103/2
env['halfheightqfc'] = 0.075/2
ap_qfc = xt.LimitEllipse(a=env['halfwidthqfc'],b=env['halfheightqfc'])

#QDN types
env['radiusqdn'] = 0.140/2
ap_qdn = xt.LimitEllipse(a=env['radiusqdn'],b=env['radiusqdn'])

#DR.QDN05 DR.QDN33
env['radiusqdn_05_33'] = 0.137/2
ap_qdn05 = xt.LimitEllipse(a=env['radiusqdn_05_33'],b=env['radiusqdn_05_33'])
ap_qdn33 = xt.LimitEllipse(a=env['radiusqdn_05_33'],b=env['radiusqdn_05_33'])

#QDC types
env['halfwidthqdc53']  = 0.112 #/2
env['halfheightqdc53'] = 0.085 #/2
ap_qdc = xt.LimitRect(max_x=env['halfwidthqdc53'],max_y=env['halfheightqdc53'])

#QFW6
env['radius_qfw6'] = 0.223/2
ap_qfw6 = xt.LimitEllipse(a=env['radius_qfw6'],b=env['radius_qfw6'])

#QDW7
env['radius_qdw7'] = 0.223/2
ap_qdw7 = xt.LimitEllipse(a=env['radius_qdw7'],b=env['radius_qdw7'])

#QFW8
env['halfwidth_qfw8'] = 0.340 #/2
env['halfheight_qfw8'] = 0.080 #/2
ap_qfw8 = xt.LimitRect(max_x=env['halfwidth_qfw8'],max_y=env['halfheight_qfw8'])

#QDW9
env['radius_qdw9'] = 0.223/2
ap_qdw9 = xt.LimitEllipse(a=env['radius_qdw9'],b=env['radius_qdw9'])

#skew quads QSK14 and QSK43 
env['radiusskew'] = 0.156/2
ap_qsk14 = xt.LimitEllipse(a=env['radiusskew'],b=env['radiusskew'])
ap_qsk43 = xt.LimitEllipse(a=env['radiusskew'],b=env['radiusskew'])

#### Dipoles

#BHW
env['halfwidthbhw'] = 0.410  #/2
env['halfheightbhw'] = 0.1165 #/2
ap_bhw = xt.LimitRect(max_x=env['halfwidthbhw'], max_y=env['halfheightbhw']) # PROB is this ok?

#BHN
env['halfwidthbhn']  = 0.240 #/2
env['halfheightbhn'] = 0.107 #/2
ap_bhn = xt.LimitRect(max_x=env['halfwidthbhn'], max_y=env['halfheightbhn'])

#BHS
#! BHS has been visually inspected by A.S. and G.R. it has the same dimensions as BHN 
#! PROB (no drawing has been found)
env['halfwidthbhs']  = 'halfwidthbhn'
env['halfheightbhs'] = 'halfheightbhn'
ap_bhs = xt.LimitRect(max_x=env['halfwidthbhs'], max_y=env['halfheightbhs']) 

#BHN45
env['halfwidth_bhn45'] = 0.18826 #/2
env['halfheight_bhn45'] = 0.087 #/2
ap_bhn45 = xt.LimitRect(max_x=env['halfwidth_bhn45'], max_y=env['halfheight_bhn45']) 

# solenoids
ap_sec2910 = xt.LimitEllipse(a=0.056, b=0.036)

env['radiussolin'] = 0.09000
ap_scomp = xt.LimitEllipse(a=env['radiussolin'],b=env['radiussolin'])
#ap_scomp2607 = xt.LimitEllipse(a=env['radiussolin'],b=env['radiussolin'])
#ap_scomp3106 = xt.LimitEllipse(a=env['radiussolin'],b=env['radiussolin'])

# Stochastic cooling objects
env['halfwidth_kicker0307'] = 0.1068 #/2 !preivously 0.04970
env['halfheight_kicker0307'] = 0.0604 #/2; !preivously 0.03970
ap_khm0307 = xt.LimitRect(max_x=env['halfwidth_kicker0307'], max_y=env['halfheight_kicker0307']) 

ap_uvm3207 = xt.LimitRect(max_x=env['halfwidth_kicker0307'], max_y=env['halfheight_kicker0307']) 

env['halfwidth_kicker0407'] = 0.0626 #/2; !preivously 0.03975
env['halfheight_kicker0407'] = 0.1068 #/2; !preivously 0.04625
ap_kvm0407 = xt.LimitRect(max_x=env['halfwidth_kicker0407'], max_y=env['halfheight_kicker0407']) 

ap_uhm3107 = xt.LimitRect(max_x=env['halfwidth_kicker0407'], max_y=env['halfheight_kicker0407']) 

#drift
#random value?
env['size_drift'] = 0.99999 * 2 #in madx its plain number so i do *2
ap_smi = xt.LimitRect(max_x=env['size_drift'], max_y=env['size_drift']) 

######################

line = env['AD']
tab = line.get_table()
env = xt.get_environment()


#def give_me_data():
#    global aper_points
#    print('called data funct')
#    return aper_points


aper_points = []



global get_aper_point # Note: fixes "name is not defined" problem
#####################
def get_aper_point(ap_type, s):

    if (type(ap_type) == xt.beam_elements.apertures.LimitEllipse): #is ellipse

        #append: s - type -  val1(a, x) val2(b, y)
        val1 = ap_type.a
        val2 = ap_type.b

        aper_combo = [s, 'ellipse', val1, val2]
    
    elif (type(ap_type) == xt.beam_elements.apertures.LimitRect): #is rectangle
        
        #append: s - type -  val1(a, x) val2(b, y)
        val1 = ap_type.max_x
        val2 = ap_type.max_y

        aper_combo = [s, 'rectangle', val1, val2]

    return aper_combo
#####################


# to inserrt element in all of the splits - find the name of the splits
def insert_aper(element, ap_type, l_type):

    env = xt.get_environment()
    line = env['AD']
    tab = line.get_table()

    global aper_points


    s_array = tab.rows[element + '.*'].s
    l = len(s_array)

    if (l >= 1):
        for i in range(0, l):
            #insert before every element
            line.insert_element('a'+ element[2:]+'..'+str(i), ap_type, at_s=s_array[i])

            aper_combo = get_aper_point(ap_type, s_array[i])
            aper_points.append(aper_combo)

        #insert one after the last element
        line.insert_element('a'+ element[2:], ap_type, at_s=s_array[l-1]+ l_type)

        aper_combo = get_aper_point(ap_type, s_array[l-1]+ l_type)
        aper_points.append(aper_combo)

    else:
        line.insert_element('a'+ element[2:], ap_type, index=element)
        line.insert_element('a'+ element[2:], ap_type, at_s= s_array[0] + l_type)

        aper_combo = get_aper_point(ap_type, tab.rows[element].s)
        aper_points.append(aper_combo)

        aper_combo = get_aper_point(ap_type, s_array[0] + l_type)
        aper_points.append(aper_combo)

    #print('aper ppoint list: ', aper_points)

    return aper_points


# Insert the aperture upstream & downstream of the element - in all positions
insert_aper('dr.qds01.h1', ap_qds, env['l_qds']/2)

insert_aper('dr.qds01.h2', ap_qds, env['l_qds']/2)

insert_aper('dr.qds03', ap_qds, env['l_qds'])

insert_aper('dr.qds15', ap_qds15, env['l_qds'])

insert_aper('dr.qds43', ap_qds43, env['l_qds'])

insert_aper('dr.qds55', ap_qds55, env['l_qds'])

insert_aper('dr.qfn02', ap_qfns, env['l_qfns'])

insert_aper('dr.qfn56', ap_qfns56, env['l_qfns'])

insert_aper('dr.qdn27', ap_qdn27, env['l_qdnec'])

insert_aper('dr.qdn31', ap_qdn31, env['l_qdnec'])

insert_aper('dr.qdn05', ap_qdn05, env['l_qdn'])

insert_aper('dr.qdn33', ap_qdn33, env['l_qdn'])

insert_aper('dr.qsk1404', ap_qsk14, env['l_qsk'])

insert_aper('dr.qsk4308', ap_qsk43, env['l_qsk'])

insert_aper('dr.bhs52', ap_bhs, env['l_bhs'])

insert_aper('dr.qfc54', ap_qfc, env['l_qfc'])

insert_aper('dr.qdc53', ap_qdc, env['l_qdc'])

insert_aper('dr.bhn45', ap_bhn45, env['l_bhn'])

insert_aper('dr.sec2910', ap_sec2910, env['l_sec'])

insert_aper('dr.khm0307', ap_khm0307, 2.2) #PROB length 2.2 not set as var

insert_aper('dr.uvm3207', ap_uvm3207, env['l_uvm'])

insert_aper('dr.kvm0407', ap_kvm0407, 2.2) #PROB length 2.2 not set as var

insert_aper('dr.uhm3107', ap_uhm3107, env['l_uhm'])

#insert_aper('dr.smi5306', ap_smi, env['l_smi'])


all_scomp_type = ['dr.scomp2607','dr.scomp3106']
for element in all_scomp_type:
    
    insert_aper(element, ap_scomp, env['l_sol'])

all_qfn_type = ['dr.qfn04', 'dr.qfn14', 'dr.qfn16', 'dr.qfn26','dr.qfn32','dr.qfn42','dr.qfn44']
for element in all_qfn_type:
    insert_aper(element, ap_qfn, env['l_qfn'])

all_qfw6_type = ['dr.qfw06', 'dr.qfw12', 'dr.qfw18', 'dr.qfw24', 'dr.qfw34', 'dr.qfw40', 'dr.qfw46', 'dr.qfw52']
for element in all_qfw6_type:
    insert_aper(element, ap_qfw6, env['l_qfw6'])

all_qfw8_type = ['dr.qfw08', 'dr.qfw10', 'dr.qfw20', 'dr.qfw22','dr.qfw36','dr.qfw38','dr.qfw48','dr.qfw50']
for element in all_qfw8_type:
    insert_aper(element, ap_qfw8, env['l_qfw8'])

all_qdw7_type = ['dr.qdw07', 'dr.qdw11', 'dr.qdw19','dr.qdw23','dr.qdw35','dr.qdw39', 'dr.qdw51'] #'dr.qdw47': new apertures
for element in all_qdw7_type:
    insert_aper(element, ap_qdw7, env['l_qdw7'])

all_qdw9_type = ['dr.qdw09', 'dr.qdw21', 'dr.qdw37', 'dr.qdw49']
for element in all_qdw9_type:
    insert_aper(element, ap_qdw9, env['l_qdw9'])

all_qdn_type = ['dr.qdn13','dr.qdn17','dr.qdn25', 'dr.qdn41','dr.qdn45']
for element in all_qdn_type:
    insert_aper(element, ap_qdn, env['l_qdn'])

all_bhw_type = ['dr.bhw08','dr.bhw09', 'dr.bhw20', 'dr.bhw21','dr.bhw36', 'dr.bhw37','dr.bhw48','dr.bhw49']
for element in all_bhw_type:
    insert_aper(element, ap_bhw, env['l_bhw'])

all_bhn_type = ['dr.bhn05', 'dr.bhn06', 'dr.bhn11', 'dr.bhn12', 'dr.bhn17', 'dr.bhn18','dr.bhn23','dr.bhn24','dr.bhn33','dr.bhn34','dr.bhn39','dr.bhn40','dr.bhn46','dr.bhn51']
for element in all_bhn_type:
    insert_aper(element, ap_bhn, env['l_bhn'])

all_qdnec_type = ['dr.qdn28', 'dr.qdn30']
for element in all_qdnec_type:
    insert_aper(element, ap_qdnec, env['l_qdnec'])

all_xrc_type = ['dr.xrc1604', 'dr.xrc4108']
for element in all_xrc_type:
    insert_aper(element, ap_xrc, env['l_xrc'])

all_qfnec_type = ['dr.qfn29a', 'dr.qfn29b']
for element in all_qfnec_type:
    insert_aper(element, ap_qfnec, env['l_qfnec'])


#print(aper_points)

s = []
val1 = []
val2 =[]

for i in range(0, len(aper_points)):

    s.append(aper_points[i][0])
    val1.append([aper_points[i][2]])
    val2.append([aper_points[i][3]])

    #print('s: ', aper_points[i][0], 'aper1: ', aper_points[i][2], 'aper2: ', aper_points[i][3])


#give_me_data(aper_points)

#plot
fig1, (sb1, sb2) = plt.subplots(2)
fig1.suptitle('apertures from aper file')

sb1.plot(s, val1, '.')
sb1.legend([ '~x'])

sb2.plot(s, val2, '.')
sb2.legend([ '~y'])

#plt.show()

#################################

'''
old way to add - does not care for new names because of splits

line.insert_element('a.qds01.h1.s', ap_qds, index='dr.qds01.h1')
line.insert_element('a.qds01.h1.e', ap_qds, at_s=tab['s', 'dr.qds01.h1'] + env['l_qds']/2)

line.insert_element('a.qds01.h2.s', ap_qds, index='dr.qds01.h2')
line.insert_element('a.qds01.h2.e', ap_qds, at_s=tab['s', 'dr.qds01.h2'] + env['l_qds']/2)

line.insert_element('a.qdn05.s', ap_qdn05, index='dr.qdn05')
line.insert_element('a.qdn05.e', ap_qdn05, at_s=tab['s', 'dr.qdn05'] + env['l_qdn'])

line.insert_element('a.qsk1404.s', ap_qsk14, index='dr.qsk1404')
line.insert_element('a.qsk1404.e', ap_qsk14, at_s=tab['s', 'dr.qsk1404'] + env['l_qsk'])

line.insert_element('a.qsk4308.s', ap_qsk43, index='dr.qsk4308')
line.insert_element('a.qsk4308.e', ap_qsk43, at_s=tab['s', 'dr.qsk4308'] + env['l_qsk'])

line.insert_element('a.bhs52.s', ap_bhs, index='dr.bhs52')
line.insert_element('a.bhs52.e', ap_bhs, at_s=tab['s', 'dr.bhs52'] + env['l_bhs'])

#line.insert_element('a.qfc54.s', ap_qfc, index='dr.qfc54')
#line.insert_element('a.qfc54.e', ap_qfc, at_s=tab['s', 'dr.qfc54'] + env['l_qfc'])

line.insert_element('a.qdc53.s', ap_qdc, index='dr.qdc53')
line.insert_element('a.qdc53.e', ap_qdc, at_s=tab['s', 'dr.qdc53'] + env['l_qdc'])

line.insert_element('a.bhn45.s', ap_bhn45, index='dr.bhn45')
line.insert_element('a.bhn45.e', ap_bhn45, at_s=tab['s', 'dr.bhn45'] + env['l_bhn'])

line.insert_element('a.sec2910.s', ap_sec2910, index='dr.sec2910')
line.insert_element('a.sec2910.e', ap_sec2910, at_s=tab['s', 'dr.sec2910'] + env['l_sec'])

#line.insert_element('a.khm0307.s', ap_khm0307, index='dr.khm0307')
#line.insert_element('a.khm0307.e', ap_khm0307, at_s=tab['s', 'dr.khm0307'] + 2.2) #PROB length 2.2 not set as var
#
#line.insert_element('a.uvm3207.s', ap_uvm3207, index='dr.uvm3207')
#line.insert_element('a.uvm3207.e', ap_uvm3207, at_s=tab['s', 'dr.uvm3207'] + env['l_uvm'])
#
#line.insert_element('a.kvm0407.s', ap_kvm0407, index='dr.kvm0407')
#line.insert_element('a.kvm0407.e', ap_kvm0407, at_s=tab['s', 'dr.kvm0407'] + 2.2) #PROB length 2.2 not set as var
#
#line.insert_element('a.uhm3107.s', ap_uhm3107, index='dr.uhm3107')
#line.insert_element('a.uhm3107.e', ap_uhm3107, at_s=tab['s', 'dr.uhm3107'] + env['l_uhm'])


all_scomp_type = ['dr.scomp2607','dr.scomp3106']
for element in all_scomp_type:
    line.insert_element('a'+ element[2:]+'.s', ap_scomp, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_scomp, at_s=tab['s', element] + env['l_sol'])

all_qfns_type = ['dr.qfn02','dr.qfn56']
for element in all_qfns_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qfns, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qfns, at_s=tab['s', element] + env['l_qfns'])

all_qfn_type = ['dr.qfn04', 'dr.qfn14', 'dr.qfn16', 'dr.qfn26','dr.qfn32','dr.qfn42','dr.qfn44']
for element in all_qfn_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qfn, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qfn, at_s=tab['s', element] + env['l_qfn'])

all_qfw6_type = ['dr.qfw06', 'dr.qfw12', 'dr.qfw18', 'dr.qfw24', 'dr.qfw34', 'dr.qfw40', 'dr.qfw46', 'dr.qfw52']
for element in all_qfw6_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qfw6, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qfw6, at_s=tab['s', element] + env['l_qfw6'])

all_qds_type = ['dr.qds03', 'dr.qds15','dr.qds43', 'dr.qds55']
for element in all_qds_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qds, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qds, at_s=tab['s', element] + env['l_qds'])

all_qfw8_type = ['dr.qfw08', 'dr.qfw10', 'dr.qfw20', 'dr.qfw22','dr.qfw36','dr.qfw38','dr.qfw48','dr.qfw50']
for element in all_qfw8_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qfw8, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qfw8, at_s=tab['s', element] + env['l_qfw8'])

all_qdw7_type = ['dr.qdw07', 'dr.qdw11', 'dr.qdw19','dr.qdw23','dr.qdw35','dr.qdw39','dr.qdw47','dr.qdw51']
for element in all_qdw7_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qdw7, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qdw7, at_s=tab['s', element] + env['l_qdw7'])

all_qdw9_type = ['dr.qdw09', 'dr.qdw21', 'dr.qdw37', 'dr.qdw49']
for element in all_qdw9_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qdw9, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qdw9, at_s=tab['s', element] + env['l_qdw9'])

all_qdn_type = ['dr.qdn13','dr.qdn17','dr.qdn25', 'dr.qdn33', 'dr.qdn41','dr.qdn45']
for element in all_qdn_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qdn, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qdn, at_s=tab['s', element] + env['l_qdn'])

all_bhw_type = ['dr.bhw08','dr.bhw09', 'dr.bhw21', 'dr.bhw20','dr.bhw36', 'dr.bhw37','dr.bhw48','dr.bhw49']
for element in all_bhw_type:
   line.insert_element('a'+ element[2:]+'.s', ap_bhw, index=element)
   line.insert_element('a'+ element[2:]+'.e', ap_bhw, at_s=tab['s', element] + env['l_bhw'])

all_bhn_type = ['dr.bhn05', 'dr.bhn06', 'dr.bhn11', 'dr.bhn12', 'dr.bhn17', 'dr.bhn18','dr.bhn23','dr.bhn24','dr.bhn33','dr.bhn34','dr.bhn39','dr.bhn40','dr.bhn46','dr.bhn51']
for element in all_bhn_type:
    line.insert_element('a'+ element[2:]+'.s', ap_bhn, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_bhn, at_s=tab['s', element] + env['l_bhn'])

all_qdnec_type = ['dr.qdn27', 'dr.qdn28', 'dr.qdn30', 'dr.qdn31']
for element in all_qdnec_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qdnec, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qdnec, at_s=tab['s', element] + env['l_qdnec'])

all_xrc_type = ['dr.xrc1604', 'dr.xrc4108']
for element in all_xrc_type:
    line.insert_element('a'+ element[2:]+'.s', ap_xrc, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_xrc, at_s=tab['s', element] + env['l_xrc'])

all_qfnec_type = ['dr.qfn29a', 'dr.qfn29b']
for element in all_qfnec_type:
    line.insert_element('a'+ element[2:]+'.s', ap_qfnec, index=element)
    line.insert_element('a'+ element[2:]+'.e', ap_qfnec, at_s=tab['s', element] + env['l_qfnec'])
  '''  

'''
/* ******************* */
! Injection/Extraction kickers
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


# E-cooler related
#! Choosing the most restrictive of those two - Davide May 21
#// COL.EC_ENDS:    RCOLLIMATOR,XSIZE=0.056,YSIZE=0.036;
#//  -> installed at the extremeties of EC solenoid
#// COL.EC:         ECOLLIMATOR,XSIZE=0.07,YSIZE=0.05; !  will be removed


#not installed yet

/* ******************* */
! Stochastic cooling objects
!COL.KHM0307.W,     APERTYPE=RECTANGLE,   APERTURE={ 0.04970, 0.03970 };
!COL.KHM0307.N,     APERTYPE=RECTANGLE,   APERTURE={ 0.03175, 0.05365 };
!
!COL.KVM0407.W,     APERTYPE=RECTANGLE,   APERTURE={ 0.03975, 0.04625 };
!COL.KVM0407.N,     APERTYPE=RECTANGLE,   APERTURE={ 0.05385, 0.03000 };
!
!COL.UHM3107.W,     APERTYPE=RECTANGLE,   APERTURE={ 0.04920, 0.03950 };
!COL.UHM3107.N,     APERTYPE=RECTANGLE,   APERTURE={ 0.03630, 0.05340 };
!

!COL.UVM3207.W,     APERTYPE=RECTANGLE,   APERTURE={ 0.03950, 0.04640 };
!COL.UVM3207.N,     APERTYPE=RECTANGLE,   APERTURE={ 0.05340, 0.03020 };
!

/* ******************* */
! PROB Unknown....  DAVIDE - MAY 2021

COL.SSVI: ECOLLIMATOR,XSIZE=0.155,YSIZE=0.055;
COL.SSVI, APERTYPE=ELLIPSE, APERTURE={ 0.15500, 0.05500 };
!
COL.SSVE: ECOLLIMATOR,XSIZE=0.155,YSIZE=0.035;
COL.SSVE, APERTYPE=ELLIPSE, APERTURE={ 0.15500, 0.03500 };
!
COL.SSHI: ECOLLIMATOR,XSIZE=0.055,YSIZE=0.155;
COL.SSHI, APERTYPE=ELLIPSE, APERTURE={ 0.05500, 0.15500 };
!
COL.SSHE: ECOLLIMATOR,XSIZE=0.035,YSIZE=0.155;
COL.SSHE, APERTYPE=ELLIPSE, APERTURE={ 0.03500, 0.15500 };

// COL.PU_QF4:     RCOLLIMATOR,XSIZE=0.0518,YSIZE=0.0293;
COL.PU_QF4,        APERTYPE=RECTANGLE,   APERTURE={ 0.05180, 0.02930 };

// COL.PU_EC:      ECOLLIMATOR,XSIZE=0.077,YSIZE=0.077;
COL.PU_EC,         APERTYPE=ELLIPSE,     APERTURE={ 0.07700, 0.07700 };

// COL.PU_QD1:     ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.PU_QD1,        APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.PU_QF2:     ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.PU_QF2,        APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.PU_QD3:     ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.PU_QD3,        APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.PU_QD5:     ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.PU_QD5,        APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.USV0205.N:  ECOLLIMATOR,XSIZE=0.0525,YSIZE=0.0295;
COL.USV0205.N,     APERTYPE=ELLIPSE,     APERTURE={ 0.05250, 0.02950 };

// COL.USV0205.W:  ECOLLIMATOR,XSIZE=0.041,YSIZE=0.0365;
COL.USV0205.W,     APERTYPE=ELLIPSE,     APERTURE={ 0.04100, 0.03650 };

// COL.USH0207.W:  ECOLLIMATOR,XSIZE=0.04,YSIZE=10.0;
COL.USH0207.W,     APERTYPE=ELLIPSE,     APERTURE={ 0.04000, 0.99999 };

// COL.USH0207.N:  ECOLLIMATOR,XSIZE=0.0295,YSIZE=0.045;
COL.USH0207.N,     APERTYPE=ELLIPSE,     APERTURE={ 0.02950, 0.04500 };

// COL.USL4104.N:  ECOLLIMATOR,XSIZE=0.036,YSIZE=0.036;
COL.USL4104.N,     APERTYPE=ELLIPSE,     APERTURE={ 0.03600, 0.03600 };

// COL.DAV1605.N:  ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.DAV1605.N,     APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.DAV1605.W:  ECOLLIMATOR,XSIZE=10.,YSIZE=0.0409;
COL.DAV1605.W,     APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.04090 };

// COL.DAH1607.W:  ECOLLIMATOR,XSIZE=10.,YSIZE=10.;
COL.DAH1607.W,     APERTYPE=ELLIPSE,     APERTURE={ 0.99999, 0.99999 };

// COL.DAH1607.N:  ECOLLIMATOR,XSIZE=0.03675,YSIZE=10.;
COL.DAH1607.N,     APERTYPE=ELLIPSE,     APERTURE={ 0.03675, 0.99999 };

'''
