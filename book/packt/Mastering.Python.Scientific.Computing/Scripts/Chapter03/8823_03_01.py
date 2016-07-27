import random


print random.random()   			# Output 0.532115164018

print random.uniform(1,9) 		# Output 4.14478788005

print random.randrange(20)    	# Output 19

print random.randrange(0, 99, 3) # Output 93

print random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # Output 'P'

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(items)
print items					# Output [6, 4, 7, 10, 2, 9, 1, 3, 8, 5]

print random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  5)   # Output [10, 1, 3, 4, 2]

weighted_choices = [('Three', 3), ('Two', 2), ('One', 1), ('Four', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
print random.choice(population) # Output 'Two'
