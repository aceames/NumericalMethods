'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
from Functions import H, QR
# A = np.matrix([[1.0, 2.0, 0.0], [0.0, 1.0, 1.0], [1.0, 0.0, 1.0]])
# print A
# QR(A)
# print QR(A)
# #
# #
# #
# B = np.matrix([[3.0, -6.0], [4.0, -8.0], [0.0, 1.0]])
# print B 
# QR(B)
# print QR(B)
#
#
#
C = np.matrix([[1, 1, 1], [1, 2, 3], [1, 3, 6]])
print "\nC\n=========================================="
print C 
Q, R    = QR(C)
#
#
#

print "\nQ\n=========================================="
print Q
print "\nR\n=========================================="
print R
print "\nQ*R\n=========================================="
print Q*R
