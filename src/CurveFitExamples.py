'''
Created on Jul 27, 2015

@author: aeames
'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.distributions import t 
#
#
"Example from http://www2.mpia-hd.mpg.de/~robitaille/PY4SCI_SS_2014/_static/15.%20Fitting%20models%20to%20data.html"
#
#
#
"Fake dataset with some random noise"
x = np.random.uniform(0., 100., 100)
y = 3. * x+2. + np.random.normal(0., 10., 100)
print plt.plot(x, y, '.')
#
#
#
def line(x, a, b):
    return a*x + b 
#
#
popt, pcov = curve_fit(line, x, y)
print popt 
print pcov
#
#
"fit the data assuming each point has a vertical error (standard deviation) of +/- 10:"
e = np.repeat(10., 100)
print plt.errorbar(x, y, yerr=e, fmt=None)
popt, pcov = curve_fit(line, x, y, sigma=e)
print popt
"Now pcov will contain the true variance and covariance of the parameters, so that the best-fit parameters are:"
print "a =", popt[0], "+/-", pcov[0,0]**0.5
print "b =", popt[1], "+/-", pcov[1,1]**0.5
"No plot the best fit line"
plt.errorbar(x, y, yerr=e, fmt=None)
xfine = np.linspace(0., 100., 100) #define values to plot the function for 
plt.plot(xfine, line(xfine, popt[0], popt[1]), 'r-')
#plt.show()
plt.savefig('Pictures/example.png')
#
#
# "Nonlinear example from http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/"
# #
# #
# "Nonlinear curve fit with confidence interval"
# x = np.array([0.5, 0.387, 0.24, 0.136, 0.04, 0.011])
# y = np.array([1.255, 1.25, 1.189, 1.124, 0.783, 0.402])
# #
# "This is the function we want to fit to our data"
# def func(x, a, b):
#     'non linear function in a and b to fit to data'
#     return a * x / (b + x)
# #
# initial_guess = [1.2, 0.03]
# pars, pcov = curve_fit(func, x, y, p0=initial_guess)
# #
# alpha = 0.05 #95% confidence interval = 100*(1-alpha)
# #
# #
# n = len(y)     # number of data points
# p = len(pars)  # number of parameters
# #
# #
# dof = max(0, n - p) #number of degrees of freedom
# #
# "Student-t value for the dof and confidence level"
# tval = t.ppf(1.0-alpha/2., dof)
# #
# for i, p, var in zip(range(n), pars, np.diag(pcov)):
#     sigma = var**0.5
#     print 'p{0}: {1} [{2} {3}]'.format(i, p, p-sigma*tval, p+sigma*tval)
# #
# plt.plot(x,y,'bo')
# xfit = np.linspace(0,1)
# yfit = func(xfit, pars[0], pars[1])
# plt.plot(xfit, yfit, 'b-')
# plt.legend(['data', 'fit'], loc='best')
#
#
# "Another nonlinear problem from http://www.walkingrandomly.com/?p=5215"
# #
# #
# xdata = np.array([-2, -1.64, -1.33, -0.7, 0, 0.45, 1.2, 1.64, 2.32, 2.9])
# ydata = np.array([0.699369, 0.700462, 0.695354, 1.03905, 1.97389, 2.41143, 1.91091, 0.919576, -0.730975, -1.42001])
# #
# def func(x, p1, p2):
#     return p1*np.cos(p2*x) + p2*np.sin(p1*x)
# #
# #
# popt, pcov = curve_fit(func, xdata, ydata, p0=(1.0, 0.2))
# print popt
# p1 = popt[0]
# p2 = popt[1]
# residuals = ydata-func(xdata, p1, p2) 
# fres = sum(residuals**2)
# print fres 

