import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling.models import Sersic1D

xArray = [];
yArray = [];
sxArray = [];
syArray = [];
exArray = [];
eyArray = [];

s1 = Sersic1D(amplitude=15, r_eff=25)
e1 = Sersic1D(amplitude=100, r_eff=25, n=1)

with open('NGC5772_i.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        if count:
            index = count - 1
            lineArray = line.split()
            x = float(lineArray[0])
            y = float(lineArray[1])
            print(str(x) + ' ' + str(y))
            xArray.append(x)
            yArray.append(y)
            sxArray.append(x)
            syArray.append(s1(x))
            exArray.append(x)
            eyArray.append(e1(x))

        count += 1
plt.yscale('log')
plt.plot(xArray, yArray,'r--')
plt.plot(sxArray, syArray)
plt.plot(exArray, eyArray)
plt.savefig('NGC5772_i-txt.png')
plt.show()
