#!/usr/bin/env python

import sys

for line in sys.stdin:
	try:
		line = line.strip()
		# split the line into words
		words = line.split()
		# increase counters	
		if words[0] == "WARC-Target-URI:" :
			uri = words[1].split("/")
			print '%s\t%s' % (uri[0]+"//"+uri[2], 1)
	except Exception:
		""
#hadoop jar /usr/local/apache/hadoop2/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file /mapper.py    -mapper /mapper.py -file /reducer.py   -reducer /reducer.py -input /text.txt -output /output
