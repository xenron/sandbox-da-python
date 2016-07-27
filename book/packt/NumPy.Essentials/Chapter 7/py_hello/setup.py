# !/usr/bin/env python
"""
Created for packt publishing. 
author: Tanmay
"""

from setuptools import setup
import os
description = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()
setup(
    name = "py_hello",
    packages = ["greeter"],
    scripts = ["bin/greeter.bat"],
    include_package_data = True,
    package_data = {
        "py_hello":[]
        },
    version = "0.1.0",
    description = "Simple Application",
    author = "packt",
    author_email = "packt@packt.com",
    url = "https://bitbucket.org/tdatta/book/py_hello",
    download_url = "https://bitbucket.org/tdatta/book/py_hello/zipball/master",
    keywords = ["tanmay", "example_seutp", "packt"  "app"],
    install_requires=[
        "setuptools", 
        "python-dateutil >= 2"],
    license='LICENSE',
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: release 0.1",
        "Intended Audience :: seutp newbies",
        "License :: Public",
        "Operating System :: POSIX :: Linux",
        "Topic :: Demo",
        ],
    long_description = description
    )
 
