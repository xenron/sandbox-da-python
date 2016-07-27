# Author : Tanmay Dutta
# Demo setup to show how to write the setup for extension using numpy c api
from distutils.core import setup, Extension
import numpy
# define the extension module
demo_module = Extension('numpy_api_demo', sources=['numpy_api.c'],
                        include_dirs=[numpy.get_include()])  

# run the setup
setup(ext_modules=[demo_module])
