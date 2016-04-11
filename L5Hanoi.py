#towers of hanoi recursion code

def printmove(fr, to):
	#this line prints the instruction
	print('move from ' +str(fr) + ' to ' +str(to))

def towers(n, fr, to, spare):
	# base case "move from the 'from' place to the 'to' place"
	if n == 1 :
		printmove(fr, to)
	else:
		# otherwise move smaller stack to spare space, 
		#from the space I started to.
		towers(n-1, fr, spare, to)
		# then move whats left (stack of size 1) to target location.
		towers(1, fr, to, spare)
		#move smaller stack above from spare to target location.
		towers(n-1, fr, spare, to, fr)
'''
To summerize, to move a stack of size n, move a stack of n-1 to the
spare location. Then move the bottom (remaining) disk to target location.
'''