'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
from Functions import H
x = np.array([1, 2, 3], float)
u = np.array([1, 2, 3], float)
H(x, u)
print H(x, u)