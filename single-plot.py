# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:49:16 2022

@author: Usuario
"""


from astropy .io. ascii import read
import matplotlib . pyplot as plt
import numpy as np
import os

data = read("NGC5772_i_no_header.txt") #Lectura de Número de Galaxia
xx = data["col1"]
yy = data["col2"]

xaxis = np.linspace (np.min(xx),np.max(xx),len(xx))

plt.plot(xx,yy)
plt.show()