'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
from H2S_Solubility_Model import f 
from DGA_DATA import *
from scipy.optimize import curve_fit
#
X_input         = np.zeros((3, 35))
X_input[0, :]   = P
X_input[1, :]   = T_F
X_input[2, :]   = A_w
Y_input         = np.asarray(Loading)
#
k_1_guess       = 1.e-9
#
popt, pcov = curve_fit(f, X_input, Y_input, p0=k_1_guess)

print popt
print pcov

