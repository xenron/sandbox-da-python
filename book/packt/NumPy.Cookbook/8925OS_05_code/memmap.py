import numpy
import matplotlib.pyplot
import sys

N = 512

if(len(sys.argv) != 2):
   print "Please input the number of squares to generate"
   sys.exit()

NSQUARES = int(sys.argv[1]) 

# Initialize
img = numpy.zeros((N, N), numpy.uint8)
centers = numpy.random.random_integers(0, N, size=(NSQUARES, 2))
radii = numpy.random.randint(0, N/9, size=NSQUARES)
colors = numpy.random.randint(100, 255, size=NSQUARES)

# Generate squares
for i in xrange(NSQUARES):
   xindices = range(centers[i][0] - radii[i], centers[i][0] + radii[i])
   xindices = numpy.clip(xindices, 0, N - 1)
   yindices = range(centers[i][1] - radii[i], centers[i][1] + radii[i])
   yindices = numpy.clip(yindices, 0, N - 1)

   if len(xindices) == 0 or len(yindices) == 0:
      continue

   coordinates = numpy.meshgrid(xindices, yindices)
   img[coordinates] = colors[i]

# Load into memory map
img.tofile('random_squares.raw')
img_memmap = numpy.memmap('random_squares.raw', shape=img.shape)

# Display image
matplotlib.pyplot.imshow(img_memmap)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.show()
