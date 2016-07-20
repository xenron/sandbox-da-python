import threading
import time
class demoThread (threading.Thread):
	def __init__(self, threadID, name, ctr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ctr = ctr
	def run(self):
		print "Start of The Thread: " + self.name
		print_time(self.name, self.ctr, 8)
		print "Thread about to Exit:" + self.name

def print_time(threadName, delay, counter):
		while counter:
			time.sleep(delay)
			print "%s: %s" % (threadName, time.ctime(time.time()))
			counter -= 1

thrd1 = demoThread(1, "FirstThread", 4)
thrd2 = demoThread(2, "SecondThread", 5)

thrd1.start()
thrd2.start()

print "Main Thread exits"