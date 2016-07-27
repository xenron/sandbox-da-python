#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

try:
	#Open the file via HTTP.
	response = urllib2.urlopen('http://www.packtpub.com/rss.xml') 
	#Read the file to a variable we named 'xml'
	xml = response.read() 
	#print to the console.
	print(xml) 
	#Finally, close our open network.
	response.close() 

except:
	#If we have an issue show a message and alert the user.
	print('Unable to connect to RSS...') 