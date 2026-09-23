import imageio.v3 as iio

filenames = ['Ajani1.png', 'Ajani2.png', 'Ajani3.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('ajani.gif', images, duration = 500, loop = 0)

