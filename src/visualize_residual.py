'''
Created on Jul 28, 2015

@author: aeames
'''
import matplotlib.pyplot as plt
from numpy import linspace, exp, zeros, log10
from H2S_Solubility_Model import Residual
#
#
#
num_pts = 10000
args    = (8.4175e-10, 1.95604912e-14, 1.42888090e-7, 4.62657821e-14, 10334.01626172, 0.0023788868995999997, 6.1822332128590451)
x_exp   = linspace (-12, 0, num_pts)
x       = 10.**(x_exp)
y       = zeros((num_pts))
#
for i in range(num_pts):
    y[i]    = Residual(x[i], args[0], args[1], args[2], args[3], args[4], args[5], args[6])
#
print max(y)
plt.plot(x_exp,log10(y))
plt.show()