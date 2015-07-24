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
    A = np.matrix([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    u_1 = np.matrix([[-2], [6], [-4]])
    u_2 = np.matrix([[126],[168]])
    Q_t_1 = np.matrix([[(6/7), (3/7), (-2/7)], [(3/7), (-2/7), (6/7)], [(-2/7), (6/7), (3/7)]])
    R_1 = np.matrix([[14, 21, -14], [0, -49, -14], [0, 168, -77]])
    Q_t_2 = np.matrix([[(6/7), (3/7), (-2/7)], [(69/175), (-158/175), (-6/35)], [(-58/175), (6/175), (-33/35)]])
    R = np.matrix([[14, 21, -14], [0, -175, 70], [0, 0, 35]])
    Q = Q_t_2.transpose()
    assert_equal(A.QRFactorization, Q, R)