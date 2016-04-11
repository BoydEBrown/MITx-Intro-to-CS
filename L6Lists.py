# Operations on lists
# 
#Iteration

#Cloning
#note: avoid mutating a list over which one is iterating.
#The following is bad code!! see above.
'''
def removeDupes(L1,L2):
	for e1 in L1:
		if e1 in L2:
			L1.remove(e1)

L1 = ['a','b','c','d','e','f','g']
L2 = ['d','e','f','g','h','i','j']
removeDupes(L1, L2)
print L1
'''
#The following iterates over a clone of L1, this prevents
# the error caused by mutation in the above code.

def removeDupes(L1,L2):
	#This line creates a clone of L1 called L1Start.
	L1Start = L1[:]
	#Note that the loop iterates over L1Start..
	for e1 in L1Start:
		if e1 in L2:
			#... but makes mutations to L1.
			L1.remove(e1)
L1 = ['a','b','c','d','e','f','g']
L2 = ['d','e','f','g','h','i','j']
removeDupes(L1, L2)
print L1