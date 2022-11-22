from mpdaf.obj import moffat_image
from astropy import units as u

image = moffat_image(shape=(51,51), wcs=None, factor=1, moffat=None, center=None, flux=1.0, fwhm=(0.609840,0.609840), peak=False, n=2, rot=0.0, cont=0, unit_fwhm=u.pix)
image.write('moffat.fits')
