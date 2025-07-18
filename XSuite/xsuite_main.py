# calls sequence & scenario files to make computations

import xobjects as xo
import xtrack as xt
import xpart as xp
import runpy
import numpy as np
import matplotlib.pyplot as plt

import sys
#sys.path.append('')

######################


#call files


'''
env = xt.Environment() 


env.call('./xsuite_seq_main.py') #sequence
env.call('../scenarios/xsuite_highenergy.py') #scenario
env.call('./xsuite_extras.py') #new elements - splitting
env.call('./xsuite_apertures.py') #apertures
env.call('./xsuite_new_apertures.py') #apertures



line = env['AD']
'''


# Call files (runs them in isolated namespaces, returns their variables)
seq_main_vars = runpy.run_path('/home/vtsianti/2409/scooling/studies/XSuite/xsuite_seq_main.py')
#scenario_vars = runpy.run_path('/home/vtsianti/2409/scooling/studies/XSuite/xsuite_highenergy.py')
#extras_vars = runpy.run_path('/home/vtsianti/2409/scooling/studies/XSuite/xsuite_extras.py')
#apertures_vars = runpy.run_path('/home/vtsianti/2409/scooling/studies/XSuite/xsuite_apertures.py')
#new_apertures_vars = runpy.run_path('/home/vtsianti/2409/scooling/studies/XSuite/xsuite_new_apertures.py')

# Assuming your line is defined inside one of these, like seq_main_vars
# If it was in xsuite_seq_main.py:
line = seq_main_vars['AD']  # replace 'AD' with the actual variable name if different

emitt_x = 50e-6
emitt_y = 50e-6
sig_p = 1e-2 # Dp/p = 1% = 0.01

#line.particle_ref = xp.Particles(mass0=xp.PROTON_MASS_EV, q0=-1, gamma0=3.9368)
line.particle_ref = xp.Particles(delta = sig_p)

# num_multipole_kicks: to fix x orbit variation
line.configure_bend_model(core='full', edge='full', num_multipole_kicks=50)
line.build_tracker()

line_table = line.get_table()#.show() 
line.survey().plot()
plt.show()
line.survey()#.show()


aper = line.check_aperture()


line.twiss_default['method'] = '4d'
#line.twiss_default['group_compound_elements'] = True

tw = line.twiss(strengths=True)#, betx=3.5886, bety=11.7745)
plt.close('all')


#put survey in a file
#sur = line.survey()
#pathout = '/home/nzikos/work/gitlab-mine/giulia/acc-models-ad/XSuite/compare/survey_from_xsuite.txt'
#file = open(pathout,'w') #output
#for row in sur.rows:
#    file.write(str(row) +'\n')
#file.close()
##########

#####################

# APERTURE GET & PLOT THINGS

# gets all aperture elements - named a.***
tab = line.get_table()

aper_elements = tab.rows['a.*']
l = len(aper_elements)

aper_points = []


for i in range(0, l):

    # TERRIBLE

    #iterates through all apertures
    curr_aper = aper_elements.rows[i]

    #a way to take the name so it can be accesed through the nvironmnet
    name = curr_aper.name[0]
    
    # a way to check if its ellipse or rect
    #different length of expression
    if(len(env[name].get_expr()) == 8): #is ellipse

        #append: s - type -  val1(a, x) val2(b, y)
        val1 = env[name].a
        val2 = env[name].b
        s = aper_elements.rows[i].s[0]

        aper_combo = [s, 'ellipse', val1, val2]

        #if(val1 < 0.1 and val2<0.08):
        aper_points.append(aper_combo)

    elif(len(env[name].get_expr()) == 9):#is rectangle


        #append: s - type -  val1(a, x) val2(b, y)
        val1 = env[name].max_x
        val2 = env[name].max_y
        s = aper_elements.rows[i].s[0]


        aper_combo = [s, 'rectangle', val1, val2]

        #if(val1 < 0.1 and val2<0.08):
        aper_points.append(aper_combo)
 
 

s = []
val1 = []
val2 =[]

for i in range(0, len(aper_points)):

    s.append(aper_points[i][0])
    val1.append([aper_points[i][2]])
    val2.append([aper_points[i][3]])

    #print('s: ', aper_points[i][0], 'aper1: ', aper_points[i][2], 'aper2: ', aper_points[i][3])

#BEAM SIZE

# Transverse normalized emittances
emitt_x = 200e-6
emitt_y = 200e-6
sig_p = 3e-2 # Dp/p = 1% = 0.01

sig_x = (emitt_x * tw.betx)**(1/2)
sig_y = (emitt_y * tw.bety)**(1/2)

#uncorelatted for general num
#sig_x_total = (sig_x**2 + (tw.dx* sig_p)**2 )**(1/2) 
#sig_y_total = (sig_y**2 + (tw.dy* sig_p)**2 )**(1/2) 

#actual acceptance limits
sig_x_total = sig_x + (tw.dx* sig_p)
sig_y_total = sig_y + (tw.dy* sig_p)

aper_problem = [] 

for i in range(0, len(s)): #runs for all apers

    index_tw = np.where(np.isclose(tw.s, s[i], atol=1e-3))
    ind = int(index_tw[0][0])

    if((val1[i]<= sig_x_total[ind]) or (val2[i]<= sig_y_total[ind])):

        #name - type - s - val1 - val2
        aper_problem.append([aper_elements.name[i], aper_elements.element_type[i], s[i], val1[i], val2[i]])

        #print('problem at: ', s[i], 'values: ', val1[i], val2[i])

#print(aper_problem)
#arr_problem = np.array(aper_problem)
print('N of problems: ', len(aper_problem))
for a in range(len(aper_problem)):
    print(aper_problem[a])

#plot
fig1, (sb1, sb2) = plt.subplots(2)
fig1.suptitle('apertures from main file')

sb1.plot(tw.s, sig_x)
sb1.plot(tw.s, sig_x_total)
sb1.plot(s, val1, '.')
#sb1.plot(arr_problem[:, 2],arr_problem[:,3], 'r')
sb1.legend([ 'sigx', ' sigx total', 'aper~x'])
sb1.set_ylim([0,0.2])

sb2.plot(tw.s, sig_y)
sb2.plot(tw.s, sig_y_total)
sb2.plot(s, val2, '.')
#sb2.plot(arr_problem[:, 2],arr_problem[:,4], 'r')
sb2.legend([ 'sigy', ' sigy total', 'aper~y'])
sb2.set_ylim([0,0.2])

plt.show()

#plot betxy, dxy, xy
fig1, (sb1, sb2, sb3) = plt.subplots(3)
fig1.suptitle('betXY, DXY, XY from xsuite')

sb1.plot(tw.s, tw.betx)
sb1.plot(tw.s, tw.bety)
sb1.legend(['BETA_X', 'BETA_Y'])

sb2.plot(tw.s, tw.dx)
sb2.plot(tw.s, tw.dy)
sb2.legend(['d_X', 'd_Y', ])

sb3.plot(tw.s, tw.x)
sb3.plot(tw.s, tw.y)
sb3.legend(['X', 'Y'])

plt.show()

#plot strengths
fig2, (sb4, sb5) = plt.subplots(2)
fig2.suptitle('k1l, k2l from xsuite')

sb4.plot(tw.s, tw.k1l, '.')
sb4.legend([ 'k1l'])

sb5.plot(tw.s, tw.k2l)
sb5.legend(['k2l'])

#plt.show()
