# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:08:08 2016

@author: Administrator
"""

# coding:utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import random


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                        href=re.compile("^(/wiki/)((?!:).)*$"))
                        
links = getLinks('/wiki/Statistics')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

