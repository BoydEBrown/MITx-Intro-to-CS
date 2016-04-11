'''
Iterative and recursion functions to compute n!.
'''

#iterative
def factI(n):
	result = 1
	while n > 1:
		result = result * n
		n -=1
	return result

print factI(6)

#recursion
def factR(n):
	#this is the base case.
	if n == 1:
		return n
	# this is the recursive step... n(n-1)...n(n-1)(n-2).
	return n*factR(n-1)

print factR(6)
