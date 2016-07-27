import datetime 
import time

# the user defined function that retruns 5 digit random number
def	next_5digit_int():
	# this will introduce randomness at the microsecond level
	time.sleep(0.123)						
current_time = datetime.datetime.now().time() 
	random_no = int(current_time.strftime('%S%f'))
	# this will trim last three zeros
	return random_no/1000					

# to demonstrate generation of ten random numbers
for x in range(0, 10):
	i = next_5digit_int()
	print i
