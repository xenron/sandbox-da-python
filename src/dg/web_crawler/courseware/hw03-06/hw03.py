# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:36:29 2016

@author: Administrator
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen

#1
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
r=html.read()

soup=BeautifulSoup(r,'lxml')
for s in soup.find_all(class_="red"):
    print(s.string)


#2
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
r=html.read()

soup=BeautifulSoup(r,'lxml')
for s in soup.find_all('tr',class_="gift"):
    message=s.find_all('td')
    print(message[0].string,message[2].string)

print("Dead Parrot's price is "+soup.find(text=u'\nDead Parrot\n').parent.next_sibling.next_sibling.string)
