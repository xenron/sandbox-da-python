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
		threadLock.acquire()
		print_time(self.name, self.ctr, 8)
		print "Thread about to Exit:" + self.name
		threadLock.release()

def print_time(threadName, delay, counter):
		while counter:
			time.sleep(delay)
			print "%s: %s" % (threadName, time.ctime(time.time()))
			counter -= 1

threadLock = threading.Lock()
thrds = []

thrd1 = demoThread(1, "FirstThread", 4)
thrd2 = demoThread(2, "SecondThread", 5)

thrd1.start()
thrd2.start()

thrds.append(thrd1)
thrds.append(thrd2)

for thrd in threads:
	thrd.join()

print "Main Thread Exits"