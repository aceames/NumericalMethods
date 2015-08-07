'''
Created on Jul 28, 2015

@author: aeames
'''
import numpy as np
from scipy.optimize import curve_fit, brenth, fsolve
import matplotlib.pyplot as plt
#
#
#
"Brenth example y=f(x)=x**-1*exp(yx)"
x = np.random.uniform(0., 10., 10)
y = np.random.uniform(0., 10., 10)
#
x_range = len(x)
#
def f(y, x):
    return y*x - np.exp(y*x) + 3.
#
z = f(y, x)
#
#
#
#
def minimize_residual(y, x):
    y_list = []
    x = np.asarray(x)
    for i in range(x_range):
        a           = 0
        b           = 10
        y_new       = brenth(f, a, b, args=x[i])
        y_list      = y_list + [y_new]
    return np.asarray(y_list)
# 
#
# "Multivariate example of curve_fit, ax+by+epsilon, now combined with above"
#
y_prime             = minimize_residual(y, x)
#
XCOMBINED           = np.zeros((2, 10))
XCOMBINED[0, :]     = x
XCOMBINED[1, :]     = y 
#
z                   = 3. * x + 3. * y_prime + np.random.normal(0., 1., 10)
#
def function(Input_Array, a, b):
    return a*Input_Array[0] + b*Input_Array[1]
#
#
vopt, vcov = curve_fit(function, XCOMBINED, z)
print vopt
print vcov 
