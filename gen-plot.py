from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

minorLocator = AutoMinorLocator()

def radial_profile(data, center):
    x, y = np.indices((data.shape))
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    r = r.astype(int)

    tbin = np.bincount(r.ravel(), data.ravel())
    nr = np.bincount(r.ravel())
    radialprofile = tbin / nr
    return radialprofile


fitsFile = fits.open('model-6.fits')
fitsFile.info()


img = fitsFile[0].data
img[np.isnan(img)] = 0

center = np.unravel_index(img.argmax(), img.shape)
center = (278,342)
print(center)

print(img.shape)

rad_profile = radial_profile(img, center)

fig, ax = plt.subplots()
plt.plot(rad_profile[0:500], 'b')

ax.xaxis.set_minor_locator(minorLocator)

plt.tick_params(which='both', width=2)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4, color='r')
plt.grid()
ax.set_ylabel("Y")
ax.set_xlabel("Pixels")
plt.grid(which="minor")
plt.show()
plt.savefig('model-6-plot.png')

fitsFile = fits.open('NGC5772_i.fits')
fitsFile.info()


img = fitsFile[0].data
img[np.isnan(img)] = 0

center = np.unravel_index(img.argmax(), img.shape)
center = (278,342)
print(center)

print(img.shape)

rad_profile = radial_profile(img, center)

fig, ax = plt.subplots()
plt.plot(rad_profile[0:500], 'b')

ax.xaxis.set_minor_locator(minorLocator)

plt.tick_params(which='both', width=2)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4, color='r')
plt.grid()
ax.set_ylabel("Y")
ax.set_xlabel("Pixels")
plt.grid(which="minor")
plt.show()
plt.savefig('NGC5772_i-plot.png')
