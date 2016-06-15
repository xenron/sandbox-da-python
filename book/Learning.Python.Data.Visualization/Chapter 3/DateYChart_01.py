# -*- coding: utf-8 -*-
import datetime
from time import sleep

start = datetime.datetime.now()
sleep(5) #delay the python script for 5 seconds.
stop = datetime.datetime.now()

elapsed = stop - start

if elapsed > datetime.timedelta(minutes=4):
    print "Slept for greater than 4 minutes"

if elapsed > datetime.timedelta(seconds=4):
    print "Slept for greater than 4 seconds"
