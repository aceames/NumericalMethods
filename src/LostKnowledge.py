'''
Created on Jul 16, 2015

@author: aeames
'''
#
#
#
from numpy import asarray
#
#
#
a   = asarray([[1, 2, 3]])
#
#
#
print type(a)
print a.dot(a.transpose())
