'''
Created on Jul 28, 2015

@author: aeames
'''
import numpy as np
from scipy.optimize import curve_fit, brenth, fsolve
import matplotlib.pyplot as plt
#
# "Multivariate example of curve_fit, ax+by+epsilon"
# #
# x                   = np.random.uniform(0., 100., 100)
# y                   = np.random.uniform(0., 100., 100)
# #
# XCOMBINED           = np.zeros((2, 100))
# XCOMBINED[0, :]     = x
# XCOMBINED[1, :]     = y 
# #
# z = 3. * x + 3. * y + np.random.normal(0., 1., 100)
# #
# def function(Input_Array, a, b):
#     return a*Input_Array[0] + b*Input_Array[1]
# #
# #
# vopt, vcov = curve_fit(function, XCOMBINED, z)
# print vopt
# print vcov
#
#
"Brenth example y=f(x)=x**-1*exp(yx)"
x = np.random.uniform(0., 10., 10)
y = np.random.uniform(0., 10., 10)
#
x_range = len(x)
# def f(y):
#     for i in range(x_range):
#         z = y*x[i] - np.exp(y*x[i])
#     return z
#
def f(y, x):
    return y*x - np.exp(y*x) + 3.
#
z = f(y, x)
#
# plt.loglog(z)
# plt.show()
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

# a           = 0
# b           = 100
# fa          = f(a, x)
# fb          = f(b, x)
# real_y      = brenth(f, a, b, args=x)
# print real_y
# print f(real_y, x)