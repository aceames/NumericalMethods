'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
from H2S_Solubility_Model import f , ln_k_1_function, inputs
from DGA_DATA import *
from scipy.optimize import curve_fit
#
X_input         = np.zeros((3, 75))
X_input[0, :]   = P
X_input[1, :]   = T_F
X_input[2, :]   = A_w
Y_input         = np.asarray(Loading)
#
A_guess = -2.
b_guess = -5.5e3
B_M_guess = 1.

Initial_guess = [A_guess, b_guess, B_M_guess]
#
popt, pcov = curve_fit(f, X_input, Y_input, p0=Initial_guess)     
print popt
print pcov

print Y_input
print "---------------"
print f(X_input, popt[0], popt[1], popt[2])

#
# def ln_k_1_function(T, A, B, C, D, E, num_params):
#     # parameters A, B, C, D, E of k_1 function
#     if num_params == 2:
#         C = 0
#         D = 0
#         E = 0
#     elif num_params == 3:
#         D = 0
#         E = 0
#     elif num_params == 4:
#         E = 0
#     return A + B*(T**-1)+C*(T**-2)+D*(T**-3)+E*(T**-4)
        