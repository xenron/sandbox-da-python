#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from xml.etree import ElementTree

try:
    #Open the file via HTTP.
    response = urllib2.urlopen('http://www.packtpub.com/rss.xml')

    tree = ElementTree.parse(response)
    root = tree.getroot()

    #Create an 'Element' group from our XPATH using findall.
    news_post_title = root.findall("channel//title")

    #Iterate in all our searched elements and print the inner text for each.
    for title in news_post_title:
        print title.text

    #Finally, close our open network.
    response.close()
except Exception as e:
    #If we have an issue show a message and alert the user.
    print(e)