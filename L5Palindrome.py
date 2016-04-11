# Is it a palindrome?

# isPalindrome() is defined as a procedure, with two sub procedures
# toChars() and isPal().
def isPalindrome(s):
	#This function changes the string to lowercase
	# and strips spaces.  
	def toChars(s):
		#First the string is reassigned to lower case by
		# calling the .lower() method on s.
		s = s lower()
		#Then new string 'ans' is created.
		ans = ''
		#The for loop takes each charater in s and compaires
		#the charater to a string of alpha charaters, and if the 
		#the chars are in alpha char string add to string 'ans'.
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + c
		return ans
	# This function checks the base case and intruduces the recursion 
	# to check the first and last charaters of the string.
	def isPal(s):
		#This is the base case, if 0 or 1 return True.
		if len(s) <= 1:
			return True
		#Else, take the first position last position, if they are the same,
		# pull out the sub string starting at 1 position and ending just
		# before last position, check each first and last pair of substring 
		#for remainder of string through recursive of isPal function.
		else:
			return s[0]==s[-1] and isPals(s[1:-1])
	#Here isPalindrome uses toChar to convert the string, then calls isPal()
	# on that string, and uses the answer computed by that to answer the 
	# overall solution.
	return isPal(toChars(s))

