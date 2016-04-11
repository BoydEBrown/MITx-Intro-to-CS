# fibonacci's rabbits
#recursive fibonacci sequence

'''
def fib(x):
	# In this line, assert takes the following two boolean
	# sub-exspressions and checks to see if the statement as a
	# whole is true. If the statment is true, the body of the statement
	#(the if and else statements) will be evaluated. if false it will 
	#retun an error.
	assert type(x) == int and x >= 0
	if x == 0 or x == 1:
		return 1
	else:
		#sums x-1 and x-2, or the two prior x.
		return fib(x-1) + fib(x-2)

print fib(4)

'''
# This is a fibonacci using global variables to count the number of times
# the sequence is called.

def fibMetered(x):
	#The global key word means that the global variable numCalls if not 
	# evaluated within the fibMetered() enviroment. 
	global numCalls
	# Note numCalls is defined in fibTest(), not in fibMetered(). 
	numCalls += 1
	if x == 0 or x == 1:
		return 1
	else:
		return fibMetered(x-1) + fibMetered(x-2)
'''
def testFib(n):
	for i in range(n+1):
		global numCalls
		numCalls = 0
		print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
		print('fib called ' + str(numCalls) + ' times')

'''
#Just a test to see if 'global numCalls delcaration' needs to be in 
# side of the loop.
def testFib(n):
	global numCalls
	for i in range(n+1):
		numCalls = 0
		print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
		print('fib called ' + str(numCalls) + ' times')

print testFib(5)
