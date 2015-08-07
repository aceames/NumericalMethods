'''
Created on Jul 28, 2015

@author: aeames
'''
import numpy as np
from LegacyCode.Example import minimize_residual, f
q = np.random.uniform(0., 10., 10)
p = np.random.uniform(0., 10., 10)
y_new = minimize_residual(p, q)
print y_new
print f(y_new, q)
#
#

