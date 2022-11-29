# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:33:14 2022

@author: Usuario
"""

import numpy as np
from astropy.modeling.models import Sersic1D
import matplotlib.pyplot as plt
from astropy .io. ascii import read
import matplotlib.patches as mpatches

plt.figure()
plt.subplot(111, yscale='log')

data = read("NGC5772_i_no_header.txt") #Lectura de Número de Galaxia
xx = data["col1"]
yy = data["col2"]

red_patch = mpatches.Patch(color='red', label='The red data')

s1 = Sersic1D(amplitude=390.212, r_eff=9.4929)
s2 = Sersic1D(amplitude=337.699, r_eff=9.4929)
r=np.arange(0, 200, .01)
plt.ylim([0.1, 100000])




s1.n = 5
l1, = plt.plot(r, s1(r), color='r')

s2.n = 1
l2, = plt.plot(r, s2(r), color='b')

l3, = plt.plot(xx,yy, color='g')

plt.legend([l1, l2, l3],["Sersic", "Exponential", "Observed"])

plt.xlabel('Radius')
plt.ylabel('Surface Brightness')
plt.savefig('multiple-model-comparison.png')
plt.show()
