'''
Created on Jul 27, 2015

@author: aeames
'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
#
#
"Fake dataset with some random noise"
x = np.random.uniform(0., 100., 100)
y = 3. * x+2. + np.random.normal(0., 10., 100)
plt.plot(x, y, '.')