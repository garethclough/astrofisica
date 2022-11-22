import numpy as np
from astropy.modeling.models import Sersic1D
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(111)
s1 = Sersic1D(amplitude=52.2309, r_eff=51.2196)
r=np.arange(0, 100, .01)

s1.n = 3.86392
plt.plot(r, s1(r), color=str(float(3.86) / 15))

plt.axis([0, 1e5, 0, 1e5])
plt.xlabel('log Radius')
plt.ylabel('log Surface Brightness')
plt.text(.25, 1.5, 'n=1')
plt.text(.25, 300, 'n=10')
plt.xticks([])
plt.yticks([])
plt.savefig('sersic.png')
