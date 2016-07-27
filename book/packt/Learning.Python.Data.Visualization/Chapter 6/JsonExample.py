# -*- coding: utf-8 -*-

import urllib2
import json

try:
    #Set a URL variable.
    url = 'https://www.googleapis.com/books/v1/volumes/s1gVAAAAYAAJ'
    #Open the file via HTTP.
    response = urllib2.urlopen(url) 

    #Read the request as one string.
    bookdata = response.read()

    #Convert the string to a JSON object in Python.
    data = json.loads(bookdata)

    for r in data ['volumeInfo']:
        print r

    #Close our response.
    response.close()

except:
	#If we have an issue show a message and alert the user.
	print('Unable to connect to JSON API...')