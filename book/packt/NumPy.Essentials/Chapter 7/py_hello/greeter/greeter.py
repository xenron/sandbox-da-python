# !/usr/bin/env python
"""
Created for packt publishing. 
author: Tanmay
"""

import os


def greet():
    print "Hi {}, you are awesome".format(os.environ.get( "USERNAME" ))
