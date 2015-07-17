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
def H(X,u):
    #
    m = X.shape[0]
    n = X.shape[1]
    #
    NewX    = np.asmatrix(np.zeros((m,n)))
    #
    
    for i in range(n):
        NewX[:, i]   = np.asmatrix(HouseholderReflection(X[:,i], u))
    return NewX
#
#
#
def QR(X):
    return QRFactorization(X)
#
#
#
def vector_u(x, k):
    m   = x.shape[0]
    sigma = float(-1*np.sign(x[k])*np.sqrt((x.transpose()).dot(x)))
    e_k = np.asmatrix(np.zeros((m, 1)))
    e_k[k, 0] = 1.0 
    u = np.asmatrix(x + sigma * e_k) 
    return u 
    
def matrix_H_u(u):
    """ get the householder reflection matrix H = I - puu_t """
    n = u.shape[1]
    I   = np.asmatrix(np.identity(n))
    u_t = np.asmatrix(u.transpose())
    rho = 2 / float(u.transpose().dot(u))
    H_u = np.asmatrix(I - rho * u.dot(u_t))
    return H_u 
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
    u_t = np.asmatrix(u.transpose())
    rho = 2 / float(u_t.dot(u))
    tau = float(rho * (u_t.dot(x)))
    Reflected_x = np.asmatrix(x - tau*u)   
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
    m       = X.shape[0]
    n       = X.shape[1]
    assert(m >= n)
    #
    u       = vector_u(X[:, 0], 0)
    Q_t     = matrix_H_u(u) # STARTS AS H1
    R       = H(X,u)
    #now loop through the rest of the columns of X and apply Hn...H2 to H1 to get Qt and R
    for i in range(1, (n-1)):
        #
        u           = vector_u(R[i:,i], 0) 
        #
        R[i:,i:]    = H(R[i:,i:],   u)
        Q_t[i:,i:]  = H(Q_t[i:,i:], u)
    #
    Q   = Q_t.transpose()
    #
    return (Q, R)
#
#
