'''Given a radio active decay curve for Co,
calculate the radioactive exsposure of a person 
over time'''

import numpy as np
import math

#This is our line. It represents the rate od decay.
def f(x):
    return 10*math.e**(math.log(0.5)/5.27 * x)

   
def radiationExposure(start, stop, step):
	L = np.arange(start, stop+1, step)
	for i in L:
		return sum(f(L)*step)



print radiationExposure(40,100,1.5)