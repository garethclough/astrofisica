from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import sys

def radial_profile(data, center):
    x, y = np.indices((data.shape))
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    r = r.astype(int)

    tbin = np.bincount(r.ravel(), data.ravel())
    nr = np.bincount(r.ravel())
    radialprofile = tbin / nr
    return radialprofile

if len(sys.argv) != 5:
    print('Specify 4 arguments: observed.fits exponential.fits sersic.fits exp_and_sersic.fits')
    sys.exit()

observed_file = sys.argv[1]
exp_file = sys.argv[2]
serc_file = sys.argv[3]
comb_file = sys.argv[4]

print('using observed file ' + observed_file)

minorLocator = AutoMinorLocator()




fitsFile = fits.open(exp_file)
fitsFile.info()
img = fitsFile[0].data
img[np.isnan(img)] = 0

center = (278,342)
print(center)
print(img.shape)

rad_profile = radial_profile(img, center)

fig, ax = plt.subplots()
plt.plot(rad_profile[0:500], 'b')

#ax.xaxis.set_minor_locator(minorLocator)

#plt.tick_params(which='both', width=2)
#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=4, color='r')
#plt.grid()
ax.set_ylabel("counts")
ax.set_xlabel("radius (pixels)")
#plt.grid(which="minor")
#plt.show()
#plt.savefig('model-6-plot.png')

fitsFile = fits.open(observed_file)
fitsFile.info()


img = fitsFile[0].data
img[np.isnan(img)] = 0
rad_profile = radial_profile(img, center)
plt.plot(rad_profile[0:500], 'r')

#ax.xaxis.set_minor_locator(minorLocator)

#plt.tick_params(which='both', width=2)
#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=4, color='r')
#plt.grid()
#ax.set_ylabel("Y")
#ax.set_xlabel("Pixels")
#plt.grid(which="minor")
plt.show()
#plt.savefig('NGC5772_i-plot.png')
