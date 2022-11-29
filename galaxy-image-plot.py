from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib import colors
import math

image_file = 'NGC5772_i.fits'

image_data = fits.getdata(image_file, ext=0)
image_data[image_data < 1] = 1

max_val = None
x_count = 0
y_count = 0
x_ticks = []

zcal = -23.720301
pix_to_arcsec = 0.369
mag_pixels = 5 * math.log(pix_to_arcsec)
gain = 4.86
print('mp:' + str(mag_pixels))
for row in image_data:
    for val in row:
        mag = zcal - (2.5 * math.log(val)) + mag_pixels
        image_data[y_count][x_count] = mag
        if max_val == None or mag > max_val:
            print(str(mag) + ' (' + str(x_count) + ',' + str(y_count))
            max_val = mag
        x_count += 1
    y_count += 1
    x_count = 0

print(image_data.shape)

plt.figure()
plt.imshow(image_data, cmap='gray_r',origin='lower')
ax = plt.gca()
x_ticks = ax.get_xticks()
d = 30 / 0.396
cx = 342
new_x_ticks = [cx]
for i in range(5):
    tick_x = ((i + 1) * d) + cx
    if (tick_x < image_data.shape[1]):
        new_x_ticks.append(tick_x)
    tick_x = cx - ((i + 1) * d)
    if (tick_x > 0):
        new_x_ticks.insert(0,tick_x)
ax.set_xticks(new_x_ticks)

new_x_ticks = []
x_ticks = ax.get_xticks()
for tick in x_ticks:
    tick_label = round((tick - cx) * 0.396)
    new_x_ticks.append(tick_label)

ax.set_xticklabels(new_x_ticks)

cy = 278
new_y_ticks = [cy]
for i in range(5):
    tick_y = ((i + 1) * d) + cy
    if (tick_y < image_data.shape[0]):
        new_y_ticks.append(tick_y)
    tick_y = cy - ((i + 1) * d)
    if (tick_y > 0):
        new_y_ticks.insert(0,tick_y)
ax.set_yticks(new_y_ticks)

new_y_ticks = []
y_ticks = ax.get_yticks()
for tick in y_ticks:
    tick_label = round((tick - cy) * 0.396)
    new_y_ticks.append(tick_label)

ax.set_yticklabels(new_y_ticks)

plt.xlabel("Radius (arcsec)")
plt.ylabel("Radius (arcsec)")

plt.colorbar(label="μ (mag/arcsec²)")
plt.savefig('galaxy-image-plot.png')
plt.show()
