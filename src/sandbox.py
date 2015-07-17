'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
from Functions import H, QR, HouseholderReflection, vector_u, matrix_H_u
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
C = np.matrix([[1, -1, 4], [1, 4, -2], [1, 4, 2], [1, -1, 0]])

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
print "\nQ*Q^T\n=========================================="
print Q*Q.T


# x = np.matrix([[1.0], [-2.0], [np.sqrt(11.0)]])
# #u = np.matrix([[0], [0], [1]])
# a = vector_u(x, 1)
# print a 
# print HouseholderReflection(x, a)
# print matrix_H_u(a)
