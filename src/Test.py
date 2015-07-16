'''
Created on Jul 16, 2015

@author: aeames
'''
#
#
#
def H(x,u):
    return HouseholderReflection(x, u)
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
        - x, the vector being reflected about a hyperplane
        - u, a unit vector normal to the hyperplane
    Outputs:
        - Reflected_x,    x after reflection about the hyperplane
    '''
    #
    Reflected_x = None
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