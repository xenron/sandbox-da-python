# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:57:55 2016

@author: Administrator
"""

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import requests
from urllib import urlopen


url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urlopen(url)
raw = response.read()
type(raw)
len(raw)
raw[:75]

####################################################################
####################################################################
####################################################################
