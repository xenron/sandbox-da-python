#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import urllib2, time
from xml.etree import ElementTree 

try: 
   #Open the file via HTTP. 
   response = urllib2.urlopen('http://www.packtpub.com/rss.xml') 
   tree = ElementTree.parse(response) 
   root = tree.getroot() 
    
   #Array of post dates.
   news_post_date = root.findall("channel//pubDate") 
    
   #Iterate in all our searched elements and print the inner text for each. 
   for date in news_post_date: 
       #Create a variable striping out commas, and generating a new array item for every space.
       datestr_array = date.text.replace(',', '').split(' ')

	   #Create a formatted string to match up with our strptime method.
       formatted_date = "{0} {1}, {2}, {3}".format(datestr_array[2], datestr_array[1], datestr_array[3], datestr_array[4])

	   #Parse a time object from our string.
       blog_datetime = time.strptime(formatted_date, "%b %d, %Y, %H:%M:%S")
       print blog_datetime
        
   #Finally, close our open network. 
   response.close() 
    
except Exception as e: 
   #If we have an issue show a message and alert the user. 
   print(e)