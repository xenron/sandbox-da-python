# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:35:58 2016

@author: Administrator
"""
import re
from urllib2 import urlopen

#1
re1=u'^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]+'
re.findall(re1,'123@qq.com')

#2
re2=u'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
re.findall(re2,'http://www.dataguru.cn')

#3
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
content=re.findall("<img.*?>",html.read(),re.S) 
for content in content: 
    print content 


#4
re4=r'^[1-9]*[1-9][0-9]*$'
re.findall(re4,'1991')