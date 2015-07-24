'''
Created on Jul 17, 2015

@author: aeames
'''
from nose.tools import *
import numpy as np
from Functions import HouseholderReflection, QRFactorization
#
def test_HouseholderReflection():
    x = np.matrix([[1], [2], [3]])
    u = np.matrix([[0], [0], [1]])
    x_prime = np.matrix([[1], [2], [-3]])
    m = x.shape[0]
    m_prime = x_prime.shape[0]
    assert_equal(m, m_prime)
    H_x = HouseholderReflection(x, u)
    for i in range(m):
        assert_equal(x_prime[i, 0], H_x[i, 0])
    
def test_QRfactorization():
    A = np.matrix([[12, -51, 4], 
                   [6, 167, -68], 
                   [-4, 24, -41]])
    u_1 = np.matrix([[-2], [6], [-4]])
    u_2 = np.matrix([[126],[168]])
    Q_t_1 = np.matrix([[(6/7), (3/7), (-2/7)], 
                       [(3/7), (-2/7), (6/7)], 
                       [(-2/7), (6/7), (3/7)]])
    R_1 = np.matrix([[14, 21, -14], [0, -49, -14], [0, 168, -77]])
    Q_t_2 = np.matrix([[0.857142857, 0.428571429, -0.285714286], 
                       [0.394285714, -0.902857143, -0.171428571], 
                       [-0.331428571, 0.034285714, -0.942857143]])
    R = np.matrix([[14, 21, -14], [0, -175, 70], [0, 0, 35]])
    Q = Q_t_2.transpose()
    m = A.shape[0]
    n = A.shape[1]
    R_m= R.shape[0]
    R_n = R.shape[1]
    Q_m = Q.shape[0]
    Q_n=Q.shape[1]
    assert_equal(m, R_m)
    assert_equal(n, R_n)
    assert_equal(m, Q_m)
    assert_equal(m, Q_n)
    QR_A = QRFactorization(A)
    Q_A = QR_A[0]
    R_A = QR_A[1]
    Product = Q_A.dot(R_A)
    I   = np.asmatrix(np.identity(m))
    QQ_t = Q_A.dot(Q_A.transpose())
    for i in range(m):
        for j in range(n):
            assert_almost_equals(Q_A[i, j], Q[i, j], places=9)
            assert_almost_equals(R_A[i, j], R[i, j], places=9)
            assert_almost_equals(I[i, j], QQ_t[i, j], places=10)
            assert_almost_equals(A[i, j], Product[i, j], places=4)
        