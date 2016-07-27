import numpy
import matplotlib.pyplot
import sys
import scipy

if(len(sys.argv) != 2):
   print "Please input the number of iterations for the fractal"
   sys.exit()

ITERATIONS = int(sys.argv[1])
lena = scipy.misc.lena()
SIZE = lena.shape[0]
MAX_COLOR = 255.
x_min, x_max = -2.5, 1
y_min, y_max = -1, 1

# Initialize arrays
x, y = numpy.meshgrid(numpy.linspace(x_min, x_max, SIZE),
                   numpy.linspace(y_min, y_max, SIZE))
c = x + 1j * y
z = c.copy()
fractal = numpy.zeros(z.shape, dtype=numpy.uint8) + MAX_COLOR

# Generate fractal
for n in range(ITERATIONS):
    print n
    mask = numpy.abs(z) <= 4 
    z[mask] = z[mask] ** 2 +  c[mask]
    fractal[(fractal == MAX_COLOR) & (-mask)] = (MAX_COLOR - 1) * n / ITERATIONS

# Display the fractal
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.imshow(fractal)
matplotlib.pyplot.title('Mandelbrot')
matplotlib.pyplot.axis('off')

# Combine with lena
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.imshow(numpy.choose(fractal < lena, [fractal, lena]))
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title('Mandelbrot + Lena')

matplotlib.pyplot.show()
