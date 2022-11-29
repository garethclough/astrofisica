# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:33:14 2022

@author: Usuario
"""

import numpy as np
from astropy.modeling.models import Sersic1D
import matplotlib.pyplot as plt
from astropy .io. ascii import read

plt.figure()
plt.subplot(121, yscale='log')

data = read("NGC5772_i_no_header.txt") #Lectura de Número de Galaxia
xx = data["col1"]
yy = data["col2"]

xaxis = np.linspace (np.min(xx),np.max(xx),len(xx))

s1 = Sersic1D(amplitude=390.212, r_eff=9.4929)
s2 = Sersic1D(amplitude=337.699, r_eff=9.4929)
r=np.arange(0, 200, .01)
plt.ylim([0.1, 100000])




s1.n = 5
plt.plot(r, s1(r), color='r')

s2.n = 1
plt.plot(r, s2(r), color='b')

plt.plot(xx,yy, color='g')

plt.xlabel('Radius')
plt.ylabel('Surface Brightness')

#---------------------------------------------------------------------------------------------------------------------------------------------------

plt.subplot(122, yscale='log')

data = read("NGC5772_i_no_header.txt") #Lectura de Número de Galaxia
xx = data["col1"]
yy = data["col2"]

xaxis = np.linspace (np.min(xx),np.max(xx),len(xx))

s1 = Sersic1D(amplitude=200.212, r_eff=30)
s2 = Sersic1D(amplitude=337.699, r_eff=9.4929)
r=np.arange(0, 200, .01)
plt.ylim([0.1, 100000])




s1.n = 5
plt.plot(r, s1(r), color='r')

s2.n = 1
plt.plot(r, s2(r), color='b')

plt.plot(xx,yy, color='g')

plt.xlabel('Radius')
plt.ylabel('Surface Brightness')
plt.show()