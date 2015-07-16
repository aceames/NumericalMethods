'''
Created on Jul 16, 2015

@author: aeames
'''
#
#
#
import numpy as np
#
#
def H(x,u):
    #
    m = x.shape[0]
    n = x.shape[1]
    #
    NewX    = np.zeros((m,n))
    #
    
    for i in range(n):
        new_Xcolumn_i = HouseholderReflection(Xcolumn_i, u)
    return NewX
#
#
#
def QR(X):
    return QRFactorization(X)
#
#
#
def HouseholderReflection(x, u):
    '''
    Inputs:
        - x, the (Mx1) vector being reflected about a hyperplane
        - u, a (Mx1) unit vector normal to the hyperplane
    Outputs:
        - Reflected_x,    x after reflection about the hyperplane
    '''
    #
#     try:
#         x.shape
#     except:
#         try:
#             x   = asarray(x)
#             u   = asarray(u)
#         except:
#             print "Either x or u is not an ndarray and is not convertible. Aborting!"
#             return
#     
#     try:
#         assert(x.shape == u.shape)
#     except:
#         print "Not the same size. Aborting!"
#         return
    rho = 2 / (x.dot(x))
    tau = rho * (u.transpose()).dot(x)
    Reflected_x = x - tau*u   
    #
    return Reflected_x
#
#
#
def QRFactorization(X):
    '''
    Inputs:
        - X, an (MxN) rectangular matrix
    Outputs:
        - Q, an (NxN) orthogonal matrix
        - R, an (MxN) upper triangular matrix such that X = QR
    '''
    #
    Q       = None
    R       = None
    #
    return (Q, R)
#
#
