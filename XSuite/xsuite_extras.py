#way to add things that are on top of each other
# monitors kickers

import numpy as np
import xtrack as xt

env = xt.get_environment()

env.vars.default_to_zero = True

line = env['AD']
#tab = line.get_table()


#### BPMs

# HMonitors

env['l_hmonitor'] = 0.
hmonitor = xt.Drift(length = env['l_hmonitor'])

line.insert_element('dr.uhz0200', hmonitor, at_s =  2.939500)
line.insert_element('dr.uhz0400', hmonitor, at_s =  9.440000)
line.insert_element('dr.uhz0600', hmonitor, at_s = 16.115800)
line.insert_element('dr.uhz0702', hmonitor, at_s = 20.388100)
line.insert_element('dr.uhz0902', hmonitor, at_s = 26.489600)
line.insert_element('dr.uhz1100', hmonitor, at_s = 31.820100)
line.insert_element('dr.uhz1202', hmonitor, at_s = 36.092400)
line.insert_element('dr.uhz1402', hmonitor, at_s = 42.768200)
line.insert_element('dr.uhz1602', hmonitor, at_s = 48.448200)
line.insert_element('dr.uhz1800', hmonitor, at_s = 55.124000)
line.insert_element('dr.uhz1902', hmonitor, at_s = 59.396300)
line.insert_element('dr.uhz2100', hmonitor, at_s = 64.726800)
line.insert_element('dr.uhz2300', hmonitor, at_s = 70.828300)
line.insert_element('dr.uhz2402', hmonitor, at_s = 75.100600)
line.insert_element('dr.uhz2600', hmonitor, at_s = 81.056400)
line.insert_element('dr.uhz2902', hmonitor, at_s = 87.406140)
line.insert_element('dr.uhz2909', hmonitor, at_s = 90.565400)
line.insert_element('dr.uhz2911', hmonitor, at_s = 91.867400)
line.insert_element('dr.uhz2920', hmonitor, at_s = 95.026660)
line.insert_element('dr.uhz3200', hmonitor, at_s = 101.376400)
line.insert_element('dr.uhz3400', hmonitor, at_s = 107.332200)
line.insert_element('dr.uhz3502', hmonitor, at_s = 111.604500)
line.insert_element('dr.uhz3702', hmonitor, at_s = 117.706000)
line.insert_element('dr.uhz3900', hmonitor, at_s = 123.036500)
line.insert_element('dr.uhz4002', hmonitor, at_s = 127.308800)
line.insert_element('dr.uhz4202', hmonitor, at_s = 133.984600)
line.insert_element('dr.uhz4400', hmonitor, at_s = 139.664600)
line.insert_element('dr.uhz4600', hmonitor, at_s = 146.340400)
line.insert_element('dr.uhz4702', hmonitor, at_s = 150.612700)
line.insert_element('dr.uhz4900', hmonitor, at_s = 155.943200)
line.insert_element('dr.uhz5100', hmonitor, at_s = 162.044700)
line.insert_element('dr.uhz5202', hmonitor, at_s = 166.317000)
line.insert_element('dr.uhz5402', hmonitor, at_s = 173.346800)
line.insert_element('dr.uhz5602', hmonitor, at_s = 179.493300)

# V monitors
env['l_vmonitor'] = 0.
vmonitor = xt.Drift(length = env['l_vmonitor'])

line.insert_element('dr.uvt0300', vmonitor, at_s =   6.960500)
line.insert_element('dr.uvt0502', vmonitor, at_s =  13.360500)
line.insert_element('dr.uvt0700', vmonitor, at_s =  19.617100)
line.insert_element('dr.uvt0900', vmonitor, at_s =  25.718600)
line.insert_element('dr.uvt1102', vmonitor, at_s =  32.591100)
line.insert_element('dr.uvt1300', vmonitor, at_s =  38.847700)
line.insert_element('dr.uvt1500', vmonitor, at_s =  45.247700)
line.insert_element('dr.uvt1702', vmonitor, at_s =  52.368700)
line.insert_element('dr.uvt1900', vmonitor, at_s =  58.625300)
line.insert_element('dr.uvt2102', vmonitor, at_s =  65.497800)
line.insert_element('dr.uvt2302', vmonitor, at_s =  71.599300)
line.insert_element('dr.uvt2500', vmonitor, at_s =  77.855900)
line.insert_element('dr.uvt2802', vmonitor, at_s =  87.110540)
line.insert_element('dr.uvt2909', vmonitor, at_s =  90.565400)
line.insert_element('dr.uvt2911', vmonitor, at_s =  91.867400)
line.insert_element('dr.uvt3000', vmonitor, at_s =  95.322260)
line.insert_element('dr.uvt3302', vmonitor, at_s = 104.576900)
line.insert_element('dr.uvt3500', vmonitor, at_s = 110.833500)
line.insert_element('dr.uvt3700', vmonitor, at_s = 116.935000)
line.insert_element('dr.uvt3902', vmonitor, at_s = 123.807500)
line.insert_element('dr.uvt4100', vmonitor, at_s = 130.064100)
line.insert_element('dr.uvt4300', vmonitor, at_s = 136.464100)
line.insert_element('dr.uvt4502', vmonitor, at_s = 143.585100)
line.insert_element('dr.uvt4700', vmonitor, at_s = 149.841700)
line.insert_element('dr.uvt4902', vmonitor, at_s = 156.714200)
line.insert_element('dr.uvt5102', vmonitor, at_s = 162.815700)
line.insert_element('dr.uvt5300', vmonitor, at_s = 169.076950)
line.insert_element('dr.uvt5502', vmonitor, at_s = 176.193300)
line.insert_element('dr.uvt0100', vmonitor, at_s = 182.072300)

#### Kickers 

#### H Kicks

# DBname: PXMCXABCIP -> dr.dhz2908 & dr.dhz2913
env['dr.dhz2908_i'] = 0
dhz2908 = xt.Multipole(knl=[-(env['dr.dhz2908_i']* 0.035/5) * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dhz2908', dhz2908 , at_s = 89.266400)

env['dr.dhz2913_i'] = 0
dhz2913 = xt.Multipole(knl=[-(env['dr.dhz2913_i']* 0.035/5) * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dhz2913', dhz2908 , at_s = 93.166400)

# DBname: PXMCXBBWAP
dhz0204 = xt.Multipole(knl = [0])
line.insert_element('dr.dhz0204', dhz0204 , at_s = 5.240000)

# DBname: PXMCXBBWAP
dhz5404 = xt.Multipole(knl = [0])
line.insert_element('dr.dhz5404', dhz5404 , at_s = 174.000800)

#env['aux.elm.at'] = 14.750650
bhztr05 = xt.Multipole(knl = [env['k.bhztr05.06']])
line.insert_element('dr.bhztr05', bhztr05 , at_s = 14.750650 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 18.251950
bhztr06 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr06', bhztr06 , at_s = 18.251950 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 24.353450
bhztr08 = xt.Multipole(knl = [env['k.bhztrim'] + env['k.bhztr08.09']])
line.insert_element('dr.bhztr08', bhztr08 , at_s = 24.353450 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 27.854750
bhztr09 = xt.Multipole(knl = [env['k.bhztrim']])
line.insert_element('dr.bhztr09', bhztr09 , at_s = 27.854750 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 33.956250
bhztr11 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr11', bhztr11 , at_s = 33.956250 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 37.457550
bhztr12 = xt.Multipole(knl = [env['k.bhztr11.12']])
line.insert_element('dr.bhztr12', bhztr12 , at_s = 37.457550 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 53.758850
bhztr17 = xt.Multipole(knl = [env['k.bhztr17.18']])
line.insert_element('dr.bhztr17', bhztr17 , at_s = 53.758850 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 57.260150
bhztr18 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr18', bhztr18 , at_s = 57.260150 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 63.361650
bhztr20 = xt.Multipole(knl = [env['k.bhztrim'] + env['k.bhztr20.21']])
line.insert_element('dr.bhztr20', bhztr20 , at_s = 63.361650 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 66.862950
bhztr21 = xt.Multipole(knl = [env['k.bhztrim']])
line.insert_element('dr.bhztr21', bhztr21 , at_s = 66.862950 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 72.964450
bhztr23 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr23', bhztr23 , at_s = 72.964450 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 76.465750
bhztr24 = xt.Multipole(knl = [env['k.bhztr23.24']])
line.insert_element('dr.bhztr24', bhztr24 , at_s = 76.465750 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 105.967050
bhztr33 = xt.Multipole(knl = [env['k.bhztr33.34']])
line.insert_element('dr.bhztr33', bhztr33 , at_s = 105.967050 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 109.468350
bhztr34 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr34', bhztr34 , at_s = 109.468350 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 115.569850
bhztr36 = xt.Multipole(knl = [env['k.bhztrim']])
line.insert_element('dr.bhztr36', bhztr36 , at_s = 115.569850 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 119.071150
bhztr37 = xt.Multipole(knl = [env['k.bhztrim'] + env['k.bhztr36.37']])  
line.insert_element('dr.bhztr37', bhztr37 , at_s = 119.071150 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 125.172650
bhztr39 = xt.Multipole(knl = [0])  
line.insert_element('dr.bhztr39', bhztr39 , at_s = 125.172650 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 128.673950
bhztr40 = xt.Multipole(knl = [env['k.bhztr39.40']]) 
line.insert_element('dr.bhztr40', bhztr40 , at_s = 128.673950 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 144.975250
bhztr45 = xt.Multipole(knl = [env['k.bhztr45.46']]) 
line.insert_element('dr.bhztr45', bhztr45 , at_s = 144.975250 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 148.476550
bhztr46 = xt.Multipole(knl = [0]) 
line.insert_element('dr.bhztr46', bhztr46 , at_s = 148.476550 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 154.578050
bhztr48 = xt.Multipole(knl = [env['k.bhztrim']])
line.insert_element('dr.bhztr48', bhztr48 , at_s = 154.578050 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 158.079350
bhztr49 = xt.Multipole(knl = [env['k.bhztrim'] + env['k.bhztr48.49']])
line.insert_element('dr.bhztr49', bhztr49 , at_s = 158.079350 - env['l_bhw']/2 + 0.975650)

#env['aux.elm.at'] = 164.180850
bhztr51 = xt.Multipole(knl = [0])
line.insert_element('dr.bhztr51', bhztr51 , at_s = 164.180850 - env['l_bhn']/2 + 0.975650)

#env['aux.elm.at'] = 167.682150
bhztr52 = xt.Multipole(knl = [env['k.bhztr51.52']])
line.insert_element('dr.bhztr52', bhztr52 , at_s = 167.682150 - env['l_bhs']/2 + 0.975650)


#### V Kicks

# DBname: PXMCXAACAP
dvt1304 = xt.Multipole(ksl = [0])
line.insert_element('dr.dvt1304', dvt1304 , at_s = 39.986200)

# DBname: PXMCXBBWAP
dvt0208 = xt.Multipole(ksl = [0])
line.insert_element('dr.dvt0208', dvt0208 , at_s = 5.825000)

# DBname: PXMCXBBWAP
dvt5408 = xt.Multipole(ksl = [0])
line.insert_element('dr.dvt5408', dvt5408 , at_s = 174.673300)

# DBname: PXMCXAACAP
dvt1608 = xt.Multipole(ksl = [0])
line.insert_element('dr.dvt1608', dvt1608 , at_s = 51.163000)

# DBname: PXMCXAACAP
dvt4408 = xt.Multipole(ksl = [0])
line.insert_element('dr.dvt4408', dvt4408 , at_s = 142.438600)

# DBname: PXMCHAAWAP -> dr.dvt2608 & dr.dvt3105
env['dr.dvt2608_i'] = 0
dvt2608 = xt.Multipole(ksl = [env['dr.dvt2608_i']* (0.025/15) * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dvt2608', dvt2608 , at_s = 84.946400)

env['dr.dvt3105_i'] = 0
dvt3105 = xt.Multipole(ksl = [env['dr.dvt3105_i']* (0.025/15) * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dvt3105', dvt3105 , at_s = 97.486400)


#### Kicks

# DBname: PXMCCAVWAP -> dr.dhv2904 & dr.dhv2917
env['dr.dhv2904_hi'] = 0
env['dr.dhv2904_vi'] = 0
dhv2904 = xt.Multipole(knl=[-(env['dr.dhv2904_hi']* 0.028/15) * (1/(3.3356*env['momentum']))],
                       ksl=[env['dr.dhv2904_vi'] * 0.028/15 * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dhv2904', dhv2904 , at_s = 88.586400)

env['dr.dhv2917_hi'] = 0
env['dr.dhv2917_vi'] = 0
dhv2917 = xt.Multipole(knl=[-(env['dr.dhv2917_hi']* 0.028/15) * (1/(3.3356*env['momentum']))],
                       ksl=[env['dr.dhv2917_vi'] * 0.028/15 * (1/(3.3356*env['momentum']))])
line.insert_element('dr.dhv2917', dhv2917 , at_s = 93.846400)


#### T Kicks

# there are T kickers with length installed in the main sequence 
# they do not overlap with anything

hvcor01 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor01', hvcor01 , at_s = 0)

hvcor04 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor04', hvcor04 , at_s = 9.8)

hvcor05 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor05', hvcor05 , at_s = 13.0)

hvcor13 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor13', hvcor13 , at_s = 39.2082) #38.8384 + 0.7396/2

hvcor14 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor14', hvcor14 , at_s = 42.4082) #42.042150000 + 0.7321/2

hvcor16 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor16', hvcor16 , at_s = 48.8082) #48.442150 + 0.7321/2

hvcor17 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor17', hvcor17 , at_s = 52.0082) #51.6384 + 0.7396/2

hvcor25 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor25', hvcor25 , at_s = 78.2164) #77.8466 + 0.7396/2

hvcor26 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor26', hvcor26 , at_s = 81.4164) #81.050350 + 0.7321/2

hvcor32 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor32', hvcor32 , at_s = 101.0164) #100.650350 + 0.7321/2

hvcor33 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor33', hvcor33 , at_s = 104.2164) #103.8466 + 0.7396/2

hvcor41 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor41', hvcor41 , at_s = 130.4246) #130.054800 + 0.7396/2

hvcor42 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor42', hvcor42 , at_s = 133.6246) # 133.258550 + 0.7321/2

hvcor44 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor44', hvcor44 , at_s = 140.0246) # 139.658550 + 0.7321/2

hvcor45 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor45', hvcor45 , at_s = 143.2246) #142.854800 + 0.7396/2

hvcor53 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor53', hvcor53 , at_s = 169.4328) #169.063000 + 0.7396/2

#env['aux.elm.at'] = 3.300000
hvcor02 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor02', hvcor02 , at_s = 3.300000 - env['l_qfns']/2 + 0.355300)

#env['aux.elm.at'] = 6.600000
hvcor03 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor03', hvcor03 , at_s = 6.600000 - env['l_qds']/2 + 0.355300)

#env['aux.elm.at'] = 16.501300
hvcor06 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor06', hvcor06 , at_s = 16.501300 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 20.002600
hvcor07 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor07', hvcor07 , at_s = 20.002600 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 22.602800
hvcor08 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor08', hvcor08 , at_s = 22.602800 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 26.104100
hvcor09 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor09', hvcor09 , at_s = 26.104100 - env['l_qdw9']/2 + 0.382050)

#env['aux.elm.at'] = 29.60540
hvcor10 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor10', hvcor10 , at_s = 29.60540 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 32.205600
hvcor11 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor11', hvcor11 , at_s = 32.205600 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 35.706900
hvcor12 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor12', hvcor12 , at_s = 35.706900 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 45.608200
hvcor15 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor15', hvcor15 , at_s = 45.608200 - env['l_qds']/2 + 0.355300)

#env['aux.elm.at'] = 55.509500
hvcor18 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor18', hvcor18 , at_s = 55.509500 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 59.010800
hvcor19 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor19', hvcor19 , at_s = 59.010800 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 61.611000
hvcor20 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor20', hvcor20 , at_s = 61.611000 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 65.11230
hvcor21 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor21', hvcor21 , at_s = 65.11230 - env['l_qdw9']/2 + 0.382050)

#env['aux.elm.at'] = 68.61360
hvcor22 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor22', hvcor22 , at_s = 68.61360 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 71.213800
hvcor23 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor23', hvcor23 , at_s = 71.213800 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 74.715100
hvcor24 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor24', hvcor24 , at_s = 74.715100 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 85.776800
hvcor27 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor27', hvcor27 , at_s = 85.776800 - env['l_qdnec']/2 + 0.359800)

#env['aux.elm.at'] = 86.729540
hvcor28 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor28', hvcor28 , at_s =  86.729540 - env['l_qdnec']/2 + 0.359800)

#env['aux.elm.at'] = 87.785840
hvcor29a = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor29a', hvcor29a , at_s = 87.785840 - env['l_qfnec']/2 + 0.354500)

#env['aux.elm.at'] = 94.646960
hvcor29b= xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor29b', hvcor29b , at_s = 94.646960 - env['l_qfnec']/2 + 0.354500)

#env['aux.elm.at'] = 95.703260
hvcor30 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor30', hvcor30 , at_s = 95.703260 - env['l_qdnec']/2 + 0.359800)

#env['aux.elm.at'] = 96.656000
hvcor31 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor31', hvcor31 , at_s = 96.656000 - env['l_qdnec']/2 + 0.359800)

#env['aux.elm.at'] = 107.717700
hvcor34 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor34', hvcor34 , at_s = 107.717700 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 111.219000
hvcor35 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor35', hvcor35 , at_s = 111.219000 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 113.819200
hvcor36 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor36', hvcor36 , at_s = 113.819200 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 117.320500
hvcor37 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor37', hvcor37 , at_s = 117.320500 - env['l_qdw9']/2 + 0.382050)

#env['aux.elm.at'] = 120.821800
hvcor38 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor38', hvcor38 , at_s = 120.821800 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 123.42200
hvcor39 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor39', hvcor39 , at_s = 123.42200 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 126.92330
hvcor40 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor40', hvcor40 , at_s = 126.92330 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 136.82460
hvcor43 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor43', hvcor43 , at_s = 136.82460 - env['l_qds']/2 + 0.355300)

#env['aux.elm.at'] = 146.725900
hvcor46 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor46', hvcor46 , at_s = 146.725900 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 150.227200
hvcor47 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor47', hvcor47 , at_s = 150.227200 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 152.827400
hvcor48 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor48', hvcor48 , at_s = 152.827400 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 156.328700
hvcor49 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor49', hvcor49 , at_s = 156.328700 - env['l_qdw9']/2 + 0.382050)

#env['aux.elm.at'] = 159.830000
hvcor50 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor50', hvcor50 , at_s = 159.830000 - env['l_qfw8']/2 + 0.374700)

#env['aux.elm.at'] = 162.430200
hvcor51 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor51', hvcor51 , at_s = 162.430200 - env['l_qdw7']/2 + 0.374950)

#env['aux.elm.at'] = 165.931500
hvcor52 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor52', hvcor52 , at_s = 165.931500 - env['l_qfw6']/2 + 0.378400)

#env['aux.elm.at'] = 172.632800
hvcor54 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor54', hvcor54 , at_s = 172.632800 - env['l_qfc']/2 + 0.366050)

#env['aux.elm.at'] = 175.832800
hvcor55 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor55', hvcor55 , at_s = 175.832800 - env['l_qds']/2 + 0.355300)

#env['aux.elm.at'] = 179.132800
hvcor56 = xt.Multipole(knl=[-0.], ksl=[0.])
line.insert_element('dr.hvcor56', hvcor56 , at_s = 179.132800 - env['l_qfns']/2 + 0.355300)


#### Electron cooler toroids - T kickers

env['th.tkick'] = env['on_eckick'] * (0.00497 * env['dr.sec2910_i']/ (400 * env['momentum']))
tec2908 = xt.Multipole(length = 0, knl=[-env['th.tkick']], ksl=[0.])
line.insert_element('dr.tec2908', tec2908 , at_s = 90.076400)

tec2912 = xt.Multipole(length = 0, knl=[env['th.tkick']], ksl=[0.])
line.insert_element('dr.tec2912', tec2912 , at_s = 92.356400)


#### Stochastic Cooling Pus - T kickers
# PROB at_s has refer=left - value from madx is refer=center
# changing now given s to: s -l/2 for elements with length
khm0307 = xt.Multipole(length = 2.2, knl=[-0.])
line.insert_element('dr.khm0307', khm0307 , at_s = 7.0975) #8.1975) #7.097500 + 1.1

kvm0407 = xt.Multipole(length = 2.2, ksl=[0.])
line.insert_element('dr.kvm0407', kvm0407 , at_s = 10.2975) #11.397499) #10.297500 + 1.1


#### Tune Measurement system - T Kickers

dav1605 = xt.Multipole(length = 0., knl=[-0.])
line.insert_element('dr.dav1605', dav1605 , at_s = 49.8332) #49.698200 + 0.270/2

dah1607 = xt.Multipole(length = 0., ksl=[0.])
line.insert_element('dr.dah1607', dah1607 , at_s = 51.2082) #48.808200 + (52.008200 - 48.808200)*(3/4)


#### Implement kicks due to IPM being ON - T Kicks

bipm4207_kick = xt.Multipole(ksl=[env['ipm_on']*0.001], knl=[-0.])
line.insert_element('dr.bipm4207_kick', bipm4207_kick , at_s = 134.8106) #133.624600 + 0.732/2 + 1*0.82

bipm4208_kick = xt.Multipole(ksl=[0.], knl=[-env['ipm_on']*0.001])
line.insert_element('dr.bipm4208_kick', bipm4208_kick , at_s = 135.6306) #133.624600 + 0.732/2 + 2*0.82


#### Markers

marker = xt.Marker()
line.insert_element('dr.sec2910.s', marker , at_s = 89.691400)
line.insert_element('dr.sec2910.m', marker , at_s = 91.216400)
line.insert_element('dr.sec2910.e', marker , at_s = 92.741400)

# was in main sequence bu tcrashed because of overlap - moved here
line.insert_element('dr.mid.ad', marker , at_s = 91.216400) #mid AD

  
        


  
