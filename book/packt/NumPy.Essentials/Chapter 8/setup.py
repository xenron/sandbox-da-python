# Author: Tanmay Dutta
# Copyright: Packt Publishing
# To be distributed with the book
# The setup builds the extension for dynamic black scholes monte carlo code

from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy.distutils.misc_util

include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs()


setup(

    name="numpy_first",
    version="0.1",
    ext_modules=[Extension('dynamic_BS_MC',
                           ['dynamic_BS_MC.pyx'],
                           include_dirs = include_dirs)],
    cmdclass={'build_ext': build_ext}
)

