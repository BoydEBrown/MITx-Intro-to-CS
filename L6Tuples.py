#Manipulating tuples

#Iterating over a tuple

# This function finds and retuns tuples containing
# common divisors of n1 and n2, assuming both are 
# positive ints.


def findDivisors(n1, n2):
	#Creates the empty tuple
	divisors = () 
	#For loop looks at the ints between 1 and lower value of 
	# n1 + n2. 
	for i in range(1, min(n1,n2) +1):
		#If the above ints are devisors of n1 and n2...
		if n1%i == 0 and n2%i == 0:
			#...Add that int to the divisors tuple as a 
			#singelton.
			divisors = divisors + (i,)
	return divisors

print findDivisors(63, 21)

'''
divs = findDivisors(63,21)
total = 0
for d in divs:
	total += divs
print(total)
'''